---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sparc_8h_source.html
original_path: doxygen/html/sparc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sparc.h

[Go to the documentation of this file.](sparc_8h.md)

1/\*

2 \* Copyright (c) 2019-2020 Cobham Gaisler AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_SPARC\_SPARC\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_SPARC\_SPARC\_H\_

9

10/\*

11 \* @file

12 \* @brief Definitions for the SPARC V8 architecture.

13 \*/

14

15/\* Processor State Register \*/

[ 16](sparc_8h.md#a3b6b8aa082ab1ef6344a85bdc761025c)#define PSR\_VER\_BIT 24

[ 17](sparc_8h.md#a5ee580d14f9c267d76dc0906fa0f6f69)#define PSR\_PIL\_BIT 8

18

[ 19](sparc_8h.md#a6244f06da2bcc9c79499b354055c400e)#define PSR\_VER (0xf << PSR\_VER\_BIT)

[ 20](sparc_8h.md#a49e2f0d06eb855c6797e2009736eac09)#define PSR\_EF (1 << 12)

[ 21](sparc_8h.md#adbf732343370fc1685ba4176db1db6bb)#define PSR\_S (1 << 7)

[ 22](sparc_8h.md#a2345b54dbade90ec8d3723229cb88dc0)#define PSR\_PS (1 << 6)

[ 23](sparc_8h.md#ada37afa7445b2faaa141677c30d2378f)#define PSR\_ET (1 << 5)

[ 24](sparc_8h.md#af64517c44f7cf67c25602590b4b21fea)#define PSR\_PIL (0xf << PSR\_PIL\_BIT)

[ 25](sparc_8h.md#a105dcd98b0429c955fdd858442104506)#define PSR\_CWP 0x1f

26

27

28/\* Trap Base Register \*/

[ 29](sparc_8h.md#a5bfb42f867f7289edacc0f3ced61df2b)#define TBR\_TT\_BIT 4

30

[ 31](sparc_8h.md#a86c8e0acfd7ed01269c4798f98abb8cb)#define TBR\_TBA 0xfffff000

[ 32](sparc_8h.md#a2653671b7568158f24260ea9e8faae7e)#define TBR\_TT 0x00000ff0

33

34/\* Trap types in TBR.TT \*/

[ 35](sparc_8h.md#a7d9ae67a7bb9cf93025c25ab95232e58)#define TT\_RESET 0x00

[ 36](sparc_8h.md#a3719eb7c4a6fd22df0479afe14e9cf88)#define TT\_WINDOW\_OVERFLOW 0x05

[ 37](sparc_8h.md#abf7f57c61c88ac4a7734d3f847c4f067)#define TT\_WINDOW\_UNDERFLOW 0x06

[ 38](sparc_8h.md#a6e50cb2d56076ea595e9208ffca3f420)#define TT\_DATA\_ACCESS\_EXCEPTION 0x09

39

40#endif /\* ZEPHYR\_INCLUDE\_ARCH\_SPARC\_SPARC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [sparc](dir_0b6b538994b3c7630127059eac21a61b.md)
- [sparc.h](sparc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
