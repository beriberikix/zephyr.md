---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcdc__ncm__descriptor.html
original_path: doxygen/html/structcdc__ncm__descriptor.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdc\_ncm\_descriptor Struct Reference

Ethernet Network Control Model (NCM) Descriptor.
[More...](#details)

`#include <[usb_cdc.h](usb__cdc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bFunctionLength](#a932a73d95abf90a0ba7f0de3e1760375) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#a9dea58db91413ebcff65151e006a3b2c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorSubtype](#a9fb11a778a65e5e8538619467cd6c6d6) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bcdNcmVersion](#aa9b5bd71a73783e4a3c85a1d39f9def3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bmNetworkCapabilities](#a8a88e3d7d2b36876a38fa8025118f069) |

## Detailed Description

Ethernet Network Control Model (NCM) Descriptor.

## Field Documentation

## [◆ ](#aa9b5bd71a73783e4a3c85a1d39f9def3)bcdNcmVersion

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cdc\_ncm\_descriptor::bcdNcmVersion |
| --- |

## [◆ ](#a9fb11a778a65e5e8538619467cd6c6d6)bDescriptorSubtype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ncm\_descriptor::bDescriptorSubtype |
| --- |

## [◆ ](#a9dea58db91413ebcff65151e006a3b2c)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ncm\_descriptor::bDescriptorType |
| --- |

## [◆ ](#a932a73d95abf90a0ba7f0de3e1760375)bFunctionLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ncm\_descriptor::bFunctionLength |
| --- |

## [◆ ](#a8a88e3d7d2b36876a38fa8025118f069)bmNetworkCapabilities

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_ncm\_descriptor::bmNetworkCapabilities |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_cdc.h](usb__cdc_8h_source.md)

- [cdc\_ncm\_descriptor](structcdc__ncm__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
