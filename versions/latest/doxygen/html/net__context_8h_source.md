---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__context_8h_source.html
original_path: doxygen/html/net__context_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_context.h

[Go to the documentation of this file.](net__context_8h.md)

1

6

7/\*

8 \* Copyright (c) 2016 Intel Corporation

9 \* Copyright (c) 2021 Nordic Semiconductor

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_CONTEXT\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_NET\_CONTEXT\_H\_

16

23

24#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

25#include <[zephyr/sys/atomic.h](atomic_8h.md)>

26

27#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

28#include <[zephyr/net/net\_if.h](net__if_8h.md)>

29#include <[zephyr/net/net\_stats.h](net__stats_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 36](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29)#define NET\_CONTEXT\_IN\_USE BIT(0)

37

[ 39](group__net__context.md#ga62753cf9e6218d37e65f8b461bf8c8dd)enum [net\_context\_state](group__net__context.md#ga62753cf9e6218d37e65f8b461bf8c8dd) {

[ 40](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda1997d732e8a49fd42895917afe160de2) [NET\_CONTEXT\_IDLE](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda1997d732e8a49fd42895917afe160de2) = 0,

[ 41](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda8d946fd7f7895cce804bf617313a2c40) [NET\_CONTEXT\_UNCONNECTED](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda8d946fd7f7895cce804bf617313a2c40) = 0,

[ 42](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8ddaaa50d60ab4b2aa7db248402c522fd3f6) [NET\_CONTEXT\_CONFIGURING](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8ddaaa50d60ab4b2aa7db248402c522fd3f6) = 1,

[ 43](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda26bdeef9794c4051446339bb38a6999e) [NET\_CONTEXT\_CONNECTING](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda26bdeef9794c4051446339bb38a6999e) = 1,

[ 44](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda69163a1ec7757a0307b326bdc3e2697b) [NET\_CONTEXT\_READY](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda69163a1ec7757a0307b326bdc3e2697b) = 2,

[ 45](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda18b286eb1d9a61595b70f76eead211e7) [NET\_CONTEXT\_CONNECTED](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda18b286eb1d9a61595b70f76eead211e7) = 2,

[ 46](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8ddab77dbc57d8c05b742bc28f01793179a9) [NET\_CONTEXT\_LISTENING](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8ddab77dbc57d8c05b742bc28f01793179a9) = 3,

47};

48

[ 54](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)#define NET\_CONTEXT\_FAMILY (BIT(3) | BIT(4) | BIT(5))

55

[ 57](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)#define NET\_CONTEXT\_TYPE (BIT(6) | BIT(7))

58

[ 60](group__net__context.md#ga84206421e8f2e1eb114d393f0c81428b)#define NET\_CONTEXT\_REMOTE\_ADDR\_SET BIT(8)

61

[ 63](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e)#define NET\_CONTEXT\_ACCEPTING\_SOCK BIT(9)

64

[ 66](group__net__context.md#ga90385e51999494c0d530c97b57a01865)#define NET\_CONTEXT\_CLOSING\_SOCK BIT(10)

67

68/\* Context is bound to a specific interface \*/

[ 69](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1)#define NET\_CONTEXT\_BOUND\_TO\_IFACE BIT(11)

70

71struct [net\_context](structnet__context.md);

72

[ 93](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)typedef void (\*[net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317))(struct [net\_context](structnet__context.md) \*context,

94 struct [net\_pkt](structnet__pkt.md) \*pkt,

95 union net\_ip\_header \*ip\_hdr,

96 union net\_proto\_header \*proto\_hdr,

97 int status,

98 void \*user\_data);

99

[ 114](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)typedef void (\*[net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93))(struct [net\_context](structnet__context.md) \*context,

115 int status,

116 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

117

[ 134](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8)typedef void (\*[net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8))(struct [net\_context](structnet__context.md) \*new\_context,

135 struct [sockaddr](structsockaddr.md) \*addr,

136 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

137 int status,

138 void \*user\_data);

139

[ 161](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)typedef void (\*[net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71))(struct [net\_context](structnet__context.md) \*context,

162 int status,

163 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

164

165/\* The net\_pkt\_get\_slab\_func\_t is here in order to avoid circular

166 \* dependency between net\_pkt.h and net\_context.h

167 \*/

176typedef struct k\_mem\_slab \*(\*net\_pkt\_get\_slab\_func\_t)(void);

177

178/\* The net\_pkt\_get\_pool\_func\_t is here in order to avoid circular

179 \* dependency between net\_pkt.h and net\_context.h

180 \*/

189typedef struct [net\_buf\_pool](structnet__buf__pool.md) \*(\*net\_pkt\_get\_pool\_func\_t)(void);

190

191struct net\_tcp;

192

193struct net\_conn\_handle;

194

[ 201](structnet__context.md)\_\_net\_socket struct [net\_context](structnet__context.md) {

[ 204](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7) void \*[fifo\_reserved](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7);

205

[ 208](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb) void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb);

209

[ 212](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [refcount](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a);

213

[ 216](structnet__context.md#a730e72866e94ed1695010b50c618a281) struct [k\_mutex](structk__mutex.md) [lock](structnet__context.md#a730e72866e94ed1695010b50c618a281);

217

[ 221](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955) struct sockaddr\_ptr [local](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955);

222

[ 226](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c) struct [sockaddr](structsockaddr.md) [remote](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c);

227

[ 229](structnet__context.md#abd8ff1b4826535df911d2af14b46e312) struct net\_conn\_handle \*[conn\_handler](structnet__context.md#abd8ff1b4826535df911d2af14b46e312);

230

[ 234](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4) [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) [recv\_cb](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4);

235

[ 239](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c) [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) [send\_cb](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c);

240

[ 244](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d) [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) [connect\_cb](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d);

245

246#if defined(CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL)

249 [net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770) tx\_slab;

250

253 [net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91) data\_pool;

254#endif /\* CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL \*/

255

256#if defined(CONFIG\_NET\_TCP)

[ 258](structnet__context.md#adee6e668bfae2749df9b986d0049f10b) void \*[tcp](structnet__context.md#adee6e668bfae2749df9b986d0049f10b);

259#endif /\* CONFIG\_NET\_TCP \*/

260

261#if defined(CONFIG\_NET\_CONTEXT\_SYNC\_RECV)

265 struct k\_sem recv\_data\_wait;

266#endif /\* CONFIG\_NET\_CONTEXT\_SYNC\_RECV \*/

267

268#if defined(CONFIG\_NET\_SOCKETS)

270 void \*socket\_data;

271

273 union {

274 struct [k\_fifo](structk__fifo.md) recv\_q;

275 struct [k\_fifo](structk__fifo.md) accept\_q;

276 };

277

278 struct {

280 struct [k\_condvar](structk__condvar.md) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40);

281

283 struct [k\_mutex](structk__mutex.md) \*lock;

284 } cond;

285#endif /\* CONFIG\_NET\_SOCKETS \*/

286

287#if defined(CONFIG\_NET\_OFFLOAD)

289 void \*offload\_context;

290#endif /\* CONFIG\_NET\_OFFLOAD \*/

291

292#if defined(CONFIG\_NET\_SOCKETS\_CAN)

293 int can\_filter\_id;

294#endif /\* CONFIG\_NET\_SOCKETS\_CAN \*/

295

297 struct {

298#if defined(CONFIG\_NET\_CONTEXT\_PRIORITY)

300 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority;

301#endif

302#if defined(CONFIG\_NET\_CONTEXT\_TXTIME)

304 bool txtime;

305#endif

306#if defined(CONFIG\_SOCKS)

308 struct {

309 struct sockaddr addr;

310 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen;

311 } proxy;

312#endif

313#if defined(CONFIG\_NET\_CONTEXT\_RCVTIMEO)

315 k\_timeout\_t rcvtimeo;

316#endif

317#if defined(CONFIG\_NET\_CONTEXT\_SNDTIMEO)

319 k\_timeout\_t sndtimeo;

320#endif

321#if defined(CONFIG\_NET\_CONTEXT\_RCVBUF)

323 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rcvbuf;

324#endif

325#if defined(CONFIG\_NET\_CONTEXT\_SNDBUF)

327 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sndbuf;

328#endif

329#if defined(CONFIG\_NET\_CONTEXT\_DSCP\_ECN)

334 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dscp\_ecn;

335#endif

336#if defined(CONFIG\_NET\_CONTEXT\_REUSEADDR)

338 bool reuseaddr;

339#endif

340#if defined(CONFIG\_NET\_CONTEXT\_REUSEPORT)

342 bool reuseport;

343#endif

344#if defined(CONFIG\_NET\_IPV4\_MAPPING\_TO\_IPV6)

346 bool ipv6\_v6only;

347#endif

348#if defined(CONFIG\_NET\_CONTEXT\_RECV\_PKTINFO)

350 bool recv\_pktinfo;

351#endif

[ 352](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07) } [options](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07);

353

[ 355](structnet__context.md#abfb04fc163636498f72b29aa12087e19) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19);

356

[ 358](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c);

359

[ 361](structnet__context.md#ad71d151e1e9e35b934949482066f1947) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947);

362

364 union {

365 struct {

[ 366](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4);

[ 367](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7);

368 };

369 struct {

[ 370](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb);

[ 371](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd);

372 };

373 };

374

375#if defined(CONFIG\_SOCKS)

377 bool proxy\_enabled;

378#endif

379

380};

381

[ 389](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)static inline bool [net\_context\_is\_used](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)(struct [net\_context](structnet__context.md) \*context)

390{

391 NET\_ASSERT(context);

392

393 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_IN\_USE](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29);

394}

395

[ 403](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)static inline bool [net\_context\_is\_bound\_to\_iface](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)(struct [net\_context](structnet__context.md) \*context)

404{

405 NET\_ASSERT(context);

406

407 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1);

408}

409

[ 417](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)static inline bool [net\_context\_is\_accepting](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)(struct [net\_context](structnet__context.md) \*context)

418{

419 NET\_ASSERT(context);

420

421 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

422}

423

[ 430](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)static inline void [net\_context\_set\_accepting](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)(struct [net\_context](structnet__context.md) \*context,

431 bool accepting)

432{

433 NET\_ASSERT(context);

434

435 if (accepting) {

436 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

437 } else {

438 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= [~NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

439 }

440}

441

[ 449](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)static inline bool [net\_context\_is\_closing](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)(struct [net\_context](structnet__context.md) \*context)

450{

451 NET\_ASSERT(context);

452

453 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

454}

455

[ 462](group__net__context.md#ga9941aa201206448b6b34789d252f6385)static inline void [net\_context\_set\_closing](group__net__context.md#ga9941aa201206448b6b34789d252f6385)(struct [net\_context](structnet__context.md) \*context,

463 bool closing)

464{

465 NET\_ASSERT(context);

466

467 if (closing) {

468 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

469 } else {

470 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= [~NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

471 }

472}

473

[ 474](group__net__context.md#gacd1592ed32c7de5ecdeb69f569cb701f)#define NET\_CONTEXT\_STATE\_SHIFT 1

[ 475](group__net__context.md#gac63c02e444e17b268c230ba15c7c4339)#define NET\_CONTEXT\_STATE\_MASK 0x03

476

486static inline

[ 487](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)enum [net\_context\_state](group__net__context.md#ga62753cf9e6218d37e65f8b461bf8c8dd) [net\_context\_get\_state](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)(struct [net\_context](structnet__context.md) \*context)

488{

489 NET\_ASSERT(context);

490

491 return (enum [net\_context\_state](group__net__context.md#ga62753cf9e6218d37e65f8b461bf8c8dd))

492 ((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) >> [NET\_CONTEXT\_STATE\_SHIFT](group__net__context.md#gacd1592ed32c7de5ecdeb69f569cb701f)) &

493 [NET\_CONTEXT\_STATE\_MASK](group__net__context.md#gac63c02e444e17b268c230ba15c7c4339));

494}

495

[ 504](group__net__context.md#gaac934209341db606a4d563b3c48cce45)static inline void [net\_context\_set\_state](group__net__context.md#gaac934209341db606a4d563b3c48cce45)(struct [net\_context](structnet__context.md) \*context,

505 enum [net\_context\_state](group__net__context.md#ga62753cf9e6218d37e65f8b461bf8c8dd) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

506{

507 NET\_ASSERT(context);

508

509 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= ~([NET\_CONTEXT\_STATE\_MASK](group__net__context.md#gac63c02e444e17b268c230ba15c7c4339) << [NET\_CONTEXT\_STATE\_SHIFT](group__net__context.md#gacd1592ed32c7de5ecdeb69f569cb701f));

510 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= (([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) & [NET\_CONTEXT\_STATE\_MASK](group__net__context.md#gac63c02e444e17b268c230ba15c7c4339)) <<

511 [NET\_CONTEXT\_STATE\_SHIFT](group__net__context.md#gacd1592ed32c7de5ecdeb69f569cb701f));

512}

513

[ 524](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)static inline [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [net\_context\_get\_family](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)(struct [net\_context](structnet__context.md) \*context)

525{

526 NET\_ASSERT(context);

527

528 return ((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_FAMILY](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)) >> 3);

529}

530

[ 540](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)static inline void [net\_context\_set\_family](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)(struct [net\_context](structnet__context.md) \*context,

541 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family)

542{

543 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flag = 0U;

544

545 NET\_ASSERT(context);

546

547 if (family == [AF\_UNSPEC](group__ip__4__6.md#gae77ae24b14b7b7f294f3e04121173f12) || family == [AF\_INET](group__ip__4__6.md#ga9930604d0e32588eae76f43ca38e7826) || family == [AF\_INET6](group__ip__4__6.md#gaa03706b2738b9a58d4985dfbe99e1bac) ||

548 family == [AF\_PACKET](group__ip__4__6.md#gaa89aa4cd481fe17260c3f5d493cc23f5) || family == [AF\_CAN](group__ip__4__6.md#ga546620c7e758f003b24b7fdae4f97bd4)) {

549 /\* Family is in BIT(4), BIT(5) and BIT(6) \*/

550 flag = family << 3;

551 }

552

553 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= flag;

554}

555

566static inline

[ 567](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) [net\_context\_get\_type](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)(struct [net\_context](structnet__context.md) \*context)

568{

569 NET\_ASSERT(context);

570

571 return (enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c))((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_TYPE](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)) >> 6);

572}

573

[ 583](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277)static inline void [net\_context\_set\_type](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277)(struct [net\_context](structnet__context.md) \*context,

584 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type)

585{

586 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) flag = 0U;

587

588 NET\_ASSERT(context);

589

590 if (type == [SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc) || type == [SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) || type == [SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)) {

591 /\* Type is in BIT(6) and BIT(7)\*/

592 flag = type << 6;

593 }

594

595 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= flag;

596}

597

606#if defined(CONFIG\_NET\_SOCKETS\_CAN)

607static inline void [net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)(struct [net\_context](structnet__context.md) \*context,

608 int filter\_id)

609{

610 NET\_ASSERT(context);

611

612 context->can\_filter\_id = filter\_id;

613}

614#else

[ 615](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)static inline void [net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)(struct [net\_context](structnet__context.md) \*context,

616 int filter\_id)

617{

618 ARG\_UNUSED(context);

619 ARG\_UNUSED(filter\_id);

620}

621#endif

622

632#if defined(CONFIG\_NET\_SOCKETS\_CAN)

633static inline int [net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)(struct [net\_context](structnet__context.md) \*context)

634{

635 NET\_ASSERT(context);

636

637 return context->can\_filter\_id;

638}

639#else

[ 640](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)static inline int [net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)(struct [net\_context](structnet__context.md) \*context)

641{

642 ARG\_UNUSED(context);

643

644 return -1;

645}

646#endif

647

[ 658](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_context\_get\_proto](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)(struct [net\_context](structnet__context.md) \*context)

659{

660 return context->[proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19);

661}

662

[ 673](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)static inline void [net\_context\_set\_proto](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)(struct [net\_context](structnet__context.md) \*context,

674 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) proto)

675{

676 context->[proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19) = proto;

677}

678

689static inline

[ 690](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)struct [net\_if](structnet__if.md) \*[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)(struct [net\_context](structnet__context.md) \*context)

691{

692 NET\_ASSERT(context);

693

694 return [net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)(context->[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

695}

696

[ 705](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)static inline void [net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)(struct [net\_context](structnet__context.md) \*context,

706 struct [net\_if](structnet__if.md) \*iface)

707{

708 NET\_ASSERT(iface);

709

710 context->[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947) = [net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)(iface);

711}

712

[ 721](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)static inline void [net\_context\_bind\_iface](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)(struct [net\_context](structnet__context.md) \*context,

722 struct [net\_if](structnet__if.md) \*iface)

723{

724 NET\_ASSERT(iface);

725

726 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1);

727 [net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)(context, iface);

728}

729

[ 740](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv4\_ttl](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)(struct [net\_context](structnet__context.md) \*context)

741{

742 return context->[ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb);

743}

744

[ 754](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)static inline void [net\_context\_set\_ipv4\_ttl](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)(struct [net\_context](structnet__context.md) \*context,

755 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

756{

757 context->[ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb) = ttl;

758}

759

[ 770](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv4\_mcast\_ttl](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)(struct [net\_context](structnet__context.md) \*context)

771{

772 return context->[ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd);

773}

774

[ 784](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)static inline void [net\_context\_set\_ipv4\_mcast\_ttl](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)(struct [net\_context](structnet__context.md) \*context,

785 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

786{

787 context->[ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd) = ttl;

788}

789

[ 800](group__net__context.md#ga977b08a77586e0e4752bff725139427c)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv6\_hop\_limit](group__net__context.md#ga977b08a77586e0e4752bff725139427c)(struct [net\_context](structnet__context.md) \*context)

801{

802 return context->[ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4);

803}

804

[ 813](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)static inline void [net\_context\_set\_ipv6\_hop\_limit](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)(struct [net\_context](structnet__context.md) \*context,

814 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

815{

816 context->[ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4) = hop\_limit;

817}

818

[ 829](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv6\_mcast\_hop\_limit](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)(struct [net\_context](structnet__context.md) \*context)

830{

831 return context->[ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7);

832}

833

[ 843](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)static inline void [net\_context\_set\_ipv6\_mcast\_hop\_limit](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)(struct [net\_context](structnet__context.md) \*context,

844 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

845{

846 context->[ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7) = hop\_limit;

847}

848

858#if defined(CONFIG\_SOCKS)

859static inline void [net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)(struct [net\_context](structnet__context.md) \*context,

860 bool enable)

861{

862 context->proxy\_enabled = enable;

863}

864#else

[ 865](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)static inline void [net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)(struct [net\_context](structnet__context.md) \*context,

866 bool enable)

867{

868 ARG\_UNUSED(context);

869 ARG\_UNUSED(enable);

870}

871#endif

872

883#if defined(CONFIG\_SOCKS)

884static inline bool [net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)(struct [net\_context](structnet__context.md) \*context)

885{

886 return context->proxy\_enabled;

887}

888#else

[ 889](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)static inline bool [net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)(struct [net\_context](structnet__context.md) \*context)

890{

891 return false;

892}

893#endif

894

[ 912](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)int [net\_context\_get](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

913 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

914 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ip\_proto,

915 struct [net\_context](structnet__context.md) \*\*context);

916

[ 930](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)int [net\_context\_put](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)(struct [net\_context](structnet__context.md) \*context);

931

[ 944](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)int [net\_context\_ref](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)(struct [net\_context](structnet__context.md) \*context);

945

[ 959](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)int [net\_context\_unref](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)(struct [net\_context](structnet__context.md) \*context);

960

971#if defined(CONFIG\_NET\_IPV4)

972int [net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)(struct [net\_context](structnet__context.md) \*context,

973 struct [net\_pkt](structnet__pkt.md) \*pkt,

974 const struct [in\_addr](structin__addr.md) \*src,

975 const struct [in\_addr](structin__addr.md) \*dst);

976#else

[ 977](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)static inline int [net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)(struct [net\_context](structnet__context.md) \*context,

978 struct [net\_pkt](structnet__pkt.md) \*pkt,

979 const struct [in\_addr](structin__addr.md) \*src,

980 const struct [in\_addr](structin__addr.md) \*dst)

981{

982 return -1;

983}

984#endif /\* CONFIG\_NET\_IPV4 \*/

985

996#if defined(CONFIG\_NET\_IPV6)

997int [net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)(struct [net\_context](structnet__context.md) \*context,

998 struct [net\_pkt](structnet__pkt.md) \*pkt,

999 const struct [in6\_addr](structin6__addr.md) \*src,

1000 const struct [in6\_addr](structin6__addr.md) \*dst);

1001#else

[ 1002](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)static inline int [net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)(struct [net\_context](structnet__context.md) \*context,

1003 struct [net\_pkt](structnet__pkt.md) \*pkt,

1004 const struct [in6\_addr](structin6__addr.md) \*src,

1005 const struct [in6\_addr](structin6__addr.md) \*dst)

1006{

1007 return -1;

1008}

1009#endif /\* CONFIG\_NET\_IPV6 \*/

1010

[ 1022](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)int [net\_context\_bind](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)(struct [net\_context](structnet__context.md) \*context,

1023 const struct [sockaddr](structsockaddr.md) \*addr,

1024 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

1025

[ 1036](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)int [net\_context\_listen](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)(struct [net\_context](structnet__context.md) \*context,

1037 int backlog);

1038

[ 1067](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)int [net\_context\_connect](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)(struct [net\_context](structnet__context.md) \*context,

1068 const struct [sockaddr](structsockaddr.md) \*addr,

1069 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

1070 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

1071 [k\_timeout\_t](structk__timeout__t.md) timeout,

1072 void \*user\_data);

1073

[ 1099](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)int [net\_context\_accept](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)(struct [net\_context](structnet__context.md) \*context,

1100 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

1101 [k\_timeout\_t](structk__timeout__t.md) timeout,

1102 void \*user\_data);

1103

[ 1123](group__net__context.md#gac793e1def18200416e3f679067c56ab3)int [net\_context\_send](group__net__context.md#gac793e1def18200416e3f679067c56ab3)(struct [net\_context](structnet__context.md) \*context,

1124 const void \*buf,

1125 size\_t len,

1126 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1127 [k\_timeout\_t](structk__timeout__t.md) timeout,

1128 void \*user\_data);

1129

[ 1151](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)int [net\_context\_sendto](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)(struct [net\_context](structnet__context.md) \*context,

1152 const void \*buf,

1153 size\_t len,

1154 const struct [sockaddr](structsockaddr.md) \*dst\_addr,

1155 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

1156 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1157 [k\_timeout\_t](structk__timeout__t.md) timeout,

1158 void \*user\_data);

1159

[ 1178](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)int [net\_context\_sendmsg](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)(struct [net\_context](structnet__context.md) \*context,

1179 const struct [msghdr](structmsghdr.md) \*[msghdr](structmsghdr.md),

1180 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

1181 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1182 [k\_timeout\_t](structk__timeout__t.md) timeout,

1183 void \*user\_data);

1184

[ 1221](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)int [net\_context\_recv](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)(struct [net\_context](structnet__context.md) \*context,

1222 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

1223 [k\_timeout\_t](structk__timeout__t.md) timeout,

1224 void \*user\_data);

1225

[ 1246](group__net__context.md#gab3cc2a13e24f9c263bc40cc87d752a9f)int [net\_context\_update\_recv\_wnd](group__net__context.md#gab3cc2a13e24f9c263bc40cc87d752a9f)(struct [net\_context](structnet__context.md) \*context,

1247 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) delta);

1248

[ 1249](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d)enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) {

[ 1250](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c) [NET\_OPT\_PRIORITY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c) = 1,

[ 1251](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184) [NET\_OPT\_TXTIME](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184) = 2,

[ 1252](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c) [NET\_OPT\_SOCKS5](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c) = 3,

[ 1253](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076) [NET\_OPT\_RCVTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076) = 4,

[ 1254](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668) [NET\_OPT\_SNDTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668) = 5,

[ 1255](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1) [NET\_OPT\_RCVBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1) = 6,

[ 1256](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08) [NET\_OPT\_SNDBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08) = 7,

[ 1257](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c) [NET\_OPT\_DSCP\_ECN](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c) = 8,

[ 1258](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561) [NET\_OPT\_REUSEADDR](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561) = 9,

[ 1259](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4) [NET\_OPT\_REUSEPORT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4) = 10,

[ 1260](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c) [NET\_OPT\_IPV6\_V6ONLY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c) = 11,

[ 1261](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a) [NET\_OPT\_RECV\_PKTINFO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a) = 12,

[ 1262](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e) [NET\_OPT\_MCAST\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e) = 13,

[ 1263](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d) [NET\_OPT\_MCAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d) = 14,

[ 1264](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3) [NET\_OPT\_UNICAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3) = 15,

[ 1265](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184) [NET\_OPT\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184) = 16,

1266};

1267

[ 1278](group__net__context.md#gabd932d5ded649f9a8c8bab40810e9eae)int [net\_context\_set\_option](group__net__context.md#gabd932d5ded649f9a8c8bab40810e9eae)(struct [net\_context](structnet__context.md) \*context,

1279 enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) option,

1280 const void \*value, size\_t len);

1281

[ 1292](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)int [net\_context\_get\_option](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)(struct [net\_context](structnet__context.md) \*context,

1293 enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) option,

1294 void \*value, size\_t \*len);

1295

[ 1303](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba)typedef void (\*[net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba))(struct [net\_context](structnet__context.md) \*context, void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

1304

[ 1312](group__net__context.md#gabb751f7d213d00f8eec72a67f4ce3491)void [net\_context\_foreach](group__net__context.md#gabb751f7d213d00f8eec72a67f4ce3491)([net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba) cb, void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

1313

1334#if defined(CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL)

1335static inline void [net\_context\_setup\_pools](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)(struct [net\_context](structnet__context.md) \*context,

1336 [net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770) tx\_slab,

1337 [net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91) data\_pool)

1338{

1339 NET\_ASSERT(context);

1340

1341 context->tx\_slab = tx\_slab;

1342 context->data\_pool = data\_pool;

1343}

1344#else

[ 1345](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)#define net\_context\_setup\_pools(context, tx\_pool, data\_pool)

1346#endif

1347

[ 1361](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)bool [net\_context\_port\_in\_use](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)(enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

1362 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) local\_port, const struct [sockaddr](structsockaddr.md) \*local\_addr);

1363

1364#ifdef \_\_cplusplus

1365}

1366#endif

1367

1371

1372#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_CONTEXT\_H\_ \*/

[atomic.h](atomic_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:888

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[AF\_CAN](group__ip__4__6.md#ga546620c7e758f003b24b7fdae4f97bd4)

#define AF\_CAN

Controller Area Network.

**Definition** net\_ip.h:56

[AF\_INET](group__ip__4__6.md#ga9930604d0e32588eae76f43ca38e7826)

#define AF\_INET

IP protocol family version 4.

**Definition** net\_ip.h:53

[AF\_INET6](group__ip__4__6.md#gaa03706b2738b9a58d4985dfbe99e1bac)

#define AF\_INET6

IP protocol family version 6.

**Definition** net\_ip.h:54

[AF\_PACKET](group__ip__4__6.md#gaa89aa4cd481fe17260c3f5d493cc23f5)

#define AF\_PACKET

Packet family.

**Definition** net\_ip.h:55

[net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)

net\_sock\_type

Socket type.

**Definition** net\_ip.h:84

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[AF\_UNSPEC](group__ip__4__6.md#gae77ae24b14b7b7f294f3e04121173f12)

#define AF\_UNSPEC

Unspecified address family.

**Definition** net\_ip.h:52

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:62

[SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc)

@ SOCK\_DGRAM

Datagram socket type.

**Definition** net\_ip.h:86

[SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)

@ SOCK\_RAW

RAW socket type.

**Definition** net\_ip.h:87

[SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424)

@ SOCK\_STREAM

Stream socket type.

**Definition** net\_ip.h:85

[net\_context\_set\_type](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277)

static void net\_context\_set\_type(struct net\_context \*context, enum net\_sock\_type type)

Set context type for this network context.

**Definition** net\_context.h:583

[net\_context\_set\_ipv6\_hop\_limit](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)

static void net\_context\_set\_ipv6\_hop\_limit(struct net\_context \*context, uint8\_t hop\_limit)

Set IPv6 hop limit value for this context.

**Definition** net\_context.h:813

[net\_context\_unref](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)

int net\_context\_unref(struct net\_context \*context)

Decrement the reference count to a network context.

[net\_context\_bind](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)

int net\_context\_bind(struct net\_context \*context, const struct sockaddr \*addr, socklen\_t addrlen)

Assign a socket a local address.

[net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)

static void net\_context\_set\_iface(struct net\_context \*context, struct net\_if \*iface)

Set network interface for this context.

**Definition** net\_context.h:705

[net\_context\_set\_ipv4\_ttl](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)

static void net\_context\_set\_ipv4\_ttl(struct net\_context \*context, uint8\_t ttl)

Set IPv4 TTL (time-to-live) value for this context.

**Definition** net\_context.h:754

[net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)

void(\* net\_context\_connect\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Connection callback.

**Definition** net\_context.h:161

[net\_context\_accept](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)

int net\_context\_accept(struct net\_context \*context, net\_tcp\_accept\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Accept a network connection attempt.

[net\_context\_put](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)

int net\_context\_put(struct net\_context \*context)

Close and unref a network context.

[net\_context\_get\_type](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)

static enum net\_sock\_type net\_context\_get\_type(struct net\_context \*context)

Get context type for this network context.

**Definition** net\_context.h:567

[net\_context\_is\_accepting](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)

static bool net\_context\_is\_accepting(struct net\_context \*context)

Is this context is accepting data now.

**Definition** net\_context.h:417

[net\_context\_get\_family](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)

static sa\_family\_t net\_context\_get\_family(struct net\_context \*context)

Get address family for this network context.

**Definition** net\_context.h:524

[net\_context\_is\_bound\_to\_iface](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)

static bool net\_context\_is\_bound\_to\_iface(struct net\_context \*context)

Is this context bound to a network interface.

**Definition** net\_context.h:403

[net\_context\_bind\_iface](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)

static void net\_context\_bind\_iface(struct net\_context \*context, struct net\_if \*iface)

Bind network interface to this context.

**Definition** net\_context.h:721

[net\_context\_listen](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)

int net\_context\_listen(struct net\_context \*context, int backlog)

Mark the context as a listening one.

[net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770)

struct k\_mem\_slab \*(\* net\_pkt\_get\_slab\_func\_t)(void)

Function that is called to get the slab that is used for net\_pkt allocations.

**Definition** net\_context.h:176

[net\_context\_get\_ipv4\_mcast\_ttl](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)

static uint8\_t net\_context\_get\_ipv4\_mcast\_ttl(struct net\_context \*context)

Get IPv4 multicast TTL (time-to-live) value for this context.

**Definition** net\_context.h:770

[net\_context\_is\_used](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)

static bool net\_context\_is\_used(struct net\_context \*context)

Is this context used or not.

**Definition** net\_context.h:389

[net\_context\_sendmsg](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)

int net\_context\_sendmsg(struct net\_context \*context, const struct msghdr \*msghdr, int flags, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data in iovec to a peer specified in msghdr struct.

[net\_context\_ref](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)

int net\_context\_ref(struct net\_context \*context)

Take a reference count to a net\_context, preventing destruction.

[net\_context\_get\_state](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)

static enum net\_context\_state net\_context\_get\_state(struct net\_context \*context)

Get state for this network context.

**Definition** net\_context.h:487

[net\_context\_connect](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)

int net\_context\_connect(struct net\_context \*context, const struct sockaddr \*addr, socklen\_t addrlen, net\_context\_connect\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Create a network connection.

[net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)

static void net\_context\_set\_can\_filter\_id(struct net\_context \*context, int filter\_id)

Set CAN filter id for this network context.

**Definition** net\_context.h:615

[net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)

static bool net\_context\_is\_proxy\_enabled(struct net\_context \*context)

Is socks proxy support enabled or disabled for this context.

**Definition** net\_context.h:889

[NET\_CONTEXT\_IN\_USE](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29)

#define NET\_CONTEXT\_IN\_USE

Is this context used or not.

**Definition** net\_context.h:36

[net\_context\_set\_accepting](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)

static void net\_context\_set\_accepting(struct net\_context \*context, bool accepting)

Set this context to accept data now.

**Definition** net\_context.h:430

[net\_context\_state](group__net__context.md#ga62753cf9e6218d37e65f8b461bf8c8dd)

net\_context\_state

State of the context (bits 1 & 2 in the flags).

**Definition** net\_context.h:39

[net\_context\_port\_in\_use](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)

bool net\_context\_port\_in\_use(enum net\_ip\_protocol ip\_proto, uint16\_t local\_port, const struct sockaddr \*local\_addr)

Check if a port is in use (bound).

[net\_context\_set\_family](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)

static void net\_context\_set\_family(struct net\_context \*context, sa\_family\_t family)

Set address family for this network context.

**Definition** net\_context.h:540

[net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)

static int net\_context\_create\_ipv6\_new(struct net\_context \*context, struct net\_pkt \*pkt, const struct in6\_addr \*src, const struct in6\_addr \*dst)

Create IPv6 packet in provided net\_pkt from context.

**Definition** net\_context.h:1002

[net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)

static int net\_context\_create\_ipv4\_new(struct net\_context \*context, struct net\_pkt \*pkt, const struct in\_addr \*src, const struct in\_addr \*dst)

Create IPv4 packet in provided net\_pkt from context.

**Definition** net\_context.h:977

[net\_context\_recv](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)

int net\_context\_recv(struct net\_context \*context, net\_context\_recv\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Receive network data from a peer specified by context.

[net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)

static int net\_context\_get\_can\_filter\_id(struct net\_context \*context)

Get CAN filter id for this network context.

**Definition** net\_context.h:640

[NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865)

#define NET\_CONTEXT\_CLOSING\_SOCK

Is the socket closing / closed.

**Definition** net\_context.h:66

[net\_context\_get\_ipv6\_hop\_limit](group__net__context.md#ga977b08a77586e0e4752bff725139427c)

static uint8\_t net\_context\_get\_ipv6\_hop\_limit(struct net\_context \*context)

Get IPv6 hop limit value for this context.

**Definition** net\_context.h:800

[net\_context\_set\_closing](group__net__context.md#ga9941aa201206448b6b34789d252f6385)

static void net\_context\_set\_closing(struct net\_context \*context, bool closing)

Set this context to closing.

**Definition** net\_context.h:462

[net\_context\_get\_ipv6\_mcast\_hop\_limit](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)

static uint8\_t net\_context\_get\_ipv6\_mcast\_hop\_limit(struct net\_context \*context)

Get IPv6 multicast hop limit value for this context.

**Definition** net\_context.h:829

[net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)

static void net\_context\_set\_proxy\_enabled(struct net\_context \*context, bool enable)

Enable or disable socks proxy support for this context.

**Definition** net\_context.h:865

[net\_context\_get\_ipv4\_ttl](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)

static uint8\_t net\_context\_get\_ipv4\_ttl(struct net\_context \*context)

Get IPv4 TTL (time-to-live) value for this context.

**Definition** net\_context.h:740

[NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1)

#define NET\_CONTEXT\_BOUND\_TO\_IFACE

**Definition** net\_context.h:69

[net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba)

void(\* net\_context\_cb\_t)(struct net\_context \*context, void \*user\_data)

Callback used while iterating over network contexts.

**Definition** net\_context.h:1303

[net\_context\_set\_state](group__net__context.md#gaac934209341db606a4d563b3c48cce45)

static void net\_context\_set\_state(struct net\_context \*context, enum net\_context\_state state)

Set state for this network context.

**Definition** net\_context.h:504

[net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d)

net\_context\_option

**Definition** net\_context.h:1249

[net\_context\_set\_ipv4\_mcast\_ttl](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)

static void net\_context\_set\_ipv4\_mcast\_ttl(struct net\_context \*context, uint8\_t ttl)

Set IPv4 multicast TTL (time-to-live) value for this context.

**Definition** net\_context.h:784

[net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)

void(\* net\_context\_send\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Network data send callback.

**Definition** net\_context.h:114

[net\_context\_update\_recv\_wnd](group__net__context.md#gab3cc2a13e24f9c263bc40cc87d752a9f)

int net\_context\_update\_recv\_wnd(struct net\_context \*context, int32\_t delta)

Update TCP receive window for context.

[net\_context\_foreach](group__net__context.md#gabb751f7d213d00f8eec72a67f4ce3491)

void net\_context\_foreach(net\_context\_cb\_t cb, void \*user\_data)

Go through all the network connections and call callback for each network context.

[net\_context\_set\_option](group__net__context.md#gabd932d5ded649f9a8c8bab40810e9eae)

int net\_context\_set\_option(struct net\_context \*context, enum net\_context\_option option, const void \*value, size\_t len)

Set an connection option for this context.

[net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8)

void(\* net\_tcp\_accept\_cb\_t)(struct net\_context \*new\_context, struct sockaddr \*addr, socklen\_t addrlen, int status, void \*user\_data)

Accept callback.

**Definition** net\_context.h:134

[NET\_CONTEXT\_STATE\_MASK](group__net__context.md#gac63c02e444e17b268c230ba15c7c4339)

#define NET\_CONTEXT\_STATE\_MASK

**Definition** net\_context.h:475

[net\_context\_send](group__net__context.md#gac793e1def18200416e3f679067c56ab3)

int net\_context\_send(struct net\_context \*context, const void \*buf, size\_t len, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data to a peer.

[net\_context\_is\_closing](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)

static bool net\_context\_is\_closing(struct net\_context \*context)

Is this context closing.

**Definition** net\_context.h:449

[NET\_CONTEXT\_FAMILY](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)

#define NET\_CONTEXT\_FAMILY

The address family, connection type and IP protocol are stored into a bit field to save space.

**Definition** net\_context.h:54

[NET\_CONTEXT\_TYPE](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)

#define NET\_CONTEXT\_TYPE

Type of the connection (datagram / stream / raw).

**Definition** net\_context.h:57

[NET\_CONTEXT\_STATE\_SHIFT](group__net__context.md#gacd1592ed32c7de5ecdeb69f569cb701f)

#define NET\_CONTEXT\_STATE\_SHIFT

**Definition** net\_context.h:474

[net\_context\_set\_proto](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)

static void net\_context\_set\_proto(struct net\_context \*context, uint16\_t proto)

Set context IP protocol for this network context.

**Definition** net\_context.h:673

[net\_context\_setup\_pools](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)

#define net\_context\_setup\_pools(context, tx\_pool, data\_pool)

Set custom network buffer pools for context send operations.

**Definition** net\_context.h:1345

[net\_context\_get\_proto](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)

static uint16\_t net\_context\_get\_proto(struct net\_context \*context)

Get context IP protocol for this network context.

**Definition** net\_context.h:658

[net\_context\_get](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)

int net\_context\_get(sa\_family\_t family, enum net\_sock\_type type, uint16\_t ip\_proto, struct net\_context \*\*context)

Get network context.

[net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91)

struct net\_buf\_pool \*(\* net\_pkt\_get\_pool\_func\_t)(void)

Function that is called to get the pool that is used for net\_buf allocations.

**Definition** net\_context.h:189

[NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e)

#define NET\_CONTEXT\_ACCEPTING\_SOCK

Is the socket accepting connections.

**Definition** net\_context.h:63

[net\_context\_get\_option](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)

int net\_context\_get\_option(struct net\_context \*context, enum net\_context\_option option, void \*value, size\_t \*len)

Get connection option value for this context.

[net\_context\_set\_ipv6\_mcast\_hop\_limit](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)

static void net\_context\_set\_ipv6\_mcast\_hop\_limit(struct net\_context \*context, uint8\_t hop\_limit)

Set IPv6 multicast hop limit value for this context.

**Definition** net\_context.h:843

[net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)

void(\* net\_context\_recv\_cb\_t)(struct net\_context \*context, struct net\_pkt \*pkt, union net\_ip\_header \*ip\_hdr, union net\_proto\_header \*proto\_hdr, int status, void \*user\_data)

Network data receive callback.

**Definition** net\_context.h:93

[net\_context\_sendto](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)

int net\_context\_sendto(struct net\_context \*context, const void \*buf, size\_t len, const struct sockaddr \*dst\_addr, socklen\_t addrlen, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data to a peer specified by address.

[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)

static struct net\_if \* net\_context\_get\_iface(struct net\_context \*context)

Get network interface for this context.

**Definition** net\_context.h:690

[NET\_CONTEXT\_CONNECTED](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda18b286eb1d9a61595b70f76eead211e7)

@ NET\_CONTEXT\_CONNECTED

**Definition** net\_context.h:45

[NET\_CONTEXT\_IDLE](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda1997d732e8a49fd42895917afe160de2)

@ NET\_CONTEXT\_IDLE

**Definition** net\_context.h:40

[NET\_CONTEXT\_CONNECTING](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda26bdeef9794c4051446339bb38a6999e)

@ NET\_CONTEXT\_CONNECTING

**Definition** net\_context.h:43

[NET\_CONTEXT\_READY](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda69163a1ec7757a0307b326bdc3e2697b)

@ NET\_CONTEXT\_READY

**Definition** net\_context.h:44

[NET\_CONTEXT\_UNCONNECTED](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8dda8d946fd7f7895cce804bf617313a2c40)

@ NET\_CONTEXT\_UNCONNECTED

**Definition** net\_context.h:41

[NET\_CONTEXT\_CONFIGURING](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8ddaaa50d60ab4b2aa7db248402c522fd3f6)

@ NET\_CONTEXT\_CONFIGURING

**Definition** net\_context.h:42

[NET\_CONTEXT\_LISTENING](group__net__context.md#gga62753cf9e6218d37e65f8b461bf8c8ddab77dbc57d8c05b742bc28f01793179a9)

@ NET\_CONTEXT\_LISTENING

**Definition** net\_context.h:46

[NET\_OPT\_MCAST\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e)

@ NET\_OPT\_MCAST\_TTL

**Definition** net\_context.h:1262

[NET\_OPT\_REUSEADDR](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561)

@ NET\_OPT\_REUSEADDR

**Definition** net\_context.h:1258

[NET\_OPT\_SNDBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08)

@ NET\_OPT\_SNDBUF

**Definition** net\_context.h:1256

[NET\_OPT\_RECV\_PKTINFO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a)

@ NET\_OPT\_RECV\_PKTINFO

**Definition** net\_context.h:1261

[NET\_OPT\_PRIORITY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c)

@ NET\_OPT\_PRIORITY

**Definition** net\_context.h:1250

[NET\_OPT\_REUSEPORT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4)

@ NET\_OPT\_REUSEPORT

**Definition** net\_context.h:1259

[NET\_OPT\_MCAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d)

@ NET\_OPT\_MCAST\_HOP\_LIMIT

**Definition** net\_context.h:1263

[NET\_OPT\_RCVTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076)

@ NET\_OPT\_RCVTIMEO

**Definition** net\_context.h:1253

[NET\_OPT\_TXTIME](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184)

@ NET\_OPT\_TXTIME

**Definition** net\_context.h:1251

[NET\_OPT\_SNDTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668)

@ NET\_OPT\_SNDTIMEO

**Definition** net\_context.h:1254

[NET\_OPT\_SOCKS5](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c)

@ NET\_OPT\_SOCKS5

**Definition** net\_context.h:1252

[NET\_OPT\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184)

@ NET\_OPT\_TTL

**Definition** net\_context.h:1265

[NET\_OPT\_RCVBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1)

@ NET\_OPT\_RCVBUF

**Definition** net\_context.h:1255

[NET\_OPT\_UNICAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3)

@ NET\_OPT\_UNICAST\_HOP\_LIMIT

**Definition** net\_context.h:1264

[NET\_OPT\_DSCP\_ECN](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c)

@ NET\_OPT\_DSCP\_ECN

**Definition** net\_context.h:1257

[NET\_OPT\_IPV6\_V6ONLY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c)

@ NET\_OPT\_IPV6\_V6ONLY

**Definition** net\_context.h:1260

[net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)

int net\_if\_get\_by\_iface(struct net\_if \*iface)

Get interface index according to pointer.

[net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)

struct net\_if \* net\_if\_get\_by\_index(int index)

Get interface according to index.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_stats.h](net__stats_8h.md)

Network statistics.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[k\_condvar](structk__condvar.md)

**Definition** kernel.h:3012

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[msghdr](structmsghdr.md)

**Definition** net\_ip.h:238

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:976

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:201

[net\_context::refcount](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a)

atomic\_t refcount

Reference count.

**Definition** net\_context.h:212

[net\_context::user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb)

void \* user\_data

User data associated with a context.

**Definition** net\_context.h:208

[net\_context::fifo\_reserved](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7)

void \* fifo\_reserved

First member of the structure to allow to put contexts into a FIFO.

**Definition** net\_context.h:204

[net\_context::flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c)

uint16\_t flags

Flags for the context.

**Definition** net\_context.h:358

[net\_context::ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd)

uint8\_t ipv4\_mcast\_ttl

IPv4 multicast TTL.

**Definition** net\_context.h:371

[net\_context::send\_cb](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c)

net\_context\_send\_cb\_t send\_cb

Send callback to be called when the packet has been sent successfully.

**Definition** net\_context.h:239

[net\_context::remote](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c)

struct sockaddr remote

Remote endpoint address.

**Definition** net\_context.h:226

[net\_context::lock](structnet__context.md#a730e72866e94ed1695010b50c618a281)

struct k\_mutex lock

Internal lock for protecting this context from multiple access.

**Definition** net\_context.h:216

[net\_context::local](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955)

struct sockaddr\_ptr local

Local endpoint address.

**Definition** net\_context.h:221

[net\_context::ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb)

uint8\_t ipv4\_ttl

IPv4 TTL.

**Definition** net\_context.h:370

[net\_context::ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7)

uint8\_t ipv6\_mcast\_hop\_limit

IPv6 multicast hop limit.

**Definition** net\_context.h:367

[net\_context::connect\_cb](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d)

net\_context\_connect\_cb\_t connect\_cb

Connect callback to be called when a connection has been established.

**Definition** net\_context.h:244

[net\_context::conn\_handler](structnet__context.md#abd8ff1b4826535df911d2af14b46e312)

struct net\_conn\_handle \* conn\_handler

Connection handle.

**Definition** net\_context.h:229

[net\_context::proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19)

uint16\_t proto

Protocol (UDP, TCP or IEEE 802.3 protocol value).

**Definition** net\_context.h:355

[net\_context::iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)

int8\_t iface

Network interface assigned to this context.

**Definition** net\_context.h:361

[net\_context::tcp](structnet__context.md#adee6e668bfae2749df9b986d0049f10b)

void \* tcp

TCP connection information.

**Definition** net\_context.h:258

[net\_context::options](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07)

struct net\_context::@301222043044136136127251054270033130365030331345 options

Option values.

[net\_context::recv\_cb](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4)

net\_context\_recv\_cb\_t recv\_cb

Receive callback to be called when desired packet has been received.

**Definition** net\_context.h:234

[net\_context::ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4)

uint8\_t ipv6\_hop\_limit

IPv6 hop limit.

**Definition** net\_context.h:366

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_context.h](net__context_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
