---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fpu_8h_source.html
original_path: doxygen/html/fpu_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fpu.h

[Go to the documentation of this file.](fpu_8h.md)

1/\*

2 \* Copyright (c) 2021, Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_FPU\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_FPU\_H\_

9

[ 10](structfpu__ctx__full.md)struct [fpu\_ctx\_full](structfpu__ctx__full.md) {

[ 11](structfpu__ctx__full.md#af4654001584aa8606c7c2bd3a20bb74f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [caller\_saved](structfpu__ctx__full.md#af4654001584aa8606c7c2bd3a20bb74f)[16];

[ 12](structfpu__ctx__full.md#ad50e1fc3ec931979f9c3f6508fec259b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [callee\_saved](structfpu__ctx__full.md#ad50e1fc3ec931979f9c3f6508fec259b)[16];

[ 13](structfpu__ctx__full.md#a66ea3fea6f0209273e960831bfab09c6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fpscr](structfpu__ctx__full.md#a66ea3fea6f0209273e960831bfab09c6);

[ 14](structfpu__ctx__full.md#a6866578483d0340161bb84231ceee120) bool [ctx\_saved](structfpu__ctx__full.md#a6866578483d0340161bb84231ceee120);

15};

16

17void z\_arm\_save\_fp\_context(struct [fpu\_ctx\_full](structfpu__ctx__full.md) \*buffer);

18void z\_arm\_restore\_fp\_context(const struct [fpu\_ctx\_full](structfpu__ctx__full.md) \*buffer);

19

20#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_FPU\_H\_ \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[fpu\_ctx\_full](structfpu__ctx__full.md)

**Definition** fpu.h:10

[fpu\_ctx\_full::fpscr](structfpu__ctx__full.md#a66ea3fea6f0209273e960831bfab09c6)

uint32\_t fpscr

**Definition** fpu.h:13

[fpu\_ctx\_full::ctx\_saved](structfpu__ctx__full.md#a6866578483d0340161bb84231ceee120)

bool ctx\_saved

**Definition** fpu.h:14

[fpu\_ctx\_full::callee\_saved](structfpu__ctx__full.md#ad50e1fc3ec931979f9c3f6508fec259b)

uint32\_t callee\_saved[16]

**Definition** fpu.h:12

[fpu\_ctx\_full::caller\_saved](structfpu__ctx__full.md#af4654001584aa8606c7c2bd3a20bb74f)

uint32\_t caller\_saved[16]

**Definition** fpu.h:11

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [fpu.h](fpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
