---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pacs_8h_source.html
original_path: doxygen/html/pacs_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pacs.h

[Go to the documentation of this file.](pacs_8h.md)

1

5

6/\* Copyright (c) 2021 Intel Corporation

7 \* Copyright (c) 2021-2024 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PACS\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PACS\_H\_

14

28

29#include <[stdbool.h](stdbool_8h.md)>

30

31#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

32#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

33#include <[zephyr/sys/slist.h](slist_8h.md)>

34

35#ifdef \_\_cplusplus

36extern "C" {

37#endif

38

[ 40](structbt__pacs__cap.md)struct [bt\_pacs\_cap](structbt__pacs__cap.md) {

[ 42](structbt__pacs__cap.md#a2f311677a17aacec91f1ab7e1a7c787f) const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*[codec\_cap](structbt__pacs__cap.md#a2f311677a17aacec91f1ab7e1a7c787f);

43

45 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

46};

47

[ 58](group__bt__pacs.md#ga452591f80b6be5d79609b25ade2154a9)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[bt\_pacs\_cap\_foreach\_func\_t](group__bt__pacs.md#ga452591f80b6be5d79609b25ade2154a9))(const struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap,

59 void \*user\_data);

60

[ 70](group__bt__pacs.md#ga31e2c7e9a4b5b6a291b96832c1218a49)void [bt\_pacs\_cap\_foreach](group__bt__pacs.md#ga31e2c7e9a4b5b6a291b96832c1218a49)(enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

71 [bt\_pacs\_cap\_foreach\_func\_t](group__bt__pacs.md#ga452591f80b6be5d79609b25ade2154a9) func,

72 void \*user\_data);

73

[ 84](group__bt__pacs.md#ga251b36d4f5775eea1f69873709f847cc)int [bt\_pacs\_cap\_register](group__bt__pacs.md#ga251b36d4f5775eea1f69873709f847cc)(enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap);

85

[ 96](group__bt__pacs.md#ga4f6015eba63ffc7a9377afe54a290da1)int [bt\_pacs\_cap\_unregister](group__bt__pacs.md#ga4f6015eba63ffc7a9377afe54a290da1)(enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap);

97

[ 106](group__bt__pacs.md#gaff290fd59bb05012abcf405dbdc72884)int [bt\_pacs\_set\_location](group__bt__pacs.md#gaff290fd59bb05012abcf405dbdc72884)(enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

107 enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) location);

108

[ 117](group__bt__pacs.md#ga29a1ec26c1e5e82e02eac39e1088332c)int [bt\_pacs\_set\_available\_contexts](group__bt__pacs.md#ga29a1ec26c1e5e82e02eac39e1088332c)(enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

118 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts);

119

[ 127](group__bt__pacs.md#ga437d824d0a944b6c30db492dbe28514f)enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) [bt\_pacs\_get\_available\_contexts](group__bt__pacs.md#ga437d824d0a944b6c30db492dbe28514f)(enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir);

128

[ 144](group__bt__pacs.md#ga12f283d2daf72302a01cefb4a4a8fc70)int [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](group__bt__pacs.md#ga12f283d2daf72302a01cefb4a4a8fc70)(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

145 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) \*contexts);

146

[ 160](group__bt__pacs.md#ga7b28aa42525344445b20bb90a19441aa)enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) [bt\_pacs\_get\_available\_contexts\_for\_conn](group__bt__pacs.md#ga7b28aa42525344445b20bb90a19441aa)(struct bt\_conn \*conn,

161 enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir);

162

[ 171](group__bt__pacs.md#gabae9cf025f32ce80b660ebd7f95241b2)int [bt\_pacs\_set\_supported\_contexts](group__bt__pacs.md#gabae9cf025f32ce80b660ebd7f95241b2)(enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir,

172 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts);

173

174#ifdef \_\_cplusplus

175}

176#endif

177

179

180#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PACS\_H\_ \*/

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)

bt\_audio\_dir

Audio direction from the perspective of the BAP Unicast Server / BAP Broadcast Sink.

**Definition** audio.h:796

[bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)

bt\_audio\_location

Location values for BT Audio.

**Definition** audio.h:590

[bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)

bt\_audio\_context

Audio Context Type for Generic Audio.

**Definition** audio.h:303

[bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](group__bt__pacs.md#ga12f283d2daf72302a01cefb4a4a8fc70)

int bt\_pacs\_conn\_set\_available\_contexts\_for\_conn(struct bt\_conn \*conn, enum bt\_audio\_dir dir, enum bt\_audio\_context \*contexts)

Set the available contexts for a given connection.

[bt\_pacs\_cap\_register](group__bt__pacs.md#ga251b36d4f5775eea1f69873709f847cc)

int bt\_pacs\_cap\_register(enum bt\_audio\_dir dir, struct bt\_pacs\_cap \*cap)

Register Published Audio Capability.

[bt\_pacs\_set\_available\_contexts](group__bt__pacs.md#ga29a1ec26c1e5e82e02eac39e1088332c)

int bt\_pacs\_set\_available\_contexts(enum bt\_audio\_dir dir, enum bt\_audio\_context contexts)

Set the available contexts for an endpoint type.

[bt\_pacs\_cap\_foreach](group__bt__pacs.md#ga31e2c7e9a4b5b6a291b96832c1218a49)

void bt\_pacs\_cap\_foreach(enum bt\_audio\_dir dir, bt\_pacs\_cap\_foreach\_func\_t func, void \*user\_data)

Published Audio Capability iterator.

[bt\_pacs\_get\_available\_contexts](group__bt__pacs.md#ga437d824d0a944b6c30db492dbe28514f)

enum bt\_audio\_context bt\_pacs\_get\_available\_contexts(enum bt\_audio\_dir dir)

Get the available contexts for an endpoint type.

[bt\_pacs\_cap\_foreach\_func\_t](group__bt__pacs.md#ga452591f80b6be5d79609b25ade2154a9)

bool(\* bt\_pacs\_cap\_foreach\_func\_t)(const struct bt\_pacs\_cap \*cap, void \*user\_data)

Published Audio Capability iterator callback.

**Definition** pacs.h:58

[bt\_pacs\_cap\_unregister](group__bt__pacs.md#ga4f6015eba63ffc7a9377afe54a290da1)

int bt\_pacs\_cap\_unregister(enum bt\_audio\_dir dir, struct bt\_pacs\_cap \*cap)

Unregister Published Audio Capability.

[bt\_pacs\_get\_available\_contexts\_for\_conn](group__bt__pacs.md#ga7b28aa42525344445b20bb90a19441aa)

enum bt\_audio\_context bt\_pacs\_get\_available\_contexts\_for\_conn(struct bt\_conn \*conn, enum bt\_audio\_dir dir)

Get the available contexts for a given connection.

[bt\_pacs\_set\_supported\_contexts](group__bt__pacs.md#gabae9cf025f32ce80b660ebd7f95241b2)

int bt\_pacs\_set\_supported\_contexts(enum bt\_audio\_dir dir, enum bt\_audio\_context contexts)

Set the supported contexts for an endpoint type.

[bt\_pacs\_set\_location](group__bt__pacs.md#gaff290fd59bb05012abcf405dbdc72884)

int bt\_pacs\_set\_location(enum bt\_audio\_dir dir, enum bt\_audio\_location location)

Set the location for an endpoint type.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[bt\_audio\_codec\_cap](structbt__audio__codec__cap.md)

Codec capability structure.

**Definition** audio.h:684

[bt\_pacs\_cap](structbt__pacs__cap.md)

Published Audio Capability structure.

**Definition** pacs.h:40

[bt\_pacs\_cap::codec\_cap](structbt__pacs__cap.md#a2f311677a17aacec91f1ab7e1a7c787f)

const struct bt\_audio\_codec\_cap \* codec\_cap

Codec capability reference.

**Definition** pacs.h:42

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [pacs.h](pacs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
