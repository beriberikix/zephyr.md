---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__link__ctrl__blk.html
original_path: doxygen/html/structlog__link__ctrl__blk.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_link\_ctrl\_blk Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Log link API](group__log__link.md)

`#include <[log_link.h](log__link_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [domain\_cnt](#a96eab52ab1863b8d9e9b2570d9fd9808) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [source\_cnt](#a5c443cba449be55477220dcd350c6a68) [1+[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_LOG\_MULTIDOMAIN,(CONFIG\_LOG\_REMOTE\_DOMAIN\_MAX\_COUNT),(0))] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [domain\_offset](#a6fe49a96b5b9d79f641125e43c67ba50) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [filters](#a3352b5f8f8ee8b78825db1216c60aa0d) |

## Field Documentation

## [◆ ](#a96eab52ab1863b8d9e9b2570d9fd9808)domain\_cnt

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_link\_ctrl\_blk::domain\_cnt |
| --- |

## [◆ ](#a6fe49a96b5b9d79f641125e43c67ba50)domain\_offset

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_link\_ctrl\_blk::domain\_offset |
| --- |

## [◆ ](#a3352b5f8f8ee8b78825db1216c60aa0d)filters

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* log\_link\_ctrl\_blk::filters |
| --- |

## [◆ ](#a5c443cba449be55477220dcd350c6a68)source\_cnt

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) log\_link\_ctrl\_blk::source\_cnt[1+[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_LOG\_MULTIDOMAIN,(CONFIG\_LOG\_REMOTE\_DOMAIN\_MAX\_COUNT),(0))] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_link.h](log__link_8h_source.md)

- [log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
