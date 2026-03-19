---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcan__mcan__tx__buffer__hdr.html
original_path: doxygen/html/structcan__mcan__tx__buffer__hdr.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_tx\_buffer\_hdr Struct Reference

Bosch M\_CAN Tx Buffer Element header.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [ext\_id](#ab4800365c1f2cd76c2e19c27b8d72956): 29 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [rtr](#a6ef37c0a073550c2b99ec29fdb834ca1): 1 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [xtd](#a0ee2e857b6f63c2d70179d89398ffb9a): 1 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [esi](#ae30ffd52da3ea38188fa04ace20054ad): 1 |  |
| } |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pad1](#ac78c3e0f4dda2eddc25ae8066cc29134): 18 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [std\_id](#a9b1f4f0f66d1de07cf6ed212baa713be): 11 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pad2](#aa43b5da1708dbf49794c586ca3af7365): 3 |  |
| } |  |
| }; |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [res1](#a4bd206867f0ba937b93888285ea4095a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dlc](#a9b96b8b75d4ff4c9df3192a244dabc82): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [brs](#af6554e36649326a1ee01757096e1c68f): 1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fdf](#a7ac73d1c09b84267a4701b5d4fa7c920): 1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tsce](#a053c1a8d986dd4537398c052712d394d): 1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [efc](#a6f760970f0483dc16aa8ecc0715591d3): 1 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mm](#ac76ce5728912347d0193c4ed5f467c92) |

## Detailed Description

Bosch M\_CAN Tx Buffer Element header.

See Bosch M\_CAN Users Manual section 2.4.3 for details.

## Field Documentation

## [◆ ](#a72bb766ab7715e149e53e57247c26781)[union]

| union { ... } [can\_mcan\_tx\_buffer\_hdr](structcan__mcan__tx__buffer__hdr.md) |
| --- |

## [◆ ](#af6554e36649326a1ee01757096e1c68f)brs

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_buffer\_hdr::brs |
| --- |

## [◆ ](#a9b96b8b75d4ff4c9df3192a244dabc82)dlc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_buffer\_hdr::dlc |
| --- |

## [◆ ](#a6f760970f0483dc16aa8ecc0715591d3)efc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_buffer\_hdr::efc |
| --- |

## [◆ ](#ae30ffd52da3ea38188fa04ace20054ad)esi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_buffer\_hdr::esi |
| --- |

## [◆ ](#ab4800365c1f2cd76c2e19c27b8d72956)ext\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_buffer\_hdr::ext\_id |
| --- |

## [◆ ](#a7ac73d1c09b84267a4701b5d4fa7c920)fdf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_buffer\_hdr::fdf |
| --- |

## [◆ ](#ac76ce5728912347d0193c4ed5f467c92)mm

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_buffer\_hdr::mm |
| --- |

## [◆ ](#ac78c3e0f4dda2eddc25ae8066cc29134)pad1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_buffer\_hdr::pad1 |
| --- |

## [◆ ](#aa43b5da1708dbf49794c586ca3af7365)pad2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_buffer\_hdr::pad2 |
| --- |

## [◆ ](#a4bd206867f0ba937b93888285ea4095a)res1

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_mcan\_tx\_buffer\_hdr::res1 |
| --- |

## [◆ ](#a6ef37c0a073550c2b99ec29fdb834ca1)rtr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_buffer\_hdr::rtr |
| --- |

## [◆ ](#a9b1f4f0f66d1de07cf6ed212baa713be)std\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_buffer\_hdr::std\_id |
| --- |

## [◆ ](#a053c1a8d986dd4537398c052712d394d)tsce

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_mcan\_tx\_buffer\_hdr::tsce |
| --- |

## [◆ ](#a0ee2e857b6f63c2d70179d89398ffb9a)xtd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_tx\_buffer\_hdr::xtd |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_tx\_buffer\_hdr](structcan__mcan__tx__buffer__hdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
