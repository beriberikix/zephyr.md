---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ina226_8h_source.html
original_path: doxygen/html/ina226_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ina226.h

[Go to the documentation of this file.](ina226_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA226\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA226\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

12/\* Reset Mode. \*/

[ 13](ina226_8h.md#a8174524d294a89bcedeec335538cc373)#define INA226\_RST\_NORMAL\_OPERATION 0x00

[ 14](ina226_8h.md#a1369ecef1266f83dd93f970002ff61b7)#define INA226\_RST\_SYSTEM\_RESET 0x01

15

16/\* Averaging Mode. \*/

[ 17](ina226_8h.md#a5fb596bda9235774ae63f602366b7f75)#define INA226\_AVG\_MODE\_1 0x00

[ 18](ina226_8h.md#a23954364dead3a9df1a878c106939275)#define INA226\_AVG\_MODE\_4 0x01

[ 19](ina226_8h.md#a55785fdf8ae4aa57531dc5107303dce6)#define INA226\_AVG\_MODE\_16 0x02

[ 20](ina226_8h.md#a6d0365e097575da1f80cc9dfa20a69f3)#define INA226\_AVG\_MODE\_64 0x03

[ 21](ina226_8h.md#a22345ffb861e057d34a31e4df7340d04)#define INA226\_AVG\_MODE\_128 0x04

[ 22](ina226_8h.md#adc89cd11a9ece7a53f85c5fb2d81842c)#define INA226\_AVG\_MODE\_256 0x05

[ 23](ina226_8h.md#af02590f29166255a35e63305e39be4e0)#define INA226\_AVG\_MODE\_512 0x06

[ 24](ina226_8h.md#a035c1834dcf1ae41135371b2d9e64110)#define INA226\_AVG\_MODE\_1024 0x07

25

26/\* Conversion time for bus and shunt voltage in micro-seconds. \*/

[ 27](ina226_8h.md#a95a71cdbb30e0eddfd05f336c53a0bbb)#define INA226\_CONV\_TIME\_140 0x00

[ 28](ina226_8h.md#a49a08f6e61463403ac18fd89f9f6facb)#define INA226\_CONV\_TIME\_204 0x01

[ 29](ina226_8h.md#a6f45151cb3e367e9b2a66184fbd1ebf8)#define INA226\_CONV\_TIME\_332 0x02

[ 30](ina226_8h.md#a445eaee2b6aa6bbdb1caa106580b6036)#define INA226\_CONV\_TIME\_588 0x03

[ 31](ina226_8h.md#ae063a0b167607657e1ffc1f8e68b2a6c)#define INA226\_CONV\_TIME\_1100 0x04

[ 32](ina226_8h.md#a83b8bb8b54b2e4857793bf014d9f57af)#define INA226\_CONV\_TIME\_2116 0x05

[ 33](ina226_8h.md#a02b694b57e4304736d88639d64cebec4)#define INA226\_CONV\_TIME\_4156 0x06

[ 34](ina226_8h.md#af3037329e3f8b9c984308bf8f4fef851)#define INA226\_CONV\_TIME\_8244 0x07

35

36/\* Operating Mode. \*/

[ 37](ina226_8h.md#a8780c1da54c2e5ae863efb7ef1b310b9)#define INA226\_OPER\_MODE\_POWER\_DOWN 0x00

[ 38](ina226_8h.md#aed00293346e09e6ef3114dd3167d1ce5)#define INA226\_OPER\_MODE\_SHUNT\_VOLTAGE\_TRIG 0x01

[ 39](ina226_8h.md#a88aa0c1378cfe356b643c89bf1418e3e)#define INA226\_OPER\_MODE\_BUS\_VOLTAGE\_TRIG 0x02

[ 40](ina226_8h.md#a7e88c1ab79bed8425f3074b37903113b)#define INA226\_OPER\_MODE\_SHUNT\_BUS\_VOLTAGE\_TRIG 0x03

[ 41](ina226_8h.md#afad378147deb5e1789a40e5dd7611de9)#define INA226\_OPER\_MODE\_SHUNT\_VOLTAGE\_CONT 0x05

[ 42](ina226_8h.md#adcf4265f1272f33a8385cf6a8c20bc42)#define INA226\_OPER\_MODE\_BUS\_VOLTAGE\_CONT 0x06

[ 43](ina226_8h.md#aba344632242e46fcd392eaf7f114f820)#define INA226\_OPER\_MODE\_SHUNT\_BUS\_VOLTAGE\_CONT 0x07

44

45#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA226\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [ina226.h](ina226_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
