---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dfu__srv_8h_source.html
original_path: doxygen/html/dfu__srv_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu\_srv.h

[Go to the documentation of this file.](dfu__srv_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_SRV\_H\_\_

16#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_SRV\_H\_\_

17

18#include <[zephyr/bluetooth/mesh/dfu.h](dfu_8h.md)>

19#include <[zephyr/bluetooth/mesh/blob\_srv.h](blob__srv_8h.md)>

20#include <[zephyr/bluetooth/mesh/access.h](access_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md);

27

[ 36](group__bt__mesh__dfu__srv.md#ga8467cd5241dfdcd7add718bbaae6fa60)#define BT\_MESH\_DFU\_SRV\_INIT(\_handlers, \_imgs, \_img\_count) \

37 { \

38 .blob = { .cb = &\_bt\_mesh\_dfu\_srv\_blob\_cb }, .cb = \_handlers, \

39 .imgs = \_imgs, .img\_count = \_img\_count, \

40 }

41

[ 48](group__bt__mesh__dfu__srv.md#gafdf78cc0f99668d38df4f29138392632)#define BT\_MESH\_MODEL\_DFU\_SRV(\_srv) \

49 BT\_MESH\_MODEL\_BLOB\_SRV(&(\_srv)->blob), \

50 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_DFU\_SRV, \_bt\_mesh\_dfu\_srv\_op, NULL, \

51 \_srv, &\_bt\_mesh\_dfu\_srv\_cb)

52

[ 54](structbt__mesh__dfu__srv__cb.md)struct [bt\_mesh\_dfu\_srv\_cb](structbt__mesh__dfu__srv__cb.md) {

[ 80](structbt__mesh__dfu__srv__cb.md#afbde918804e66160ffa176c206540027) int (\*[check](structbt__mesh__dfu__srv__cb.md#afbde918804e66160ffa176c206540027))(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv,

81 const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img,

82 struct [net\_buf\_simple](structnet__buf__simple.md) \*metadata,

83 enum [bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8) \*effect);

84

[ 113](structbt__mesh__dfu__srv__cb.md#adaefef5067cf3ea273f1db95ca536254) int (\*[start](structbt__mesh__dfu__srv__cb.md#adaefef5067cf3ea273f1db95ca536254))(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv,

114 const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img,

115 struct [net\_buf\_simple](structnet__buf__simple.md) \*metadata,

116 const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io);

117

[ 133](structbt__mesh__dfu__srv__cb.md#a822ed15f15286ad4c5ce69009349f6cf) void (\*[end](structbt__mesh__dfu__srv__cb.md#a822ed15f15286ad4c5ce69009349f6cf))(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv,

134 const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img, bool success);

135

[ 152](structbt__mesh__dfu__srv__cb.md#a3fec449cebe43dd2d8e6ecf3c148234d) int (\*[recover](structbt__mesh__dfu__srv__cb.md#a3fec449cebe43dd2d8e6ecf3c148234d))(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv,

153 const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img,

154 const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io);

155

[ 168](structbt__mesh__dfu__srv__cb.md#afe4b6ca9f56938695addba6ecc18bb4b) int (\*[apply](structbt__mesh__dfu__srv__cb.md#afe4b6ca9f56938695addba6ecc18bb4b))(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv,

169 const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*img);

170};

171

[ 176](structbt__mesh__dfu__srv.md)struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) {

[ 178](structbt__mesh__dfu__srv.md#a75fa0d64310958904435f0b08ae9e5a4) struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) [blob](structbt__mesh__dfu__srv.md#a75fa0d64310958904435f0b08ae9e5a4);

[ 180](structbt__mesh__dfu__srv.md#a23fad6646192b4bdaf80e5bfa3cdf928) const struct [bt\_mesh\_dfu\_srv\_cb](structbt__mesh__dfu__srv__cb.md) \*[cb](structbt__mesh__dfu__srv.md#a23fad6646192b4bdaf80e5bfa3cdf928);

[ 182](structbt__mesh__dfu__srv.md#ab372c28be95c833146f10236d9e3ecfe) const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \*[imgs](structbt__mesh__dfu__srv.md#ab372c28be95c833146f10236d9e3ecfe);

[ 184](structbt__mesh__dfu__srv.md#ab3cdb7ca3928bccebfcf59fab7f76e51) size\_t [img\_count](structbt__mesh__dfu__srv.md#ab3cdb7ca3928bccebfcf59fab7f76e51);

185

186 /\* Runtime state \*/

[ 187](structbt__mesh__dfu__srv.md#aa38a46b0947e5eda84f826703b875ca4) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](structbt__mesh__dfu__srv.md#aa38a46b0947e5eda84f826703b875ca4);

188 struct {

189 /\* Effect of transfer, @see bt\_mesh\_dfu\_effect. \*/

[ 190](structbt__mesh__dfu__srv.md#a5a8f467b0c49dc28b83088d25633f3ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [effect](structbt__mesh__dfu__srv.md#a5a8f467b0c49dc28b83088d25633f3ba);

191 /\* Current phase, @see bt\_mesh\_dfu\_phase. \*/

[ 192](structbt__mesh__dfu__srv.md#a7f9f19a61bf6c0c81dce92e09965936a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phase](structbt__mesh__dfu__srv.md#a7f9f19a61bf6c0c81dce92e09965936a);

[ 193](structbt__mesh__dfu__srv.md#ad8a709d983ee1e00c0becc06f31c23fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__dfu__srv.md#ad8a709d983ee1e00c0becc06f31c23fe);

[ 194](structbt__mesh__dfu__srv.md#a204df1e38192e796fcde5d4b353cc9da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [idx](structbt__mesh__dfu__srv.md#a204df1e38192e796fcde5d4b353cc9da);

[ 195](structbt__mesh__dfu__srv.md#a2916eb8caa2c383f2d1b2a86451a1e6c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout\_base](structbt__mesh__dfu__srv.md#a2916eb8caa2c383f2d1b2a86451a1e6c);

[ 196](structbt__mesh__dfu__srv.md#a273795dbb39d4f822baa35b64362d4ca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [meta](structbt__mesh__dfu__srv.md#a273795dbb39d4f822baa35b64362d4ca);

[ 197](structbt__mesh__dfu__srv.md#a5765c6e143b5fcd0f579f7671a86c4ea) } [update](structbt__mesh__dfu__srv.md#a5765c6e143b5fcd0f579f7671a86c4ea);

198};

199

[ 210](group__bt__mesh__dfu__srv.md#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)void [bt\_mesh\_dfu\_srv\_verified](group__bt__mesh__dfu__srv.md#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv);

211

[ 222](group__bt__mesh__dfu__srv.md#ga77142a1f3cfe2ff1d53332114f977b38)void [bt\_mesh\_dfu\_srv\_rejected](group__bt__mesh__dfu__srv.md#ga77142a1f3cfe2ff1d53332114f977b38)(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv);

223

[ 228](group__bt__mesh__dfu__srv.md#gaf5a00dd89faf52cd7797c54c572e1211)void [bt\_mesh\_dfu\_srv\_cancel](group__bt__mesh__dfu__srv.md#gaf5a00dd89faf52cd7797c54c572e1211)(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv);

229

[ 236](group__bt__mesh__dfu__srv.md#ga45aef92fe1de4c45ccb5369c1f5222ee)void [bt\_mesh\_dfu\_srv\_applied](group__bt__mesh__dfu__srv.md#ga45aef92fe1de4c45ccb5369c1f5222ee)(struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv);

237

[ 244](group__bt__mesh__dfu__srv.md#ga94107fb1ca9207fc6918eae1fb1b3755)bool [bt\_mesh\_dfu\_srv\_is\_busy](group__bt__mesh__dfu__srv.md#ga94107fb1ca9207fc6918eae1fb1b3755)(const struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv);

245

[ 252](group__bt__mesh__dfu__srv.md#ga9f125ace97a40f060e0d8c59fd49f514)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_mesh\_dfu\_srv\_progress](group__bt__mesh__dfu__srv.md#ga9f125ace97a40f060e0d8c59fd49f514)(const struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) \*srv);

253

255extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_dfu\_srv\_op[];

256extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_dfu\_srv\_cb;

257extern const struct [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md) \_bt\_mesh\_dfu\_srv\_blob\_cb;

259

260#ifdef \_\_cplusplus

261}

262#endif

263

264#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_SRV\_H\_\_ \*/

265

[access.h](access_8h.md)

Access layer APIs.

[blob\_srv.h](blob__srv_8h.md)

[dfu.h](dfu_8h.md)

[bt\_mesh\_dfu\_srv\_applied](group__bt__mesh__dfu__srv.md#ga45aef92fe1de4c45ccb5369c1f5222ee)

void bt\_mesh\_dfu\_srv\_applied(struct bt\_mesh\_dfu\_srv \*srv)

Confirm that the received DFU transfer was applied.

[bt\_mesh\_dfu\_srv\_verified](group__bt__mesh__dfu__srv.md#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)

void bt\_mesh\_dfu\_srv\_verified(struct bt\_mesh\_dfu\_srv \*srv)

Accept the received DFU transfer.

[bt\_mesh\_dfu\_srv\_rejected](group__bt__mesh__dfu__srv.md#ga77142a1f3cfe2ff1d53332114f977b38)

void bt\_mesh\_dfu\_srv\_rejected(struct bt\_mesh\_dfu\_srv \*srv)

Reject the received DFU transfer.

[bt\_mesh\_dfu\_srv\_is\_busy](group__bt__mesh__dfu__srv.md#ga94107fb1ca9207fc6918eae1fb1b3755)

bool bt\_mesh\_dfu\_srv\_is\_busy(const struct bt\_mesh\_dfu\_srv \*srv)

Check if the Firmware Update Server is busy processing a transfer.

[bt\_mesh\_dfu\_srv\_progress](group__bt__mesh__dfu__srv.md#ga9f125ace97a40f060e0d8c59fd49f514)

uint8\_t bt\_mesh\_dfu\_srv\_progress(const struct bt\_mesh\_dfu\_srv \*srv)

Get the progress of the current DFU procedure, in percent.

[bt\_mesh\_dfu\_srv\_cancel](group__bt__mesh__dfu__srv.md#gaf5a00dd89faf52cd7797c54c572e1211)

void bt\_mesh\_dfu\_srv\_cancel(struct bt\_mesh\_dfu\_srv \*srv)

Cancel the ongoing DFU transfer.

[bt\_mesh\_dfu\_effect](group__bt__mesh__dfu.md#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)

bt\_mesh\_dfu\_effect

Expected effect of a DFU transfer.

**Definition** dfu.h:108

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)

BLOB stream.

**Definition** blob.h:145

[bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md)

BLOB Transfer Server model event handlers.

**Definition** blob\_srv.h:51

[bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md)

BLOB Transfer Server model instance.

**Definition** blob\_srv.h:131

[bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md)

DFU image instance.

**Definition** dfu.h:140

[bt\_mesh\_dfu\_srv\_cb](structbt__mesh__dfu__srv__cb.md)

Firmware Update Server event callbacks.

**Definition** dfu\_srv.h:54

[bt\_mesh\_dfu\_srv\_cb::recover](structbt__mesh__dfu__srv__cb.md#a3fec449cebe43dd2d8e6ecf3c148234d)

int(\* recover)(struct bt\_mesh\_dfu\_srv \*srv, const struct bt\_mesh\_dfu\_img \*img, const struct bt\_mesh\_blob\_io \*\*io)

Transfer recovery callback.

**Definition** dfu\_srv.h:152

[bt\_mesh\_dfu\_srv\_cb::end](structbt__mesh__dfu__srv__cb.md#a822ed15f15286ad4c5ce69009349f6cf)

void(\* end)(struct bt\_mesh\_dfu\_srv \*srv, const struct bt\_mesh\_dfu\_img \*img, bool success)

Transfer end callback.

**Definition** dfu\_srv.h:133

[bt\_mesh\_dfu\_srv\_cb::start](structbt__mesh__dfu__srv__cb.md#adaefef5067cf3ea273f1db95ca536254)

int(\* start)(struct bt\_mesh\_dfu\_srv \*srv, const struct bt\_mesh\_dfu\_img \*img, struct net\_buf\_simple \*metadata, const struct bt\_mesh\_blob\_io \*\*io)

Transfer start callback.

**Definition** dfu\_srv.h:113

[bt\_mesh\_dfu\_srv\_cb::check](structbt__mesh__dfu__srv__cb.md#afbde918804e66160ffa176c206540027)

int(\* check)(struct bt\_mesh\_dfu\_srv \*srv, const struct bt\_mesh\_dfu\_img \*img, struct net\_buf\_simple \*metadata, enum bt\_mesh\_dfu\_effect \*effect)

Transfer check callback.

**Definition** dfu\_srv.h:80

[bt\_mesh\_dfu\_srv\_cb::apply](structbt__mesh__dfu__srv__cb.md#afe4b6ca9f56938695addba6ecc18bb4b)

int(\* apply)(struct bt\_mesh\_dfu\_srv \*srv, const struct bt\_mesh\_dfu\_img \*img)

Transfer apply callback.

**Definition** dfu\_srv.h:168

[bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md)

Firmware Update Server instance.

**Definition** dfu\_srv.h:176

[bt\_mesh\_dfu\_srv::idx](structbt__mesh__dfu__srv.md#a204df1e38192e796fcde5d4b353cc9da)

uint8\_t idx

**Definition** dfu\_srv.h:194

[bt\_mesh\_dfu\_srv::cb](structbt__mesh__dfu__srv.md#a23fad6646192b4bdaf80e5bfa3cdf928)

const struct bt\_mesh\_dfu\_srv\_cb \* cb

Callback structure.

**Definition** dfu\_srv.h:180

[bt\_mesh\_dfu\_srv::meta](structbt__mesh__dfu__srv.md#a273795dbb39d4f822baa35b64362d4ca)

uint16\_t meta

**Definition** dfu\_srv.h:196

[bt\_mesh\_dfu\_srv::timeout\_base](structbt__mesh__dfu__srv.md#a2916eb8caa2c383f2d1b2a86451a1e6c)

uint16\_t timeout\_base

**Definition** dfu\_srv.h:195

[bt\_mesh\_dfu\_srv::update](structbt__mesh__dfu__srv.md#a5765c6e143b5fcd0f579f7671a86c4ea)

struct bt\_mesh\_dfu\_srv::@204141015330054241064150375156056317111103346337 update

[bt\_mesh\_dfu\_srv::effect](structbt__mesh__dfu__srv.md#a5a8f467b0c49dc28b83088d25633f3ba)

uint8\_t effect

**Definition** dfu\_srv.h:190

[bt\_mesh\_dfu\_srv::blob](structbt__mesh__dfu__srv.md#a75fa0d64310958904435f0b08ae9e5a4)

struct bt\_mesh\_blob\_srv blob

Underlying BLOB Transfer Server.

**Definition** dfu\_srv.h:178

[bt\_mesh\_dfu\_srv::phase](structbt__mesh__dfu__srv.md#a7f9f19a61bf6c0c81dce92e09965936a)

uint8\_t phase

**Definition** dfu\_srv.h:192

[bt\_mesh\_dfu\_srv::mod](structbt__mesh__dfu__srv.md#aa38a46b0947e5eda84f826703b875ca4)

const struct bt\_mesh\_model \* mod

**Definition** dfu\_srv.h:187

[bt\_mesh\_dfu\_srv::imgs](structbt__mesh__dfu__srv.md#ab372c28be95c833146f10236d9e3ecfe)

const struct bt\_mesh\_dfu\_img \* imgs

List of updatable images.

**Definition** dfu\_srv.h:182

[bt\_mesh\_dfu\_srv::img\_count](structbt__mesh__dfu__srv.md#ab3cdb7ca3928bccebfcf59fab7f76e51)

size\_t img\_count

Number of updatable images.

**Definition** dfu\_srv.h:184

[bt\_mesh\_dfu\_srv::ttl](structbt__mesh__dfu__srv.md#ad8a709d983ee1e00c0becc06f31c23fe)

uint8\_t ttl

**Definition** dfu\_srv.h:193

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:891

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfu\_srv.h](dfu__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
