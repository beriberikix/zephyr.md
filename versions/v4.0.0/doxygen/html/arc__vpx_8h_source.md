---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arc__vpx_8h_source.html
original_path: doxygen/html/arc__vpx_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_vpx.h

[Go to the documentation of this file.](arc__vpx_8h.md)

1/\*

2 \* Copyright (c) 2024 Synopsys.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_VPX\_ARC\_VPX\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_VPX\_ARC\_VPX\_H\_

9

10#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

11

[ 28](arc__vpx_8h.md#a97f5476f56ce69acf4a0d169c6a78ba6)int [arc\_vpx\_lock](arc__vpx_8h.md#a97f5476f56ce69acf4a0d169c6a78ba6)([k\_timeout\_t](structk__timeout__t.md) timeout);

29

[ 39](arc__vpx_8h.md#a40a9dcc39bc184cb1a5aca5b8e7ad3ad)void [arc\_vpx\_unlock](arc__vpx_8h.md#a40a9dcc39bc184cb1a5aca5b8e7ad3ad)(void);

40

[ 52](arc__vpx_8h.md#aae826e8f1a2ce10b8183798633da8a20)void [arc\_vpx\_unlock\_force](arc__vpx_8h.md#aae826e8f1a2ce10b8183798633da8a20)(unsigned int cpu\_id);

53

54#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_VPX\_ARC\_VPX\_H\_ \*/

[arc\_vpx\_unlock](arc__vpx_8h.md#a40a9dcc39bc184cb1a5aca5b8e7ad3ad)

void arc\_vpx\_unlock(void)

Release cooperative lock on the VPX vector registers.

[arc\_vpx\_lock](arc__vpx_8h.md#a97f5476f56ce69acf4a0d169c6a78ba6)

int arc\_vpx\_lock(k\_timeout\_t timeout)

Obtain a cooperative lock on the VPX vector registers.

[arc\_vpx\_unlock\_force](arc__vpx_8h.md#aae826e8f1a2ce10b8183798633da8a20)

void arc\_vpx\_unlock\_force(unsigned int cpu\_id)

Release cooperative lock on a CPU's VPX vector registers.

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [vpx](dir_163ac165fb52f03f9d4ffcae544ed3b1.md)
- [arc\_vpx.h](arc__vpx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
