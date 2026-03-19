---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mld_8h.html
original_path: doxygen/html/mld_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mld.h File Reference

Multicast Listener Discovery API.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](mld_8h_source.md)

| Functions | |
| --- | --- |
| static int | [net\_ipv6\_mld\_join](group__mld.md#ga53af11b1107b0375d219f2a3f517fcce) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Join a given multicast group. |
| static int | [net\_ipv6\_mld\_leave](group__mld.md#gaa1ccc2b362787fe28fb118af51b49465) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Leave a given multicast group. |

## Detailed Description

Multicast Listener Discovery API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mld.h](mld_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
