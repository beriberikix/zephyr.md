---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structshell__websocket__line__buf.html
original_path: doxygen/html/structshell__websocket__line__buf.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_websocket\_line\_buf Struct Reference

Line buffer structure.
[More...](#details)

`#include <[shell_websocket.h](shell__websocket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [buf](#a10a756bb4194410962dfffa59338664c) [CONFIG\_SHELL\_WEBSOCKET\_LINE\_BUF\_SIZE] |
|  | Line buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#a336e882343a970379b95fcf8d8998f59) |
|  | Current line length. |

## Detailed Description

Line buffer structure.

## Field Documentation

## [◆ ](#a10a756bb4194410962dfffa59338664c)buf

| char shell\_websocket\_line\_buf::buf[CONFIG\_SHELL\_WEBSOCKET\_LINE\_BUF\_SIZE] |
| --- |

Line buffer.

## [◆ ](#a336e882343a970379b95fcf8d8998f59)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_websocket\_line\_buf::len |
| --- |

Current line length.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_websocket.h](shell__websocket_8h_source.md)

- [shell\_websocket\_line\_buf](structshell__websocket__line__buf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
