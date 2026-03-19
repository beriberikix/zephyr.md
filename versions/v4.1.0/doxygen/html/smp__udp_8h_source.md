---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/smp__udp_8h_source.html
original_path: doxygen/html/smp__udp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_udp.h

[Go to the documentation of this file.](smp__udp_8h.md)

1/\*

2 \* Copyright (c) 2019, Prevas A/S

3 \* Copyright (c) 2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_MGMT\_SMP\_UDP\_H\_

14#define ZEPHYR\_INCLUDE\_MGMT\_SMP\_UDP\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 29](smp__udp_8h.md#a768f36cea02d7d7781113d36516e1763)int [smp\_udp\_open](smp__udp_8h.md#a768f36cea02d7d7781113d36516e1763)(void);

30

[ 39](smp__udp_8h.md#add428f3ed2ae0d9e580e45897a98a293)int [smp\_udp\_close](smp__udp_8h.md#add428f3ed2ae0d9e580e45897a98a293)(void);

40

41#ifdef \_\_cplusplus

42}

43#endif

44

45#endif

[smp\_udp\_open](smp__udp_8h.md#a768f36cea02d7d7781113d36516e1763)

int smp\_udp\_open(void)

Enables the UDP SMP MCUmgr transport thread(s) which will open a socket and listen to requests.

[smp\_udp\_close](smp__udp_8h.md#add428f3ed2ae0d9e580e45897a98a293)

int smp\_udp\_close(void)

Disables the UDP SMP MCUmgr transport thread(s) which will close open sockets.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_udp.h](smp__udp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
