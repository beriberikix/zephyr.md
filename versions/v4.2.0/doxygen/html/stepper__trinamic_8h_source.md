---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stepper__trinamic_8h_source.html
original_path: doxygen/html/stepper__trinamic_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

10 \* SPDX-FileCopyrightText: Copyright (c) 2025 Prevas A/S

11 \*

12 \* SPDX-License-Identifier: Apache-2.0

13 \*/

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_TRINAMIC\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_TRINAMIC\_H\_

17

24

25#include <[stdint.h](stdint_8h.md)>

26#include <[zephyr/drivers/stepper.h](stepper_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 35](group__trinamic__stepper__interface.md#ga9e9a9e371a79b153226645383867f57c)#define TMC\_RAMP\_VSTART\_MAX GENMASK(17, 0)

[ 36](group__trinamic__stepper__interface.md#ga7569a6172df37f1e669eed75a1acb5d5)#define TMC\_RAMP\_VSTART\_MIN 0

[ 37](group__trinamic__stepper__interface.md#ga9530d64f9c331681b33230fcc8ef7512)#define TMC\_RAMP\_V1\_MAX GENMASK(19, 0)

[ 38](group__trinamic__stepper__interface.md#ga6f07fdd1e99eff62f93d28b7c2527283)#define TMC\_RAMP\_V1\_MIN 0

[ 39](group__trinamic__stepper__interface.md#ga6bd3a7d1578f4d9729327cdc9bcb2214)#define TMC\_RAMP\_VMAX\_MAX (GENMASK(22, 0) - 512)

[ 40](group__trinamic__stepper__interface.md#ga42fe12c7afa3411279df79323b6005ff)#define TMC\_RAMP\_VMAX\_MIN 0

[ 41](group__trinamic__stepper__interface.md#ga2043631a9382df69c0cddf69e57845ba)#define TMC\_RAMP\_A1\_MAX GENMASK(15, 0)

[ 42](group__trinamic__stepper__interface.md#gae93384303a1aa78ecee86df6749449a1)#define TMC\_RAMP\_A1\_MIN 0

[ 43](group__trinamic__stepper__interface.md#gac4ae29a8dee3c5f30afd9ad879eb841f)#define TMC\_RAMP\_AMAX\_MAX GENMASK(15, 0)

[ 44](group__trinamic__stepper__interface.md#ga50e4297381755484bbddf9976f1d51f5)#define TMC\_RAMP\_AMAX\_MIN 0

[ 45](group__trinamic__stepper__interface.md#ga9ae3e36281fbf1a83e3c6cf71ef2441f)#define TMC\_RAMP\_D1\_MAX GENMASK(15, 0)

[ 46](group__trinamic__stepper__interface.md#ga9d825b4269d204eaded8b0559114a8ac)#define TMC\_RAMP\_D1\_MIN 1

[ 47](group__trinamic__stepper__interface.md#ga80d3cbcb6455cbafd36c677e292622c4)#define TMC\_RAMP\_DMAX\_MAX GENMASK(15, 0)

[ 48](group__trinamic__stepper__interface.md#gaed3825c79b588840c355fd1d3da9d3bb)#define TMC\_RAMP\_DMAX\_MIN 0

[ 49](group__trinamic__stepper__interface.md#ga7b121c433e4bf33da2a5f14ec53bf627)#define TMC\_RAMP\_VSTOP\_MAX GENMASK(17, 0)

[ 50](group__trinamic__stepper__interface.md#gada43f70cfca38bd5bb3208474c92f276)#define TMC\_RAMP\_VSTOP\_MIN 1

[ 51](group__trinamic__stepper__interface.md#ga0bb50350111fb8a7dc22dae9948690f6)#define TMC\_RAMP\_TZEROWAIT\_MAX (GENMASK(15, 0) - 512)

[ 52](group__trinamic__stepper__interface.md#ga509b5bb88d3976323f90cd9647af97b1)#define TMC\_RAMP\_TZEROWAIT\_MIN 0

[ 53](group__trinamic__stepper__interface.md#gaeab2e7683232b2f77c6e57602af268e1)#define TMC\_RAMP\_IHOLD\_IRUN\_MAX GENMASK(4, 0)

[ 54](group__trinamic__stepper__interface.md#ga732705b9ea5208d16caabfd36f9b0ea8)#define TMC\_RAMP\_IHOLD\_IRUN\_MIN 0

[ 55](group__trinamic__stepper__interface.md#ga5cdbd0068d00533a8cf6d952be8c943e)#define TMC\_RAMP\_IHOLDDELAY\_MAX GENMASK(3, 0)

[ 56](group__trinamic__stepper__interface.md#ga7b787ce2fffd9e689230a4abf2070bf2)#define TMC\_RAMP\_IHOLDDELAY\_MIN 0

[ 57](group__trinamic__stepper__interface.md#ga3aee23f87376c760f43d714df646ad54)#define TMC\_RAMP\_VACTUAL\_SHIFT 22

[ 58](group__trinamic__stepper__interface.md#ga5e6d87a484aa64da36d05321f12c92a5)#define TMC\_RAMP\_XACTUAL\_SHIFT 31

59

60/\* TMC50XX specific \*/

[ 61](group__trinamic__stepper__interface.md#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)#define TMC\_RAMP\_VCOOLTHRS\_MAX GENMASK(22, 0)

[ 62](group__trinamic__stepper__interface.md#ga37a395c0056c9b20520cace7ba925014)#define TMC\_RAMP\_VCOOLTHRS\_MIN 0

[ 63](group__trinamic__stepper__interface.md#ga4134f638119d89b559118028a65fd5c7)#define TMC\_RAMP\_VHIGH\_MAX GENMASK(22, 0)

[ 64](group__trinamic__stepper__interface.md#ga7d87a071f418cecd2f80a1a1403ff2c5)#define TMC\_RAMP\_VHIGH\_MIN 0

65

66/\* TMC51XX specific \*/

[ 67](group__trinamic__stepper__interface.md#ga686fee8768ba3821f67e533067b4b165)#define TMC\_RAMP\_TPOWERDOWN\_MAX GENMASK(7, 0)

[ 68](group__trinamic__stepper__interface.md#ga03f09f2a3a8b1ee37a7abf49baaeab0a)#define TMC\_RAMP\_TPOWERDOWN\_MIN 0

[ 69](group__trinamic__stepper__interface.md#gad06256f808f37c879533254468f3920c)#define TMC\_RAMP\_TPWMTHRS\_MAX GENMASK(19, 0)

[ 70](group__trinamic__stepper__interface.md#gacd563e95d901c133624fc24678a88040)#define TMC\_RAMP\_TPWMTHRS\_MIN 0

[ 71](group__trinamic__stepper__interface.md#gaf43cc157aa2842cfbf5577d8b98c3d4c)#define TMC\_RAMP\_TCOOLTHRS\_MAX GENMASK(19, 0)

[ 72](group__trinamic__stepper__interface.md#ga0dc9a4f1d7e83849220b62175855548b)#define TMC\_RAMP\_TCOOLTHRS\_MIN 0

[ 73](group__trinamic__stepper__interface.md#ga74c583adc60323a2753b82425a9dd745)#define TMC\_RAMP\_THIGH\_MAX GENMASK(19, 0)

[ 74](group__trinamic__stepper__interface.md#gaa3a1c83e852bf2e020eb793f495eee23)#define TMC\_RAMP\_THIGH\_MIN 0

75

[ 79](structtmc__ramp__generator__data.md)struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) {

[ 80](structtmc__ramp__generator__data.md#a6b861b90bb7e4c637b21b7809608152f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vstart](structtmc__ramp__generator__data.md#a6b861b90bb7e4c637b21b7809608152f);

[ 81](structtmc__ramp__generator__data.md#ae9377878720cc03760d207b750997997) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [v1](structtmc__ramp__generator__data.md#ae9377878720cc03760d207b750997997);

[ 82](structtmc__ramp__generator__data.md#a54558710f19a1781bbec3dc857cb8fcf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vmax](structtmc__ramp__generator__data.md#a54558710f19a1781bbec3dc857cb8fcf);

[ 83](structtmc__ramp__generator__data.md#aff69cc918c9ed7e067d728a936b9a5f0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [a1](structtmc__ramp__generator__data.md#aff69cc918c9ed7e067d728a936b9a5f0);

[ 84](structtmc__ramp__generator__data.md#a277403bbb0bbc8a7562bf7b6c3e22333) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [amax](structtmc__ramp__generator__data.md#a277403bbb0bbc8a7562bf7b6c3e22333);

[ 85](structtmc__ramp__generator__data.md#a8672451e2bff4af7f13b72f8a4bc4ed1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [d1](structtmc__ramp__generator__data.md#a8672451e2bff4af7f13b72f8a4bc4ed1);

[ 86](structtmc__ramp__generator__data.md#a34bc24f327a5c1a6315fa4869c5418df) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dmax](structtmc__ramp__generator__data.md#a34bc24f327a5c1a6315fa4869c5418df);

[ 87](structtmc__ramp__generator__data.md#a5f4a921ae3ba0fec18633e659ad42573) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vstop](structtmc__ramp__generator__data.md#a5f4a921ae3ba0fec18633e659ad42573);

[ 88](structtmc__ramp__generator__data.md#ad3846d55690f835623fceca620ec3b23) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tzerowait](structtmc__ramp__generator__data.md#ad3846d55690f835623fceca620ec3b23);

[ 89](structtmc__ramp__generator__data.md#acd7d7b5170ce3ce8839272ecc4dccd52) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [iholdrun](structtmc__ramp__generator__data.md#acd7d7b5170ce3ce8839272ecc4dccd52);

90 union {

91 /\* TMC50XX specific \*/

92 struct {

[ 93](structtmc__ramp__generator__data.md#a522f3c11bcac25852a0d7088795f46bd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vcoolthrs](structtmc__ramp__generator__data.md#a522f3c11bcac25852a0d7088795f46bd);

[ 94](structtmc__ramp__generator__data.md#a5ee17564fb78bbbfd1097c6b440bd30c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vhigh](structtmc__ramp__generator__data.md#a5ee17564fb78bbbfd1097c6b440bd30c);

95 };

96 /\* TMC51XX specific \*/

97 struct {

[ 98](structtmc__ramp__generator__data.md#a3b7d2176725aef71e12950fde1ae3ee0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tpowerdown](structtmc__ramp__generator__data.md#a3b7d2176725aef71e12950fde1ae3ee0);

[ 99](structtmc__ramp__generator__data.md#a94352ae1924cbc900545065c7302379b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tpwmthrs](structtmc__ramp__generator__data.md#a94352ae1924cbc900545065c7302379b);

[ 100](structtmc__ramp__generator__data.md#a871cb11fb3d1aacfd29b85f8ea42b502) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tcoolthrs](structtmc__ramp__generator__data.md#a871cb11fb3d1aacfd29b85f8ea42b502);

[ 101](structtmc__ramp__generator__data.md#a8045473482ca1272a75e99938564a700) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [thigh](structtmc__ramp__generator__data.md#a8045473482ca1272a75e99938564a700);

102 };

103 };

104};

105

[ 109](group__trinamic__stepper__interface.md#ga2066d314a74cbcb47934b7c9b0067791)#define CHECK\_RAMP\_DT\_DATA(node) \

110 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vstart), \

111 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vstart), TMC\_RAMP\_VSTART\_MIN, \

112 TMC\_RAMP\_VSTART\_MAX), "vstart out of range"), ()); \

113 COND\_CODE\_1(DT\_PROP\_EXISTS(node, v1), \

114 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, v1), TMC\_RAMP\_V1\_MIN, \

115 TMC\_RAMP\_V1\_MAX), "v1 out of range"), ()); \

116 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vmax), \

117 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vmax), TMC\_RAMP\_VMAX\_MIN, \

118 TMC\_RAMP\_VMAX\_MAX), "vmax out of range"), ()); \

119 COND\_CODE\_1(DT\_PROP\_EXISTS(node, a1), \

120 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, a1), TMC\_RAMP\_A1\_MIN, \

121 TMC\_RAMP\_A1\_MAX), "a1 out of range"), ()); \

122 COND\_CODE\_1(DT\_PROP\_EXISTS(node, amax), \

123 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, amax), TMC\_RAMP\_AMAX\_MIN, \

124 TMC\_RAMP\_AMAX\_MAX), "amax out of range"), ()); \

125 COND\_CODE\_1(DT\_PROP\_EXISTS(node, d1), \

126 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, d1), TMC\_RAMP\_D1\_MIN, \

127 TMC\_RAMP\_D1\_MAX), "d1 out of range"), ()); \

128 COND\_CODE\_1(DT\_PROP\_EXISTS(node, dmax), \

129 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, dmax), TMC\_RAMP\_DMAX\_MIN, \

130 TMC\_RAMP\_DMAX\_MAX), "dmax out of range"), ()); \

131 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vstop), \

132 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vstop), TMC\_RAMP\_VSTOP\_MIN, \

133 TMC\_RAMP\_VSTOP\_MAX), "vstop out of range"), ()); \

134 COND\_CODE\_1(DT\_PROP\_EXISTS(node, tzerowait), \

135 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, tzerowait), TMC\_RAMP\_TZEROWAIT\_MIN, \

136 TMC\_RAMP\_TZEROWAIT\_MAX), "tzerowait out of range"), ()); \

137 COND\_CODE\_1(DT\_PROP\_EXISTS(node, ihold), \

138 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, ihold), TMC\_RAMP\_IHOLD\_IRUN\_MIN, \

139 TMC\_RAMP\_IHOLD\_IRUN\_MAX), "ihold out of range"), ()); \

140 COND\_CODE\_1(DT\_PROP\_EXISTS(node, irun), \

141 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, irun), TMC\_RAMP\_IHOLD\_IRUN\_MIN, \

142 TMC\_RAMP\_IHOLD\_IRUN\_MAX), "irun out of range"), ()); \

143 COND\_CODE\_1(DT\_PROP\_EXISTS(node, iholddelay), \

144 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, iholddelay), TMC\_RAMP\_IHOLDDELAY\_MIN, \

145 TMC\_RAMP\_IHOLDDELAY\_MAX), "iholddelay out of range"), ());\

146 /\* TMC50XX specific \*/ \

147 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vcoolthrs), \

148 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vcoolthrs), TMC\_RAMP\_VCOOLTHRS\_MIN, \

149 TMC\_RAMP\_VCOOLTHRS\_MAX), "vcoolthrs out of range"), ()); \

150 COND\_CODE\_1(DT\_PROP\_EXISTS(node, vhigh), \

151 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, vhigh), TMC\_RAMP\_VHIGH\_MIN, \

152 TMC\_RAMP\_VHIGH\_MAX), "vhigh out of range"), ()); \

153 /\* TMC51XX specific \*/ \

154 COND\_CODE\_1(DT\_PROP\_EXISTS(node, tpowerdown), \

155 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, tpowerdown), TMC\_RAMP\_TPOWERDOWN\_MIN, \

156 TMC\_RAMP\_TPOWERDOWN\_MAX), "tpowerdown out of range"), ());\

157 COND\_CODE\_1(DT\_PROP\_EXISTS(node, tpwmthrs), \

158 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, tpwmthrs), TMC\_RAMP\_TPWMTHRS\_MIN, \

159 TMC\_RAMP\_TPWMTHRS\_MAX), "tpwmthrs out of range"), ()); \

160 COND\_CODE\_1(DT\_PROP\_EXISTS(node, tcoolthrs), \

161 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, tcoolthrs), TMC\_RAMP\_TCOOLTHRS\_MIN, \

162 TMC\_RAMP\_TCOOLTHRS\_MAX), "tcoolthrs out of range"), ()); \

163 COND\_CODE\_1(DT\_PROP\_EXISTS(node, thigh), \

164 BUILD\_ASSERT(IN\_RANGE(DT\_PROP(node, thigh), TMC\_RAMP\_THIGH\_MIN, \

165 TMC\_RAMP\_THIGH\_MAX), "thigh out of range"), ());

166

[ 174](group__trinamic__stepper__interface.md#ga05fe4dd5a148d23cd1240d3e3534726c)#define TMC\_RAMP\_DT\_SPEC\_GET\_COMMON(node) \

175 .vstart = DT\_PROP(node, vstart), \

176 .v1 = DT\_PROP(node, v1), \

177 .vmax = DT\_PROP(node, vmax), \

178 .a1 = DT\_PROP(node, a1), \

179 .amax = DT\_PROP(node, amax), \

180 .d1 = DT\_PROP(node, d1), \

181 .dmax = DT\_PROP(node, dmax), \

182 .vstop = DT\_PROP(node, vstop), \

183 .tzerowait = DT\_PROP(node, tzerowait), \

184 .iholdrun = (TMC5XXX\_IRUN(DT\_PROP(node, irun)) | \

185 TMC5XXX\_IHOLD(DT\_PROP(node, ihold)) | \

186 TMC5XXX\_IHOLDDELAY(DT\_PROP(node, iholddelay))),

187

[ 188](group__trinamic__stepper__interface.md#ga485a07aa34b72643ef77203d6e7c0de2)#define TMC\_RAMP\_DT\_SPEC\_GET\_TMC50XX(node) \

189 { \

190 TMC\_RAMP\_DT\_SPEC\_GET\_COMMON(node) \

191 .vhigh = DT\_PROP(node, vhigh), \

192 .vcoolthrs = DT\_PROP(node, vcoolthrs), \

193 }

194

[ 195](group__trinamic__stepper__interface.md#ga92c5a6a95451f15cc5b5712ac2e50ad7)#define TMC\_RAMP\_DT\_SPEC\_GET\_TMC51XX(node) \

196 { \

197 TMC\_RAMP\_DT\_SPEC\_GET\_COMMON(DT\_DRV\_INST(node)) \

198 .tpowerdown = DT\_INST\_PROP(node, tpowerdown), \

199 .tpwmthrs = DT\_INST\_PROP(node, tpwmthrs), \

200 .tcoolthrs = DT\_INST\_PROP(node, tcoolthrs), \

201 .thigh = DT\_INST\_PROP(node, thigh), \

202 }

203

[ 214](group__trinamic__stepper__interface.md#ga9c186c3a7e094dce76ace821abcc9e86)int [tmc50xx\_stepper\_set\_ramp](group__trinamic__stepper__interface.md#ga9c186c3a7e094dce76ace821abcc9e86)(const struct [device](structdevice.md) \*dev,

215 const struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) \*ramp\_data);

216

[ 226](group__trinamic__stepper__interface.md#gac2c7168e3618951b65df3257553260f6)int [tmc50xx\_stepper\_set\_max\_velocity](group__trinamic__stepper__interface.md#gac2c7168e3618951b65df3257553260f6)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) velocity);

227

231

232#ifdef \_\_cplusplus

233}

234#endif

235

236#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_TRINAMIC\_H\_ \*/

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

**Definition** device.h:510

[tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md)

Trinamic Stepper Ramp Generator data.

**Definition** stepper\_trinamic.h:79

[tmc\_ramp\_generator\_data::amax](structtmc__ramp__generator__data.md#a277403bbb0bbc8a7562bf7b6c3e22333)

uint16\_t amax

**Definition** stepper\_trinamic.h:84

[tmc\_ramp\_generator\_data::dmax](structtmc__ramp__generator__data.md#a34bc24f327a5c1a6315fa4869c5418df)

uint16\_t dmax

**Definition** stepper\_trinamic.h:86

[tmc\_ramp\_generator\_data::tpowerdown](structtmc__ramp__generator__data.md#a3b7d2176725aef71e12950fde1ae3ee0)

uint32\_t tpowerdown

**Definition** stepper\_trinamic.h:98

[tmc\_ramp\_generator\_data::vcoolthrs](structtmc__ramp__generator__data.md#a522f3c11bcac25852a0d7088795f46bd)

uint32\_t vcoolthrs

**Definition** stepper\_trinamic.h:93

[tmc\_ramp\_generator\_data::vmax](structtmc__ramp__generator__data.md#a54558710f19a1781bbec3dc857cb8fcf)

uint32\_t vmax

**Definition** stepper\_trinamic.h:82

[tmc\_ramp\_generator\_data::vhigh](structtmc__ramp__generator__data.md#a5ee17564fb78bbbfd1097c6b440bd30c)

uint32\_t vhigh

**Definition** stepper\_trinamic.h:94

[tmc\_ramp\_generator\_data::vstop](structtmc__ramp__generator__data.md#a5f4a921ae3ba0fec18633e659ad42573)

uint32\_t vstop

**Definition** stepper\_trinamic.h:87

[tmc\_ramp\_generator\_data::vstart](structtmc__ramp__generator__data.md#a6b861b90bb7e4c637b21b7809608152f)

uint32\_t vstart

**Definition** stepper\_trinamic.h:80

[tmc\_ramp\_generator\_data::thigh](structtmc__ramp__generator__data.md#a8045473482ca1272a75e99938564a700)

uint32\_t thigh

**Definition** stepper\_trinamic.h:101

[tmc\_ramp\_generator\_data::d1](structtmc__ramp__generator__data.md#a8672451e2bff4af7f13b72f8a4bc4ed1)

uint16\_t d1

**Definition** stepper\_trinamic.h:85

[tmc\_ramp\_generator\_data::tcoolthrs](structtmc__ramp__generator__data.md#a871cb11fb3d1aacfd29b85f8ea42b502)

uint32\_t tcoolthrs

**Definition** stepper\_trinamic.h:100

[tmc\_ramp\_generator\_data::tpwmthrs](structtmc__ramp__generator__data.md#a94352ae1924cbc900545065c7302379b)

uint32\_t tpwmthrs

**Definition** stepper\_trinamic.h:99

[tmc\_ramp\_generator\_data::iholdrun](structtmc__ramp__generator__data.md#acd7d7b5170ce3ce8839272ecc4dccd52)

uint32\_t iholdrun

**Definition** stepper\_trinamic.h:89

[tmc\_ramp\_generator\_data::tzerowait](structtmc__ramp__generator__data.md#ad3846d55690f835623fceca620ec3b23)

uint16\_t tzerowait

**Definition** stepper\_trinamic.h:88

[tmc\_ramp\_generator\_data::v1](structtmc__ramp__generator__data.md#ae9377878720cc03760d207b750997997)

uint32\_t v1

**Definition** stepper\_trinamic.h:81

[tmc\_ramp\_generator\_data::a1](structtmc__ramp__generator__data.md#aff69cc918c9ed7e067d728a936b9a5f0)

uint16\_t a1

**Definition** stepper\_trinamic.h:83

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_trinamic.h](stepper__trinamic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
