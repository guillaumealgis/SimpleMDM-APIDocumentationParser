#!/usr/bin/env python3

import os
import pathlib
import re

from bs4 import BeautifulSoup
import requests

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

OUTPUT_DIRECTORY = os.path.join(SCRIPT_PATH, "Versions")
CACHE_DIRECTORY = os.path.join(SCRIPT_PATH, "cache")
CACHE_FILENAME = "Documentation.html"
CACHE_FILEPATH = os.path.join(CACHE_DIRECTORY, CACHE_FILENAME)


class DocExample:
    def __init__(
        self, title, http_request=None, http_return_code=None, json_result=None
    ):
        self.title = title
        self.http_request = http_request
        self.http_return_code = http_return_code
        self.json_result = json_result

    def as_markdown(self):
        s = f"# {self.title}\n\n"
        if self.http_request:
            s += "```shell\n"
            s += f"$ {self.http_request}\n"
            if self.http_return_code:
                s += f"-> {self.http_return_code}\n"
            s += "```\n\n"
        if self.json_result:
            s += "```json\n"
            s += self.json_result
            s += "\n```\n"
        s += "\n"

        return s


class DocParser:
    def __init__(self):
        with open(CACHE_FILEPATH, "r") as fp:
            self.soup = BeautifulSoup(fp, "html.parser")

    def parse_version(self):
        version_tag = self.soup.find_all(class_="version")

        if len(version_tag) > 1:
            raise ValueError("Found multiple tags with class 'version'")

        full_version_text = version_tag[0].get_text()

        matches = re.fullmatch(r".*?(\d+\.\d+(\.\d+)?)", full_version_text)
        version = matches.group(1)

        return version

    def parse_examples(self):
        doc_examples = []

        codeblocks = self.soup.find_all("pre")
        for codeblock in codeblocks:
            title = self.parse_example_title(codeblock)
            if "shell" in codeblock["class"]:
                http_request = self.parse_example_http_request(codeblock)
                http_return_code = self.parse_example_http_return_code(codeblock)
            else:
                http_request = None
                http_return_code = None
            json = self.parse_example_json(codeblock)

            doc_example = DocExample(
                title=title,
                http_request=http_request,
                http_return_code=http_return_code,
                json_result=json,
            )
            doc_examples.append(doc_example)

        return doc_examples

    def parse_example_title(self, codeblock):
        first_level_title = codeblock.find_previous_sibling("h1")
        second_level_title = None

        prev_sibling = codeblock.previous_sibling
        while prev_sibling and prev_sibling != first_level_title:
            if prev_sibling.name == "h2":
                second_level_title = prev_sibling
                break
            prev_sibling = prev_sibling.previous_sibling

        if not second_level_title:
            return first_level_title.get_text()

        return f"{first_level_title.get_text()} / {second_level_title.get_text()}"

    def parse_example_http_request(self, codeblock):
        full_text = codeblock.get_text()
        http_request_lines = []

        for line in full_text.splitlines():
            line = line.strip()

            if not line:
                continue
            if line.startswith("#"):
                continue
            if line.endswith("\\"):
                line = line[:-1].strip()

            if "API_KEY" not in line:
                http_request_lines.append(line)

            if line.endswith(":"):
                break

        http_request = " ".join(http_request_lines)
        return http_request

    def parse_example_http_return_code(self, codeblock):
        full_text = codeblock.get_text()
        http_request_lines = []

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

    def parse_webhooks_events(self):
        events_title = self.soup.find("h2", id="events")
        events_ul = events_title.find_next_sibling("ul")
        events = [li.get_text() for li in events_ul.find_all("li")]

        return events


def main():
    fetch_api_doc()
    doc_parser = DocParser()
    version = doc_parser.parse_version()
    doc_examples = doc_parser.parse_examples()
    webhooks_events = doc_parser.parse_webhooks_events()
    formatted = formatted_documentation(version, doc_examples, webhooks_events)

    write_formatted_documentation(version, formatted)


def fetch_api_doc():
    if os.path.isfile(CACHE_FILEPATH):
        return

    pathlib.Path(CACHE_DIRECTORY).mkdir(parents=False, exist_ok=True)

    r = requests.get("https://simplemdm.com/docs/api/")
    r.raise_for_status()

    with open(CACHE_FILEPATH, "w") as fp:
        fp.write(r.text)


def formatted_documentation(version, doc_examples, webhooks_events):
    s = f"// SimpleMDM API Version {version}\n\n"
    for doc_example in doc_examples:
        s += doc_example.as_markdown()

    s += formatted_webhooks_events(webhooks_events)

    return s


def formatted_webhooks_events(webhooks_events):
    s = "# Webhooks / Events\n"
    s += "\n"
    for event in webhooks_events:
        s += f"- {event}\n"
    s += "\n"

    return s


def write_formatted_documentation(version, formatted_documentation):
    out_filename = f"SimpleMDM-API-{version}.md"
    out_filepath = os.path.join(OUTPUT_DIRECTORY, out_filename)
    with open(out_filepath, "w") as fp:
        fp.write(formatted_documentation)


if __name__ == "__main__":
    main()
