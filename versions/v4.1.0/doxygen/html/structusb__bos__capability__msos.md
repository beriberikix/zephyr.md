---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusb__bos__capability__msos.html
original_path: doxygen/html/structusb__bos__capability__msos.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_bos\_capability\_msos Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB BOS support](group__usb__bos.md)

Microsoft OS 2.0 descriptor specific part of platform capability descriptor.
[More...](#details)

`#include <[bos.h](bos_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dwWindowsVersion](#a5e10aed83d93d2ddc1278245aab9cb0a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wMSOSDescriptorSetTotalLength](#adbf37ee9a5d7479d59cd1a44ab8d8ca5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bMS\_VendorCode](#a4da7539d3bc58fe1da48e3d4d8c965e2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bAltEnumCode](#a0945c68d9e7911add0c0586b000c90d3) |

## Detailed Description

Microsoft OS 2.0 descriptor specific part of platform capability descriptor.

## Field Documentation

## [◆ ](#a0945c68d9e7911add0c0586b000c90d3)bAltEnumCode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_bos\_capability\_msos::bAltEnumCode |
| --- |

## [◆ ](#a4da7539d3bc58fe1da48e3d4d8c965e2)bMS\_VendorCode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_bos\_capability\_msos::bMS\_VendorCode |
| --- |

## [◆ ](#a5e10aed83d93d2ddc1278245aab9cb0a)dwWindowsVersion

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usb\_bos\_capability\_msos::dwWindowsVersion |
| --- |

## [◆ ](#adbf37ee9a5d7479d59cd1a44ab8d8ca5)wMSOSDescriptorSetTotalLength

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_bos\_capability\_msos::wMSOSDescriptorSetTotalLength |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[bos.h](bos_8h_source.md)

- [usb\_bos\_capability\_msos](structusb__bos__capability__msos.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
