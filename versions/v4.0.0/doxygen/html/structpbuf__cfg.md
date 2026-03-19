---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structpbuf__cfg.html
original_path: doxygen/html/structpbuf__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pbuf\_cfg Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [Packed Buffer API](group__pbuf.md)

Control block of packet buffer.
[More...](#details)

`#include <[pbuf.h](pbuf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [rd\_idx\_loc](#aaec17609d27ad086678dafab940e2ae1) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [wr\_idx\_loc](#afb7da887c911f2530cd9168b0a00b3b6) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dcache\_alignment](#a8e6a0f423a4c2cab92b515246483e8b0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [len](#aad5a0bc4bdef7cec0496e15d75d131dc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data\_loc](#a427cea0b6f83a0411ed251c0fa9cdad5) |

## Detailed Description

Control block of packet buffer.

The structure contains configuration data.

## Field Documentation

## [◆ ](#a427cea0b6f83a0411ed251c0fa9cdad5)data\_loc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* pbuf\_cfg::data\_loc |
| --- |

## [◆ ](#a8e6a0f423a4c2cab92b515246483e8b0)dcache\_alignment

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pbuf\_cfg::dcache\_alignment |
| --- |

## [◆ ](#aad5a0bc4bdef7cec0496e15d75d131dc)len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pbuf\_cfg::len |
| --- |

## [◆ ](#aaec17609d27ad086678dafab940e2ae1)rd\_idx\_loc

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* pbuf\_cfg::rd\_idx\_loc |
| --- |

## [◆ ](#afb7da887c911f2530cd9168b0a00b3b6)wr\_idx\_loc

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* pbuf\_cfg::wr\_idx\_loc |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[pbuf.h](pbuf_8h_source.md)

- [pbuf\_cfg](structpbuf__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
