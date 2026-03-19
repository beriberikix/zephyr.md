---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dfu_8h_source.html
original_path: doxygen/html/dfu_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu.h

[Go to the documentation of this file.](dfu_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_H\_\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_H\_\_

9

10#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

11

12#include <[zephyr/kernel.h](kernel_8h.md)>

13#include <[zephyr/bluetooth/mesh/blob.h](blob_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

25#ifndef CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN

[ 26](group__bt__mesh__dfu.md#gacd0f7b01837809a0a92d27f248a9fdd3)#define CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN 0

27#endif

28

29#ifndef CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN

[ 30](group__bt__mesh__dfu.md#ga8f2afd35a2215f51cd08debe6e1c8ae4)#define CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN 0

31#endif

32

33#ifndef CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN

[ 34](group__bt__mesh__dfu.md#gaa0812409217dd069b00d386d8ab17f5c)#define CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN 0

35#endif

36

37#ifndef CONFIG\_BT\_MESH\_DFU\_SLOT\_CNT

[ 38](group__bt__mesh__dfu.md#gab517e917ec3279ba50f1ac92ec62b8cf)#define CONFIG\_BT\_MESH\_DFU\_SLOT\_CNT 0

39#endif

40

[ 42](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2)enum [bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2) {

[ 44](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156) [BT\_MESH\_DFU\_PHASE\_IDLE](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156),

45

[ 47](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771) [BT\_MESH\_DFU\_PHASE\_TRANSFER\_ERR](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771),

48

[ 50](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad) [BT\_MESH\_DFU\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad),

51

[ 53](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65) [BT\_MESH\_DFU\_PHASE\_VERIFY](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65),

54

[ 56](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8) [BT\_MESH\_DFU\_PHASE\_VERIFY\_OK](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8),

57

[ 59](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e) [BT\_MESH\_DFU\_PHASE\_VERIFY\_FAIL](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e),

60

[ 62](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f) [BT\_MESH\_DFU\_PHASE\_APPLYING](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f),

63

[ 65](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51) [BT\_MESH\_DFU\_PHASE\_TRANSFER\_CANCELED](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51),

66

[ 68](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca) [BT\_MESH\_DFU\_PHASE\_APPLY\_SUCCESS](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca),

69

[ 71](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266) [BT\_MESH\_DFU\_PHASE\_APPLY\_FAIL](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266),

72

[ 74](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7) [BT\_MESH\_DFU\_PHASE\_UNKNOWN](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7),

75};

76

77

[ 79](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d)enum [bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d) {

[ 81](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad) [BT\_MESH\_DFU\_SUCCESS](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad),

82

[ 84](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27) [BT\_MESH\_DFU\_ERR\_RESOURCES](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27),

85

[ 89](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047) [BT\_MESH\_DFU\_ERR\_WRONG\_PHASE](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047),

90

[ 92](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806) [BT\_MESH\_DFU\_ERR\_INTERNAL](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806),

93

[ 95](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c) [BT\_MESH\_DFU\_ERR\_FW\_IDX](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c),

96

[ 98](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934) [BT\_MESH\_DFU\_ERR\_METADATA](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934),

99

[ 101](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a) [BT\_MESH\_DFU\_ERR\_TEMPORARILY\_UNAVAILABLE](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a),

102

[ 104](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25) [BT\_MESH\_DFU\_ERR\_BLOB\_XFER\_BUSY](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25),

105};

106

[ 108](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) {

[ 110](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e) [BT\_MESH\_DFU\_EFFECT\_NONE](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e),

111

[ 115](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc) [BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE\_NO\_RPR](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc),

116

[ 121](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8) [BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8),

122

[ 124](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211) [BT\_MESH\_DFU\_EFFECT\_UNPROV](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211),

125};

126

[ 128](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6)enum [bt\_mesh\_dfu\_iter](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6) {

[ 130](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be) [BT\_MESH\_DFU\_ITER\_STOP](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be),

131

[ 133](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba) [BT\_MESH\_DFU\_ITER\_CONTINUE](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba),

134};

135

[ 140](structbt__mesh__dfu__img.md)struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) {

[ 142](structbt__mesh__dfu__img.md#aa4d91e47dd4c20939d8ef8ada0b86f83) const void \*[fwid](structbt__mesh__dfu__img.md#aa4d91e47dd4c20939d8ef8ada0b86f83);

143

[ 145](structbt__mesh__dfu__img.md#a97e17c59a0528462d554d6bbe78858da) size\_t [fwid\_len](structbt__mesh__dfu__img.md#a97e17c59a0528462d554d6bbe78858da);

146

[ 148](structbt__mesh__dfu__img.md#a578b2932efb07a3e4eb80043902cc7a0) const char \*[uri](structbt__mesh__dfu__img.md#a578b2932efb07a3e4eb80043902cc7a0);

149};

150

[ 152](structbt__mesh__dfu__slot.md)struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) {

[ 154](structbt__mesh__dfu__slot.md#a3f6258793af506b639dd384562fc4a20) size\_t [size](structbt__mesh__dfu__slot.md#a3f6258793af506b639dd384562fc4a20);

[ 156](structbt__mesh__dfu__slot.md#a47ab534d52e931155dfc7cf4e2444999) size\_t [fwid\_len](structbt__mesh__dfu__slot.md#a47ab534d52e931155dfc7cf4e2444999);

[ 158](structbt__mesh__dfu__slot.md#af3e056bf835365afda82f3ec8342d926) size\_t [metadata\_len](structbt__mesh__dfu__slot.md#af3e056bf835365afda82f3ec8342d926);

[ 160](structbt__mesh__dfu__slot.md#a9ab5db428c7d57803d6bbc5f26f9c7bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fwid](structbt__mesh__dfu__slot.md#a9ab5db428c7d57803d6bbc5f26f9c7bb)[[CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN](group__bt__mesh__dfu.md#gacd0f7b01837809a0a92d27f248a9fdd3)];

[ 162](structbt__mesh__dfu__slot.md#aa554bde6cdffa419ada8ea7410118947) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [metadata](structbt__mesh__dfu__slot.md#aa554bde6cdffa419ada8ea7410118947)[[CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN](group__bt__mesh__dfu.md#ga8f2afd35a2215f51cd08debe6e1c8ae4)];

163};

164

166

167#ifdef \_\_cplusplus

168}

169#endif

170

171#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_H\_\_ \*/

[blob.h](blob_8h.md)

[bt\_mesh\_dfu\_iter](group__bt__mesh__dfu.md#ga82475cb72f2ea8b60e70d6987eca2ff6)

bt\_mesh\_dfu\_iter

Action for DFU iteration callbacks.

**Definition** dfu.h:128

[CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN](group__bt__mesh__dfu.md#ga8f2afd35a2215f51cd08debe6e1c8ae4)

#define CONFIG\_BT\_MESH\_DFU\_METADATA\_MAXLEN

**Definition** dfu.h:30

[bt\_mesh\_dfu\_phase](group__bt__mesh__dfu.md#ga99919dcee1e41bc74bd59e33bec2ded2)

bt\_mesh\_dfu\_phase

DFU transfer phase.

**Definition** dfu.h:42

[bt\_mesh\_dfu\_status](group__bt__mesh__dfu.md#ga9e627a3c15de782faa11ef6c4ec5e05d)

bt\_mesh\_dfu\_status

DFU status.

**Definition** dfu.h:79

[CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN](group__bt__mesh__dfu.md#gacd0f7b01837809a0a92d27f248a9fdd3)

#define CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN

**Definition** dfu.h:26

[bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)

bt\_mesh\_dfu\_effect

Expected effect of a DFU transfer.

**Definition** dfu.h:108

[BT\_MESH\_DFU\_ITER\_CONTINUE](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6a2457890f9b50223f94a6383656c003ba)

@ BT\_MESH\_DFU\_ITER\_CONTINUE

Continue iterating.

**Definition** dfu.h:133

[BT\_MESH\_DFU\_ITER\_STOP](group__bt__mesh__dfu.md#gga82475cb72f2ea8b60e70d6987eca2ff6ad069cc2a4174056bb1b09e1cdae967be)

@ BT\_MESH\_DFU\_ITER\_STOP

Stop iterating.

**Definition** dfu.h:130

[BT\_MESH\_DFU\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a36ff3279f4e7683310015b80710e11ad)

@ BT\_MESH\_DFU\_PHASE\_TRANSFER\_ACTIVE

The Receive Firmware procedure is being executed.

**Definition** dfu.h:50

[BT\_MESH\_DFU\_PHASE\_UNKNOWN](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a7be52104081ed2b8880aa4175351d4b7)

@ BT\_MESH\_DFU\_PHASE\_UNKNOWN

Phase of a node was not yet retrieved.

**Definition** dfu.h:74

[BT\_MESH\_DFU\_PHASE\_VERIFY](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a98de12815a145378849c71d4a4c3bc65)

@ BT\_MESH\_DFU\_PHASE\_VERIFY

The Verify Firmware procedure is being executed.

**Definition** dfu.h:53

[BT\_MESH\_DFU\_PHASE\_IDLE](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2a9de660580a58dea6ba6e97ea0d371156)

@ BT\_MESH\_DFU\_PHASE\_IDLE

Ready to start a Receive Firmware procedure.

**Definition** dfu.h:44

[BT\_MESH\_DFU\_PHASE\_TRANSFER\_ERR](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab0e56b13787d57d1db20c04f197b0771)

@ BT\_MESH\_DFU\_PHASE\_TRANSFER\_ERR

The Transfer BLOB procedure failed.

**Definition** dfu.h:47

[BT\_MESH\_DFU\_PHASE\_APPLY\_FAIL](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab36713294a0e68d8b1615374d2a65266)

@ BT\_MESH\_DFU\_PHASE\_APPLY\_FAIL

Firmware applying failed.

**Definition** dfu.h:71

[BT\_MESH\_DFU\_PHASE\_APPLY\_SUCCESS](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ab51ff97ee07154b6e94f7886bf99ffca)

@ BT\_MESH\_DFU\_PHASE\_APPLY\_SUCCESS

Firmware applying succeeded.

**Definition** dfu.h:68

[BT\_MESH\_DFU\_PHASE\_VERIFY\_OK](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2abf0e855c2393a272887df9f45e9475e8)

@ BT\_MESH\_DFU\_PHASE\_VERIFY\_OK

The Verify Firmware procedure completed successfully.

**Definition** dfu.h:56

[BT\_MESH\_DFU\_PHASE\_APPLYING](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ad8fdc7da5216a666999a5918f4632c7f)

@ BT\_MESH\_DFU\_PHASE\_APPLYING

The Apply New Firmware procedure is being executed.

**Definition** dfu.h:62

[BT\_MESH\_DFU\_PHASE\_VERIFY\_FAIL](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2ade806d4326588400748caef1a0bb587e)

@ BT\_MESH\_DFU\_PHASE\_VERIFY\_FAIL

The Verify Firmware procedure failed.

**Definition** dfu.h:59

[BT\_MESH\_DFU\_PHASE\_TRANSFER\_CANCELED](group__bt__mesh__dfu.md#gga99919dcee1e41bc74bd59e33bec2ded2af9515160965c55602e623498e01bbc51)

@ BT\_MESH\_DFU\_PHASE\_TRANSFER\_CANCELED

Firmware transfer has been canceled.

**Definition** dfu.h:65

[BT\_MESH\_DFU\_ERR\_WRONG\_PHASE](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da1f23483a915866abeeefddb0ff126047)

@ BT\_MESH\_DFU\_ERR\_WRONG\_PHASE

The operation cannot be performed while the Server is in the current phase.

**Definition** dfu.h:89

[BT\_MESH\_DFU\_ERR\_FW\_IDX](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da2eb1e712cc20311cc303eeed7d94701c)

@ BT\_MESH\_DFU\_ERR\_FW\_IDX

The message contains a firmware index value that is not expected.

**Definition** dfu.h:95

[BT\_MESH\_DFU\_ERR\_INTERNAL](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da3e95581f4bd3981b86c037df8e38f806)

@ BT\_MESH\_DFU\_ERR\_INTERNAL

An internal error occurred on the node.

**Definition** dfu.h:92

[BT\_MESH\_DFU\_ERR\_TEMPORARILY\_UNAVAILABLE](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da4b5aeee1bfc7e4d855205c7d623ad33a)

@ BT\_MESH\_DFU\_ERR\_TEMPORARILY\_UNAVAILABLE

The Server cannot start a firmware update.

**Definition** dfu.h:101

[BT\_MESH\_DFU\_ERR\_METADATA](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da59c78171ab24cffdd2453dff1f377934)

@ BT\_MESH\_DFU\_ERR\_METADATA

The metadata check failed.

**Definition** dfu.h:98

[BT\_MESH\_DFU\_ERR\_RESOURCES](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da8021a64fb42385544cb8f8ef7b2bca27)

@ BT\_MESH\_DFU\_ERR\_RESOURCES

Insufficient resources on the node.

**Definition** dfu.h:84

[BT\_MESH\_DFU\_ERR\_BLOB\_XFER\_BUSY](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da8e1990cba0513aa0ad0a95625e949e25)

@ BT\_MESH\_DFU\_ERR\_BLOB\_XFER\_BUSY

Another BLOB transfer is in progress.

**Definition** dfu.h:104

[BT\_MESH\_DFU\_SUCCESS](group__bt__mesh__dfu.md#gga9e627a3c15de782faa11ef6c4ec5e05da9829bf8e37e6eeec483752ebb73325ad)

@ BT\_MESH\_DFU\_SUCCESS

The message was processed successfully.

**Definition** dfu.h:81

[BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a049447eb32bcc0b1b18d5ae908de30b8)

@ BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE

Node Composition Data changed, and remote provisioning is supported.

**Definition** dfu.h:121

[BT\_MESH\_DFU\_EFFECT\_UNPROV](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211)

@ BT\_MESH\_DFU\_EFFECT\_UNPROV

Node will be unprovisioned after the update.

**Definition** dfu.h:124

[BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE\_NO\_RPR](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a399d11f493d538d6d11a6aee927015dc)

@ BT\_MESH\_DFU\_EFFECT\_COMP\_CHANGE\_NO\_RPR

Node Composition Data changed and the node does not support remote provisioning.

**Definition** dfu.h:115

[BT\_MESH\_DFU\_EFFECT\_NONE](group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8af8fba9033b663ce141c099b48128b22e)

@ BT\_MESH\_DFU\_EFFECT\_NONE

No changes to node Composition Data.

**Definition** dfu.h:110

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md)

DFU image instance.

**Definition** dfu.h:140

[bt\_mesh\_dfu\_img::uri](structbt__mesh__dfu__img.md#a578b2932efb07a3e4eb80043902cc7a0)

const char \* uri

Update URI, or NULL.

**Definition** dfu.h:148

[bt\_mesh\_dfu\_img::fwid\_len](structbt__mesh__dfu__img.md#a97e17c59a0528462d554d6bbe78858da)

size\_t fwid\_len

Length of the firmware ID.

**Definition** dfu.h:145

[bt\_mesh\_dfu\_img::fwid](structbt__mesh__dfu__img.md#aa4d91e47dd4c20939d8ef8ada0b86f83)

const void \* fwid

Firmware ID.

**Definition** dfu.h:142

[bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md)

DFU image slot for DFU distribution.

**Definition** dfu.h:152

[bt\_mesh\_dfu\_slot::size](structbt__mesh__dfu__slot.md#a3f6258793af506b639dd384562fc4a20)

size\_t size

Size of the firmware in bytes.

**Definition** dfu.h:154

[bt\_mesh\_dfu\_slot::fwid\_len](structbt__mesh__dfu__slot.md#a47ab534d52e931155dfc7cf4e2444999)

size\_t fwid\_len

Length of the firmware ID.

**Definition** dfu.h:156

[bt\_mesh\_dfu\_slot::fwid](structbt__mesh__dfu__slot.md#a9ab5db428c7d57803d6bbc5f26f9c7bb)

uint8\_t fwid[0]

Firmware ID.

**Definition** dfu.h:160

[bt\_mesh\_dfu\_slot::metadata](structbt__mesh__dfu__slot.md#aa554bde6cdffa419ada8ea7410118947)

uint8\_t metadata[0]

Metadata.

**Definition** dfu.h:162

[bt\_mesh\_dfu\_slot::metadata\_len](structbt__mesh__dfu__slot.md#af3e056bf835365afda82f3ec8342d926)

size\_t metadata\_len

Length of the metadata.

**Definition** dfu.h:158

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfu.h](dfu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
