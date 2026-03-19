---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__backend__control__block.html
original_path: doxygen/html/structlog__backend__control__block.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_control\_block Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md)

Logger backend control block.
[More...](#details)

`#include <[log_backend.h](log__backend_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [ctx](#afe83e2bdd97c544905b913eb81676eb4) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a0024522b0ae3dd547f048752e7dd047e) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [active](#a99528f4b8d70d7c882c7c1b81b62a168) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [level](#aa024c78a507c89056cd634f3a190efec) |

## Detailed Description

Logger backend control block.

## Field Documentation

## [◆ ](#a99528f4b8d70d7c882c7c1b81b62a168)active

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_backend\_control\_block::active |
| --- |

## [◆ ](#afe83e2bdd97c544905b913eb81676eb4)ctx

| void\* log\_backend\_control\_block::ctx |
| --- |

## [◆ ](#a0024522b0ae3dd547f048752e7dd047e)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_backend\_control\_block::id |
| --- |

## [◆ ](#aa024c78a507c89056cd634f3a190efec)level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_backend\_control\_block::level |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_backend.h](log__backend_8h_source.md)

- [log\_backend\_control\_block](structlog__backend__control__block.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
