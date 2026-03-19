---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/socket__select_8h.html
original_path: doxygen/html/socket__select_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_select.h File Reference

BSD select support functions.
[More...](#details)

`#include <time.h>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/net/socket_types.h](socket__types_8h_source.md)>`  
`#include <[zephyr/sys/fdtable.h](fdtable_8h_source.md)>`

[Go to the source code of this file.](socket__select_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ZSOCK\_FD\_SETSIZE](group__bsd__sockets.md#ga5c88da69b8d9401d3ae02495056f7e23)   [ZVFS\_FD\_SETSIZE](fdtable_8h.md#ae8d10dc8bd02e619f8c384c493f53709) |
|  | Number of file descriptors which can be added to [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8 "Socket file descriptor set."). |

| Typedefs | |
| --- | --- |
| typedef struct [zvfs\_fd\_set](structzvfs__fd__set.md) | [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) |
|  | Socket file descriptor set. |

| Functions | |
| --- | --- |
| static int | [zsock\_select](group__bsd__sockets.md#ga1a065da89061bcb10b10663a9ffbdd10) (int nfds, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*readfds, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*writefds, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*exceptfds, struct zsock\_timeval \*timeout) |
|  | Legacy function to poll multiple sockets for events. |
| static void | [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gaa4855f07c1329a150f371044e4384490) ([zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*set) |
|  | Initialize (clear) [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2). |
| static int | [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#gab92b08adccc22a85e7a1c06bf11a88bc) (int fd, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*set) |
|  | Check whether socket is a member of [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2). |
| static void | [ZSOCK\_FD\_CLR](group__bsd__sockets.md#ga7023ec00d24af41a7cbf5f376fb44487) (int fd, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*set) |
|  | Remove socket from [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2). |
| static void | [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga5d07f52910f6d881295ec659716767f1) (int fd, [zsock\_fd\_set](group__bsd__sockets.md#ga1cdeeddce9000b9fd29b638c422f48f8) \*set) |
|  | Add socket to [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2). |

## Detailed Description

BSD select support functions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_select.h](socket__select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
