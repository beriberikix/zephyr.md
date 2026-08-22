---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__rx__cgc_8h_source.html
original_path: doxygen/html/renesas__rx__cgc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rx\_cgc.h

[Go to the documentation of this file.](renesas__rx__cgc_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RENESAS\_RX\_CGC\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RENESAS\_RX\_CGC\_H\_

8

9#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

10#include <[zephyr/dt-bindings/clock/rx\_clock.h](rx__clock_8h.md)>

11

[ 12](renesas__rx__cgc_8h.md#a722b55a0a83757487eff84b93fe90964)#define RX\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR(node\_id, prop, default\_value) \

13 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(node\_id, okay), (DT\_PROP(node\_id, prop)), (default\_value))

14

[ 15](renesas__rx__cgc_8h.md#a7a7b76c8c7318a073b4f43f72d1d412f)#define RX\_CGC\_CLK\_SRC(node\_id) \

16 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(node\_id, okay), \

17 (UTIL\_CAT(RX\_CLOCKS\_SOURCE\_, DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN(node\_id))), \

18 (RX\_CLOCKS\_CLOCK\_DISABLED))

19

[ 20](structclock__control__rx__pclk__cfg.md)struct [clock\_control\_rx\_pclk\_cfg](structclock__control__rx__pclk__cfg.md) {

[ 21](structclock__control__rx__pclk__cfg.md#a46ba3c9011b9bfeb792db0017da55d5c) const struct [device](structdevice.md) \*[clock\_src\_dev](structclock__control__rx__pclk__cfg.md#a46ba3c9011b9bfeb792db0017da55d5c);

[ 22](structclock__control__rx__pclk__cfg.md#ad6b95060d8b16fc514451c9403facbe3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_div](structclock__control__rx__pclk__cfg.md#ad6b95060d8b16fc514451c9403facbe3);

23};

24

[ 25](structclock__control__rx__subsys__cfg.md)struct [clock\_control\_rx\_subsys\_cfg](structclock__control__rx__subsys__cfg.md) {

[ 26](structclock__control__rx__subsys__cfg.md#aa47beb43957995ad7eda8f5934ae307a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mstp](structclock__control__rx__subsys__cfg.md#aa47beb43957995ad7eda8f5934ae307a);

[ 27](structclock__control__rx__subsys__cfg.md#a8668364871caea64aab66294a2fb915e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stop\_bit](structclock__control__rx__subsys__cfg.md#a8668364871caea64aab66294a2fb915e);

28};

29

[ 30](structclock__control__rx__pll__cfg.md)struct [clock\_control\_rx\_pll\_cfg](structclock__control__rx__pll__cfg.md) {

[ 31](structclock__control__rx__pll__cfg.md#a06f3394bdaadb0f06cce23cd90c95061) const struct [device](structdevice.md) \*[clock\_dev](structclock__control__rx__pll__cfg.md#a06f3394bdaadb0f06cce23cd90c95061);

32};

33

[ 34](structclock__control__rx__pll__data.md)struct [clock\_control\_rx\_pll\_data](structclock__control__rx__pll__data.md) {

[ 35](structclock__control__rx__pll__data.md#a81def945f92f0b71412e6945378364fb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pll\_div](structclock__control__rx__pll__data.md#a81def945f92f0b71412e6945378364fb);

[ 36](structclock__control__rx__pll__data.md#aa8df23fd39a75b6a6a5fde7d4a657dd4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pll\_mul](structclock__control__rx__pll__data.md#aa8df23fd39a75b6a6a5fde7d4a657dd4);

37};

38

[ 39](structclock__control__rx__root__cfg.md)struct [clock\_control\_rx\_root\_cfg](structclock__control__rx__root__cfg.md) {

[ 40](structclock__control__rx__root__cfg.md#a3c551c54867d14793fc67b1321f93a92) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rate](structclock__control__rx__root__cfg.md#a3c551c54867d14793fc67b1321f93a92);

41};

42

43#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RENESAS\_RX\_CGC\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[rx\_clock.h](rx__clock_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[clock\_control\_rx\_pclk\_cfg](structclock__control__rx__pclk__cfg.md)

**Definition** renesas\_rx\_cgc.h:20

[clock\_control\_rx\_pclk\_cfg::clock\_src\_dev](structclock__control__rx__pclk__cfg.md#a46ba3c9011b9bfeb792db0017da55d5c)

const struct device \* clock\_src\_dev

**Definition** renesas\_rx\_cgc.h:21

[clock\_control\_rx\_pclk\_cfg::clk\_div](structclock__control__rx__pclk__cfg.md#ad6b95060d8b16fc514451c9403facbe3)

uint32\_t clk\_div

**Definition** renesas\_rx\_cgc.h:22

[clock\_control\_rx\_pll\_cfg](structclock__control__rx__pll__cfg.md)

**Definition** renesas\_rx\_cgc.h:30

[clock\_control\_rx\_pll\_cfg::clock\_dev](structclock__control__rx__pll__cfg.md#a06f3394bdaadb0f06cce23cd90c95061)

const struct device \* clock\_dev

**Definition** renesas\_rx\_cgc.h:31

[clock\_control\_rx\_pll\_data](structclock__control__rx__pll__data.md)

**Definition** renesas\_rx\_cgc.h:34

[clock\_control\_rx\_pll\_data::pll\_div](structclock__control__rx__pll__data.md#a81def945f92f0b71412e6945378364fb)

uint32\_t pll\_div

**Definition** renesas\_rx\_cgc.h:35

[clock\_control\_rx\_pll\_data::pll\_mul](structclock__control__rx__pll__data.md#aa8df23fd39a75b6a6a5fde7d4a657dd4)

uint32\_t pll\_mul

**Definition** renesas\_rx\_cgc.h:36

[clock\_control\_rx\_root\_cfg](structclock__control__rx__root__cfg.md)

**Definition** renesas\_rx\_cgc.h:39

[clock\_control\_rx\_root\_cfg::rate](structclock__control__rx__root__cfg.md#a3c551c54867d14793fc67b1321f93a92)

uint32\_t rate

**Definition** renesas\_rx\_cgc.h:40

[clock\_control\_rx\_subsys\_cfg](structclock__control__rx__subsys__cfg.md)

**Definition** renesas\_rx\_cgc.h:25

[clock\_control\_rx\_subsys\_cfg::stop\_bit](structclock__control__rx__subsys__cfg.md#a8668364871caea64aab66294a2fb915e)

uint32\_t stop\_bit

**Definition** renesas\_rx\_cgc.h:27

[clock\_control\_rx\_subsys\_cfg::mstp](structclock__control__rx__subsys__cfg.md#aa47beb43957995ad7eda8f5934ae307a)

uint32\_t mstp

**Definition** renesas\_rx\_cgc.h:26

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [renesas\_rx\_cgc.h](renesas__rx__cgc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
