---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/trickle_8h_source.html
original_path: doxygen/html/trickle_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

19#include <[zephyr/kernel.h](kernel_8h.md)>

20#include <[zephyr/net/net\_core.h](net__core_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

34

35struct [net\_trickle](structnet__trickle.md);

36

[ 47](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44)typedef void (\*[net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44))(struct [net\_trickle](structnet__trickle.md) \*trickle,

48 bool do\_suppress, void \*[user\_data](structnet__trickle.md#a40f69e10d41e34541ca88c092d6a3341));

49

[ 55](structnet__trickle.md)struct [net\_trickle](structnet__trickle.md) {

[ 56](structnet__trickle.md#a6186d8e41cce5193851587d1c72162ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [I](structnet__trickle.md#a6186d8e41cce5193851587d1c72162ea);

[ 57](structnet__trickle.md#aaf14e013a0fa74488a26cd7ff476f6e7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [Imin](structnet__trickle.md#aaf14e013a0fa74488a26cd7ff476f6e7);

[ 58](structnet__trickle.md#aab8a98c8a918528db6f2ddec85df4796) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [Istart](structnet__trickle.md#aab8a98c8a918528db6f2ddec85df4796);

[ 59](structnet__trickle.md#ae9f7ecd9b9730cd1c232ead5d21fec05) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [Imax\_abs](structnet__trickle.md#ae9f7ecd9b9730cd1c232ead5d21fec05);

[ 60](structnet__trickle.md#a01ffd968b645bb66db67c759520298aa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [Imax](structnet__trickle.md#a01ffd968b645bb66db67c759520298aa);

61

[ 62](structnet__trickle.md#a7c3399e45f85874cec48434d605066d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [k](structnet__trickle.md#a7c3399e45f85874cec48434d605066d9);

[ 63](structnet__trickle.md#aaa03f7763e6bd335b932896ee4433b3b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c](structnet__trickle.md#aaa03f7763e6bd335b932896ee4433b3b);

64

[ 65](structnet__trickle.md#a2a1fb8ad04123ebcb781bc3e0173d8be) bool [double\_to](structnet__trickle.md#a2a1fb8ad04123ebcb781bc3e0173d8be);

66

[ 67](structnet__trickle.md#a2dde5d732f009a85a27ff6fa0c778636) struct [k\_work\_delayable](structk__work__delayable.md) [timer](structnet__trickle.md#a2dde5d732f009a85a27ff6fa0c778636);

[ 68](structnet__trickle.md#a63a3cbf019c99def91e3a9dde7c2f9b4) [net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44) [cb](structnet__trickle.md#a63a3cbf019c99def91e3a9dde7c2f9b4);

[ 69](structnet__trickle.md#a40f69e10d41e34541ca88c092d6a3341) void \*[user\_data](structnet__trickle.md#a40f69e10d41e34541ca88c092d6a3341);

70};

71

73#define NET\_TRICKLE\_INFINITE\_REDUNDANCY 0

75

[ 86](group__trickle.md#gac412d65ad2a8483920de32c1e0ae6be5)int [net\_trickle\_create](group__trickle.md#gac412d65ad2a8483920de32c1e0ae6be5)(struct [net\_trickle](structnet__trickle.md) \*trickle,

87 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) Imin,

88 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) Imax,

89 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k);

90

[ 101](group__trickle.md#ga6674fac118a187320d73dc742f0e216f)int [net\_trickle\_start](group__trickle.md#ga6674fac118a187320d73dc742f0e216f)(struct [net\_trickle](structnet__trickle.md) \*trickle,

102 [net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44) cb,

103 void \*user\_data);

104

[ 112](group__trickle.md#ga8477e45a95abccfb714e3f3369686c6d)int [net\_trickle\_stop](group__trickle.md#ga8477e45a95abccfb714e3f3369686c6d)(struct [net\_trickle](structnet__trickle.md) \*trickle);

113

[ 120](group__trickle.md#gacefb4b5ba518fd1e3f776df012998a9b)void [net\_trickle\_consistency](group__trickle.md#gacefb4b5ba518fd1e3f776df012998a9b)(struct [net\_trickle](structnet__trickle.md) \*trickle);

121

[ 128](group__trickle.md#gad0815f9368a17532c8b5293a122cd8a9)void [net\_trickle\_inconsistency](group__trickle.md#gad0815f9368a17532c8b5293a122cd8a9)(struct [net\_trickle](structnet__trickle.md) \*trickle);

129

[ 137](group__trickle.md#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)static inline bool [net\_trickle\_is\_running](group__trickle.md#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)(struct [net\_trickle](structnet__trickle.md) \*trickle)

138{

139 NET\_ASSERT(trickle);

140

141 return trickle->[I](structnet__trickle.md#a6186d8e41cce5193851587d1c72162ea) != 0U;

142}

143

147

148#ifdef \_\_cplusplus

149}

150#endif

151

152#endif /\* ZEPHYR\_INCLUDE\_NET\_TRICKLE\_H\_ \*/

[net\_trickle\_start](group__trickle.md#ga6674fac118a187320d73dc742f0e216f)

int net\_trickle\_start(struct net\_trickle \*trickle, net\_trickle\_cb\_t cb, void \*user\_data)

Start a Trickle timer.

[net\_trickle\_stop](group__trickle.md#ga8477e45a95abccfb714e3f3369686c6d)

int net\_trickle\_stop(struct net\_trickle \*trickle)

Stop a Trickle timer.

[net\_trickle\_is\_running](group__trickle.md#ga95ceb01a7d56ce5a9d9128a42e1f8eb9)

static bool net\_trickle\_is\_running(struct net\_trickle \*trickle)

Check if the Trickle timer is running or not.

**Definition** trickle.h:137

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

**Definition** trickle.h:47

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

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

**Definition** kernel.h:3985

[net\_trickle](structnet__trickle.md)

The variable names are taken directly from RFC 6206 when applicable.

**Definition** trickle.h:55

[net\_trickle::Imax](structnet__trickle.md#a01ffd968b645bb66db67c759520298aa)

uint8\_t Imax

Max number of doublings.

**Definition** trickle.h:60

[net\_trickle::double\_to](structnet__trickle.md#a2a1fb8ad04123ebcb781bc3e0173d8be)

bool double\_to

Flag telling if the internval is doubled.

**Definition** trickle.h:65

[net\_trickle::timer](structnet__trickle.md#a2dde5d732f009a85a27ff6fa0c778636)

struct k\_work\_delayable timer

Internal timer struct.

**Definition** trickle.h:67

[net\_trickle::user\_data](structnet__trickle.md#a40f69e10d41e34541ca88c092d6a3341)

void \* user\_data

User specific opaque data.

**Definition** trickle.h:69

[net\_trickle::I](structnet__trickle.md#a6186d8e41cce5193851587d1c72162ea)

uint32\_t I

Current interval size.

**Definition** trickle.h:56

[net\_trickle::cb](structnet__trickle.md#a63a3cbf019c99def91e3a9dde7c2f9b4)

net\_trickle\_cb\_t cb

Callback to be called when timer expires.

**Definition** trickle.h:68

[net\_trickle::k](structnet__trickle.md#a7c3399e45f85874cec48434d605066d9)

uint8\_t k

Redundancy constant.

**Definition** trickle.h:62

[net\_trickle::c](structnet__trickle.md#aaa03f7763e6bd335b932896ee4433b3b)

uint8\_t c

Consistency counter.

**Definition** trickle.h:63

[net\_trickle::Istart](structnet__trickle.md#aab8a98c8a918528db6f2ddec85df4796)

uint32\_t Istart

Start of the interval in ms.

**Definition** trickle.h:58

[net\_trickle::Imin](structnet__trickle.md#aaf14e013a0fa74488a26cd7ff476f6e7)

uint32\_t Imin

Min interval size in ms.

**Definition** trickle.h:57

[net\_trickle::Imax\_abs](structnet__trickle.md#ae9f7ecd9b9730cd1c232ead5d21fec05)

uint32\_t Imax\_abs

Max interval size in ms (not doublings).

**Definition** trickle.h:59

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [trickle.h](trickle_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
