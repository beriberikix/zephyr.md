---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlog__multidomain__set__runtime__level.html
original_path: doxygen/html/structlog__multidomain__set__runtime__level.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_set\_runtime\_level Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Content of the message for setting logging level.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [domain\_id](#ae259c42a8cc2ef7dae8fe82104733d47) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [source\_id](#a7e59a0573f101053d4f73166a97ba834) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [runtime\_level](#a8afa5236860ceea88847e36ca8fcf72c) |

## Detailed Description

Content of the message for setting logging level.

## Field Documentation

## [◆ ](#ae259c42a8cc2ef7dae8fe82104733d47)domain\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_set\_runtime\_level::domain\_id |
| --- |

## [◆ ](#a8afa5236860ceea88847e36ca8fcf72c)runtime\_level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_set\_runtime\_level::runtime\_level |
| --- |

## [◆ ](#a7e59a0573f101053d4f73166a97ba834)source\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) log\_multidomain\_set\_runtime\_level::source\_id |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_set\_runtime\_level](structlog__multidomain__set__runtime__level.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
