---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/target__device_8h_source.html
original_path: doxygen/html/target__device_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

target\_device.h

[Go to the documentation of this file.](target__device_8h.md)

1/\*

2 \* Copyright 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_TARGET\_DEVICE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_TARGET\_DEVICE\_H\_

9

16

17#include <[zephyr/device.h](device_8h.md)>

18#include <[zephyr/kernel.h](kernel_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <[zephyr/sys/util.h](util_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26struct i3c\_driver\_api;

27

[ 34](structi3c__config__target.md)struct [i3c\_config\_target](structi3c__config__target.md) {

[ 39](structi3c__config__target.md#abbfb2e5c4d061b60f3e0f92ee17f4ee7) bool [enable](structi3c__config__target.md#abbfb2e5c4d061b60f3e0f92ee17f4ee7);

40

[ 47](structi3c__config__target.md#ab5345d23ba2afffbf48010e7edff3c26) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__config__target.md#ab5345d23ba2afffbf48010e7edff3c26);

48

[ 50](structi3c__config__target.md#a62e1b1a3dff6cc570ecccdfcfc6b196d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pid](structi3c__config__target.md#a62e1b1a3dff6cc570ecccdfcfc6b196d);

51

[ 58](structi3c__config__target.md#a2ad289658811d142ba9091574acf485b) bool [pid\_random](structi3c__config__target.md#a2ad289658811d142ba9091574acf485b);

59

[ 61](structi3c__config__target.md#a1d0b97d6428e471bcf9b6945da947b36) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__config__target.md#a1d0b97d6428e471bcf9b6945da947b36);

62

[ 64](structi3c__config__target.md#afaa68c94b35f512a597b35752db8d66e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__config__target.md#afaa68c94b35f512a597b35752db8d66e);

65

[ 67](structi3c__config__target.md#a4339c8dd33b17ce8363bf28177411830) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_read\_len](structi3c__config__target.md#a4339c8dd33b17ce8363bf28177411830);

68

[ 70](structi3c__config__target.md#aca4dc4aa873ca447d06e573d485ab854) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_write\_len](structi3c__config__target.md#aca4dc4aa873ca447d06e573d485ab854);

71

[ 78](structi3c__config__target.md#a78a74f81e632a428db59803b55239419) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [supported\_hdr](structi3c__config__target.md#a78a74f81e632a428db59803b55239419);

79};

80

[ 92](structi3c__target__config.md)struct [i3c\_target\_config](structi3c__target__config.md) {

[ 94](structi3c__target__config.md#a4e0fc180a85b4ec2f9fc5d3f3b8e030b) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi3c__target__config.md#a4e0fc180a85b4ec2f9fc5d3f3b8e030b);

95

[ 100](structi3c__target__config.md#ae27fb5be1c29a3f7a38955d5954f1bf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structi3c__target__config.md#ae27fb5be1c29a3f7a38955d5954f1bf6);

101

[ 103](structi3c__target__config.md#a89b7f8bd52beec7dd733ab6dd1111758) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [address](structi3c__target__config.md#a89b7f8bd52beec7dd733ab6dd1111758);

104

[ 106](structi3c__target__config.md#a43ed9a3679d54f7bb91dade34a5897b6) const struct [i3c\_target\_callbacks](structi3c__target__callbacks.md) \*[callbacks](structi3c__target__config.md#a43ed9a3679d54f7bb91dade34a5897b6);

107};

108

[ 109](structi3c__target__callbacks.md)struct [i3c\_target\_callbacks](structi3c__target__callbacks.md) {

[ 126](structi3c__target__callbacks.md#ad9e51587a8f86f08d065071d28241ee2) int (\*[write\_requested\_cb](structi3c__target__callbacks.md#ad9e51587a8f86f08d065071d28241ee2))(struct [i3c\_target\_config](structi3c__target__config.md) \*config);

127

[ 147](structi3c__target__callbacks.md#a7288f143d19ad306616e25e68ffedc03) int (\*[write\_received\_cb](structi3c__target__callbacks.md#a7288f143d19ad306616e25e68ffedc03))(struct [i3c\_target\_config](structi3c__target__config.md) \*config,

148 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val);

149

[ 170](structi3c__target__callbacks.md#ac72e0bab1eeff6995983f90f6d934749) int (\*[read\_requested\_cb](structi3c__target__callbacks.md#ac72e0bab1eeff6995983f90f6d934749))(struct [i3c\_target\_config](structi3c__target__config.md) \*config,

171 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val);

172

[ 193](structi3c__target__callbacks.md#ae53661cfa98a3b58a9702fef28234c30) int (\*[read\_processed\_cb](structi3c__target__callbacks.md#ae53661cfa98a3b58a9702fef28234c30))(struct [i3c\_target\_config](structi3c__target__config.md) \*config,

194 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val);

195

[ 211](structi3c__target__callbacks.md#a15a1bacdd10c0d6803fbd24f1a1a3323) int (\*[stop\_cb](structi3c__target__callbacks.md#a15a1bacdd10c0d6803fbd24f1a1a3323))(struct [i3c\_target\_config](structi3c__target__config.md) \*config);

212};

213

[ 214](structi3c__target__driver__api.md)\_\_subsystem struct [i3c\_target\_driver\_api](structi3c__target__driver__api.md) {

[ 215](structi3c__target__driver__api.md#ae4cfbf1bfa1549086d120e3ea49c3d38) int (\*[driver\_register](structi3c__target__driver__api.md#ae4cfbf1bfa1549086d120e3ea49c3d38))(const struct [device](structdevice.md) \*dev);

[ 216](structi3c__target__driver__api.md#a23fe52e8c1f700b6c39cabec667a80b8) int (\*[driver\_unregister](structi3c__target__driver__api.md#a23fe52e8c1f700b6c39cabec667a80b8))(const struct [device](structdevice.md) \*dev);

217};

218

[ 242](group__i3c__target__device.md#ga5d9e529f4c2eeccbedf491532dc209e2)static inline int [i3c\_target\_tx\_write](group__i3c__target__device.md#ga5d9e529f4c2eeccbedf491532dc209e2)(const struct [device](structdevice.md) \*dev,

243 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

244{

245 const struct i3c\_driver\_api \*api =

246 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

247

248 if (api->target\_tx\_write == NULL) {

249 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

250 }

251

252 return api->target\_tx\_write(dev, buf, len);

253}

254

[ 278](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42)static inline int [i3c\_target\_register](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42)(const struct [device](structdevice.md) \*dev,

279 struct [i3c\_target\_config](structi3c__target__config.md) \*cfg)

280{

281 const struct i3c\_driver\_api \*api =

282 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

283

284 if (api->target\_register == NULL) {

285 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

286 }

287

288 return api->target\_register(dev, cfg);

289}

290

[ 307](group__i3c__target__device.md#ga3dc0e6451fb13fa063c5ec3e18fe22e4)static inline int [i3c\_target\_unregister](group__i3c__target__device.md#ga3dc0e6451fb13fa063c5ec3e18fe22e4)(const struct [device](structdevice.md) \*dev,

308 struct [i3c\_target\_config](structi3c__target__config.md) \*cfg)

309{

310 const struct i3c\_driver\_api \*api =

311 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

312

313 if (api->target\_unregister == NULL) {

314 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

315 }

316

317 return api->target\_unregister(dev, cfg);

318}

319

320#ifdef \_\_cplusplus

321}

322#endif

323

327

328#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_TARGET\_DEVICE\_H\_ \*/

[device.h](device_8h.md)

[i3c\_target\_unregister](group__i3c__target__device.md#ga3dc0e6451fb13fa063c5ec3e18fe22e4)

static int i3c\_target\_unregister(const struct device \*dev, struct i3c\_target\_config \*cfg)

Unregisters the provided config as target device.

**Definition** target\_device.h:307

[i3c\_target\_tx\_write](group__i3c__target__device.md#ga5d9e529f4c2eeccbedf491532dc209e2)

static int i3c\_target\_tx\_write(const struct device \*dev, uint8\_t \*buf, uint16\_t len)

Writes to the target's TX FIFO.

**Definition** target\_device.h:242

[i3c\_target\_register](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42)

static int i3c\_target\_register(const struct device \*dev, struct i3c\_target\_config \*cfg)

Registers the provided config as target device of a controller.

**Definition** target\_device.h:278

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[i3c\_config\_target](structi3c__config__target.md)

Configuration parameters for I3C hardware to act as target device.

**Definition** target\_device.h:34

[i3c\_config\_target::bcr](structi3c__config__target.md#a1d0b97d6428e471bcf9b6945da947b36)

uint8\_t bcr

Bus Characteristics Register (BCR).

**Definition** target\_device.h:61

[i3c\_config\_target::pid\_random](structi3c__config__target.md#a2ad289658811d142ba9091574acf485b)

bool pid\_random

True if lower 32-bit of Provisioned ID is random.

**Definition** target\_device.h:58

[i3c\_config\_target::max\_read\_len](structi3c__config__target.md#a4339c8dd33b17ce8363bf28177411830)

uint16\_t max\_read\_len

Maximum Read Length (MRL).

**Definition** target\_device.h:67

[i3c\_config\_target::pid](structi3c__config__target.md#a62e1b1a3dff6cc570ecccdfcfc6b196d)

uint64\_t pid

Provisioned ID.

**Definition** target\_device.h:50

[i3c\_config\_target::supported\_hdr](structi3c__config__target.md#a78a74f81e632a428db59803b55239419)

uint8\_t supported\_hdr

Bit mask of supported HDR modes (0 - 7).

**Definition** target\_device.h:78

[i3c\_config\_target::static\_addr](structi3c__config__target.md#ab5345d23ba2afffbf48010e7edff3c26)

uint8\_t static\_addr

I3C target address.

**Definition** target\_device.h:47

[i3c\_config\_target::enable](structi3c__config__target.md#abbfb2e5c4d061b60f3e0f92ee17f4ee7)

bool enable

If the hardware is to act as a target device on the bus.

**Definition** target\_device.h:39

[i3c\_config\_target::max\_write\_len](structi3c__config__target.md#aca4dc4aa873ca447d06e573d485ab854)

uint16\_t max\_write\_len

Maximum Write Length (MWL).

**Definition** target\_device.h:70

[i3c\_config\_target::dcr](structi3c__config__target.md#afaa68c94b35f512a597b35752db8d66e)

uint8\_t dcr

Device Characteristics Register (DCR).

**Definition** target\_device.h:64

[i3c\_target\_callbacks](structi3c__target__callbacks.md)

**Definition** target\_device.h:109

[i3c\_target\_callbacks::stop\_cb](structi3c__target__callbacks.md#a15a1bacdd10c0d6803fbd24f1a1a3323)

int(\* stop\_cb)(struct i3c\_target\_config \*config)

Function called when a stop condition is observed after a start condition addressed to a particular d...

**Definition** target\_device.h:211

[i3c\_target\_callbacks::write\_received\_cb](structi3c__target__callbacks.md#a7288f143d19ad306616e25e68ffedc03)

int(\* write\_received\_cb)(struct i3c\_target\_config \*config, uint8\_t val)

Function called when a write to the device is continued.

**Definition** target\_device.h:147

[i3c\_target\_callbacks::read\_requested\_cb](structi3c__target__callbacks.md#ac72e0bab1eeff6995983f90f6d934749)

int(\* read\_requested\_cb)(struct i3c\_target\_config \*config, uint8\_t \*val)

Function called when a read from the device is initiated.

**Definition** target\_device.h:170

[i3c\_target\_callbacks::write\_requested\_cb](structi3c__target__callbacks.md#ad9e51587a8f86f08d065071d28241ee2)

int(\* write\_requested\_cb)(struct i3c\_target\_config \*config)

Function called when a write to the device is initiated.

**Definition** target\_device.h:126

[i3c\_target\_callbacks::read\_processed\_cb](structi3c__target__callbacks.md#ae53661cfa98a3b58a9702fef28234c30)

int(\* read\_processed\_cb)(struct i3c\_target\_config \*config, uint8\_t \*val)

Function called when a read from the device is continued.

**Definition** target\_device.h:193

[i3c\_target\_config](structi3c__target__config.md)

Structure describing a device that supports the I3C target API.

**Definition** target\_device.h:92

[i3c\_target\_config::callbacks](structi3c__target__config.md#a43ed9a3679d54f7bb91dade34a5897b6)

const struct i3c\_target\_callbacks \* callbacks

Callback functions.

**Definition** target\_device.h:106

[i3c\_target\_config::node](structi3c__target__config.md#a4e0fc180a85b4ec2f9fc5d3f3b8e030b)

sys\_snode\_t node

Private, do not modify.

**Definition** target\_device.h:94

[i3c\_target\_config::address](structi3c__target__config.md#a89b7f8bd52beec7dd733ab6dd1111758)

uint8\_t address

Address for this target device.

**Definition** target\_device.h:103

[i3c\_target\_config::flags](structi3c__target__config.md#ae27fb5be1c29a3f7a38955d5954f1bf6)

uint8\_t flags

Flags for the target device defined by I3C\_TARGET\_FLAGS\_\* constants.

**Definition** target\_device.h:100

[i3c\_target\_driver\_api](structi3c__target__driver__api.md)

**Definition** target\_device.h:214

[i3c\_target\_driver\_api::driver\_unregister](structi3c__target__driver__api.md#a23fe52e8c1f700b6c39cabec667a80b8)

int(\* driver\_unregister)(const struct device \*dev)

**Definition** target\_device.h:216

[i3c\_target\_driver\_api::driver\_register](structi3c__target__driver__api.md#ae4cfbf1bfa1549086d120e3ea49c3d38)

int(\* driver\_register)(const struct device \*dev)

**Definition** target\_device.h:215

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [target\_device.h](target__device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
