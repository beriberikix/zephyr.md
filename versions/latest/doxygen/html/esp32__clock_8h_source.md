---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32__clock_8h_source.html
original_path: doxygen/html/esp32__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32\_clock.h

[Go to the documentation of this file.](esp32__clock_8h.md)

1/\*

2 \* Copyright (c) 2020 Mohamed ElShahawi

3 \* Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32\_H\_

10

11/\* System Clock Source \*/

[ 12](esp32__clock_8h.md#afca77320ca383abd16c3da3dd9f5475b)#define ESP32\_CLK\_SRC\_XTAL 0U

[ 13](esp32__clock_8h.md#a2b6410b41a6a9b646ed1030e8626a8f8)#define ESP32\_CLK\_SRC\_PLL 1U

[ 14](esp32__clock_8h.md#a4de6bcb9ee3b5c6dfc4887528999af77)#define ESP32\_CLK\_SRC\_RTC8M 2U

[ 15](esp32__clock_8h.md#a9d8f8be2dbba1b9cfc31e2188868b025)#define ESP32\_CLK\_SRC\_APLL 3U

16

17/\* Supported CPU Frequencies \*/

[ 18](esp32__clock_8h.md#ada91f47dd4cd7f9ceac7fb68b2042c23)#define ESP32\_CLK\_CPU\_26M 26000000

[ 19](esp32__clock_8h.md#a3360cb00458b450b1517d75d2b42b6ee)#define ESP32\_CLK\_CPU\_40M 40000000

[ 20](esp32__clock_8h.md#a7ef1aa6b333059931611dd948b93e147)#define ESP32\_CLK\_CPU\_80M 80000000

[ 21](esp32__clock_8h.md#a4ce7aae7fa038527cc1892e94762ddf5)#define ESP32\_CLK\_CPU\_160M 160000000

[ 22](esp32__clock_8h.md#afcd84cbe162c507b9fa70d7d397e417e)#define ESP32\_CLK\_CPU\_240M 240000000

23

24/\* Supported XTAL Frequencies \*/

[ 25](esp32__clock_8h.md#a85c15a3031e661eb41db77782e231316)#define ESP32\_CLK\_XTAL\_24M 0U

[ 26](esp32__clock_8h.md#a06efe791ed749209eb07de5066c6eddc)#define ESP32\_CLK\_XTAL\_26M 1U

[ 27](esp32__clock_8h.md#a6afe38f9f9c44a1bd2e5279163523a98)#define ESP32\_CLK\_XTAL\_40M 2U

[ 28](esp32__clock_8h.md#a223c87d4b1b57de1ec28fdc0a69ece81)#define ESP32\_CLK\_XTAL\_AUTO 3U

29

30/\* Supported RTC fast clock frequencies \*/

[ 31](esp32__clock_8h.md#a7545a9269b1a9db19e45913f77e93ae1)#define ESP32\_RTC\_FAST\_CLK\_FREQ\_8M 8500000U

32

33/\* Supported RTC slow clock frequencies \*/

[ 34](esp32__clock_8h.md#a6e4d2f91c11d9fe33ad38bd431408e53)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_150K 150000U

[ 35](esp32__clock_8h.md#ac977efbcfd0b8665b9362b40af6657e8)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K 32000U

[ 36](esp32__clock_8h.md#a995e21929ecfb57c86d7ca1b1cf8e010)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256 (ESP32\_RTC\_FAST\_CLK\_FREQ\_8M / 256)

37

38/\* Modules IDs

39 \* These IDs are actually offsets in CLK and RST Control registers.

40 \* These IDs shouldn't be changed unless there is a Hardware change

41 \* from Espressif.

42 \*

43 \* Basic Modules

44 \* Registers: DPORT\_PERIP\_CLK\_EN\_REG, DPORT\_PERIP\_RST\_EN\_REG

45 \*/

[ 46](esp32__clock_8h.md#a60f4f5ee56d788f2161b52ebbc2aa510)#define ESP32\_LEDC\_MODULE 0

[ 47](esp32__clock_8h.md#a9708d046fbadfb7ccbc5df3e0ae57844)#define ESP32\_UART0\_MODULE 1

[ 48](esp32__clock_8h.md#a480803130ef80df04527f4dd12525d48)#define ESP32\_UART1\_MODULE 2

[ 49](esp32__clock_8h.md#a975be76987c86a84903dcc626bdc1478)#define ESP32\_UART2\_MODULE 3

[ 50](esp32__clock_8h.md#a7331ffa2ec41896d05f1f86c4d30f758)#define ESP32\_I2C0\_MODULE 4

[ 51](esp32__clock_8h.md#a5068c510487e0ce3002e4bf7082601cd)#define ESP32\_I2C1\_MODULE 5

[ 52](esp32__clock_8h.md#a21c262b775f6d533621d4ba8e8d6c9aa)#define ESP32\_I2S0\_MODULE 6

[ 53](esp32__clock_8h.md#a1cc05bfada949af9e9265abaadb1b6bc)#define ESP32\_I2S1\_MODULE 7

[ 54](esp32__clock_8h.md#a88ae2c1bafdc6e78258ada5cbb9368f9)#define ESP32\_TIMG0\_MODULE 8

[ 55](esp32__clock_8h.md#a251462caa49fc6fe0ae1c8fe99a87caa)#define ESP32\_TIMG1\_MODULE 9

[ 56](esp32__clock_8h.md#a8f939663db0f14133c2beb6dfc7dc3b7)#define ESP32\_PWM0\_MODULE 10

[ 57](esp32__clock_8h.md#aa5690cffa8770c3e2d0457557e52f300)#define ESP32\_PWM1\_MODULE 11

[ 58](esp32__clock_8h.md#af5ef985d4eaf1ffe565e2662493178c6)#define ESP32\_UHCI0\_MODULE 12

[ 59](esp32__clock_8h.md#aa2c199cff85bcf8e5a306a056e71f1f5)#define ESP32\_UHCI1\_MODULE 13

[ 60](esp32__clock_8h.md#a4a2d8ca15cd619022c02f97842d54159)#define ESP32\_RMT\_MODULE 14

[ 61](esp32__clock_8h.md#ac0d8fb4397baaac7ff45dee8f4e1cb7c)#define ESP32\_PCNT\_MODULE 15

[ 62](esp32__clock_8h.md#a5652d0e2b1fc766dde13b84294d4576b)#define ESP32\_SPI\_MODULE 16

[ 63](esp32__clock_8h.md#af9492b3e7cf5282eff0a4ee342eac278)#define ESP32\_HSPI\_MODULE 17

[ 64](esp32__clock_8h.md#a982e8ce4deccacd4d020cdfed8771cac)#define ESP32\_VSPI\_MODULE 18

[ 65](esp32__clock_8h.md#ac44ad6537fde43047aa04ba8ee35586e)#define ESP32\_SPI\_DMA\_MODULE 19

[ 66](esp32__clock_8h.md#a72052a75b3541623f59063260c4dbc32)#define ESP32\_SDMMC\_MODULE 20

[ 67](esp32__clock_8h.md#a83b43d5f4d6373a5bb437de5ee5c091f)#define ESP32\_SDIO\_SLAVE\_MODULE 21

[ 68](esp32__clock_8h.md#aba65cf1082c8422cc1e91c710bb702cc)#define ESP32\_TWAI\_MODULE 22

[ 69](esp32__clock_8h.md#a411f896c814f629db94562be1c55e108)#define ESP32\_CAN\_MODULE ESP32\_TWAI\_MODULE

[ 70](esp32__clock_8h.md#a1360ddff70c3a29ce4a0b93199e4292e)#define ESP32\_EMAC\_MODULE 23

[ 71](esp32__clock_8h.md#ad5423ca02819aab6b3fe63c11b3cf998)#define ESP32\_RNG\_MODULE 24

[ 72](esp32__clock_8h.md#a4013c1fc7538bf46d5c1771f837a8b21)#define ESP32\_WIFI\_MODULE 25

[ 73](esp32__clock_8h.md#ad180ebcea5567ce6c3145998f3761584)#define ESP32\_BT\_MODULE 26

[ 74](esp32__clock_8h.md#aba1295479849f8b4dc44245e330e3020)#define ESP32\_WIFI\_BT\_COMMON\_MODULE 27

[ 75](esp32__clock_8h.md#a653e6d1f91c532b3ba313be27a97c2af)#define ESP32\_BT\_BASEBAND\_MODULE 28

[ 76](esp32__clock_8h.md#a8e27f45346390d8909f9424f13280b76)#define ESP32\_BT\_LC\_MODULE 29

[ 77](esp32__clock_8h.md#a290ac6ab6c5de2e8d84a911e389e1cfc)#define ESP32\_AES\_MODULE 30

[ 78](esp32__clock_8h.md#a683dd8814bf170018b63b57268c0fde9)#define ESP32\_SHA\_MODULE 31

[ 79](esp32__clock_8h.md#a5261565b59c0a5b75794014b80692b33)#define ESP32\_RSA\_MODULE 32

[ 80](esp32__clock_8h.md#abe244da38fbe794e93094feef9b188fe)#define ESP32\_SARADC\_MODULE 33

[ 81](esp32__clock_8h.md#ac380a7ff843ee465763a355cb01ef295)#define ESP32\_MODULE\_MAX 34

82

83#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32\_clock.h](esp32__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
