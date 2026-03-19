---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp32c6__clock_8h_source.html
original_path: doxygen/html/esp32c6__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c6\_clock.h

[Go to the documentation of this file.](esp32c6__clock_8h.md)

1/\*

2 \* Copyright (c) 2023 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C6\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C6\_H\_

9

10/\* Supported CPU clock Sources \*/

[ 11](esp32c6__clock_8h.md#a44ee3670c3168dd0ffbc79a563a7f074)#define ESP32\_CPU\_CLK\_SRC\_XTAL 0U

[ 12](esp32c6__clock_8h.md#a7a723b6353a23b55ef44d720297fe26f)#define ESP32\_CPU\_CLK\_SRC\_PLL 1U

[ 13](esp32c6__clock_8h.md#a1962dad90f737a51fcc70cea1931b236)#define ESP32\_CLK\_SRC\_RC\_FAST 2U

14

15/\* Supported CPU frequencies \*/

[ 16](esp32c6__clock_8h.md#a61275f95111fb2a6bdbe446c0228f877)#define ESP32\_CLK\_CPU\_PLL\_80M 80000000

[ 17](esp32c6__clock_8h.md#ad80a59287e6a2f3771fd448982be9555)#define ESP32\_CLK\_CPU\_PLL\_160M 160000000

[ 18](esp32c6__clock_8h.md#ab779f427209fda571ec4d229b8ef8bfc)#define ESP32\_CLK\_CPU\_RC\_FAST\_FREQ 17500000

19

20/\* Supported XTAL Frequencies \*/

[ 21](esp32c6__clock_8h.md#aeb5c606e77a85fa858ab7af6061c7949)#define ESP32\_CLK\_XTAL\_32M 32000000

[ 22](esp32c6__clock_8h.md#a6afe38f9f9c44a1bd2e5279163523a98)#define ESP32\_CLK\_XTAL\_40M 40000000

23

24/\* Supported RTC fast clock sources \*/

[ 25](esp32c6__clock_8h.md#aae48d9f1288771e11c11d6177ecf3af7)#define ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST 0

[ 26](esp32c6__clock_8h.md#a725193bf445b7f8f2c1058a6735ca476)#define ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2 1

27

28/\* Supported RTC slow clock frequencies \*/

[ 29](esp32c6__clock_8h.md#ad1d90df80dee3040dbe8c968cd774443)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW 0

[ 30](esp32c6__clock_8h.md#aeaccf7695cab85cd7523c6ebc21704c4)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K 1

[ 31](esp32c6__clock_8h.md#ad2816af571c412c39237c7e2f5f18c04)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC32K 2

[ 32](esp32c6__clock_8h.md#aa5d6a46de7da027832aa02489c062069)#define ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC 9

33

34/\* RTC slow clock frequencies \*/

[ 35](esp32c6__clock_8h.md#af5cdcfa17e680ceda2f90e375eded6e6)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ 136000

[ 36](esp32c6__clock_8h.md#ab63ec0973bfb87f7f09c5614ab66deb8)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ 32768

[ 37](esp32c6__clock_8h.md#a3b18cdc509424e2249c7f4c3f1d93107)#define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC32K\_FREQ 32768

38

39/\* Modules IDs

40 \* These IDs are actually offsets in CLK and RST Control registers.

41 \* These IDs shouldn't be changed unless there is a Hardware change

42 \* from Espressif.

43 \*

44 \* Basic Modules

45 \* Registers: DPORT\_PERIP\_CLK\_EN\_REG, DPORT\_PERIP\_RST\_EN\_REG

46 \*/

[ 47](esp32c6__clock_8h.md#a60f4f5ee56d788f2161b52ebbc2aa510)#define ESP32\_LEDC\_MODULE 0

[ 48](esp32c6__clock_8h.md#a9708d046fbadfb7ccbc5df3e0ae57844)#define ESP32\_UART0\_MODULE 1

[ 49](esp32c6__clock_8h.md#a480803130ef80df04527f4dd12525d48)#define ESP32\_UART1\_MODULE 2

[ 50](esp32c6__clock_8h.md#afcf8170a750f4dc35326010b52f4e082)#define ESP32\_USB\_MODULE 3

[ 51](esp32c6__clock_8h.md#a7331ffa2ec41896d05f1f86c4d30f758)#define ESP32\_I2C0\_MODULE 4

[ 52](esp32c6__clock_8h.md#a1cc05bfada949af9e9265abaadb1b6bc)#define ESP32\_I2S1\_MODULE 5

[ 53](esp32c6__clock_8h.md#a88ae2c1bafdc6e78258ada5cbb9368f9)#define ESP32\_TIMG0\_MODULE 6

[ 54](esp32c6__clock_8h.md#a251462caa49fc6fe0ae1c8fe99a87caa)#define ESP32\_TIMG1\_MODULE 7

[ 55](esp32c6__clock_8h.md#af5ef985d4eaf1ffe565e2662493178c6)#define ESP32\_UHCI0\_MODULE 8

[ 56](esp32c6__clock_8h.md#a4a2d8ca15cd619022c02f97842d54159)#define ESP32\_RMT\_MODULE 9

[ 57](esp32c6__clock_8h.md#ac0d8fb4397baaac7ff45dee8f4e1cb7c)#define ESP32\_PCNT\_MODULE 10

[ 58](esp32c6__clock_8h.md#a5652d0e2b1fc766dde13b84294d4576b)#define ESP32\_SPI\_MODULE 11

[ 59](esp32c6__clock_8h.md#a5e5283c23811e9c4f30980f1d865773b)#define ESP32\_SPI2\_MODULE 12

[ 60](esp32c6__clock_8h.md#ad6847f96f663ae04ca4d2c324b793d16)#define ESP32\_TWAI0\_MODULE 13

[ 61](esp32c6__clock_8h.md#a0f0617f973ff3de27881f36957cd7cf2)#define ESP32\_TWAI1\_MODULE 14

[ 62](esp32c6__clock_8h.md#ad5423ca02819aab6b3fe63c11b3cf998)#define ESP32\_RNG\_MODULE 15

[ 63](esp32c6__clock_8h.md#a5261565b59c0a5b75794014b80692b33)#define ESP32\_RSA\_MODULE 16

[ 64](esp32c6__clock_8h.md#a290ac6ab6c5de2e8d84a911e389e1cfc)#define ESP32\_AES\_MODULE 17

[ 65](esp32c6__clock_8h.md#a683dd8814bf170018b63b57268c0fde9)#define ESP32\_SHA\_MODULE 18

[ 66](esp32c6__clock_8h.md#a27bd450bf21c8b7502d1f32d9536129f)#define ESP32\_ECC\_MODULE 19

[ 67](esp32c6__clock_8h.md#ae17c59442b576d1b9aade6019850e6f8)#define ESP32\_HMAC\_MODULE 20

[ 68](esp32c6__clock_8h.md#aaea0a7a0e789019e4ddfd38365e83688)#define ESP32\_DS\_MODULE 21

[ 69](esp32c6__clock_8h.md#a83b43d5f4d6373a5bb437de5ee5c091f)#define ESP32\_SDIO\_SLAVE\_MODULE 22

[ 70](esp32c6__clock_8h.md#a701fec66fac239e66a19389ea153ff75)#define ESP32\_GDMA\_MODULE 23

[ 71](esp32c6__clock_8h.md#a13e722b2a08b3ea2da2ba3b40d794697)#define ESP32\_MCPWM0\_MODULE 24

[ 72](esp32c6__clock_8h.md#a991c820648c7ef77b5aff2cecefee45d)#define ESP32\_ETM\_MODULE 25

[ 73](esp32c6__clock_8h.md#ada34a774bc3ec003c91cfe7c89939763)#define ESP32\_PARLIO\_MODULE 26

[ 74](esp32c6__clock_8h.md#aaf8e1de1e86906ba539863b9009ebe37)#define ESP32\_SYSTIMER\_MODULE 27

[ 75](esp32c6__clock_8h.md#abe244da38fbe794e93094feef9b188fe)#define ESP32\_SARADC\_MODULE 28

[ 76](esp32c6__clock_8h.md#a488d6d32cf66e81a27f0999f837fe39a)#define ESP32\_TEMPSENSOR\_MODULE 29

[ 77](esp32c6__clock_8h.md#a4a2832234309c8525ce7ce35a05ae41f)#define ESP32\_REGDMA\_MODULE 30

[ 78](esp32c6__clock_8h.md#a5ccf92c28d468d746c24d34453ff1caa)#define ESP32\_LP\_I2C0\_MODULE 31

79/\* Peripherals clock managed by the modem\_clock driver must be listed last \*/

[ 80](esp32c6__clock_8h.md#a4013c1fc7538bf46d5c1771f837a8b21)#define ESP32\_WIFI\_MODULE 32

[ 81](esp32c6__clock_8h.md#ad180ebcea5567ce6c3145998f3761584)#define ESP32\_BT\_MODULE 33

[ 82](esp32c6__clock_8h.md#adf10ec1f34cbc43fb1e896da892c677d)#define ESP32\_IEEE802154\_MODULE 34

[ 83](esp32c6__clock_8h.md#afe4f89e4a6712cc76536ea1b6a769a2d)#define ESP32\_COEX\_MODULE 35

[ 84](esp32c6__clock_8h.md#ae77d17fb45b7464a1ae16cc8e95ad6a2)#define ESP32\_PHY\_MODULE 36

[ 85](esp32c6__clock_8h.md#ac380a7ff843ee465763a355cb01ef295)#define ESP32\_MODULE\_MAX 37

86

87#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_ESP32C6\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32c6\_clock.h](esp32c6__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
