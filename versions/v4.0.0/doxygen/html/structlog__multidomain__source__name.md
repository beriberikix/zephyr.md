---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__multidomain__source__name.html
original_path: doxygen/html/structlog__multidomain__source__name.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_source\_name Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Content of the source name message.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [domain\_id](#a4a89f856d19bb122e8db88ecc98c5c11) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [source\_id](#aca793d56690b18a2fd33ca191ae4d186) |
| char | [name](#af49c1f590284e7b8da65801e062c83de) [0] |

## Detailed Description

Content of the source name message.

## Field Documentation

## [◆ ](#a4a89f856d19bb122e8db88ecc98c5c11)domain\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_source\_name::domain\_id |
| --- |

## [◆ ](#af49c1f590284e7b8da65801e062c83de)name

| char log\_multidomain\_source\_name::name[0] |
| --- |

## [◆ ](#aca793d56690b18a2fd33ca191ae4d186)source\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) log\_multidomain\_source\_name::source\_id |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_source\_name](structlog__multidomain__source__name.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
