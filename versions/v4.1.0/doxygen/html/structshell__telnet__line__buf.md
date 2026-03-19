---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structshell__telnet__line__buf.html
original_path: doxygen/html/structshell__telnet__line__buf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_telnet\_line\_buf Struct Reference

Line buffer structure.
[More...](#details)

`#include <[shell_telnet.h](shell__telnet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [buf](#afdbfe1cad9640b8d9575303c77a8a97e) [CONFIG\_SHELL\_TELNET\_LINE\_BUF\_SIZE] |
|  | Line buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#aaad811b725d1cb7a4601457c0a98b4aa) |
|  | Current line length. |

## Detailed Description

Line buffer structure.

## Field Documentation

## [◆ ](#afdbfe1cad9640b8d9575303c77a8a97e)buf

| char shell\_telnet\_line\_buf::buf[CONFIG\_SHELL\_TELNET\_LINE\_BUF\_SIZE] |
| --- |

Line buffer.

## [◆ ](#aaad811b725d1cb7a4601457c0a98b4aa)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_telnet\_line\_buf::len |
| --- |

Current line length.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_telnet.h](shell__telnet_8h_source.md)

- [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
