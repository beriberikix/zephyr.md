---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/socket__offload_8h_source.html
original_path: doxygen/html/socket__offload_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

[ 29](structsocket__dns__offload.md#a5241208180bcc8f553d0db6e74e5c115) int (\*[getaddrinfo](structsocket__dns__offload.md#a5241208180bcc8f553d0db6e74e5c115))(const char \*node, const char \*service,

30 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

31 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

[ 32](structsocket__dns__offload.md#a73640bb24b4838c337ef1a61ffd4949f) void (\*[freeaddrinfo](structsocket__dns__offload.md#a73640bb24b4838c337ef1a61ffd4949f))(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res);

33};

34

[ 40](socket__offload_8h.md#a1b56446dd816af7101088bb0a474d0f4)void [socket\_offload\_dns\_register](socket__offload_8h.md#a1b56446dd816af7101088bb0a474d0f4)(const struct [socket\_dns\_offload](structsocket__dns__offload.md) \*ops);

41

[ 42](socket__offload_8h.md#a78d9171dc948e37e3413507c1016e8cf)int [socket\_offload\_getaddrinfo](socket__offload_8h.md#a78d9171dc948e37e3413507c1016e8cf)(const char \*node, const char \*service,

43 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

44 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

45

[ 46](socket__offload_8h.md#a0be4370de0a45dfa6907f6514f5079cb)void [socket\_offload\_freeaddrinfo](socket__offload_8h.md#a0be4370de0a45dfa6907f6514f5079cb)(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res);

47

48#ifdef \_\_cplusplus

49}

50#endif

51

52#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_OFFLOAD\_H\_ \*/

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[socket\_offload\_freeaddrinfo](socket__offload_8h.md#a0be4370de0a45dfa6907f6514f5079cb)

void socket\_offload\_freeaddrinfo(struct zsock\_addrinfo \*res)

[socket\_offload\_dns\_register](socket__offload_8h.md#a1b56446dd816af7101088bb0a474d0f4)

void socket\_offload\_dns\_register(const struct socket\_dns\_offload \*ops)

Register an offloaded socket DNS API interface.

[socket\_offload\_getaddrinfo](socket__offload_8h.md#a78d9171dc948e37e3413507c1016e8cf)

int socket\_offload\_getaddrinfo(const char \*node, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

[socket\_dns\_offload](structsocket__dns__offload.md)

An offloaded Socket DNS API interface.

**Definition** socket\_offload.h:28

[socket\_dns\_offload::getaddrinfo](structsocket__dns__offload.md#a5241208180bcc8f553d0db6e74e5c115)

int(\* getaddrinfo)(const char \*node, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

**Definition** socket\_offload.h:29

[socket\_dns\_offload::freeaddrinfo](structsocket__dns__offload.md#a73640bb24b4838c337ef1a61ffd4949f)

void(\* freeaddrinfo)(struct zsock\_addrinfo \*res)

**Definition** socket\_offload.h:32

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:280

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_offload.h](socket__offload_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
