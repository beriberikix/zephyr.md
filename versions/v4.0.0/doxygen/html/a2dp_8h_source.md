---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/a2dp_8h_source.html
original_path: doxygen/html/a2dp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

[ 24](a2dp_8h.md#a9fce344cfaa8b96ca41a5866f9e3b3d1)#define BT\_A2DP\_STREAM\_BUF\_RESERVE (12u + BT\_L2CAP\_BUF\_SIZE(0))

25

[ 27](a2dp_8h.md#af83aa927ac312cfc8577056afffeae56)#define BT\_A2DP\_SBC\_IE\_LENGTH (4u)

[ 29](a2dp_8h.md#a313fec2276421be6f29c0309e67755eb)#define BT\_A2DP\_MPEG\_1\_2\_IE\_LENGTH (4u)

[ 31](a2dp_8h.md#a73ae4b6e2913b3772b32c520bf84de8c)#define BT\_A2DP\_MPEG\_2\_4\_IE\_LENGTH (6u)

[ 33](a2dp_8h.md#ab42c7fe29752fb43bb573a752de9c693)#define A2DP\_MAX\_IE\_LENGTH (8U)

34

[ 40](a2dp_8h.md#afe0cc7b22a941d272de4f8353865d626)#define BT\_A2DP\_EP\_INIT(\_role, \_codec, \_capability)\

41{\

42 .codec\_type = \_codec,\

43 .sep = {.sep\_info = {.media\_type = BT\_AVDTP\_AUDIO, .tsep = \_role}},\

44 .codec\_cap = \_capability,\

45 .stream = NULL,\

46}

47

[ 52](a2dp_8h.md#a892825546a211982b8809dc0f7596ba2)#define BT\_A2DP\_SINK\_EP\_INIT(\_codec, \_capability)\

53BT\_A2DP\_EP\_INIT(BT\_AVDTP\_SINK, \_codec, \_capability)

54

[ 59](a2dp_8h.md#a78089fb18ea7a16dff7ba05370bb452c)#define BT\_A2DP\_SOURCE\_EP\_INIT(\_codec, \_capability)\

60BT\_A2DP\_EP\_INIT(BT\_AVDTP\_SOURCE, \_codec, \_capability)

61

[ 83](a2dp_8h.md#abf08745833eacb9b409627442ac4c8a2)#define BT\_A2DP\_SBC\_SINK\_EP(\_name, \_freq, \_ch\_mode, \_blk\_len, \_subband,\

84\_alloc\_mthd, \_min\_bitpool, \_max\_bitpool)\

85static struct bt\_a2dp\_codec\_ie bt\_a2dp\_ep\_cap\_ie##\_name =\

86{.len = BT\_A2DP\_SBC\_IE\_LENGTH, .codec\_ie = {\_freq | \_ch\_mode,\

87\_blk\_len | \_subband | \_alloc\_mthd, \_min\_bitpool, \_max\_bitpool}};\

88static struct bt\_a2dp\_ep \_name = BT\_A2DP\_SINK\_EP\_INIT(BT\_A2DP\_SBC,\

89(&bt\_a2dp\_ep\_cap\_ie##\_name))

90

[ 111](a2dp_8h.md#a9b9d32d04f96f64d7c5f9bf10e03f9a8)#define BT\_A2DP\_SBC\_SOURCE\_EP(\_name, \_freq, \_ch\_mode, \_blk\_len, \_subband,\

112\_alloc\_mthd, \_min\_bitpool, \_max\_bitpool)\

113static struct bt\_a2dp\_codec\_ie bt\_a2dp\_ep\_cap\_ie##\_name =\

114{.len = BT\_A2DP\_SBC\_IE\_LENGTH, .codec\_ie = {\_freq | \_ch\_mode,\

115\_blk\_len | \_subband | \_alloc\_mthd, \_min\_bitpool, \_max\_bitpool}};\

116static struct bt\_a2dp\_ep \_name = BT\_A2DP\_SOURCE\_EP\_INIT(BT\_A2DP\_SBC,\

117&bt\_a2dp\_ep\_cap\_ie##\_name)

118

[ 127](a2dp_8h.md#a76fb351efe2730311baae1ad6cddbcb1)#define BT\_A2DP\_SBC\_SINK\_EP\_DEFAULT(\_name)\

128static struct bt\_a2dp\_codec\_ie bt\_a2dp\_ep\_cap\_ie##\_name =\

129{.len = BT\_A2DP\_SBC\_IE\_LENGTH, .codec\_ie = {A2DP\_SBC\_SAMP\_FREQ\_44100 |\

130A2DP\_SBC\_SAMP\_FREQ\_48000 | A2DP\_SBC\_CH\_MODE\_MONO | A2DP\_SBC\_CH\_MODE\_STREO |\

131A2DP\_SBC\_CH\_MODE\_JOINT, A2DP\_SBC\_BLK\_LEN\_16 |\

132A2DP\_SBC\_SUBBAND\_8 | A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS, 18U, 35U}};\

133static struct bt\_a2dp\_ep \_name = BT\_A2DP\_SINK\_EP\_INIT(BT\_A2DP\_SBC,\

134&bt\_a2dp\_ep\_cap\_ie##\_name)

135

[ 144](a2dp_8h.md#a6830ae27e85471935ae604b18cf779e2)#define BT\_A2DP\_SBC\_SOURCE\_EP\_DEFAULT(\_name)\

145static struct bt\_a2dp\_codec\_ie bt\_a2dp\_ep\_cap\_ie##\_name =\

146{.len = BT\_A2DP\_SBC\_IE\_LENGTH, .codec\_ie = {A2DP\_SBC\_SAMP\_FREQ\_44100 | \

147A2DP\_SBC\_SAMP\_FREQ\_48000 | A2DP\_SBC\_CH\_MODE\_MONO | A2DP\_SBC\_CH\_MODE\_STREO | \

148A2DP\_SBC\_CH\_MODE\_JOINT, A2DP\_SBC\_BLK\_LEN\_16 | A2DP\_SBC\_SUBBAND\_8 | A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS,\

14918U, 35U},};\

150static struct bt\_a2dp\_ep \_name = BT\_A2DP\_SOURCE\_EP\_INIT(BT\_A2DP\_SBC,\

151&bt\_a2dp\_ep\_cap\_ie##\_name)

152

[ 169](a2dp_8h.md#ac879cbea5f0bbecfc0ec948d6e46c073)#define BT\_A2DP\_SBC\_EP\_CFG(\_name, \_freq\_cfg, \_ch\_mode\_cfg, \_blk\_len\_cfg, \_subband\_cfg,\

170\_alloc\_mthd\_cfg, \_min\_bitpool\_cfg, \_max\_bitpool\_cfg)\

171static struct bt\_a2dp\_codec\_ie bt\_a2dp\_codec\_ie##\_name = {\

172.len = BT\_A2DP\_SBC\_IE\_LENGTH, .codec\_ie = {\_freq\_cfg | \_ch\_mode\_cfg,\

173\_blk\_len\_cfg | \_subband\_cfg | \_alloc\_mthd\_cfg, \_min\_bitpool\_cfg, \_max\_bitpool\_cfg},};\

174struct bt\_a2dp\_codec\_cfg \_name = {.codec\_config = &bt\_a2dp\_codec\_ie##\_name,}

175

[ 181](a2dp_8h.md#abbfd3bc3fa080517ef4395b30fd697f7)#define BT\_A2DP\_SBC\_EP\_CFG\_DEFAULT(\_name, \_freq\_cfg)\

182static struct bt\_a2dp\_codec\_ie bt\_a2dp\_codec\_ie##\_name = {\

183.len = BT\_A2DP\_SBC\_IE\_LENGTH, .codec\_ie = {\_freq\_cfg | A2DP\_SBC\_CH\_MODE\_JOINT,\

184A2DP\_SBC\_BLK\_LEN\_16 | A2DP\_SBC\_SUBBAND\_8 | A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS, 18U, 35U},};\

185struct bt\_a2dp\_codec\_cfg \_name = {.codec\_config = &bt\_a2dp\_codec\_ie##\_name,}

186

[ 190](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c)enum [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c) {

[ 192](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591) [BT\_A2DP\_INVALID\_CODEC\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591) = 0xC1,

[ 194](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f) [BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f) = 0xC2,

[ 196](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c) [BT\_A2DP\_INVALID\_SAMPLING\_FREQUENCY](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c) = 0xC3,

[ 198](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76) [BT\_A2DP\_NOT\_SUPPORTED\_SAMPLING\_FREQUENCY](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76) = 0xC4,

[ 200](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396) [BT\_A2DP\_INVALID\_CHANNEL\_MODE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396) = 0xC5,

[ 202](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755) [BT\_A2DP\_NOT\_SUPPORTED\_CHANNEL\_MODE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755) = 0xC6,

[ 204](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f) [BT\_A2DP\_INVALID\_SUBBANDS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f) = 0xC7,

[ 206](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d) [BT\_A2DP\_NOT\_SUPPORTED\_SUBBANDS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d) = 0xC8,

[ 208](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a) [BT\_A2DP\_INVALID\_ALLOCATION\_METHOD](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a) = 0xC9,

[ 210](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8) [BT\_A2DP\_NOT\_SUPPORTED\_ALLOCATION\_METHOD](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8) = 0xCA,

[ 212](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02) [BT\_A2DP\_INVALID\_MINIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02) = 0xCB,

[ 214](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3) [BT\_A2DP\_NOT\_SUPPORTED\_MINIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3) = 0xCC,

[ 216](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf) [BT\_A2DP\_INVALID\_MAXIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf) = 0xCD,

[ 218](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f) [BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f) = 0xCE,

[ 220](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41) [BT\_A2DP\_INVALID\_LAYER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41) = 0xCF,

[ 222](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e) [BT\_A2DP\_NOT\_SUPPORTED\_LAYER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e) = 0xD0,

[ 224](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec) [BT\_A2DP\_NOT\_SUPPORTED\_CRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec) = 0xD1,

[ 226](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f) [BT\_A2DP\_NOT\_SUPPORTED\_MPF](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f) = 0xD2,

[ 228](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51) [BT\_A2DP\_NOT\_SUPPORTED\_VBR](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51) = 0xD3,

[ 230](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476) [BT\_A2DP\_INVALID\_BIT\_RATE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476) = 0xD4,

[ 232](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1) [BT\_A2DP\_NOT\_SUPPORTED\_BIT\_RATE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1) = 0xD5,

[ 236](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429) [BT\_A2DP\_INVALID\_OBJECT\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429) = 0xD6,

[ 238](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615) [BT\_A2DP\_NOT\_SUPPORTED\_OBJECT\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615) = 0xD7,

[ 242](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483) [BT\_A2DP\_INVALID\_CHANNELS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483) = 0xD8,

[ 244](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a) [BT\_A2DP\_NOT\_SUPPORTED\_CHANNELS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a) = 0xD9,

[ 246](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d) [BT\_A2DP\_INVALID\_VERSION](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d) = 0xDA,

[ 248](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c) [BT\_A2DP\_NOT\_SUPPORTED\_VERSION](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c) = 0xDB,

[ 250](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b) [BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_SUL](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b) = 0xDC,

[ 252](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3) [BT\_A2DP\_INVALID\_BLOCK\_LENGTH](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3) = 0xDD,

[ 254](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611) [BT\_A2DP\_INVALID\_CP\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611) = 0xE0,

[ 258](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63) [BT\_A2DP\_INVALID\_CP\_FORMAT](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63) = 0xE1,

[ 262](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396) [BT\_A2DP\_INVALID\_CODEC\_PARAMETER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396) = 0xE2,

[ 266](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9) [BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_PARAMETER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9) = 0xE3,

[ 268](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96) [BT\_A2DP\_INVALID\_DRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96) = 0xE4,

[ 270](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd) [BT\_A2DP\_NOT\_SUPPORTED\_DRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd) = 0xE5,

271};

272

[ 274](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6)enum [bt\_a2dp\_codec\_type](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6) {

[ 276](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00) [BT\_A2DP\_SBC](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00) = 0x00,

[ 278](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497) [BT\_A2DP\_MPEG1](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497) = 0x01,

[ 280](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88) [BT\_A2DP\_MPEG2](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88) = 0x02,

[ 282](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83) [BT\_A2DP\_ATRAC](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83) = 0x04,

[ 284](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701) [BT\_A2DP\_VENDOR](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701) = 0xff

285};

286

288struct bt\_a2dp;

289

290/\* Internal to pass build \*/

291struct [bt\_a2dp\_stream](structbt__a2dp__stream.md);

292

[ 294](structbt__a2dp__codec__ie.md)struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) {

[ 296](structbt__a2dp__codec__ie.md#a8ba1a0bfcbfd180cb19fb7c4a4ce8225) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__a2dp__codec__ie.md#a8ba1a0bfcbfd180cb19fb7c4a4ce8225);

[ 298](structbt__a2dp__codec__ie.md#acf258c8d4b123e3765ad7e2568ac43aa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_ie](structbt__a2dp__codec__ie.md#acf258c8d4b123e3765ad7e2568ac43aa)[[A2DP\_MAX\_IE\_LENGTH](a2dp_8h.md#ab42c7fe29752fb43bb573a752de9c693)];

299};

300

[ 302](structbt__a2dp__codec__cfg.md)struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) {

[ 304](structbt__a2dp__codec__cfg.md#a178eb806a01729d940e6e8c34b0fb513) struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) \*[codec\_config](structbt__a2dp__codec__cfg.md#a178eb806a01729d940e6e8c34b0fb513);

305};

306

[ 308](structbt__a2dp__ep.md)struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) {

[ 310](structbt__a2dp__ep.md#a912cf7cd18a58a1cc1a5e326e8bebb73) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_type](structbt__a2dp__ep.md#a912cf7cd18a58a1cc1a5e326e8bebb73);

[ 312](structbt__a2dp__ep.md#ae4dcc7f4bca5cc34cf05c2277379a1b3) struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) \*[codec\_cap](structbt__a2dp__ep.md#ae4dcc7f4bca5cc34cf05c2277379a1b3);

[ 314](structbt__a2dp__ep.md#a2565b03e09e5abcf239c4c671b348c50) struct [bt\_avdtp\_sep](structbt__avdtp__sep.md) [sep](structbt__a2dp__ep.md#a2565b03e09e5abcf239c4c671b348c50);

315 /\* Internally used stream object pointer \*/

[ 316](structbt__a2dp__ep.md#a4902b9fde9be1aa9b7a35c22a21cd4a6) struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*[stream](structbt__a2dp__ep.md#a4902b9fde9be1aa9b7a35c22a21cd4a6);

317};

318

[ 319](structbt__a2dp__ep__info.md)struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) {

[ 321](structbt__a2dp__ep__info.md#aca4f893b087a8429dd104b67114e36d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_type](structbt__a2dp__ep__info.md#aca4f893b087a8429dd104b67114e36d7);

[ 323](structbt__a2dp__ep__info.md#a7647012b4ea73a0124e2a3239a3bad7b) struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) [codec\_cap](structbt__a2dp__ep__info.md#a7647012b4ea73a0124e2a3239a3bad7b);

[ 325](structbt__a2dp__ep__info.md#a114c3b267587efa71922e31e474fd8e4) struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) [sep\_info](structbt__a2dp__ep__info.md#a114c3b267587efa71922e31e474fd8e4);

326};

327

331enum {

[ 332](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2) [BT\_A2DP\_DISCOVER\_EP\_STOP](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2) = 0,

[ 333](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367) [BT\_A2DP\_DISCOVER\_EP\_CONTINUE](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367),

334};

335

[ 361](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_a2dp\_discover\_ep\_cb](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed))(struct bt\_a2dp \*a2dp,

362 struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) \*info, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*\*ep);

363

[ 364](structbt__a2dp__discover__param.md)struct [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md) {

[ 366](structbt__a2dp__discover__param.md#a806fdbaf6d26ad269608afaa21c2035f) [bt\_a2dp\_discover\_ep\_cb](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed) [cb](structbt__a2dp__discover__param.md#a806fdbaf6d26ad269608afaa21c2035f);

[ 368](structbt__a2dp__discover__param.md#a14b69e2449f1d2379183690246f55a88) struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) [info](structbt__a2dp__discover__param.md#a14b69e2449f1d2379183690246f55a88);

[ 372](structbt__a2dp__discover__param.md#ab4174f0b43d1804192cd4647d29779d3) struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) \*[seps\_info](structbt__a2dp__discover__param.md#ab4174f0b43d1804192cd4647d29779d3);

[ 374](structbt__a2dp__discover__param.md#a382ce8462958f69af19e325491c6f01b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sep\_count](structbt__a2dp__discover__param.md#a382ce8462958f69af19e325491c6f01b);

375};

376

[ 378](structbt__a2dp__cb.md)struct [bt\_a2dp\_cb](structbt__a2dp__cb.md) {

[ 389](structbt__a2dp__cb.md#ab0b6a895c2f050ab0961325b8ce7e862) void (\*[connected](structbt__a2dp__cb.md#ab0b6a895c2f050ab0961325b8ce7e862))(struct bt\_a2dp \*a2dp, int err);

[ 397](structbt__a2dp__cb.md#a80401da71ae6dc74d058163624f78518) void (\*[disconnected](structbt__a2dp__cb.md#a80401da71ae6dc74d058163624f78518))(struct bt\_a2dp \*a2dp);

[ 413](structbt__a2dp__cb.md#aab8f5f53a7b507d55e1d594995739222) int (\*[config\_req](structbt__a2dp__cb.md#aab8f5f53a7b507d55e1d594995739222))(struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*ep,

414 struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*codec\_cfg, struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*\*stream,

415 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 424](structbt__a2dp__cb.md#a3b2f6c42bcdefe8a2591fc59c2357786) void (\*[config\_rsp](structbt__a2dp__cb.md#a3b2f6c42bcdefe8a2591fc59c2357786))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 437](structbt__a2dp__cb.md#adc611ad1a28c3da94f261cc94f63698f) int (\*[establish\_req](structbt__a2dp__cb.md#adc611ad1a28c3da94f261cc94f63698f))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 447](structbt__a2dp__cb.md#af19a1f6bb65c60cb0ec7294e66468ba6) void (\*[establish\_rsp](structbt__a2dp__cb.md#af19a1f6bb65c60cb0ec7294e66468ba6))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 460](structbt__a2dp__cb.md#a90a637e6e81bf5a74c878c3b4b2e63c0) int (\*[release\_req](structbt__a2dp__cb.md#a90a637e6e81bf5a74c878c3b4b2e63c0))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 470](structbt__a2dp__cb.md#ab4c148eb7be896dec8f6a33217b475e1) void (\*[release\_rsp](structbt__a2dp__cb.md#ab4c148eb7be896dec8f6a33217b475e1))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 483](structbt__a2dp__cb.md#a1388b0365e46afce78b4f08f25af6858) int (\*[start\_req](structbt__a2dp__cb.md#a1388b0365e46afce78b4f08f25af6858))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 492](structbt__a2dp__cb.md#a49bae91e1cac18a5da90160214a61725) void (\*[start\_rsp](structbt__a2dp__cb.md#a49bae91e1cac18a5da90160214a61725))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 505](structbt__a2dp__cb.md#a79d2edefa0e6e979bfcfcffe9391a7c0) int (\*[suspend\_req](structbt__a2dp__cb.md#a79d2edefa0e6e979bfcfcffe9391a7c0))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 514](structbt__a2dp__cb.md#a6064e5d61acb3cdd0f83246ce90e712f) void (\*[suspend\_rsp](structbt__a2dp__cb.md#a6064e5d61acb3cdd0f83246ce90e712f))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

[ 527](structbt__a2dp__cb.md#a44c7e59f8b14487aa1bbe42b2526aea2) int (\*[reconfig\_req](structbt__a2dp__cb.md#a44c7e59f8b14487aa1bbe42b2526aea2))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code);

[ 536](structbt__a2dp__cb.md#a8a35f295adc0c7d102e3cb7d72a76cf9) void (\*[reconfig\_rsp](structbt__a2dp__cb.md#a8a35f295adc0c7d102e3cb7d72a76cf9))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code);

537};

538

[ 553](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)struct bt\_a2dp \*[bt\_a2dp\_connect](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)(struct bt\_conn \*conn);

554

[ 564](a2dp_8h.md#abbf0d012860a233ecc84ed333e0da051)int [bt\_a2dp\_disconnect](a2dp_8h.md#abbf0d012860a233ecc84ed333e0da051)(struct bt\_a2dp \*a2dp);

565

[ 574](a2dp_8h.md#adccb916ce9ee1a229f7a9f89ec3adc1b)int [bt\_a2dp\_register\_ep](a2dp_8h.md#adccb916ce9ee1a229f7a9f89ec3adc1b)(struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) media\_type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) role);

575

[ 584](a2dp_8h.md#a4af29d7c162743c00534868ba945b7ec)int [bt\_a2dp\_register\_cb](a2dp_8h.md#a4af29d7c162743c00534868ba945b7ec)(struct [bt\_a2dp\_cb](structbt__a2dp__cb.md) \*cb);

585

[ 593](a2dp_8h.md#a931234227bc2b9eaed9cd60471ee54db)int [bt\_a2dp\_discover](a2dp_8h.md#a931234227bc2b9eaed9cd60471ee54db)(struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md) \*param);

594

[ 596](structbt__a2dp__stream.md)struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) {

[ 598](structbt__a2dp__stream.md#aa490bb24525c50cf8c1675a01223420c) struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*[local\_ep](structbt__a2dp__stream.md#aa490bb24525c50cf8c1675a01223420c);

[ 600](structbt__a2dp__stream.md#a4ea9de245b573b7d0c495aacd7534099) struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*[remote\_ep](structbt__a2dp__stream.md#a4ea9de245b573b7d0c495aacd7534099);

[ 602](structbt__a2dp__stream.md#a3361f68c31075014c2c3cf62494ff3ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [remote\_ep\_id](structbt__a2dp__stream.md#a3361f68c31075014c2c3cf62494ff3ec);

[ 604](structbt__a2dp__stream.md#aa51509d9f0c50118177345988ddb8fa5) struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) \*[ops](structbt__a2dp__stream.md#aa51509d9f0c50118177345988ddb8fa5);

[ 606](structbt__a2dp__stream.md#ab62b3f17a198600e683c26cf3d3e87e2) struct bt\_a2dp \*[a2dp](structbt__a2dp__stream.md#ab62b3f17a198600e683c26cf3d3e87e2);

[ 608](structbt__a2dp__stream.md#aff775fe292618da4de467aa96cbf79b0) struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) [codec\_config](structbt__a2dp__stream.md#aff775fe292618da4de467aa96cbf79b0);

609};

610

[ 612](structbt__a2dp__stream__ops.md)struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) {

[ 620](structbt__a2dp__stream__ops.md#a146f907aa60ae130b3248da7475db0cb) void (\*[configured](structbt__a2dp__stream__ops.md#a146f907aa60ae130b3248da7475db0cb))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 628](structbt__a2dp__stream__ops.md#a88d7a0598a5af6740747eb575b8b57df) void (\*[established](structbt__a2dp__stream__ops.md#a88d7a0598a5af6740747eb575b8b57df))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 636](structbt__a2dp__stream__ops.md#acaa2c8b7e59a0b0bb652c9801110234b) void (\*[released](structbt__a2dp__stream__ops.md#acaa2c8b7e59a0b0bb652c9801110234b))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 644](structbt__a2dp__stream__ops.md#a292e604e7db2faca1915533eab76830e) void (\*[started](structbt__a2dp__stream__ops.md#a292e604e7db2faca1915533eab76830e))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 652](structbt__a2dp__stream__ops.md#af839ecbcb131cb68165c516c2e049fe5) void (\*[suspended](structbt__a2dp__stream__ops.md#af839ecbcb131cb68165c516c2e049fe5))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

[ 660](structbt__a2dp__stream__ops.md#aba623932df3dfd4072f20794b71922ab) void (\*[reconfigured](structbt__a2dp__stream__ops.md#aba623932df3dfd4072f20794b71922ab))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

661#if defined(CONFIG\_BT\_A2DP\_SINK)

668 void (\*[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream,

669 struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

670#endif

671#if defined(CONFIG\_BT\_A2DP\_SOURCE)

684 void (\*sent)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

685#endif

686};

687

[ 696](a2dp_8h.md#ab8459d999437daa7a107b1bdf4c5ea46)void [bt\_a2dp\_stream\_cb\_register](a2dp_8h.md#ab8459d999437daa7a107b1bdf4c5ea46)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) \*[ops](structbt__a2dp__stream.md#aa51509d9f0c50118177345988ddb8fa5));

697

[ 713](a2dp_8h.md#a3ff3ca4cd016025f95690e89643f0ff5)int [bt\_a2dp\_stream\_config](a2dp_8h.md#a3ff3ca4cd016025f95690e89643f0ff5)(struct bt\_a2dp \*[a2dp](structbt__a2dp__stream.md#ab62b3f17a198600e683c26cf3d3e87e2), struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream,

714 struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*[local\_ep](structbt__a2dp__stream.md#aa490bb24525c50cf8c1675a01223420c), struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*[remote\_ep](structbt__a2dp__stream.md#a4ea9de245b573b7d0c495aacd7534099),

715 struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*config);

716

[ 725](a2dp_8h.md#af47e0028176494f5353ee00261ffa49a)int [bt\_a2dp\_stream\_establish](a2dp_8h.md#af47e0028176494f5353ee00261ffa49a)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

726

[ 735](a2dp_8h.md#a194e7ec86715cf9007de30f6492e4f58)int [bt\_a2dp\_stream\_release](a2dp_8h.md#a194e7ec86715cf9007de30f6492e4f58)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

736

[ 745](a2dp_8h.md#a368403c64581b761099631280014d877)int [bt\_a2dp\_stream\_start](a2dp_8h.md#a368403c64581b761099631280014d877)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

746

[ 755](a2dp_8h.md#af22030f4edd5401b2d5359bcb0590145)int [bt\_a2dp\_stream\_suspend](a2dp_8h.md#af22030f4edd5401b2d5359bcb0590145)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

756

[ 766](a2dp_8h.md#a70fc5f43265a4c407a847c4205cd7697)int [bt\_a2dp\_stream\_reconfig](a2dp_8h.md#a70fc5f43265a4c407a847c4205cd7697)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*config);

767

[ 774](a2dp_8h.md#afb67c234c9d5748e54d5e67c7b148353)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bt\_a2dp\_get\_mtu](a2dp_8h.md#afb67c234c9d5748e54d5e67c7b148353)(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream);

775

776#if defined(CONFIG\_BT\_A2DP\_SOURCE)

788int bt\_a2dp\_stream\_send(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf,

789 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

790#endif

791

792#ifdef \_\_cplusplus

793}

794#endif

795

796#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_H\_ \*/

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

**Definition** a2dp.h:190

[BT\_A2DP\_INVALID\_CP\_FORMAT](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca0554b3ef221c98b5cb4580ae049a6e63)

@ BT\_A2DP\_INVALID\_CP\_FORMAT

The format of Content Protection Service Capability/Content Protection Scheme Dependent Data is not c...

**Definition** a2dp.h:258

[BT\_A2DP\_INVALID\_CODEC\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1718e53b8632688eb1aa9253248e7591)

@ BT\_A2DP\_INVALID\_CODEC\_TYPE

Media Codec Type is not valid.

**Definition** a2dp.h:192

[BT\_A2DP\_INVALID\_CHANNELS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca182de8e823efe2f6575a900a567b3483)

@ BT\_A2DP\_INVALID\_CHANNELS

Either 1) Channels is not valid or 2) None or multiple values have been selected for Channels.

**Definition** a2dp.h:242

[BT\_A2DP\_NOT\_SUPPORTED\_DRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca198bd8a559eca40d9d95f6edf8a703fd)

@ BT\_A2DP\_NOT\_SUPPORTED\_DRC

DRC is not supported.

**Definition** a2dp.h:270

[BT\_A2DP\_NOT\_SUPPORTED\_VERSION](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca1d4c42781c74ebda2b084fe609ac284c)

@ BT\_A2DP\_NOT\_SUPPORTED\_VERSION

Version is not supported.

**Definition** a2dp.h:248

[BT\_A2DP\_NOT\_SUPPORTED\_SUBBANDS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca2a20d81b47a5b3119988c3702ba1e84d)

@ BT\_A2DP\_NOT\_SUPPORTED\_SUBBANDS

Number of Subbands is not supported.

**Definition** a2dp.h:206

[BT\_A2DP\_NOT\_SUPPORTED\_CHANNELS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3619a0a5c74de24b7dd8bd79b99ca91a)

@ BT\_A2DP\_NOT\_SUPPORTED\_CHANNELS

Channels is not supported.

**Definition** a2dp.h:244

[BT\_A2DP\_INVALID\_OBJECT\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3896984afb4b5d164503bd53f0d4e429)

@ BT\_A2DP\_INVALID\_OBJECT\_TYPE

Either 1) Object type is not valid or 2) None or multiple values have been selected for Object Type.

**Definition** a2dp.h:236

[BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_PARAMETER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca3c801158e7ed2623c2d2930ca91b94a9)

@ BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_PARAMETER

The codec parameter is not supported.

**Definition** a2dp.h:266

[BT\_A2DP\_INVALID\_VERSION](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca47dbe86cbbd2859243995d1d39c46d8d)

@ BT\_A2DP\_INVALID\_VERSION

Version is not valid.

**Definition** a2dp.h:246

[BT\_A2DP\_NOT\_SUPPORTED\_LAYER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca48b381cca4ddd1ccb26037e84b0bea9e)

@ BT\_A2DP\_NOT\_SUPPORTED\_LAYER

Layer is not supported.

**Definition** a2dp.h:222

[BT\_A2DP\_NOT\_SUPPORTED\_SAMPLING\_FREQUENCY](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca499c532b0069432802cbe72bc33e5a76)

@ BT\_A2DP\_NOT\_SUPPORTED\_SAMPLING\_FREQUENCY

Sampling Frequency is not supported.

**Definition** a2dp.h:198

[BT\_A2DP\_NOT\_SUPPORTED\_CRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca4e204c6ea5acfe20be37da6fca38eaec)

@ BT\_A2DP\_NOT\_SUPPORTED\_CRC

CRC is not supported.

**Definition** a2dp.h:224

[BT\_A2DP\_INVALID\_CHANNEL\_MODE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca6222f61712e16dbd0b56fda692844396)

@ BT\_A2DP\_INVALID\_CHANNEL\_MODE

Channel Mode is not valid or multiple values have been selected.

**Definition** a2dp.h:200

[BT\_A2DP\_INVALID\_SAMPLING\_FREQUENCY](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca68471cd1037db6687bc1f60cf500681c)

@ BT\_A2DP\_INVALID\_SAMPLING\_FREQUENCY

Sampling Frequency is not valid or multiple values have been selected.

**Definition** a2dp.h:196

[BT\_A2DP\_INVALID\_MAXIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca71dfaa290af68147e83541e37d59d5cf)

@ BT\_A2DP\_INVALID\_MAXIMUM\_BITPOOL\_VALUE

Maximum Bitpool Value is not valid.

**Definition** a2dp.h:216

[BT\_A2DP\_NOT\_SUPPORTED\_OBJECT\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca7b5bafd55d8020029e429b142c572615)

@ BT\_A2DP\_NOT\_SUPPORTED\_OBJECT\_TYPE

Object Type is not supported.

**Definition** a2dp.h:238

[BT\_A2DP\_NOT\_SUPPORTED\_ALLOCATION\_METHOD](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca81723b89ccf0d40db2a2edacd2cbaca8)

@ BT\_A2DP\_NOT\_SUPPORTED\_ALLOCATION\_METHOD

Allocation Method is not supported.

**Definition** a2dp.h:210

[BT\_A2DP\_INVALID\_SUBBANDS](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e06f678574f38b9538f8c45622cee3f)

@ BT\_A2DP\_INVALID\_SUBBANDS

None or multiple values have been selected for Number of Subbands.

**Definition** a2dp.h:204

[BT\_A2DP\_NOT\_SUPPORTED\_CHANNEL\_MODE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca8e62e8df4d9e2a5389ad1620de7af755)

@ BT\_A2DP\_NOT\_SUPPORTED\_CHANNEL\_MODE

Channel Mode is not supported.

**Definition** a2dp.h:202

[BT\_A2DP\_NOT\_SUPPORTED\_VBR](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca92d1fb010cc69e27ec988de69c9bbd51)

@ BT\_A2DP\_NOT\_SUPPORTED\_VBR

VBR is not supported.

**Definition** a2dp.h:228

[BT\_A2DP\_NOT\_SUPPORTED\_MPF](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca95a7b280dbdb757fab3b8b2077120d8f)

@ BT\_A2DP\_NOT\_SUPPORTED\_MPF

MPF-2 is not supported.

**Definition** a2dp.h:226

[BT\_A2DP\_INVALID\_CODEC\_PARAMETER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9aa4fc1c6f365b686ab4dc3875b93396)

@ BT\_A2DP\_INVALID\_CODEC\_PARAMETER

The codec parameter is invalid.

**Definition** a2dp.h:262

[BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8ca9fe3d3aea48e5c5122ce058e8918133f)

@ BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_BITPOOL\_VALUE

Maximum Bitpool Value is not supported.

**Definition** a2dp.h:218

[BT\_A2DP\_INVALID\_CP\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caab4c2af80c9588443a297e120f8ee611)

@ BT\_A2DP\_INVALID\_CP\_TYPE

The requested CP Type is not supported.

**Definition** a2dp.h:254

[BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_TYPE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cabda2c831224e1c994b5c67ea9fe7be7f)

@ BT\_A2DP\_NOT\_SUPPORTED\_CODEC\_TYPE

Media Codec Type is not supported.

**Definition** a2dp.h:194

[BT\_A2DP\_NOT\_SUPPORTED\_MINIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cacd474a29c941a1b1ad164a63d07763d3)

@ BT\_A2DP\_NOT\_SUPPORTED\_MINIMUM\_BITPOOL\_VALUE

Minimum Bitpool Value is not supported.

**Definition** a2dp.h:214

[BT\_A2DP\_INVALID\_MINIMUM\_BITPOOL\_VALUE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cad81217701b215d26e65c220c83ed4a02)

@ BT\_A2DP\_INVALID\_MINIMUM\_BITPOOL\_VALUE

Minimum Bitpool Value is not valid.

**Definition** a2dp.h:212

[BT\_A2DP\_INVALID\_BIT\_RATE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cadb4d2cc815b2c01e6f7e2666305d4476)

@ BT\_A2DP\_INVALID\_BIT\_RATE

None or multiple values have been selected for Bit Rate.

**Definition** a2dp.h:230

[BT\_A2DP\_INVALID\_BLOCK\_LENGTH](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caebf8a58263b517b79947e9cc8a9678c3)

@ BT\_A2DP\_INVALID\_BLOCK\_LENGTH

None or multiple values have been selected for Block Length.

**Definition** a2dp.h:252

[BT\_A2DP\_INVALID\_ALLOCATION\_METHOD](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf13a2a05042cb4ee373017fabd92303a)

@ BT\_A2DP\_INVALID\_ALLOCATION\_METHOD

None or multiple values have been selected for Allocation Method.

**Definition** a2dp.h:208

[BT\_A2DP\_INVALID\_LAYER](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf2bd03a778271c6310fb51d3dccccb41)

@ BT\_A2DP\_INVALID\_LAYER

None or multiple values have been selected for Layer.

**Definition** a2dp.h:220

[BT\_A2DP\_NOT\_SUPPORTED\_BIT\_RATE](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8caf86c457a7e016f440089469c9f442ad1)

@ BT\_A2DP\_NOT\_SUPPORTED\_BIT\_RATE

Bit Rate is not supported.

**Definition** a2dp.h:232

[BT\_A2DP\_INVALID\_DRC](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafd0982a65fc5657b13f35e0761425d96)

@ BT\_A2DP\_INVALID\_DRC

Combination of Object Type and DRC is invalid.

**Definition** a2dp.h:268

[BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_SUL](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8cafdf002100cc0d7d1f07cf833ed331f2b)

@ BT\_A2DP\_NOT\_SUPPORTED\_MAXIMUM\_SUL

Maximum SUL is not acceptable for the Decoder in the SNK.

**Definition** a2dp.h:250

[bt\_a2dp\_register\_cb](a2dp_8h.md#a4af29d7c162743c00534868ba945b7ec)

int bt\_a2dp\_register\_cb(struct bt\_a2dp\_cb \*cb)

register callback.

[bt\_a2dp\_stream\_reconfig](a2dp_8h.md#a70fc5f43265a4c407a847c4205cd7697)

int bt\_a2dp\_stream\_reconfig(struct bt\_a2dp\_stream \*stream, struct bt\_a2dp\_codec\_cfg \*config)

re-configure a2dp streamer

[BT\_A2DP\_DISCOVER\_EP\_STOP](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eab55d2d864da292240e19ee251de832f2)

@ BT\_A2DP\_DISCOVER\_EP\_STOP

**Definition** a2dp.h:332

[BT\_A2DP\_DISCOVER\_EP\_CONTINUE](a2dp_8h.md#a7830b874f18be8fc1c62cb9fc69d3c7eae38f6b8bd78c8a975d0f59c74fe9d367)

@ BT\_A2DP\_DISCOVER\_EP\_CONTINUE

**Definition** a2dp.h:333

[bt\_a2dp\_discover](a2dp_8h.md#a931234227bc2b9eaed9cd60471ee54db)

int bt\_a2dp\_discover(struct bt\_a2dp \*a2dp, struct bt\_a2dp\_discover\_param \*param)

Discover remote endpoints.

[A2DP\_MAX\_IE\_LENGTH](a2dp_8h.md#ab42c7fe29752fb43bb573a752de9c693)

#define A2DP\_MAX\_IE\_LENGTH

The max IE (Codec Info Element) length.

**Definition** a2dp.h:33

[bt\_a2dp\_stream\_cb\_register](a2dp_8h.md#ab8459d999437daa7a107b1bdf4c5ea46)

void bt\_a2dp\_stream\_cb\_register(struct bt\_a2dp\_stream \*stream, struct bt\_a2dp\_stream\_ops \*ops)

Register Audio callbacks for a stream.

[bt\_a2dp\_disconnect](a2dp_8h.md#abbf0d012860a233ecc84ed333e0da051)

int bt\_a2dp\_disconnect(struct bt\_a2dp \*a2dp)

disconnect l2cap a2dp

[bt\_a2dp\_connect](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)

struct bt\_a2dp \* bt\_a2dp\_connect(struct bt\_conn \*conn)

A2DP Connect.

[bt\_a2dp\_register\_ep](a2dp_8h.md#adccb916ce9ee1a229f7a9f89ec3adc1b)

int bt\_a2dp\_register\_ep(struct bt\_a2dp\_ep \*ep, uint8\_t media\_type, uint8\_t role)

Endpoint Registration.

[bt\_a2dp\_discover\_ep\_cb](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed)

uint8\_t(\* bt\_a2dp\_discover\_ep\_cb)(struct bt\_a2dp \*a2dp, struct bt\_a2dp\_ep\_info \*info, struct bt\_a2dp\_ep \*\*ep)

Called when a stream endpoint is discovered.

**Definition** a2dp.h:361

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

**Definition** a2dp.h:274

[BT\_A2DP\_MPEG1](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a1f1840d90c1d5ee28b650978bf012497)

@ BT\_A2DP\_MPEG1

Codec MPEG-1.

**Definition** a2dp.h:278

[BT\_A2DP\_ATRAC](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6a8b969e35e28d18cf05802e1381995e83)

@ BT\_A2DP\_ATRAC

Codec ATRAC.

**Definition** a2dp.h:282

[BT\_A2DP\_SBC](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6abd097d204d4136c5205afe7dfe3dfe00)

@ BT\_A2DP\_SBC

Codec SBC.

**Definition** a2dp.h:276

[BT\_A2DP\_VENDOR](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6ad3c292360558ea515a84d570c43c1701)

@ BT\_A2DP\_VENDOR

Codec Non-A2DP.

**Definition** a2dp.h:284

[BT\_A2DP\_MPEG2](a2dp_8h.md#afdb0a28b03d1e11f0595dd3f0b3cb4d6aefe729d388e0a3d8bb7759b986123c88)

@ BT\_A2DP\_MPEG2

Codec MPEG-2.

**Definition** a2dp.h:280

[avdtp.h](avdtp_8h.md)

Audio/Video Distribution Transport Protocol header.

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:873

[l2cap.h](l2cap_8h.md)

Bluetooth L2CAP handling.

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

**Definition** a2dp.h:378

[bt\_a2dp\_cb::start\_req](structbt__a2dp__cb.md#a1388b0365e46afce78b4f08f25af6858)

int(\* start\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

stream start request callback

**Definition** a2dp.h:483

[bt\_a2dp\_cb::config\_rsp](structbt__a2dp__cb.md#a3b2f6c42bcdefe8a2591fc59c2357786)

void(\* config\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_config().

**Definition** a2dp.h:424

[bt\_a2dp\_cb::reconfig\_req](structbt__a2dp__cb.md#a44c7e59f8b14487aa1bbe42b2526aea2)

int(\* reconfig\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

Endpoint config request callback.

**Definition** a2dp.h:527

[bt\_a2dp\_cb::start\_rsp](structbt__a2dp__cb.md#a49bae91e1cac18a5da90160214a61725)

void(\* start\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_start().

**Definition** a2dp.h:492

[bt\_a2dp\_cb::suspend\_rsp](structbt__a2dp__cb.md#a6064e5d61acb3cdd0f83246ce90e712f)

void(\* suspend\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_suspend().

**Definition** a2dp.h:514

[bt\_a2dp\_cb::suspend\_req](structbt__a2dp__cb.md#a79d2edefa0e6e979bfcfcffe9391a7c0)

int(\* suspend\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

Endpoint suspend request callback.

**Definition** a2dp.h:505

[bt\_a2dp\_cb::disconnected](structbt__a2dp__cb.md#a80401da71ae6dc74d058163624f78518)

void(\* disconnected)(struct bt\_a2dp \*a2dp)

A a2dp connection has been disconnected.

**Definition** a2dp.h:397

[bt\_a2dp\_cb::reconfig\_rsp](structbt__a2dp__cb.md#a8a35f295adc0c7d102e3cb7d72a76cf9)

void(\* reconfig\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_reconfig().

**Definition** a2dp.h:536

[bt\_a2dp\_cb::release\_req](structbt__a2dp__cb.md#a90a637e6e81bf5a74c878c3b4b2e63c0)

int(\* release\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

stream release request callback

**Definition** a2dp.h:460

[bt\_a2dp\_cb::config\_req](structbt__a2dp__cb.md#aab8f5f53a7b507d55e1d594995739222)

int(\* config\_req)(struct bt\_a2dp \*a2dp, struct bt\_a2dp\_ep \*ep, struct bt\_a2dp\_codec\_cfg \*codec\_cfg, struct bt\_a2dp\_stream \*\*stream, uint8\_t \*rsp\_err\_code)

Endpoint config request callback.

**Definition** a2dp.h:413

[bt\_a2dp\_cb::connected](structbt__a2dp__cb.md#ab0b6a895c2f050ab0961325b8ce7e862)

void(\* connected)(struct bt\_a2dp \*a2dp, int err)

A a2dp connection has been established.

**Definition** a2dp.h:389

[bt\_a2dp\_cb::release\_rsp](structbt__a2dp__cb.md#ab4c148eb7be896dec8f6a33217b475e1)

void(\* release\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_release().

**Definition** a2dp.h:470

[bt\_a2dp\_cb::establish\_req](structbt__a2dp__cb.md#adc611ad1a28c3da94f261cc94f63698f)

int(\* establish\_req)(struct bt\_a2dp\_stream \*stream, uint8\_t \*rsp\_err\_code)

stream establishment request callback

**Definition** a2dp.h:437

[bt\_a2dp\_cb::establish\_rsp](structbt__a2dp__cb.md#af19a1f6bb65c60cb0ec7294e66468ba6)

void(\* establish\_rsp)(struct bt\_a2dp\_stream \*stream, uint8\_t rsp\_err\_code)

Callback function for bt\_a2dp\_stream\_establish().

**Definition** a2dp.h:447

[bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md)

The endpoint configuration.

**Definition** a2dp.h:302

[bt\_a2dp\_codec\_cfg::codec\_config](structbt__a2dp__codec__cfg.md#a178eb806a01729d940e6e8c34b0fb513)

struct bt\_a2dp\_codec\_ie \* codec\_config

The media codec configuration content.

**Definition** a2dp.h:304

[bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md)

codec information elements for the endpoint

**Definition** a2dp.h:294

[bt\_a2dp\_codec\_ie::len](structbt__a2dp__codec__ie.md#a8ba1a0bfcbfd180cb19fb7c4a4ce8225)

uint8\_t len

Length of codec\_cap.

**Definition** a2dp.h:296

[bt\_a2dp\_codec\_ie::codec\_ie](structbt__a2dp__codec__ie.md#acf258c8d4b123e3765ad7e2568ac43aa)

uint8\_t codec\_ie[(8U)]

codec information element

**Definition** a2dp.h:298

[bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md)

**Definition** a2dp.h:364

[bt\_a2dp\_discover\_param::info](structbt__a2dp__discover__param.md#a14b69e2449f1d2379183690246f55a88)

struct bt\_a2dp\_ep\_info info

The discovered endpoint info that is callbacked by cb.

**Definition** a2dp.h:368

[bt\_a2dp\_discover\_param::sep\_count](structbt__a2dp__discover__param.md#a382ce8462958f69af19e325491c6f01b)

uint8\_t sep\_count

The max count of seps (stream endpoint) that can be got in this call route.

**Definition** a2dp.h:374

[bt\_a2dp\_discover\_param::cb](structbt__a2dp__discover__param.md#a806fdbaf6d26ad269608afaa21c2035f)

bt\_a2dp\_discover\_ep\_cb cb

discover callback

**Definition** a2dp.h:366

[bt\_a2dp\_discover\_param::seps\_info](structbt__a2dp__discover__param.md#ab4174f0b43d1804192cd4647d29779d3)

struct bt\_avdtp\_sep\_info \* seps\_info

The max count of remote endpoints that can be got, it save endpoint info internally.

**Definition** a2dp.h:372

[bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md)

**Definition** a2dp.h:319

[bt\_a2dp\_ep\_info::sep\_info](structbt__a2dp__ep__info.md#a114c3b267587efa71922e31e474fd8e4)

struct bt\_avdtp\_sep\_info sep\_info

Stream End Point Information.

**Definition** a2dp.h:325

[bt\_a2dp\_ep\_info::codec\_cap](structbt__a2dp__ep__info.md#a7647012b4ea73a0124e2a3239a3bad7b)

struct bt\_a2dp\_codec\_ie codec\_cap

Codec capabilities, if SBC, use function of a2dp\_codec\_sbc.h to parse it.

**Definition** a2dp.h:323

[bt\_a2dp\_ep\_info::codec\_type](structbt__a2dp__ep__info.md#aca4f893b087a8429dd104b67114e36d7)

uint8\_t codec\_type

Code Type bt\_a2dp\_codec\_type.

**Definition** a2dp.h:321

[bt\_a2dp\_ep](structbt__a2dp__ep.md)

Stream End Point.

**Definition** a2dp.h:308

[bt\_a2dp\_ep::sep](structbt__a2dp__ep.md#a2565b03e09e5abcf239c4c671b348c50)

struct bt\_avdtp\_sep sep

AVDTP Stream End Point Identifier.

**Definition** a2dp.h:314

[bt\_a2dp\_ep::stream](structbt__a2dp__ep.md#a4902b9fde9be1aa9b7a35c22a21cd4a6)

struct bt\_a2dp\_stream \* stream

**Definition** a2dp.h:316

[bt\_a2dp\_ep::codec\_type](structbt__a2dp__ep.md#a912cf7cd18a58a1cc1a5e326e8bebb73)

uint8\_t codec\_type

Code Type bt\_a2dp\_codec\_type.

**Definition** a2dp.h:310

[bt\_a2dp\_ep::codec\_cap](structbt__a2dp__ep.md#ae4dcc7f4bca5cc34cf05c2277379a1b3)

struct bt\_a2dp\_codec\_ie \* codec\_cap

Capabilities.

**Definition** a2dp.h:312

[bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md)

The stream endpoint related operations.

**Definition** a2dp.h:612

[bt\_a2dp\_stream\_ops::configured](structbt__a2dp__stream__ops.md#a146f907aa60ae130b3248da7475db0cb)

void(\* configured)(struct bt\_a2dp\_stream \*stream)

Stream configured callback.

**Definition** a2dp.h:620

[bt\_a2dp\_stream\_ops::started](structbt__a2dp__stream__ops.md#a292e604e7db2faca1915533eab76830e)

void(\* started)(struct bt\_a2dp\_stream \*stream)

Stream start callback.

**Definition** a2dp.h:644

[bt\_a2dp\_stream\_ops::established](structbt__a2dp__stream__ops.md#a88d7a0598a5af6740747eb575b8b57df)

void(\* established)(struct bt\_a2dp\_stream \*stream)

Stream establishment callback.

**Definition** a2dp.h:628

[bt\_a2dp\_stream\_ops::reconfigured](structbt__a2dp__stream__ops.md#aba623932df3dfd4072f20794b71922ab)

void(\* reconfigured)(struct bt\_a2dp\_stream \*stream)

Stream reconfigured callback.

**Definition** a2dp.h:660

[bt\_a2dp\_stream\_ops::released](structbt__a2dp__stream__ops.md#acaa2c8b7e59a0b0bb652c9801110234b)

void(\* released)(struct bt\_a2dp\_stream \*stream)

Stream release callback.

**Definition** a2dp.h:636

[bt\_a2dp\_stream\_ops::suspended](structbt__a2dp__stream__ops.md#af839ecbcb131cb68165c516c2e049fe5)

void(\* suspended)(struct bt\_a2dp\_stream \*stream)

Stream suspend callback.

**Definition** a2dp.h:652

[bt\_a2dp\_stream](structbt__a2dp__stream.md)

A2DP Stream.

**Definition** a2dp.h:596

[bt\_a2dp\_stream::remote\_ep\_id](structbt__a2dp__stream.md#a3361f68c31075014c2c3cf62494ff3ec)

uint8\_t remote\_ep\_id

remote endpoint's Stream End Point ID

**Definition** a2dp.h:602

[bt\_a2dp\_stream::remote\_ep](structbt__a2dp__stream.md#a4ea9de245b573b7d0c495aacd7534099)

struct bt\_a2dp\_ep \* remote\_ep

remote endpoint

**Definition** a2dp.h:600

[bt\_a2dp\_stream::local\_ep](structbt__a2dp__stream.md#aa490bb24525c50cf8c1675a01223420c)

struct bt\_a2dp\_ep \* local\_ep

local endpoint

**Definition** a2dp.h:598

[bt\_a2dp\_stream::ops](structbt__a2dp__stream.md#aa51509d9f0c50118177345988ddb8fa5)

struct bt\_a2dp\_stream\_ops \* ops

Audio stream operations.

**Definition** a2dp.h:604

[bt\_a2dp\_stream::a2dp](structbt__a2dp__stream.md#ab62b3f17a198600e683c26cf3d3e87e2)

struct bt\_a2dp \* a2dp

the a2dp connection

**Definition** a2dp.h:606

[bt\_a2dp\_stream::codec\_config](structbt__a2dp__stream.md#aff775fe292618da4de467aa96cbf79b0)

struct bt\_a2dp\_codec\_ie codec\_config

the stream current configuration

**Definition** a2dp.h:608

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
