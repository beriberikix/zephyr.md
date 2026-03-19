---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unioni3c__ccc__getcaps.html
original_path: doxygen/html/unioni3c__ccc__getcaps.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_getcaps Union Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for GETCAPS CCC (Get Optional Feature Capabilities).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [gethdrcap](#ac3a378ed34efc38aa2f9605208e24cef) |  |
|  | I3C v1.0 HDR Capabilities. [More...](#ac3a378ed34efc38aa2f9605208e24cef) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [getcaps](#ab16e2b0e084371a9cbf57abf518f3e7e) [4] |  |
|  | I3C v1.1+ Device Capabilities Byte 1 GETCAPS1. [More...](#ab16e2b0e084371a9cbf57abf518f3e7e) |
| } | [fmt1](#a908096a7dc051b59b9953575f9e5bf3b) |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [tgtcaps](#a99f11e2283bde1d4370a792a46ef8bad) [4] |  |
|  | Defining Byte 0x00: TGTCAPS. [More...](#a99f11e2283bde1d4370a792a46ef8bad) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [testpat](#afd68057c626bb954cee2b6b46350ebae) |  |
|  | Defining Byte 0x5A: TESTPAT. [More...](#afd68057c626bb954cee2b6b46350ebae) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [crcaps](#a6266e60251e02ed9f1009ce1721adef8) [2] |  |
|  | Defining Byte 0x91: CRCAPS Byte 1 CRCAPS1. [More...](#a6266e60251e02ed9f1009ce1721adef8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [vtcaps](#ae7ab28922904daa7ef7380f0ddb41cb3) [2] |  |
|  | Defining Byte 0x93: VTCAPS Byte 1 VTCAPS1. [More...](#ae7ab28922904daa7ef7380f0ddb41cb3) |
| } | [fmt2](#a4b09537b6b796aa2b4fb962d7a4c446d) |

## Detailed Description

Payload for GETCAPS CCC (Get Optional Feature Capabilities).

Note
:   Only supports GETCAPS Format 1 and Format 2. In I3C v1.0 this was GETHDRCAP which only returned a single byte which is the same as the GETCAPS1 byte.

## Field Documentation

## [◆ ](#a6266e60251e02ed9f1009ce1721adef8)crcaps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getcaps::crcaps[2] |
| --- |

Defining Byte 0x91: CRCAPS Byte 1 CRCAPS1.

- Bit[0]: Hot-Join Support
- Bit[1]: Group Management Support
- Bit[2]: Multi-Lane Support Byte 2 CRCAPS2
- Bit[0]: In-Band Interrupt Support
- Bit[1]: Controller Pass-Back
- Bit[2]: Deep Sleep Capable
- Bit[3]: Delayed Controller Handoff

## [◆ ](#a908096a7dc051b59b9953575f9e5bf3b)[union]

| union { ... } i3c\_ccc\_getcaps::fmt1 |
| --- |

## [◆ ](#a4b09537b6b796aa2b4fb962d7a4c446d)[union]

| union { ... } i3c\_ccc\_getcaps::fmt2 |
| --- |

## [◆ ](#ab16e2b0e084371a9cbf57abf518f3e7e)getcaps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getcaps::getcaps[4] |
| --- |

I3C v1.1+ Device Capabilities Byte 1 GETCAPS1.

- Bit[0]: HDR-DDR
- Bit[1]: HDR-TSP
- Bit[2]: HDR-TSL
- Bit[3]: HDR-BT
- Bit[7:4]: Reserved Byte 2 GETCAPS2
- Bit[3:0]: I3C 1.x Specification Version
- Bit[5:4]: Group Address Capabilities
- Bit[6]: HDR-DDR Write Abort
- Bit[7]: HDR-DDR Abort CRC Byte 3 GETCAPS3
- Bit[0]: Multi-Lane (ML) Data Transfer Support
- Bit[1]: Device to Device Transfer (D2DXFER) Support
- Bit[2]: Device to Device Transfer (D2DXFER) IBI Capable
- Bit[3]: Defining Byte Support in GETCAPS
- Bit[4]: Defining Byte Support in GETSTATUS
- Bit[5]: HDR-BT CRC-32 Support
- Bit[6]: IBI MDB Support for Pending Read Notification
- Bit[7]: Reserved Byte 4 GETCAPS4
- Bit[7:0]: Reserved

## [◆ ](#ac3a378ed34efc38aa2f9605208e24cef)gethdrcap

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getcaps::gethdrcap |
| --- |

I3C v1.0 HDR Capabilities.

- Bit[0]: HDR-DDR
- Bit[1]: HDR-TSP
- Bit[2]: HDR-TSL
- Bit[7:3]: Reserved

## [◆ ](#afd68057c626bb954cee2b6b46350ebae)testpat

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i3c\_ccc\_getcaps::testpat |
| --- |

Defining Byte 0x5A: TESTPAT.

Note
:   should always be 0xA55AA55A in big endian

## [◆ ](#a99f11e2283bde1d4370a792a46ef8bad)tgtcaps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getcaps::tgtcaps[4] |
| --- |

Defining Byte 0x00: TGTCAPS.

See also
:   i3c\_ccc\_getcaps::fmt1::getcaps

## [◆ ](#ae7ab28922904daa7ef7380f0ddb41cb3)vtcaps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getcaps::vtcaps[2] |
| --- |

Defining Byte 0x93: VTCAPS Byte 1 VTCAPS1.

- Bit[2:0]: Virtual Target Type
- Bit[4]: Side Effects
- Bit[5]: Shared Peripheral Detect Byte 2 VTCAPS2
- Bit[1:0]: Interrupt Requests
- Bit[2]: Address Remapping
- Bit[4:3]: Bus Context and Conditions

---

The documentation for this union was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
