---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlog__msg__desc.html
original_path: doxygen/html/structlog__msg__desc.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_msg\_desc Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Log message API](group__log__msg.md)

`#include <[log_msg.h](log__msg_8h_source.md)>`

| Data Fields | |
| --- | --- |
|  | [MPSC\_PBUF\_HDR](#adf93cabaf90a5104ff1100cb727ee06c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [type](#a54df4eb52aea2b2039ebe453c74b3ad5):1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [domain](#a2636fe29ddba79450689b90beff3c3c7):3 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [level](#a8cc3ca0930b892a6a9b7b73d20f8628e):3 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [package\_len](#a3b9fb3a9e612ec8642e5e595d6478ac3):11 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data\_len](#aff700ad436ba87af141268e8f7aa5f6f):12 |

## Field Documentation

## [◆ ](#aff700ad436ba87af141268e8f7aa5f6f)data\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_msg\_desc::data\_len |
| --- |

## [◆ ](#a2636fe29ddba79450689b90beff3c3c7)domain

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_msg\_desc::domain |
| --- |

## [◆ ](#a8cc3ca0930b892a6a9b7b73d20f8628e)level

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_msg\_desc::level |
| --- |

## [◆ ](#adf93cabaf90a5104ff1100cb727ee06c)MPSC\_PBUF\_HDR

| log\_msg\_desc::MPSC\_PBUF\_HDR |
| --- |

## [◆ ](#a3b9fb3a9e612ec8642e5e595d6478ac3)package\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_msg\_desc::package\_len |
| --- |

## [◆ ](#a54df4eb52aea2b2039ebe453c74b3ad5)type

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_msg\_desc::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_msg.h](log__msg_8h_source.md)

- [log\_msg\_desc](structlog__msg__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
