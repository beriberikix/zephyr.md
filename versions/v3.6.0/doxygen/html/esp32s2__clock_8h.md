---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32s2__clock_8h.html
original_path: doxygen/html/esp32s2__clock_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s2\_clock.h File Reference

[Go to the source code of this file.](esp32s2__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_CLK\_SRC\_XTAL](#afca77320ca383abd16c3da3dd9f5475b)   0U |
| #define | [ESP32\_CLK\_SRC\_PLL](#a2b6410b41a6a9b646ed1030e8626a8f8)   1U |
| #define | [ESP32\_CLK\_SRC\_RTC8M](#a4de6bcb9ee3b5c6dfc4887528999af77)   2U |
| #define | [ESP32\_CLK\_SRC\_APLL](#a9d8f8be2dbba1b9cfc31e2188868b025)   3U |
| #define | [ESP32\_CLK\_CPU\_26M](#ada91f47dd4cd7f9ceac7fb68b2042c23)   26000000 |
| #define | [ESP32\_CLK\_CPU\_40M](#a3360cb00458b450b1517d75d2b42b6ee)   40000000 |
| #define | [ESP32\_CLK\_CPU\_80M](#a7ef1aa6b333059931611dd948b93e147)   80000000 |
| #define | [ESP32\_CLK\_CPU\_160M](#a4ce7aae7fa038527cc1892e94762ddf5)   160000000 |
| #define | [ESP32\_CLK\_CPU\_240M](#afcd84cbe162c507b9fa70d7d397e417e)   240000000 |
| #define | [ESP32\_CLK\_XTAL\_40M](#a6afe38f9f9c44a1bd2e5279163523a98)   0U |
| #define | [ESP32\_RTC\_FAST\_CLK\_FREQ\_8M](#a7545a9269b1a9db19e45913f77e93ae1)   8500000U |
| #define | [ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX](#accb6c4420081f80615e07a97606c6b62)   [ESP32\_RTC\_FAST\_CLK\_FREQ\_8M](#a7545a9269b1a9db19e45913f77e93ae1) |
| #define | [ESP32\_RTC\_SLOW\_CLK\_FREQ\_90K](#ac1907007a9016544d3a8a84b350c2f0f)   90000U |
| #define | [ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256](#a995e21929ecfb57c86d7ca1b1cf8e010)   ([ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX](#accb6c4420081f80615e07a97606c6b62) / 256) |
| #define | [ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K](#ac977efbcfd0b8665b9362b40af6657e8)   32768U |
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

## [◆ ](#a4ce7aae7fa038527cc1892e94762ddf5)ESP32\_CLK\_CPU\_160M

| #define ESP32\_CLK\_CPU\_160M   160000000 |
| --- |

## [◆ ](#afcd84cbe162c507b9fa70d7d397e417e)ESP32\_CLK\_CPU\_240M

| #define ESP32\_CLK\_CPU\_240M   240000000 |
| --- |

## [◆ ](#ada91f47dd4cd7f9ceac7fb68b2042c23)ESP32\_CLK\_CPU\_26M

| #define ESP32\_CLK\_CPU\_26M   26000000 |
| --- |

## [◆ ](#a3360cb00458b450b1517d75d2b42b6ee)ESP32\_CLK\_CPU\_40M

| #define ESP32\_CLK\_CPU\_40M   40000000 |
| --- |

## [◆ ](#a7ef1aa6b333059931611dd948b93e147)ESP32\_CLK\_CPU\_80M

| #define ESP32\_CLK\_CPU\_80M   80000000 |
| --- |

## [◆ ](#a9d8f8be2dbba1b9cfc31e2188868b025)ESP32\_CLK\_SRC\_APLL

| #define ESP32\_CLK\_SRC\_APLL   3U |
| --- |

## [◆ ](#a2b6410b41a6a9b646ed1030e8626a8f8)ESP32\_CLK\_SRC\_PLL

| #define ESP32\_CLK\_SRC\_PLL   1U |
| --- |

## [◆ ](#a4de6bcb9ee3b5c6dfc4887528999af77)ESP32\_CLK\_SRC\_RTC8M

| #define ESP32\_CLK\_SRC\_RTC8M   2U |
| --- |

## [◆ ](#afca77320ca383abd16c3da3dd9f5475b)ESP32\_CLK\_SRC\_XTAL

| #define ESP32\_CLK\_SRC\_XTAL   0U |
| --- |

## [◆ ](#a6afe38f9f9c44a1bd2e5279163523a98)ESP32\_CLK\_XTAL\_40M

| #define ESP32\_CLK\_XTAL\_40M   0U |
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

## [◆ ](#a7545a9269b1a9db19e45913f77e93ae1)ESP32\_RTC\_FAST\_CLK\_FREQ\_8M

| #define ESP32\_RTC\_FAST\_CLK\_FREQ\_8M   8500000U |
| --- |

## [◆ ](#accb6c4420081f80615e07a97606c6b62)ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX

| #define ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX   [ESP32\_RTC\_FAST\_CLK\_FREQ\_8M](#a7545a9269b1a9db19e45913f77e93ae1) |
| --- |

## [◆ ](#ac977efbcfd0b8665b9362b40af6657e8)ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K

| #define ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K   32768U |
| --- |

## [◆ ](#a995e21929ecfb57c86d7ca1b1cf8e010)ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256

| #define ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256   ([ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX](#accb6c4420081f80615e07a97606c6b62) / 256) |
| --- |

## [◆ ](#ac1907007a9016544d3a8a84b350c2f0f)ESP32\_RTC\_SLOW\_CLK\_FREQ\_90K

| #define ESP32\_RTC\_SLOW\_CLK\_FREQ\_90K   90000U |
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
