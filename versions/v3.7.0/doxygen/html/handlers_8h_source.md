---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/handlers_8h_source.html
original_path: doxygen/html/handlers_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

handlers.h

[Go to the documentation of this file.](handlers_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_MCUMGR\_MGMT\_HANDLERS\_

8#define H\_MCUMGR\_MGMT\_HANDLERS\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

12#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif /\* \_\_cplusplus \*/

17

24

[ 26](group__mcumgr__handler__api.md#gaceb63293a54178de29ce0cdf6a03083a)typedef void (\*[mcumgr\_handler\_init\_t](group__mcumgr__handler__api.md#gaceb63293a54178de29ce0cdf6a03083a))(void);

27

29struct mcumgr\_handler {

31 const [mcumgr\_handler\_init\_t](group__mcumgr__handler__api.md#gaceb63293a54178de29ce0cdf6a03083a) init;

32};

34

[ 43](group__mcumgr__handler__api.md#ga59833a6c16520816e4488210308b7c7b)#define MCUMGR\_HANDLER\_DEFINE(name, \_init) \

44 STRUCT\_SECTION\_ITERABLE(mcumgr\_handler, name) = { \

45 .init = \_init, \

46 }

47

48#ifdef \_\_cplusplus

49}

50#endif /\* \_\_cplusplus \*/

51

55

56#endif /\* H\_MCUMGR\_MGMT\_HANDLERS\_ \*/

[mcumgr\_handler\_init\_t](group__mcumgr__handler__api.md#gaceb63293a54178de29ce0cdf6a03083a)

void(\* mcumgr\_handler\_init\_t)(void)

Type definition for a MCUmgr handler initialisation function.

**Definition** handlers.h:26

[kernel.h](kernel_8h.md)

Public kernel APIs.

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [mgmt](dir_138c477f5f1e916a824d5e5e3c2b43b2.md)
- [handlers.h](handlers_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
