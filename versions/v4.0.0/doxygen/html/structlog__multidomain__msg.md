---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__multidomain__msg.html
original_path: doxygen/html/structlog__multidomain__msg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_msg Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Message.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a87d6e66eea288c0505acce44d6358cf0) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a032ef0893b06fe0b414305948ca3efa7) |
| union [log\_multidomain\_msg\_data](unionlog__multidomain__msg__data.md) | [data](#a83b96cb88a0ed6fccb7c451bb79bc12f) |

## Detailed Description

Message.

## Field Documentation

## [◆ ](#a83b96cb88a0ed6fccb7c451bb79bc12f)data

| union [log\_multidomain\_msg\_data](unionlog__multidomain__msg__data.md) log\_multidomain\_msg::data |
| --- |

## [◆ ](#a87d6e66eea288c0505acce44d6358cf0)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_msg::id |
| --- |

## [◆ ](#a032ef0893b06fe0b414305948ca3efa7)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_msg::status |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_msg](structlog__multidomain__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
