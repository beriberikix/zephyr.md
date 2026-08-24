---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structshell__cmd__help.html
original_path: doxygen/html/structshell__cmd__help.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_cmd\_help Struct Reference

[Operating System Services](group__os__services.md) » [Shell API](group__shell__api.md)

Shell structured help descriptor.
[More...](#details)

`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [description](#af9e182e1599c3cfcc42f739d40a511bb) |
|  | Command description. |
| const char \* | [usage](#a3735f4afeeea3d968d9e8fc74e0aa68f) |
|  | Command usage string. |

## Detailed Description

Shell structured help descriptor.

This structure provides an organized way to specify command help as opposed to a free-form string. This helps make help messages more consistent and easier to read.

## Field Documentation

## [◆ ](#af9e182e1599c3cfcc42f739d40a511bb)description

| const char\* shell\_cmd\_help::description |
| --- |

Command description.

## [◆ ](#a3735f4afeeea3d968d9e8fc74e0aa68f)usage

| const char\* shell\_cmd\_help::usage |
| --- |

Command usage string.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell.h](shell_2shell_8h_source.md)

- [shell\_cmd\_help](structshell__cmd__help.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
