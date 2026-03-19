---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/socketcan__utils_8h.html
original_path: doxygen/html/socketcan__utils_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socketcan\_utils.h File Reference

SocketCAN utilities.
[More...](#details)

`#include <[zephyr/drivers/can.h](drivers_2can_8h_source.md)>`  
`#include <[zephyr/net/socketcan.h](socketcan_8h_source.md)>`

[Go to the source code of this file.](socketcan__utils_8h_source.md)

| Functions | |
| --- | --- |
| static void | [socketcan\_to\_can\_frame](group__socket__can.md#gaccedf1d7bf2131797e53a16dc93cd7e1) (const struct [socketcan\_frame](structsocketcan__frame.md) \*sframe, struct [can\_frame](structcan__frame.md) \*zframe) |
|  | Translate a *[socketcan\_frame](structsocketcan__frame.md "CAN frame for Linux SocketCAN compatibility.")* struct to a *[can\_frame](structcan__frame.md "CAN frame structure.")* struct. |
| static void | [socketcan\_from\_can\_frame](group__socket__can.md#ga49ffbe49124fdc472946fd0978f9a6d5) (const struct [can\_frame](structcan__frame.md) \*zframe, struct [socketcan\_frame](structsocketcan__frame.md) \*sframe) |
|  | Translate a *[can\_frame](structcan__frame.md "CAN frame structure.")* struct to a *[socketcan\_frame](structsocketcan__frame.md "CAN frame for Linux SocketCAN compatibility.")* struct. |
| static void | [socketcan\_to\_can\_filter](group__socket__can.md#ga040c4882d349cdc3c568f3580e823cba) (const struct [socketcan\_filter](structsocketcan__filter.md) \*sfilter, struct [can\_filter](structcan__filter.md) \*zfilter) |
|  | Translate a *[socketcan\_filter](structsocketcan__filter.md "CAN filter for Linux SocketCAN compatibility.")* struct to a *[can\_filter](structcan__filter.md "CAN filter structure.")* struct. |
| static void | [socketcan\_from\_can\_filter](group__socket__can.md#gaf5cee7f0d6385c6fc4736e9399ed06b3) (const struct [can\_filter](structcan__filter.md) \*zfilter, struct [socketcan\_filter](structsocketcan__filter.md) \*sfilter) |
|  | Translate a *[can\_filter](structcan__filter.md "CAN filter structure.")* struct to a *[socketcan\_filter](structsocketcan__filter.md "CAN filter for Linux SocketCAN compatibility.")* struct. |

## Detailed Description

SocketCAN utilities.

Utilities for SocketCAN support.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socketcan\_utils.h](socketcan__utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
