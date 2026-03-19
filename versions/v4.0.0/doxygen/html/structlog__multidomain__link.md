---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__multidomain__link.html
original_path: doxygen/html/structlog__multidomain__link.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_link Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Remote link structure.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [log\_multidomain\_link\_transport\_api](structlog__multidomain__link__transport__api.md) \* | [transport\_api](#a4e7e588f666952942191da56aac35e5c) |
| struct k\_sem | [rdy\_sem](#a17e4202830edfafe9ca27b1431d3f0f0) |
| const struct [log\_link](structlog__link.md) \* | [link](#a42c7fc83f2e30e1b63a353915d8cc5af) |
| union [log\_multidomain\_link\_dst](unionlog__multidomain__link__dst.md) | [dst](#a60eb6654d6a53e1cbf0d5cb207c62188) |
| int | [status](#ae98c1ed7276d518c037acf65d1c953d3) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ready](#aabc75deb5b28fb76c7915586ad38b082) |

## Detailed Description

Remote link structure.

## Field Documentation

## [◆ ](#a60eb6654d6a53e1cbf0d5cb207c62188)dst

| union [log\_multidomain\_link\_dst](unionlog__multidomain__link__dst.md) log\_multidomain\_link::dst |
| --- |

## [◆ ](#a42c7fc83f2e30e1b63a353915d8cc5af)link

| const struct [log\_link](structlog__link.md)\* log\_multidomain\_link::link |
| --- |

## [◆ ](#a17e4202830edfafe9ca27b1431d3f0f0)rdy\_sem

| struct k\_sem log\_multidomain\_link::rdy\_sem |
| --- |

## [◆ ](#aabc75deb5b28fb76c7915586ad38b082)ready

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_multidomain\_link::ready |
| --- |

## [◆ ](#ae98c1ed7276d518c037acf65d1c953d3)status

| int log\_multidomain\_link::status |
| --- |

## [◆ ](#a4e7e588f666952942191da56aac35e5c)transport\_api

| const struct [log\_multidomain\_link\_transport\_api](structlog__multidomain__link__transport__api.md)\* log\_multidomain\_link::transport\_api |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_link](structlog__multidomain__link.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
