---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dt-bindings_2sensor_2tmag5273_8h_source.html
original_path: doxygen/html/dt-bindings_2sensor_2tmag5273_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmag5273.h

[Go to the documentation of this file.](dt-bindings_2sensor_2tmag5273_8h.md)

1/\*

2 \* Copyright (c) 2023 deveritec GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_TMAG5273\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_TMAG5273\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

11/\* Operating Mode \*/

[ 12](dt-bindings_2sensor_2tmag5273_8h.md#a7c4ac425f1167fca06025db9a2b92153)#define TMAG5273\_DT\_OPER\_MODE\_CONTINUOUS 0

[ 13](dt-bindings_2sensor_2tmag5273_8h.md#a13fea164a14fc3a2d38aebce67e38e12)#define TMAG5273\_DT\_OPER\_MODE\_STANDBY 1

14

15/\* Axis \*/

[ 16](dt-bindings_2sensor_2tmag5273_8h.md#a258a2507f733c059f2b5b212d505ccd8)#define TMAG5273\_DT\_AXIS\_NONE 0x0

[ 17](dt-bindings_2sensor_2tmag5273_8h.md#a3040ac9025679745dbfe52463f95bd9f)#define TMAG5273\_DT\_AXIS\_X 0x1

[ 18](dt-bindings_2sensor_2tmag5273_8h.md#a0d352bd659851f02169036f205e8b012)#define TMAG5273\_DT\_AXIS\_Y 0x2

[ 19](dt-bindings_2sensor_2tmag5273_8h.md#a10d89d64876dc4d32398e2765ef5079f)#define TMAG5273\_DT\_AXIS\_Z 0x4

[ 20](dt-bindings_2sensor_2tmag5273_8h.md#a08aacefba8f390ac1ace72e672de83cc)#define TMAG5273\_DT\_AXIS\_XY (TMAG5273\_DT\_AXIS\_X | TMAG5273\_DT\_AXIS\_Y)

[ 21](dt-bindings_2sensor_2tmag5273_8h.md#a53b02b4b3cf5126abd4ab939c74fc633)#define TMAG5273\_DT\_AXIS\_XZ (TMAG5273\_DT\_AXIS\_X | TMAG5273\_DT\_AXIS\_Z)

[ 22](dt-bindings_2sensor_2tmag5273_8h.md#a1ee1d7f126feb9b5652670e53d24f0b6)#define TMAG5273\_DT\_AXIS\_YZ (TMAG5273\_DT\_AXIS\_Y | TMAG5273\_DT\_AXIS\_Z)

[ 23](dt-bindings_2sensor_2tmag5273_8h.md#ae16a8c01eafc1196d8fe0ffcf4976c72)#define TMAG5273\_DT\_AXIS\_XYZ (TMAG5273\_DT\_AXIS\_X | TMAG5273\_DT\_AXIS\_Y | TMAG5273\_DT\_AXIS\_Z)

[ 24](dt-bindings_2sensor_2tmag5273_8h.md#a6dcc34a5877ff11329c570f27184bbe7)#define TMAG5273\_DT\_AXIS\_XYX 0x8

[ 25](dt-bindings_2sensor_2tmag5273_8h.md#a000a0c930e0cdad6e7e91dc887004e4f)#define TMAG5273\_DT\_AXIS\_YXY 0x9

[ 26](dt-bindings_2sensor_2tmag5273_8h.md#ad778956fdac899196bc7782e2306d18d)#define TMAG5273\_DT\_AXIS\_YZY 0xA

[ 27](dt-bindings_2sensor_2tmag5273_8h.md#a6e1e7c54e34d9f82abe8c8f4e38826ed)#define TMAG5273\_DT\_AXIS\_XZX 0xB

28

29/\* Range \*/

[ 30](dt-bindings_2sensor_2tmag5273_8h.md#ad536884f65cfb8d90f35c15b26afec04)#define TMAG5273\_DT\_AXIS\_RANGE\_LOW 0

[ 31](dt-bindings_2sensor_2tmag5273_8h.md#a6b279486342219e7dfd5555c34cc7d37)#define TMAG5273\_DT\_AXIS\_RANGE\_HIGH 1

[ 32](dt-bindings_2sensor_2tmag5273_8h.md#a2aa9dfa7a74f61a821d2d7f0c2629b55)#define TMAG5273\_DT\_AXIS\_RANGE\_RUNTIME 2

33

34/\* Interrupt-Mode \*/

[ 35](dt-bindings_2sensor_2tmag5273_8h.md#ac7a80f12307ebb946ab106381704f2bc)#define TMAG5273\_DT\_INT\_THROUGH\_INT 0

[ 36](dt-bindings_2sensor_2tmag5273_8h.md#a97a154a99cf41aaadfbcb4fbaaa0fbdc)#define TMAG5273\_DT\_INT\_THROUGH\_INT\_EXC\_I2C 1

[ 37](dt-bindings_2sensor_2tmag5273_8h.md#a47ffb1ce227b6fc8cccda39898dabb96)#define TMAG5273\_DT\_INT\_THROUGH\_SCL 2

[ 38](dt-bindings_2sensor_2tmag5273_8h.md#a5757c3a1364e72c3d4c0b30b5cfc0698)#define TMAG5273\_DT\_INT\_THROUGH\_SCL\_EXC\_I2C 3

39

40/\* Threshold crossings \*/

[ 41](dt-bindings_2sensor_2tmag5273_8h.md#a71b6e856b5a5db7af4e4ed0001de2f66)#define TMAG5273\_DT\_THRX\_COUNT\_1 0

[ 42](dt-bindings_2sensor_2tmag5273_8h.md#a3940888f116795a9d060195fdb717ff1)#define TMAG5273\_DT\_THRX\_COUNT\_4 1

43

44/\* Threshold direction \*/

[ 45](dt-bindings_2sensor_2tmag5273_8h.md#ab59755856b8372698deab44d9b8ec9a2)#define TMAG5273\_DT\_THRX\_ABOVE 0

[ 46](dt-bindings_2sensor_2tmag5273_8h.md#a348bd07ca130ff996bea612ad8cecba3)#define TMAG5273\_DT\_THRX\_BELOW 1

[ 47](dt-bindings_2sensor_2tmag5273_8h.md#a630c77a70f3db408a139dd10b3a28bb1)#define TMAG5273\_DT\_THRX\_OUTSIDE 2

[ 48](dt-bindings_2sensor_2tmag5273_8h.md#ac0b966cb05b35abe701b8af474fd0498)#define TMAG5273\_DT\_THRX\_INSIDE 3

49

50/\* Temperature coefficient \*/

[ 51](dt-bindings_2sensor_2tmag5273_8h.md#a19f4de1abe7275ec75641e5e5ce47826)#define TMAG5273\_DT\_TEMP\_COEFF\_NONE 0

[ 52](dt-bindings_2sensor_2tmag5273_8h.md#af51ec112fe16a5c8a5a55a42dd14fd92)#define TMAG5273\_DT\_TEMP\_COEFF\_NDBFE 1

[ 53](dt-bindings_2sensor_2tmag5273_8h.md#aec27747fbae8c0c62912431a3f9d2309)#define TMAG5273\_DT\_TEMP\_COEFF\_CERAMIC 2

54

55/\* Angle/Magnitude calculation \*/

[ 56](dt-bindings_2sensor_2tmag5273_8h.md#a7ba462d2a09ae0118a991c655fdca672)#define TMAG5273\_DT\_ANGLE\_MAG\_NONE 0

[ 57](dt-bindings_2sensor_2tmag5273_8h.md#ad34b392bf32680634ec9dddacee24c9b)#define TMAG5273\_DT\_ANGLE\_MAG\_XY 1

[ 58](dt-bindings_2sensor_2tmag5273_8h.md#aa48cfafa9b65e23e5f5915fc32f65633)#define TMAG5273\_DT\_ANGLE\_MAG\_YZ 2

[ 59](dt-bindings_2sensor_2tmag5273_8h.md#a074869eda0ffdc0a88138b8b3caaafec)#define TMAG5273\_DT\_ANGLE\_MAG\_XZ 3

[ 60](dt-bindings_2sensor_2tmag5273_8h.md#a88151dfd7f1aaeb43df745e88ef49241)#define TMAG5273\_DT\_ANGLE\_MAG\_RUNTIME 4

61

62/\* Channel Magnitude Gain Correction \*/

[ 63](dt-bindings_2sensor_2tmag5273_8h.md#a3d314538e20d924b9f5395b5d88be792)#define TMAG5273\_DT\_CORRECTION\_CH\_1 0

[ 64](dt-bindings_2sensor_2tmag5273_8h.md#a2174de2be873e446dafa512f6c67d4e2)#define TMAG5273\_DT\_CORRECTION\_CH\_2 1

65

66/\* Averaging \*/

[ 67](dt-bindings_2sensor_2tmag5273_8h.md#a13c1237e1040e5505e52525ab7c73a1a)#define TMAG5273\_DT\_AVERAGING\_NONE 0

[ 68](dt-bindings_2sensor_2tmag5273_8h.md#aed2549fe3a62ba565ec2e81eea214ec1)#define TMAG5273\_DT\_AVERAGING\_2X 1

[ 69](dt-bindings_2sensor_2tmag5273_8h.md#a4150c85cf8a5790fc3385899293aadce)#define TMAG5273\_DT\_AVERAGING\_4X 2

[ 70](dt-bindings_2sensor_2tmag5273_8h.md#a4981e523e151b8a7d36839b6312dd1ef)#define TMAG5273\_DT\_AVERAGING\_8X 3

[ 71](dt-bindings_2sensor_2tmag5273_8h.md#a2ec0413e64f5688429e28588c6194428)#define TMAG5273\_DT\_AVERAGING\_16X 4

[ 72](dt-bindings_2sensor_2tmag5273_8h.md#a965c7f2fc5ec1ccca97f666060fd24ef)#define TMAG5273\_DT\_AVERAGING\_32X 5

73

74/\* Sleeptime \*/

[ 75](dt-bindings_2sensor_2tmag5273_8h.md#a396ab63225a243e75eebb38d37b77b27)#define TMAG5273\_DT\_SLEEPTIME\_1MS 0

[ 76](dt-bindings_2sensor_2tmag5273_8h.md#ab88e09d09437f57ce31d1ab0f58a19cb)#define TMAG5273\_DT\_SLEEPTIME\_5MS 1

[ 77](dt-bindings_2sensor_2tmag5273_8h.md#aee41d1df9c33164ac47213b4e0079f8e)#define TMAG5273\_DT\_SLEEPTIME\_10MS 2

[ 78](dt-bindings_2sensor_2tmag5273_8h.md#a88cb7a5cdd0d52e31dae2c03b83b5874)#define TMAG5273\_DT\_SLEEPTIME\_15MS 3

[ 79](dt-bindings_2sensor_2tmag5273_8h.md#ac29e91afbd4636e495726e3252abcea7)#define TMAG5273\_DT\_SLEEPTIME\_20MS 4

[ 80](dt-bindings_2sensor_2tmag5273_8h.md#aad1cc10df9f35d2bb63cb4a3f021152f)#define TMAG5273\_DT\_SLEEPTIME\_30MS 5

[ 81](dt-bindings_2sensor_2tmag5273_8h.md#a03c1e099cd98b1b09a121bd5c353fc97)#define TMAG5273\_DT\_SLEEPTIME\_50MS 6

[ 82](dt-bindings_2sensor_2tmag5273_8h.md#a08371bf90c5ffe3ccd3634078c037779)#define TMAG5273\_DT\_SLEEPTIME\_100MS 7

[ 83](dt-bindings_2sensor_2tmag5273_8h.md#abc58f37d75364d3f8c7c03ee774ed091)#define TMAG5273\_DT\_SLEEPTIME\_500MS 8

[ 84](dt-bindings_2sensor_2tmag5273_8h.md#a7f011c43133f25c7653fa41aae041095)#define TMAG5273\_DT\_SLEEPTIME\_1000MS 9

[ 85](dt-bindings_2sensor_2tmag5273_8h.md#a947cb9dc7689e460f1ddbd8bd94bc15b)#define TMAG5273\_DT\_SLEEPTIME\_2000MS 10

[ 86](dt-bindings_2sensor_2tmag5273_8h.md#afddb082d0306a7858086c4ac227852e0)#define TMAG5273\_DT\_SLEEPTIME\_5000MS 11

[ 87](dt-bindings_2sensor_2tmag5273_8h.md#a69e543ed3e6df3c2b6df67618b546de3)#define TMAG5273\_DT\_SLEEPTIME\_20000MS 12

88

89#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_TMAG5273\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [tmag5273.h](dt-bindings_2sensor_2tmag5273_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
