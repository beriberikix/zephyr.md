---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcdc__acm__line__coding.html
original_path: doxygen/html/structcdc__acm__line__coding.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdc\_acm\_line\_coding Struct Reference

Data structure for GET\_LINE\_CODING / SET\_LINE\_CODING class requests.
[More...](#details)

`#include <[usb_cdc.h](usb__cdc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dwDTERate](#a14d35b67e6f00b0d6196ba0e9ef6dfab) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bCharFormat](#afd2fd70a7da783d7aac0d99f9f267383) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bParityType](#a472270d84e160348e024f756b834cbb8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDataBits](#ab685d018d83e3e2d38c87c27902cca3e) |

## Detailed Description

Data structure for GET\_LINE\_CODING / SET\_LINE\_CODING class requests.

## Field Documentation

## [◆ ](#afd2fd70a7da783d7aac0d99f9f267383)bCharFormat

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_acm\_line\_coding::bCharFormat |
| --- |

## [◆ ](#ab685d018d83e3e2d38c87c27902cca3e)bDataBits

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_acm\_line\_coding::bDataBits |
| --- |

## [◆ ](#a472270d84e160348e024f756b834cbb8)bParityType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_acm\_line\_coding::bParityType |
| --- |

## [◆ ](#a14d35b67e6f00b0d6196ba0e9ef6dfab)dwDTERate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cdc\_acm\_line\_coding::dwDTERate |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_cdc.h](usb__cdc_8h_source.md)

- [cdc\_acm\_line\_coding](structcdc__acm__line__coding.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
