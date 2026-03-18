---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sntp_8h_source.html
original_path: doxygen/html/sntp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

8#ifndef ZEPHYR\_INCLUDE\_NET\_SNTP\_H\_

9#define ZEPHYR\_INCLUDE\_NET\_SNTP\_H\_

10

11#include <[zephyr/net/socket.h](net_2socket_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 25](structsntp__time.md)struct [sntp\_time](structsntp__time.md) {

[ 26](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [seconds](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f);

[ 27](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fraction](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8);

28#if defined(CONFIG\_SNTP\_UNCERTAINTY)

29 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) uptime\_us;

30 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uncertainty\_us;

31#endif

32};

33

[ 35](structsntp__ctx.md)struct [sntp\_ctx](structsntp__ctx.md) {

36 struct {

[ 37](structsntp__ctx.md#a6eec3a1aab8430c5edf39f9f386ee51a) struct [zsock\_pollfd](structzsock__pollfd.md) [fds](structsntp__ctx.md#a6eec3a1aab8430c5edf39f9f386ee51a)[1];

[ 38](structsntp__ctx.md#a388a7d7591a6d76df83d975276398a25) int [nfds](structsntp__ctx.md#a388a7d7591a6d76df83d975276398a25);

[ 39](structsntp__ctx.md#a46b36989e639c675caa3a729dffc8f65) int [fd](structsntp__ctx.md#a46b36989e639c675caa3a729dffc8f65);

[ 40](structsntp__ctx.md#a297ca36079700db840de4a5b3d247611) } [sock](structsntp__ctx.md#a297ca36079700db840de4a5b3d247611);

41

[ 46](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc) struct [sntp\_time](structsntp__time.md) [expected\_orig\_ts](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc);

47};

48

[ 58](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)int [sntp\_init](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx, struct [sockaddr](structsockaddr.md) \*addr,

59 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len);

60

[ 71](group__sntp.md#ga8a32571c1706fbe50d4e58e1cb7f38f6)int [sntp\_query](group__sntp.md#ga8a32571c1706fbe50d4e58e1cb7f38f6)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout,

72 struct [sntp\_time](structsntp__time.md) \*[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067));

73

[ 79](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)void [sntp\_close](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx);

80

[ 94](group__sntp.md#gab2fe2668477065f4c8c381e738324b51)int [sntp\_simple](group__sntp.md#gab2fe2668477065f4c8c381e738324b51)(const char \*server, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout,

95 struct [sntp\_time](structsntp__time.md) \*[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067));

96

97#ifdef \_\_cplusplus

98}

99#endif

100

104

105#endif

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[sntp\_close](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)

void sntp\_close(struct sntp\_ctx \*ctx)

Release SNTP context.

[sntp\_query](group__sntp.md#ga8a32571c1706fbe50d4e58e1cb7f38f6)

int sntp\_query(struct sntp\_ctx \*ctx, uint32\_t timeout, struct sntp\_time \*time)

Perform SNTP query.

[sntp\_init](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)

int sntp\_init(struct sntp\_ctx \*ctx, struct sockaddr \*addr, socklen\_t addr\_len)

Initialize SNTP context.

[sntp\_simple](group__sntp.md#gab2fe2668477065f4c8c381e738324b51)

int sntp\_simple(const char \*server, uint32\_t timeout, struct sntp\_time \*time)

Convenience function to query SNTP in one-shot fashion.

[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)

time\_t time(time\_t \*tloc)

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[sntp\_ctx](structsntp__ctx.md)

SNTP context.

**Definition** sntp.h:35

[sntp\_ctx::sock](structsntp__ctx.md#a297ca36079700db840de4a5b3d247611)

struct sntp\_ctx::@023200030035024071210221027277034102012303120051 sock

[sntp\_ctx::nfds](structsntp__ctx.md#a388a7d7591a6d76df83d975276398a25)

int nfds

**Definition** sntp.h:38

[sntp\_ctx::fd](structsntp__ctx.md#a46b36989e639c675caa3a729dffc8f65)

int fd

**Definition** sntp.h:39

[sntp\_ctx::expected\_orig\_ts](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc)

struct sntp\_time expected\_orig\_ts

Timestamp when the request was sent from client to server.

**Definition** sntp.h:46

[sntp\_ctx::fds](structsntp__ctx.md#a6eec3a1aab8430c5edf39f9f386ee51a)

struct zsock\_pollfd fds[1]

**Definition** sntp.h:37

[sntp\_time](structsntp__time.md)

Time as returned by SNTP API, fractional seconds since 1 Jan 1970.

**Definition** sntp.h:25

[sntp\_time::seconds](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f)

uint64\_t seconds

**Definition** sntp.h:26

[sntp\_time::fraction](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8)

uint32\_t fraction

**Definition** sntp.h:27

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket.h:43

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [sntp.h](sntp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
