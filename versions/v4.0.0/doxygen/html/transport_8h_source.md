---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/transport_8h_source.html
original_path: doxygen/html/transport_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

transport.h

[Go to the documentation of this file.](transport_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_TRANSPORT\_H\_

13#define \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_TRANSPORT\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/kernel.h](kernel_8h.md)>

17

18struct [scmi\_message](structscmi__message.md);

19struct [scmi\_channel](structscmi__channel.md);

20

[ 35](transport_8h.md#a2ae1a5afd4489cf4cf60bd45de2c6956)typedef void (\*[scmi\_channel\_cb](transport_8h.md#a2ae1a5afd4489cf4cf60bd45de2c6956))(struct [scmi\_channel](structscmi__channel.md) \*chan);

36

[ 45](structscmi__channel.md)struct [scmi\_channel](structscmi__channel.md) {

[ 52](structscmi__channel.md#a69391f18950bd0347585855a59897af8) struct [k\_mutex](structk__mutex.md) [lock](structscmi__channel.md#a69391f18950bd0347585855a59897af8);

[ 58](structscmi__channel.md#a29fc109cdf2675e4d9ffde786b41664d) struct k\_sem [sem](structscmi__channel.md#a29fc109cdf2675e4d9ffde786b41664d);

[ 60](structscmi__channel.md#a1b69c9d0c6b49f5496ad59270ab8f157) void \*[data](structscmi__channel.md#a1b69c9d0c6b49f5496ad59270ab8f157);

[ 67](structscmi__channel.md#a81065fcba9755ccf88c3ce372ded5d56) [scmi\_channel\_cb](transport_8h.md#a2ae1a5afd4489cf4cf60bd45de2c6956) [cb](structscmi__channel.md#a81065fcba9755ccf88c3ce372ded5d56);

[ 69](structscmi__channel.md#a26b9aff015d25d775818bfb7a28e4cdb) bool [ready](structscmi__channel.md#a26b9aff015d25d775818bfb7a28e4cdb);

70};

71

[ 72](structscmi__transport__api.md)struct [scmi\_transport\_api](structscmi__transport__api.md) {

[ 73](structscmi__transport__api.md#a2d90efd745ef78a07482c51a5748fef4) int (\*[init](structscmi__transport__api.md#a2d90efd745ef78a07482c51a5748fef4))(const struct [device](structdevice.md) \*transport);

[ 74](structscmi__transport__api.md#a7946a4f860d706d7e0f132aaf532662e) int (\*[send\_message](structscmi__transport__api.md#a7946a4f860d706d7e0f132aaf532662e))(const struct [device](structdevice.md) \*transport,

75 struct [scmi\_channel](structscmi__channel.md) \*chan,

76 struct [scmi\_message](structscmi__message.md) \*msg);

[ 77](structscmi__transport__api.md#a452deceb4eb343b19adf720eae7fb602) int (\*[setup\_chan](structscmi__transport__api.md#a452deceb4eb343b19adf720eae7fb602))(const struct [device](structdevice.md) \*transport,

78 struct [scmi\_channel](structscmi__channel.md) \*chan,

79 bool tx);

[ 80](structscmi__transport__api.md#a8cc80f631a74b7cf253140fa1a7707d9) int (\*[read\_message](structscmi__transport__api.md#a8cc80f631a74b7cf253140fa1a7707d9))(const struct [device](structdevice.md) \*transport,

81 struct [scmi\_channel](structscmi__channel.md) \*chan,

82 struct [scmi\_message](structscmi__message.md) \*msg);

[ 83](structscmi__transport__api.md#a52c33e80eda1ac892d2e04e3692ced58) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[channel\_is\_free](structscmi__transport__api.md#a52c33e80eda1ac892d2e04e3692ced58))(const struct [device](structdevice.md) \*transport,

84 struct [scmi\_channel](structscmi__channel.md) \*chan);

85 struct [scmi\_channel](structscmi__channel.md) \*(\*request\_channel)(const struct [device](structdevice.md) \*transport,

86 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) proto, bool tx);

87};

88

109static inline struct [scmi\_channel](structscmi__channel.md) \*

[ 110](transport_8h.md#aa944ea05d5b9995e7bf58220f5a8b119)[scmi\_transport\_request\_channel](transport_8h.md#aa944ea05d5b9995e7bf58220f5a8b119)(const struct [device](structdevice.md) \*transport,

111 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) proto, bool tx)

112{

113 const struct [scmi\_transport\_api](structscmi__transport__api.md) \*api =

114 (const struct [scmi\_transport\_api](structscmi__transport__api.md) \*)transport->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

115

116 if (api->[request\_channel](structscmi__transport__api.md#a517cb99fc369eec024d4a4acf66865e3)) {

117 return api->[request\_channel](structscmi__transport__api.md#a517cb99fc369eec024d4a4acf66865e3)(transport, proto, tx);

118 }

119

120 return NULL;

121}

122

[ 142](transport_8h.md#a91d51238836162336350c3cdde8757ea)static inline int [scmi\_transport\_init](transport_8h.md#a91d51238836162336350c3cdde8757ea)(const struct [device](structdevice.md) \*transport)

143{

144 const struct [scmi\_transport\_api](structscmi__transport__api.md) \*api =

145 (const struct [scmi\_transport\_api](structscmi__transport__api.md) \*)transport->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

146

147 if (api->[init](structscmi__transport__api.md#a2d90efd745ef78a07482c51a5748fef4)) {

148 return api->[init](structscmi__transport__api.md#a2d90efd745ef78a07482c51a5748fef4)(transport);

149 }

150

151 return 0;

152}

153

[ 170](transport_8h.md#a5b62be6ee7f3887c433774f2f5f0f660)static inline int [scmi\_transport\_setup\_chan](transport_8h.md#a5b62be6ee7f3887c433774f2f5f0f660)(const struct [device](structdevice.md) \*transport,

171 struct [scmi\_channel](structscmi__channel.md) \*chan,

172 bool tx)

173{

174 const struct [scmi\_transport\_api](structscmi__transport__api.md) \*api =

175 (const struct [scmi\_transport\_api](structscmi__transport__api.md) \*)transport->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

176

177 if (!api || !api->[setup\_chan](structscmi__transport__api.md#a452deceb4eb343b19adf720eae7fb602)) {

178 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

179 }

180

181 return api->[setup\_chan](structscmi__transport__api.md#a452deceb4eb343b19adf720eae7fb602)(transport, chan, tx);

182}

183

[ 199](transport_8h.md#a98a6783dc94c460d3ff1be99e6906ba4)static inline int [scmi\_transport\_send\_message](transport_8h.md#a98a6783dc94c460d3ff1be99e6906ba4)(const struct [device](structdevice.md) \*transport,

200 struct [scmi\_channel](structscmi__channel.md) \*chan,

201 struct [scmi\_message](structscmi__message.md) \*msg)

202{

203 const struct [scmi\_transport\_api](structscmi__transport__api.md) \*api =

204 (const struct [scmi\_transport\_api](structscmi__transport__api.md) \*)transport->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

205

206 if (!api || !api->[send\_message](structscmi__transport__api.md#a7946a4f860d706d7e0f132aaf532662e)) {

207 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

208 }

209

210 return api->[send\_message](structscmi__transport__api.md#a7946a4f860d706d7e0f132aaf532662e)(transport, chan, msg);

211}

212

[ 225](transport_8h.md#abf042179f87393ce314cd13df00b097b)static inline int [scmi\_transport\_read\_message](transport_8h.md#abf042179f87393ce314cd13df00b097b)(const struct [device](structdevice.md) \*transport,

226 struct [scmi\_channel](structscmi__channel.md) \*chan,

227 struct [scmi\_message](structscmi__message.md) \*msg)

228{

229 const struct [scmi\_transport\_api](structscmi__transport__api.md) \*api =

230 (const struct [scmi\_transport\_api](structscmi__transport__api.md) \*)transport->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

231

232 if (!api || !api->[read\_message](structscmi__transport__api.md#a8cc80f631a74b7cf253140fa1a7707d9)) {

233 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

234 }

235

236 return api->[read\_message](structscmi__transport__api.md#a8cc80f631a74b7cf253140fa1a7707d9)(transport, chan, msg);

237}

238

[ 250](transport_8h.md#a3acea301a1e966324bd47ebac1b73cc9)static inline bool [scmi\_transport\_channel\_is\_free](transport_8h.md#a3acea301a1e966324bd47ebac1b73cc9)(const struct [device](structdevice.md) \*transport,

251 struct [scmi\_channel](structscmi__channel.md) \*chan)

252{

253 const struct [scmi\_transport\_api](structscmi__transport__api.md) \*api =

254 (const struct [scmi\_transport\_api](structscmi__transport__api.md) \*)transport->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

255

256 if (!api || !api->[channel\_is\_free](structscmi__transport__api.md#a52c33e80eda1ac892d2e04e3692ced58)) {

257 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

258 }

259

260 return api->[channel\_is\_free](structscmi__transport__api.md#a52c33e80eda1ac892d2e04e3692ced58)(transport, chan);

261}

262

[ 272](transport_8h.md#a58dfdf0d4d0495babc6ef0d83974c1da)int [scmi\_core\_transport\_init](transport_8h.md#a58dfdf0d4d0495babc6ef0d83974c1da)(const struct [device](structdevice.md) \*transport);

273

274#endif /\* \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_TRANSPORT\_H\_ \*/

[device.h](device_8h.md)

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[kernel.h](kernel_8h.md)

Public kernel APIs.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[scmi\_channel](structscmi__channel.md)

SCMI channel structure.

**Definition** transport.h:45

[scmi\_channel::data](structscmi__channel.md#a1b69c9d0c6b49f5496ad59270ab8f157)

void \* data

channel private data

**Definition** transport.h:60

[scmi\_channel::ready](structscmi__channel.md#a26b9aff015d25d775818bfb7a28e4cdb)

bool ready

is the channel ready to be used by a protocol?

**Definition** transport.h:69

[scmi\_channel::sem](structscmi__channel.md#a29fc109cdf2675e4d9ffde786b41664d)

struct k\_sem sem

binary semaphore.

**Definition** transport.h:58

[scmi\_channel::lock](structscmi__channel.md#a69391f18950bd0347585855a59897af8)

struct k\_mutex lock

channel lock.

**Definition** transport.h:52

[scmi\_channel::cb](structscmi__channel.md#a81065fcba9755ccf88c3ce372ded5d56)

scmi\_channel\_cb cb

callback function.

**Definition** transport.h:67

[scmi\_message](structscmi__message.md)

SCMI message structure.

**Definition** protocol.h:90

[scmi\_transport\_api](structscmi__transport__api.md)

**Definition** transport.h:72

[scmi\_transport\_api::init](structscmi__transport__api.md#a2d90efd745ef78a07482c51a5748fef4)

int(\* init)(const struct device \*transport)

**Definition** transport.h:73

[scmi\_transport\_api::setup\_chan](structscmi__transport__api.md#a452deceb4eb343b19adf720eae7fb602)

int(\* setup\_chan)(const struct device \*transport, struct scmi\_channel \*chan, bool tx)

**Definition** transport.h:77

[scmi\_transport\_api::request\_channel](structscmi__transport__api.md#a517cb99fc369eec024d4a4acf66865e3)

struct scmi\_channel \*(\* request\_channel)(const struct device \*transport, uint32\_t proto, bool tx)

**Definition** transport.h:85

[scmi\_transport\_api::channel\_is\_free](structscmi__transport__api.md#a52c33e80eda1ac892d2e04e3692ced58)

bool(\* channel\_is\_free)(const struct device \*transport, struct scmi\_channel \*chan)

**Definition** transport.h:83

[scmi\_transport\_api::send\_message](structscmi__transport__api.md#a7946a4f860d706d7e0f132aaf532662e)

int(\* send\_message)(const struct device \*transport, struct scmi\_channel \*chan, struct scmi\_message \*msg)

**Definition** transport.h:74

[scmi\_transport\_api::read\_message](structscmi__transport__api.md#a8cc80f631a74b7cf253140fa1a7707d9)

int(\* read\_message)(const struct device \*transport, struct scmi\_channel \*chan, struct scmi\_message \*msg)

**Definition** transport.h:80

[scmi\_channel\_cb](transport_8h.md#a2ae1a5afd4489cf4cf60bd45de2c6956)

void(\* scmi\_channel\_cb)(struct scmi\_channel \*chan)

Callback function for message replies.

**Definition** transport.h:35

[scmi\_transport\_channel\_is\_free](transport_8h.md#a3acea301a1e966324bd47ebac1b73cc9)

static bool scmi\_transport\_channel\_is\_free(const struct device \*transport, struct scmi\_channel \*chan)

Check if an SCMI channel is free.

**Definition** transport.h:250

[scmi\_core\_transport\_init](transport_8h.md#a58dfdf0d4d0495babc6ef0d83974c1da)

int scmi\_core\_transport\_init(const struct device \*transport)

Perfrom SCMI core initialization.

[scmi\_transport\_setup\_chan](transport_8h.md#a5b62be6ee7f3887c433774f2f5f0f660)

static int scmi\_transport\_setup\_chan(const struct device \*transport, struct scmi\_channel \*chan, bool tx)

Setup an SCMI channel.

**Definition** transport.h:170

[scmi\_transport\_init](transport_8h.md#a91d51238836162336350c3cdde8757ea)

static int scmi\_transport\_init(const struct device \*transport)

Perform initialization for the transport layer driver.

**Definition** transport.h:142

[scmi\_transport\_send\_message](transport_8h.md#a98a6783dc94c460d3ff1be99e6906ba4)

static int scmi\_transport\_send\_message(const struct device \*transport, struct scmi\_channel \*chan, struct scmi\_message \*msg)

Send an SCMI channel.

**Definition** transport.h:199

[scmi\_transport\_request\_channel](transport_8h.md#aa944ea05d5b9995e7bf58220f5a8b119)

static struct scmi\_channel \* scmi\_transport\_request\_channel(const struct device \*transport, uint32\_t proto, bool tx)

Request an SCMI channel dynamically.

**Definition** transport.h:110

[scmi\_transport\_read\_message](transport_8h.md#abf042179f87393ce314cd13df00b097b)

static int scmi\_transport\_read\_message(const struct device \*transport, struct scmi\_channel \*chan, struct scmi\_message \*msg)

Read an SCMI message.

**Definition** transport.h:225

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [transport.h](transport_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
