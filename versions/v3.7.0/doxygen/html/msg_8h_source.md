---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/msg_8h_source.html
original_path: doxygen/html/msg_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msg.h

[Go to the documentation of this file.](msg_8h.md)

1

4

5/\*

6 \* Copyright (c) 2021 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_MSG\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_MSG\_H\_

12

19

20#include <[zephyr/kernel.h](kernel_8h.md)>

21#include <[zephyr/net/buf.h](net_2buf_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27struct [bt\_mesh\_model](structbt__mesh__model.md);

28

[ 30](group__bt__mesh__msg.md#ga658d38a7be18355f6ecd5f7fb4dcabed)#define BT\_MESH\_MIC\_SHORT 4

[ 32](group__bt__mesh__msg.md#ga6e8fc0bb4ed35870c0f1652c18a8117d)#define BT\_MESH\_MIC\_LONG 8

33

[ 39](group__bt__mesh__msg.md#gad0b5f56cc9741fcd5dadf157c5e62701)#define BT\_MESH\_MODEL\_OP\_LEN(\_op) ((\_op) <= 0xff ? 1 : (\_op) <= 0xffff ? 2 : 3)

40

[ 50](group__bt__mesh__msg.md#ga5352d6fa05808722eba8a76e2446eddb)#define BT\_MESH\_MODEL\_BUF\_LEN(\_op, \_payload\_len) \

51 (BT\_MESH\_MODEL\_OP\_LEN(\_op) + (\_payload\_len) + BT\_MESH\_MIC\_SHORT)

52

[ 62](group__bt__mesh__msg.md#gabb16a024db39706af46ad86e2b04b00d)#define BT\_MESH\_MODEL\_BUF\_LEN\_LONG\_MIC(\_op, \_payload\_len) \

63 (BT\_MESH\_MODEL\_OP\_LEN(\_op) + (\_payload\_len) + BT\_MESH\_MIC\_LONG)

64

[ 72](group__bt__mesh__msg.md#ga6a61ace773e331d82860b343d51f62e7)#define BT\_MESH\_MODEL\_BUF\_DEFINE(\_buf, \_op, \_payload\_len) \

73 NET\_BUF\_SIMPLE\_DEFINE(\_buf, BT\_MESH\_MODEL\_BUF\_LEN(\_op, (\_payload\_len)))

74

[ 76](structbt__mesh__msg__ctx.md)struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) {

[ 78](structbt__mesh__msg__ctx.md#a106a615ce13040e99413a15ff74bb0a9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__msg__ctx.md#a106a615ce13040e99413a15ff74bb0a9);

79

[ 81](structbt__mesh__msg__ctx.md#a58de4d7cef6a8236a6517fc0bd961917) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [app\_idx](structbt__mesh__msg__ctx.md#a58de4d7cef6a8236a6517fc0bd961917);

82

[ 84](structbt__mesh__msg__ctx.md#a2ead7791000e9a55ed1b92c40b84bc7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__msg__ctx.md#a2ead7791000e9a55ed1b92c40b84bc7a);

85

[ 87](structbt__mesh__msg__ctx.md#a682b192d416620a33a12b248b299b31e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [recv\_dst](structbt__mesh__msg__ctx.md#a682b192d416620a33a12b248b299b31e);

88

[ 90](structbt__mesh__msg__ctx.md#a548cab1ea578b29d6adf36afcf5d0299) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[uuid](structbt__mesh__msg__ctx.md#a548cab1ea578b29d6adf36afcf5d0299);

91

[ 93](structbt__mesh__msg__ctx.md#a1838579bb63c1976322e8eda039052db) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [recv\_rssi](structbt__mesh__msg__ctx.md#a1838579bb63c1976322e8eda039052db);

94

[ 96](structbt__mesh__msg__ctx.md#af8ff3238c184c541ff5417f37dd2c1e4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recv\_ttl](structbt__mesh__msg__ctx.md#af8ff3238c184c541ff5417f37dd2c1e4);

97

[ 99](structbt__mesh__msg__ctx.md#a21cfb308ed8c718303bb2bc414c50753) bool [send\_rel](structbt__mesh__msg__ctx.md#a21cfb308ed8c718303bb2bc414c50753);

100

[ 102](structbt__mesh__msg__ctx.md#acb5b5de55f35b37ba4f34ffc08943184) bool [rnd\_delay](structbt__mesh__msg__ctx.md#acb5b5de55f35b37ba4f34ffc08943184);

103

[ 105](structbt__mesh__msg__ctx.md#a43b0ebfdc3c8018a02886d93dfe2f21b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [send\_ttl](structbt__mesh__msg__ctx.md#a43b0ebfdc3c8018a02886d93dfe2f21b);

106};

107

[ 119](group__bt__mesh__msg.md#ga90200861df2575a974e7414e3642058a)#define BT\_MESH\_MSG\_CTX\_INIT(net\_key\_idx, app\_key\_idx, dst, ttl) \

120 { \

121 .net\_idx = (net\_key\_idx), \

122 .app\_idx = (app\_key\_idx), \

123 .addr = (dst), \

124 .send\_ttl = (ttl), \

125 }

126

[ 133](group__bt__mesh__msg.md#ga98470d8a351528f4ccb8c0ef2edbc030)#define BT\_MESH\_MSG\_CTX\_INIT\_APP(app\_key\_idx, dst) \

134 BT\_MESH\_MSG\_CTX\_INIT(0, app\_key\_idx, dst, BT\_MESH\_TTL\_DEFAULT)

135

[ 143](group__bt__mesh__msg.md#ga3cab6b5e400a205befdc5a6c7609c453)#define BT\_MESH\_MSG\_CTX\_INIT\_DEV(net\_key\_idx, dst) \

144 BT\_MESH\_MSG\_CTX\_INIT(net\_key\_idx, BT\_MESH\_KEY\_DEV\_REMOTE, dst, BT\_MESH\_TTL\_DEFAULT)

145

[ 151](group__bt__mesh__msg.md#ga4afe7dad3e38f7e54d65ca608adc9ba3)#define BT\_MESH\_MSG\_CTX\_INIT\_PUB(pub) \

152 { \

153 .app\_idx = (pub)->key, \

154 .addr = (pub)->addr, \

155 .send\_ttl = (pub)->ttl, \

156 .uuid = (pub)->uuid, \

157 }

158

[ 167](group__bt__mesh__msg.md#gaa26850aebc9bfc97d1dafb66ba02021c)void [bt\_mesh\_model\_msg\_init](group__bt__mesh__msg.md#gaa26850aebc9bfc97d1dafb66ba02021c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcode);

168

[ 172](structbt__mesh__msg__ack__ctx.md)struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) {

[ 173](structbt__mesh__msg__ack__ctx.md#a53ce3e10f27da773c227de6d6eaba5e3) struct k\_sem [sem](structbt__mesh__msg__ack__ctx.md#a53ce3e10f27da773c227de6d6eaba5e3);

[ 174](structbt__mesh__msg__ack__ctx.md#a08f50fcae687026c45d891c9381bd9c2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [op](structbt__mesh__msg__ack__ctx.md#a08f50fcae687026c45d891c9381bd9c2);

[ 175](structbt__mesh__msg__ack__ctx.md#ac83626299e197dbd0a9a36a6617c3b21) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst](structbt__mesh__msg__ack__ctx.md#ac83626299e197dbd0a9a36a6617c3b21);

[ 176](structbt__mesh__msg__ack__ctx.md#a510baede03d53b2419ade8da6d02fa10) void \*[user\_data](structbt__mesh__msg__ack__ctx.md#a510baede03d53b2419ade8da6d02fa10);

177};

178

[ 186](group__bt__mesh__msg.md#gadd25e335133fe29f234243a39f4d7626)static inline void [bt\_mesh\_msg\_ack\_ctx\_init](group__bt__mesh__msg.md#gadd25e335133fe29f234243a39f4d7626)(struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack)

187{

188 [k\_sem\_init](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)(&ack->[sem](structbt__mesh__msg__ack__ctx.md#a53ce3e10f27da773c227de6d6eaba5e3), 0, 1);

189}

190

[ 197](group__bt__mesh__msg.md#ga86d3803bde26f496b7de3fa348a04525)static inline void [bt\_mesh\_msg\_ack\_ctx\_reset](group__bt__mesh__msg.md#ga86d3803bde26f496b7de3fa348a04525)(struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack)

198{

199 [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)(&ack->[sem](structbt__mesh__msg__ack__ctx.md#a53ce3e10f27da773c227de6d6eaba5e3));

200}

201

[ 209](group__bt__mesh__msg.md#ga3da92606640cdba69a676c2a03c72311)void [bt\_mesh\_msg\_ack\_ctx\_clear](group__bt__mesh__msg.md#ga3da92606640cdba69a676c2a03c72311)(struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack);

210

[ 223](group__bt__mesh__msg.md#ga1bb34a904103933140e2159cb53d49f5)int [bt\_mesh\_msg\_ack\_ctx\_prepare](group__bt__mesh__msg.md#ga1bb34a904103933140e2159cb53d49f5)(struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack,

224 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst, void \*user\_data);

225

[ 233](group__bt__mesh__msg.md#ga974ba5d7df597a21945b75ac5919debd)static inline bool [bt\_mesh\_msg\_ack\_ctx\_busy](group__bt__mesh__msg.md#ga974ba5d7df597a21945b75ac5919debd)(struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack)

234{

235 return (ack->[op](structbt__mesh__msg__ack__ctx.md#a08f50fcae687026c45d891c9381bd9c2) != 0);

236}

237

[ 247](group__bt__mesh__msg.md#ga83561f4d003c6c3c2b91a6afd180d1fd)int [bt\_mesh\_msg\_ack\_ctx\_wait](group__bt__mesh__msg.md#ga83561f4d003c6c3c2b91a6afd180d1fd)(struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack, [k\_timeout\_t](structk__timeout__t.md) timeout);

248

[ 255](group__bt__mesh__msg.md#ga2b054f7dc01daeef067cd3d819a7c42c)static inline void [bt\_mesh\_msg\_ack\_ctx\_rx](group__bt__mesh__msg.md#ga2b054f7dc01daeef067cd3d819a7c42c)(struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack)

256{

257 [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)(&ack->[sem](structbt__mesh__msg__ack__ctx.md#a53ce3e10f27da773c227de6d6eaba5e3));

258}

259

[ 270](group__bt__mesh__msg.md#gae10c4229cabf7774684c99154d4ed8ae)bool [bt\_mesh\_msg\_ack\_ctx\_match](group__bt__mesh__msg.md#gae10c4229cabf7774684c99154d4ed8ae)(const struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) \*ack,

271 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) op, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, void \*\*user\_data);

272

273#ifdef \_\_cplusplus

274}

275#endif

276

280

281#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_MSG\_H\_ \*/

[bt\_mesh\_msg\_ack\_ctx\_prepare](group__bt__mesh__msg.md#ga1bb34a904103933140e2159cb53d49f5)

int bt\_mesh\_msg\_ack\_ctx\_prepare(struct bt\_mesh\_msg\_ack\_ctx \*ack, uint32\_t op, uint16\_t dst, void \*user\_data)

Prepare an acknowledged message context for the incoming message to wait.

[bt\_mesh\_msg\_ack\_ctx\_rx](group__bt__mesh__msg.md#ga2b054f7dc01daeef067cd3d819a7c42c)

static void bt\_mesh\_msg\_ack\_ctx\_rx(struct bt\_mesh\_msg\_ack\_ctx \*ack)

Mark a message as acknowledged.

**Definition** msg.h:255

[bt\_mesh\_msg\_ack\_ctx\_clear](group__bt__mesh__msg.md#ga3da92606640cdba69a676c2a03c72311)

void bt\_mesh\_msg\_ack\_ctx\_clear(struct bt\_mesh\_msg\_ack\_ctx \*ack)

Clear parameters of an acknowledged message context.

[bt\_mesh\_msg\_ack\_ctx\_wait](group__bt__mesh__msg.md#ga83561f4d003c6c3c2b91a6afd180d1fd)

int bt\_mesh\_msg\_ack\_ctx\_wait(struct bt\_mesh\_msg\_ack\_ctx \*ack, k\_timeout\_t timeout)

Wait for a message acknowledge.

[bt\_mesh\_msg\_ack\_ctx\_reset](group__bt__mesh__msg.md#ga86d3803bde26f496b7de3fa348a04525)

static void bt\_mesh\_msg\_ack\_ctx\_reset(struct bt\_mesh\_msg\_ack\_ctx \*ack)

Reset the synchronization semaphore in an acknowledged message context.

**Definition** msg.h:197

[bt\_mesh\_msg\_ack\_ctx\_busy](group__bt__mesh__msg.md#ga974ba5d7df597a21945b75ac5919debd)

static bool bt\_mesh\_msg\_ack\_ctx\_busy(struct bt\_mesh\_msg\_ack\_ctx \*ack)

Check if the acknowledged message context is initialized with an opcode.

**Definition** msg.h:233

[bt\_mesh\_model\_msg\_init](group__bt__mesh__msg.md#gaa26850aebc9bfc97d1dafb66ba02021c)

void bt\_mesh\_model\_msg\_init(struct net\_buf\_simple \*msg, uint32\_t opcode)

Initialize a model message.

[bt\_mesh\_msg\_ack\_ctx\_init](group__bt__mesh__msg.md#gadd25e335133fe29f234243a39f4d7626)

static void bt\_mesh\_msg\_ack\_ctx\_init(struct bt\_mesh\_msg\_ack\_ctx \*ack)

Initialize an acknowledged message context.

**Definition** msg.h:186

[bt\_mesh\_msg\_ack\_ctx\_match](group__bt__mesh__msg.md#gae10c4229cabf7774684c99154d4ed8ae)

bool bt\_mesh\_msg\_ack\_ctx\_match(const struct bt\_mesh\_msg\_ack\_ctx \*ack, uint32\_t op, uint16\_t addr, void \*\*user\_data)

Check if an opcode and address of a message matches the expected one.

[k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)

void k\_sem\_reset(struct k\_sem \*sem)

Resets a semaphore's count to zero.

[k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84)

void k\_sem\_give(struct k\_sem \*sem)

Give a semaphore.

[k\_sem\_init](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845)

int k\_sem\_init(struct k\_sem \*sem, unsigned int initial\_count, unsigned int limit)

Initialize a semaphore.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[buf.h](net_2buf_8h.md)

Buffer management.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:887

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

[bt\_mesh\_msg\_ack\_ctx::op](structbt__mesh__msg__ack__ctx.md#a08f50fcae687026c45d891c9381bd9c2)

uint32\_t op

Opcode we're waiting for.

**Definition** msg.h:174

[bt\_mesh\_msg\_ack\_ctx::user\_data](structbt__mesh__msg__ack__ctx.md#a510baede03d53b2419ade8da6d02fa10)

void \* user\_data

User specific parameter.

**Definition** msg.h:176

[bt\_mesh\_msg\_ack\_ctx::sem](structbt__mesh__msg__ack__ctx.md#a53ce3e10f27da773c227de6d6eaba5e3)

struct k\_sem sem

Sync semaphore.

**Definition** msg.h:173

[bt\_mesh\_msg\_ack\_ctx::dst](structbt__mesh__msg__ack__ctx.md#ac83626299e197dbd0a9a36a6617c3b21)

uint16\_t dst

Address of the node that should respond.

**Definition** msg.h:175

[bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md)

Message sending context.

**Definition** msg.h:76

[bt\_mesh\_msg\_ctx::net\_idx](structbt__mesh__msg__ctx.md#a106a615ce13040e99413a15ff74bb0a9)

uint16\_t net\_idx

NetKey Index of the subnet to send the message on.

**Definition** msg.h:78

[bt\_mesh\_msg\_ctx::recv\_rssi](structbt__mesh__msg__ctx.md#a1838579bb63c1976322e8eda039052db)

int8\_t recv\_rssi

RSSI of received packet.

**Definition** msg.h:93

[bt\_mesh\_msg\_ctx::send\_rel](structbt__mesh__msg__ctx.md#a21cfb308ed8c718303bb2bc414c50753)

bool send\_rel

Force sending reliably by using segment acknowledgment.

**Definition** msg.h:99

[bt\_mesh\_msg\_ctx::addr](structbt__mesh__msg__ctx.md#a2ead7791000e9a55ed1b92c40b84bc7a)

uint16\_t addr

Remote address.

**Definition** msg.h:84

[bt\_mesh\_msg\_ctx::send\_ttl](structbt__mesh__msg__ctx.md#a43b0ebfdc3c8018a02886d93dfe2f21b)

uint8\_t send\_ttl

TTL, or BT\_MESH\_TTL\_DEFAULT for default TTL.

**Definition** msg.h:105

[bt\_mesh\_msg\_ctx::uuid](structbt__mesh__msg__ctx.md#a548cab1ea578b29d6adf36afcf5d0299)

const uint8\_t \* uuid

Label UUID if Remote address is Virtual address, or NULL otherwise.

**Definition** msg.h:90

[bt\_mesh\_msg\_ctx::app\_idx](structbt__mesh__msg__ctx.md#a58de4d7cef6a8236a6517fc0bd961917)

uint16\_t app\_idx

AppKey Index to encrypt the message with.

**Definition** msg.h:81

[bt\_mesh\_msg\_ctx::recv\_dst](structbt__mesh__msg__ctx.md#a682b192d416620a33a12b248b299b31e)

uint16\_t recv\_dst

Destination address of a received message.

**Definition** msg.h:87

[bt\_mesh\_msg\_ctx::rnd\_delay](structbt__mesh__msg__ctx.md#acb5b5de55f35b37ba4f34ffc08943184)

bool rnd\_delay

Send message with a random delay according to the Access layer transmitting rules.

**Definition** msg.h:102

[bt\_mesh\_msg\_ctx::recv\_ttl](structbt__mesh__msg__ctx.md#af8ff3238c184c541ff5417f37dd2c1e4)

uint8\_t recv\_ttl

Received TTL value.

**Definition** msg.h:96

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [msg.h](msg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
