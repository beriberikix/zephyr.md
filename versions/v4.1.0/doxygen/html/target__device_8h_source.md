---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/target__device_8h_source.html
original_path: doxygen/html/target__device_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

17#include <[errno.h](errno_8h.md)>

18#include <stddef.h>

19#include <[stdint.h](stdint_8h.md)>

20

21#include <[zephyr/device.h](device_8h.md)>

22#include <[zephyr/sys/slist.h](slist_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28struct i3c\_driver\_api;

29

[ 36](structi3c__config__target.md)struct [i3c\_config\_target](structi3c__config__target.md) {

[ 41](structi3c__config__target.md#abbfb2e5c4d061b60f3e0f92ee17f4ee7) bool [enable](structi3c__config__target.md#abbfb2e5c4d061b60f3e0f92ee17f4ee7);

42

[ 49](structi3c__config__target.md#aac5e8a92468df108ce964bb6a9a7ae9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dynamic\_addr](structi3c__config__target.md#aac5e8a92468df108ce964bb6a9a7ae9c);

50

[ 57](structi3c__config__target.md#ab5345d23ba2afffbf48010e7edff3c26) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [static\_addr](structi3c__config__target.md#ab5345d23ba2afffbf48010e7edff3c26);

58

[ 60](structi3c__config__target.md#a62e1b1a3dff6cc570ecccdfcfc6b196d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [pid](structi3c__config__target.md#a62e1b1a3dff6cc570ecccdfcfc6b196d);

61

[ 68](structi3c__config__target.md#a2ad289658811d142ba9091574acf485b) bool [pid\_random](structi3c__config__target.md#a2ad289658811d142ba9091574acf485b);

69

[ 71](structi3c__config__target.md#a1d0b97d6428e471bcf9b6945da947b36) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcr](structi3c__config__target.md#a1d0b97d6428e471bcf9b6945da947b36);

72

[ 74](structi3c__config__target.md#afaa68c94b35f512a597b35752db8d66e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dcr](structi3c__config__target.md#afaa68c94b35f512a597b35752db8d66e);

75

[ 77](structi3c__config__target.md#a4339c8dd33b17ce8363bf28177411830) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_read\_len](structi3c__config__target.md#a4339c8dd33b17ce8363bf28177411830);

78

[ 80](structi3c__config__target.md#aca4dc4aa873ca447d06e573d485ab854) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_write\_len](structi3c__config__target.md#aca4dc4aa873ca447d06e573d485ab854);

81

[ 88](structi3c__config__target.md#a78a74f81e632a428db59803b55239419) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [supported\_hdr](structi3c__config__target.md#a78a74f81e632a428db59803b55239419);

89};

90

[ 102](structi3c__target__config.md)struct [i3c\_target\_config](structi3c__target__config.md) {

[ 103](structi3c__target__config.md#a4e0fc180a85b4ec2f9fc5d3f3b8e030b) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi3c__target__config.md#a4e0fc180a85b4ec2f9fc5d3f3b8e030b);

104

[ 109](structi3c__target__config.md#ae27fb5be1c29a3f7a38955d5954f1bf6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structi3c__target__config.md#ae27fb5be1c29a3f7a38955d5954f1bf6);

110

[ 112](structi3c__target__config.md#a89b7f8bd52beec7dd733ab6dd1111758) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [address](structi3c__target__config.md#a89b7f8bd52beec7dd733ab6dd1111758);

113

[ 115](structi3c__target__config.md#a43ed9a3679d54f7bb91dade34a5897b6) const struct [i3c\_target\_callbacks](structi3c__target__callbacks.md) \*[callbacks](structi3c__target__config.md#a43ed9a3679d54f7bb91dade34a5897b6);

116};

117

[ 118](structi3c__target__callbacks.md)struct [i3c\_target\_callbacks](structi3c__target__callbacks.md) {

[ 135](structi3c__target__callbacks.md#ad9e51587a8f86f08d065071d28241ee2) int (\*[write\_requested\_cb](structi3c__target__callbacks.md#ad9e51587a8f86f08d065071d28241ee2))(struct [i3c\_target\_config](structi3c__target__config.md) \*config);

136

[ 156](structi3c__target__callbacks.md#a7288f143d19ad306616e25e68ffedc03) int (\*[write\_received\_cb](structi3c__target__callbacks.md#a7288f143d19ad306616e25e68ffedc03))(struct [i3c\_target\_config](structi3c__target__config.md) \*config,

157 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val);

158

[ 179](structi3c__target__callbacks.md#ac72e0bab1eeff6995983f90f6d934749) int (\*[read\_requested\_cb](structi3c__target__callbacks.md#ac72e0bab1eeff6995983f90f6d934749))(struct [i3c\_target\_config](structi3c__target__config.md) \*config,

180 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val);

181

[ 202](structi3c__target__callbacks.md#ae53661cfa98a3b58a9702fef28234c30) int (\*[read\_processed\_cb](structi3c__target__callbacks.md#ae53661cfa98a3b58a9702fef28234c30))(struct [i3c\_target\_config](structi3c__target__config.md) \*config,

203 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val);

204

205#ifdef CONFIG\_I3C\_TARGET\_BUFFER\_MODE

219 void (\*buf\_write\_received\_cb)(struct [i3c\_target\_config](structi3c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ptr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len);

220

245 int (\*buf\_read\_requested\_cb)(struct [i3c\_target\_config](structi3c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ptr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*len,

246 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hdr\_mode);

247#endif

[ 263](structi3c__target__callbacks.md#a15a1bacdd10c0d6803fbd24f1a1a3323) int (\*[stop\_cb](structi3c__target__callbacks.md#a15a1bacdd10c0d6803fbd24f1a1a3323))(struct [i3c\_target\_config](structi3c__target__config.md) \*config);

264

[ 279](structi3c__target__callbacks.md#a1e92d1a9bd94b0ef3930bc692764721f) int (\*[controller\_handoff\_cb](structi3c__target__callbacks.md#a1e92d1a9bd94b0ef3930bc692764721f))(struct [i3c\_target\_config](structi3c__target__config.md) \*config);

280};

281

[ 282](structi3c__target__driver__api.md)\_\_subsystem struct [i3c\_target\_driver\_api](structi3c__target__driver__api.md) {

[ 283](structi3c__target__driver__api.md#ae4cfbf1bfa1549086d120e3ea49c3d38) int (\*[driver\_register](structi3c__target__driver__api.md#ae4cfbf1bfa1549086d120e3ea49c3d38))(const struct [device](structdevice.md) \*dev);

[ 284](structi3c__target__driver__api.md#a23fe52e8c1f700b6c39cabec667a80b8) int (\*[driver\_unregister](structi3c__target__driver__api.md#a23fe52e8c1f700b6c39cabec667a80b8))(const struct [device](structdevice.md) \*dev);

285};

286

[ 299](group__i3c__target__device.md#ga09be7f73861bede0071fd8ade344d092)static inline int [i3c\_target\_controller\_handoff](group__i3c__target__device.md#ga09be7f73861bede0071fd8ade344d092)(const struct [device](structdevice.md) \*dev,

300 bool [accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864))

301{

302 const struct i3c\_driver\_api \*api =

303 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

304

305 if (api->target\_controller\_handoff == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

306 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

307 }

308

309 return api->target\_controller\_handoff(dev, [accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864));

310}

311

[ 336](group__i3c__target__device.md#gafb5ebdfd5536ee265a3719beb8ae81dc)static inline int [i3c\_target\_tx\_write](group__i3c__target__device.md#gafb5ebdfd5536ee265a3719beb8ae81dc)(const struct [device](structdevice.md) \*dev,

337 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hdr\_mode)

338{

339 const struct i3c\_driver\_api \*api =

340 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

341

342 if (api->target\_tx\_write == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

343 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

344 }

345

346 return api->target\_tx\_write(dev, buf, len, hdr\_mode);

347}

348

[ 372](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42)static inline int [i3c\_target\_register](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42)(const struct [device](structdevice.md) \*dev,

373 struct [i3c\_target\_config](structi3c__target__config.md) \*cfg)

374{

375 const struct i3c\_driver\_api \*api =

376 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

377

378 if (api->target\_register == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

379 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

380 }

381

382 return api->target\_register(dev, cfg);

383}

384

[ 401](group__i3c__target__device.md#ga3dc0e6451fb13fa063c5ec3e18fe22e4)static inline int [i3c\_target\_unregister](group__i3c__target__device.md#ga3dc0e6451fb13fa063c5ec3e18fe22e4)(const struct [device](structdevice.md) \*dev,

402 struct [i3c\_target\_config](structi3c__target__config.md) \*cfg)

403{

404 const struct i3c\_driver\_api \*api =

405 (const struct i3c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

406

407 if (api->target\_unregister == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

408 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

409 }

410

411 return api->target\_unregister(dev, cfg);

412}

413

414#ifdef \_\_cplusplus

415}

416#endif

417

421

422#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_TARGET\_DEVICE\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[i3c\_target\_controller\_handoff](group__i3c__target__device.md#ga09be7f73861bede0071fd8ade344d092)

static int i3c\_target\_controller\_handoff(const struct device \*dev, bool accept)

Accept or Decline Controller Handoffs.

**Definition** target\_device.h:299

[i3c\_target\_unregister](group__i3c__target__device.md#ga3dc0e6451fb13fa063c5ec3e18fe22e4)

static int i3c\_target\_unregister(const struct device \*dev, struct i3c\_target\_config \*cfg)

Unregisters the provided config as target device.

**Definition** target\_device.h:401

[i3c\_target\_register](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42)

static int i3c\_target\_register(const struct device \*dev, struct i3c\_target\_config \*cfg)

Registers the provided config as target device of a controller.

**Definition** target\_device.h:372

[i3c\_target\_tx\_write](group__i3c__target__device.md#gafb5ebdfd5536ee265a3719beb8ae81dc)

static int i3c\_target\_tx\_write(const struct device \*dev, uint8\_t \*buf, uint16\_t len, uint8\_t hdr\_mode)

Writes to the target's TX FIFO.

**Definition** target\_device.h:336

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864)

int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

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

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[i3c\_config\_target](structi3c__config__target.md)

Configuration parameters for I3C hardware to act as target device.

**Definition** target\_device.h:36

[i3c\_config\_target::bcr](structi3c__config__target.md#a1d0b97d6428e471bcf9b6945da947b36)

uint8\_t bcr

Bus Characteristics Register (BCR).

**Definition** target\_device.h:71

[i3c\_config\_target::pid\_random](structi3c__config__target.md#a2ad289658811d142ba9091574acf485b)

bool pid\_random

True if lower 32-bit of Provisioned ID is random.

**Definition** target\_device.h:68

[i3c\_config\_target::max\_read\_len](structi3c__config__target.md#a4339c8dd33b17ce8363bf28177411830)

uint16\_t max\_read\_len

Maximum Read Length (MRL).

**Definition** target\_device.h:77

[i3c\_config\_target::pid](structi3c__config__target.md#a62e1b1a3dff6cc570ecccdfcfc6b196d)

uint64\_t pid

Provisioned ID.

**Definition** target\_device.h:60

[i3c\_config\_target::supported\_hdr](structi3c__config__target.md#a78a74f81e632a428db59803b55239419)

uint8\_t supported\_hdr

Bit mask of supported HDR modes (0 - 7).

**Definition** target\_device.h:88

[i3c\_config\_target::dynamic\_addr](structi3c__config__target.md#aac5e8a92468df108ce964bb6a9a7ae9c)

uint8\_t dynamic\_addr

I3C target dynamic address.

**Definition** target\_device.h:49

[i3c\_config\_target::static\_addr](structi3c__config__target.md#ab5345d23ba2afffbf48010e7edff3c26)

uint8\_t static\_addr

I3C target static address.

**Definition** target\_device.h:57

[i3c\_config\_target::enable](structi3c__config__target.md#abbfb2e5c4d061b60f3e0f92ee17f4ee7)

bool enable

If the hardware is to act as a target device on the bus.

**Definition** target\_device.h:41

[i3c\_config\_target::max\_write\_len](structi3c__config__target.md#aca4dc4aa873ca447d06e573d485ab854)

uint16\_t max\_write\_len

Maximum Write Length (MWL).

**Definition** target\_device.h:80

[i3c\_config\_target::dcr](structi3c__config__target.md#afaa68c94b35f512a597b35752db8d66e)

uint8\_t dcr

Device Characteristics Register (DCR).

**Definition** target\_device.h:74

[i3c\_target\_callbacks](structi3c__target__callbacks.md)

**Definition** target\_device.h:118

[i3c\_target\_callbacks::stop\_cb](structi3c__target__callbacks.md#a15a1bacdd10c0d6803fbd24f1a1a3323)

int(\* stop\_cb)(struct i3c\_target\_config \*config)

Function called when a stop condition is observed after a start condition addressed to a particular d...

**Definition** target\_device.h:263

[i3c\_target\_callbacks::controller\_handoff\_cb](structi3c__target__callbacks.md#a1e92d1a9bd94b0ef3930bc692764721f)

int(\* controller\_handoff\_cb)(struct i3c\_target\_config \*config)

Function called when an active controller handoffs controlership to this target.

**Definition** target\_device.h:279

[i3c\_target\_callbacks::write\_received\_cb](structi3c__target__callbacks.md#a7288f143d19ad306616e25e68ffedc03)

int(\* write\_received\_cb)(struct i3c\_target\_config \*config, uint8\_t val)

Function called when a write to the device is continued.

**Definition** target\_device.h:156

[i3c\_target\_callbacks::read\_requested\_cb](structi3c__target__callbacks.md#ac72e0bab1eeff6995983f90f6d934749)

int(\* read\_requested\_cb)(struct i3c\_target\_config \*config, uint8\_t \*val)

Function called when a read from the device is initiated.

**Definition** target\_device.h:179

[i3c\_target\_callbacks::write\_requested\_cb](structi3c__target__callbacks.md#ad9e51587a8f86f08d065071d28241ee2)

int(\* write\_requested\_cb)(struct i3c\_target\_config \*config)

Function called when a write to the device is initiated.

**Definition** target\_device.h:135

[i3c\_target\_callbacks::read\_processed\_cb](structi3c__target__callbacks.md#ae53661cfa98a3b58a9702fef28234c30)

int(\* read\_processed\_cb)(struct i3c\_target\_config \*config, uint8\_t \*val)

Function called when a read from the device is continued.

**Definition** target\_device.h:202

[i3c\_target\_config](structi3c__target__config.md)

Structure describing a device that supports the I3C target API.

**Definition** target\_device.h:102

[i3c\_target\_config::callbacks](structi3c__target__config.md#a43ed9a3679d54f7bb91dade34a5897b6)

const struct i3c\_target\_callbacks \* callbacks

Callback functions.

**Definition** target\_device.h:115

[i3c\_target\_config::node](structi3c__target__config.md#a4e0fc180a85b4ec2f9fc5d3f3b8e030b)

sys\_snode\_t node

**Definition** target\_device.h:103

[i3c\_target\_config::address](structi3c__target__config.md#a89b7f8bd52beec7dd733ab6dd1111758)

uint8\_t address

Address for this target device.

**Definition** target\_device.h:112

[i3c\_target\_config::flags](structi3c__target__config.md#ae27fb5be1c29a3f7a38955d5954f1bf6)

uint8\_t flags

Flags for the target device defined by I3C\_TARGET\_FLAGS\_\* constants.

**Definition** target\_device.h:109

[i3c\_target\_driver\_api](structi3c__target__driver__api.md)

**Definition** target\_device.h:282

[i3c\_target\_driver\_api::driver\_unregister](structi3c__target__driver__api.md#a23fe52e8c1f700b6c39cabec667a80b8)

int(\* driver\_unregister)(const struct device \*dev)

**Definition** target\_device.h:284

[i3c\_target\_driver\_api::driver\_register](structi3c__target__driver__api.md#ae4cfbf1bfa1549086d120e3ea49c3d38)

int(\* driver\_register)(const struct device \*dev)

**Definition** target\_device.h:283

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [target\_device.h](target__device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
