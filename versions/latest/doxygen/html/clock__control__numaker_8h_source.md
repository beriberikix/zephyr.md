---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/clock__control__numaker_8h_source.html
original_path: doxygen/html/clock__control__numaker_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control\_numaker.h

[Go to the documentation of this file.](clock__control__numaker_8h.md)

1/\*

2 \* Copyright (c) 2023 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[stdint.h](stdint_8h.md)>

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NUMAKER\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NUMAKER\_H\_

11

[ 15](clock__control__numaker_8h.md#a45da36b4d2240d67426c24173c418244)#define NUMAKER\_SCC\_CLKSW\_UNTOUCHED 0

[ 16](clock__control__numaker_8h.md#adf1d45b58eba1825231c031b993562c7)#define NUMAKER\_SCC\_CLKSW\_ENABLE 1

[ 17](clock__control__numaker_8h.md#a35485fa37bb7eeac9d761cf5c98d5177)#define NUMAKER\_SCC\_CLKSW\_DISABLE 2

18

[ 22](clock__control__numaker_8h.md#a276ba4e34017fda5c4b77f4abb82a7af)#define NUMAKER\_SCC\_SUBSYS\_ID\_PCC 1

23

[ 24](structnumaker__scc__subsys.md)struct [numaker\_scc\_subsys](structnumaker__scc__subsys.md) {

[ 25](structnumaker__scc__subsys.md#af8e2099977ecba2c53808fe8db4e041a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [subsys\_id](structnumaker__scc__subsys.md#af8e2099977ecba2c53808fe8db4e041a); /\* SCC sybsystem ID \*/

26

27 /\* Peripheral clock control configuration structure

28 \* clk\_modidx is same as u32ModuleIdx in BSP CLK\_SetModuleClock().

29 \* clk\_src is same as u32ClkSrc in BSP CLK\_SetModuleClock().

30 \* clk\_div is same as u32ClkDiv in BSP CLK\_SetModuleClock().

31 \*/

32 union {

33 struct {

[ 34](structnumaker__scc__subsys.md#a97179646f9df3ef16e7d3e79a16738b2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_modidx](structnumaker__scc__subsys.md#a97179646f9df3ef16e7d3e79a16738b2);

[ 35](structnumaker__scc__subsys.md#ab7b47761009d1e4ca7ef0f5f5af19999) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_src](structnumaker__scc__subsys.md#ab7b47761009d1e4ca7ef0f5f5af19999);

[ 36](structnumaker__scc__subsys.md#a0f9ce23b7e8f97ba9733542d5c743b75) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_div](structnumaker__scc__subsys.md#a0f9ce23b7e8f97ba9733542d5c743b75);

[ 37](structnumaker__scc__subsys.md#ab9d9ea175b9ccb3a15e7e897a128021a) } [pcc](structnumaker__scc__subsys.md#ab9d9ea175b9ccb3a15e7e897a128021a);

38 };

39};

40

41#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NUMAKER\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[numaker\_scc\_subsys](structnumaker__scc__subsys.md)

**Definition** clock\_control\_numaker.h:24

[numaker\_scc\_subsys::clk\_div](structnumaker__scc__subsys.md#a0f9ce23b7e8f97ba9733542d5c743b75)

uint32\_t clk\_div

**Definition** clock\_control\_numaker.h:36

[numaker\_scc\_subsys::clk\_modidx](structnumaker__scc__subsys.md#a97179646f9df3ef16e7d3e79a16738b2)

uint32\_t clk\_modidx

**Definition** clock\_control\_numaker.h:34

[numaker\_scc\_subsys::clk\_src](structnumaker__scc__subsys.md#ab7b47761009d1e4ca7ef0f5f5af19999)

uint32\_t clk\_src

**Definition** clock\_control\_numaker.h:35

[numaker\_scc\_subsys::pcc](structnumaker__scc__subsys.md#ab9d9ea175b9ccb3a15e7e897a128021a)

struct numaker\_scc\_subsys::@015361254300117344271072222152047045156163314340::@007053104331100314203020363266244043337353117171 pcc

[numaker\_scc\_subsys::subsys\_id](structnumaker__scc__subsys.md#af8e2099977ecba2c53808fe8db4e041a)

uint32\_t subsys\_id

**Definition** clock\_control\_numaker.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_control\_numaker.h](clock__control__numaker_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
