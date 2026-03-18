---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/a2dp-codec_8h_source.html
original_path: doxygen/html/a2dp-codec_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

a2dp-codec.h

[Go to the documentation of this file.](a2dp-codec_8h.md)

1

4/\*

5 \* SPDX-License-Identifier: Apache-2.0

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* Licensed under the Apache License, Version 2.0 (the "License");

9 \* you may not use this file except in compliance with the License.

10 \* You may obtain a copy of the License at

11 \*

12 \* http://www.apache.org/licenses/LICENSE-2.0

13 \*

14 \* Unless required by applicable law or agreed to in writing, software

15 \* distributed under the License is distributed on an "AS IS" BASIS,

16 \* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

17 \* See the License for the specific language governing permissions and

18 \* limitations under the License.

19 \*/

20#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_CODEC\_H\_

21#define ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_CODEC\_H\_

22

23#include <[stdint.h](stdint_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 33](a2dp-codec_8h.md#a054dbbaf58ccc3b64142008e3da31ca5)#define A2DP\_SBC\_SAMP\_FREQ\_16000 BIT(7)

[ 34](a2dp-codec_8h.md#a8e4b5399fb5366770a42fd4dfeece220)#define A2DP\_SBC\_SAMP\_FREQ\_32000 BIT(6)

[ 35](a2dp-codec_8h.md#a57d7b85560b36603651fae6c055c32c6)#define A2DP\_SBC\_SAMP\_FREQ\_44100 BIT(5)

[ 36](a2dp-codec_8h.md#a0ebafbef2cddd4b6c7c7990ca77db0f9)#define A2DP\_SBC\_SAMP\_FREQ\_48000 BIT(4)

38

[ 43](a2dp-codec_8h.md#aa9b58737fa1561b684a20980ea0b6feb)#define A2DP\_SBC\_CH\_MODE\_MONO BIT(3)

[ 44](a2dp-codec_8h.md#aab5ab0b151f0a150c392be2f4cc82def)#define A2DP\_SBC\_CH\_MODE\_DUAL BIT(2)

[ 45](a2dp-codec_8h.md#acc5be684b75804f72a28d025fc5cc9bb)#define A2DP\_SBC\_CH\_MODE\_STREO BIT(1)

[ 46](a2dp-codec_8h.md#afcf64fa599e4d820dccdf40990f5ba39)#define A2DP\_SBC\_CH\_MODE\_JOINT BIT(0)

48

[ 53](a2dp-codec_8h.md#a3abfc1c5202d2659055fc3480c2d3cc2)#define A2DP\_SBC\_BLK\_LEN\_4 BIT(7)

[ 54](a2dp-codec_8h.md#aeb90df4a33ce9ebdfc38d873fd54abab)#define A2DP\_SBC\_BLK\_LEN\_8 BIT(6)

[ 55](a2dp-codec_8h.md#a9890a0cb8a813e010855c10fc4d22bf8)#define A2DP\_SBC\_BLK\_LEN\_12 BIT(5)

[ 56](a2dp-codec_8h.md#a1cb9425713c325442652fb406557e52a)#define A2DP\_SBC\_BLK\_LEN\_16 BIT(4)

58

[ 63](a2dp-codec_8h.md#ad5916cf243e40e5a674ceed13477023e)#define A2DP\_SBC\_SUBBAND\_4 BIT(3)

[ 64](a2dp-codec_8h.md#a6b4bd1ef891c14c4f863c9623dcb63f7)#define A2DP\_SBC\_SUBBAND\_8 BIT(2)

66

[ 71](a2dp-codec_8h.md#a7e54f1c971e1fd63e52f0322e7f85105)#define A2DP\_SBC\_ALLOC\_MTHD\_SNR BIT(1)

[ 72](a2dp-codec_8h.md#a27d905ddf0fdb3dea4d3c12dd3ca33fe)#define A2DP\_SBC\_ALLOC\_MTHD\_LOUDNESS BIT(0)

74

[ 79](a2dp-codec_8h.md#a092b0f76c2af2d41c28b457b87ea8756)#define BT\_A2DP\_SBC\_SAMP\_FREQ(preset) ((preset->config[0] >> 4) & 0x0f)

[ 84](a2dp-codec_8h.md#abc9b0f85b8f338d24a62943857858bd4)#define BT\_A2DP\_SBC\_CHAN\_MODE(preset) ((preset->config[0]) & 0x0f)

[ 89](a2dp-codec_8h.md#a33d36b781d3ff7eac73be1a29a0c260a)#define BT\_A2DP\_SBC\_BLK\_LEN(preset) ((preset->config[1] >> 4) & 0x0f)

[ 94](a2dp-codec_8h.md#aeacdc6a1857382ff1f4363d7eddce88e)#define BT\_A2DP\_SBC\_SUB\_BAND(preset) ((preset->config[1] >> 2) & 0x03)

[ 99](a2dp-codec_8h.md#a6bed8046031b53111bf0a45057d04565)#define BT\_A2DP\_SBC\_ALLOC\_MTHD(preset) ((preset->config[1]) & 0x03)

100

[ 102](structbt__a2dp__codec__sbc__params.md)struct [bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md) {

[ 104](structbt__a2dp__codec__sbc__params.md#a80b0705befa9c573e4653a5f88f81e8d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [config](structbt__a2dp__codec__sbc__params.md#a80b0705befa9c573e4653a5f88f81e8d)[2];

[ 106](structbt__a2dp__codec__sbc__params.md#a026f28b42a3e8b41a2597cfa4ca01f95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_bitpool](structbt__a2dp__codec__sbc__params.md#a026f28b42a3e8b41a2597cfa4ca01f95);

[ 108](structbt__a2dp__codec__sbc__params.md#a34319bc3d168e5eb7d3ef2cae521ca96) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_bitpool](structbt__a2dp__codec__sbc__params.md#a34319bc3d168e5eb7d3ef2cae521ca96);

109} \_\_packed;

110

111#ifdef \_\_cplusplus

112}

113#endif

114

115#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_CODEC\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_a2dp\_codec\_sbc\_params](structbt__a2dp__codec__sbc__params.md)

SBC Codec.

**Definition** a2dp-codec.h:102

[bt\_a2dp\_codec\_sbc\_params::min\_bitpool](structbt__a2dp__codec__sbc__params.md#a026f28b42a3e8b41a2597cfa4ca01f95)

uint8\_t min\_bitpool

Minimum Bitpool Value.

**Definition** a2dp-codec.h:106

[bt\_a2dp\_codec\_sbc\_params::max\_bitpool](structbt__a2dp__codec__sbc__params.md#a34319bc3d168e5eb7d3ef2cae521ca96)

uint8\_t max\_bitpool

Maximum Bitpool Value.

**Definition** a2dp-codec.h:108

[bt\_a2dp\_codec\_sbc\_params::config](structbt__a2dp__codec__sbc__params.md#a80b0705befa9c573e4653a5f88f81e8d)

uint8\_t config[2]

First two octets of configuration.

**Definition** a2dp-codec.h:104

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [a2dp-codec.h](a2dp-codec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
