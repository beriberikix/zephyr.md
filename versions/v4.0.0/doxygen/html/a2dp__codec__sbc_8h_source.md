---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/a2dp__codec__sbc_8h_source.html
original_path: doxygen/html/a2dp__codec__sbc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

a2dp\_codec\_sbc.h

[Go to the documentation of this file.](a2dp__codec__sbc_8h.md)

1

4/\*

5 \* SPDX-License-Identifier: Apache-2.0

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \* Copyright (c) 2021 NXP

8 \*

9 \* Licensed under the Apache License, Version 2.0 (the "License");

10 \* you may not use this file except in compliance with the License.

11 \* You may obtain a copy of the License at

12 \*

13 \* http://www.apache.org/licenses/LICENSE-2.0

14 \*

15 \* Unless required by applicable law or agreed to in writing, software

16 \* distributed under the License is distributed on an "AS IS" BASIS,

17 \* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

18 \* See the License for the specific language governing permissions and

19 \* limitations under the License.

20 \*/

21#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_CODEC\_H\_

22#define ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_CODEC\_H\_

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28/\* Sampling Frequency \*/

[ 29](a2dp__codec__sbc_8h.md#a054dbbaf58ccc3b64142008e3da31ca5)#define A2DP\_SBC\_SAMP\_FREQ\_16000 BIT(7)

[ 30](a2dp__codec__sbc_8h.md#a8e4b5399fb5366770a42fd4dfeece220)#define A2DP\_SBC\_SAMP\_FREQ\_32000 BIT(6)

[ 31](a2dp__codec__sbc_8h.md#a57d7b85560b36603651fae6c055c32c6)#define A2DP\_SBC\_SAMP\_FREQ\_44100 BIT(5)

[ 32](a2dp__codec__sbc_8h.md#a0ebafbef2cddd4b6c7c7990ca77db0f9)#define A2DP\_SBC\_SAMP\_FREQ\_48000 BIT(4)

33

34/\* Channel Mode \*/

[ 35](a2dp__codec__sbc_8h.md#aa9b58737fa1561b684a20980ea0b6feb)#define A2DP\_SBC\_CH\_MODE\_MONO BIT(3)

[ 36](a2dp__codec__sbc_8h.md#aab5ab0b151f0a150c392be2f4cc82def)#define A2DP\_SBC\_CH\_MODE\_DUAL BIT(2)

[ 37](a2dp__codec__sbc_8h.md#acc5be684b75804f72a28d025fc5cc9bb)#define A2DP\_SBC\_CH\_MODE\_STREO BIT(1)

[ 38](a2dp__codec__sbc_8h.md#afcf64fa599e4d820dccdf40990f5ba39)#define A2DP\_SBC\_CH\_MODE\_JOINT BIT(0)

39

40/\* Block Length \*/

[ 41](a2dp__codec__sbc_8h.md#a3abfc1c5202d2659055fc3480c2d3cc2)#define A2DP\_SBC\_BLK\_LEN\_4 BIT(7)

[ 42](a2dp__codec__sbc_8h.md#aeb90df4a33ce9ebdfc38d873fd54abab)#define A2DP\_SBC\_BLK\_LEN\_8 BIT(6)

[ 43](a2dp__codec__sbc_8h.md#a9890a0cb8a813e010855c10fc4d22bf8)#define A2DP\_SBC\_BLK\_LEN\_12 BIT(5)

[ 44](a2dp__codec__sbc_8h.md#a1cb9425713c325442652fb406557e52a)#define A2DP\_SBC\_BLK\_LEN\_16 BIT(4)

45

46/\* Subbands \*/

[ 47](a2dp__codec__sbc_8h.md#ad5916cf243e40e5a674ceed13477023e)#define A2DP\_SBC\_SUBBAND\_4 BIT(3)

[ 48](a2dp__codec__sbc_8h.md#a6b4bd1ef891c14c4f863c9623dcb63f7)#define A2DP\_SBC\_SUBBAND\_8 BIT(2)

49

50/\* Allocation Method \*/

[ 51](a2dp__codec__sbc_8h.md#a7e54f1c971e1fd63e52f0322e7f85105)#define A2DP\_SBC\_ALLOC\_MTHD\_SNR BIT(1)

[ 52](a2dp__codec__sbc_8h.md#a27d905ddf0fdb3dea4d3c12dd3ca33fe)#define A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS BIT(0)

53

[ 54](a2dp__codec__sbc_8h.md#a5b9313959439cc91be71efa214383ef7)#define BT\_A2DP\_SBC\_SAMP\_FREQ(cap) ((cap->config[0] >> 4) & 0x0f)

[ 55](a2dp__codec__sbc_8h.md#a8d058052eb87cf22314395cc2581ac5d)#define BT\_A2DP\_SBC\_CHAN\_MODE(cap) ((cap->config[0]) & 0x0f)

[ 56](a2dp__codec__sbc_8h.md#a1721d8cc832b5a74306943074132369a)#define BT\_A2DP\_SBC\_BLK\_LEN(cap) ((cap->config[1] >> 4) & 0x0f)

[ 57](a2dp__codec__sbc_8h.md#aa4eb6816559e80400f1767e230d0efdf)#define BT\_A2DP\_SBC\_SUB\_BAND(cap) ((cap->config[1] >> 2) & 0x03)

[ 58](a2dp__codec__sbc_8h.md#a58878ea86ed87c6c5bfede0fe217ade8)#define BT\_A2DP\_SBC\_ALLOC\_MTHD(cap) ((cap->config[1]) & 0x03)

59

[ 61](structbt__a2dp__codec__sbc__params.md)struct [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) {

[ 63](structbt__a2dp__codec__sbc__params.md#a80b0705befa9c573e4653a5f88f81e8d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config](structbt__a2dp__codec__sbc__params.md#a80b0705befa9c573e4653a5f88f81e8d)[2];

[ 65](structbt__a2dp__codec__sbc__params.md#a026f28b42a3e8b41a2597cfa4ca01f95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_bitpool](structbt__a2dp__codec__sbc__params.md#a026f28b42a3e8b41a2597cfa4ca01f95);

[ 67](structbt__a2dp__codec__sbc__params.md#a34319bc3d168e5eb7d3ef2cae521ca96) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_bitpool](structbt__a2dp__codec__sbc__params.md#a34319bc3d168e5eb7d3ef2cae521ca96);

68} \_\_packed;

69

[ 75](a2dp__codec__sbc_8h.md#a5d79c5a628c9740a81d5fe9626e14463)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_NUM\_FRAMES\_GET(hdr) FIELD\_GET(GENMASK(3, 0), (hdr))

[ 77](a2dp__codec__sbc_8h.md#ab84850ce399e236f10ef80f0d2d2acde)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_L\_GET(hdr) FIELD\_GET(BIT(5), (hdr))

[ 79](a2dp__codec__sbc_8h.md#a164ada24748d1fb21248274a02d11301)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_S\_GET(hdr) FIELD\_GET(BIT(6), (hdr))

[ 81](a2dp__codec__sbc_8h.md#aaf18a29764a148b007f10e9a9f1a5437)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_F\_GET(hdr) FIELD\_GET(BIT(7), (hdr))

82

[ 88](a2dp__codec__sbc_8h.md#af8da63e80785a6fa5a53fd29c6da5b9c)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_NUM\_FRAMES\_SET(hdr, val)\

89 hdr = ((hdr) & ~GENMASK(3, 0)) | FIELD\_PREP(GENMASK(3, 0), (val))

90

[ 91](a2dp__codec__sbc_8h.md#a7f00326a7dcd0839da6ea8557303c45f)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_L\_SET(hdr, val)\

92 hdr = ((hdr) & ~BIT(5)) | FIELD\_PREP(BIT(5), (val))

93

[ 94](a2dp__codec__sbc_8h.md#a85bb7d78a1d654a68812517ddcebf76a)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_S\_SET(hdr, val)\

95 hdr = ((hdr) & ~BIT(6)) | FIELD\_PREP(BIT(6), (val))

96

[ 97](a2dp__codec__sbc_8h.md#ab007b2c51612b05f9edc127bd9090536)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_F\_SET(hdr, val)\

98 hdr = ((hdr) & ~BIT(7)) | FIELD\_PREP(BIT(7), (val))

99

[ 100](a2dp__codec__sbc_8h.md#aa9a0484c4eefe685c0cbde87ce781734)#define BT\_A2DP\_SBC\_MEDIA\_HDR\_ENCODE(num\_frames, l, s, f)\

101 FIELD\_PREP(GENMASK(3, 0), num\_frames) | FIELD\_PREP(BIT(5), l) |\

102 FIELD\_PREP(BIT(6), s) | FIELD\_PREP(BIT(7), f)

103

[ 110](a2dp__codec__sbc_8h.md#a8791ff3f4f02b46ea879df5e20ba5dd6)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_a2dp\_sbc\_get\_channel\_num](a2dp__codec__sbc_8h.md#a8791ff3f4f02b46ea879df5e20ba5dd6)(struct [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) \*sbc\_codec);

111

[ 118](a2dp__codec__sbc_8h.md#a7af2c05d2605d7d21e656222238922c1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bt\_a2dp\_sbc\_get\_sampling\_frequency](a2dp__codec__sbc_8h.md#a7af2c05d2605d7d21e656222238922c1)(struct [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) \*sbc\_codec);

119

120#ifdef \_\_cplusplus

121}

122#endif

123

124#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_CODEC\_H\_ \*/

[bt\_a2dp\_sbc\_get\_sampling\_frequency](a2dp__codec__sbc_8h.md#a7af2c05d2605d7d21e656222238922c1)

uint32\_t bt\_a2dp\_sbc\_get\_sampling\_frequency(struct bt\_a2dp\_codec\_sbc\_params \*sbc\_codec)

get sample rate of a2dp sbc config.

[bt\_a2dp\_sbc\_get\_channel\_num](a2dp__codec__sbc_8h.md#a8791ff3f4f02b46ea879df5e20ba5dd6)

uint8\_t bt\_a2dp\_sbc\_get\_channel\_num(struct bt\_a2dp\_codec\_sbc\_params \*sbc\_codec)

get channel num of a2dp sbc config.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md)

SBC Codec.

**Definition** a2dp\_codec\_sbc.h:61

[bt\_a2dp\_codec\_sbc\_params::min\_bitpool](structbt__a2dp__codec__sbc__params.md#a026f28b42a3e8b41a2597cfa4ca01f95)

uint8\_t min\_bitpool

Minimum Bitpool Value.

**Definition** a2dp\_codec\_sbc.h:65

[bt\_a2dp\_codec\_sbc\_params::max\_bitpool](structbt__a2dp__codec__sbc__params.md#a34319bc3d168e5eb7d3ef2cae521ca96)

uint8\_t max\_bitpool

Maximum Bitpool Value.

**Definition** a2dp\_codec\_sbc.h:67

[bt\_a2dp\_codec\_sbc\_params::config](structbt__a2dp__codec__sbc__params.md#a80b0705befa9c573e4653a5f88f81e8d)

uint8\_t config[2]

First two octets of configuration.

**Definition** a2dp\_codec\_sbc.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [a2dp\_codec\_sbc.h](a2dp__codec__sbc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
