---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/loopback_8h_source.html
original_path: doxygen/html/loopback_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loopback.h

[Go to the documentation of this file.](loopback_8h.md)

1

4

5/\*

6 \* Copyright (c) 2022 Radarxense B.V.

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_LOOPBACK\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_LOOPBACK\_H\_

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18#ifdef CONFIG\_NET\_LOOPBACK\_SIMULATE\_PACKET\_DROP

26int loopback\_set\_packet\_drop\_ratio(float ratio);

27

33int loopback\_get\_num\_dropped\_packets(void);

34#endif

35

36#ifdef \_\_cplusplus

37}

38#endif

39

40#endif /\* ZEPHYR\_INCLUDE\_NET\_LOOPBACK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [loopback.h](loopback_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
