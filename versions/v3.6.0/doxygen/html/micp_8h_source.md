---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/micp_8h_source.html
original_path: doxygen/html/micp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

micp.h

[Go to the documentation of this file.](micp_8h.md)

1/\*

2 \* Copyright (c) 2020-2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MICP\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MICP\_H\_

9

21

22#include <[stdint.h](stdint_8h.md)>

23

24#include <[zephyr/bluetooth/audio/aics.h](aics_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

30#if defined(CONFIG\_BT\_MICP\_MIC\_DEV)

31#define BT\_MICP\_MIC\_DEV\_AICS\_CNT CONFIG\_BT\_MICP\_MIC\_DEV\_AICS\_INSTANCE\_COUNT

32#else

[ 33](group__bt__gatt__micp.md#ga46cc0362c55cd9bdaf331de834a5fef5)#define BT\_MICP\_MIC\_DEV\_AICS\_CNT 0

34#endif /\* CONFIG\_BT\_MICP\_MIC\_DEV \*/

35

[ 37](group__bt__gatt__micp.md#ga31ce5cce4aa28662de82735241ee49d8)#define BT\_MICP\_ERR\_MUTE\_DISABLED 0x80

38

[ 40](group__bt__gatt__micp.md#gaaf0327be66ebf4b0dd23282d4a46aa54)#define BT\_MICP\_MUTE\_UNMUTED 0x00

[ 41](group__bt__gatt__micp.md#ga5718e29fefc336fbee1875aa5b81f233)#define BT\_MICP\_MUTE\_MUTED 0x01

[ 42](group__bt__gatt__micp.md#gafc7ed719d471ca27aeb96aaa638c05cb)#define BT\_MICP\_MUTE\_DISABLED 0x02

43

45struct bt\_micp\_mic\_ctlr;

46

[ 48](structbt__micp__mic__dev__register__param.md)struct [bt\_micp\_mic\_dev\_register\_param](structbt__micp__mic__dev__register__param.md) {

49#if defined(CONFIG\_BT\_MICP\_MIC\_DEV\_AICS)

51 struct [bt\_aics\_register\_param](structbt__aics__register__param.md) aics\_param[[BT\_MICP\_MIC\_DEV\_AICS\_CNT](group__bt__gatt__micp.md#ga46cc0362c55cd9bdaf331de834a5fef5)];

52#endif /\* CONFIG\_BT\_MICP\_MIC\_DEV\_AICS \*/

53

[ 55](structbt__micp__mic__dev__register__param.md#adbb6cf96e7f1d3e48b88cd3fbc5fd71a) struct [bt\_micp\_mic\_dev\_cb](structbt__micp__mic__dev__cb.md) \*[cb](structbt__micp__mic__dev__register__param.md#adbb6cf96e7f1d3e48b88cd3fbc5fd71a);

56};

57

[ 66](structbt__micp__included.md)struct [bt\_micp\_included](structbt__micp__included.md) {

[ 68](structbt__micp__included.md#a32cff1b68d96319958eeba66f249cd67) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [aics\_cnt](structbt__micp__included.md#a32cff1b68d96319958eeba66f249cd67);

[ 70](structbt__micp__included.md#a2afddd15bd726039682151038b2415d1) struct bt\_aics \*\*[aics](structbt__micp__included.md#a2afddd15bd726039682151038b2415d1);

71};

72

[ 83](group__bt__gatt__micp.md#ga5dee6c7a1115bffbea39ba0575f369fc)int [bt\_micp\_mic\_dev\_register](group__bt__gatt__micp.md#ga5dee6c7a1115bffbea39ba0575f369fc)(struct [bt\_micp\_mic\_dev\_register\_param](structbt__micp__mic__dev__register__param.md) \*param);

84

[ 97](group__bt__gatt__micp.md#ga0541a36655024d9eadcff2d3e0c877f6)int [bt\_micp\_mic\_dev\_included\_get](group__bt__gatt__micp.md#ga0541a36655024d9eadcff2d3e0c877f6)(struct [bt\_micp\_included](structbt__micp__included.md) \*included);

98

[ 99](structbt__micp__mic__dev__cb.md)struct [bt\_micp\_mic\_dev\_cb](structbt__micp__mic__dev__cb.md) {

[ 109](structbt__micp__mic__dev__cb.md#ad674b130546ceabbb90e6004121ccd98) void (\*[mute](structbt__micp__mic__dev__cb.md#ad674b130546ceabbb90e6004121ccd98))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](structbt__micp__mic__dev__cb.md#ad674b130546ceabbb90e6004121ccd98));

110};

111

[ 117](group__bt__gatt__micp.md#ga19ec08afa7784b80fce039fe84a4e33c)int [bt\_micp\_mic\_dev\_unmute](group__bt__gatt__micp.md#ga19ec08afa7784b80fce039fe84a4e33c)(void);

118

[ 124](group__bt__gatt__micp.md#ga47f971c9c259e43504d586a55cf22c4e)int [bt\_micp\_mic\_dev\_mute](group__bt__gatt__micp.md#ga47f971c9c259e43504d586a55cf22c4e)(void);

125

[ 133](group__bt__gatt__micp.md#ga525c5d694f7d510d33f088e848733af6)int [bt\_micp\_mic\_dev\_mute\_disable](group__bt__gatt__micp.md#ga525c5d694f7d510d33f088e848733af6)(void);

134

[ 140](group__bt__gatt__micp.md#ga263bf5cf51e4ef8d7e6986f0d8358da3)int [bt\_micp\_mic\_dev\_mute\_get](group__bt__gatt__micp.md#ga263bf5cf51e4ef8d7e6986f0d8358da3)(void);

141

[ 142](structbt__micp__mic__ctlr__cb.md)struct [bt\_micp\_mic\_ctlr\_cb](structbt__micp__mic__ctlr__cb.md) {

[ 155](structbt__micp__mic__ctlr__cb.md#a21786359322dbd6f814929293a69482f) void (\*[mute](structbt__micp__mic__ctlr__cb.md#a21786359322dbd6f814929293a69482f))(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mute](structbt__micp__mic__ctlr__cb.md#a21786359322dbd6f814929293a69482f));

156

[ 165](structbt__micp__mic__ctlr__cb.md#a2359b88344bf36c3a491b0126dac006b) void (\*[discover](structbt__micp__mic__ctlr__cb.md#a2359b88344bf36c3a491b0126dac006b))(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err,

166 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) aics\_count);

167

[ 174](structbt__micp__mic__ctlr__cb.md#ae15fb539599feab59041e30a121021f0) void (\*[mute\_written](structbt__micp__mic__ctlr__cb.md#ae15fb539599feab59041e30a121021f0))(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err);

175

[ 182](structbt__micp__mic__ctlr__cb.md#a03afd3a79838c15be9262f441a3d338b) void (\*[unmute\_written](structbt__micp__mic__ctlr__cb.md#a03afd3a79838c15be9262f441a3d338b))(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err);

183

184#if defined(CONFIG\_BT\_MICP\_MIC\_CTLR\_AICS)

186 struct [bt\_aics\_cb](structbt__aics__cb.md) aics\_cb;

187#endif /\* CONFIG\_BT\_MICP\_MIC\_CTLR\_AICS \*/

188

190 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

191};

192

[ 207](group__bt__gatt__micp.md#ga21e04942da32b15e75a0b0de3fb84167)int [bt\_micp\_mic\_ctlr\_included\_get](group__bt__gatt__micp.md#ga21e04942da32b15e75a0b0de3fb84167)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr,

208 struct [bt\_micp\_included](structbt__micp__included.md) \*included);

209

[ 220](group__bt__gatt__micp.md#ga4b564e6b315a3861f1c3ba6098eabfe1)int [bt\_micp\_mic\_ctlr\_conn\_get](group__bt__gatt__micp.md#ga4b564e6b315a3861f1c3ba6098eabfe1)(const struct bt\_micp\_mic\_ctlr \*mic\_ctlr,

221 struct bt\_conn \*\*conn);

222

[ 235](group__bt__gatt__micp.md#ga863030e1b836c01a1be964bce0c72025)struct bt\_micp\_mic\_ctlr \*[bt\_micp\_mic\_ctlr\_get\_by\_conn](group__bt__gatt__micp.md#ga863030e1b836c01a1be964bce0c72025)(const struct bt\_conn \*conn);

236

[ 250](group__bt__gatt__micp.md#ga26187007ebf35ba2a5c57a076a3a7212)int [bt\_micp\_mic\_ctlr\_discover](group__bt__gatt__micp.md#ga26187007ebf35ba2a5c57a076a3a7212)(struct bt\_conn \*conn,

251 struct bt\_micp\_mic\_ctlr \*\*mic\_ctlr);

252

[ 260](group__bt__gatt__micp.md#ga6248c90bb94cd138c5bf9c68cffda4fe)int [bt\_micp\_mic\_ctlr\_unmute](group__bt__gatt__micp.md#ga6248c90bb94cd138c5bf9c68cffda4fe)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr);

261

[ 269](group__bt__gatt__micp.md#ga2d50f432703233c0f03cb139b6119faa)int [bt\_micp\_mic\_ctlr\_mute](group__bt__gatt__micp.md#ga2d50f432703233c0f03cb139b6119faa)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr);

270

[ 278](group__bt__gatt__micp.md#ga5148e78053a3052d27677a1fa24e3847)int [bt\_micp\_mic\_ctlr\_mute\_get](group__bt__gatt__micp.md#ga5148e78053a3052d27677a1fa24e3847)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr);

279

[ 289](group__bt__gatt__micp.md#ga148ffcd0672adff9ccfaf35c522897c4)int [bt\_micp\_mic\_ctlr\_cb\_register](group__bt__gatt__micp.md#ga148ffcd0672adff9ccfaf35c522897c4)(struct [bt\_micp\_mic\_ctlr\_cb](structbt__micp__mic__ctlr__cb.md) \*cb);

290#ifdef \_\_cplusplus

291}

292#endif

293

297

298#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MICP\_H\_ \*/

[aics.h](aics_8h.md)

[bt\_micp\_mic\_dev\_included\_get](group__bt__gatt__micp.md#ga0541a36655024d9eadcff2d3e0c877f6)

int bt\_micp\_mic\_dev\_included\_get(struct bt\_micp\_included \*included)

Get Microphone Device included services.

[bt\_micp\_mic\_ctlr\_cb\_register](group__bt__gatt__micp.md#ga148ffcd0672adff9ccfaf35c522897c4)

int bt\_micp\_mic\_ctlr\_cb\_register(struct bt\_micp\_mic\_ctlr\_cb \*cb)

Registers the callbacks used by Microphone Controller.

[bt\_micp\_mic\_dev\_unmute](group__bt__gatt__micp.md#ga19ec08afa7784b80fce039fe84a4e33c)

int bt\_micp\_mic\_dev\_unmute(void)

Unmute the Microphone Device.

[bt\_micp\_mic\_ctlr\_included\_get](group__bt__gatt__micp.md#ga21e04942da32b15e75a0b0de3fb84167)

int bt\_micp\_mic\_ctlr\_included\_get(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, struct bt\_micp\_included \*included)

Get Microphone Control Profile included services.

[bt\_micp\_mic\_ctlr\_discover](group__bt__gatt__micp.md#ga26187007ebf35ba2a5c57a076a3a7212)

int bt\_micp\_mic\_ctlr\_discover(struct bt\_conn \*conn, struct bt\_micp\_mic\_ctlr \*\*mic\_ctlr)

Discover Microphone Control Service.

[bt\_micp\_mic\_dev\_mute\_get](group__bt__gatt__micp.md#ga263bf5cf51e4ef8d7e6986f0d8358da3)

int bt\_micp\_mic\_dev\_mute\_get(void)

Read the mute state on the Microphone Device.

[bt\_micp\_mic\_ctlr\_mute](group__bt__gatt__micp.md#ga2d50f432703233c0f03cb139b6119faa)

int bt\_micp\_mic\_ctlr\_mute(struct bt\_micp\_mic\_ctlr \*mic\_ctlr)

Mute a remote Microphone Device.

[BT\_MICP\_MIC\_DEV\_AICS\_CNT](group__bt__gatt__micp.md#ga46cc0362c55cd9bdaf331de834a5fef5)

#define BT\_MICP\_MIC\_DEV\_AICS\_CNT

**Definition** micp.h:33

[bt\_micp\_mic\_dev\_mute](group__bt__gatt__micp.md#ga47f971c9c259e43504d586a55cf22c4e)

int bt\_micp\_mic\_dev\_mute(void)

Mute the Microphone Device.

[bt\_micp\_mic\_ctlr\_conn\_get](group__bt__gatt__micp.md#ga4b564e6b315a3861f1c3ba6098eabfe1)

int bt\_micp\_mic\_ctlr\_conn\_get(const struct bt\_micp\_mic\_ctlr \*mic\_ctlr, struct bt\_conn \*\*conn)

Get the connection pointer of a Microphone Controller instance.

[bt\_micp\_mic\_ctlr\_mute\_get](group__bt__gatt__micp.md#ga5148e78053a3052d27677a1fa24e3847)

int bt\_micp\_mic\_ctlr\_mute\_get(struct bt\_micp\_mic\_ctlr \*mic\_ctlr)

Read the mute state of a remote Microphone Device.

[bt\_micp\_mic\_dev\_mute\_disable](group__bt__gatt__micp.md#ga525c5d694f7d510d33f088e848733af6)

int bt\_micp\_mic\_dev\_mute\_disable(void)

Disable the mute functionality on the Microphone Device.

[bt\_micp\_mic\_dev\_register](group__bt__gatt__micp.md#ga5dee6c7a1115bffbea39ba0575f369fc)

int bt\_micp\_mic\_dev\_register(struct bt\_micp\_mic\_dev\_register\_param \*param)

Initialize the Microphone Control Profile Microphone Device.

[bt\_micp\_mic\_ctlr\_unmute](group__bt__gatt__micp.md#ga6248c90bb94cd138c5bf9c68cffda4fe)

int bt\_micp\_mic\_ctlr\_unmute(struct bt\_micp\_mic\_ctlr \*mic\_ctlr)

Unmute a remote Microphone Device.

[bt\_micp\_mic\_ctlr\_get\_by\_conn](group__bt__gatt__micp.md#ga863030e1b836c01a1be964bce0c72025)

struct bt\_micp\_mic\_ctlr \* bt\_micp\_mic\_ctlr\_get\_by\_conn(const struct bt\_conn \*conn)

Get the volume controller from a connection pointer.

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

[bt\_micp\_included](structbt__micp__included.md)

Microphone Control Profile included services.

**Definition** micp.h:66

[bt\_micp\_included::aics](structbt__micp__included.md#a2afddd15bd726039682151038b2415d1)

struct bt\_aics \*\* aics

Array of pointers to Audio Input Control Service instances.

**Definition** micp.h:70

[bt\_micp\_included::aics\_cnt](structbt__micp__included.md#a32cff1b68d96319958eeba66f249cd67)

uint8\_t aics\_cnt

Number of Audio Input Control Service instances.

**Definition** micp.h:68

[bt\_micp\_mic\_ctlr\_cb](structbt__micp__mic__ctlr__cb.md)

**Definition** micp.h:142

[bt\_micp\_mic\_ctlr\_cb::unmute\_written](structbt__micp__mic__ctlr__cb.md#a03afd3a79838c15be9262f441a3d338b)

void(\* unmute\_written)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err)

Callback function for Microphone Control Profile mute/unmute.

**Definition** micp.h:182

[bt\_micp\_mic\_ctlr\_cb::mute](structbt__micp__mic__ctlr__cb.md#a21786359322dbd6f814929293a69482f)

void(\* mute)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, uint8\_t mute)

Callback function for Microphone Control Profile mute.

**Definition** micp.h:155

[bt\_micp\_mic\_ctlr\_cb::discover](structbt__micp__mic__ctlr__cb.md#a2359b88344bf36c3a491b0126dac006b)

void(\* discover)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err, uint8\_t aics\_count)

Callback function for bt\_micp\_mic\_ctlr\_discover().

**Definition** micp.h:165

[bt\_micp\_mic\_ctlr\_cb::mute\_written](structbt__micp__mic__ctlr__cb.md#ae15fb539599feab59041e30a121021f0)

void(\* mute\_written)(struct bt\_micp\_mic\_ctlr \*mic\_ctlr, int err)

Callback function for Microphone Control Profile mute/unmute.

**Definition** micp.h:174

[bt\_micp\_mic\_dev\_cb](structbt__micp__mic__dev__cb.md)

**Definition** micp.h:99

[bt\_micp\_mic\_dev\_cb::mute](structbt__micp__mic__dev__cb.md#ad674b130546ceabbb90e6004121ccd98)

void(\* mute)(uint8\_t mute)

Callback function for Microphone Device mute.

**Definition** micp.h:109

[bt\_micp\_mic\_dev\_register\_param](structbt__micp__mic__dev__register__param.md)

Register parameters structure for Microphone Control Service.

**Definition** micp.h:48

[bt\_micp\_mic\_dev\_register\_param::cb](structbt__micp__mic__dev__register__param.md#adbb6cf96e7f1d3e48b88cd3fbc5fd71a)

struct bt\_micp\_mic\_dev\_cb \* cb

Microphone Control Profile callback structure.

**Definition** micp.h:55

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [micp.h](micp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
