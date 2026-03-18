---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sntp_8h_source.html
original_path: doxygen/html/sntp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

[ 30](structsntp__time.md)struct [sntp\_time](structsntp__time.md) {

[ 31](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [seconds](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f);

[ 32](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fraction](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8);

33#if defined(CONFIG\_SNTP\_UNCERTAINTY)

34 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) uptime\_us;

35 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uncertainty\_us;

36#endif

37};

38

[ 40](structsntp__ctx.md)struct [sntp\_ctx](structsntp__ctx.md) {

41

43 struct {

44 struct [zsock\_pollfd](structzsock__pollfd.md) fds[1];

45 int nfds;

46 int fd;

47 } sock;

49

[ 54](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc) struct [sntp\_time](structsntp__time.md) [expected\_orig\_ts](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc);

55};

56

[ 66](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)int [sntp\_init](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx, struct [sockaddr](structsockaddr.md) \*addr,

67 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len);

68

[ 79](group__sntp.md#ga8a32571c1706fbe50d4e58e1cb7f38f6)int [sntp\_query](group__sntp.md#ga8a32571c1706fbe50d4e58e1cb7f38f6)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout,

80 struct [sntp\_time](structsntp__time.md) \*[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067));

81

[ 87](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)void [sntp\_close](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)(struct [sntp\_ctx](structsntp__ctx.md) \*ctx);

88

[ 102](group__sntp.md#ga25c894db6d24a5e729b4edcb8917ce9c)int [sntp\_simple](group__sntp.md#ga25c894db6d24a5e729b4edcb8917ce9c)(const char \*server, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout,

103 struct [sntp\_time](structsntp__time.md) \*ts);

104

[ 120](group__sntp.md#ga75aaee9a8f8490c0cc826a0e9298cd88)int [sntp\_simple\_addr](group__sntp.md#ga75aaee9a8f8490c0cc826a0e9298cd88)(struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout,

121 struct [sntp\_time](structsntp__time.md) \*ts);

122

123#ifdef \_\_cplusplus

124}

125#endif

126

130

131#endif

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[sntp\_close](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d)

void sntp\_close(struct sntp\_ctx \*ctx)

Release SNTP context.

[sntp\_simple](group__sntp.md#ga25c894db6d24a5e729b4edcb8917ce9c)

int sntp\_simple(const char \*server, uint32\_t timeout, struct sntp\_time \*ts)

Convenience function to query SNTP in one-shot fashion.

[sntp\_simple\_addr](group__sntp.md#ga75aaee9a8f8490c0cc826a0e9298cd88)

int sntp\_simple\_addr(struct sockaddr \*addr, socklen\_t addr\_len, uint32\_t timeout, struct sntp\_time \*ts)

Convenience function to query SNTP in one-shot fashion using a pre-initialized address struct.

[sntp\_query](group__sntp.md#ga8a32571c1706fbe50d4e58e1cb7f38f6)

int sntp\_query(struct sntp\_ctx \*ctx, uint32\_t timeout, struct sntp\_time \*time)

Perform SNTP query.

[sntp\_init](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13)

int sntp\_init(struct sntp\_ctx \*ctx, struct sockaddr \*addr, socklen\_t addr\_len)

Initialize SNTP context.

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

**Definition** sntp.h:40

[sntp\_ctx::expected\_orig\_ts](structsntp__ctx.md#a58bd69ad86d00183e32ed07a9fbebfdc)

struct sntp\_time expected\_orig\_ts

Timestamp when the request was sent from client to server.

**Definition** sntp.h:54

[sntp\_time](structsntp__time.md)

Time as returned by SNTP API, fractional seconds since 1 Jan 1970.

**Definition** sntp.h:30

[sntp\_time::seconds](structsntp__time.md#a7dc90613b6ac0265ff49b931a786354f)

uint64\_t seconds

Second value.

**Definition** sntp.h:31

[sntp\_time::fraction](structsntp__time.md#ad33fb2e743756bde8538ac6d2ff3eae8)

uint32\_t fraction

Fractional seconds value.

**Definition** sntp.h:32

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [sntp.h](sntp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
