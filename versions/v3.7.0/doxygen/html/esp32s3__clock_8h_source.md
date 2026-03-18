---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp32s3__clock_8h_source.html
original_path: doxygen/html/esp32s3__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s3\_clock.h

[Go to the documentation of this file.](esp32s3__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32S3\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32S3\_H\_

9

10/\* Supported CPU clock Sources \*/

[ 11](esp32s3__clock_8h.md#a44ee3670c3168dd0ffbc79a563a7f074)#define ESP32\_CPU\_CLK\_SRC\_XTAL 0U

[ 12](esp32s3__clock_8h.md#a7a723b6353a23b55ef44d720297fe26f)#define ESP32\_CPU\_CLK\_SRC\_PLL 1U

[ 13](esp32s3__clock_8h.md#a1962dad90f737a51fcc70cea1931b236)#define ESP32\_CLK\_SRC\_RC\_FAST 2U

14

15/\* Supported PLL CPU frequencies \*/

[ 16](esp32s3__clock_8h.md#a61275f95111fb2a6bdbe446c0228f877)#define ESP32\_CLK\_CPU\_PLL\_80M 80000000

[ 17](esp32s3__clock_8h.md#ad80a59287e6a2f3771fd448982be9555)#define ESP32\_CLK\_CPU\_PLL\_160M 160000000

[ 18](esp32s3__clock_8h.md#ae0cca31853cf16bf9fa85508bbf9347f)#define ESP32\_CLK\_CPU\_PLL\_240M 240000000

[ 19](esp32s3__clock_8h.md#ab779f427209fda571ec4d229b8ef8bfc)#define ESP32\_CLK\_CPU\_RC\_FAST\_FREQ 17500000

20

21/\* Supported XTAL frequencies \*/

[ 22](esp32s3__clock_8h.md#aeb5c606e77a85fa858ab7af6061c7949)#define ESP32\_CLK\_XTAL\_32M 32000000

[ 23](esp32s3__clock_8h.md#a6afe38f9f9c44a1bd2e5279163523a98)#define ESP32\_CLK\_XTAL\_40M 40000000

24

25/\* Supported RTC fast clock sources \*/

[ 26](esp32s3__clock_8h.md#a725193bf445b7f8f2c1058a6735ca476)#define ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2 0

[ 27](esp32s3__clock_8h.md#aae48d9f1288771e11c11d6177ecf3af7)#define ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST 1

28

29/\* Supported RTC slow clock sources \*/

[ 30](esp32s3__clock_8h.md#ad1d90df80dee3040dbe8c968cd774443)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW 0

[ 31](esp32s3__clock_8h.md#aeaccf7695cab85cd7523c6ebc21704c4)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K 1

[ 32](esp32s3__clock_8h.md#aaec50946dbdaabaf2199e795a389634e)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256 2

[ 33](esp32s3__clock_8h.md#aa5d6a46de7da027832aa02489c062069)#define ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC 9

34

35/\* RTC slow clock frequencies \*/

[ 36](esp32s3__clock_8h.md#af5cdcfa17e680ceda2f90e375eded6e6)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ 136000

[ 37](esp32s3__clock_8h.md#ab63ec0973bfb87f7f09c5614ab66deb8)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ 32768

[ 38](esp32s3__clock_8h.md#a8531ee06161cae4ea8516d00825c32c8)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ 68359

39

40/\* Modules IDs

41 \* These IDs are actually offsets in CLK and RST Control registers.

42 \* These IDs shouldn't be changed unless there is a Hardware change

43 \* from Espressif.

44 \*

45 \* Basic Modules

46 \* Registers: DPORT\_PERIP\_CLK\_EN\_REG, DPORT\_PERIP\_RST\_EN\_REG

47 \*/

[ 48](esp32s3__clock_8h.md#a60f4f5ee56d788f2161b52ebbc2aa510)#define ESP32\_LEDC\_MODULE 0

[ 49](esp32s3__clock_8h.md#a9708d046fbadfb7ccbc5df3e0ae57844)#define ESP32\_UART0\_MODULE 1

[ 50](esp32s3__clock_8h.md#a480803130ef80df04527f4dd12525d48)#define ESP32\_UART1\_MODULE 2

[ 51](esp32s3__clock_8h.md#a975be76987c86a84903dcc626bdc1478)#define ESP32\_UART2\_MODULE 3

[ 52](esp32s3__clock_8h.md#afcf8170a750f4dc35326010b52f4e082)#define ESP32\_USB\_MODULE 4

[ 53](esp32s3__clock_8h.md#a7331ffa2ec41896d05f1f86c4d30f758)#define ESP32\_I2C0\_MODULE 5

[ 54](esp32s3__clock_8h.md#a5068c510487e0ce3002e4bf7082601cd)#define ESP32\_I2C1\_MODULE 6

[ 55](esp32s3__clock_8h.md#a21c262b775f6d533621d4ba8e8d6c9aa)#define ESP32\_I2S0\_MODULE 7

[ 56](esp32s3__clock_8h.md#a1cc05bfada949af9e9265abaadb1b6bc)#define ESP32\_I2S1\_MODULE 8

[ 57](esp32s3__clock_8h.md#af001f35d3c109955b027a97f7b676edd)#define ESP32\_LCD\_CAM\_MODULE 9

[ 58](esp32s3__clock_8h.md#a88ae2c1bafdc6e78258ada5cbb9368f9)#define ESP32\_TIMG0\_MODULE 10

[ 59](esp32s3__clock_8h.md#a251462caa49fc6fe0ae1c8fe99a87caa)#define ESP32\_TIMG1\_MODULE 11

[ 60](esp32s3__clock_8h.md#a8f939663db0f14133c2beb6dfc7dc3b7)#define ESP32\_PWM0\_MODULE 12

[ 61](esp32s3__clock_8h.md#aa5690cffa8770c3e2d0457557e52f300)#define ESP32\_PWM1\_MODULE 13

[ 62](esp32s3__clock_8h.md#a843cfd7e2a80b664b132a6ae6532410b)#define ESP32\_PWM2\_MODULE 14

[ 63](esp32s3__clock_8h.md#a1783f3089e7375ae7b55077ac80871d1)#define ESP32\_PWM3\_MODULE 15

[ 64](esp32s3__clock_8h.md#af5ef985d4eaf1ffe565e2662493178c6)#define ESP32\_UHCI0\_MODULE 16

[ 65](esp32s3__clock_8h.md#aa2c199cff85bcf8e5a306a056e71f1f5)#define ESP32\_UHCI1\_MODULE 17

[ 66](esp32s3__clock_8h.md#a4a2d8ca15cd619022c02f97842d54159)#define ESP32\_RMT\_MODULE 18

[ 67](esp32s3__clock_8h.md#ac0d8fb4397baaac7ff45dee8f4e1cb7c)#define ESP32\_PCNT\_MODULE 19

[ 68](esp32s3__clock_8h.md#a5652d0e2b1fc766dde13b84294d4576b)#define ESP32\_SPI\_MODULE 20

[ 69](esp32s3__clock_8h.md#a5e5283c23811e9c4f30980f1d865773b)#define ESP32\_SPI2\_MODULE 21

[ 70](esp32s3__clock_8h.md#aaaa2f3fbdc6e647799666e1885d4b4ff)#define ESP32\_SPI3\_MODULE 22

[ 71](esp32s3__clock_8h.md#a72052a75b3541623f59063260c4dbc32)#define ESP32\_SDMMC\_MODULE 23

[ 72](esp32s3__clock_8h.md#aba65cf1082c8422cc1e91c710bb702cc)#define ESP32\_TWAI\_MODULE 24

[ 73](esp32s3__clock_8h.md#ad5423ca02819aab6b3fe63c11b3cf998)#define ESP32\_RNG\_MODULE 25

[ 74](esp32s3__clock_8h.md#a4013c1fc7538bf46d5c1771f837a8b21)#define ESP32\_WIFI\_MODULE 26

[ 75](esp32s3__clock_8h.md#ad180ebcea5567ce6c3145998f3761584)#define ESP32\_BT\_MODULE 27

[ 76](esp32s3__clock_8h.md#aba1295479849f8b4dc44245e330e3020)#define ESP32\_WIFI\_BT\_COMMON\_MODULE 28

[ 77](esp32s3__clock_8h.md#a653e6d1f91c532b3ba313be27a97c2af)#define ESP32\_BT\_BASEBAND\_MODULE 29

[ 78](esp32s3__clock_8h.md#a8e27f45346390d8909f9424f13280b76)#define ESP32\_BT\_LC\_MODULE 30

[ 79](esp32s3__clock_8h.md#a290ac6ab6c5de2e8d84a911e389e1cfc)#define ESP32\_AES\_MODULE 31

[ 80](esp32s3__clock_8h.md#a683dd8814bf170018b63b57268c0fde9)#define ESP32\_SHA\_MODULE 32

[ 81](esp32s3__clock_8h.md#ae17c59442b576d1b9aade6019850e6f8)#define ESP32\_HMAC\_MODULE 33

[ 82](esp32s3__clock_8h.md#aaea0a7a0e789019e4ddfd38365e83688)#define ESP32\_DS\_MODULE 34

[ 83](esp32s3__clock_8h.md#a5261565b59c0a5b75794014b80692b33)#define ESP32\_RSA\_MODULE 35

[ 84](esp32s3__clock_8h.md#aaf8e1de1e86906ba539863b9009ebe37)#define ESP32\_SYSTIMER\_MODULE 36

[ 85](esp32s3__clock_8h.md#a701fec66fac239e66a19389ea153ff75)#define ESP32\_GDMA\_MODULE 37

[ 86](esp32s3__clock_8h.md#abbb147eb71a9d6e655ed68d2d7478a84)#define ESP32\_DEDIC\_GPIO\_MODULE 38

[ 87](esp32s3__clock_8h.md#abe244da38fbe794e93094feef9b188fe)#define ESP32\_SARADC\_MODULE 39

[ 88](esp32s3__clock_8h.md#ac380a7ff843ee465763a355cb01ef295)#define ESP32\_MODULE\_MAX 40

89

90#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32S3\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32s3\_clock.h](esp32s3__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
