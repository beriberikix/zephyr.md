---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dt-bindings_2sensor_2tmag5273_8h.html
original_path: doxygen/html/dt-bindings_2sensor_2tmag5273_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmag5273.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](dt-bindings_2sensor_2tmag5273_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TMAG5273\_DT\_OPER\_MODE\_CONTINUOUS](#a7c4ac425f1167fca06025db9a2b92153)   0 |
| #define | [TMAG5273\_DT\_OPER\_MODE\_STANDBY](#a13fea164a14fc3a2d38aebce67e38e12)   1 |
| #define | [TMAG5273\_DT\_AXIS\_NONE](#a258a2507f733c059f2b5b212d505ccd8)   0x0 |
| #define | [TMAG5273\_DT\_AXIS\_X](#a3040ac9025679745dbfe52463f95bd9f)   0x1 |
| #define | [TMAG5273\_DT\_AXIS\_Y](#a0d352bd659851f02169036f205e8b012)   0x2 |
| #define | [TMAG5273\_DT\_AXIS\_Z](#a10d89d64876dc4d32398e2765ef5079f)   0x4 |
| #define | [TMAG5273\_DT\_AXIS\_XY](#a08aacefba8f390ac1ace72e672de83cc)   ([TMAG5273\_DT\_AXIS\_X](#a3040ac9025679745dbfe52463f95bd9f) | [TMAG5273\_DT\_AXIS\_Y](#a0d352bd659851f02169036f205e8b012)) |
| #define | [TMAG5273\_DT\_AXIS\_XZ](#a53b02b4b3cf5126abd4ab939c74fc633)   ([TMAG5273\_DT\_AXIS\_X](#a3040ac9025679745dbfe52463f95bd9f) | [TMAG5273\_DT\_AXIS\_Z](#a10d89d64876dc4d32398e2765ef5079f)) |
| #define | [TMAG5273\_DT\_AXIS\_YZ](#a1ee1d7f126feb9b5652670e53d24f0b6)   ([TMAG5273\_DT\_AXIS\_Y](#a0d352bd659851f02169036f205e8b012) | [TMAG5273\_DT\_AXIS\_Z](#a10d89d64876dc4d32398e2765ef5079f)) |
| #define | [TMAG5273\_DT\_AXIS\_XYZ](#ae16a8c01eafc1196d8fe0ffcf4976c72)   ([TMAG5273\_DT\_AXIS\_X](#a3040ac9025679745dbfe52463f95bd9f) | [TMAG5273\_DT\_AXIS\_Y](#a0d352bd659851f02169036f205e8b012) | [TMAG5273\_DT\_AXIS\_Z](#a10d89d64876dc4d32398e2765ef5079f)) |
| #define | [TMAG5273\_DT\_AXIS\_XYX](#a6dcc34a5877ff11329c570f27184bbe7)   0x8 |
| #define | [TMAG5273\_DT\_AXIS\_YXY](#a000a0c930e0cdad6e7e91dc887004e4f)   0x9 |
| #define | [TMAG5273\_DT\_AXIS\_YZY](#ad778956fdac899196bc7782e2306d18d)   0xA |
| #define | [TMAG5273\_DT\_AXIS\_XZX](#a6e1e7c54e34d9f82abe8c8f4e38826ed)   0xB |
| #define | [TMAG5273\_DT\_AXIS\_RANGE\_LOW](#ad536884f65cfb8d90f35c15b26afec04)   0 |
| #define | [TMAG5273\_DT\_AXIS\_RANGE\_HIGH](#a6b279486342219e7dfd5555c34cc7d37)   1 |
| #define | [TMAG5273\_DT\_AXIS\_RANGE\_RUNTIME](#a2aa9dfa7a74f61a821d2d7f0c2629b55)   2 |
| #define | [TMAG5273\_DT\_INT\_THROUGH\_INT](#ac7a80f12307ebb946ab106381704f2bc)   0 |
| #define | [TMAG5273\_DT\_INT\_THROUGH\_INT\_EXC\_I2C](#a97a154a99cf41aaadfbcb4fbaaa0fbdc)   1 |
| #define | [TMAG5273\_DT\_INT\_THROUGH\_SCL](#a47ffb1ce227b6fc8cccda39898dabb96)   2 |
| #define | [TMAG5273\_DT\_INT\_THROUGH\_SCL\_EXC\_I2C](#a5757c3a1364e72c3d4c0b30b5cfc0698)   3 |
| #define | [TMAG5273\_DT\_THRX\_COUNT\_1](#a71b6e856b5a5db7af4e4ed0001de2f66)   0 |
| #define | [TMAG5273\_DT\_THRX\_COUNT\_4](#a3940888f116795a9d060195fdb717ff1)   1 |
| #define | [TMAG5273\_DT\_THRX\_ABOVE](#ab59755856b8372698deab44d9b8ec9a2)   0 |
| #define | [TMAG5273\_DT\_THRX\_BELOW](#a348bd07ca130ff996bea612ad8cecba3)   1 |
| #define | [TMAG5273\_DT\_THRX\_OUTSIDE](#a630c77a70f3db408a139dd10b3a28bb1)   2 |
| #define | [TMAG5273\_DT\_THRX\_INSIDE](#ac0b966cb05b35abe701b8af474fd0498)   3 |
| #define | [TMAG5273\_DT\_TEMP\_COEFF\_NONE](#a19f4de1abe7275ec75641e5e5ce47826)   0 |
| #define | [TMAG5273\_DT\_TEMP\_COEFF\_NDBFE](#af51ec112fe16a5c8a5a55a42dd14fd92)   1 |
| #define | [TMAG5273\_DT\_TEMP\_COEFF\_CERAMIC](#aec27747fbae8c0c62912431a3f9d2309)   2 |
| #define | [TMAG5273\_DT\_ANGLE\_MAG\_NONE](#a7ba462d2a09ae0118a991c655fdca672)   0 |
| #define | [TMAG5273\_DT\_ANGLE\_MAG\_XY](#ad34b392bf32680634ec9dddacee24c9b)   1 |
| #define | [TMAG5273\_DT\_ANGLE\_MAG\_YZ](#aa48cfafa9b65e23e5f5915fc32f65633)   2 |
| #define | [TMAG5273\_DT\_ANGLE\_MAG\_XZ](#a074869eda0ffdc0a88138b8b3caaafec)   3 |
| #define | [TMAG5273\_DT\_ANGLE\_MAG\_RUNTIME](#a88151dfd7f1aaeb43df745e88ef49241)   4 |
| #define | [TMAG5273\_DT\_CORRECTION\_CH\_1](#a3d314538e20d924b9f5395b5d88be792)   0 |
| #define | [TMAG5273\_DT\_CORRECTION\_CH\_2](#a2174de2be873e446dafa512f6c67d4e2)   1 |
| #define | [TMAG5273\_DT\_AVERAGING\_NONE](#a13c1237e1040e5505e52525ab7c73a1a)   0 |
| #define | [TMAG5273\_DT\_AVERAGING\_2X](#aed2549fe3a62ba565ec2e81eea214ec1)   1 |
| #define | [TMAG5273\_DT\_AVERAGING\_4X](#a4150c85cf8a5790fc3385899293aadce)   2 |
| #define | [TMAG5273\_DT\_AVERAGING\_8X](#a4981e523e151b8a7d36839b6312dd1ef)   3 |
| #define | [TMAG5273\_DT\_AVERAGING\_16X](#a2ec0413e64f5688429e28588c6194428)   4 |
| #define | [TMAG5273\_DT\_AVERAGING\_32X](#a965c7f2fc5ec1ccca97f666060fd24ef)   5 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_1MS](#a396ab63225a243e75eebb38d37b77b27)   0 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_5MS](#ab88e09d09437f57ce31d1ab0f58a19cb)   1 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_10MS](#aee41d1df9c33164ac47213b4e0079f8e)   2 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_15MS](#a88cb7a5cdd0d52e31dae2c03b83b5874)   3 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_20MS](#ac29e91afbd4636e495726e3252abcea7)   4 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_30MS](#aad1cc10df9f35d2bb63cb4a3f021152f)   5 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_50MS](#a03c1e099cd98b1b09a121bd5c353fc97)   6 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_100MS](#a08371bf90c5ffe3ccd3634078c037779)   7 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_500MS](#abc58f37d75364d3f8c7c03ee774ed091)   8 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_1000MS](#a7f011c43133f25c7653fa41aae041095)   9 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_2000MS](#a947cb9dc7689e460f1ddbd8bd94bc15b)   10 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_5000MS](#afddb082d0306a7858086c4ac227852e0)   11 |
| #define | [TMAG5273\_DT\_SLEEPTIME\_20000MS](#a69e543ed3e6df3c2b6df67618b546de3)   12 |

## Macro Definition Documentation

## [◆ ](#a7ba462d2a09ae0118a991c655fdca672)TMAG5273\_DT\_ANGLE\_MAG\_NONE

| #define TMAG5273\_DT\_ANGLE\_MAG\_NONE   0 |
| --- |

## [◆ ](#a88151dfd7f1aaeb43df745e88ef49241)TMAG5273\_DT\_ANGLE\_MAG\_RUNTIME

| #define TMAG5273\_DT\_ANGLE\_MAG\_RUNTIME   4 |
| --- |

## [◆ ](#ad34b392bf32680634ec9dddacee24c9b)TMAG5273\_DT\_ANGLE\_MAG\_XY

| #define TMAG5273\_DT\_ANGLE\_MAG\_XY   1 |
| --- |

## [◆ ](#a074869eda0ffdc0a88138b8b3caaafec)TMAG5273\_DT\_ANGLE\_MAG\_XZ

| #define TMAG5273\_DT\_ANGLE\_MAG\_XZ   3 |
| --- |

## [◆ ](#aa48cfafa9b65e23e5f5915fc32f65633)TMAG5273\_DT\_ANGLE\_MAG\_YZ

| #define TMAG5273\_DT\_ANGLE\_MAG\_YZ   2 |
| --- |

## [◆ ](#a2ec0413e64f5688429e28588c6194428)TMAG5273\_DT\_AVERAGING\_16X

| #define TMAG5273\_DT\_AVERAGING\_16X   4 |
| --- |

## [◆ ](#aed2549fe3a62ba565ec2e81eea214ec1)TMAG5273\_DT\_AVERAGING\_2X

| #define TMAG5273\_DT\_AVERAGING\_2X   1 |
| --- |

## [◆ ](#a965c7f2fc5ec1ccca97f666060fd24ef)TMAG5273\_DT\_AVERAGING\_32X

| #define TMAG5273\_DT\_AVERAGING\_32X   5 |
| --- |

## [◆ ](#a4150c85cf8a5790fc3385899293aadce)TMAG5273\_DT\_AVERAGING\_4X

| #define TMAG5273\_DT\_AVERAGING\_4X   2 |
| --- |

## [◆ ](#a4981e523e151b8a7d36839b6312dd1ef)TMAG5273\_DT\_AVERAGING\_8X

| #define TMAG5273\_DT\_AVERAGING\_8X   3 |
| --- |

## [◆ ](#a13c1237e1040e5505e52525ab7c73a1a)TMAG5273\_DT\_AVERAGING\_NONE

| #define TMAG5273\_DT\_AVERAGING\_NONE   0 |
| --- |

## [◆ ](#a258a2507f733c059f2b5b212d505ccd8)TMAG5273\_DT\_AXIS\_NONE

| #define TMAG5273\_DT\_AXIS\_NONE   0x0 |
| --- |

## [◆ ](#a6b279486342219e7dfd5555c34cc7d37)TMAG5273\_DT\_AXIS\_RANGE\_HIGH

| #define TMAG5273\_DT\_AXIS\_RANGE\_HIGH   1 |
| --- |

## [◆ ](#ad536884f65cfb8d90f35c15b26afec04)TMAG5273\_DT\_AXIS\_RANGE\_LOW

| #define TMAG5273\_DT\_AXIS\_RANGE\_LOW   0 |
| --- |

## [◆ ](#a2aa9dfa7a74f61a821d2d7f0c2629b55)TMAG5273\_DT\_AXIS\_RANGE\_RUNTIME

| #define TMAG5273\_DT\_AXIS\_RANGE\_RUNTIME   2 |
| --- |

## [◆ ](#a3040ac9025679745dbfe52463f95bd9f)TMAG5273\_DT\_AXIS\_X

| #define TMAG5273\_DT\_AXIS\_X   0x1 |
| --- |

## [◆ ](#a08aacefba8f390ac1ace72e672de83cc)TMAG5273\_DT\_AXIS\_XY

| #define TMAG5273\_DT\_AXIS\_XY   ([TMAG5273\_DT\_AXIS\_X](#a3040ac9025679745dbfe52463f95bd9f) | [TMAG5273\_DT\_AXIS\_Y](#a0d352bd659851f02169036f205e8b012)) |
| --- |

## [◆ ](#a6dcc34a5877ff11329c570f27184bbe7)TMAG5273\_DT\_AXIS\_XYX

| #define TMAG5273\_DT\_AXIS\_XYX   0x8 |
| --- |

## [◆ ](#ae16a8c01eafc1196d8fe0ffcf4976c72)TMAG5273\_DT\_AXIS\_XYZ

| #define TMAG5273\_DT\_AXIS\_XYZ   ([TMAG5273\_DT\_AXIS\_X](#a3040ac9025679745dbfe52463f95bd9f) | [TMAG5273\_DT\_AXIS\_Y](#a0d352bd659851f02169036f205e8b012) | [TMAG5273\_DT\_AXIS\_Z](#a10d89d64876dc4d32398e2765ef5079f)) |
| --- |

## [◆ ](#a53b02b4b3cf5126abd4ab939c74fc633)TMAG5273\_DT\_AXIS\_XZ

| #define TMAG5273\_DT\_AXIS\_XZ   ([TMAG5273\_DT\_AXIS\_X](#a3040ac9025679745dbfe52463f95bd9f) | [TMAG5273\_DT\_AXIS\_Z](#a10d89d64876dc4d32398e2765ef5079f)) |
| --- |

## [◆ ](#a6e1e7c54e34d9f82abe8c8f4e38826ed)TMAG5273\_DT\_AXIS\_XZX

| #define TMAG5273\_DT\_AXIS\_XZX   0xB |
| --- |

## [◆ ](#a0d352bd659851f02169036f205e8b012)TMAG5273\_DT\_AXIS\_Y

| #define TMAG5273\_DT\_AXIS\_Y   0x2 |
| --- |

## [◆ ](#a000a0c930e0cdad6e7e91dc887004e4f)TMAG5273\_DT\_AXIS\_YXY

| #define TMAG5273\_DT\_AXIS\_YXY   0x9 |
| --- |

## [◆ ](#a1ee1d7f126feb9b5652670e53d24f0b6)TMAG5273\_DT\_AXIS\_YZ

| #define TMAG5273\_DT\_AXIS\_YZ   ([TMAG5273\_DT\_AXIS\_Y](#a0d352bd659851f02169036f205e8b012) | [TMAG5273\_DT\_AXIS\_Z](#a10d89d64876dc4d32398e2765ef5079f)) |
| --- |

## [◆ ](#ad778956fdac899196bc7782e2306d18d)TMAG5273\_DT\_AXIS\_YZY

| #define TMAG5273\_DT\_AXIS\_YZY   0xA |
| --- |

## [◆ ](#a10d89d64876dc4d32398e2765ef5079f)TMAG5273\_DT\_AXIS\_Z

| #define TMAG5273\_DT\_AXIS\_Z   0x4 |
| --- |

## [◆ ](#a3d314538e20d924b9f5395b5d88be792)TMAG5273\_DT\_CORRECTION\_CH\_1

| #define TMAG5273\_DT\_CORRECTION\_CH\_1   0 |
| --- |

## [◆ ](#a2174de2be873e446dafa512f6c67d4e2)TMAG5273\_DT\_CORRECTION\_CH\_2

| #define TMAG5273\_DT\_CORRECTION\_CH\_2   1 |
| --- |

## [◆ ](#ac7a80f12307ebb946ab106381704f2bc)TMAG5273\_DT\_INT\_THROUGH\_INT

| #define TMAG5273\_DT\_INT\_THROUGH\_INT   0 |
| --- |

## [◆ ](#a97a154a99cf41aaadfbcb4fbaaa0fbdc)TMAG5273\_DT\_INT\_THROUGH\_INT\_EXC\_I2C

| #define TMAG5273\_DT\_INT\_THROUGH\_INT\_EXC\_I2C   1 |
| --- |

## [◆ ](#a47ffb1ce227b6fc8cccda39898dabb96)TMAG5273\_DT\_INT\_THROUGH\_SCL

| #define TMAG5273\_DT\_INT\_THROUGH\_SCL   2 |
| --- |

## [◆ ](#a5757c3a1364e72c3d4c0b30b5cfc0698)TMAG5273\_DT\_INT\_THROUGH\_SCL\_EXC\_I2C

| #define TMAG5273\_DT\_INT\_THROUGH\_SCL\_EXC\_I2C   3 |
| --- |

## [◆ ](#a7c4ac425f1167fca06025db9a2b92153)TMAG5273\_DT\_OPER\_MODE\_CONTINUOUS

| #define TMAG5273\_DT\_OPER\_MODE\_CONTINUOUS   0 |
| --- |

## [◆ ](#a13fea164a14fc3a2d38aebce67e38e12)TMAG5273\_DT\_OPER\_MODE\_STANDBY

| #define TMAG5273\_DT\_OPER\_MODE\_STANDBY   1 |
| --- |

## [◆ ](#a7f011c43133f25c7653fa41aae041095)TMAG5273\_DT\_SLEEPTIME\_1000MS

| #define TMAG5273\_DT\_SLEEPTIME\_1000MS   9 |
| --- |

## [◆ ](#a08371bf90c5ffe3ccd3634078c037779)TMAG5273\_DT\_SLEEPTIME\_100MS

| #define TMAG5273\_DT\_SLEEPTIME\_100MS   7 |
| --- |

## [◆ ](#aee41d1df9c33164ac47213b4e0079f8e)TMAG5273\_DT\_SLEEPTIME\_10MS

| #define TMAG5273\_DT\_SLEEPTIME\_10MS   2 |
| --- |

## [◆ ](#a88cb7a5cdd0d52e31dae2c03b83b5874)TMAG5273\_DT\_SLEEPTIME\_15MS

| #define TMAG5273\_DT\_SLEEPTIME\_15MS   3 |
| --- |

## [◆ ](#a396ab63225a243e75eebb38d37b77b27)TMAG5273\_DT\_SLEEPTIME\_1MS

| #define TMAG5273\_DT\_SLEEPTIME\_1MS   0 |
| --- |

## [◆ ](#a69e543ed3e6df3c2b6df67618b546de3)TMAG5273\_DT\_SLEEPTIME\_20000MS

| #define TMAG5273\_DT\_SLEEPTIME\_20000MS   12 |
| --- |

## [◆ ](#a947cb9dc7689e460f1ddbd8bd94bc15b)TMAG5273\_DT\_SLEEPTIME\_2000MS

| #define TMAG5273\_DT\_SLEEPTIME\_2000MS   10 |
| --- |

## [◆ ](#ac29e91afbd4636e495726e3252abcea7)TMAG5273\_DT\_SLEEPTIME\_20MS

| #define TMAG5273\_DT\_SLEEPTIME\_20MS   4 |
| --- |

## [◆ ](#aad1cc10df9f35d2bb63cb4a3f021152f)TMAG5273\_DT\_SLEEPTIME\_30MS

| #define TMAG5273\_DT\_SLEEPTIME\_30MS   5 |
| --- |

## [◆ ](#afddb082d0306a7858086c4ac227852e0)TMAG5273\_DT\_SLEEPTIME\_5000MS

| #define TMAG5273\_DT\_SLEEPTIME\_5000MS   11 |
| --- |

## [◆ ](#abc58f37d75364d3f8c7c03ee774ed091)TMAG5273\_DT\_SLEEPTIME\_500MS

| #define TMAG5273\_DT\_SLEEPTIME\_500MS   8 |
| --- |

## [◆ ](#a03c1e099cd98b1b09a121bd5c353fc97)TMAG5273\_DT\_SLEEPTIME\_50MS

| #define TMAG5273\_DT\_SLEEPTIME\_50MS   6 |
| --- |

## [◆ ](#ab88e09d09437f57ce31d1ab0f58a19cb)TMAG5273\_DT\_SLEEPTIME\_5MS

| #define TMAG5273\_DT\_SLEEPTIME\_5MS   1 |
| --- |

## [◆ ](#aec27747fbae8c0c62912431a3f9d2309)TMAG5273\_DT\_TEMP\_COEFF\_CERAMIC

| #define TMAG5273\_DT\_TEMP\_COEFF\_CERAMIC   2 |
| --- |

## [◆ ](#af51ec112fe16a5c8a5a55a42dd14fd92)TMAG5273\_DT\_TEMP\_COEFF\_NDBFE

| #define TMAG5273\_DT\_TEMP\_COEFF\_NDBFE   1 |
| --- |

## [◆ ](#a19f4de1abe7275ec75641e5e5ce47826)TMAG5273\_DT\_TEMP\_COEFF\_NONE

| #define TMAG5273\_DT\_TEMP\_COEFF\_NONE   0 |
| --- |

## [◆ ](#ab59755856b8372698deab44d9b8ec9a2)TMAG5273\_DT\_THRX\_ABOVE

| #define TMAG5273\_DT\_THRX\_ABOVE   0 |
| --- |

## [◆ ](#a348bd07ca130ff996bea612ad8cecba3)TMAG5273\_DT\_THRX\_BELOW

| #define TMAG5273\_DT\_THRX\_BELOW   1 |
| --- |

## [◆ ](#a71b6e856b5a5db7af4e4ed0001de2f66)TMAG5273\_DT\_THRX\_COUNT\_1

| #define TMAG5273\_DT\_THRX\_COUNT\_1   0 |
| --- |

## [◆ ](#a3940888f116795a9d060195fdb717ff1)TMAG5273\_DT\_THRX\_COUNT\_4

| #define TMAG5273\_DT\_THRX\_COUNT\_4   1 |
| --- |

## [◆ ](#ac0b966cb05b35abe701b8af474fd0498)TMAG5273\_DT\_THRX\_INSIDE

| #define TMAG5273\_DT\_THRX\_INSIDE   3 |
| --- |

## [◆ ](#a630c77a70f3db408a139dd10b3a28bb1)TMAG5273\_DT\_THRX\_OUTSIDE

| #define TMAG5273\_DT\_THRX\_OUTSIDE   2 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [tmag5273.h](dt-bindings_2sensor_2tmag5273_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
