---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__elc_8h_source.html
original_path: doxygen/html/renesas__elc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_elc.h

[Go to the documentation of this file.](renesas__elc_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MISC\_RENESAS\_ELC\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_MISC\_RENESAS\_ELC\_H\_

14

21

22#include <[stdint.h](stdint_8h.md)>

23#include <[zephyr/sys/slist.h](slist_8h.md)>

24#include <[zephyr/device.h](device_8h.md)>

25#include <[zephyr/kernel.h](kernel_8h.md)>

26#include <[zephyr/internal/syscall\_handler.h](syscall__handler_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 42](structrenesas__elc__dt__spec.md)struct [renesas\_elc\_dt\_spec](structrenesas__elc__dt__spec.md) {

[ 44](structrenesas__elc__dt__spec.md#ae759c1c19bd7c69d14165a12331f3df4) const struct [device](structdevice.md) \*[dev](structrenesas__elc__dt__spec.md#ae759c1c19bd7c69d14165a12331f3df4);

[ 46](structrenesas__elc__dt__spec.md#a7b20982a91e3bb944c7aaf94b6fd33dd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [peripheral](structrenesas__elc__dt__spec.md#a7b20982a91e3bb944c7aaf94b6fd33dd);

[ 48](structrenesas__elc__dt__spec.md#a9004b468890e2901b4316e9f2fa648ea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [event](structrenesas__elc__dt__spec.md#a9004b468890e2901b4316e9f2fa648ea);

49};

50

[ 59](group__renesas__elc__interface.md#ga32d4b23c3857552a8fe1ca6ce04f97d4)#define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME(node\_id, name) \

60 DEVICE\_DT\_GET(DT\_PHANDLE\_BY\_NAME(node\_id, renesas\_elcs, name))

61

[ 70](group__renesas__elc__interface.md#ga79a705be3efa01b6fcc1413dd4acfec2)#define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX(node\_id, idx) \

71 DEVICE\_DT\_GET(DT\_PHANDLE\_BY\_IDX(node\_id, renesas\_elcs, idx))

72

[ 82](group__renesas__elc__interface.md#ga996e259c97fc2511086664865b4c0e3d)#define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME\_OR\_NULL(node\_id, name) \

83 DEVICE\_DT\_GET\_OR\_NULL(DT\_PHANDLE\_BY\_NAME(node\_id, renesas\_elcs, name))

84

[ 94](group__renesas__elc__interface.md#ga5e79207cee205406247a972e23360110)#define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX\_OR\_NULL(node\_id, idx) \

95 DEVICE\_DT\_GET\_OR\_NULL(DT\_PHANDLE\_BY\_IDX(node\_id, renesas\_elcs, idx))

96

[ 106](group__renesas__elc__interface.md#gaab4d583c93f1d5990d4a6733caaded81)#define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME(inst, name) \

107 DEVICE\_DT\_GET(DT\_PHANDLE\_BY\_NAME(DT\_DRV\_INST(inst), renesas\_elcs, name))

108

[ 118](group__renesas__elc__interface.md#ga788709121dbfb2db3f74ccf9a9d51002)#define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX(inst, idx) \

119 DEVICE\_DT\_GET(DT\_PHANDLE\_BY\_IDX(DT\_DRV\_INST(inst), renesas\_elcs, idx))

120

[ 130](group__renesas__elc__interface.md#ga1d58940758c664c22cb3e183e9810370)#define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME\_OR\_NULL(inst, name) \

131 DEVICE\_DT\_GET\_OR\_NULL(DT\_PHANDLE\_BY\_NAME(DT\_DRV\_INST(inst), renesas\_elcs, name))

132

[ 142](group__renesas__elc__interface.md#ga65ccb580212ee15dc9329d76e810190e)#define RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX\_OR\_NULL(inst, idx) \

143 DEVICE\_DT\_GET\_OR\_NULL(DT\_PHANDLE\_BY\_IDX(DT\_DRV\_INST(inst), renesas\_elcs, idx))

144

[ 153](group__renesas__elc__interface.md#ga1f196ad20380dedf193c754906c5ed14)#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME(node\_id, name) \

154 DT\_PHA\_BY\_NAME(node\_id, renesas\_elcs, name, peripheral)

155

[ 164](group__renesas__elc__interface.md#gace33f51f3a3a2efd42932a816e05be0b)#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX(node\_id, idx) \

165 DT\_PHA\_BY\_IDX(node\_id, renesas\_elcs, idx, peripheral)

166

[ 177](group__renesas__elc__interface.md#ga35d7aef6829d74e92fa7c82306711a6c)#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR(node\_id, name, default\_value) \

178 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, renesas\_elcs), \

179 (RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME(node\_id, name)), \

180 (default\_value))

181

[ 192](group__renesas__elc__interface.md#ga915d2760bd3c8ecf1b689bed286035d8)#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value) \

193 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, renesas\_elcs), \

194 (RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX(node\_id, idx)), \

195 (default\_value))

196

[ 205](group__renesas__elc__interface.md#ga3a0b277cb45636a86bf9b665fd75d133)#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME(inst, name) \

206 RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME(DT\_DRV\_INST(inst), name)

207

[ 216](group__renesas__elc__interface.md#gaeab186e0f09ee56ce87719a7d5566f50)#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX(inst, idx) \

217 RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX(DT\_DRV\_INST(inst), idx)

218

[ 229](group__renesas__elc__interface.md#ga0e1c393825d778fd22a9a190eaedc308)#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME\_OR(inst, name, default\_value) \

230 RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

231

[ 242](group__renesas__elc__interface.md#ga360d362b3fc26afb7cc81bfd28f6fc6a)#define RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX\_OR(inst, idx, default\_value) \

243 RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR(DT\_DRV\_INST(inst), idx, default\_value)

244

[ 253](group__renesas__elc__interface.md#ga920e3b26fb52a728ed2a3cd1ab5af7f0)#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME(node\_id, name) \

254 DT\_PHA\_BY\_NAME(node\_id, renesas\_elcs, name, event)

255

[ 264](group__renesas__elc__interface.md#ga6f3093b0556eb8eb1931e9b8b746245a)#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX(node\_id, idx) \

265 DT\_PHA\_BY\_IDX(node\_id, renesas\_elcs, idx, event)

266

[ 277](group__renesas__elc__interface.md#ga41c5adcf8817d529b5521727d9937b42)#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR(node\_id, name, default\_value) \

278 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, renesas\_elcs), \

279 (RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME(node\_id, name)), \

280 (default\_value))

281

[ 292](group__renesas__elc__interface.md#ga2b0a12781acca4123dd7899446a94b6f)#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value) \

293 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, renesas\_elcs), \

294 (RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX(node\_id, idx)), \

295 (default\_value))

296

[ 305](group__renesas__elc__interface.md#ga86ded9427001c5d3b315b71dcbfad7d0)#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME(inst, name) \

306 RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME(DT\_DRV\_INST(inst), name)

307

[ 316](group__renesas__elc__interface.md#gac5dfa5e30e1ac9ac703842e61dd3fa3b)#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX(inst, idx) \

317 RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX(DT\_DRV\_INST(inst), idx)

318

[ 329](group__renesas__elc__interface.md#ga94f2bc95761722c93019371f432da262)#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME\_OR(inst, name, default\_value) \

330 RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR(DT\_DRV\_INST(inst), name, default\_value)

331

[ 342](group__renesas__elc__interface.md#ga7d57a1a3bf47feda6c2831712bfd033c)#define RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX\_OR(inst, idx, default\_value) \

343 RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR(DT\_DRV\_INST(inst), idx, default\_value)

344

352\_\_subsystem struct renesas\_elc\_driver\_api {

353 int (\*software\_event\_generate)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event);

354 int (\*link\_set)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69));

355 int (\*link\_break)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral);

356 int (\*enable)(const struct [device](structdevice.md) \*dev);

357 int (\*disable)(const struct [device](structdevice.md) \*dev);

358};

359

363

[ 376](group__renesas__elc__interface.md#gab3b55b83b38469854aae726a71f6ad55)\_\_syscall int [renesas\_elc\_software\_event\_generate](group__renesas__elc__interface.md#gab3b55b83b38469854aae726a71f6ad55)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event);

377

378static inline int z\_impl\_renesas\_elc\_software\_event\_generate(const struct [device](structdevice.md) \*dev,

379 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event)

380{

381 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(renesas\_elc, dev)->software\_event\_generate(dev, event);

382}

383

[ 397](group__renesas__elc__interface.md#ga444e17d01310283e61bcde9a1022c47a)\_\_syscall int [renesas\_elc\_link\_set](group__renesas__elc__interface.md#ga444e17d01310283e61bcde9a1022c47a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event);

398

399static inline int z\_impl\_renesas\_elc\_link\_set(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral,

400 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event)

401{

402 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(renesas\_elc, dev)->link\_set(dev, peripheral, event);

403}

404

[ 416](group__renesas__elc__interface.md#ga65c950ccf0087c514daf6d543a0a7ecf)\_\_syscall int [renesas\_elc\_link\_break](group__renesas__elc__interface.md#ga65c950ccf0087c514daf6d543a0a7ecf)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral);

417

418static inline int z\_impl\_renesas\_elc\_link\_break(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral)

419{

420 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(renesas\_elc, dev)->link\_break(dev, peripheral);

421}

422

[ 433](group__renesas__elc__interface.md#gafbffc029fd9482be578bd05cbdb3a03f)\_\_syscall int [renesas\_elc\_enable](group__renesas__elc__interface.md#gafbffc029fd9482be578bd05cbdb3a03f)(const struct [device](structdevice.md) \*dev);

434

435static inline int z\_impl\_renesas\_elc\_enable(const struct [device](structdevice.md) \*dev)

436{

437 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(renesas\_elc, dev)->enable(dev);

438}

439

[ 450](group__renesas__elc__interface.md#gaac75089657f841c80225aa40de9c2a93)\_\_syscall int [renesas\_elc\_disable](group__renesas__elc__interface.md#gaac75089657f841c80225aa40de9c2a93)(const struct [device](structdevice.md) \*dev);

451

452static inline int z\_impl\_renesas\_elc\_disable(const struct [device](structdevice.md) \*dev)

453{

454 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(renesas\_elc, dev)->disable(dev);

455}

456

460

461#ifdef \_\_cplusplus

462}

463#endif

464

465#include <zephyr/syscalls/renesas\_elc.h>

466

467#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MISC\_RENESAS\_ELC\_H\_ \*/

[device.h](device_8h.md)

[DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)

#define DEVICE\_API\_GET(\_class, \_dev)

Expands to the pointer of a device's API for a given class.

**Definition** device.h:1350

[renesas\_elc\_link\_set](group__renesas__elc__interface.md#ga444e17d01310283e61bcde9a1022c47a)

int renesas\_elc\_link\_set(const struct device \*dev, uint32\_t peripheral, uint32\_t event)

Create a single event link.

[renesas\_elc\_link\_break](group__renesas__elc__interface.md#ga65c950ccf0087c514daf6d543a0a7ecf)

int renesas\_elc\_link\_break(const struct device \*dev, uint32\_t peripheral)

Break an event link.

[renesas\_elc\_disable](group__renesas__elc__interface.md#gaac75089657f841c80225aa40de9c2a93)

int renesas\_elc\_disable(const struct device \*dev)

Disable the operation of the Event Link Controller.

[renesas\_elc\_software\_event\_generate](group__renesas__elc__interface.md#gab3b55b83b38469854aae726a71f6ad55)

int renesas\_elc\_software\_event\_generate(const struct device \*dev, uint32\_t event)

Generate a software event in the Event Link Controller.

[renesas\_elc\_enable](group__renesas__elc__interface.md#gafbffc029fd9482be578bd05cbdb3a03f)

int renesas\_elc\_enable(const struct device \*dev)

Enable the operation of the Event Link Controller.

[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)

sighandler\_t signal(int signo, sighandler\_t handler)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[renesas\_elc\_dt\_spec](structrenesas__elc__dt__spec.md)

Container for Renesas ELC information specified in devicetree.

**Definition** renesas\_elc.h:42

[renesas\_elc\_dt\_spec::peripheral](structrenesas__elc__dt__spec.md#a7b20982a91e3bb944c7aaf94b6fd33dd)

uint32\_t peripheral

Renesas ELC peripheral ID.

**Definition** renesas\_elc.h:46

[renesas\_elc\_dt\_spec::event](structrenesas__elc__dt__spec.md#a9004b468890e2901b4316e9f2fa648ea)

uint32\_t event

Renesas ELC event ID.

**Definition** renesas\_elc.h:48

[renesas\_elc\_dt\_spec::dev](structrenesas__elc__dt__spec.md#ae759c1c19bd7c69d14165a12331f3df4)

const struct device \* dev

Renesas ELC device instance.

**Definition** renesas\_elc.h:44

[syscall\_handler.h](syscall__handler_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [interconn](dir_433d0485cb495c15eb8c324a866644da.md)
- [renesas\_elc](dir_41f42e06f91d3fe7cdafa18f2f825332.md)
- [renesas\_elc.h](renesas__elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
