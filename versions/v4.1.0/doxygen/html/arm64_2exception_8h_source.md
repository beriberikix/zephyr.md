---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm64_2exception_8h_source.html
original_path: doxygen/html/arm64_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](arm64_2exception_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_EXCEPTION\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_EXCEPTION\_H\_

16

17/\* for assembler, only works with constants \*/

18

19#ifdef \_ASMLANGUAGE

20#else

21#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27struct [arch\_esf](structarch__esf.md) {

[ 28](structarch__esf.md#a2eac86aa1bfe72c5382555ac7c4da87a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x0](structarch__esf.md#a2eac86aa1bfe72c5382555ac7c4da87a);

[ 29](structarch__esf.md#a0306fa0bf609c4b555c94e7c0b261389) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x1](structarch__esf.md#a0306fa0bf609c4b555c94e7c0b261389);

[ 30](structarch__esf.md#a7673457760d24a5d3559642ac89fc815) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x2](structarch__esf.md#a7673457760d24a5d3559642ac89fc815);

[ 31](structarch__esf.md#a6b194085ef2a4649361f86c78070061a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x3](structarch__esf.md#a6b194085ef2a4649361f86c78070061a);

[ 32](structarch__esf.md#a69fe42719d302c62ba05c08c8548451a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x4](structarch__esf.md#a69fe42719d302c62ba05c08c8548451a);

[ 33](structarch__esf.md#a565c8f1b98b8bb4920ed54447559bbe7) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x5](structarch__esf.md#a565c8f1b98b8bb4920ed54447559bbe7);

[ 34](structarch__esf.md#af3b381fa07e8cc809422f759e03e526b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x6](structarch__esf.md#af3b381fa07e8cc809422f759e03e526b);

[ 35](structarch__esf.md#a8c7d66e7eb8a30e76c588ac07c242446) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x7](structarch__esf.md#a8c7d66e7eb8a30e76c588ac07c242446);

[ 36](structarch__esf.md#ad38f2f48dedc67706db4a78a6c16a74a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x8](structarch__esf.md#ad38f2f48dedc67706db4a78a6c16a74a);

[ 37](structarch__esf.md#af84d11e6ca50633cd6a1449df29f9853) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x9](structarch__esf.md#af84d11e6ca50633cd6a1449df29f9853);

[ 38](structarch__esf.md#aeeb737c86d1e14ebe89d908586b21213) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x10](structarch__esf.md#aeeb737c86d1e14ebe89d908586b21213);

[ 39](structarch__esf.md#a041472053798550ecc0ed1641aad0a36) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x11](structarch__esf.md#a041472053798550ecc0ed1641aad0a36);

[ 40](structarch__esf.md#afe82dc7299245360c215d874ab6e4fc5) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x12](structarch__esf.md#afe82dc7299245360c215d874ab6e4fc5);

[ 41](structarch__esf.md#aa7a17c78c884e3e76ac20efce28cc07b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x13](structarch__esf.md#aa7a17c78c884e3e76ac20efce28cc07b);

[ 42](structarch__esf.md#a6d1deb8481db2cb4b16a4227eeb7156b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x14](structarch__esf.md#a6d1deb8481db2cb4b16a4227eeb7156b);

[ 43](structarch__esf.md#a9e244148142ac2ddced13d6f4adad723) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x15](structarch__esf.md#a9e244148142ac2ddced13d6f4adad723);

[ 44](structarch__esf.md#ad14eaf73e5ef14e5e47bed09ddd8fae8) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x16](structarch__esf.md#ad14eaf73e5ef14e5e47bed09ddd8fae8);

[ 45](structarch__esf.md#aa8e0bd15d3fae88ef7afa2e122b23287) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x17](structarch__esf.md#aa8e0bd15d3fae88ef7afa2e122b23287);

[ 46](structarch__esf.md#a29dbefef813eba8c1cb9e8d97ddff060) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [x18](structarch__esf.md#a29dbefef813eba8c1cb9e8d97ddff060);

[ 47](structarch__esf.md#ad9047b114956222cd07503fe9339b43d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [lr](structarch__esf.md#ad9047b114956222cd07503fe9339b43d);

[ 48](structarch__esf.md#ae587b84ee192f1b4f3bc3649b9358931) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [spsr](structarch__esf.md#ae587b84ee192f1b4f3bc3649b9358931);

[ 49](structarch__esf.md#a28e161a6b7203eb0abe91c1970a9bd89) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elr](structarch__esf.md#a28e161a6b7203eb0abe91c1970a9bd89);

50#ifdef CONFIG\_FRAME\_POINTER

51 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) fp;

52#endif

53#ifdef CONFIG\_ARM64\_SAFE\_EXCEPTION\_STACK

54 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sp](structarch__esf.md#a9c3e060a48caeb59d2625e921f1f6d15);

55#endif

56} \_\_aligned(16);

57

58#ifdef \_\_cplusplus

59}

60#endif

61

62#endif /\* \_ASMLANGUAGE \*/

63

64#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_EXCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::x1](structarch__esf.md#a0306fa0bf609c4b555c94e7c0b261389)

uint64\_t x1

**Definition** exception.h:29

[arch\_esf::x11](structarch__esf.md#a041472053798550ecc0ed1641aad0a36)

uint64\_t x11

**Definition** exception.h:39

[arch\_esf::elr](structarch__esf.md#a28e161a6b7203eb0abe91c1970a9bd89)

uint64\_t elr

**Definition** exception.h:49

[arch\_esf::x18](structarch__esf.md#a29dbefef813eba8c1cb9e8d97ddff060)

uint64\_t x18

**Definition** exception.h:46

[arch\_esf::x0](structarch__esf.md#a2eac86aa1bfe72c5382555ac7c4da87a)

uint64\_t x0

**Definition** exception.h:28

[arch\_esf::x5](structarch__esf.md#a565c8f1b98b8bb4920ed54447559bbe7)

uint64\_t x5

**Definition** exception.h:33

[arch\_esf::x4](structarch__esf.md#a69fe42719d302c62ba05c08c8548451a)

uint64\_t x4

**Definition** exception.h:32

[arch\_esf::x3](structarch__esf.md#a6b194085ef2a4649361f86c78070061a)

uint64\_t x3

**Definition** exception.h:31

[arch\_esf::x14](structarch__esf.md#a6d1deb8481db2cb4b16a4227eeb7156b)

uint64\_t x14

**Definition** exception.h:42

[arch\_esf::x2](structarch__esf.md#a7673457760d24a5d3559642ac89fc815)

uint64\_t x2

**Definition** exception.h:30

[arch\_esf::x7](structarch__esf.md#a8c7d66e7eb8a30e76c588ac07c242446)

uint64\_t x7

**Definition** exception.h:35

[arch\_esf::sp](structarch__esf.md#a9c3e060a48caeb59d2625e921f1f6d15)

unsigned long sp

**Definition** exception.h:91

[arch\_esf::x15](structarch__esf.md#a9e244148142ac2ddced13d6f4adad723)

uint64\_t x15

**Definition** exception.h:43

[arch\_esf::x13](structarch__esf.md#aa7a17c78c884e3e76ac20efce28cc07b)

uint64\_t x13

**Definition** exception.h:41

[arch\_esf::x17](structarch__esf.md#aa8e0bd15d3fae88ef7afa2e122b23287)

uint64\_t x17

**Definition** exception.h:45

[arch\_esf::x16](structarch__esf.md#ad14eaf73e5ef14e5e47bed09ddd8fae8)

uint64\_t x16

**Definition** exception.h:44

[arch\_esf::x8](structarch__esf.md#ad38f2f48dedc67706db4a78a6c16a74a)

uint64\_t x8

**Definition** exception.h:36

[arch\_esf::lr](structarch__esf.md#ad9047b114956222cd07503fe9339b43d)

uint64\_t lr

**Definition** exception.h:47

[arch\_esf::spsr](structarch__esf.md#ae587b84ee192f1b4f3bc3649b9358931)

uint64\_t spsr

**Definition** exception.h:48

[arch\_esf::x10](structarch__esf.md#aeeb737c86d1e14ebe89d908586b21213)

uint64\_t x10

**Definition** exception.h:38

[arch\_esf::x6](structarch__esf.md#af3b381fa07e8cc809422f759e03e526b)

uint64\_t x6

**Definition** exception.h:34

[arch\_esf::x9](structarch__esf.md#af84d11e6ca50633cd6a1449df29f9853)

uint64\_t x9

**Definition** exception.h:37

[arch\_esf::x12](structarch__esf.md#afe82dc7299245360c215d874ab6e4fc5)

uint64\_t x12

**Definition** exception.h:40

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [exception.h](arm64_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
