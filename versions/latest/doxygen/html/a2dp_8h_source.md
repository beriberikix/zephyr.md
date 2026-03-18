---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/a2dp_8h_source.html
original_path: doxygen/html/a2dp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_H\_

12

13#include <[stdint.h](stdint_8h.md)>

14

15#include <[zephyr/bluetooth/avdtp.h](avdtp_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 22](structbt__a2dp__stream.md)struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) {

23 /\* TODO \*/

24};

25

[ 27](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49)enum [bt\_a2dp\_codec\_id](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49) {

[ 29](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49abd097d204d4136c5205afe7dfe3dfe00) [BT\_A2DP\_SBC](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49abd097d204d4136c5205afe7dfe3dfe00) = 0x00,

[ 31](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49a1f1840d90c1d5ee28b650978bf012497) [BT\_A2DP\_MPEG1](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49a1f1840d90c1d5ee28b650978bf012497) = 0x01,

[ 33](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49aefe729d388e0a3d8bb7759b986123c88) [BT\_A2DP\_MPEG2](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49aefe729d388e0a3d8bb7759b986123c88) = 0x02,

[ 35](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49a8b969e35e28d18cf05802e1381995e83) [BT\_A2DP\_ATRAC](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49a8b969e35e28d18cf05802e1381995e83) = 0x04,

[ 37](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49ad3c292360558ea515a84d570c43c1701) [BT\_A2DP\_VENDOR](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49ad3c292360558ea515a84d570c43c1701) = 0xff

38};

39

[ 41](structbt__a2dp__preset.md)struct [bt\_a2dp\_preset](structbt__a2dp__preset.md) {

[ 43](structbt__a2dp__preset.md#a83c5d7c862b47616ea00b46a1e75874a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structbt__a2dp__preset.md#a83c5d7c862b47616ea00b46a1e75874a);

[ 45](structbt__a2dp__preset.md#a8fdf5815108d7d0b28521c649d78e03f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [preset](structbt__a2dp__preset.md#a8fdf5815108d7d0b28521c649d78e03f)[0];

46};

47

[ 49](structbt__a2dp__endpoint.md)struct [bt\_a2dp\_endpoint](structbt__a2dp__endpoint.md) {

[ 51](structbt__a2dp__endpoint.md#a924c4a4d4e1e90eb032ae327f75aac65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [codec\_id](structbt__a2dp__endpoint.md#a924c4a4d4e1e90eb032ae327f75aac65);

[ 53](structbt__a2dp__endpoint.md#a5db1b3737f3127669a99013801516413) struct [bt\_avdtp\_seid\_lsep](structbt__avdtp__seid__lsep.md) [info](structbt__a2dp__endpoint.md#a5db1b3737f3127669a99013801516413);

[ 55](structbt__a2dp__endpoint.md#a9f502266d67fe501f0dd179b4b9017f1) struct [bt\_a2dp\_preset](structbt__a2dp__preset.md) \*[preset](structbt__a2dp__endpoint.md#a9f502266d67fe501f0dd179b4b9017f1);

[ 57](structbt__a2dp__endpoint.md#a178e9894c3399cc96340eab917d0ba49) struct [bt\_a2dp\_preset](structbt__a2dp__preset.md) \*[caps](structbt__a2dp__endpoint.md#a178e9894c3399cc96340eab917d0ba49);

58};

59

[ 61](a2dp_8h.md#a6244624a5a6adb228209853282d6f7da)enum [MEDIA\_TYPE](a2dp_8h.md#a6244624a5a6adb228209853282d6f7da) {

[ 63](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daa66c74e3fc9ff01974bd9afad0ad03ac1) [BT\_A2DP\_AUDIO](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daa66c74e3fc9ff01974bd9afad0ad03ac1) = 0x00,

[ 65](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daacd255bc0a24d060761460859b8a47e28) [BT\_A2DP\_VIDEO](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daacd255bc0a24d060761460859b8a47e28) = 0x01,

[ 67](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daa4fdde75334bd82a9127d1752b561710a) [BT\_A2DP\_MULTIMEDIA](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daa4fdde75334bd82a9127d1752b561710a) = 0x02

68};

69

[ 71](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306ce)enum [ROLE\_TYPE](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306ce) {

[ 73](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306cea81c8031ba8926d0471226a8d146abcb8) [BT\_A2DP\_SOURCE](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306cea81c8031ba8926d0471226a8d146abcb8) = 0,

[ 75](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306ceac9ae751ed0468f82fc606daf3a56f240) [BT\_A2DP\_SINK](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306ceac9ae751ed0468f82fc606daf3a56f240) = 1

76};

77

79struct bt\_a2dp;

80

[ 92](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)struct bt\_a2dp \*[bt\_a2dp\_connect](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)(struct bt\_conn \*conn);

93

[ 106](a2dp_8h.md#ad2b12e8d4b509d6a3c360b64225b536e)int [bt\_a2dp\_register\_endpoint](a2dp_8h.md#ad2b12e8d4b509d6a3c360b64225b536e)(struct [bt\_a2dp\_endpoint](structbt__a2dp__endpoint.md) \*endpoint,

107 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) media\_type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) role);

108

109#ifdef \_\_cplusplus

110}

111#endif

112

113#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_A2DP\_H\_ \*/

[MEDIA\_TYPE](a2dp_8h.md#a6244624a5a6adb228209853282d6f7da)

MEDIA\_TYPE

Stream End Point Media Type.

**Definition** a2dp.h:61

[BT\_A2DP\_MULTIMEDIA](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daa4fdde75334bd82a9127d1752b561710a)

@ BT\_A2DP\_MULTIMEDIA

Multimedia Media Type.

**Definition** a2dp.h:67

[BT\_A2DP\_AUDIO](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daa66c74e3fc9ff01974bd9afad0ad03ac1)

@ BT\_A2DP\_AUDIO

Audio Media Type.

**Definition** a2dp.h:63

[BT\_A2DP\_VIDEO](a2dp_8h.md#a6244624a5a6adb228209853282d6f7daacd255bc0a24d060761460859b8a47e28)

@ BT\_A2DP\_VIDEO

Video Media Type.

**Definition** a2dp.h:65

[ROLE\_TYPE](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306ce)

ROLE\_TYPE

Stream End Point Role.

**Definition** a2dp.h:71

[BT\_A2DP\_SOURCE](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306cea81c8031ba8926d0471226a8d146abcb8)

@ BT\_A2DP\_SOURCE

Source Role.

**Definition** a2dp.h:73

[BT\_A2DP\_SINK](a2dp_8h.md#aa6f56dccc53ab8d3a1cf6c2bde5306ceac9ae751ed0468f82fc606daf3a56f240)

@ BT\_A2DP\_SINK

Sink Role.

**Definition** a2dp.h:75

[bt\_a2dp\_connect](a2dp_8h.md#abc74f6c2a0cf619adbefcf9ffbca1c03)

struct bt\_a2dp \* bt\_a2dp\_connect(struct bt\_conn \*conn)

A2DP Connect.

[bt\_a2dp\_register\_endpoint](a2dp_8h.md#ad2b12e8d4b509d6a3c360b64225b536e)

int bt\_a2dp\_register\_endpoint(struct bt\_a2dp\_endpoint \*endpoint, uint8\_t media\_type, uint8\_t role)

Endpoint Registration.

[bt\_a2dp\_codec\_id](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49)

bt\_a2dp\_codec\_id

Codec ID.

**Definition** a2dp.h:27

[BT\_A2DP\_MPEG1](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49a1f1840d90c1d5ee28b650978bf012497)

@ BT\_A2DP\_MPEG1

Codec MPEG-1.

**Definition** a2dp.h:31

[BT\_A2DP\_ATRAC](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49a8b969e35e28d18cf05802e1381995e83)

@ BT\_A2DP\_ATRAC

Codec ATRAC.

**Definition** a2dp.h:35

[BT\_A2DP\_SBC](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49abd097d204d4136c5205afe7dfe3dfe00)

@ BT\_A2DP\_SBC

Codec SBC.

**Definition** a2dp.h:29

[BT\_A2DP\_VENDOR](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49ad3c292360558ea515a84d570c43c1701)

@ BT\_A2DP\_VENDOR

Codec Non-A2DP.

**Definition** a2dp.h:37

[BT\_A2DP\_MPEG2](a2dp_8h.md#ade5dadb0a608a460be3c3fcb59413b49aefe729d388e0a3d8bb7759b986123c88)

@ BT\_A2DP\_MPEG2

Codec MPEG-2.

**Definition** a2dp.h:33

[avdtp.h](avdtp_8h.md)

Audio/Video Distribution Transport Protocol header.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_a2dp\_endpoint](structbt__a2dp__endpoint.md)

Stream End Point.

**Definition** a2dp.h:49

[bt\_a2dp\_endpoint::caps](structbt__a2dp__endpoint.md#a178e9894c3399cc96340eab917d0ba49)

struct bt\_a2dp\_preset \* caps

Capabilities.

**Definition** a2dp.h:57

[bt\_a2dp\_endpoint::info](structbt__a2dp__endpoint.md#a5db1b3737f3127669a99013801516413)

struct bt\_avdtp\_seid\_lsep info

Stream End Point Information.

**Definition** a2dp.h:53

[bt\_a2dp\_endpoint::codec\_id](structbt__a2dp__endpoint.md#a924c4a4d4e1e90eb032ae327f75aac65)

uint8\_t codec\_id

Code ID.

**Definition** a2dp.h:51

[bt\_a2dp\_endpoint::preset](structbt__a2dp__endpoint.md#a9f502266d67fe501f0dd179b4b9017f1)

struct bt\_a2dp\_preset \* preset

Pointer to preset codec chosen.

**Definition** a2dp.h:55

[bt\_a2dp\_preset](structbt__a2dp__preset.md)

Preset for the endpoint.

**Definition** a2dp.h:41

[bt\_a2dp\_preset::len](structbt__a2dp__preset.md#a83c5d7c862b47616ea00b46a1e75874a)

uint8\_t len

Length of preset.

**Definition** a2dp.h:43

[bt\_a2dp\_preset::preset](structbt__a2dp__preset.md#a8fdf5815108d7d0b28521c649d78e03f)

uint8\_t preset[0]

Preset.

**Definition** a2dp.h:45

[bt\_a2dp\_stream](structbt__a2dp__stream.md)

Stream Structure.

**Definition** a2dp.h:22

[bt\_avdtp\_seid\_lsep](structbt__avdtp__seid__lsep.md)

AVDTP Local SEP.

**Definition** avdtp.h:36

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [a2dp.h](a2dp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
