---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32n6__clock_8h.html
original_path: doxygen/html/stm32n6__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32n6\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32n6__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | Domain clocks. |
| #define | [STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| #define | [STM32\_SRC\_MSI](#a542b4426a15d849545af2fd6012c520c)   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| #define | [STM32\_SRC\_PLL1](#a19b07a1053f648e063c71884f58644f5)   ([STM32\_SRC\_MSI](#a542b4426a15d849545af2fd6012c520c) + 1) |
|  | PLL outputs. |
| #define | [STM32\_SRC\_PLL2](#ad3883851983b32dec66ee645f123ae55)   ([STM32\_SRC\_PLL1](#a19b07a1053f648e063c71884f58644f5) + 1) |
| #define | [STM32\_SRC\_PLL3](#a848b0c6079f693252c1aea11ff1f22d3)   ([STM32\_SRC\_PLL2](#ad3883851983b32dec66ee645f123ae55) + 1) |
| #define | [STM32\_SRC\_PLL4](#a45ea694120a93c1971fe65ec82d1c4d1)   ([STM32\_SRC\_PLL3](#a848b0c6079f693252c1aea11ff1f22d3) + 1) |
| #define | [STM32\_SRC\_CKPER](#a8b7025d7f4be00a152c53097a414668e)   ([STM32\_SRC\_PLL4](#a45ea694120a93c1971fe65ec82d1c4d1) + 1) |
|  | Clock muxes. |
| #define | [STM32\_SRC\_IC1](#aa13b836db0b585e0998b17edb43c41d7)   ([STM32\_SRC\_CKPER](#a8b7025d7f4be00a152c53097a414668e) + 1) |
| #define | [STM32\_SRC\_IC2](#aed86ff6d9d94396b0dfa38a94fc3c121)   ([STM32\_SRC\_IC1](#aa13b836db0b585e0998b17edb43c41d7) + 1) |
| #define | [STM32\_SRC\_IC3](#a5cbf858b015f3d890d5584d1a817ee28)   ([STM32\_SRC\_IC2](#aed86ff6d9d94396b0dfa38a94fc3c121) + 1) |
| #define | [STM32\_SRC\_IC4](#aa04f6065e9e9c206bbd4b977231a4407)   ([STM32\_SRC\_IC3](#a5cbf858b015f3d890d5584d1a817ee28) + 1) |
| #define | [STM32\_SRC\_IC5](#ac1865fa9a7e303b05f1bc6ff6cca5cdc)   ([STM32\_SRC\_IC4](#aa04f6065e9e9c206bbd4b977231a4407) + 1) |
| #define | [STM32\_SRC\_IC6](#abd8ade42581f7a8375d8548c7968ae54)   ([STM32\_SRC\_IC5](#ac1865fa9a7e303b05f1bc6ff6cca5cdc) + 1) |
| #define | [STM32\_SRC\_IC7](#a590359462bd90dc5e50055e35d794077)   ([STM32\_SRC\_IC6](#abd8ade42581f7a8375d8548c7968ae54) + 1) |
| #define | [STM32\_SRC\_IC8](#a2b8c5564a40658105375154f69169d4c)   ([STM32\_SRC\_IC7](#a590359462bd90dc5e50055e35d794077) + 1) |
| #define | [STM32\_SRC\_IC9](#a161620be8255ff4c06bbb9fbe22cea3b)   ([STM32\_SRC\_IC8](#a2b8c5564a40658105375154f69169d4c) + 1) |
| #define | [STM32\_SRC\_IC10](#a155f8b76c1702064125e99b5facec123)   ([STM32\_SRC\_IC9](#a161620be8255ff4c06bbb9fbe22cea3b) + 1) |
| #define | [STM32\_SRC\_IC11](#aac341fc606e3cf6ee2ef69603d60a250)   ([STM32\_SRC\_IC10](#a155f8b76c1702064125e99b5facec123) + 1) |
| #define | [STM32\_SRC\_IC12](#a95e0637f72e0f6fbc80f9ce771abc111)   ([STM32\_SRC\_IC11](#aac341fc606e3cf6ee2ef69603d60a250) + 1) |
| #define | [STM32\_SRC\_IC13](#a3d76a5bd14d0e0f5a61e38ae33190223)   ([STM32\_SRC\_IC12](#a95e0637f72e0f6fbc80f9ce771abc111) + 1) |
| #define | [STM32\_SRC\_IC14](#aac5bc01ec42163ed149440284bdf8592)   ([STM32\_SRC\_IC13](#a3d76a5bd14d0e0f5a61e38ae33190223) + 1) |
| #define | [STM32\_SRC\_IC15](#af1fba356ba1dc06132d763d02df1234c)   ([STM32\_SRC\_IC14](#aac5bc01ec42163ed149440284bdf8592) + 1) |
| #define | [STM32\_SRC\_IC16](#a47414e92c3cff773978026dede6272ee)   ([STM32\_SRC\_IC15](#af1fba356ba1dc06132d763d02df1234c) + 1) |
| #define | [STM32\_SRC\_IC17](#a04b6c1123aa4c7db12e1fb83a9afd838)   ([STM32\_SRC\_IC16](#a47414e92c3cff773978026dede6272ee) + 1) |
| #define | [STM32\_SRC\_IC18](#add609ce4fd1723b9662335ab0a835523)   ([STM32\_SRC\_IC17](#a04b6c1123aa4c7db12e1fb83a9afd838) + 1) |
| #define | [STM32\_SRC\_IC19](#aee9cb50a33915e66260a0205041091d7)   ([STM32\_SRC\_IC18](#add609ce4fd1723b9662335ab0a835523) + 1) |
| #define | [STM32\_SRC\_IC20](#a9aedd874a88b96145f31a76585806ff3)   ([STM32\_SRC\_IC19](#aee9cb50a33915e66260a0205041091d7) + 1) |
| #define | [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c)   0x250 |
|  | Bus clocks. |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x254 |
| #define | [STM32\_CLOCK\_BUS\_AHB3](#ab2a3c819828eb0186ac3a3f15f4b4569)   0x258 |
| #define | [STM32\_CLOCK\_BUS\_AHB4](#a49bccabc3065f192086f16929a7b762d)   0x25C |
| #define | [STM32\_CLOCK\_BUS\_AHB5](#a623a8ba4dc47622dfbf76801f1582f58)   0x260 |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x264 |
| #define | [STM32\_CLOCK\_BUS\_APB1\_2](#ad25510091b50e823c9860089a9f23deb)   0x268 |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x26C |
| #define | [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d)   0x270 |
| #define | [STM32\_CLOCK\_BUS\_APB4](#a537105e6125ce3b95a2d69435f47dd51)   0x274 |
| #define | [STM32\_CLOCK\_BUS\_APB4\_2](#a4dc3ff62777a32dfc4e76b281a564c86)   0x278 |
| #define | [STM32\_CLOCK\_BUS\_APB5](#a02ec780a692439efebf0bf8181bf7803)   0x27C |
| #define | [STM32\_CLOCK\_LP\_BUS\_SHIFT](#a3931aa4b01e07a95df585779323a7f48)   0x40 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_APB5](#a02ec780a692439efebf0bf8181bf7803) |
| #define | [CCIPR1\_REG](#a5a41b990eca365907d09bb4416fb22d2)   0x144 |
|  | RCC\_CCIPRx register offset (RM0468.pdf). |
| #define | [CCIPR2\_REG](#a60349691a29a48b727f302acb8025b89)   0x148 |
| #define | [CCIPR3\_REG](#a302577067fac290b578130da822dc146)   0x14C |
| #define | [CCIPR4\_REG](#a92eb5c50a767e0f704356d52398f9723)   0x150 |
| #define | [CCIPR5\_REG](#a62e39113c018ae0b2c31254ff003d148)   0x154 |
| #define | [CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b)   0x158 |
| #define | [CCIPR7\_REG](#a3fcb658bb097cce8697024fe6b7b44c3)   0x15C |
| #define | [CCIPR8\_REG](#a43a90b0127d5a177fbebc8c2fac53a79)   0x160 |
| #define | [CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351)   0x164 |
| #define | [CCIPR12\_REG](#a7cb03c6ceaa338c1850b28a2758e11a8)   0x170 |
| #define | [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb)   0x174 |
| #define | [CCIPR14\_REG](#a07372cf80165afcc7f9297f5b1c33128)   0x178 |
| #define | [ADF1\_SEL](#a2965fce3cbae0a73506ddf383c78783f)(val) |
|  | Device domain clocks selection helpers. |
| #define | [ADC12\_SEL](#a937fbb74cf970ef8033c16c68b27400f)(val) |
| #define | [DCMIPP\_SEL](#a5b9758e95788f06d93382daec60fdf3f)(val) |
| #define | [ETH1PTP\_SEL](#aee7f83f9ca88503a6c8b29ba1e220743)(val) |
|  | CCIPR2 devices. |
| #define | [ETH1CLK\_SEL](#a0005c1d3bc4ed6b8c5c30c07051aa4ea)(val) |
| #define | [ETH1\_SEL](#a4e9282866e4f40cf5d6fd0a655fa6fa1)(val) |
| #define | [ETH1REFCLK\_SEL](#ae853e04c239d4321ca2b58c6fcdbe197)(val) |
| #define | [ETH1GTXCLK\_SEL](#af972ee87a5e3d879b50b3232af19a794)(val) |
| #define | [FDCAN\_SEL](#ac1df6369669b4b3febd0525426e76499)(val) |
|  | CCIPR3 devices. |
| #define | [FMC\_SEL](#a0de89c03e0cd384de7f594aa5c5e82de)(val) |
| #define | [I2C1\_SEL](#a3fbef8f2542fc6921236bd2709acf64c)(val) |
|  | CCIPR4 devices. |
| #define | [I2C2\_SEL](#abdd79c9ce90458b53e81123d181fed98)(val) |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [I2C4\_SEL](#a55880006ae28021de4d148924c06001e)(val) |
| #define | [I3C1\_SEL](#a576dca08c22370326fefc540bf056b81)(val) |
| #define | [I3C2\_SEL](#a647bc22bf65d67e9e2c5361d0dce925d)(val) |
| #define | [LTDC\_SEL](#ac299465bc5d655ecc6dd1e8e7a347e0c)(val) |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | CCIPR5 devices. |
| #define | [MCO2\_SEL](#ab5fc05cb6aa1154c54c29b95f3154a75)(val) |
| #define | [MDF1SEL](#a75330910b0ff85fa8a8ccd99f3754970)(val) |
| #define | [XSPI1\_SEL](#a15df14366d6921bac34208b0c1af0ebb)(val) |
|  | CCIPR6 devices. |
| #define | [XSPI2\_SEL](#a58f2e1e8be7e4e9b50783f03afc687ff)(val) |
| #define | [XSPI3\_SEL](#abc02f0330af9bc5e21bccf01204441bc)(val) |
| #define | [OTGPHY1\_SEL](#a3a59519ef352041f5fc6b73847feff36)(val) |
| #define | [OTGPHY1CKREF\_SEL](#a0dfca2709116f9933488ac82b894ab75)(val) |
| #define | [OTGPHY2\_SEL](#a3378b1ba6ba842c341b02c8b3423794c)(val) |
| #define | [OTGPHY2CKREF\_SEL](#a462cc4388ed9cd167341e583aeb2b9e3)(val) |
| #define | [PER\_SEL](#a822d6e1a5aaaec0e634ea961e18902f6)(val) |
|  | CCIPR7 devices. |
| #define | [PSSI\_SEL](#af67616db4defc072c759f2f6b6006a9d)(val) |
| #define | [RTC\_SEL](#a4836377699efa295c56d340e150695b0)(val) |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
| #define | [SAI2\_SEL](#a4fb9a6b79339e822f0ae426e8bba7486)(val) |
| #define | [SDMMC1\_SEL](#a1a4999da331afff86581c8a6cea6afe9)(val) |
|  | CCIPR8 devices. |
| #define | [SDMMC2\_SEL](#a7319710d63129ad13039565cad2b4950)(val) |
| #define | [SPDIFRX1\_SEL](#a9559c1e35f44860aee803e7269e9cede)(val) |
|  | CCIPR9 devices. |
| #define | [SPI1\_SEL](#a5199102173e9dbe957230f356e14d910)(val) |
| #define | [SPI2\_SEL](#ad3e84eac634b9d943acea9b2ab884fb5)(val) |
| #define | [SPI3\_SEL](#aaa096904d8a97bedc81f9a565e65c332)(val) |
| #define | [SPI4\_SEL](#a55086a94321a6e1af527a46c644f6c5e)(val) |
| #define | [SPI5\_SEL](#ac7193e508815171a4d73795d24086136)(val) |
| #define | [SPI6\_SEL](#ab43d49ec71267eb1d8002909cc3360bf)(val) |
| #define | [LPTIM1\_SEL](#a042804bf8a52b3dd28033f8814442bfb)(val) |
|  | CCIPR12 devices. |
| #define | [LPTIM2\_SEL](#aa713f6ff001bfa6352747e7a66e3f98a)(val) |
| #define | [LPTIM3\_SEL](#ac705aa5789ca3b11ac5115d22ec2a5e5)(val) |
| #define | [LPTIM4\_SEL](#a7c23812b481c3743f393d301d7cf7e27)(val) |
| #define | [LPTIM5\_SEL](#ad508257c2f92e7ced0f6317ea3397965)(val) |
| #define | [USART1\_SEL](#a17f3ec5f86995a2c4087f2988a9486c5)(val) |
|  | CCIPR13 devices. |
| #define | [USART2\_SEL](#ad67d92dfc439018a7a231e661d10d7f9)(val) |
| #define | [USART3\_SEL](#ad2f356c0bc0e43d6f629cdb840846526)(val) |
| #define | [UART4\_SEL](#a091d597b4979c49951f880bc6ccb4d71)(val) |
| #define | [UART5\_SEL](#a136c2c36c89ebdf2c5b97686bbce0209)(val) |
| #define | [USART6\_SEL](#a99c9026d61766ec9b91872ee64ad63eb)(val) |
| #define | [UART7\_SEL](#a2d0071bb5cc287b8be749d8abcca6eab)(val) |
| #define | [UART8\_SEL](#a1b66b237c80c002bc2b422d8fbf61824)(val) |
| #define | [UART9\_SEL](#a866e45ef86e20589a96ae4533382fb5b)(val) |
|  | CCIPR14 devices. |
| #define | [USART10\_SEL](#a5eef37bd8c6a90bf0de08faf5d05f410)(val) |
| #define | [LPUART1\_SEL](#aac31ca48bf87a722f6e0519f25f764dd)(val) |
| #define | [ICxCFGR\_REG](#a3e7bf66713ac3a485e415ff3635fff0e)(ic) |
|  | RCC\_ICxCFGR register offset (RM0468.pdf). |
| #define | [ICx\_PLLy\_SEL](#aaa6058bcba48e870acb5ee09a338bf0c)(ic, pll) |
|  | Divider ICx source selection. |
| #define | [CFGR1\_REG](#a6b894fe6e036f03831faddf28bce43c6)   0x20 |
|  | RCC\_CFGR1 register offset (RM0468.pdf). |
| #define | [CPU\_SEL](#a640e40ac4ae8af3906b84267d5ee7bea)(val) |
|  | CPU clock switch selection. |

## Macro Definition Documentation

## [◆ ](#a937fbb74cf970ef8033c16c68b27400f)ADC12\_SEL

| #define ADC12\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2)

#define CCIPR1\_REG

RCC\_CCIPRx register offset (RM0456.pdf).

**Definition** stm32h5\_clock.h:55

## [◆ ](#a2965fce3cbae0a73506ddf383c78783f)ADF1\_SEL

| #define ADF1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

Device domain clocks selection helpers.

CCIPR1 devices

## [◆ ](#a7cb03c6ceaa338c1850b28a2758e11a8)CCIPR12\_REG

| #define CCIPR12\_REG   0x170 |
| --- |

## [◆ ](#ac5db8f44fd62365a2b508969767acceb)CCIPR13\_REG

| #define CCIPR13\_REG   0x174 |
| --- |

## [◆ ](#a07372cf80165afcc7f9297f5b1c33128)CCIPR14\_REG

| #define CCIPR14\_REG   0x178 |
| --- |

## [◆ ](#a5a41b990eca365907d09bb4416fb22d2)CCIPR1\_REG

| #define CCIPR1\_REG   0x144 |
| --- |

RCC\_CCIPRx register offset (RM0468.pdf).

## [◆ ](#a60349691a29a48b727f302acb8025b89)CCIPR2\_REG

| #define CCIPR2\_REG   0x148 |
| --- |

## [◆ ](#a302577067fac290b578130da822dc146)CCIPR3\_REG

| #define CCIPR3\_REG   0x14C |
| --- |

## [◆ ](#a92eb5c50a767e0f704356d52398f9723)CCIPR4\_REG

| #define CCIPR4\_REG   0x150 |
| --- |

## [◆ ](#a62e39113c018ae0b2c31254ff003d148)CCIPR5\_REG

| #define CCIPR5\_REG   0x154 |
| --- |

## [◆ ](#ab00ea8c2d2b0918b738001b972aacf6b)CCIPR6\_REG

| #define CCIPR6\_REG   0x158 |
| --- |

## [◆ ](#a3fcb658bb097cce8697024fe6b7b44c3)CCIPR7\_REG

| #define CCIPR7\_REG   0x15C |
| --- |

## [◆ ](#a43a90b0127d5a177fbebc8c2fac53a79)CCIPR8\_REG

| #define CCIPR8\_REG   0x160 |
| --- |

## [◆ ](#a3a5cc0435932cbd3235d59f6ce043351)CCIPR9\_REG

| #define CCIPR9\_REG   0x164 |
| --- |

## [◆ ](#a6b894fe6e036f03831faddf28bce43c6)CFGR1\_REG

| #define CFGR1\_REG   0x20 |
| --- |

RCC\_CFGR1 register offset (RM0468.pdf).

## [◆ ](#a640e40ac4ae8af3906b84267d5ee7bea)CPU\_SEL

| #define CPU\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 16, [CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6))

[CFGR1\_REG](stm32c0__clock_8h.md#a6b894fe6e036f03831faddf28bce43c6)

#define CFGR1\_REG

RCC\_CFGRx register offset.

**Definition** stm32c0\_clock.h:39

CPU clock switch selection.

## [◆ ](#a5b9758e95788f06d93382daec60fdf3f)DCMIPP\_SEL

| #define DCMIPP\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 20, [CCIPR1\_REG](stm32h5__clock_8h.md#a5a41b990eca365907d09bb4416fb22d2))

## [◆ ](#a4e9282866e4f40cf5d6fd0a655fa6fa1)ETH1\_SEL

| #define ETH1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

[CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89)

#define CCIPR2\_REG

**Definition** stm32g0\_clock.h:40

## [◆ ](#a0005c1d3bc4ed6b8c5c30c07051aa4ea)ETH1CLK\_SEL

| #define ETH1CLK\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 12, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#af972ee87a5e3d879b50b3232af19a794)ETH1GTXCLK\_SEL

| #define ETH1GTXCLK\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 24, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#aee7f83f9ca88503a6c8b29ba1e220743)ETH1PTP\_SEL

| #define ETH1PTP\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

CCIPR2 devices.

## [◆ ](#ae853e04c239d4321ca2b58c6fcdbe197)ETH1REFCLK\_SEL

| #define ETH1REFCLK\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 20, [CCIPR2\_REG](stm32g0__clock_8h.md#a60349691a29a48b727f302acb8025b89))

## [◆ ](#ac1df6369669b4b3febd0525426e76499)FDCAN\_SEL

| #define FDCAN\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

[CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146)

#define CCIPR3\_REG

**Definition** stm32h5\_clock.h:57

CCIPR3 devices.

## [◆ ](#a0de89c03e0cd384de7f594aa5c5e82de)FMC\_SEL

| #define FMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 4, [CCIPR3\_REG](stm32h5__clock_8h.md#a302577067fac290b578130da822dc146))

## [◆ ](#a3fbef8f2542fc6921236bd2709acf64c)I2C1\_SEL

| #define I2C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR4\_REG](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723))

[CCIPR4\_REG](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723)

#define CCIPR4\_REG

**Definition** stm32h5\_clock.h:58

CCIPR4 devices.

## [◆ ](#abdd79c9ce90458b53e81123d181fed98)I2C2\_SEL

| #define I2C2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [CCIPR4\_REG](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [CCIPR4\_REG](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#a55880006ae28021de4d148924c06001e)I2C4\_SEL

| #define I2C4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [CCIPR4\_REG](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#a576dca08c22370326fefc540bf056b81)I3C1\_SEL

| #define I3C1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR4\_REG](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#a647bc22bf65d67e9e2c5361d0dce925d)I3C2\_SEL

| #define I3C2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 20, [CCIPR4\_REG](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#aaa6058bcba48e870acb5ee09a338bf0c)ICx\_PLLy\_SEL

| #define ICx\_PLLy\_SEL | ( |  | *ic*, |
| --- | --- | --- | --- |
|  |  |  | *pll* ) |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((pll) - 1, 3, 28, [ICxCFGR\_REG](#a3e7bf66713ac3a485e415ff3635fff0e)(ic))

[ICxCFGR\_REG](#a3e7bf66713ac3a485e415ff3635fff0e)

#define ICxCFGR\_REG(ic)

RCC\_ICxCFGR register offset (RM0468.pdf).

**Definition** stm32n6\_clock.h:154

Divider ICx source selection.

## [◆ ](#a3e7bf66713ac3a485e415ff3635fff0e)ICxCFGR\_REG

| #define ICxCFGR\_REG | ( |  | *ic* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(0xC4 + ((ic) - 1) \* 4)

RCC\_ICxCFGR register offset (RM0468.pdf).

## [◆ ](#a042804bf8a52b3dd28033f8814442bfb)LPTIM1\_SEL

| #define LPTIM1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [CCIPR12\_REG](#a7cb03c6ceaa338c1850b28a2758e11a8))

[CCIPR12\_REG](#a7cb03c6ceaa338c1850b28a2758e11a8)

#define CCIPR12\_REG

**Definition** stm32n6\_clock.h:78

CCIPR12 devices.

## [◆ ](#aa713f6ff001bfa6352747e7a66e3f98a)LPTIM2\_SEL

| #define LPTIM2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [CCIPR12\_REG](#a7cb03c6ceaa338c1850b28a2758e11a8))

## [◆ ](#ac705aa5789ca3b11ac5115d22ec2a5e5)LPTIM3\_SEL

| #define LPTIM3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR12\_REG](#a7cb03c6ceaa338c1850b28a2758e11a8))

## [◆ ](#a7c23812b481c3743f393d301d7cf7e27)LPTIM4\_SEL

| #define LPTIM4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 20, [CCIPR12\_REG](#a7cb03c6ceaa338c1850b28a2758e11a8))

## [◆ ](#ad508257c2f92e7ced0f6317ea3397965)LPTIM5\_SEL

| #define LPTIM5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 24, [CCIPR12\_REG](#a7cb03c6ceaa338c1850b28a2758e11a8))

## [◆ ](#aac31ca48bf87a722f6e0519f25f764dd)LPUART1\_SEL

| #define LPUART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [CCIPR14\_REG](#a07372cf80165afcc7f9297f5b1c33128))

[CCIPR14\_REG](#a07372cf80165afcc7f9297f5b1c33128)

#define CCIPR14\_REG

**Definition** stm32n6\_clock.h:80

## [◆ ](#ac299465bc5d655ecc6dd1e8e7a347e0c)LTDC\_SEL

| #define LTDC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 24, [CCIPR4\_REG](stm32h5__clock_8h.md#a92eb5c50a767e0f704356d52398f9723))

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR5\_REG](stm32h5__clock_8h.md#a62e39113c018ae0b2c31254ff003d148))

[CCIPR5\_REG](stm32h5__clock_8h.md#a62e39113c018ae0b2c31254ff003d148)

#define CCIPR5\_REG

**Definition** stm32h5\_clock.h:59

CCIPR5 devices.

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [CCIPR5\_REG](stm32h5__clock_8h.md#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#a75330910b0ff85fa8a8ccd99f3754970)MDF1SEL

| #define MDF1SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR5\_REG](stm32h5__clock_8h.md#a62e39113c018ae0b2c31254ff003d148))

## [◆ ](#a3a59519ef352041f5fc6b73847feff36)OTGPHY1\_SEL

| #define OTGPHY1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 12, [CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b))

[CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b)

#define CCIPR6\_REG

**Definition** stm32n6\_clock.h:74

## [◆ ](#a0dfca2709116f9933488ac82b894ab75)OTGPHY1CKREF\_SEL

| #define OTGPHY1CKREF\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 16, [CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b))

## [◆ ](#a3378b1ba6ba842c341b02c8b3423794c)OTGPHY2\_SEL

| #define OTGPHY2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 20, [CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b))

## [◆ ](#a462cc4388ed9cd167341e583aeb2b9e3)OTGPHY2CKREF\_SEL

| #define OTGPHY2CKREF\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 1, 24, [CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b))

## [◆ ](#a822d6e1a5aaaec0e634ea961e18902f6)PER\_SEL

| #define PER\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR7\_REG](#a3fcb658bb097cce8697024fe6b7b44c3))

[CCIPR7\_REG](#a3fcb658bb097cce8697024fe6b7b44c3)

#define CCIPR7\_REG

**Definition** stm32n6\_clock.h:75

CCIPR7 devices.

## [◆ ](#af67616db4defc072c759f2f6b6006a9d)PSSI\_SEL

| #define PSSI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 4, [CCIPR7\_REG](#a3fcb658bb097cce8697024fe6b7b44c3))

## [◆ ](#a4836377699efa295c56d340e150695b0)RTC\_SEL

| #define RTC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 8, [CCIPR7\_REG](#a3fcb658bb097cce8697024fe6b7b44c3))

## [◆ ](#ab8e49f6309adb53edd9ad3d051d451db)SAI1\_SEL

| #define SAI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 20, [CCIPR7\_REG](#a3fcb658bb097cce8697024fe6b7b44c3))

## [◆ ](#a4fb9a6b79339e822f0ae426e8bba7486)SAI2\_SEL

| #define SAI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 24, [CCIPR7\_REG](#a3fcb658bb097cce8697024fe6b7b44c3))

## [◆ ](#a1a4999da331afff86581c8a6cea6afe9)SDMMC1\_SEL

| #define SDMMC1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR8\_REG](#a43a90b0127d5a177fbebc8c2fac53a79))

[CCIPR8\_REG](#a43a90b0127d5a177fbebc8c2fac53a79)

#define CCIPR8\_REG

**Definition** stm32n6\_clock.h:76

CCIPR8 devices.

## [◆ ](#a7319710d63129ad13039565cad2b4950)SDMMC2\_SEL

| #define SDMMC2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 4, [CCIPR8\_REG](#a43a90b0127d5a177fbebc8c2fac53a79))

## [◆ ](#a9559c1e35f44860aee803e7269e9cede)SPDIFRX1\_SEL

| #define SPDIFRX1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351))

[CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351)

#define CCIPR9\_REG

**Definition** stm32n6\_clock.h:77

CCIPR9 devices.

## [◆ ](#a5199102173e9dbe957230f356e14d910)SPI1\_SEL

| #define SPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351))

## [◆ ](#ad3e84eac634b9d943acea9b2ab884fb5)SPI2\_SEL

| #define SPI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351))

## [◆ ](#aaa096904d8a97bedc81f9a565e65c332)SPI3\_SEL

| #define SPI3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351))

## [◆ ](#a55086a94321a6e1af527a46c644f6c5e)SPI4\_SEL

| #define SPI4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351))

## [◆ ](#ac7193e508815171a4d73795d24086136)SPI5\_SEL

| #define SPI5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 20, [CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351))

## [◆ ](#ab43d49ec71267eb1d8002909cc3360bf)SPI6\_SEL

| #define SPI6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 24, [CCIPR9\_REG](#a3a5cc0435932cbd3235d59f6ce043351))

## [◆ ](#a186de4b3566a20794e4483a9569abe3c)STM32\_CLOCK\_BUS\_AHB1

| #define STM32\_CLOCK\_BUS\_AHB1   0x250 |
| --- |

Bus clocks.

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x254 |
| --- |

## [◆ ](#ab2a3c819828eb0186ac3a3f15f4b4569)STM32\_CLOCK\_BUS\_AHB3

| #define STM32\_CLOCK\_BUS\_AHB3   0x258 |
| --- |

## [◆ ](#a49bccabc3065f192086f16929a7b762d)STM32\_CLOCK\_BUS\_AHB4

| #define STM32\_CLOCK\_BUS\_AHB4   0x25C |
| --- |

## [◆ ](#a623a8ba4dc47622dfbf76801f1582f58)STM32\_CLOCK\_BUS\_AHB5

| #define STM32\_CLOCK\_BUS\_AHB5   0x260 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x264 |
| --- |

## [◆ ](#ad25510091b50e823c9860089a9f23deb)STM32\_CLOCK\_BUS\_APB1\_2

| #define STM32\_CLOCK\_BUS\_APB1\_2   0x268 |
| --- |

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x26C |
| --- |

## [◆ ](#af7165e22b71d1beaf0dd4f59d5b4db6d)STM32\_CLOCK\_BUS\_APB3

| #define STM32\_CLOCK\_BUS\_APB3   0x270 |
| --- |

## [◆ ](#a537105e6125ce3b95a2d69435f47dd51)STM32\_CLOCK\_BUS\_APB4

| #define STM32\_CLOCK\_BUS\_APB4   0x274 |
| --- |

## [◆ ](#a4dc3ff62777a32dfc4e76b281a564c86)STM32\_CLOCK\_BUS\_APB4\_2

| #define STM32\_CLOCK\_BUS\_APB4\_2   0x278 |
| --- |

## [◆ ](#a02ec780a692439efebf0bf8181bf7803)STM32\_CLOCK\_BUS\_APB5

| #define STM32\_CLOCK\_BUS\_APB5   0x27C |
| --- |

## [◆ ](#a3931aa4b01e07a95df585779323a7f48)STM32\_CLOCK\_LP\_BUS\_SHIFT

| #define STM32\_CLOCK\_LP\_BUS\_SHIFT   0x40 |
| --- |

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_APB5](#a02ec780a692439efebf0bf8181bf7803) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_AHB1](#a186de4b3566a20794e4483a9569abe3c) |
| --- |

## [◆ ](#a8b7025d7f4be00a152c53097a414668e)STM32\_SRC\_CKPER

| #define STM32\_SRC\_CKPER   ([STM32\_SRC\_PLL4](#a45ea694120a93c1971fe65ec82d1c4d1) + 1) |
| --- |

Clock muxes.

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

Domain clocks.

System clock Fixed clocks

## [◆ ](#a7bc1dd03186b763b407a044ddffb4ab2)STM32\_SRC\_HSI

| #define STM32\_SRC\_HSI   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

## [◆ ](#aa13b836db0b585e0998b17edb43c41d7)STM32\_SRC\_IC1

| #define STM32\_SRC\_IC1   ([STM32\_SRC\_CKPER](#a8b7025d7f4be00a152c53097a414668e) + 1) |
| --- |

## [◆ ](#a155f8b76c1702064125e99b5facec123)STM32\_SRC\_IC10

| #define STM32\_SRC\_IC10   ([STM32\_SRC\_IC9](#a161620be8255ff4c06bbb9fbe22cea3b) + 1) |
| --- |

## [◆ ](#aac341fc606e3cf6ee2ef69603d60a250)STM32\_SRC\_IC11

| #define STM32\_SRC\_IC11   ([STM32\_SRC\_IC10](#a155f8b76c1702064125e99b5facec123) + 1) |
| --- |

## [◆ ](#a95e0637f72e0f6fbc80f9ce771abc111)STM32\_SRC\_IC12

| #define STM32\_SRC\_IC12   ([STM32\_SRC\_IC11](#aac341fc606e3cf6ee2ef69603d60a250) + 1) |
| --- |

## [◆ ](#a3d76a5bd14d0e0f5a61e38ae33190223)STM32\_SRC\_IC13

| #define STM32\_SRC\_IC13   ([STM32\_SRC\_IC12](#a95e0637f72e0f6fbc80f9ce771abc111) + 1) |
| --- |

## [◆ ](#aac5bc01ec42163ed149440284bdf8592)STM32\_SRC\_IC14

| #define STM32\_SRC\_IC14   ([STM32\_SRC\_IC13](#a3d76a5bd14d0e0f5a61e38ae33190223) + 1) |
| --- |

## [◆ ](#af1fba356ba1dc06132d763d02df1234c)STM32\_SRC\_IC15

| #define STM32\_SRC\_IC15   ([STM32\_SRC\_IC14](#aac5bc01ec42163ed149440284bdf8592) + 1) |
| --- |

## [◆ ](#a47414e92c3cff773978026dede6272ee)STM32\_SRC\_IC16

| #define STM32\_SRC\_IC16   ([STM32\_SRC\_IC15](#af1fba356ba1dc06132d763d02df1234c) + 1) |
| --- |

## [◆ ](#a04b6c1123aa4c7db12e1fb83a9afd838)STM32\_SRC\_IC17

| #define STM32\_SRC\_IC17   ([STM32\_SRC\_IC16](#a47414e92c3cff773978026dede6272ee) + 1) |
| --- |

## [◆ ](#add609ce4fd1723b9662335ab0a835523)STM32\_SRC\_IC18

| #define STM32\_SRC\_IC18   ([STM32\_SRC\_IC17](#a04b6c1123aa4c7db12e1fb83a9afd838) + 1) |
| --- |

## [◆ ](#aee9cb50a33915e66260a0205041091d7)STM32\_SRC\_IC19

| #define STM32\_SRC\_IC19   ([STM32\_SRC\_IC18](#add609ce4fd1723b9662335ab0a835523) + 1) |
| --- |

## [◆ ](#aed86ff6d9d94396b0dfa38a94fc3c121)STM32\_SRC\_IC2

| #define STM32\_SRC\_IC2   ([STM32\_SRC\_IC1](#aa13b836db0b585e0998b17edb43c41d7) + 1) |
| --- |

## [◆ ](#a9aedd874a88b96145f31a76585806ff3)STM32\_SRC\_IC20

| #define STM32\_SRC\_IC20   ([STM32\_SRC\_IC19](#aee9cb50a33915e66260a0205041091d7) + 1) |
| --- |

## [◆ ](#a5cbf858b015f3d890d5584d1a817ee28)STM32\_SRC\_IC3

| #define STM32\_SRC\_IC3   ([STM32\_SRC\_IC2](#aed86ff6d9d94396b0dfa38a94fc3c121) + 1) |
| --- |

## [◆ ](#aa04f6065e9e9c206bbd4b977231a4407)STM32\_SRC\_IC4

| #define STM32\_SRC\_IC4   ([STM32\_SRC\_IC3](#a5cbf858b015f3d890d5584d1a817ee28) + 1) |
| --- |

## [◆ ](#ac1865fa9a7e303b05f1bc6ff6cca5cdc)STM32\_SRC\_IC5

| #define STM32\_SRC\_IC5   ([STM32\_SRC\_IC4](#aa04f6065e9e9c206bbd4b977231a4407) + 1) |
| --- |

## [◆ ](#abd8ade42581f7a8375d8548c7968ae54)STM32\_SRC\_IC6

| #define STM32\_SRC\_IC6   ([STM32\_SRC\_IC5](#ac1865fa9a7e303b05f1bc6ff6cca5cdc) + 1) |
| --- |

## [◆ ](#a590359462bd90dc5e50055e35d794077)STM32\_SRC\_IC7

| #define STM32\_SRC\_IC7   ([STM32\_SRC\_IC6](#abd8ade42581f7a8375d8548c7968ae54) + 1) |
| --- |

## [◆ ](#a2b8c5564a40658105375154f69169d4c)STM32\_SRC\_IC8

| #define STM32\_SRC\_IC8   ([STM32\_SRC\_IC7](#a590359462bd90dc5e50055e35d794077) + 1) |
| --- |

## [◆ ](#a161620be8255ff4c06bbb9fbe22cea3b)STM32\_SRC\_IC9

| #define STM32\_SRC\_IC9   ([STM32\_SRC\_IC8](#a2b8c5564a40658105375154f69169d4c) + 1) |
| --- |

## [◆ ](#a542b4426a15d849545af2fd6012c520c)STM32\_SRC\_MSI

| #define STM32\_SRC\_MSI   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| --- |

## [◆ ](#a19b07a1053f648e063c71884f58644f5)STM32\_SRC\_PLL1

| #define STM32\_SRC\_PLL1   ([STM32\_SRC\_MSI](#a542b4426a15d849545af2fd6012c520c) + 1) |
| --- |

PLL outputs.

## [◆ ](#ad3883851983b32dec66ee645f123ae55)STM32\_SRC\_PLL2

| #define STM32\_SRC\_PLL2   ([STM32\_SRC\_PLL1](#a19b07a1053f648e063c71884f58644f5) + 1) |
| --- |

## [◆ ](#a848b0c6079f693252c1aea11ff1f22d3)STM32\_SRC\_PLL3

| #define STM32\_SRC\_PLL3   ([STM32\_SRC\_PLL2](#ad3883851983b32dec66ee645f123ae55) + 1) |
| --- |

## [◆ ](#a45ea694120a93c1971fe65ec82d1c4d1)STM32\_SRC\_PLL4

| #define STM32\_SRC\_PLL4   ([STM32\_SRC\_PLL3](#a848b0c6079f693252c1aea11ff1f22d3) + 1) |
| --- |

## [◆ ](#a091d597b4979c49951f880bc6ccb4d71)UART4\_SEL

| #define UART4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 12, [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb))

[CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb)

#define CCIPR13\_REG

**Definition** stm32n6\_clock.h:79

## [◆ ](#a136c2c36c89ebdf2c5b97686bbce0209)UART5\_SEL

| #define UART5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 16, [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb))

## [◆ ](#a2d0071bb5cc287b8be749d8abcca6eab)UART7\_SEL

| #define UART7\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 24, [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb))

## [◆ ](#a1b66b237c80c002bc2b422d8fbf61824)UART8\_SEL

| #define UART8\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 28, [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb))

## [◆ ](#a866e45ef86e20589a96ae4533382fb5b)UART9\_SEL

| #define UART9\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR14\_REG](#a07372cf80165afcc7f9297f5b1c33128))

CCIPR14 devices.

## [◆ ](#a5eef37bd8c6a90bf0de08faf5d05f410)USART10\_SEL

| #define USART10\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [CCIPR14\_REG](#a07372cf80165afcc7f9297f5b1c33128))

## [◆ ](#a17f3ec5f86995a2c4087f2988a9486c5)USART1\_SEL

| #define USART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 0, [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb))

CCIPR13 devices.

## [◆ ](#ad67d92dfc439018a7a231e661d10d7f9)USART2\_SEL

| #define USART2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 4, [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb))

## [◆ ](#ad2f356c0bc0e43d6f629cdb840846526)USART3\_SEL

| #define USART3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 8, [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb))

## [◆ ](#a99c9026d61766ec9b91872ee64ad63eb)USART6\_SEL

| #define USART6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 7, 20, [CCIPR13\_REG](#ac5db8f44fd62365a2b508969767acceb))

## [◆ ](#a15df14366d6921bac34208b0c1af0ebb)XSPI1\_SEL

| #define XSPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 0, [CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b))

CCIPR6 devices.

## [◆ ](#a58f2e1e8be7e4e9b50783f03afc687ff)XSPI2\_SEL

| #define XSPI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 4, [CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b))

## [◆ ](#abc02f0330af9bc5e21bccf01204441bc)XSPI3\_SEL

| #define XSPI3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 3, 8, [CCIPR6\_REG](#ab00ea8c2d2b0918b738001b972aacf6b))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32n6\_clock.h](stm32n6__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
