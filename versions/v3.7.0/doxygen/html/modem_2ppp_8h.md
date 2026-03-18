---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/modem_2ppp_8h.html
original_path: doxygen/html/modem_2ppp_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ppp.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/net_pkt.h](net__pkt_8h_source.md)>`  
`#include <[zephyr/sys/ring_buffer.h](ring__buffer_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`  
`#include <[zephyr/modem/stats.h](modem_2stats_8h_source.md)>`

[Go to the source code of this file.](modem_2ppp_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ZEPHYR\_MODEM\_PPP\_](#a4c10bd93401ebba9cc89f81a6f9ab6f2) |
| #define | [MODEM\_PPP\_DEFINE](group__modem__ppp.md#ga78bbcfb655ae8009a6abbc8e09dfbcc0)(\_name, \_init\_iface, \_prio, \_mtu, \_buf\_size) |
|  | Define a modem PPP module and bind it to a network interface. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_ppp\_init\_iface](group__modem__ppp.md#gafdd04a06c32e9ab70755d4f2e68deaad)) (struct [net\_if](structnet__if.md) \*iface) |
|  | L2 network interface init callback. |

| Functions | |
| --- | --- |
| int | [modem\_ppp\_attach](group__modem__ppp.md#gad3ce02dd0a6cf7067c5ca0341f807f88) (struct modem\_ppp \*ppp, struct modem\_pipe \*pipe) |
|  | Attach pipe to instance and connect. |
| struct [net\_if](structnet__if.md) \* | [modem\_ppp\_get\_iface](group__modem__ppp.md#gaebb69341b2b88338b2cfccaa1c0cba0b) (struct modem\_ppp \*ppp) |
|  | Get network interface modem PPP instance is bound to. |
| void | [modem\_ppp\_release](group__modem__ppp.md#gaf2177b83100647ed0894cac7fa435cb3) (struct modem\_ppp \*ppp) |
|  | Release pipe from instance. |

## Macro Definition Documentation

## [◆ ](#a4c10bd93401ebba9cc89f81a6f9ab6f2)ZEPHYR\_MODEM\_PPP\_

| #define ZEPHYR\_MODEM\_PPP\_ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ppp.h](modem_2ppp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
