---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/health__srv_8h_source.html
original_path: doxygen/html/health__srv_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

health\_srv.h

[Go to the documentation of this file.](health__srv_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_SRV\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_SRV\_H\_

12

19

20#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

21#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 28](structbt__mesh__health__srv__cb.md)struct [bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md) {

[ 56](structbt__mesh__health__srv__cb.md#a03ff8869793804dd5943f5d2cd63cc3e) int (\*[fault\_get\_cur](structbt__mesh__health__srv__cb.md#a03ff8869793804dd5943f5d2cd63cc3e))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id,

57 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*company\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults,

58 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*fault\_count);

59

[ 82](structbt__mesh__health__srv__cb.md#a555711f2892d8e5a96661c6fff03c7f8) int (\*[fault\_get\_reg](structbt__mesh__health__srv__cb.md#a555711f2892d8e5a96661c6fff03c7f8))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id,

83 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*test\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*faults,

84 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*fault\_count);

85

[ 94](structbt__mesh__health__srv__cb.md#afdc878362b78ccfeb4473bcdfb02b9d1) int (\*[fault\_clear](structbt__mesh__health__srv__cb.md#afdc878362b78ccfeb4473bcdfb02b9d1))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id);

95

[ 111](structbt__mesh__health__srv__cb.md#ab426938525f8478ab27dc08a2f25273f) int (\*[fault\_test](structbt__mesh__health__srv__cb.md#ab426938525f8478ab27dc08a2f25273f))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) test\_id,

112 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company\_id);

113

[ 128](structbt__mesh__health__srv__cb.md#ad9e8a392943d4848190c4513327bc52c) void (\*[attn\_on](structbt__mesh__health__srv__cb.md#ad9e8a392943d4848190c4513327bc52c))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model);

129

[ 137](structbt__mesh__health__srv__cb.md#abd881db6cf849433808bc6464e109b60) void (\*[attn\_off](structbt__mesh__health__srv__cb.md#abd881db6cf849433808bc6464e109b60))(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model);

138};

139

[ 146](group__bt__mesh__health__srv.md#ga35c500e915092ec365862b11e76f92ad)#define BT\_MESH\_HEALTH\_PUB\_DEFINE(\_name, \_max\_faults) \

147 BT\_MESH\_MODEL\_PUB\_DEFINE(\_name, NULL, (1 + 3 + (\_max\_faults)))

148

[ 150](structbt__mesh__health__srv.md)struct [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md) {

[ 152](structbt__mesh__health__srv.md#aff95fc381ea8048d4d76668b92126dc6) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__health__srv.md#aff95fc381ea8048d4d76668b92126dc6);

153

[ 155](structbt__mesh__health__srv.md#a4d316010b2737eca7bad3aef6774d52b) const struct [bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md) \*[cb](structbt__mesh__health__srv.md#a4d316010b2737eca7bad3aef6774d52b);

156

[ 158](structbt__mesh__health__srv.md#a8df7f6c7e434cb717b9b51a3167b5e86) struct [k\_work\_delayable](structk__work__delayable.md) [attn\_timer](structbt__mesh__health__srv.md#a8df7f6c7e434cb717b9b51a3167b5e86);

159};

160

[ 175](group__bt__mesh__health__srv.md#gafcab7a9c9264c52f42b5409ccad1c931)#define BT\_MESH\_MODEL\_HEALTH\_SRV(srv, pub, ...) \

176 BT\_MESH\_MODEL\_METADATA\_CB(BT\_MESH\_MODEL\_ID\_HEALTH\_SRV, \

177 bt\_mesh\_health\_srv\_op, \

178 pub, \

179 srv, \

180 &bt\_mesh\_health\_srv\_cb, \_\_VA\_ARGS\_\_)

181

[ 186](group__bt__mesh__health__srv.md#ga240e4632cdf7c425d4beec3c6a290306)#define BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID 0x0000

187

[ 188](group__bt__mesh__health__srv.md#ga37a52318699187a92de82d45dccf325d)#define BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA(tests) \

189 { \

190 .len = ARRAY\_SIZE(tests), \

191 .id = BT\_MESH\_HEALTH\_TEST\_INFO\_METADATA\_ID, \

192 .data = tests, \

193 }

194

[ 204](group__bt__mesh__health__srv.md#ga29ca643e811a2c4f03eca7fed8d1cf4d)#define BT\_MESH\_HEALTH\_TEST\_INFO(cid, tests...) \

205 BT\_BYTES\_LIST\_LE16(cid), sizeof((uint8\_t[]){ tests }), tests

206

[ 217](group__bt__mesh__health__srv.md#gad04789eb167b61d5ff19827c560ceb6e)int [bt\_mesh\_health\_srv\_fault\_update](group__bt__mesh__health__srv.md#gad04789eb167b61d5ff19827c560ceb6e)(const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem);

218

220extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) bt\_mesh\_health\_srv\_op[];

221extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) [bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md);

223

224#ifdef \_\_cplusplus

225}

226#endif

227

231

232#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_SRV\_H\_ \*/

[byteorder.h](bluetooth_2byteorder_8h.md)

Bluetooth byteorder API.

[bt\_mesh\_health\_srv\_fault\_update](group__bt__mesh__health__srv.md#gad04789eb167b61d5ff19827c560ceb6e)

int bt\_mesh\_health\_srv\_fault\_update(const struct bt\_mesh\_elem \*elem)

Notify the stack that the fault array state of the given element has changed.

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_elem](structbt__mesh__elem.md)

Abstraction that describes a Mesh Element.

**Definition** access.h:154

[bt\_mesh\_health\_srv\_cb](structbt__mesh__health__srv__cb.md)

Callback function for the Health Server model.

**Definition** health\_srv.h:28

[bt\_mesh\_health\_srv\_cb::fault\_get\_cur](structbt__mesh__health__srv__cb.md#a03ff8869793804dd5943f5d2cd63cc3e)

int(\* fault\_get\_cur)(const struct bt\_mesh\_model \*model, uint8\_t \*test\_id, uint16\_t \*company\_id, uint8\_t \*faults, uint8\_t \*fault\_count)

Callback for fetching current faults.

**Definition** health\_srv.h:56

[bt\_mesh\_health\_srv\_cb::fault\_get\_reg](structbt__mesh__health__srv__cb.md#a555711f2892d8e5a96661c6fff03c7f8)

int(\* fault\_get\_reg)(const struct bt\_mesh\_model \*model, uint16\_t company\_id, uint8\_t \*test\_id, uint8\_t \*faults, uint8\_t \*fault\_count)

Callback for fetching all registered faults.

**Definition** health\_srv.h:82

[bt\_mesh\_health\_srv\_cb::fault\_test](structbt__mesh__health__srv__cb.md#ab426938525f8478ab27dc08a2f25273f)

int(\* fault\_test)(const struct bt\_mesh\_model \*model, uint8\_t test\_id, uint16\_t company\_id)

Run a self-test.

**Definition** health\_srv.h:111

[bt\_mesh\_health\_srv\_cb::attn\_off](structbt__mesh__health__srv__cb.md#abd881db6cf849433808bc6464e109b60)

void(\* attn\_off)(const struct bt\_mesh\_model \*model)

Stop the attention state.

**Definition** health\_srv.h:137

[bt\_mesh\_health\_srv\_cb::attn\_on](structbt__mesh__health__srv__cb.md#ad9e8a392943d4848190c4513327bc52c)

void(\* attn\_on)(const struct bt\_mesh\_model \*model)

Start calling attention to the device.

**Definition** health\_srv.h:128

[bt\_mesh\_health\_srv\_cb::fault\_clear](structbt__mesh__health__srv__cb.md#afdc878362b78ccfeb4473bcdfb02b9d1)

int(\* fault\_clear)(const struct bt\_mesh\_model \*model, uint16\_t company\_id)

Clear all registered faults associated with the given Company ID.

**Definition** health\_srv.h:94

[bt\_mesh\_health\_srv](structbt__mesh__health__srv.md)

Mesh Health Server Model Context.

**Definition** health\_srv.h:150

[bt\_mesh\_health\_srv::cb](structbt__mesh__health__srv.md#a4d316010b2737eca7bad3aef6774d52b)

const struct bt\_mesh\_health\_srv\_cb \* cb

Optional callback struct.

**Definition** health\_srv.h:155

[bt\_mesh\_health\_srv::attn\_timer](structbt__mesh__health__srv.md#a8df7f6c7e434cb717b9b51a3167b5e86)

struct k\_work\_delayable attn\_timer

Attention Timer state.

**Definition** health\_srv.h:158

[bt\_mesh\_health\_srv::model](structbt__mesh__health__srv.md#aff95fc381ea8048d4d76668b92126dc6)

const struct bt\_mesh\_model \* model

Composition data model entry pointer.

**Definition** health\_srv.h:152

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:891

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4034

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [health\_srv.h](health__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
