---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/large__comp__data__cli_8h_source.html
original_path: doxygen/html/large__comp__data__cli_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

large\_comp\_data\_cli.h

[Go to the documentation of this file.](large__comp__data__cli_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef BT\_MESH\_LARGE\_COMP\_DATA\_CLI\_H\_\_

8#define BT\_MESH\_LARGE\_COMP\_DATA\_CLI\_H\_\_

9

10#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

22struct [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md);

23

[ 25](structbt__mesh__large__comp__data__rsp.md)struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) {

[ 27](structbt__mesh__large__comp__data__rsp.md#ad3d781276eaf84fd1a8a4d031c005deb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [page](structbt__mesh__large__comp__data__rsp.md#ad3d781276eaf84fd1a8a4d031c005deb);

[ 29](structbt__mesh__large__comp__data__rsp.md#a8bba19b3687a67442e91873c228be361) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset](structbt__mesh__large__comp__data__rsp.md#a8bba19b3687a67442e91873c228be361);

[ 31](structbt__mesh__large__comp__data__rsp.md#aaab8add82c9f24d68af0ddd279164882) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [total\_size](structbt__mesh__large__comp__data__rsp.md#aaab8add82c9f24d68af0ddd279164882);

[ 33](structbt__mesh__large__comp__data__rsp.md#a02d92a210b5b7a26b1df4f5076ed99d8) struct [net\_buf\_simple](structnet__buf__simple.md) \*[data](structbt__mesh__large__comp__data__rsp.md#a02d92a210b5b7a26b1df4f5076ed99d8);

34};

35

[ 37](structbt__mesh__large__comp__data__cli__cb.md)struct [bt\_mesh\_large\_comp\_data\_cli\_cb](structbt__mesh__large__comp__data__cli__cb.md) {

[ 50](structbt__mesh__large__comp__data__cli__cb.md#ab0e17df5eb165a44d70542b8edd36ab9) void (\*[large\_comp\_data\_status](structbt__mesh__large__comp__data__cli__cb.md#ab0e17df5eb165a44d70542b8edd36ab9))(struct [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

51 struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp);

52

[ 65](structbt__mesh__large__comp__data__cli__cb.md#ade54d137534ffb2274e366140f6cbd3c) void (\*[models\_metadata\_status](structbt__mesh__large__comp__data__cli__cb.md#ade54d137534ffb2274e366140f6cbd3c))(struct [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

66 struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp);

67};

68

[ 70](structbt__mesh__large__comp__data__cli.md)struct [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) {

[ 72](structbt__mesh__large__comp__data__cli.md#a4401ff19edfe69c018dd0dbb6f81dc0d) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__large__comp__data__cli.md#a4401ff19edfe69c018dd0dbb6f81dc0d);

73

[ 75](structbt__mesh__large__comp__data__cli.md#afec070cb549d56b3900c4df1e14656ed) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [ack\_ctx](structbt__mesh__large__comp__data__cli.md#afec070cb549d56b3900c4df1e14656ed);

76

[ 78](structbt__mesh__large__comp__data__cli.md#a39d9086c8d9803f939c6103e613699b1) const struct [bt\_mesh\_large\_comp\_data\_cli\_cb](structbt__mesh__large__comp__data__cli__cb.md) \*[cb](structbt__mesh__large__comp__data__cli.md#a39d9086c8d9803f939c6103e613699b1);

79};

80

[ 87](group__bt__mesh__large__comp__data__cli.md#ga5860da397d1cd830e8010946c5b32f1e)#define BT\_MESH\_MODEL\_LARGE\_COMP\_DATA\_CLI(cli\_data) \

88 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI, \

89 \_bt\_mesh\_large\_comp\_data\_cli\_op, NULL, cli\_data, \

90 &\_bt\_mesh\_large\_comp\_data\_cli\_cb)

91

[ 113](group__bt__mesh__large__comp__data__cli.md#gaf505ee14246746fc245a34328443d1c6)int [bt\_mesh\_large\_comp\_data\_get](group__bt__mesh__large__comp__data__cli.md#gaf505ee14246746fc245a34328443d1c6)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page,

114 size\_t offset, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp);

115

[ 137](group__bt__mesh__large__comp__data__cli.md#ga4073eb48c43460804705d80ac0919864)int [bt\_mesh\_models\_metadata\_get](group__bt__mesh__large__comp__data__cli.md#ga4073eb48c43460804705d80ac0919864)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page,

138 size\_t offset, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp);

139

141extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_large\_comp\_data\_cli\_op[];

142extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_large\_comp\_data\_cli\_cb;

144

148

149#ifdef \_\_cplusplus

150}

151#endif

152

153#endif /\* BT\_MESH\_LARGE\_COMP\_DATA\_CLI\_H\_\_ \*/

[bt\_mesh\_models\_metadata\_get](group__bt__mesh__large__comp__data__cli.md#ga4073eb48c43460804705d80ac0919864)

int bt\_mesh\_models\_metadata\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t page, size\_t offset, struct bt\_mesh\_large\_comp\_data\_rsp \*rsp)

Send Models Metadata Get message.

[bt\_mesh\_large\_comp\_data\_get](group__bt__mesh__large__comp__data__cli.md#gaf505ee14246746fc245a34328443d1c6)

int bt\_mesh\_large\_comp\_data\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t page, size\_t offset, struct bt\_mesh\_large\_comp\_data\_rsp \*rsp)

Send Large Composition Data Get message.

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_large\_comp\_data\_cli\_cb](structbt__mesh__large__comp__data__cli__cb.md)

Large Composition Data Status messages callbacks.

**Definition** large\_comp\_data\_cli.h:37

[bt\_mesh\_large\_comp\_data\_cli\_cb::large\_comp\_data\_status](structbt__mesh__large__comp__data__cli__cb.md#ab0e17df5eb165a44d70542b8edd36ab9)

void(\* large\_comp\_data\_status)(struct bt\_mesh\_large\_comp\_data\_cli \*cli, uint16\_t addr, struct bt\_mesh\_large\_comp\_data\_rsp \*rsp)

Optional callback for Large Composition Data Status message.

**Definition** large\_comp\_data\_cli.h:50

[bt\_mesh\_large\_comp\_data\_cli\_cb::models\_metadata\_status](structbt__mesh__large__comp__data__cli__cb.md#ade54d137534ffb2274e366140f6cbd3c)

void(\* models\_metadata\_status)(struct bt\_mesh\_large\_comp\_data\_cli \*cli, uint16\_t addr, struct bt\_mesh\_large\_comp\_data\_rsp \*rsp)

Optional callback for Models Metadata Status message.

**Definition** large\_comp\_data\_cli.h:65

[bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md)

Large Composition Data Client model context.

**Definition** large\_comp\_data\_cli.h:70

[bt\_mesh\_large\_comp\_data\_cli::cb](structbt__mesh__large__comp__data__cli.md#a39d9086c8d9803f939c6103e613699b1)

const struct bt\_mesh\_large\_comp\_data\_cli\_cb \* cb

Optional callback for Large Composition Data Status messages.

**Definition** large\_comp\_data\_cli.h:78

[bt\_mesh\_large\_comp\_data\_cli::model](structbt__mesh__large__comp__data__cli.md#a4401ff19edfe69c018dd0dbb6f81dc0d)

const struct bt\_mesh\_model \* model

Model entry pointer.

**Definition** large\_comp\_data\_cli.h:72

[bt\_mesh\_large\_comp\_data\_cli::ack\_ctx](structbt__mesh__large__comp__data__cli.md#afec070cb549d56b3900c4df1e14656ed)

struct bt\_mesh\_msg\_ack\_ctx ack\_ctx

Internal parameters for tracking message responses.

**Definition** large\_comp\_data\_cli.h:75

[bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md)

Large Composition Data response.

**Definition** large\_comp\_data\_cli.h:25

[bt\_mesh\_large\_comp\_data\_rsp::data](structbt__mesh__large__comp__data__rsp.md#a02d92a210b5b7a26b1df4f5076ed99d8)

struct net\_buf\_simple \* data

Pointer to allocated buffer for storing received data.

**Definition** large\_comp\_data\_cli.h:33

[bt\_mesh\_large\_comp\_data\_rsp::offset](structbt__mesh__large__comp__data__rsp.md#a8bba19b3687a67442e91873c228be361)

uint16\_t offset

Offset within the page.

**Definition** large\_comp\_data\_cli.h:29

[bt\_mesh\_large\_comp\_data\_rsp::total\_size](structbt__mesh__large__comp__data__rsp.md#aaab8add82c9f24d68af0ddd279164882)

uint16\_t total\_size

Total size of the page.

**Definition** large\_comp\_data\_cli.h:31

[bt\_mesh\_large\_comp\_data\_rsp::page](structbt__mesh__large__comp__data__rsp.md#ad3d781276eaf84fd1a8a4d031c005deb)

uint8\_t page

Page number.

**Definition** large\_comp\_data\_cli.h:27

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

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [large\_comp\_data\_cli.h](large__comp__data__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
