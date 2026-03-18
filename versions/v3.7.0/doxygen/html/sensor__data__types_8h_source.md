---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sensor__data__types_8h_source.html
original_path: doxygen/html/sensor__data__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_data\_types.h

[Go to the documentation of this file.](sensor__data__types_8h.md)

1/\*

2 \* Copyright (c) 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_DATA\_TYPES\_H

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_DATA\_TYPES\_H

9

10#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h.md)>

11#include <[zephyr/dsp/print\_format.h](print__format_8h.md)>

12

13#include <[inttypes.h](inttypes_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](structsensor__data__header.md)struct [sensor\_data\_header](structsensor__data__header.md) {

[ 24](structsensor__data__header.md#a1db93386466e8e4778f448ae0d8ca556) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [base\_timestamp\_ns](structsensor__data__header.md#a1db93386466e8e4778f448ae0d8ca556);

[ 30](structsensor__data__header.md#ad31873d402a02842eb3098431591c151) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reading\_count](structsensor__data__header.md#ad31873d402a02842eb3098431591c151);

31};

32

[ 52](structsensor__three__axis__data.md)struct [sensor\_three\_axis\_data](structsensor__three__axis__data.md) {

[ 53](structsensor__three__axis__data.md#a6017fc7964204235e2222c4950f3650a) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__three__axis__data.md#a6017fc7964204235e2222c4950f3650a);

[ 54](structsensor__three__axis__data.md#ade10fa0bd60d4b31eebed92e564539c5) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensor__three__axis__data.md#ade10fa0bd60d4b31eebed92e564539c5);

[ 55](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md) struct [sensor\_three\_axis\_sample\_data](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md) {

[ 56](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a62dd4febada1d6b0b0fad600747089a2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a62dd4febada1d6b0b0fad600747089a2);

57 union {

[ 58](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#aa8a07324f3139a6a34f695927a1d6486) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [values](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#aa8a07324f3139a6a34f695927a1d6486)[3];

[ 59](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#aa0de6e1354c259857b2b5a89717a5f9a) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [v](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#aa0de6e1354c259857b2b5a89717a5f9a)[3];

60 struct {

[ 61](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a60a8b323508fb4ececd4c3bdad770525) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [x](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a60a8b323508fb4ececd4c3bdad770525);

[ 62](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#ac78d9fa7e085025f1ccc9f53bf30f3bb) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [y](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#ac78d9fa7e085025f1ccc9f53bf30f3bb);

[ 63](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a5ef91a336b07c2c3e79ed34afbbf8850) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [z](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a5ef91a336b07c2c3e79ed34afbbf8850);

64 };

65 };

[ 66](structsensor__three__axis__data.md#ad1a498b1cc31b18b17e69300749bbbc0) } [readings](structsensor__three__axis__data.md#ad1a498b1cc31b18b17e69300749bbbc0)[1];

67};

68

[ 69](sensor__data__types_8h.md#a0c6a78118f9360ed97b1327cf3a3fa9a)#define PRIsensor\_three\_axis\_data PRIu64 "ns, (%" PRIq(6) ", %" PRIq(6) ", %" PRIq(6) ")"

70

[ 71](sensor__data__types_8h.md#af8c5897a6515c73ec1795b800590a7b4)#define PRIsensor\_three\_axis\_data\_arg(data\_, readings\_offset\_) \

72 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

73 PRIq\_arg((data\_).readings[(readings\_offset\_)].x, 6, (data\_).shift), \

74 PRIq\_arg((data\_).readings[(readings\_offset\_)].y, 6, (data\_).shift), \

75 PRIq\_arg((data\_).readings[(readings\_offset\_)].z, 6, (data\_).shift)

76

[ 80](structsensor__occurrence__data.md)struct [sensor\_occurrence\_data](structsensor__occurrence__data.md) {

[ 81](structsensor__occurrence__data.md#a06e7c6b24166e1c85d05286d44f60768) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__occurrence__data.md#a06e7c6b24166e1c85d05286d44f60768);

[ 82](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md) struct [sensor\_occurrence\_sample\_data](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md) {

[ 83](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md#a19fb2f7d23a2d58e0bf7f2009f8aba59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md#a19fb2f7d23a2d58e0bf7f2009f8aba59);

[ 84](structsensor__occurrence__data.md#a181279d03759db87e3855d46d30c5aaf) } [readings](structsensor__occurrence__data.md#a181279d03759db87e3855d46d30c5aaf)[1];

85};

86

[ 87](sensor__data__types_8h.md#a9862e4197bb6146b3e41958f427c9f9a)#define PRIsensor\_occurrence\_data PRIu64 "ns"

88

[ 89](sensor__data__types_8h.md#a3f8a660a28578bbb7baf08fefbca7ac4)#define PRIsensor\_occurrence\_data\_arg(data\_, readings\_offset\_) \

90 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta

91

[ 92](structsensor__q31__data.md)struct [sensor\_q31\_data](structsensor__q31__data.md) {

[ 93](structsensor__q31__data.md#a9dcc5ffe1d31c37eef75b4132c5f94fd) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__q31__data.md#a9dcc5ffe1d31c37eef75b4132c5f94fd);

[ 94](structsensor__q31__data.md#a41f8315cbe740bdc7aec6bd30ce0e096) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensor__q31__data.md#a41f8315cbe740bdc7aec6bd30ce0e096);

[ 95](structsensor__q31__data_1_1sensor__q31__sample__data.md) struct [sensor\_q31\_sample\_data](structsensor__q31__data_1_1sensor__q31__sample__data.md) {

[ 96](structsensor__q31__data_1_1sensor__q31__sample__data.md#afdf41c27c4f3f55c3ed18c73ab8b6183) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__q31__data_1_1sensor__q31__sample__data.md#afdf41c27c4f3f55c3ed18c73ab8b6183);

97 union {

[ 98](structsensor__q31__data_1_1sensor__q31__sample__data.md#afd73a2b1b6e4e262e89e242853f4ef23) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [value](structsensor__q31__data_1_1sensor__q31__sample__data.md#afd73a2b1b6e4e262e89e242853f4ef23);

[ 99](structsensor__q31__data_1_1sensor__q31__sample__data.md#a7ae2d145a778a72322a78ed433781a0d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [light](structsensor__q31__data_1_1sensor__q31__sample__data.md#a7ae2d145a778a72322a78ed433781a0d);

[ 100](structsensor__q31__data_1_1sensor__q31__sample__data.md#ae07081204f6c01334ea9f2e970879b72) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [pressure](structsensor__q31__data_1_1sensor__q31__sample__data.md#ae07081204f6c01334ea9f2e970879b72);

[ 101](structsensor__q31__data_1_1sensor__q31__sample__data.md#a8101423f27270dcee7a356cabcc4d9dd) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [temperature](structsensor__q31__data_1_1sensor__q31__sample__data.md#a8101423f27270dcee7a356cabcc4d9dd);

[ 102](structsensor__q31__data_1_1sensor__q31__sample__data.md#a39f4f4bf64dd49ff2fe027f6e8f8a04d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [percent](structsensor__q31__data_1_1sensor__q31__sample__data.md#a39f4f4bf64dd49ff2fe027f6e8f8a04d);

[ 103](structsensor__q31__data_1_1sensor__q31__sample__data.md#ad5d6a48016d474635c0f8a829915a8d2) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [distance](structsensor__q31__data_1_1sensor__q31__sample__data.md#ad5d6a48016d474635c0f8a829915a8d2);

[ 104](structsensor__q31__data_1_1sensor__q31__sample__data.md#a2ed468c4be6417f0ea2bb324560e622d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [density](structsensor__q31__data_1_1sensor__q31__sample__data.md#a2ed468c4be6417f0ea2bb324560e622d);

[ 105](structsensor__q31__data_1_1sensor__q31__sample__data.md#a1493dc66c9d6e4782aed2ddadd74e178) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [density\_ppm](structsensor__q31__data_1_1sensor__q31__sample__data.md#a1493dc66c9d6e4782aed2ddadd74e178);

[ 106](structsensor__q31__data_1_1sensor__q31__sample__data.md#a215aab449c2b5ee8cf32d971aa5e7708) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [density\_ppb](structsensor__q31__data_1_1sensor__q31__sample__data.md#a215aab449c2b5ee8cf32d971aa5e7708);

[ 107](structsensor__q31__data_1_1sensor__q31__sample__data.md#aeb66bf289c9e17ac6473eb69c22d4eb3) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [resistance](structsensor__q31__data_1_1sensor__q31__sample__data.md#aeb66bf289c9e17ac6473eb69c22d4eb3);

[ 108](structsensor__q31__data_1_1sensor__q31__sample__data.md#af63a2f7a618c8ff17be31a0543920525) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [voltage](structsensor__q31__data_1_1sensor__q31__sample__data.md#af63a2f7a618c8ff17be31a0543920525);

[ 109](structsensor__q31__data_1_1sensor__q31__sample__data.md#a60f0af8beb207f90ed916fe445525fed) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [current](structsensor__q31__data_1_1sensor__q31__sample__data.md#a60f0af8beb207f90ed916fe445525fed);

[ 110](structsensor__q31__data_1_1sensor__q31__sample__data.md#a428adc52033ba50b871c8986e55b06af) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [power](structsensor__q31__data_1_1sensor__q31__sample__data.md#a428adc52033ba50b871c8986e55b06af);

[ 111](structsensor__q31__data_1_1sensor__q31__sample__data.md#a9e58a7ea902e27b02b34cc8f619aca96) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [angle](structsensor__q31__data_1_1sensor__q31__sample__data.md#a9e58a7ea902e27b02b34cc8f619aca96);

[ 112](structsensor__q31__data_1_1sensor__q31__sample__data.md#aafb3c0aa55c129b310525f7181b59d51) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [electric\_charge](structsensor__q31__data_1_1sensor__q31__sample__data.md#aafb3c0aa55c129b310525f7181b59d51);

[ 113](structsensor__q31__data_1_1sensor__q31__sample__data.md#ac0d247952ae488af354fa1462a014d1d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [humidity](structsensor__q31__data_1_1sensor__q31__sample__data.md#ac0d247952ae488af354fa1462a014d1d);

114 };

[ 115](structsensor__q31__data.md#a23fc75fd1dafe2789a7d0bff116cb681) } [readings](structsensor__q31__data.md#a23fc75fd1dafe2789a7d0bff116cb681)[1];

116};

117

[ 118](sensor__data__types_8h.md#a92ae9197089ece9de51db496c9ed5ed6)#define PRIsensor\_q31\_data PRIu64 "ns (%" PRIq(6) ")"

119

[ 120](sensor__data__types_8h.md#aac3d2a0c462c05c26f7dee0fa0e1ef62)#define PRIsensor\_q31\_data\_arg(data\_, readings\_offset\_) \

121 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

122 PRIq\_arg((data\_).readings[(readings\_offset\_)].value, 6, (data\_).shift)

123

[ 128](structsensor__byte__data.md)struct [sensor\_byte\_data](structsensor__byte__data.md) {

[ 129](structsensor__byte__data.md#ab18ad72251bae040fc4752bc125be3ba) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__byte__data.md#ab18ad72251bae040fc4752bc125be3ba);

[ 130](structsensor__byte__data_1_1sensor__byte__sample__data.md) struct [sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md) {

[ 131](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab29a911990794b35bde3114e813d2c9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab29a911990794b35bde3114e813d2c9a);

132 union {

[ 133](structsensor__byte__data_1_1sensor__byte__sample__data.md#a3ad640ff448fe87d2eda7c5118404b7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structsensor__byte__data_1_1sensor__byte__sample__data.md#a3ad640ff448fe87d2eda7c5118404b7a);

134 struct {

[ 135](structsensor__byte__data_1_1sensor__byte__sample__data.md#acd42cfa0dc446378cebf998c1b795963) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_near](structsensor__byte__data_1_1sensor__byte__sample__data.md#acd42cfa0dc446378cebf998c1b795963): 1;

[ 136](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab07c2a7ce6e47c61249606a88aeda2bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [padding](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab07c2a7ce6e47c61249606a88aeda2bd): 7;

137 };

138 };

[ 139](structsensor__byte__data.md#ad4ac07ed10938265e89a43133c41af24) } [readings](structsensor__byte__data.md#ad4ac07ed10938265e89a43133c41af24)[1];

140};

141

[ 142](sensor__data__types_8h.md#af73f68f6b94dc1251dfeeb5caf141e94)#define PRIsensor\_byte\_data(field\_name\_) PRIu64 "ns (" STRINGIFY(field\_name\_) " = %" PRIu8 ")"

143

[ 144](sensor__data__types_8h.md#a36cfa50e20150d44c6a254afc149eb5b)#define PRIsensor\_byte\_data\_arg(data\_, readings\_offset\_, field\_name\_) \

145 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

146 (data\_).readings[(readings\_offset\_)].field\_name\_

147

[ 152](structsensor__uint64__data.md)struct [sensor\_uint64\_data](structsensor__uint64__data.md) {

[ 153](structsensor__uint64__data.md#a61e2d0796ba3c0e95a0455e03ce01d76) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__uint64__data.md#a61e2d0796ba3c0e95a0455e03ce01d76);

[ 154](structsensor__uint64__data_1_1sensor__uint64__sample__data.md) struct [sensor\_uint64\_sample\_data](structsensor__uint64__data_1_1sensor__uint64__sample__data.md) {

[ 155](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#af0274c154cbc342161b46cb6c3ca0984) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#af0274c154cbc342161b46cb6c3ca0984);

[ 156](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#a37b7eb52969798316f23102dfc66f343) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#a37b7eb52969798316f23102dfc66f343);

[ 157](structsensor__uint64__data.md#a86a1b96bd7a3aeb6b615e6ab0c3a96a6) } [readings](structsensor__uint64__data.md#a86a1b96bd7a3aeb6b615e6ab0c3a96a6)[1];

158};

159

[ 160](sensor__data__types_8h.md#abc9a284dcd602d240f9bd9b097703634)#define PRIsensor\_uint64\_data PRIu64 "ns (%" PRIu64 ")"

161

[ 162](sensor__data__types_8h.md#a06ef9de1e3821289cd22575410edc80f)#define PRIsensor\_uint64\_data\_arg(data\_, readings\_offset\_) \

163 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

164 (data\_).readings[(readings\_offset\_)].value

165

166#ifdef \_\_cplusplus

167}

168#endif

169

170#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_DATA\_TYPES\_H \*/

[q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)

int32\_t q31\_t

32-bit fractional data type in 1.31 format.

**Definition** types.h:35

[types.h](include_2zephyr_2dsp_2types_8h.md)

[inttypes.h](inttypes_8h.md)

[print\_format.h](print__format_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[sensor\_byte\_data::sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md)

**Definition** sensor\_data\_types.h:130

[sensor\_byte\_data::sensor\_byte\_sample\_data::value](structsensor__byte__data_1_1sensor__byte__sample__data.md#a3ad640ff448fe87d2eda7c5118404b7a)

uint8\_t value

**Definition** sensor\_data\_types.h:133

[sensor\_byte\_data::sensor\_byte\_sample\_data::padding](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab07c2a7ce6e47c61249606a88aeda2bd)

uint8\_t padding

**Definition** sensor\_data\_types.h:136

[sensor\_byte\_data::sensor\_byte\_sample\_data::timestamp\_delta](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab29a911990794b35bde3114e813d2c9a)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:131

[sensor\_byte\_data::sensor\_byte\_sample\_data::is\_near](structsensor__byte__data_1_1sensor__byte__sample__data.md#acd42cfa0dc446378cebf998c1b795963)

uint8\_t is\_near

**Definition** sensor\_data\_types.h:135

[sensor\_byte\_data](structsensor__byte__data.md)

Data from a sensor that produces a byte of data.

**Definition** sensor\_data\_types.h:128

[sensor\_byte\_data::header](structsensor__byte__data.md#ab18ad72251bae040fc4752bc125be3ba)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:129

[sensor\_byte\_data::readings](structsensor__byte__data.md#ad4ac07ed10938265e89a43133c41af24)

struct sensor\_byte\_data::sensor\_byte\_sample\_data readings[1]

[sensor\_data\_header](structsensor__data__header.md)

**Definition** sensor\_data\_types.h:19

[sensor\_data\_header::base\_timestamp\_ns](structsensor__data__header.md#a1db93386466e8e4778f448ae0d8ca556)

uint64\_t base\_timestamp\_ns

The closest timestamp for when the first frame was generated as attained by :c:func:k\_uptime\_ticks.

**Definition** sensor\_data\_types.h:24

[sensor\_data\_header::reading\_count](structsensor__data__header.md#ad31873d402a02842eb3098431591c151)

uint16\_t reading\_count

The number of elements in the 'readings' array.

**Definition** sensor\_data\_types.h:30

[sensor\_occurrence\_data::sensor\_occurrence\_sample\_data](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md)

**Definition** sensor\_data\_types.h:82

[sensor\_occurrence\_data::sensor\_occurrence\_sample\_data::timestamp\_delta](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md#a19fb2f7d23a2d58e0bf7f2009f8aba59)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:83

[sensor\_occurrence\_data](structsensor__occurrence__data.md)

Data from a sensor where we only care about an event occurring.

**Definition** sensor\_data\_types.h:80

[sensor\_occurrence\_data::header](structsensor__occurrence__data.md#a06e7c6b24166e1c85d05286d44f60768)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:81

[sensor\_occurrence\_data::readings](structsensor__occurrence__data.md#a181279d03759db87e3855d46d30c5aaf)

struct sensor\_occurrence\_data::sensor\_occurrence\_sample\_data readings[1]

[sensor\_q31\_data::sensor\_q31\_sample\_data](structsensor__q31__data_1_1sensor__q31__sample__data.md)

**Definition** sensor\_data\_types.h:95

[sensor\_q31\_data::sensor\_q31\_sample\_data::density\_ppm](structsensor__q31__data_1_1sensor__q31__sample__data.md#a1493dc66c9d6e4782aed2ddadd74e178)

q31\_t density\_ppm

Unit: parts per million.

**Definition** sensor\_data\_types.h:105

[sensor\_q31\_data::sensor\_q31\_sample\_data::density\_ppb](structsensor__q31__data_1_1sensor__q31__sample__data.md#a215aab449c2b5ee8cf32d971aa5e7708)

q31\_t density\_ppb

Unit: parts per billion.

**Definition** sensor\_data\_types.h:106

[sensor\_q31\_data::sensor\_q31\_sample\_data::density](structsensor__q31__data_1_1sensor__q31__sample__data.md#a2ed468c4be6417f0ea2bb324560e622d)

q31\_t density

Unit: ug/m^3.

**Definition** sensor\_data\_types.h:104

[sensor\_q31\_data::sensor\_q31\_sample\_data::percent](structsensor__q31__data_1_1sensor__q31__sample__data.md#a39f4f4bf64dd49ff2fe027f6e8f8a04d)

q31\_t percent

Unit: percent.

**Definition** sensor\_data\_types.h:102

[sensor\_q31\_data::sensor\_q31\_sample\_data::power](structsensor__q31__data_1_1sensor__q31__sample__data.md#a428adc52033ba50b871c8986e55b06af)

q31\_t power

Unit: watts.

**Definition** sensor\_data\_types.h:110

[sensor\_q31\_data::sensor\_q31\_sample\_data::current](structsensor__q31__data_1_1sensor__q31__sample__data.md#a60f0af8beb207f90ed916fe445525fed)

q31\_t current

Unit: amps.

**Definition** sensor\_data\_types.h:109

[sensor\_q31\_data::sensor\_q31\_sample\_data::light](structsensor__q31__data_1_1sensor__q31__sample__data.md#a7ae2d145a778a72322a78ed433781a0d)

q31\_t light

Unit: lux.

**Definition** sensor\_data\_types.h:99

[sensor\_q31\_data::sensor\_q31\_sample\_data::temperature](structsensor__q31__data_1_1sensor__q31__sample__data.md#a8101423f27270dcee7a356cabcc4d9dd)

q31\_t temperature

Unit: degrees Celsius.

**Definition** sensor\_data\_types.h:101

[sensor\_q31\_data::sensor\_q31\_sample\_data::angle](structsensor__q31__data_1_1sensor__q31__sample__data.md#a9e58a7ea902e27b02b34cc8f619aca96)

q31\_t angle

Unit: degrees.

**Definition** sensor\_data\_types.h:111

[sensor\_q31\_data::sensor\_q31\_sample\_data::electric\_charge](structsensor__q31__data_1_1sensor__q31__sample__data.md#aafb3c0aa55c129b310525f7181b59d51)

q31\_t electric\_charge

Unit: mAh.

**Definition** sensor\_data\_types.h:112

[sensor\_q31\_data::sensor\_q31\_sample\_data::humidity](structsensor__q31__data_1_1sensor__q31__sample__data.md#ac0d247952ae488af354fa1462a014d1d)

q31\_t humidity

Unit: RH.

**Definition** sensor\_data\_types.h:113

[sensor\_q31\_data::sensor\_q31\_sample\_data::distance](structsensor__q31__data_1_1sensor__q31__sample__data.md#ad5d6a48016d474635c0f8a829915a8d2)

q31\_t distance

Unit: meters.

**Definition** sensor\_data\_types.h:103

[sensor\_q31\_data::sensor\_q31\_sample\_data::pressure](structsensor__q31__data_1_1sensor__q31__sample__data.md#ae07081204f6c01334ea9f2e970879b72)

q31\_t pressure

Unit: kilopascal.

**Definition** sensor\_data\_types.h:100

[sensor\_q31\_data::sensor\_q31\_sample\_data::resistance](structsensor__q31__data_1_1sensor__q31__sample__data.md#aeb66bf289c9e17ac6473eb69c22d4eb3)

q31\_t resistance

Unit: ohms.

**Definition** sensor\_data\_types.h:107

[sensor\_q31\_data::sensor\_q31\_sample\_data::voltage](structsensor__q31__data_1_1sensor__q31__sample__data.md#af63a2f7a618c8ff17be31a0543920525)

q31\_t voltage

Unit: volts.

**Definition** sensor\_data\_types.h:108

[sensor\_q31\_data::sensor\_q31\_sample\_data::value](structsensor__q31__data_1_1sensor__q31__sample__data.md#afd73a2b1b6e4e262e89e242853f4ef23)

q31\_t value

**Definition** sensor\_data\_types.h:98

[sensor\_q31\_data::sensor\_q31\_sample\_data::timestamp\_delta](structsensor__q31__data_1_1sensor__q31__sample__data.md#afdf41c27c4f3f55c3ed18c73ab8b6183)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:96

[sensor\_q31\_data](structsensor__q31__data.md)

**Definition** sensor\_data\_types.h:92

[sensor\_q31\_data::readings](structsensor__q31__data.md#a23fc75fd1dafe2789a7d0bff116cb681)

struct sensor\_q31\_data::sensor\_q31\_sample\_data readings[1]

[sensor\_q31\_data::shift](structsensor__q31__data.md#a41f8315cbe740bdc7aec6bd30ce0e096)

int8\_t shift

**Definition** sensor\_data\_types.h:94

[sensor\_q31\_data::header](structsensor__q31__data.md#a9dcc5ffe1d31c37eef75b4132c5f94fd)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:93

[sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md)

**Definition** sensor\_data\_types.h:55

[sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::z](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a5ef91a336b07c2c3e79ed34afbbf8850)

q31\_t z

**Definition** sensor\_data\_types.h:63

[sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::x](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a60a8b323508fb4ececd4c3bdad770525)

q31\_t x

**Definition** sensor\_data\_types.h:61

[sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::timestamp\_delta](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#a62dd4febada1d6b0b0fad600747089a2)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:56

[sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::v](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#aa0de6e1354c259857b2b5a89717a5f9a)

q31\_t v[3]

**Definition** sensor\_data\_types.h:59

[sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::values](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#aa8a07324f3139a6a34f695927a1d6486)

q31\_t values[3]

**Definition** sensor\_data\_types.h:58

[sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data::y](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md#ac78d9fa7e085025f1ccc9f53bf30f3bb)

q31\_t y

**Definition** sensor\_data\_types.h:62

[sensor\_three\_axis\_data](structsensor__three__axis__data.md)

Data for a sensor channel which reports on three axes.

**Definition** sensor\_data\_types.h:52

[sensor\_three\_axis\_data::header](structsensor__three__axis__data.md#a6017fc7964204235e2222c4950f3650a)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:53

[sensor\_three\_axis\_data::readings](structsensor__three__axis__data.md#ad1a498b1cc31b18b17e69300749bbbc0)

struct sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data readings[1]

[sensor\_three\_axis\_data::shift](structsensor__three__axis__data.md#ade10fa0bd60d4b31eebed92e564539c5)

int8\_t shift

**Definition** sensor\_data\_types.h:54

[sensor\_uint64\_data::sensor\_uint64\_sample\_data](structsensor__uint64__data_1_1sensor__uint64__sample__data.md)

**Definition** sensor\_data\_types.h:154

[sensor\_uint64\_data::sensor\_uint64\_sample\_data::value](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#a37b7eb52969798316f23102dfc66f343)

uint64\_t value

**Definition** sensor\_data\_types.h:156

[sensor\_uint64\_data::sensor\_uint64\_sample\_data::timestamp\_delta](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#af0274c154cbc342161b46cb6c3ca0984)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:155

[sensor\_uint64\_data](structsensor__uint64__data.md)

Data from a sensor that produces a count like value.

**Definition** sensor\_data\_types.h:152

[sensor\_uint64\_data::header](structsensor__uint64__data.md#a61e2d0796ba3c0e95a0455e03ce01d76)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:153

[sensor\_uint64\_data::readings](structsensor__uint64__data.md#a86a1b96bd7a3aeb6b615e6ab0c3a96a6)

struct sensor\_uint64\_data::sensor\_uint64\_sample\_data readings[1]

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor\_data\_types.h](sensor__data__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
