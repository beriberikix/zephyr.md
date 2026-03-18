---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2mbox_8h_source.html
original_path: doxygen/html/drivers_2mbox_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mbox.h

[Go to the documentation of this file.](drivers_2mbox_8h.md)

1

6

7/\*

8 \* Copyright (c) 2021 Carlo Caione <ccaione@baylibre.com>

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MBOX\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_MBOX\_H\_

15

68

69#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

70#include <[zephyr/device.h](device_8h.md)>

71#include <[zephyr/devicetree/mbox.h](devicetree_2mbox_8h.md)>

72

73#ifdef \_\_cplusplus

74extern "C" {

75#endif

76

[ 80](structmbox__msg.md)struct [mbox\_msg](structmbox__msg.md) {

[ 82](structmbox__msg.md#aa9b02c7a3b1620ca2c6ffa42528cfe0c) const void \*[data](structmbox__msg.md#aa9b02c7a3b1620ca2c6ffa42528cfe0c);

83

[ 85](structmbox__msg.md#a9870d0667d97e4d4ab9ba985b75e1dc4) size\_t [size](structmbox__msg.md#a9870d0667d97e4d4ab9ba985b75e1dc4);

86};

87

[ 93](structmbox__channel.md)struct [mbox\_channel](structmbox__channel.md) {

[ 95](structmbox__channel.md#a6fe03cc3209c832b295a2f7ff2ba7c63) const struct [device](structdevice.md) \*[dev](structmbox__channel.md#a6fe03cc3209c832b295a2f7ff2ba7c63);

96

[ 98](structmbox__channel.md#a0b8104fdbeca9badb76d7779b6e6f8e4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structmbox__channel.md#a0b8104fdbeca9badb76d7779b6e6f8e4);

99};

100

[ 125](group__mbox__interface.md#ga9e02e3a523a63ff564ce2bb42c03aa1f)#define MBOX\_DT\_CHANNEL\_GET(node\_id, name) \

126 { \

127 .dev = DEVICE\_DT\_GET(DT\_MBOX\_CTLR\_BY\_NAME(node\_id, name)), \

128 .id = DT\_MBOX\_CHANNEL\_BY\_NAME(node\_id, name), \

129 }

130

[ 148](group__mbox__interface.md#ga3f1273aa6518b36f6c7f95e57292b7b8)typedef void (\*[mbox\_callback\_t](group__mbox__interface.md#ga3f1273aa6518b36f6c7f95e57292b7b8))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

149 void \*user\_data, struct [mbox\_msg](structmbox__msg.md) \*[data](structmbox__msg.md#aa9b02c7a3b1620ca2c6ffa42528cfe0c));

150

[ 164](group__mbox__interface.md#gaaecf1d595053c6ea282abb0bbe637beb)typedef int (\*[mbox\_send\_t](group__mbox__interface.md#gaaecf1d595053c6ea282abb0bbe637beb))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

165 const struct [mbox\_msg](structmbox__msg.md) \*msg);

166

[ 174](group__mbox__interface.md#gadce4d6561407c2d8d7bc54a0b7350297)typedef int (\*[mbox\_mtu\_get\_t](group__mbox__interface.md#gadce4d6561407c2d8d7bc54a0b7350297))(const struct [device](structdevice.md) \*dev);

175

[ 191](group__mbox__interface.md#gac8959349175e67d0e02f98252a52647b)typedef int (\*[mbox\_register\_callback\_t](group__mbox__interface.md#gac8959349175e67d0e02f98252a52647b))(const struct [device](structdevice.md) \*dev,

192 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

193 [mbox\_callback\_t](group__mbox__interface.md#ga3f1273aa6518b36f6c7f95e57292b7b8) cb,

194 void \*user\_data);

195

[ 209](group__mbox__interface.md#ga64dad0e5a73903e3a55d619838f53176)typedef int (\*[mbox\_set\_enabled\_t](group__mbox__interface.md#ga64dad0e5a73903e3a55d619838f53176))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, bool enable);

210

[ 218](group__mbox__interface.md#ga822c7691cdd429f18f2e5e922102ef1c)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[mbox\_max\_channels\_get\_t](group__mbox__interface.md#ga822c7691cdd429f18f2e5e922102ef1c))(const struct [device](structdevice.md) \*dev);

219

[ 220](structmbox__driver__api.md)\_\_subsystem struct [mbox\_driver\_api](structmbox__driver__api.md) {

[ 221](structmbox__driver__api.md#a2e801550dc6a5f2d5546d8a3f4089466) [mbox\_send\_t](group__mbox__interface.md#gaaecf1d595053c6ea282abb0bbe637beb) [send](structmbox__driver__api.md#a2e801550dc6a5f2d5546d8a3f4089466);

[ 222](structmbox__driver__api.md#a8f63707ce94fc87018f9b6949a9d1980) [mbox\_register\_callback\_t](group__mbox__interface.md#gac8959349175e67d0e02f98252a52647b) [register\_callback](structmbox__driver__api.md#a8f63707ce94fc87018f9b6949a9d1980);

[ 223](structmbox__driver__api.md#a6033f037a164a28c8c19ab8907c30bb4) [mbox\_mtu\_get\_t](group__mbox__interface.md#gadce4d6561407c2d8d7bc54a0b7350297) [mtu\_get](structmbox__driver__api.md#a6033f037a164a28c8c19ab8907c30bb4);

[ 224](structmbox__driver__api.md#a64782da56cb5305dd091bdb026d1ebdb) [mbox\_max\_channels\_get\_t](group__mbox__interface.md#ga822c7691cdd429f18f2e5e922102ef1c) [max\_channels\_get](structmbox__driver__api.md#a64782da56cb5305dd091bdb026d1ebdb);

[ 225](structmbox__driver__api.md#aadc6a255f108894fc0dcd304de774383) [mbox\_set\_enabled\_t](group__mbox__interface.md#ga64dad0e5a73903e3a55d619838f53176) [set\_enabled](structmbox__driver__api.md#aadc6a255f108894fc0dcd304de774383);

226};

227

[ 240](group__mbox__interface.md#ga70253c432c8064a2760731f1d237f2b7)static inline void [mbox\_init\_channel](group__mbox__interface.md#ga70253c432c8064a2760731f1d237f2b7)(struct [mbox\_channel](structmbox__channel.md) \*channel, const struct [device](structdevice.md) \*dev,

241 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ch\_id)

242{

243 channel->[dev](structmbox__channel.md#a6fe03cc3209c832b295a2f7ff2ba7c63) = dev;

244 channel->[id](structmbox__channel.md#a0b8104fdbeca9badb76d7779b6e6f8e4) = ch\_id;

245}

246

[ 266](group__mbox__interface.md#ga18828e5c28201ad838ed9ba7c0afabfe)\_\_syscall int [mbox\_send](group__mbox__interface.md#ga18828e5c28201ad838ed9ba7c0afabfe)(const struct [mbox\_channel](structmbox__channel.md) \*channel, const struct [mbox\_msg](structmbox__msg.md) \*msg);

267

268static inline int z\_impl\_mbox\_send(const struct [mbox\_channel](structmbox__channel.md) \*channel, const struct [mbox\_msg](structmbox__msg.md) \*msg)

269{

270 const struct [mbox\_driver\_api](structmbox__driver__api.md) \*api =

271 (const struct [mbox\_driver\_api](structmbox__driver__api.md) \*)channel->[dev](structmbox__channel.md#a6fe03cc3209c832b295a2f7ff2ba7c63)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

272

273 if (api->send == NULL) {

274 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

275 }

276

277 return api->send(channel->dev, channel->id, msg);

278}

279

[ 294](group__mbox__interface.md#gad48e48c984e70348336a896bb2835c77)static inline int [mbox\_register\_callback](group__mbox__interface.md#gad48e48c984e70348336a896bb2835c77)(const struct [mbox\_channel](structmbox__channel.md) \*channel,

295 [mbox\_callback\_t](group__mbox__interface.md#ga3f1273aa6518b36f6c7f95e57292b7b8) cb,

296 void \*user\_data)

297{

298 const struct [mbox\_driver\_api](structmbox__driver__api.md) \*api =

299 (const struct [mbox\_driver\_api](structmbox__driver__api.md) \*)channel->[dev](structmbox__channel.md#a6fe03cc3209c832b295a2f7ff2ba7c63)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

300

301 if (api->[register\_callback](structmbox__driver__api.md#a8f63707ce94fc87018f9b6949a9d1980) == NULL) {

302 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

303 }

304

305 return api->[register\_callback](structmbox__driver__api.md#a8f63707ce94fc87018f9b6949a9d1980)(channel->[dev](structmbox__channel.md#a6fe03cc3209c832b295a2f7ff2ba7c63), channel->[id](structmbox__channel.md#a0b8104fdbeca9badb76d7779b6e6f8e4), cb, user\_data);

306}

307

[ 327](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f)\_\_syscall int [mbox\_mtu\_get](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f)(const struct [device](structdevice.md) \*dev);

328

329static inline int z\_impl\_mbox\_mtu\_get(const struct [device](structdevice.md) \*dev)

330{

331 const struct [mbox\_driver\_api](structmbox__driver__api.md) \*api =

332 (const struct [mbox\_driver\_api](structmbox__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

333

334 if (api->mtu\_get == NULL) {

335 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

336 }

337

338 return api->mtu\_get(dev);

339}

340

[ 364](group__mbox__interface.md#ga563c6c0e2199b0608b2cd0606c46fc81)\_\_syscall int [mbox\_set\_enabled](group__mbox__interface.md#ga563c6c0e2199b0608b2cd0606c46fc81)(const struct [mbox\_channel](structmbox__channel.md) \*channel, bool enable);

365

366static inline int z\_impl\_mbox\_set\_enabled(const struct [mbox\_channel](structmbox__channel.md) \*channel, bool enable)

367{

368 const struct [mbox\_driver\_api](structmbox__driver__api.md) \*api =

369 (const struct [mbox\_driver\_api](structmbox__driver__api.md) \*)channel->[dev](structmbox__channel.md#a6fe03cc3209c832b295a2f7ff2ba7c63)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

370

371 if (api->set\_enabled == NULL) {

372 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

373 }

374

375 return api->set\_enabled(channel->dev, channel->id, enable);

376}

377

[ 388](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mbox\_max\_channels\_get](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)(const struct [device](structdevice.md) \*dev);

389

390static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_mbox\_max\_channels\_get(const struct [device](structdevice.md) \*dev)

391{

392 const struct [mbox\_driver\_api](structmbox__driver__api.md) \*api =

393 (const struct [mbox\_driver\_api](structmbox__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

394

395 if (api->max\_channels\_get == NULL) {

396 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

397 }

398

399 return api->max\_channels\_get(dev);

400}

401

402#ifdef \_\_cplusplus

403}

404#endif

405

409

410#include <syscalls/mbox.h>

411

412#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MBOX\_H\_ \*/

[device.h](device_8h.md)

[mbox.h](devicetree_2mbox_8h.md)

MBOX Devicetree macro public API header file.

[mbox\_send](group__mbox__interface.md#ga18828e5c28201ad838ed9ba7c0afabfe)

int mbox\_send(const struct mbox\_channel \*channel, const struct mbox\_msg \*msg)

Try to send a message over the MBOX device.

[mbox\_callback\_t](group__mbox__interface.md#ga3f1273aa6518b36f6c7f95e57292b7b8)

void(\* mbox\_callback\_t)(const struct device \*dev, uint32\_t channel, void \*user\_data, struct mbox\_msg \*data)

Callback API for incoming MBOX messages.

**Definition** mbox.h:148

[mbox\_set\_enabled](group__mbox__interface.md#ga563c6c0e2199b0608b2cd0606c46fc81)

int mbox\_set\_enabled(const struct mbox\_channel \*channel, bool enable)

Enable (disable) interrupts and callbacks for inbound channels.

[mbox\_set\_enabled\_t](group__mbox__interface.md#ga64dad0e5a73903e3a55d619838f53176)

int(\* mbox\_set\_enabled\_t)(const struct device \*dev, uint32\_t channel, bool enable)

Callback API upon enablement of interrupts.

**Definition** mbox.h:209

[mbox\_init\_channel](group__mbox__interface.md#ga70253c432c8064a2760731f1d237f2b7)

static void mbox\_init\_channel(struct mbox\_channel \*channel, const struct device \*dev, uint32\_t ch\_id)

Initialize a channel struct.

**Definition** mbox.h:240

[mbox\_max\_channels\_get\_t](group__mbox__interface.md#ga822c7691cdd429f18f2e5e922102ef1c)

uint32\_t(\* mbox\_max\_channels\_get\_t)(const struct device \*dev)

Callback API to get maximum number of channels.

**Definition** mbox.h:218

[mbox\_mtu\_get](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f)

int mbox\_mtu\_get(const struct device \*dev)

Return the maximum number of bytes possible in an outbound message.

[mbox\_send\_t](group__mbox__interface.md#gaaecf1d595053c6ea282abb0bbe637beb)

int(\* mbox\_send\_t)(const struct device \*dev, uint32\_t channel, const struct mbox\_msg \*msg)

Callback API to send MBOX messages.

**Definition** mbox.h:164

[mbox\_register\_callback\_t](group__mbox__interface.md#gac8959349175e67d0e02f98252a52647b)

int(\* mbox\_register\_callback\_t)(const struct device \*dev, uint32\_t channel, mbox\_callback\_t cb, void \*user\_data)

Callback API upon registration.

**Definition** mbox.h:191

[mbox\_register\_callback](group__mbox__interface.md#gad48e48c984e70348336a896bb2835c77)

static int mbox\_register\_callback(const struct mbox\_channel \*channel, mbox\_callback\_t cb, void \*user\_data)

Register a callback function on a channel for incoming messages.

**Definition** mbox.h:294

[mbox\_mtu\_get\_t](group__mbox__interface.md#gadce4d6561407c2d8d7bc54a0b7350297)

int(\* mbox\_mtu\_get\_t)(const struct device \*dev)

Callback API to get maximum data size.

**Definition** mbox.h:174

[mbox\_max\_channels\_get](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)

uint32\_t mbox\_max\_channels\_get(const struct device \*dev)

Return the maximum number of channels.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[mbox\_channel](structmbox__channel.md)

Provides a type to hold an MBOX channel.

**Definition** mbox.h:93

[mbox\_channel::id](structmbox__channel.md#a0b8104fdbeca9badb76d7779b6e6f8e4)

uint32\_t id

Channel ID.

**Definition** mbox.h:98

[mbox\_channel::dev](structmbox__channel.md#a6fe03cc3209c832b295a2f7ff2ba7c63)

const struct device \* dev

MBOX device pointer.

**Definition** mbox.h:95

[mbox\_driver\_api](structmbox__driver__api.md)

**Definition** mbox.h:220

[mbox\_driver\_api::send](structmbox__driver__api.md#a2e801550dc6a5f2d5546d8a3f4089466)

mbox\_send\_t send

**Definition** mbox.h:221

[mbox\_driver\_api::mtu\_get](structmbox__driver__api.md#a6033f037a164a28c8c19ab8907c30bb4)

mbox\_mtu\_get\_t mtu\_get

**Definition** mbox.h:223

[mbox\_driver\_api::max\_channels\_get](structmbox__driver__api.md#a64782da56cb5305dd091bdb026d1ebdb)

mbox\_max\_channels\_get\_t max\_channels\_get

**Definition** mbox.h:224

[mbox\_driver\_api::register\_callback](structmbox__driver__api.md#a8f63707ce94fc87018f9b6949a9d1980)

mbox\_register\_callback\_t register\_callback

**Definition** mbox.h:222

[mbox\_driver\_api::set\_enabled](structmbox__driver__api.md#aadc6a255f108894fc0dcd304de774383)

mbox\_set\_enabled\_t set\_enabled

**Definition** mbox.h:225

[mbox\_msg](structmbox__msg.md)

Message struct (to hold data and its size).

**Definition** mbox.h:80

[mbox\_msg::size](structmbox__msg.md#a9870d0667d97e4d4ab9ba985b75e1dc4)

size\_t size

Size of the data.

**Definition** mbox.h:85

[mbox\_msg::data](structmbox__msg.md#aa9b02c7a3b1620ca2c6ffa42528cfe0c)

const void \* data

Pointer to the data sent in the message.

**Definition** mbox.h:82

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mbox.h](drivers_2mbox_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
