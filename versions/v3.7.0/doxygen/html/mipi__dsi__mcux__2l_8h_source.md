---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mipi__dsi__mcux__2l_8h_source.html
original_path: doxygen/html/mipi__dsi__mcux__2l_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dsi\_mcux\_2l.h

[Go to the documentation of this file.](mipi__dsi__mcux__2l_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DSI\_MCUX\_2L\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DSI\_MCUX\_2L\_

8

9/\*

10 \* HW specific flag- indicates to the MIPI DSI 2L peripheral that the

11 \* data being sent is framebuffer data, which the DSI peripheral may

12 \* byte swap depending on KConfig settings

13 \*/

[ 14](mipi__dsi__mcux__2l_8h.md#aad6f6584fe0ce93f385b3692ee3de1a1)#define MCUX\_DSI\_2L\_FB\_DATA BIT(0x1)

15

16#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DSI\_MCUX\_2L\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mipi\_dsi](dir_39eeed2fee673188c90c99680225996b.md)
- [mipi\_dsi\_mcux\_2l.h](mipi__dsi__mcux__2l_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
