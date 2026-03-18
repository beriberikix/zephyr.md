---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2mbox_8h_source.html
original_path: doxygen/html/drivers_2mbox_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mbox.h

[Go to the documentation of this file.](drivers_2mbox_8h.md)

1/\*

2 \* Copyright (c) 2021 Carlo Caione <ccaione@baylibre.com>

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MBOX\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MBOX\_H\_

8

9#include <[errno.h](errno_8h.md)>

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdlib.h](stdlib_8h.md)>

12

13#include <[zephyr/device.h](device_8h.md)>

14#include <[zephyr/devicetree.h](devicetree_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

74

[ 76](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37);

77

[ 79](structmbox__msg.md)struct [mbox\_msg](structmbox__msg.md) {

[ 81](structmbox__msg.md#aa9b02c7a3b1620ca2c6ffa42528cfe0c) const void \*[data](structmbox__msg.md#aa9b02c7a3b1620ca2c6ffa42528cfe0c);

[ 83](structmbox__msg.md#a9870d0667d97e4d4ab9ba985b75e1dc4) size\_t [size](structmbox__msg.md#a9870d0667d97e4d4ab9ba985b75e1dc4);

84};

85

[ 87](structmbox__dt__spec.md)struct [mbox\_dt\_spec](structmbox__dt__spec.md) {

[ 89](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52) const struct [device](structdevice.md) \*[dev](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52);

[ 91](structmbox__dt__spec.md#aa72163f47124446dab00d93f239b70e7) [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) [channel\_id](structmbox__dt__spec.md#aa72163f47124446dab00d93f239b70e7);

92};

93

[ 122](group__mbox__interface.md#gadd0a5b06ab4b208460cf49952a2b4b43)#define MBOX\_DT\_SPEC\_GET(node\_id, name) \

123 { \

124 .dev = DEVICE\_DT\_GET(DT\_MBOX\_CTLR\_BY\_NAME(node\_id, name)), \

125 .channel\_id = DT\_MBOX\_CHANNEL\_BY\_NAME(node\_id, name), \

126 }

127

[ 136](group__mbox__interface.md#gafb05876cbac7967d93d9ffccbd4761a5)#define MBOX\_DT\_SPEC\_INST\_GET(inst, name) \

137 MBOX\_DT\_SPEC\_GET(DT\_DRV\_INST(inst), name)

138

140

155typedef void (\*mbox\_callback\_t)(const struct [device](structdevice.md) \*dev,

156 [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, void \*user\_data,

157 struct [mbox\_msg](structmbox__msg.md) \*[data](structmbox__msg.md#aa9b02c7a3b1620ca2c6ffa42528cfe0c));

158

169typedef int (\*mbox\_send\_t)(const struct [device](structdevice.md) \*dev,

170 [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id,

171 const struct [mbox\_msg](structmbox__msg.md) \*msg);

172

181typedef int (\*mbox\_mtu\_get\_t)(const struct [device](structdevice.md) \*dev);

182

195typedef int (\*mbox\_register\_callback\_t)(const struct [device](structdevice.md) \*dev,

196 [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id,

197 mbox\_callback\_t cb, void \*user\_data);

198

209typedef int (\*mbox\_set\_enabled\_t)(const struct [device](structdevice.md) \*dev,

210 [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, bool enabled);

211

220typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*mbox\_max\_channels\_get\_t)(const struct [device](structdevice.md) \*dev);

221

222\_\_subsystem struct mbox\_driver\_api {

223 mbox\_send\_t [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d);

224 mbox\_register\_callback\_t register\_callback;

225 mbox\_mtu\_get\_t mtu\_get;

226 mbox\_max\_channels\_get\_t max\_channels\_get;

227 mbox\_set\_enabled\_t set\_enabled;

228};

229

231

[ 239](group__mbox__interface.md#gab1bea02e9f49442b7454706fb434f5f2)static inline bool [mbox\_is\_ready\_dt](group__mbox__interface.md#gab1bea02e9f49442b7454706fb434f5f2)(const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec)

240{

241 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[dev](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52));

242}

243

[ 263](group__mbox__interface.md#gaf4d02fb3a3ed788ba28a58783209d359)\_\_syscall int [mbox\_send](group__mbox__interface.md#gaf4d02fb3a3ed788ba28a58783209d359)(const struct [device](structdevice.md) \*dev, [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id,

264 const struct [mbox\_msg](structmbox__msg.md) \*msg);

265

266static inline int z\_impl\_mbox\_send(const struct [device](structdevice.md) \*dev,

267 [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id,

268 const struct [mbox\_msg](structmbox__msg.md) \*msg)

269{

270 const struct mbox\_driver\_api \*api =

271 (const struct mbox\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

272

273 if (api->send == NULL) {

274 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

275 }

276

277 return api->send(dev, channel\_id, msg);

278}

279

[ 288](group__mbox__interface.md#ga8f737ce94afac19dd8924526d48c68ba)static inline int [mbox\_send\_dt](group__mbox__interface.md#ga8f737ce94afac19dd8924526d48c68ba)(const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec,

289 const struct [mbox\_msg](structmbox__msg.md) \*msg)

290{

291 return [mbox\_send](group__mbox__interface.md#gaf4d02fb3a3ed788ba28a58783209d359)(spec->[dev](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52), spec->[channel\_id](structmbox__dt__spec.md#aa72163f47124446dab00d93f239b70e7), msg);

292}

293

[ 310](group__mbox__interface.md#gac1cc65cc54b9c7e6cf2639152a4d6a7a)static inline int [mbox\_register\_callback](group__mbox__interface.md#gac1cc65cc54b9c7e6cf2639152a4d6a7a)(const struct [device](structdevice.md) \*dev,

311 [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id,

312 mbox\_callback\_t cb,

313 void \*user\_data)

314{

315 const struct mbox\_driver\_api \*api =

316 (const struct mbox\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

317

318 if (api->register\_callback == NULL) {

319 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

320 }

321

322 return api->register\_callback(dev, channel\_id, cb, user\_data);

323}

324

[ 336](group__mbox__interface.md#ga9cda3048389f4f57d425eac8257048a7)static inline int [mbox\_register\_callback\_dt](group__mbox__interface.md#ga9cda3048389f4f57d425eac8257048a7)(const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec,

337 mbox\_callback\_t cb, void \*user\_data)

338{

339 return [mbox\_register\_callback](group__mbox__interface.md#gac1cc65cc54b9c7e6cf2639152a4d6a7a)(spec->[dev](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52), spec->[channel\_id](structmbox__dt__spec.md#aa72163f47124446dab00d93f239b70e7), cb,

340 user\_data);

341}

342

[ 363](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f)\_\_syscall int [mbox\_mtu\_get](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f)(const struct [device](structdevice.md) \*dev);

364

365static inline int z\_impl\_mbox\_mtu\_get(const struct [device](structdevice.md) \*dev)

366{

367 const struct mbox\_driver\_api \*api =

368 (const struct mbox\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

369

370 if (api->mtu\_get == NULL) {

371 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

372 }

373

374 return api->mtu\_get(dev);

375}

376

[ 385](group__mbox__interface.md#ga9565933b282fe8e5fd057fbb238e00b9)static inline int [mbox\_mtu\_get\_dt](group__mbox__interface.md#ga9565933b282fe8e5fd057fbb238e00b9)(const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec)

386{

387 return [mbox\_mtu\_get](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f)(spec->[dev](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52));

388}

389

[ 415](group__mbox__interface.md#ga9eea4b9501751919125cd6124f9e9868)\_\_syscall int [mbox\_set\_enabled](group__mbox__interface.md#ga9eea4b9501751919125cd6124f9e9868)(const struct [device](structdevice.md) \*dev,

416 [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, bool enabled);

417

418static inline int z\_impl\_mbox\_set\_enabled(const struct [device](structdevice.md) \*dev,

419 [mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id,

420 bool enabled)

421{

422 const struct mbox\_driver\_api \*api =

423 (const struct mbox\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

424

425 if (api->set\_enabled == NULL) {

426 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

427 }

428

429 return api->set\_enabled(dev, channel\_id, enabled);

430}

431

[ 441](group__mbox__interface.md#ga50282848e03481fe8b6f5caa900892d3)static inline int [mbox\_set\_enabled\_dt](group__mbox__interface.md#ga50282848e03481fe8b6f5caa900892d3)(const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec,

442 bool enabled)

443{

444 return [mbox\_set\_enabled](group__mbox__interface.md#ga9eea4b9501751919125cd6124f9e9868)(spec->[dev](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52), spec->[channel\_id](structmbox__dt__spec.md#aa72163f47124446dab00d93f239b70e7), enabled);

445}

446

[ 457](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mbox\_max\_channels\_get](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)(const struct [device](structdevice.md) \*dev);

458

459static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_mbox\_max\_channels\_get(const struct [device](structdevice.md) \*dev)

460{

461 const struct mbox\_driver\_api \*api =

462 (const struct mbox\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

463

464 if (api->max\_channels\_get == NULL) {

465 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

466 }

467

468 return api->max\_channels\_get(dev);

469}

470

[ 478](group__mbox__interface.md#gad9321777457f958e9291ded26e4ed5c6)static inline int [mbox\_max\_channels\_get\_dt](group__mbox__interface.md#gad9321777457f958e9291ded26e4ed5c6)(const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec)

479{

480 return [mbox\_max\_channels\_get](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)(spec->[dev](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52));

481}

482

484

485#ifdef \_\_cplusplus

486}

487#endif

488

489#include <zephyr/syscalls/mbox.h>

490

491#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MBOX\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[errno.h](errno_8h.md)

System error numbers.

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:916

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[mbox\_set\_enabled\_dt](group__mbox__interface.md#ga50282848e03481fe8b6f5caa900892d3)

static int mbox\_set\_enabled\_dt(const struct mbox\_dt\_spec \*spec, bool enabled)

Enable (disable) interrupts and callbacks for inbound channels from a struct mbox\_dt\_spec.

**Definition** mbox.h:441

[mbox\_mtu\_get](group__mbox__interface.md#ga82d9def1b5c31c574d2114abcce2eb1f)

int mbox\_mtu\_get(const struct device \*dev)

Return the maximum number of bytes possible in an outbound message.

[mbox\_send\_dt](group__mbox__interface.md#ga8f737ce94afac19dd8924526d48c68ba)

static int mbox\_send\_dt(const struct mbox\_dt\_spec \*spec, const struct mbox\_msg \*msg)

Try to send a message over the MBOX device from a struct mbox\_dt\_spec.

**Definition** mbox.h:288

[mbox\_mtu\_get\_dt](group__mbox__interface.md#ga9565933b282fe8e5fd057fbb238e00b9)

static int mbox\_mtu\_get\_dt(const struct mbox\_dt\_spec \*spec)

Return the maximum number of bytes possible in an outbound message from struct mbox\_dt\_spec.

**Definition** mbox.h:385

[mbox\_register\_callback\_dt](group__mbox__interface.md#ga9cda3048389f4f57d425eac8257048a7)

static int mbox\_register\_callback\_dt(const struct mbox\_dt\_spec \*spec, mbox\_callback\_t cb, void \*user\_data)

Register a callback function on a channel for incoming messages from a struct mbox\_dt\_spec.

**Definition** mbox.h:336

[mbox\_set\_enabled](group__mbox__interface.md#ga9eea4b9501751919125cd6124f9e9868)

int mbox\_set\_enabled(const struct device \*dev, mbox\_channel\_id\_t channel\_id, bool enabled)

Enable (disable) interrupts and callbacks for inbound channels.

[mbox\_is\_ready\_dt](group__mbox__interface.md#gab1bea02e9f49442b7454706fb434f5f2)

static bool mbox\_is\_ready\_dt(const struct mbox\_dt\_spec \*spec)

Validate if MBOX device instance from a struct mbox\_dt\_spec is ready.

**Definition** mbox.h:239

[mbox\_register\_callback](group__mbox__interface.md#gac1cc65cc54b9c7e6cf2639152a4d6a7a)

static int mbox\_register\_callback(const struct device \*dev, mbox\_channel\_id\_t channel\_id, mbox\_callback\_t cb, void \*user\_data)

Register a callback function on a channel for incoming messages.

**Definition** mbox.h:310

[mbox\_max\_channels\_get\_dt](group__mbox__interface.md#gad9321777457f958e9291ded26e4ed5c6)

static int mbox\_max\_channels\_get\_dt(const struct mbox\_dt\_spec \*spec)

Return the maximum number of channels from a struct mbox\_dt\_spec.

**Definition** mbox.h:478

[mbox\_channel\_id\_t](group__mbox__interface.md#gaf16ce0f9d2138b63165f6e9862c9df37)

uint32\_t mbox\_channel\_id\_t

Type for MBOX channel identifiers.

**Definition** mbox.h:76

[mbox\_max\_channels\_get](group__mbox__interface.md#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)

uint32\_t mbox\_max\_channels\_get(const struct device \*dev)

Return the maximum number of channels.

[mbox\_send](group__mbox__interface.md#gaf4d02fb3a3ed788ba28a58783209d359)

int mbox\_send(const struct device \*dev, mbox\_channel\_id\_t channel\_id, const struct mbox\_msg \*msg)

Try to send a message over the MBOX device.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[stdlib.h](stdlib_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[mbox\_dt\_spec](structmbox__dt__spec.md)

MBOX specification from DT.

**Definition** mbox.h:87

[mbox\_dt\_spec::dev](structmbox__dt__spec.md#a672422e5d38633b5e2d238bf22a20a52)

const struct device \* dev

MBOX device pointer.

**Definition** mbox.h:89

[mbox\_dt\_spec::channel\_id](structmbox__dt__spec.md#aa72163f47124446dab00d93f239b70e7)

mbox\_channel\_id\_t channel\_id

Channel ID.

**Definition** mbox.h:91

[mbox\_msg](structmbox__msg.md)

Message struct (to hold data and its size).

**Definition** mbox.h:79

[mbox\_msg::size](structmbox__msg.md#a9870d0667d97e4d4ab9ba985b75e1dc4)

size\_t size

Size of the data.

**Definition** mbox.h:83

[mbox\_msg::data](structmbox__msg.md#aa9b02c7a3b1620ca2c6ffa42528cfe0c)

const void \* data

Pointer to the data sent in the message.

**Definition** mbox.h:81

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mbox.h](drivers_2mbox_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
