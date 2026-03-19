---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcdc__ecm__descriptor.html
original_path: doxygen/html/structcdc__ecm__descriptor.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdc\_ecm\_descriptor Struct Reference

Ethernet Networking Functional Descriptor.
[More...](#details)

`#include <[usb_cdc.h](usb__cdc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bFunctionLength](#aa5cfb3a02e9818cf3faaff1dbb9dd487) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#ae000bdad185ca5af3674274ea3fa45d6) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorSubtype](#aaf95074ec751f227a33317325567c890) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [iMACAddress](#ad43f97e428ef743d4655a1e91b91478d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bmEthernetStatistics](#a3a7b901bef04212b217a69d055e37e66) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wMaxSegmentSize](#afdf7f4478515917b1ed653118e7a8540) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wNumberMCFilters](#a196fcac7b1c9bf0f2b42a6d4ccb48de6) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bNumberPowerFilters](#aed687a9629eb3c793af9260db407a136) |

## Detailed Description

Ethernet Networking Functional Descriptor.

## Field Documentation

## [◆ ](#aaf95074ec751f227a33317325567c890)bDescriptorSubtype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ecm\_descriptor::bDescriptorSubtype |
| --- |

## [◆ ](#ae000bdad185ca5af3674274ea3fa45d6)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ecm\_descriptor::bDescriptorType |
| --- |

## [◆ ](#aa5cfb3a02e9818cf3faaff1dbb9dd487)bFunctionLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ecm\_descriptor::bFunctionLength |
| --- |

## [◆ ](#a3a7b901bef04212b217a69d055e37e66)bmEthernetStatistics

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cdc\_ecm\_descriptor::bmEthernetStatistics |
| --- |

## [◆ ](#aed687a9629eb3c793af9260db407a136)bNumberPowerFilters

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ecm\_descriptor::bNumberPowerFilters |
| --- |

## [◆ ](#ad43f97e428ef743d4655a1e91b91478d)iMACAddress

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ecm\_descriptor::iMACAddress |
| --- |

## [◆ ](#afdf7f4478515917b1ed653118e7a8540)wMaxSegmentSize

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cdc\_ecm\_descriptor::wMaxSegmentSize |
| --- |

## [◆ ](#a196fcac7b1c9bf0f2b42a6d4ccb48de6)wNumberMCFilters

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cdc\_ecm\_descriptor::wNumberMCFilters |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_cdc.h](usb__cdc_8h_source.md)

- [cdc\_ecm\_descriptor](structcdc__ecm__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
