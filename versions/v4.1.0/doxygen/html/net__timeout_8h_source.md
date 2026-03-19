---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__timeout_8h_source.html
original_path: doxygen/html/net__timeout_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_timeout.h

[Go to the documentation of this file.](net__timeout_8h.md)

1

6

7/\*

8 \* Copyright (c) 2018 Intel Corporation

9 \* Copyright (c) 2020 Nordic Semiconductor ASA

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_TIMEOUT\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_NET\_TIMEOUT\_H\_

16

25

26#include <[string.h](string_8h.md)>

27#include <[stdbool.h](stdbool_8h.md)>

28#include <[limits.h](limits_8h.md)>

29#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

30#include <[zephyr/sys/slist.h](slist_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 50](group__net__timeout.md#gab59bff1cb36902a27ee8e887ef39a4ce)#define NET\_TIMEOUT\_MAX\_VALUE ((uint32\_t)INT32\_MAX)

51

[ 57](structnet__timeout.md)struct [net\_timeout](structnet__timeout.md) {

[ 64](structnet__timeout.md#aad22be1aa3cdc73fbb14a436fc778282) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__timeout.md#aad22be1aa3cdc73fbb14a436fc778282);

65

[ 70](structnet__timeout.md#af4cdf7a22fea4da9bb68105850c2f1ad) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timer\_start](structnet__timeout.md#af4cdf7a22fea4da9bb68105850c2f1ad);

71

[ 78](structnet__timeout.md#a05142cac2404dc31bf068a439ed309e1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timer\_timeout](structnet__timeout.md#a05142cac2404dc31bf068a439ed309e1);

79

[ 86](structnet__timeout.md#a35b1f793d3f1432123093ca48220426b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wrap\_counter](structnet__timeout.md#a35b1f793d3f1432123093ca48220426b);

87};

88

[ 98](group__net__timeout.md#ga833e08b83a671d4adff799d648a12417)void [net\_timeout\_set](group__net__timeout.md#ga833e08b83a671d4adff799d648a12417)(struct [net\_timeout](structnet__timeout.md) \*timeout,

99 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lifetime,

100 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now);

101

[ 115](group__net__timeout.md#ga3d9804474050d070fc4224e834f8cefc)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [net\_timeout\_deadline](group__net__timeout.md#ga3d9804474050d070fc4224e834f8cefc)(const struct [net\_timeout](structnet__timeout.md) \*timeout,

116 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) now);

117

[ 135](group__net__timeout.md#ga34e39484b19c39b3e37a4799848ad502)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_timeout\_remaining](group__net__timeout.md#ga34e39484b19c39b3e37a4799848ad502)(const struct [net\_timeout](structnet__timeout.md) \*timeout,

136 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now);

137

[ 156](group__net__timeout.md#ga07b07966dd10929f6d3774467614f006)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_timeout\_evaluate](group__net__timeout.md#ga07b07966dd10929f6d3774467614f006)(struct [net\_timeout](structnet__timeout.md) \*timeout,

157 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) now);

158

159#ifdef \_\_cplusplus

160}

161#endif

162

166

167

168#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_TIMEOUT\_H\_ \*/

[net\_timeout\_evaluate](group__net__timeout.md#ga07b07966dd10929f6d3774467614f006)

uint32\_t net\_timeout\_evaluate(struct net\_timeout \*timeout, uint32\_t now)

Update state to reflect elapsed time and get new delay.

[net\_timeout\_remaining](group__net__timeout.md#ga34e39484b19c39b3e37a4799848ad502)

uint32\_t net\_timeout\_remaining(const struct net\_timeout \*timeout, uint32\_t now)

Calculate the remaining time to the timeout in whole seconds.

[net\_timeout\_deadline](group__net__timeout.md#ga3d9804474050d070fc4224e834f8cefc)

int64\_t net\_timeout\_deadline(const struct net\_timeout \*timeout, int64\_t now)

Return the 64-bit system time at which the timeout will complete.

[net\_timeout\_set](group__net__timeout.md#ga833e08b83a671d4adff799d648a12417)

void net\_timeout\_set(struct net\_timeout \*timeout, uint32\_t lifetime, uint32\_t now)

Configure a network timeout structure.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[limits.h](limits_8h.md)

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[string.h](string_8h.md)

[net\_timeout](structnet__timeout.md)

Generic struct for handling network timeouts.

**Definition** net\_timeout.h:57

[net\_timeout::timer\_timeout](structnet__timeout.md#a05142cac2404dc31bf068a439ed309e1)

uint32\_t timer\_timeout

Portion of remaining timeout that does not exceed NET\_TIMEOUT\_MAX\_VALUE.

**Definition** net\_timeout.h:78

[net\_timeout::wrap\_counter](structnet__timeout.md#a35b1f793d3f1432123093ca48220426b)

uint32\_t wrap\_counter

Timer wrap count.

**Definition** net\_timeout.h:86

[net\_timeout::node](structnet__timeout.md#aad22be1aa3cdc73fbb14a436fc778282)

sys\_snode\_t node

Used to link multiple timeouts that share a common timer infrastructure.

**Definition** net\_timeout.h:64

[net\_timeout::timer\_start](structnet__timeout.md#af4cdf7a22fea4da9bb68105850c2f1ad)

uint32\_t timer\_start

Time at which the timer was last set.

**Definition** net\_timeout.h:70

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_timeout.h](net__timeout_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
