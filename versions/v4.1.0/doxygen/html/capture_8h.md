---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/capture_8h.html
original_path: doxygen/html/capture_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

capture.h File Reference

Network packet capture definitions.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](capture_8h_source.md)

| Functions | |
| --- | --- |
| int | [net\_capture\_setup](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262) (const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr, const struct [device](structdevice.md) \*\*dev) |
|  | Setup network packet capturing support. |
| static int | [net\_capture\_cleanup](group__net__capture.md#ga7a56719068938c34c9c6149296074d01) (const struct [device](structdevice.md) \*dev) |
|  | Cleanup network packet capturing support. |
| static int | [net\_capture\_enable](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa) (const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface) |
|  | Enable network packet capturing support. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_capture\_is\_enabled](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc) (const struct [device](structdevice.md) \*dev) |
|  | Is network packet capture enabled or disabled. |
| static int | [net\_capture\_disable](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951) (const struct [device](structdevice.md) \*dev) |
|  | Disable network packet capturing support. |

## Detailed Description

Network packet capture definitions.

Definitions for capturing network packets.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [capture.h](capture_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
