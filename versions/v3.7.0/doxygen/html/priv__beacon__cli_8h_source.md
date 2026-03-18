---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/priv__beacon__cli_8h_source.html
original_path: doxygen/html/priv__beacon__cli_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

priv\_beacon\_cli.h

[Go to the documentation of this file.](priv__beacon__cli_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_PRIV\_BEACON\_CLI\_H\_\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_PRIV\_BEACON\_CLI\_H\_\_

9

10#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 28](group__bt__mesh__priv__beacon__cli.md#ga65008412f2fc89aa9f71c067ad3fe264)#define BT\_MESH\_MODEL\_PRIV\_BEACON\_CLI(cli\_data) \

29 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI, \

30 bt\_mesh\_priv\_beacon\_cli\_op, NULL, cli\_data, \

31 &bt\_mesh\_priv\_beacon\_cli\_cb)

32

33struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md);

34

[ 36](structbt__mesh__priv__beacon.md)struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) {

[ 38](structbt__mesh__priv__beacon.md#ac38424ed4ebcd69307568763ff2d6ffb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [enabled](structbt__mesh__priv__beacon.md#ac38424ed4ebcd69307568763ff2d6ffb);

[ 42](structbt__mesh__priv__beacon.md#a1a4972527afde6f9aa5c7726d85ddd45) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rand\_interval](structbt__mesh__priv__beacon.md#a1a4972527afde6f9aa5c7726d85ddd45);

43};

44

[ 46](structbt__mesh__priv__node__id.md)struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) {

[ 48](structbt__mesh__priv__node__id.md#ab772f79daa361a9199f8445b7bda7e44) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__priv__node__id.md#ab772f79daa361a9199f8445b7bda7e44);

[ 50](structbt__mesh__priv__node__id.md#a5bd318e61b974a94765e0d28db15994f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__mesh__priv__node__id.md#a5bd318e61b974a94765e0d28db15994f);

[ 52](structbt__mesh__priv__node__id.md#a49c60fedb24de61a399f3da967f4ac7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__mesh__priv__node__id.md#a49c60fedb24de61a399f3da967f4ac7c);

53};

54

[ 56](structbt__mesh__priv__beacon__cli__cb.md)struct [bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md) {

[ 65](structbt__mesh__priv__beacon__cli__cb.md#ab4b58af5af27be22dc395df4b2fd35c4) void (\*[priv\_beacon\_status](structbt__mesh__priv__beacon__cli__cb.md#ab4b58af5af27be22dc395df4b2fd35c4))(struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

66 struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*priv\_beacon);

67

[ 76](structbt__mesh__priv__beacon__cli__cb.md#a825bb5dee44075a8b6d14efc5f68c372) void (\*[priv\_gatt\_proxy\_status](structbt__mesh__priv__beacon__cli__cb.md#a825bb5dee44075a8b6d14efc5f68c372))(struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

77 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gatt\_proxy);

78

[ 87](structbt__mesh__priv__beacon__cli__cb.md#aa1206f9a75beb79449e5a1bad8e62f41) void (\*[priv\_node\_id\_status](structbt__mesh__priv__beacon__cli__cb.md#aa1206f9a75beb79449e5a1bad8e62f41))(struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

88 struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*priv\_node\_id);

89};

90

[ 92](structbt__mesh__priv__beacon__cli.md)struct [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md) {

[ 93](structbt__mesh__priv__beacon__cli.md#a506b13407e466908d8a8684386bf3927) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__priv__beacon__cli.md#a506b13407e466908d8a8684386bf3927);

94

95 /\* Internal parameters for tracking message responses. \*/

[ 96](structbt__mesh__priv__beacon__cli.md#aa4105b00e2a3ad9027b888f0ebbea23e) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [ack\_ctx](structbt__mesh__priv__beacon__cli.md#aa4105b00e2a3ad9027b888f0ebbea23e);

97

[ 99](structbt__mesh__priv__beacon__cli.md#ab281b9ac10c54068372f90bccfe07feb) const struct [bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md) \*[cb](structbt__mesh__priv__beacon__cli.md#ab281b9ac10c54068372f90bccfe07feb);

100};

101

[ 115](group__bt__mesh__priv__beacon__cli.md#ga8a535d31954d8871fed557808b6abc71)int [bt\_mesh\_priv\_beacon\_cli\_set](group__bt__mesh__priv__beacon__cli.md#ga8a535d31954d8871fed557808b6abc71)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

116 struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*val,

117 struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*rsp);

118

[ 127](group__bt__mesh__priv__beacon__cli.md#ga76d797a76d8f8fda31feacce840a6f9e)int [bt\_mesh\_priv\_beacon\_cli\_get](group__bt__mesh__priv__beacon__cli.md#ga76d797a76d8f8fda31feacce840a6f9e)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

128 struct [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md) \*val);

129

[ 143](group__bt__mesh__priv__beacon__cli.md#ga389626a517c1bb9cae31501663725483)int [bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_set](group__bt__mesh__priv__beacon__cli.md#ga389626a517c1bb9cae31501663725483)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

144 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp);

145

[ 154](group__bt__mesh__priv__beacon__cli.md#ga838880ae8391b33d0481fba069ea921b)int [bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_get](group__bt__mesh__priv__beacon__cli.md#ga838880ae8391b33d0481fba069ea921b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

155 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val);

156

[ 170](group__bt__mesh__priv__beacon__cli.md#ga2a581e49b8812bd78604fc829bd1d79a)int [bt\_mesh\_priv\_beacon\_cli\_node\_id\_set](group__bt__mesh__priv__beacon__cli.md#ga2a581e49b8812bd78604fc829bd1d79a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

171 struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*val,

172 struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*rsp);

173

[ 183](group__bt__mesh__priv__beacon__cli.md#gadd6fc3321cd536771921566bbc650396)int [bt\_mesh\_priv\_beacon\_cli\_node\_id\_get](group__bt__mesh__priv__beacon__cli.md#gadd6fc3321cd536771921566bbc650396)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

184 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx,

185 struct [bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md) \*val);

186

188extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) bt\_mesh\_priv\_beacon\_cli\_op[];

189extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) [bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md);

191

193

194#ifdef \_\_cplusplus

195}

196#endif

197

198#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_PRIV\_BEACON\_CLI\_H\_\_ \*/

[bt\_mesh\_priv\_beacon\_cli\_node\_id\_set](group__bt__mesh__priv__beacon__cli.md#ga2a581e49b8812bd78604fc829bd1d79a)

int bt\_mesh\_priv\_beacon\_cli\_node\_id\_set(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_priv\_node\_id \*val, struct bt\_mesh\_priv\_node\_id \*rsp)

Set the target's Private Node Identity state.

[bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_set](group__bt__mesh__priv__beacon__cli.md#ga389626a517c1bb9cae31501663725483)

int bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*rsp)

Set the target's Private GATT Proxy state.

[bt\_mesh\_priv\_beacon\_cli\_get](group__bt__mesh__priv__beacon__cli.md#ga76d797a76d8f8fda31feacce840a6f9e)

int bt\_mesh\_priv\_beacon\_cli\_get(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_priv\_beacon \*val)

Get the target's Private Beacon state.

[bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_get](group__bt__mesh__priv__beacon__cli.md#ga838880ae8391b33d0481fba069ea921b)

int bt\_mesh\_priv\_beacon\_cli\_gatt\_proxy\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*val)

Get the target's Private GATT Proxy state.

[bt\_mesh\_priv\_beacon\_cli\_set](group__bt__mesh__priv__beacon__cli.md#ga8a535d31954d8871fed557808b6abc71)

int bt\_mesh\_priv\_beacon\_cli\_set(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_priv\_beacon \*val, struct bt\_mesh\_priv\_beacon \*rsp)

Set the target's Private Beacon state.

[bt\_mesh\_priv\_beacon\_cli\_node\_id\_get](group__bt__mesh__priv__beacon__cli.md#gadd6fc3321cd536771921566bbc650396)

int bt\_mesh\_priv\_beacon\_cli\_node\_id\_get(uint16\_t net\_idx, uint16\_t addr, uint16\_t key\_net\_idx, struct bt\_mesh\_priv\_node\_id \*val)

Get the target's Private Node Identity state.

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:809

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:887

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

[bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md)

Private Beacon Client Status messages callbacks.

**Definition** priv\_beacon\_cli.h:56

[bt\_mesh\_priv\_beacon\_cli\_cb::priv\_gatt\_proxy\_status](structbt__mesh__priv__beacon__cli__cb.md#a825bb5dee44075a8b6d14efc5f68c372)

void(\* priv\_gatt\_proxy\_status)(struct bt\_mesh\_priv\_beacon\_cli \*cli, uint16\_t addr, uint8\_t gatt\_proxy)

Optional callback for Private GATT Proxy Status message.

**Definition** priv\_beacon\_cli.h:76

[bt\_mesh\_priv\_beacon\_cli\_cb::priv\_node\_id\_status](structbt__mesh__priv__beacon__cli__cb.md#aa1206f9a75beb79449e5a1bad8e62f41)

void(\* priv\_node\_id\_status)(struct bt\_mesh\_priv\_beacon\_cli \*cli, uint16\_t addr, struct bt\_mesh\_priv\_node\_id \*priv\_node\_id)

Optional callback for Private Node Identity Status message.

**Definition** priv\_beacon\_cli.h:87

[bt\_mesh\_priv\_beacon\_cli\_cb::priv\_beacon\_status](structbt__mesh__priv__beacon__cli__cb.md#ab4b58af5af27be22dc395df4b2fd35c4)

void(\* priv\_beacon\_status)(struct bt\_mesh\_priv\_beacon\_cli \*cli, uint16\_t addr, struct bt\_mesh\_priv\_beacon \*priv\_beacon)

Optional callback for Private Beacon Status message.

**Definition** priv\_beacon\_cli.h:65

[bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md)

Mesh Private Beacon Client model.

**Definition** priv\_beacon\_cli.h:92

[bt\_mesh\_priv\_beacon\_cli::model](structbt__mesh__priv__beacon__cli.md#a506b13407e466908d8a8684386bf3927)

const struct bt\_mesh\_model \* model

**Definition** priv\_beacon\_cli.h:93

[bt\_mesh\_priv\_beacon\_cli::ack\_ctx](structbt__mesh__priv__beacon__cli.md#aa4105b00e2a3ad9027b888f0ebbea23e)

struct bt\_mesh\_msg\_ack\_ctx ack\_ctx

**Definition** priv\_beacon\_cli.h:96

[bt\_mesh\_priv\_beacon\_cli::cb](structbt__mesh__priv__beacon__cli.md#ab281b9ac10c54068372f90bccfe07feb)

const struct bt\_mesh\_priv\_beacon\_cli\_cb \* cb

Optional callback for Private Beacon Client Status messages.

**Definition** priv\_beacon\_cli.h:99

[bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md)

Private Beacon.

**Definition** priv\_beacon\_cli.h:36

[bt\_mesh\_priv\_beacon::rand\_interval](structbt__mesh__priv__beacon.md#a1a4972527afde6f9aa5c7726d85ddd45)

uint8\_t rand\_interval

Random refresh interval (in 10 second steps), or 0 to keep current value.

**Definition** priv\_beacon\_cli.h:42

[bt\_mesh\_priv\_beacon::enabled](structbt__mesh__priv__beacon.md#ac38424ed4ebcd69307568763ff2d6ffb)

uint8\_t enabled

Private beacon is enabled.

**Definition** priv\_beacon\_cli.h:38

[bt\_mesh\_priv\_node\_id](structbt__mesh__priv__node__id.md)

Private Node Identity.

**Definition** priv\_beacon\_cli.h:46

[bt\_mesh\_priv\_node\_id::status](structbt__mesh__priv__node__id.md#a49c60fedb24de61a399f3da967f4ac7c)

uint8\_t status

Response status code.

**Definition** priv\_beacon\_cli.h:52

[bt\_mesh\_priv\_node\_id::state](structbt__mesh__priv__node__id.md#a5bd318e61b974a94765e0d28db15994f)

uint8\_t state

Private Node Identity state.

**Definition** priv\_beacon\_cli.h:50

[bt\_mesh\_priv\_node\_id::net\_idx](structbt__mesh__priv__node__id.md#ab772f79daa361a9199f8445b7bda7e44)

uint16\_t net\_idx

Index of the NetKey.

**Definition** priv\_beacon\_cli.h:48

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [priv\_beacon\_cli.h](priv__beacon__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
