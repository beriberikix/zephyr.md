---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/socket__offload_8h_source.html
original_path: doxygen/html/socket__offload_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_offload.h

[Go to the documentation of this file.](socket__offload_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_OFFLOAD\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_OFFLOAD\_H\_

14

15#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

16#include <[zephyr/net/socket.h](net_2socket_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

[ 28](structsocket__dns__offload.md)struct [socket\_dns\_offload](structsocket__dns__offload.md) {

[ 30](structsocket__dns__offload.md#a5241208180bcc8f553d0db6e74e5c115) int (\*[getaddrinfo](structsocket__dns__offload.md#a5241208180bcc8f553d0db6e74e5c115))(const char \*node, const char \*service,

31 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

32 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

[ 34](structsocket__dns__offload.md#a73640bb24b4838c337ef1a61ffd4949f) void (\*[freeaddrinfo](structsocket__dns__offload.md#a73640bb24b4838c337ef1a61ffd4949f))(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res);

35};

36

[ 42](socket__offload_8h.md#a1b56446dd816af7101088bb0a474d0f4)void [socket\_offload\_dns\_register](socket__offload_8h.md#a1b56446dd816af7101088bb0a474d0f4)(const struct [socket\_dns\_offload](structsocket__dns__offload.md) \*ops);

43

45

46int socket\_offload\_getaddrinfo(const char \*node, const char \*service,

47 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

48 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

49

50void socket\_offload\_freeaddrinfo(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res);

51

53

54#ifdef \_\_cplusplus

55}

56#endif

57

58#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_OFFLOAD\_H\_ \*/

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[socket\_offload\_dns\_register](socket__offload_8h.md#a1b56446dd816af7101088bb0a474d0f4)

void socket\_offload\_dns\_register(const struct socket\_dns\_offload \*ops)

Register an offloaded socket DNS API interface.

[socket\_dns\_offload](structsocket__dns__offload.md)

An offloaded Socket DNS API interface.

**Definition** socket\_offload.h:28

[socket\_dns\_offload::getaddrinfo](structsocket__dns__offload.md#a5241208180bcc8f553d0db6e74e5c115)

int(\* getaddrinfo)(const char \*node, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

DNS getaddrinfo offloaded implementation API.

**Definition** socket\_offload.h:30

[socket\_dns\_offload::freeaddrinfo](structsocket__dns__offload.md#a73640bb24b4838c337ef1a61ffd4949f)

void(\* freeaddrinfo)(struct zsock\_addrinfo \*res)

DNS freeaddrinfo offloaded implementation API.

**Definition** socket\_offload.h:34

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:272

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_offload.h](socket__offload_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
