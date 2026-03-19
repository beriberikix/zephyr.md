---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/brg__cfg__cli_8h_source.html
original_path: doxygen/html/brg__cfg__cli_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

brg\_cfg\_cli.h

[Go to the documentation of this file.](brg__cfg__cli_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_CLI\_H\_\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_CLI\_H\_\_

9

10#include <[zephyr/bluetooth/mesh/brg\_cfg.h](brg__cfg_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

22

23struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md);

24

[ 30](group__bt__mesh__brg__cfg__cli.md#ga4cf994be4732bd99b2c8a4642f670efe)#define BT\_MESH\_MODEL\_BRG\_CFG\_CLI(\_cli) \

31 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_BRG\_CFG\_CLI, \_bt\_mesh\_brg\_cfg\_cli\_op, NULL, \_cli, \

32 &\_bt\_mesh\_brg\_cfg\_cli\_cb)

33

[ 35](structbt__mesh__brg__cfg__cli__cb.md)struct [bt\_mesh\_brg\_cfg\_cli\_cb](structbt__mesh__brg__cfg__cli__cb.md) {

[ 45](structbt__mesh__brg__cfg__cli__cb.md#ac045febf91cc95982985e6de094e403b) void (\*[bridge\_status](structbt__mesh__brg__cfg__cli__cb.md#ac045febf91cc95982985e6de094e403b))(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

46 enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) status);

47

[ 57](structbt__mesh__brg__cfg__cli__cb.md#afe8e0a5ed681630e826ff0aa3889cd88) void (\*[table\_size\_status](structbt__mesh__brg__cfg__cli__cb.md#afe8e0a5ed681630e826ff0aa3889cd88))(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size);

58

[ 68](structbt__mesh__brg__cfg__cli__cb.md#a608b74d78f2f4bb06130f40071ac93af) void (\*[table\_status](structbt__mesh__brg__cfg__cli__cb.md#a608b74d78f2f4bb06130f40071ac93af))(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

69 struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp);

70

[ 80](structbt__mesh__brg__cfg__cli__cb.md#a947e2169ed2cb0964c082bd82c1b0943) void (\*[subnets\_list](structbt__mesh__brg__cfg__cli__cb.md#a947e2169ed2cb0964c082bd82c1b0943))(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

81 struct [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) \*rsp);

82

[ 92](structbt__mesh__brg__cfg__cli__cb.md#a3817e30dd90b161a7442604207ed0ba8) void (\*[table\_list](structbt__mesh__brg__cfg__cli__cb.md#a3817e30dd90b161a7442604207ed0ba8))(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

93 struct [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) \*rsp);

94};

95

[ 97](structbt__mesh__brg__cfg__cli.md)struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) {

[ 99](structbt__mesh__brg__cfg__cli.md#a6cbc5bb1a79c9951b4cd2f16e06d1beb) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__brg__cfg__cli.md#a6cbc5bb1a79c9951b4cd2f16e06d1beb);

100

[ 102](structbt__mesh__brg__cfg__cli.md#a5a7b181b3d026de617085efc0c671474) const struct [bt\_mesh\_brg\_cfg\_cli\_cb](structbt__mesh__brg__cfg__cli__cb.md) \*[cb](structbt__mesh__brg__cfg__cli.md#a5a7b181b3d026de617085efc0c671474);

103

104 /\* Internal parameters for tracking message responses. \*/

[ 105](structbt__mesh__brg__cfg__cli.md#ac0f982fa211bb6660a3159f7e796abb7) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [ack\_ctx](structbt__mesh__brg__cfg__cli.md#ac0f982fa211bb6660a3159f7e796abb7);

106};

107

[ 128](group__bt__mesh__brg__cfg__cli.md#ga6a4507190e425013a9d21ea0a1be1b5c)int [bt\_mesh\_brg\_cfg\_cli\_get](group__bt__mesh__brg__cfg__cli.md#ga6a4507190e425013a9d21ea0a1be1b5c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) \*status);

129

[ 154](group__bt__mesh__brg__cfg__cli.md#ga6643d4d043af4b0cb30470a5c9a46f38)int [bt\_mesh\_brg\_cfg\_cli\_set](group__bt__mesh__brg__cfg__cli.md#ga6643d4d043af4b0cb30470a5c9a46f38)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) val,

155 enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) \*status);

156

[ 176](group__bt__mesh__brg__cfg__cli.md#ga99951987bd6787e3e1348d8e51e64fe5)int [bt\_mesh\_brg\_cfg\_cli\_table\_size\_get](group__bt__mesh__brg__cfg__cli.md#ga99951987bd6787e3e1348d8e51e64fe5)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*size);

177

[ 198](group__bt__mesh__brg__cfg__cli.md#ga8f055e8ee384e8ea4887a56720959b26)int [bt\_mesh\_brg\_cfg\_cli\_table\_add](group__bt__mesh__brg__cfg__cli.md#ga8f055e8ee384e8ea4887a56720959b26)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

199 struct [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) \*entry,

200 struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp);

201

[ 226](group__bt__mesh__brg__cfg__cli.md#gabdb919dcf177b8d5c8a28b057469bf18)int [bt\_mesh\_brg\_cfg\_cli\_table\_remove](group__bt__mesh__brg__cfg__cli.md#gabdb919dcf177b8d5c8a28b057469bf18)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx1,

227 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr2,

228 struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp);

229

[ 256](group__bt__mesh__brg__cfg__cli.md#ga04bb227d14d4f478e4f32a8ca87d2c38)int [bt\_mesh\_brg\_cfg\_cli\_subnets\_get](group__bt__mesh__brg__cfg__cli.md#ga04bb227d14d4f478e4f32a8ca87d2c38)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

257 struct [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) filter\_net\_idx,

258 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_idx, struct [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) \*rsp);

259

[ 290](group__bt__mesh__brg__cfg__cli.md#gacd3811be7b87d2d9187aed6c50945b85)int [bt\_mesh\_brg\_cfg\_cli\_table\_get](group__bt__mesh__brg__cfg__cli.md#gacd3811be7b87d2d9187aed6c50945b85)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx1,

291 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_idx,

292 struct [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) \*rsp);

293

[ 298](group__bt__mesh__brg__cfg__cli.md#ga252994dd3119387703af45c0932ef253)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [bt\_mesh\_brg\_cfg\_cli\_timeout\_get](group__bt__mesh__brg__cfg__cli.md#ga252994dd3119387703af45c0932ef253)(void);

299

[ 304](group__bt__mesh__brg__cfg__cli.md#gad30102a29983545ec79f178b1390ce74)void [bt\_mesh\_brg\_cfg\_cli\_timeout\_set](group__bt__mesh__brg__cfg__cli.md#gad30102a29983545ec79f178b1390ce74)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

305

307extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_brg\_cfg\_cli\_op[];

308extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_brg\_cfg\_cli\_cb;

310

314

315#ifdef \_\_cplusplus

316}

317#endif

318

319#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_CLI\_H\_\_ \*/

[brg\_cfg.h](brg__cfg_8h.md)

[bt\_mesh\_brg\_cfg\_cli\_subnets\_get](group__bt__mesh__brg__cfg__cli.md#ga04bb227d14d4f478e4f32a8ca87d2c38)

int bt\_mesh\_brg\_cfg\_cli\_subnets\_get(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_brg\_cfg\_filter\_netkey filter\_net\_idx, uint8\_t start\_idx, struct bt\_mesh\_brg\_cfg\_subnets\_list \*rsp)

Sends a Bridged Subnets Get message to the given destination address with the given parameters.

[bt\_mesh\_brg\_cfg\_cli\_timeout\_get](group__bt__mesh__brg__cfg__cli.md#ga252994dd3119387703af45c0932ef253)

int32\_t bt\_mesh\_brg\_cfg\_cli\_timeout\_get(void)

Get the current transmission timeout value.

[bt\_mesh\_brg\_cfg\_cli\_set](group__bt__mesh__brg__cfg__cli.md#ga6643d4d043af4b0cb30470a5c9a46f38)

int bt\_mesh\_brg\_cfg\_cli\_set(uint16\_t net\_idx, uint16\_t addr, enum bt\_mesh\_brg\_cfg\_state val, enum bt\_mesh\_brg\_cfg\_state \*status)

Sends a Subnet Bridge Set message to the given destination address with the given parameters.

[bt\_mesh\_brg\_cfg\_cli\_get](group__bt__mesh__brg__cfg__cli.md#ga6a4507190e425013a9d21ea0a1be1b5c)

int bt\_mesh\_brg\_cfg\_cli\_get(uint16\_t net\_idx, uint16\_t addr, enum bt\_mesh\_brg\_cfg\_state \*status)

Sends a Subnet Bridge Get message to the given destination address.

[bt\_mesh\_brg\_cfg\_cli\_table\_add](group__bt__mesh__brg__cfg__cli.md#ga8f055e8ee384e8ea4887a56720959b26)

int bt\_mesh\_brg\_cfg\_cli\_table\_add(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_brg\_cfg\_table\_entry \*entry, struct bt\_mesh\_brg\_cfg\_table\_status \*rsp)

Sends a Bridging Table Add message to the given destination address with the given parameters.

[bt\_mesh\_brg\_cfg\_cli\_table\_size\_get](group__bt__mesh__brg__cfg__cli.md#ga99951987bd6787e3e1348d8e51e64fe5)

int bt\_mesh\_brg\_cfg\_cli\_table\_size\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t \*size)

Sends a Bridging Table Size Get message to the given destination address with the given parameters.

[bt\_mesh\_brg\_cfg\_cli\_table\_remove](group__bt__mesh__brg__cfg__cli.md#gabdb919dcf177b8d5c8a28b057469bf18)

int bt\_mesh\_brg\_cfg\_cli\_table\_remove(uint16\_t net\_idx, uint16\_t addr, uint16\_t net\_idx1, uint16\_t net\_idx2, uint16\_t addr1, uint16\_t addr2, struct bt\_mesh\_brg\_cfg\_table\_status \*rsp)

Sends a Bridging Table Remove message to the given destination address with the given parameters.

[bt\_mesh\_brg\_cfg\_cli\_table\_get](group__bt__mesh__brg__cfg__cli.md#gacd3811be7b87d2d9187aed6c50945b85)

int bt\_mesh\_brg\_cfg\_cli\_table\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t net\_idx1, uint16\_t net\_idx2, uint16\_t start\_idx, struct bt\_mesh\_brg\_cfg\_table\_list \*rsp)

Sends a Bridging Table Get message to the given destination address with the given parameters.

[bt\_mesh\_brg\_cfg\_cli\_timeout\_set](group__bt__mesh__brg__cfg__cli.md#gad30102a29983545ec79f178b1390ce74)

void bt\_mesh\_brg\_cfg\_cli\_timeout\_set(int32\_t timeout)

Set the transmission timeout value.

[bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9)

bt\_mesh\_brg\_cfg\_state

Subnet Bridge states.

**Definition** brg\_cfg.h:24

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_brg\_cfg\_cli\_cb](structbt__mesh__brg__cfg__cli__cb.md)

Mesh Bridge Configuration Client Status messages callback.

**Definition** brg\_cfg\_cli.h:35

[bt\_mesh\_brg\_cfg\_cli\_cb::table\_list](structbt__mesh__brg__cfg__cli__cb.md#a3817e30dd90b161a7442604207ed0ba8)

void(\* table\_list)(struct bt\_mesh\_brg\_cfg\_cli \*cli, uint16\_t addr, struct bt\_mesh\_brg\_cfg\_table\_list \*rsp)

Optional callback for Bridging Table List message.

**Definition** brg\_cfg\_cli.h:92

[bt\_mesh\_brg\_cfg\_cli\_cb::table\_status](structbt__mesh__brg__cfg__cli__cb.md#a608b74d78f2f4bb06130f40071ac93af)

void(\* table\_status)(struct bt\_mesh\_brg\_cfg\_cli \*cli, uint16\_t addr, struct bt\_mesh\_brg\_cfg\_table\_status \*rsp)

Optional callback for Bridging Table Status message.

**Definition** brg\_cfg\_cli.h:68

[bt\_mesh\_brg\_cfg\_cli\_cb::subnets\_list](structbt__mesh__brg__cfg__cli__cb.md#a947e2169ed2cb0964c082bd82c1b0943)

void(\* subnets\_list)(struct bt\_mesh\_brg\_cfg\_cli \*cli, uint16\_t addr, struct bt\_mesh\_brg\_cfg\_subnets\_list \*rsp)

Optional callback for Bridged Subnets List message.

**Definition** brg\_cfg\_cli.h:80

[bt\_mesh\_brg\_cfg\_cli\_cb::bridge\_status](structbt__mesh__brg__cfg__cli__cb.md#ac045febf91cc95982985e6de094e403b)

void(\* bridge\_status)(struct bt\_mesh\_brg\_cfg\_cli \*cli, uint16\_t addr, enum bt\_mesh\_brg\_cfg\_state status)

Optional callback for Subnet Bridge Status message.

**Definition** brg\_cfg\_cli.h:45

[bt\_mesh\_brg\_cfg\_cli\_cb::table\_size\_status](structbt__mesh__brg__cfg__cli__cb.md#afe8e0a5ed681630e826ff0aa3889cd88)

void(\* table\_size\_status)(struct bt\_mesh\_brg\_cfg\_cli \*cli, uint16\_t addr, uint16\_t size)

Optional callback for Bridging Table Size Status message.

**Definition** brg\_cfg\_cli.h:57

[bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md)

Bridge Configuration Client Model Context.

**Definition** brg\_cfg\_cli.h:97

[bt\_mesh\_brg\_cfg\_cli::cb](structbt__mesh__brg__cfg__cli.md#a5a7b181b3d026de617085efc0c671474)

const struct bt\_mesh\_brg\_cfg\_cli\_cb \* cb

Event handler callbacks.

**Definition** brg\_cfg\_cli.h:102

[bt\_mesh\_brg\_cfg\_cli::model](structbt__mesh__brg__cfg__cli.md#a6cbc5bb1a79c9951b4cd2f16e06d1beb)

const struct bt\_mesh\_model \* model

Bridge Configuration model entry pointer.

**Definition** brg\_cfg\_cli.h:99

[bt\_mesh\_brg\_cfg\_cli::ack\_ctx](structbt__mesh__brg__cfg__cli.md#ac0f982fa211bb6660a3159f7e796abb7)

struct bt\_mesh\_msg\_ack\_ctx ack\_ctx

**Definition** brg\_cfg\_cli.h:105

[bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md)

Used to filter set of pairs of NetKey Indexes from the Bridging Table.

**Definition** brg\_cfg.h:59

[bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md)

Bridged Subnets List response.

**Definition** brg\_cfg.h:66

[bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md)

Bridging Table state entry corresponding to a entry in the Bridging Table.

**Definition** brg\_cfg.h:37

[bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md)

Bridging Table List response.

**Definition** brg\_cfg.h:76

[bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md)

Bridging Table Status response.

**Definition** brg\_cfg.h:51

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:891

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [brg\_cfg\_cli.h](brg__cfg__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
