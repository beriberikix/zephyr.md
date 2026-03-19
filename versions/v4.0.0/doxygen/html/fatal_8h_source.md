---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fatal_8h_source.html
original_path: doxygen/html/fatal_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

14#include <[zephyr/arch/cpu.h](cpu_8h.md)>

15#include <[zephyr/arch/exception.h](exception_8h.md)>

16#include <[zephyr/toolchain.h](toolchain_8h.md)>

17#include <[zephyr/fatal\_types.h](fatal__types_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

28

[ 37](group__fatal__apis.md#gaa8c0b43a2360e5319d7910e8e0ceb951)FUNC\_NORETURN void [k\_fatal\_halt](group__fatal__apis.md#gaa8c0b43a2360e5319d7910e8e0ceb951)(unsigned int reason);

38

[ 68](group__fatal__apis.md#ga255cc816d227f0a5c0e80e61bfba11fa)void [k\_sys\_fatal\_error\_handler](group__fatal__apis.md#ga255cc816d227f0a5c0e80e61bfba11fa)(unsigned int reason, const struct [arch\_esf](structarch__esf.md) \*esf);

69

84void z\_fatal\_error(unsigned int reason, const struct [arch\_esf](structarch__esf.md) \*esf);

85

87

88#ifdef \_\_cplusplus

89}

90#endif

91

92#endif /\* ZEPHYR\_INCLUDE\_FATAL\_H \*/

[cpu.h](cpu_8h.md)

[exception.h](exception_8h.md)

[fatal\_types.h](fatal__types_8h.md)

Fatal base type definitions.

[k\_sys\_fatal\_error\_handler](group__fatal__apis.md#ga255cc816d227f0a5c0e80e61bfba11fa)

void k\_sys\_fatal\_error\_handler(unsigned int reason, const struct arch\_esf \*esf)

Fatal error policy handler.

[k\_fatal\_halt](group__fatal__apis.md#gaa8c0b43a2360e5319d7910e8e0ceb951)

FUNC\_NORETURN void k\_fatal\_halt(unsigned int reason)

Halt the system on a fatal error.

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fatal.h](fatal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
