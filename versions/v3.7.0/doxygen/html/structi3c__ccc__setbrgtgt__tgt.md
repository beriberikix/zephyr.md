---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi3c__ccc__setbrgtgt__tgt.html
original_path: doxygen/html/structi3c__ccc__setbrgtgt__tgt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_setbrgtgt\_tgt Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

One Bridged Target for SETBRGTGT payload.
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#a6fa24f8354e856031464aaaa2c8fd1bb) |
|  | Dynamic address of the bridged target. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#a1dca2717ca9502f11b300a0d9a1fc0e6) |
|  | 16-bit ID for the bridged target. |

## Detailed Description

One Bridged Target for SETBRGTGT payload.

## Field Documentation

## [◆ ](#a6fa24f8354e856031464aaaa2c8fd1bb)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_setbrgtgt\_tgt::addr |
| --- |

Dynamic address of the bridged target.

Note
:   The address is left-shift by 1, and bit[0] is always 0.

## [◆ ](#a1dca2717ca9502f11b300a0d9a1fc0e6)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_ccc\_setbrgtgt\_tgt::id |
| --- |

16-bit ID for the bridged target.

Note
:   For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
