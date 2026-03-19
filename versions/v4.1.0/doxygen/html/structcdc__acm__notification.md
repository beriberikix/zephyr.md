---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcdc__acm__notification.html
original_path: doxygen/html/structcdc__acm__notification.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdc\_acm\_notification Struct Reference

Data structure for the notification about SerialState.
[More...](#details)

`#include <[usb_cdc.h](usb__cdc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bmRequestType](#a57b007a8ec893d660e6ec8a1b25f7dd3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bNotificationType](#af24dae76a280c008e40a0d031171235c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wValue](#a3bf290bc6e851331e93bedf49ae5dbe0) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wIndex](#a290717590343376c8f1f9a865cb4b0ae) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [wLength](#af2f8fbceeaa9a3ad0ae1330b8f82bff2) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [data](#a5666402ce9fbe5fad5f80592aa6f53ec) |

## Detailed Description

Data structure for the notification about SerialState.

## Field Documentation

## [◆ ](#a57b007a8ec893d660e6ec8a1b25f7dd3)bmRequestType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_acm\_notification::bmRequestType |
| --- |

## [◆ ](#af24dae76a280c008e40a0d031171235c)bNotificationType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cdc\_acm\_notification::bNotificationType |
| --- |

## [◆ ](#a5666402ce9fbe5fad5f80592aa6f53ec)data

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cdc\_acm\_notification::data |
| --- |

## [◆ ](#a290717590343376c8f1f9a865cb4b0ae)wIndex

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cdc\_acm\_notification::wIndex |
| --- |

## [◆ ](#af2f8fbceeaa9a3ad0ae1330b8f82bff2)wLength

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cdc\_acm\_notification::wLength |
| --- |

## [◆ ](#a3bf290bc6e851331e93bedf49ae5dbe0)wValue

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cdc\_acm\_notification::wValue |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_cdc.h](usb__cdc_8h_source.md)

- [cdc\_acm\_notification](structcdc__acm__notification.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
