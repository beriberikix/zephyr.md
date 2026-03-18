---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ra__clock_8h_source.html
original_path: doxygen/html/ra__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra\_clock.h

[Go to the documentation of this file.](ra__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RA\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RA\_H\_

9

[ 10](ra__clock_8h.md#a6df4559dab59308b357cefe023ae89c8)#define RA\_PLL\_SOURCE\_HOCO 0

[ 11](ra__clock_8h.md#aff8b2b7011d5e03b776b806c62e66f6b)#define RA\_PLL\_SOURCE\_MOCO 1

[ 12](ra__clock_8h.md#a1c0b1b77cb18225f4196a1480ae82766)#define RA\_PLL\_SOURCE\_LOCO 2

[ 13](ra__clock_8h.md#a90f8782ed751ad0b35cb21cce4a1716f)#define RA\_PLL\_SOURCE\_MAIN\_OSC 3

[ 14](ra__clock_8h.md#ab77652bdc44562f92f6055414cbc2287)#define RA\_PLL\_SOURCE\_SUBCLOCK 4

[ 15](ra__clock_8h.md#a9e47ee5607c3d6955e75b0e4551dcd15)#define RA\_PLL\_SOURCE\_DISABLE 0xff

16

[ 17](ra__clock_8h.md#ae35a65177b4142d4f07eddf0ab40df33)#define RA\_CLOCK\_SOURCE\_HOCO 0

[ 18](ra__clock_8h.md#ad42f2504d5b0261ace81597e73911331)#define RA\_CLOCK\_SOURCE\_MOCO 1

[ 19](ra__clock_8h.md#ad0ce2791d94bc68af24f63c1cc67ff73)#define RA\_CLOCK\_SOURCE\_LOCO 2

[ 20](ra__clock_8h.md#a5567912f07ea0a24d76d55bd8dbad9cf)#define RA\_CLOCK\_SOURCE\_MAIN\_OSC 3

[ 21](ra__clock_8h.md#a517cd2b1a890211a735bdeaef6142530)#define RA\_CLOCK\_SOURCE\_SUBCLOCK 4

[ 22](ra__clock_8h.md#a4bb52320b850e14029174b7746c61b54)#define RA\_CLOCK\_SOURCE\_PLL 5

[ 23](ra__clock_8h.md#a3b0150622e2a1c9da9bb1da8e942cca9)#define RA\_CLOCK\_SOURCE\_PLL1P RA\_CLOCK\_SOURCE\_PLL

[ 24](ra__clock_8h.md#aca4f5f2379035e4a1dee3df18afdcb9e)#define RA\_CLOCK\_SOURCE\_PLL2 6

[ 25](ra__clock_8h.md#ae5bec436b24ae74026243f8e7665fbd7)#define RA\_CLOCK\_SOURCE\_PLL2P RA\_CLOCK\_SOURCE\_PLL2

[ 26](ra__clock_8h.md#a66422a2f5b337e32f18ab57d18a78e5b)#define RA\_CLOCK\_SOURCE\_PLL1Q 7

[ 27](ra__clock_8h.md#a7eea05b974e849a408ca9019a1debfda)#define RA\_CLOCK\_SOURCE\_PLL1R 8

[ 28](ra__clock_8h.md#aee05df1e5a2c648055373d49990569e3)#define RA\_CLOCK\_SOURCE\_PLL2Q 9

[ 29](ra__clock_8h.md#a1cb8309a816e6409bcb75039fab6b0f5)#define RA\_CLOCK\_SOURCE\_PLL2R 10

[ 30](ra__clock_8h.md#abbc0d942ce24748d3263e7ec02910d94)#define RA\_CLOCK\_SOURCE\_DISABLE 0xff

31

[ 32](ra__clock_8h.md#aae1e2cd401d2480d1abff8b0bda591ed)#define RA\_SYS\_CLOCK\_DIV\_1 0

[ 33](ra__clock_8h.md#a38607259c5f2182938a56a99becb4c4e)#define RA\_SYS\_CLOCK\_DIV\_2 1

[ 34](ra__clock_8h.md#a178331022231b6cb616855d7459c6980)#define RA\_SYS\_CLOCK\_DIV\_4 2

[ 35](ra__clock_8h.md#a96c3aa19c6dadfdfeec1d086cdcc3d2c)#define RA\_SYS\_CLOCK\_DIV\_8 3

[ 36](ra__clock_8h.md#afe31f97422a1776552c24a525ac516e6)#define RA\_SYS\_CLOCK\_DIV\_16 4

[ 37](ra__clock_8h.md#a49b424d172df6218f379f63bcca4244f)#define RA\_SYS\_CLOCK\_DIV\_32 5

[ 38](ra__clock_8h.md#ad09b79222fa40fdb315e631a6ec96db9)#define RA\_SYS\_CLOCK\_DIV\_64 6

[ 39](ra__clock_8h.md#a4e73c7a5c69137975b9e0ed9c7fbc1fd)#define RA\_SYS\_CLOCK\_DIV\_128 7 /\* available for CLKOUT only \*/

[ 40](ra__clock_8h.md#a63fb703d984f2df30cc6eff1cd89a9f2)#define RA\_SYS\_CLOCK\_DIV\_3 8

[ 41](ra__clock_8h.md#a93c19762ebbc81c502098348ad751891)#define RA\_SYS\_CLOCK\_DIV\_6 9

[ 42](ra__clock_8h.md#aa93ea7cec9f299c0d048af15fd0cefdf)#define RA\_SYS\_CLOCK\_DIV\_12 10

43

44/\* PLL divider options. \*/

[ 45](ra__clock_8h.md#a046126abddf50ea207c05df75fa6c68c)#define RA\_PLL\_DIV\_1 0

[ 46](ra__clock_8h.md#a2aa987b52f259c49d4d6f05b8c8bc4b7)#define RA\_PLL\_DIV\_2 1

[ 47](ra__clock_8h.md#a2d914720a2384eb9862099d130fded28)#define RA\_PLL\_DIV\_3 2

[ 48](ra__clock_8h.md#ae09fdfd3db62b395337e5a3710eb3b3e)#define RA\_PLL\_DIV\_4 3

[ 49](ra__clock_8h.md#a9e8c825a10243c5034693af3fc355548)#define RA\_PLL\_DIV\_5 4

[ 50](ra__clock_8h.md#a30ae1f54fe31e2f698c5c64838bb4283)#define RA\_PLL\_DIV\_6 5

[ 51](ra__clock_8h.md#afb613fe17569a95716313d692f31266c)#define RA\_PLL\_DIV\_8 7

[ 52](ra__clock_8h.md#a5edfa3185e26bff4b5eadfa8a26f206c)#define RA\_PLL\_DIV\_9 8

[ 53](ra__clock_8h.md#a462c23c3e245dc805e733b21f80e11e3)#define RA\_PLL\_DIV\_16 15

54

55/\* USB clock divider options. \*/

[ 56](ra__clock_8h.md#adfd6bc03cc7f69fbcf4db1e0e2a023a9)#define RA\_USB\_CLOCK\_DIV\_1 0

[ 57](ra__clock_8h.md#ae578f652d03eba790e2d3a5bb4d76278)#define RA\_USB\_CLOCK\_DIV\_2 1

[ 58](ra__clock_8h.md#ae809900343836e4cfed4a6deb44302e3)#define RA\_USB\_CLOCK\_DIV\_3 2

[ 59](ra__clock_8h.md#afe08b7b4322d08571efcc9669ccb7186)#define RA\_USB\_CLOCK\_DIV\_4 3

[ 60](ra__clock_8h.md#a9cbcc6afc38af571d411b152f67b4758)#define RA\_USB\_CLOCK\_DIV\_5 4

[ 61](ra__clock_8h.md#ac7ad5cec29753c7ded9f85a93050e177)#define RA\_USB\_CLOCK\_DIV\_6 5

[ 62](ra__clock_8h.md#af209617942121a0daf7527cab6516ec3)#define RA\_USB\_CLOCK\_DIV\_8 7

63

64/\* USB60 clock divider options. \*/

[ 65](ra__clock_8h.md#a046b490274c8f5b93f36b3ad5385e097)#define RA\_USB60\_CLOCK\_DIV\_1 0

[ 66](ra__clock_8h.md#a7fd36b4211873e0b50f8c9b9c959b50b)#define RA\_USB60\_CLOCK\_DIV\_2 1

[ 67](ra__clock_8h.md#af5530c8446920e6f59396f1285d05f24)#define RA\_USB60\_CLOCK\_DIV\_3 5

[ 68](ra__clock_8h.md#a45c3f796b41f42cee1172e274dcbf7b0)#define RA\_USB60\_CLOCK\_DIV\_4 2

[ 69](ra__clock_8h.md#a72394db1de5e527c518e902f39edee35)#define RA\_USB60\_CLOCK\_DIV\_5 6

[ 70](ra__clock_8h.md#adcfd9d314bc1fb3d026054610447a591)#define RA\_USB60\_CLOCK\_DIV\_6 3

[ 71](ra__clock_8h.md#a70fb43dad2deda929e59572943a7aafa)#define RA\_USB60\_CLOCK\_DIV\_8 4

72

73/\* OCTA clock divider options. \*/

[ 74](ra__clock_8h.md#a63f16703f2b7ecb717e11d19aad7eb56)#define RA\_OCTA\_CLOCK\_DIV\_1 0

[ 75](ra__clock_8h.md#a6bb15aaf847b154b918d2d8e420f9df0)#define RA\_OCTA\_CLOCK\_DIV\_2 1

[ 76](ra__clock_8h.md#a0915b140bd8267f0f427d15718e42873)#define RA\_OCTA\_CLOCK\_DIV\_4 2

[ 77](ra__clock_8h.md#a54aee624cce8b4e909361997356447ce)#define RA\_OCTA\_CLOCK\_DIV\_6 3

[ 78](ra__clock_8h.md#a82e601378259824c1f0fda94f5ce5012)#define RA\_OCTA\_CLOCK\_DIV\_8 4

79

80/\* CANFD clock divider options. \*/

[ 81](ra__clock_8h.md#a9ba0a95f94486b4c8f7cbda2030ceaf6)#define RA\_CANFD\_CLOCK\_DIV\_1 0

[ 82](ra__clock_8h.md#abcf12b01cb9ab3cd7f18cd6b0ea7f23e)#define RA\_CANFD\_CLOCK\_DIV\_2 1

[ 83](ra__clock_8h.md#a84559895052e982ff3755ded12db5552)#define RA\_CANFD\_CLOCK\_DIV\_3 5

[ 84](ra__clock_8h.md#a1e83d9c2d2b8d031450a3f8650f2421c)#define RA\_CANFD\_CLOCK\_DIV\_4 2

[ 85](ra__clock_8h.md#ade1466385f49ef834f545bcb2a2100c0)#define RA\_CANFD\_CLOCK\_DIV\_5 6

[ 86](ra__clock_8h.md#a20569f5237d82417567e68d434fdf622)#define RA\_CANFD\_CLOCK\_DIV\_6 3

[ 87](ra__clock_8h.md#a20f623493bce3ee2c69449039bf94ece)#define RA\_CANFD\_CLOCK\_DIV\_8 4

88

89/\* SCI clock divider options. \*/

[ 90](ra__clock_8h.md#a96d8751a01cec675ab69b367d452ac4d)#define RA\_SCI\_CLOCK\_DIV\_1 0

[ 91](ra__clock_8h.md#ad1fb8b58a27e72ca19779e3aee760b9e)#define RA\_SCI\_CLOCK\_DIV\_2 1

[ 92](ra__clock_8h.md#a335127adc0d43fdcf1c59929a04470f4)#define RA\_SCI\_CLOCK\_DIV\_3 5

[ 93](ra__clock_8h.md#a837945005b5a8e654b94cdd510d3e997)#define RA\_SCI\_CLOCK\_DIV\_4 2

[ 94](ra__clock_8h.md#aecf92d04cdb2a692985cc9ad836776d4)#define RA\_SCI\_CLOCK\_DIV\_5 6

[ 95](ra__clock_8h.md#ac7b0bd11959c349a904709d6b4b88ed7)#define RA\_SCI\_CLOCK\_DIV\_6 3

[ 96](ra__clock_8h.md#a526e4a031d9a815be975512beebe2b5a)#define RA\_SCI\_CLOCK\_DIV\_8 4

97

98/\* SPI clock divider options. \*/

[ 99](ra__clock_8h.md#ae66b1e285ffc091c03fcae5ed8b7a07d)#define RA\_SPI\_CLOCK\_DIV\_1 0

[ 100](ra__clock_8h.md#aa5882b4f686b67d95a0b5f687a33977e)#define RA\_SPI\_CLOCK\_DIV\_2 1

[ 101](ra__clock_8h.md#a170314872a1190353dd98d6c1f75151e)#define RA\_SPI\_CLOCK\_DIV\_3 5

[ 102](ra__clock_8h.md#adde8606c62fe8e185e003ccc3016827d)#define RA\_SPI\_CLOCK\_DIV\_4 2

[ 103](ra__clock_8h.md#ab38acb26566f19b4092d616d62586e6d)#define RA\_SPI\_CLOCK\_DIV\_5 6

[ 104](ra__clock_8h.md#a2090654df8c6abe43b6595facca7505f)#define RA\_SPI\_CLOCK\_DIV\_6 3

[ 105](ra__clock_8h.md#a9f6a031ba5b0c38ae53821f385890316)#define RA\_SPI\_CLOCK\_DIV\_8 4

106

107/\* CEC clock divider options. \*/

[ 108](ra__clock_8h.md#ac1b3ef7fbe307c7c7c92402eb7580772)#define RA\_CEC\_CLOCK\_DIV\_1 0

[ 109](ra__clock_8h.md#a9e5d72530c66a972babd3bfe60ff870e)#define RA\_CEC\_CLOCK\_DIV\_2 1

110

111/\* I3C clock divider options. \*/

[ 112](ra__clock_8h.md#a452d0d3cec46233af1689bc52f230ba6)#define RA\_I3C\_CLOCK\_DIV\_1 0

[ 113](ra__clock_8h.md#a863e8185df35e7b3ec0cbfc46a941882)#define RA\_I3C\_CLOCK\_DIV\_2 1

[ 114](ra__clock_8h.md#ae3776ace31e13c119cf7d3a788d81c75)#define RA\_I3C\_CLOCK\_DIV\_3 5

[ 115](ra__clock_8h.md#ac2669c765998063a4cead50fb4964faf)#define RA\_I3C\_CLOCK\_DIV\_4 2

[ 116](ra__clock_8h.md#a8eb82f6e626430439b83ee5fc3f46b89)#define RA\_I3C\_CLOCK\_DIV\_5 6

[ 117](ra__clock_8h.md#ac2f503b05bf4562734b305843b2920ac)#define RA\_I3C\_CLOCK\_DIV\_6 3

[ 118](ra__clock_8h.md#a88ca992c47154accf6ad200d711f93af)#define RA\_I3C\_CLOCK\_DIV\_8 4

119

120#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [ra\_clock.h](ra__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
