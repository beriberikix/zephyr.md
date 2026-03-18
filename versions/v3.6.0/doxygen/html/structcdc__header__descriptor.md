---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcdc__header__descriptor.html
original_path: doxygen/html/structcdc__header__descriptor.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdc\_header\_descriptor Struct Reference

Header Functional Descriptor.
[More...](#details)

`#include <[usb_cdc.h](usb__cdc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bFunctionLength](#ac4ad6939d5a075ff2fe6d7505cba630b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#a3b8cc0d8b9d56db158f3b027b2cd6f6a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorSubtype](#a49bf7e700891057f30cd3be77dec0752) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bcdCDC](#ab66b3b87594a4510f11ba9ee950f230c) |

## Detailed Description

Header Functional Descriptor.

## Field Documentation

## [◆ ](#ab66b3b87594a4510f11ba9ee950f230c)bcdCDC

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cdc\_header\_descriptor::bcdCDC |
| --- |

## [◆ ](#a49bf7e700891057f30cd3be77dec0752)bDescriptorSubtype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_header\_descriptor::bDescriptorSubtype |
| --- |

## [◆ ](#a3b8cc0d8b9d56db158f3b027b2cd6f6a)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_header\_descriptor::bDescriptorType |
| --- |

## [◆ ](#ac4ad6939d5a075ff2fe6d7505cba630b)bFunctionLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_header\_descriptor::bFunctionLength |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_cdc.h](usb__cdc_8h_source.md)

- [cdc\_header\_descriptor](structcdc__header__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
