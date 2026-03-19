---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/renesas__ra__cgc_8h_source.html
original_path: doxygen/html/renesas__ra__cgc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_ra\_cgc.h

[Go to the documentation of this file.](renesas__ra__cgc_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RENESAS\_RA\_CGC\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RENESAS\_RA\_CGC\_H\_

8

9#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

10#include <[zephyr/dt-bindings/clock/ra\_clock.h](ra__clock_8h.md)>

11

[ 12](renesas__ra__cgc_8h.md#a69f75bb6ad2e7c3d22936754ba3bf5b5)#define RA\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR(node\_id, prop, default\_value) \

13 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(node\_id, okay), (DT\_PROP(node\_id, prop)), (default\_value))

14

[ 15](renesas__ra__cgc_8h.md#a45ba53a59830676d22f80b29165ae399)#define RA\_CGC\_CLK\_SRC(node\_id) \

16 COND\_CODE\_1(DT\_NODE\_HAS\_STATUS(node\_id, okay), \

17 (UTIL\_CAT(BSP\_CLOCKS\_SOURCE\_, DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN(node\_id))), \

18 (BSP\_CLOCKS\_CLOCK\_DISABLED))

19

[ 20](renesas__ra__cgc_8h.md#af54cadef83174db1f2180c65fb436c28)#define RA\_CGC\_CLK\_DIV(clk, prop, default\_value) \

21 UTIL\_CAT(RA\_CGC\_DIV\_, DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN(clk)) \

22 (RA\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR(clk, prop, default\_value))

23

[ 24](renesas__ra__cgc_8h.md#ac836d0409da1193de27a8c61510d06c5)#define RA\_CGC\_DIV\_BCLK(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 25](renesas__ra__cgc_8h.md#aa6e8ba963160224076dacac43db705d7)#define RA\_CGC\_DIV\_CANFDCLK(n) UTIL\_CAT(BSP\_CLOCKS\_CANFD\_CLOCK\_DIV\_, n)

[ 26](renesas__ra__cgc_8h.md#aae1620e152c33e3d4a95b5cac0cb1c76)#define RA\_CGC\_DIV\_CECCLK(n) UTIL\_CAT(BSP\_CLOCKS\_CEC\_CLOCK\_DIV\_, n)

[ 27](renesas__ra__cgc_8h.md#a8b169aba21f7e00cb80ffa0229cf0ca7)#define RA\_CGC\_DIV\_CLKOUT(n) UTIL\_CAT(BSP\_CLOCKS\_CLKOUT\_DIV\_, n)

[ 28](renesas__ra__cgc_8h.md#abf6b0bc9229f7b9b667662d5e7287af3)#define RA\_CGC\_DIV\_CPUCLK(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 29](renesas__ra__cgc_8h.md#a8006ac020337b43c9039290de93b237c)#define RA\_CGC\_DIV\_FCLK(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 30](renesas__ra__cgc_8h.md#ae414f33fc622f1eea25ed38b4e48b284)#define RA\_CGC\_DIV\_I3CCLK(n) UTIL\_CAT(BSP\_CLOCKS\_I3C\_CLOCK\_DIV\_, n)

[ 31](renesas__ra__cgc_8h.md#a152905c07ac6744e4dbcaa88cc44b7b0)#define RA\_CGC\_DIV\_ICLK(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 32](renesas__ra__cgc_8h.md#ade972ca4dc22a1438ae0ee8a7f0b1c86)#define RA\_CGC\_DIV\_LCDCLK(n) UTIL\_CAT(BSP\_CLOCKS\_LCD\_CLOCK\_DIV\_, n)

[ 33](renesas__ra__cgc_8h.md#a6e21efeff2e4b079ba56bf33524517d5)#define RA\_CGC\_DIV\_OCTASPICLK(n) UTIL\_CAT(BSP\_CLOCKS\_OCTA\_CLOCK\_DIV\_, n)

[ 34](renesas__ra__cgc_8h.md#a40a2d9224061ee4b25e98407ee60eecc)#define RA\_CGC\_DIV\_PCLKA(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 35](renesas__ra__cgc_8h.md#ad3881c28b08b0775b6596f7e1932f2ff)#define RA\_CGC\_DIV\_PCLKB(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 36](renesas__ra__cgc_8h.md#a38799ae63c6aef7b8f637826fe5de9fd)#define RA\_CGC\_DIV\_PCLKC(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 37](renesas__ra__cgc_8h.md#a775ccb80b8d68022e8e4a3e93f2d347c)#define RA\_CGC\_DIV\_PCLKD(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 38](renesas__ra__cgc_8h.md#aa8cde7ee7535ddd404a05ae72f598b28)#define RA\_CGC\_DIV\_PCLKE(n) UTIL\_CAT(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

[ 39](renesas__ra__cgc_8h.md#a0f6bd3b07d9c1c4e07daa28443c8148e)#define RA\_CGC\_DIV\_PLL(n) UTIL\_CAT(BSP\_CLOCKS\_PLL\_DIV\_, n)

[ 40](renesas__ra__cgc_8h.md#aa5fd2b712624e2c73aac2574a5ea6512)#define RA\_CGC\_DIV\_PLLP(n) UTIL\_CAT(BSP\_CLOCKS\_PLL\_DIV\_, n)

[ 41](renesas__ra__cgc_8h.md#a255f1f50393cf7f3396e1890b7728f49)#define RA\_CGC\_DIV\_PLLQ(n) UTIL\_CAT(BSP\_CLOCKS\_PLL\_DIV\_, n)

[ 42](renesas__ra__cgc_8h.md#ab1ea3ce0335620c286430c0af2de0b89)#define RA\_CGC\_DIV\_PLLR(n) UTIL\_CAT(BSP\_CLOCKS\_PLL\_DIV\_, n)

[ 43](renesas__ra__cgc_8h.md#ace4275eba4a646416ef6e0ffad3efafb)#define RA\_CGC\_DIV\_PLL2(n) UTIL\_CAT(BSP\_CLOCKS\_PLL\_DIV\_, n)

[ 44](renesas__ra__cgc_8h.md#a11dbb86891568e5f75f9666107aac1bc)#define RA\_CGC\_DIV\_PLL2P(n) UTIL\_CAT(BSP\_CLOCKS\_PLL\_DIV\_, n)

[ 45](renesas__ra__cgc_8h.md#a1dc330555e762496bb90f9d623c6bbfb)#define RA\_CGC\_DIV\_PLL2Q(n) UTIL\_CAT(BSP\_CLOCKS\_PLL\_DIV\_, n)

[ 46](renesas__ra__cgc_8h.md#a9e61fda937cc02e1484c64c0dbeb6dd5)#define RA\_CGC\_DIV\_PLL2R(n) UTIL\_CAT(BSP\_CLOCKS\_PLL\_DIV\_, n)

[ 47](renesas__ra__cgc_8h.md#af20a6aa81df58686419d3163430aa59f)#define RA\_CGC\_DIV\_SCICLK(n) UTIL\_CAT(BSP\_CLOCKS\_SCI\_CLOCK\_DIV\_, n)

[ 48](renesas__ra__cgc_8h.md#a28b424f22f72071af6fbe8351ad72101)#define RA\_CGC\_DIV\_SPICLK(n) UTIL\_CAT(BSP\_CLOCKS\_SPI\_CLOCK\_DIV\_, n)

[ 49](renesas__ra__cgc_8h.md#a944584d8d7372fad12f8e13bab00e7ae)#define RA\_CGC\_DIV\_U60CLK(n) UTIL\_CAT(BSP\_CLOCKS\_USB60\_CLOCK\_DIV\_, n)

[ 50](renesas__ra__cgc_8h.md#a90a5ab20631fff89d39980a144ec2ea0)#define RA\_CGC\_DIV\_UCLK(n) UTIL\_CAT(BSP\_CLOCKS\_USB\_CLOCK\_DIV\_, n)

51

[ 52](renesas__ra__cgc_8h.md#ac6d940bf68229ce58e586d99e88021ad)#define BSP\_CLOCKS\_SOURCE\_PLL BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL

[ 53](renesas__ra__cgc_8h.md#a80b3c5e721364e07c795d759e56bef5f)#define BSP\_CLOCKS\_SOURCE\_PLLP BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL

[ 54](renesas__ra__cgc_8h.md#a198180ae8a259e478c13cb667efdc036)#define BSP\_CLOCKS\_SOURCE\_PLLQ BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL1Q

[ 55](renesas__ra__cgc_8h.md#a9cf8b84320ad1c418e554c44d0ae324c)#define BSP\_CLOCKS\_SOURCE\_PLLR BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL1R

56

[ 57](renesas__ra__cgc_8h.md#a526d6007889c727bc820b23a8bd57eb1)#define BSP\_CLOCKS\_SOURCE\_PLL2 BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2

[ 58](renesas__ra__cgc_8h.md#a7d74f3dc378453283c5a2752d261a635)#define BSP\_CLOCKS\_SOURCE\_PLL2P BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2

[ 59](renesas__ra__cgc_8h.md#ae21c8ebb5bfd4160ced33343517cf755)#define BSP\_CLOCKS\_SOURCE\_PLL2Q BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2Q

[ 60](renesas__ra__cgc_8h.md#a2c9eb4860dc00767ec81567b7e1ef915)#define BSP\_CLOCKS\_SOURCE\_PLL2R BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2R

61

[ 62](renesas__ra__cgc_8h.md#ad56dead80f923b0b8840b3c84bdf65fa)#define BSP\_CLOCKS\_CLKOUT\_DIV\_1 (0)

[ 63](renesas__ra__cgc_8h.md#a46ed6e2dc58841f0b112003ed9f4a5db)#define BSP\_CLOCKS\_CLKOUT\_DIV\_2 (1)

[ 64](renesas__ra__cgc_8h.md#a2ef0885ff687beeb8c5ec867bb97424b)#define BSP\_CLOCKS\_CLKOUT\_DIV\_4 (2)

[ 65](renesas__ra__cgc_8h.md#a79d6afda43cf5f9f6246fdb28285fd8e)#define BSP\_CLOCKS\_CLKOUT\_DIV\_8 (3)

[ 66](renesas__ra__cgc_8h.md#ac15fa2c5d5533746dd002636063bbf17)#define BSP\_CLOCKS\_CLKOUT\_DIV\_16 (4)

[ 67](renesas__ra__cgc_8h.md#a58684d2331eb5cd218bbfc58254b27e7)#define BSP\_CLOCKS\_CLKOUT\_DIV\_32 (5)

[ 68](renesas__ra__cgc_8h.md#aae419122d7da67d550e5d93e8108c237)#define BSP\_CLOCKS\_CLKOUT\_DIV\_64 (6)

[ 69](renesas__ra__cgc_8h.md#a1541a9c2e367cea7a96da0d522d2c7eb)#define BSP\_CLOCKS\_CLKOUT\_DIV\_128 (7)

70

[ 71](structclock__control__ra__pclk__cfg.md)struct [clock\_control\_ra\_pclk\_cfg](structclock__control__ra__pclk__cfg.md) {

[ 72](structclock__control__ra__pclk__cfg.md#a7e4090da84776edb0db7f0eec18767a3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_src](structclock__control__ra__pclk__cfg.md#a7e4090da84776edb0db7f0eec18767a3);

[ 73](structclock__control__ra__pclk__cfg.md#a2ce24e482ea7557d197c87230eba0361) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clk\_div](structclock__control__ra__pclk__cfg.md#a2ce24e482ea7557d197c87230eba0361);

74};

75

[ 76](structclock__control__ra__subsys__cfg.md)struct [clock\_control\_ra\_subsys\_cfg](structclock__control__ra__subsys__cfg.md) {

[ 77](structclock__control__ra__subsys__cfg.md#accdec304bb04737be3f75f0df3a29023) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mstp](structclock__control__ra__subsys__cfg.md#accdec304bb04737be3f75f0df3a29023);

[ 78](structclock__control__ra__subsys__cfg.md#ad2dd15542bd355b716407bf9d9992f15) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stop\_bit](structclock__control__ra__subsys__cfg.md#ad2dd15542bd355b716407bf9d9992f15);

79};

80

81#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_RENESAS\_RA\_CGC\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[ra\_clock.h](ra__clock_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[clock\_control\_ra\_pclk\_cfg](structclock__control__ra__pclk__cfg.md)

**Definition** renesas\_ra\_cgc.h:71

[clock\_control\_ra\_pclk\_cfg::clk\_div](structclock__control__ra__pclk__cfg.md#a2ce24e482ea7557d197c87230eba0361)

uint32\_t clk\_div

**Definition** renesas\_ra\_cgc.h:73

[clock\_control\_ra\_pclk\_cfg::clk\_src](structclock__control__ra__pclk__cfg.md#a7e4090da84776edb0db7f0eec18767a3)

uint32\_t clk\_src

**Definition** renesas\_ra\_cgc.h:72

[clock\_control\_ra\_subsys\_cfg](structclock__control__ra__subsys__cfg.md)

**Definition** renesas\_ra\_cgc.h:76

[clock\_control\_ra\_subsys\_cfg::mstp](structclock__control__ra__subsys__cfg.md#accdec304bb04737be3f75f0df3a29023)

uint32\_t mstp

**Definition** renesas\_ra\_cgc.h:77

[clock\_control\_ra\_subsys\_cfg::stop\_bit](structclock__control__ra__subsys__cfg.md#ad2dd15542bd355b716407bf9d9992f15)

uint32\_t stop\_bit

**Definition** renesas\_ra\_cgc.h:78

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [renesas\_ra\_cgc.h](renesas__ra__cgc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
