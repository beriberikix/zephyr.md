---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/select_8h.html
original_path: doxygen/html/select_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

select.h File Reference

`#include <[zephyr/net/socket_types.h](socket__types_8h_source.md)>`  
`#include <[zephyr/net/socket_select.h](socket__select_8h_source.md)>`

[Go to the source code of this file.](select_8h_source.md)

| Macros | |
| --- | --- |
| #define | [fd\_set](#a7acea921b59df1dc48b89b21ecfa446b)   [zsock\_fd\_set](structzsock__fd__set.md) |
| #define | [FD\_SETSIZE](#a86c5dbf5a99358e288f573d6a1e0873f)   [ZSOCK\_FD\_SETSIZE](group__bsd__sockets.md#ga5c88da69b8d9401d3ae02495056f7e23) |
| #define | [FD\_ZERO](#aaf62b9bedda0be6bd5a878a9146883fe)   [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb) |
| #define | [FD\_SET](#a279931aa1d0b7974e7a5a7cbaab4244f)   [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25) |
| #define | [FD\_CLR](#a3246fcda97abc25e2187633c7800df66)   [ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5) |
| #define | [FD\_ISSET](#ad23e70ae9e622bb3aa740c623d276d6f)   [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab) |

| Functions | |
| --- | --- |
| int | [select](#aa95a19f21c5fced38c8bd3a64f362192) (int nfds, [zsock\_fd\_set](structzsock__fd__set.md) \*readfds, [zsock\_fd\_set](structzsock__fd__set.md) \*writefds, [zsock\_fd\_set](structzsock__fd__set.md) \*exceptfds, struct [timeval](structtimeval.md) \*timeout) |

## Macro Definition Documentation

## [◆ ](#a3246fcda97abc25e2187633c7800df66)FD\_CLR

| #define FD\_CLR   [ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5) |
| --- |

## [◆ ](#ad23e70ae9e622bb3aa740c623d276d6f)FD\_ISSET

| #define FD\_ISSET   [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab) |
| --- |

## [◆ ](#a279931aa1d0b7974e7a5a7cbaab4244f)FD\_SET

| #define FD\_SET   [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25) |
| --- |

## [◆ ](#a7acea921b59df1dc48b89b21ecfa446b)fd\_set

| #define fd\_set   [zsock\_fd\_set](structzsock__fd__set.md) |
| --- |

## [◆ ](#a86c5dbf5a99358e288f573d6a1e0873f)FD\_SETSIZE

| #define FD\_SETSIZE   [ZSOCK\_FD\_SETSIZE](group__bsd__sockets.md#ga5c88da69b8d9401d3ae02495056f7e23) |
| --- |

## [◆ ](#aaf62b9bedda0be6bd5a878a9146883fe)FD\_ZERO

| #define FD\_ZERO   [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb) |
| --- |

## Function Documentation

## [◆ ](#aa95a19f21c5fced38c8bd3a64f362192)select()

| int select | ( | int | *nfds*, |
| --- | --- | --- | --- |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *readfds*, |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *writefds*, |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *exceptfds*, |
|  |  | struct [timeval](structtimeval.md) \* | *timeout* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [select.h](select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
