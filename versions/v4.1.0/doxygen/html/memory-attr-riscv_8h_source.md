---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/memory-attr-riscv_8h_source.html
original_path: doxygen/html/memory-attr-riscv_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr-riscv.h

[Go to the documentation of this file.](memory-attr-riscv_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_RISCV\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_RISCV\_H\_

8

9#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

10#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h.md)>

11

12/\*

13 \* Architecture specific RISCV related attributes.

14 \*/

[ 15](memory-attr-riscv_8h.md#a9a9ef79de1ef1c634e27dcec5a6ca8e3)#define DT\_MEM\_RISCV\_MASK DT\_MEM\_ARCH\_ATTR\_MASK

[ 16](memory-attr-riscv_8h.md#afea331be5ba6698753abd1a1a1d958eb)#define DT\_MEM\_RISCV\_GET(x) ((x) & DT\_MEM\_RISCV\_MASK)

[ 17](memory-attr-riscv_8h.md#a26562c62513dfb712404e3a636c6b7b2)#define DT\_MEM\_RISCV(x) ((x) << DT\_MEM\_ARCH\_ATTR\_SHIFT)

18

[ 19](memory-attr-riscv_8h.md#a326a99ea398a6972b5f6412a619b7729)#define ATTR\_RISCV\_TYPE\_MAIN BIT(0)

[ 20](memory-attr-riscv_8h.md#a7edefffaeae15842d748376348354e01)#define ATTR\_RISCV\_TYPE\_IO BIT(1)

[ 21](memory-attr-riscv_8h.md#a4298e697fdee5155acc0dae339e8c7b0)#define ATTR\_RISCV\_TYPE\_EMPTY BIT(2)

[ 22](memory-attr-riscv_8h.md#a5b3078bb1a6db09697ca57f47c31f0d0)#define ATTR\_RISCV\_AMO\_SWAP BIT(3)

[ 23](memory-attr-riscv_8h.md#aed9286d69906a98892dd15602b747629)#define ATTR\_RISCV\_AMO\_LOGICAL BIT(4)

[ 24](memory-attr-riscv_8h.md#af404c9544d1487688bf0a275c02cf80e)#define ATTR\_RISCV\_AMO\_ARITHMETIC BIT(5)

[ 25](memory-attr-riscv_8h.md#a2e51b151a96c55c5a4ab63a265a93161)#define ATTR\_RISCV\_IO\_IDEMPOTENT\_READ BIT(6)

[ 26](memory-attr-riscv_8h.md#a9969de51c4a6ed2c6b332bf67b55820b)#define ATTR\_RISCV\_IO\_IDEMPOTENT\_WRITE BIT(7)

27

[ 28](memory-attr-riscv_8h.md#a4c67437419601ee8c81b9c34f39122c4)#define DT\_MEM\_RISCV\_TYPE\_MAIN DT\_MEM\_RISCV(ATTR\_RISCV\_TYPE\_MAIN)

[ 29](memory-attr-riscv_8h.md#a30903aee0dabbf6f15c8526834b11f11)#define DT\_MEM\_RISCV\_TYPE\_IO DT\_MEM\_RISCV(ATTR\_RISCV\_TYPE\_IO)

[ 30](memory-attr-riscv_8h.md#a938f9f8b108f8e1230726bf3cbadbe99)#define DT\_MEM\_RISCV\_TYPE\_EMPTY DT\_MEM\_RISCV(ATTR\_RISCV\_TYPE\_EMPTY)

[ 31](memory-attr-riscv_8h.md#afe6b3c00217e837092384b2baf36d613)#define DT\_MEM\_RISCV\_AMO\_SWAP DT\_MEM\_RISCV(ATTR\_RISCV\_AMO\_SWAP)

[ 32](memory-attr-riscv_8h.md#a1b28fc152f2c96c3236e2e4c37c8fbb2)#define DT\_MEM\_RISCV\_AMO\_LOGICAL DT\_MEM\_RISCV(ATTR\_RISCV\_AMO\_LOGICAL)

[ 33](memory-attr-riscv_8h.md#adafec66eb70663372088154a2703012e)#define DT\_MEM\_RISCV\_AMO\_ARITHMETIC DT\_MEM\_RISCV(ATTR\_RISCV\_AMO\_ARITHMETIC)

[ 34](memory-attr-riscv_8h.md#a2be0609b3bc135633711554e840e512a)#define DT\_MEM\_RISCV\_IO\_IDEMPOTENT\_READ DT\_MEM\_RISCV(ATTR\_RISCV\_IO\_IDEMPOTENT\_READ)

[ 35](memory-attr-riscv_8h.md#a1b04dd65a2a5bf184b0965a352cba49f)#define DT\_MEM\_RISCV\_IO\_IDEMPOTENT\_WRITE DT\_MEM\_RISCV(ATTR\_RISCV\_IO\_IDEMPOTENT\_WRITE)

[ 36](memory-attr-riscv_8h.md#ae008d2f860df3c52c9a02e97757f4168)#define DT\_MEM\_RISCV\_UNKNOWN DT\_MEM\_ARCH\_ATTR\_UNKNOWN

37

38#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEM\_ATTR\_RISCV\_H\_ \*/

[memory-attr.h](memory-attr_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr-riscv.h](memory-attr-riscv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
