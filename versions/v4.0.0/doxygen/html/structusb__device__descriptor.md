---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusb__device__descriptor.html
original_path: doxygen/html/structusb__device__descriptor.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_device\_descriptor Struct Reference

USB Standard Device Descriptor defined in spec.
[More...](#details)

`#include <[usb_ch9.h](usb__ch9_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bLength](#af3f980ad55af3fd6c222a8802996ab63) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#ad1ba08da6ad5b6023f1d0d1461daab7d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bcdUSB](#aa400edb6c3183d4922411cdaf980b84e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDeviceClass](#aa657267e1d9762b7d2ed3eb60a78d9ad) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDeviceSubClass](#aecfbe730bc3eeccc9c4b5fd17f5f3c3c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDeviceProtocol](#a56829af76e57a6ea4fc621b52a0664f8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bMaxPacketSize0](#ac7f47eb197506ac5c555bb4f2fe82d32) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [idVendor](#a043126e48bebbab536540e44428b6b4f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [idProduct](#a70d5ecc7bad486b8a8840d86aa151579) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bcdDevice](#a41416aa4a49999d2f3f0f67bdc5fa7da) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [iManufacturer](#ad082330020575944b8471459b816cb40) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [iProduct](#acb90b91c59e65adbcc21949cf0f486f7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [iSerialNumber](#a105d91b68091e61c9b13ea673fb98eaf) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bNumConfigurations](#a603204b0517e9ece9bc0d8476b2a7cdc) |

## Detailed Description

USB Standard Device Descriptor defined in spec.

Table 9-8

## Field Documentation

## [◆ ](#a41416aa4a49999d2f3f0f67bdc5fa7da)bcdDevice

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_device\_descriptor::bcdDevice |
| --- |

## [◆ ](#aa400edb6c3183d4922411cdaf980b84e)bcdUSB

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_device\_descriptor::bcdUSB |
| --- |

## [◆ ](#ad1ba08da6ad5b6023f1d0d1461daab7d)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::bDescriptorType |
| --- |

## [◆ ](#aa657267e1d9762b7d2ed3eb60a78d9ad)bDeviceClass

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::bDeviceClass |
| --- |

## [◆ ](#a56829af76e57a6ea4fc621b52a0664f8)bDeviceProtocol

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::bDeviceProtocol |
| --- |

## [◆ ](#aecfbe730bc3eeccc9c4b5fd17f5f3c3c)bDeviceSubClass

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::bDeviceSubClass |
| --- |

## [◆ ](#af3f980ad55af3fd6c222a8802996ab63)bLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::bLength |
| --- |

## [◆ ](#ac7f47eb197506ac5c555bb4f2fe82d32)bMaxPacketSize0

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::bMaxPacketSize0 |
| --- |

## [◆ ](#a603204b0517e9ece9bc0d8476b2a7cdc)bNumConfigurations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::bNumConfigurations |
| --- |

## [◆ ](#a70d5ecc7bad486b8a8840d86aa151579)idProduct

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_device\_descriptor::idProduct |
| --- |

## [◆ ](#a043126e48bebbab536540e44428b6b4f)idVendor

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_device\_descriptor::idVendor |
| --- |

## [◆ ](#ad082330020575944b8471459b816cb40)iManufacturer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::iManufacturer |
| --- |

## [◆ ](#acb90b91c59e65adbcc21949cf0f486f7)iProduct

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::iProduct |
| --- |

## [◆ ](#a105d91b68091e61c9b13ea673fb98eaf)iSerialNumber

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_descriptor::iSerialNumber |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usb\_ch9.h](usb__ch9_8h_source.md)

- [usb\_device\_descriptor](structusb__device__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
