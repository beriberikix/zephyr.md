---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/socket__select_8h.html
original_path: doxygen/html/socket__select_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_select.h File Reference

BSD select support functions.
[More...](#details)

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/net/socket_types.h](socket__types_8h_source.md)>`  
`#include <zephyr/syscalls/socket_select.h>`

[Go to the source code of this file.](socket__select_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [zsock\_fd\_set](structzsock__fd__set.md) |
|  | Socket file descriptor set. [More...](structzsock__fd__set.md#details) |

| Macros | |
| --- | --- |
| #define | [ZSOCK\_FD\_SETSIZE](group__bsd__sockets.md#ga5c88da69b8d9401d3ae02495056f7e23)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)((([zsock\_fd\_set](structzsock__fd__set.md) \*)0)->bitset) \* 8) |
|  | Number of file descriptors which can be added to [zsock\_fd\_set](structzsock__fd__set.md "Socket file descriptor set."). |

| Typedefs | |
| --- | --- |
| typedef struct zsock\_fd\_set | [zsock\_fd\_set](group__bsd__sockets.md#ga1fcb157f9f7dece784f5d2c0cb2efb77) |
|  | Socket file descriptor set. |

| Functions | |
| --- | --- |
| int | [zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045) (int nfds, [zsock\_fd\_set](structzsock__fd__set.md) \*readfds, [zsock\_fd\_set](structzsock__fd__set.md) \*writefds, [zsock\_fd\_set](structzsock__fd__set.md) \*exceptfds, struct zsock\_timeval \*timeout) |
|  | Legacy function to poll multiple sockets for events. |
| void | [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb) ([zsock\_fd\_set](structzsock__fd__set.md) \*set) |
|  | Initialize (clear) fd\_set. |
| int | [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |
|  | Check whether socket is a member of fd\_set. |
| void | [ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |
|  | Remove socket from fd\_set. |
| void | [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |
|  | Add socket to fd\_set. |

## Detailed Description

BSD select support functions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_select.h](socket__select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
