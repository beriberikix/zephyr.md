---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusb__setup__packet.html
original_path: doxygen/html/structusb__setup__packet.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_setup\_packet Struct Reference

USB Setup Data packet defined in spec.
[More...](#details)

`#include <[usb_ch9.h](usb__ch9_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [bmRequestType](#a326cfb3e8b11cc2e7cf4738d593cf10a) |  |
| struct [usb\_req\_type\_field](structusb__req__type__field.md)   [RequestType](#afa3d273ae57c3124b14ab100ac9f9a24) |  |
| }; |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bRequest](#aab50ed2f2cdcc1d747f6f224fe9d2018) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wValue](#a619fbc1b9b6452f4394da713bdbc6a89) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wIndex](#a953c058f0e31481a3d59b404037be009) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wLength](#a3421c921569bf3727534652c5f71da96) |

## Detailed Description

USB Setup Data packet defined in spec.

Table 9-2

## Field Documentation

## [◆ ](#aa922c5946a3421318de5ae77f53c464b)[union]

| union { ... } [usb\_setup\_packet](structusb__setup__packet.md) |
| --- |

## [◆ ](#a326cfb3e8b11cc2e7cf4738d593cf10a)bmRequestType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_setup\_packet::bmRequestType |
| --- |

## [◆ ](#aab50ed2f2cdcc1d747f6f224fe9d2018)bRequest

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_setup\_packet::bRequest |
| --- |

## [◆ ](#afa3d273ae57c3124b14ab100ac9f9a24)RequestType

| struct [usb\_req\_type\_field](structusb__req__type__field.md) usb\_setup\_packet::RequestType |
| --- |

## [◆ ](#a953c058f0e31481a3d59b404037be009)wIndex

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_setup\_packet::wIndex |
| --- |

## [◆ ](#a3421c921569bf3727534652c5f71da96)wLength

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_setup\_packet::wLength |
| --- |

## [◆ ](#a619fbc1b9b6452f4394da713bdbc6a89)wValue

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) usb\_setup\_packet::wValue |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usb\_ch9.h](usb__ch9_8h_source.md)

- [usb\_setup\_packet](structusb__setup__packet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
