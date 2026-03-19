---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlog__multidomain__backend__transport__api.html
original_path: doxygen/html/structlog__multidomain__backend__transport__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_backend\_transport\_api Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Backend transport API.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [init](#aa46c6422f1a5972f6ec139a65abf129e) )(struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend) |
| int(\* | [send](#a95be75d8eb9e6efae986679b3a250dbe) )(struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |

## Detailed Description

Backend transport API.

## Field Documentation

## [◆ ](#aa46c6422f1a5972f6ec139a65abf129e)init

| int(\* log\_multidomain\_backend\_transport\_api::init) (struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend) |
| --- |

## [◆ ](#a95be75d8eb9e6efae986679b3a250dbe)send

| int(\* log\_multidomain\_backend\_transport\_api::send) (struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_backend\_transport\_api](structlog__multidomain__backend__transport__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
