---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arc__mpu_8h_source.html
original_path: doxygen/html/arc__mpu_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_mpu.h

[Go to the documentation of this file.](arc__mpu_8h.md)

1/\*

2 \* Copyright (c) 2017 Synopsys.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_MPU\_ARC\_MPU\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_MPU\_ARC\_MPU\_H\_

8

9

10

[ 11](arc__mpu_8h.md#a60ee20e3975aded266f071b5153f1182)#define AUX\_MPU\_ATTR\_UE 0x008 /\* allow user execution \*/

[ 12](arc__mpu_8h.md#af51359c9aec81469777457d74f465e48)#define AUX\_MPU\_ATTR\_UW 0x010 /\* allow user write \*/

[ 13](arc__mpu_8h.md#ab35d3ffeca1f3ca004e3952bd667f017)#define AUX\_MPU\_ATTR\_UR 0x020 /\* allow user read \*/

[ 14](arc__mpu_8h.md#ad5a4cc46b1ebb1e6446ac4c47a73a9e4)#define AUX\_MPU\_ATTR\_KE 0x040 /\* only allow kernel execution \*/

[ 15](arc__mpu_8h.md#af04748698a580d965f022feff3305451)#define AUX\_MPU\_ATTR\_KW 0x080 /\* only allow kernel write \*/

[ 16](arc__mpu_8h.md#a22e4bcde2d658fa56547f33e06528808)#define AUX\_MPU\_ATTR\_KR 0x100 /\* only allow kernel read \*/

[ 17](arc__mpu_8h.md#a5b508144ec92ab7f0fc96849e3ef0825)#define AUX\_MPU\_ATTR\_S 0x8000 /\* secure \*/

[ 18](arc__mpu_8h.md#a03a96c3795cd1aa145f77a26b59812ab)#define AUX\_MPU\_ATTR\_N 0x0000 /\* normal \*/

19

20

21/\*

22 \* a region is dynamic means it can be split into sub regions.

23 \* This attribute is meaningful for ARC MPUv3 which does not support mpu

24 \* entry overlap. For ARC MPUv2, this attribute will be ignored as it

25 \* supports mpu overlap in hardware.

26 \*/

[ 27](arc__mpu_8h.md#a7f1db86633b3dc543e0b697a3f12fa69)#define REGION\_DYNAMIC 0x800 /\* dynamic flag \*/

28

29

30/\* Some helper defines for common regions \*/

31

[ 32](arc__mpu_8h.md#a57e6358e26ba6264bc56328cddbd0aa8)#define REGION\_KERNEL\_RAM\_ATTR \

33 (AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR)

34

[ 35](arc__mpu_8h.md#ad13a9474effb053ddae4a1902b10f114)#define REGION\_KERNEL\_ROM\_ATTR \

36 (AUX\_MPU\_ATTR\_KE | AUX\_MPU\_ATTR\_KR)

37

[ 38](arc__mpu_8h.md#a859d811feecb32c788b16a413e1b4781)#define REGION\_RAM\_ATTR \

39 (AUX\_MPU\_ATTR\_UW | AUX\_MPU\_ATTR\_UR | \

40 AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR)

41

[ 42](arc__mpu_8h.md#a73b0d7c2fe809fe019f5c425917342ef)#define REGION\_ROM\_ATTR \

43 (AUX\_MPU\_ATTR\_UE | AUX\_MPU\_ATTR\_UR | \

44 AUX\_MPU\_ATTR\_KE | AUX\_MPU\_ATTR\_KR)

45

[ 46](arc__mpu_8h.md#a4ce0d123898b8cb22cb161c8d69c411f)#define REGION\_IO\_ATTR \

47 (AUX\_MPU\_ATTR\_UW | AUX\_MPU\_ATTR\_UR | \

48 AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR)

49

[ 50](arc__mpu_8h.md#a377228517c6cac1549a12a8a642c53e3)#define REGION\_ALL\_ATTR \

51 (AUX\_MPU\_ATTR\_UW | AUX\_MPU\_ATTR\_UR | \

52 AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR | \

53 AUX\_MPU\_ATTR\_KE | AUX\_MPU\_ATTR\_UE)

54

55

[ 56](arc__mpu_8h.md#a5cb4dfcb39c8cddde7d00be07abbf186)#define REGION\_32B 0x200

[ 57](arc__mpu_8h.md#af0032361a1f7303ea36d4a78484ed991)#define REGION\_64B 0x201

[ 58](arc__mpu_8h.md#af93290eb28d2d1eafaa1cad375cb994e)#define REGION\_128B 0x202

[ 59](arc__mpu_8h.md#ae4a7b8266e1048e53ab72a96af99dfa9)#define REGION\_256B 0x203

[ 60](arc__mpu_8h.md#abef640d835bc8fe9e49ebb23fed5eacc)#define REGION\_512B 0x400

[ 61](arc__mpu_8h.md#a9216de2e7190dedac57efc79367a6c49)#define REGION\_1K 0x401

[ 62](arc__mpu_8h.md#aa22b0f233ecd96b8097e45260110845e)#define REGION\_2K 0x402

[ 63](arc__mpu_8h.md#a0dd685b0698d16ea2bed3b7ac3038a41)#define REGION\_4K 0x403

[ 64](arc__mpu_8h.md#a0d4b53088d0e9e4e4552c5b4a496731d)#define REGION\_8K 0x600

[ 65](arc__mpu_8h.md#a1f382e52ddd7a8c50571664736cb2b27)#define REGION\_16K 0x601

[ 66](arc__mpu_8h.md#a5354ce614160f66300ac71616f708a61)#define REGION\_32K 0x602

[ 67](arc__mpu_8h.md#ab75ccffbfbc1389e1303bb2415dc7c24)#define REGION\_64K 0x603

[ 68](arc__mpu_8h.md#ab6ee612fe19a00c67fba398da06f6f09)#define REGION\_128K 0x800

[ 69](arc__mpu_8h.md#a8a949eee20d66206a9c700eb68f4a614)#define REGION\_256K 0x801

[ 70](arc__mpu_8h.md#ae5fc1f5ea7a3bbbc85dce33cee2aa85b)#define REGION\_512K 0x802

[ 71](arc__mpu_8h.md#a1ad0013ace85d499c8d554602066c7e1)#define REGION\_1M 0x803

[ 72](arc__mpu_8h.md#a1bc46af188d58128dce0e7f6bf851515)#define REGION\_2M 0xA00

[ 73](arc__mpu_8h.md#a4837e15ddf1dfa198442883d705d5eb1)#define REGION\_4M 0xA01

[ 74](arc__mpu_8h.md#a464e54c991784aed5061b93adcfc387e)#define REGION\_8M 0xA02

[ 75](arc__mpu_8h.md#ace038f88373aec532761c3c4f5193be3)#define REGION\_16M 0xA03

[ 76](arc__mpu_8h.md#a2dacd02f000be694c6e4e1bcfe4e6d6e)#define REGION\_32M 0xC00

[ 77](arc__mpu_8h.md#a66785668a244bc13dd0c5553a68384d2)#define REGION\_64M 0xC01

[ 78](arc__mpu_8h.md#a2f0bf4c7ad62232ed5a185cb65708be0)#define REGION\_128M 0xC02

[ 79](arc__mpu_8h.md#a81428ec21df3db24dee2b09c5f2c3ad5)#define REGION\_256M 0xC03

[ 80](arc__mpu_8h.md#a4f61982635b2ed4099836c61811a8ce6)#define REGION\_512M 0xE00

[ 81](arc__mpu_8h.md#ac959b468a34a1b202e3682f15bcd26fe)#define REGION\_1G 0xE01

[ 82](arc__mpu_8h.md#a97835cec29142060938be2d53438e9f6)#define REGION\_2G 0xE02

[ 83](arc__mpu_8h.md#ac14cdd5594b034fa65f3baf6b2e2bde9)#define REGION\_4G 0xE03

84

85/\* Region definition data structure \*/

[ 86](structarc__mpu__region.md)struct [arc\_mpu\_region](structarc__mpu__region.md) {

87 /\* Region Name \*/

[ 88](structarc__mpu__region.md#a59db0045486098963ca5646c2995374a) const char \*[name](structarc__mpu__region.md#a59db0045486098963ca5646c2995374a);

89 /\* Region Base Address \*/

[ 90](structarc__mpu__region.md#a4d748e5dcec541bf5aca089861cf931c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [base](structarc__mpu__region.md#a4d748e5dcec541bf5aca089861cf931c);

[ 91](structarc__mpu__region.md#a17107d330203fcad8ef8222485a205e9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structarc__mpu__region.md#a17107d330203fcad8ef8222485a205e9);

92 /\* Region Attributes \*/

[ 93](structarc__mpu__region.md#abc3ff764104a4db2d986f30eed370e4a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attr](structarc__mpu__region.md#abc3ff764104a4db2d986f30eed370e4a);

94};

95

[ 96](arc__mpu_8h.md#a10e2e694074c67f95d995679064c067e)#define MPU\_REGION\_ENTRY(\_name, \_base, \_size, \_attr) \

97 {\

98 .name = \_name, \

99 .base = \_base, \

100 .size = \_size, \

101 .attr = \_attr, \

102 }

103

104/\* MPU configuration data structure \*/

[ 105](structarc__mpu__config.md)struct [arc\_mpu\_config](structarc__mpu__config.md) {

106 /\* Number of regions \*/

[ 107](structarc__mpu__config.md#a1310febf88e32ea1638445246d8a38f2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_regions](structarc__mpu__config.md#a1310febf88e32ea1638445246d8a38f2);

108 /\* Regions \*/

[ 109](structarc__mpu__config.md#ad81a6593ea0f7550d9739706267061a1) struct [arc\_mpu\_region](structarc__mpu__region.md) \*[mpu\_regions](structarc__mpu__config.md#ad81a6593ea0f7550d9739706267061a1);

110};

111

112/\* Reference to the MPU configuration \*/

113extern struct [arc\_mpu\_config](structarc__mpu__config.md) [mpu\_config](arc__mpu_8h.md#a347b2bb6c23b874d7a20d4b5ce4d23b1);

114

115#endif /\* \_ARC\_CORE\_MPU\_H\_ \*/

[mpu\_config](arc__mpu_8h.md#a347b2bb6c23b874d7a20d4b5ce4d23b1)

struct arc\_mpu\_config mpu\_config

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arc\_mpu\_config](structarc__mpu__config.md)

**Definition** arc\_mpu.h:105

[arc\_mpu\_config::num\_regions](structarc__mpu__config.md#a1310febf88e32ea1638445246d8a38f2)

uint32\_t num\_regions

**Definition** arc\_mpu.h:107

[arc\_mpu\_config::mpu\_regions](structarc__mpu__config.md#ad81a6593ea0f7550d9739706267061a1)

struct arc\_mpu\_region \* mpu\_regions

**Definition** arc\_mpu.h:109

[arc\_mpu\_region](structarc__mpu__region.md)

**Definition** arc\_mpu.h:86

[arc\_mpu\_region::size](structarc__mpu__region.md#a17107d330203fcad8ef8222485a205e9)

uint32\_t size

**Definition** arc\_mpu.h:91

[arc\_mpu\_region::base](structarc__mpu__region.md#a4d748e5dcec541bf5aca089861cf931c)

uint32\_t base

**Definition** arc\_mpu.h:90

[arc\_mpu\_region::name](structarc__mpu__region.md#a59db0045486098963ca5646c2995374a)

const char \* name

**Definition** arc\_mpu.h:88

[arc\_mpu\_region::attr](structarc__mpu__region.md#abc3ff764104a4db2d986f30eed370e4a)

uint32\_t attr

**Definition** arc\_mpu.h:93

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [mpu](dir_c51b2f0fffc5b62554252c09f16a5032.md)
- [arc\_mpu.h](arc__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
