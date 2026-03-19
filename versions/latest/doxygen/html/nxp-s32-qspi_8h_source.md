---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp-s32-qspi_8h_source.html
original_path: doxygen/html/nxp-s32-qspi_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-s32-qspi.h

[Go to the documentation of this file.](nxp-s32-qspi_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_NXP\_S32\_QSPI\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_NXP\_S32\_QSPI\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

12/\* The QSPI secure attribute and secure policy references \*/

[ 13](nxp-s32-qspi_8h.md#aa902b22a3aaa19aac93d02463067b6f0)#define NXP\_S32\_QSPI\_NON\_SECURE BIT(0)

[ 14](nxp-s32-qspi_8h.md#a2bcb1e3b1b71871dd0a8cf98f9f99296)#define NXP\_S32\_QSPI\_SECURE BIT(1)

[ 15](nxp-s32-qspi_8h.md#ade7b80ec34b01229dfaf622f83dd2b73)#define NXP\_S32\_QSPI\_PRIVILEGE BIT(2)

16

17#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_NXP\_S32\_QSPI\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [qspi](dir_800384d1c4c1f0b32a31e18258fc08e1.md)
- [nxp-s32-qspi.h](nxp-s32-qspi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
