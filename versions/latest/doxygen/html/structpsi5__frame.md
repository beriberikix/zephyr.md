---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structpsi5__frame.html
original_path: doxygen/html/structpsi5__frame.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

psi5\_frame Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [PSI5 Interface](group__psi5__interface.md)

PSI5 frame structure.
[More...](#details)

`#include <[zephyr/drivers/psi5/psi5.h](psi5_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [psi5\_frame\_type](group__psi5__interface.md#ga5cb0ef3be35e9ff2d05c39cc17f2659f) | [type](#a975b56a545604103687679c2cb0561eb) |
|  | Type of PSI5 frame. |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [data](#a159d66a7eeee3ffc6714f5058ddeefe9) |  |
|  | Message data. [More...](#a159d66a7eeee3ffc6714f5058ddeefe9) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [id](#ad32ba54088b03cbd4b91e77d9adadec8) |  |
|  | Serial message ID. [More...](#ad32ba54088b03cbd4b91e77d9adadec8) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [data](#abdca8ada802a3352e2da439736f7f2aa) |  |
|  | Serial message data. [More...](#abdca8ada802a3352e2da439736f7f2aa) |
| }   [serial](#a04a7d9d8d1238c823d787543ba2188c3) |
|  | Serial message. [More...](#a04a7d9d8d1238c823d787543ba2188c3) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timestamp](#a3b7f3b38ab831e2789c326a327a05e53) |
|  | Timestamp of when the frame was captured. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc](#abd146305031fa97378b96d46e3e6e97d) |
|  | CRC checksum for message integrity validation. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_number](#aec97ec5f2ebef6903fd0b98d8fd2bec4) |
|  | Slot Number. |

## Detailed Description

PSI5 frame structure.

## Field Documentation

## [◆ ](#ae445da12a7cecf3c30b73ae94efec38b)[union]

| union { ... } [psi5\_frame](structpsi5__frame.md) |
| --- |

## [◆ ](#abd146305031fa97378b96d46e3e6e97d)crc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) psi5\_frame::crc |
| --- |

CRC checksum for message integrity validation.

## [◆ ](#abdca8ada802a3352e2da439736f7f2aa)data [1/2]

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psi5\_frame::data |
| --- |

Serial message data.

## [◆ ](#a159d66a7eeee3ffc6714f5058ddeefe9)data [2/2]

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psi5\_frame::data |
| --- |

Message data.

## [◆ ](#ad32ba54088b03cbd4b91e77d9adadec8)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) psi5\_frame::id |
| --- |

Serial message ID.

## [◆ ](#a04a7d9d8d1238c823d787543ba2188c3)[struct]

| struct { ... } psi5\_frame::serial |
| --- |

Serial message.

## [◆ ](#aec97ec5f2ebef6903fd0b98d8fd2bec4)slot\_number

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) psi5\_frame::slot\_number |
| --- |

Slot Number.

## [◆ ](#a3b7f3b38ab831e2789c326a327a05e53)timestamp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psi5\_frame::timestamp |
| --- |

Timestamp of when the frame was captured.

## [◆ ](#a975b56a545604103687679c2cb0561eb)type

| enum [psi5\_frame\_type](group__psi5__interface.md#ga5cb0ef3be35e9ff2d05c39cc17f2659f) psi5\_frame::type |
| --- |

Type of PSI5 frame.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/psi5/[psi5.h](psi5_8h_source.md)

- [psi5\_frame](structpsi5__frame.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
