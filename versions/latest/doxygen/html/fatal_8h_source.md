---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fatal_8h_source.html
original_path: doxygen/html/fatal_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fatal.h

[Go to the documentation of this file.](fatal_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_FATAL\_H

12#define ZEPHYR\_INCLUDE\_FATAL\_H

13

14#include <zephyr/arch/cpu.h>

15#include <[zephyr/toolchain.h](toolchain_8h.md)>

16#include <[zephyr/fatal\_types.h](fatal__types_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

27

[ 36](group__fatal__apis.md#gaa8c0b43a2360e5319d7910e8e0ceb951)FUNC\_NORETURN void [k\_fatal\_halt](group__fatal__apis.md#gaa8c0b43a2360e5319d7910e8e0ceb951)(unsigned int reason);

37

[ 67](group__fatal__apis.md#gab6dfd75572a84729df534fde49ef7d85)void [k\_sys\_fatal\_error\_handler](group__fatal__apis.md#gab6dfd75572a84729df534fde49ef7d85)(unsigned int reason, const z\_arch\_esf\_t \*esf);

68

83void z\_fatal\_error(unsigned int reason, const z\_arch\_esf\_t \*esf);

84

86

87#ifdef \_\_cplusplus

88}

89#endif

90

91#endif /\* ZEPHYR\_INCLUDE\_FATAL\_H \*/

[fatal\_types.h](fatal__types_8h.md)

Fatal base type definitions.

[k\_fatal\_halt](group__fatal__apis.md#gaa8c0b43a2360e5319d7910e8e0ceb951)

FUNC\_NORETURN void k\_fatal\_halt(unsigned int reason)

Halt the system on a fatal error.

[k\_sys\_fatal\_error\_handler](group__fatal__apis.md#gab6dfd75572a84729df534fde49ef7d85)

void k\_sys\_fatal\_error\_handler(unsigned int reason, const z\_arch\_esf\_t \*esf)

Fatal error policy handler.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fatal.h](fatal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
