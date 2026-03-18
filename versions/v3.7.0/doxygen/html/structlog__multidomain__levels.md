---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlog__multidomain__levels.html
original_path: doxygen/html/structlog__multidomain__levels.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_levels Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Content of the message for getting logging levels.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [domain\_id](#aaf98df3f72ba16ead6b087aeb05d7861) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [source\_id](#a7033cf517c4166ef31649e99a23e5459) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [level](#abc21eda27ec20f85721d8d03ee7bdc5a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [runtime\_level](#a9d50693b380f28c9c6738a32d9688068) |

## Detailed Description

Content of the message for getting logging levels.

## Field Documentation

## [◆ ](#aaf98df3f72ba16ead6b087aeb05d7861)domain\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_levels::domain\_id |
| --- |

## [◆ ](#abc21eda27ec20f85721d8d03ee7bdc5a)level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_levels::level |
| --- |

## [◆ ](#a9d50693b380f28c9c6738a32d9688068)runtime\_level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_levels::runtime\_level |
| --- |

## [◆ ](#a7033cf517c4166ef31649e99a23e5459)source\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) log\_multidomain\_levels::source\_id |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_levels](structlog__multidomain__levels.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
