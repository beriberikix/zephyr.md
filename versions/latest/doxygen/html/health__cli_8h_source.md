---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/health__cli_8h_source.html
original_path: doxygen/html/health__cli_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

health\_cli.h

[Go to the documentation of this file.](health__cli_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_CLI\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_CLI\_H\_

12

13#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

14

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 27](structbt__mesh__health__cli.md)struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) {

[ 29](structbt__mesh__health__cli.md#ae472c161f7da7c1cb646102ca78f262b) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__health__cli.md#ae472c161f7da7c1cb646102ca78f262b);

30

[ 32](structbt__mesh__health__cli.md#ae33ffa14689438b39166f4d90386f329) struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) [pub](structbt__mesh__health__cli.md#ae33ffa14689438b39166f4d90386f329);

33

[ 35](structbt__mesh__health__cli.md#a9ae3415b328b25c6206dacdad874c2aa) struct [net\_buf\_simple](structnet__buf__simple.md) [pub\_buf](structbt__mesh__health__cli.md#a9ae3415b328b25c6206dacdad874c2aa);

36

[ 38](structbt__mesh__health__cli.md#a103d110c6cccd69a9e48619668fc60bc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pub\_data](structbt__mesh__health__cli.md#a103d110c6cccd69a9e48619668fc60bc)[[BT\_MESH\_MODEL\_BUF\_LEN](group__bt__mesh__msg.md#ga5352d6fa05808722eba8a76e2446eddb)([BT\_MESH\_MODEL\_OP\_2](group__bt__mesh__access.md#gaa52a40ef5972c4f34cf5ff5a10e21289)(0x80, 0x32), 3)];

39

[ 49](structbt__mesh__health__cli.md#a395f525d846ef029bf5ff9fdde6e7c61) void (\*[period\_status](structbt__mesh__health__cli.md#a395f525d846ef029bf5ff9fdde6e7c61))(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

50 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor);

51

[ 61](structbt__mesh__health__cli.md#ae8d023ac56beb39c0d73a3b9e75f6c96) void (\*[attention\_status](structbt__mesh__health__cli.md#ae8d023ac56beb39c0d73a3b9e75f6c96))(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

62 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention);

63

[ 79](structbt__mesh__health__cli.md#a4cbf24a2407df9bb80e19c1da1558294) void (\*[fault\_status](structbt__mesh__health__cli.md#a4cbf24a2407df9bb80e19c1da1558294))(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

80 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults,

81 size\_t fault\_count);

82

[ 98](structbt__mesh__health__cli.md#a6246d36f8110f401f55003661ab15c86) void (\*[current\_status](structbt__mesh__health__cli.md#a6246d36f8110f401f55003661ab15c86))(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

99 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults,

100 size\_t fault\_count);

101

102 /\* Internal parameters for tracking message responses. \*/

[ 103](structbt__mesh__health__cli.md#ac2ef6ae4fd8e14ad854a9f2c5c80fc43) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [ack\_ctx](structbt__mesh__health__cli.md#ac2ef6ae4fd8e14ad854a9f2c5c80fc43);

104};

105

[ 111](group__bt__mesh__health__cli.md#ga0f869fc7d19f5e8be5953a8ece6e07f6)#define BT\_MESH\_MODEL\_HEALTH\_CLI(cli\_data) \

112 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_HEALTH\_CLI, bt\_mesh\_health\_cli\_op, \

113 &(cli\_data)->pub, cli\_data, &bt\_mesh\_health\_cli\_cb)

114

[ 137](group__bt__mesh__health__cli.md#ga2951f45aaaee75f4c77c4381b1ddd617)int [bt\_mesh\_health\_cli\_fault\_get](group__bt__mesh__health__cli.md#ga2951f45aaaee75f4c77c4381b1ddd617)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

138 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults,

139 size\_t \*fault\_count);

140

[ 163](group__bt__mesh__health__cli.md#ga77cc4e97193cca60d79a8076f3761ef5)int [bt\_mesh\_health\_cli\_fault\_clear](group__bt__mesh__health__cli.md#ga77cc4e97193cca60d79a8076f3761ef5)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

164 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults,

165 size\_t \*fault\_count);

166

[ 178](group__bt__mesh__health__cli.md#gafb0a46136f82f1aff4273704f1c47ac4)int [bt\_mesh\_health\_cli\_fault\_clear\_unack](group__bt__mesh__health__cli.md#gafb0a46136f82f1aff4273704f1c47ac4)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli,

179 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid);

180

[ 200](group__bt__mesh__health__cli.md#ga00cef275cdf90876f1381ffaff04b25c)int [bt\_mesh\_health\_cli\_fault\_test](group__bt__mesh__health__cli.md#ga00cef275cdf90876f1381ffaff04b25c)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

201 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults,

202 size\_t \*fault\_count);

203

[ 214](group__bt__mesh__health__cli.md#ga8e58519ef78946e88258b335c350d754)int [bt\_mesh\_health\_cli\_fault\_test\_unack](group__bt__mesh__health__cli.md#ga8e58519ef78946e88258b335c350d754)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

215 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id);

216

[ 241](group__bt__mesh__health__cli.md#ga1e8e25681b9fcbc6584a29336924a78a)int [bt\_mesh\_health\_cli\_period\_get](group__bt__mesh__health__cli.md#ga1e8e25681b9fcbc6584a29336924a78a)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

242 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*divisor);

243

[ 269](group__bt__mesh__health__cli.md#ga2ef46f0b5059a959d5b06d6e49c4f552)int [bt\_mesh\_health\_cli\_period\_set](group__bt__mesh__health__cli.md#ga2ef46f0b5059a959d5b06d6e49c4f552)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

270 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*updated\_divisor);

271

[ 283](group__bt__mesh__health__cli.md#ga536c631d87daaca017af078d49094fc1)int [bt\_mesh\_health\_cli\_period\_set\_unack](group__bt__mesh__health__cli.md#ga536c631d87daaca017af078d49094fc1)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

284 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) divisor);

285

[ 302](group__bt__mesh__health__cli.md#gad6f322f506b8577c56bb0613f7dcbd93)int [bt\_mesh\_health\_cli\_attention\_get](group__bt__mesh__health__cli.md#gad6f322f506b8577c56bb0613f7dcbd93)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

303 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*attention);

304

[ 323](group__bt__mesh__health__cli.md#ga1b910d0849ce4c33d6de4bf1ff47ece8)int [bt\_mesh\_health\_cli\_attention\_set](group__bt__mesh__health__cli.md#ga1b910d0849ce4c33d6de4bf1ff47ece8)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

324 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*updated\_attention);

325

[ 335](group__bt__mesh__health__cli.md#ga3a528688e340edf49b4bd62317284834)int [bt\_mesh\_health\_cli\_attention\_set\_unack](group__bt__mesh__health__cli.md#ga3a528688e340edf49b4bd62317284834)(struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) \*cli,

336 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention);

337

[ 342](group__bt__mesh__health__cli.md#ga9abc0db22da327d02d23371bba59b46a)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [bt\_mesh\_health\_cli\_timeout\_get](group__bt__mesh__health__cli.md#ga9abc0db22da327d02d23371bba59b46a)(void);

343

[ 348](group__bt__mesh__health__cli.md#gaf3d54597a74a458df0053bd0599d39e9)void [bt\_mesh\_health\_cli\_timeout\_set](group__bt__mesh__health__cli.md#gaf3d54597a74a458df0053bd0599d39e9)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

349

351extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) bt\_mesh\_health\_cli\_op[];

352extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) bt\_mesh\_health\_cli\_cb;

354

355#ifdef \_\_cplusplus

356}

357#endif

358

362

363#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_CLI\_H\_ \*/

[BT\_MESH\_MODEL\_OP\_2](group__bt__mesh__access.md#gaa52a40ef5972c4f34cf5ff5a10e21289)

#define BT\_MESH\_MODEL\_OP\_2(b0, b1)

**Definition** access.h:386

[bt\_mesh\_health\_cli\_fault\_test](group__bt__mesh__health__cli.md#ga00cef275cdf90876f1381ffaff04b25c)

int bt\_mesh\_health\_cli\_fault\_test(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint16\_t cid, uint8\_t test\_id, uint8\_t \*faults, size\_t \*fault\_count)

Invoke a self-test procedure for the given Company ID.

[bt\_mesh\_health\_cli\_attention\_set](group__bt__mesh__health__cli.md#ga1b910d0849ce4c33d6de4bf1ff47ece8)

int bt\_mesh\_health\_cli\_attention\_set(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint8\_t attention, uint8\_t \*updated\_attention)

Set the attention timer.

[bt\_mesh\_health\_cli\_period\_get](group__bt__mesh__health__cli.md#ga1e8e25681b9fcbc6584a29336924a78a)

int bt\_mesh\_health\_cli\_period\_get(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint8\_t \*divisor)

Get the target node's Health fast period divisor.

[bt\_mesh\_health\_cli\_fault\_get](group__bt__mesh__health__cli.md#ga2951f45aaaee75f4c77c4381b1ddd617)

int bt\_mesh\_health\_cli\_fault\_get(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint16\_t cid, uint8\_t \*test\_id, uint8\_t \*faults, size\_t \*fault\_count)

Get the registered fault state for the given Company ID.

[bt\_mesh\_health\_cli\_period\_set](group__bt__mesh__health__cli.md#ga2ef46f0b5059a959d5b06d6e49c4f552)

int bt\_mesh\_health\_cli\_period\_set(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint8\_t divisor, uint8\_t \*updated\_divisor)

Set the target node's Health fast period divisor.

[bt\_mesh\_health\_cli\_attention\_set\_unack](group__bt__mesh__health__cli.md#ga3a528688e340edf49b4bd62317284834)

int bt\_mesh\_health\_cli\_attention\_set\_unack(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint8\_t attention)

Set the attention timer (unacknowledged).

[bt\_mesh\_health\_cli\_period\_set\_unack](group__bt__mesh__health__cli.md#ga536c631d87daaca017af078d49094fc1)

int bt\_mesh\_health\_cli\_period\_set\_unack(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint8\_t divisor)

Set the target node's Health fast period divisor (unacknowledged).

[bt\_mesh\_health\_cli\_fault\_clear](group__bt__mesh__health__cli.md#ga77cc4e97193cca60d79a8076f3761ef5)

int bt\_mesh\_health\_cli\_fault\_clear(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint16\_t cid, uint8\_t \*test\_id, uint8\_t \*faults, size\_t \*fault\_count)

Clear the registered faults for the given Company ID.

[bt\_mesh\_health\_cli\_fault\_test\_unack](group__bt__mesh__health__cli.md#ga8e58519ef78946e88258b335c350d754)

int bt\_mesh\_health\_cli\_fault\_test\_unack(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint16\_t cid, uint8\_t test\_id)

Invoke a self-test procedure for the given Company ID (unacked).

[bt\_mesh\_health\_cli\_timeout\_get](group__bt__mesh__health__cli.md#ga9abc0db22da327d02d23371bba59b46a)

int32\_t bt\_mesh\_health\_cli\_timeout\_get(void)

Get the current transmission timeout value.

[bt\_mesh\_health\_cli\_attention\_get](group__bt__mesh__health__cli.md#gad6f322f506b8577c56bb0613f7dcbd93)

int bt\_mesh\_health\_cli\_attention\_get(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint8\_t \*attention)

Get the current attention timer value.

[bt\_mesh\_health\_cli\_timeout\_set](group__bt__mesh__health__cli.md#gaf3d54597a74a458df0053bd0599d39e9)

void bt\_mesh\_health\_cli\_timeout\_set(int32\_t timeout)

Set the transmission timeout value.

[bt\_mesh\_health\_cli\_fault\_clear\_unack](group__bt__mesh__health__cli.md#gafb0a46136f82f1aff4273704f1c47ac4)

int bt\_mesh\_health\_cli\_fault\_clear\_unack(struct bt\_mesh\_health\_cli \*cli, struct bt\_mesh\_msg\_ctx \*ctx, uint16\_t cid)

Clear the registered faults for the given Company ID (unacked).

[BT\_MESH\_MODEL\_BUF\_LEN](group__bt__mesh__msg.md#ga5352d6fa05808722eba8a76e2446eddb)

#define BT\_MESH\_MODEL\_BUF\_LEN(\_op, \_payload\_len)

Helper for model message buffer length.

**Definition** msg.h:50

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_health\_cli](structbt__mesh__health__cli.md)

Health Client Model Context.

**Definition** health\_cli.h:27

[bt\_mesh\_health\_cli::pub\_data](structbt__mesh__health__cli.md#a103d110c6cccd69a9e48619668fc60bc)

uint8\_t pub\_data[BT\_MESH\_MODEL\_BUF\_LEN(BT\_MESH\_MODEL\_OP\_2(0x80, 0x32), 3)]

Publication data.

**Definition** health\_cli.h:38

[bt\_mesh\_health\_cli::period\_status](structbt__mesh__health__cli.md#a395f525d846ef029bf5ff9fdde6e7c61)

void(\* period\_status)(struct bt\_mesh\_health\_cli \*cli, uint16\_t addr, uint8\_t divisor)

Optional callback for Health Period Status messages.

**Definition** health\_cli.h:49

[bt\_mesh\_health\_cli::fault\_status](structbt__mesh__health__cli.md#a4cbf24a2407df9bb80e19c1da1558294)

void(\* fault\_status)(struct bt\_mesh\_health\_cli \*cli, uint16\_t addr, uint8\_t test\_id, uint16\_t cid, uint8\_t \*faults, size\_t fault\_count)

Optional callback for Health Fault Status messages.

**Definition** health\_cli.h:79

[bt\_mesh\_health\_cli::current\_status](structbt__mesh__health__cli.md#a6246d36f8110f401f55003661ab15c86)

void(\* current\_status)(struct bt\_mesh\_health\_cli \*cli, uint16\_t addr, uint8\_t test\_id, uint16\_t cid, uint8\_t \*faults, size\_t fault\_count)

Optional callback for Health Current Status messages.

**Definition** health\_cli.h:98

[bt\_mesh\_health\_cli::pub\_buf](structbt__mesh__health__cli.md#a9ae3415b328b25c6206dacdad874c2aa)

struct net\_buf\_simple pub\_buf

Publication buffer.

**Definition** health\_cli.h:35

[bt\_mesh\_health\_cli::ack\_ctx](structbt__mesh__health__cli.md#ac2ef6ae4fd8e14ad854a9f2c5c80fc43)

struct bt\_mesh\_msg\_ack\_ctx ack\_ctx

**Definition** health\_cli.h:103

[bt\_mesh\_health\_cli::pub](structbt__mesh__health__cli.md#ae33ffa14689438b39166f4d90386f329)

struct bt\_mesh\_model\_pub pub

Publication structure instance.

**Definition** health\_cli.h:32

[bt\_mesh\_health\_cli::model](structbt__mesh__health__cli.md#ae472c161f7da7c1cb646102ca78f262b)

const struct bt\_mesh\_model \* model

Composition data model entry pointer.

**Definition** health\_cli.h:29

[bt\_mesh\_health\_cli::attention\_status](structbt__mesh__health__cli.md#ae8d023ac56beb39c0d73a3b9e75f6c96)

void(\* attention\_status)(struct bt\_mesh\_health\_cli \*cli, uint16\_t addr, uint8\_t attention)

Optional callback for Health Attention Status messages.

**Definition** health\_cli.h:61

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:803

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model\_pub](structbt__mesh__model__pub.md)

Model publication context.

**Definition** access.h:698

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:881

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

[bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md)

Message sending context.

**Definition** msg.h:76

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [health\_cli.h](health__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
