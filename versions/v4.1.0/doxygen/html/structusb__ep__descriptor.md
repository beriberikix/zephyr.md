---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusb__ep__descriptor.html
original_path: doxygen/html/structusb__ep__descriptor.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_ep\_descriptor Struct Reference

USB Standard Endpoint Descriptor defined in spec.
[More...](#details)

`#include <[usb_ch9.h](usb__ch9_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bLength](#ae75468872ec37d8c986534cd78fce717) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#a21412242cf380750e2623f50b5c294e6) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bEndpointAddress](#a60234a9d35e232957672a5bc5573d541) |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [bmAttributes](#ada1c690dfdee3427f303c04b5825ccca) |  |
| struct [usb\_ep\_desc\_bmattr](structusb__ep__desc__bmattr.md)   [Attributes](#a6be879be0aac0c679c9d50bbaa9e6dda) |  |
| }; |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wMaxPacketSize](#a802ba531354e1d8a1c361af1d0716d82) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bInterval](#a6facefd49d301bbe357e1d420583cf1d) |

## Detailed Description

USB Standard Endpoint Descriptor defined in spec.

Table 9-13

## Field Documentation

## [◆ ](#a6adb255db6a848c460b018d13ec0e1e6)[union]

| union { ... } [usb\_ep\_descriptor](structusb__ep__descriptor.md) |
| --- |

## [◆ ](#a6be879be0aac0c679c9d50bbaa9e6dda)Attributes

| struct [usb\_ep\_desc\_bmattr](structusb__ep__desc__bmattr.md) usb\_ep\_descriptor::Attributes |
| --- |

## [◆ ](#a21412242cf380750e2623f50b5c294e6)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_ep\_descriptor::bDescriptorType |
| --- |

## [◆ ](#a60234a9d35e232957672a5bc5573d541)bEndpointAddress

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_ep\_descriptor::bEndpointAddress |
| --- |

## [◆ ](#a6facefd49d301bbe357e1d420583cf1d)bInterval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_ep\_descriptor::bInterval |
| --- |

## [◆ ](#ae75468872ec37d8c986534cd78fce717)bLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_ep\_descriptor::bLength |
| --- |

## [◆ ](#ada1c690dfdee3427f303c04b5825ccca)bmAttributes

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_ep\_descriptor::bmAttributes |
| --- |

## [◆ ](#a802ba531354e1d8a1c361af1d0716d82)wMaxPacketSize

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_ep\_descriptor::wMaxPacketSize |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usb\_ch9.h](usb__ch9_8h_source.md)

- [usb\_ep\_descriptor](structusb__ep__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
