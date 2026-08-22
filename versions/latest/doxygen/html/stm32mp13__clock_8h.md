---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32mp13__clock_8h.html
original_path: doxygen/html/stm32mp13__clock_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32mp13\_clock.h File Reference

`#include "[stm32_common_clocks.h](stm32__common__clocks_8h_source.md)"`

[Go to the source code of this file.](stm32mp13__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6)   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
|  | System clock. |
| #define | [STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2)   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| #define | [STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62)   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
|  | PLL outputs. |
| #define | [STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac)   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
| #define | [STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717)   ([STM32\_SRC\_PLL2\_P](#ae568673a4eca1b42afc59faabb5810ac) + 1) |
| #define | [STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd)   ([STM32\_SRC\_PLL2\_Q](#aaf0a956dda42c2a031cabce49dd3e717) + 1) |
| #define | [STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206)   ([STM32\_SRC\_PLL2\_R](#a57af8944eefa865aa75b6286c13a53cd) + 1) |
| #define | [STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9)   ([STM32\_SRC\_PLL3\_P](#a17c753e0bb8547ea9452f48a65a0a206) + 1) |
| #define | [STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a)   ([STM32\_SRC\_PLL3\_Q](#a9a31a3adebff6a1eee31c287673412c9) + 1) |
| #define | [STM32\_SRC\_PLL4\_P](#a614e65076b0724a4b9a90a9761df7012)   ([STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a) + 1) |
| #define | [STM32\_SRC\_PLL4\_Q](#a4939e61101ce0b4e4c481cce256963f4)   ([STM32\_SRC\_PLL4\_P](#a614e65076b0724a4b9a90a9761df7012) + 1) |
| #define | [STM32\_SRC\_PLL4\_R](#aa4e74a6cd263af35031984b3bd42aa0d)   ([STM32\_SRC\_PLL4\_Q](#a4939e61101ce0b4e4c481cce256963f4) + 1) |
| #define | [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95)   0x700 |
|  | Bus clocks. |
| #define | [STM32\_CLOCK\_BUS\_APB2](#adb7becb609763568b91303041c9cd4db)   0x708 |
| #define | [STM32\_CLOCK\_BUS\_APB3](#af7165e22b71d1beaf0dd4f59d5b4db6d)   0x710 |
| #define | [STM32\_CLOCK\_BUS\_APB4](#a537105e6125ce3b95a2d69435f47dd51)   0x728 |
| #define | [STM32\_CLOCK\_BUS\_APB4\_NS](#ae152597ed9e57e1067dd16994d62fb0a)   0x738 |
| #define | [STM32\_CLOCK\_BUS\_APB5](#a02ec780a692439efebf0bf8181bf7803)   0x740 |
| #define | [STM32\_CLOCK\_BUS\_APB6](#a55ecb827ff96585f31fa9fc3d1535822)   0x748 |
| #define | [STM32\_CLOCK\_BUS\_AHB2](#a5e58ef1846c185b04bed598b26ee9205)   0x750 |
| #define | [STM32\_CLOCK\_BUS\_AHB4](#a49bccabc3065f192086f16929a7b762d)   0x768 |
| #define | [STM32\_CLOCK\_BUS\_AHB5](#a623a8ba4dc47622dfbf76801f1582f58)   0x778 |
| #define | [STM32\_CLOCK\_BUS\_AHB6](#a19119341d73264f1f9f18f3fe64f7bd1)   0x780 |
| #define | [STM32\_PERIPH\_BUS\_MIN](#acc0577552371fcda95685f6424ecb4b2)   [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95) |
| #define | [STM32\_PERIPH\_BUS\_MAX](#a561265772438ab8995251760c7f3dc30)   [STM32\_CLOCK\_BUS\_AHB6](#a19119341d73264f1f9f18f3fe64f7bd1) |
| #define | [MCO1CFGR\_REG](#a6394a79a2e9e8b066b86c801fc728d59)   0x460 |
|  | Device domain clocks selection helpers. |
| #define | [MCO2CFGR\_REG](#aa24514646b50cd8b0dc9ed0773e5f82d)   0x464 |
| #define | [I2C12CKSELR\_REG](#a33a4edf33375910dce464a5a66643d52)   0x600 |
| #define | [I2C345CKSELR\_REG](#a36dacdc312d713a66aebc2a2dbd568ae)   0x604 |
| #define | [SPI2S1CKSELR\_REG](#a100ef3300f3e05ec061477fc686ae998)   0x608 |
| #define | [SPI2S23CKSELR\_REG](#a16d5d1e10cd09338e1dc841b81c28229)   0x60c |
| #define | [SPI45CKSELR\_REG](#aff103be77a79465724670d76af7c9c4e)   0x610 |
| #define | [UART12CKSELR\_REG](#aa8eb2eef02227733c7c0961e4561f965)   0x614 |
| #define | [UART35CKSELR\_REG](#a3f8eee67e3fa900605d15dde78b8f357)   0x618 |
| #define | [UART4CKSELR\_REG](#ae7ab8abfbe4879ee20fce191d0c17611)   0x61c |
| #define | [UART6CKSELR\_REG](#a769e1f639865d81e2b4bb9be3ab8cc0b)   0x620 |
| #define | [UART78CKSELR\_REG](#a729992dea3365b21bc53cdf3ea5e2fa6)   0x624 |
| #define | [LPTIM1CKSELR\_REG](#aa173ef84dcba8fe29452c21cdb7e7d75)   0x628 |
| #define | [LPTIM23CKSELR\_REG](#a884ca27b18f8dc3f1a04891170d564c7)   0x62c |
| #define | [LPTIM45CKSELR\_REG](#a5806e02253853ba1156a1a4c69ea49d3)   0x630 |
| #define | [SAI1CKSELR\_REG](#a12d0eb312c74a9127853994b3daa7418)   0x634 |
| #define | [SAI2CKSELR\_REG](#abb4307131a38e26886cd9f27af4ddfe1)   0x638 |
| #define | [FDCANCKSELR\_REG](#a971421a8deec5635012305b26ef563ec)   0x63c |
| #define | [SPDIFCKSELR\_REG](#a1e0da281a34b9257e8d9dd0b81d7fafd)   0x640 |
| #define | [ADC12CKSELR\_REG](#aa783dacddb5a6116d7b10dc5f858a02c)   0x644 |
| #define | [SDMMC12CKSELR\_REG](#a778eac4d709f73d443089c52f0085c65)   0x648 |
| #define | [ETH12CKSELR\_REG](#a921b805671555768481672596d54d5a0)   0x64c |
| #define | [USBCKSELR\_REG](#ae42a4c180140e1b6b87ff3a2fb666955)   0x650 |
| #define | [QSPICKSELR\_REG](#a774ea01b7d6909ec3629cbe73a1e75de)   0x654 |
| #define | [FMCCKSELR\_REG](#aab13b7fbac5eb80767b83e4bf8c09fd9)   0x658 |
| #define | [RNG1CKSELR\_REG](#ade77c5f1a8d268bcddf37e6e8e94d02c)   0x65c |
| #define | [STGENCKSELR\_REG](#a5d1600ae93964d82568442decaf7eb72)   0x660 |
| #define | [DCMIPPCKSELR\_REG](#a1f817073a47e6bfb9bcaab295c5a9b4e)   0x664 |
| #define | [SAESCKSELR\_REG](#aeb686993b410efe3ce5a68a3ac43657f)   0x668 |
| #define | [MCO1\_SEL](#acc5c7aed4e842ca212471d7a58504821)(val) |
|  | MCO1CFGR / MCO2CFGR devices. |
| #define | [MCO1\_PRE](#a2805cf7e0b5ed0a9bb4bfff863327081)(val) |
| #define | [MCO2\_SEL](#ab5fc05cb6aa1154c54c29b95f3154a75)(val) |
| #define | [MCO2\_PRE](#ab02a0ccbb8588979ca4742c72c59589f)(val) |
| #define | [MCOX\_ON](#ac41d16cf96d9a7495857b70211abc1e1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [MCO1\_SEL\_HSI](#a6eb144ce115b853faa29de37eb146bc7)   0 |
| #define | [MCO1\_SEL\_HSE](#a2c84d124af72fb9a2f579a4a1df078bb)   1 |
| #define | [MCO1\_SEL\_CSI](#a8515ec118d2560401c351ee232836ad4)   2 |
| #define | [MCO1\_SEL\_LSI](#ad5b4da133657b2efb33699c71f636ff2)   3 |
| #define | [MCO1\_SEL\_LSE](#af573b66b787ce18736116b4c503bc616)   4 |
| #define | [MCO2\_SEL\_MPU](#a9704e8e10de965c55fbb5fd24c7f3578)   0 |
| #define | [MCO2\_SEL\_AXI](#a76cf5ab48c0607ebe1325522a0a09128)   1 |
| #define | [MCO2\_SEL\_MLAHB](#a0cb908baba3eea8c42c26c3b75c9ef30)   2 |
| #define | [MCO2\_SEL\_PLL4](#ad9461d250a0bfe95f3bd2227424a8e39)   3 |
| #define | [MCO2\_SEL\_HSE](#a08e910755a034001bf34746f7be51186)   4 |
| #define | [MCO2\_SEL\_HSI](#acb06f32d3df5fd05f665f7fbaea3ffd6)   5 |
| #define | [MCO\_PRE\_DIV\_1](#aa6d6446aa7a1c84324475f6e8665fbb7)   0 |
| #define | [MCO\_PRE\_DIV\_2](#a36db847c7932669759f64844a15c42c3)   1 |
| #define | [MCO\_PRE\_DIV\_3](#a1d99057b6886474182adffcff4f246f2)   2 |
| #define | [MCO\_PRE\_DIV\_4](#a74c5b485d9169c489ab19e788b43c657)   3 |
| #define | [MCO\_PRE\_DIV\_5](#aad3773cb5fbea15e6cddf688dea3cd04)   4 |
| #define | [MCO\_PRE\_DIV\_6](#a3cb780fda9d369607e1c51a7cddff300)   5 |
| #define | [MCO\_PRE\_DIV\_7](#a08634986618842af08073f59c6da3e8f)   6 |
| #define | [MCO\_PRE\_DIV\_8](#ad1bb69ff2fe6748978c31666f201947c)   7 |
| #define | [MCO\_PRE\_DIV\_9](#a7841c7ceb21754059717c5996a081cb4)   8 |
| #define | [MCO\_PRE\_DIV\_10](#aecc309343fad5680088593eff549748c)   9 |
| #define | [MCO\_PRE\_DIV\_11](#a3c4b271ad0c50ec7eb9edd779c30b3d9)   10 |
| #define | [MCO\_PRE\_DIV\_12](#aa93517f599cd367844383018b962319f)   11 |
| #define | [MCO\_PRE\_DIV\_13](#a3fcce904cb4650ec093f4aba0a8b7a51)   12 |
| #define | [MCO\_PRE\_DIV\_14](#aff3b9f97c2b1b70f090a7c27ca57ca58)   13 |
| #define | [MCO\_PRE\_DIV\_15](#affa380b0a33facd4d5fdd9dc405c6ddc)   14 |
| #define | [MCO\_PRE\_DIV\_16](#a111fd8dc5850b16b1308c8eaba8a9458)   15 |
| #define | [I2C12\_SEL](#abf19277267381c87be1cfe8c674b2fd3)(val) |
| #define | [I2C3\_SEL](#aa12a1d2ac790880b7148d1e5660eb941)(val) |
| #define | [I2C4\_SEL](#a55880006ae28021de4d148924c06001e)(val) |
| #define | [I2C5\_SEL](#ab9c645c57c03d284386ba0b4fd37d11f)(val) |
| #define | [SPI1\_SEL](#a5199102173e9dbe957230f356e14d910)(val) |
| #define | [SPI23\_SEL](#ad760ef96e4fd9ca527e7d9c746d1c9f3)(val) |
| #define | [SPI4\_SEL](#a55086a94321a6e1af527a46c644f6c5e)(val) |
| #define | [SPI5\_SEL](#ac7193e508815171a4d73795d24086136)(val) |
| #define | [UART1\_SEL](#ac6a3ae8d4166fa44f582f4f16e53db50)(val) |
| #define | [UART2\_SEL](#a8d63eb1134e04f1785e24f119b474d91)(val) |
| #define | [UART35\_SEL](#a68421d716894d77ca963a15ccc9d162c)(val) |
| #define | [UART4\_SEL](#a091d597b4979c49951f880bc6ccb4d71)(val) |
| #define | [UART6\_SEL](#ab1e6024b64a1715165a2ca7c78bb595e)(val) |
| #define | [UART78\_SEL](#a6c82e4677e11f3cb61af1c092b786233)(val) |
| #define | [LPTIME1\_SEL](#aaf12c6964a0787aebb10ab1e2bbc7406)(val) |
| #define | [LPTIME2\_SEL](#ace6379a6f2d2e1803abff6c0215c3c7d)(val) |
| #define | [LPTIME3\_SEL](#a43016575086a5ab614d1edaaecfbfb83)(val) |
| #define | [LPTIME45\_SEL](#ae4eb19cd052b1ef0efc4b1f175048867)(val) |
| #define | [SAI1\_SEL](#ab8e49f6309adb53edd9ad3d051d451db)(val) |
| #define | [SAI2\_SEL](#a4fb9a6b79339e822f0ae426e8bba7486)(val) |
| #define | [FDCAN\_SEL](#ac1df6369669b4b3febd0525426e76499)(val) |
| #define | [SPDIF\_SEL](#a37e4a34b034dee8d7f0b1fa1378e6ff6)(val) |
| #define | [ADC1\_SEL](#a0751699f49808d31e15ec33f2b7d4618)(val) |
| #define | [ADC2\_SEL](#adeba2b1b877321bce680ae778659b5a7)(val) |
| #define | [SDMMC1\_SEL](#a1a4999da331afff86581c8a6cea6afe9)(val) |
| #define | [SDMMC2\_SEL](#a7319710d63129ad13039565cad2b4950)(val) |
| #define | [ETH1\_SEL](#a4e9282866e4f40cf5d6fd0a655fa6fa1)(val) |
| #define | [ETH2\_SEL](#a1e424c22dd1d25c08ce3d36bce3a7c70)(val) |
| #define | [USBPHY\_SEL](#a84d56b16e3adca6411bc9daabb32a31b)(val) |
| #define | [USBOTG\_SEL](#a2d691cea81bfb356af592ccedafc62ef)(val) |
| #define | [QSPI\_SEL](#ae66e7abfb9009e737cff676fb4e5155f)(val) |
| #define | [FMC\_SEL](#a0de89c03e0cd384de7f594aa5c5e82de)(val) |
| #define | [RNG1\_SEL](#aedecc651f8bde3a11944772354691a93)(val) |
| #define | [STGEN\_SEL](#aa94e7a102c493fafd093208e079062a7)(val) |
| #define | [DCMIPP\_SEL](#a5b9758e95788f06d93382daec60fdf3f)(val) |
| #define | [SAES\_SEL](#a9072e326043742dc4299de1b64a2dd9d)(val) |

## Macro Definition Documentation

## [◆ ](#aa783dacddb5a6116d7b10dc5f858a02c)ADC12CKSELR\_REG

| #define ADC12CKSELR\_REG   0x644 |
| --- |

## [◆ ](#a0751699f49808d31e15ec33f2b7d4618)ADC1\_SEL

| #define ADC1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [ADC12CKSELR\_REG](#aa783dacddb5a6116d7b10dc5f858a02c))

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)

#define STM32\_DT\_CLOCK\_SELECT(val, mask, shift, reg)

Pack STM32 source clock selection RCC register bit fields for the DT.

**Definition** stm32\_common\_clocks.h:46

[ADC12CKSELR\_REG](#aa783dacddb5a6116d7b10dc5f858a02c)

#define ADC12CKSELR\_REG

**Definition** stm32mp13\_clock.h:65

## [◆ ](#adeba2b1b877321bce680ae778659b5a7)ADC2\_SEL

| #define ADC2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 2, [ADC12CKSELR\_REG](#aa783dacddb5a6116d7b10dc5f858a02c))

## [◆ ](#a5b9758e95788f06d93382daec60fdf3f)DCMIPP\_SEL

| #define DCMIPP\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [DCMIPPCKSELR\_REG](#a1f817073a47e6bfb9bcaab295c5a9b4e))

[DCMIPPCKSELR\_REG](#a1f817073a47e6bfb9bcaab295c5a9b4e)

#define DCMIPPCKSELR\_REG

**Definition** stm32mp13\_clock.h:73

## [◆ ](#a1f817073a47e6bfb9bcaab295c5a9b4e)DCMIPPCKSELR\_REG

| #define DCMIPPCKSELR\_REG   0x664 |
| --- |

## [◆ ](#a921b805671555768481672596d54d5a0)ETH12CKSELR\_REG

| #define ETH12CKSELR\_REG   0x64c |
| --- |

## [◆ ](#a4e9282866e4f40cf5d6fd0a655fa6fa1)ETH1\_SEL

| #define ETH1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [ETH12CKSELR\_REG](#a921b805671555768481672596d54d5a0))

[ETH12CKSELR\_REG](#a921b805671555768481672596d54d5a0)

#define ETH12CKSELR\_REG

**Definition** stm32mp13\_clock.h:67

## [◆ ](#a1e424c22dd1d25c08ce3d36bce3a7c70)ETH2\_SEL

| #define ETH2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 8, [ETH12CKSELR\_REG](#a921b805671555768481672596d54d5a0))

## [◆ ](#ac1df6369669b4b3febd0525426e76499)FDCAN\_SEL

| #define FDCAN\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [FDCANCKSELR\_REG](#a971421a8deec5635012305b26ef563ec))

[FDCANCKSELR\_REG](#a971421a8deec5635012305b26ef563ec)

#define FDCANCKSELR\_REG

**Definition** stm32mp13\_clock.h:63

## [◆ ](#a971421a8deec5635012305b26ef563ec)FDCANCKSELR\_REG

| #define FDCANCKSELR\_REG   0x63c |
| --- |

## [◆ ](#a0de89c03e0cd384de7f594aa5c5e82de)FMC\_SEL

| #define FMC\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [FMCCKSELR\_REG](#aab13b7fbac5eb80767b83e4bf8c09fd9))

[FMCCKSELR\_REG](#aab13b7fbac5eb80767b83e4bf8c09fd9)

#define FMCCKSELR\_REG

**Definition** stm32mp13\_clock.h:70

## [◆ ](#aab13b7fbac5eb80767b83e4bf8c09fd9)FMCCKSELR\_REG

| #define FMCCKSELR\_REG   0x658 |
| --- |

## [◆ ](#abf19277267381c87be1cfe8c674b2fd3)I2C12\_SEL

| #define I2C12\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [I2C12CKSELR\_REG](#a33a4edf33375910dce464a5a66643d52))

[I2C12CKSELR\_REG](#a33a4edf33375910dce464a5a66643d52)

#define I2C12CKSELR\_REG

**Definition** stm32mp13\_clock.h:48

## [◆ ](#a33a4edf33375910dce464a5a66643d52)I2C12CKSELR\_REG

| #define I2C12CKSELR\_REG   0x600 |
| --- |

## [◆ ](#a36dacdc312d713a66aebc2a2dbd568ae)I2C345CKSELR\_REG

| #define I2C345CKSELR\_REG   0x604 |
| --- |

## [◆ ](#aa12a1d2ac790880b7148d1e5660eb941)I2C3\_SEL

| #define I2C3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [I2C345CKSELR\_REG](#a36dacdc312d713a66aebc2a2dbd568ae))

[I2C345CKSELR\_REG](#a36dacdc312d713a66aebc2a2dbd568ae)

#define I2C345CKSELR\_REG

**Definition** stm32mp13\_clock.h:49

## [◆ ](#a55880006ae28021de4d148924c06001e)I2C4\_SEL

| #define I2C4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 3, [I2C345CKSELR\_REG](#a36dacdc312d713a66aebc2a2dbd568ae))

## [◆ ](#ab9c645c57c03d284386ba0b4fd37d11f)I2C5\_SEL

| #define I2C5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 6, [I2C345CKSELR\_REG](#a36dacdc312d713a66aebc2a2dbd568ae))

## [◆ ](#aa173ef84dcba8fe29452c21cdb7e7d75)LPTIM1CKSELR\_REG

| #define LPTIM1CKSELR\_REG   0x628 |
| --- |

## [◆ ](#a884ca27b18f8dc3f1a04891170d564c7)LPTIM23CKSELR\_REG

| #define LPTIM23CKSELR\_REG   0x62c |
| --- |

## [◆ ](#a5806e02253853ba1156a1a4c69ea49d3)LPTIM45CKSELR\_REG

| #define LPTIM45CKSELR\_REG   0x630 |
| --- |

## [◆ ](#aaf12c6964a0787aebb10ab1e2bbc7406)LPTIME1\_SEL

| #define LPTIME1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [LPTIM1CKSELR\_REG](#aa173ef84dcba8fe29452c21cdb7e7d75))

[LPTIM1CKSELR\_REG](#aa173ef84dcba8fe29452c21cdb7e7d75)

#define LPTIM1CKSELR\_REG

**Definition** stm32mp13\_clock.h:58

## [◆ ](#ace6379a6f2d2e1803abff6c0215c3c7d)LPTIME2\_SEL

| #define LPTIME2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [LPTIM23CKSELR\_REG](#a884ca27b18f8dc3f1a04891170d564c7))

[LPTIM23CKSELR\_REG](#a884ca27b18f8dc3f1a04891170d564c7)

#define LPTIM23CKSELR\_REG

**Definition** stm32mp13\_clock.h:59

## [◆ ](#a43016575086a5ab614d1edaaecfbfb83)LPTIME3\_SEL

| #define LPTIME3\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 3, [LPTIM23CKSELR\_REG](#a884ca27b18f8dc3f1a04891170d564c7))

## [◆ ](#ae4eb19cd052b1ef0efc4b1f175048867)LPTIME45\_SEL

| #define LPTIME45\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [LPTIM45CKSELR\_REG](#a5806e02253853ba1156a1a4c69ea49d3))

[LPTIM45CKSELR\_REG](#a5806e02253853ba1156a1a4c69ea49d3)

#define LPTIM45CKSELR\_REG

**Definition** stm32mp13\_clock.h:60

## [◆ ](#a2805cf7e0b5ed0a9bb4bfff863327081)MCO1\_PRE

| #define MCO1\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0xf, 4, [MCO1CFGR\_REG](#a6394a79a2e9e8b066b86c801fc728d59))

[MCO1CFGR\_REG](#a6394a79a2e9e8b066b86c801fc728d59)

#define MCO1CFGR\_REG

Device domain clocks selection helpers.

**Definition** stm32mp13\_clock.h:46

## [◆ ](#acc5c7aed4e842ca212471d7a58504821)MCO1\_SEL

| #define MCO1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [MCO1CFGR\_REG](#a6394a79a2e9e8b066b86c801fc728d59))

MCO1CFGR / MCO2CFGR devices.

## [◆ ](#a8515ec118d2560401c351ee232836ad4)MCO1\_SEL\_CSI

| #define MCO1\_SEL\_CSI   2 |
| --- |

## [◆ ](#a2c84d124af72fb9a2f579a4a1df078bb)MCO1\_SEL\_HSE

| #define MCO1\_SEL\_HSE   1 |
| --- |

## [◆ ](#a6eb144ce115b853faa29de37eb146bc7)MCO1\_SEL\_HSI

| #define MCO1\_SEL\_HSI   0 |
| --- |

## [◆ ](#af573b66b787ce18736116b4c503bc616)MCO1\_SEL\_LSE

| #define MCO1\_SEL\_LSE   4 |
| --- |

## [◆ ](#ad5b4da133657b2efb33699c71f636ff2)MCO1\_SEL\_LSI

| #define MCO1\_SEL\_LSI   3 |
| --- |

## [◆ ](#a6394a79a2e9e8b066b86c801fc728d59)MCO1CFGR\_REG

| #define MCO1CFGR\_REG   0x460 |
| --- |

Device domain clocks selection helpers.

## [◆ ](#ab02a0ccbb8588979ca4742c72c59589f)MCO2\_PRE

| #define MCO2\_PRE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0xf, 4, [MCO2CFGR\_REG](#aa24514646b50cd8b0dc9ed0773e5f82d))

[MCO2CFGR\_REG](#aa24514646b50cd8b0dc9ed0773e5f82d)

#define MCO2CFGR\_REG

**Definition** stm32mp13\_clock.h:47

## [◆ ](#ab5fc05cb6aa1154c54c29b95f3154a75)MCO2\_SEL

| #define MCO2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [MCO2CFGR\_REG](#aa24514646b50cd8b0dc9ed0773e5f82d))

## [◆ ](#a76cf5ab48c0607ebe1325522a0a09128)MCO2\_SEL\_AXI

| #define MCO2\_SEL\_AXI   1 |
| --- |

## [◆ ](#a08e910755a034001bf34746f7be51186)MCO2\_SEL\_HSE

| #define MCO2\_SEL\_HSE   4 |
| --- |

## [◆ ](#acb06f32d3df5fd05f665f7fbaea3ffd6)MCO2\_SEL\_HSI

| #define MCO2\_SEL\_HSI   5 |
| --- |

## [◆ ](#a0cb908baba3eea8c42c26c3b75c9ef30)MCO2\_SEL\_MLAHB

| #define MCO2\_SEL\_MLAHB   2 |
| --- |

## [◆ ](#a9704e8e10de965c55fbb5fd24c7f3578)MCO2\_SEL\_MPU

| #define MCO2\_SEL\_MPU   0 |
| --- |

## [◆ ](#ad9461d250a0bfe95f3bd2227424a8e39)MCO2\_SEL\_PLL4

| #define MCO2\_SEL\_PLL4   3 |
| --- |

## [◆ ](#aa24514646b50cd8b0dc9ed0773e5f82d)MCO2CFGR\_REG

| #define MCO2CFGR\_REG   0x464 |
| --- |

## [◆ ](#aa6d6446aa7a1c84324475f6e8665fbb7)MCO\_PRE\_DIV\_1

| #define MCO\_PRE\_DIV\_1   0 |
| --- |

## [◆ ](#aecc309343fad5680088593eff549748c)MCO\_PRE\_DIV\_10

| #define MCO\_PRE\_DIV\_10   9 |
| --- |

## [◆ ](#a3c4b271ad0c50ec7eb9edd779c30b3d9)MCO\_PRE\_DIV\_11

| #define MCO\_PRE\_DIV\_11   10 |
| --- |

## [◆ ](#aa93517f599cd367844383018b962319f)MCO\_PRE\_DIV\_12

| #define MCO\_PRE\_DIV\_12   11 |
| --- |

## [◆ ](#a3fcce904cb4650ec093f4aba0a8b7a51)MCO\_PRE\_DIV\_13

| #define MCO\_PRE\_DIV\_13   12 |
| --- |

## [◆ ](#aff3b9f97c2b1b70f090a7c27ca57ca58)MCO\_PRE\_DIV\_14

| #define MCO\_PRE\_DIV\_14   13 |
| --- |

## [◆ ](#affa380b0a33facd4d5fdd9dc405c6ddc)MCO\_PRE\_DIV\_15

| #define MCO\_PRE\_DIV\_15   14 |
| --- |

## [◆ ](#a111fd8dc5850b16b1308c8eaba8a9458)MCO\_PRE\_DIV\_16

| #define MCO\_PRE\_DIV\_16   15 |
| --- |

## [◆ ](#a36db847c7932669759f64844a15c42c3)MCO\_PRE\_DIV\_2

| #define MCO\_PRE\_DIV\_2   1 |
| --- |

## [◆ ](#a1d99057b6886474182adffcff4f246f2)MCO\_PRE\_DIV\_3

| #define MCO\_PRE\_DIV\_3   2 |
| --- |

## [◆ ](#a74c5b485d9169c489ab19e788b43c657)MCO\_PRE\_DIV\_4

| #define MCO\_PRE\_DIV\_4   3 |
| --- |

## [◆ ](#aad3773cb5fbea15e6cddf688dea3cd04)MCO\_PRE\_DIV\_5

| #define MCO\_PRE\_DIV\_5   4 |
| --- |

## [◆ ](#a3cb780fda9d369607e1c51a7cddff300)MCO\_PRE\_DIV\_6

| #define MCO\_PRE\_DIV\_6   5 |
| --- |

## [◆ ](#a08634986618842af08073f59c6da3e8f)MCO\_PRE\_DIV\_7

| #define MCO\_PRE\_DIV\_7   6 |
| --- |

## [◆ ](#ad1bb69ff2fe6748978c31666f201947c)MCO\_PRE\_DIV\_8

| #define MCO\_PRE\_DIV\_8   7 |
| --- |

## [◆ ](#a7841c7ceb21754059717c5996a081cb4)MCO\_PRE\_DIV\_9

| #define MCO\_PRE\_DIV\_9   8 |
| --- |

## [◆ ](#ac41d16cf96d9a7495857b70211abc1e1)MCOX\_ON

| #define MCOX\_ON   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#ae66e7abfb9009e737cff676fb4e5155f)QSPI\_SEL

| #define QSPI\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [QSPICKSELR\_REG](#a774ea01b7d6909ec3629cbe73a1e75de))

[QSPICKSELR\_REG](#a774ea01b7d6909ec3629cbe73a1e75de)

#define QSPICKSELR\_REG

**Definition** stm32mp13\_clock.h:69

## [◆ ](#a774ea01b7d6909ec3629cbe73a1e75de)QSPICKSELR\_REG

| #define QSPICKSELR\_REG   0x654 |
| --- |

## [◆ ](#aedecc651f8bde3a11944772354691a93)RNG1\_SEL

| #define RNG1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [RNG1CKSELR\_REG](#ade77c5f1a8d268bcddf37e6e8e94d02c))

[RNG1CKSELR\_REG](#ade77c5f1a8d268bcddf37e6e8e94d02c)

#define RNG1CKSELR\_REG

**Definition** stm32mp13\_clock.h:71

## [◆ ](#ade77c5f1a8d268bcddf37e6e8e94d02c)RNG1CKSELR\_REG

| #define RNG1CKSELR\_REG   0x65c |
| --- |

## [◆ ](#a9072e326043742dc4299de1b64a2dd9d)SAES\_SEL

| #define SAES\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [SAESCKSELR\_REG](#aeb686993b410efe3ce5a68a3ac43657f))

[SAESCKSELR\_REG](#aeb686993b410efe3ce5a68a3ac43657f)

#define SAESCKSELR\_REG

**Definition** stm32mp13\_clock.h:74

## [◆ ](#aeb686993b410efe3ce5a68a3ac43657f)SAESCKSELR\_REG

| #define SAESCKSELR\_REG   0x668 |
| --- |

## [◆ ](#ab8e49f6309adb53edd9ad3d051d451db)SAI1\_SEL

| #define SAI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [SAI1CKSELR\_REG](#a12d0eb312c74a9127853994b3daa7418))

[SAI1CKSELR\_REG](#a12d0eb312c74a9127853994b3daa7418)

#define SAI1CKSELR\_REG

**Definition** stm32mp13\_clock.h:61

## [◆ ](#a12d0eb312c74a9127853994b3daa7418)SAI1CKSELR\_REG

| #define SAI1CKSELR\_REG   0x634 |
| --- |

## [◆ ](#a4fb9a6b79339e822f0ae426e8bba7486)SAI2\_SEL

| #define SAI2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [SAI2CKSELR\_REG](#abb4307131a38e26886cd9f27af4ddfe1))

[SAI2CKSELR\_REG](#abb4307131a38e26886cd9f27af4ddfe1)

#define SAI2CKSELR\_REG

**Definition** stm32mp13\_clock.h:62

## [◆ ](#abb4307131a38e26886cd9f27af4ddfe1)SAI2CKSELR\_REG

| #define SAI2CKSELR\_REG   0x638 |
| --- |

## [◆ ](#a778eac4d709f73d443089c52f0085c65)SDMMC12CKSELR\_REG

| #define SDMMC12CKSELR\_REG   0x648 |
| --- |

## [◆ ](#a1a4999da331afff86581c8a6cea6afe9)SDMMC1\_SEL

| #define SDMMC1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [SDMMC12CKSELR\_REG](#a778eac4d709f73d443089c52f0085c65))

[SDMMC12CKSELR\_REG](#a778eac4d709f73d443089c52f0085c65)

#define SDMMC12CKSELR\_REG

**Definition** stm32mp13\_clock.h:66

## [◆ ](#a7319710d63129ad13039565cad2b4950)SDMMC2\_SEL

| #define SDMMC2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 3, [SDMMC12CKSELR\_REG](#a778eac4d709f73d443089c52f0085c65))

## [◆ ](#a37e4a34b034dee8d7f0b1fa1378e6ff6)SPDIF\_SEL

| #define SPDIF\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [SPDIFCKSELR\_REG](#a1e0da281a34b9257e8d9dd0b81d7fafd))

[SPDIFCKSELR\_REG](#a1e0da281a34b9257e8d9dd0b81d7fafd)

#define SPDIFCKSELR\_REG

**Definition** stm32mp13\_clock.h:64

## [◆ ](#a1e0da281a34b9257e8d9dd0b81d7fafd)SPDIFCKSELR\_REG

| #define SPDIFCKSELR\_REG   0x640 |
| --- |

## [◆ ](#a5199102173e9dbe957230f356e14d910)SPI1\_SEL

| #define SPI1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [SPI2S1CKSELR\_REG](#a100ef3300f3e05ec061477fc686ae998))

[SPI2S1CKSELR\_REG](#a100ef3300f3e05ec061477fc686ae998)

#define SPI2S1CKSELR\_REG

**Definition** stm32mp13\_clock.h:50

## [◆ ](#ad760ef96e4fd9ca527e7d9c746d1c9f3)SPI23\_SEL

| #define SPI23\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [SPI2S23CKSELR\_REG](#a16d5d1e10cd09338e1dc841b81c28229))

[SPI2S23CKSELR\_REG](#a16d5d1e10cd09338e1dc841b81c28229)

#define SPI2S23CKSELR\_REG

**Definition** stm32mp13\_clock.h:51

## [◆ ](#a100ef3300f3e05ec061477fc686ae998)SPI2S1CKSELR\_REG

| #define SPI2S1CKSELR\_REG   0x608 |
| --- |

## [◆ ](#a16d5d1e10cd09338e1dc841b81c28229)SPI2S23CKSELR\_REG

| #define SPI2S23CKSELR\_REG   0x60c |
| --- |

## [◆ ](#aff103be77a79465724670d76af7c9c4e)SPI45CKSELR\_REG

| #define SPI45CKSELR\_REG   0x610 |
| --- |

## [◆ ](#a55086a94321a6e1af527a46c644f6c5e)SPI4\_SEL

| #define SPI4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [SPI45CKSELR\_REG](#aff103be77a79465724670d76af7c9c4e))

[SPI45CKSELR\_REG](#aff103be77a79465724670d76af7c9c4e)

#define SPI45CKSELR\_REG

**Definition** stm32mp13\_clock.h:52

## [◆ ](#ac7193e508815171a4d73795d24086136)SPI5\_SEL

| #define SPI5\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 3, [SPI45CKSELR\_REG](#aff103be77a79465724670d76af7c9c4e))

## [◆ ](#aa94e7a102c493fafd093208e079062a7)STGEN\_SEL

| #define STGEN\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [STGENCKSELR\_REG](#a5d1600ae93964d82568442decaf7eb72))

[STGENCKSELR\_REG](#a5d1600ae93964d82568442decaf7eb72)

#define STGENCKSELR\_REG

**Definition** stm32mp13\_clock.h:72

## [◆ ](#a5d1600ae93964d82568442decaf7eb72)STGENCKSELR\_REG

| #define STGENCKSELR\_REG   0x660 |
| --- |

## [◆ ](#a5e58ef1846c185b04bed598b26ee9205)STM32\_CLOCK\_BUS\_AHB2

| #define STM32\_CLOCK\_BUS\_AHB2   0x750 |
| --- |

## [◆ ](#a49bccabc3065f192086f16929a7b762d)STM32\_CLOCK\_BUS\_AHB4

| #define STM32\_CLOCK\_BUS\_AHB4   0x768 |
| --- |

## [◆ ](#a623a8ba4dc47622dfbf76801f1582f58)STM32\_CLOCK\_BUS\_AHB5

| #define STM32\_CLOCK\_BUS\_AHB5   0x778 |
| --- |

## [◆ ](#a19119341d73264f1f9f18f3fe64f7bd1)STM32\_CLOCK\_BUS\_AHB6

| #define STM32\_CLOCK\_BUS\_AHB6   0x780 |
| --- |

## [◆ ](#ac763945fc36124f9c978c423826faa95)STM32\_CLOCK\_BUS\_APB1

| #define STM32\_CLOCK\_BUS\_APB1   0x700 |
| --- |

Bus clocks.

## [◆ ](#adb7becb609763568b91303041c9cd4db)STM32\_CLOCK\_BUS\_APB2

| #define STM32\_CLOCK\_BUS\_APB2   0x708 |
| --- |

## [◆ ](#af7165e22b71d1beaf0dd4f59d5b4db6d)STM32\_CLOCK\_BUS\_APB3

| #define STM32\_CLOCK\_BUS\_APB3   0x710 |
| --- |

## [◆ ](#a537105e6125ce3b95a2d69435f47dd51)STM32\_CLOCK\_BUS\_APB4

| #define STM32\_CLOCK\_BUS\_APB4   0x728 |
| --- |

## [◆ ](#ae152597ed9e57e1067dd16994d62fb0a)STM32\_CLOCK\_BUS\_APB4\_NS

| #define STM32\_CLOCK\_BUS\_APB4\_NS   0x738 |
| --- |

## [◆ ](#a02ec780a692439efebf0bf8181bf7803)STM32\_CLOCK\_BUS\_APB5

| #define STM32\_CLOCK\_BUS\_APB5   0x740 |
| --- |

## [◆ ](#a55ecb827ff96585f31fa9fc3d1535822)STM32\_CLOCK\_BUS\_APB6

| #define STM32\_CLOCK\_BUS\_APB6   0x748 |
| --- |

## [◆ ](#a561265772438ab8995251760c7f3dc30)STM32\_PERIPH\_BUS\_MAX

| #define STM32\_PERIPH\_BUS\_MAX   [STM32\_CLOCK\_BUS\_AHB6](#a19119341d73264f1f9f18f3fe64f7bd1) |
| --- |

## [◆ ](#acc0577552371fcda95685f6424ecb4b2)STM32\_PERIPH\_BUS\_MIN

| #define STM32\_PERIPH\_BUS\_MIN   [STM32\_CLOCK\_BUS\_APB1](#ac763945fc36124f9c978c423826faa95) |
| --- |

## [◆ ](#aa7e82706a146d0f40dc7e9755b3be9a6)STM32\_SRC\_HSE

| #define STM32\_SRC\_HSE   ([STM32\_SRC\_LSI](stm32__common__clocks_8h.md#ac6233dbbaff45f6862b21debbf180640) + 1) |
| --- |

System clock.

Fixed clocks

## [◆ ](#a7bc1dd03186b763b407a044ddffb4ab2)STM32\_SRC\_HSI

| #define STM32\_SRC\_HSI   ([STM32\_SRC\_HSE](#aa7e82706a146d0f40dc7e9755b3be9a6) + 1) |
| --- |

## [◆ ](#aa074615a92c5ff479f4fbed6fdf27f62)STM32\_SRC\_PLL1\_P

| #define STM32\_SRC\_PLL1\_P   ([STM32\_SRC\_HSI](#a7bc1dd03186b763b407a044ddffb4ab2) + 1) |
| --- |

PLL outputs.

## [◆ ](#ae568673a4eca1b42afc59faabb5810ac)STM32\_SRC\_PLL2\_P

| #define STM32\_SRC\_PLL2\_P   ([STM32\_SRC\_PLL1\_P](#aa074615a92c5ff479f4fbed6fdf27f62) + 1) |
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

## [◆ ](#a614e65076b0724a4b9a90a9761df7012)STM32\_SRC\_PLL4\_P

| #define STM32\_SRC\_PLL4\_P   ([STM32\_SRC\_PLL3\_R](#a604c22ff137a35cd1725b70991696f9a) + 1) |
| --- |

## [◆ ](#a4939e61101ce0b4e4c481cce256963f4)STM32\_SRC\_PLL4\_Q

| #define STM32\_SRC\_PLL4\_Q   ([STM32\_SRC\_PLL4\_P](#a614e65076b0724a4b9a90a9761df7012) + 1) |
| --- |

## [◆ ](#aa4e74a6cd263af35031984b3bd42aa0d)STM32\_SRC\_PLL4\_R

| #define STM32\_SRC\_PLL4\_R   ([STM32\_SRC\_PLL4\_Q](#a4939e61101ce0b4e4c481cce256963f4) + 1) |
| --- |

## [◆ ](#aa8eb2eef02227733c7c0961e4561f965)UART12CKSELR\_REG

| #define UART12CKSELR\_REG   0x614 |
| --- |

## [◆ ](#ac6a3ae8d4166fa44f582f4f16e53db50)UART1\_SEL

| #define UART1\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [UART12CKSELR\_REG](#aa8eb2eef02227733c7c0961e4561f965))

[UART12CKSELR\_REG](#aa8eb2eef02227733c7c0961e4561f965)

#define UART12CKSELR\_REG

**Definition** stm32mp13\_clock.h:53

## [◆ ](#a8d63eb1134e04f1785e24f119b474d91)UART2\_SEL

| #define UART2\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 3, [UART12CKSELR\_REG](#aa8eb2eef02227733c7c0961e4561f965))

## [◆ ](#a68421d716894d77ca963a15ccc9d162c)UART35\_SEL

| #define UART35\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [UART35CKSELR\_REG](#a3f8eee67e3fa900605d15dde78b8f357))

[UART35CKSELR\_REG](#a3f8eee67e3fa900605d15dde78b8f357)

#define UART35CKSELR\_REG

**Definition** stm32mp13\_clock.h:54

## [◆ ](#a3f8eee67e3fa900605d15dde78b8f357)UART35CKSELR\_REG

| #define UART35CKSELR\_REG   0x618 |
| --- |

## [◆ ](#a091d597b4979c49951f880bc6ccb4d71)UART4\_SEL

| #define UART4\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [UART4CKSELR\_REG](#ae7ab8abfbe4879ee20fce191d0c17611))

[UART4CKSELR\_REG](#ae7ab8abfbe4879ee20fce191d0c17611)

#define UART4CKSELR\_REG

**Definition** stm32mp13\_clock.h:55

## [◆ ](#ae7ab8abfbe4879ee20fce191d0c17611)UART4CKSELR\_REG

| #define UART4CKSELR\_REG   0x61c |
| --- |

## [◆ ](#ab1e6024b64a1715165a2ca7c78bb595e)UART6\_SEL

| #define UART6\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [UART6CKSELR\_REG](#a769e1f639865d81e2b4bb9be3ab8cc0b))

[UART6CKSELR\_REG](#a769e1f639865d81e2b4bb9be3ab8cc0b)

#define UART6CKSELR\_REG

**Definition** stm32mp13\_clock.h:56

## [◆ ](#a769e1f639865d81e2b4bb9be3ab8cc0b)UART6CKSELR\_REG

| #define UART6CKSELR\_REG   0x620 |
| --- |

## [◆ ](#a6c82e4677e11f3cb61af1c092b786233)UART78\_SEL

| #define UART78\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x7, 0, [UART78CKSELR\_REG](#a729992dea3365b21bc53cdf3ea5e2fa6))

[UART78CKSELR\_REG](#a729992dea3365b21bc53cdf3ea5e2fa6)

#define UART78CKSELR\_REG

**Definition** stm32mp13\_clock.h:57

## [◆ ](#a729992dea3365b21bc53cdf3ea5e2fa6)UART78CKSELR\_REG

| #define UART78CKSELR\_REG   0x624 |
| --- |

## [◆ ](#ae42a4c180140e1b6b87ff3a2fb666955)USBCKSELR\_REG

| #define USBCKSELR\_REG   0x650 |
| --- |

## [◆ ](#a2d691cea81bfb356af592ccedafc62ef)USBOTG\_SEL

| #define USBOTG\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x1, 4, [USBCKSELR\_REG](#ae42a4c180140e1b6b87ff3a2fb666955))

[USBCKSELR\_REG](#ae42a4c180140e1b6b87ff3a2fb666955)

#define USBCKSELR\_REG

**Definition** stm32mp13\_clock.h:68

## [◆ ](#a84d56b16e3adca6411bc9daabb32a31b)USBPHY\_SEL

| #define USBPHY\_SEL | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STM32\_DT\_CLOCK\_SELECT](stm32__common__clocks_8h.md#af00e387856ff4e47b7b7d47ab2f61c8d)((val), 0x3, 0, [USBCKSELR\_REG](#ae42a4c180140e1b6b87ff3a2fb666955))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32mp13\_clock.h](stm32mp13__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
