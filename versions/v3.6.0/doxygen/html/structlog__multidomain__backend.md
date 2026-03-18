---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structlog__multidomain__backend.html
original_path: doxygen/html/structlog__multidomain__backend.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_backend Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Remote backend structure.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [log\_multidomain\_backend\_transport\_api](structlog__multidomain__backend__transport__api.md) \* | [transport\_api](#a0208bacfc4ef3f7a97d6c21cb285a802) |
| const struct [log\_backend](structlog__backend.md) \* | [log\_backend](#af69ce1d65d227bf3c44451351d0c763d) |
| struct k\_sem | [rdy\_sem](#a831975a0c04da8d3aff75d8775fddad6) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [panic](#a073949c15827b039772a00d31dbc9cf9) |
| int | [status](#a42f76ae7ee8bf4aaf24c18743b9b92fa) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ready](#afe4ae23396d02875f7865adc349496e4) |

## Detailed Description

Remote backend structure.

## Field Documentation

## [◆ ](#af69ce1d65d227bf3c44451351d0c763d)log\_backend

| const struct [log\_backend](structlog__backend.md)\* log\_multidomain\_backend::log\_backend |
| --- |

## [◆ ](#a073949c15827b039772a00d31dbc9cf9)panic

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_multidomain\_backend::panic |
| --- |

## [◆ ](#a831975a0c04da8d3aff75d8775fddad6)rdy\_sem

| struct k\_sem log\_multidomain\_backend::rdy\_sem |
| --- |

## [◆ ](#afe4ae23396d02875f7865adc349496e4)ready

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_multidomain\_backend::ready |
| --- |

## [◆ ](#a42f76ae7ee8bf4aaf24c18743b9b92fa)status

| int log\_multidomain\_backend::status |
| --- |

## [◆ ](#a0208bacfc4ef3f7a97d6c21cb285a802)transport\_api

| const struct [log\_multidomain\_backend\_transport\_api](structlog__multidomain__backend__transport__api.md)\* log\_multidomain\_backend::transport\_api |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_backend](structlog__multidomain__backend.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
