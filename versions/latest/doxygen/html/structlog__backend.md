---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structlog__backend.html
original_path: doxygen/html/structlog__backend.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md)

Logger backend structure.
[More...](#details)

`#include <[log_backend.h](log__backend_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [log\_backend\_api](structlog__backend__api.md) \* | [api](#a87067e427a94d3543c7c50b950649b33) |
| struct [log\_backend\_control\_block](structlog__backend__control__block.md) \* | [cb](#ab8c377e796af0ef81dcf459eeee56a1d) |
| const char \* | [name](#a22b343a8fc32b9aa05f5f4649d78f7d4) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [autostart](#afe5ce6ac891bef0264dabafe18db88a2) |

## Detailed Description

Logger backend structure.

## Field Documentation

## [◆ ](#a87067e427a94d3543c7c50b950649b33)api

| const struct [log\_backend\_api](structlog__backend__api.md)\* log\_backend::api |
| --- |

## [◆ ](#afe5ce6ac891bef0264dabafe18db88a2)autostart

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_backend::autostart |
| --- |

## [◆ ](#ab8c377e796af0ef81dcf459eeee56a1d)cb

| struct [log\_backend\_control\_block](structlog__backend__control__block.md)\* log\_backend::cb |
| --- |

## [◆ ](#a22b343a8fc32b9aa05f5f4649d78f7d4)name

| const char\* log\_backend::name |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_backend.h](log__backend_8h_source.md)

- [log\_backend](structlog__backend.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
