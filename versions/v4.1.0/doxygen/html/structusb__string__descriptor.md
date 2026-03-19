---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusb__string__descriptor.html
original_path: doxygen/html/structusb__string__descriptor.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_string\_descriptor Struct Reference

USB Unicode (UTF16LE) String Descriptor defined in spec.
[More...](#details)

`#include <[usb_ch9.h](usb__ch9_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bLength](#a93d9bb7c2c44f6f0cae1a871a4a18789) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#a37d44e07cb6d5b449b03fb70c9677b15) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bString](#aefde51bb570c2bb2eb172c07d48233f1) |

## Detailed Description

USB Unicode (UTF16LE) String Descriptor defined in spec.

Table 9-15

## Field Documentation

## [◆ ](#a37d44e07cb6d5b449b03fb70c9677b15)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_string\_descriptor::bDescriptorType |
| --- |

## [◆ ](#a93d9bb7c2c44f6f0cae1a871a4a18789)bLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_string\_descriptor::bLength |
| --- |

## [◆ ](#aefde51bb570c2bb2eb172c07d48233f1)bString

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_string\_descriptor::bString |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usb\_ch9.h](usb__ch9_8h_source.md)

- [usb\_string\_descriptor](structusb__string__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
