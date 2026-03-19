---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pm__cpu__ops_8h_source.html
original_path: doxygen/html/pm__cpu__ops_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_cpu\_ops.h

[Go to the documentation of this file.](pm__cpu__ops_8h.md)

1/\*

2 \* Copyright 2021 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PM\_CPU\_OPS\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_PM\_CPU\_OPS\_H\_

9

14

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <stddef.h>

17#include <[zephyr/device.h](device_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23/\* System reset types. \*/

[ 24](pm__cpu__ops_8h.md#a98f079e56ab5b320bb52e1ebaa873d9b)#define SYS\_WARM\_RESET 0

[ 25](pm__cpu__ops_8h.md#a92747266cafef3783fcfb550e08ce132)#define SYS\_COLD\_RESET 1

31

[ 41](group__power__management__cpu__api.md#gaa6de91e837b262f432b4a80ef5e2b781)int [pm\_cpu\_off](group__power__management__cpu__api.md#gaa6de91e837b262f432b4a80ef5e2b781)(void);

42

[ 56](group__power__management__cpu__api.md#ga68c37acfc53eee990c34398ca0f1a3f5)int [pm\_cpu\_on](group__power__management__cpu__api.md#ga68c37acfc53eee990c34398ca0f1a3f5)(unsigned long cpuid, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) entry\_point);

57

[ 67](group__power__management__cpu__api.md#ga65dfe4b0c47af092c50c0022227ac8eb)int [pm\_system\_reset](group__power__management__cpu__api.md#ga65dfe4b0c47af092c50c0022227ac8eb)(unsigned char reset);

68

69#ifdef \_\_cplusplus

70}

71#endif

72

76

77#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PM\_CPU\_OPS\_H\_ \*/

[device.h](device_8h.md)

[pm\_system\_reset](group__power__management__cpu__api.md#ga65dfe4b0c47af092c50c0022227ac8eb)

int pm\_system\_reset(unsigned char reset)

System reset.

[pm\_cpu\_on](group__power__management__cpu__api.md#ga68c37acfc53eee990c34398ca0f1a3f5)

int pm\_cpu\_on(unsigned long cpuid, uintptr\_t entry\_point)

Power up a core.

[pm\_cpu\_off](group__power__management__cpu__api.md#gaa6de91e837b262f432b4a80ef5e2b781)

int pm\_cpu\_off(void)

Power down the calling core.

[types.h](include_2zephyr_2types_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pm\_cpu\_ops.h](pm__cpu__ops_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
