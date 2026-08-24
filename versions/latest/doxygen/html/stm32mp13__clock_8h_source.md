---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32mp13__clock_8h_source.html
original_path: doxygen/html/stm32mp13__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32mp13\_clock.h

[Go to the documentation of this file.](stm32mp13__clock_8h.md)

1/\*

2 \* Copyright (c) 2025 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32MP13\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32MP13\_CLOCK\_H\_

8

9#include "[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)"

10

12/\* defined in stm32\_common\_clocks.h \*/

[ 14](stm32mp13__clock_8h.md#aa7e82706a146d0f40dc7e9755b3be9a6)#define STM32\_SRC\_HSE (STM32\_SRC\_LSI + 1)

[ 15](stm32mp13__clock_8h.md#a7bc1dd03186b763b407a044ddffb4ab2)#define STM32\_SRC\_HSI (STM32\_SRC\_HSE + 1)

16

[ 18](stm32mp13__clock_8h.md#aa074615a92c5ff479f4fbed6fdf27f62)#define STM32\_SRC\_PLL1\_P (STM32\_SRC\_HSI + 1)

[ 19](stm32mp13__clock_8h.md#ae568673a4eca1b42afc59faabb5810ac)#define STM32\_SRC\_PLL2\_P (STM32\_SRC\_PLL1\_P + 1)

[ 20](stm32mp13__clock_8h.md#aaf0a956dda42c2a031cabce49dd3e717)#define STM32\_SRC\_PLL2\_Q (STM32\_SRC\_PLL2\_P + 1)

[ 21](stm32mp13__clock_8h.md#a57af8944eefa865aa75b6286c13a53cd)#define STM32\_SRC\_PLL2\_R (STM32\_SRC\_PLL2\_Q + 1)

[ 22](stm32mp13__clock_8h.md#a17c753e0bb8547ea9452f48a65a0a206)#define STM32\_SRC\_PLL3\_P (STM32\_SRC\_PLL2\_R + 1)

[ 23](stm32mp13__clock_8h.md#a9a31a3adebff6a1eee31c287673412c9)#define STM32\_SRC\_PLL3\_Q (STM32\_SRC\_PLL3\_P + 1)

[ 24](stm32mp13__clock_8h.md#a604c22ff137a35cd1725b70991696f9a)#define STM32\_SRC\_PLL3\_R (STM32\_SRC\_PLL3\_Q + 1)

[ 25](stm32mp13__clock_8h.md#a614e65076b0724a4b9a90a9761df7012)#define STM32\_SRC\_PLL4\_P (STM32\_SRC\_PLL3\_R + 1)

[ 26](stm32mp13__clock_8h.md#a4939e61101ce0b4e4c481cce256963f4)#define STM32\_SRC\_PLL4\_Q (STM32\_SRC\_PLL4\_P + 1)

[ 27](stm32mp13__clock_8h.md#aa4e74a6cd263af35031984b3bd42aa0d)#define STM32\_SRC\_PLL4\_R (STM32\_SRC\_PLL4\_Q + 1)

28

[ 30](stm32mp13__clock_8h.md#ac763945fc36124f9c978c423826faa95)#define STM32\_CLOCK\_BUS\_APB1 0x700

[ 31](stm32mp13__clock_8h.md#adb7becb609763568b91303041c9cd4db)#define STM32\_CLOCK\_BUS\_APB2 0x708

[ 32](stm32mp13__clock_8h.md#af7165e22b71d1beaf0dd4f59d5b4db6d)#define STM32\_CLOCK\_BUS\_APB3 0x710

[ 33](stm32mp13__clock_8h.md#a537105e6125ce3b95a2d69435f47dd51)#define STM32\_CLOCK\_BUS\_APB4 0x728

[ 34](stm32mp13__clock_8h.md#ae152597ed9e57e1067dd16994d62fb0a)#define STM32\_CLOCK\_BUS\_APB4\_NS 0x738

[ 35](stm32mp13__clock_8h.md#a02ec780a692439efebf0bf8181bf7803)#define STM32\_CLOCK\_BUS\_APB5 0x740

[ 36](stm32mp13__clock_8h.md#a55ecb827ff96585f31fa9fc3d1535822)#define STM32\_CLOCK\_BUS\_APB6 0x748

[ 37](stm32mp13__clock_8h.md#a5e58ef1846c185b04bed598b26ee9205)#define STM32\_CLOCK\_BUS\_AHB2 0x750

[ 38](stm32mp13__clock_8h.md#a49bccabc3065f192086f16929a7b762d)#define STM32\_CLOCK\_BUS\_AHB4 0x768

[ 39](stm32mp13__clock_8h.md#a623a8ba4dc47622dfbf76801f1582f58)#define STM32\_CLOCK\_BUS\_AHB5 0x778

[ 40](stm32mp13__clock_8h.md#a19119341d73264f1f9f18f3fe64f7bd1)#define STM32\_CLOCK\_BUS\_AHB6 0x780

41

[ 42](stm32mp13__clock_8h.md#acc0577552371fcda95685f6424ecb4b2)#define STM32\_PERIPH\_BUS\_MIN STM32\_CLOCK\_BUS\_APB1

[ 43](stm32mp13__clock_8h.md#a561265772438ab8995251760c7f3dc30)#define STM32\_PERIPH\_BUS\_MAX STM32\_CLOCK\_BUS\_AHB6

44

[ 46](stm32mp13__clock_8h.md#a6394a79a2e9e8b066b86c801fc728d59)#define MCO1CFGR\_REG 0x460

[ 47](stm32mp13__clock_8h.md#aa24514646b50cd8b0dc9ed0773e5f82d)#define MCO2CFGR\_REG 0x464

[ 48](stm32mp13__clock_8h.md#a33a4edf33375910dce464a5a66643d52)#define I2C12CKSELR\_REG 0x600

[ 49](stm32mp13__clock_8h.md#a36dacdc312d713a66aebc2a2dbd568ae)#define I2C345CKSELR\_REG 0x604

[ 50](stm32mp13__clock_8h.md#a100ef3300f3e05ec061477fc686ae998)#define SPI2S1CKSELR\_REG 0x608

[ 51](stm32mp13__clock_8h.md#a16d5d1e10cd09338e1dc841b81c28229)#define SPI2S23CKSELR\_REG 0x60c

[ 52](stm32mp13__clock_8h.md#aff103be77a79465724670d76af7c9c4e)#define SPI45CKSELR\_REG 0x610

[ 53](stm32mp13__clock_8h.md#aa8eb2eef02227733c7c0961e4561f965)#define UART12CKSELR\_REG 0x614

[ 54](stm32mp13__clock_8h.md#a3f8eee67e3fa900605d15dde78b8f357)#define UART35CKSELR\_REG 0x618

[ 55](stm32mp13__clock_8h.md#ae7ab8abfbe4879ee20fce191d0c17611)#define UART4CKSELR\_REG 0x61c

[ 56](stm32mp13__clock_8h.md#a769e1f639865d81e2b4bb9be3ab8cc0b)#define UART6CKSELR\_REG 0x620

[ 57](stm32mp13__clock_8h.md#a729992dea3365b21bc53cdf3ea5e2fa6)#define UART78CKSELR\_REG 0x624

[ 58](stm32mp13__clock_8h.md#aa173ef84dcba8fe29452c21cdb7e7d75)#define LPTIM1CKSELR\_REG 0x628

[ 59](stm32mp13__clock_8h.md#a884ca27b18f8dc3f1a04891170d564c7)#define LPTIM23CKSELR\_REG 0x62c

[ 60](stm32mp13__clock_8h.md#a5806e02253853ba1156a1a4c69ea49d3)#define LPTIM45CKSELR\_REG 0x630

[ 61](stm32mp13__clock_8h.md#a12d0eb312c74a9127853994b3daa7418)#define SAI1CKSELR\_REG 0x634

[ 62](stm32mp13__clock_8h.md#abb4307131a38e26886cd9f27af4ddfe1)#define SAI2CKSELR\_REG 0x638

[ 63](stm32mp13__clock_8h.md#a971421a8deec5635012305b26ef563ec)#define FDCANCKSELR\_REG 0x63c

[ 64](stm32mp13__clock_8h.md#a1e0da281a34b9257e8d9dd0b81d7fafd)#define SPDIFCKSELR\_REG 0x640

[ 65](stm32mp13__clock_8h.md#aa783dacddb5a6116d7b10dc5f858a02c)#define ADC12CKSELR\_REG 0x644

[ 66](stm32mp13__clock_8h.md#a778eac4d709f73d443089c52f0085c65)#define SDMMC12CKSELR\_REG 0x648

[ 67](stm32mp13__clock_8h.md#a921b805671555768481672596d54d5a0)#define ETH12CKSELR\_REG 0x64c

[ 68](stm32mp13__clock_8h.md#ae42a4c180140e1b6b87ff3a2fb666955)#define USBCKSELR\_REG 0x650

[ 69](stm32mp13__clock_8h.md#a774ea01b7d6909ec3629cbe73a1e75de)#define QSPICKSELR\_REG 0x654

[ 70](stm32mp13__clock_8h.md#aab13b7fbac5eb80767b83e4bf8c09fd9)#define FMCCKSELR\_REG 0x658

[ 71](stm32mp13__clock_8h.md#ade77c5f1a8d268bcddf37e6e8e94d02c)#define RNG1CKSELR\_REG 0x65c

[ 72](stm32mp13__clock_8h.md#a5d1600ae93964d82568442decaf7eb72)#define STGENCKSELR\_REG 0x660

[ 73](stm32mp13__clock_8h.md#a1f817073a47e6bfb9bcaab295c5a9b4e)#define DCMIPPCKSELR\_REG 0x664

[ 74](stm32mp13__clock_8h.md#aeb686993b410efe3ce5a68a3ac43657f)#define SAESCKSELR\_REG 0x668

75

[ 77](stm32mp13__clock_8h.md#acc5c7aed4e842ca212471d7a58504821)#define MCO1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, MCO1CFGR\_REG)

[ 78](stm32mp13__clock_8h.md#a2805cf7e0b5ed0a9bb4bfff863327081)#define MCO1\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0xf, 4, MCO1CFGR\_REG)

[ 79](stm32mp13__clock_8h.md#ab5fc05cb6aa1154c54c29b95f3154a75)#define MCO2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, MCO2CFGR\_REG)

[ 80](stm32mp13__clock_8h.md#ab02a0ccbb8588979ca4742c72c59589f)#define MCO2\_PRE(val) STM32\_DT\_CLOCK\_SELECT((val), 0xf, 4, MCO2CFGR\_REG)

81

[ 82](stm32mp13__clock_8h.md#ac41d16cf96d9a7495857b70211abc1e1)#define MCOX\_ON BIT(12)

83

84/\* MCO1 source \*/

[ 85](stm32mp13__clock_8h.md#a6eb144ce115b853faa29de37eb146bc7)#define MCO1\_SEL\_HSI 0

[ 86](stm32mp13__clock_8h.md#a2c84d124af72fb9a2f579a4a1df078bb)#define MCO1\_SEL\_HSE 1

[ 87](stm32mp13__clock_8h.md#a8515ec118d2560401c351ee232836ad4)#define MCO1\_SEL\_CSI 2

[ 88](stm32mp13__clock_8h.md#ad5b4da133657b2efb33699c71f636ff2)#define MCO1\_SEL\_LSI 3

[ 89](stm32mp13__clock_8h.md#af573b66b787ce18736116b4c503bc616)#define MCO1\_SEL\_LSE 4

90

91/\* MCO2 source \*/

[ 92](stm32mp13__clock_8h.md#a9704e8e10de965c55fbb5fd24c7f3578)#define MCO2\_SEL\_MPU 0

[ 93](stm32mp13__clock_8h.md#a76cf5ab48c0607ebe1325522a0a09128)#define MCO2\_SEL\_AXI 1

[ 94](stm32mp13__clock_8h.md#a0cb908baba3eea8c42c26c3b75c9ef30)#define MCO2\_SEL\_MLAHB 2

[ 95](stm32mp13__clock_8h.md#ad9461d250a0bfe95f3bd2227424a8e39)#define MCO2\_SEL\_PLL4 3

[ 96](stm32mp13__clock_8h.md#a08e910755a034001bf34746f7be51186)#define MCO2\_SEL\_HSE 4

[ 97](stm32mp13__clock_8h.md#acb06f32d3df5fd05f665f7fbaea3ffd6)#define MCO2\_SEL\_HSI 5

98

99/\* MCO prescaler : division factor \*/

[ 100](stm32mp13__clock_8h.md#aa6d6446aa7a1c84324475f6e8665fbb7)#define MCO\_PRE\_DIV\_1 0

[ 101](stm32mp13__clock_8h.md#a36db847c7932669759f64844a15c42c3)#define MCO\_PRE\_DIV\_2 1

[ 102](stm32mp13__clock_8h.md#a1d99057b6886474182adffcff4f246f2)#define MCO\_PRE\_DIV\_3 2

[ 103](stm32mp13__clock_8h.md#a74c5b485d9169c489ab19e788b43c657)#define MCO\_PRE\_DIV\_4 3

[ 104](stm32mp13__clock_8h.md#aad3773cb5fbea15e6cddf688dea3cd04)#define MCO\_PRE\_DIV\_5 4

[ 105](stm32mp13__clock_8h.md#a3cb780fda9d369607e1c51a7cddff300)#define MCO\_PRE\_DIV\_6 5

[ 106](stm32mp13__clock_8h.md#a08634986618842af08073f59c6da3e8f)#define MCO\_PRE\_DIV\_7 6

[ 107](stm32mp13__clock_8h.md#ad1bb69ff2fe6748978c31666f201947c)#define MCO\_PRE\_DIV\_8 7

[ 108](stm32mp13__clock_8h.md#a7841c7ceb21754059717c5996a081cb4)#define MCO\_PRE\_DIV\_9 8

[ 109](stm32mp13__clock_8h.md#aecc309343fad5680088593eff549748c)#define MCO\_PRE\_DIV\_10 9

[ 110](stm32mp13__clock_8h.md#a3c4b271ad0c50ec7eb9edd779c30b3d9)#define MCO\_PRE\_DIV\_11 10

[ 111](stm32mp13__clock_8h.md#aa93517f599cd367844383018b962319f)#define MCO\_PRE\_DIV\_12 11

[ 112](stm32mp13__clock_8h.md#a3fcce904cb4650ec093f4aba0a8b7a51)#define MCO\_PRE\_DIV\_13 12

[ 113](stm32mp13__clock_8h.md#aff3b9f97c2b1b70f090a7c27ca57ca58)#define MCO\_PRE\_DIV\_14 13

[ 114](stm32mp13__clock_8h.md#affa380b0a33facd4d5fdd9dc405c6ddc)#define MCO\_PRE\_DIV\_15 14

[ 115](stm32mp13__clock_8h.md#a111fd8dc5850b16b1308c8eaba8a9458)#define MCO\_PRE\_DIV\_16 15

116

[ 117](stm32mp13__clock_8h.md#abf19277267381c87be1cfe8c674b2fd3)#define I2C12\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, I2C12CKSELR\_REG)

[ 118](stm32mp13__clock_8h.md#aa12a1d2ac790880b7148d1e5660eb941)#define I2C3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, I2C345CKSELR\_REG)

[ 119](stm32mp13__clock_8h.md#a55880006ae28021de4d148924c06001e)#define I2C4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 3, I2C345CKSELR\_REG)

[ 120](stm32mp13__clock_8h.md#ab9c645c57c03d284386ba0b4fd37d11f)#define I2C5\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 6, I2C345CKSELR\_REG)

[ 121](stm32mp13__clock_8h.md#a5199102173e9dbe957230f356e14d910)#define SPI1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, SPI2S1CKSELR\_REG)

[ 122](stm32mp13__clock_8h.md#ad760ef96e4fd9ca527e7d9c746d1c9f3)#define SPI23\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, SPI2S23CKSELR\_REG)

[ 123](stm32mp13__clock_8h.md#a55086a94321a6e1af527a46c644f6c5e)#define SPI4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, SPI45CKSELR\_REG)

[ 124](stm32mp13__clock_8h.md#ac7193e508815171a4d73795d24086136)#define SPI5\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 3, SPI45CKSELR\_REG)

[ 125](stm32mp13__clock_8h.md#ac6a3ae8d4166fa44f582f4f16e53db50)#define UART1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, UART12CKSELR\_REG)

[ 126](stm32mp13__clock_8h.md#a8d63eb1134e04f1785e24f119b474d91)#define UART2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 3, UART12CKSELR\_REG)

[ 127](stm32mp13__clock_8h.md#a68421d716894d77ca963a15ccc9d162c)#define UART35\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, UART35CKSELR\_REG)

[ 128](stm32mp13__clock_8h.md#a091d597b4979c49951f880bc6ccb4d71)#define UART4\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, UART4CKSELR\_REG)

[ 129](stm32mp13__clock_8h.md#ab1e6024b64a1715165a2ca7c78bb595e)#define UART6\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, UART6CKSELR\_REG)

[ 130](stm32mp13__clock_8h.md#a6c82e4677e11f3cb61af1c092b786233)#define UART78\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, UART78CKSELR\_REG)

[ 131](stm32mp13__clock_8h.md#aaf12c6964a0787aebb10ab1e2bbc7406)#define LPTIME1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, LPTIM1CKSELR\_REG)

[ 132](stm32mp13__clock_8h.md#ace6379a6f2d2e1803abff6c0215c3c7d)#define LPTIME2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, LPTIM23CKSELR\_REG)

[ 133](stm32mp13__clock_8h.md#a43016575086a5ab614d1edaaecfbfb83)#define LPTIME3\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 3, LPTIM23CKSELR\_REG)

[ 134](stm32mp13__clock_8h.md#ae4eb19cd052b1ef0efc4b1f175048867)#define LPTIME45\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, LPTIM45CKSELR\_REG)

[ 135](stm32mp13__clock_8h.md#ab8e49f6309adb53edd9ad3d051d451db)#define SAI1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, SAI1CKSELR\_REG)

[ 136](stm32mp13__clock_8h.md#a4fb9a6b79339e822f0ae426e8bba7486)#define SAI2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, SAI2CKSELR\_REG)

[ 137](stm32mp13__clock_8h.md#ac1df6369669b4b3febd0525426e76499)#define FDCAN\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, FDCANCKSELR\_REG)

[ 138](stm32mp13__clock_8h.md#a37e4a34b034dee8d7f0b1fa1378e6ff6)#define SPDIF\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, SPDIFCKSELR\_REG)

[ 139](stm32mp13__clock_8h.md#a0751699f49808d31e15ec33f2b7d4618)#define ADC1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, ADC12CKSELR\_REG)

[ 140](stm32mp13__clock_8h.md#adeba2b1b877321bce680ae778659b5a7)#define ADC2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 2, ADC12CKSELR\_REG)

[ 141](stm32mp13__clock_8h.md#a1a4999da331afff86581c8a6cea6afe9)#define SDMMC1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 0, SDMMC12CKSELR\_REG)

[ 142](stm32mp13__clock_8h.md#a7319710d63129ad13039565cad2b4950)#define SDMMC2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x7, 3, SDMMC12CKSELR\_REG)

[ 143](stm32mp13__clock_8h.md#a4e9282866e4f40cf5d6fd0a655fa6fa1)#define ETH1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, ETH12CKSELR\_REG)

[ 144](stm32mp13__clock_8h.md#a1e424c22dd1d25c08ce3d36bce3a7c70)#define ETH2\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 8, ETH12CKSELR\_REG)

[ 145](stm32mp13__clock_8h.md#a84d56b16e3adca6411bc9daabb32a31b)#define USBPHY\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, USBCKSELR\_REG)

[ 146](stm32mp13__clock_8h.md#a2d691cea81bfb356af592ccedafc62ef)#define USBOTG\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x1, 4, USBCKSELR\_REG)

[ 147](stm32mp13__clock_8h.md#ae66e7abfb9009e737cff676fb4e5155f)#define QSPI\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, QSPICKSELR\_REG)

[ 148](stm32mp13__clock_8h.md#a0de89c03e0cd384de7f594aa5c5e82de)#define FMC\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, FMCCKSELR\_REG)

[ 149](stm32mp13__clock_8h.md#aedecc651f8bde3a11944772354691a93)#define RNG1\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, RNG1CKSELR\_REG)

[ 150](stm32mp13__clock_8h.md#aa94e7a102c493fafd093208e079062a7)#define STGEN\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, STGENCKSELR\_REG)

[ 151](stm32mp13__clock_8h.md#a5b9758e95788f06d93382daec60fdf3f)#define DCMIPP\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, DCMIPPCKSELR\_REG)

[ 152](stm32mp13__clock_8h.md#a9072e326043742dc4299de1b64a2dd9d)#define SAES\_SEL(val) STM32\_DT\_CLOCK\_SELECT((val), 0x3, 0, SAESCKSELR\_REG)

153

154#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_STM32MP13\_CLOCK\_H\_ \*/

[stm32\_common\_clocks.h](stm32__common__clocks_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [stm32mp13\_clock.h](stm32mp13__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
