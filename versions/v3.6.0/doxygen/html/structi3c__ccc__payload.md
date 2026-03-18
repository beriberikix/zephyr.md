---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi3c__ccc__payload.html
original_path: doxygen/html/structi3c__ccc__payload.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_payload Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload structure for one CCC transaction.
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [id](#ae6aa0a3465af855872ae0006def29fea) |  |
|  | The CCC ID (`I3C_CCC_*`). [More...](#ae6aa0a3465af855872ae0006def29fea) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [data](#ac52dbf51c5d7903c02c9f149e47a1b0b) |  |
|  | Pointer to byte array of data for this CCC. [More...](#ac52dbf51c5d7903c02c9f149e47a1b0b) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [data\_len](#afcc17965b8bdd0e5e26cd15cebe49cee) |  |
|  | Length in bytes for optional data array. [More...](#afcc17965b8bdd0e5e26cd15cebe49cee) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [num\_xfer](#a9d0f7efcc7774941f057c2ab0fb14439) |  |
|  | Total number of bytes transferred. [More...](#a9d0f7efcc7774941f057c2ab0fb14439) |
| } | [ccc](#a45b2f35955bbb2bcaf89077e5abf3466) |
| struct { |  |
| struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md) \*   [payloads](#a3dcab72bf5b627426f963df56514c38d) |  |
|  | Array of struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md "Payload structure for Direct CCC to one target."). [More...](#a3dcab72bf5b627426f963df56514c38d) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [num\_targets](#afc1706d47d22300e7fa44754920b2685) |  |
|  | Number of targets. [More...](#afc1706d47d22300e7fa44754920b2685) |
| } | [targets](#aa93b97b77f8dff8e931731c1f9edcd86) |

## Detailed Description

Payload structure for one CCC transaction.

## Field Documentation

## [◆ ](#a45b2f35955bbb2bcaf89077e5abf3466)[struct]

| struct { ... } i3c\_ccc\_payload::ccc |
| --- |

## [◆ ](#ac52dbf51c5d7903c02c9f149e47a1b0b)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* i3c\_ccc\_payload::data |
| --- |

Pointer to byte array of data for this CCC.

This is the bytes following the CCC command in CCC frame. Set to `NULL` if no associated data.

## [◆ ](#afcc17965b8bdd0e5e26cd15cebe49cee)data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) i3c\_ccc\_payload::data\_len |
| --- |

Length in bytes for optional data array.

## [◆ ](#ae6aa0a3465af855872ae0006def29fea)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_payload::id |
| --- |

The CCC ID (`I3C_CCC_*`).

## [◆ ](#afc1706d47d22300e7fa44754920b2685)num\_targets

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) i3c\_ccc\_payload::num\_targets |
| --- |

Number of targets.

## [◆ ](#a9d0f7efcc7774941f057c2ab0fb14439)num\_xfer

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) i3c\_ccc\_payload::num\_xfer |
| --- |

Total number of bytes transferred.

A Controller can abort a transfer before the length of the buffer. It is expected for the driver to write to this after the transfer.

## [◆ ](#a3dcab72bf5b627426f963df56514c38d)payloads

| struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md)\* i3c\_ccc\_payload::payloads |
| --- |

Array of struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md "Payload structure for Direct CCC to one target.").

Each element describes the target and associated payloads for this CCC.

Use with Direct CCC.

## [◆ ](#aa93b97b77f8dff8e931731c1f9edcd86)[struct]

| struct { ... } i3c\_ccc\_payload::targets |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_payload](structi3c__ccc__payload.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
