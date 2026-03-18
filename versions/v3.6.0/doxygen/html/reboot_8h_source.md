---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/reboot_8h_source.html
original_path: doxygen/html/reboot_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reboot.h

[Go to the documentation of this file.](reboot_8h.md)

1/\*

2 \* Copyright (c) 2015 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_SYS\_REBOOT\_H\_

15#define ZEPHYR\_INCLUDE\_SYS\_REBOOT\_H\_

16

17#include <[zephyr/toolchain.h](toolchain_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 23](reboot_8h.md#a956528997e1fa2cf52f3795b95dcc01b)#define SYS\_REBOOT\_WARM 0

[ 24](reboot_8h.md#aa2589ee8e2e252dedeee80ec0f58ed15)#define SYS\_REBOOT\_COLD 1

25

[ 35](reboot_8h.md#a18abe5d5b8089e8429c25bafa5e76d3d)FUNC\_NORETURN void [sys\_reboot](reboot_8h.md#a18abe5d5b8089e8429c25bafa5e76d3d)(int type);

36

37#ifdef \_\_cplusplus

38}

39#endif

40

41#endif /\* ZEPHYR\_INCLUDE\_SYS\_REBOOT\_H\_ \*/

[sys\_reboot](reboot_8h.md#a18abe5d5b8089e8429c25bafa5e76d3d)

FUNC\_NORETURN void sys\_reboot(int type)

Reboot the system.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [reboot.h](reboot_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
