---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/socket__offload_8h_source.html
original_path: doxygen/html/socket__offload_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

[ 52](socket__offload_8h.md#a87f67b6c07b7271778e919ccc88b6d7b)int [socket\_offload\_dns\_deregister](socket__offload_8h.md#a87f67b6c07b7271778e919ccc88b6d7b)(const struct [socket\_dns\_offload](structsocket__dns__offload.md) \*ops);

53

[ 59](socket__offload_8h.md#a0d0123d234cd292282a272cb2e2eeb3c)void [socket\_offload\_dns\_enable](socket__offload_8h.md#a0d0123d234cd292282a272cb2e2eeb3c)(bool enable);

60

67#if defined(CONFIG\_NET\_SOCKETS\_OFFLOAD)

68bool [socket\_offload\_dns\_is\_enabled](socket__offload_8h.md#af341a4e569196545165962e17544d2c9)(void);

69#else

[ 70](socket__offload_8h.md#af341a4e569196545165962e17544d2c9)#define socket\_offload\_dns\_is\_enabled() false

71#endif /\* defined(CONFIG\_NET\_SOCKETS\_OFFLOAD) \*/

72

73

75

76int socket\_offload\_getaddrinfo(const char \*node, const char \*service,

77 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

78 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

79

80void socket\_offload\_freeaddrinfo(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res);

81

83

84#ifdef \_\_cplusplus

85}

86#endif

87

88#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_OFFLOAD\_H\_ \*/

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[socket\_offload\_dns\_enable](socket__offload_8h.md#a0d0123d234cd292282a272cb2e2eeb3c)

void socket\_offload\_dns\_enable(bool enable)

Enable/disable DNS offloading at runtime.

[socket\_offload\_dns\_register](socket__offload_8h.md#a1b56446dd816af7101088bb0a474d0f4)

void socket\_offload\_dns\_register(const struct socket\_dns\_offload \*ops)

Register an offloaded socket DNS API interface.

[socket\_offload\_dns\_deregister](socket__offload_8h.md#a87f67b6c07b7271778e919ccc88b6d7b)

int socket\_offload\_dns\_deregister(const struct socket\_dns\_offload \*ops)

Deregister an offloaded socket DNS API interface.

[socket\_offload\_dns\_is\_enabled](socket__offload_8h.md#af341a4e569196545165962e17544d2c9)

#define socket\_offload\_dns\_is\_enabled()

Check if DNS offloading is enabled.

**Definition** socket\_offload.h:70

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

**Definition** socket.h:313

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_offload.h](socket__offload_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
