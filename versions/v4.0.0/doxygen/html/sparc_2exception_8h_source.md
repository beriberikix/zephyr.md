---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sparc_2exception_8h_source.html
original_path: doxygen/html/sparc_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](sparc_2exception_8h.md)

1/\*

2 \* Copyright (c) 2019-2020 Cobham Gaisler AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_SPARC\_EXPCEPTION\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_SPARC\_EXPCEPTION\_H\_

9

10#ifndef \_ASMLANGUAGE

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17struct [arch\_esf](structarch__esf.md) {

[ 18](structarch__esf.md#a25d416d377e446b577945a71ff0cd02a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [out](structarch__esf.md#a25d416d377e446b577945a71ff0cd02a)[8];

[ 19](structarch__esf.md#a29a4fe6ed5b2f8c892f0378be0babd78) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [global](structarch__esf.md#a29a4fe6ed5b2f8c892f0378be0babd78)[8];

[ 20](structarch__esf.md#ae0487ae046fbd1544bd04bf8fab1a300) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [psr](structarch__esf.md#ae0487ae046fbd1544bd04bf8fab1a300);

[ 21](structarch__esf.md#a5547d9c022e6c4a6492df49f11f21493) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pc](structarch__esf.md#a5547d9c022e6c4a6492df49f11f21493);

[ 22](structarch__esf.md#a0d5ee2c404dc3322ae7c0350d5d6e02f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [npc](structarch__esf.md#a0d5ee2c404dc3322ae7c0350d5d6e02f);

[ 23](structarch__esf.md#abcb68c0ffad3c9d44c353b7d6cdb1a50) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wim](structarch__esf.md#abcb68c0ffad3c9d44c353b7d6cdb1a50);

[ 24](structarch__esf.md#a07426991d80b58a64b1fed1d00c88e8f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tbr](structarch__esf.md#a07426991d80b58a64b1fed1d00c88e8f);

[ 25](structarch__esf.md#aacb0e92d3b12a154085994040402103e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [y](structarch__esf.md#aacb0e92d3b12a154085994040402103e);

26};

27

28#ifdef \_\_cplusplus

29}

30#endif

31

32#endif /\* \_ASMLANGUAGE \*/

33

34#endif /\* ZEPHYR\_INCLUDE\_ARCH\_SPARC\_EXPCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::tbr](structarch__esf.md#a07426991d80b58a64b1fed1d00c88e8f)

uint32\_t tbr

**Definition** exception.h:24

[arch\_esf::npc](structarch__esf.md#a0d5ee2c404dc3322ae7c0350d5d6e02f)

uint32\_t npc

**Definition** exception.h:22

[arch\_esf::out](structarch__esf.md#a25d416d377e446b577945a71ff0cd02a)

uint32\_t out[8]

**Definition** exception.h:18

[arch\_esf::global](structarch__esf.md#a29a4fe6ed5b2f8c892f0378be0babd78)

uint32\_t global[8]

**Definition** exception.h:19

[arch\_esf::pc](structarch__esf.md#a5547d9c022e6c4a6492df49f11f21493)

uint32\_t pc

**Definition** exception.h:21

[arch\_esf::y](structarch__esf.md#aacb0e92d3b12a154085994040402103e)

uint32\_t y

**Definition** exception.h:25

[arch\_esf::wim](structarch__esf.md#abcb68c0ffad3c9d44c353b7d6cdb1a50)

uint32\_t wim

**Definition** exception.h:23

[arch\_esf::psr](structarch__esf.md#ae0487ae046fbd1544bd04bf8fab1a300)

uint32\_t psr

**Definition** exception.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [sparc](dir_0b6b538994b3c7630127059eac21a61b.md)
- [exception.h](sparc_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
