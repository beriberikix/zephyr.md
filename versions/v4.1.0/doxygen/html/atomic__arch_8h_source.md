---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/atomic__arch_8h_source.html
original_path: doxygen/html/atomic__arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_arch.h

[Go to the documentation of this file.](atomic__arch_8h.md)

1/\*

2 \* Copyright (c) 2021 Demant A/S

3 \* Copyright (c) 2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_ARCH\_H\_

9#define ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_ARCH\_H\_

10

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[zephyr/sys/atomic\_types.h](atomic__types_8h.md)>

13

14/\* Included from <atomic.h> \*/

15

16/\* Arch specific atomic primitives \*/

17

[ 18](atomic__arch_8h.md#ab879da5aa1ffcc317adc664c016586f7)bool [atomic\_cas](atomic__arch_8h.md#ab879da5aa1ffcc317adc664c016586f7)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value,

19 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value);

20

[ 21](atomic__arch_8h.md#adb8b37f84beeb5c8ab46faa0c7f6cf33)bool [atomic\_ptr\_cas](atomic__arch_8h.md#adb8b37f84beeb5c8ab46faa0c7f6cf33)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, void \*old\_value,

22 void \*new\_value);

23

[ 24](atomic__arch_8h.md#a518c07595daaca29a9e53071ed59c9c0)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_add](atomic__arch_8h.md#a518c07595daaca29a9e53071ed59c9c0)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

25

[ 26](atomic__arch_8h.md#a84ab58fd0a6dbbf1bf675722b5900bd7)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_sub](atomic__arch_8h.md#a84ab58fd0a6dbbf1bf675722b5900bd7)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

27

[ 28](atomic__arch_8h.md#aae47a9cbe5a6534967b417f602b37ac2)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_inc](atomic__arch_8h.md#aae47a9cbe5a6534967b417f602b37ac2)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

29

[ 30](atomic__arch_8h.md#ac260f0efbd970717eae4ac3bb493a0c4)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_dec](atomic__arch_8h.md#ac260f0efbd970717eae4ac3bb493a0c4)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

31

[ 32](atomic__arch_8h.md#a33bb426a17535bd1022895a7e44b32fa)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_get](atomic__arch_8h.md#a33bb426a17535bd1022895a7e44b32fa)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

33

[ 34](atomic__arch_8h.md#a11a456c5b154bed43c4fc8859b5f6547)void \*[atomic\_ptr\_get](atomic__arch_8h.md#a11a456c5b154bed43c4fc8859b5f6547)(const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target);

35

[ 36](atomic__arch_8h.md#a5f0555245d8932c2e7f7e94575e1a095)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_set](atomic__arch_8h.md#a5f0555245d8932c2e7f7e94575e1a095)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

37

[ 38](atomic__arch_8h.md#aaaeac347d3727fee6b85efb289285cb4)void \*[atomic\_ptr\_set](atomic__arch_8h.md#aaaeac347d3727fee6b85efb289285cb4)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, void \*value);

39

[ 40](atomic__arch_8h.md#a879b5f540c25fd09f1b84563e3dc8a91)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_clear](atomic__arch_8h.md#a879b5f540c25fd09f1b84563e3dc8a91)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

41

[ 42](atomic__arch_8h.md#a7dca81028baa3f371ef487d683745762)void \*[atomic\_ptr\_clear](atomic__arch_8h.md#a7dca81028baa3f371ef487d683745762)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target);

43

[ 44](atomic__arch_8h.md#a1564a44a260e7d0d02e30ae045a99764)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_or](atomic__arch_8h.md#a1564a44a260e7d0d02e30ae045a99764)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

45

[ 46](atomic__arch_8h.md#a18592bcf38d667fb9b428f81ea691bd4)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_xor](atomic__arch_8h.md#a18592bcf38d667fb9b428f81ea691bd4)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

47

[ 48](atomic__arch_8h.md#a4bc1f6a6f5d98eef742b4541d235811d)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_and](atomic__arch_8h.md#a4bc1f6a6f5d98eef742b4541d235811d)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

49

[ 50](atomic__arch_8h.md#a3e954286e40de73e45598a00a0a2b864)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_nand](atomic__arch_8h.md#a3e954286e40de73e45598a00a0a2b864)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

51

52

53#endif /\* ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_ARCH\_H\_ \*/

[atomic\_ptr\_get](atomic__arch_8h.md#a11a456c5b154bed43c4fc8859b5f6547)

void \* atomic\_ptr\_get(const atomic\_ptr\_t \*target)

[atomic\_or](atomic__arch_8h.md#a1564a44a260e7d0d02e30ae045a99764)

atomic\_val\_t atomic\_or(atomic\_t \*target, atomic\_val\_t value)

[atomic\_xor](atomic__arch_8h.md#a18592bcf38d667fb9b428f81ea691bd4)

atomic\_val\_t atomic\_xor(atomic\_t \*target, atomic\_val\_t value)

[atomic\_get](atomic__arch_8h.md#a33bb426a17535bd1022895a7e44b32fa)

atomic\_val\_t atomic\_get(const atomic\_t \*target)

[atomic\_nand](atomic__arch_8h.md#a3e954286e40de73e45598a00a0a2b864)

atomic\_val\_t atomic\_nand(atomic\_t \*target, atomic\_val\_t value)

[atomic\_and](atomic__arch_8h.md#a4bc1f6a6f5d98eef742b4541d235811d)

atomic\_val\_t atomic\_and(atomic\_t \*target, atomic\_val\_t value)

[atomic\_add](atomic__arch_8h.md#a518c07595daaca29a9e53071ed59c9c0)

atomic\_val\_t atomic\_add(atomic\_t \*target, atomic\_val\_t value)

[atomic\_set](atomic__arch_8h.md#a5f0555245d8932c2e7f7e94575e1a095)

atomic\_val\_t atomic\_set(atomic\_t \*target, atomic\_val\_t value)

[atomic\_ptr\_clear](atomic__arch_8h.md#a7dca81028baa3f371ef487d683745762)

void \* atomic\_ptr\_clear(atomic\_ptr\_t \*target)

[atomic\_sub](atomic__arch_8h.md#a84ab58fd0a6dbbf1bf675722b5900bd7)

atomic\_val\_t atomic\_sub(atomic\_t \*target, atomic\_val\_t value)

[atomic\_clear](atomic__arch_8h.md#a879b5f540c25fd09f1b84563e3dc8a91)

atomic\_val\_t atomic\_clear(atomic\_t \*target)

[atomic\_ptr\_set](atomic__arch_8h.md#aaaeac347d3727fee6b85efb289285cb4)

void \* atomic\_ptr\_set(atomic\_ptr\_t \*target, void \*value)

[atomic\_inc](atomic__arch_8h.md#aae47a9cbe5a6534967b417f602b37ac2)

atomic\_val\_t atomic\_inc(atomic\_t \*target)

[atomic\_cas](atomic__arch_8h.md#ab879da5aa1ffcc317adc664c016586f7)

bool atomic\_cas(atomic\_t \*target, atomic\_val\_t old\_value, atomic\_val\_t new\_value)

[atomic\_dec](atomic__arch_8h.md#ac260f0efbd970717eae4ac3bb493a0c4)

atomic\_val\_t atomic\_dec(atomic\_t \*target)

[atomic\_ptr\_cas](atomic__arch_8h.md#adb8b37f84beeb5c8ab46faa0c7f6cf33)

bool atomic\_ptr\_cas(atomic\_ptr\_t \*target, void \*old\_value, void \*new\_value)

[atomic\_types.h](atomic__types_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)

atomic\_t atomic\_val\_t

**Definition** atomic\_types.h:16

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [atomic\_arch.h](atomic__arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
