---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32__clock__control_8h.html
original_path: doxygen/html/stm32__clock__control_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_clock\_control.h File Reference

`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`  
`#include <[zephyr/dt-bindings/clock/stm32_clock.h](stm32__clock_8h_source.md)>`

[Go to the source code of this file.](stm32__clock__control_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [stm32\_pclken](structstm32__pclken.md) |
|  | Driver structure definition. [More...](structstm32__pclken.md#details) |

| Macros | |
| --- | --- |
| #define | [STM32\_CLOCK\_CONTROL\_NODE](#ad33dc3d92546f9a4162a65a06ac6c673)   [DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc) |
|  | Common clock control device node for all STM32 chips. |
| #define | [STM32\_AHB\_PRESCALER](#a38a0117c88924c6e1beca37e6cdea56b)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb\_prescaler) |
|  | RCC node related symbols. |
| #define | [STM32\_APB1\_PRESCALER](#a7af7ec37fc9d13d8d3bd6c3193ac8660)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb1\_prescaler) |
| #define | [STM32\_APB2\_PRESCALER](#ad82f77d7d85845342bfa613557b1f569)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb2\_prescaler) |
| #define | [STM32\_APB3\_PRESCALER](#ad1ffa671b55ad88e624ed9b7c4a22839)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb3\_prescaler) |
| #define | [STM32\_APB4\_PRESCALER](#adf8be1edd443c074679ad6b2ae7d19ed)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb4\_prescaler) |
| #define | [STM32\_APB5\_PRESCALER](#aa3510cdd90c9cc8b34933954f6e71caa)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb5\_prescaler) |
| #define | [STM32\_APB7\_PRESCALER](#a5b3ff33cd4a1ac4c8acfbe1ca921b9c3)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb7\_prescaler) |
| #define | [STM32\_AHB3\_PRESCALER](#afca170bc72a77d8905b6c2ca0cce9e7b)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb3\_prescaler) |
| #define | [STM32\_AHB4\_PRESCALER](#a3da9fd6fe11ceb8c2225e43eb2556d2d)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb4\_prescaler) |
| #define | [STM32\_AHB5\_PRESCALER](#aeb1fabf85560ccd6cc1c0bdb34c86ec2)   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb5\_prescaler, 1) |
| #define | [STM32\_CPU1\_PRESCALER](#a18dc4749249030d371007b5135f5af54)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), cpu1\_prescaler) |
| #define | [STM32\_CPU2\_PRESCALER](#a4f1975635dc6244f98263636c44f3942)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), cpu2\_prescaler) |
| #define | [STM32\_FLASH\_PRESCALER](#ac3274b70aee7aff6282eaa77ca819f27)   STM32\_CORE\_PRESCALER |
| #define | [STM32\_ADC\_PRESCALER](#a29ef6b98c22a522cde9f7dab5b11ace0)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), adc\_prescaler) |
| #define | [STM32\_ADC12\_PRESCALER](#a35954cadc11af5ee499918be312acf38)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), adc12\_prescaler) |
| #define | [STM32\_ADC34\_PRESCALER](#a1cae4646086d8f855b72d55fee1483ad)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), adc34\_prescaler) |
| #define | [STM32\_D1CPRE](#a51967fd4dcf9ec8fe8e7250b5af32c87)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d1cpre) |
|  | STM2H7RS specific RCC dividers. |
| #define | [STM32\_HPRE](#a035ea0d8259c0f89306c6a7d344705f2)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), hpre) |
| #define | [STM32\_D2PPRE1](#a844064bd8ccafb5df4bf02748840491d)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d2ppre1) |
| #define | [STM32\_D2PPRE2](#a50394a7e040433c738fc7e9f03b7aff3)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d2ppre2) |
| #define | [STM32\_D1PPRE](#a02a098a3296751f55ea349faecff7bd5)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d1ppre) |
| #define | [STM32\_D3PPRE](#a9dd9b0e8ef84e6ff033a707b2a0ec231)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d3ppre) |
| #define | [STM32\_AHB5\_DIV](#aea3d7b8e3adedef5f93cdb38852a8097)   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb5\_div) |
|  | STM2WBA specifics RCC dividers. |
| #define | [DT\_RCC\_CLOCKS\_CTRL](#ad9bff8a9cfbe0dbe0db73d077cb7a227)   [DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc)) |
| #define | [STM32\_LSE\_ENABLED](#a05b49e91f478558d33b2b862718758fa)   0 |
|  | PLL node related symbols. |
| #define | [STM32\_LSE\_FREQ](#aedfe731de4f32e8dacd027bb115ca0e9)   0 |
| #define | [STM32\_LSE\_DRIVING](#aead1c5c5ac685af96410f4883f7e988b)   0 |
| #define | [STM32\_LSE\_BYPASS](#a94745d7699b62ef9e7f8bbfbc6803727)   0 |
| #define | [STM32\_MSIS\_ENABLED](#a1a83a4c9a806689ac963e2ea8b142fda)   0 |
| #define | [STM32\_MSIS\_RANGE](#a0109485d9cfd70782ce6aff604399330)   0 |
| #define | [STM32\_MSIS\_PLL\_MODE](#a02f0311b8e9c41a004ed355aff37a7b3)   0 |
| #define | [STM32\_MSIK\_ENABLED](#a379e09d2e380483155b0ef8cc39d490b)   0 |
| #define | [STM32\_MSIK\_RANGE](#a2fb4bc355d7e69e6b676794d0ab4cbba)   0 |
| #define | [STM32\_MSIK\_PLL\_MODE](#a67d63326f5ebe1b249eb56b227aecb29)   0 |
| #define | [STM32\_CSI\_FREQ](#a2110dbb73ce08ba40555f1d95b50ce5c)   0 |
| #define | [STM32\_LSI\_FREQ](#ae4ad7f2e4844901d753a91c1ba5c58c5)   0 |
| #define | [STM32\_HSI\_DIV\_ENABLED](#aa67c0b4d532b58d78b12d36ae6817912)   0 |
| #define | [STM32\_HSI\_DIVISOR](#a2cc52c346227b2dfb91e1ab5aeda586c)   1 |
| #define | [STM32\_HSI\_FREQ](#af906386de1fde7ab0894971723a0a801)   0 |
| #define | [STM32\_HSE\_FREQ](#a7c3796ef481224c9e2f7516853677ec9)   0 |
| #define | [STM32\_CLOCK\_INFO](#aa1b0949b4c58d57dcd2e979320cbed0a)(clk\_index, node\_id) |
|  | Device tree clocks helpers. |
| #define | [STM32\_DT\_CLOCKS](#a9eb57b349f41edec11ff52a78015aea9)(node\_id) |
| #define | [STM32\_DT\_INST\_CLOCKS](#a693176c2c60364d327aa5768ebfac185)(inst) |
| #define | [STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT](#a38559b31633eca5475b73b8a88df1fcd)(inst) |
| #define | [STM32\_DT\_INST\_DEV\_DOMAIN\_CLOCK\_SUPPORT](#aac932dfd992b11d479edf2a2d5e8de47)   ([DT\_INST\_FOREACH\_STATUS\_OKAY](group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)([STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT](#a38559b31633eca5475b73b8a88df1fcd)) 0) |
| #define | [STM32\_DOMAIN\_CLOCK\_SUPPORT](#a8743160d8765b466f8ac6a89efaa9dbc)(id) |
| #define | [STM32\_DT\_DEV\_DOMAIN\_CLOCK\_SUPPORT](#a7951b8025683529eebdd415d6b65688b)   ([DT\_FOREACH\_STATUS\_OKAY](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)([STM32\_DOMAIN\_CLOCK\_SUPPORT](#a8743160d8765b466f8ac6a89efaa9dbc)) 0) |
| #define | [STM32\_DT\_CLKSEL\_REG\_GET](#a932d2b05943fc3511f0ad82f4e10c98a)(clock) |
|  | Clock source binding accessors. |
| #define | [STM32\_DT\_CLKSEL\_SHIFT\_GET](#a721bbde6ed4c76019fba67677e359c05)(clock) |
|  | Obtain position field from clock source selection configuration. |
| #define | [STM32\_DT\_CLKSEL\_MASK\_GET](#ad2c6955f07a96ff6ffecf2b1b267de2c)(clock) |
|  | Obtain mask field from clock source selection configuration. |
| #define | [STM32\_DT\_CLKSEL\_VAL\_GET](#aecf915cbdbf64d743b6ccb020a905abe)(clock) |
|  | Obtain value field from clock source selection configuration. |

## Macro Definition Documentation

## [◆ ](#ad9bff8a9cfbe0dbe0db73d077cb7a227)DT\_RCC\_CLOCKS\_CTRL

| #define DT\_RCC\_CLOCKS\_CTRL   [DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc)) |
| --- |

## [◆ ](#a35954cadc11af5ee499918be312acf38)STM32\_ADC12\_PRESCALER

| #define STM32\_ADC12\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), adc12\_prescaler) |
| --- |

## [◆ ](#a1cae4646086d8f855b72d55fee1483ad)STM32\_ADC34\_PRESCALER

| #define STM32\_ADC34\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), adc34\_prescaler) |
| --- |

## [◆ ](#a29ef6b98c22a522cde9f7dab5b11ace0)STM32\_ADC\_PRESCALER

| #define STM32\_ADC\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), adc\_prescaler) |
| --- |

## [◆ ](#afca170bc72a77d8905b6c2ca0cce9e7b)STM32\_AHB3\_PRESCALER

| #define STM32\_AHB3\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb3\_prescaler) |
| --- |

## [◆ ](#a3da9fd6fe11ceb8c2225e43eb2556d2d)STM32\_AHB4\_PRESCALER

| #define STM32\_AHB4\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb4\_prescaler) |
| --- |

## [◆ ](#aea3d7b8e3adedef5f93cdb38852a8097)STM32\_AHB5\_DIV

| #define STM32\_AHB5\_DIV   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb5\_div) |
| --- |

STM2WBA specifics RCC dividers.

## [◆ ](#aeb1fabf85560ccd6cc1c0bdb34c86ec2)STM32\_AHB5\_PRESCALER

| #define STM32\_AHB5\_PRESCALER   [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb5\_prescaler, 1) |
| --- |

## [◆ ](#a38a0117c88924c6e1beca37e6cdea56b)STM32\_AHB\_PRESCALER

| #define STM32\_AHB\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), ahb\_prescaler) |
| --- |

RCC node related symbols.

## [◆ ](#a7af7ec37fc9d13d8d3bd6c3193ac8660)STM32\_APB1\_PRESCALER

| #define STM32\_APB1\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb1\_prescaler) |
| --- |

## [◆ ](#ad82f77d7d85845342bfa613557b1f569)STM32\_APB2\_PRESCALER

| #define STM32\_APB2\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb2\_prescaler) |
| --- |

## [◆ ](#ad1ffa671b55ad88e624ed9b7c4a22839)STM32\_APB3\_PRESCALER

| #define STM32\_APB3\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb3\_prescaler) |
| --- |

## [◆ ](#adf8be1edd443c074679ad6b2ae7d19ed)STM32\_APB4\_PRESCALER

| #define STM32\_APB4\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb4\_prescaler) |
| --- |

## [◆ ](#aa3510cdd90c9cc8b34933954f6e71caa)STM32\_APB5\_PRESCALER

| #define STM32\_APB5\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb5\_prescaler) |
| --- |

## [◆ ](#a5b3ff33cd4a1ac4c8acfbe1ca921b9c3)STM32\_APB7\_PRESCALER

| #define STM32\_APB7\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), apb7\_prescaler) |
| --- |

## [◆ ](#ad33dc3d92546f9a4162a65a06ac6c673)STM32\_CLOCK\_CONTROL\_NODE

| #define STM32\_CLOCK\_CONTROL\_NODE   [DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc) |
| --- |

Common clock control device node for all STM32 chips.

## [◆ ](#aa1b0949b4c58d57dcd2e979320cbed0a)STM32\_CLOCK\_INFO

| #define STM32\_CLOCK\_INFO | ( |  | *clk\_index*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

**Value:**

{ \

.enr = [DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, clk\_index, bits), \

.bus = [DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, clk\_index, bus) & \

GENMASK([STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0) - 1, 0), \

.div = [DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, clk\_index, bus) >> \

[STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0), \

}

[DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)

#define DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, idx, cell)

Get a clock specifier's cell value at an index.

**Definition** clocks.h:207

[STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0)

#define STM32\_CLOCK\_DIV\_SHIFT

**Definition** stm32\_clock.h:27

Device tree clocks helpers.

## [◆ ](#a18dc4749249030d371007b5135f5af54)STM32\_CPU1\_PRESCALER

| #define STM32\_CPU1\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), cpu1\_prescaler) |
| --- |

## [◆ ](#a4f1975635dc6244f98263636c44f3942)STM32\_CPU2\_PRESCALER

| #define STM32\_CPU2\_PRESCALER   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), cpu2\_prescaler) |
| --- |

## [◆ ](#a2110dbb73ce08ba40555f1d95b50ce5c)STM32\_CSI\_FREQ

| #define STM32\_CSI\_FREQ   0 |
| --- |

## [◆ ](#a51967fd4dcf9ec8fe8e7250b5af32c87)STM32\_D1CPRE

| #define STM32\_D1CPRE   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d1cpre) |
| --- |

STM2H7RS specific RCC dividers.

## [◆ ](#a02a098a3296751f55ea349faecff7bd5)STM32\_D1PPRE

| #define STM32\_D1PPRE   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d1ppre) |
| --- |

## [◆ ](#a844064bd8ccafb5df4bf02748840491d)STM32\_D2PPRE1

| #define STM32\_D2PPRE1   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d2ppre1) |
| --- |

## [◆ ](#a50394a7e040433c738fc7e9f03b7aff3)STM32\_D2PPRE2

| #define STM32\_D2PPRE2   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d2ppre2) |
| --- |

## [◆ ](#a9dd9b0e8ef84e6ff033a707b2a0ec231)STM32\_D3PPRE

| #define STM32\_D3PPRE   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), d3ppre) |
| --- |

## [◆ ](#a38559b31633eca5475b73b8a88df1fcd)STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT

| #define STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_INST\_CLOCKS\_HAS\_IDX](group__devicetree-clocks.md#gaf8ebb6ccd4915cc4069e92f804fb63ac)(inst, 1) ||

[DT\_INST\_CLOCKS\_HAS\_IDX](group__devicetree-clocks.md#gaf8ebb6ccd4915cc4069e92f804fb63ac)

#define DT\_INST\_CLOCKS\_HAS\_IDX(inst, idx)

Equivalent to DT\_CLOCKS\_HAS\_IDX(DT\_DRV\_INST(inst), idx).

**Definition** clocks.h:261

## [◆ ](#a8743160d8765b466f8ac6a89efaa9dbc)STM32\_DOMAIN\_CLOCK\_SUPPORT

| #define STM32\_DOMAIN\_CLOCK\_SUPPORT | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_CLOCKS\_HAS\_IDX](group__devicetree-clocks.md#gabfdf51e2b14c05e84366cff1bb056da0)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(id), 1) ||

[DT\_CLOCKS\_HAS\_IDX](group__devicetree-clocks.md#gabfdf51e2b14c05e84366cff1bb056da0)

#define DT\_CLOCKS\_HAS\_IDX(node\_id, idx)

Test if a node has a clocks phandle-array property at a given index.

**Definition** clocks.h:52

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

## [◆ ](#ad2c6955f07a96ff6ffecf2b1b267de2c)STM32\_DT\_CLKSEL\_MASK\_GET

| #define STM32\_DT\_CLKSEL\_MASK\_GET | ( |  | *clock* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((clock) >> [STM32\_DT\_CLKSEL\_MASK\_SHIFT](stm32__common__clocks_8h.md#a627de44bae59bdf8febc6518bcaeb595)) & [STM32\_DT\_CLKSEL\_MASK\_MASK](stm32__common__clocks_8h.md#afaa23be867f51da7ddb8b72ef429e51a))

[STM32\_DT\_CLKSEL\_MASK\_SHIFT](stm32__common__clocks_8h.md#a627de44bae59bdf8febc6518bcaeb595)

#define STM32\_DT\_CLKSEL\_MASK\_SHIFT

**Definition** stm32\_common\_clocks.h:29

[STM32\_DT\_CLKSEL\_MASK\_MASK](stm32__common__clocks_8h.md#afaa23be867f51da7ddb8b72ef429e51a)

#define STM32\_DT\_CLKSEL\_MASK\_MASK

**Definition** stm32\_common\_clocks.h:28

Obtain mask field from clock source selection configuration.

Parameters
:   | clock | Clock bit field value. |
    | --- | --- |

## [◆ ](#a932d2b05943fc3511f0ad82f4e10c98a)STM32\_DT\_CLKSEL\_REG\_GET

| #define STM32\_DT\_CLKSEL\_REG\_GET | ( |  | *clock* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((clock) >> [STM32\_DT\_CLKSEL\_REG\_SHIFT](stm32__common__clocks_8h.md#a007f65a597867a03a6dc9b1e73d27a2d)) & [STM32\_DT\_CLKSEL\_REG\_MASK](stm32__common__clocks_8h.md#a9ad0be6cd421f8b608f74a3676bf9d6d))

[STM32\_DT\_CLKSEL\_REG\_SHIFT](stm32__common__clocks_8h.md#a007f65a597867a03a6dc9b1e73d27a2d)

#define STM32\_DT\_CLKSEL\_REG\_SHIFT

**Definition** stm32\_common\_clocks.h:25

[STM32\_DT\_CLKSEL\_REG\_MASK](stm32__common__clocks_8h.md#a9ad0be6cd421f8b608f74a3676bf9d6d)

#define STM32\_DT\_CLKSEL\_REG\_MASK

Helper macros to pack RCC clock source selection register info in the DT.

**Definition** stm32\_common\_clocks.h:24

Clock source binding accessors.

Obtain register field from clock source selection configuration.

Parameters
:   | clock | clock bit field value. |
    | --- | --- |

## [◆ ](#a721bbde6ed4c76019fba67677e359c05)STM32\_DT\_CLKSEL\_SHIFT\_GET

| #define STM32\_DT\_CLKSEL\_SHIFT\_GET | ( |  | *clock* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((clock) >> [STM32\_DT\_CLKSEL\_SHIFT\_SHIFT](stm32__common__clocks_8h.md#a6db7bff4699d60cc318494bdebd85b42)) & [STM32\_DT\_CLKSEL\_SHIFT\_MASK](stm32__common__clocks_8h.md#a01c12bdd437dd33ff01e2ed45617dfff))

[STM32\_DT\_CLKSEL\_SHIFT\_MASK](stm32__common__clocks_8h.md#a01c12bdd437dd33ff01e2ed45617dfff)

#define STM32\_DT\_CLKSEL\_SHIFT\_MASK

**Definition** stm32\_common\_clocks.h:26

[STM32\_DT\_CLKSEL\_SHIFT\_SHIFT](stm32__common__clocks_8h.md#a6db7bff4699d60cc318494bdebd85b42)

#define STM32\_DT\_CLKSEL\_SHIFT\_SHIFT

**Definition** stm32\_common\_clocks.h:27

Obtain position field from clock source selection configuration.

Parameters
:   | clock | Clock bit field value. |
    | --- | --- |

## [◆ ](#aecf915cbdbf64d743b6ccb020a905abe)STM32\_DT\_CLKSEL\_VAL\_GET

| #define STM32\_DT\_CLKSEL\_VAL\_GET | ( |  | *clock* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((clock) >> [STM32\_DT\_CLKSEL\_VAL\_SHIFT](stm32__common__clocks_8h.md#a7353643376cec80b57a89886e19ad6d9)) & [STM32\_DT\_CLKSEL\_VAL\_MASK](stm32__common__clocks_8h.md#a7ba7ca05cdad21911bc39d69e5674e3b))

[STM32\_DT\_CLKSEL\_VAL\_SHIFT](stm32__common__clocks_8h.md#a7353643376cec80b57a89886e19ad6d9)

#define STM32\_DT\_CLKSEL\_VAL\_SHIFT

**Definition** stm32\_common\_clocks.h:31

[STM32\_DT\_CLKSEL\_VAL\_MASK](stm32__common__clocks_8h.md#a7ba7ca05cdad21911bc39d69e5674e3b)

#define STM32\_DT\_CLKSEL\_VAL\_MASK

**Definition** stm32\_common\_clocks.h:30

Obtain value field from clock source selection configuration.

Parameters
:   | clock | Clock bit field value. |
    | --- | --- |

## [◆ ](#a9eb57b349f41edec11ff52a78015aea9)STM32\_DT\_CLOCKS

| #define STM32\_DT\_CLOCKS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

LISTIFY([DT\_NUM\_CLOCKS](group__devicetree-clocks.md#ga22d4e8621b5bf56ed0ac8295dd11d7e3)(node\_id), \

[STM32\_CLOCK\_INFO](#aa1b0949b4c58d57dcd2e979320cbed0a), (,), node\_id) \

}

[DT\_NUM\_CLOCKS](group__devicetree-clocks.md#ga22d4e8621b5bf56ed0ac8295dd11d7e3)

#define DT\_NUM\_CLOCKS(node\_id)

Get the number of elements in a clocks property.

**Definition** clocks.h:107

[STM32\_CLOCK\_INFO](#aa1b0949b4c58d57dcd2e979320cbed0a)

#define STM32\_CLOCK\_INFO(clk\_index, node\_id)

Device tree clocks helpers.

**Definition** stm32\_clock\_control.h:633

## [◆ ](#a7951b8025683529eebdd415d6b65688b)STM32\_DT\_DEV\_DOMAIN\_CLOCK\_SUPPORT

| #define STM32\_DT\_DEV\_DOMAIN\_CLOCK\_SUPPORT   ([DT\_FOREACH\_STATUS\_OKAY](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)([STM32\_DOMAIN\_CLOCK\_SUPPORT](#a8743160d8765b466f8ac6a89efaa9dbc)) 0) |
| --- |

## [◆ ](#a693176c2c60364d327aa5768ebfac185)STM32\_DT\_INST\_CLOCKS

| #define STM32\_DT\_INST\_CLOCKS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCKS](#a9eb57b349f41edec11ff52a78015aea9)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

[STM32\_DT\_CLOCKS](#a9eb57b349f41edec11ff52a78015aea9)

#define STM32\_DT\_CLOCKS(node\_id)

**Definition** stm32\_clock\_control.h:641

## [◆ ](#aac932dfd992b11d479edf2a2d5e8de47)STM32\_DT\_INST\_DEV\_DOMAIN\_CLOCK\_SUPPORT

| #define STM32\_DT\_INST\_DEV\_DOMAIN\_CLOCK\_SUPPORT   ([DT\_INST\_FOREACH\_STATUS\_OKAY](group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)([STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT](#a38559b31633eca5475b73b8a88df1fcd)) 0) |
| --- |

## [◆ ](#ac3274b70aee7aff6282eaa77ca819f27)STM32\_FLASH\_PRESCALER

| #define STM32\_FLASH\_PRESCALER   STM32\_CORE\_PRESCALER |
| --- |

## [◆ ](#a035ea0d8259c0f89306c6a7d344705f2)STM32\_HPRE

| #define STM32\_HPRE   [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(rcc), hpre) |
| --- |

## [◆ ](#a7c3796ef481224c9e2f7516853677ec9)STM32\_HSE\_FREQ

| #define STM32\_HSE\_FREQ   0 |
| --- |

## [◆ ](#aa67c0b4d532b58d78b12d36ae6817912)STM32\_HSI\_DIV\_ENABLED

| #define STM32\_HSI\_DIV\_ENABLED   0 |
| --- |

## [◆ ](#a2cc52c346227b2dfb91e1ab5aeda586c)STM32\_HSI\_DIVISOR

| #define STM32\_HSI\_DIVISOR   1 |
| --- |

## [◆ ](#af906386de1fde7ab0894971723a0a801)STM32\_HSI\_FREQ

| #define STM32\_HSI\_FREQ   0 |
| --- |

## [◆ ](#a94745d7699b62ef9e7f8bbfbc6803727)STM32\_LSE\_BYPASS

| #define STM32\_LSE\_BYPASS   0 |
| --- |

## [◆ ](#aead1c5c5ac685af96410f4883f7e988b)STM32\_LSE\_DRIVING

| #define STM32\_LSE\_DRIVING   0 |
| --- |

## [◆ ](#a05b49e91f478558d33b2b862718758fa)STM32\_LSE\_ENABLED

| #define STM32\_LSE\_ENABLED   0 |
| --- |

PLL node related symbols.

PLL/PLL1 clock source PLL2 clock source PLL3 clock source PLL4 clock source Fixed clocks related symbols

## [◆ ](#aedfe731de4f32e8dacd027bb115ca0e9)STM32\_LSE\_FREQ

| #define STM32\_LSE\_FREQ   0 |
| --- |

## [◆ ](#ae4ad7f2e4844901d753a91c1ba5c58c5)STM32\_LSI\_FREQ

| #define STM32\_LSI\_FREQ   0 |
| --- |

## [◆ ](#a379e09d2e380483155b0ef8cc39d490b)STM32\_MSIK\_ENABLED

| #define STM32\_MSIK\_ENABLED   0 |
| --- |

## [◆ ](#a67d63326f5ebe1b249eb56b227aecb29)STM32\_MSIK\_PLL\_MODE

| #define STM32\_MSIK\_PLL\_MODE   0 |
| --- |

## [◆ ](#a2fb4bc355d7e69e6b676794d0ab4cbba)STM32\_MSIK\_RANGE

| #define STM32\_MSIK\_RANGE   0 |
| --- |

## [◆ ](#a1a83a4c9a806689ac963e2ea8b142fda)STM32\_MSIS\_ENABLED

| #define STM32\_MSIS\_ENABLED   0 |
| --- |

## [◆ ](#a02f0311b8e9c41a004ed355aff37a7b3)STM32\_MSIS\_PLL\_MODE

| #define STM32\_MSIS\_PLL\_MODE   0 |
| --- |

## [◆ ](#a0109485d9cfd70782ce6aff604399330)STM32\_MSIS\_RANGE

| #define STM32\_MSIS\_RANGE   0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [stm32\_clock\_control.h](stm32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
