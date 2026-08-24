---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2arch_2rx_2error_8h_source.html
original_path: doxygen/html/include_2zephyr_2arch_2rx_2error_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h

[Go to the documentation of this file.](include_2zephyr_2arch_2rx_2error_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_RX\_ERROR\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_RX\_ERROR\_H\_

17

18#include <[stdbool.h](stdbool_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](include_2zephyr_2arch_2rx_2error_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) \

25 do { \

26 arch\_irq\_unlock(0); \

27 \_\_asm\_\_ volatile("mov %[\_reason], r1\n\t" \

28 "int #2\n\t" ::[\_reason] "r"(reason\_p) \

29 : "r1", "memory"); \

30 } while (false)

31

32#ifdef \_\_cplusplus

33}

34#endif

35

36#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RX\_ERROR\_H\_ \*/

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [rx](dir_eb52b7f9d95392aedf108916f743bdaf.md)
- [error.h](include_2zephyr_2arch_2rx_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
