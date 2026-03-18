---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/vcp_8h_source.html
original_path: doxygen/html/vcp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vcp.h

[Go to the documentation of this file.](vcp_8h.md)

1/\*

2 \* Copyright (c) 2020-2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VCP\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VCP\_H\_

9

21

22#include <[stdint.h](stdint_8h.md)>

23

24#include <[zephyr/bluetooth/audio/aics.h](aics_8h.md)>

25#include <[zephyr/bluetooth/audio/vocs.h](vocs_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

31#if defined(CONFIG\_BT\_VCP\_VOL\_REND)

32#define BT\_VCP\_VOL\_REND\_VOCS\_CNT CONFIG\_BT\_VCP\_VOL\_REND\_VOCS\_INSTANCE\_COUNT

33#define BT\_VCP\_VOL\_REND\_AICS\_CNT CONFIG\_BT\_VCP\_VOL\_REND\_AICS\_INSTANCE\_COUNT

34#else

[ 35](group__bt__gatt__vcp.md#gae7195f4556ad2442bc45d8d43cdeedd0)#define BT\_VCP\_VOL\_REND\_VOCS\_CNT 0

[ 36](group__bt__gatt__vcp.md#ga571d7ff5a6a507fcd7cbdfa32a04643b)#define BT\_VCP\_VOL\_REND\_AICS\_CNT 0

37#endif /\* CONFIG\_BT\_VCP\_VOL\_REND \*/

38

[ 40](group__bt__gatt__vcp.md#gabb8bdfde60f1cbb31bab41fd61b3384b)#define BT\_VCP\_ERR\_INVALID\_COUNTER 0x80

[ 41](group__bt__gatt__vcp.md#gad979c43e4d84f52009d9931fb74628e6)#define BT\_VCP\_ERR\_OP\_NOT\_SUPPORTED 0x81

42

[ 44](group__bt__gatt__vcp.md#ga4660f938a16113f715dd8aec3ed3baf6)#define BT\_VCP\_STATE\_UNMUTED 0x00

[ 45](group__bt__gatt__vcp.md#ga3d6ffdfb9e0d8d58073f4a130a8020b0)#define BT\_VCP\_STATE\_MUTED 0x01

46

48struct bt\_vcp\_vol\_ctlr;

49

[ 51](structbt__vcp__vol__rend__register__param.md)struct [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md) {

[ 53](structbt__vcp__vol__rend__register__param.md#a098e6c6921813b3f0dc7512cd483c829) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [step](structbt__vcp__vol__rend__register__param.md#a098e6c6921813b3f0dc7512cd483c829);

54

[ 56](structbt__vcp__vol__rend__register__param.md#a93f2b246ac4241db468a46a64909866e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](structbt__vcp__vol__rend__register__param.md#a93f2b246ac4241db468a46a64909866e);

57

[ 59](structbt__vcp__vol__rend__register__param.md#a6cf1343a2b3033c3f4676d66017cfda7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [volume](structbt__vcp__vol__rend__register__param.md#a6cf1343a2b3033c3f4676d66017cfda7);

60

[ 62](structbt__vcp__vol__rend__register__param.md#a45eb75a4590d278cec0cf4cf6d94dda3) struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) [vocs\_param](structbt__vcp__vol__rend__register__param.md#a45eb75a4590d278cec0cf4cf6d94dda3)[[BT\_VCP\_VOL\_REND\_VOCS\_CNT](group__bt__gatt__vcp.md#gae7195f4556ad2442bc45d8d43cdeedd0)];

63

[ 65](structbt__vcp__vol__rend__register__param.md#a1e3a4744de697d92d0fc8b9e27593417) struct [bt\_aics\_register\_param](structbt__aics__register__param.md) [aics\_param](structbt__vcp__vol__rend__register__param.md#a1e3a4744de697d92d0fc8b9e27593417)[[BT\_VCP\_VOL\_REND\_AICS\_CNT](group__bt__gatt__vcp.md#ga571d7ff5a6a507fcd7cbdfa32a04643b)];

66

[ 68](structbt__vcp__vol__rend__register__param.md#af9a09c453394fd4a28d6415e2775c3f5) struct [bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md) \*[cb](structbt__vcp__vol__rend__register__param.md#af9a09c453394fd4a28d6415e2775c3f5);

69};

70

[ 78](structbt__vcp__included.md)struct [bt\_vcp\_included](structbt__vcp__included.md) {

[ 80](structbt__vcp__included.md#acb0c8e853808adfd9c3b92b45e874103) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vocs\_cnt](structbt__vcp__included.md#acb0c8e853808adfd9c3b92b45e874103);

[ 82](structbt__vcp__included.md#a1f04068dd88d2fecef5fd78a3c7d4429) struct bt\_vocs \*\*[vocs](structbt__vcp__included.md#a1f04068dd88d2fecef5fd78a3c7d4429);

83

[ 85](structbt__vcp__included.md#af521bb12ebef4c5f60609040140474c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [aics\_cnt](structbt__vcp__included.md#af521bb12ebef4c5f60609040140474c0);

[ 87](structbt__vcp__included.md#aa6c87b8c9b4b2be6ec6429fd2ee68398) struct bt\_aics \*\*[aics](structbt__vcp__included.md#aa6c87b8c9b4b2be6ec6429fd2ee68398);

88};

89

[ 102](group__bt__gatt__vcp.md#ga1761d6618c48983e034cee5574c9c34f)int [bt\_vcp\_vol\_rend\_included\_get](group__bt__gatt__vcp.md#ga1761d6618c48983e034cee5574c9c34f)(struct [bt\_vcp\_included](structbt__vcp__included.md) \*included);

103

[ 114](group__bt__gatt__vcp.md#ga752d8ff54a4b8c8c854a9c693617e64d)int [bt\_vcp\_vol\_rend\_register](group__bt__gatt__vcp.md#ga752d8ff54a4b8c8c854a9c693617e64d)(struct [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md) \*param);

115

[ 116](structbt__vcp__vol__rend__cb.md)struct [bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md) {

[ 129](structbt__vcp__vol__rend__cb.md#a45af48fd29d8c6ca48a1948f5cc9c7ac) void (\*[state](structbt__vcp__vol__rend__cb.md#a45af48fd29d8c6ca48a1948f5cc9c7ac))(int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute);

130

[ 142](structbt__vcp__vol__rend__cb.md#a3c73bb3d09405be64e0a1539306d1e95) void (\*[flags](structbt__vcp__vol__rend__cb.md#a3c73bb3d09405be64e0a1539306d1e95))(int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__vcp__vol__rend__cb.md#a3c73bb3d09405be64e0a1539306d1e95));

143};

144

[ 157](group__bt__gatt__vcp.md#ga56e0f99d2688fb6f9e0e4d9103de706c)int [bt\_vcp\_vol\_rend\_set\_step](group__bt__gatt__vcp.md#ga56e0f99d2688fb6f9e0e4d9103de706c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume\_step);

158

[ 164](group__bt__gatt__vcp.md#ga9d1ac028abc88549ea18b6a0c585c781)int [bt\_vcp\_vol\_rend\_get\_state](group__bt__gatt__vcp.md#ga9d1ac028abc88549ea18b6a0c585c781)(void);

165

[ 171](group__bt__gatt__vcp.md#ga1e6c9cfa0d012a4b701c99d8e6b5985d)int [bt\_vcp\_vol\_rend\_get\_flags](group__bt__gatt__vcp.md#ga1e6c9cfa0d012a4b701c99d8e6b5985d)(void);

172

[ 178](group__bt__gatt__vcp.md#gaf3c622f151a21d1dd617e97917c5ff5e)int [bt\_vcp\_vol\_rend\_vol\_down](group__bt__gatt__vcp.md#gaf3c622f151a21d1dd617e97917c5ff5e)(void);

179

[ 185](group__bt__gatt__vcp.md#ga6c10dd5a029b524994739f0b37a82c84)int [bt\_vcp\_vol\_rend\_vol\_up](group__bt__gatt__vcp.md#ga6c10dd5a029b524994739f0b37a82c84)(void);

186

[ 192](group__bt__gatt__vcp.md#ga3e6236a8679f95ba512181284a05923d)int [bt\_vcp\_vol\_rend\_unmute\_vol\_down](group__bt__gatt__vcp.md#ga3e6236a8679f95ba512181284a05923d)(void);

193

[ 199](group__bt__gatt__vcp.md#gadf77729fee34f6605101c278fd2b7c46)int [bt\_vcp\_vol\_rend\_unmute\_vol\_up](group__bt__gatt__vcp.md#gadf77729fee34f6605101c278fd2b7c46)(void);

200

[ 208](group__bt__gatt__vcp.md#ga61279baeba11152625cd3a87c5d973c9)int [bt\_vcp\_vol\_rend\_set\_vol](group__bt__gatt__vcp.md#ga61279baeba11152625cd3a87c5d973c9)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume);

209

[ 215](group__bt__gatt__vcp.md#ga303d4b6b77987ab41cb1753ef861dd6c)int [bt\_vcp\_vol\_rend\_unmute](group__bt__gatt__vcp.md#ga303d4b6b77987ab41cb1753ef861dd6c)(void);

216

[ 222](group__bt__gatt__vcp.md#ga0c6d0b6b015f069a9adc1332a32c79f9)int [bt\_vcp\_vol\_rend\_mute](group__bt__gatt__vcp.md#ga0c6d0b6b015f069a9adc1332a32c79f9)(void);

223

[ 224](structbt__vcp__vol__ctlr__cb.md)struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) {

[ 238](structbt__vcp__vol__ctlr__cb.md#ac3b89f35b79d35384f9ead31cf15ac4e) void (\*[state](structbt__vcp__vol__ctlr__cb.md#ac3b89f35b79d35384f9ead31cf15ac4e))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume,

239 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](structbt__vcp__vol__ctlr__cb.md#aa2cd77992831eef7e59d3e4a01a0e542));

240

255

[ 256](structbt__vcp__vol__ctlr__cb.md#a4df90987abe0e53894e4064b3487c2bb) void (\*[flags](structbt__vcp__vol__ctlr__cb.md#a4df90987abe0e53894e4064b3487c2bb))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__vcp__vol__ctlr__cb.md#a4df90987abe0e53894e4064b3487c2bb));

257

[ 271](structbt__vcp__vol__ctlr__cb.md#ada8fe8d838d6d2c983d746e7e7ed1171) void (\*[discover](structbt__vcp__vol__ctlr__cb.md#ada8fe8d838d6d2c983d746e7e7ed1171))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vocs\_count,

272 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aics\_count);

273

[ 283](structbt__vcp__vol__ctlr__cb.md#ac986e0c5cb49395fe8581f5b1dae1a88) void (\*[vol\_down](structbt__vcp__vol__ctlr__cb.md#ac986e0c5cb49395fe8581f5b1dae1a88))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

284

[ 294](structbt__vcp__vol__ctlr__cb.md#ae1beaa5d0a61c630fa90b4a5236ce743) void (\*[vol\_up](structbt__vcp__vol__ctlr__cb.md#ae1beaa5d0a61c630fa90b4a5236ce743))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

295

[ 305](structbt__vcp__vol__ctlr__cb.md#aa2cd77992831eef7e59d3e4a01a0e542) void (\*[mute](structbt__vcp__vol__ctlr__cb.md#aa2cd77992831eef7e59d3e4a01a0e542))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

306

[ 316](structbt__vcp__vol__ctlr__cb.md#a6a217e0d8cbcc56e5128d5b7acdaac6d) void (\*[unmute](structbt__vcp__vol__ctlr__cb.md#a6a217e0d8cbcc56e5128d5b7acdaac6d))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

317

[ 327](structbt__vcp__vol__ctlr__cb.md#a770e300127b8357f1e76f0cca21b74e5) void (\*[vol\_down\_unmute](structbt__vcp__vol__ctlr__cb.md#a770e300127b8357f1e76f0cca21b74e5))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

328

[ 338](structbt__vcp__vol__ctlr__cb.md#af4ca636d19c83694f9b86102404b0538) void (\*[vol\_up\_unmute](structbt__vcp__vol__ctlr__cb.md#af4ca636d19c83694f9b86102404b0538))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

339

[ 349](structbt__vcp__vol__ctlr__cb.md#abe7cf51858428db6b953a21a6ba40f83) void (\*[vol\_set](structbt__vcp__vol__ctlr__cb.md#abe7cf51858428db6b953a21a6ba40f83))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

350

351 /\* Volume Offset Control Service callbacks \*/

[ 352](structbt__vcp__vol__ctlr__cb.md#af6407bb0652539608f0100f02cfaadd1) struct [bt\_vocs\_cb](structbt__vocs__cb.md) [vocs\_cb](structbt__vcp__vol__ctlr__cb.md#af6407bb0652539608f0100f02cfaadd1);

353

354 /\* Audio Input Control Service callbacks \*/

[ 355](structbt__vcp__vol__ctlr__cb.md#a430b1ee27c9bf7d6c7f8498748d91b21) struct [bt\_aics\_cb](structbt__aics__cb.md) [aics\_cb](structbt__vcp__vol__ctlr__cb.md#a430b1ee27c9bf7d6c7f8498748d91b21);

356

358 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

359};

360

[ 370](group__bt__gatt__vcp.md#ga7861d0c3426870c015106e8e170004a3)int [bt\_vcp\_vol\_ctlr\_cb\_register](group__bt__gatt__vcp.md#ga7861d0c3426870c015106e8e170004a3)(struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \*cb);

371

[ 381](group__bt__gatt__vcp.md#gae69e4730df4341bbb9bbbba1bea14005)int [bt\_vcp\_vol\_ctlr\_cb\_unregister](group__bt__gatt__vcp.md#gae69e4730df4341bbb9bbbba1bea14005)(struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \*cb);

382

[ 399](group__bt__gatt__vcp.md#gac18d43a0785155c1131249f95554f2de)int [bt\_vcp\_vol\_ctlr\_discover](group__bt__gatt__vcp.md#gac18d43a0785155c1131249f95554f2de)(struct bt\_conn \*conn,

400 struct bt\_vcp\_vol\_ctlr \*\*vol\_ctlr);

401

[ 414](group__bt__gatt__vcp.md#ga0c8faa95cc36950c70ff572c931eedee)struct bt\_vcp\_vol\_ctlr \*[bt\_vcp\_vol\_ctlr\_get\_by\_conn](group__bt__gatt__vcp.md#ga0c8faa95cc36950c70ff572c931eedee)(const struct bt\_conn \*conn);

415

[ 427](group__bt__gatt__vcp.md#gab287197243191e3dbf162c6d16b6d726)int [bt\_vcp\_vol\_ctlr\_conn\_get](group__bt__gatt__vcp.md#gab287197243191e3dbf162c6d16b6d726)(const struct bt\_vcp\_vol\_ctlr \*vol\_ctlr,

428 struct bt\_conn \*\*conn);

429

[ 446](group__bt__gatt__vcp.md#gaaa748c49e103ff161f67df9663ea6330)int [bt\_vcp\_vol\_ctlr\_included\_get](group__bt__gatt__vcp.md#gaaa748c49e103ff161f67df9663ea6330)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr,

447 struct [bt\_vcp\_included](structbt__vcp__included.md) \*included);

448

[ 456](group__bt__gatt__vcp.md#ga68cab2f59c63542b6a7da33d555da0ab)int [bt\_vcp\_vol\_ctlr\_read\_state](group__bt__gatt__vcp.md#ga68cab2f59c63542b6a7da33d555da0ab)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

457

[ 465](group__bt__gatt__vcp.md#gaefc226a5abb6bb1540d4b44ac4ddc236)int [bt\_vcp\_vol\_ctlr\_read\_flags](group__bt__gatt__vcp.md#gaefc226a5abb6bb1540d4b44ac4ddc236)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

466

[ 474](group__bt__gatt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4)int [bt\_vcp\_vol\_ctlr\_vol\_down](group__bt__gatt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

475

[ 483](group__bt__gatt__vcp.md#ga908eb20727e1d68ed569badfd13ff896)int [bt\_vcp\_vol\_ctlr\_vol\_up](group__bt__gatt__vcp.md#ga908eb20727e1d68ed569badfd13ff896)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

484

[ 492](group__bt__gatt__vcp.md#ga20348b220988c700cabf356f7165d4d6)int [bt\_vcp\_vol\_ctlr\_unmute\_vol\_down](group__bt__gatt__vcp.md#ga20348b220988c700cabf356f7165d4d6)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

493

[ 501](group__bt__gatt__vcp.md#ga2defdeee7486eee22a3416db8aa7c251)int [bt\_vcp\_vol\_ctlr\_unmute\_vol\_up](group__bt__gatt__vcp.md#ga2defdeee7486eee22a3416db8aa7c251)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

502

[ 511](group__bt__gatt__vcp.md#gaaa5b5cd9a11c0e1fcdabce690ba20616)int [bt\_vcp\_vol\_ctlr\_set\_vol](group__bt__gatt__vcp.md#gaaa5b5cd9a11c0e1fcdabce690ba20616)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume);

512

[ 520](group__bt__gatt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36)int [bt\_vcp\_vol\_ctlr\_unmute](group__bt__gatt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

521

[ 529](group__bt__gatt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867)int [bt\_vcp\_vol\_ctlr\_mute](group__bt__gatt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

530

531#ifdef \_\_cplusplus

532}

533#endif

534

538

539#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VCP\_H\_ \*/

[aics.h](aics_8h.md)

[bt\_vcp\_vol\_ctlr\_vol\_down](group__bt__gatt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4)

int bt\_vcp\_vol\_ctlr\_vol\_down(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Turn the volume down one step on a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_mute](group__bt__gatt__vcp.md#ga0c6d0b6b015f069a9adc1332a32c79f9)

int bt\_vcp\_vol\_rend\_mute(void)

Mute the server.

[bt\_vcp\_vol\_ctlr\_get\_by\_conn](group__bt__gatt__vcp.md#ga0c8faa95cc36950c70ff572c931eedee)

struct bt\_vcp\_vol\_ctlr \* bt\_vcp\_vol\_ctlr\_get\_by\_conn(const struct bt\_conn \*conn)

Get the volume controller from a connection pointer.

[bt\_vcp\_vol\_ctlr\_mute](group__bt__gatt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867)

int bt\_vcp\_vol\_ctlr\_mute(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Mute a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_included\_get](group__bt__gatt__vcp.md#ga1761d6618c48983e034cee5574c9c34f)

int bt\_vcp\_vol\_rend\_included\_get(struct bt\_vcp\_included \*included)

Get Volume Control Service included services.

[bt\_vcp\_vol\_rend\_get\_flags](group__bt__gatt__vcp.md#ga1e6c9cfa0d012a4b701c99d8e6b5985d)

int bt\_vcp\_vol\_rend\_get\_flags(void)

Get the Volume Control Service flags.

[bt\_vcp\_vol\_ctlr\_unmute\_vol\_down](group__bt__gatt__vcp.md#ga20348b220988c700cabf356f7165d4d6)

int bt\_vcp\_vol\_ctlr\_unmute\_vol\_down(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Turn the volume down one step and unmute on a remote Volume Renderer.

[bt\_vcp\_vol\_ctlr\_unmute\_vol\_up](group__bt__gatt__vcp.md#ga2defdeee7486eee22a3416db8aa7c251)

int bt\_vcp\_vol\_ctlr\_unmute\_vol\_up(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Turn the volume up one step and unmute on a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_unmute](group__bt__gatt__vcp.md#ga303d4b6b77987ab41cb1753ef861dd6c)

int bt\_vcp\_vol\_rend\_unmute(void)

Unmute the server.

[bt\_vcp\_vol\_rend\_unmute\_vol\_down](group__bt__gatt__vcp.md#ga3e6236a8679f95ba512181284a05923d)

int bt\_vcp\_vol\_rend\_unmute\_vol\_down(void)

Turn the volume down and unmute the server.

[bt\_vcp\_vol\_ctlr\_unmute](group__bt__gatt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36)

int bt\_vcp\_vol\_ctlr\_unmute(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Unmute a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_set\_step](group__bt__gatt__vcp.md#ga56e0f99d2688fb6f9e0e4d9103de706c)

int bt\_vcp\_vol\_rend\_set\_step(uint8\_t volume\_step)

Set the Volume Control Service volume step size.

[BT\_VCP\_VOL\_REND\_AICS\_CNT](group__bt__gatt__vcp.md#ga571d7ff5a6a507fcd7cbdfa32a04643b)

#define BT\_VCP\_VOL\_REND\_AICS\_CNT

**Definition** vcp.h:36

[bt\_vcp\_vol\_rend\_set\_vol](group__bt__gatt__vcp.md#ga61279baeba11152625cd3a87c5d973c9)

int bt\_vcp\_vol\_rend\_set\_vol(uint8\_t volume)

Set the volume on the server.

[bt\_vcp\_vol\_ctlr\_read\_state](group__bt__gatt__vcp.md#ga68cab2f59c63542b6a7da33d555da0ab)

int bt\_vcp\_vol\_ctlr\_read\_state(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Read the volume state of a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_vol\_up](group__bt__gatt__vcp.md#ga6c10dd5a029b524994739f0b37a82c84)

int bt\_vcp\_vol\_rend\_vol\_up(void)

Turn the volume up by one step on the server.

[bt\_vcp\_vol\_rend\_register](group__bt__gatt__vcp.md#ga752d8ff54a4b8c8c854a9c693617e64d)

int bt\_vcp\_vol\_rend\_register(struct bt\_vcp\_vol\_rend\_register\_param \*param)

Register the Volume Control Service.

[bt\_vcp\_vol\_ctlr\_cb\_register](group__bt__gatt__vcp.md#ga7861d0c3426870c015106e8e170004a3)

int bt\_vcp\_vol\_ctlr\_cb\_register(struct bt\_vcp\_vol\_ctlr\_cb \*cb)

Registers the callbacks used by the Volume Controller.

[bt\_vcp\_vol\_ctlr\_vol\_up](group__bt__gatt__vcp.md#ga908eb20727e1d68ed569badfd13ff896)

int bt\_vcp\_vol\_ctlr\_vol\_up(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Turn the volume up one step on a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_get\_state](group__bt__gatt__vcp.md#ga9d1ac028abc88549ea18b6a0c585c781)

int bt\_vcp\_vol\_rend\_get\_state(void)

Get the Volume Control Service volume state.

[bt\_vcp\_vol\_ctlr\_set\_vol](group__bt__gatt__vcp.md#gaaa5b5cd9a11c0e1fcdabce690ba20616)

int bt\_vcp\_vol\_ctlr\_set\_vol(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, uint8\_t volume)

Set the absolute volume on a remote Volume Renderer.

[bt\_vcp\_vol\_ctlr\_included\_get](group__bt__gatt__vcp.md#gaaa748c49e103ff161f67df9663ea6330)

int bt\_vcp\_vol\_ctlr\_included\_get(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct bt\_vcp\_included \*included)

Get Volume Control Service included services.

[bt\_vcp\_vol\_ctlr\_conn\_get](group__bt__gatt__vcp.md#gab287197243191e3dbf162c6d16b6d726)

int bt\_vcp\_vol\_ctlr\_conn\_get(const struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct bt\_conn \*\*conn)

Get the connection pointer of a client instance.

[bt\_vcp\_vol\_ctlr\_discover](group__bt__gatt__vcp.md#gac18d43a0785155c1131249f95554f2de)

int bt\_vcp\_vol\_ctlr\_discover(struct bt\_conn \*conn, struct bt\_vcp\_vol\_ctlr \*\*vol\_ctlr)

Discover Volume Control Service and included services.

[bt\_vcp\_vol\_rend\_unmute\_vol\_up](group__bt__gatt__vcp.md#gadf77729fee34f6605101c278fd2b7c46)

int bt\_vcp\_vol\_rend\_unmute\_vol\_up(void)

Turn the volume up and unmute the server.

[bt\_vcp\_vol\_ctlr\_cb\_unregister](group__bt__gatt__vcp.md#gae69e4730df4341bbb9bbbba1bea14005)

int bt\_vcp\_vol\_ctlr\_cb\_unregister(struct bt\_vcp\_vol\_ctlr\_cb \*cb)

Unregisters the callbacks used by the Volume Controller.

[BT\_VCP\_VOL\_REND\_VOCS\_CNT](group__bt__gatt__vcp.md#gae7195f4556ad2442bc45d8d43cdeedd0)

#define BT\_VCP\_VOL\_REND\_VOCS\_CNT

**Definition** vcp.h:35

[bt\_vcp\_vol\_ctlr\_read\_flags](group__bt__gatt__vcp.md#gaefc226a5abb6bb1540d4b44ac4ddc236)

int bt\_vcp\_vol\_ctlr\_read\_flags(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Read the volume flags of a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_vol\_down](group__bt__gatt__vcp.md#gaf3c622f151a21d1dd617e97917c5ff5e)

int bt\_vcp\_vol\_rend\_vol\_down(void)

Turn the volume down by one step on the server.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_aics\_cb](structbt__aics__cb.md)

**Definition** aics.h:254

[bt\_aics\_register\_param](structbt__aics__register__param.md)

Structure for initializing a Audio Input Control Service instance.

**Definition** aics.h:66

[bt\_vcp\_included](structbt__vcp__included.md)

Volume Control Service included services.

**Definition** vcp.h:78

[bt\_vcp\_included::vocs](structbt__vcp__included.md#a1f04068dd88d2fecef5fd78a3c7d4429)

struct bt\_vocs \*\* vocs

Array of pointers to Volume Offset Control Service instances.

**Definition** vcp.h:82

[bt\_vcp\_included::aics](structbt__vcp__included.md#aa6c87b8c9b4b2be6ec6429fd2ee68398)

struct bt\_aics \*\* aics

Array of pointers to Audio Input Control Service instances.

**Definition** vcp.h:87

[bt\_vcp\_included::vocs\_cnt](structbt__vcp__included.md#acb0c8e853808adfd9c3b92b45e874103)

uint8\_t vocs\_cnt

Number of Volume Offset Control Service instances.

**Definition** vcp.h:80

[bt\_vcp\_included::aics\_cnt](structbt__vcp__included.md#af521bb12ebef4c5f60609040140474c0)

uint8\_t aics\_cnt

Number of Audio Input Control Service instances.

**Definition** vcp.h:85

[bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md)

**Definition** vcp.h:224

[bt\_vcp\_vol\_ctlr\_cb::aics\_cb](structbt__vcp__vol__ctlr__cb.md#a430b1ee27c9bf7d6c7f8498748d91b21)

struct bt\_aics\_cb aics\_cb

**Definition** vcp.h:355

[bt\_vcp\_vol\_ctlr\_cb::flags](structbt__vcp__vol__ctlr__cb.md#a4df90987abe0e53894e4064b3487c2bb)

void(\* flags)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t flags)

Callback function for Volume Control Profile volume flags.

**Definition** vcp.h:256

[bt\_vcp\_vol\_ctlr\_cb::unmute](structbt__vcp__vol__ctlr__cb.md#a6a217e0d8cbcc56e5128d5b7acdaac6d)

void(\* unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_unmute().

**Definition** vcp.h:316

[bt\_vcp\_vol\_ctlr\_cb::vol\_down\_unmute](structbt__vcp__vol__ctlr__cb.md#a770e300127b8357f1e76f0cca21b74e5)

void(\* vol\_down\_unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_down\_unmute().

**Definition** vcp.h:327

[bt\_vcp\_vol\_ctlr\_cb::mute](structbt__vcp__vol__ctlr__cb.md#aa2cd77992831eef7e59d3e4a01a0e542)

void(\* mute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_mute().

**Definition** vcp.h:305

[bt\_vcp\_vol\_ctlr\_cb::vol\_set](structbt__vcp__vol__ctlr__cb.md#abe7cf51858428db6b953a21a6ba40f83)

void(\* vol\_set)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_set().

**Definition** vcp.h:349

[bt\_vcp\_vol\_ctlr\_cb::state](structbt__vcp__vol__ctlr__cb.md#ac3b89f35b79d35384f9ead31cf15ac4e)

void(\* state)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t volume, uint8\_t mute)

Callback function for Volume Control Profile volume state.

**Definition** vcp.h:238

[bt\_vcp\_vol\_ctlr\_cb::vol\_down](structbt__vcp__vol__ctlr__cb.md#ac986e0c5cb49395fe8581f5b1dae1a88)

void(\* vol\_down)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_down().

**Definition** vcp.h:283

[bt\_vcp\_vol\_ctlr\_cb::discover](structbt__vcp__vol__ctlr__cb.md#ada8fe8d838d6d2c983d746e7e7ed1171)

void(\* discover)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t vocs\_count, uint8\_t aics\_count)

Callback function for bt\_vcp\_vol\_ctlr\_discover().

**Definition** vcp.h:271

[bt\_vcp\_vol\_ctlr\_cb::vol\_up](structbt__vcp__vol__ctlr__cb.md#ae1beaa5d0a61c630fa90b4a5236ce743)

void(\* vol\_up)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_up().

**Definition** vcp.h:294

[bt\_vcp\_vol\_ctlr\_cb::vol\_up\_unmute](structbt__vcp__vol__ctlr__cb.md#af4ca636d19c83694f9b86102404b0538)

void(\* vol\_up\_unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_up\_unmute().

**Definition** vcp.h:338

[bt\_vcp\_vol\_ctlr\_cb::vocs\_cb](structbt__vcp__vol__ctlr__cb.md#af6407bb0652539608f0100f02cfaadd1)

struct bt\_vocs\_cb vocs\_cb

**Definition** vcp.h:352

[bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md)

**Definition** vcp.h:116

[bt\_vcp\_vol\_rend\_cb::flags](structbt__vcp__vol__rend__cb.md#a3c73bb3d09405be64e0a1539306d1e95)

void(\* flags)(int err, uint8\_t flags)

Callback function for Volume Control Service flags.

**Definition** vcp.h:142

[bt\_vcp\_vol\_rend\_cb::state](structbt__vcp__vol__rend__cb.md#a45af48fd29d8c6ca48a1948f5cc9c7ac)

void(\* state)(int err, uint8\_t volume, uint8\_t mute)

Callback function for Volume Control Service volume state.

**Definition** vcp.h:129

[bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md)

Register structure for Volume Control Service.

**Definition** vcp.h:51

[bt\_vcp\_vol\_rend\_register\_param::step](structbt__vcp__vol__rend__register__param.md#a098e6c6921813b3f0dc7512cd483c829)

uint8\_t step

Initial step size (1-255).

**Definition** vcp.h:53

[bt\_vcp\_vol\_rend\_register\_param::aics\_param](structbt__vcp__vol__rend__register__param.md#a1e3a4744de697d92d0fc8b9e27593417)

struct bt\_aics\_register\_param aics\_param[0]

Register parameters for Audio Input Control Services.

**Definition** vcp.h:65

[bt\_vcp\_vol\_rend\_register\_param::vocs\_param](structbt__vcp__vol__rend__register__param.md#a45eb75a4590d278cec0cf4cf6d94dda3)

struct bt\_vocs\_register\_param vocs\_param[0]

Register parameters for Volume Offset Control Services.

**Definition** vcp.h:62

[bt\_vcp\_vol\_rend\_register\_param::volume](structbt__vcp__vol__rend__register__param.md#a6cf1343a2b3033c3f4676d66017cfda7)

uint8\_t volume

Initial volume level (0-255).

**Definition** vcp.h:59

[bt\_vcp\_vol\_rend\_register\_param::mute](structbt__vcp__vol__rend__register__param.md#a93f2b246ac4241db468a46a64909866e)

uint8\_t mute

Initial mute state (0-1).

**Definition** vcp.h:56

[bt\_vcp\_vol\_rend\_register\_param::cb](structbt__vcp__vol__rend__register__param.md#af9a09c453394fd4a28d6415e2775c3f5)

struct bt\_vcp\_vol\_rend\_cb \* cb

Volume Control Service callback structure.

**Definition** vcp.h:68

[bt\_vocs\_cb](structbt__vocs__cb.md)

**Definition** vocs.h:192

[bt\_vocs\_register\_param](structbt__vocs__register__param.md)

Structure for registering a Volume Offset Control Service instance.

**Definition** vocs.h:50

[vocs.h](vocs_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [vcp.h](vcp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
