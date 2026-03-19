---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sys_2sys__io_8h_source.html
original_path: doxygen/html/sys_2sys__io_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_io.h

[Go to the documentation of this file.](sys_2sys__io_8h.md)

1/\* Port and memory mapped registers I/O operations \*/

2

3/\*

4 \* Copyright (c) 2015 Intel Corporation.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_SYS\_SYS\_IO\_H\_

10#define ZEPHYR\_INCLUDE\_SYS\_SYS\_IO\_H\_

11

12#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

13#include <stddef.h>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86);

[ 20](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0);

[ 21](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d)typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d);

22

23/\* Port I/O functions \*/

24

34

45

55

66

76

87

97

107

120

133

146

147/\* Memory mapped registers I/O functions \*/

148

158

169

179

191

201

213

223

235

236/\* Memory bits manipulation functions \*/

237

247

257

267

277

290

303

316

326

336

349

362

375

376

377#ifdef \_\_cplusplus

378}

379#endif

380

381#endif /\* ZEPHYR\_INCLUDE\_SYS\_SYS\_IO\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86)

uint32\_t io\_port\_t

**Definition** sys\_io.h:19

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

[mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d)

uintptr\_t mem\_addr\_t

**Definition** sys\_io.h:21

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sys\_io.h](sys_2sys__io_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
