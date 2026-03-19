---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas__ra__cgc_8h.html
original_path: doxygen/html/renesas__ra__cgc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_ra\_cgc.h File Reference

`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`  
`#include <[zephyr/dt-bindings/clock/ra_clock.h](ra__clock_8h_source.md)>`

[Go to the source code of this file.](renesas__ra__cgc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [clock\_control\_ra\_pclk\_cfg](structclock__control__ra__pclk__cfg.md) |
| struct | [clock\_control\_ra\_subsys\_cfg](structclock__control__ra__subsys__cfg.md) |

| Macros | |
| --- | --- |
| #define | [RA\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR](#a69f75bb6ad2e7c3d22936754ba3bf5b5)(node\_id, prop, default\_value) |
| #define | [RA\_CGC\_CLK\_SRC](#a45ba53a59830676d22f80b29165ae399)(node\_id) |
| #define | [RA\_CGC\_CLK\_DIV](#af54cadef83174db1f2180c65fb436c28)(clk, prop, default\_value) |
| #define | [RA\_CGC\_DIV\_BCLK](#ac836d0409da1193de27a8c61510d06c5)(n) |
| #define | [RA\_CGC\_DIV\_CANFDCLK](#aa6e8ba963160224076dacac43db705d7)(n) |
| #define | [RA\_CGC\_DIV\_CECCLK](#aae1620e152c33e3d4a95b5cac0cb1c76)(n) |
| #define | [RA\_CGC\_DIV\_CLKOUT](#a8b169aba21f7e00cb80ffa0229cf0ca7)(n) |
| #define | [RA\_CGC\_DIV\_CPUCLK](#abf6b0bc9229f7b9b667662d5e7287af3)(n) |
| #define | [RA\_CGC\_DIV\_FCLK](#a8006ac020337b43c9039290de93b237c)(n) |
| #define | [RA\_CGC\_DIV\_I3CCLK](#ae414f33fc622f1eea25ed38b4e48b284)(n) |
| #define | [RA\_CGC\_DIV\_ICLK](#a152905c07ac6744e4dbcaa88cc44b7b0)(n) |
| #define | [RA\_CGC\_DIV\_LCDCLK](#ade972ca4dc22a1438ae0ee8a7f0b1c86)(n) |
| #define | [RA\_CGC\_DIV\_OCTASPICLK](#a6e21efeff2e4b079ba56bf33524517d5)(n) |
| #define | [RA\_CGC\_DIV\_PCLKA](#a40a2d9224061ee4b25e98407ee60eecc)(n) |
| #define | [RA\_CGC\_DIV\_PCLKB](#ad3881c28b08b0775b6596f7e1932f2ff)(n) |
| #define | [RA\_CGC\_DIV\_PCLKC](#a38799ae63c6aef7b8f637826fe5de9fd)(n) |
| #define | [RA\_CGC\_DIV\_PCLKD](#a775ccb80b8d68022e8e4a3e93f2d347c)(n) |
| #define | [RA\_CGC\_DIV\_PCLKE](#aa8cde7ee7535ddd404a05ae72f598b28)(n) |
| #define | [RA\_CGC\_DIV\_PLL](#a0f6bd3b07d9c1c4e07daa28443c8148e)(n) |
| #define | [RA\_CGC\_DIV\_PLLP](#aa5fd2b712624e2c73aac2574a5ea6512)(n) |
| #define | [RA\_CGC\_DIV\_PLLQ](#a255f1f50393cf7f3396e1890b7728f49)(n) |
| #define | [RA\_CGC\_DIV\_PLLR](#ab1ea3ce0335620c286430c0af2de0b89)(n) |
| #define | [RA\_CGC\_DIV\_PLL2](#ace4275eba4a646416ef6e0ffad3efafb)(n) |
| #define | [RA\_CGC\_DIV\_PLL2P](#a11dbb86891568e5f75f9666107aac1bc)(n) |
| #define | [RA\_CGC\_DIV\_PLL2Q](#a1dc330555e762496bb90f9d623c6bbfb)(n) |
| #define | [RA\_CGC\_DIV\_PLL2R](#a9e61fda937cc02e1484c64c0dbeb6dd5)(n) |
| #define | [RA\_CGC\_DIV\_SCICLK](#af20a6aa81df58686419d3163430aa59f)(n) |
| #define | [RA\_CGC\_DIV\_SPICLK](#a28b424f22f72071af6fbe8351ad72101)(n) |
| #define | [RA\_CGC\_DIV\_U60CLK](#a944584d8d7372fad12f8e13bab00e7ae)(n) |
| #define | [RA\_CGC\_DIV\_UCLK](#a90a5ab20631fff89d39980a144ec2ea0)(n) |
| #define | [BSP\_CLOCKS\_SOURCE\_PLL](#ac6d940bf68229ce58e586d99e88021ad)   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL |
| #define | [BSP\_CLOCKS\_SOURCE\_PLLP](#a80b3c5e721364e07c795d759e56bef5f)   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL |
| #define | [BSP\_CLOCKS\_SOURCE\_PLLQ](#a198180ae8a259e478c13cb667efdc036)   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL1Q |
| #define | [BSP\_CLOCKS\_SOURCE\_PLLR](#a9cf8b84320ad1c418e554c44d0ae324c)   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL1R |
| #define | [BSP\_CLOCKS\_SOURCE\_PLL2](#a526d6007889c727bc820b23a8bd57eb1)   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2 |
| #define | [BSP\_CLOCKS\_SOURCE\_PLL2P](#a7d74f3dc378453283c5a2752d261a635)   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2 |
| #define | [BSP\_CLOCKS\_SOURCE\_PLL2Q](#ae21c8ebb5bfd4160ced33343517cf755)   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2Q |
| #define | [BSP\_CLOCKS\_SOURCE\_PLL2R](#a2c9eb4860dc00767ec81567b7e1ef915)   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2R |
| #define | [BSP\_CLOCKS\_CLKOUT\_DIV\_1](#ad56dead80f923b0b8840b3c84bdf65fa)   (0) |
| #define | [BSP\_CLOCKS\_CLKOUT\_DIV\_2](#a46ed6e2dc58841f0b112003ed9f4a5db)   (1) |
| #define | [BSP\_CLOCKS\_CLKOUT\_DIV\_4](#a2ef0885ff687beeb8c5ec867bb97424b)   (2) |
| #define | [BSP\_CLOCKS\_CLKOUT\_DIV\_8](#a79d6afda43cf5f9f6246fdb28285fd8e)   (3) |
| #define | [BSP\_CLOCKS\_CLKOUT\_DIV\_16](#ac15fa2c5d5533746dd002636063bbf17)   (4) |
| #define | [BSP\_CLOCKS\_CLKOUT\_DIV\_32](#a58684d2331eb5cd218bbfc58254b27e7)   (5) |
| #define | [BSP\_CLOCKS\_CLKOUT\_DIV\_64](#aae419122d7da67d550e5d93e8108c237)   (6) |
| #define | [BSP\_CLOCKS\_CLKOUT\_DIV\_128](#a1541a9c2e367cea7a96da0d522d2c7eb)   (7) |

## Macro Definition Documentation

## [◆ ](#ad56dead80f923b0b8840b3c84bdf65fa)BSP\_CLOCKS\_CLKOUT\_DIV\_1

| #define BSP\_CLOCKS\_CLKOUT\_DIV\_1   (0) |
| --- |

## [◆ ](#a1541a9c2e367cea7a96da0d522d2c7eb)BSP\_CLOCKS\_CLKOUT\_DIV\_128

| #define BSP\_CLOCKS\_CLKOUT\_DIV\_128   (7) |
| --- |

## [◆ ](#ac15fa2c5d5533746dd002636063bbf17)BSP\_CLOCKS\_CLKOUT\_DIV\_16

| #define BSP\_CLOCKS\_CLKOUT\_DIV\_16   (4) |
| --- |

## [◆ ](#a46ed6e2dc58841f0b112003ed9f4a5db)BSP\_CLOCKS\_CLKOUT\_DIV\_2

| #define BSP\_CLOCKS\_CLKOUT\_DIV\_2   (1) |
| --- |

## [◆ ](#a58684d2331eb5cd218bbfc58254b27e7)BSP\_CLOCKS\_CLKOUT\_DIV\_32

| #define BSP\_CLOCKS\_CLKOUT\_DIV\_32   (5) |
| --- |

## [◆ ](#a2ef0885ff687beeb8c5ec867bb97424b)BSP\_CLOCKS\_CLKOUT\_DIV\_4

| #define BSP\_CLOCKS\_CLKOUT\_DIV\_4   (2) |
| --- |

## [◆ ](#aae419122d7da67d550e5d93e8108c237)BSP\_CLOCKS\_CLKOUT\_DIV\_64

| #define BSP\_CLOCKS\_CLKOUT\_DIV\_64   (6) |
| --- |

## [◆ ](#a79d6afda43cf5f9f6246fdb28285fd8e)BSP\_CLOCKS\_CLKOUT\_DIV\_8

| #define BSP\_CLOCKS\_CLKOUT\_DIV\_8   (3) |
| --- |

## [◆ ](#ac6d940bf68229ce58e586d99e88021ad)BSP\_CLOCKS\_SOURCE\_PLL

| #define BSP\_CLOCKS\_SOURCE\_PLL   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL |
| --- |

## [◆ ](#a526d6007889c727bc820b23a8bd57eb1)BSP\_CLOCKS\_SOURCE\_PLL2

| #define BSP\_CLOCKS\_SOURCE\_PLL2   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2 |
| --- |

## [◆ ](#a7d74f3dc378453283c5a2752d261a635)BSP\_CLOCKS\_SOURCE\_PLL2P

| #define BSP\_CLOCKS\_SOURCE\_PLL2P   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2 |
| --- |

## [◆ ](#ae21c8ebb5bfd4160ced33343517cf755)BSP\_CLOCKS\_SOURCE\_PLL2Q

| #define BSP\_CLOCKS\_SOURCE\_PLL2Q   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2Q |
| --- |

## [◆ ](#a2c9eb4860dc00767ec81567b7e1ef915)BSP\_CLOCKS\_SOURCE\_PLL2R

| #define BSP\_CLOCKS\_SOURCE\_PLL2R   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL2R |
| --- |

## [◆ ](#a80b3c5e721364e07c795d759e56bef5f)BSP\_CLOCKS\_SOURCE\_PLLP

| #define BSP\_CLOCKS\_SOURCE\_PLLP   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL |
| --- |

## [◆ ](#a198180ae8a259e478c13cb667efdc036)BSP\_CLOCKS\_SOURCE\_PLLQ

| #define BSP\_CLOCKS\_SOURCE\_PLLQ   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL1Q |
| --- |

## [◆ ](#a9cf8b84320ad1c418e554c44d0ae324c)BSP\_CLOCKS\_SOURCE\_PLLR

| #define BSP\_CLOCKS\_SOURCE\_PLLR   BSP\_CLOCKS\_SOURCE\_CLOCK\_PLL1R |
| --- |

## [◆ ](#af54cadef83174db1f2180c65fb436c28)RA\_CGC\_CLK\_DIV

| #define RA\_CGC\_CLK\_DIV | ( |  | *clk*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(RA\_CGC\_DIV\_, [DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN](group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b)(clk)) \

([RA\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR](#a69f75bb6ad2e7c3d22936754ba3bf5b5)(clk, prop, default\_value))

[DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN](group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b)

#define DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN(node\_id)

Like DT\_NODE\_FULL\_NAME\_TOKEN(), but uppercased.

**Definition** devicetree.h:623

[RA\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR](#a69f75bb6ad2e7c3d22936754ba3bf5b5)

#define RA\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR(node\_id, prop, default\_value)

**Definition** renesas\_ra\_cgc.h:12

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

## [◆ ](#a45ba53a59830676d22f80b29165ae399)RA\_CGC\_CLK\_SRC

| #define RA\_CGC\_CLK\_SRC | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_STATUS](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, okay), \

([UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SOURCE\_, [DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN](group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b)(node\_id))), \

(BSP\_CLOCKS\_CLOCK\_DISABLED))

[DT\_NODE\_HAS\_STATUS](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)

#define DT\_NODE\_HAS\_STATUS(node\_id, status)

Does a node identifier refer to a node with a status?

**Definition** devicetree.h:3667

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

## [◆ ](#ac836d0409da1193de27a8c61510d06c5)RA\_CGC\_DIV\_BCLK

| #define RA\_CGC\_DIV\_BCLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#aa6e8ba963160224076dacac43db705d7)RA\_CGC\_DIV\_CANFDCLK

| #define RA\_CGC\_DIV\_CANFDCLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_CANFD\_CLOCK\_DIV\_, n)

## [◆ ](#aae1620e152c33e3d4a95b5cac0cb1c76)RA\_CGC\_DIV\_CECCLK

| #define RA\_CGC\_DIV\_CECCLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_CEC\_CLOCK\_DIV\_, n)

## [◆ ](#a8b169aba21f7e00cb80ffa0229cf0ca7)RA\_CGC\_DIV\_CLKOUT

| #define RA\_CGC\_DIV\_CLKOUT | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_CLKOUT\_DIV\_, n)

## [◆ ](#abf6b0bc9229f7b9b667662d5e7287af3)RA\_CGC\_DIV\_CPUCLK

| #define RA\_CGC\_DIV\_CPUCLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#a8006ac020337b43c9039290de93b237c)RA\_CGC\_DIV\_FCLK

| #define RA\_CGC\_DIV\_FCLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#ae414f33fc622f1eea25ed38b4e48b284)RA\_CGC\_DIV\_I3CCLK

| #define RA\_CGC\_DIV\_I3CCLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_I3C\_CLOCK\_DIV\_, n)

## [◆ ](#a152905c07ac6744e4dbcaa88cc44b7b0)RA\_CGC\_DIV\_ICLK

| #define RA\_CGC\_DIV\_ICLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#ade972ca4dc22a1438ae0ee8a7f0b1c86)RA\_CGC\_DIV\_LCDCLK

| #define RA\_CGC\_DIV\_LCDCLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_LCD\_CLOCK\_DIV\_, n)

## [◆ ](#a6e21efeff2e4b079ba56bf33524517d5)RA\_CGC\_DIV\_OCTASPICLK

| #define RA\_CGC\_DIV\_OCTASPICLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_OCTA\_CLOCK\_DIV\_, n)

## [◆ ](#a40a2d9224061ee4b25e98407ee60eecc)RA\_CGC\_DIV\_PCLKA

| #define RA\_CGC\_DIV\_PCLKA | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#ad3881c28b08b0775b6596f7e1932f2ff)RA\_CGC\_DIV\_PCLKB

| #define RA\_CGC\_DIV\_PCLKB | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#a38799ae63c6aef7b8f637826fe5de9fd)RA\_CGC\_DIV\_PCLKC

| #define RA\_CGC\_DIV\_PCLKC | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#a775ccb80b8d68022e8e4a3e93f2d347c)RA\_CGC\_DIV\_PCLKD

| #define RA\_CGC\_DIV\_PCLKD | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#aa8cde7ee7535ddd404a05ae72f598b28)RA\_CGC\_DIV\_PCLKE

| #define RA\_CGC\_DIV\_PCLKE | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SYS\_CLOCK\_DIV\_, n)

## [◆ ](#a0f6bd3b07d9c1c4e07daa28443c8148e)RA\_CGC\_DIV\_PLL

| #define RA\_CGC\_DIV\_PLL | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_PLL\_DIV\_, n)

## [◆ ](#ace4275eba4a646416ef6e0ffad3efafb)RA\_CGC\_DIV\_PLL2

| #define RA\_CGC\_DIV\_PLL2 | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_PLL\_DIV\_, n)

## [◆ ](#a11dbb86891568e5f75f9666107aac1bc)RA\_CGC\_DIV\_PLL2P

| #define RA\_CGC\_DIV\_PLL2P | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_PLL\_DIV\_, n)

## [◆ ](#a1dc330555e762496bb90f9d623c6bbfb)RA\_CGC\_DIV\_PLL2Q

| #define RA\_CGC\_DIV\_PLL2Q | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_PLL\_DIV\_, n)

## [◆ ](#a9e61fda937cc02e1484c64c0dbeb6dd5)RA\_CGC\_DIV\_PLL2R

| #define RA\_CGC\_DIV\_PLL2R | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_PLL\_DIV\_, n)

## [◆ ](#aa5fd2b712624e2c73aac2574a5ea6512)RA\_CGC\_DIV\_PLLP

| #define RA\_CGC\_DIV\_PLLP | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_PLL\_DIV\_, n)

## [◆ ](#a255f1f50393cf7f3396e1890b7728f49)RA\_CGC\_DIV\_PLLQ

| #define RA\_CGC\_DIV\_PLLQ | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_PLL\_DIV\_, n)

## [◆ ](#ab1ea3ce0335620c286430c0af2de0b89)RA\_CGC\_DIV\_PLLR

| #define RA\_CGC\_DIV\_PLLR | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_PLL\_DIV\_, n)

## [◆ ](#af20a6aa81df58686419d3163430aa59f)RA\_CGC\_DIV\_SCICLK

| #define RA\_CGC\_DIV\_SCICLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SCI\_CLOCK\_DIV\_, n)

## [◆ ](#a28b424f22f72071af6fbe8351ad72101)RA\_CGC\_DIV\_SPICLK

| #define RA\_CGC\_DIV\_SPICLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_SPI\_CLOCK\_DIV\_, n)

## [◆ ](#a944584d8d7372fad12f8e13bab00e7ae)RA\_CGC\_DIV\_U60CLK

| #define RA\_CGC\_DIV\_U60CLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_USB60\_CLOCK\_DIV\_, n)

## [◆ ](#a90a5ab20631fff89d39980a144ec2ea0)RA\_CGC\_DIV\_UCLK

| #define RA\_CGC\_DIV\_UCLK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BSP\_CLOCKS\_USB\_CLOCK\_DIV\_, n)

## [◆ ](#a69f75bb6ad2e7c3d22936754ba3bf5b5)RA\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR

| #define RA\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_STATUS](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, okay), ([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, prop)), (default\_value))

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [renesas\_ra\_cgc.h](renesas__ra__cgc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
