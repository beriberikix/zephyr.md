---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm__mem_8h_source.html
original_path: doxygen/html/arm__mem_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mem.h

[Go to the documentation of this file.](arm__mem_8h.md)

1/\*

2 \* Copyright 2022 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARM\_MEM\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARM\_MEM\_H\_

8

9/\*

10 \* Define ARM specific memory flags used by k\_mem\_map\_phys\_bare()

11 \* followed public definitions in include/kernel/mm.h.

12 \*/

13/\* For ARM64, K\_MEM\_CACHE\_NONE is nGnRnE. \*/

[ 14](arm__mem_8h.md#a6a8eedb0c07f7762c2e5ead28f379263)#define K\_MEM\_ARM\_DEVICE\_nGnRnE K\_MEM\_CACHE\_NONE

15

[ 17](arm__mem_8h.md#a6c1bcf312b434b77e5cec56e130ba70f)#define K\_MEM\_ARM\_DEVICE\_nGnRE 3

18

[ 20](arm__mem_8h.md#a95b11cabfc9c5c231239210120b768f5)#define K\_MEM\_ARM\_DEVICE\_GRE 4

21

[ 23](arm__mem_8h.md#aae4f0f0d87cdb19161ad56af822a78a1)#define K\_MEM\_ARM\_NORMAL\_NC 5

24

25#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARM\_MEM\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arm\_mem.h](arm__mem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
