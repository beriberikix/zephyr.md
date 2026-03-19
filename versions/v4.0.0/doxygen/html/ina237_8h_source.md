---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ina237_8h_source.html
original_path: doxygen/html/ina237_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ina237.h

[Go to the documentation of this file.](ina237_8h.md)

1/\*

2 \* Copyright (c) 2021 Grinn

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA237\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA237\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

11/\* Operating Mode \*/

[ 12](ina237_8h.md#a829d7aa6a07bad8da2583a648b6c0be9)#define INA237\_CFG\_HIGH\_PRECISION BIT(4)

[ 13](ina237_8h.md#ab42708837c802141acc358a385f6c5df)#define INA237\_OPER\_MODE\_SHUTDOWN 0x00

[ 14](ina237_8h.md#a6ed1315d8bd3eaa1c73fd398e9ce1c62)#define INA237\_OPER\_MODE\_BUS\_VOLTAGE\_TRIG 0x01

[ 15](ina237_8h.md#a90c2ca6edab1e6940a37026ca45d38cf)#define INA237\_OPER\_MODE\_SHUNT\_VOLTAGE\_TRIG 0x02

[ 16](ina237_8h.md#a2313b32f90362ff4f0be94c813c2d915)#define INA237\_OPER\_MODE\_SHUNT\_BUS\_VOLTAGE\_TRIG 0x03

[ 17](ina237_8h.md#af48a2674ff69fe726f3161962afb5172)#define INA237\_OPER\_MODE\_TEMP\_TRIG 0x04

[ 18](ina237_8h.md#a61bd0c9161348b93c1b781324de3b20f)#define INA237\_OPER\_MODE\_TEMP\_BUS\_VOLTAGE\_TRIG 0x05

[ 19](ina237_8h.md#a8a83cbfc8a517d8dc696431134f55b8a)#define INA237\_OPER\_MODE\_TEMP\_SHUNT\_VOLTAGE\_TRIG 0x06

[ 20](ina237_8h.md#a5f524151fa6b5583add8522337aa275b)#define INA237\_OPER\_MODE\_BUS\_SHUNT\_VOLTAGE\_TEMP\_TRIG 0x07

[ 21](ina237_8h.md#a4a6874ebe2fa43ab99812d4de4d6b2c1)#define INA237\_OPER\_MODE\_BUS\_VOLTAGE\_CONT 0x09

[ 22](ina237_8h.md#ae24188265ba63cd1b947585ea96efa42)#define INA237\_OPER\_MODE\_SHUNT\_VOLTAGE\_CONT 0x0A

[ 23](ina237_8h.md#a75919399317285114b63746e41fa9aae)#define INA237\_OPER\_MODE\_SHUNT\_BUS\_VOLTAGE\_CONT 0x0B

[ 24](ina237_8h.md#a96afd10c7f0e435cdef6a999295afae5)#define INA237\_OPER\_MODE\_TEMP\_CONT 0x0C

[ 25](ina237_8h.md#a51366870d0ef5c451ffdc92adf462b80)#define INA237\_OPER\_MODE\_BUS\_VOLTAGE\_TEMP\_CONT 0x0D

[ 26](ina237_8h.md#a51142226eb02138a1462b32e6a6b9c3d)#define INA237\_OPER\_MODE\_TEMP\_SHUNT\_VOLTAGE\_CONT 0x0E

[ 27](ina237_8h.md#a5cfe6bc07b3dff06c2eefc3f73101289)#define INA237\_OPER\_MODE\_BUS\_SHUNT\_VOLTAGE\_TEMP\_CONT 0x0F

28

29/\* Conversion time for bus, shunt and temp in micro-seconds \*/

[ 30](ina237_8h.md#a4c283158c66d3492efcbcb05bc797f43)#define INA237\_CONV\_TIME\_50 0x00

[ 31](ina237_8h.md#afa48d1d9aab85913e75d4413ca0ade61)#define INA237\_CONV\_TIME\_84 0x01

[ 32](ina237_8h.md#a1f9505d58321c288af4324577c98b722)#define INA237\_CONV\_TIME\_150 0x02

[ 33](ina237_8h.md#a37f20de30929ec2aab29568799d03ba9)#define INA237\_CONV\_TIME\_280 0x03

[ 34](ina237_8h.md#adfe72090337a08de1e334ecec1a83cd2)#define INA237\_CONV\_TIME\_540 0x04

[ 35](ina237_8h.md#a0c59baa9f6713fb4b651876934babca6)#define INA237\_CONV\_TIME\_1052 0x05

[ 36](ina237_8h.md#a73f063d5afcc5956769b1027a8ee7b6d)#define INA237\_CONV\_TIME\_2074 0x06

[ 37](ina237_8h.md#a5492b364f79ed890f67b6bc3b51b10ee)#define INA237\_CONV\_TIME\_4120 0x07

38

39/\* Averaging Mode \*/

[ 40](ina237_8h.md#a3c84d5be0bbca9a23fa823b5d0d01a33)#define INA237\_AVG\_MODE\_1 0x00

[ 41](ina237_8h.md#a4877129f08b10b594e05372a92e19987)#define INA237\_AVG\_MODE\_4 0x01

[ 42](ina237_8h.md#a3e199273cf3f18cd35cf0cc71f54d395)#define INA237\_AVG\_MODE\_16 0x02

[ 43](ina237_8h.md#aa1754bb85646932d2e3d269c6585fc4e)#define INA237\_AVG\_MODE\_64 0x03

[ 44](ina237_8h.md#a1501acf37a027128d62037757140c84a)#define INA237\_AVG\_MODE\_128 0x04

[ 45](ina237_8h.md#a88f55660b69e5620ea60c3a53fafb170)#define INA237\_AVG\_MODE\_256 0x05

[ 46](ina237_8h.md#a8f7c1aad6dd88132e5d791788eb96055)#define INA237\_AVG\_MODE\_512 0x06

[ 47](ina237_8h.md#a692ea64b27f36b455e361ff9f20eacc9)#define INA237\_AVG\_MODE\_1024 0x07

48

49/\* Reset Mode \*/

[ 50](ina237_8h.md#a21d67009b5359d2408bcf8c2bfc7bd01)#define INA237\_RST\_NORMAL\_OPERATION 0x00

[ 51](ina237_8h.md#a79451943b97ee1146c536838b687f926)#define INA237\_RST\_SYSTEM\_RESET 0x01

52

53/\* Delay for initial ADC conversion in steps of 2 ms \*/

[ 54](ina237_8h.md#a9bda801d1ba220808ee7bc7cadb4e1a8)#define INA237\_INIT\_ADC\_DELAY\_0\_S 0x00

[ 55](ina237_8h.md#a726c19fef618b0b81219b569e3dc318a)#define INA237\_INIT\_ADC\_DELAY\_2\_MS 0x01

[ 56](ina237_8h.md#ac088479421d24217c570770466f50b4b)#define INA237\_INIT\_ADC\_DELAY\_510\_MS 0xFF

57

58/\* Shunt full scale range selection across IN+ and IN–. \*/

[ 59](ina237_8h.md#a5afae9b977793fb53823085c83986bb6)#define INA237\_ADC\_RANGE\_163\_84 0x00

[ 60](ina237_8h.md#ae1c622a578b919b83781d3bc78429009)#define INA237\_ADC\_RANGE\_40\_96 0x01

61

[ 70](ina237_8h.md#a721c648626cab01daf4013fc199aead4)#define INA237\_CONFIG(rst\_mode, \

71 convdly, \

72 adc\_range) \

73 (((rst\_mode) << 15) | ((convdly) << 6) | ((adc\_range) << 4))

74

[ 84](ina237_8h.md#a7310c76dac4ff27046970be6b24caa59)#define INA237\_ADC\_CONFIG(mode, \

85 vshct, \

86 vbusct, \

87 vtct, \

88 avg) \

89 (((mode) << 12) | ((vbusct) << 9) | ((vshct) << 6) | ((vtct) << 3) | (avg))

90

91#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INA237\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [ina237.h](ina237_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
