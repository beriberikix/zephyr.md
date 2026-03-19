---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arc_2v2_2exception_8h_source.html
original_path: doxygen/html/arc_2v2_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](arc_2v2_2exception_8h.md)

1/\*

2 \* Copyright (c) 2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_EXCEPTION\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_EXCEPTION\_H\_

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21#ifdef \_\_cplusplus

22}

23#endif

24

25/\* ARCv2 Exception vector numbers \*/

[ 26](arc_2v2_2exception_8h.md#a2f8e6622ee49d9a5eed7f15288e7d8ae)#define ARC\_EV\_RESET 0x0

[ 27](arc_2v2_2exception_8h.md#a79e227883063d92c0d47cc750c37eb86)#define ARC\_EV\_MEM\_ERROR 0x1

[ 28](arc_2v2_2exception_8h.md#a57a4267b70061307f2fed74473e17015)#define ARC\_EV\_INS\_ERROR 0x2

[ 29](arc_2v2_2exception_8h.md#a10e5ab692a8dcb6bc6bb849222e12940)#define ARC\_EV\_MACHINE\_CHECK 0x3

[ 30](arc_2v2_2exception_8h.md#af2d95f9ded1396dd2c0aa7cb41952033)#define ARC\_EV\_TLB\_MISS\_I 0x4

[ 31](arc_2v2_2exception_8h.md#a48c63c54328299dfa3bec2b71c4ab610)#define ARC\_EV\_TLB\_MISS\_D 0x5

[ 32](arc_2v2_2exception_8h.md#ad42a3dc7f1f4f4da9978ce667ae1ec2f)#define ARC\_EV\_PROT\_V 0x6

[ 33](arc_2v2_2exception_8h.md#a604874d6ae9f845175e425bc897751f8)#define ARC\_EV\_PRIVILEGE\_V 0x7

[ 34](arc_2v2_2exception_8h.md#a42b3a14ded2c98e7e37a7375efd81e91)#define ARC\_EV\_SWI 0x8

[ 35](arc_2v2_2exception_8h.md#abd2003e15eb7839a2454c9da245ee56b)#define ARC\_EV\_TRAP 0x9

[ 36](arc_2v2_2exception_8h.md#ab6d6036ccdf6dc66959ca3ac90aa6cde)#define ARC\_EV\_EXTENSION 0xA

[ 37](arc_2v2_2exception_8h.md#a0c132bd763cf093dd7f87318607977fa)#define ARC\_EV\_DIV\_ZERO 0xB

[ 38](arc_2v2_2exception_8h.md#aca9e2d443855714d67aa0001affd2c4a)#define ARC\_EV\_DC\_ERROR 0xC

[ 39](arc_2v2_2exception_8h.md#a2b2768d051be571940d8f0ca5acc8ddf)#define ARC\_EV\_MISALIGNED 0xD

[ 40](arc_2v2_2exception_8h.md#a777a56039909a5634ad59c04cf240104)#define ARC\_EV\_VEC\_UNIT 0xE

41

42#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_EXCEPTION\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [exception.h](arc_2v2_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
