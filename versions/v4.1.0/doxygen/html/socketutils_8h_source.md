---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/socketutils_8h_source.html
original_path: doxygen/html/socketutils_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socketutils.h

[Go to the documentation of this file.](socketutils_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKETUTILS\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_SOCKETUTILS\_H\_

14

15#include <[zephyr/net/socket.h](net_2socket_8h.md)>

16

[ 24](socketutils_8h.md#aae0889a4a96fd9763e3f5337b4703205)const char \*[net\_addr\_str\_find\_port](socketutils_8h.md#aae0889a4a96fd9763e3f5337b4703205)(const char \*addr\_str);

25

[ 41](socketutils_8h.md#ab60f526101571078d9b24055f130b1a0)int [net\_getaddrinfo\_addr\_str](socketutils_8h.md#ab60f526101571078d9b24055f130b1a0)(const char \*addr\_str, const char \*def\_port,

42 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

43 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

44

45#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKETUTILS\_H\_ \*/

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[net\_addr\_str\_find\_port](socketutils_8h.md#aae0889a4a96fd9763e3f5337b4703205)

const char \* net\_addr\_str\_find\_port(const char \*addr\_str)

Find port in addr:port string.

[net\_getaddrinfo\_addr\_str](socketutils_8h.md#ab60f526101571078d9b24055f130b1a0)

int net\_getaddrinfo\_addr\_str(const char \*addr\_str, const char \*def\_port, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

Call getaddrinfo() on addr:port string.

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:276

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socketutils.h](socketutils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
