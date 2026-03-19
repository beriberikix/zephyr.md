---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usbd__uac2_8h.html
original_path: doxygen/html/usbd__uac2_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_uac2.h File Reference

USB Audio Class 2 device public header.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](usbd__uac2_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uac2\_ops](structuac2__ops.md) |
|  | USB Audio 2 application event handlers. [More...](structuac2__ops.md#details) |

| Macros | |
| --- | --- |
| #define | [UAC2\_ENTITY\_ID](group__uac2__device.md#gaa35265e83d894896806fcca28feb84a3)(node) |
|  | Get entity ID. |

| Functions | |
| --- | --- |
| void | [usbd\_uac2\_set\_ops](group__uac2__device.md#ga802a727c1a201c26a3bd74f0e7f0900c) (const struct [device](structdevice.md) \*dev, const struct [uac2\_ops](structuac2__ops.md) \*ops, void \*user\_data) |
|  | Register USB Audio 2 application callbacks. |
| int | [usbd\_uac2\_send](group__uac2__device.md#gae899d75d786f5b1df86db48de88d1254) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) terminal, void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size) |
|  | Send audio data to output terminal. |

## Detailed Description

USB Audio Class 2 device public header.

This header describes only class API interaction with application. The audio device itself is modelled with devicetree zephyr,uac2 compatible.

This API is currently considered experimental.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_uac2.h](usbd__uac2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
