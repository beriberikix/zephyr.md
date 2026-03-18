---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32s2__clock_8h_source.html
original_path: doxygen/html/esp32s2__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s2\_clock.h

[Go to the documentation of this file.](esp32s2__clock_8h.md)

1/\*

2 \* Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32S2\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32S2\_H\_

9

10/\* System Clock Source \*/

[ 11](esp32s2__clock_8h.md#afca77320ca383abd16c3da3dd9f5475b)#define ESP32\_CLK\_SRC\_XTAL 0U

[ 12](esp32s2__clock_8h.md#a2b6410b41a6a9b646ed1030e8626a8f8)#define ESP32\_CLK\_SRC\_PLL 1U

[ 13](esp32s2__clock_8h.md#a4de6bcb9ee3b5c6dfc4887528999af77)#define ESP32\_CLK\_SRC\_RTC8M 2U

[ 14](esp32s2__clock_8h.md#a9d8f8be2dbba1b9cfc31e2188868b025)#define ESP32\_CLK\_SRC\_APLL 3U

15

16/\* Supported CPU Frequencies \*/

[ 17](esp32s2__clock_8h.md#ada91f47dd4cd7f9ceac7fb68b2042c23)#define ESP32\_CLK\_CPU\_26M 26000000

[ 18](esp32s2__clock_8h.md#a3360cb00458b450b1517d75d2b42b6ee)#define ESP32\_CLK\_CPU\_40M 40000000

[ 19](esp32s2__clock_8h.md#a7ef1aa6b333059931611dd948b93e147)#define ESP32\_CLK\_CPU\_80M 80000000

[ 20](esp32s2__clock_8h.md#a4ce7aae7fa038527cc1892e94762ddf5)#define ESP32\_CLK\_CPU\_160M 160000000

[ 21](esp32s2__clock_8h.md#afcd84cbe162c507b9fa70d7d397e417e)#define ESP32\_CLK\_CPU\_240M 240000000

22

23/\* Supported XTAL Frequencies \*/

[ 24](esp32s2__clock_8h.md#a6afe38f9f9c44a1bd2e5279163523a98)#define ESP32\_CLK\_XTAL\_40M 0U

25

26/\* Supported RTC fast clock frequencies \*/

[ 27](esp32s2__clock_8h.md#a7545a9269b1a9db19e45913f77e93ae1)#define ESP32\_RTC\_FAST\_CLK\_FREQ\_8M 8500000U

[ 28](esp32s2__clock_8h.md#accb6c4420081f80615e07a97606c6b62)#define ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX ESP32\_RTC\_FAST\_CLK\_FREQ\_8M

29

30/\* Supported RTC slow clock frequencies \*/

[ 31](esp32s2__clock_8h.md#ac1907007a9016544d3a8a84b350c2f0f)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_90K 90000U

[ 32](esp32s2__clock_8h.md#a995e21929ecfb57c86d7ca1b1cf8e010)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256 (ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX / 256)

[ 33](esp32s2__clock_8h.md#ac977efbcfd0b8665b9362b40af6657e8)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K 32768U

34

35/\* Modules IDs

36 \* These IDs are actually offsets in CLK and RST Control registers.

37 \* These IDs shouldn't be changed unless there is a Hardware change

38 \* from Espressif.

39 \*

40 \* Basic Modules

41 \* Registers: DPORT\_PERIP\_CLK\_EN\_REG, DPORT\_PERIP\_RST\_EN\_REG

42 \*/

[ 43](esp32s2__clock_8h.md#a60f4f5ee56d788f2161b52ebbc2aa510)#define ESP32\_LEDC\_MODULE 0

[ 44](esp32s2__clock_8h.md#a9708d046fbadfb7ccbc5df3e0ae57844)#define ESP32\_UART0\_MODULE 1

[ 45](esp32s2__clock_8h.md#a480803130ef80df04527f4dd12525d48)#define ESP32\_UART1\_MODULE 2

[ 46](esp32s2__clock_8h.md#afcf8170a750f4dc35326010b52f4e082)#define ESP32\_USB\_MODULE 3

[ 47](esp32s2__clock_8h.md#a7331ffa2ec41896d05f1f86c4d30f758)#define ESP32\_I2C0\_MODULE 4

[ 48](esp32s2__clock_8h.md#a5068c510487e0ce3002e4bf7082601cd)#define ESP32\_I2C1\_MODULE 5

[ 49](esp32s2__clock_8h.md#a21c262b775f6d533621d4ba8e8d6c9aa)#define ESP32\_I2S0\_MODULE 6

[ 50](esp32s2__clock_8h.md#a88ae2c1bafdc6e78258ada5cbb9368f9)#define ESP32\_TIMG0\_MODULE 7

[ 51](esp32s2__clock_8h.md#a251462caa49fc6fe0ae1c8fe99a87caa)#define ESP32\_TIMG1\_MODULE 8

[ 52](esp32s2__clock_8h.md#af5ef985d4eaf1ffe565e2662493178c6)#define ESP32\_UHCI0\_MODULE 9

[ 53](esp32s2__clock_8h.md#aa2c199cff85bcf8e5a306a056e71f1f5)#define ESP32\_UHCI1\_MODULE 10

[ 54](esp32s2__clock_8h.md#a4a2d8ca15cd619022c02f97842d54159)#define ESP32\_RMT\_MODULE 11

[ 55](esp32s2__clock_8h.md#ac0d8fb4397baaac7ff45dee8f4e1cb7c)#define ESP32\_PCNT\_MODULE 12

[ 56](esp32s2__clock_8h.md#a5652d0e2b1fc766dde13b84294d4576b)#define ESP32\_SPI\_MODULE 13

[ 57](esp32s2__clock_8h.md#abd1ec14355055113ef0e2db037664fed)#define ESP32\_FSPI\_MODULE 14

[ 58](esp32s2__clock_8h.md#af9492b3e7cf5282eff0a4ee342eac278)#define ESP32\_HSPI\_MODULE 15

[ 59](esp32s2__clock_8h.md#a196ac4b4192907882a85cf00f4b7b265)#define ESP32\_SPI2\_DMA\_MODULE 16

[ 60](esp32s2__clock_8h.md#a47b6ec180d6d07b21ffa9174fb6c9632)#define ESP32\_SPI3\_DMA\_MODULE 17

[ 61](esp32s2__clock_8h.md#aba65cf1082c8422cc1e91c710bb702cc)#define ESP32\_TWAI\_MODULE 18

[ 62](esp32s2__clock_8h.md#ad5423ca02819aab6b3fe63c11b3cf998)#define ESP32\_RNG\_MODULE 19

[ 63](esp32s2__clock_8h.md#a4013c1fc7538bf46d5c1771f837a8b21)#define ESP32\_WIFI\_MODULE 20

[ 64](esp32s2__clock_8h.md#aba1295479849f8b4dc44245e330e3020)#define ESP32\_WIFI\_BT\_COMMON\_MODULE 21

[ 65](esp32s2__clock_8h.md#aaf8e1de1e86906ba539863b9009ebe37)#define ESP32\_SYSTIMER\_MODULE 22

[ 66](esp32s2__clock_8h.md#a290ac6ab6c5de2e8d84a911e389e1cfc)#define ESP32\_AES\_MODULE 23

[ 67](esp32s2__clock_8h.md#a683dd8814bf170018b63b57268c0fde9)#define ESP32\_SHA\_MODULE 24

[ 68](esp32s2__clock_8h.md#a5261565b59c0a5b75794014b80692b33)#define ESP32\_RSA\_MODULE 25

[ 69](esp32s2__clock_8h.md#a538c91c0abb6956aa1aaf4f641cd2bc6)#define ESP32\_CRYPTO\_DMA\_MODULE 26

[ 70](esp32s2__clock_8h.md#aa75a0ac88fa73935c1d7b44359e506d6)#define ESP32\_AES\_DMA\_MODULE 27

[ 71](esp32s2__clock_8h.md#ac90b41ab8feed70d67e1d074c3bfda7b)#define ESP32\_SHA\_DMA\_MODULE 28

[ 72](esp32s2__clock_8h.md#abbb147eb71a9d6e655ed68d2d7478a84)#define ESP32\_DEDIC\_GPIO\_MODULE 29

[ 73](esp32s2__clock_8h.md#a1274254ab9bfbea5a9ada1c18ebaac24)#define ESP32\_PERIPH\_SARADC\_MODULE 30

[ 74](esp32s2__clock_8h.md#ac380a7ff843ee465763a355cb01ef295)#define ESP32\_MODULE\_MAX 31

75

76#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32S2\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32s2\_clock.h](esp32s2__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
