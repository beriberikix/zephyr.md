---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/esp32c2__clock_8h_source.html
original_path: doxygen/html/esp32c2__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c2\_clock.h

[Go to the documentation of this file.](esp32c2__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C2\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C2\_H\_

9

10/\* Supported CPU clock Sources \*/

[ 11](esp32c2__clock_8h.md#a44ee3670c3168dd0ffbc79a563a7f074)#define ESP32\_CPU\_CLK\_SRC\_XTAL 0U

[ 12](esp32c2__clock_8h.md#a7a723b6353a23b55ef44d720297fe26f)#define ESP32\_CPU\_CLK\_SRC\_PLL 1U

[ 13](esp32c2__clock_8h.md#a1962dad90f737a51fcc70cea1931b236)#define ESP32\_CLK\_SRC\_RC\_FAST 2U

14

15/\* Supported CPU frequencies \*/

[ 16](esp32c2__clock_8h.md#aa61a2254926bfec49b2eb959f307ff30)#define ESP32\_CLK\_CPU\_PLL\_40M 40000000

[ 17](esp32c2__clock_8h.md#af817a387d83b343413616ee4eaa73bc4)#define ESP32\_CLK\_CPU\_PLL\_60M 60000000

[ 18](esp32c2__clock_8h.md#a61275f95111fb2a6bdbe446c0228f877)#define ESP32\_CLK\_CPU\_PLL\_80M 80000000

[ 19](esp32c2__clock_8h.md#a31d4aba38136e01b31ff34c81b08256e)#define ESP32\_CLK\_CPU\_PLL\_120M 120000000

[ 20](esp32c2__clock_8h.md#ab779f427209fda571ec4d229b8ef8bfc)#define ESP32\_CLK\_CPU\_RC\_FAST\_FREQ 8750000

21

22/\* Supported XTAL frequencies \*/

[ 23](esp32c2__clock_8h.md#a06efe791ed749209eb07de5066c6eddc)#define ESP32\_CLK\_XTAL\_26M 26000000

[ 24](esp32c2__clock_8h.md#aeb5c606e77a85fa858ab7af6061c7949)#define ESP32\_CLK\_XTAL\_32M 32000000

[ 25](esp32c2__clock_8h.md#a6afe38f9f9c44a1bd2e5279163523a98)#define ESP32\_CLK\_XTAL\_40M 40000000

26

27/\* Supported RTC fast clock sources \*/

[ 28](esp32c2__clock_8h.md#a725193bf445b7f8f2c1058a6735ca476)#define ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2 0

[ 29](esp32c2__clock_8h.md#aae48d9f1288771e11c11d6177ecf3af7)#define ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST 1

30

31/\* Supported RTC slow clock sources \*/

[ 32](esp32c2__clock_8h.md#ad1d90df80dee3040dbe8c968cd774443)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW 0

[ 33](esp32c2__clock_8h.md#a0c9ed1e9c69731554227e93ddd086e9e)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_OSC\_SLOW 1

[ 34](esp32c2__clock_8h.md#aaec50946dbdaabaf2199e795a389634e)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256 2

35

36/\* RTC slow clock frequencies \*/

[ 37](esp32c2__clock_8h.md#af5cdcfa17e680ceda2f90e375eded6e6)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ 136000

[ 38](esp32c2__clock_8h.md#ab3d6d4b49e506dac9b7812b9abd30a82)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_OSC\_SLOW\_FREQ 32768

[ 39](esp32c2__clock_8h.md#a8531ee06161cae4ea8516d00825c32c8)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ 68359

40

41/\* Modules IDs

42 \* These IDs are actually offsets in CLK and RST Control registers.

43 \* These IDs shouldn't be changed unless there is a Hardware change

44 \* from Espressif.

45 \*

46 \* Basic Modules

47 \* Registers: DPORT\_PERIP\_CLK\_EN\_REG, DPORT\_PERIP\_RST\_EN\_REG

48 \*/

[ 49](esp32c2__clock_8h.md#a60f4f5ee56d788f2161b52ebbc2aa510)#define ESP32\_LEDC\_MODULE 0

[ 50](esp32c2__clock_8h.md#a9708d046fbadfb7ccbc5df3e0ae57844)#define ESP32\_UART0\_MODULE 1

[ 51](esp32c2__clock_8h.md#a480803130ef80df04527f4dd12525d48)#define ESP32\_UART1\_MODULE 2

[ 52](esp32c2__clock_8h.md#a7331ffa2ec41896d05f1f86c4d30f758)#define ESP32\_I2C0\_MODULE 3

[ 53](esp32c2__clock_8h.md#a88ae2c1bafdc6e78258ada5cbb9368f9)#define ESP32\_TIMG0\_MODULE 4

[ 54](esp32c2__clock_8h.md#a251462caa49fc6fe0ae1c8fe99a87caa)#define ESP32\_TIMG1\_MODULE 5 /\* No timg1 on esp32c2, TODO: IDF-3825 \*/

[ 55](esp32c2__clock_8h.md#af5ef985d4eaf1ffe565e2662493178c6)#define ESP32\_UHCI0\_MODULE 6

[ 56](esp32c2__clock_8h.md#a5652d0e2b1fc766dde13b84294d4576b)#define ESP32\_SPI\_MODULE 7 /\* SPI1 \*/

[ 57](esp32c2__clock_8h.md#a5e5283c23811e9c4f30980f1d865773b)#define ESP32\_SPI2\_MODULE 8 /\* SPI2 \*/

[ 58](esp32c2__clock_8h.md#ad5423ca02819aab6b3fe63c11b3cf998)#define ESP32\_RNG\_MODULE 9

[ 59](esp32c2__clock_8h.md#a4013c1fc7538bf46d5c1771f837a8b21)#define ESP32\_WIFI\_MODULE 10

[ 60](esp32c2__clock_8h.md#ad180ebcea5567ce6c3145998f3761584)#define ESP32\_BT\_MODULE 11

[ 61](esp32c2__clock_8h.md#aba1295479849f8b4dc44245e330e3020)#define ESP32\_WIFI\_BT\_COMMON\_MODULE 12

[ 62](esp32c2__clock_8h.md#a653e6d1f91c532b3ba313be27a97c2af)#define ESP32\_BT\_BASEBAND\_MODULE 13

[ 63](esp32c2__clock_8h.md#a8e27f45346390d8909f9424f13280b76)#define ESP32\_BT\_LC\_MODULE 14

[ 64](esp32c2__clock_8h.md#a290ac6ab6c5de2e8d84a911e389e1cfc)#define ESP32\_AES\_MODULE 15

[ 65](esp32c2__clock_8h.md#a683dd8814bf170018b63b57268c0fde9)#define ESP32\_SHA\_MODULE 16

[ 66](esp32c2__clock_8h.md#a27bd450bf21c8b7502d1f32d9536129f)#define ESP32\_ECC\_MODULE 17

[ 67](esp32c2__clock_8h.md#a701fec66fac239e66a19389ea153ff75)#define ESP32\_GDMA\_MODULE 18

[ 68](esp32c2__clock_8h.md#aaf8e1de1e86906ba539863b9009ebe37)#define ESP32\_SYSTIMER\_MODULE 19

[ 69](esp32c2__clock_8h.md#abe244da38fbe794e93094feef9b188fe)#define ESP32\_SARADC\_MODULE 20

[ 70](esp32c2__clock_8h.md#a488d6d32cf66e81a27f0999f837fe39a)#define ESP32\_TEMPSENSOR\_MODULE 21

[ 71](esp32c2__clock_8h.md#a65f83f03cf7bdda167c25d3bb283f99b)#define ESP32\_MODEM\_RPA\_MODULE 22

[ 72](esp32c2__clock_8h.md#ac380a7ff843ee465763a355cb01ef295)#define ESP32\_MODULE\_MAX 23

73

74#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C2\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32c2\_clock.h](esp32c2__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
