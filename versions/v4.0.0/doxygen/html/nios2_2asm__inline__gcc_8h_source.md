---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nios2_2asm__inline__gcc_8h_source.html
original_path: doxygen/html/nios2_2asm__inline__gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline\_gcc.h

[Go to the documentation of this file.](nios2_2asm__inline__gcc_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_ASM\_INLINE\_GCC\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_ASM\_INLINE\_GCC\_H\_

9

10/\*

11 \* The file must not be included directly

12 \* Include arch/cpu.h instead

13 \*/

14

15#ifndef \_ASMLANGUAGE

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

18#include <[zephyr/toolchain.h](toolchain_8h.md)>

19

20/\* Using the \*io variants of these instructions to prevent issues on

21 \* devices that have an instruction/data cache

22 \*/

23

[ 24](nios2_2asm__inline__gcc_8h.md#ae9b07f6441d8496a44a189b88cf061c6)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write32](nios2_2asm__inline__gcc_8h.md#ae9b07f6441d8496a44a189b88cf061c6)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

25{

26 \_\_builtin\_stwio((void \*)addr, data);

27}

28

[ 29](nios2_2asm__inline__gcc_8h.md#a63b36c1442f805db4d1bc5a51a035c42)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_read32](nios2_2asm__inline__gcc_8h.md#a63b36c1442f805db4d1bc5a51a035c42)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

30{

31 return \_\_builtin\_ldwio((void \*)addr);

32}

33

[ 34](nios2_2asm__inline__gcc_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write8](nios2_2asm__inline__gcc_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

35{

36 [sys\_write32](nios2_2asm__inline__gcc_8h.md#ae9b07f6441d8496a44a189b88cf061c6)(data, addr);

37}

38

[ 39](nios2_2asm__inline__gcc_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_read8](nios2_2asm__inline__gcc_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

40{

41 return \_\_builtin\_ldbuio((void \*)addr);

42}

43

[ 44](nios2_2asm__inline__gcc_8h.md#abacfedeea46690ae169b9636a94cfa5a)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write16](nios2_2asm__inline__gcc_8h.md#abacfedeea46690ae169b9636a94cfa5a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

45{

46 [sys\_write32](nios2_2asm__inline__gcc_8h.md#ae9b07f6441d8496a44a189b88cf061c6)(data, addr);

47}

48

[ 49](nios2_2asm__inline__gcc_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_read16](nios2_2asm__inline__gcc_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

50{

51 return \_\_builtin\_ldhuio((void \*)addr);

52}

53

54#endif /\* \_ASMLANGUAGE \*/

55

56#endif /\* \_ASM\_INLINE\_GCC\_PUBLIC\_GCC\_H \*/

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[sys\_write8](nios2_2asm__inline__gcc_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)

static ALWAYS\_INLINE void sys\_write8(uint8\_t data, mm\_reg\_t addr)

**Definition** asm\_inline\_gcc.h:34

[sys\_read32](nios2_2asm__inline__gcc_8h.md#a63b36c1442f805db4d1bc5a51a035c42)

static ALWAYS\_INLINE uint32\_t sys\_read32(mm\_reg\_t addr)

**Definition** asm\_inline\_gcc.h:29

[sys\_read16](nios2_2asm__inline__gcc_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)

static ALWAYS\_INLINE uint16\_t sys\_read16(mm\_reg\_t addr)

**Definition** asm\_inline\_gcc.h:49

[sys\_write16](nios2_2asm__inline__gcc_8h.md#abacfedeea46690ae169b9636a94cfa5a)

static ALWAYS\_INLINE void sys\_write16(uint16\_t data, mm\_reg\_t addr)

**Definition** asm\_inline\_gcc.h:44

[sys\_read8](nios2_2asm__inline__gcc_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)

static ALWAYS\_INLINE uint8\_t sys\_read8(mm\_reg\_t addr)

**Definition** asm\_inline\_gcc.h:39

[sys\_write32](nios2_2asm__inline__gcc_8h.md#ae9b07f6441d8496a44a189b88cf061c6)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mm\_reg\_t addr)

**Definition** asm\_inline\_gcc.h:24

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[sys\_io.h](sys_2sys__io_8h.md)

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [nios2](dir_bcfa142ae77c1ee311b7ef8e30037d11.md)
- [asm\_inline\_gcc.h](nios2_2asm__inline__gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
