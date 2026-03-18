---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dfd__srv_8h_source.html
original_path: doxygen/html/dfd__srv_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfd\_srv.h

[Go to the documentation of this file.](dfd__srv_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFD\_SRV\_H\_\_

16#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFD\_SRV\_H\_\_

17

18#include <[zephyr/bluetooth/mesh/access.h](access_8h.md)>

19#include <[zephyr/bluetooth/mesh/dfd.h](dfd_8h.md)>

20#include <[zephyr/bluetooth/mesh/blob\_srv.h](blob__srv_8h.md)>

21#include <[zephyr/bluetooth/mesh/blob\_cli.h](blob__cli_8h.md)>

22#include <[zephyr/bluetooth/mesh/dfu\_cli.h](dfu__cli_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28#ifndef CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX

[ 29](group__bt__mesh__dfd__srv.md#ga126e2d4df8f58b7de36da46c14b2c804)#define CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX 0

30#endif

31

32#ifndef CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_MAX\_SIZE

[ 33](group__bt__mesh__dfd__srv.md#gab26590917c9de6edaccf07540c88f7c1)#define CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_MAX\_SIZE 0

34#endif

35

36#ifndef CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_SPACE

[ 37](group__bt__mesh__dfd__srv.md#ga394c367492c72f66231b5cf3e2789f5f)#define CONFIG\_BT\_MESH\_DFD\_SRV\_SLOT\_SPACE 0

38#endif

39

40struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md);

41

42#ifdef CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD

54#define BT\_MESH\_DFD\_SRV\_OOB\_INIT(\_cb, \_oob\_schemes, \_oob\_schemes\_count) \

55 { \

56 .cb = \_cb, \

57 .dfu = BT\_MESH\_DFU\_CLI\_INIT(&\_bt\_mesh\_dfd\_srv\_dfu\_cb), \

58 .upload = { \

59 .blob = { .cb = &\_bt\_mesh\_dfd\_srv\_blob\_cb }, \

60 }, \

61 .oob\_schemes = { \

62 .schemes = \_oob\_schemes, \

63 .count = \_oob\_schemes\_count, \

64 }, \

65 }

66#endif /\* CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD \*/

67

[ 74](group__bt__mesh__dfd__srv.md#ga20b1232269b2e859608c21e84305196c)#define BT\_MESH\_DFD\_SRV\_INIT(\_cb) \

75 { \

76 .cb = \_cb, \

77 .dfu = BT\_MESH\_DFU\_CLI\_INIT(&\_bt\_mesh\_dfd\_srv\_dfu\_cb), \

78 .upload = { \

79 .blob = { .cb = &\_bt\_mesh\_dfd\_srv\_blob\_cb }, \

80 }, \

81 }

82

[ 89](group__bt__mesh__dfd__srv.md#ga27457d4d72119ab080828359d43ad6cf)#define BT\_MESH\_MODEL\_DFD\_SRV(\_srv) \

90 BT\_MESH\_MODEL\_DFU\_CLI(&(\_srv)->dfu), \

91 BT\_MESH\_MODEL\_BLOB\_SRV(&(\_srv)->upload.blob), \

92 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_DFD\_SRV, \_bt\_mesh\_dfd\_srv\_op, NULL, \

93 \_srv, &\_bt\_mesh\_dfd\_srv\_cb)

94

[ 96](structbt__mesh__dfd__srv__cb.md)struct [bt\_mesh\_dfd\_srv\_cb](structbt__mesh__dfd__srv__cb.md) {

97

[ 110](structbt__mesh__dfd__srv__cb.md#a6d6d991b3a5bd5fe69b1648fea94ebe4) int (\*[recv](structbt__mesh__dfd__srv__cb.md#a6d6d991b3a5bd5fe69b1648fea94ebe4))(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv,

111 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot,

112 const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io);

113

114#ifdef CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD

140 int (\*start\_oob\_upload)(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv,

141 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot,

142 const char \*uri, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uri\_len,

143 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*fwid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fwid\_len);

144

154 void (\*cancel\_oob\_upload)(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv,

155 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot);

156

168 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*oob\_progress\_get)(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv,

169 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot);

170#endif /\* CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD \*/

171

[ 181](structbt__mesh__dfd__srv__cb.md#a73f230a76ea32fb1faee15a5d4adb550) void (\*[del](structbt__mesh__dfd__srv__cb.md#a73f230a76ea32fb1faee15a5d4adb550))(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv,

182 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot);

183

[ 196](structbt__mesh__dfd__srv__cb.md#a84e14ad78ebe520bad3ad6ee24fbb629) int (\*[send](structbt__mesh__dfd__srv__cb.md#a84e14ad78ebe520bad3ad6ee24fbb629))(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv,

197 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot,

198 const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*\*io);

199

[ 207](structbt__mesh__dfd__srv__cb.md#ae72a527cae827e0a234af3277384d07f) void (\*[phase](structbt__mesh__dfd__srv__cb.md#ae72a527cae827e0a234af3277384d07f))(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv, enum [bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) [phase](structbt__mesh__dfd__srv__cb.md#ae72a527cae827e0a234af3277384d07f));

208};

209

[ 211](structbt__mesh__dfd__srv.md)struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) {

[ 212](structbt__mesh__dfd__srv.md#a7edbfa6bedb887a941b7567b9eeac8fd) const struct [bt\_mesh\_dfd\_srv\_cb](structbt__mesh__dfd__srv__cb.md) \*[cb](structbt__mesh__dfd__srv.md#a7edbfa6bedb887a941b7567b9eeac8fd);

[ 213](structbt__mesh__dfd__srv.md#a20bce6a528c1ef8433f55e8a4277a0ca) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](structbt__mesh__dfd__srv.md#a20bce6a528c1ef8433f55e8a4277a0ca);

[ 214](structbt__mesh__dfd__srv.md#a1d022e6e15350cd85999f0b07e34f519) struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) [dfu](structbt__mesh__dfd__srv.md#a1d022e6e15350cd85999f0b07e34f519);

[ 215](structbt__mesh__dfd__srv.md#abde92a8837d687ef213836d593bf979d) struct [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md) [targets](structbt__mesh__dfd__srv.md#abde92a8837d687ef213836d593bf979d)[[CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX](group__bt__mesh__dfd__srv.md#ga126e2d4df8f58b7de36da46c14b2c804)];

[ 216](structbt__mesh__dfd__srv.md#a1345da3143b1d3334a55ad8053967bf9) struct [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md) [pull\_ctxs](structbt__mesh__dfd__srv.md#a1345da3143b1d3334a55ad8053967bf9)[[CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX](group__bt__mesh__dfd__srv.md#ga126e2d4df8f58b7de36da46c14b2c804)];

[ 217](structbt__mesh__dfd__srv.md#a691eb383f51fd6e10b615ab8921005de) const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*[io](structbt__mesh__dfd__srv.md#a691eb383f51fd6e10b615ab8921005de);

[ 218](structbt__mesh__dfd__srv.md#a67e4997a4367d9547a0ae9ff6c2017d6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [target\_cnt](structbt__mesh__dfd__srv.md#a67e4997a4367d9547a0ae9ff6c2017d6);

[ 219](structbt__mesh__dfd__srv.md#af61665ebb2f46bd3e6277c6ee95ff68c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [slot\_idx](structbt__mesh__dfd__srv.md#af61665ebb2f46bd3e6277c6ee95ff68c);

[ 220](structbt__mesh__dfd__srv.md#af1ac88ae8d9e1e42ff8a98d3969c359d) bool [apply](structbt__mesh__dfd__srv.md#af1ac88ae8d9e1e42ff8a98d3969c359d);

[ 221](structbt__mesh__dfd__srv.md#a4a7847580637713b305918c77210e3c0) enum [bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) [phase](structbt__mesh__dfd__srv.md#a4a7847580637713b305918c77210e3c0);

[ 222](structbt__mesh__dfd__srv.md#a4e28f0e0845d1aeb6ebc03032ecfe813) struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) [inputs](structbt__mesh__dfd__srv.md#a4e28f0e0845d1aeb6ebc03032ecfe813);

223

224 struct {

[ 225](structbt__mesh__dfd__srv.md#aa71e5affa0bf002499f3176794c6d9ca) enum [bt\_mesh\_dfd\_upload\_phase](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb) [phase](structbt__mesh__dfd__srv.md#a4a7847580637713b305918c77210e3c0);

[ 226](structbt__mesh__dfd__srv.md#a02b5ed65738bf08715bbc6a177c6f1ce) struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*[slot](structbt__mesh__dfd__srv.md#a02b5ed65738bf08715bbc6a177c6f1ce);

[ 227](structbt__mesh__dfd__srv.md#a52b10a938105d0fb22e72e30fc92df5c) const struct [flash\_area](structflash__area.md) \*[area](structbt__mesh__dfd__srv.md#a52b10a938105d0fb22e72e30fc92df5c);

[ 228](structbt__mesh__dfd__srv.md#ab538079d9f6b98f0de65583d6bdfe7f0) struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) [blob](structbt__mesh__dfd__srv.md#ab538079d9f6b98f0de65583d6bdfe7f0);

229#ifdef CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD

230 bool is\_oob;

231 bool is\_pending\_oob\_check;

232 struct {

233 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uri\_len;

234 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uri[[CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN](group__bt__mesh__dfu.md#gaa0812409217dd069b00d386d8ab17f5c)];

235 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) current\_fwid\_len;

236 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) current\_fwid[[CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN](group__bt__mesh__dfu.md#gacd0f7b01837809a0a92d27f248a9fdd3)];

237 struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) ctx;

238 } oob;

239#endif /\* CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD \*/

[ 240](structbt__mesh__dfd__srv.md#a26e4b13a8688f26c3330a2b0948bfc8d) } [upload](structbt__mesh__dfd__srv.md#a26e4b13a8688f26c3330a2b0948bfc8d);

241

242#ifdef CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD

243 struct {

244 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*schemes;

245 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count;

246 } oob\_schemes;

247#endif /\* CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD \*/

248};

249

250#ifdef CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD

276int bt\_mesh\_dfd\_srv\_oob\_check\_complete(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv,

277 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot, int status,

278 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*fwid, size\_t fwid\_len);

279

295int bt\_mesh\_dfd\_srv\_oob\_store\_complete(struct [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md) \*srv,

296 const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*slot, bool success,

297 size\_t size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*metadata, size\_t metadata\_len);

298#endif /\* CONFIG\_BT\_MESH\_DFD\_SRV\_OOB\_UPLOAD \*/

299

301extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_dfd\_srv\_op[];

302extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_dfd\_srv\_cb;

303extern const struct [bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md) \_bt\_mesh\_dfd\_srv\_dfu\_cb;

304extern const struct [bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md) \_bt\_mesh\_dfd\_srv\_blob\_cb;

306

307#ifdef \_\_cplusplus

308}

309#endif

310

311#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFD\_SRV\_H\_\_ \*/

312

[access.h](access_8h.md)

Access layer APIs.

[blob\_cli.h](blob__cli_8h.md)

[blob\_srv.h](blob__srv_8h.md)

[dfd.h](dfd_8h.md)

[dfu\_cli.h](dfu__cli_8h.md)

[CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX](group__bt__mesh__dfd__srv.md#ga126e2d4df8f58b7de36da46c14b2c804)

#define CONFIG\_BT\_MESH\_DFD\_SRV\_TARGETS\_MAX

**Definition** dfd\_srv.h:29

[bt\_mesh\_dfd\_upload\_phase](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb)

bt\_mesh\_dfd\_upload\_phase

Firmware upload phases.

**Definition** dfd.h:100

[bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2)

bt\_mesh\_dfd\_phase

Firmware distribution phases.

**Definition** dfd.h:73

[CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN](group__bt__mesh__dfu.md#gaa0812409217dd069b00d386d8ab17f5c)

#define CONFIG\_BT\_MESH\_DFU\_URI\_MAXLEN

**Definition** dfu.h:34

[CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN](group__bt__mesh__dfu.md#gacd0f7b01837809a0a92d27f248a9fdd3)

#define CONFIG\_BT\_MESH\_DFU\_FWID\_MAXLEN

**Definition** dfu.h:26

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md)

BLOB Transfer Client transfer inputs.

**Definition** blob\_cli.h:104

[bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)

BLOB stream.

**Definition** blob.h:145

[bt\_mesh\_blob\_srv\_cb](structbt__mesh__blob__srv__cb.md)

BLOB Transfer Server model event handlers.

**Definition** blob\_srv.h:51

[bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md)

BLOB Transfer Server instance.

**Definition** blob\_srv.h:131

[bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md)

Target node's Pull mode (Pull BLOB Transfer Mode) context used while sending chunks to the Target nod...

**Definition** blob\_cli.h:40

[bt\_mesh\_dfd\_srv\_cb](structbt__mesh__dfd__srv__cb.md)

Firmware Distribution Server callbacks:

**Definition** dfd\_srv.h:96

[bt\_mesh\_dfd\_srv\_cb::recv](structbt__mesh__dfd__srv__cb.md#a6d6d991b3a5bd5fe69b1648fea94ebe4)

int(\* recv)(struct bt\_mesh\_dfd\_srv \*srv, const struct bt\_mesh\_dfu\_slot \*slot, const struct bt\_mesh\_blob\_io \*\*io)

Slot receive callback.

**Definition** dfd\_srv.h:110

[bt\_mesh\_dfd\_srv\_cb::del](structbt__mesh__dfd__srv__cb.md#a73f230a76ea32fb1faee15a5d4adb550)

void(\* del)(struct bt\_mesh\_dfd\_srv \*srv, const struct bt\_mesh\_dfu\_slot \*slot)

Slot delete callback.

**Definition** dfd\_srv.h:181

[bt\_mesh\_dfd\_srv\_cb::send](structbt__mesh__dfd__srv__cb.md#a84e14ad78ebe520bad3ad6ee24fbb629)

int(\* send)(struct bt\_mesh\_dfd\_srv \*srv, const struct bt\_mesh\_dfu\_slot \*slot, const struct bt\_mesh\_blob\_io \*\*io)

Slot send callback.

**Definition** dfd\_srv.h:196

[bt\_mesh\_dfd\_srv\_cb::phase](structbt__mesh__dfd__srv__cb.md#ae72a527cae827e0a234af3277384d07f)

void(\* phase)(struct bt\_mesh\_dfd\_srv \*srv, enum bt\_mesh\_dfd\_phase phase)

Phase change callback (Optional).

**Definition** dfd\_srv.h:207

[bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md)

Firmware Distribution Server instance.

**Definition** dfd\_srv.h:211

[bt\_mesh\_dfd\_srv::slot](structbt__mesh__dfd__srv.md#a02b5ed65738bf08715bbc6a177c6f1ce)

struct bt\_mesh\_dfu\_slot \* slot

**Definition** dfd\_srv.h:226

[bt\_mesh\_dfd\_srv::pull\_ctxs](structbt__mesh__dfd__srv.md#a1345da3143b1d3334a55ad8053967bf9)

struct bt\_mesh\_blob\_target\_pull pull\_ctxs[0]

**Definition** dfd\_srv.h:216

[bt\_mesh\_dfd\_srv::dfu](structbt__mesh__dfd__srv.md#a1d022e6e15350cd85999f0b07e34f519)

struct bt\_mesh\_dfu\_cli dfu

**Definition** dfd\_srv.h:214

[bt\_mesh\_dfd\_srv::mod](structbt__mesh__dfd__srv.md#a20bce6a528c1ef8433f55e8a4277a0ca)

const struct bt\_mesh\_model \* mod

**Definition** dfd\_srv.h:213

[bt\_mesh\_dfd\_srv::upload](structbt__mesh__dfd__srv.md#a26e4b13a8688f26c3330a2b0948bfc8d)

struct bt\_mesh\_dfd\_srv::@070235355176037046140127151237103017237244046360 upload

[bt\_mesh\_dfd\_srv::phase](structbt__mesh__dfd__srv.md#a4a7847580637713b305918c77210e3c0)

enum bt\_mesh\_dfd\_phase phase

**Definition** dfd\_srv.h:221

[bt\_mesh\_dfd\_srv::inputs](structbt__mesh__dfd__srv.md#a4e28f0e0845d1aeb6ebc03032ecfe813)

struct bt\_mesh\_blob\_cli\_inputs inputs

**Definition** dfd\_srv.h:222

[bt\_mesh\_dfd\_srv::area](structbt__mesh__dfd__srv.md#a52b10a938105d0fb22e72e30fc92df5c)

const struct flash\_area \* area

**Definition** dfd\_srv.h:227

[bt\_mesh\_dfd\_srv::target\_cnt](structbt__mesh__dfd__srv.md#a67e4997a4367d9547a0ae9ff6c2017d6)

uint16\_t target\_cnt

**Definition** dfd\_srv.h:218

[bt\_mesh\_dfd\_srv::io](structbt__mesh__dfd__srv.md#a691eb383f51fd6e10b615ab8921005de)

const struct bt\_mesh\_blob\_io \* io

**Definition** dfd\_srv.h:217

[bt\_mesh\_dfd\_srv::cb](structbt__mesh__dfd__srv.md#a7edbfa6bedb887a941b7567b9eeac8fd)

const struct bt\_mesh\_dfd\_srv\_cb \* cb

**Definition** dfd\_srv.h:212

[bt\_mesh\_dfd\_srv::blob](structbt__mesh__dfd__srv.md#ab538079d9f6b98f0de65583d6bdfe7f0)

struct bt\_mesh\_blob\_srv blob

**Definition** dfd\_srv.h:228

[bt\_mesh\_dfd\_srv::targets](structbt__mesh__dfd__srv.md#abde92a8837d687ef213836d593bf979d)

struct bt\_mesh\_dfu\_target targets[0]

**Definition** dfd\_srv.h:215

[bt\_mesh\_dfd\_srv::apply](structbt__mesh__dfd__srv.md#af1ac88ae8d9e1e42ff8a98d3969c359d)

bool apply

**Definition** dfd\_srv.h:220

[bt\_mesh\_dfd\_srv::slot\_idx](structbt__mesh__dfd__srv.md#af61665ebb2f46bd3e6277c6ee95ff68c)

uint16\_t slot\_idx

**Definition** dfd\_srv.h:219

[bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md)

Firmware Update Client event callbacks.

**Definition** dfu\_cli.h:130

[bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md)

Firmware Update Client model instance.

**Definition** dfu\_cli.h:184

[bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md)

DFU image slot for DFU distribution.

**Definition** dfu.h:152

[bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md)

DFU Target node.

**Definition** dfu\_cli.h:54

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:809

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:887

[bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md)

Message sending context.

**Definition** msg.h:76

[flash\_area](structflash__area.md)

Flash partition.

**Definition** flash\_map.h:59

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfd\_srv.h](dfd__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
