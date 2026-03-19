---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32h7__clock_8h.html
original_path: doxygen/html/stm32h7__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32h7\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32h7__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| #define | [STM32\_SRC\_HSI\_KER](#ab574ca48f488778e54bdabcd78588ed4)   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) /\* HSI + HSIKERON \*/ |
| #define | [STM32\_SRC\_CSI\_KER](#a469a687b3d587b881bd607634251faf4)   ([STM32\_SRC\_HSI\_KER](#ab574ca48f488778e54bdabcd78588ed4) + 1) /\* CSI + CSIKERON \*/ |
| #define | [STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62)   ([STM32\_SRC\_CSI\_KER](#a469a687b3d587b881bd607634251faf4) + 1) |
|  | PLL outputs. |
| #define | [STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637)   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| #define | [STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9)   ([STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637) + 1) |
| #define | [STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac)   ([STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9) + 1) |
| #define | [STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717)   ([STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac) + 1) |
| #define | [STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd)   ([STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717) + 1) |
| #define | [STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206)   ([STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd) + 1) |
| #define | [STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9)   ([STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206) + 1) |
| #define | [STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a)   ([STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9) + 1) |
| #define | [STM32\_SRC\_CKPER](#a8b7025d7f4be00a152c53097a414668e)   ([STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a) + 1) |
|  | Clock muxes. |
| #define | [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569)   0x0D4 |
|  | Others: Not yet supported. |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x0D8 |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x0DC |
| #define | [STM32\_CLOCK\_BUS\_AHB4](#a49bccabc3065f192086f16929a7b762d)   0x0E0 |
| #define | [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d)   0x0E4 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x0E8 |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x0EC |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x0F0 |
| #define | [STM32\_CLOCK\_BUS\_APB4](#a537105e6125ce3b95a2d69435f47dd51)   0x0F4 |
| #define | [STM32\_SRC\_PCLK1](#a72ffaa9863e167f47e06e91151b47831)   [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95) |
|  | Alias D1/2/3 domains clocks. |
| #define | [STM32\_SRC\_PCLK2](#a68f7335900538f3beb2c2d09e33376b3)   [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db) |
| #define | [STM32\_SRC\_HCLK3](#af15978643f6f5a5f9fa427cb59fa17c7)   [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569) |
| #define | [STM32\_SRC\_PCLK3](#ae54654dc761dca391f56e95ebd6db625)   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| #define | [STM32\_SRC\_PCLK4](#a4c6b45a1c2d1e1eeccdd946eb52ef85e)   [STM32\_CLOCK\_BUS\_APB4](#a537105e6125ce3b95a2d69435f47dd51) |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB4](#a537105e6125ce3b95a2d69435f47dd51) |
| #define | [STM32\_CLOCK\_REG\_MASK](#a33d66849c63db64784317260b06ceb24)   0xFFU |
| #define | [STM32\_CLOCK\_REG\_SHIFT](#a2e73bdb1691751ffd616a5c4e2762423)   0U |
| #define | [STM32\_CLOCK\_SHIFT\_MASK](#af3001a7541ea4df9e4948fd559352f60)   0x1FU |
| #define | [STM32\_CLOCK\_SHIFT\_SHIFT](#a147846b77bd51e42c85bea5aca50ad4f)   8U |
| #define | [STM32\_CLOCK\_MASK\_MASK](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)   0x7U |
| #define | [STM32\_CLOCK\_MASK\_SHIFT](#abfdb31d824fc5c6cf809a1dcff022b5d)   13U |
| #define | [STM32\_CLOCK\_VAL\_MASK](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)   0x7U |
| #define | [STM32\_CLOCK\_VAL\_SHIFT](#adf2ca8c7f707b82b7ec4820dfc32929a)   16U |
| #define | [STM32\_DOMAIN\_CLOCK](#a13a09d4e73c5f6485cbbb541c9e81c35)(val, mask, shift, reg) |
|  | STM32H7 clock configuration bit field. |
| #define | [D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9)   0x4C |
|  | RCC\_DxCCIP register offset (RM0399.pdf). |
| #define | [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef)   0x50 |
| #define | [D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51)   0x54 |
| #define | [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda)   0x58 |
| #define | [BDCR\_REG](#a70a10f70b4f5058508e8983ad0a4de3a)   0x70 |
|  | RCC\_BDCR register offset. |
| #define | [CFGR\_REG](#afb2336a33a23f9671b26010594232ba3)   0x10 |
|  | RCC\_CFGRx register offset. |
| #define | [FMC\_SEL](#a0de89c03e0cd384de7f594aa5c5e82de)(val) |
|  | Device domain clocks selection helpers (RM0399.pdf). |
| #define | [QSPI\_SEL](#ae66e7abfb9009e737cff676fb4e5155f)(val) |
| #define | [DSI\_SEL](#a2e82c24eb0c9e22635966752eebb2a05)(val) |
| #define | [SDMMC\_SEL](#a42688c1d17e09ab58029feedd7491c0b)(val) |
| #define | [CKPER\_SEL](#adc32e4d489d72766d6df1783eedf7628)(val) |
| #define | [OSPI\_SEL](#a098cb5d65a4a2b4cd7da394289eb38ff)(val) |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
|  | D2CCIP1R devices. |
| #define | [SAI23\_SEL](#a8a4600ad412c94bae8c79918ec2bd867)(val) |
| #define | [SPI123\_SEL](#a3852b519c300afd2fd1757c717076b0f)(val) |
| #define | [SPI45\_SEL](#a6919b0ea063667adb88c7c2d79877426)(val) |
| #define | [SPDIF\_SEL](#a37e4a34b034dee8d7f0b1fa1378e6ff6)(val) |
| #define | [DFSDM1\_SEL](#a5364dd3606acfca9d1c00e60255a6634)(val) |
| #define | [FDCAN\_SEL](#ac1df6369669b4b3febd0525426e76499)(val) |
| #define | [SWP\_SEL](#a5ab7d8af86893729938fec97b28ef605)(val) |
| #define | [USART2345678\_SEL](#a80d004ccf51b0621ce404db882bf8b72)(val) |
|  | D2CCIP2R devices. |
| #define | [USART16\_SEL](#ae5f861161482b8888ff3aa5ea79b49a3)(val) |
| #define | [RNG\_SEL](#abfff4355a498febbcf4ebcb237930a57)(val) |
| #define | [I2C123\_SEL](#a6ee55f4ccc3fa2c0a3a5387ba0fd587e)(val) |
| #define | [USB\_SEL](#a3247ad782f1e2c7db84989d03831139b)(val) |
| #define | [CEC\_SEL](#affd653e901474991857a29deba53cf82)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
|  | D3CCIPR devices. |
| #define | [I2C4\_SEL](#a55880006ae28021de4d148924c06001e)(val) |
| #define | [LPTIM2\_SEL](#aa713f6ff001bfa6352747e7a66e3f98a)(val) |
| #define | [LPTIM345\_SEL](#af321430d682d7447d63282a0f380bc8a)(val) |
| #define | [ADC\_SEL](#a635d17ad991ded52d41a6e7b0bec5773)(val) |
| #define | [SAI4A\_SEL](#ae118097634082d8365c0418902ca23c7)(val) |
| #define | [SAI4B\_SEL](#ad2946a4efd35a3a9cd22b00a24675236)(val) |
| #define | [SPI6\_SEL](#ab43d49ec71267eb1d8002909cc3360bf)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
|  | BDCR devices. |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | CFGR devices. |
| #define | [MCO1\_PRE](#a2805cf7e0b5ed0a9bb4bfff863327081)(val) |
| #define | [MCO2\_SEL](#ab5fc05cb6aa1154c54c29b95f3154a75)(val) |
| #define | [MCO2\_PRE](#ab02a0ccbb8588979ca4742c72c59589f)(val) |

## Macro Definition Documentation

## [◆ ](#a635d17ad991ded52d41a6e7b0bec5773)ADC\_SEL

| #define ADC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 16, [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda))

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)

#define STM32\_DOMAIN\_CLOCK(val, mask, shift, reg)

STM32 clock configuration bit field.

**Definition** stm32c0\_clock.h:54

[D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda)

#define D3CCIPR\_REG

**Definition** stm32h7\_clock.h:93

## [◆ ](#a70a10f70b4f5058508e8983ad0a4de3a)BDCR\_REG

| #define BDCR\_REG   0x70 |
| --- |

RCC\_BDCR register offset.

## [◆ ](#affd653e901474991857a29deba53cf82)CEC\_SEL

| #define CEC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 22, [D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51))

[D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51)

#define D2CCIP2R\_REG

**Definition** stm32h7\_clock.h:92

## [◆ ](#afb2336a33a23f9671b26010594232ba3)CFGR\_REG

| #define CFGR\_REG   0x10 |
| --- |

RCC\_CFGRx register offset.

## [◆ ](#adc32e4d489d72766d6df1783eedf7628)CKPER\_SEL

| #define CKPER\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 28, [D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9))

[D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9)

#define D1CCIPR\_REG

RCC\_DxCCIP register offset (RM0399.pdf).

**Definition** stm32h7\_clock.h:90

## [◆ ](#a9a43f736d68c30870b3f1ee545b2cff9)D1CCIPR\_REG

| #define D1CCIPR\_REG   0x4C |
| --- |

RCC\_DxCCIP register offset (RM0399.pdf).

## [◆ ](#ab1fb4611db93643e87a5435ebf0eecef)D2CCIP1R\_REG

| #define D2CCIP1R\_REG   0x50 |
| --- |

## [◆ ](#a44f6b0e94c505441a7ff7f14d26a5f51)D2CCIP2R\_REG

| #define D2CCIP2R\_REG   0x54 |
| --- |

## [◆ ](#aeda9dd86b920e734a85ce06acbd75eda)D3CCIPR\_REG

| #define D3CCIPR\_REG   0x58 |
| --- |

## [◆ ](#a5364dd3606acfca9d1c00e60255a6634)DFSDM1\_SEL

| #define DFSDM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 24, [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef))

[D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef)

#define D2CCIP1R\_REG

**Definition** stm32h7\_clock.h:91

## [◆ ](#a2e82c24eb0c9e22635966752eebb2a05)DSI\_SEL

| #define DSI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 8, [D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9))

## [◆ ](#ac1df6369669b4b3febd0525426e76499)FDCAN\_SEL

| #define FDCAN\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 28, [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef))

## [◆ ](#a0de89c03e0cd384de7f594aa5c5e82de)FMC\_SEL

| #define FMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 0, [D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9))

Device domain clocks selection helpers (RM0399.pdf).

D1CCIPR devices

## [◆ ](#a6ee55f4ccc3fa2c0a3a5387ba0fd587e)I2C123\_SEL

| #define I2C123\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 12, [D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51))

## [◆ ](#a55880006ae28021de4d148924c06001e)I2C4\_SEL

| #define I2C4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 8, [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#a042804bf8a52b3dd28033f8814442bfb)LPTIM1\_SEL

| #define LPTIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 28, [D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51))

## [◆ ](#aa713f6ff001bfa6352747e7a66e3f98a)LPTIM2\_SEL

| #define LPTIM2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 10, [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#af321430d682d7447d63282a0f380bc8a)LPTIM345\_SEL

| #define LPTIM345\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 13, [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#aac31ca48bf87a722f6e0519f25f764dd)LPUART1\_SEL

| #define LPUART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 0, [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda))

D3CCIPR devices.

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 18, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)

#define STM32\_MCO\_CFGR(val, mask, shift, reg)

STM32 MCO configuration register bit field.

**Definition** stm32\_common\_clocks.h:42

[CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3)

#define CFGR\_REG

RCC\_CFGRx register offset.

**Definition** stm32f3\_clock.h:63

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0xF, 22, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

CFGR devices.

## [◆ ](#ab02a0ccbb8588979ca4742c72c59589f)MCO2\_PRE

| #define MCO2\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0x7, 25, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_MCO\_CFGR](stm32__common__clocks_8h.md#ae14adf3f41ed69e7eb58397ab4d5dc44)(val, 0xF, 29, [CFGR\_REG](stm32f3__clock_8h.md#afb2336a33a23f9671b26010594232ba3))

## [◆ ](#a098cb5d65a4a2b4cd7da394289eb38ff)OSPI\_SEL

| #define OSPI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 4, [D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9))

## [◆ ](#ae66e7abfb9009e737cff676fb4e5155f)QSPI\_SEL

| #define QSPI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 4, [D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9))

## [◆ ](#abfff4355a498febbcf4ebcb237930a57)RNG\_SEL

| #define RNG\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 8, [D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51))

## [◆ ](#a4836377699efa295c56d340e150695b0)RTC\_SEL

| #define RTC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 8, [BDCR\_REG](stm32f0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a))

[BDCR\_REG](stm32f0__clock_8h.md#a70a10f70b4f5058508e8983ad0a4de3a)

#define BDCR\_REG

RCC\_BDCR register offset.

**Definition** stm32f0\_clock.h:66

BDCR devices.

## [◆ ](#ab8e49f6309adb53edd9ad3d051d451db)SAI1\_SEL

| #define SAI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 0, [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef))

D2CCIP1R devices.

## [◆ ](#a8a4600ad412c94bae8c79918ec2bd867)SAI23\_SEL

| #define SAI23\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 6, [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef))

## [◆ ](#ae118097634082d8365c0418902ca23c7)SAI4A\_SEL

| #define SAI4A\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 21, [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#ad2946a4efd35a3a9cd22b00a24675236)SAI4B\_SEL

| #define SAI4B\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 24, [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#a42688c1d17e09ab58029feedd7491c0b)SDMMC\_SEL

| #define SDMMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 16, [D1CCIPR\_REG](#a9a43f736d68c30870b3f1ee545b2cff9))

## [◆ ](#a37e4a34b034dee8d7f0b1fa1378e6ff6)SPDIF\_SEL

| #define SPDIF\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 20, [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef))

## [◆ ](#a3852b519c300afd2fd1757c717076b0f)SPI123\_SEL

| #define SPI123\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 12, [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef))

## [◆ ](#a6919b0ea063667adb88c7c2d79877426)SPI45\_SEL

| #define SPI45\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 16, [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef))

## [◆ ](#ab43d49ec71267eb1d8002909cc3360bf)SPI6\_SEL

| #define SPI6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 28, [D3CCIPR\_REG](#aeda9dd86b920e734a85ce06acbd75eda))

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x0D8 |
| --- |

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x0DC |
| --- |

## [◆ ](#ab2a3c819828eb0186ac3a3f15f4b4569)STM32\_CLOCK\_BUS\_AHB3

| #define STM32\_CLOCK\_BUS\_AHB3   0x0D4 |
| --- |

Others: Not yet supported.

Bus clocks

## [◆ ](#a49bccabc3065f192086f16929a7b762d)STM32\_CLOCK\_BUS\_AHB4

| #define STM32\_CLOCK\_BUS\_AHB4   0x0E0 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x0E8 |
| --- |

## [◆ ](#ad25510091b50e823c9860089a9f23deb)STM32\_CLOCK\_BUS\_APB1\_2

| #define STM32\_CLOCK\_BUS\_APB1\_2   0x0EC |
| --- |

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x0F0 |
| --- |

## [◆ ](#af7165e22b71d1beaf0dd4f59d5b4db6d)STM32\_CLOCK\_BUS\_APB3

| #define STM32\_CLOCK\_BUS\_APB3   0x0E4 |
| --- |

## [◆ ](#a537105e6125ce3b95a2d69435f47dd51)STM32\_CLOCK\_BUS\_APB4

| #define STM32\_CLOCK\_BUS\_APB4   0x0F4 |
| --- |

## [◆ ](#a63ecbd205c0dd6cb3eab7bcbfdce38b9)STM32\_CLOCK\_MASK\_MASK

| #define STM32\_CLOCK\_MASK\_MASK   0x7U |
| --- |

## [◆ ](#abfdb31d824fc5c6cf809a1dcff022b5d)STM32\_CLOCK\_MASK\_SHIFT

| #define STM32\_CLOCK\_MASK\_SHIFT   13U |
| --- |

## [◆ ](#a33d66849c63db64784317260b06ceb24)STM32\_CLOCK\_REG\_MASK

| #define STM32\_CLOCK\_REG\_MASK   0xFFU |
| --- |

## [◆ ](#a2e73bdb1691751ffd616a5c4e2762423)STM32\_CLOCK\_REG\_SHIFT

| #define STM32\_CLOCK\_REG\_SHIFT   0U |
| --- |

## [◆ ](#af3001a7541ea4df9e4948fd559352f60)STM32\_CLOCK\_SHIFT\_MASK

| #define STM32\_CLOCK\_SHIFT\_MASK   0x1FU |
| --- |

## [◆ ](#a147846b77bd51e42c85bea5aca50ad4f)STM32\_CLOCK\_SHIFT\_SHIFT

| #define STM32\_CLOCK\_SHIFT\_SHIFT   8U |
| --- |

## [◆ ](#a6b4f80c7dbd047ca1ebac0b233ad1d1b)STM32\_CLOCK\_VAL\_MASK

| #define STM32\_CLOCK\_VAL\_MASK   0x7U |
| --- |

## [◆ ](#adf2ca8c7f707b82b7ec4820dfc32929a)STM32\_CLOCK\_VAL\_SHIFT

| #define STM32\_CLOCK\_VAL\_SHIFT   16U |
| --- |

## [◆ ](#a13a09d4e73c5f6485cbbb541c9e81c35)STM32\_DOMAIN\_CLOCK

| #define STM32\_DOMAIN\_CLOCK | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *mask*, |
|  |  |  | *shift*, |
|  |  |  | *reg* ) |

**Value:**

((((reg) & [STM32\_CLOCK\_REG\_MASK](stm32c0__clock_8h.md#a33d66849c63db64784317260b06ceb24)) << [STM32\_CLOCK\_REG\_SHIFT](stm32c0__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)) | \

(((shift) & [STM32\_CLOCK\_SHIFT\_MASK](stm32c0__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)) << [STM32\_CLOCK\_SHIFT\_SHIFT](stm32c0__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)) | \

(((mask) & [STM32\_CLOCK\_MASK\_MASK](stm32c0__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)) << [STM32\_CLOCK\_MASK\_SHIFT](stm32c0__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)) | \

(((val) & [STM32\_CLOCK\_VAL\_MASK](stm32c0__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)) << [STM32\_CLOCK\_VAL\_SHIFT](stm32c0__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)))

[STM32\_CLOCK\_SHIFT\_SHIFT](stm32c0__clock_8h.md#a147846b77bd51e42c85bea5aca50ad4f)

#define STM32\_CLOCK\_SHIFT\_SHIFT

**Definition** stm32c0\_clock.h:35

[STM32\_CLOCK\_REG\_SHIFT](stm32c0__clock_8h.md#a2e73bdb1691751ffd616a5c4e2762423)

#define STM32\_CLOCK\_REG\_SHIFT

**Definition** stm32c0\_clock.h:33

[STM32\_CLOCK\_REG\_MASK](stm32c0__clock_8h.md#a33d66849c63db64784317260b06ceb24)

#define STM32\_CLOCK\_REG\_MASK

**Definition** stm32c0\_clock.h:32

[STM32\_CLOCK\_MASK\_MASK](stm32c0__clock_8h.md#a63ecbd205c0dd6cb3eab7bcbfdce38b9)

#define STM32\_CLOCK\_MASK\_MASK

**Definition** stm32c0\_clock.h:36

[STM32\_CLOCK\_VAL\_MASK](stm32c0__clock_8h.md#a6b4f80c7dbd047ca1ebac0b233ad1d1b)

#define STM32\_CLOCK\_VAL\_MASK

**Definition** stm32c0\_clock.h:38

[STM32\_CLOCK\_MASK\_SHIFT](stm32c0__clock_8h.md#abfdb31d824fc5c6cf809a1dcff022b5d)

#define STM32\_CLOCK\_MASK\_SHIFT

**Definition** stm32c0\_clock.h:37

[STM32\_CLOCK\_VAL\_SHIFT](stm32c0__clock_8h.md#adf2ca8c7f707b82b7ec4820dfc32929a)

#define STM32\_CLOCK\_VAL\_SHIFT

**Definition** stm32c0\_clock.h:39

[STM32\_CLOCK\_SHIFT\_MASK](stm32c0__clock_8h.md#af3001a7541ea4df9e4948fd559352f60)

#define STM32\_CLOCK\_SHIFT\_MASK

**Definition** stm32c0\_clock.h:34

STM32H7 clock configuration bit field.

- reg (0/1) [ 0 : 7 ]
- shift (0..31) [ 8 : 12 ]
- mask (0x1, 0x3, 0x7) [ 13 : 15 ]
- val (0..3) [ 16 : 18 ]

Parameters
:   | reg | RCC\_DxCCIP register offset |
    | --- | --- |
    | shift | Position within RCC\_DxCCIP. |
    | mask | Mask for the RCC\_DxCCIP field. |
    | val | Clock value (0, 1, 2 or 3). |

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB4](#a537105e6125ce3b95a2d69435f47dd51) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569) |
| --- |

## [◆ ](#a8b7025d7f4be00a152c53097a414668e)STM32\_SRC\_CKPER

| #define STM32\_SRC\_CKPER   ([STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a) + 1) |
| --- |

Clock muxes.

## [◆ ](#a469a687b3d587b881bd607634251faf4)STM32\_SRC\_CSI\_KER

| #define STM32\_SRC\_CSI\_KER   ([STM32\_SRC\_HSI\_KER](#ab574ca48f488778e54bdabcd78588ed4) + 1) /\* CSI + CSIKERON \*/ |
| --- |

## [◆ ](#af15978643f6f5a5f9fa427cb59fa17c7)STM32\_SRC\_HCLK3

| #define STM32\_SRC\_HCLK3   [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569) |
| --- |

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#ae12e6bda1c30174c98303f692a42960f)STM32\_SRC\_HSI48

| #define STM32\_SRC\_HSI48   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

## [◆ ](#ab574ca48f488778e54bdabcd78588ed4)STM32\_SRC\_HSI\_KER

| #define STM32\_SRC\_HSI\_KER   ([STM32\_SRC\_HSI48](#ae12e6bda1c30174c98303f692a42960f) + 1) /\* HSI + HSIKERON \*/ |
| --- |

## [◆ ](#a72ffaa9863e167f47e06e91151b47831)STM32\_SRC\_PCLK1

| #define STM32\_SRC\_PCLK1   [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95) |
| --- |

Alias D1/2/3 domains clocks.

## [◆ ](#a68f7335900538f3beb2c2d09e33376b3)STM32\_SRC\_PCLK2

| #define STM32\_SRC\_PCLK2   [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db) |
| --- |

## [◆ ](#ae54654dc761dca391f56e95ebd6db625)STM32\_SRC\_PCLK3

| #define STM32\_SRC\_PCLK3   [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d) |
| --- |

## [◆ ](#a4c6b45a1c2d1e1eeccdd946eb52ef85e)STM32\_SRC\_PCLK4

| #define STM32\_SRC\_PCLK4   [STM32\_CLOCK\_BUS\_APB4](#a537105e6125ce3b95a2d69435f47dd51) |
| --- |

## [◆ ](#aa074615a92c5ff479f4fbed6fdf27f62)STM32\_SRC\_PLL1\_P

| #define STM32\_SRC\_PLL1\_P   ([STM32\_SRC\_CSI\_KER](#a469a687b3d587b881bd607634251faf4) + 1) |
| --- |

PLL outputs.

## [◆ ](#a6edb3dc598055ceeb82045fdee647637)STM32\_SRC\_PLL1\_Q

| #define STM32\_SRC\_PLL1\_Q   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| --- |

## [◆ ](#a6063632b32a970b9abbf711bab8a77c9)STM32\_SRC\_PLL1\_R

| #define STM32\_SRC\_PLL1\_R   ([STM32\_SRC\_PLL1\_Q](#a6edb3dc598055ceeb82045fdee647637) + 1) |
| --- |

## [◆ ](#ae568673a4eca1b42afc59faabb5810ac)STM32\_SRC\_PLL2\_P

| #define STM32\_SRC\_PLL2\_P   ([STM32\_SRC\_PLL1\_R](#a6063632b32a970b9abbf711bab8a77c9) + 1) |
| --- |

## [◆ ](#aaf0a956dda42c2a031cabce49dd3e717)STM32\_SRC\_PLL2\_Q

| #define STM32\_SRC\_PLL2\_Q   ([STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac) + 1) |
| --- |

## [◆ ](#a57af8944eefa865aa75b6286c13a53cd)STM32\_SRC\_PLL2\_R

| #define STM32\_SRC\_PLL2\_R   ([STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717) + 1) |
| --- |

## [◆ ](#a17c753e0bb8547ea9452f48a65a0a206)STM32\_SRC\_PLL3\_P

| #define STM32\_SRC\_PLL3\_P   ([STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd) + 1) |
| --- |

## [◆ ](#a9a31a3adebff6a1eee31c287673412c9)STM32\_SRC\_PLL3\_Q

| #define STM32\_SRC\_PLL3\_Q   ([STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206) + 1) |
| --- |

## [◆ ](#a604c22ff137a35cd1725b70991696f9a)STM32\_SRC\_PLL3\_R

| #define STM32\_SRC\_PLL3\_R   ([STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9) + 1) |
| --- |

## [◆ ](#a5ab7d8af86893729938fec97b28ef605)SWP\_SEL

| #define SWP\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 1, 31, [D2CCIP1R\_REG](#ab1fb4611db93643e87a5435ebf0eecef))

## [◆ ](#ae5f861161482b8888ff3aa5ea79b49a3)USART16\_SEL

| #define USART16\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 3, [D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51))

## [◆ ](#a80d004ccf51b0621ce404db882bf8b72)USART2345678\_SEL

| #define USART2345678\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 7, 0, [D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51))

D2CCIP2R devices.

## [◆ ](#a3247ad782f1e2c7db84989d03831139b)USB\_SEL

| #define USB\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DOMAIN\_CLOCK](stm32c0__clock_8h.md#a13a09d4e73c5f6485cbbb541c9e81c35)(val, 3, 20, [D2CCIP2R\_REG](#a44f6b0e94c505441a7ff7f14d26a5f51))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32h7\_clock.h](stm32h7__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
