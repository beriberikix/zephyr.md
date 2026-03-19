---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusb__device__qualifier__descriptor.html
original_path: doxygen/html/structusb__device__qualifier__descriptor.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_device\_qualifier\_descriptor Struct Reference

USB Device Qualifier Descriptor defined in spec.
[More...](#details)

`#include <[usb_ch9.h](usb__ch9_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bLength](#ab1bf7ff669706ee5370f90d72f2a6856) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#a1547d76b3c2f7599d2621e4c73ef485d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bcdUSB](#aabe610da20b0b4ccc9aefdabd3396bf1) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDeviceClass](#aeb3cbfe114aa775d5121a5580dafa16e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDeviceSubClass](#a9335b5c4955f68463484b55eb480a1fb) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDeviceProtocol](#a9665e7509c611a4eaa0345d3f96ec707) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bMaxPacketSize0](#ad065540e5d99fbd241b0712e601f62ee) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bNumConfigurations](#a4022310ac474e11b6813af8c1f5d093f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bReserved](#aa1557859c9220ae5fda7d32833845444) |

## Detailed Description

USB Device Qualifier Descriptor defined in spec.

Table 9-9

## Field Documentation

## [◆ ](#aabe610da20b0b4ccc9aefdabd3396bf1)bcdUSB

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_device\_qualifier\_descriptor::bcdUSB |
| --- |

## [◆ ](#a1547d76b3c2f7599d2621e4c73ef485d)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_qualifier\_descriptor::bDescriptorType |
| --- |

## [◆ ](#aeb3cbfe114aa775d5121a5580dafa16e)bDeviceClass

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_qualifier\_descriptor::bDeviceClass |
| --- |

## [◆ ](#a9665e7509c611a4eaa0345d3f96ec707)bDeviceProtocol

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_qualifier\_descriptor::bDeviceProtocol |
| --- |

## [◆ ](#a9335b5c4955f68463484b55eb480a1fb)bDeviceSubClass

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_qualifier\_descriptor::bDeviceSubClass |
| --- |

## [◆ ](#ab1bf7ff669706ee5370f90d72f2a6856)bLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_qualifier\_descriptor::bLength |
| --- |

## [◆ ](#ad065540e5d99fbd241b0712e601f62ee)bMaxPacketSize0

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_qualifier\_descriptor::bMaxPacketSize0 |
| --- |

## [◆ ](#a4022310ac474e11b6813af8c1f5d093f)bNumConfigurations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_qualifier\_descriptor::bNumConfigurations |
| --- |

## [◆ ](#aa1557859c9220ae5fda7d32833845444)bReserved

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device\_qualifier\_descriptor::bReserved |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usb\_ch9.h](usb__ch9_8h_source.md)

- [usb\_device\_qualifier\_descriptor](structusb__device__qualifier__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
