---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/promiscuous_8h.html
original_path: doxygen/html/promiscuous_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

promiscuous.h File Reference

Network interface promiscuous mode support.
[More...](#details)

`#include <[zephyr/net/net_pkt.h](net__pkt_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`

[Go to the source code of this file.](promiscuous_8h_source.md)

| Functions | |
| --- | --- |
| static struct [net\_pkt](structnet__pkt.md) \* | [net\_promisc\_mode\_wait\_data](group__promiscuous.md#ga2fc01f791b635c54e85346cf898b324e) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Start to wait received network packets. |
| static int | [net\_promisc\_mode\_on](group__promiscuous.md#gac1a4b50b547d0f4b9396d71eecafd926) (struct [net\_if](structnet__if.md) \*iface) |
|  | Enable promiscuous mode for a given network interface. |
| static int | [net\_promisc\_mode\_off](group__promiscuous.md#ga089aebe5ce5b6ffc48b485d361bf9e7a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Disable promiscuous mode for a given network interface. |

## Detailed Description

Network interface promiscuous mode support.

An API for applications to start listening network traffic. This requires support from network device driver and from application.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [promiscuous.h](promiscuous_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
