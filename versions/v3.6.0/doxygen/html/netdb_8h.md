---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/netdb_8h.html
original_path: doxygen/html/netdb_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

netdb.h File Reference

`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](netdb_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NI\_MAXSERV](#aefdeadf85356cc2fa0870d86a6055eb1)   32 |
|  | Provide a reasonable size for apps using getnameinfo. |
| #define | [EAI\_BADFLAGS](#a3f3b38f2ac6688612a0fd20f3e6210be)   DNS\_EAI\_BADFLAGS |
| #define | [EAI\_NONAME](#a0bb00f48d6ba1e8c55b7d85c8e3a19a7)   [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) |
| #define | [EAI\_AGAIN](#a7a0f2f10f8778fe201a68932d18434e5)   [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) |
| #define | [EAI\_FAIL](#acfc712115bf29357d33472da2209dc15)   [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) |
| #define | [EAI\_NODATA](#aae1a32f26ffbb7461251d7c4a7c3a0a2)   [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) |
| #define | [EAI\_MEMORY](#a33d8eb0c89167f95dcdaf23386631174)   [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) |
| #define | [EAI\_SYSTEM](#a8e864fa95f26341c27127deb6237c88c)   DNS\_EAI\_SYSTEM |
| #define | [EAI\_SERVICE](#ac7f08e3ee3c38f7c869beb5a44c9f651)   DNS\_EAI\_SERVICE |
| #define | [EAI\_SOCKTYPE](#a110777c2c99dab32101324b3b1dd1df5)   DNS\_EAI\_SOCKTYPE |
| #define | [EAI\_FAMILY](#a1d195add54c14a8903441848fb2f7da6)   DNS\_EAI\_FAMILY |
| #define | [EAI\_OVERFLOW](#a01d6798d308152b919a0b9f998bbd336)   [DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) |

## Macro Definition Documentation

## [◆ ](#a7a0f2f10f8778fe201a68932d18434e5)EAI\_AGAIN

| #define EAI\_AGAIN   [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) |
| --- |

## [◆ ](#a3f3b38f2ac6688612a0fd20f3e6210be)EAI\_BADFLAGS

| #define EAI\_BADFLAGS   DNS\_EAI\_BADFLAGS |
| --- |

## [◆ ](#acfc712115bf29357d33472da2209dc15)EAI\_FAIL

| #define EAI\_FAIL   [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) |
| --- |

## [◆ ](#a1d195add54c14a8903441848fb2f7da6)EAI\_FAMILY

| #define EAI\_FAMILY   DNS\_EAI\_FAMILY |
| --- |

## [◆ ](#a33d8eb0c89167f95dcdaf23386631174)EAI\_MEMORY

| #define EAI\_MEMORY   [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) |
| --- |

## [◆ ](#aae1a32f26ffbb7461251d7c4a7c3a0a2)EAI\_NODATA

| #define EAI\_NODATA   [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) |
| --- |

## [◆ ](#a0bb00f48d6ba1e8c55b7d85c8e3a19a7)EAI\_NONAME

| #define EAI\_NONAME   [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) |
| --- |

## [◆ ](#a01d6798d308152b919a0b9f998bbd336)EAI\_OVERFLOW

| #define EAI\_OVERFLOW   [DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) |
| --- |

## [◆ ](#ac7f08e3ee3c38f7c869beb5a44c9f651)EAI\_SERVICE

| #define EAI\_SERVICE   DNS\_EAI\_SERVICE |
| --- |

## [◆ ](#a110777c2c99dab32101324b3b1dd1df5)EAI\_SOCKTYPE

| #define EAI\_SOCKTYPE   DNS\_EAI\_SOCKTYPE |
| --- |

## [◆ ](#a8e864fa95f26341c27127deb6237c88c)EAI\_SYSTEM

| #define EAI\_SYSTEM   DNS\_EAI\_SYSTEM |
| --- |

## [◆ ](#aefdeadf85356cc2fa0870d86a6055eb1)NI\_MAXSERV

| #define NI\_MAXSERV   32 |
| --- |

Provide a reasonable size for apps using getnameinfo.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [netdb.h](netdb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
