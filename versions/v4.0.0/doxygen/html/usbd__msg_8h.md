---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usbd__msg_8h.html
original_path: doxygen/html/usbd__msg_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_msg.h File Reference

USB support message types and structure.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](usbd__msg_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usbd\_msg](structusbd__msg.md) |
|  | USB device message. [More...](structusbd__msg.md#details) |

| Enumerations | |
| --- | --- |
| enum | [usbd\_msg\_type](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56) {     [USBD\_MSG\_VBUS\_READY](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d) , [USBD\_MSG\_VBUS\_REMOVED](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268) , [USBD\_MSG\_RESUME](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32) , [USBD\_MSG\_SUSPEND](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6) ,     [USBD\_MSG\_RESET](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156) , [USBD\_MSG\_CONFIGURATION](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce) , [USBD\_MSG\_UDC\_ERROR](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3) , [USBD\_MSG\_STACK\_ERROR](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641) ,     [USBD\_MSG\_CDC\_ACM\_LINE\_CODING](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1) , [USBD\_MSG\_CDC\_ACM\_CONTROL\_LINE\_STATE](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f) , [USBD\_MSG\_MAX\_NUMBER](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af)   } |
|  | USB device support message types. [More...](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56) |

| Functions | |
| --- | --- |
| static const char \* | [usbd\_msg\_type\_string](group__usbd__msg__api.md#ga6cf3d874b1516256187bd96cf73ddde4) (const enum [usbd\_msg\_type](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56) type) |
|  | Returns the message type as a constant string. |

## Detailed Description

USB support message types and structure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usbd\_msg.h](usbd__msg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
