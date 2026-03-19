---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/blob__srv_8h_source.html
original_path: doxygen/html/blob__srv_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

blob\_srv.h

[Go to the documentation of this file.](blob__srv_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_SRV\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_SRV\_H\_

9

10#include <[zephyr/bluetooth/mesh/access.h](access_8h.md)>

11#include <[zephyr/bluetooth/mesh/blob.h](blob_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

22

23struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md);

24

29#if defined(CONFIG\_BT\_MESH\_BLOB\_SRV)

30#define BT\_MESH\_BLOB\_BLOCKS\_MAX \

31 (DIV\_ROUND\_UP(CONFIG\_BT\_MESH\_BLOB\_SIZE\_MAX, \

32 CONFIG\_BT\_MESH\_BLOB\_BLOCK\_SIZE\_MIN))

33#else

[ 34](group__bt__mesh__blob__srv.md#gaae3dfbf15f33739bc0a42c924de99cba)#define BT\_MESH\_BLOB\_BLOCKS\_MAX 1

35#endif

36

[ 43](group__bt__mesh__blob__srv.md#gad9db3253c13d50cfb6c89dff881dbfe9)#define BT\_MESH\_MODEL\_BLOB\_SRV(\_srv) \

44 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_BLOB\_SRV, \_bt\_mesh\_blob\_srv\_op, \

45 NULL, \_srv, &\_bt\_mesh\_blob\_srv\_cb)

46

[ 51](structbt__mesh__blob__srv__cb.md)struct [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md) {

[ 65](structbt__mesh__blob__srv__cb.md#aad5ab6e396f049a3b8a239e9f0d1c063) int (\*[start](structbt__mesh__blob__srv__cb.md#aad5ab6e396f049a3b8a239e9f0d1c063))(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx,

66 struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer);

67

[ 80](structbt__mesh__blob__srv__cb.md#af7b6f557f38c15a174a2a75d1210dab3) void (\*[end](structbt__mesh__blob__srv__cb.md#af7b6f557f38c15a174a2a75d1210dab3))(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id, bool success);

81

[ 99](structbt__mesh__blob__srv__cb.md#a99a054d410f0a82101b15309a8f4ec33) void (\*[suspended](structbt__mesh__blob__srv__cb.md#a99a054d410f0a82101b15309a8f4ec33))(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv);

100

[ 107](structbt__mesh__blob__srv__cb.md#ae032ff1d52f46f1716451dc5ff138d0f) void (\*[resume](structbt__mesh__blob__srv__cb.md#ae032ff1d52f46f1716451dc5ff138d0f))(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv);

108

[ 125](structbt__mesh__blob__srv__cb.md#a94b56462c5fd95535a5f1e0ba2ddf99a) int (\*[recover](structbt__mesh__blob__srv__cb.md#a94b56462c5fd95535a5f1e0ba2ddf99a))(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv,

126 struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer,

127 const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io);

128};

129

[ 131](structbt__mesh__blob__srv.md)struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) {

[ 133](structbt__mesh__blob__srv.md#a65d08187dce1ed86cbfbb4f977cd32df) const struct [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md) \*[cb](structbt__mesh__blob__srv.md#a65d08187dce1ed86cbfbb4f977cd32df);

134

135 /\* Runtime state: \*/

[ 136](structbt__mesh__blob__srv.md#a23d12a803a2414aa1460ea9a862cc78b) const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*[io](structbt__mesh__blob__srv.md#a23d12a803a2414aa1460ea9a862cc78b);

[ 137](structbt__mesh__blob__srv.md#a82a5c7fc2ad37e531ec10bada27bf10a) struct [k\_work\_delayable](structk__work__delayable.md) [rx\_timeout](structbt__mesh__blob__srv.md#a82a5c7fc2ad37e531ec10bada27bf10a);

[ 138](structbt__mesh__blob__srv.md#a8d6a01849e95c4a26d3270f4320c214f) struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) [block](structbt__mesh__blob__srv.md#a8d6a01849e95c4a26d3270f4320c214f);

[ 139](structbt__mesh__blob__srv.md#a1066d309b56748223183d39e8fc7fd82) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](structbt__mesh__blob__srv.md#a1066d309b56748223183d39e8fc7fd82);

[ 140](structbt__mesh__blob__srv.md#a75b8ecd846fcf96708d31fb5efb0bea1) enum [bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) [phase](structbt__mesh__blob__srv.md#a75b8ecd846fcf96708d31fb5efb0bea1);

141

[ 142](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md) struct [bt\_mesh\_blob\_srv\_state](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md) {

[ 143](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#ac5d12eef4c5723af0e19296d75f1c820) struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) [xfer](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#ac5d12eef4c5723af0e19296d75f1c820);

[ 144](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a08358fb301e775ed23c0d062676fbf22) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cli](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a08358fb301e775ed23c0d062676fbf22);

[ 145](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a6273d55eda23f868d51382c56bc41e27) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [app\_idx](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a6273d55eda23f868d51382c56bc41e27);

[ 146](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a0c87b3052680c675303747e805c2990e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout\_base](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a0c87b3052680c675303747e805c2990e);

[ 147](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#aadd08825d36f3ae1e4fe3a7845903f41) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu\_size](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#aadd08825d36f3ae1e4fe3a7845903f41);

[ 148](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a79b0521bbd2473c6b414a24c5a7bf98a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a79b0521bbd2473c6b414a24c5a7bf98a);

149

150 /\* Bitfield of pending blocks. \*/

[ 151](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a0f5d7d310be154f85ee96ccceb12e971) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([blocks](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a0f5d7d310be154f85ee96ccceb12e971), [BT\_MESH\_BLOB\_BLOCKS\_MAX](group__bt__mesh__blob__srv.md#gaae3dfbf15f33739bc0a42c924de99cba));

[ 152](structbt__mesh__blob__srv.md#a86ed657bc97fc3c299e6fca6cdaee4e4) } [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

153

154 /\* Pull mode (Pull BLOB Transfer Mode) behavior. \*/

155 struct {

[ 156](structbt__mesh__blob__srv.md#aa3ac872db59f2f1cd67d25e97020d484) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chunk\_idx](structbt__mesh__blob__srv.md#aa3ac872db59f2f1cd67d25e97020d484);

[ 157](structbt__mesh__blob__srv.md#aad6ef41a187cc5489d6a8d5f4a5b3003) struct [k\_work\_delayable](structk__work__delayable.md) [report](structbt__mesh__blob__srv.md#aad6ef41a187cc5489d6a8d5f4a5b3003);

[ 158](structbt__mesh__blob__srv.md#afec2237da95cc7ffbbdeb99d8ffb12b6) } [pull](structbt__mesh__blob__srv.md#afec2237da95cc7ffbbdeb99d8ffb12b6);

159};

160

[ 176](group__bt__mesh__blob__srv.md#ga5d35f13eeb6f7a1fb252e8fb905e9cb3)int [bt\_mesh\_blob\_srv\_recv](group__bt__mesh__blob__srv.md#ga5d35f13eeb6f7a1fb252e8fb905e9cb3)(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id,

177 const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl,

178 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout\_base);

179

[ 190](group__bt__mesh__blob__srv.md#gae8739e96f2157f588072e91b51891835)int [bt\_mesh\_blob\_srv\_cancel](group__bt__mesh__blob__srv.md#gae8739e96f2157f588072e91b51891835)(struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv);

191

[ 199](group__bt__mesh__blob__srv.md#gaa7a253c9a577eaa1307bc0e6b93a3d66)bool [bt\_mesh\_blob\_srv\_is\_busy](group__bt__mesh__blob__srv.md#gaa7a253c9a577eaa1307bc0e6b93a3d66)(const struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv);

200

[ 207](group__bt__mesh__blob__srv.md#ga674b59ff721575539818ef74e8d1b91c)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_mesh\_blob\_srv\_progress](group__bt__mesh__blob__srv.md#ga674b59ff721575539818ef74e8d1b91c)(const struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) \*srv);

208

210extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_blob\_srv\_op[];

211extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_blob\_srv\_cb;

213

215

216#ifdef \_\_cplusplus

217}

218#endif

219

220#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_SRV\_H\_ \*/

[access.h](access_8h.md)

Access layer APIs.

[blob.h](blob_8h.md)

[ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)

#define ATOMIC\_DEFINE(name, num\_bits)

Define an array of atomic variables.

**Definition** atomic.h:111

[bt\_mesh\_blob\_srv\_recv](group__bt__mesh__blob__srv.md#ga5d35f13eeb6f7a1fb252e8fb905e9cb3)

int bt\_mesh\_blob\_srv\_recv(struct bt\_mesh\_blob\_srv \*srv, uint64\_t id, const struct bt\_mesh\_blob\_io \*io, uint8\_t ttl, uint16\_t timeout\_base)

Prepare BLOB Transfer Server for an incoming transfer.

[bt\_mesh\_blob\_srv\_progress](group__bt__mesh__blob__srv.md#ga674b59ff721575539818ef74e8d1b91c)

uint8\_t bt\_mesh\_blob\_srv\_progress(const struct bt\_mesh\_blob\_srv \*srv)

Get the current progress of the active transfer in percent.

[bt\_mesh\_blob\_srv\_is\_busy](group__bt__mesh__blob__srv.md#gaa7a253c9a577eaa1307bc0e6b93a3d66)

bool bt\_mesh\_blob\_srv\_is\_busy(const struct bt\_mesh\_blob\_srv \*srv)

Get the current state of the BLOB Transfer Server.

[BT\_MESH\_BLOB\_BLOCKS\_MAX](group__bt__mesh__blob__srv.md#gaae3dfbf15f33739bc0a42c924de99cba)

#define BT\_MESH\_BLOB\_BLOCKS\_MAX

Max number of blocks in a single transfer.

**Definition** blob\_srv.h:34

[bt\_mesh\_blob\_srv\_cancel](group__bt__mesh__blob__srv.md#gae8739e96f2157f588072e91b51891835)

int bt\_mesh\_blob\_srv\_cancel(struct bt\_mesh\_blob\_srv \*srv)

Cancel the current BLOB transfer.

[bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81)

bt\_mesh\_blob\_xfer\_phase

Transfer phase.

**Definition** blob.h:41

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_blob\_block](structbt__mesh__blob__block.md)

BLOB transfer data block.

**Definition** blob.h:98

[bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)

BLOB stream.

**Definition** blob.h:145

[bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md)

**Definition** blob\_srv.h:142

[bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::cli](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a08358fb301e775ed23c0d062676fbf22)

uint16\_t cli

**Definition** blob\_srv.h:144

[bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::timeout\_base](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a0c87b3052680c675303747e805c2990e)

uint16\_t timeout\_base

**Definition** blob\_srv.h:146

[bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::blocks](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a0f5d7d310be154f85ee96ccceb12e971)

atomic\_t blocks[ATOMIC\_BITMAP\_SIZE(1)]

**Definition** blob\_srv.h:151

[bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::app\_idx](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a6273d55eda23f868d51382c56bc41e27)

uint16\_t app\_idx

**Definition** blob\_srv.h:145

[bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::ttl](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#a79b0521bbd2473c6b414a24c5a7bf98a)

uint8\_t ttl

**Definition** blob\_srv.h:148

[bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::mtu\_size](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#aadd08825d36f3ae1e4fe3a7845903f41)

uint16\_t mtu\_size

**Definition** blob\_srv.h:147

[bt\_mesh\_blob\_srv::bt\_mesh\_blob\_srv\_state::xfer](structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.md#ac5d12eef4c5723af0e19296d75f1c820)

struct bt\_mesh\_blob\_xfer xfer

**Definition** blob\_srv.h:143

[bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md)

BLOB Transfer Server model event handlers.

**Definition** blob\_srv.h:51

[bt\_mesh\_blob\_srv\_cb::recover](structbt__mesh__blob__srv__cb.md#a94b56462c5fd95535a5f1e0ba2ddf99a)

int(\* recover)(struct bt\_mesh\_blob\_srv \*srv, struct bt\_mesh\_blob\_xfer \*xfer, const struct bt\_mesh\_blob\_io \*\*io)

Transfer recovery callback.

**Definition** blob\_srv.h:125

[bt\_mesh\_blob\_srv\_cb::suspended](structbt__mesh__blob__srv__cb.md#a99a054d410f0a82101b15309a8f4ec33)

void(\* suspended)(struct bt\_mesh\_blob\_srv \*srv)

Transfer suspended callback.

**Definition** blob\_srv.h:99

[bt\_mesh\_blob\_srv\_cb::start](structbt__mesh__blob__srv__cb.md#aad5ab6e396f049a3b8a239e9f0d1c063)

int(\* start)(struct bt\_mesh\_blob\_srv \*srv, struct bt\_mesh\_msg\_ctx \*ctx, struct bt\_mesh\_blob\_xfer \*xfer)

Transfer start callback.

**Definition** blob\_srv.h:65

[bt\_mesh\_blob\_srv\_cb::resume](structbt__mesh__blob__srv__cb.md#ae032ff1d52f46f1716451dc5ff138d0f)

void(\* resume)(struct bt\_mesh\_blob\_srv \*srv)

Transfer resume callback.

**Definition** blob\_srv.h:107

[bt\_mesh\_blob\_srv\_cb::end](structbt__mesh__blob__srv__cb.md#af7b6f557f38c15a174a2a75d1210dab3)

void(\* end)(struct bt\_mesh\_blob\_srv \*srv, uint64\_t id, bool success)

Transfer end callback.

**Definition** blob\_srv.h:80

[bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md)

BLOB Transfer Server model instance.

**Definition** blob\_srv.h:131

[bt\_mesh\_blob\_srv::mod](structbt__mesh__blob__srv.md#a1066d309b56748223183d39e8fc7fd82)

const struct bt\_mesh\_model \* mod

**Definition** blob\_srv.h:139

[bt\_mesh\_blob\_srv::io](structbt__mesh__blob__srv.md#a23d12a803a2414aa1460ea9a862cc78b)

const struct bt\_mesh\_blob\_io \* io

**Definition** blob\_srv.h:136

[bt\_mesh\_blob\_srv::cb](structbt__mesh__blob__srv.md#a65d08187dce1ed86cbfbb4f977cd32df)

const struct bt\_mesh\_blob\_srv\_cb \* cb

Event handler callbacks.

**Definition** blob\_srv.h:133

[bt\_mesh\_blob\_srv::phase](structbt__mesh__blob__srv.md#a75b8ecd846fcf96708d31fb5efb0bea1)

enum bt\_mesh\_blob\_xfer\_phase phase

**Definition** blob\_srv.h:140

[bt\_mesh\_blob\_srv::rx\_timeout](structbt__mesh__blob__srv.md#a82a5c7fc2ad37e531ec10bada27bf10a)

struct k\_work\_delayable rx\_timeout

**Definition** blob\_srv.h:137

[bt\_mesh\_blob\_srv::block](structbt__mesh__blob__srv.md#a8d6a01849e95c4a26d3270f4320c214f)

struct bt\_mesh\_blob\_block block

**Definition** blob\_srv.h:138

[bt\_mesh\_blob\_srv::chunk\_idx](structbt__mesh__blob__srv.md#aa3ac872db59f2f1cd67d25e97020d484)

uint16\_t chunk\_idx

**Definition** blob\_srv.h:156

[bt\_mesh\_blob\_srv::report](structbt__mesh__blob__srv.md#aad6ef41a187cc5489d6a8d5f4a5b3003)

struct k\_work\_delayable report

**Definition** blob\_srv.h:157

[bt\_mesh\_blob\_srv::pull](structbt__mesh__blob__srv.md#afec2237da95cc7ffbbdeb99d8ffb12b6)

struct bt\_mesh\_blob\_srv::@067133117245337364026014036366273070063164131043 pull

[bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md)

BLOB transfer.

**Definition** blob.h:123

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:891

[bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md)

Message sending context.

**Definition** msg.h:76

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4034

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [blob\_srv.h](blob__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
