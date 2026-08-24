---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pm_2device_8h_source.html
original_path: doxygen/html/pm_2device_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device.h

[Go to the documentation of this file.](pm_2device_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PM\_DEVICE\_H\_

8#define ZEPHYR\_INCLUDE\_PM\_DEVICE\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

13#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

25

27

28struct [device](structdevice.md);

29

31enum pm\_device\_flag {

33 PM\_DEVICE\_FLAG\_BUSY,

35 PM\_DEVICE\_FLAG\_TURN\_ON\_FAILED,

37 PM\_DEVICE\_FLAG\_PD\_CLAIMED,

42 PM\_DEVICE\_FLAG\_WS\_CAPABLE,

44 PM\_DEVICE\_FLAG\_WS\_ENABLED,

46 PM\_DEVICE\_FLAG\_RUNTIME\_ENABLED,

48 PM\_DEVICE\_FLAG\_PD,

50 PM\_DEVICE\_FLAG\_RUNTIME\_AUTO,

52 PM\_DEVICE\_FLAG\_ISR\_SAFE,

53};

54

56

[ 65](group__subsys__pm__device.md#ga18bb96fc4d5003516ab2eaf73cb35912)#define PM\_DEVICE\_ISR\_SAFE 1

66

[ 68](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6)enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) {

[ 70](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7) [PM\_DEVICE\_STATE\_ACTIVE](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7),

[ 77](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5) [PM\_DEVICE\_STATE\_SUSPENDED](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5),

[ 79](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a51a5904aff980deff73d29568b6f7deb) [PM\_DEVICE\_STATE\_SUSPENDING](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a51a5904aff980deff73d29568b6f7deb),

[ 86](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2) [PM\_DEVICE\_STATE\_OFF](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2)

87};

88

[ 90](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c)enum [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) {

[ 92](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca5b7ae11deaee85eb0b8452bc89383790) [PM\_DEVICE\_ACTION\_SUSPEND](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca5b7ae11deaee85eb0b8452bc89383790),

[ 94](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca757c6ab81eeac0d6afae479d6a0ac564) [PM\_DEVICE\_ACTION\_RESUME](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca757c6ab81eeac0d6afae479d6a0ac564),

[ 100](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca2bcd7dee3a85b27157bbc465bacf521e) [PM\_DEVICE\_ACTION\_TURN\_OFF](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca2bcd7dee3a85b27157bbc465bacf521e),

[ 106](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4cac7690e0ffd27742acf58fdbdb7b89544) [PM\_DEVICE\_ACTION\_TURN\_ON](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4cac7690e0ffd27742acf58fdbdb7b89544),

107};

108

[ 119](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179)typedef int (\*[pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179))(const struct [device](structdevice.md) \*dev,

120 enum [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) action);

121

[ 130](group__subsys__pm__device.md#ga9cfb6437873089714635d2b26aafefac)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[pm\_device\_action\_failed\_cb\_t](group__subsys__pm__device.md#ga9cfb6437873089714635d2b26aafefac))(const struct [device](structdevice.md) \*dev,

131 int err);

132

[ 139](structpm__device__base.md)struct [pm\_device\_base](structpm__device__base.md) {

[ 141](structpm__device__base.md#af9a24c7aaa0425b335fe147908c1fd4d) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](structpm__device__base.md#af9a24c7aaa0425b335fe147908c1fd4d);

[ 143](structpm__device__base.md#af4c9ef16800538148dcfa1d93b69bccb) enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) [state](structpm__device__base.md#af4c9ef16800538148dcfa1d93b69bccb);

[ 145](structpm__device__base.md#abd3a07f0e7c54cb0bee7f835be79dac6) [pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179) [action\_cb](structpm__device__base.md#abd3a07f0e7c54cb0bee7f835be79dac6);

146#if defined(CONFIG\_PM\_DEVICE\_RUNTIME) || defined(\_\_DOXYGEN\_\_)

[ 148](structpm__device__base.md#a4a9eeb093de1b1e60222b25a06a6361d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [usage](structpm__device__base.md#a4a9eeb093de1b1e60222b25a06a6361d);

149#endif /\* CONFIG\_PM\_DEVICE\_RUNTIME \*/

150#ifdef CONFIG\_PM\_DEVICE\_POWER\_DOMAIN

152 const struct [device](structdevice.md) \*domain;

153#endif /\* CONFIG\_PM\_DEVICE\_POWER\_DOMAIN \*/

154};

155

[ 163](structpm__device.md)struct [pm\_device](structpm__device.md) {

[ 165](structpm__device.md#afb5db0142ebab7891a42f71b59fd55cb) struct [pm\_device\_base](structpm__device__base.md) [base](structpm__device.md#afb5db0142ebab7891a42f71b59fd55cb);

166#if defined(CONFIG\_PM\_DEVICE\_RUNTIME) || defined(\_\_DOXYGEN\_\_)

[ 168](structpm__device.md#aec09c5708cda21c6e3af2a4e7082b432) const struct [device](structdevice.md) \*[dev](structpm__device.md#aec09c5708cda21c6e3af2a4e7082b432);

[ 170](structpm__device.md#ab7e54f9195359f60cc0a4b06677df0c7) struct [k\_sem](structk__sem.md) [lock](structpm__device.md#ab7e54f9195359f60cc0a4b06677df0c7);

[ 172](structpm__device.md#aa8ed27c6c0cff89062922bedae4dca35) struct [k\_event](structk__event.md) [event](structpm__device.md#aa8ed27c6c0cff89062922bedae4dca35);

173#if defined(CONFIG\_PM\_DEVICE\_RUNTIME\_ASYNC) || defined(\_\_DOXYGEN\_\_)

[ 175](structpm__device.md#a5dc3b48b3139d546206c8b9cacaf09fd) struct [k\_work\_delayable](structk__work__delayable.md) [work](structpm__device.md#a5dc3b48b3139d546206c8b9cacaf09fd);

176#endif /\* CONFIG\_PM\_DEVICE\_RUNTIME\_ASYNC \*/

177#endif /\* CONFIG\_PM\_DEVICE\_RUNTIME \*/

178};

179

[ 187](structpm__device__isr.md)struct [pm\_device\_isr](structpm__device__isr.md) {

[ 189](structpm__device__isr.md#ad501eabcd3370e9edb6b0851928fd7ac) struct [pm\_device\_base](structpm__device__base.md) [base](structpm__device__isr.md#ad501eabcd3370e9edb6b0851928fd7ac);

190#if defined(CONFIG\_PM\_DEVICE\_RUNTIME) || defined(\_\_DOXYGEN\_\_)

[ 192](structpm__device__isr.md#a24d7dd68bb57794be25450389fc95b33) struct [k\_spinlock](structk__spinlock.md) [lock](structpm__device__isr.md#a24d7dd68bb57794be25450389fc95b33);

193#endif

194};

195

196/\* Base part must be the first element. \*/

197BUILD\_ASSERT(offsetof(struct [pm\_device](structpm__device.md), base) == 0);

198BUILD\_ASSERT(offsetof(struct [pm\_device\_isr](structpm__device__isr.md), base) == 0);

199

201

202#ifdef CONFIG\_PM\_DEVICE\_RUNTIME

203#define Z\_PM\_DEVICE\_RUNTIME\_INIT(obj) \

204 .lock = Z\_SEM\_INITIALIZER(obj.lock, 1, 1), \

205 .event = Z\_EVENT\_INITIALIZER(obj.event),

206#else

207#define Z\_PM\_DEVICE\_RUNTIME\_INIT(obj)

208#endif /\* CONFIG\_PM\_DEVICE\_RUNTIME \*/

209

210#ifdef CONFIG\_PM\_DEVICE\_POWER\_DOMAIN

211#define Z\_PM\_DEVICE\_POWER\_DOMAIN\_INIT(\_node\_id) \

212 .domain = DEVICE\_DT\_GET\_OR\_NULL(DT\_PHANDLE(\_node\_id, \

213 power\_domains)),

214#else

215#define Z\_PM\_DEVICE\_POWER\_DOMAIN\_INIT(obj)

216#endif /\* CONFIG\_PM\_DEVICE\_POWER\_DOMAIN \*/

217

223#define Z\_PM\_DEVICE\_FLAGS(node\_id) \

224 (COND\_CODE\_1( \

225 DT\_NODE\_EXISTS(node\_id), \

226 ((DT\_PROP\_OR(node\_id, wakeup\_source, 0) \

227 << PM\_DEVICE\_FLAG\_WS\_CAPABLE) | \

228 (DT\_PROP\_OR(node\_id, zephyr\_pm\_device\_runtime\_auto, 0) \

229 << PM\_DEVICE\_FLAG\_RUNTIME\_AUTO) | \

230 (DT\_NODE\_HAS\_COMPAT(node\_id, power\_domain) << \

231 PM\_DEVICE\_FLAG\_PD)), \

232 (0)))

233

245#define Z\_PM\_DEVICE\_BASE\_INIT(obj, node\_id, pm\_action\_cb, \_flags) \

246 { \

247 .flags = ATOMIC\_INIT(Z\_PM\_DEVICE\_FLAGS(node\_id) | (\_flags)), \

248 .state = PM\_DEVICE\_STATE\_ACTIVE, \

249 .action\_cb = pm\_action\_cb, \

250 Z\_PM\_DEVICE\_POWER\_DOMAIN\_INIT(node\_id) \

251 }

252

263#define Z\_PM\_DEVICE\_INIT(obj, node\_id, pm\_action\_cb, isr\_safe) \

264 { \

265 .base = Z\_PM\_DEVICE\_BASE\_INIT(obj, node\_id, pm\_action\_cb, \

266 isr\_safe ? BIT(PM\_DEVICE\_FLAG\_ISR\_SAFE) : 0), \

267 COND\_CODE\_1(isr\_safe, (), (Z\_PM\_DEVICE\_RUNTIME\_INIT(obj))) \

268 }

269

275#define Z\_PM\_DEVICE\_NAME(dev\_id) \_CONCAT(\_\_pm\_device\_, dev\_id)

276

277#ifdef CONFIG\_PM

289#define Z\_PM\_DEVICE\_DEFINE\_SLOT(dev\_id) \

290 static STRUCT\_SECTION\_ITERABLE\_ALTERNATE(pm\_device\_slots, device, \

291 \_CONCAT(\_\_pm\_slot\_, dev\_id))

292#else

293#define Z\_PM\_DEVICE\_DEFINE\_SLOT(dev\_id)

294#endif /\* CONFIG\_PM \*/

295

296#ifdef CONFIG\_PM\_DEVICE

304#define Z\_PM\_DEVICE\_DEFINE(node\_id, dev\_id, pm\_action\_cb, isr\_safe) \

305 Z\_PM\_DEVICE\_DEFINE\_SLOT(dev\_id); \

306 static struct COND\_CODE\_1(isr\_safe, (pm\_device\_isr), (pm\_device)) \

307 Z\_PM\_DEVICE\_NAME(dev\_id) = \

308 Z\_PM\_DEVICE\_INIT(Z\_PM\_DEVICE\_NAME(dev\_id), node\_id, \

309 pm\_action\_cb, isr\_safe)

310

316#define Z\_PM\_DEVICE\_GET(dev\_id) ((struct pm\_device\_base \*)&Z\_PM\_DEVICE\_NAME(dev\_id))

317

318#else

319#define Z\_PM\_DEVICE\_DEFINE(node\_id, dev\_id, pm\_action\_cb, isr\_safe)

320#define Z\_PM\_DEVICE\_GET(dev\_id) NULL

321#endif /\* CONFIG\_PM\_DEVICE \*/

322

324

[ 336](group__subsys__pm__device.md#gae85fb5a7c31863a3663cef8dd7229c6c)#define PM\_DEVICE\_DEFINE(dev\_id, pm\_action\_cb, ...) \

337 Z\_PM\_DEVICE\_DEFINE(DT\_INVALID\_NODE, dev\_id, pm\_action\_cb, \

338 COND\_CODE\_1(IS\_EMPTY(\_\_VA\_ARGS\_\_), (0), (\_\_VA\_ARGS\_\_)))

339

[ 351](group__subsys__pm__device.md#gaa2bd2c490fee99a6fc2b23605e799ef0)#define PM\_DEVICE\_DT\_DEFINE(node\_id, pm\_action\_cb, ...) \

352 Z\_PM\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), pm\_action\_cb, \

353 COND\_CODE\_1(IS\_EMPTY(\_\_VA\_ARGS\_\_), (0), (\_\_VA\_ARGS\_\_)))

354

[ 366](group__subsys__pm__device.md#ga5b201836d9c19a1c87cdde93631a4b0c)#define PM\_DEVICE\_DT\_INST\_DEFINE(idx, pm\_action\_cb, ...) \

367 Z\_PM\_DEVICE\_DEFINE(DT\_DRV\_INST(idx), \

368 Z\_DEVICE\_DT\_DEV\_ID(DT\_DRV\_INST(idx)), \

369 pm\_action\_cb, \

370 COND\_CODE\_1(IS\_EMPTY(\_\_VA\_ARGS\_\_), (0), (\_\_VA\_ARGS\_\_)))

371

[ 380](group__subsys__pm__device.md#gaa94d19d0590659b7aba83566de9bd0c5)#define PM\_DEVICE\_GET(dev\_id) \

381 Z\_PM\_DEVICE\_GET(dev\_id)

382

[ 391](group__subsys__pm__device.md#gad244d742bc6b9874bfb90a2c3c87c4e8)#define PM\_DEVICE\_DT\_GET(node\_id) \

392 PM\_DEVICE\_GET(Z\_DEVICE\_DT\_DEV\_ID(node\_id))

393

[ 402](group__subsys__pm__device.md#ga52892f2c34f6ccc9598002625baf12ce)#define PM\_DEVICE\_DT\_INST\_GET(idx) \

403 PM\_DEVICE\_DT\_GET(DT\_DRV\_INST(idx))

404

[ 410](group__subsys__pm__device.md#gad109511e4314fa6145ee97dd655ec7bb)const char \*[pm\_device\_state\_str](group__subsys__pm__device.md#gad109511e4314fa6145ee97dd655ec7bb)(enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

411

[ 429](group__subsys__pm__device.md#ga3840d6e7832a00b93763247a5951bfde)int [pm\_device\_action\_run](group__subsys__pm__device.md#ga3840d6e7832a00b93763247a5951bfde)(const struct [device](structdevice.md) \*dev,

430 enum [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) action);

431

[ 442](group__subsys__pm__device.md#ga765a5412f66070ccefd8e80ed9f62b1b)void [pm\_device\_children\_action\_run](group__subsys__pm__device.md#ga765a5412f66070ccefd8e80ed9f62b1b)(const struct [device](structdevice.md) \*dev,

443 enum [pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c) action,

444 [pm\_device\_action\_failed\_cb\_t](group__subsys__pm__device.md#ga9cfb6437873089714635d2b26aafefac) failure\_cb);

445

446#if defined(CONFIG\_PM\_DEVICE) || defined(\_\_DOXYGEN\_\_)

[ 456](group__subsys__pm__device.md#gaffcf0aea5df10657235d4ed1f8c74d5a)int [pm\_device\_state\_get](group__subsys__pm__device.md#gaffcf0aea5df10657235d4ed1f8c74d5a)(const struct [device](structdevice.md) \*dev,

457 enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

458

[ 470](group__subsys__pm__device.md#ga4c366f49e326a8b8e01d90cb2ee424ba)static inline void [pm\_device\_init\_suspended](group__subsys__pm__device.md#ga4c366f49e326a8b8e01d90cb2ee424ba)(const struct [device](structdevice.md) \*dev)

471{

472 struct [pm\_device\_base](structpm__device__base.md) \*pm = dev->[pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99);

473

474 pm->[state](structpm__device__base.md#af4c9ef16800538148dcfa1d93b69bccb) = [PM\_DEVICE\_STATE\_SUSPENDED](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5);

475}

476

[ 490](group__subsys__pm__device.md#gafb12ecf4679dd449e2faad0ede2c75fd)static inline void [pm\_device\_init\_off](group__subsys__pm__device.md#gafb12ecf4679dd449e2faad0ede2c75fd)(const struct [device](structdevice.md) \*dev)

491{

492 struct [pm\_device\_base](structpm__device__base.md) \*pm = dev->[pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99);

493

494 pm->[state](structpm__device__base.md#af4c9ef16800538148dcfa1d93b69bccb) = [PM\_DEVICE\_STATE\_OFF](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2);

495}

496

[ 508](group__subsys__pm__device.md#ga7ea002352f3d1c90aecff1d54c255a06)void [pm\_device\_busy\_set](group__subsys__pm__device.md#ga7ea002352f3d1c90aecff1d54c255a06)(const struct [device](structdevice.md) \*dev);

509

[ 517](group__subsys__pm__device.md#ga8b527314f0c61b85602876b4f5a52275)void [pm\_device\_busy\_clear](group__subsys__pm__device.md#ga8b527314f0c61b85602876b4f5a52275)(const struct [device](structdevice.md) \*dev);

518

[ 525](group__subsys__pm__device.md#gae59a1fbcd2399717076fbfcee1e5e411)bool [pm\_device\_is\_any\_busy](group__subsys__pm__device.md#gae59a1fbcd2399717076fbfcee1e5e411)(void);

526

[ 535](group__subsys__pm__device.md#ga8ff7c3197d5ded860878302d00ac709c)bool [pm\_device\_is\_busy](group__subsys__pm__device.md#ga8ff7c3197d5ded860878302d00ac709c)(const struct [device](structdevice.md) \*dev);

536

[ 550](group__subsys__pm__device.md#ga74fde62f71393fb9863916b3a2e5c460)bool [pm\_device\_wakeup\_enable](group__subsys__pm__device.md#ga74fde62f71393fb9863916b3a2e5c460)(const struct [device](structdevice.md) \*dev, bool enable);

551

[ 560](group__subsys__pm__device.md#ga0716c6158804ac48022280d8d237f8c1)bool [pm\_device\_wakeup\_is\_enabled](group__subsys__pm__device.md#ga0716c6158804ac48022280d8d237f8c1)(const struct [device](structdevice.md) \*dev);

561

[ 570](group__subsys__pm__device.md#gac818aafb748b57d70909808b45d89379)bool [pm\_device\_wakeup\_is\_capable](group__subsys__pm__device.md#gac818aafb748b57d70909808b45d89379)(const struct [device](structdevice.md) \*dev);

571

[ 580](group__subsys__pm__device.md#ga32eb5e210d2f0ba533b0185a94c8744e)bool [pm\_device\_on\_power\_domain](group__subsys__pm__device.md#ga32eb5e210d2f0ba533b0185a94c8744e)(const struct [device](structdevice.md) \*dev);

581

[ 595](group__subsys__pm__device.md#gaa10a3f1ce71409cb591db416a1611377)int [pm\_device\_power\_domain\_add](group__subsys__pm__device.md#gaa10a3f1ce71409cb591db416a1611377)(const struct [device](structdevice.md) \*dev,

596 const struct [device](structdevice.md) \*domain);

597

[ 610](group__subsys__pm__device.md#ga1d7ab9b0b497e016b9b22d2506cd23f9)int [pm\_device\_power\_domain\_remove](group__subsys__pm__device.md#ga1d7ab9b0b497e016b9b22d2506cd23f9)(const struct [device](structdevice.md) \*dev,

611 const struct [device](structdevice.md) \*domain);

612

[ 622](group__subsys__pm__device.md#ga9e926dffd7eafc567499ce1ea537486b)bool [pm\_device\_is\_powered](group__subsys__pm__device.md#ga9e926dffd7eafc567499ce1ea537486b)(const struct [device](structdevice.md) \*dev);

623

[ 638](group__subsys__pm__device.md#gad563094c2d4ad066bc4ce30586e13fb3)int [pm\_device\_driver\_init](group__subsys__pm__device.md#gad563094c2d4ad066bc4ce30586e13fb3)(const struct [device](structdevice.md) \*dev, [pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179) [action\_cb](structpm__device__base.md#abd3a07f0e7c54cb0bee7f835be79dac6));

639

640#else

641static inline int [pm\_device\_state\_get](group__subsys__pm__device.md#gaffcf0aea5df10657235d4ed1f8c74d5a)(const struct [device](structdevice.md) \*dev,

642 enum [pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

643{

644 ARG\_UNUSED(dev);

645

646 \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) = [PM\_DEVICE\_STATE\_ACTIVE](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7);

647

648 return 0;

649}

650

651static inline void [pm\_device\_init\_suspended](group__subsys__pm__device.md#ga4c366f49e326a8b8e01d90cb2ee424ba)(const struct [device](structdevice.md) \*dev)

652{

653 ARG\_UNUSED(dev);

654}

655static inline void [pm\_device\_init\_off](group__subsys__pm__device.md#gafb12ecf4679dd449e2faad0ede2c75fd)(const struct [device](structdevice.md) \*dev)

656{

657 ARG\_UNUSED(dev);

658}

659static inline void [pm\_device\_busy\_set](group__subsys__pm__device.md#ga7ea002352f3d1c90aecff1d54c255a06)(const struct [device](structdevice.md) \*dev)

660{

661 ARG\_UNUSED(dev);

662}

663static inline void [pm\_device\_busy\_clear](group__subsys__pm__device.md#ga8b527314f0c61b85602876b4f5a52275)(const struct [device](structdevice.md) \*dev)

664{

665 ARG\_UNUSED(dev);

666}

667static inline bool [pm\_device\_is\_any\_busy](group__subsys__pm__device.md#gae59a1fbcd2399717076fbfcee1e5e411)(void) { return false; }

668static inline bool [pm\_device\_is\_busy](group__subsys__pm__device.md#ga8ff7c3197d5ded860878302d00ac709c)(const struct [device](structdevice.md) \*dev)

669{

670 ARG\_UNUSED(dev);

671 return false;

672}

673static inline bool [pm\_device\_wakeup\_enable](group__subsys__pm__device.md#ga74fde62f71393fb9863916b3a2e5c460)(const struct [device](structdevice.md) \*dev,

674 bool enable)

675{

676 ARG\_UNUSED(dev);

677 ARG\_UNUSED(enable);

678 return false;

679}

680static inline bool [pm\_device\_wakeup\_is\_enabled](group__subsys__pm__device.md#ga0716c6158804ac48022280d8d237f8c1)(const struct [device](structdevice.md) \*dev)

681{

682 ARG\_UNUSED(dev);

683 return false;

684}

685static inline bool [pm\_device\_wakeup\_is\_capable](group__subsys__pm__device.md#gac818aafb748b57d70909808b45d89379)(const struct [device](structdevice.md) \*dev)

686{

687 ARG\_UNUSED(dev);

688 return false;

689}

690static inline bool [pm\_device\_on\_power\_domain](group__subsys__pm__device.md#ga32eb5e210d2f0ba533b0185a94c8744e)(const struct [device](structdevice.md) \*dev)

691{

692 ARG\_UNUSED(dev);

693 return false;

694}

695

696static inline int [pm\_device\_power\_domain\_add](group__subsys__pm__device.md#gaa10a3f1ce71409cb591db416a1611377)(const struct [device](structdevice.md) \*dev,

697 const struct [device](structdevice.md) \*domain)

698{

699 ARG\_UNUSED(dev);

700 ARG\_UNUSED(domain);

701 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

702}

703

704static inline int [pm\_device\_power\_domain\_remove](group__subsys__pm__device.md#ga1d7ab9b0b497e016b9b22d2506cd23f9)(const struct [device](structdevice.md) \*dev,

705 const struct [device](structdevice.md) \*domain)

706{

707 ARG\_UNUSED(dev);

708 ARG\_UNUSED(domain);

709 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

710}

711

712static inline bool [pm\_device\_is\_powered](group__subsys__pm__device.md#ga9e926dffd7eafc567499ce1ea537486b)(const struct [device](structdevice.md) \*dev)

713{

714 ARG\_UNUSED(dev);

715 return true;

716}

717

718static inline int [pm\_device\_driver\_init](group__subsys__pm__device.md#gad563094c2d4ad066bc4ce30586e13fb3)(const struct [device](structdevice.md) \*dev, [pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179) [action\_cb](structpm__device__base.md#abd3a07f0e7c54cb0bee7f835be79dac6))

719{

720 int rc;

721

722 /\* When power management is not enabled, all drivers should initialise to active state \*/

723 rc = [action\_cb](structpm__device__base.md#abd3a07f0e7c54cb0bee7f835be79dac6)(dev, [PM\_DEVICE\_ACTION\_TURN\_ON](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4cac7690e0ffd27742acf58fdbdb7b89544));

724 if ((rc < 0) && (rc != -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33))) {

725 return rc;

726 }

727

728 rc = [action\_cb](structpm__device__base.md#abd3a07f0e7c54cb0bee7f835be79dac6)(dev, [PM\_DEVICE\_ACTION\_RESUME](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca757c6ab81eeac0d6afae479d6a0ac564));

729 if (rc < 0) {

730 return rc;

731 }

732

733 return 0;

734}

735

736#endif /\* CONFIG\_PM\_DEVICE \*/

737

739

740#ifdef \_\_cplusplus

741}

742#endif

743

744#endif

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[pm\_device\_wakeup\_is\_enabled](group__subsys__pm__device.md#ga0716c6158804ac48022280d8d237f8c1)

bool pm\_device\_wakeup\_is\_enabled(const struct device \*dev)

Check if a device is enabled as a wake up source.

[pm\_device\_power\_domain\_remove](group__subsys__pm__device.md#ga1d7ab9b0b497e016b9b22d2506cd23f9)

int pm\_device\_power\_domain\_remove(const struct device \*dev, const struct device \*domain)

Remove a device from a power domain.

[pm\_device\_on\_power\_domain](group__subsys__pm__device.md#ga32eb5e210d2f0ba533b0185a94c8744e)

bool pm\_device\_on\_power\_domain(const struct device \*dev)

Check if the device is on a switchable power domain.

[pm\_device\_action\_run](group__subsys__pm__device.md#ga3840d6e7832a00b93763247a5951bfde)

int pm\_device\_action\_run(const struct device \*dev, enum pm\_device\_action action)

Run a pm action on a device.

[pm\_device\_init\_suspended](group__subsys__pm__device.md#ga4c366f49e326a8b8e01d90cb2ee424ba)

static void pm\_device\_init\_suspended(const struct device \*dev)

Initialize a device state to PM\_DEVICE\_STATE\_SUSPENDED.

**Definition** device.h:470

[pm\_device\_state](group__subsys__pm__device.md#ga561c0789071e3c3963f21f4c4a1bb2c6)

pm\_device\_state

Device power states.

**Definition** device.h:68

[pm\_device\_wakeup\_enable](group__subsys__pm__device.md#ga74fde62f71393fb9863916b3a2e5c460)

bool pm\_device\_wakeup\_enable(const struct device \*dev, bool enable)

Enable or disable a device as a wake up source.

[pm\_device\_children\_action\_run](group__subsys__pm__device.md#ga765a5412f66070ccefd8e80ed9f62b1b)

void pm\_device\_children\_action\_run(const struct device \*dev, enum pm\_device\_action action, pm\_device\_action\_failed\_cb\_t failure\_cb)

Run a pm action on all children of a device.

[pm\_device\_busy\_set](group__subsys__pm__device.md#ga7ea002352f3d1c90aecff1d54c255a06)

void pm\_device\_busy\_set(const struct device \*dev)

Mark a device as busy.

[pm\_device\_action\_cb\_t](group__subsys__pm__device.md#ga81d4ee32f5bbb1b343234b9b3afc0179)

int(\* pm\_device\_action\_cb\_t)(const struct device \*dev, enum pm\_device\_action action)

Device PM action callback.

**Definition** device.h:119

[pm\_device\_busy\_clear](group__subsys__pm__device.md#ga8b527314f0c61b85602876b4f5a52275)

void pm\_device\_busy\_clear(const struct device \*dev)

Clear a device busy status.

[pm\_device\_is\_busy](group__subsys__pm__device.md#ga8ff7c3197d5ded860878302d00ac709c)

bool pm\_device\_is\_busy(const struct device \*dev)

Check if a device is busy.

[pm\_device\_action\_failed\_cb\_t](group__subsys__pm__device.md#ga9cfb6437873089714635d2b26aafefac)

bool(\* pm\_device\_action\_failed\_cb\_t)(const struct device \*dev, int err)

Device PM action failed callback.

**Definition** device.h:130

[pm\_device\_is\_powered](group__subsys__pm__device.md#ga9e926dffd7eafc567499ce1ea537486b)

bool pm\_device\_is\_powered(const struct device \*dev)

Check if the device is currently powered.

[pm\_device\_power\_domain\_add](group__subsys__pm__device.md#gaa10a3f1ce71409cb591db416a1611377)

int pm\_device\_power\_domain\_add(const struct device \*dev, const struct device \*domain)

Add a device to a power domain.

[pm\_device\_wakeup\_is\_capable](group__subsys__pm__device.md#gac818aafb748b57d70909808b45d89379)

bool pm\_device\_wakeup\_is\_capable(const struct device \*dev)

Check if a device is wake up capable.

[pm\_device\_state\_str](group__subsys__pm__device.md#gad109511e4314fa6145ee97dd655ec7bb)

const char \* pm\_device\_state\_str(enum pm\_device\_state state)

Get name of device PM state.

[pm\_device\_driver\_init](group__subsys__pm__device.md#gad563094c2d4ad066bc4ce30586e13fb3)

int pm\_device\_driver\_init(const struct device \*dev, pm\_device\_action\_cb\_t action\_cb)

Setup a device driver into the lowest valid power mode.

[pm\_device\_is\_any\_busy](group__subsys__pm__device.md#gae59a1fbcd2399717076fbfcee1e5e411)

bool pm\_device\_is\_any\_busy(void)

Check if any device is busy.

[pm\_device\_action](group__subsys__pm__device.md#gaee5546eacb9be7caa9d59ab63926cc4c)

pm\_device\_action

Device PM actions.

**Definition** device.h:90

[pm\_device\_init\_off](group__subsys__pm__device.md#gafb12ecf4679dd449e2faad0ede2c75fd)

static void pm\_device\_init\_off(const struct device \*dev)

Initialize a device state to PM\_DEVICE\_STATE\_OFF.

**Definition** device.h:490

[pm\_device\_state\_get](group__subsys__pm__device.md#gaffcf0aea5df10657235d4ed1f8c74d5a)

int pm\_device\_state\_get(const struct device \*dev, enum pm\_device\_state \*state)

Obtain the power state of a device.

[PM\_DEVICE\_STATE\_SUSPENDED](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5)

@ PM\_DEVICE\_STATE\_SUSPENDED

Device is suspended.

**Definition** device.h:77

[PM\_DEVICE\_STATE\_OFF](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2)

@ PM\_DEVICE\_STATE\_OFF

Device is turned off (power removed).

**Definition** device.h:86

[PM\_DEVICE\_STATE\_SUSPENDING](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a51a5904aff980deff73d29568b6f7deb)

@ PM\_DEVICE\_STATE\_SUSPENDING

Device is being suspended.

**Definition** device.h:79

[PM\_DEVICE\_STATE\_ACTIVE](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7)

@ PM\_DEVICE\_STATE\_ACTIVE

Device is in active or regular state.

**Definition** device.h:70

[PM\_DEVICE\_ACTION\_TURN\_OFF](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca2bcd7dee3a85b27157bbc465bacf521e)

@ PM\_DEVICE\_ACTION\_TURN\_OFF

Turn off.

**Definition** device.h:100

[PM\_DEVICE\_ACTION\_SUSPEND](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca5b7ae11deaee85eb0b8452bc89383790)

@ PM\_DEVICE\_ACTION\_SUSPEND

Suspend.

**Definition** device.h:92

[PM\_DEVICE\_ACTION\_RESUME](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4ca757c6ab81eeac0d6afae479d6a0ac564)

@ PM\_DEVICE\_ACTION\_RESUME

Resume.

**Definition** device.h:94

[PM\_DEVICE\_ACTION\_TURN\_ON](group__subsys__pm__device.md#ggaee5546eacb9be7caa9d59ab63926cc4cac7690e0ffd27742acf58fdbdb7b89544)

@ PM\_DEVICE\_ACTION\_TURN\_ON

Turn on.

**Definition** device.h:106

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[kernel.h](kernel_8h.md)

Public kernel APIs.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::pm\_base](structdevice.md#a05ebf64a113d562fb9328ea62cfa8f99)

struct pm\_device\_base \* pm\_base

**Definition** device.h:542

[k\_event](structk__event.md)

Event Structure.

**Definition** kernel.h:2356

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4101

[pm\_device\_base](structpm__device__base.md)

Device PM info.

**Definition** device.h:139

[pm\_device\_base::usage](structpm__device__base.md#a4a9eeb093de1b1e60222b25a06a6361d)

uint32\_t usage

Device usage count.

**Definition** device.h:148

[pm\_device\_base::action\_cb](structpm__device__base.md#abd3a07f0e7c54cb0bee7f835be79dac6)

pm\_device\_action\_cb\_t action\_cb

Device PM action callback.

**Definition** device.h:145

[pm\_device\_base::state](structpm__device__base.md#af4c9ef16800538148dcfa1d93b69bccb)

enum pm\_device\_state state

Device power state.

**Definition** device.h:143

[pm\_device\_base::flags](structpm__device__base.md#af9a24c7aaa0425b335fe147908c1fd4d)

atomic\_t flags

Device PM status flags.

**Definition** device.h:141

[pm\_device\_isr](structpm__device__isr.md)

Runtime PM info for device with synchronous PM.

**Definition** device.h:187

[pm\_device\_isr::lock](structpm__device__isr.md#a24d7dd68bb57794be25450389fc95b33)

struct k\_spinlock lock

Lock to synchronize the synchronous get/put operations.

**Definition** device.h:192

[pm\_device\_isr::base](structpm__device__isr.md#ad501eabcd3370e9edb6b0851928fd7ac)

struct pm\_device\_base base

Base info.

**Definition** device.h:189

[pm\_device](structpm__device.md)

Runtime PM info for device with generic PM.

**Definition** device.h:163

[pm\_device::work](structpm__device.md#a5dc3b48b3139d546206c8b9cacaf09fd)

struct k\_work\_delayable work

Work object for asynchronous calls.

**Definition** device.h:175

[pm\_device::event](structpm__device.md#aa8ed27c6c0cff89062922bedae4dca35)

struct k\_event event

Event var to listen to the sync request events.

**Definition** device.h:172

[pm\_device::lock](structpm__device.md#ab7e54f9195359f60cc0a4b06677df0c7)

struct k\_sem lock

Lock to synchronize the get/put operations.

**Definition** device.h:170

[pm\_device::dev](structpm__device.md#aec09c5708cda21c6e3af2a4e7082b432)

const struct device \* dev

Pointer to the device.

**Definition** device.h:168

[pm\_device::base](structpm__device.md#afb5db0142ebab7891a42f71b59fd55cb)

struct pm\_device\_base base

Base info.

**Definition** device.h:165

[atomic.h](sys_2atomic_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [device.h](pm_2device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
