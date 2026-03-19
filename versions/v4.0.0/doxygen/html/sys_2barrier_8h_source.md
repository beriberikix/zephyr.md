---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sys_2barrier_8h_source.html
original_path: doxygen/html/sys_2barrier_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

barrier.h

[Go to the documentation of this file.](sys_2barrier_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_BARRIER\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_BARRIER\_H\_

9

10#include <[zephyr/toolchain.h](toolchain_8h.md)>

11

12#if defined(CONFIG\_BARRIER\_OPERATIONS\_ARCH)

13# if defined(CONFIG\_ARM)

14# include <[zephyr/arch/arm/barrier.h](arch_2arm_2barrier_8h.md)>

15# elif defined(CONFIG\_ARM64)

16# include <[zephyr/arch/arm64/barrier.h](arch_2arm64_2barrier_8h.md)>

17# endif

18#elif defined(CONFIG\_BARRIER\_OPERATIONS\_BUILTIN)

19#include <[zephyr/sys/barrier\_builtin.h](barrier__builtin_8h.md)>

20#endif

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

33

[ 40](group__barrier__apis.md#gab0dd6769236babde7cf48c32007edf31)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [barrier\_dmem\_fence\_full](group__barrier__apis.md#gab0dd6769236babde7cf48c32007edf31)(void)

41{

42#if defined(CONFIG\_BARRIER\_OPERATIONS\_ARCH) || defined(CONFIG\_BARRIER\_OPERATIONS\_BUILTIN)

43 z\_barrier\_dmem\_fence\_full();

44#endif

45}

46

[ 59](group__barrier__apis.md#gaaa6909c1410bc371f59ad3eec21ee5ef)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [barrier\_dsync\_fence\_full](group__barrier__apis.md#gaaa6909c1410bc371f59ad3eec21ee5ef)(void)

60{

61#if defined(CONFIG\_BARRIER\_OPERATIONS\_ARCH) || defined(CONFIG\_BARRIER\_OPERATIONS\_BUILTIN)

62 z\_barrier\_dsync\_fence\_full();

63#endif

64}

65

[ 78](group__barrier__apis.md#gaa916454a2ff58e50b2f51845447177ec)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [barrier\_isync\_fence\_full](group__barrier__apis.md#gaa916454a2ff58e50b2f51845447177ec)(void)

79{

80#if defined(CONFIG\_BARRIER\_OPERATIONS\_ARCH) || defined(CONFIG\_BARRIER\_OPERATIONS\_BUILTIN)

81 z\_barrier\_isync\_fence\_full();

82#endif

83}

84

86

87#ifdef \_\_cplusplus

88} /\* extern "C" \*/

89#endif

90

91#endif /\* ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_H\_ \*/

[barrier.h](arch_2arm64_2barrier_8h.md)

[barrier.h](arch_2arm_2barrier_8h.md)

[barrier\_builtin.h](barrier__builtin_8h.md)

[barrier\_isync\_fence\_full](group__barrier__apis.md#gaa916454a2ff58e50b2f51845447177ec)

static ALWAYS\_INLINE void barrier\_isync\_fence\_full(void)

Full/sequentially-consistent instruction synchronization barrier.

**Definition** barrier.h:78

[barrier\_dsync\_fence\_full](group__barrier__apis.md#gaaa6909c1410bc371f59ad3eec21ee5ef)

static ALWAYS\_INLINE void barrier\_dsync\_fence\_full(void)

Full/sequentially-consistent data synchronization barrier.

**Definition** barrier.h:59

[barrier\_dmem\_fence\_full](group__barrier__apis.md#gab0dd6769236babde7cf48c32007edf31)

static ALWAYS\_INLINE void barrier\_dmem\_fence\_full(void)

Full/sequentially-consistent data memory barrier.

**Definition** barrier.h:40

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [barrier.h](sys_2barrier_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
