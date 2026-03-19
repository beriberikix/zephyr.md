---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ordinals_8h_source.html
original_path: doxygen/html/ordinals_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ordinals.h

[Go to the documentation of this file.](ordinals_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_ORDINALS\_H\_

7#define ZEPHYR\_INCLUDE\_DEVICETREE\_ORDINALS\_H\_

8

13

19

[ 25](group__devicetree-dep-ord.md#ga5b96dccfd349dd0ddba1812aa942c1bd)#define DT\_DEP\_ORD(node\_id) DT\_CAT(node\_id, \_ORD)

26

[ 32](group__devicetree-dep-ord.md#ga6c31d58b47d826f1a1de1e5d0044e2f7)#define DT\_DEP\_ORD\_STR\_SORTABLE(node\_id) DT\_CAT(node\_id, \_ORD\_STR\_SORTABLE)

33

[ 51](group__devicetree-dep-ord.md#ga22dd1b0c89eb5ddfbfdd1e723d44f509)#define DT\_REQUIRES\_DEP\_ORDS(node\_id) DT\_CAT(node\_id, \_REQUIRES\_ORDS)

52

[ 68](group__devicetree-dep-ord.md#ga3f559e9a787792685ed08be124b374ae)#define DT\_SUPPORTS\_DEP\_ORDS(node\_id) DT\_CAT(node\_id, \_SUPPORTS\_ORDS)

69

[ 78](group__devicetree-dep-ord.md#ga9c5e6f36c6e7a250368177a9f0713f86)#define DT\_INST\_DEP\_ORD(inst) DT\_DEP\_ORD(DT\_DRV\_INST(inst))

79

[ 90](group__devicetree-dep-ord.md#gac7d43a7916bdc8c46fafeee0213e538c)#define DT\_INST\_REQUIRES\_DEP\_ORDS(inst) DT\_REQUIRES\_DEP\_ORDS(DT\_DRV\_INST(inst))

91

[ 102](group__devicetree-dep-ord.md#ga027cc1361d1e059dde039926980e26fa)#define DT\_INST\_SUPPORTS\_DEP\_ORDS(inst) DT\_SUPPORTS\_DEP\_ORDS(DT\_DRV\_INST(inst))

103

107

108#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_ORDINALS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [ordinals.h](ordinals_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
