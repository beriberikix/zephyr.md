---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/vcp_8h_source.html
original_path: doxygen/html/vcp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vcp.h

[Go to the documentation of this file.](vcp_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020-2024 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VCP\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VCP\_H\_

14

29

30#include <[stdint.h](stdint_8h.md)>

31

32#include <[zephyr/bluetooth/audio/aics.h](aics_8h.md)>

33#include <[zephyr/bluetooth/audio/vocs.h](vocs_8h.md)>

34#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

35#include <[zephyr/sys/slist.h](slist_8h.md)>

36

37#ifdef \_\_cplusplus

38extern "C" {

39#endif

40

45#if defined(CONFIG\_BT\_VCP\_VOL\_REND)

46#define BT\_VCP\_VOL\_REND\_VOCS\_CNT CONFIG\_BT\_VCP\_VOL\_REND\_VOCS\_INSTANCE\_COUNT

47#else

[ 48](group__bt__vcp.md#gae7195f4556ad2442bc45d8d43cdeedd0)#define BT\_VCP\_VOL\_REND\_VOCS\_CNT 0

49#endif /\* CONFIG\_BT\_VCP\_VOL\_REND \*/

50

55#if defined(CONFIG\_BT\_VCP\_VOL\_REND)

56#define BT\_VCP\_VOL\_REND\_AICS\_CNT CONFIG\_BT\_VCP\_VOL\_REND\_AICS\_INSTANCE\_COUNT

57#else

[ 58](group__bt__vcp.md#ga571d7ff5a6a507fcd7cbdfa32a04643b)#define BT\_VCP\_VOL\_REND\_AICS\_CNT 0

59#endif /\* CONFIG\_BT\_VCP\_VOL\_REND \*/

60

[ 69](group__bt__vcp.md#gabb8bdfde60f1cbb31bab41fd61b3384b)#define BT\_VCP\_ERR\_INVALID\_COUNTER 0x80

[ 71](group__bt__vcp.md#gad979c43e4d84f52009d9931fb74628e6)#define BT\_VCP\_ERR\_OP\_NOT\_SUPPORTED 0x81

73

[ 79](group__bt__vcp.md#ga4660f938a16113f715dd8aec3ed3baf6)#define BT\_VCP\_STATE\_UNMUTED 0x00

[ 81](group__bt__vcp.md#ga3d6ffdfb9e0d8d58073f4a130a8020b0)#define BT\_VCP\_STATE\_MUTED 0x01

83

85struct bt\_vcp\_vol\_ctlr;

86

[ 88](structbt__vcp__vol__rend__register__param.md)struct [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md) {

[ 90](structbt__vcp__vol__rend__register__param.md#a098e6c6921813b3f0dc7512cd483c829) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [step](structbt__vcp__vol__rend__register__param.md#a098e6c6921813b3f0dc7512cd483c829);

91

[ 93](structbt__vcp__vol__rend__register__param.md#a93f2b246ac4241db468a46a64909866e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](structbt__vcp__vol__rend__register__param.md#a93f2b246ac4241db468a46a64909866e);

94

[ 96](structbt__vcp__vol__rend__register__param.md#a6cf1343a2b3033c3f4676d66017cfda7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [volume](structbt__vcp__vol__rend__register__param.md#a6cf1343a2b3033c3f4676d66017cfda7);

97

[ 99](structbt__vcp__vol__rend__register__param.md#a45eb75a4590d278cec0cf4cf6d94dda3) struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) [vocs\_param](structbt__vcp__vol__rend__register__param.md#a45eb75a4590d278cec0cf4cf6d94dda3)[[BT\_VCP\_VOL\_REND\_VOCS\_CNT](group__bt__vcp.md#gae7195f4556ad2442bc45d8d43cdeedd0)];

100

[ 102](structbt__vcp__vol__rend__register__param.md#a1e3a4744de697d92d0fc8b9e27593417) struct [bt\_aics\_register\_param](structbt__aics__register__param.md) [aics\_param](structbt__vcp__vol__rend__register__param.md#a1e3a4744de697d92d0fc8b9e27593417)[[BT\_VCP\_VOL\_REND\_AICS\_CNT](group__bt__vcp.md#ga571d7ff5a6a507fcd7cbdfa32a04643b)];

103

[ 105](structbt__vcp__vol__rend__register__param.md#af9a09c453394fd4a28d6415e2775c3f5) struct [bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md) \*[cb](structbt__vcp__vol__rend__register__param.md#af9a09c453394fd4a28d6415e2775c3f5);

106};

107

[ 115](structbt__vcp__included.md)struct [bt\_vcp\_included](structbt__vcp__included.md) {

[ 117](structbt__vcp__included.md#acb0c8e853808adfd9c3b92b45e874103) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vocs\_cnt](structbt__vcp__included.md#acb0c8e853808adfd9c3b92b45e874103);

[ 119](structbt__vcp__included.md#a1f04068dd88d2fecef5fd78a3c7d4429) struct bt\_vocs \*\*[vocs](structbt__vcp__included.md#a1f04068dd88d2fecef5fd78a3c7d4429);

120

[ 122](structbt__vcp__included.md#af521bb12ebef4c5f60609040140474c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [aics\_cnt](structbt__vcp__included.md#af521bb12ebef4c5f60609040140474c0);

[ 124](structbt__vcp__included.md#aa6c87b8c9b4b2be6ec6429fd2ee68398) struct bt\_aics \*\*[aics](structbt__vcp__included.md#aa6c87b8c9b4b2be6ec6429fd2ee68398);

125};

126

[ 139](group__bt__vcp.md#ga1761d6618c48983e034cee5574c9c34f)int [bt\_vcp\_vol\_rend\_included\_get](group__bt__vcp.md#ga1761d6618c48983e034cee5574c9c34f)(struct [bt\_vcp\_included](structbt__vcp__included.md) \*included);

140

[ 151](group__bt__vcp.md#ga752d8ff54a4b8c8c854a9c693617e64d)int [bt\_vcp\_vol\_rend\_register](group__bt__vcp.md#ga752d8ff54a4b8c8c854a9c693617e64d)(struct [bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md) \*param);

152

[ 158](structbt__vcp__vol__rend__cb.md)struct [bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md) {

[ 173](structbt__vcp__vol__rend__cb.md#a05f84d8a2deedbc426ef22b89c87bd40) void (\*[state](structbt__vcp__vol__rend__cb.md#a05f84d8a2deedbc426ef22b89c87bd40))(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute);

174

[ 188](structbt__vcp__vol__rend__cb.md#a3413d33fa8c3362ded6ec81533c27c86) void (\*[flags](structbt__vcp__vol__rend__cb.md#a3413d33fa8c3362ded6ec81533c27c86))(struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__vcp__vol__rend__cb.md#a3413d33fa8c3362ded6ec81533c27c86));

189};

190

[ 203](group__bt__vcp.md#ga56e0f99d2688fb6f9e0e4d9103de706c)int [bt\_vcp\_vol\_rend\_set\_step](group__bt__vcp.md#ga56e0f99d2688fb6f9e0e4d9103de706c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume\_step);

204

[ 210](group__bt__vcp.md#ga9d1ac028abc88549ea18b6a0c585c781)int [bt\_vcp\_vol\_rend\_get\_state](group__bt__vcp.md#ga9d1ac028abc88549ea18b6a0c585c781)(void);

211

[ 217](group__bt__vcp.md#ga1e6c9cfa0d012a4b701c99d8e6b5985d)int [bt\_vcp\_vol\_rend\_get\_flags](group__bt__vcp.md#ga1e6c9cfa0d012a4b701c99d8e6b5985d)(void);

218

[ 224](group__bt__vcp.md#gaf3c622f151a21d1dd617e97917c5ff5e)int [bt\_vcp\_vol\_rend\_vol\_down](group__bt__vcp.md#gaf3c622f151a21d1dd617e97917c5ff5e)(void);

225

[ 231](group__bt__vcp.md#ga6c10dd5a029b524994739f0b37a82c84)int [bt\_vcp\_vol\_rend\_vol\_up](group__bt__vcp.md#ga6c10dd5a029b524994739f0b37a82c84)(void);

232

[ 238](group__bt__vcp.md#ga3e6236a8679f95ba512181284a05923d)int [bt\_vcp\_vol\_rend\_unmute\_vol\_down](group__bt__vcp.md#ga3e6236a8679f95ba512181284a05923d)(void);

239

[ 245](group__bt__vcp.md#gadf77729fee34f6605101c278fd2b7c46)int [bt\_vcp\_vol\_rend\_unmute\_vol\_up](group__bt__vcp.md#gadf77729fee34f6605101c278fd2b7c46)(void);

246

[ 254](group__bt__vcp.md#ga61279baeba11152625cd3a87c5d973c9)int [bt\_vcp\_vol\_rend\_set\_vol](group__bt__vcp.md#ga61279baeba11152625cd3a87c5d973c9)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume);

255

[ 261](group__bt__vcp.md#ga303d4b6b77987ab41cb1753ef861dd6c)int [bt\_vcp\_vol\_rend\_unmute](group__bt__vcp.md#ga303d4b6b77987ab41cb1753ef861dd6c)(void);

262

[ 268](group__bt__vcp.md#ga0c6d0b6b015f069a9adc1332a32c79f9)int [bt\_vcp\_vol\_rend\_mute](group__bt__vcp.md#ga0c6d0b6b015f069a9adc1332a32c79f9)(void);

269

[ 275](structbt__vcp__vol__ctlr__cb.md)struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) {

[ 289](structbt__vcp__vol__ctlr__cb.md#ac3b89f35b79d35384f9ead31cf15ac4e) void (\*[state](structbt__vcp__vol__ctlr__cb.md#ac3b89f35b79d35384f9ead31cf15ac4e))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume,

290 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](structbt__vcp__vol__ctlr__cb.md#aa2cd77992831eef7e59d3e4a01a0e542));

291

306

[ 307](structbt__vcp__vol__ctlr__cb.md#a4df90987abe0e53894e4064b3487c2bb) void (\*[flags](structbt__vcp__vol__ctlr__cb.md#a4df90987abe0e53894e4064b3487c2bb))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__vcp__vol__ctlr__cb.md#a4df90987abe0e53894e4064b3487c2bb));

308

[ 322](structbt__vcp__vol__ctlr__cb.md#ada8fe8d838d6d2c983d746e7e7ed1171) void (\*[discover](structbt__vcp__vol__ctlr__cb.md#ada8fe8d838d6d2c983d746e7e7ed1171))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vocs\_count,

323 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aics\_count);

324

[ 334](structbt__vcp__vol__ctlr__cb.md#ac986e0c5cb49395fe8581f5b1dae1a88) void (\*[vol\_down](structbt__vcp__vol__ctlr__cb.md#ac986e0c5cb49395fe8581f5b1dae1a88))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

335

[ 345](structbt__vcp__vol__ctlr__cb.md#ae1beaa5d0a61c630fa90b4a5236ce743) void (\*[vol\_up](structbt__vcp__vol__ctlr__cb.md#ae1beaa5d0a61c630fa90b4a5236ce743))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

346

[ 356](structbt__vcp__vol__ctlr__cb.md#aa2cd77992831eef7e59d3e4a01a0e542) void (\*[mute](structbt__vcp__vol__ctlr__cb.md#aa2cd77992831eef7e59d3e4a01a0e542))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

357

[ 367](structbt__vcp__vol__ctlr__cb.md#a6a217e0d8cbcc56e5128d5b7acdaac6d) void (\*[unmute](structbt__vcp__vol__ctlr__cb.md#a6a217e0d8cbcc56e5128d5b7acdaac6d))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

368

[ 378](structbt__vcp__vol__ctlr__cb.md#a770e300127b8357f1e76f0cca21b74e5) void (\*[vol\_down\_unmute](structbt__vcp__vol__ctlr__cb.md#a770e300127b8357f1e76f0cca21b74e5))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

379

[ 389](structbt__vcp__vol__ctlr__cb.md#af4ca636d19c83694f9b86102404b0538) void (\*[vol\_up\_unmute](structbt__vcp__vol__ctlr__cb.md#af4ca636d19c83694f9b86102404b0538))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

390

[ 400](structbt__vcp__vol__ctlr__cb.md#abe7cf51858428db6b953a21a6ba40f83) void (\*[vol\_set](structbt__vcp__vol__ctlr__cb.md#abe7cf51858428db6b953a21a6ba40f83))(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err);

401

[ 403](structbt__vcp__vol__ctlr__cb.md#af6407bb0652539608f0100f02cfaadd1) struct [bt\_vocs\_cb](structbt__vocs__cb.md) [vocs\_cb](structbt__vcp__vol__ctlr__cb.md#af6407bb0652539608f0100f02cfaadd1);

404

[ 406](structbt__vcp__vol__ctlr__cb.md#a430b1ee27c9bf7d6c7f8498748d91b21) struct [bt\_aics\_cb](structbt__aics__cb.md) [aics\_cb](structbt__vcp__vol__ctlr__cb.md#a430b1ee27c9bf7d6c7f8498748d91b21);

407

410 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

412};

413

[ 423](group__bt__vcp.md#ga7861d0c3426870c015106e8e170004a3)int [bt\_vcp\_vol\_ctlr\_cb\_register](group__bt__vcp.md#ga7861d0c3426870c015106e8e170004a3)(struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \*cb);

424

[ 434](group__bt__vcp.md#gae69e4730df4341bbb9bbbba1bea14005)int [bt\_vcp\_vol\_ctlr\_cb\_unregister](group__bt__vcp.md#gae69e4730df4341bbb9bbbba1bea14005)(struct [bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md) \*cb);

435

[ 452](group__bt__vcp.md#gac18d43a0785155c1131249f95554f2de)int [bt\_vcp\_vol\_ctlr\_discover](group__bt__vcp.md#gac18d43a0785155c1131249f95554f2de)(struct bt\_conn \*conn,

453 struct bt\_vcp\_vol\_ctlr \*\*vol\_ctlr);

454

[ 467](group__bt__vcp.md#ga0c8faa95cc36950c70ff572c931eedee)struct bt\_vcp\_vol\_ctlr \*[bt\_vcp\_vol\_ctlr\_get\_by\_conn](group__bt__vcp.md#ga0c8faa95cc36950c70ff572c931eedee)(const struct bt\_conn \*conn);

468

[ 480](group__bt__vcp.md#gab287197243191e3dbf162c6d16b6d726)int [bt\_vcp\_vol\_ctlr\_conn\_get](group__bt__vcp.md#gab287197243191e3dbf162c6d16b6d726)(const struct bt\_vcp\_vol\_ctlr \*vol\_ctlr,

481 struct bt\_conn \*\*conn);

482

[ 499](group__bt__vcp.md#gaaa748c49e103ff161f67df9663ea6330)int [bt\_vcp\_vol\_ctlr\_included\_get](group__bt__vcp.md#gaaa748c49e103ff161f67df9663ea6330)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr,

500 struct [bt\_vcp\_included](structbt__vcp__included.md) \*included);

501

[ 509](group__bt__vcp.md#ga68cab2f59c63542b6a7da33d555da0ab)int [bt\_vcp\_vol\_ctlr\_read\_state](group__bt__vcp.md#ga68cab2f59c63542b6a7da33d555da0ab)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

510

[ 518](group__bt__vcp.md#gaefc226a5abb6bb1540d4b44ac4ddc236)int [bt\_vcp\_vol\_ctlr\_read\_flags](group__bt__vcp.md#gaefc226a5abb6bb1540d4b44ac4ddc236)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

519

[ 527](group__bt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4)int [bt\_vcp\_vol\_ctlr\_vol\_down](group__bt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

528

[ 536](group__bt__vcp.md#ga908eb20727e1d68ed569badfd13ff896)int [bt\_vcp\_vol\_ctlr\_vol\_up](group__bt__vcp.md#ga908eb20727e1d68ed569badfd13ff896)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

537

[ 545](group__bt__vcp.md#ga20348b220988c700cabf356f7165d4d6)int [bt\_vcp\_vol\_ctlr\_unmute\_vol\_down](group__bt__vcp.md#ga20348b220988c700cabf356f7165d4d6)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

546

[ 554](group__bt__vcp.md#ga2defdeee7486eee22a3416db8aa7c251)int [bt\_vcp\_vol\_ctlr\_unmute\_vol\_up](group__bt__vcp.md#ga2defdeee7486eee22a3416db8aa7c251)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

555

[ 564](group__bt__vcp.md#gaaa5b5cd9a11c0e1fcdabce690ba20616)int [bt\_vcp\_vol\_ctlr\_set\_vol](group__bt__vcp.md#gaaa5b5cd9a11c0e1fcdabce690ba20616)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) volume);

565

[ 573](group__bt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36)int [bt\_vcp\_vol\_ctlr\_unmute](group__bt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

574

[ 582](group__bt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867)int [bt\_vcp\_vol\_ctlr\_mute](group__bt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr);

583

584#ifdef \_\_cplusplus

585}

586#endif

587

591

592#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VCP\_H\_ \*/

[aics.h](aics_8h.md)

Bluetooth Audio Input Control Service APIs.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_vcp\_vol\_ctlr\_vol\_down](group__bt__vcp.md#ga03e073e29920f4a530d2f8851b4b8df4)

int bt\_vcp\_vol\_ctlr\_vol\_down(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Turn the volume down one step on a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_mute](group__bt__vcp.md#ga0c6d0b6b015f069a9adc1332a32c79f9)

int bt\_vcp\_vol\_rend\_mute(void)

Mute the server.

[bt\_vcp\_vol\_ctlr\_get\_by\_conn](group__bt__vcp.md#ga0c8faa95cc36950c70ff572c931eedee)

struct bt\_vcp\_vol\_ctlr \* bt\_vcp\_vol\_ctlr\_get\_by\_conn(const struct bt\_conn \*conn)

Get the volume controller from a connection pointer.

[bt\_vcp\_vol\_ctlr\_mute](group__bt__vcp.md#ga106b7f826adec665b4f0ac3d5e82b867)

int bt\_vcp\_vol\_ctlr\_mute(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Mute a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_included\_get](group__bt__vcp.md#ga1761d6618c48983e034cee5574c9c34f)

int bt\_vcp\_vol\_rend\_included\_get(struct bt\_vcp\_included \*included)

Get Volume Control Service included services.

[bt\_vcp\_vol\_rend\_get\_flags](group__bt__vcp.md#ga1e6c9cfa0d012a4b701c99d8e6b5985d)

int bt\_vcp\_vol\_rend\_get\_flags(void)

Get the Volume Control Service flags.

[bt\_vcp\_vol\_ctlr\_unmute\_vol\_down](group__bt__vcp.md#ga20348b220988c700cabf356f7165d4d6)

int bt\_vcp\_vol\_ctlr\_unmute\_vol\_down(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Turn the volume down one step and unmute on a remote Volume Renderer.

[bt\_vcp\_vol\_ctlr\_unmute\_vol\_up](group__bt__vcp.md#ga2defdeee7486eee22a3416db8aa7c251)

int bt\_vcp\_vol\_ctlr\_unmute\_vol\_up(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Turn the volume up one step and unmute on a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_unmute](group__bt__vcp.md#ga303d4b6b77987ab41cb1753ef861dd6c)

int bt\_vcp\_vol\_rend\_unmute(void)

Unmute the server.

[bt\_vcp\_vol\_rend\_unmute\_vol\_down](group__bt__vcp.md#ga3e6236a8679f95ba512181284a05923d)

int bt\_vcp\_vol\_rend\_unmute\_vol\_down(void)

Turn the volume down and unmute the server.

[bt\_vcp\_vol\_ctlr\_unmute](group__bt__vcp.md#ga4e95c3fb071cb94fbe75f88e96d34b36)

int bt\_vcp\_vol\_ctlr\_unmute(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Unmute a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_set\_step](group__bt__vcp.md#ga56e0f99d2688fb6f9e0e4d9103de706c)

int bt\_vcp\_vol\_rend\_set\_step(uint8\_t volume\_step)

Set the Volume Control Service volume step size.

[BT\_VCP\_VOL\_REND\_AICS\_CNT](group__bt__vcp.md#ga571d7ff5a6a507fcd7cbdfa32a04643b)

#define BT\_VCP\_VOL\_REND\_AICS\_CNT

Defines the maximum number of Audio Input Control service instances for the Volume Control Profile Vo...

**Definition** vcp.h:58

[bt\_vcp\_vol\_rend\_set\_vol](group__bt__vcp.md#ga61279baeba11152625cd3a87c5d973c9)

int bt\_vcp\_vol\_rend\_set\_vol(uint8\_t volume)

Set the volume on the server.

[bt\_vcp\_vol\_ctlr\_read\_state](group__bt__vcp.md#ga68cab2f59c63542b6a7da33d555da0ab)

int bt\_vcp\_vol\_ctlr\_read\_state(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Read the volume state of a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_vol\_up](group__bt__vcp.md#ga6c10dd5a029b524994739f0b37a82c84)

int bt\_vcp\_vol\_rend\_vol\_up(void)

Turn the volume up by one step on the server.

[bt\_vcp\_vol\_rend\_register](group__bt__vcp.md#ga752d8ff54a4b8c8c854a9c693617e64d)

int bt\_vcp\_vol\_rend\_register(struct bt\_vcp\_vol\_rend\_register\_param \*param)

Register the Volume Control Service.

[bt\_vcp\_vol\_ctlr\_cb\_register](group__bt__vcp.md#ga7861d0c3426870c015106e8e170004a3)

int bt\_vcp\_vol\_ctlr\_cb\_register(struct bt\_vcp\_vol\_ctlr\_cb \*cb)

Registers the callbacks used by the Volume Controller.

[bt\_vcp\_vol\_ctlr\_vol\_up](group__bt__vcp.md#ga908eb20727e1d68ed569badfd13ff896)

int bt\_vcp\_vol\_ctlr\_vol\_up(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Turn the volume up one step on a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_get\_state](group__bt__vcp.md#ga9d1ac028abc88549ea18b6a0c585c781)

int bt\_vcp\_vol\_rend\_get\_state(void)

Get the Volume Control Service volume state.

[bt\_vcp\_vol\_ctlr\_set\_vol](group__bt__vcp.md#gaaa5b5cd9a11c0e1fcdabce690ba20616)

int bt\_vcp\_vol\_ctlr\_set\_vol(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, uint8\_t volume)

Set the absolute volume on a remote Volume Renderer.

[bt\_vcp\_vol\_ctlr\_included\_get](group__bt__vcp.md#gaaa748c49e103ff161f67df9663ea6330)

int bt\_vcp\_vol\_ctlr\_included\_get(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct bt\_vcp\_included \*included)

Get Volume Control Service included services.

[bt\_vcp\_vol\_ctlr\_conn\_get](group__bt__vcp.md#gab287197243191e3dbf162c6d16b6d726)

int bt\_vcp\_vol\_ctlr\_conn\_get(const struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, struct bt\_conn \*\*conn)

Get the connection pointer of a client instance.

[bt\_vcp\_vol\_ctlr\_discover](group__bt__vcp.md#gac18d43a0785155c1131249f95554f2de)

int bt\_vcp\_vol\_ctlr\_discover(struct bt\_conn \*conn, struct bt\_vcp\_vol\_ctlr \*\*vol\_ctlr)

Discover Volume Control Service and included services.

[bt\_vcp\_vol\_rend\_unmute\_vol\_up](group__bt__vcp.md#gadf77729fee34f6605101c278fd2b7c46)

int bt\_vcp\_vol\_rend\_unmute\_vol\_up(void)

Turn the volume up and unmute the server.

[bt\_vcp\_vol\_ctlr\_cb\_unregister](group__bt__vcp.md#gae69e4730df4341bbb9bbbba1bea14005)

int bt\_vcp\_vol\_ctlr\_cb\_unregister(struct bt\_vcp\_vol\_ctlr\_cb \*cb)

Unregisters the callbacks used by the Volume Controller.

[BT\_VCP\_VOL\_REND\_VOCS\_CNT](group__bt__vcp.md#gae7195f4556ad2442bc45d8d43cdeedd0)

#define BT\_VCP\_VOL\_REND\_VOCS\_CNT

Defines the maximum number of Volume Offset Control service instances for the Volume Control Profile ...

**Definition** vcp.h:48

[bt\_vcp\_vol\_ctlr\_read\_flags](group__bt__vcp.md#gaefc226a5abb6bb1540d4b44ac4ddc236)

int bt\_vcp\_vol\_ctlr\_read\_flags(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr)

Read the volume flags of a remote Volume Renderer.

[bt\_vcp\_vol\_rend\_vol\_down](group__bt__vcp.md#gaf3c622f151a21d1dd617e97917c5ff5e)

int bt\_vcp\_vol\_rend\_vol\_down(void)

Turn the volume down by one step on the server.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_aics\_cb](structbt__aics__cb.md)

Struct to hold callbacks for the Audio Input Control Service.

**Definition** aics.h:327

[bt\_aics\_register\_param](structbt__aics__register__param.md)

Structure for initializing a Audio Input Control Service instance.

**Definition** aics.h:132

[bt\_vcp\_included](structbt__vcp__included.md)

Volume Control Service included services.

**Definition** vcp.h:115

[bt\_vcp\_included::vocs](structbt__vcp__included.md#a1f04068dd88d2fecef5fd78a3c7d4429)

struct bt\_vocs \*\* vocs

Array of pointers to Volume Offset Control Service instances.

**Definition** vcp.h:119

[bt\_vcp\_included::aics](structbt__vcp__included.md#aa6c87b8c9b4b2be6ec6429fd2ee68398)

struct bt\_aics \*\* aics

Array of pointers to Audio Input Control Service instances.

**Definition** vcp.h:124

[bt\_vcp\_included::vocs\_cnt](structbt__vcp__included.md#acb0c8e853808adfd9c3b92b45e874103)

uint8\_t vocs\_cnt

Number of Volume Offset Control Service instances.

**Definition** vcp.h:117

[bt\_vcp\_included::aics\_cnt](structbt__vcp__included.md#af521bb12ebef4c5f60609040140474c0)

uint8\_t aics\_cnt

Number of Audio Input Control Service instances.

**Definition** vcp.h:122

[bt\_vcp\_vol\_ctlr\_cb](structbt__vcp__vol__ctlr__cb.md)

Struct to hold the Volume Controller callbacks.

**Definition** vcp.h:275

[bt\_vcp\_vol\_ctlr\_cb::aics\_cb](structbt__vcp__vol__ctlr__cb.md#a430b1ee27c9bf7d6c7f8498748d91b21)

struct bt\_aics\_cb aics\_cb

Audio Input Control Service callbacks.

**Definition** vcp.h:406

[bt\_vcp\_vol\_ctlr\_cb::flags](structbt__vcp__vol__ctlr__cb.md#a4df90987abe0e53894e4064b3487c2bb)

void(\* flags)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t flags)

Callback function for Volume Control Profile volume flags.

**Definition** vcp.h:307

[bt\_vcp\_vol\_ctlr\_cb::unmute](structbt__vcp__vol__ctlr__cb.md#a6a217e0d8cbcc56e5128d5b7acdaac6d)

void(\* unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_unmute().

**Definition** vcp.h:367

[bt\_vcp\_vol\_ctlr\_cb::vol\_down\_unmute](structbt__vcp__vol__ctlr__cb.md#a770e300127b8357f1e76f0cca21b74e5)

void(\* vol\_down\_unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_down\_unmute().

**Definition** vcp.h:378

[bt\_vcp\_vol\_ctlr\_cb::mute](structbt__vcp__vol__ctlr__cb.md#aa2cd77992831eef7e59d3e4a01a0e542)

void(\* mute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_mute().

**Definition** vcp.h:356

[bt\_vcp\_vol\_ctlr\_cb::vol\_set](structbt__vcp__vol__ctlr__cb.md#abe7cf51858428db6b953a21a6ba40f83)

void(\* vol\_set)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_set().

**Definition** vcp.h:400

[bt\_vcp\_vol\_ctlr\_cb::state](structbt__vcp__vol__ctlr__cb.md#ac3b89f35b79d35384f9ead31cf15ac4e)

void(\* state)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t volume, uint8\_t mute)

Callback function for Volume Control Profile volume state.

**Definition** vcp.h:289

[bt\_vcp\_vol\_ctlr\_cb::vol\_down](structbt__vcp__vol__ctlr__cb.md#ac986e0c5cb49395fe8581f5b1dae1a88)

void(\* vol\_down)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_down().

**Definition** vcp.h:334

[bt\_vcp\_vol\_ctlr\_cb::discover](structbt__vcp__vol__ctlr__cb.md#ada8fe8d838d6d2c983d746e7e7ed1171)

void(\* discover)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err, uint8\_t vocs\_count, uint8\_t aics\_count)

Callback function for bt\_vcp\_vol\_ctlr\_discover().

**Definition** vcp.h:322

[bt\_vcp\_vol\_ctlr\_cb::vol\_up](structbt__vcp__vol__ctlr__cb.md#ae1beaa5d0a61c630fa90b4a5236ce743)

void(\* vol\_up)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_up().

**Definition** vcp.h:345

[bt\_vcp\_vol\_ctlr\_cb::vol\_up\_unmute](structbt__vcp__vol__ctlr__cb.md#af4ca636d19c83694f9b86102404b0538)

void(\* vol\_up\_unmute)(struct bt\_vcp\_vol\_ctlr \*vol\_ctlr, int err)

Callback function for bt\_vcp\_vol\_ctlr\_vol\_up\_unmute().

**Definition** vcp.h:389

[bt\_vcp\_vol\_ctlr\_cb::vocs\_cb](structbt__vcp__vol__ctlr__cb.md#af6407bb0652539608f0100f02cfaadd1)

struct bt\_vocs\_cb vocs\_cb

Volume Offset Control Service callbacks.

**Definition** vcp.h:403

[bt\_vcp\_vol\_rend\_cb](structbt__vcp__vol__rend__cb.md)

Struct to hold the Volume Renderer callbacks.

**Definition** vcp.h:158

[bt\_vcp\_vol\_rend\_cb::state](structbt__vcp__vol__rend__cb.md#a05f84d8a2deedbc426ef22b89c87bd40)

void(\* state)(struct bt\_conn \*conn, int err, uint8\_t volume, uint8\_t mute)

Callback function for Volume Control Service volume state.

**Definition** vcp.h:173

[bt\_vcp\_vol\_rend\_cb::flags](structbt__vcp__vol__rend__cb.md#a3413d33fa8c3362ded6ec81533c27c86)

void(\* flags)(struct bt\_conn \*conn, int err, uint8\_t flags)

Callback function for Volume Control Service flags.

**Definition** vcp.h:188

[bt\_vcp\_vol\_rend\_register\_param](structbt__vcp__vol__rend__register__param.md)

Register structure for Volume Control Service.

**Definition** vcp.h:88

[bt\_vcp\_vol\_rend\_register\_param::step](structbt__vcp__vol__rend__register__param.md#a098e6c6921813b3f0dc7512cd483c829)

uint8\_t step

Initial step size (1-255).

**Definition** vcp.h:90

[bt\_vcp\_vol\_rend\_register\_param::aics\_param](structbt__vcp__vol__rend__register__param.md#a1e3a4744de697d92d0fc8b9e27593417)

struct bt\_aics\_register\_param aics\_param[0]

Register parameters for Audio Input Control Services.

**Definition** vcp.h:102

[bt\_vcp\_vol\_rend\_register\_param::vocs\_param](structbt__vcp__vol__rend__register__param.md#a45eb75a4590d278cec0cf4cf6d94dda3)

struct bt\_vocs\_register\_param vocs\_param[0]

Register parameters for Volume Offset Control Services.

**Definition** vcp.h:99

[bt\_vcp\_vol\_rend\_register\_param::volume](structbt__vcp__vol__rend__register__param.md#a6cf1343a2b3033c3f4676d66017cfda7)

uint8\_t volume

Initial volume level (0-255).

**Definition** vcp.h:96

[bt\_vcp\_vol\_rend\_register\_param::mute](structbt__vcp__vol__rend__register__param.md#a93f2b246ac4241db468a46a64909866e)

uint8\_t mute

Initial mute state (0-1).

**Definition** vcp.h:93

[bt\_vcp\_vol\_rend\_register\_param::cb](structbt__vcp__vol__rend__register__param.md#af9a09c453394fd4a28d6415e2775c3f5)

struct bt\_vcp\_vol\_rend\_cb \* cb

Volume Control Service callback structure.

**Definition** vcp.h:105

[bt\_vocs\_cb](structbt__vocs__cb.md)

Struct to hold the Volume Offset Control Service callbacks.

**Definition** vocs.h:221

[bt\_vocs\_register\_param](structbt__vocs__register__param.md)

Structure for registering a Volume Offset Control Service instance.

**Definition** vocs.h:73

[vocs.h](vocs_8h.md)

Bluetooth Volume Offset Control Service (VOCS) APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [vcp.h](vcp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
