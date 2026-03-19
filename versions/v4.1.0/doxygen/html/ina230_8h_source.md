---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ina230_8h_source.html
original_path: doxygen/html/ina230_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ina230.h

[Go to the documentation of this file.](ina230_8h.md)

1/\*

2 \* Copyright 2021 The Chromium OS Authors

3 \* Copyright (c) 2021 Grinn

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA230\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA230\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

12/\* Mask/Enable bits that asserts the ALERT pin \*/

[ 13](ina230_8h.md#ac66cd3c1e640e40e03cfd0fa8eb6b553)#define INA230\_SHUNT\_VOLTAGE\_OVER BIT(15)

[ 14](ina230_8h.md#a040092c7325a5466a46941a5313cc4e8)#define INA230\_SHUNT\_VOLTAGE\_UNDER BIT(14)

[ 15](ina230_8h.md#a19e8853f4cd17ab415b0dff751019e61)#define INA230\_BUS\_VOLTAGE\_OVER BIT(13)

[ 16](ina230_8h.md#a6358dc1460787287df8248b0ed304784)#define INA230\_BUS\_VOLTAGE\_UNDER BIT(12)

[ 17](ina230_8h.md#a3b72c1af082ed974c74dfeabe6d8f15b)#define INA230\_OVER\_LIMIT\_POWER BIT(11)

[ 18](ina230_8h.md#aa789596e247090cd2829beafbbed6200)#define INA230\_CONVERSION\_READY BIT(10)

[ 19](ina230_8h.md#a168b1902c7fd80b20a63cc70653ce51a)#define INA230\_ALERT\_FUNCTION\_FLAG BIT(4)

[ 20](ina230_8h.md#a4985c309b299ca5b69afe92c127bba15)#define INA230\_CONVERSION\_READY\_FLAG BIT(3)

[ 21](ina230_8h.md#a0a34427f40f5100e98d3aed0e2d92c8f)#define INA230\_MATH\_OVERFLOW\_FLAG BIT(2)

[ 22](ina230_8h.md#aa97cd11f72647303d4ec67e49ef3739b)#define INA230\_ALERT\_POLARITY BIT(1)

[ 23](ina230_8h.md#aaeafbd49251d2c92f6cfb0f0fc067fc5)#define INA230\_ALERT\_LATCH\_ENABLE BIT(0)

24

25/\* Operating Mode \*/

[ 26](ina230_8h.md#acb3862f380fd234f8109cfc5c600a4d1)#define INA230\_OPER\_MODE\_POWER\_DOWN 0x00

[ 27](ina230_8h.md#a40b158024fc20e70683b264c1b6a15c1)#define INA230\_OPER\_MODE\_SHUNT\_VOLTAGE\_TRIG 0x01

[ 28](ina230_8h.md#abacc74f8d1e0890f566d7b8c26c0f999)#define INA230\_OPER\_MODE\_BUS\_VOLTAGE\_TRIG 0x02

[ 29](ina230_8h.md#a20379c383fc0d36177719d2fd3083375)#define INA230\_OPER\_MODE\_SHUNT\_BUS\_VOLTAGE\_TRIG 0x03

[ 30](ina230_8h.md#a0db3092938ca8768f1bdb2911499bd06)#define INA230\_OPER\_MODE\_SHUNT\_VOLTAGE\_CONT 0x05

[ 31](ina230_8h.md#a3c9319a04c00c3e8c4b3281be91c7274)#define INA230\_OPER\_MODE\_BUS\_VOLTAGE\_CONT 0x06

[ 32](ina230_8h.md#a8aa6b641d5304db934e97a9acc4e8185)#define INA230\_OPER\_MODE\_SHUNT\_BUS\_VOLTAGE\_CONT 0x07

33

34/\* Conversion time for bus and shunt in micro-seconds \*/

[ 35](ina230_8h.md#a609d89e2e03f973897892086c58373b3)#define INA230\_CONV\_TIME\_140 0x00

[ 36](ina230_8h.md#a3aaa2b4bbc38c2c6e813af488761d6fd)#define INA230\_CONV\_TIME\_204 0x01

[ 37](ina230_8h.md#afa298eb42a7ef83966d01f41d21694dd)#define INA230\_CONV\_TIME\_332 0x02

[ 38](ina230_8h.md#a38d12e2f397fb9606137dd3e8aa9a6d9)#define INA230\_CONV\_TIME\_588 0x03

[ 39](ina230_8h.md#af3558b94073c94a4a51a18e1138b9d9d)#define INA230\_CONV\_TIME\_1100 0x04

[ 40](ina230_8h.md#a75fa32c27aa4e5759e7b3248536f1478)#define INA230\_CONV\_TIME\_2116 0x05

[ 41](ina230_8h.md#ada84f5fe71c258478085a519e55bb70c)#define INA230\_CONV\_TIME\_4156 0x06

[ 42](ina230_8h.md#a6ce6c967ffd224b2e0df7a41ee77979f)#define INA230\_CONV\_TIME\_8244 0x07

43

44/\* Averaging Mode \*/

[ 45](ina230_8h.md#af6170f95a07663623351b693a76c772f)#define INA230\_AVG\_MODE\_1 0x00

[ 46](ina230_8h.md#a41491081f78b148c6776884d81e612be)#define INA230\_AVG\_MODE\_4 0x01

[ 47](ina230_8h.md#a9a8f69817a981937f2c61ce89420f9db)#define INA230\_AVG\_MODE\_16 0x02

[ 48](ina230_8h.md#a25553b578940087be9d6c61a1049fa51)#define INA230\_AVG\_MODE\_64 0x03

[ 49](ina230_8h.md#a1fe17a0d83b831a9e66a41abe09576c6)#define INA230\_AVG\_MODE\_128 0x04

[ 50](ina230_8h.md#a1a7c91438e80b95ba61a6096fbae569a)#define INA230\_AVG\_MODE\_256 0x05

[ 51](ina230_8h.md#a77be8bb5db31c9c610ea9e9b3a00285c)#define INA230\_AVG\_MODE\_512 0x06

[ 52](ina230_8h.md#a02ba7889aa1088a3e0038612b86a8401)#define INA230\_AVG\_MODE\_1024 0x07

53

[ 62](ina230_8h.md#a0cda48f2739c01d3f0c25e7ba5249cb7)#define INA230\_CONFIG(mode, \

63 svct, \

64 bvct, \

65 avg) \

66 (((avg) << 9) | ((bvct) << 6) | ((svct) << 3) | (mode))

67

68#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA230\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [ina230.h](ina230_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
