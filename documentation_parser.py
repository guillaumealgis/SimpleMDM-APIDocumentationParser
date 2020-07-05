#!/usr/bin/env python3

from functools import reduce
from pprint import pprint
import datetime
import json
import os
import pathlib
import re
import sys

from bs4 import BeautifulSoup
import requests

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

OUTPUT_DIRECTORY = os.path.join(SCRIPT_PATH, "Versions")

CACHE_DIRECTORY = os.path.join(SCRIPT_PATH, "cache")
CACHE_FILENAME = "Documentation.html"
CACHE_FILEPATH = os.path.join(CACHE_DIRECTORY, CACHE_FILENAME)

MAX_CACHE_DURATION = datetime.timedelta(days=1)

HTTP_VERBS = ("GET", "POST", "PATCH", "PUT", "DELETE")


class IncompleteAPIRequest(ValueError):
    pass


class APIRequest:
    def __init__(self, title):
        # The list() ensure we're copying the title and not retaining a
        # reference.
        self.title = list(title)
        self.http_verb = None
        self.endpoint = None
        self.parameters = {}
        self.response = None

    @property
    def is_empty(self):
        return (
            not self.http_verb
            and not self.endpoint
            and not self.parameters
            and not self.response
        )

    def validate(self):
        try:
            if not self.title:
                raise IncompleteAPIRequest("Invalid title")
            if self.http_verb in HTTP_VERBS and not self.endpoint:
                raise IncompleteAPIRequest("Invalid endpoint")
            if self.endpoint and self.http_verb not in HTTP_VERBS:
                raise IncompleteAPIRequest("Invalid HTTP verb")
        except IncompleteAPIRequest:
            pprint(vars(self), stream=sys.stderr)
            raise

    def as_markdown(self):
        title = " / ".join(self.title)
        s = f"# {title}\n"

        if self.http_verb:
            s += "\n```http\n"
            s += f"{self.http_verb} {self.endpoint}\n"
            s += "```\n"

        if self.parameters:
            arg_width = reduce(max, [len(x) for x in self.parameters.keys()]) + 2
            desc_width = reduce(max, [len(x) for x in self.parameters.values()])
            s += "\n"
            s += f"| {'Argument'.ljust(arg_width)} | {'Description'.ljust(desc_width)} |\n"
            s += f"|{'-'.ljust(arg_width + 2, '-')}|{'-'.ljust(desc_width + 2, '-')}|\n"
            for arg, desc in self.parameters.items():
                arg = f"`{arg}`"
                s += f"| {arg.ljust(arg_width)} | {desc.ljust(desc_width)} |\n"
            s += "\n"

        if self.response:
            s += f"\n{self.response.as_markdown()}\n"

        s += "\n"

        return s


class CodeSnippet:
    def __init__(self, code, language=None):
        self.code = code
        self.language = language
        self._reparse_snippet()

    def _reparse_snippet(self):
        if not self.code.strip().startswith("curl"):
            return

        # Strip the curl request from the snippet
        lines = self.code.splitlines()
        new_snippet = ""
        found_end_of_curl = False
        for line in lines:
            if not line.strip():
                found_end_of_curl = True
            elif not found_end_of_curl:
                continue
            else:
                new_snippet += f"{line}\n"

        new_snippet = new_snippet.strip()
        if not new_snippet:
            self.response = None
        elif new_snippet.startswith("HTTP"):
            self._reparse_snippet_as_HTTP_response(new_snippet)
        else:
            self._reparse_snippet_as_JSON_response(new_snippet)

    def _reparse_snippet_as_HTTP_response(self, snippet):
        self.language = "http"
        self.code = snippet

    def _reparse_snippet_as_JSON_response(self, snippet):
        # Try to make the response parsable...
        ellipsis_token = '"__API_DOC_PARSER__ELLIPSIS__"'
        snippet = snippet.replace("...", ellipsis_token)
        snippet = snippet.replace("=>", ":")
        snippet = re.sub(r'([^\w"])nil([^\w"])', r"\1null\2", snippet)

        json_data = json.loads(snippet)
        self.language = "json"
        formatted_json = json.dumps(json_data, indent=2, sort_keys=True)
        formatted_json = formatted_json.replace(ellipsis_token, "...")
        self.code = formatted_json

    def as_markdown(self):
        return f"```{self.language}\n{self.code}\n```"


class DocParser:
    def __init__(self, doc_path):
        with open(doc_path, "r") as fp:
            self.soup = BeautifulSoup(fp, "html.parser")

        self.api_requests = []
        self.current_title_hierarchy = []
        self.current_api_request = None

    def _current_title(self, level):
        try:
            return self.current_title_hierarchy[level - 1]
        except IndexError:
            return None

    @property
    def _current_h1(self):
        return self._current_title(1)

    @property
    def current_h2(self):
        return self._current_title(2)

    @property
    def current_h3(self):
        return self._current_title(3)

    def parse_version(self):
        version_tag = self.soup.find_all(class_="version")

        if len(version_tag) > 1:
            raise ValueError("Found multiple tags with class 'version'")

        full_version_text = version_tag[0].get_text()

        matches = re.fullmatch(r".*?(\d+\.\d+(\.\d+)?)", full_version_text)
        version = matches.group(1)

        return version

    def parse_content(self):
        content = self.soup.find("div", class_="content")

        self._parse_children(content)

        return self.api_requests

    def _parse_children(self, node):
        for child in node.children:
            if not child.name:
                continue

            if re.fullmatch(r"h\d+", child.name, re.I):
                level = self._parse_title(child)

                # h2 tags starts a API request section
                if level == 2:
                    self._begin_parsing_new_api_request()

            elif child.name == "table":
                self._parse_parameters(child)

            elif child.name == "pre" or child.name == "code":
                self._parse_code_block(child)

            elif child.name == "p":
                self._parse_children(child)

    def _begin_parsing_new_api_request(self):
        if self.current_api_request and not self.current_api_request.is_empty:
            self.current_api_request.validate()
            self.api_requests.append(self.current_api_request)

        self.current_api_request = APIRequest(title=list(self.current_title_hierarchy))

    def _parse_title(self, title_tag):
        level = int(title_tag.name[1:])
        title = title_tag.string

        assert title is not None

        if level == 1:
            self.current_title_hierarchy = [title]
        else:
            previous_lvl = level - 1
            del self.current_title_hierarchy[previous_lvl:]
            # Fill the list if the document skipped intermediate levels
            while len(self.current_title_hierarchy) < previous_lvl:
                self.current_title_hierarchy.append("")
            self.current_title_hierarchy.append(title)

        return level

    def _parse_parameters(self, table_tag):
        if not self.current_api_request:
            # Some global examples use tables but are not tied to a specific
            # API request.
            return

        for child in table_tag.children:
            if child.name.lower() == "thead":
                content = self._parse_parameters_thead(child)
                # Only parse tables describing the requests arguments.
                if content[0].strip().lower() != "argument":
                    return
            elif child.name.lower() == "tbody":
                self._parse_parameters_tbody(child)

    def _parse_parameters_thead(self, thead):
        row = thead.find("tr")
        return self._parse_table_row(row)

    def _parse_parameters_tbody(self, tbody):
        parameters = {}
        for row in tbody.find_all("tr"):
            assert row.name.lower() == "tr"
            param, desc = self._parse_table_row(row)
            parameters[param] = desc

        self.current_api_request.parameters = parameters

    def _parse_table_row(self, row):
        cells_content = []
        for cell in row.find_all(["th", "td"]):
            cells_content.append(cell.get_text())

        return tuple(cells_content)

    def _parse_code_block(self, codeblock, language=None):
        if not self.current_api_request:
            return

        classes = codeblock.get("class", [])
        if "shell" in classes:
            language = "shell"
        elif "json" in classes:
            language = "json"

        if len(codeblock.contents) == 1 and codeblock.contents[0].name == "code":
            self._parse_code_block(codeblock.contents[0], language=language)
            return

        code = codeblock.get_text()
        if code.strip().startswith(HTTP_VERBS):
            language = "http"
            self._parse_http_request(code)
        else:
            snippet = CodeSnippet(code.strip(), language=language)
            self.current_api_request.response = snippet

    def _parse_http_request(self, http_request_code):
        http_request_code = http_request_code.strip()
        http_verb, endpoint = http_request_code.split(maxsplit=1)
        self.current_api_request.http_verb = http_verb
        self.current_api_request.endpoint = endpoint

    def parse_example_http_request(self, codeblock):
        full_text = codeblock.get_text()

        http_request_lines = []
        in_http_request = False
        for line in full_text.splitlines():
            line = line.strip()

            if not in_http_request and line.startswith("curl "):
                in_http_request = True

            if line.startswith("#") or "API_KEY" in line:
                continue
            if line.endswith("\\"):
                line = line[:-1].strip()

            if not line:
                break

        if not http_request_lines:
            return None

        http_request = " ".join(http_request_lines)
        return http_request

    def parse_example_http_return_code(self, codeblock):
        full_text = codeblock.get_text()

        for line in full_text.splitlines():
            line = line.strip()

            if "HTTP/" in line:
                return line

        return None

    def parse_example_json(self, codeblock):
        full_text = codeblock.get_text()

        json_lines = []
        in_json = False
        for line in full_text.splitlines():
            if not in_json and line.strip().startswith("{"):
                in_json = True

            if not in_json:
                continue

            json_lines.append(line)

        if not json_lines:
            return None

        json_str = "\n".join(json_lines)

        return json_str


def main():
    fetch_api_doc(CACHE_FILEPATH)
    doc_parser = DocParser(CACHE_FILEPATH)
    version = doc_parser.parse_version()
    api_requests = doc_parser.parse_content()
    formatted = formatted_documentation(version, api_requests)

    write_formatted_documentation(version, formatted)

    print(f"Wrote documentation for version {version}")


def fetch_api_doc(output_path):
    cache_path = pathlib.Path(output_path)

    cache_path.parent.mkdir(parents=False, exist_ok=True)

    if not cache_path.exists():
        should_refresh_cache = True
    else:
        cache_modification_date = datetime.datetime.fromtimestamp(
            cache_path.stat().st_mtime
        )
        cache_modification_timedelta = datetime.datetime.now() - cache_modification_date

        should_refresh_cache = cache_modification_timedelta > MAX_CACHE_DURATION

    if not should_refresh_cache:
        return

    print("Refreshing cache")

    r = requests.get("https://simplemdm.com/docs/api/")
    r.raise_for_status()

    with open(CACHE_FILEPATH, "w") as fp:
        fp.write(r.text)


def formatted_documentation(version, api_requests):
    s = f"// SimpleMDM API Version {version}\n\n"
    for api_request in api_requests:
        s += api_request.as_markdown()

    return s


def write_formatted_documentation(version, formatted_doc):
    out_filename = f"SimpleMDM-API-{version}.md"
    out_filepath = os.path.join(OUTPUT_DIRECTORY, out_filename)
    with open(out_filepath, "w") as fp:
        fp.write(formatted_doc)


if __name__ == "__main__":
    main()
