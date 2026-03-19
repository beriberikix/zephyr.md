---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/psci_8h_source.html
original_path: doxygen/html/psci_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

psci.h

[Go to the documentation of this file.](psci_8h.md)

1/\*

2 \* Copyright 2020 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PM\_CPU\_OPS\_PSCI\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_PM\_CPU\_OPS\_PSCI\_H\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11#include <[zephyr/arch/arm64/arm-smccc.h](arm-smccc_8h.md)>

12#include <stddef.h>

13#include <[zephyr/device.h](device_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19/\* PSCI version decoding (independent of PSCI version) \*/

[ 20](psci_8h.md#aba5a843b7c3cd4ac675cd036b0048d25)#define PSCI\_VERSION\_MAJOR\_SHIFT 16

[ 21](psci_8h.md#a119caefd53e8915d794c1e41da8c2057)#define PSCI\_VERSION\_MINOR\_MASK \

22 ((1U << PSCI\_VERSION\_MAJOR\_SHIFT) - 1)

[ 23](psci_8h.md#a27ec15f0330589ee26e3a5623a0ba15d)#define PSCI\_VERSION\_MAJOR\_MASK ~PSCI\_VERSION\_MINOR\_MASK

24

[ 25](psci_8h.md#a1e6404a2f880eccc43566b399c1aded7)#define PSCI\_VERSION\_MAJOR(ver) \

26 (((ver) & PSCI\_VERSION\_MAJOR\_MASK) >> PSCI\_VERSION\_MAJOR\_SHIFT)

[ 27](psci_8h.md#affdc7b10fe33298091cfbfbd4ef290b0)#define PSCI\_VERSION\_MINOR(ver) \

28 ((ver) & PSCI\_VERSION\_MINOR\_MASK)

29

[ 30](psci_8h.md#a1964266f31f19eb7e7e0acd4bb660f4c)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [psci\_version](psci_8h.md#a1964266f31f19eb7e7e0acd4bb660f4c)(void);

31

32#ifdef \_\_cplusplus

33}

34#endif

35

36#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PM\_CPU\_OPS\_PSCI\_H\_ \*/

[arm-smccc.h](arm-smccc_8h.md)

[device.h](device_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[psci\_version](psci_8h.md#a1964266f31f19eb7e7e0acd4bb660f4c)

uint32\_t psci\_version(void)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pm\_cpu\_ops](dir_e793b4b61545b17399e4385df57fcbb6.md)
- [psci.h](psci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
