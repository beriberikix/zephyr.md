---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__config_8h.html
original_path: doxygen/html/net__config_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_config.h File Reference

Routines for network subsystem initialization.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`

[Go to the source code of this file.](net__config_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NET\_CONFIG\_NEED\_ROUTER](group__net__config.md#ga5c1a321477ce072a964bc610aef805f1)   0x00000001 |
|  | Application needs routers to be set so that connectivity to remote network is possible. |
| #define | [NET\_CONFIG\_NEED\_IPV6](group__net__config.md#ga469731c167f97b5df40b51ee0c87313c)   0x00000002 |
|  | Application needs IPv6 subsystem configured and initialized. |
| #define | [NET\_CONFIG\_NEED\_IPV4](group__net__config.md#ga4312efaa62093c93968c0ae81efc36dd)   0x00000004 |
|  | Application needs IPv4 subsystem configured and initialized. |

| Functions | |
| --- | --- |
| int | [net\_config\_init](group__net__config.md#ga02a2b4fbac3eba68a175630293c91484) (const char \*app\_info, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Initialize this network application. |
| int | [net\_config\_init\_by\_iface](group__net__config.md#gab19ec1b3411f38d9bee5abcb25926ea0) (struct [net\_if](structnet__if.md) \*iface, const char \*app\_info, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Initialize this network application using a specific network interface. |
| int | [net\_config\_init\_app](group__net__config.md#ga49c6b4cd9d338f1b3d76225a9872c84c) (const struct [device](structdevice.md) \*dev, const char \*app\_info) |
|  | Initialize this network application. |

## Detailed Description

Routines for network subsystem initialization.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_config.h](net__config_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
