---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/rx_2exception_8h_source.html
original_path: doxygen/html/rx_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](rx_2exception_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_RX\_INLINES\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_RX\_INLINES\_H\_

9

10#ifndef \_ASMLANGUAGE

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17struct [arch\_esf](structarch__esf.md) {

[ 18](structarch__esf.md#afd1d67ce9a72a03ec1f2024b0128d317) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [acc\_l](structarch__esf.md#afd1d67ce9a72a03ec1f2024b0128d317);

[ 19](structarch__esf.md#a3ec04f7de3b0fe032d4da49f99fe2163) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [acc\_h](structarch__esf.md#a3ec04f7de3b0fe032d4da49f99fe2163);

[ 20](structarch__esf.md#a74f77230b78880d1aca123886d7786af) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r1](structarch__esf.md#a74f77230b78880d1aca123886d7786af);

[ 21](structarch__esf.md#a53a4e45913aba2541648c0be71f53e67) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r2](structarch__esf.md#a53a4e45913aba2541648c0be71f53e67);

[ 22](structarch__esf.md#a613182d7fc3c3ed0f5680fa382eee82b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r3](structarch__esf.md#a613182d7fc3c3ed0f5680fa382eee82b);

[ 23](structarch__esf.md#a247b2b132e00b25c58770323da69e5f1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r4](structarch__esf.md#a247b2b132e00b25c58770323da69e5f1);

[ 24](structarch__esf.md#accb4010250c2c4abedb4b7877878915e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r5](structarch__esf.md#accb4010250c2c4abedb4b7877878915e);

[ 25](structarch__esf.md#a47c73f90f7d944cd1c8463c7dd4a5fcf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r6](structarch__esf.md#a47c73f90f7d944cd1c8463c7dd4a5fcf);

[ 26](structarch__esf.md#a8e1a7067a6c8046ba7d190812582441a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r7](structarch__esf.md#a8e1a7067a6c8046ba7d190812582441a);

[ 27](structarch__esf.md#a3db521d02db9c611954ea76718e3ee99) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r8](structarch__esf.md#a3db521d02db9c611954ea76718e3ee99);

[ 28](structarch__esf.md#a9887069365ebcd852ab8d78c19854927) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r9](structarch__esf.md#a9887069365ebcd852ab8d78c19854927);

[ 29](structarch__esf.md#a44ea57b6f2ae62b30809394843076290) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r10](structarch__esf.md#a44ea57b6f2ae62b30809394843076290);

[ 30](structarch__esf.md#a2f561242c8a2415ec7de7848ee946677) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r11](structarch__esf.md#a2f561242c8a2415ec7de7848ee946677);

[ 31](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r12](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229);

[ 32](structarch__esf.md#a252de1dd78f9ea00aeae7c8cbe7280ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r13](structarch__esf.md#a252de1dd78f9ea00aeae7c8cbe7280ef);

[ 33](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r14](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca);

[ 34](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r15](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a);

[ 35](structarch__esf.md#a1e092149349ca5b53ec687ed602da3bc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [entry\_point](structarch__esf.md#a1e092149349ca5b53ec687ed602da3bc);

[ 36](structarch__esf.md#ae35f1f7175cdfbc5a5051955530b5df7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [psw](structarch__esf.md#ae35f1f7175cdfbc5a5051955530b5df7);

37};

38

39#ifdef \_\_cplusplus

40}

41#endif

42

43#endif /\* \_ASMLANGUAGE \*/

44

45#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RX\_INLINES\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::entry\_point](structarch__esf.md#a1e092149349ca5b53ec687ed602da3bc)

uint32\_t entry\_point

**Definition** exception.h:35

[arch\_esf::r4](structarch__esf.md#a247b2b132e00b25c58770323da69e5f1)

uint32\_t r4

**Definition** exception.h:23

[arch\_esf::r13](structarch__esf.md#a252de1dd78f9ea00aeae7c8cbe7280ef)

uint32\_t r13

**Definition** exception.h:32

[arch\_esf::r11](structarch__esf.md#a2f561242c8a2415ec7de7848ee946677)

uint32\_t r11

**Definition** exception.h:30

[arch\_esf::r8](structarch__esf.md#a3db521d02db9c611954ea76718e3ee99)

uint32\_t r8

**Definition** exception.h:27

[arch\_esf::acc\_h](structarch__esf.md#a3ec04f7de3b0fe032d4da49f99fe2163)

uint32\_t acc\_h

**Definition** exception.h:19

[arch\_esf::r10](structarch__esf.md#a44ea57b6f2ae62b30809394843076290)

uint32\_t r10

**Definition** exception.h:29

[arch\_esf::r6](structarch__esf.md#a47c73f90f7d944cd1c8463c7dd4a5fcf)

uint32\_t r6

**Definition** exception.h:25

[arch\_esf::r2](structarch__esf.md#a53a4e45913aba2541648c0be71f53e67)

uint32\_t r2

**Definition** exception.h:21

[arch\_esf::r3](structarch__esf.md#a613182d7fc3c3ed0f5680fa382eee82b)

uint32\_t r3

**Definition** exception.h:22

[arch\_esf::r1](structarch__esf.md#a74f77230b78880d1aca123886d7786af)

uint32\_t r1

**Definition** exception.h:20

[arch\_esf::r15](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a)

uint32\_t r15

**Definition** exception.h:34

[arch\_esf::r7](structarch__esf.md#a8e1a7067a6c8046ba7d190812582441a)

uint32\_t r7

**Definition** exception.h:26

[arch\_esf::r9](structarch__esf.md#a9887069365ebcd852ab8d78c19854927)

uint32\_t r9

**Definition** exception.h:28

[arch\_esf::r12](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229)

uint32\_t r12

**Definition** exception.h:31

[arch\_esf::r5](structarch__esf.md#accb4010250c2c4abedb4b7877878915e)

uint32\_t r5

**Definition** exception.h:24

[arch\_esf::psw](structarch__esf.md#ae35f1f7175cdfbc5a5051955530b5df7)

uint32\_t psw

**Definition** exception.h:36

[arch\_esf::r14](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca)

uint32\_t r14

**Definition** exception.h:33

[arch\_esf::acc\_l](structarch__esf.md#afd1d67ce9a72a03ec1f2024b0128d317)

uint32\_t acc\_l

**Definition** exception.h:18

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [rx](dir_eb52b7f9d95392aedf108916f743bdaf.md)
- [exception.h](rx_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
