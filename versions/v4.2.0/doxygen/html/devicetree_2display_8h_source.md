---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/devicetree_2display_8h_source.html
original_path: doxygen/html/devicetree_2display_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

display.h

[Go to the documentation of this file.](devicetree_2display_8h.md)

1

5

6/\*

7 \* Copyright (c) 2025 Abderrahmane JARMOUNI

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_DISPLAY\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_DISPLAY\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 59](group__devicetree-display.md#ga265c3a81b2f6962b11931028c8727863)#define DT\_ZEPHYR\_DISPLAY(idx) \

60 DT\_PHANDLE\_BY\_IDX(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(zephyr\_displays), displays, idx)

61

[ 68](group__devicetree-display.md#ga5a5f5bc95a76e4f1d09d970a18e6e5b5)#define DT\_ZEPHYR\_DISPLAYS\_COUNT \

69 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(zephyr\_displays), \

70 (DT\_PROP\_LEN(DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(zephyr\_displays), displays)), \

71 (DT\_HAS\_CHOSEN(zephyr\_display)))

72

75

76#ifdef \_\_cplusplus

77}

78#endif

79

80#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_DMAS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [display.h](devicetree_2display_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
