---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nios2_2exception_8h_source.html
original_path: doxygen/html/nios2_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](nios2_2exception_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_EXPCEPTION\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_EXPCEPTION\_H\_

9

10#ifndef \_ASMLANGUAGE

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17struct [arch\_esf](structarch__esf.md) {

[ 18](structarch__esf.md#af925780dd5a600bcc9741aa588ae3c32) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ra](structarch__esf.md#a22241917474aaf5718780c55c65be33f); /\* return address r31 \*/

[ 19](structarch__esf.md#a74f77230b78880d1aca123886d7786af) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r1](structarch__esf.md#a74f77230b78880d1aca123886d7786af); /\* at \*/

[ 20](structarch__esf.md#a53a4e45913aba2541648c0be71f53e67) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r2](structarch__esf.md#a53a4e45913aba2541648c0be71f53e67); /\* return value \*/

[ 21](structarch__esf.md#a613182d7fc3c3ed0f5680fa382eee82b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r3](structarch__esf.md#a613182d7fc3c3ed0f5680fa382eee82b); /\* return value \*/

[ 22](structarch__esf.md#a247b2b132e00b25c58770323da69e5f1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r4](structarch__esf.md#a247b2b132e00b25c58770323da69e5f1); /\* register args \*/

[ 23](structarch__esf.md#accb4010250c2c4abedb4b7877878915e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r5](structarch__esf.md#accb4010250c2c4abedb4b7877878915e); /\* register args \*/

[ 24](structarch__esf.md#a47c73f90f7d944cd1c8463c7dd4a5fcf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r6](structarch__esf.md#a47c73f90f7d944cd1c8463c7dd4a5fcf); /\* register args \*/

[ 25](structarch__esf.md#a8e1a7067a6c8046ba7d190812582441a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r7](structarch__esf.md#a8e1a7067a6c8046ba7d190812582441a); /\* register args \*/

[ 26](structarch__esf.md#a3db521d02db9c611954ea76718e3ee99) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r8](structarch__esf.md#a3db521d02db9c611954ea76718e3ee99); /\* Caller-saved general purpose \*/

[ 27](structarch__esf.md#a9887069365ebcd852ab8d78c19854927) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r9](structarch__esf.md#a9887069365ebcd852ab8d78c19854927); /\* Caller-saved general purpose \*/

[ 28](structarch__esf.md#a44ea57b6f2ae62b30809394843076290) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r10](structarch__esf.md#a44ea57b6f2ae62b30809394843076290); /\* Caller-saved general purpose \*/

[ 29](structarch__esf.md#a2f561242c8a2415ec7de7848ee946677) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r11](structarch__esf.md#a2f561242c8a2415ec7de7848ee946677); /\* Caller-saved general purpose \*/

[ 30](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r12](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229); /\* Caller-saved general purpose \*/

[ 31](structarch__esf.md#a252de1dd78f9ea00aeae7c8cbe7280ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r13](structarch__esf.md#a252de1dd78f9ea00aeae7c8cbe7280ef); /\* Caller-saved general purpose \*/

[ 32](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r14](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca); /\* Caller-saved general purpose \*/

[ 33](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r15](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a); /\* Caller-saved general purpose \*/

[ 34](structarch__esf.md#abe51f26556e845597e495628ed653ca0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [estatus](structarch__esf.md#abe51f26556e845597e495628ed653ca0);

[ 35](structarch__esf.md#ac79618cfb2d8d57f995b29ef81ff7f60) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [instr](structarch__esf.md#ac79618cfb2d8d57f995b29ef81ff7f60); /\* Instruction being executed when exc occurred \*/

36};

37

38#ifdef \_\_cplusplus

39}

40#endif

41

42#endif /\* \_ASMLANGUAGE \*/

43

44#endif /\* ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_EXPCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::ra](structarch__esf.md#a22241917474aaf5718780c55c65be33f)

unsigned long ra

**Definition** exception.h:21

[arch\_esf::r4](structarch__esf.md#a247b2b132e00b25c58770323da69e5f1)

uint32\_t r4

**Definition** exception.h:22

[arch\_esf::r13](structarch__esf.md#a252de1dd78f9ea00aeae7c8cbe7280ef)

uint32\_t r13

**Definition** exception.h:31

[arch\_esf::r11](structarch__esf.md#a2f561242c8a2415ec7de7848ee946677)

uint32\_t r11

**Definition** exception.h:29

[arch\_esf::r8](structarch__esf.md#a3db521d02db9c611954ea76718e3ee99)

uint32\_t r8

**Definition** exception.h:26

[arch\_esf::r10](structarch__esf.md#a44ea57b6f2ae62b30809394843076290)

uint32\_t r10

**Definition** exception.h:28

[arch\_esf::r6](structarch__esf.md#a47c73f90f7d944cd1c8463c7dd4a5fcf)

uint32\_t r6

**Definition** exception.h:24

[arch\_esf::r2](structarch__esf.md#a53a4e45913aba2541648c0be71f53e67)

uint32\_t r2

**Definition** exception.h:20

[arch\_esf::r3](structarch__esf.md#a613182d7fc3c3ed0f5680fa382eee82b)

uint32\_t r3

**Definition** exception.h:21

[arch\_esf::r1](structarch__esf.md#a74f77230b78880d1aca123886d7786af)

uint32\_t r1

**Definition** exception.h:19

[arch\_esf::r15](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a)

uint32\_t r15

**Definition** exception.h:33

[arch\_esf::r7](structarch__esf.md#a8e1a7067a6c8046ba7d190812582441a)

uint32\_t r7

**Definition** exception.h:25

[arch\_esf::r9](structarch__esf.md#a9887069365ebcd852ab8d78c19854927)

uint32\_t r9

**Definition** exception.h:27

[arch\_esf::r12](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229)

uint32\_t r12

**Definition** exception.h:30

[arch\_esf::estatus](structarch__esf.md#abe51f26556e845597e495628ed653ca0)

uint32\_t estatus

**Definition** exception.h:34

[arch\_esf::instr](structarch__esf.md#ac79618cfb2d8d57f995b29ef81ff7f60)

uint32\_t instr

**Definition** exception.h:35

[arch\_esf::r5](structarch__esf.md#accb4010250c2c4abedb4b7877878915e)

uint32\_t r5

**Definition** exception.h:23

[arch\_esf::r14](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca)

uint32\_t r14

**Definition** exception.h:32

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [nios2](dir_bcfa142ae77c1ee311b7ef8e30037d11.md)
- [exception.h](nios2_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
