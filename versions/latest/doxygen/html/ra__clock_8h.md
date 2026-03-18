---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ra__clock_8h.html
original_path: doxygen/html/ra__clock_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra\_clock.h File Reference

[Go to the source code of this file.](ra__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RA\_PLL\_SOURCE\_HOCO](#a6df4559dab59308b357cefe023ae89c8)   0 |
| #define | [RA\_PLL\_SOURCE\_MOCO](#aff8b2b7011d5e03b776b806c62e66f6b)   1 |
| #define | [RA\_PLL\_SOURCE\_LOCO](#a1c0b1b77cb18225f4196a1480ae82766)   2 |
| #define | [RA\_PLL\_SOURCE\_MAIN\_OSC](#a90f8782ed751ad0b35cb21cce4a1716f)   3 |
| #define | [RA\_PLL\_SOURCE\_SUBCLOCK](#ab77652bdc44562f92f6055414cbc2287)   4 |
| #define | [RA\_PLL\_SOURCE\_DISABLE](#a9e47ee5607c3d6955e75b0e4551dcd15)   0xff |
| #define | [RA\_CLOCK\_SOURCE\_HOCO](#ae35a65177b4142d4f07eddf0ab40df33)   0 |
| #define | [RA\_CLOCK\_SOURCE\_MOCO](#ad42f2504d5b0261ace81597e73911331)   1 |
| #define | [RA\_CLOCK\_SOURCE\_LOCO](#ad0ce2791d94bc68af24f63c1cc67ff73)   2 |
| #define | [RA\_CLOCK\_SOURCE\_MAIN\_OSC](#a5567912f07ea0a24d76d55bd8dbad9cf)   3 |
| #define | [RA\_CLOCK\_SOURCE\_SUBCLOCK](#a517cd2b1a890211a735bdeaef6142530)   4 |
| #define | [RA\_CLOCK\_SOURCE\_PLL](#a4bb52320b850e14029174b7746c61b54)   5 |
| #define | [RA\_CLOCK\_SOURCE\_PLL1P](#a3b0150622e2a1c9da9bb1da8e942cca9)   [RA\_CLOCK\_SOURCE\_PLL](#a4bb52320b850e14029174b7746c61b54) |
| #define | [RA\_CLOCK\_SOURCE\_PLL2](#aca4f5f2379035e4a1dee3df18afdcb9e)   6 |
| #define | [RA\_CLOCK\_SOURCE\_PLL2P](#ae5bec436b24ae74026243f8e7665fbd7)   [RA\_CLOCK\_SOURCE\_PLL2](#aca4f5f2379035e4a1dee3df18afdcb9e) |
| #define | [RA\_CLOCK\_SOURCE\_PLL1Q](#a66422a2f5b337e32f18ab57d18a78e5b)   7 |
| #define | [RA\_CLOCK\_SOURCE\_PLL1R](#a7eea05b974e849a408ca9019a1debfda)   8 |
| #define | [RA\_CLOCK\_SOURCE\_PLL2Q](#aee05df1e5a2c648055373d49990569e3)   9 |
| #define | [RA\_CLOCK\_SOURCE\_PLL2R](#a1cb8309a816e6409bcb75039fab6b0f5)   10 |
| #define | [RA\_CLOCK\_SOURCE\_DISABLE](#abbc0d942ce24748d3263e7ec02910d94)   0xff |
| #define | [RA\_SYS\_CLOCK\_DIV\_1](#aae1e2cd401d2480d1abff8b0bda591ed)   0 |
| #define | [RA\_SYS\_CLOCK\_DIV\_2](#a38607259c5f2182938a56a99becb4c4e)   1 |
| #define | [RA\_SYS\_CLOCK\_DIV\_4](#a178331022231b6cb616855d7459c6980)   2 |
| #define | [RA\_SYS\_CLOCK\_DIV\_8](#a96c3aa19c6dadfdfeec1d086cdcc3d2c)   3 |
| #define | [RA\_SYS\_CLOCK\_DIV\_16](#afe31f97422a1776552c24a525ac516e6)   4 |
| #define | [RA\_SYS\_CLOCK\_DIV\_32](#a49b424d172df6218f379f63bcca4244f)   5 |
| #define | [RA\_SYS\_CLOCK\_DIV\_64](#ad09b79222fa40fdb315e631a6ec96db9)   6 |
| #define | [RA\_SYS\_CLOCK\_DIV\_128](#a4e73c7a5c69137975b9e0ed9c7fbc1fd)   7 /\* available for CLKOUT only \*/ |
| #define | [RA\_SYS\_CLOCK\_DIV\_3](#a63fb703d984f2df30cc6eff1cd89a9f2)   8 |
| #define | [RA\_SYS\_CLOCK\_DIV\_6](#a93c19762ebbc81c502098348ad751891)   9 |
| #define | [RA\_SYS\_CLOCK\_DIV\_12](#aa93ea7cec9f299c0d048af15fd0cefdf)   10 |
| #define | [RA\_PLL\_DIV\_1](#a046126abddf50ea207c05df75fa6c68c)   0 |
| #define | [RA\_PLL\_DIV\_2](#a2aa987b52f259c49d4d6f05b8c8bc4b7)   1 |
| #define | [RA\_PLL\_DIV\_3](#a2d914720a2384eb9862099d130fded28)   2 |
| #define | [RA\_PLL\_DIV\_4](#ae09fdfd3db62b395337e5a3710eb3b3e)   3 |
| #define | [RA\_PLL\_DIV\_5](#a9e8c825a10243c5034693af3fc355548)   4 |
| #define | [RA\_PLL\_DIV\_6](#a30ae1f54fe31e2f698c5c64838bb4283)   5 |
| #define | [RA\_PLL\_DIV\_8](#afb613fe17569a95716313d692f31266c)   7 |
| #define | [RA\_PLL\_DIV\_9](#a5edfa3185e26bff4b5eadfa8a26f206c)   8 |
| #define | [RA\_PLL\_DIV\_16](#a462c23c3e245dc805e733b21f80e11e3)   15 |
| #define | [RA\_USB\_CLOCK\_DIV\_1](#adfd6bc03cc7f69fbcf4db1e0e2a023a9)   0 |
| #define | [RA\_USB\_CLOCK\_DIV\_2](#ae578f652d03eba790e2d3a5bb4d76278)   1 |
| #define | [RA\_USB\_CLOCK\_DIV\_3](#ae809900343836e4cfed4a6deb44302e3)   2 |
| #define | [RA\_USB\_CLOCK\_DIV\_4](#afe08b7b4322d08571efcc9669ccb7186)   3 |
| #define | [RA\_USB\_CLOCK\_DIV\_5](#a9cbcc6afc38af571d411b152f67b4758)   4 |
| #define | [RA\_USB\_CLOCK\_DIV\_6](#ac7ad5cec29753c7ded9f85a93050e177)   5 |
| #define | [RA\_USB\_CLOCK\_DIV\_8](#af209617942121a0daf7527cab6516ec3)   7 |
| #define | [RA\_USB60\_CLOCK\_DIV\_1](#a046b490274c8f5b93f36b3ad5385e097)   0 |
| #define | [RA\_USB60\_CLOCK\_DIV\_2](#a7fd36b4211873e0b50f8c9b9c959b50b)   1 |
| #define | [RA\_USB60\_CLOCK\_DIV\_3](#af5530c8446920e6f59396f1285d05f24)   5 |
| #define | [RA\_USB60\_CLOCK\_DIV\_4](#a45c3f796b41f42cee1172e274dcbf7b0)   2 |
| #define | [RA\_USB60\_CLOCK\_DIV\_5](#a72394db1de5e527c518e902f39edee35)   6 |
| #define | [RA\_USB60\_CLOCK\_DIV\_6](#adcfd9d314bc1fb3d026054610447a591)   3 |
| #define | [RA\_USB60\_CLOCK\_DIV\_8](#a70fb43dad2deda929e59572943a7aafa)   4 |
| #define | [RA\_OCTA\_CLOCK\_DIV\_1](#a63f16703f2b7ecb717e11d19aad7eb56)   0 |
| #define | [RA\_OCTA\_CLOCK\_DIV\_2](#a6bb15aaf847b154b918d2d8e420f9df0)   1 |
| #define | [RA\_OCTA\_CLOCK\_DIV\_4](#a0915b140bd8267f0f427d15718e42873)   2 |
| #define | [RA\_OCTA\_CLOCK\_DIV\_6](#a54aee624cce8b4e909361997356447ce)   3 |
| #define | [RA\_OCTA\_CLOCK\_DIV\_8](#a82e601378259824c1f0fda94f5ce5012)   4 |
| #define | [RA\_CANFD\_CLOCK\_DIV\_1](#a9ba0a95f94486b4c8f7cbda2030ceaf6)   0 |
| #define | [RA\_CANFD\_CLOCK\_DIV\_2](#abcf12b01cb9ab3cd7f18cd6b0ea7f23e)   1 |
| #define | [RA\_CANFD\_CLOCK\_DIV\_3](#a84559895052e982ff3755ded12db5552)   5 |
| #define | [RA\_CANFD\_CLOCK\_DIV\_4](#a1e83d9c2d2b8d031450a3f8650f2421c)   2 |
| #define | [RA\_CANFD\_CLOCK\_DIV\_5](#ade1466385f49ef834f545bcb2a2100c0)   6 |
| #define | [RA\_CANFD\_CLOCK\_DIV\_6](#a20569f5237d82417567e68d434fdf622)   3 |
| #define | [RA\_CANFD\_CLOCK\_DIV\_8](#a20f623493bce3ee2c69449039bf94ece)   4 |
| #define | [RA\_SCI\_CLOCK\_DIV\_1](#a96d8751a01cec675ab69b367d452ac4d)   0 |
| #define | [RA\_SCI\_CLOCK\_DIV\_2](#ad1fb8b58a27e72ca19779e3aee760b9e)   1 |
| #define | [RA\_SCI\_CLOCK\_DIV\_3](#a335127adc0d43fdcf1c59929a04470f4)   5 |
| #define | [RA\_SCI\_CLOCK\_DIV\_4](#a837945005b5a8e654b94cdd510d3e997)   2 |
| #define | [RA\_SCI\_CLOCK\_DIV\_5](#aecf92d04cdb2a692985cc9ad836776d4)   6 |
| #define | [RA\_SCI\_CLOCK\_DIV\_6](#ac7b0bd11959c349a904709d6b4b88ed7)   3 |
| #define | [RA\_SCI\_CLOCK\_DIV\_8](#a526e4a031d9a815be975512beebe2b5a)   4 |
| #define | [RA\_SPI\_CLOCK\_DIV\_1](#ae66b1e285ffc091c03fcae5ed8b7a07d)   0 |
| #define | [RA\_SPI\_CLOCK\_DIV\_2](#aa5882b4f686b67d95a0b5f687a33977e)   1 |
| #define | [RA\_SPI\_CLOCK\_DIV\_3](#a170314872a1190353dd98d6c1f75151e)   5 |
| #define | [RA\_SPI\_CLOCK\_DIV\_4](#adde8606c62fe8e185e003ccc3016827d)   2 |
| #define | [RA\_SPI\_CLOCK\_DIV\_5](#ab38acb26566f19b4092d616d62586e6d)   6 |
| #define | [RA\_SPI\_CLOCK\_DIV\_6](#a2090654df8c6abe43b6595facca7505f)   3 |
| #define | [RA\_SPI\_CLOCK\_DIV\_8](#a9f6a031ba5b0c38ae53821f385890316)   4 |
| #define | [RA\_CEC\_CLOCK\_DIV\_1](#ac1b3ef7fbe307c7c7c92402eb7580772)   0 |
| #define | [RA\_CEC\_CLOCK\_DIV\_2](#a9e5d72530c66a972babd3bfe60ff870e)   1 |
| #define | [RA\_I3C\_CLOCK\_DIV\_1](#a452d0d3cec46233af1689bc52f230ba6)   0 |
| #define | [RA\_I3C\_CLOCK\_DIV\_2](#a863e8185df35e7b3ec0cbfc46a941882)   1 |
| #define | [RA\_I3C\_CLOCK\_DIV\_3](#ae3776ace31e13c119cf7d3a788d81c75)   5 |
| #define | [RA\_I3C\_CLOCK\_DIV\_4](#ac2669c765998063a4cead50fb4964faf)   2 |
| #define | [RA\_I3C\_CLOCK\_DIV\_5](#a8eb82f6e626430439b83ee5fc3f46b89)   6 |
| #define | [RA\_I3C\_CLOCK\_DIV\_6](#ac2f503b05bf4562734b305843b2920ac)   3 |
| #define | [RA\_I3C\_CLOCK\_DIV\_8](#a88ca992c47154accf6ad200d711f93af)   4 |

## Macro Definition Documentation

## [◆ ](#a9ba0a95f94486b4c8f7cbda2030ceaf6)RA\_CANFD\_CLOCK\_DIV\_1

| #define RA\_CANFD\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#abcf12b01cb9ab3cd7f18cd6b0ea7f23e)RA\_CANFD\_CLOCK\_DIV\_2

| #define RA\_CANFD\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#a84559895052e982ff3755ded12db5552)RA\_CANFD\_CLOCK\_DIV\_3

| #define RA\_CANFD\_CLOCK\_DIV\_3   5 |
| --- |

## [◆ ](#a1e83d9c2d2b8d031450a3f8650f2421c)RA\_CANFD\_CLOCK\_DIV\_4

| #define RA\_CANFD\_CLOCK\_DIV\_4   2 |
| --- |

## [◆ ](#ade1466385f49ef834f545bcb2a2100c0)RA\_CANFD\_CLOCK\_DIV\_5

| #define RA\_CANFD\_CLOCK\_DIV\_5   6 |
| --- |

## [◆ ](#a20569f5237d82417567e68d434fdf622)RA\_CANFD\_CLOCK\_DIV\_6

| #define RA\_CANFD\_CLOCK\_DIV\_6   3 |
| --- |

## [◆ ](#a20f623493bce3ee2c69449039bf94ece)RA\_CANFD\_CLOCK\_DIV\_8

| #define RA\_CANFD\_CLOCK\_DIV\_8   4 |
| --- |

## [◆ ](#ac1b3ef7fbe307c7c7c92402eb7580772)RA\_CEC\_CLOCK\_DIV\_1

| #define RA\_CEC\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#a9e5d72530c66a972babd3bfe60ff870e)RA\_CEC\_CLOCK\_DIV\_2

| #define RA\_CEC\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#abbc0d942ce24748d3263e7ec02910d94)RA\_CLOCK\_SOURCE\_DISABLE

| #define RA\_CLOCK\_SOURCE\_DISABLE   0xff |
| --- |

## [◆ ](#ae35a65177b4142d4f07eddf0ab40df33)RA\_CLOCK\_SOURCE\_HOCO

| #define RA\_CLOCK\_SOURCE\_HOCO   0 |
| --- |

## [◆ ](#ad0ce2791d94bc68af24f63c1cc67ff73)RA\_CLOCK\_SOURCE\_LOCO

| #define RA\_CLOCK\_SOURCE\_LOCO   2 |
| --- |

## [◆ ](#a5567912f07ea0a24d76d55bd8dbad9cf)RA\_CLOCK\_SOURCE\_MAIN\_OSC

| #define RA\_CLOCK\_SOURCE\_MAIN\_OSC   3 |
| --- |

## [◆ ](#ad42f2504d5b0261ace81597e73911331)RA\_CLOCK\_SOURCE\_MOCO

| #define RA\_CLOCK\_SOURCE\_MOCO   1 |
| --- |

## [◆ ](#a4bb52320b850e14029174b7746c61b54)RA\_CLOCK\_SOURCE\_PLL

| #define RA\_CLOCK\_SOURCE\_PLL   5 |
| --- |

## [◆ ](#a3b0150622e2a1c9da9bb1da8e942cca9)RA\_CLOCK\_SOURCE\_PLL1P

| #define RA\_CLOCK\_SOURCE\_PLL1P   [RA\_CLOCK\_SOURCE\_PLL](#a4bb52320b850e14029174b7746c61b54) |
| --- |

## [◆ ](#a66422a2f5b337e32f18ab57d18a78e5b)RA\_CLOCK\_SOURCE\_PLL1Q

| #define RA\_CLOCK\_SOURCE\_PLL1Q   7 |
| --- |

## [◆ ](#a7eea05b974e849a408ca9019a1debfda)RA\_CLOCK\_SOURCE\_PLL1R

| #define RA\_CLOCK\_SOURCE\_PLL1R   8 |
| --- |

## [◆ ](#aca4f5f2379035e4a1dee3df18afdcb9e)RA\_CLOCK\_SOURCE\_PLL2

| #define RA\_CLOCK\_SOURCE\_PLL2   6 |
| --- |

## [◆ ](#ae5bec436b24ae74026243f8e7665fbd7)RA\_CLOCK\_SOURCE\_PLL2P

| #define RA\_CLOCK\_SOURCE\_PLL2P   [RA\_CLOCK\_SOURCE\_PLL2](#aca4f5f2379035e4a1dee3df18afdcb9e) |
| --- |

## [◆ ](#aee05df1e5a2c648055373d49990569e3)RA\_CLOCK\_SOURCE\_PLL2Q

| #define RA\_CLOCK\_SOURCE\_PLL2Q   9 |
| --- |

## [◆ ](#a1cb8309a816e6409bcb75039fab6b0f5)RA\_CLOCK\_SOURCE\_PLL2R

| #define RA\_CLOCK\_SOURCE\_PLL2R   10 |
| --- |

## [◆ ](#a517cd2b1a890211a735bdeaef6142530)RA\_CLOCK\_SOURCE\_SUBCLOCK

| #define RA\_CLOCK\_SOURCE\_SUBCLOCK   4 |
| --- |

## [◆ ](#a452d0d3cec46233af1689bc52f230ba6)RA\_I3C\_CLOCK\_DIV\_1

| #define RA\_I3C\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#a863e8185df35e7b3ec0cbfc46a941882)RA\_I3C\_CLOCK\_DIV\_2

| #define RA\_I3C\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#ae3776ace31e13c119cf7d3a788d81c75)RA\_I3C\_CLOCK\_DIV\_3

| #define RA\_I3C\_CLOCK\_DIV\_3   5 |
| --- |

## [◆ ](#ac2669c765998063a4cead50fb4964faf)RA\_I3C\_CLOCK\_DIV\_4

| #define RA\_I3C\_CLOCK\_DIV\_4   2 |
| --- |

## [◆ ](#a8eb82f6e626430439b83ee5fc3f46b89)RA\_I3C\_CLOCK\_DIV\_5

| #define RA\_I3C\_CLOCK\_DIV\_5   6 |
| --- |

## [◆ ](#ac2f503b05bf4562734b305843b2920ac)RA\_I3C\_CLOCK\_DIV\_6

| #define RA\_I3C\_CLOCK\_DIV\_6   3 |
| --- |

## [◆ ](#a88ca992c47154accf6ad200d711f93af)RA\_I3C\_CLOCK\_DIV\_8

| #define RA\_I3C\_CLOCK\_DIV\_8   4 |
| --- |

## [◆ ](#a63f16703f2b7ecb717e11d19aad7eb56)RA\_OCTA\_CLOCK\_DIV\_1

| #define RA\_OCTA\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#a6bb15aaf847b154b918d2d8e420f9df0)RA\_OCTA\_CLOCK\_DIV\_2

| #define RA\_OCTA\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#a0915b140bd8267f0f427d15718e42873)RA\_OCTA\_CLOCK\_DIV\_4

| #define RA\_OCTA\_CLOCK\_DIV\_4   2 |
| --- |

## [◆ ](#a54aee624cce8b4e909361997356447ce)RA\_OCTA\_CLOCK\_DIV\_6

| #define RA\_OCTA\_CLOCK\_DIV\_6   3 |
| --- |

## [◆ ](#a82e601378259824c1f0fda94f5ce5012)RA\_OCTA\_CLOCK\_DIV\_8

| #define RA\_OCTA\_CLOCK\_DIV\_8   4 |
| --- |

## [◆ ](#a046126abddf50ea207c05df75fa6c68c)RA\_PLL\_DIV\_1

| #define RA\_PLL\_DIV\_1   0 |
| --- |

## [◆ ](#a462c23c3e245dc805e733b21f80e11e3)RA\_PLL\_DIV\_16

| #define RA\_PLL\_DIV\_16   15 |
| --- |

## [◆ ](#a2aa987b52f259c49d4d6f05b8c8bc4b7)RA\_PLL\_DIV\_2

| #define RA\_PLL\_DIV\_2   1 |
| --- |

## [◆ ](#a2d914720a2384eb9862099d130fded28)RA\_PLL\_DIV\_3

| #define RA\_PLL\_DIV\_3   2 |
| --- |

## [◆ ](#ae09fdfd3db62b395337e5a3710eb3b3e)RA\_PLL\_DIV\_4

| #define RA\_PLL\_DIV\_4   3 |
| --- |

## [◆ ](#a9e8c825a10243c5034693af3fc355548)RA\_PLL\_DIV\_5

| #define RA\_PLL\_DIV\_5   4 |
| --- |

## [◆ ](#a30ae1f54fe31e2f698c5c64838bb4283)RA\_PLL\_DIV\_6

| #define RA\_PLL\_DIV\_6   5 |
| --- |

## [◆ ](#afb613fe17569a95716313d692f31266c)RA\_PLL\_DIV\_8

| #define RA\_PLL\_DIV\_8   7 |
| --- |

## [◆ ](#a5edfa3185e26bff4b5eadfa8a26f206c)RA\_PLL\_DIV\_9

| #define RA\_PLL\_DIV\_9   8 |
| --- |

## [◆ ](#a9e47ee5607c3d6955e75b0e4551dcd15)RA\_PLL\_SOURCE\_DISABLE

| #define RA\_PLL\_SOURCE\_DISABLE   0xff |
| --- |

## [◆ ](#a6df4559dab59308b357cefe023ae89c8)RA\_PLL\_SOURCE\_HOCO

| #define RA\_PLL\_SOURCE\_HOCO   0 |
| --- |

## [◆ ](#a1c0b1b77cb18225f4196a1480ae82766)RA\_PLL\_SOURCE\_LOCO

| #define RA\_PLL\_SOURCE\_LOCO   2 |
| --- |

## [◆ ](#a90f8782ed751ad0b35cb21cce4a1716f)RA\_PLL\_SOURCE\_MAIN\_OSC

| #define RA\_PLL\_SOURCE\_MAIN\_OSC   3 |
| --- |

## [◆ ](#aff8b2b7011d5e03b776b806c62e66f6b)RA\_PLL\_SOURCE\_MOCO

| #define RA\_PLL\_SOURCE\_MOCO   1 |
| --- |

## [◆ ](#ab77652bdc44562f92f6055414cbc2287)RA\_PLL\_SOURCE\_SUBCLOCK

| #define RA\_PLL\_SOURCE\_SUBCLOCK   4 |
| --- |

## [◆ ](#a96d8751a01cec675ab69b367d452ac4d)RA\_SCI\_CLOCK\_DIV\_1

| #define RA\_SCI\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#ad1fb8b58a27e72ca19779e3aee760b9e)RA\_SCI\_CLOCK\_DIV\_2

| #define RA\_SCI\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#a335127adc0d43fdcf1c59929a04470f4)RA\_SCI\_CLOCK\_DIV\_3

| #define RA\_SCI\_CLOCK\_DIV\_3   5 |
| --- |

## [◆ ](#a837945005b5a8e654b94cdd510d3e997)RA\_SCI\_CLOCK\_DIV\_4

| #define RA\_SCI\_CLOCK\_DIV\_4   2 |
| --- |

## [◆ ](#aecf92d04cdb2a692985cc9ad836776d4)RA\_SCI\_CLOCK\_DIV\_5

| #define RA\_SCI\_CLOCK\_DIV\_5   6 |
| --- |

## [◆ ](#ac7b0bd11959c349a904709d6b4b88ed7)RA\_SCI\_CLOCK\_DIV\_6

| #define RA\_SCI\_CLOCK\_DIV\_6   3 |
| --- |

## [◆ ](#a526e4a031d9a815be975512beebe2b5a)RA\_SCI\_CLOCK\_DIV\_8

| #define RA\_SCI\_CLOCK\_DIV\_8   4 |
| --- |

## [◆ ](#ae66b1e285ffc091c03fcae5ed8b7a07d)RA\_SPI\_CLOCK\_DIV\_1

| #define RA\_SPI\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#aa5882b4f686b67d95a0b5f687a33977e)RA\_SPI\_CLOCK\_DIV\_2

| #define RA\_SPI\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#a170314872a1190353dd98d6c1f75151e)RA\_SPI\_CLOCK\_DIV\_3

| #define RA\_SPI\_CLOCK\_DIV\_3   5 |
| --- |

## [◆ ](#adde8606c62fe8e185e003ccc3016827d)RA\_SPI\_CLOCK\_DIV\_4

| #define RA\_SPI\_CLOCK\_DIV\_4   2 |
| --- |

## [◆ ](#ab38acb26566f19b4092d616d62586e6d)RA\_SPI\_CLOCK\_DIV\_5

| #define RA\_SPI\_CLOCK\_DIV\_5   6 |
| --- |

## [◆ ](#a2090654df8c6abe43b6595facca7505f)RA\_SPI\_CLOCK\_DIV\_6

| #define RA\_SPI\_CLOCK\_DIV\_6   3 |
| --- |

## [◆ ](#a9f6a031ba5b0c38ae53821f385890316)RA\_SPI\_CLOCK\_DIV\_8

| #define RA\_SPI\_CLOCK\_DIV\_8   4 |
| --- |

## [◆ ](#aae1e2cd401d2480d1abff8b0bda591ed)RA\_SYS\_CLOCK\_DIV\_1

| #define RA\_SYS\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#aa93ea7cec9f299c0d048af15fd0cefdf)RA\_SYS\_CLOCK\_DIV\_12

| #define RA\_SYS\_CLOCK\_DIV\_12   10 |
| --- |

## [◆ ](#a4e73c7a5c69137975b9e0ed9c7fbc1fd)RA\_SYS\_CLOCK\_DIV\_128

| #define RA\_SYS\_CLOCK\_DIV\_128   7 /\* available for CLKOUT only \*/ |
| --- |

## [◆ ](#afe31f97422a1776552c24a525ac516e6)RA\_SYS\_CLOCK\_DIV\_16

| #define RA\_SYS\_CLOCK\_DIV\_16   4 |
| --- |

## [◆ ](#a38607259c5f2182938a56a99becb4c4e)RA\_SYS\_CLOCK\_DIV\_2

| #define RA\_SYS\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#a63fb703d984f2df30cc6eff1cd89a9f2)RA\_SYS\_CLOCK\_DIV\_3

| #define RA\_SYS\_CLOCK\_DIV\_3   8 |
| --- |

## [◆ ](#a49b424d172df6218f379f63bcca4244f)RA\_SYS\_CLOCK\_DIV\_32

| #define RA\_SYS\_CLOCK\_DIV\_32   5 |
| --- |

## [◆ ](#a178331022231b6cb616855d7459c6980)RA\_SYS\_CLOCK\_DIV\_4

| #define RA\_SYS\_CLOCK\_DIV\_4   2 |
| --- |

## [◆ ](#a93c19762ebbc81c502098348ad751891)RA\_SYS\_CLOCK\_DIV\_6

| #define RA\_SYS\_CLOCK\_DIV\_6   9 |
| --- |

## [◆ ](#ad09b79222fa40fdb315e631a6ec96db9)RA\_SYS\_CLOCK\_DIV\_64

| #define RA\_SYS\_CLOCK\_DIV\_64   6 |
| --- |

## [◆ ](#a96c3aa19c6dadfdfeec1d086cdcc3d2c)RA\_SYS\_CLOCK\_DIV\_8

| #define RA\_SYS\_CLOCK\_DIV\_8   3 |
| --- |

## [◆ ](#a046b490274c8f5b93f36b3ad5385e097)RA\_USB60\_CLOCK\_DIV\_1

| #define RA\_USB60\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#a7fd36b4211873e0b50f8c9b9c959b50b)RA\_USB60\_CLOCK\_DIV\_2

| #define RA\_USB60\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#af5530c8446920e6f59396f1285d05f24)RA\_USB60\_CLOCK\_DIV\_3

| #define RA\_USB60\_CLOCK\_DIV\_3   5 |
| --- |

## [◆ ](#a45c3f796b41f42cee1172e274dcbf7b0)RA\_USB60\_CLOCK\_DIV\_4

| #define RA\_USB60\_CLOCK\_DIV\_4   2 |
| --- |

## [◆ ](#a72394db1de5e527c518e902f39edee35)RA\_USB60\_CLOCK\_DIV\_5

| #define RA\_USB60\_CLOCK\_DIV\_5   6 |
| --- |

## [◆ ](#adcfd9d314bc1fb3d026054610447a591)RA\_USB60\_CLOCK\_DIV\_6

| #define RA\_USB60\_CLOCK\_DIV\_6   3 |
| --- |

## [◆ ](#a70fb43dad2deda929e59572943a7aafa)RA\_USB60\_CLOCK\_DIV\_8

| #define RA\_USB60\_CLOCK\_DIV\_8   4 |
| --- |

## [◆ ](#adfd6bc03cc7f69fbcf4db1e0e2a023a9)RA\_USB\_CLOCK\_DIV\_1

| #define RA\_USB\_CLOCK\_DIV\_1   0 |
| --- |

## [◆ ](#ae578f652d03eba790e2d3a5bb4d76278)RA\_USB\_CLOCK\_DIV\_2

| #define RA\_USB\_CLOCK\_DIV\_2   1 |
| --- |

## [◆ ](#ae809900343836e4cfed4a6deb44302e3)RA\_USB\_CLOCK\_DIV\_3

| #define RA\_USB\_CLOCK\_DIV\_3   2 |
| --- |

## [◆ ](#afe08b7b4322d08571efcc9669ccb7186)RA\_USB\_CLOCK\_DIV\_4

| #define RA\_USB\_CLOCK\_DIV\_4   3 |
| --- |

## [◆ ](#a9cbcc6afc38af571d411b152f67b4758)RA\_USB\_CLOCK\_DIV\_5

| #define RA\_USB\_CLOCK\_DIV\_5   4 |
| --- |

## [◆ ](#ac7ad5cec29753c7ded9f85a93050e177)RA\_USB\_CLOCK\_DIV\_6

| #define RA\_USB\_CLOCK\_DIV\_6   5 |
| --- |

## [◆ ](#af209617942121a0daf7527cab6516ec3)RA\_USB\_CLOCK\_DIV\_8

| #define RA\_USB\_CLOCK\_DIV\_8   7 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [ra\_clock.h](ra__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
