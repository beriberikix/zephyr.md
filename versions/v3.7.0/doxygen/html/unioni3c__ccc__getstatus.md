---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unioni3c__ccc__getstatus.html
original_path: doxygen/html/unioni3c__ccc__getstatus.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_getstatus Union Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for GETSTATUS CCC (Get Device Status).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [status](#a23fe55c75741457ea399a6c7074017f6) |  |
|  | Device Status. [More...](#a23fe55c75741457ea399a6c7074017f6) |
| } | [fmt1](#adbc4805456634d5602ab74c2cde4d903) |
| union { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [tgtstat](#a18b3c86f3157b3dfb30dc51127de2b69) |  |
|  | Defining Byte 0x00: TGTSTAT. [More...](#a18b3c86f3157b3dfb30dc51127de2b69) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [precr](#a104f75402b9ea4b07c9aafc376349d84) |  |
|  | Defining Byte 0x91: PRECR. [More...](#a104f75402b9ea4b07c9aafc376349d84) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [raw\_u16](#ab7a174cc76dd5da060cf420de1f3093e) |  |
| } | [fmt2](#ac3a7629c6d213beff8ab38863a366b11) |

## Detailed Description

Payload for GETSTATUS CCC (Get Device Status).

## Field Documentation

## [◆ ](#adbc4805456634d5602ab74c2cde4d903)[struct]

| struct { ... } i3c\_ccc\_getstatus::fmt1 |
| --- |

## [◆ ](#ac3a7629c6d213beff8ab38863a366b11)[union]

| union { ... } i3c\_ccc\_getstatus::fmt2 |
| --- |

## [◆ ](#a104f75402b9ea4b07c9aafc376349d84)precr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_ccc\_getstatus::precr |
| --- |

Defining Byte 0x91: PRECR.

- Bit[15:8]: Vendor Reserved
- Bit[7:2]: Reserved
- Bit[1]: Handoff Delay NACK
- Bit[0]: Deep Sleep Detected

Note
:   For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

## [◆ ](#ab7a174cc76dd5da060cf420de1f3093e)raw\_u16

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_ccc\_getstatus::raw\_u16 |
| --- |

## [◆ ](#a23fe55c75741457ea399a6c7074017f6)status

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_ccc\_getstatus::status |
| --- |

Device Status.

- Bit[15:8]: Reserved.
- Bit[7:6]: Activity Mode.
- Bit[5]: Protocol Error.
- Bit[4]: Reserved.
- Bit[3:0]: Number of Pending Interrupts.

Note
:   For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

## [◆ ](#a18b3c86f3157b3dfb30dc51127de2b69)tgtstat

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_ccc\_getstatus::tgtstat |
| --- |

Defining Byte 0x00: TGTSTAT.

See also
:   i3c\_ccc\_getstatus::fmt1::status

---

The documentation for this union was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
