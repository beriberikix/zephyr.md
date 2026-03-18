---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__core_8h.html
original_path: doxygen/html/net__core_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_core.h File Reference

Network core definitions.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/logging/log.h](log_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net/net_timeout.h](net__timeout_8h_source.md)>`

[Go to the source code of this file.](net__core_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) { [NET\_OK](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047) , [NET\_CONTINUE](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f) , [NET\_DROP](group__net__core.md#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3) } |
|  | Net Verdict. [More...](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) |

| Functions | |
| --- | --- |
| int | [net\_recv\_data](group__net__core.md#ga3421119d2b1797ee5d70f736a61f93b7) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Called by lower network stack or network device driver when a network packet has been received. |
| int | [net\_send\_data](group__net__core.md#ga1a1699666716229a59486a51e46044fc) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send data to network. |

## Detailed Description

Network core definitions.

Definitions for networking support.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_core.h](net__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
