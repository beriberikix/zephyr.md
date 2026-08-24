---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/sntp_8h_source.html
original_path: doxygen/html/sntp_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sntp.h

[Go to the documentation of this file.](sntp_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \* Copyright (c) 2019 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_SNTP\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_SNTP\_H\_

15

16#include <[zephyr/net/socket.h](net_2socket_8h.md)>

17#include <[zephyr/net/socket\_service.h](socket__service_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

31

[ 33](structsntp__time.md)struct [sntp\_time](structsntp__time.md) {

[ 34](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [seconds](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f);

[ 35](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fraction](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8);

36#if defined(CONFIG\_SNTP\_UNCERTAINTY)

37 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) uptime\_us;

38 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uncertainty\_us;

39#endif

40};

41

[ 43](structsntp__ctx.md)struct [sntp\_ctx](structsntp__ctx.md) {

44

46 struct {

47 struct [zsock\_pollfd](structzsock__pollfd.md) fds[1];

48 int nfds;

49 int fd;

50 } sock;

52

[ 57](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc) struct [sntp\_time](structsntp__time.md) [expected\_orig\_ts](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc);

58};

59

[ 69](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)int [sntp\_init](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx, struct [sockaddr](structsockaddr.md) \*addr,

70 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len);

71

[ 82](group__sntp.md#ga25ef46cc74be71bbe2f76de7c30cbe45)int [sntp\_query](group__sntp.md#ga25ef46cc74be71bbe2f76de7c30cbe45)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts);

83

[ 94](group__sntp.md#ga8771cdc6e64ab1489b333cc0c1731e9f)int [sntp\_recv\_response](group__sntp.md#ga8771cdc6e64ab1489b333cc0c1731e9f)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts);

95

[ 101](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)void [sntp\_close](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx);

102

[ 115](group__sntp.md#ga3a45c2b5af5e30b5cbd153368fc7ec3d)int [sntp\_init\_async](group__sntp.md#ga3a45c2b5af5e30b5cbd153368fc7ec3d)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len,

116 const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service);

117

[ 125](group__sntp.md#gab6adcd7259bdfa841b57e535c380508d)int [sntp\_send\_async](group__sntp.md#gab6adcd7259bdfa841b57e535c380508d)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx);

126

[ 139](group__sntp.md#gac73db957041a6814abb286fd9143ddb5)int [sntp\_read\_async](group__sntp.md#gac73db957041a6814abb286fd9143ddb5)(struct [net\_socket\_service\_event](structnet__socket__service__event.md) \*event, struct [sntp\_time](structsntp__time.md) \*ts);

140

[ 146](group__sntp.md#gaeb595e89c56fbb619010e3c8d7b2b5b1)void [sntp\_close\_async](group__sntp.md#gaeb595e89c56fbb619010e3c8d7b2b5b1)(const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service);

147

[ 161](group__sntp.md#ga25c894db6d24a5e729b4edcb8917ce9c)int [sntp\_simple](group__sntp.md#ga25c894db6d24a5e729b4edcb8917ce9c)(const char \*server, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout,

162 struct [sntp\_time](structsntp__time.md) \*ts);

163

[ 179](group__sntp.md#ga75aaee9a8f8490c0cc826a0e9298cd88)int [sntp\_simple\_addr](group__sntp.md#ga75aaee9a8f8490c0cc826a0e9298cd88)(struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout,

180 struct [sntp\_time](structsntp__time.md) \*ts);

181

182#ifdef \_\_cplusplus

183}

184#endif

185

189

190#endif

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[sntp\_close](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)

void sntp\_close(struct sntp\_ctx \*ctx)

Release SNTP context.

[sntp\_simple](group__sntp.md#ga25c894db6d24a5e729b4edcb8917ce9c)

int sntp\_simple(const char \*server, uint32\_t timeout, struct sntp\_time \*ts)

Convenience function to query SNTP in one-shot fashion.

[sntp\_query](group__sntp.md#ga25ef46cc74be71bbe2f76de7c30cbe45)

int sntp\_query(struct sntp\_ctx \*ctx, uint32\_t timeout, struct sntp\_time \*ts)

Perform SNTP query.

[sntp\_init\_async](group__sntp.md#ga3a45c2b5af5e30b5cbd153368fc7ec3d)

int sntp\_init\_async(struct sntp\_ctx \*ctx, struct sockaddr \*addr, socklen\_t addr\_len, const struct net\_socket\_service\_desc \*service)

Initialise SNTP context for async operation.

[sntp\_simple\_addr](group__sntp.md#ga75aaee9a8f8490c0cc826a0e9298cd88)

int sntp\_simple\_addr(struct sockaddr \*addr, socklen\_t addr\_len, uint32\_t timeout, struct sntp\_time \*ts)

Convenience function to query SNTP in one-shot fashion using a pre-initialized address struct.

[sntp\_recv\_response](group__sntp.md#ga8771cdc6e64ab1489b333cc0c1731e9f)

int sntp\_recv\_response(struct sntp\_ctx \*ctx, uint32\_t timeout, struct sntp\_time \*ts)

Attempt to receive an SNTP response after issuing a query.

[sntp\_init](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)

int sntp\_init(struct sntp\_ctx \*ctx, struct sockaddr \*addr, socklen\_t addr\_len)

Initialize SNTP context.

[sntp\_send\_async](group__sntp.md#gab6adcd7259bdfa841b57e535c380508d)

int sntp\_send\_async(struct sntp\_ctx \*ctx)

Send the SNTP query.

[sntp\_read\_async](group__sntp.md#gac73db957041a6814abb286fd9143ddb5)

int sntp\_read\_async(struct net\_socket\_service\_event \*event, struct sntp\_time \*ts)

Read the result of the SNTP query.

[sntp\_close\_async](group__sntp.md#gaeb595e89c56fbb619010e3c8d7b2b5b1)

void sntp\_close\_async(const struct net\_socket\_service\_desc \*service)

Release SNTP context.

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[socket\_service.h](socket__service_8h.md)

BSD Socket service API.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[net\_socket\_service\_desc](structnet__socket__service__desc.md)

Main structure holding socket service configuration information.

**Definition** socket\_service.h:70

[net\_socket\_service\_event](structnet__socket__service__event.md)

This struct contains information which socket triggered calls to the callback function.

**Definition** socket\_service.h:49

[sntp\_ctx](structsntp__ctx.md)

SNTP context.

**Definition** sntp.h:43

[sntp\_ctx::expected\_orig\_ts](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc)

struct sntp\_time expected\_orig\_ts

Timestamp when the request was sent from client to server.

**Definition** sntp.h:57

[sntp\_time](structsntp__time.md)

Time as returned by SNTP API, fractional seconds since 1 Jan 1970.

**Definition** sntp.h:33

[sntp\_time::seconds](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f)

uint64\_t seconds

Second value.

**Definition** sntp.h:34

[sntp\_time::fraction](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8)

uint32\_t fraction

Fractional seconds value.

**Definition** sntp.h:35

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:410

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [sntp.h](sntp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
