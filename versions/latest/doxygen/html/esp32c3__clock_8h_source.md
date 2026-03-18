---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32c3__clock_8h_source.html
original_path: doxygen/html/esp32c3__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c3\_clock.h

[Go to the documentation of this file.](esp32c3__clock_8h.md)

1/\*

2 \* Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C3\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C3\_H\_

9

10/\* System Clock Source \*/

[ 11](esp32c3__clock_8h.md#afca77320ca383abd16c3da3dd9f5475b)#define ESP32\_CLK\_SRC\_XTAL 0U

[ 12](esp32c3__clock_8h.md#a2b6410b41a6a9b646ed1030e8626a8f8)#define ESP32\_CLK\_SRC\_PLL 1U

[ 13](esp32c3__clock_8h.md#a4de6bcb9ee3b5c6dfc4887528999af77)#define ESP32\_CLK\_SRC\_RTC8M 2U

[ 14](esp32c3__clock_8h.md#a9d8f8be2dbba1b9cfc31e2188868b025)#define ESP32\_CLK\_SRC\_APLL 3U

15

16/\* Supported CPU Frequencies \*/

[ 17](esp32c3__clock_8h.md#a7ef1aa6b333059931611dd948b93e147)#define ESP32\_CLK\_CPU\_80M 80000000

[ 18](esp32c3__clock_8h.md#a4ce7aae7fa038527cc1892e94762ddf5)#define ESP32\_CLK\_CPU\_160M 160000000

19

20/\* Supported XTAL Frequencies \*/

[ 21](esp32c3__clock_8h.md#aeb5c606e77a85fa858ab7af6061c7949)#define ESP32\_CLK\_XTAL\_32M 0U

[ 22](esp32c3__clock_8h.md#a6afe38f9f9c44a1bd2e5279163523a98)#define ESP32\_CLK\_XTAL\_40M 1U

23

24/\* Supported RTC fast clock frequencies \*/

[ 25](esp32c3__clock_8h.md#a7545a9269b1a9db19e45913f77e93ae1)#define ESP32\_RTC\_FAST\_CLK\_FREQ\_8M 8500000U

[ 26](esp32c3__clock_8h.md#accb6c4420081f80615e07a97606c6b62)#define ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX ESP32\_RTC\_FAST\_CLK\_FREQ\_8M

27

28/\* Supported RTC slow clock frequencies \*/

[ 29](esp32c3__clock_8h.md#ac1907007a9016544d3a8a84b350c2f0f)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_90K 90000U

[ 30](esp32c3__clock_8h.md#a995e21929ecfb57c86d7ca1b1cf8e010)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256 (ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX / 256)

[ 31](esp32c3__clock_8h.md#ac977efbcfd0b8665b9362b40af6657e8)#define ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K 32768U

32

33/\* Modules IDs

34 \* These IDs are actually offsets in CLK and RST Control registers.

35 \* These IDs shouldn't be changed unless there is a Hardware change

36 \* from Espressif.

37 \*

38 \* Basic Modules

39 \* Registers: DPORT\_PERIP\_CLK\_EN\_REG, DPORT\_PERIP\_RST\_EN\_REG

40 \*/

[ 41](esp32c3__clock_8h.md#a60f4f5ee56d788f2161b52ebbc2aa510)#define ESP32\_LEDC\_MODULE 0

[ 42](esp32c3__clock_8h.md#a9708d046fbadfb7ccbc5df3e0ae57844)#define ESP32\_UART0\_MODULE 1

[ 43](esp32c3__clock_8h.md#a480803130ef80df04527f4dd12525d48)#define ESP32\_UART1\_MODULE 2

[ 44](esp32c3__clock_8h.md#afcf8170a750f4dc35326010b52f4e082)#define ESP32\_USB\_MODULE 3

[ 45](esp32c3__clock_8h.md#a7331ffa2ec41896d05f1f86c4d30f758)#define ESP32\_I2C0\_MODULE 4

[ 46](esp32c3__clock_8h.md#a1cc05bfada949af9e9265abaadb1b6bc)#define ESP32\_I2S1\_MODULE 5

[ 47](esp32c3__clock_8h.md#a88ae2c1bafdc6e78258ada5cbb9368f9)#define ESP32\_TIMG0\_MODULE 6

[ 48](esp32c3__clock_8h.md#a251462caa49fc6fe0ae1c8fe99a87caa)#define ESP32\_TIMG1\_MODULE 7

[ 49](esp32c3__clock_8h.md#af5ef985d4eaf1ffe565e2662493178c6)#define ESP32\_UHCI0\_MODULE 8

[ 50](esp32c3__clock_8h.md#a4a2d8ca15cd619022c02f97842d54159)#define ESP32\_RMT\_MODULE 9

[ 51](esp32c3__clock_8h.md#a5652d0e2b1fc766dde13b84294d4576b)#define ESP32\_SPI\_MODULE 10

[ 52](esp32c3__clock_8h.md#a5e5283c23811e9c4f30980f1d865773b)#define ESP32\_SPI2\_MODULE 11

[ 53](esp32c3__clock_8h.md#aba65cf1082c8422cc1e91c710bb702cc)#define ESP32\_TWAI\_MODULE 12

[ 54](esp32c3__clock_8h.md#ad5423ca02819aab6b3fe63c11b3cf998)#define ESP32\_RNG\_MODULE 13

[ 55](esp32c3__clock_8h.md#a4013c1fc7538bf46d5c1771f837a8b21)#define ESP32\_WIFI\_MODULE 14

[ 56](esp32c3__clock_8h.md#ad180ebcea5567ce6c3145998f3761584)#define ESP32\_BT\_MODULE 15

[ 57](esp32c3__clock_8h.md#aba1295479849f8b4dc44245e330e3020)#define ESP32\_WIFI\_BT\_COMMON\_MODULE 16

[ 58](esp32c3__clock_8h.md#a653e6d1f91c532b3ba313be27a97c2af)#define ESP32\_BT\_BASEBAND\_MODULE 17

[ 59](esp32c3__clock_8h.md#a8e27f45346390d8909f9424f13280b76)#define ESP32\_BT\_LC\_MODULE 18

[ 60](esp32c3__clock_8h.md#a5261565b59c0a5b75794014b80692b33)#define ESP32\_RSA\_MODULE 19

[ 61](esp32c3__clock_8h.md#a290ac6ab6c5de2e8d84a911e389e1cfc)#define ESP32\_AES\_MODULE 20

[ 62](esp32c3__clock_8h.md#a683dd8814bf170018b63b57268c0fde9)#define ESP32\_SHA\_MODULE 21

[ 63](esp32c3__clock_8h.md#ae17c59442b576d1b9aade6019850e6f8)#define ESP32\_HMAC\_MODULE 22

[ 64](esp32c3__clock_8h.md#aaea0a7a0e789019e4ddfd38365e83688)#define ESP32\_DS\_MODULE 23

[ 65](esp32c3__clock_8h.md#a701fec66fac239e66a19389ea153ff75)#define ESP32\_GDMA\_MODULE 24

[ 66](esp32c3__clock_8h.md#aaf8e1de1e86906ba539863b9009ebe37)#define ESP32\_SYSTIMER\_MODULE 25

[ 67](esp32c3__clock_8h.md#abe244da38fbe794e93094feef9b188fe)#define ESP32\_SARADC\_MODULE 26

[ 68](esp32c3__clock_8h.md#ac380a7ff843ee465763a355cb01ef295)#define ESP32\_MODULE\_MAX 27

69

70#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C3\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32c3\_clock.h](esp32c3__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
