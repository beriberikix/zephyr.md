---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/dsa__core_8h.html
original_path: doxygen/html/dsa__core_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsa\_core.h File Reference

Distributed Switch Architecture (DSA).
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/phy.h](phy_8h_source.md)>`

[Go to the source code of this file.](dsa__core_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [dsa\_switch\_context](structdsa__switch__context.md) |
|  | DSA switch context data. [More...](structdsa__switch__context.md#details) |
| struct | [dsa\_api](structdsa__api.md) |
|  | Structure to provide DSA switch api callbacks - it is an augmented struct [ethernet\_api](structethernet__api.md "Ethernet L2 API operations."). [More...](structdsa__api.md#details) |
| struct | [dsa\_port\_config](structdsa__port__config.md) |
|  | Structure of DSA port configuration. [More...](structdsa__port__config.md#details) |

| Macros | |
| --- | --- |
| #define | [DSA\_PORT\_INST\_INIT](group__dsa__core.md#ga012eeda4facb67b5c387b74878b53188)(port, n, cfg) |
|  | Macro for DSA port instance initialization. |
| #define | [DSA\_SWITCH\_INST\_INIT](group__dsa__core.md#gaa7665e4b96cbc40cbae6de621f773aa4)(n, \_dapi, data, fn) |
|  | Macro for DSA switch instance initialization. |

| Functions | |
| --- | --- |
| struct [net\_if](structnet__if.md) \* | [dsa\_user\_get\_iface](group__dsa__core.md#ga16d03129d1e4c39f8662dae4b35598d9) (struct [net\_if](structnet__if.md) \*iface, int port\_idx) |
|  | Get network interface of a user port. |

## Detailed Description

Distributed Switch Architecture (DSA).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dsa\_core.h](dsa__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
