---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp32s3__clock_8h.html
original_path: doxygen/html/esp32s3__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s3\_clock.h File Reference

[Go to the source code of this file.](esp32s3__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_CPU\_CLK\_SRC\_XTAL](#a44ee3670c3168dd0ffbc79a563a7f074)   0U |
| #define | [ESP32\_CPU\_CLK\_SRC\_PLL](#a7a723b6353a23b55ef44d720297fe26f)   1U |
| #define | [ESP32\_CLK\_SRC\_RC\_FAST](#a1962dad90f737a51fcc70cea1931b236)   2U |
| #define | [ESP32\_CLK\_CPU\_PLL\_80M](#a61275f95111fb2a6bdbe446c0228f877)   80000000 |
| #define | [ESP32\_CLK\_CPU\_PLL\_160M](#ad80a59287e6a2f3771fd448982be9555)   160000000 |
| #define | [ESP32\_CLK\_CPU\_PLL\_240M](#ae0cca31853cf16bf9fa85508bbf9347f)   240000000 |
| #define | [ESP32\_CLK\_CPU\_RC\_FAST\_FREQ](#ab779f427209fda571ec4d229b8ef8bfc)   17500000 |
| #define | [ESP32\_CLK\_XTAL\_32M](#aeb5c606e77a85fa858ab7af6061c7949)   32000000 |
| #define | [ESP32\_CLK\_XTAL\_40M](#a6afe38f9f9c44a1bd2e5279163523a98)   40000000 |
| #define | [ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2](#a725193bf445b7f8f2c1058a6735ca476)   0 |
| #define | [ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST](#aae48d9f1288771e11c11d6177ecf3af7)   1 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW](#ad1d90df80dee3040dbe8c968cd774443)   0 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K](#aeaccf7695cab85cd7523c6ebc21704c4)   1 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256](#aaec50946dbdaabaf2199e795a389634e)   2 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC](#aa5d6a46de7da027832aa02489c062069)   9 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ](#af5cdcfa17e680ceda2f90e375eded6e6)   136000 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ](#ab63ec0973bfb87f7f09c5614ab66deb8)   32768 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ](#a8531ee06161cae4ea8516d00825c32c8)   68359 |
| #define | [ESP32\_LEDC\_MODULE](#a60f4f5ee56d788f2161b52ebbc2aa510)   0 |
| #define | [ESP32\_UART0\_MODULE](#a9708d046fbadfb7ccbc5df3e0ae57844)   1 |
| #define | [ESP32\_UART1\_MODULE](#a480803130ef80df04527f4dd12525d48)   2 |
| #define | [ESP32\_UART2\_MODULE](#a975be76987c86a84903dcc626bdc1478)   3 |
| #define | [ESP32\_USB\_MODULE](#afcf8170a750f4dc35326010b52f4e082)   4 |
| #define | [ESP32\_I2C0\_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)   5 |
| #define | [ESP32\_I2C1\_MODULE](#a5068c510487e0ce3002e4bf7082601cd)   6 |
| #define | [ESP32\_I2S0\_MODULE](#a21c262b775f6d533621d4ba8e8d6c9aa)   7 |
| #define | [ESP32\_I2S1\_MODULE](#a1cc05bfada949af9e9265abaadb1b6bc)   8 |
| #define | [ESP32\_LCD\_CAM\_MODULE](#af001f35d3c109955b027a97f7b676edd)   9 |
| #define | [ESP32\_TIMG0\_MODULE](#a88ae2c1bafdc6e78258ada5cbb9368f9)   10 |
| #define | [ESP32\_TIMG1\_MODULE](#a251462caa49fc6fe0ae1c8fe99a87caa)   11 |
| #define | [ESP32\_PWM0\_MODULE](#a8f939663db0f14133c2beb6dfc7dc3b7)   12 |
| #define | [ESP32\_PWM1\_MODULE](#aa5690cffa8770c3e2d0457557e52f300)   13 |
| #define | [ESP32\_PWM2\_MODULE](#a843cfd7e2a80b664b132a6ae6532410b)   14 |
| #define | [ESP32\_PWM3\_MODULE](#a1783f3089e7375ae7b55077ac80871d1)   15 |
| #define | [ESP32\_UHCI0\_MODULE](#af5ef985d4eaf1ffe565e2662493178c6)   16 |
| #define | [ESP32\_UHCI1\_MODULE](#aa2c199cff85bcf8e5a306a056e71f1f5)   17 |
| #define | [ESP32\_RMT\_MODULE](#a4a2d8ca15cd619022c02f97842d54159)   18 |
| #define | [ESP32\_PCNT\_MODULE](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)   19 |
| #define | [ESP32\_SPI\_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)   20 |
| #define | [ESP32\_SPI2\_MODULE](#a5e5283c23811e9c4f30980f1d865773b)   21 |
| #define | [ESP32\_SPI3\_MODULE](#aaaa2f3fbdc6e647799666e1885d4b4ff)   22 |
| #define | [ESP32\_SDMMC\_MODULE](#a72052a75b3541623f59063260c4dbc32)   23 |
| #define | [ESP32\_TWAI\_MODULE](#aba65cf1082c8422cc1e91c710bb702cc)   24 |
| #define | [ESP32\_RNG\_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)   25 |
| #define | [ESP32\_WIFI\_MODULE](#a4013c1fc7538bf46d5c1771f837a8b21)   26 |
| #define | [ESP32\_BT\_MODULE](#ad180ebcea5567ce6c3145998f3761584)   27 |
| #define | [ESP32\_WIFI\_BT\_COMMON\_MODULE](#aba1295479849f8b4dc44245e330e3020)   28 |
| #define | [ESP32\_BT\_BASEBAND\_MODULE](#a653e6d1f91c532b3ba313be27a97c2af)   29 |
| #define | [ESP32\_BT\_LC\_MODULE](#a8e27f45346390d8909f9424f13280b76)   30 |
| #define | [ESP32\_AES\_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)   31 |
| #define | [ESP32\_SHA\_MODULE](#a683dd8814bf170018b63b57268c0fde9)   32 |
| #define | [ESP32\_HMAC\_MODULE](#ae17c59442b576d1b9aade6019850e6f8)   33 |
| #define | [ESP32\_DS\_MODULE](#aaea0a7a0e789019e4ddfd38365e83688)   34 |
| #define | [ESP32\_RSA\_MODULE](#a5261565b59c0a5b75794014b80692b33)   35 |
| #define | [ESP32\_SYSTIMER\_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)   36 |
| #define | [ESP32\_GDMA\_MODULE](#a701fec66fac239e66a19389ea153ff75)   37 |
| #define | [ESP32\_DEDIC\_GPIO\_MODULE](#abbb147eb71a9d6e655ed68d2d7478a84)   38 |
| #define | [ESP32\_SARADC\_MODULE](#abe244da38fbe794e93094feef9b188fe)   39 |
| #define | [ESP32\_MODULE\_MAX](#ac380a7ff843ee465763a355cb01ef295)   40 |

## Macro Definition Documentation

## [◆ ](#a290ac6ab6c5de2e8d84a911e389e1cfc)ESP32\_AES\_MODULE

| #define ESP32\_AES\_MODULE   31 |
| --- |

## [◆ ](#a653e6d1f91c532b3ba313be27a97c2af)ESP32\_BT\_BASEBAND\_MODULE

| #define ESP32\_BT\_BASEBAND\_MODULE   29 |
| --- |

## [◆ ](#a8e27f45346390d8909f9424f13280b76)ESP32\_BT\_LC\_MODULE

| #define ESP32\_BT\_LC\_MODULE   30 |
| --- |

## [◆ ](#ad180ebcea5567ce6c3145998f3761584)ESP32\_BT\_MODULE

| #define ESP32\_BT\_MODULE   27 |
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

| #define ESP32\_CLK\_CPU\_RC\_FAST\_FREQ   17500000 |
| --- |

## [◆ ](#a1962dad90f737a51fcc70cea1931b236)ESP32\_CLK\_SRC\_RC\_FAST

| #define ESP32\_CLK\_SRC\_RC\_FAST   2U |
| --- |

## [◆ ](#aeb5c606e77a85fa858ab7af6061c7949)ESP32\_CLK\_XTAL\_32M

| #define ESP32\_CLK\_XTAL\_32M   32000000 |
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

## [◆ ](#abbb147eb71a9d6e655ed68d2d7478a84)ESP32\_DEDIC\_GPIO\_MODULE

| #define ESP32\_DEDIC\_GPIO\_MODULE   38 |
| --- |

## [◆ ](#aaea0a7a0e789019e4ddfd38365e83688)ESP32\_DS\_MODULE

| #define ESP32\_DS\_MODULE   34 |
| --- |

## [◆ ](#a701fec66fac239e66a19389ea153ff75)ESP32\_GDMA\_MODULE

| #define ESP32\_GDMA\_MODULE   37 |
| --- |

## [◆ ](#ae17c59442b576d1b9aade6019850e6f8)ESP32\_HMAC\_MODULE

| #define ESP32\_HMAC\_MODULE   33 |
| --- |

## [◆ ](#a7331ffa2ec41896d05f1f86c4d30f758)ESP32\_I2C0\_MODULE

| #define ESP32\_I2C0\_MODULE   5 |
| --- |

## [◆ ](#a5068c510487e0ce3002e4bf7082601cd)ESP32\_I2C1\_MODULE

| #define ESP32\_I2C1\_MODULE   6 |
| --- |

## [◆ ](#a21c262b775f6d533621d4ba8e8d6c9aa)ESP32\_I2S0\_MODULE

| #define ESP32\_I2S0\_MODULE   7 |
| --- |

## [◆ ](#a1cc05bfada949af9e9265abaadb1b6bc)ESP32\_I2S1\_MODULE

| #define ESP32\_I2S1\_MODULE   8 |
| --- |

## [◆ ](#af001f35d3c109955b027a97f7b676edd)ESP32\_LCD\_CAM\_MODULE

| #define ESP32\_LCD\_CAM\_MODULE   9 |
| --- |

## [◆ ](#a60f4f5ee56d788f2161b52ebbc2aa510)ESP32\_LEDC\_MODULE

| #define ESP32\_LEDC\_MODULE   0 |
| --- |

## [◆ ](#ac380a7ff843ee465763a355cb01ef295)ESP32\_MODULE\_MAX

| #define ESP32\_MODULE\_MAX   40 |
| --- |

## [◆ ](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)ESP32\_PCNT\_MODULE

| #define ESP32\_PCNT\_MODULE   19 |
| --- |

## [◆ ](#a8f939663db0f14133c2beb6dfc7dc3b7)ESP32\_PWM0\_MODULE

| #define ESP32\_PWM0\_MODULE   12 |
| --- |

## [◆ ](#aa5690cffa8770c3e2d0457557e52f300)ESP32\_PWM1\_MODULE

| #define ESP32\_PWM1\_MODULE   13 |
| --- |

## [◆ ](#a843cfd7e2a80b664b132a6ae6532410b)ESP32\_PWM2\_MODULE

| #define ESP32\_PWM2\_MODULE   14 |
| --- |

## [◆ ](#a1783f3089e7375ae7b55077ac80871d1)ESP32\_PWM3\_MODULE

| #define ESP32\_PWM3\_MODULE   15 |
| --- |

## [◆ ](#a4a2d8ca15cd619022c02f97842d54159)ESP32\_RMT\_MODULE

| #define ESP32\_RMT\_MODULE   18 |
| --- |

## [◆ ](#ad5423ca02819aab6b3fe63c11b3cf998)ESP32\_RNG\_MODULE

| #define ESP32\_RNG\_MODULE   25 |
| --- |

## [◆ ](#a5261565b59c0a5b75794014b80692b33)ESP32\_RSA\_MODULE

| #define ESP32\_RSA\_MODULE   35 |
| --- |

## [◆ ](#aae48d9f1288771e11c11d6177ecf3af7)ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST

| #define ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST   1 |
| --- |

## [◆ ](#a725193bf445b7f8f2c1058a6735ca476)ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2

| #define ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2   0 |
| --- |

## [◆ ](#aa5d6a46de7da027832aa02489c062069)ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC

| #define ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC   9 |
| --- |

## [◆ ](#aaec50946dbdaabaf2199e795a389634e)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256   2 |
| --- |

## [◆ ](#a8531ee06161cae4ea8516d00825c32c8)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ   68359 |
| --- |

## [◆ ](#ad1d90df80dee3040dbe8c968cd774443)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW   0 |
| --- |

## [◆ ](#af5cdcfa17e680ceda2f90e375eded6e6)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ   136000 |
| --- |

## [◆ ](#aeaccf7695cab85cd7523c6ebc21704c4)ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K   1 |
| --- |

## [◆ ](#ab63ec0973bfb87f7f09c5614ab66deb8)ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ   32768 |
| --- |

## [◆ ](#abe244da38fbe794e93094feef9b188fe)ESP32\_SARADC\_MODULE

| #define ESP32\_SARADC\_MODULE   39 |
| --- |

## [◆ ](#a72052a75b3541623f59063260c4dbc32)ESP32\_SDMMC\_MODULE

| #define ESP32\_SDMMC\_MODULE   23 |
| --- |

## [◆ ](#a683dd8814bf170018b63b57268c0fde9)ESP32\_SHA\_MODULE

| #define ESP32\_SHA\_MODULE   32 |
| --- |

## [◆ ](#a5e5283c23811e9c4f30980f1d865773b)ESP32\_SPI2\_MODULE

| #define ESP32\_SPI2\_MODULE   21 |
| --- |

## [◆ ](#aaaa2f3fbdc6e647799666e1885d4b4ff)ESP32\_SPI3\_MODULE

| #define ESP32\_SPI3\_MODULE   22 |
| --- |

## [◆ ](#a5652d0e2b1fc766dde13b84294d4576b)ESP32\_SPI\_MODULE

| #define ESP32\_SPI\_MODULE   20 |
| --- |

## [◆ ](#aaf8e1de1e86906ba539863b9009ebe37)ESP32\_SYSTIMER\_MODULE

| #define ESP32\_SYSTIMER\_MODULE   36 |
| --- |

## [◆ ](#a88ae2c1bafdc6e78258ada5cbb9368f9)ESP32\_TIMG0\_MODULE

| #define ESP32\_TIMG0\_MODULE   10 |
| --- |

## [◆ ](#a251462caa49fc6fe0ae1c8fe99a87caa)ESP32\_TIMG1\_MODULE

| #define ESP32\_TIMG1\_MODULE   11 |
| --- |

## [◆ ](#aba65cf1082c8422cc1e91c710bb702cc)ESP32\_TWAI\_MODULE

| #define ESP32\_TWAI\_MODULE   24 |
| --- |

## [◆ ](#a9708d046fbadfb7ccbc5df3e0ae57844)ESP32\_UART0\_MODULE

| #define ESP32\_UART0\_MODULE   1 |
| --- |

## [◆ ](#a480803130ef80df04527f4dd12525d48)ESP32\_UART1\_MODULE

| #define ESP32\_UART1\_MODULE   2 |
| --- |

## [◆ ](#a975be76987c86a84903dcc626bdc1478)ESP32\_UART2\_MODULE

| #define ESP32\_UART2\_MODULE   3 |
| --- |

## [◆ ](#af5ef985d4eaf1ffe565e2662493178c6)ESP32\_UHCI0\_MODULE

| #define ESP32\_UHCI0\_MODULE   16 |
| --- |

## [◆ ](#aa2c199cff85bcf8e5a306a056e71f1f5)ESP32\_UHCI1\_MODULE

| #define ESP32\_UHCI1\_MODULE   17 |
| --- |

## [◆ ](#afcf8170a750f4dc35326010b52f4e082)ESP32\_USB\_MODULE

| #define ESP32\_USB\_MODULE   4 |
| --- |

## [◆ ](#aba1295479849f8b4dc44245e330e3020)ESP32\_WIFI\_BT\_COMMON\_MODULE

| #define ESP32\_WIFI\_BT\_COMMON\_MODULE   28 |
| --- |

## [◆ ](#a4013c1fc7538bf46d5c1771f837a8b21)ESP32\_WIFI\_MODULE

| #define ESP32\_WIFI\_MODULE   26 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32s3\_clock.h](esp32s3__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
