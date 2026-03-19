---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ptp_8h_source.html
original_path: doxygen/html/ptp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ptp.h

[Go to the documentation of this file.](ptp_8h.md)

1/\*

2 \* Copyright (c) 2024 BayLibre SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_PTP\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_PTP\_H\_

16

25

26#include <[zephyr/net/ptp\_time.h](ptp__time_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 32](group__ptp.md#ga7ee0c8e25e85663efbaaa12eac6bee7b)#define PTP\_MAJOR\_VERSION 2

[ 33](group__ptp.md#ga45adf4966a9012e08dbfbbccf2b806d0)#define PTP\_MINOR\_VERSION 1

34

[ 35](group__ptp.md#ga19395e019e5a96c94ac021bd788c6b55)#define PTP\_VERSION (PTP\_MINOR\_VERSION << 4 | PTP\_MAJOR\_VERSION)

36

37#ifdef \_\_cplusplus

38}

39#endif

40

44

45#endif /\* ZEPHYR\_INCLUDE\_NET\_PTP\_H\_ \*/

[ptp\_time.h](ptp__time_8h.md)

Public functions for the Precision Time Protocol time specification.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ptp.h](ptp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
