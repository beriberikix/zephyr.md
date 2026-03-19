---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/midi_8h_source.html
original_path: doxygen/html/midi_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

midi.h

[Go to the documentation of this file.](midi_8h.md)

1/\*

2 \* Copyright (c) 2024 Titouan Christophe

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_AUDIO\_MIDI\_H\_

8#define ZEPHYR\_INCLUDE\_AUDIO\_MIDI\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[stdint.h](stdint_8h.md)>

15

26

[ 30](structmidi__ump.md)struct [midi\_ump](structmidi__ump.md) {

[ 31](structmidi__ump.md#a9c38cadb8046ba91b080604ac66ea89f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structmidi__ump.md#a9c38cadb8046ba91b080604ac66ea89f)[4];

32};

33

40

[ 42](group__midi__ump__mt.md#ga6b9f0ce12bbdcb92fb4003ba9d5ed3e3)#define UMP\_MT\_UTILITY 0x00

[ 44](group__midi__ump__mt.md#gab8f194f60f1b5de7f050009275e44412)#define UMP\_MT\_SYS\_RT\_COMMON 0x01

[ 46](group__midi__ump__mt.md#gae086e5899933e436715ed2321607ef36)#define UMP\_MT\_MIDI1\_CHANNEL\_VOICE 0x02

[ 48](group__midi__ump__mt.md#ga235bf38958774c9ccc8864b98cff7ff9)#define UMP\_MT\_DATA\_64 0x03

[ 50](group__midi__ump__mt.md#ga9f2ac215138eb6e958df9558547f805a)#define UMP\_MT\_MIDI2\_CHANNEL\_VOICE 0x04

[ 52](group__midi__ump__mt.md#gabe19506f8d84dbc84a46114768853d5b)#define UMP\_MT\_DATA\_128 0x05

[ 54](group__midi__ump__mt.md#ga916fba3c7a01dfff98f94c700a585fd5)#define UMP\_MT\_FLEX\_DATA 0x0d

[ 56](group__midi__ump__mt.md#gae14fb523ae456ca3e49a86de7d197e55)#define UMP\_MT\_UMP\_STREAM 0x0f

58

[ 63](group__midi__ump.md#gafab438886f69fb74a6e058f9343867aa)#define UMP\_MT(ump) \

64 ((ump).data[0] >> 28)

65

[ 70](group__midi__ump.md#gac718c321652066f1537ead1524137949)#define UMP\_NUM\_WORDS\_LOOKUP\_TABLE \

71 ((0U << 0) | (0U << 2) | (0U << 4) | (1U << 6) | \

72 (1U << 8) | (3U << 10) | (0U << 12) | (0U << 14) | \

73 (1U << 16) | (1U << 18) | (1U << 20) | (2U << 22) | \

74 (2U << 24) | (3U << 26) | (3U << 28) | (3U << 30))

75

[ 81](group__midi__ump.md#ga31e6cb035180b3afca9980307a07c038)#define UMP\_NUM\_WORDS(ump) \

82 (1 + ((UMP\_NUM\_WORDS\_LOOKUP\_TABLE >> (2 \* UMP\_MT(ump))) & 3))

83

[ 88](group__midi__ump.md#ga497e212c131b7366878e46f63727cab5)#define UMP\_GROUP(ump) \

89 (((ump).data[0] >> 24) & 0x0f)

90

[ 95](group__midi__ump.md#ga407db6234865dd53a0939b9e6ca7455c)#define UMP\_MIDI\_STATUS(ump) \

96 (((ump).data[0] >> 16) & 0xff)

97

[ 102](group__midi__ump.md#gac3af021e7300ab96e449da048545900f)#define UMP\_MIDI\_COMMAND(ump) \

103 (UMP\_MIDI\_STATUS(ump) >> 4)

104

[ 108](group__midi__ump.md#ga8ecdaa13831c0cf1abf79da0b343416f)#define UMP\_MIDI\_CHANNEL(ump) \

109 (UMP\_MIDI\_STATUS(ump) & 0x0f)

110

[ 114](group__midi__ump.md#gac64740902864ecb903f70083f2c638d2)#define UMP\_MIDI1\_P1(ump) \

115 (((ump).data[0] >> 8) & 0x7f)

116

[ 120](group__midi__ump.md#ga1c6c6f8928071d4d77744404e62168b4)#define UMP\_MIDI1\_P2(ump) \

121 ((ump).data[0] & 0x7f)

122

[ 132](group__midi__ump.md#gac05c1718b33d08a92bae9b4974ced501)#define UMP\_MIDI1\_CHANNEL\_VOICE(group, command, channel, p1, p2) \

133 (struct midi\_ump) {.data = { \

134 (UMP\_MT\_MIDI1\_CHANNEL\_VOICE << 28) \

135 | (((group) & 0x0f) << 24) \

136 | (((command) & 0x0f) << 20) \

137 | (((channel) & 0x0f) << 16) \

138 | (((p1) & 0x7f) << 8) \

139 | ((p2) & 0x7f) \

140 }}

141

[ 151](group__midi__ump__cmd.md#ga8300450177c4f1ec7c11ed7d8886f87e)#define UMP\_MIDI\_NOTE\_OFF 0x8

[ 152](group__midi__ump__cmd.md#ga85749d1edff030bc0d8b131b9116911e)#define UMP\_MIDI\_NOTE\_ON 0x9

[ 153](group__midi__ump__cmd.md#ga7fae224629121ad30f9f38241885452c)#define UMP\_MIDI\_AFTERTOUCH 0xa

[ 154](group__midi__ump__cmd.md#gad4b17d74027a541957c933074d0f2d1e)#define UMP\_MIDI\_CONTROL\_CHANGE 0xb

[ 155](group__midi__ump__cmd.md#gaad34de6aae0e22f5c84ef50e488e2d1a)#define UMP\_MIDI\_PROGRAM\_CHANGE 0xc

[ 156](group__midi__ump__cmd.md#gaf5708894b80514023949e163f9687fb8)#define UMP\_MIDI\_CHAN\_AFTERTOUCH 0xd

[ 157](group__midi__ump__cmd.md#gab11535e72a74baa71491264dd2c16192)#define UMP\_MIDI\_PITCH\_BEND 0xe

159

[ 169](group__midi__ump.md#ga06562acb0ec4d618d2e05b94c0a1bc4f)#define UMP\_SYS\_RT\_COMMON(group, status, p1, p2) \

170 (struct midi\_ump) {.data = { \

171 (UMP\_MT\_SYS\_RT\_COMMON << 28) \

172 | (((group) & 0x0f) << 24) \

173 | ((status) << 16) \

174 | (((p1) & 0x7f) << 8) \

175 | ((p2) & 0x7f) \

176 }}

177

[ 186](group__midi__ump__sys.md#ga85394094ca6d908b7886adc4caceb671)#define UMP\_SYS\_MIDI\_TIME\_CODE 0xf1

[ 187](group__midi__ump__sys.md#ga254845a2c32a190b0bfc217025c5ad1d)#define UMP\_SYS\_SONG\_POSITION 0xf2

[ 188](group__midi__ump__sys.md#ga1d27e0f6fffd7ec05f58b56be78d9a8d)#define UMP\_SYS\_SONG\_SELECT 0xf3

[ 189](group__midi__ump__sys.md#ga4aa12e0cdb101a38b938876ebdcca64b)#define UMP\_SYS\_TUNE\_REQUEST 0xf6

[ 190](group__midi__ump__sys.md#gae064f3f47a9387076f5045e12e6ef7b7)#define UMP\_SYS\_TIMING\_CLOCK 0xf8

[ 191](group__midi__ump__sys.md#ga368ad3719080979709699feb3d002dff)#define UMP\_SYS\_START 0xfa

[ 192](group__midi__ump__sys.md#ga766b54e3caced69c147dbc94eb932595)#define UMP\_SYS\_CONTINUE 0xfb

[ 193](group__midi__ump__sys.md#ga95542dda8f7f73f738c3ae298ca42f44)#define UMP\_SYS\_STOP 0xfc

[ 194](group__midi__ump__sys.md#gaeb794e3933a2488eadb5f57ba971f81d)#define UMP\_SYS\_ACTIVE\_SENSING 0xfe

[ 195](group__midi__ump__sys.md#ga5bd5358ae1847774409216f4e246f6f4)#define UMP\_SYS\_RESET 0xff

197

199

200#ifdef \_\_cplusplus

201}

202#endif

203

204#endif

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[midi\_ump](structmidi__ump.md)

Universal MIDI Packet container.

**Definition** midi.h:30

[midi\_ump::data](structmidi__ump.md#a9c38cadb8046ba91b080604ac66ea89f)

uint32\_t data[4]

Raw content, in the CPU native endianness.

**Definition** midi.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [audio](dir_07210b4c80db401fef5ca2f0f02fdac3.md)
- [midi.h](midi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
