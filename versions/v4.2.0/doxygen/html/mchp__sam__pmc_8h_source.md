---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mchp__sam__pmc_8h_source.html
original_path: doxygen/html/mchp__sam__pmc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp\_sam\_pmc.h

[Go to the documentation of this file.](mchp__sam__pmc_8h.md)

1/\*

2 \* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_MICROCHIP\_SAM\_PMC\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_MICROCHIP\_SAM\_PMC\_H\_

9

10#include <soc.h>

11#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

12#include <[zephyr/dt-bindings/clock/microchip\_sam\_pmc.h](microchip__sam__pmc_8h.md)>

13

[ 14](structsam__sckc__config.md)struct [sam\_sckc\_config](structsam__sckc__config.md) {

[ 15](structsam__sckc__config.md#a332b32859d73b961eb0f32f376390824) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [crystal\_osc](structsam__sckc__config.md#a332b32859d73b961eb0f32f376390824): 1;

[ 16](structsam__sckc__config.md#a9a634b76cc127423dbfcb2b86435eb96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved](structsam__sckc__config.md#a9a634b76cc127423dbfcb2b86435eb96): 31;

17};

18

[ 19](structsam__clk__cfg.md)struct [sam\_clk\_cfg](structsam__clk__cfg.md) {

[ 20](structsam__clk__cfg.md#a267eec7843a416198edf26c31db252e7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clock\_type](structsam__clk__cfg.md#a267eec7843a416198edf26c31db252e7);

[ 21](structsam__clk__cfg.md#af393258d1cf2fc592970658896075b17) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clock\_id](structsam__clk__cfg.md#af393258d1cf2fc592970658896075b17);

22};

23

24/\* Device constant configuration parameters \*/

[ 25](structsam__pmc__cfg.md)struct [sam\_pmc\_cfg](structsam__pmc__cfg.md) {

[ 26](structsam__pmc__cfg.md#aa2584519cb128e96715a6a01140f609c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const [reg](structsam__pmc__cfg.md#aa2584519cb128e96715a6a01140f609c);

[ 27](structsam__pmc__cfg.md#a0fc5ba6ce43a1f7b91d854ace83f59df) const struct [device](structdevice.md) \*[td\_slck](structsam__pmc__cfg.md#a0fc5ba6ce43a1f7b91d854ace83f59df);

[ 28](structsam__pmc__cfg.md#abd4cbbd2082fe579bc6edd3d4548f390) const struct [device](structdevice.md) \*[md\_slck](structsam__pmc__cfg.md#abd4cbbd2082fe579bc6edd3d4548f390);

[ 29](structsam__pmc__cfg.md#a8459cfb8ca7a99416e0c2e5e9a680481) const struct [device](structdevice.md) \*[main\_xtal](structsam__pmc__cfg.md#a8459cfb8ca7a99416e0c2e5e9a680481);

[ 30](structsam__pmc__cfg.md#a3029662f9fa5ca96c142a9564c44f4d2) const struct [sam\_sckc\_config](structsam__sckc__config.md) [td\_slck\_cfg](structsam__pmc__cfg.md#a3029662f9fa5ca96c142a9564c44f4d2);

[ 31](structsam__pmc__cfg.md#a149d058d1170af8eb75628dfd6b9cc92) const struct [sam\_sckc\_config](structsam__sckc__config.md) [md\_slck\_cfg](structsam__pmc__cfg.md#a149d058d1170af8eb75628dfd6b9cc92);

32};

33

34/\* Device run time data \*/

[ 35](structsam__pmc__data.md)struct [sam\_pmc\_data](structsam__pmc__data.md) {

[ 36](structsam__pmc__data.md#abdab335def8be1593fdac72a5092a77d) struct pmc\_data \*[pmc](structsam__pmc__data.md#abdab335def8be1593fdac72a5092a77d);

37};

38

[ 39](mchp__sam__pmc_8h.md#ae6ab16601edc5287a1657ff7bb1c8dbd)#define SAM\_DT\_CLOCK\_PMC\_CFG(clock, node\_id) { \

40 .clock\_type = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, \

41 clock, \

42 clock\_type), \

43 .clock\_id = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, \

44 clock, \

45 peripheral\_id) \

46 }

47

[ 48](mchp__sam__pmc_8h.md#a0f6e3f89dcfde77d27b2685220055109)#define SAM\_DT\_INST\_CLOCK\_PMC\_CFG(inst) SAM\_DT\_CLOCK\_PMC\_CFG(0, DT\_DRV\_INST(inst))

49

[ 50](mchp__sam__pmc_8h.md#adc7b9d880d6ebcf81b47eafc223e8512)#define SAM\_DT\_CLOCKS\_PMC\_CFG(node\_id) { \

51 LISTIFY(DT\_NUM\_CLOCKS(node\_id), \

52 SAM\_DT\_CLOCK\_PMC\_CFG, (,), node\_id) \

53 }

54

[ 55](mchp__sam__pmc_8h.md#af27b70e3c0fa178c3096748bb636b704)#define SAM\_DT\_INST\_CLOCKS\_PMC\_CFG(inst) SAM\_DT\_CLOCKS\_PMC\_CFG(DT\_DRV\_INST(inst))

56

57#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_MICROCHIP\_SAM\_PMC\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[microchip\_sam\_pmc.h](microchip__sam__pmc_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[sam\_clk\_cfg](structsam__clk__cfg.md)

**Definition** mchp\_sam\_pmc.h:19

[sam\_clk\_cfg::clock\_type](structsam__clk__cfg.md#a267eec7843a416198edf26c31db252e7)

uint32\_t clock\_type

**Definition** mchp\_sam\_pmc.h:20

[sam\_clk\_cfg::clock\_id](structsam__clk__cfg.md#af393258d1cf2fc592970658896075b17)

uint32\_t clock\_id

**Definition** mchp\_sam\_pmc.h:21

[sam\_pmc\_cfg](structsam__pmc__cfg.md)

**Definition** mchp\_sam\_pmc.h:25

[sam\_pmc\_cfg::td\_slck](structsam__pmc__cfg.md#a0fc5ba6ce43a1f7b91d854ace83f59df)

const struct device \* td\_slck

**Definition** mchp\_sam\_pmc.h:27

[sam\_pmc\_cfg::md\_slck\_cfg](structsam__pmc__cfg.md#a149d058d1170af8eb75628dfd6b9cc92)

const struct sam\_sckc\_config md\_slck\_cfg

**Definition** mchp\_sam\_pmc.h:31

[sam\_pmc\_cfg::td\_slck\_cfg](structsam__pmc__cfg.md#a3029662f9fa5ca96c142a9564c44f4d2)

const struct sam\_sckc\_config td\_slck\_cfg

**Definition** mchp\_sam\_pmc.h:30

[sam\_pmc\_cfg::main\_xtal](structsam__pmc__cfg.md#a8459cfb8ca7a99416e0c2e5e9a680481)

const struct device \* main\_xtal

**Definition** mchp\_sam\_pmc.h:29

[sam\_pmc\_cfg::reg](structsam__pmc__cfg.md#aa2584519cb128e96715a6a01140f609c)

uint32\_t \*const reg

**Definition** mchp\_sam\_pmc.h:26

[sam\_pmc\_cfg::md\_slck](structsam__pmc__cfg.md#abd4cbbd2082fe579bc6edd3d4548f390)

const struct device \* md\_slck

**Definition** mchp\_sam\_pmc.h:28

[sam\_pmc\_data](structsam__pmc__data.md)

**Definition** mchp\_sam\_pmc.h:35

[sam\_pmc\_data::pmc](structsam__pmc__data.md#abdab335def8be1593fdac72a5092a77d)

struct pmc\_data \* pmc

**Definition** mchp\_sam\_pmc.h:36

[sam\_sckc\_config](structsam__sckc__config.md)

**Definition** mchp\_sam\_pmc.h:14

[sam\_sckc\_config::crystal\_osc](structsam__sckc__config.md#a332b32859d73b961eb0f32f376390824)

uint32\_t crystal\_osc

**Definition** mchp\_sam\_pmc.h:15

[sam\_sckc\_config::reserved](structsam__sckc__config.md#a9a634b76cc127423dbfcb2b86435eb96)

uint32\_t reserved

**Definition** mchp\_sam\_pmc.h:16

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [mchp\_sam\_pmc.h](mchp__sam__pmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
