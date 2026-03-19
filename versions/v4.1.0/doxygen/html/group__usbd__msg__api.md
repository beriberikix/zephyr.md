---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__usbd__msg__api.html
original_path: doxygen/html/group__usbd__msg__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB device core API

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

| Data Structures | |
| --- | --- |
| struct | [usbd\_msg](structusbd__msg.md) |
|  | USB device message. [More...](structusbd__msg.md#details) |

| Enumerations | |
| --- | --- |
| enum | [usbd\_msg\_type](#gaa9163408c0006825575a919322f25f56) {     [USBD\_MSG\_VBUS\_READY](#ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d) , [USBD\_MSG\_VBUS\_REMOVED](#ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268) , [USBD\_MSG\_RESUME](#ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32) , [USBD\_MSG\_SUSPEND](#ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6) ,     [USBD\_MSG\_RESET](#ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156) , [USBD\_MSG\_CONFIGURATION](#ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce) , [USBD\_MSG\_UDC\_ERROR](#ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3) , [USBD\_MSG\_STACK\_ERROR](#ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641) ,     [USBD\_MSG\_CDC\_ACM\_LINE\_CODING](#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1) , [USBD\_MSG\_CDC\_ACM\_CONTROL\_LINE\_STATE](#ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f) , [USBD\_MSG\_DFU\_APP\_DETACH](#ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1) , [USBD\_MSG\_DFU\_DOWNLOAD\_COMPLETED](#ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071) ,     [USBD\_MSG\_MAX\_NUMBER](#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af)   } |
|  | USB device support message types. [More...](#gaa9163408c0006825575a919322f25f56) |

| Functions | |
| --- | --- |
| static const char \* | [usbd\_msg\_type\_string](#ga6cf3d874b1516256187bd96cf73ddde4) (const enum [usbd\_msg\_type](#gaa9163408c0006825575a919322f25f56) type) |
|  | Returns the message type as a constant string. |

## Detailed Description

Since
:   3.7

Version
:   0.1.0

## Enumeration Type Documentation

## [◆ ](#gaa9163408c0006825575a919322f25f56)usbd\_msg\_type

| enum [usbd\_msg\_type](#gaa9163408c0006825575a919322f25f56) |
| --- |

`#include <[usbd_msg.h](usbd__msg_8h.md)>`

USB device support message types.

The first set of message types map to event types from the UDC driver API.

| Enumerator | |
| --- | --- |
| USBD\_MSG\_VBUS\_READY | VBUS ready message (optional). |
| USBD\_MSG\_VBUS\_REMOVED | VBUS removed message (optional). |
| USBD\_MSG\_RESUME | Device resume message. |
| USBD\_MSG\_SUSPEND | Device suspended message. |
| USBD\_MSG\_RESET | Bus reset detected. |
| USBD\_MSG\_CONFIGURATION | Device changed configuration. |
| USBD\_MSG\_UDC\_ERROR | Non-correctable UDC error message. |
| USBD\_MSG\_STACK\_ERROR | Unrecoverable device stack error message. |
| USBD\_MSG\_CDC\_ACM\_LINE\_CODING | CDC ACM Line Coding update. |
| USBD\_MSG\_CDC\_ACM\_CONTROL\_LINE\_STATE | CDC ACM Line State update. |
| USBD\_MSG\_DFU\_APP\_DETACH | USB DFU class detach request. |
| USBD\_MSG\_DFU\_DOWNLOAD\_COMPLETED | USB DFU class download completed. |
| USBD\_MSG\_MAX\_NUMBER | Maximum number of message types. |

## Function Documentation

## [◆ ](#ga6cf3d874b1516256187bd96cf73ddde4)usbd\_msg\_type\_string()

| | const char \* usbd\_msg\_type\_string | ( | const enum [usbd\_msg\_type](#gaa9163408c0006825575a919322f25f56) | *type* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbd_msg.h](usbd__msg_8h.md)>`

Returns the message type as a constant string.

Parameters
:   | [in] | type | USBD message type |
    | --- | --- | --- |

Returns
:   Message type as a constant string

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
