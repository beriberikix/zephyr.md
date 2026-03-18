---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/trickle_8h_source.html
original_path: doxygen/html/trickle_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

trickle.h

[Go to the documentation of this file.](trickle_8h.md)

1

6

7/\*

8 \* Copyright (c) 2016 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_TRICKLE\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_TRICKLE\_H\_

15

16#include <[stdbool.h](stdbool_8h.md)>

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18

19#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

20#include <[zephyr/net/net\_core.h](net__core_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

32

33struct [net\_trickle](structnet__trickle.md);

34

[ 45](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44)typedef void (\*[net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44))(struct [net\_trickle](structnet__trickle.md) \*trickle,

46 bool do\_suppress, void \*[user\_data](structnet__trickle.md#a40f69e10d41e34541ca88c092d6a3341));

47

[ 53](structnet__trickle.md)struct [net\_trickle](structnet__trickle.md) {

[ 54](structnet__trickle.md#aaf14e013a0fa74488a26cd7ff476f6e7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [Imin](structnet__trickle.md#aaf14e013a0fa74488a26cd7ff476f6e7);

[ 55](structnet__trickle.md#a01ffd968b645bb66db67c759520298aa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [Imax](structnet__trickle.md#a01ffd968b645bb66db67c759520298aa);

[ 56](structnet__trickle.md#a7c3399e45f85874cec48434d605066d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [k](structnet__trickle.md#a7c3399e45f85874cec48434d605066d9);

57

[ 58](structnet__trickle.md#a6186d8e41cce5193851587d1c72162ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [I](structnet__trickle.md#a6186d8e41cce5193851587d1c72162ea);

[ 59](structnet__trickle.md#aab8a98c8a918528db6f2ddec85df4796) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [Istart](structnet__trickle.md#aab8a98c8a918528db6f2ddec85df4796);

[ 60](structnet__trickle.md#aaa03f7763e6bd335b932896ee4433b3b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c](structnet__trickle.md#aaa03f7763e6bd335b932896ee4433b3b);

61

[ 62](structnet__trickle.md#ae9f7ecd9b9730cd1c232ead5d21fec05) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [Imax\_abs](structnet__trickle.md#ae9f7ecd9b9730cd1c232ead5d21fec05);

[ 63](structnet__trickle.md#a2a1fb8ad04123ebcb781bc3e0173d8be) bool [double\_to](structnet__trickle.md#a2a1fb8ad04123ebcb781bc3e0173d8be);

64

[ 65](structnet__trickle.md#a2dde5d732f009a85a27ff6fa0c778636) struct [k\_work\_delayable](structk__work__delayable.md) [timer](structnet__trickle.md#a2dde5d732f009a85a27ff6fa0c778636);

[ 66](structnet__trickle.md#a63a3cbf019c99def91e3a9dde7c2f9b4) [net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44) [cb](structnet__trickle.md#a63a3cbf019c99def91e3a9dde7c2f9b4);

[ 67](structnet__trickle.md#a40f69e10d41e34541ca88c092d6a3341) void \*[user\_data](structnet__trickle.md#a40f69e10d41e34541ca88c092d6a3341);

68};

69

71#define NET\_TRICKLE\_INFINITE\_REDUNDANCY 0

73

[ 84](group__trickle.md#gac412d65ad2a8483920de32c1e0ae6be5)int [net\_trickle\_create](group__trickle.md#gac412d65ad2a8483920de32c1e0ae6be5)(struct [net\_trickle](structnet__trickle.md) \*trickle,

85 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) Imin,

86 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) Imax,

87 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k);

88

[ 99](group__trickle.md#ga6674fac118a187320d73dc742f0e216f)int [net\_trickle\_start](group__trickle.md#ga6674fac118a187320d73dc742f0e216f)(struct [net\_trickle](structnet__trickle.md) \*trickle,

100 [net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44) cb,

101 void \*user\_data);

102

[ 110](group__trickle.md#ga8477e45a95abccfb714e3f3369686c6d)int [net\_trickle\_stop](group__trickle.md#ga8477e45a95abccfb714e3f3369686c6d)(struct [net\_trickle](structnet__trickle.md) \*trickle);

111

[ 118](group__trickle.md#gacefb4b5ba518fd1e3f776df012998a9b)void [net\_trickle\_consistency](group__trickle.md#gacefb4b5ba518fd1e3f776df012998a9b)(struct [net\_trickle](structnet__trickle.md) \*trickle);

119

[ 126](group__trickle.md#gad0815f9368a17532c8b5293a122cd8a9)void [net\_trickle\_inconsistency](group__trickle.md#gad0815f9368a17532c8b5293a122cd8a9)(struct [net\_trickle](structnet__trickle.md) \*trickle);

127

[ 135](group__trickle.md#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)static inline bool [net\_trickle\_is\_running](group__trickle.md#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)(struct [net\_trickle](structnet__trickle.md) \*trickle)

136{

137 NET\_ASSERT(trickle);

138

139 return trickle->[I](structnet__trickle.md#a6186d8e41cce5193851587d1c72162ea) != 0U;

140}

141

145

146#ifdef \_\_cplusplus

147}

148#endif

149

150#endif /\* ZEPHYR\_INCLUDE\_NET\_TRICKLE\_H\_ \*/

[net\_trickle\_start](group__trickle.md#ga6674fac118a187320d73dc742f0e216f)

int net\_trickle\_start(struct net\_trickle \*trickle, net\_trickle\_cb\_t cb, void \*user\_data)

Start a Trickle timer.

[net\_trickle\_stop](group__trickle.md#ga8477e45a95abccfb714e3f3369686c6d)

int net\_trickle\_stop(struct net\_trickle \*trickle)

Stop a Trickle timer.

[net\_trickle\_is\_running](group__trickle.md#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)

static bool net\_trickle\_is\_running(struct net\_trickle \*trickle)

Check if the Trickle timer is running or not.

**Definition** trickle.h:135

[net\_trickle\_create](group__trickle.md#gac412d65ad2a8483920de32c1e0ae6be5)

int net\_trickle\_create(struct net\_trickle \*trickle, uint32\_t Imin, uint8\_t Imax, uint8\_t k)

Create a Trickle timer.

[net\_trickle\_consistency](group__trickle.md#gacefb4b5ba518fd1e3f776df012998a9b)

void net\_trickle\_consistency(struct net\_trickle \*trickle)

To be called by the protocol handler when it hears a consistent network transmission.

[net\_trickle\_inconsistency](group__trickle.md#gad0815f9368a17532c8b5293a122cd8a9)

void net\_trickle\_inconsistency(struct net\_trickle \*trickle)

To be called by the protocol handler when it hears an inconsistent network transmission.

[net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44)

void(\* net\_trickle\_cb\_t)(struct net\_trickle \*trickle, bool do\_suppress, void \*user\_data)

Trickle timer callback.

**Definition** trickle.h:45

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[net\_core.h](net__core_8h.md)

Network core definitions.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3889

[net\_trickle](structnet__trickle.md)

The variable names are taken directly from RFC 6206 when applicable.

**Definition** trickle.h:53

[net\_trickle::Imax](structnet__trickle.md#a01ffd968b645bb66db67c759520298aa)

uint8\_t Imax

Max number of doublings.

**Definition** trickle.h:55

[net\_trickle::double\_to](structnet__trickle.md#a2a1fb8ad04123ebcb781bc3e0173d8be)

bool double\_to

**Definition** trickle.h:63

[net\_trickle::timer](structnet__trickle.md#a2dde5d732f009a85a27ff6fa0c778636)

struct k\_work\_delayable timer

**Definition** trickle.h:65

[net\_trickle::user\_data](structnet__trickle.md#a40f69e10d41e34541ca88c092d6a3341)

void \* user\_data

**Definition** trickle.h:67

[net\_trickle::I](structnet__trickle.md#a6186d8e41cce5193851587d1c72162ea)

uint32\_t I

Current interval size.

**Definition** trickle.h:58

[net\_trickle::cb](structnet__trickle.md#a63a3cbf019c99def91e3a9dde7c2f9b4)

net\_trickle\_cb\_t cb

Callback to be called when timer expires.

**Definition** trickle.h:66

[net\_trickle::k](structnet__trickle.md#a7c3399e45f85874cec48434d605066d9)

uint8\_t k

Redundancy constant.

**Definition** trickle.h:56

[net\_trickle::c](structnet__trickle.md#aaa03f7763e6bd335b932896ee4433b3b)

uint8\_t c

Consistency counter.

**Definition** trickle.h:60

[net\_trickle::Istart](structnet__trickle.md#aab8a98c8a918528db6f2ddec85df4796)

uint32\_t Istart

Start of the interval in ms.

**Definition** trickle.h:59

[net\_trickle::Imin](structnet__trickle.md#aaf14e013a0fa74488a26cd7ff476f6e7)

uint32\_t Imin

Min interval size in ms.

**Definition** trickle.h:54

[net\_trickle::Imax\_abs](structnet__trickle.md#ae9f7ecd9b9730cd1c232ead5d21fec05)

uint32\_t Imax\_abs

Max interval size in ms (not doublings).

**Definition** trickle.h:62

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [trickle.h](trickle_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
