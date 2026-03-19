---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stepper__trinamic_8h_source.html
original_path: doxygen/html/stepper__trinamic_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper\_trinamic.h

[Go to the documentation of this file.](stepper__trinamic_8h.md)

1

7

8/\*

9 \* SPDX-FileCopyrightText: Copyright (c) 2024 Carl Zeiss Meditec AG

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_TRINAMIC\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_TRINAMIC\_H\_

16

23

24#include <[stdint.h](stdint_8h.md)>

25#include <[zephyr/drivers/stepper.h](stepper_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 34](group__trinamic__stepper__interface.md#ga9e9a9e371a79b153226645383867f57c)#define TMC\_RAMP\_VSTART\_MAX GENMASK(17, 0)

[ 35](group__trinamic__stepper__interface.md#ga7569a6172df37f1e669eed75a1acb5d5)#define TMC\_RAMP\_VSTART\_MIN 0

[ 36](group__trinamic__stepper__interface.md#ga9530d64f9c331681b33230fcc8ef7512)#define TMC\_RAMP\_V1\_MAX GENMASK(19, 0)

[ 37](group__trinamic__stepper__interface.md#ga6f07fdd1e99eff62f93d28b7c2527283)#define TMC\_RAMP\_V1\_MIN 0

[ 38](group__trinamic__stepper__interface.md#ga6bd3a7d1578f4d9729327cdc9bcb2214)#define TMC\_RAMP\_VMAX\_MAX (GENMASK(22, 0) - 512)

[ 39](group__trinamic__stepper__interface.md#ga42fe12c7afa3411279df79323b6005ff)#define TMC\_RAMP\_VMAX\_MIN 0

[ 40](group__trinamic__stepper__interface.md#ga2043631a9382df69c0cddf69e57845ba)#define TMC\_RAMP\_A1\_MAX GENMASK(15, 0)

[ 41](group__trinamic__stepper__interface.md#gae93384303a1aa78ecee86df6749449a1)#define TMC\_RAMP\_A1\_MIN 0

[ 42](group__trinamic__stepper__interface.md#gac4ae29a8dee3c5f30afd9ad879eb841f)#define TMC\_RAMP\_AMAX\_MAX GENMASK(15, 0)

[ 43](group__trinamic__stepper__interface.md#ga50e4297381755484bbddf9976f1d51f5)#define TMC\_RAMP\_AMAX\_MIN 0

[ 44](group__trinamic__stepper__interface.md#ga9ae3e36281fbf1a83e3c6cf71ef2441f)#define TMC\_RAMP\_D1\_MAX GENMASK(15, 0)

[ 45](group__trinamic__stepper__interface.md#ga9d825b4269d204eaded8b0559114a8ac)#define TMC\_RAMP\_D1\_MIN 1

[ 46](group__trinamic__stepper__interface.md#ga80d3cbcb6455cbafd36c677e292622c4)#define TMC\_RAMP\_DMAX\_MAX GENMASK(15, 0)

[ 47](group__trinamic__stepper__interface.md#gaed3825c79b588840c355fd1d3da9d3bb)#define TMC\_RAMP\_DMAX\_MIN 0

[ 48](group__trinamic__stepper__interface.md#ga7b121c433e4bf33da2a5f14ec53bf627)#define TMC\_RAMP\_VSTOP\_MAX GENMASK(17, 0)

[ 49](group__trinamic__stepper__interface.md#gada43f70cfca38bd5bb3208474c92f276)#define TMC\_RAMP\_VSTOP\_MIN 1

[ 50](group__trinamic__stepper__interface.md#ga0bb50350111fb8a7dc22dae9948690f6)#define TMC\_RAMP\_TZEROWAIT\_MAX (GENMASK(15, 0) - 512)

[ 51](group__trinamic__stepper__interface.md#ga509b5bb88d3976323f90cd9647af97b1)#define TMC\_RAMP\_TZEROWAIT\_MIN 0

[ 52](group__trinamic__stepper__interface.md#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)#define TMC\_RAMP\_VCOOLTHRS\_MAX GENMASK(22, 0)

[ 53](group__trinamic__stepper__interface.md#ga37a395c0056c9b20520cace7ba925014)#define TMC\_RAMP\_VCOOLTHRS\_MIN 0

[ 54](group__trinamic__stepper__interface.md#ga4134f638119d89b559118028a65fd5c7)#define TMC\_RAMP\_VHIGH\_MAX GENMASK(22, 0)

[ 55](group__trinamic__stepper__interface.md#ga7d87a071f418cecd2f80a1a1403ff2c5)#define TMC\_RAMP\_VHIGH\_MIN 0

[ 56](group__trinamic__stepper__interface.md#gaeab2e7683232b2f77c6e57602af268e1)#define TMC\_RAMP\_IHOLD\_IRUN\_MAX GENMASK(4, 0)

[ 57](group__trinamic__stepper__interface.md#ga732705b9ea5208d16caabfd36f9b0ea8)#define TMC\_RAMP\_IHOLD\_IRUN\_MIN 0

[ 58](group__trinamic__stepper__interface.md#ga5cdbd0068d00533a8cf6d952be8c943e)#define TMC\_RAMP\_IHOLDDELAY\_MAX GENMASK(3, 0)

[ 59](group__trinamic__stepper__interface.md#ga7b787ce2fffd9e689230a4abf2070bf2)#define TMC\_RAMP\_IHOLDDELAY\_MIN 0

[ 60](group__trinamic__stepper__interface.md#ga3aee23f87376c760f43d714df646ad54)#define TMC\_RAMP\_VACTUAL\_SHIFT 22

61

[ 65](structtmc__ramp__generator__data.md)struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) {

[ 66](structtmc__ramp__generator__data.md#a6b861b90bb7e4c637b21b7809608152f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vstart](structtmc__ramp__generator__data.md#a6b861b90bb7e4c637b21b7809608152f);

[ 67](structtmc__ramp__generator__data.md#ae9377878720cc03760d207b750997997) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [v1](structtmc__ramp__generator__data.md#ae9377878720cc03760d207b750997997);

[ 68](structtmc__ramp__generator__data.md#a54558710f19a1781bbec3dc857cb8fcf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vmax](structtmc__ramp__generator__data.md#a54558710f19a1781bbec3dc857cb8fcf);

[ 69](structtmc__ramp__generator__data.md#aff69cc918c9ed7e067d728a936b9a5f0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [a1](structtmc__ramp__generator__data.md#aff69cc918c9ed7e067d728a936b9a5f0);

[ 70](structtmc__ramp__generator__data.md#a277403bbb0bbc8a7562bf7b6c3e22333) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [amax](structtmc__ramp__generator__data.md#a277403bbb0bbc8a7562bf7b6c3e22333);

[ 71](structtmc__ramp__generator__data.md#a8672451e2bff4af7f13b72f8a4bc4ed1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [d1](structtmc__ramp__generator__data.md#a8672451e2bff4af7f13b72f8a4bc4ed1);

[ 72](structtmc__ramp__generator__data.md#a34bc24f327a5c1a6315fa4869c5418df) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dmax](structtmc__ramp__generator__data.md#a34bc24f327a5c1a6315fa4869c5418df);

[ 73](structtmc__ramp__generator__data.md#a5f4a921ae3ba0fec18633e659ad42573) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vstop](structtmc__ramp__generator__data.md#a5f4a921ae3ba0fec18633e659ad42573);

[ 74](structtmc__ramp__generator__data.md#ad3846d55690f835623fceca620ec3b23) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tzerowait](structtmc__ramp__generator__data.md#ad3846d55690f835623fceca620ec3b23);

[ 75](structtmc__ramp__generator__data.md#a522f3c11bcac25852a0d7088795f46bd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vcoolthrs](structtmc__ramp__generator__data.md#a522f3c11bcac25852a0d7088795f46bd);

[ 76](structtmc__ramp__generator__data.md#a5ee17564fb78bbbfd1097c6b440bd30c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vhigh](structtmc__ramp__generator__data.md#a5ee17564fb78bbbfd1097c6b440bd30c);

[ 77](structtmc__ramp__generator__data.md#acd7d7b5170ce3ce8839272ecc4dccd52) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [iholdrun](structtmc__ramp__generator__data.md#acd7d7b5170ce3ce8839272ecc4dccd52);

78};

79

[ 83](group__trinamic__stepper__interface.md#ga2066d314a74cbcb47934b7c9b0067791)#define CHECK\_RAMP\_DT\_DATA(node) \

84 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vstart), \

85 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vstart), TMC\_RAMP\_VSTART\_MIN, \

86 TMC\_RAMP\_VSTART\_MAX), "vstart out of range"), ()); \

87 COND\_CODE\_1(DT\_PROP\_EXISTS(node, v1), \

88 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, v1), TMC\_RAMP\_V1\_MIN, \

89 TMC\_RAMP\_V1\_MAX), "v1 out of range"), ()); \

90 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vmax), \

91 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vmax), TMC\_RAMP\_VMAX\_MIN, \

92 TMC\_RAMP\_VMAX\_MAX), "vmax out of range"), ()); \

93 COND\_CODE\_1(DT\_PROP\_EXISTS(node, a1), \

94 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, a1), TMC\_RAMP\_A1\_MIN, \

95 TMC\_RAMP\_A1\_MAX), "a1 out of range"), ()); \

96 COND\_CODE\_1(DT\_PROP\_EXISTS(node, amax), \

97 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, amax), TMC\_RAMP\_AMAX\_MIN, \

98 TMC\_RAMP\_AMAX\_MAX), "amax out of range"), ()); \

99 COND\_CODE\_1(DT\_PROP\_EXISTS(node, d1), \

100 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, d1), TMC\_RAMP\_D1\_MIN, \

101 TMC\_RAMP\_D1\_MAX), "d1 out of range"), ()); \

102 COND\_CODE\_1(DT\_PROP\_EXISTS(node, dmax), \

103 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, dmax), TMC\_RAMP\_DMAX\_MIN, \

104 TMC\_RAMP\_DMAX\_MAX), "dmax out of range"), ()); \

105 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vstop), \

106 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vstop), TMC\_RAMP\_VSTOP\_MIN, \

107 TMC\_RAMP\_VSTOP\_MAX), "vstop out of range"), ()); \

108 COND\_CODE\_1(DT\_PROP\_EXISTS(node, tzerowait), \

109 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, tzerowait), TMC\_RAMP\_TZEROWAIT\_MIN, \

110 TMC\_RAMP\_TZEROWAIT\_MAX), "tzerowait out of range"), ()); \

111 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vcoolthrs), \

112 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vcoolthrs), TMC\_RAMP\_VCOOLTHRS\_MIN, \

113 TMC\_RAMP\_VCOOLTHRS\_MAX), "vcoolthrs out of range"), ()); \

114 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vhigh), \

115 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vhigh), TMC\_RAMP\_VHIGH\_MIN, \

116 TMC\_RAMP\_VHIGH\_MAX), "vhigh out of range"), ()); \

117 COND\_CODE\_1(DT\_PROP\_EXISTS(node, ihold), \

118 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, ihold), TMC\_RAMP\_IHOLD\_IRUN\_MIN, \

119 TMC\_RAMP\_IHOLD\_IRUN\_MAX), "ihold out of range"), ()); \

120 COND\_CODE\_1(DT\_PROP\_EXISTS(node, irun), \

121 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, irun), TMC\_RAMP\_IHOLD\_IRUN\_MIN, \

122 TMC\_RAMP\_IHOLD\_IRUN\_MAX), "irun out of range"), ()); \

123 COND\_CODE\_1(DT\_PROP\_EXISTS(node, iholddelay), \

124 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, iholddelay), TMC\_RAMP\_IHOLDDELAY\_MIN, \

125 TMC\_RAMP\_IHOLDDELAY\_MAX), "iholddelay out of range"), ());

126

[ 134](group__trinamic__stepper__interface.md#gab5e5f7c14b896b580051f8b72afb529d)#define TMC\_RAMP\_DT\_SPEC\_GET(node) \

135 { \

136 .vstart = DT\_PROP(node, vstart), \

137 .v1 = DT\_PROP(node, v1), \

138 .vmax = DT\_PROP(node, vmax), \

139 .a1 = DT\_PROP(node, a1), \

140 .amax = DT\_PROP(node, amax), \

141 .d1 = DT\_PROP(node, d1), \

142 .dmax = DT\_PROP(node, dmax), \

143 .vstop = DT\_PROP(node, vstop), \

144 .tzerowait = DT\_PROP(node, tzerowait), \

145 .vcoolthrs = DT\_PROP(node, vcoolthrs), \

146 .vhigh = DT\_PROP(node, vhigh), \

147 .iholdrun = (TMC5XXX\_IRUN(DT\_PROP(node, irun)) | \

148 TMC5XXX\_IHOLD(DT\_PROP(node, ihold)) | \

149 TMC5XXX\_IHOLDDELAY(DT\_PROP(node, iholddelay))), \

150 }

151

[ 162](group__trinamic__stepper__interface.md#ga9c186c3a7e094dce76ace821abcc9e86)int [tmc50xx\_stepper\_set\_ramp](group__trinamic__stepper__interface.md#ga9c186c3a7e094dce76ace821abcc9e86)(const struct [device](structdevice.md) \*dev,

163 const struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) \*ramp\_data);

164

[ 174](group__trinamic__stepper__interface.md#gac2c7168e3618951b65df3257553260f6)int [tmc50xx\_stepper\_set\_max\_velocity](group__trinamic__stepper__interface.md#gac2c7168e3618951b65df3257553260f6)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) velocity);

175

179

180#ifdef \_\_cplusplus

181}

182#endif

183

184#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_TRINAMIC\_H\_ \*/

[tmc50xx\_stepper\_set\_ramp](group__trinamic__stepper__interface.md#ga9c186c3a7e094dce76ace821abcc9e86)

int tmc50xx\_stepper\_set\_ramp(const struct device \*dev, const struct tmc\_ramp\_generator\_data \*ramp\_data)

Configure Trinamic Stepper Ramp Generator.

[tmc50xx\_stepper\_set\_max\_velocity](group__trinamic__stepper__interface.md#gac2c7168e3618951b65df3257553260f6)

int tmc50xx\_stepper\_set\_max\_velocity(const struct device \*dev, uint32\_t velocity)

Set the maximum velocity of the stepper motor.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[stepper.h](stepper_8h.md)

Public API for Stepper Driver.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md)

Trinamic Stepper Ramp Generator data.

**Definition** stepper\_trinamic.h:65

[tmc\_ramp\_generator\_data::amax](structtmc__ramp__generator__data.md#a277403bbb0bbc8a7562bf7b6c3e22333)

uint16\_t amax

**Definition** stepper\_trinamic.h:70

[tmc\_ramp\_generator\_data::dmax](structtmc__ramp__generator__data.md#a34bc24f327a5c1a6315fa4869c5418df)

uint16\_t dmax

**Definition** stepper\_trinamic.h:72

[tmc\_ramp\_generator\_data::vcoolthrs](structtmc__ramp__generator__data.md#a522f3c11bcac25852a0d7088795f46bd)

uint32\_t vcoolthrs

**Definition** stepper\_trinamic.h:75

[tmc\_ramp\_generator\_data::vmax](structtmc__ramp__generator__data.md#a54558710f19a1781bbec3dc857cb8fcf)

uint32\_t vmax

**Definition** stepper\_trinamic.h:68

[tmc\_ramp\_generator\_data::vhigh](structtmc__ramp__generator__data.md#a5ee17564fb78bbbfd1097c6b440bd30c)

uint32\_t vhigh

**Definition** stepper\_trinamic.h:76

[tmc\_ramp\_generator\_data::vstop](structtmc__ramp__generator__data.md#a5f4a921ae3ba0fec18633e659ad42573)

uint32\_t vstop

**Definition** stepper\_trinamic.h:73

[tmc\_ramp\_generator\_data::vstart](structtmc__ramp__generator__data.md#a6b861b90bb7e4c637b21b7809608152f)

uint32\_t vstart

**Definition** stepper\_trinamic.h:66

[tmc\_ramp\_generator\_data::d1](structtmc__ramp__generator__data.md#a8672451e2bff4af7f13b72f8a4bc4ed1)

uint16\_t d1

**Definition** stepper\_trinamic.h:71

[tmc\_ramp\_generator\_data::iholdrun](structtmc__ramp__generator__data.md#acd7d7b5170ce3ce8839272ecc4dccd52)

uint32\_t iholdrun

**Definition** stepper\_trinamic.h:77

[tmc\_ramp\_generator\_data::tzerowait](structtmc__ramp__generator__data.md#ad3846d55690f835623fceca620ec3b23)

uint16\_t tzerowait

**Definition** stepper\_trinamic.h:74

[tmc\_ramp\_generator\_data::v1](structtmc__ramp__generator__data.md#ae9377878720cc03760d207b750997997)

uint32\_t v1

**Definition** stepper\_trinamic.h:67

[tmc\_ramp\_generator\_data::a1](structtmc__ramp__generator__data.md#aff69cc918c9ed7e067d728a936b9a5f0)

uint16\_t a1

**Definition** stepper\_trinamic.h:69

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_trinamic.h](stepper__trinamic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
