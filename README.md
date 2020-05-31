# SimpleMDM-APIDocumentationParser

A script to parse the online SimpleMDM API documentation for easy diffing.

[https://simplemdm.com/docs/api/](https://simplemdm.com/docs/api/)

## Goal

The goal is to parse the online HTML documentation and create a Markdown version on the content (as complete as possible). All versions of the Markdown version of the API are kept in the `Versions/` directory and can be diffed.


For example:

```bash
diff Versions/SimpleMDM-API-1.20.md Versions/SimpleMDM-API-1.21.md 
```

```diff
1c1
< // SimpleMDM API Version 1.20
---
> // SimpleMDM API Version 1.21
952a953,960
> # Devices / Clear firmware password
> 
> ```shell
> $ curl https://a.simplemdm.com/api/v1/devices/121/clear_firmware_password
> -> HTTP/1.1 202 Accepted
> ```
```

## Notes

- I developed this for myself, when developing [SimpleMDM-Swift](https://github.com/guillaumealgis/SimpleMDM-Swift)
  - Don't expect beautiful, tested code
  - Don't expect support
- Starting with API version 1.23, the script was rewritten and the output format changed, breaking diffing