---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structfcb.html
original_path: doxygen/html/structfcb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcb Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Flash Circular Buffer (FCB)](group__fcb.md) » [Flash Circular Buffer Data Structures](group__fcb__data__structures.md)

FCB instance structure.
[More...](#details)

`#include <[fcb.h](fcb_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [f\_magic](#a4206faa9ed633ba2315163c52e557397) |
|  | Magic value, should not be 0xFFFFFFFF. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [f\_version](#a030b96abd6c857295f154197278cca69) |
|  | Current version number of the data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [f\_sector\_cnt](#aa642058028d755c7bc5b6814a4cb8c16) |
|  | Number of elements in sector array. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [f\_scratch\_cnt](#aab748de6989e30de6571fc94d66ee365) |
|  | Number of sectors to keep empty. |
| struct [flash\_sector](structflash__sector.md) \* | [f\_sectors](#afc96f045d541c8d141d3427884f1fb44) |
|  | Array of sectors, must be contiguous. |
| struct [k\_mutex](structk__mutex.md) | [f\_mtx](#a1f30c78d7e02748fbf0bf5033d4bdadf) |
|  | Locking for accessing the FCB data, internal state. |
| struct [flash\_sector](structflash__sector.md) \* | [f\_oldest](#ac6dc6236f8b03e4b03f691c55b4d3327) |
|  | Pointer to flash sector containing the oldest data, internal state. |
| struct [fcb\_entry](structfcb__entry.md) | [f\_active](#a1f7922dc1e8076bcfffca117260d5e02) |
|  | internal state |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [f\_active\_id](#a8da1d0b4bef7d9ddcd5922d9bbef0cef) |
|  | Flash location where the newest data is, internal state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [f\_align](#aa745e88d4477408b40a759dd1baea637) |
|  | writes to flash have to aligned to this, internal state |
| const struct [flash\_area](structflash__area.md) \* | [fap](#a16cfc82afc8abe70291f4b462e617f2f) |
|  | Flash area used by the fcb instance, internal state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [f\_erase\_value](#a614c6441395637c6c0a17a4fd6107db3) |
|  | The value flash takes when it is erased. |

## Detailed Description

FCB instance structure.

The following data structure describes the FCB itself. First part should be filled in by the user before calling [fcb\_init](group__fcb__api.md#gab304f3e9e28f6229d7ddbe638eda2f70 "fcb_init"). The second part is used by FCB for its internal bookkeeping.

## Field Documentation

## [◆ ](#a1f7922dc1e8076bcfffca117260d5e02)f\_active

| struct [fcb\_entry](structfcb__entry.md) fcb::f\_active |
| --- |

internal state

## [◆ ](#a8da1d0b4bef7d9ddcd5922d9bbef0cef)f\_active\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fcb::f\_active\_id |
| --- |

Flash location where the newest data is, internal state.

## [◆ ](#aa745e88d4477408b40a759dd1baea637)f\_align

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fcb::f\_align |
| --- |

writes to flash have to aligned to this, internal state

## [◆ ](#a614c6441395637c6c0a17a4fd6107db3)f\_erase\_value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fcb::f\_erase\_value |
| --- |

The value flash takes when it is erased.

This is read from flash parameters and initialized upon call to fcb\_init.

## [◆ ](#a4206faa9ed633ba2315163c52e557397)f\_magic

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fcb::f\_magic |
| --- |

Magic value, should not be 0xFFFFFFFF.

It is xored with inversion of f\_erase\_value and placed in the beginning of FCB flash sector. FCB uses this when determining whether sector contains valid data or not. Giving it value of 0xFFFFFFFF means leaving bytes of the filed in "erased" state.

## [◆ ](#a1f30c78d7e02748fbf0bf5033d4bdadf)f\_mtx

| struct [k\_mutex](structk__mutex.md) fcb::f\_mtx |
| --- |

Locking for accessing the FCB data, internal state.

## [◆ ](#ac6dc6236f8b03e4b03f691c55b4d3327)f\_oldest

| struct [flash\_sector](structflash__sector.md)\* fcb::f\_oldest |
| --- |

Pointer to flash sector containing the oldest data, internal state.

## [◆ ](#aab748de6989e30de6571fc94d66ee365)f\_scratch\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fcb::f\_scratch\_cnt |
| --- |

Number of sectors to keep empty.

This can be used if you need to have scratch space for garbage collecting when FCB fills up.

## [◆ ](#aa642058028d755c7bc5b6814a4cb8c16)f\_sector\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fcb::f\_sector\_cnt |
| --- |

Number of elements in sector array.

## [◆ ](#afc96f045d541c8d141d3427884f1fb44)f\_sectors

| struct [flash\_sector](structflash__sector.md)\* fcb::f\_sectors |
| --- |

Array of sectors, must be contiguous.

## [◆ ](#a030b96abd6c857295f154197278cca69)f\_version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fcb::f\_version |
| --- |

Current version number of the data.

## [◆ ](#a16cfc82afc8abe70291f4b462e617f2f)fap

| const struct [flash\_area](structflash__area.md)\* fcb::fap |
| --- |

Flash area used by the fcb instance, internal state.

This can be transfer to FCB user

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fcb.h](fcb_8h_source.md)

- [fcb](structfcb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
