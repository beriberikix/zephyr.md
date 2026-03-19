---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm64_2asm__inline__gcc_8h_source.html
original_path: doxygen/html/arm64_2asm__inline__gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm\_inline\_gcc.h

[Go to the documentation of this file.](arm64_2asm__inline__gcc_8h.md)

1/\*

2 \* Copyright (c) 2019 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\* Either public functions or macros or invoked by public functions \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ASM\_INLINE\_GCC\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ASM\_INLINE\_GCC\_H\_

11

12/\*

13 \* The file must not be included directly

14 \* Include arch/cpu.h instead

15 \*/

16

17#ifndef \_ASMLANGUAGE

18

19#include <[zephyr/arch/arm64/lib\_helpers.h](4_2lib__helpers_8h.md)>

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 26](arm64_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](arm_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

27{

28 unsigned int key;

29

30 /\*

31 \* Return the whole DAIF register as key but use DAIFSET to disable

32 \* IRQs.

33 \*/

34 key = [read\_daif](4_2lib__helpers_8h.md#a973d6a3b1193bde3f6ac9a1724c6a00d)();

35 [disable\_irq](4_2lib__helpers_8h.md#a86526fa2425a30ae46957d0480a09f25)();

36

37 return key;

38}

39

[ 40](arm64_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](arm_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

41{

42 [write\_daif](4_2lib__helpers_8h.md#a3bbf7e8062793efc513ba6c055132263)(key);

43}

44

[ 45](arm64_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](arm_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

46{

47 /\* We only check the (I)RQ bit on the DAIF register \*/

48 return (key & [DAIF\_IRQ\_BIT](arm64_2cpu_8h.md#ad4a89cfde4c1112886aaa11b1004e2db)) == 0;

49}

50

51#ifdef \_\_cplusplus

52}

53#endif

54

55#endif /\* \_ASMLANGUAGE \*/

56

57#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ASM\_INLINE\_GCC\_H\_ \*/

[lib\_helpers.h](4_2lib__helpers_8h.md)

[write\_daif](4_2lib__helpers_8h.md#a3bbf7e8062793efc513ba6c055132263)

static ALWAYS\_INLINE void write\_daif(uint64\_t val)

**Definition** lib\_helpers.h:69

[disable\_irq](4_2lib__helpers_8h.md#a86526fa2425a30ae46957d0480a09f25)

static ALWAYS\_INLINE void disable\_irq(void)

**Definition** lib\_helpers.h:138

[read\_daif](4_2lib__helpers_8h.md#a973d6a3b1193bde3f6ac9a1724c6a00d)

static ALWAYS\_INLINE uint64\_t read\_daif(void)

**Definition** lib\_helpers.h:69

[DAIF\_IRQ\_BIT](arm64_2cpu_8h.md#ad4a89cfde4c1112886aaa11b1004e2db)

#define DAIF\_IRQ\_BIT

**Definition** cpu.h:24

[arch\_irq\_lock](arm_2asm__inline__gcc_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** asm\_inline\_gcc.h:44

[arch\_irq\_unlock](arm_2asm__inline__gcc_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** asm\_inline\_gcc.h:80

[arch\_irq\_unlocked](arm_2asm__inline__gcc_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** asm\_inline\_gcc.h:102

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [asm\_inline\_gcc.h](arm64_2asm__inline__gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
