---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlog__multidomain__link__transport__api.html
original_path: doxygen/html/structlog__multidomain__link__transport__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_link\_transport\_api Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Structure with link transport API.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [init](#ad452b214d16947dd46ae8700792bd40c) )(struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link) |
| int(\* | [send](#adf02696742ac70a1c4e53d97f21b2bd1) )(struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |

## Detailed Description

Structure with link transport API.

## Field Documentation

## [◆ ](#ad452b214d16947dd46ae8700792bd40c)init

| int(\* log\_multidomain\_link\_transport\_api::init) (struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link) |
| --- |

## [◆ ](#adf02696742ac70a1c4e53d97f21b2bd1)send

| int(\* log\_multidomain\_link\_transport\_api::send) (struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_link\_transport\_api](structlog__multidomain__link__transport__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
