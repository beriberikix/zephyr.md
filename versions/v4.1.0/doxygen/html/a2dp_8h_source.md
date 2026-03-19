---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/a2dp_8h_source.html
original_path: doxygen/html/a2dp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

a2dp.h

[Go to the documentation of this file.](a2dp_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \* Copyright 2024 NXP

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_H\_

13

14#include <[stdint.h](stdint_8h.md)>

15

16#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

17#include <[zephyr/bluetooth/l2cap.h](l2cap_8h.md)>

18#include <[zephyr/bluetooth/classic/avdtp.h](avdtp_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](a2dp_8h.md#a9fce344cfaa8b96ca41a5866f9e3b3d1)#define BT\_A2DP\_STREAM\_BUF\_RESERVE (12U + BT\_L2CAP\_BUF\_SIZE(0))

25

[ 27](a2dp_8h.md#af83aa927ac312cfc8577056afffeae56)#define BT\_A2DP\_SBC\_IE\_LENGTH (4U)

[ 29](a2dp_8h.md#a313fec2276421be6f29c0309e67755eb)#define BT\_A2DP\_MPEG\_1\_2\_IE\_LENGTH (4U)

[ 31](a2dp_8h.md#a73ae4b6e2913b3772b32c520bf84de8c)#define BT\_A2DP\_MPEG\_2\_4\_IE\_LENGTH (6U)

[ 33](a2dp_8h.md#a8c365793c40e8425d9e002208bc7863f)#define BT\_A2DP\_MAX\_IE\_LENGTH (8U)

34

[ 40](a2dp_8h.md#afe0cc7b22a941d272de4f8353865d626)#define BT\_A2DP\_EP\_INIT(\_role, \_codec, \_capability) \

41 { \

42 .codec\_type = \_codec, \

43 .sep = {.sep\_info = {.media\_type = BT\_AVDTP\_AUDIO, .tsep = \_role}}, \

44 .codec\_cap = \_capability, .stream = NULL, \

45 }

46

[ 51](a2dp_8h.md#a892825546a211982b8809dc0f7596ba2)#define BT\_A2DP\_SINK\_EP\_INIT(\_codec, \_capability) \

52 BT\_A2DP\_EP\_INIT(BT\_AVDTP\_SINK, \_codec, \_capability)

53

[ 58](a2dp_8h.md#a78089fb18ea7a16dff7ba05370bb452c)#define BT\_A2DP\_SOURCE\_EP\_INIT(\_codec, \_capability) \

59 BT\_A2DP\_EP\_INIT(BT\_AVDTP\_SOURCE, \_codec, \_capability)

60

[ 82](a2dp_8h.md#abf08745833eacb9b409627442ac4c8a2)#define BT\_A2DP\_SBC\_SINK\_EP(\_name, \_freq, \_ch\_mode, \_blk\_len, \_subband, \_alloc\_mthd, \_min\_bitpool, \

83 \_max\_bitpool) \

84 static struct bt\_a2dp\_codec\_ie bt\_a2dp\_ep\_cap\_ie##\_name = { \

85 .len = BT\_A2DP\_SBC\_IE\_LENGTH, \

86 .codec\_ie = {\_freq | \_ch\_mode, \_blk\_len | \_subband | \_alloc\_mthd, \_min\_bitpool, \

87 \_max\_bitpool}}; \

88 static struct bt\_a2dp\_ep \_name = \

89 BT\_A2DP\_SINK\_EP\_INIT(BT\_A2DP\_SBC, (&bt\_a2dp\_ep\_cap\_ie##\_name))

90

[ 111](a2dp_8h.md#a9b9d32d04f96f64d7c5f9bf10e03f9a8)#define BT\_A2DP\_SBC\_SOURCE\_EP(\_name, \_freq, \_ch\_mode, \_blk\_len, \_subband, \_alloc\_mthd, \

112 \_min\_bitpool, \_max\_bitpool) \

113 static struct bt\_a2dp\_codec\_ie bt\_a2dp\_ep\_cap\_ie##\_name = { \

114 .len = BT\_A2DP\_SBC\_IE\_LENGTH, \

115 .codec\_ie = {\_freq | \_ch\_mode, \_blk\_len | \_subband | \_alloc\_mthd, \_min\_bitpool, \

116 \_max\_bitpool}}; \

117 static struct bt\_a2dp\_ep \_name = \

118 BT\_A2DP\_SOURCE\_EP\_INIT(BT\_A2DP\_SBC, &bt\_a2dp\_ep\_cap\_ie##\_name)

119

[ 128](a2dp_8h.md#a76fb351efe2730311baae1ad6cddbcb1)#define BT\_A2DP\_SBC\_SINK\_EP\_DEFAULT(\_name) \

129 static struct bt\_a2dp\_codec\_ie bt\_a2dp\_ep\_cap\_ie##\_name = { \

130 .len = BT\_A2DP\_SBC\_IE\_LENGTH, \

131 .codec\_ie = {A2DP\_SBC\_SAMP\_FREQ\_44100 | A2DP\_SBC\_SAMP\_FREQ\_48000 | \

132 A2DP\_SBC\_CH\_MODE\_MONO | A2DP\_SBC\_CH\_MODE\_STREO | \

133 A2DP\_SBC\_CH\_MODE\_JOINT, \

134 A2DP\_SBC\_BLK\_LEN\_16 | A2DP\_SBC\_SUBBAND\_8 | \

135 A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS, \

136 18U, 35U}}; \

137 static struct bt\_a2dp\_ep \_name = \

138 BT\_A2DP\_SINK\_EP\_INIT(BT\_A2DP\_SBC, &bt\_a2dp\_ep\_cap\_ie##\_name)

139

[ 148](a2dp_8h.md#a6830ae27e85471935ae604b18cf779e2)#define BT\_A2DP\_SBC\_SOURCE\_EP\_DEFAULT(\_name) \

149 static struct bt\_a2dp\_codec\_ie bt\_a2dp\_ep\_cap\_ie##\_name = { \

150 .len = BT\_A2DP\_SBC\_IE\_LENGTH, \

151 .codec\_ie = {A2DP\_SBC\_SAMP\_FREQ\_44100 | A2DP\_SBC\_SAMP\_FREQ\_48000 | \

152 A2DP\_SBC\_CH\_MODE\_MONO | A2DP\_SBC\_CH\_MODE\_STREO | \

153 A2DP\_SBC\_CH\_MODE\_JOINT, \

154 A2DP\_SBC\_BLK\_LEN\_16 | A2DP\_SBC\_SUBBAND\_8 | \

155 A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS, \

156 18U, 35U}, \

157 }; \

158 static struct bt\_a2dp\_ep \_name = \

159 BT\_A2DP\_SOURCE\_EP\_INIT(BT\_A2DP\_SBC, &bt\_a2dp\_ep\_cap\_ie##\_name)

160

[ 177](a2dp_8h.md#ac879cbea5f0bbecfc0ec948d6e46c073)#define BT\_A2DP\_SBC\_EP\_CFG(\_name, \_freq\_cfg, \_ch\_mode\_cfg, \_blk\_len\_cfg, \_subband\_cfg, \

178 \_alloc\_mthd\_cfg, \_min\_bitpool\_cfg, \_max\_bitpool\_cfg) \

179 static struct bt\_a2dp\_codec\_ie bt\_a2dp\_codec\_ie##\_name = { \

180 .len = BT\_A2DP\_SBC\_IE\_LENGTH, \

181 .codec\_ie = {\_freq\_cfg | \_ch\_mode\_cfg, \

182 \_blk\_len\_cfg | \_subband\_cfg | \_alloc\_mthd\_cfg, \_min\_bitpool\_cfg, \

183 \_max\_bitpool\_cfg}, \

184 }; \

185 struct bt\_a2dp\_codec\_cfg \_name = { \

186 .codec\_config = &bt\_a2dp\_codec\_ie##\_name, \

187 }

188

[ 194](a2dp_8h.md#abbfd3bc3fa080517ef4395b30fd697f7)#define BT\_A2DP\_SBC\_EP\_CFG\_DEFAULT(\_name, \_freq\_cfg) \

195 static struct bt\_a2dp\_codec\_ie bt\_a2dp\_codec\_ie##\_name = { \

196 .len = BT\_A2DP\_SBC\_IE\_LENGTH, \

197 .codec\_ie = {\_freq\_cfg | A2DP\_SBC\_CH\_MODE\_JOINT, \

198 A2DP\_SBC\_BLK\_LEN\_16 | A2DP\_SBC\_SUBBAND\_8 | \

199 A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS, \

200 18U, 35U}, \

201 }; \

202 struct bt\_a2dp\_codec\_cfg \_name = { \

203 .codec\_config = &bt\_a2dp\_codec\_ie##\_name, \

204 }

205

[ 209](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c)enum [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c) {

[ 211](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591) [BT\_A2DP\_INVALID\_CODEC\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591) = 0xC1,

[ 213](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f) [BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f) = 0xC2,

[ 215](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c) [BT\_A2DP\_INVALID\_SAMPLING\_FREQUENCY](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c) = 0xC3,

[ 217](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76) [BT\_A2DP\_NOT\_SUPPORTED\_SAMPLING\_FREQUENCY](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76) = 0xC4,

[ 219](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396) [BT\_A2DP\_INVALID\_CHANNEL\_MODE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396) = 0xC5,

[ 221](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755) [BT\_A2DP\_NOT\_SUPPORTED\_CHANNEL\_MODE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755) = 0xC6,

[ 223](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f) [BT\_A2DP\_INVALID\_SUBBANDS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f) = 0xC7,

[ 225](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d) [BT\_A2DP\_NOT\_SUPPORTED\_SUBBANDS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d) = 0xC8,

[ 227](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a) [BT\_A2DP\_INVALID\_ALLOCATION\_METHOD](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a) = 0xC9,

[ 229](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8) [BT\_A2DP\_NOT\_SUPPORTED\_ALLOCATION\_METHOD](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8) = 0xCA,

[ 231](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02) [BT\_A2DP\_INVALID\_MINIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02) = 0xCB,

[ 233](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3) [BT\_A2DP\_NOT\_SUPPORTED\_MINIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3) = 0xCC,

[ 235](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf) [BT\_A2DP\_INVALID\_MAXIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf) = 0xCD,

[ 237](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f) [BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f) = 0xCE,

[ 239](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41) [BT\_A2DP\_INVALID\_LAYER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41) = 0xCF,

[ 241](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e) [BT\_A2DP\_NOT\_SUPPORTED\_LAYER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e) = 0xD0,

[ 243](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec) [BT\_A2DP\_NOT\_SUPPORTED\_CRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec) = 0xD1,

[ 245](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f) [BT\_A2DP\_NOT\_SUPPORTED\_MPF](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f) = 0xD2,

[ 247](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51) [BT\_A2DP\_NOT\_SUPPORTED\_VBR](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51) = 0xD3,

[ 249](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476) [BT\_A2DP\_INVALID\_BIT\_RATE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476) = 0xD4,

[ 251](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1) [BT\_A2DP\_NOT\_SUPPORTED\_BIT\_RATE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1) = 0xD5,

[ 255](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429) [BT\_A2DP\_INVALID\_OBJECT\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429) = 0xD6,

[ 257](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615) [BT\_A2DP\_NOT\_SUPPORTED\_OBJECT\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615) = 0xD7,

[ 261](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483) [BT\_A2DP\_INVALID\_CHANNELS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483) = 0xD8,

[ 263](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a) [BT\_A2DP\_NOT\_SUPPORTED\_CHANNELS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a) = 0xD9,

[ 265](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d) [BT\_A2DP\_INVALID\_VERSION](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d) = 0xDA,

[ 267](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c) [BT\_A2DP\_NOT\_SUPPORTED\_VERSION](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c) = 0xDB,

[ 269](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b) [BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_SUL](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b) = 0xDC,

[ 271](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3) [BT\_A2DP\_INVALID\_BLOCK\_LENGTH](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3) = 0xDD,

[ 273](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611) [BT\_A2DP\_INVALID\_CP\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611) = 0xE0,

[ 277](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63) [BT\_A2DP\_INVALID\_CP\_FORMAT](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63) = 0xE1,

[ 281](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396) [BT\_A2DP\_INVALID\_CODEC\_PARAMETER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396) = 0xE2,

[ 285](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9) [BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_PARAMETER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9) = 0xE3,

[ 287](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96) [BT\_A2DP\_INVALID\_DRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96) = 0xE4,

[ 289](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd) [BT\_A2DP\_NOT\_SUPPORTED\_DRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd) = 0xE5,

290};

291

[ 293](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6)enum [bt\_a2dp\_codec\_type](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6) {

[ 295](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00) [BT\_A2DP\_SBC](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00) = 0x00,

[ 297](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497) [BT\_A2DP\_MPEG1](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497) = 0x01,

[ 299](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88) [BT\_A2DP\_MPEG2](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88) = 0x02,

[ 301](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83) [BT\_A2DP\_ATRAC](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83) = 0x04,

[ 303](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701) [BT\_A2DP\_VENDOR](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701) = 0xff

304};

305

307struct bt\_a2dp;

308

309/\* Internal to pass build \*/

310struct [bt\_a2dp\_stream](structbt__a2dp__stream.md);

311

[ 313](structbt__a2dp__codec__ie.md)struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) {

[ 315](structbt__a2dp__codec__ie.md#a8ba1a0bfcbfd180cb19fb7c4a4ce8225) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__a2dp__codec__ie.md#a8ba1a0bfcbfd180cb19fb7c4a4ce8225);

[ 317](structbt__a2dp__codec__ie.md#acf258c8d4b123e3765ad7e2568ac43aa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_ie](structbt__a2dp__codec__ie.md#acf258c8d4b123e3765ad7e2568ac43aa)[[BT\_A2DP\_MAX\_IE\_LENGTH](a2dp_8h.md#a8c365793c40e8425d9e002208bc7863f)];

318};

319

[ 321](structbt__a2dp__codec__cfg.md)struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) {

[ 323](structbt__a2dp__codec__cfg.md#a178eb806a01729d940e6e8c34b0fb513) struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) \*[codec\_config](structbt__a2dp__codec__cfg.md#a178eb806a01729d940e6e8c34b0fb513);

324};

325

[ 327](structbt__a2dp__ep.md)struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) {

[ 329](structbt__a2dp__ep.md#a912cf7cd18a58a1cc1a5e326e8bebb73) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_type](structbt__a2dp__ep.md#a912cf7cd18a58a1cc1a5e326e8bebb73);

[ 331](structbt__a2dp__ep.md#ae4dcc7f4bca5cc34cf05c2277379a1b3) struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) \*[codec\_cap](structbt__a2dp__ep.md#ae4dcc7f4bca5cc34cf05c2277379a1b3);

[ 333](structbt__a2dp__ep.md#a2565b03e09e5abcf239c4c671b348c50) struct [bt\_avdtp\_sep](structbt__avdtp__sep.md) [sep](structbt__a2dp__ep.md#a2565b03e09e5abcf239c4c671b348c50);

334 /\* Internally used stream object pointer \*/

[ 335](structbt__a2dp__ep.md#a4902b9fde9be1aa9b7a35c22a21cd4a6) struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*[stream](structbt__a2dp__ep.md#a4902b9fde9be1aa9b7a35c22a21cd4a6);

336};

337

[ 338](structbt__a2dp__ep__info.md)struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) {

[ 340](structbt__a2dp__ep__info.md#aca4f893b087a8429dd104b67114e36d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_type](structbt__a2dp__ep__info.md#aca4f893b087a8429dd104b67114e36d7);

[ 342](structbt__a2dp__ep__info.md#a7647012b4ea73a0124e2a3239a3bad7b) struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) [codec\_cap](structbt__a2dp__ep__info.md#a7647012b4ea73a0124e2a3239a3bad7b);

[ 344](structbt__a2dp__ep__info.md#a114c3b267587efa71922e31e474fd8e4) struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) [sep\_info](structbt__a2dp__ep__info.md#a114c3b267587efa71922e31e474fd8e4);

345};

346

350enum {

[ 351](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2) [BT\_A2DP\_DISCOVER\_EP\_STOP](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2) = 0,

[ 352](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367) [BT\_A2DP\_DISCOVER\_EP\_CONTINUE](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367),

353};

354

[ 380](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_a2dp\_discover\_ep\_cb](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed))(struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) \*info,

381 struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*\*ep);

382

[ 383](structbt__a2dp__discover__param.md)struct [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md) {

[ 385](structbt__a2dp__discover__param.md#a806fdbaf6d26ad269608afaa21c2035f) [bt\_a2dp\_discover\_ep\_cb](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed) [cb](structbt__a2dp__discover__param.md#a806fdbaf6d26ad269608afaa21c2035f);

[ 387](structbt__a2dp__discover__param.md#a14b69e2449f1d2379183690246f55a88) struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) [info](structbt__a2dp__discover__param.md#a14b69e2449f1d2379183690246f55a88);

[ 391](structbt__a2dp__discover__param.md#ab4174f0b43d1804192cd4647d29779d3) struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) \*[seps\_info](structbt__a2dp__discover__param.md#ab4174f0b43d1804192cd4647d29779d3);

[ 393](structbt__a2dp__discover__param.md#a382ce8462958f69af19e325491c6f01b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sep\_count](structbt__a2dp__discover__param.md#a382ce8462958f69af19e325491c6f01b);

394};

395

[ 397](structbt__a2dp__cb.md)struct [bt\_a2dp\_cb](structbt__a2dp__cb.md) {

[ 408](structbt__a2dp__cb.md#ab0b6a895c2f050ab0961325b8ce7e862) void (\*[connected](structbt__a2dp__cb.md#ab0b6a895c2f050ab0961325b8ce7e862))(struct bt\_a2dp \*a2dp, int err);

[ 416](structbt__a2dp__cb.md#a80401da71ae6dc74d058163624f78518) void (\*[disconnected](structbt__a2dp__cb.md#a80401da71ae6dc74d058163624f78518))(struct bt\_a2dp \*a2dp);

[ 432](structbt__a2dp__cb.md#aab8f5f53a7b507d55e1d594995739222) int (\*[config\_req](structbt__a2dp__cb.md#aab8f5f53a7b507d55e1d594995739222))(struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*ep,

433 struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*codec\_cfg, struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*\*stream,

434 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 447](structbt__a2dp__cb.md#aba09a3ccebcd77068028d22036d6b53d) int (\*[reconfig\_req](structbt__a2dp__cb.md#aba09a3ccebcd77068028d22036d6b53d))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*codec\_cfg,

448 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 457](structbt__a2dp__cb.md#a3b2f6c42bcdefe8a2591fc59c2357786) void (\*[config\_rsp](structbt__a2dp__cb.md#a3b2f6c42bcdefe8a2591fc59c2357786))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 470](structbt__a2dp__cb.md#adc611ad1a28c3da94f261cc94f63698f) int (\*[establish\_req](structbt__a2dp__cb.md#adc611ad1a28c3da94f261cc94f63698f))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 480](structbt__a2dp__cb.md#af19a1f6bb65c60cb0ec7294e66468ba6) void (\*[establish\_rsp](structbt__a2dp__cb.md#af19a1f6bb65c60cb0ec7294e66468ba6))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 493](structbt__a2dp__cb.md#a90a637e6e81bf5a74c878c3b4b2e63c0) int (\*[release\_req](structbt__a2dp__cb.md#a90a637e6e81bf5a74c878c3b4b2e63c0))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 503](structbt__a2dp__cb.md#ab4c148eb7be896dec8f6a33217b475e1) void (\*[release\_rsp](structbt__a2dp__cb.md#ab4c148eb7be896dec8f6a33217b475e1))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 516](structbt__a2dp__cb.md#a1388b0365e46afce78b4f08f25af6858) int (\*[start\_req](structbt__a2dp__cb.md#a1388b0365e46afce78b4f08f25af6858))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 525](structbt__a2dp__cb.md#a49bae91e1cac18a5da90160214a61725) void (\*[start\_rsp](structbt__a2dp__cb.md#a49bae91e1cac18a5da90160214a61725))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 538](structbt__a2dp__cb.md#a79d2edefa0e6e979bfcfcffe9391a7c0) int (\*[suspend\_req](structbt__a2dp__cb.md#a79d2edefa0e6e979bfcfcffe9391a7c0))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 547](structbt__a2dp__cb.md#a6064e5d61acb3cdd0f83246ce90e712f) void (\*[suspend\_rsp](structbt__a2dp__cb.md#a6064e5d61acb3cdd0f83246ce90e712f))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 560](structbt__a2dp__cb.md#a81fe4d6d5db8ad1cf541b141c0bca18f) int (\*[abort\_req](structbt__a2dp__cb.md#a81fe4d6d5db8ad1cf541b141c0bca18f))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 569](structbt__a2dp__cb.md#af051e057f504b1d9c8da4e4958fba115) void (\*[abort\_rsp](structbt__a2dp__cb.md#af051e057f504b1d9c8da4e4958fba115))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

570};

571

[ 586](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)struct bt\_a2dp \*[bt\_a2dp\_connect](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)(struct bt\_conn \*conn);

587

[ 597](a2dp_8h.md#abbf0d012860a233ecc84ed333e0da051)int [bt\_a2dp\_disconnect](a2dp_8h.md#abbf0d012860a233ecc84ed333e0da051)(struct bt\_a2dp \*a2dp);

598

[ 607](a2dp_8h.md#ab1cd7028a41bfdc34ce8cc60aed239de)int [bt\_a2dp\_register\_ep](a2dp_8h.md#ab1cd7028a41bfdc34ce8cc60aed239de)(struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) media\_type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sep\_type);

608

[ 617](a2dp_8h.md#a4af29d7c162743c00534868ba945b7ec)int [bt\_a2dp\_register\_cb](a2dp_8h.md#a4af29d7c162743c00534868ba945b7ec)(struct [bt\_a2dp\_cb](structbt__a2dp__cb.md) \*cb);

618

[ 626](a2dp_8h.md#a931234227bc2b9eaed9cd60471ee54db)int [bt\_a2dp\_discover](a2dp_8h.md#a931234227bc2b9eaed9cd60471ee54db)(struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md) \*param);

627

[ 629](structbt__a2dp__stream.md)struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) {

[ 631](structbt__a2dp__stream.md#aa490bb24525c50cf8c1675a01223420c) struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*[local\_ep](structbt__a2dp__stream.md#aa490bb24525c50cf8c1675a01223420c);

[ 633](structbt__a2dp__stream.md#a4ea9de245b573b7d0c495aacd7534099) struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*[remote\_ep](structbt__a2dp__stream.md#a4ea9de245b573b7d0c495aacd7534099);

[ 635](structbt__a2dp__stream.md#a3361f68c31075014c2c3cf62494ff3ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [remote\_ep\_id](structbt__a2dp__stream.md#a3361f68c31075014c2c3cf62494ff3ec);

[ 637](structbt__a2dp__stream.md#aa51509d9f0c50118177345988ddb8fa5) struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) \*[ops](structbt__a2dp__stream.md#aa51509d9f0c50118177345988ddb8fa5);

[ 639](structbt__a2dp__stream.md#ab62b3f17a198600e683c26cf3d3e87e2) struct bt\_a2dp \*[a2dp](structbt__a2dp__stream.md#ab62b3f17a198600e683c26cf3d3e87e2);

[ 641](structbt__a2dp__stream.md#aff775fe292618da4de467aa96cbf79b0) struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) [codec\_config](structbt__a2dp__stream.md#aff775fe292618da4de467aa96cbf79b0);

642};

643

[ 645](structbt__a2dp__stream__ops.md)struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) {

[ 653](structbt__a2dp__stream__ops.md#a146f907aa60ae130b3248da7475db0cb) void (\*[configured](structbt__a2dp__stream__ops.md#a146f907aa60ae130b3248da7475db0cb))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 661](structbt__a2dp__stream__ops.md#a88d7a0598a5af6740747eb575b8b57df) void (\*[established](structbt__a2dp__stream__ops.md#a88d7a0598a5af6740747eb575b8b57df))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 670](structbt__a2dp__stream__ops.md#acaa2c8b7e59a0b0bb652c9801110234b) void (\*[released](structbt__a2dp__stream__ops.md#acaa2c8b7e59a0b0bb652c9801110234b))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 678](structbt__a2dp__stream__ops.md#a292e604e7db2faca1915533eab76830e) void (\*[started](structbt__a2dp__stream__ops.md#a292e604e7db2faca1915533eab76830e))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 686](structbt__a2dp__stream__ops.md#af839ecbcb131cb68165c516c2e049fe5) void (\*[suspended](structbt__a2dp__stream__ops.md#af839ecbcb131cb68165c516c2e049fe5))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 695](structbt__a2dp__stream__ops.md#ab45e951ee0854e1f937816ab6115343f) void (\*[aborted](structbt__a2dp__stream__ops.md#ab45e951ee0854e1f937816ab6115343f))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

696#if defined(CONFIG\_BT\_A2DP\_SINK)

703 void (\*[recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num,

704 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

705#endif

706#if defined(CONFIG\_BT\_A2DP\_SOURCE)

719 void (\*sent)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

720#endif

721};

722

[ 731](a2dp_8h.md#ab8459d999437daa7a107b1bdf4c5ea46)void [bt\_a2dp\_stream\_cb\_register](a2dp_8h.md#ab8459d999437daa7a107b1bdf4c5ea46)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) \*[ops](structbt__a2dp__stream.md#aa51509d9f0c50118177345988ddb8fa5));

732

[ 748](a2dp_8h.md#a3ff3ca4cd016025f95690e89643f0ff5)int [bt\_a2dp\_stream\_config](a2dp_8h.md#a3ff3ca4cd016025f95690e89643f0ff5)(struct bt\_a2dp \*[a2dp](structbt__a2dp__stream.md#ab62b3f17a198600e683c26cf3d3e87e2), struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream,

749 struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*[local\_ep](structbt__a2dp__stream.md#aa490bb24525c50cf8c1675a01223420c), struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*[remote\_ep](structbt__a2dp__stream.md#a4ea9de245b573b7d0c495aacd7534099),

750 struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*config);

751

[ 760](a2dp_8h.md#af47e0028176494f5353ee00261ffa49a)int [bt\_a2dp\_stream\_establish](a2dp_8h.md#af47e0028176494f5353ee00261ffa49a)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

761

[ 771](a2dp_8h.md#a194e7ec86715cf9007de30f6492e4f58)int [bt\_a2dp\_stream\_release](a2dp_8h.md#a194e7ec86715cf9007de30f6492e4f58)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

772

[ 781](a2dp_8h.md#a368403c64581b761099631280014d877)int [bt\_a2dp\_stream\_start](a2dp_8h.md#a368403c64581b761099631280014d877)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

782

[ 791](a2dp_8h.md#af22030f4edd5401b2d5359bcb0590145)int [bt\_a2dp\_stream\_suspend](a2dp_8h.md#af22030f4edd5401b2d5359bcb0590145)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

792

[ 802](a2dp_8h.md#a70fc5f43265a4c407a847c4205cd7697)int [bt\_a2dp\_stream\_reconfig](a2dp_8h.md#a70fc5f43265a4c407a847c4205cd7697)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*config);

803

[ 813](a2dp_8h.md#a7999e06ef74be78ec2744bb24ff72912)int [bt\_a2dp\_stream\_abort](a2dp_8h.md#a7999e06ef74be78ec2744bb24ff72912)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

814

[ 821](a2dp_8h.md#afb67c234c9d5748e54d5e67c7b148353)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bt\_a2dp\_get\_mtu](a2dp_8h.md#afb67c234c9d5748e54d5e67c7b148353)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

822

823#if defined(CONFIG\_BT\_A2DP\_SOURCE)

835int bt\_a2dp\_stream\_send(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num,

836 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

837#endif

838

839#ifdef \_\_cplusplus

840}

841#endif

842

843#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_H\_ \*/

[bt\_a2dp\_stream\_release](a2dp_8h.md#a194e7ec86715cf9007de30f6492e4f58)

int bt\_a2dp\_stream\_release(struct bt\_a2dp\_stream \*stream)

release a2dp streamer.

[bt\_a2dp\_stream\_start](a2dp_8h.md#a368403c64581b761099631280014d877)

int bt\_a2dp\_stream\_start(struct bt\_a2dp\_stream \*stream)

start a2dp streamer.

[bt\_a2dp\_stream\_config](a2dp_8h.md#a3ff3ca4cd016025f95690e89643f0ff5)

int bt\_a2dp\_stream\_config(struct bt\_a2dp \*a2dp, struct bt\_a2dp\_stream \*stream, struct bt\_a2dp\_ep \*local\_ep, struct bt\_a2dp\_ep \*remote\_ep, struct bt\_a2dp\_codec\_cfg \*config)

configure endpoint.

[bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c)

bt\_a2dp\_err\_code

A2DP error code.

**Definition** a2dp.h:209

[BT\_A2DP\_INVALID\_CP\_FORMAT](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63)

@ BT\_A2DP\_INVALID\_CP\_FORMAT

The format of Content Protection Service Capability/Content Protection Scheme Dependent Data is not c...

**Definition** a2dp.h:277

[BT\_A2DP\_INVALID\_CODEC\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591)

@ BT\_A2DP\_INVALID\_CODEC\_TYPE

Media Codec Type is not valid.

**Definition** a2dp.h:211

[BT\_A2DP\_INVALID\_CHANNELS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483)

@ BT\_A2DP\_INVALID\_CHANNELS

Either 1) Channels is not valid or 2) None or multiple values have been selected for Channels.

**Definition** a2dp.h:261

[BT\_A2DP\_NOT\_SUPPORTED\_DRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd)

@ BT\_A2DP\_NOT\_SUPPORTED\_DRC

DRC is not supported.

**Definition** a2dp.h:289

[BT\_A2DP\_NOT\_SUPPORTED\_VERSION](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c)

@ BT\_A2DP\_NOT\_SUPPORTED\_VERSION

Version is not supported.

**Definition** a2dp.h:267

[BT\_A2DP\_NOT\_SUPPORTED\_SUBBANDS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d)

@ BT\_A2DP\_NOT\_SUPPORTED\_SUBBANDS

Number of Subbands is not supported.

**Definition** a2dp.h:225

[BT\_A2DP\_NOT\_SUPPORTED\_CHANNELS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a)

@ BT\_A2DP\_NOT\_SUPPORTED\_CHANNELS

Channels is not supported.

**Definition** a2dp.h:263

[BT\_A2DP\_INVALID\_OBJECT\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429)

@ BT\_A2DP\_INVALID\_OBJECT\_TYPE

Either 1) Object type is not valid or 2) None or multiple values have been selected for Object Type.

**Definition** a2dp.h:255

[BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_PARAMETER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9)

@ BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_PARAMETER

The codec parameter is not supported.

**Definition** a2dp.h:285

[BT\_A2DP\_INVALID\_VERSION](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d)

@ BT\_A2DP\_INVALID\_VERSION

Version is not valid.

**Definition** a2dp.h:265

[BT\_A2DP\_NOT\_SUPPORTED\_LAYER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e)

@ BT\_A2DP\_NOT\_SUPPORTED\_LAYER

Layer is not supported.

**Definition** a2dp.h:241

[BT\_A2DP\_NOT\_SUPPORTED\_SAMPLING\_FREQUENCY](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76)

@ BT\_A2DP\_NOT\_SUPPORTED\_SAMPLING\_FREQUENCY

Sampling Frequency is not supported.

**Definition** a2dp.h:217

[BT\_A2DP\_NOT\_SUPPORTED\_CRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec)

@ BT\_A2DP\_NOT\_SUPPORTED\_CRC

CRC is not supported.

**Definition** a2dp.h:243

[BT\_A2DP\_INVALID\_CHANNEL\_MODE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396)

@ BT\_A2DP\_INVALID\_CHANNEL\_MODE

Channel Mode is not valid or multiple values have been selected.

**Definition** a2dp.h:219

[BT\_A2DP\_INVALID\_SAMPLING\_FREQUENCY](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c)

@ BT\_A2DP\_INVALID\_SAMPLING\_FREQUENCY

Sampling Frequency is not valid or multiple values have been selected.

**Definition** a2dp.h:215

[BT\_A2DP\_INVALID\_MAXIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf)

@ BT\_A2DP\_INVALID\_MAXIMUM\_BITPOOL\_VALUE

Maximum Bitpool Value is not valid.

**Definition** a2dp.h:235

[BT\_A2DP\_NOT\_SUPPORTED\_OBJECT\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615)

@ BT\_A2DP\_NOT\_SUPPORTED\_OBJECT\_TYPE

Object Type is not supported.

**Definition** a2dp.h:257

[BT\_A2DP\_NOT\_SUPPORTED\_ALLOCATION\_METHOD](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8)

@ BT\_A2DP\_NOT\_SUPPORTED\_ALLOCATION\_METHOD

Allocation Method is not supported.

**Definition** a2dp.h:229

[BT\_A2DP\_INVALID\_SUBBANDS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f)

@ BT\_A2DP\_INVALID\_SUBBANDS

None or multiple values have been selected for Number of Subbands.

**Definition** a2dp.h:223

[BT\_A2DP\_NOT\_SUPPORTED\_CHANNEL\_MODE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755)

@ BT\_A2DP\_NOT\_SUPPORTED\_CHANNEL\_MODE

Channel Mode is not supported.

**Definition** a2dp.h:221

[BT\_A2DP\_NOT\_SUPPORTED\_VBR](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51)

@ BT\_A2DP\_NOT\_SUPPORTED\_VBR

VBR is not supported.

**Definition** a2dp.h:247

[BT\_A2DP\_NOT\_SUPPORTED\_MPF](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f)

@ BT\_A2DP\_NOT\_SUPPORTED\_MPF

MPF-2 is not supported.

**Definition** a2dp.h:245

[BT\_A2DP\_INVALID\_CODEC\_PARAMETER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396)

@ BT\_A2DP\_INVALID\_CODEC\_PARAMETER

The codec parameter is invalid.

**Definition** a2dp.h:281

[BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f)

@ BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_BITPOOL\_VALUE

Maximum Bitpool Value is not supported.

**Definition** a2dp.h:237

[BT\_A2DP\_INVALID\_CP\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611)

@ BT\_A2DP\_INVALID\_CP\_TYPE

The requested CP Type is not supported.

**Definition** a2dp.h:273

[BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f)

@ BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_TYPE

Media Codec Type is not supported.

**Definition** a2dp.h:213

[BT\_A2DP\_NOT\_SUPPORTED\_MINIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3)

@ BT\_A2DP\_NOT\_SUPPORTED\_MINIMUM\_BITPOOL\_VALUE

Minimum Bitpool Value is not supported.

**Definition** a2dp.h:233

[BT\_A2DP\_INVALID\_MINIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02)

@ BT\_A2DP\_INVALID\_MINIMUM\_BITPOOL\_VALUE

Minimum Bitpool Value is not valid.

**Definition** a2dp.h:231

[BT\_A2DP\_INVALID\_BIT\_RATE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476)

@ BT\_A2DP\_INVALID\_BIT\_RATE

None or multiple values have been selected for Bit Rate.

**Definition** a2dp.h:249

[BT\_A2DP\_INVALID\_BLOCK\_LENGTH](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3)

@ BT\_A2DP\_INVALID\_BLOCK\_LENGTH

None or multiple values have been selected for Block Length.

**Definition** a2dp.h:271

[BT\_A2DP\_INVALID\_ALLOCATION\_METHOD](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a)

@ BT\_A2DP\_INVALID\_ALLOCATION\_METHOD

None or multiple values have been selected for Allocation Method.

**Definition** a2dp.h:227

[BT\_A2DP\_INVALID\_LAYER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41)

@ BT\_A2DP\_INVALID\_LAYER

None or multiple values have been selected for Layer.

**Definition** a2dp.h:239

[BT\_A2DP\_NOT\_SUPPORTED\_BIT\_RATE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1)

@ BT\_A2DP\_NOT\_SUPPORTED\_BIT\_RATE

Bit Rate is not supported.

**Definition** a2dp.h:251

[BT\_A2DP\_INVALID\_DRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96)

@ BT\_A2DP\_INVALID\_DRC

Combination of Object Type and DRC is invalid.

**Definition** a2dp.h:287

[BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_SUL](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b)

@ BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_SUL

Maximum SUL is not acceptable for the Decoder in the SNK.

**Definition** a2dp.h:269

[bt\_a2dp\_register\_cb](a2dp_8h.md#a4af29d7c162743c00534868ba945b7ec)

int bt\_a2dp\_register\_cb(struct bt\_a2dp\_cb \*cb)

register callback.

[bt\_a2dp\_stream\_reconfig](a2dp_8h.md#a70fc5f43265a4c407a847c4205cd7697)

int bt\_a2dp\_stream\_reconfig(struct bt\_a2dp\_stream \*stream, struct bt\_a2dp\_codec\_cfg \*config)

re-configure a2dp streamer

[BT\_A2DP\_DISCOVER\_EP\_STOP](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2)

@ BT\_A2DP\_DISCOVER\_EP\_STOP

**Definition** a2dp.h:351

[BT\_A2DP\_DISCOVER\_EP\_CONTINUE](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367)

@ BT\_A2DP\_DISCOVER\_EP\_CONTINUE

**Definition** a2dp.h:352

[bt\_a2dp\_stream\_abort](a2dp_8h.md#a7999e06ef74be78ec2744bb24ff72912)

int bt\_a2dp\_stream\_abort(struct bt\_a2dp\_stream \*stream)

abort a2dp streamer.

[BT\_A2DP\_MAX\_IE\_LENGTH](a2dp_8h.md#a8c365793c40e8425d9e002208bc7863f)

#define BT\_A2DP\_MAX\_IE\_LENGTH

The max IE (Codec Info Element) length.

**Definition** a2dp.h:33

[bt\_a2dp\_discover](a2dp_8h.md#a931234227bc2b9eaed9cd60471ee54db)

int bt\_a2dp\_discover(struct bt\_a2dp \*a2dp, struct bt\_a2dp\_discover\_param \*param)

Discover remote endpoints.

[bt\_a2dp\_register\_ep](a2dp_8h.md#ab1cd7028a41bfdc34ce8cc60aed239de)

int bt\_a2dp\_register\_ep(struct bt\_a2dp\_ep \*ep, uint8\_t media\_type, uint8\_t sep\_type)

Endpoint Registration.

[bt\_a2dp\_stream\_cb\_register](a2dp_8h.md#ab8459d999437daa7a107b1bdf4c5ea46)

void bt\_a2dp\_stream\_cb\_register(struct bt\_a2dp\_stream \*stream, struct bt\_a2dp\_stream\_ops \*ops)

Register Audio callbacks for a stream.

[bt\_a2dp\_disconnect](a2dp_8h.md#abbf0d012860a233ecc84ed333e0da051)

int bt\_a2dp\_disconnect(struct bt\_a2dp \*a2dp)

disconnect l2cap a2dp

[bt\_a2dp\_connect](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)

struct bt\_a2dp \* bt\_a2dp\_connect(struct bt\_conn \*conn)

A2DP Connect.

[bt\_a2dp\_discover\_ep\_cb](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed)

uint8\_t(\* bt\_a2dp\_discover\_ep\_cb)(struct bt\_a2dp \*a2dp, struct bt\_a2dp\_ep\_info \*info, struct bt\_a2dp\_ep \*\*ep)

Called when a stream endpoint is discovered.

**Definition** a2dp.h:380

[bt\_a2dp\_stream\_suspend](a2dp_8h.md#af22030f4edd5401b2d5359bcb0590145)

int bt\_a2dp\_stream\_suspend(struct bt\_a2dp\_stream \*stream)

suspend a2dp streamer.

[bt\_a2dp\_stream\_establish](a2dp_8h.md#af47e0028176494f5353ee00261ffa49a)

int bt\_a2dp\_stream\_establish(struct bt\_a2dp\_stream \*stream)

establish a2dp streamer.

[bt\_a2dp\_get\_mtu](a2dp_8h.md#afb67c234c9d5748e54d5e67c7b148353)

uint32\_t bt\_a2dp\_get\_mtu(struct bt\_a2dp\_stream \*stream)

get the stream l2cap mtu

[bt\_a2dp\_codec\_type](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6)

bt\_a2dp\_codec\_type

Codec Type.

**Definition** a2dp.h:293

[BT\_A2DP\_MPEG1](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497)

@ BT\_A2DP\_MPEG1

Codec MPEG-1.

**Definition** a2dp.h:297

[BT\_A2DP\_ATRAC](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83)

@ BT\_A2DP\_ATRAC

Codec ATRAC.

**Definition** a2dp.h:301

[BT\_A2DP\_SBC](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00)

@ BT\_A2DP\_SBC

Codec SBC.

**Definition** a2dp.h:295

[BT\_A2DP\_VENDOR](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701)

@ BT\_A2DP\_VENDOR

Codec Non-A2DP.

**Definition** a2dp.h:303

[BT\_A2DP\_MPEG2](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88)

@ BT\_A2DP\_MPEG2

Codec MPEG-2.

**Definition** a2dp.h:299

[avdtp.h](avdtp_8h.md)

Audio/Video Distribution Transport Protocol header.

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[l2cap.h](l2cap_8h.md)

Bluetooth L2CAP handling.

[recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)

ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_a2dp\_cb](structbt__a2dp__cb.md)

The connecting callback.

**Definition** a2dp.h:397

[bt\_a2dp\_cb::start\_req](structbt__a2dp__cb.md#a1388b0365e46afce78b4f08f25af6858)

int(\* start\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

Stream start request callback.

**Definition** a2dp.h:516

[bt\_a2dp\_cb::config\_rsp](structbt__a2dp__cb.md#a3b2f6c42bcdefe8a2591fc59c2357786)

void(\* config\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_config() and bt\_a2dp\_stream\_reconfig().

**Definition** a2dp.h:457

[bt\_a2dp\_cb::start\_rsp](structbt__a2dp__cb.md#a49bae91e1cac18a5da90160214a61725)

void(\* start\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_start().

**Definition** a2dp.h:525

[bt\_a2dp\_cb::suspend\_rsp](structbt__a2dp__cb.md#a6064e5d61acb3cdd0f83246ce90e712f)

void(\* suspend\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_suspend().

**Definition** a2dp.h:547

[bt\_a2dp\_cb::suspend\_req](structbt__a2dp__cb.md#a79d2edefa0e6e979bfcfcffe9391a7c0)

int(\* suspend\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

Stream suspend request callback.

**Definition** a2dp.h:538

[bt\_a2dp\_cb::disconnected](structbt__a2dp__cb.md#a80401da71ae6dc74d058163624f78518)

void(\* disconnected)(struct bt\_a2dp \*a2dp)

A a2dp connection has been disconnected.

**Definition** a2dp.h:416

[bt\_a2dp\_cb::abort\_req](structbt__a2dp__cb.md#a81fe4d6d5db8ad1cf541b141c0bca18f)

int(\* abort\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

Stream abort request callback.

**Definition** a2dp.h:560

[bt\_a2dp\_cb::release\_req](structbt__a2dp__cb.md#a90a637e6e81bf5a74c878c3b4b2e63c0)

int(\* release\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

Stream release request callback.

**Definition** a2dp.h:493

[bt\_a2dp\_cb::config\_req](structbt__a2dp__cb.md#aab8f5f53a7b507d55e1d594995739222)

int(\* config\_req)(struct bt\_a2dp \*a2dp, struct bt\_a2dp\_ep \*ep, struct bt\_a2dp\_codec\_cfg \*codec\_cfg, struct bt\_a2dp\_stream \*\*stream, uint8\_t \*rsp\_err\_code)

Endpoint config request callback.

**Definition** a2dp.h:432

[bt\_a2dp\_cb::connected](structbt__a2dp__cb.md#ab0b6a895c2f050ab0961325b8ce7e862)

void(\* connected)(struct bt\_a2dp \*a2dp, int err)

A a2dp connection has been established.

**Definition** a2dp.h:408

[bt\_a2dp\_cb::release\_rsp](structbt__a2dp__cb.md#ab4c148eb7be896dec8f6a33217b475e1)

void(\* release\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_release().

**Definition** a2dp.h:503

[bt\_a2dp\_cb::reconfig\_req](structbt__a2dp__cb.md#aba09a3ccebcd77068028d22036d6b53d)

int(\* reconfig\_req)(struct bt\_a2dp\_stream \*stream, struct bt\_a2dp\_codec\_cfg \*codec\_cfg, uint8\_t \*rsp\_err\_code)

Endpoint config request callback.

**Definition** a2dp.h:447

[bt\_a2dp\_cb::establish\_req](structbt__a2dp__cb.md#adc611ad1a28c3da94f261cc94f63698f)

int(\* establish\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

Stream establishment request callback.

**Definition** a2dp.h:470

[bt\_a2dp\_cb::abort\_rsp](structbt__a2dp__cb.md#af051e057f504b1d9c8da4e4958fba115)

void(\* abort\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_abort().

**Definition** a2dp.h:569

[bt\_a2dp\_cb::establish\_rsp](structbt__a2dp__cb.md#af19a1f6bb65c60cb0ec7294e66468ba6)

void(\* establish\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_establish().

**Definition** a2dp.h:480

[bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md)

The endpoint configuration.

**Definition** a2dp.h:321

[bt\_a2dp\_codec\_cfg::codec\_config](structbt__a2dp__codec__cfg.md#a178eb806a01729d940e6e8c34b0fb513)

struct bt\_a2dp\_codec\_ie \* codec\_config

The media codec configuration content.

**Definition** a2dp.h:323

[bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md)

codec information elements for the endpoint

**Definition** a2dp.h:313

[bt\_a2dp\_codec\_ie::len](structbt__a2dp__codec__ie.md#a8ba1a0bfcbfd180cb19fb7c4a4ce8225)

uint8\_t len

Length of codec\_cap.

**Definition** a2dp.h:315

[bt\_a2dp\_codec\_ie::codec\_ie](structbt__a2dp__codec__ie.md#acf258c8d4b123e3765ad7e2568ac43aa)

uint8\_t codec\_ie[(8U)]

codec information element

**Definition** a2dp.h:317

[bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md)

**Definition** a2dp.h:383

[bt\_a2dp\_discover\_param::info](structbt__a2dp__discover__param.md#a14b69e2449f1d2379183690246f55a88)

struct bt\_a2dp\_ep\_info info

The discovered endpoint info that is callbacked by cb.

**Definition** a2dp.h:387

[bt\_a2dp\_discover\_param::sep\_count](structbt__a2dp__discover__param.md#a382ce8462958f69af19e325491c6f01b)

uint8\_t sep\_count

The max count of seps (stream endpoint) that can be got in this call route.

**Definition** a2dp.h:393

[bt\_a2dp\_discover\_param::cb](structbt__a2dp__discover__param.md#a806fdbaf6d26ad269608afaa21c2035f)

bt\_a2dp\_discover\_ep\_cb cb

discover callback

**Definition** a2dp.h:385

[bt\_a2dp\_discover\_param::seps\_info](structbt__a2dp__discover__param.md#ab4174f0b43d1804192cd4647d29779d3)

struct bt\_avdtp\_sep\_info \* seps\_info

The max count of remote endpoints that can be got, it save endpoint info internally.

**Definition** a2dp.h:391

[bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md)

**Definition** a2dp.h:338

[bt\_a2dp\_ep\_info::sep\_info](structbt__a2dp__ep__info.md#a114c3b267587efa71922e31e474fd8e4)

struct bt\_avdtp\_sep\_info sep\_info

Stream End Point Information.

**Definition** a2dp.h:344

[bt\_a2dp\_ep\_info::codec\_cap](structbt__a2dp__ep__info.md#a7647012b4ea73a0124e2a3239a3bad7b)

struct bt\_a2dp\_codec\_ie codec\_cap

Codec capabilities, if SBC, use function of a2dp\_codec\_sbc.h to parse it.

**Definition** a2dp.h:342

[bt\_a2dp\_ep\_info::codec\_type](structbt__a2dp__ep__info.md#aca4f893b087a8429dd104b67114e36d7)

uint8\_t codec\_type

Code Type bt\_a2dp\_codec\_type.

**Definition** a2dp.h:340

[bt\_a2dp\_ep](structbt__a2dp__ep.md)

Stream End Point.

**Definition** a2dp.h:327

[bt\_a2dp\_ep::sep](structbt__a2dp__ep.md#a2565b03e09e5abcf239c4c671b348c50)

struct bt\_avdtp\_sep sep

AVDTP Stream End Point Identifier.

**Definition** a2dp.h:333

[bt\_a2dp\_ep::stream](structbt__a2dp__ep.md#a4902b9fde9be1aa9b7a35c22a21cd4a6)

struct bt\_a2dp\_stream \* stream

**Definition** a2dp.h:335

[bt\_a2dp\_ep::codec\_type](structbt__a2dp__ep.md#a912cf7cd18a58a1cc1a5e326e8bebb73)

uint8\_t codec\_type

Code Type bt\_a2dp\_codec\_type.

**Definition** a2dp.h:329

[bt\_a2dp\_ep::codec\_cap](structbt__a2dp__ep.md#ae4dcc7f4bca5cc34cf05c2277379a1b3)

struct bt\_a2dp\_codec\_ie \* codec\_cap

Capabilities.

**Definition** a2dp.h:331

[bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md)

The stream endpoint related operations.

**Definition** a2dp.h:645

[bt\_a2dp\_stream\_ops::configured](structbt__a2dp__stream__ops.md#a146f907aa60ae130b3248da7475db0cb)

void(\* configured)(struct bt\_a2dp\_stream \*stream)

Stream configured callback.

**Definition** a2dp.h:653

[bt\_a2dp\_stream\_ops::started](structbt__a2dp__stream__ops.md#a292e604e7db2faca1915533eab76830e)

void(\* started)(struct bt\_a2dp\_stream \*stream)

Stream start callback.

**Definition** a2dp.h:678

[bt\_a2dp\_stream\_ops::established](structbt__a2dp__stream__ops.md#a88d7a0598a5af6740747eb575b8b57df)

void(\* established)(struct bt\_a2dp\_stream \*stream)

Stream establishment callback.

**Definition** a2dp.h:661

[bt\_a2dp\_stream\_ops::aborted](structbt__a2dp__stream__ops.md#ab45e951ee0854e1f937816ab6115343f)

void(\* aborted)(struct bt\_a2dp\_stream \*stream)

Stream abort callback.

**Definition** a2dp.h:695

[bt\_a2dp\_stream\_ops::released](structbt__a2dp__stream__ops.md#acaa2c8b7e59a0b0bb652c9801110234b)

void(\* released)(struct bt\_a2dp\_stream \*stream)

Stream release callback.

**Definition** a2dp.h:670

[bt\_a2dp\_stream\_ops::suspended](structbt__a2dp__stream__ops.md#af839ecbcb131cb68165c516c2e049fe5)

void(\* suspended)(struct bt\_a2dp\_stream \*stream)

Stream suspend callback.

**Definition** a2dp.h:686

[bt\_a2dp\_stream](structbt__a2dp__stream.md)

A2DP Stream.

**Definition** a2dp.h:629

[bt\_a2dp\_stream::remote\_ep\_id](structbt__a2dp__stream.md#a3361f68c31075014c2c3cf62494ff3ec)

uint8\_t remote\_ep\_id

remote endpoint's Stream End Point ID

**Definition** a2dp.h:635

[bt\_a2dp\_stream::remote\_ep](structbt__a2dp__stream.md#a4ea9de245b573b7d0c495aacd7534099)

struct bt\_a2dp\_ep \* remote\_ep

remote endpoint

**Definition** a2dp.h:633

[bt\_a2dp\_stream::local\_ep](structbt__a2dp__stream.md#aa490bb24525c50cf8c1675a01223420c)

struct bt\_a2dp\_ep \* local\_ep

local endpoint

**Definition** a2dp.h:631

[bt\_a2dp\_stream::ops](structbt__a2dp__stream.md#aa51509d9f0c50118177345988ddb8fa5)

struct bt\_a2dp\_stream\_ops \* ops

Audio stream operations.

**Definition** a2dp.h:637

[bt\_a2dp\_stream::a2dp](structbt__a2dp__stream.md#ab62b3f17a198600e683c26cf3d3e87e2)

struct bt\_a2dp \* a2dp

the a2dp connection

**Definition** a2dp.h:639

[bt\_a2dp\_stream::codec\_config](structbt__a2dp__stream.md#aff775fe292618da4de467aa96cbf79b0)

struct bt\_a2dp\_codec\_ie codec\_config

the stream current configuration

**Definition** a2dp.h:641

[bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md)

AVDTP stream endpoint information.

**Definition** avdtp.h:88

[bt\_avdtp\_sep](structbt__avdtp__sep.md)

AVDTP Stream End Point.

**Definition** avdtp.h:124

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [a2dp.h](a2dp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
