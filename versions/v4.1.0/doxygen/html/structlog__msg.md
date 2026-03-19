---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlog__msg.html
original_path: doxygen/html/structlog__msg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_msg Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Log message API](group__log__msg.md)

`#include <[log_msg.h](log__msg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [log\_msg\_hdr](structlog__msg__hdr.md) | [hdr](#a5831ce7bc8d973714a7ca37455890d2a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [padding](#a539123bce09e55516406cf2a25610e8d) [(([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [log\_msg\_hdr](structlog__msg__hdr.md)) % [CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78)) > 0 ?([CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78) -([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [log\_msg\_hdr](structlog__msg__hdr.md)) % [CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78))) :0)] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a2336290d5ac4b87cbd998d81cc49ab7e) [] |

## Field Documentation

## [◆ ](#a2336290d5ac4b87cbd998d81cc49ab7e)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_msg::data[] |
| --- |

## [◆ ](#a5831ce7bc8d973714a7ca37455890d2a)hdr

| struct [log\_msg\_hdr](structlog__msg__hdr.md) log\_msg::hdr |
| --- |

## [◆ ](#a539123bce09e55516406cf2a25610e8d)padding

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_msg::padding[(([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [log\_msg\_hdr](structlog__msg__hdr.md)) % [CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78)) > 0 ?([CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78) -([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)(struct [log\_msg\_hdr](structlog__msg__hdr.md)) % [CBPRINTF\_PACKAGE\_ALIGNMENT](group__cbprintf__apis.md#ga3b917fb81bb246a0910066e2708dbd78))) : 0)] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_msg.h](log__msg_8h_source.md)

- [log\_msg](structlog__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
