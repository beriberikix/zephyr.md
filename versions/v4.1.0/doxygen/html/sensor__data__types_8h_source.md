---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor__data__types_8h_source.html
original_path: doxygen/html/sensor__data__types_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 81](structsensor__game__rotation__vector__data.md)struct [sensor\_game\_rotation\_vector\_data](structsensor__game__rotation__vector__data.md) {

[ 82](structsensor__game__rotation__vector__data.md#abb709edf89ac7dc720a5f307cd1a48bb) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__game__rotation__vector__data.md#abb709edf89ac7dc720a5f307cd1a48bb);

[ 83](structsensor__game__rotation__vector__data.md#a22817d2c2b6b9e04ab574eb816df5442) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensor__game__rotation__vector__data.md#a22817d2c2b6b9e04ab574eb816df5442);

[ 84](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md) struct [sensor\_game\_rotation\_vector\_sample\_data](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md) {

[ 85](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#af453e301f5d1fdacf86daddc0c683498) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#af453e301f5d1fdacf86daddc0c683498);

86 union {

[ 87](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a7e34b93a4d3393b0c7c5918e6f6acb93) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [values](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a7e34b93a4d3393b0c7c5918e6f6acb93)[4];

[ 88](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a44471cf8b4de7faa0f4abf94e9fbb36e) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [v](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a44471cf8b4de7faa0f4abf94e9fbb36e)[4];

89 struct {

[ 90](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a3ff5782e8544602eb858e034a67667b6) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [x](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a3ff5782e8544602eb858e034a67667b6);

[ 91](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a8631568f550497620734f27f2a96553d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [y](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a8631568f550497620734f27f2a96553d);

[ 92](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#acb44311f2b7bc97dae7b26a8256905cf) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [z](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#acb44311f2b7bc97dae7b26a8256905cf);

[ 93](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#ad5fcab0aaca689606cbfacb7f6b13887) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [w](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#ad5fcab0aaca689606cbfacb7f6b13887);

94 };

95 };

[ 96](structsensor__game__rotation__vector__data.md#acc17463dbd99f1ce4fc6a0c42a6bf0c2) } [readings](structsensor__game__rotation__vector__data.md#acc17463dbd99f1ce4fc6a0c42a6bf0c2)[1];

97};

98

[ 99](sensor__data__types_8h.md#a25faf87afbedf805a056ae103e98aa75)#define PRIsensor\_game\_rotation\_vector\_data PRIu64 \

100 "ns, (%" PRIq(6) ", %" PRIq(6) ", %" PRIq(6) ", %" PRIq(6) ")"

101

[ 102](sensor__data__types_8h.md#a416ce85d29265cc6b9993a50656b2cb2)#define PRIsensor\_game\_rotation\_vector\_data\_arg(data\_, readings\_offset\_) \

103 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

104 PRIq\_arg((data\_).readings[(readings\_offset\_)].x, 6, (data\_).shift), \

105 PRIq\_arg((data\_).readings[(readings\_offset\_)].y, 6, (data\_).shift), \

106 PRIq\_arg((data\_).readings[(readings\_offset\_)].z, 6, (data\_).shift), \

107 PRIq\_arg((data\_).readings[(readings\_offset\_)].w, 6, (data\_).shift)

108

[ 112](structsensor__occurrence__data.md)struct [sensor\_occurrence\_data](structsensor__occurrence__data.md) {

[ 113](structsensor__occurrence__data.md#a06e7c6b24166e1c85d05286d44f60768) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__occurrence__data.md#a06e7c6b24166e1c85d05286d44f60768);

[ 114](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md) struct [sensor\_occurrence\_sample\_data](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md) {

[ 115](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md#a19fb2f7d23a2d58e0bf7f2009f8aba59) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md#a19fb2f7d23a2d58e0bf7f2009f8aba59);

[ 116](structsensor__occurrence__data.md#a181279d03759db87e3855d46d30c5aaf) } [readings](structsensor__occurrence__data.md#a181279d03759db87e3855d46d30c5aaf)[1];

117};

118

[ 119](sensor__data__types_8h.md#a9862e4197bb6146b3e41958f427c9f9a)#define PRIsensor\_occurrence\_data PRIu64 "ns"

120

[ 121](sensor__data__types_8h.md#a3f8a660a28578bbb7baf08fefbca7ac4)#define PRIsensor\_occurrence\_data\_arg(data\_, readings\_offset\_) \

122 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta

123

[ 124](structsensor__q31__data.md)struct [sensor\_q31\_data](structsensor__q31__data.md) {

[ 125](structsensor__q31__data.md#a9dcc5ffe1d31c37eef75b4132c5f94fd) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__q31__data.md#a9dcc5ffe1d31c37eef75b4132c5f94fd);

[ 126](structsensor__q31__data.md#a41f8315cbe740bdc7aec6bd30ce0e096) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensor__q31__data.md#a41f8315cbe740bdc7aec6bd30ce0e096);

[ 127](structsensor__q31__data_1_1sensor__q31__sample__data.md) struct [sensor\_q31\_sample\_data](structsensor__q31__data_1_1sensor__q31__sample__data.md) {

[ 128](structsensor__q31__data_1_1sensor__q31__sample__data.md#afdf41c27c4f3f55c3ed18c73ab8b6183) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__q31__data_1_1sensor__q31__sample__data.md#afdf41c27c4f3f55c3ed18c73ab8b6183);

129 union {

[ 130](structsensor__q31__data_1_1sensor__q31__sample__data.md#afd73a2b1b6e4e262e89e242853f4ef23) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [value](structsensor__q31__data_1_1sensor__q31__sample__data.md#afd73a2b1b6e4e262e89e242853f4ef23);

[ 131](structsensor__q31__data_1_1sensor__q31__sample__data.md#a7ae2d145a778a72322a78ed433781a0d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [light](structsensor__q31__data_1_1sensor__q31__sample__data.md#a7ae2d145a778a72322a78ed433781a0d);

[ 132](structsensor__q31__data_1_1sensor__q31__sample__data.md#ae07081204f6c01334ea9f2e970879b72) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [pressure](structsensor__q31__data_1_1sensor__q31__sample__data.md#ae07081204f6c01334ea9f2e970879b72);

[ 133](structsensor__q31__data_1_1sensor__q31__sample__data.md#a8101423f27270dcee7a356cabcc4d9dd) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [temperature](structsensor__q31__data_1_1sensor__q31__sample__data.md#a8101423f27270dcee7a356cabcc4d9dd);

[ 134](structsensor__q31__data_1_1sensor__q31__sample__data.md#a39f4f4bf64dd49ff2fe027f6e8f8a04d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [percent](structsensor__q31__data_1_1sensor__q31__sample__data.md#a39f4f4bf64dd49ff2fe027f6e8f8a04d);

[ 135](structsensor__q31__data_1_1sensor__q31__sample__data.md#ad5d6a48016d474635c0f8a829915a8d2) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [distance](structsensor__q31__data_1_1sensor__q31__sample__data.md#ad5d6a48016d474635c0f8a829915a8d2);

[ 136](structsensor__q31__data_1_1sensor__q31__sample__data.md#a2ed468c4be6417f0ea2bb324560e622d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [density](structsensor__q31__data_1_1sensor__q31__sample__data.md#a2ed468c4be6417f0ea2bb324560e622d);

[ 137](structsensor__q31__data_1_1sensor__q31__sample__data.md#a1493dc66c9d6e4782aed2ddadd74e178) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [density\_ppm](structsensor__q31__data_1_1sensor__q31__sample__data.md#a1493dc66c9d6e4782aed2ddadd74e178);

[ 138](structsensor__q31__data_1_1sensor__q31__sample__data.md#a215aab449c2b5ee8cf32d971aa5e7708) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [density\_ppb](structsensor__q31__data_1_1sensor__q31__sample__data.md#a215aab449c2b5ee8cf32d971aa5e7708);

[ 139](structsensor__q31__data_1_1sensor__q31__sample__data.md#aeb66bf289c9e17ac6473eb69c22d4eb3) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [resistance](structsensor__q31__data_1_1sensor__q31__sample__data.md#aeb66bf289c9e17ac6473eb69c22d4eb3);

[ 140](structsensor__q31__data_1_1sensor__q31__sample__data.md#af63a2f7a618c8ff17be31a0543920525) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [voltage](structsensor__q31__data_1_1sensor__q31__sample__data.md#af63a2f7a618c8ff17be31a0543920525);

[ 141](structsensor__q31__data_1_1sensor__q31__sample__data.md#a60f0af8beb207f90ed916fe445525fed) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [current](structsensor__q31__data_1_1sensor__q31__sample__data.md#a60f0af8beb207f90ed916fe445525fed);

[ 142](structsensor__q31__data_1_1sensor__q31__sample__data.md#a428adc52033ba50b871c8986e55b06af) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [power](structsensor__q31__data_1_1sensor__q31__sample__data.md#a428adc52033ba50b871c8986e55b06af);

[ 143](structsensor__q31__data_1_1sensor__q31__sample__data.md#a9e58a7ea902e27b02b34cc8f619aca96) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [angle](structsensor__q31__data_1_1sensor__q31__sample__data.md#a9e58a7ea902e27b02b34cc8f619aca96);

[ 144](structsensor__q31__data_1_1sensor__q31__sample__data.md#aafb3c0aa55c129b310525f7181b59d51) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [electric\_charge](structsensor__q31__data_1_1sensor__q31__sample__data.md#aafb3c0aa55c129b310525f7181b59d51);

[ 145](structsensor__q31__data_1_1sensor__q31__sample__data.md#ac0d247952ae488af354fa1462a014d1d) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [humidity](structsensor__q31__data_1_1sensor__q31__sample__data.md#ac0d247952ae488af354fa1462a014d1d);

146 };

[ 147](structsensor__q31__data.md#a23fc75fd1dafe2789a7d0bff116cb681) } [readings](structsensor__q31__data.md#a23fc75fd1dafe2789a7d0bff116cb681)[1];

148};

149

[ 150](sensor__data__types_8h.md#a92ae9197089ece9de51db496c9ed5ed6)#define PRIsensor\_q31\_data PRIu64 "ns (%" PRIq(6) ")"

151

[ 152](sensor__data__types_8h.md#aac3d2a0c462c05c26f7dee0fa0e1ef62)#define PRIsensor\_q31\_data\_arg(data\_, readings\_offset\_) \

153 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

154 PRIq\_arg((data\_).readings[(readings\_offset\_)].value, 6, (data\_).shift)

155

[ 160](structsensor__byte__data.md)struct [sensor\_byte\_data](structsensor__byte__data.md) {

[ 161](structsensor__byte__data.md#ab18ad72251bae040fc4752bc125be3ba) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__byte__data.md#ab18ad72251bae040fc4752bc125be3ba);

[ 162](structsensor__byte__data_1_1sensor__byte__sample__data.md) struct [sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md) {

[ 163](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab29a911990794b35bde3114e813d2c9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab29a911990794b35bde3114e813d2c9a);

164 union {

[ 165](structsensor__byte__data_1_1sensor__byte__sample__data.md#a3ad640ff448fe87d2eda7c5118404b7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structsensor__byte__data_1_1sensor__byte__sample__data.md#a3ad640ff448fe87d2eda7c5118404b7a);

166 struct {

[ 167](structsensor__byte__data_1_1sensor__byte__sample__data.md#acd42cfa0dc446378cebf998c1b795963) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_near](structsensor__byte__data_1_1sensor__byte__sample__data.md#acd42cfa0dc446378cebf998c1b795963): 1;

[ 168](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab07c2a7ce6e47c61249606a88aeda2bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [padding](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab07c2a7ce6e47c61249606a88aeda2bd): 7;

169 };

170 };

[ 171](structsensor__byte__data.md#ad4ac07ed10938265e89a43133c41af24) } [readings](structsensor__byte__data.md#ad4ac07ed10938265e89a43133c41af24)[1];

172};

173

[ 174](sensor__data__types_8h.md#af73f68f6b94dc1251dfeeb5caf141e94)#define PRIsensor\_byte\_data(field\_name\_) PRIu64 "ns (" STRINGIFY(field\_name\_) " = %" PRIu8 ")"

175

[ 176](sensor__data__types_8h.md#a36cfa50e20150d44c6a254afc149eb5b)#define PRIsensor\_byte\_data\_arg(data\_, readings\_offset\_, field\_name\_) \

177 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

178 (data\_).readings[(readings\_offset\_)].field\_name\_

179

[ 184](structsensor__uint64__data.md)struct [sensor\_uint64\_data](structsensor__uint64__data.md) {

[ 185](structsensor__uint64__data.md#a61e2d0796ba3c0e95a0455e03ce01d76) struct [sensor\_data\_header](structsensor__data__header.md) [header](structsensor__uint64__data.md#a61e2d0796ba3c0e95a0455e03ce01d76);

[ 186](structsensor__uint64__data_1_1sensor__uint64__sample__data.md) struct [sensor\_uint64\_sample\_data](structsensor__uint64__data_1_1sensor__uint64__sample__data.md) {

[ 187](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#af0274c154cbc342161b46cb6c3ca0984) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#af0274c154cbc342161b46cb6c3ca0984);

[ 188](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#a37b7eb52969798316f23102dfc66f343) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#a37b7eb52969798316f23102dfc66f343);

[ 189](structsensor__uint64__data.md#a86a1b96bd7a3aeb6b615e6ab0c3a96a6) } [readings](structsensor__uint64__data.md#a86a1b96bd7a3aeb6b615e6ab0c3a96a6)[1];

190};

191

[ 192](sensor__data__types_8h.md#abc9a284dcd602d240f9bd9b097703634)#define PRIsensor\_uint64\_data PRIu64 "ns (%" PRIu64 ")"

193

[ 194](sensor__data__types_8h.md#a06ef9de1e3821289cd22575410edc80f)#define PRIsensor\_uint64\_data\_arg(data\_, readings\_offset\_) \

195 (data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

196 (data\_).readings[(readings\_offset\_)].value

197

198#ifdef \_\_cplusplus

199}

200#endif

201

202#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_DATA\_TYPES\_H \*/

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

**Definition** sensor\_data\_types.h:162

[sensor\_byte\_data::sensor\_byte\_sample\_data::value](structsensor__byte__data_1_1sensor__byte__sample__data.md#a3ad640ff448fe87d2eda7c5118404b7a)

uint8\_t value

**Definition** sensor\_data\_types.h:165

[sensor\_byte\_data::sensor\_byte\_sample\_data::padding](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab07c2a7ce6e47c61249606a88aeda2bd)

uint8\_t padding

**Definition** sensor\_data\_types.h:168

[sensor\_byte\_data::sensor\_byte\_sample\_data::timestamp\_delta](structsensor__byte__data_1_1sensor__byte__sample__data.md#ab29a911990794b35bde3114e813d2c9a)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:163

[sensor\_byte\_data::sensor\_byte\_sample\_data::is\_near](structsensor__byte__data_1_1sensor__byte__sample__data.md#acd42cfa0dc446378cebf998c1b795963)

uint8\_t is\_near

**Definition** sensor\_data\_types.h:167

[sensor\_byte\_data](structsensor__byte__data.md)

Data from a sensor that produces a byte of data.

**Definition** sensor\_data\_types.h:160

[sensor\_byte\_data::header](structsensor__byte__data.md#ab18ad72251bae040fc4752bc125be3ba)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:161

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

[sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md)

**Definition** sensor\_data\_types.h:84

[sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::x](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a3ff5782e8544602eb858e034a67667b6)

q31\_t x

**Definition** sensor\_data\_types.h:90

[sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::v](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a44471cf8b4de7faa0f4abf94e9fbb36e)

q31\_t v[4]

**Definition** sensor\_data\_types.h:88

[sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::values](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a7e34b93a4d3393b0c7c5918e6f6acb93)

q31\_t values[4]

**Definition** sensor\_data\_types.h:87

[sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::y](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#a8631568f550497620734f27f2a96553d)

q31\_t y

**Definition** sensor\_data\_types.h:91

[sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::z](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#acb44311f2b7bc97dae7b26a8256905cf)

q31\_t z

**Definition** sensor\_data\_types.h:92

[sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::w](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#ad5fcab0aaca689606cbfacb7f6b13887)

q31\_t w

**Definition** sensor\_data\_types.h:93

[sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data::timestamp\_delta](structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.md#af453e301f5d1fdacf86daddc0c683498)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:85

[sensor\_game\_rotation\_vector\_data](structsensor__game__rotation__vector__data.md)

Data for a sensor channel which reports game rotation vector data.

**Definition** sensor\_data\_types.h:81

[sensor\_game\_rotation\_vector\_data::shift](structsensor__game__rotation__vector__data.md#a22817d2c2b6b9e04ab574eb816df5442)

int8\_t shift

**Definition** sensor\_data\_types.h:83

[sensor\_game\_rotation\_vector\_data::header](structsensor__game__rotation__vector__data.md#abb709edf89ac7dc720a5f307cd1a48bb)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:82

[sensor\_game\_rotation\_vector\_data::readings](structsensor__game__rotation__vector__data.md#acc17463dbd99f1ce4fc6a0c42a6bf0c2)

struct sensor\_game\_rotation\_vector\_data::sensor\_game\_rotation\_vector\_sample\_data readings[1]

[sensor\_occurrence\_data::sensor\_occurrence\_sample\_data](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md)

**Definition** sensor\_data\_types.h:114

[sensor\_occurrence\_data::sensor\_occurrence\_sample\_data::timestamp\_delta](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md#a19fb2f7d23a2d58e0bf7f2009f8aba59)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:115

[sensor\_occurrence\_data](structsensor__occurrence__data.md)

Data from a sensor where we only care about an event occurring.

**Definition** sensor\_data\_types.h:112

[sensor\_occurrence\_data::header](structsensor__occurrence__data.md#a06e7c6b24166e1c85d05286d44f60768)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:113

[sensor\_occurrence\_data::readings](structsensor__occurrence__data.md#a181279d03759db87e3855d46d30c5aaf)

struct sensor\_occurrence\_data::sensor\_occurrence\_sample\_data readings[1]

[sensor\_q31\_data::sensor\_q31\_sample\_data](structsensor__q31__data_1_1sensor__q31__sample__data.md)

**Definition** sensor\_data\_types.h:127

[sensor\_q31\_data::sensor\_q31\_sample\_data::density\_ppm](structsensor__q31__data_1_1sensor__q31__sample__data.md#a1493dc66c9d6e4782aed2ddadd74e178)

q31\_t density\_ppm

Unit: parts per million.

**Definition** sensor\_data\_types.h:137

[sensor\_q31\_data::sensor\_q31\_sample\_data::density\_ppb](structsensor__q31__data_1_1sensor__q31__sample__data.md#a215aab449c2b5ee8cf32d971aa5e7708)

q31\_t density\_ppb

Unit: parts per billion.

**Definition** sensor\_data\_types.h:138

[sensor\_q31\_data::sensor\_q31\_sample\_data::density](structsensor__q31__data_1_1sensor__q31__sample__data.md#a2ed468c4be6417f0ea2bb324560e622d)

q31\_t density

Unit: ug/m^3.

**Definition** sensor\_data\_types.h:136

[sensor\_q31\_data::sensor\_q31\_sample\_data::percent](structsensor__q31__data_1_1sensor__q31__sample__data.md#a39f4f4bf64dd49ff2fe027f6e8f8a04d)

q31\_t percent

Unit: percent.

**Definition** sensor\_data\_types.h:134

[sensor\_q31\_data::sensor\_q31\_sample\_data::power](structsensor__q31__data_1_1sensor__q31__sample__data.md#a428adc52033ba50b871c8986e55b06af)

q31\_t power

Unit: watts.

**Definition** sensor\_data\_types.h:142

[sensor\_q31\_data::sensor\_q31\_sample\_data::current](structsensor__q31__data_1_1sensor__q31__sample__data.md#a60f0af8beb207f90ed916fe445525fed)

q31\_t current

Unit: amps.

**Definition** sensor\_data\_types.h:141

[sensor\_q31\_data::sensor\_q31\_sample\_data::light](structsensor__q31__data_1_1sensor__q31__sample__data.md#a7ae2d145a778a72322a78ed433781a0d)

q31\_t light

Unit: lux.

**Definition** sensor\_data\_types.h:131

[sensor\_q31\_data::sensor\_q31\_sample\_data::temperature](structsensor__q31__data_1_1sensor__q31__sample__data.md#a8101423f27270dcee7a356cabcc4d9dd)

q31\_t temperature

Unit: degrees Celsius.

**Definition** sensor\_data\_types.h:133

[sensor\_q31\_data::sensor\_q31\_sample\_data::angle](structsensor__q31__data_1_1sensor__q31__sample__data.md#a9e58a7ea902e27b02b34cc8f619aca96)

q31\_t angle

Unit: degrees.

**Definition** sensor\_data\_types.h:143

[sensor\_q31\_data::sensor\_q31\_sample\_data::electric\_charge](structsensor__q31__data_1_1sensor__q31__sample__data.md#aafb3c0aa55c129b310525f7181b59d51)

q31\_t electric\_charge

Unit: mAh.

**Definition** sensor\_data\_types.h:144

[sensor\_q31\_data::sensor\_q31\_sample\_data::humidity](structsensor__q31__data_1_1sensor__q31__sample__data.md#ac0d247952ae488af354fa1462a014d1d)

q31\_t humidity

Unit: RH.

**Definition** sensor\_data\_types.h:145

[sensor\_q31\_data::sensor\_q31\_sample\_data::distance](structsensor__q31__data_1_1sensor__q31__sample__data.md#ad5d6a48016d474635c0f8a829915a8d2)

q31\_t distance

Unit: meters.

**Definition** sensor\_data\_types.h:135

[sensor\_q31\_data::sensor\_q31\_sample\_data::pressure](structsensor__q31__data_1_1sensor__q31__sample__data.md#ae07081204f6c01334ea9f2e970879b72)

q31\_t pressure

Unit: kilopascal.

**Definition** sensor\_data\_types.h:132

[sensor\_q31\_data::sensor\_q31\_sample\_data::resistance](structsensor__q31__data_1_1sensor__q31__sample__data.md#aeb66bf289c9e17ac6473eb69c22d4eb3)

q31\_t resistance

Unit: ohms.

**Definition** sensor\_data\_types.h:139

[sensor\_q31\_data::sensor\_q31\_sample\_data::voltage](structsensor__q31__data_1_1sensor__q31__sample__data.md#af63a2f7a618c8ff17be31a0543920525)

q31\_t voltage

Unit: volts.

**Definition** sensor\_data\_types.h:140

[sensor\_q31\_data::sensor\_q31\_sample\_data::value](structsensor__q31__data_1_1sensor__q31__sample__data.md#afd73a2b1b6e4e262e89e242853f4ef23)

q31\_t value

**Definition** sensor\_data\_types.h:130

[sensor\_q31\_data::sensor\_q31\_sample\_data::timestamp\_delta](structsensor__q31__data_1_1sensor__q31__sample__data.md#afdf41c27c4f3f55c3ed18c73ab8b6183)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:128

[sensor\_q31\_data](structsensor__q31__data.md)

**Definition** sensor\_data\_types.h:124

[sensor\_q31\_data::readings](structsensor__q31__data.md#a23fc75fd1dafe2789a7d0bff116cb681)

struct sensor\_q31\_data::sensor\_q31\_sample\_data readings[1]

[sensor\_q31\_data::shift](structsensor__q31__data.md#a41f8315cbe740bdc7aec6bd30ce0e096)

int8\_t shift

**Definition** sensor\_data\_types.h:126

[sensor\_q31\_data::header](structsensor__q31__data.md#a9dcc5ffe1d31c37eef75b4132c5f94fd)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:125

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

**Definition** sensor\_data\_types.h:186

[sensor\_uint64\_data::sensor\_uint64\_sample\_data::value](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#a37b7eb52969798316f23102dfc66f343)

uint64\_t value

**Definition** sensor\_data\_types.h:188

[sensor\_uint64\_data::sensor\_uint64\_sample\_data::timestamp\_delta](structsensor__uint64__data_1_1sensor__uint64__sample__data.md#af0274c154cbc342161b46cb6c3ca0984)

uint32\_t timestamp\_delta

**Definition** sensor\_data\_types.h:187

[sensor\_uint64\_data](structsensor__uint64__data.md)

Data from a sensor that produces a count like value.

**Definition** sensor\_data\_types.h:184

[sensor\_uint64\_data::header](structsensor__uint64__data.md#a61e2d0796ba3c0e95a0455e03ce01d76)

struct sensor\_data\_header header

**Definition** sensor\_data\_types.h:185

[sensor\_uint64\_data::readings](structsensor__uint64__data.md#a86a1b96bd7a3aeb6b615e6ab0c3a96a6)

struct sensor\_uint64\_data::sensor\_uint64\_sample\_data readings[1]

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor\_data\_types.h](sensor__data__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
