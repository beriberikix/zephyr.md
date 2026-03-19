---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/clock__control__rts5912_8h_source.html
original_path: doxygen/html/clock__control__rts5912_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control\_rts5912.h

[Go to the documentation of this file.](clock__control__rts5912_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7

5 \* Author: Lin Yu-Cheng <lin\_yu\_cheng@realtek.com>

6 \*/

7

8#include <[stdint.h](stdint_8h.md)>

9

10#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RTS5912\_H\_

11#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RTS5912\_H\_

12

[ 13](structrts5912__sccon__subsys.md)struct [rts5912\_sccon\_subsys](structrts5912__sccon__subsys.md) {

[ 14](structrts5912__sccon__subsys.md#aeadd64cc7eb73d39d5f7119c2b86365e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_grp](structrts5912__sccon__subsys.md#aeadd64cc7eb73d39d5f7119c2b86365e);

[ 15](structrts5912__sccon__subsys.md#a28a8e0a3078f7a724948ecec91760382) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_idx](structrts5912__sccon__subsys.md#a28a8e0a3078f7a724948ecec91760382);

[ 16](structrts5912__sccon__subsys.md#a4743dd2a82bce16d93eb3caf60615909) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_src](structrts5912__sccon__subsys.md#a4743dd2a82bce16d93eb3caf60615909);

[ 17](structrts5912__sccon__subsys.md#a1657eff3e6d6846e87e6d844f0bd102b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_div](structrts5912__sccon__subsys.md#a1657eff3e6d6846e87e6d844f0bd102b);

18};

19

20#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RTS591X\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[rts5912\_sccon\_subsys](structrts5912__sccon__subsys.md)

**Definition** clock\_control\_rts5912.h:13

[rts5912\_sccon\_subsys::clk\_div](structrts5912__sccon__subsys.md#a1657eff3e6d6846e87e6d844f0bd102b)

uint32\_t clk\_div

**Definition** clock\_control\_rts5912.h:17

[rts5912\_sccon\_subsys::clk\_idx](structrts5912__sccon__subsys.md#a28a8e0a3078f7a724948ecec91760382)

uint32\_t clk\_idx

**Definition** clock\_control\_rts5912.h:15

[rts5912\_sccon\_subsys::clk\_src](structrts5912__sccon__subsys.md#a4743dd2a82bce16d93eb3caf60615909)

uint32\_t clk\_src

**Definition** clock\_control\_rts5912.h:16

[rts5912\_sccon\_subsys::clk\_grp](structrts5912__sccon__subsys.md#aeadd64cc7eb73d39d5f7119c2b86365e)

uint32\_t clk\_grp

**Definition** clock\_control\_rts5912.h:14

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_control\_rts5912.h](clock__control__rts5912_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
