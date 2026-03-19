---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structdfu__runtime__descriptor.html
original_path: doxygen/html/structdfu__runtime__descriptor.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu\_runtime\_descriptor Struct Reference

Run-Time Functional Descriptor.
[More...](#details)

`#include <[usb_dfu.h](usb__dfu_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bLength](#a0eeecced453c285febca7a9d867c7241) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#a5464341cf3c706af93de58c6db5edfb9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bmAttributes](#aa8d5f353530adf846b14e88c97095a50) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wDetachTimeOut](#adaf32d218daf9fc74a6639845355cd9b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wTransferSize](#a86312a99ed7c89eb027ca3e35b7b32e5) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bcdDFUVersion](#a3dca4dc35930794eaa0ac03522949048) |

## Detailed Description

Run-Time Functional Descriptor.

## Field Documentation

## [◆ ](#a3dca4dc35930794eaa0ac03522949048)bcdDFUVersion

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dfu\_runtime\_descriptor::bcdDFUVersion |
| --- |

## [◆ ](#a5464341cf3c706af93de58c6db5edfb9)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dfu\_runtime\_descriptor::bDescriptorType |
| --- |

## [◆ ](#a0eeecced453c285febca7a9d867c7241)bLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dfu\_runtime\_descriptor::bLength |
| --- |

## [◆ ](#aa8d5f353530adf846b14e88c97095a50)bmAttributes

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dfu\_runtime\_descriptor::bmAttributes |
| --- |

## [◆ ](#adaf32d218daf9fc74a6639845355cd9b)wDetachTimeOut

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dfu\_runtime\_descriptor::wDetachTimeOut |
| --- |

## [◆ ](#a86312a99ed7c89eb027ca3e35b7b32e5)wTransferSize

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dfu\_runtime\_descriptor::wTransferSize |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_dfu.h](usb__dfu_8h_source.md)

- [dfu\_runtime\_descriptor](structdfu__runtime__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
