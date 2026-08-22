---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structsent__frame.html
original_path: doxygen/html/structsent__frame.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sent\_frame Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SENT Interface](group__sent__interface.md)

SENT frame structure.
[More...](#details)

`#include <[zephyr/drivers/sent/sent.h](drivers_2sent_2sent_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [sent\_frame\_type](group__sent__interface.md#ga069232b79943be845df411539ef04993) | [type](#aafd880b826c351481b384b5fef106068) |
|  | Type of SENT frame. |
| union { |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [id](#a689cb24f6c8049e6282ca30939430c8f) |  |
|  | Serial message ID. [More...](#a689cb24f6c8049e6282ca30939430c8f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [data](#a43d52380608b7683534dc31873a396af) |  |
|  | Serial message data. [More...](#a43d52380608b7683534dc31873a396af) |
| }   [serial](#ab39f8ecf19e198ca4818fb13d522c6f4) |
|  | Serial message. [More...](#ab39f8ecf19e198ca4818fb13d522c6f4) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [data\_nibbles](#a4bef9a0871e8ecd86b6753e5bb46c6a0) [8] |  |
|  | Array of fast message data nibbles. [More...](#a4bef9a0871e8ecd86b6753e5bb46c6a0) |
| }   [fast](#a1c02dabd2b0605b77683daf17fc7980b) |
|  | Fast message. [More...](#a1c02dabd2b0605b77683daf17fc7980b) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timestamp](#aae185d5b024a3d9afc135ecc19c9410f) |
|  | Timestamp of when the frame was captured. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc](#a648203dab36ae27e874a171c71d92fe8) |
|  | CRC checksum for message integrity validation. |

## Detailed Description

SENT frame structure.

## Field Documentation

## [◆ ](#aa3f6f64517db501bd3d83b817921b9d8)[union]

| union { ... } [sent\_frame](structsent__frame.md) |
| --- |

## [◆ ](#a648203dab36ae27e874a171c71d92fe8)crc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent\_frame::crc |
| --- |

CRC checksum for message integrity validation.

## [◆ ](#a43d52380608b7683534dc31873a396af)data

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sent\_frame::data |
| --- |

Serial message data.

## [◆ ](#a4bef9a0871e8ecd86b6753e5bb46c6a0)data\_nibbles

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent\_frame::data\_nibbles[8] |
| --- |

Array of fast message data nibbles.

## [◆ ](#a1c02dabd2b0605b77683daf17fc7980b)[struct]

| struct { ... } sent\_frame::fast |
| --- |

Fast message.

## [◆ ](#a689cb24f6c8049e6282ca30939430c8f)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent\_frame::id |
| --- |

Serial message ID.

## [◆ ](#ab39f8ecf19e198ca4818fb13d522c6f4)[struct]

| struct { ... } sent\_frame::serial |
| --- |

Serial message.

## [◆ ](#aae185d5b024a3d9afc135ecc19c9410f)timestamp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sent\_frame::timestamp |
| --- |

Timestamp of when the frame was captured.

## [◆ ](#aafd880b826c351481b384b5fef106068)type

| enum [sent\_frame\_type](group__sent__interface.md#ga069232b79943be845df411539ef04993) sent\_frame::type |
| --- |

Type of SENT frame.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/sent/[sent.h](drivers_2sent_2sent_8h_source.md)

- [sent\_frame](structsent__frame.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
