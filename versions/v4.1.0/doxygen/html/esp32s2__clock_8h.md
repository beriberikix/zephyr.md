---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp32s2__clock_8h.html
original_path: doxygen/html/esp32s2__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s2\_clock.h File Reference

[Go to the source code of this file.](esp32s2__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_CPU\_CLK\_SRC\_XTAL](#a44ee3670c3168dd0ffbc79a563a7f074)   0U |
| #define | [ESP32\_CPU\_CLK\_SRC\_PLL](#a7a723b6353a23b55ef44d720297fe26f)   1U |
| #define | [ESP32\_CLK\_SRC\_RC\_FAST](#a1962dad90f737a51fcc70cea1931b236)   2U |
| #define | [ESP32\_CLK\_SRC\_APLL\_CLK](#ab5e4881ee7bff8e6fa001714f95a806d)   3U |
| #define | [ESP32\_CLK\_CPU\_PLL\_80M](#a61275f95111fb2a6bdbe446c0228f877)   80000000 |
| #define | [ESP32\_CLK\_CPU\_PLL\_160M](#ad80a59287e6a2f3771fd448982be9555)   160000000 |
| #define | [ESP32\_CLK\_CPU\_PLL\_240M](#ae0cca31853cf16bf9fa85508bbf9347f)   240000000 |
| #define | [ESP32\_CLK\_CPU\_RC\_FAST\_FREQ](#ab779f427209fda571ec4d229b8ef8bfc)   8500000 |
| #define | [ESP32\_CLK\_XTAL\_40M](#a6afe38f9f9c44a1bd2e5279163523a98)   40000000 |
| #define | [ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D4](#a5348c66760f7e577484c46d05d549193)   0 |
| #define | [ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST](#aae48d9f1288771e11c11d6177ecf3af7)   1 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW](#ad1d90df80dee3040dbe8c968cd774443)   0 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K](#aeaccf7695cab85cd7523c6ebc21704c4)   1 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256](#aaec50946dbdaabaf2199e795a389634e)   2 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC](#aa5d6a46de7da027832aa02489c062069)   9 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ](#af5cdcfa17e680ceda2f90e375eded6e6)   90000 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ](#ab63ec0973bfb87f7f09c5614ab66deb8)   32768 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ](#a8531ee06161cae4ea8516d00825c32c8)   33203 |
| #define | [ESP32\_LEDC\_MODULE](#a60f4f5ee56d788f2161b52ebbc2aa510)   0 |
| #define | [ESP32\_UART0\_MODULE](#a9708d046fbadfb7ccbc5df3e0ae57844)   1 |
| #define | [ESP32\_UART1\_MODULE](#a480803130ef80df04527f4dd12525d48)   2 |
| #define | [ESP32\_USB\_MODULE](#afcf8170a750f4dc35326010b52f4e082)   3 |
| #define | [ESP32\_I2C0\_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)   4 |
| #define | [ESP32\_I2C1\_MODULE](#a5068c510487e0ce3002e4bf7082601cd)   5 |
| #define | [ESP32\_I2S0\_MODULE](#a21c262b775f6d533621d4ba8e8d6c9aa)   6 |
| #define | [ESP32\_TIMG0\_MODULE](#a88ae2c1bafdc6e78258ada5cbb9368f9)   7 |
| #define | [ESP32\_TIMG1\_MODULE](#a251462caa49fc6fe0ae1c8fe99a87caa)   8 |
| #define | [ESP32\_UHCI0\_MODULE](#af5ef985d4eaf1ffe565e2662493178c6)   9 |
| #define | [ESP32\_UHCI1\_MODULE](#aa2c199cff85bcf8e5a306a056e71f1f5)   10 |
| #define | [ESP32\_RMT\_MODULE](#a4a2d8ca15cd619022c02f97842d54159)   11 |
| #define | [ESP32\_PCNT\_MODULE](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)   12 |
| #define | [ESP32\_SPI\_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)   13 |
| #define | [ESP32\_FSPI\_MODULE](#abd1ec14355055113ef0e2db037664fed)   14 |
| #define | [ESP32\_HSPI\_MODULE](#af9492b3e7cf5282eff0a4ee342eac278)   15 |
| #define | [ESP32\_SPI2\_DMA\_MODULE](#a196ac4b4192907882a85cf00f4b7b265)   16 |
| #define | [ESP32\_SPI3\_DMA\_MODULE](#a47b6ec180d6d07b21ffa9174fb6c9632)   17 |
| #define | [ESP32\_TWAI\_MODULE](#aba65cf1082c8422cc1e91c710bb702cc)   18 |
| #define | [ESP32\_RNG\_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)   19 |
| #define | [ESP32\_WIFI\_MODULE](#a4013c1fc7538bf46d5c1771f837a8b21)   20 |
| #define | [ESP32\_WIFI\_BT\_COMMON\_MODULE](#aba1295479849f8b4dc44245e330e3020)   21 |
| #define | [ESP32\_SYSTIMER\_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)   22 |
| #define | [ESP32\_AES\_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)   23 |
| #define | [ESP32\_SHA\_MODULE](#a683dd8814bf170018b63b57268c0fde9)   24 |
| #define | [ESP32\_RSA\_MODULE](#a5261565b59c0a5b75794014b80692b33)   25 |
| #define | [ESP32\_CRYPTO\_DMA\_MODULE](#a538c91c0abb6956aa1aaf4f641cd2bc6)   26 |
| #define | [ESP32\_AES\_DMA\_MODULE](#aa75a0ac88fa73935c1d7b44359e506d6)   27 |
| #define | [ESP32\_SHA\_DMA\_MODULE](#ac90b41ab8feed70d67e1d074c3bfda7b)   28 |
| #define | [ESP32\_DEDIC\_GPIO\_MODULE](#abbb147eb71a9d6e655ed68d2d7478a84)   29 |
| #define | [ESP32\_PERIPH\_SARADC\_MODULE](#a1274254ab9bfbea5a9ada1c18ebaac24)   30 |
| #define | [ESP32\_MODULE\_MAX](#ac380a7ff843ee465763a355cb01ef295)   31 |

## Macro Definition Documentation

## [◆ ](#aa75a0ac88fa73935c1d7b44359e506d6)ESP32\_AES\_DMA\_MODULE

| #define ESP32\_AES\_DMA\_MODULE   27 |
| --- |

## [◆ ](#a290ac6ab6c5de2e8d84a911e389e1cfc)ESP32\_AES\_MODULE

| #define ESP32\_AES\_MODULE   23 |
| --- |

## [◆ ](#ad80a59287e6a2f3771fd448982be9555)ESP32\_CLK\_CPU\_PLL\_160M

| #define ESP32\_CLK\_CPU\_PLL\_160M   160000000 |
| --- |

## [◆ ](#ae0cca31853cf16bf9fa85508bbf9347f)ESP32\_CLK\_CPU\_PLL\_240M

| #define ESP32\_CLK\_CPU\_PLL\_240M   240000000 |
| --- |

## [◆ ](#a61275f95111fb2a6bdbe446c0228f877)ESP32\_CLK\_CPU\_PLL\_80M

| #define ESP32\_CLK\_CPU\_PLL\_80M   80000000 |
| --- |

## [◆ ](#ab779f427209fda571ec4d229b8ef8bfc)ESP32\_CLK\_CPU\_RC\_FAST\_FREQ

| #define ESP32\_CLK\_CPU\_RC\_FAST\_FREQ   8500000 |
| --- |

## [◆ ](#ab5e4881ee7bff8e6fa001714f95a806d)ESP32\_CLK\_SRC\_APLL\_CLK

| #define ESP32\_CLK\_SRC\_APLL\_CLK   3U |
| --- |

## [◆ ](#a1962dad90f737a51fcc70cea1931b236)ESP32\_CLK\_SRC\_RC\_FAST

| #define ESP32\_CLK\_SRC\_RC\_FAST   2U |
| --- |

## [◆ ](#a6afe38f9f9c44a1bd2e5279163523a98)ESP32\_CLK\_XTAL\_40M

| #define ESP32\_CLK\_XTAL\_40M   40000000 |
| --- |

## [◆ ](#a7a723b6353a23b55ef44d720297fe26f)ESP32\_CPU\_CLK\_SRC\_PLL

| #define ESP32\_CPU\_CLK\_SRC\_PLL   1U |
| --- |

## [◆ ](#a44ee3670c3168dd0ffbc79a563a7f074)ESP32\_CPU\_CLK\_SRC\_XTAL

| #define ESP32\_CPU\_CLK\_SRC\_XTAL   0U |
| --- |

## [◆ ](#a538c91c0abb6956aa1aaf4f641cd2bc6)ESP32\_CRYPTO\_DMA\_MODULE

| #define ESP32\_CRYPTO\_DMA\_MODULE   26 |
| --- |

## [◆ ](#abbb147eb71a9d6e655ed68d2d7478a84)ESP32\_DEDIC\_GPIO\_MODULE

| #define ESP32\_DEDIC\_GPIO\_MODULE   29 |
| --- |

## [◆ ](#abd1ec14355055113ef0e2db037664fed)ESP32\_FSPI\_MODULE

| #define ESP32\_FSPI\_MODULE   14 |
| --- |

## [◆ ](#af9492b3e7cf5282eff0a4ee342eac278)ESP32\_HSPI\_MODULE

| #define ESP32\_HSPI\_MODULE   15 |
| --- |

## [◆ ](#a7331ffa2ec41896d05f1f86c4d30f758)ESP32\_I2C0\_MODULE

| #define ESP32\_I2C0\_MODULE   4 |
| --- |

## [◆ ](#a5068c510487e0ce3002e4bf7082601cd)ESP32\_I2C1\_MODULE

| #define ESP32\_I2C1\_MODULE   5 |
| --- |

## [◆ ](#a21c262b775f6d533621d4ba8e8d6c9aa)ESP32\_I2S0\_MODULE

| #define ESP32\_I2S0\_MODULE   6 |
| --- |

## [◆ ](#a60f4f5ee56d788f2161b52ebbc2aa510)ESP32\_LEDC\_MODULE

| #define ESP32\_LEDC\_MODULE   0 |
| --- |

## [◆ ](#ac380a7ff843ee465763a355cb01ef295)ESP32\_MODULE\_MAX

| #define ESP32\_MODULE\_MAX   31 |
| --- |

## [◆ ](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)ESP32\_PCNT\_MODULE

| #define ESP32\_PCNT\_MODULE   12 |
| --- |

## [◆ ](#a1274254ab9bfbea5a9ada1c18ebaac24)ESP32\_PERIPH\_SARADC\_MODULE

| #define ESP32\_PERIPH\_SARADC\_MODULE   30 |
| --- |

## [◆ ](#a4a2d8ca15cd619022c02f97842d54159)ESP32\_RMT\_MODULE

| #define ESP32\_RMT\_MODULE   11 |
| --- |

## [◆ ](#ad5423ca02819aab6b3fe63c11b3cf998)ESP32\_RNG\_MODULE

| #define ESP32\_RNG\_MODULE   19 |
| --- |

## [◆ ](#a5261565b59c0a5b75794014b80692b33)ESP32\_RSA\_MODULE

| #define ESP32\_RSA\_MODULE   25 |
| --- |

## [◆ ](#aae48d9f1288771e11c11d6177ecf3af7)ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST

| #define ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST   1 |
| --- |

## [◆ ](#a5348c66760f7e577484c46d05d549193)ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D4

| #define ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D4   0 |
| --- |

## [◆ ](#aa5d6a46de7da027832aa02489c062069)ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC

| #define ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC   9 |
| --- |

## [◆ ](#aaec50946dbdaabaf2199e795a389634e)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256   2 |
| --- |

## [◆ ](#a8531ee06161cae4ea8516d00825c32c8)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ   33203 |
| --- |

## [◆ ](#ad1d90df80dee3040dbe8c968cd774443)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW   0 |
| --- |

## [◆ ](#af5cdcfa17e680ceda2f90e375eded6e6)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ   90000 |
| --- |

## [◆ ](#aeaccf7695cab85cd7523c6ebc21704c4)ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K   1 |
| --- |

## [◆ ](#ab63ec0973bfb87f7f09c5614ab66deb8)ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ   32768 |
| --- |

## [◆ ](#ac90b41ab8feed70d67e1d074c3bfda7b)ESP32\_SHA\_DMA\_MODULE

| #define ESP32\_SHA\_DMA\_MODULE   28 |
| --- |

## [◆ ](#a683dd8814bf170018b63b57268c0fde9)ESP32\_SHA\_MODULE

| #define ESP32\_SHA\_MODULE   24 |
| --- |

## [◆ ](#a196ac4b4192907882a85cf00f4b7b265)ESP32\_SPI2\_DMA\_MODULE

| #define ESP32\_SPI2\_DMA\_MODULE   16 |
| --- |

## [◆ ](#a47b6ec180d6d07b21ffa9174fb6c9632)ESP32\_SPI3\_DMA\_MODULE

| #define ESP32\_SPI3\_DMA\_MODULE   17 |
| --- |

## [◆ ](#a5652d0e2b1fc766dde13b84294d4576b)ESP32\_SPI\_MODULE

| #define ESP32\_SPI\_MODULE   13 |
| --- |

## [◆ ](#aaf8e1de1e86906ba539863b9009ebe37)ESP32\_SYSTIMER\_MODULE

| #define ESP32\_SYSTIMER\_MODULE   22 |
| --- |

## [◆ ](#a88ae2c1bafdc6e78258ada5cbb9368f9)ESP32\_TIMG0\_MODULE

| #define ESP32\_TIMG0\_MODULE   7 |
| --- |

## [◆ ](#a251462caa49fc6fe0ae1c8fe99a87caa)ESP32\_TIMG1\_MODULE

| #define ESP32\_TIMG1\_MODULE   8 |
| --- |

## [◆ ](#aba65cf1082c8422cc1e91c710bb702cc)ESP32\_TWAI\_MODULE

| #define ESP32\_TWAI\_MODULE   18 |
| --- |

## [◆ ](#a9708d046fbadfb7ccbc5df3e0ae57844)ESP32\_UART0\_MODULE

| #define ESP32\_UART0\_MODULE   1 |
| --- |

## [◆ ](#a480803130ef80df04527f4dd12525d48)ESP32\_UART1\_MODULE

| #define ESP32\_UART1\_MODULE   2 |
| --- |

## [◆ ](#af5ef985d4eaf1ffe565e2662493178c6)ESP32\_UHCI0\_MODULE

| #define ESP32\_UHCI0\_MODULE   9 |
| --- |

## [◆ ](#aa2c199cff85bcf8e5a306a056e71f1f5)ESP32\_UHCI1\_MODULE

| #define ESP32\_UHCI1\_MODULE   10 |
| --- |

## [◆ ](#afcf8170a750f4dc35326010b52f4e082)ESP32\_USB\_MODULE

| #define ESP32\_USB\_MODULE   3 |
| --- |

## [◆ ](#aba1295479849f8b4dc44245e330e3020)ESP32\_WIFI\_BT\_COMMON\_MODULE

| #define ESP32\_WIFI\_BT\_COMMON\_MODULE   21 |
| --- |

## [◆ ](#a4013c1fc7538bf46d5c1771f837a8b21)ESP32\_WIFI\_MODULE

| #define ESP32\_WIFI\_MODULE   20 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32s2\_clock.h](esp32s2__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
