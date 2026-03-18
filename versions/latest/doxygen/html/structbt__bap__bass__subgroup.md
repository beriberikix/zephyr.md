---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__bass__subgroup.html
original_path: doxygen/html/structbt__bap__bass__subgroup.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_bass\_subgroup Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Struct to hold subgroup specific information for the receive state.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bis\_sync](#ac8061995eb73ba30e335e37714396ff5) |
|  | BIS synced bitfield. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [metadata\_len](#ace1c1ff5d2f5cc79838653d468166664) |
|  | Length of the metadata. |

## Detailed Description

Struct to hold subgroup specific information for the receive state.

## Field Documentation

## [◆ ](#ac8061995eb73ba30e335e37714396ff5)bis\_sync

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_bass\_subgroup::bis\_sync |
| --- |

BIS synced bitfield.

## [◆ ](#ace1c1ff5d2f5cc79838653d468166664)metadata\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_bass\_subgroup::metadata\_len |
| --- |

Length of the metadata.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
