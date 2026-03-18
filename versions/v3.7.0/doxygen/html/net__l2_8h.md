---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__l2_8h.html
original_path: doxygen/html/net__l2_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_l2.h File Reference

Public API for network L2 interface.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/net/capture.h](capture_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](net__l2_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_l2](structnet__l2.md) |
|  | Network L2 structure. [More...](structnet__l2.md#details) |

| Enumerations | |
| --- | --- |
| enum | [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) { [NET\_L2\_MULTICAST](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a830b548da2dd9598eae68540f662c231) = BIT(0) , [NET\_L2\_MULTICAST\_SKIP\_JOIN\_SOLICIT\_NODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a7751b8c8cae0d4144e4bac368ec741b1) = BIT(1) , [NET\_L2\_PROMISC\_MODE](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a80806febf13d69ca66c329020838b1f8) = BIT(2) , [NET\_L2\_POINT\_TO\_POINT](group__net__l2.md#ggac7db0cc6c56d371a5803873074ec2516a71348de528dc47fdb9d11ec57d1d1ff1) = BIT(3) } |
|  | L2 flags. [More...](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) |

## Detailed Description

Public API for network L2 interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_l2.h](net__l2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
