---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__context_8h_source.html
original_path: doxygen/html/net__context_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

25

26#include <[zephyr/kernel.h](kernel_8h.md)>

27#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

28

29#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

30#include <[zephyr/net/net\_if.h](net__if_8h.md)>

31#include <[zephyr/net/net\_stats.h](net__stats_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

[ 38](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29)#define NET\_CONTEXT\_IN\_USE BIT(0)

39

41

43enum net\_context\_state {

44 NET\_CONTEXT\_IDLE = 0,

45 NET\_CONTEXT\_UNCONNECTED = 0,

46 NET\_CONTEXT\_CONFIGURING = 1,

47 NET\_CONTEXT\_CONNECTING = 1,

48 NET\_CONTEXT\_READY = 2,

49 NET\_CONTEXT\_CONNECTED = 2,

50 NET\_CONTEXT\_LISTENING = 3,

51};

52

54

[ 60](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)#define NET\_CONTEXT\_FAMILY (BIT(3) | BIT(4) | BIT(5))

61

[ 63](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)#define NET\_CONTEXT\_TYPE (BIT(6) | BIT(7))

64

[ 66](group__net__context.md#ga84206421e8f2e1eb114d393f0c81428b)#define NET\_CONTEXT\_REMOTE\_ADDR\_SET BIT(8)

67

[ 69](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e)#define NET\_CONTEXT\_ACCEPTING\_SOCK BIT(9)

70

[ 72](group__net__context.md#ga90385e51999494c0d530c97b57a01865)#define NET\_CONTEXT\_CLOSING\_SOCK BIT(10)

73

[ 75](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1)#define NET\_CONTEXT\_BOUND\_TO\_IFACE BIT(11)

76

77struct [net\_context](structnet__context.md);

78

[ 99](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)typedef void (\*[net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317))(struct [net\_context](structnet__context.md) \*context,

100 struct [net\_pkt](structnet__pkt.md) \*pkt,

101 union net\_ip\_header \*ip\_hdr,

102 union net\_proto\_header \*proto\_hdr,

103 int status,

104 void \*user\_data);

105

[ 120](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)typedef void (\*[net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93))(struct [net\_context](structnet__context.md) \*context,

121 int status,

122 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

123

[ 140](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8)typedef void (\*[net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8))(struct [net\_context](structnet__context.md) \*new\_context,

141 struct [sockaddr](structsockaddr.md) \*addr,

142 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

143 int status,

144 void \*user\_data);

145

[ 167](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)typedef void (\*[net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71))(struct [net\_context](structnet__context.md) \*context,

168 int status,

169 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

170

171/\* The net\_pkt\_get\_slab\_func\_t is here in order to avoid circular

172 \* dependency between net\_pkt.h and net\_context.h

173 \*/

182typedef struct k\_mem\_slab \*(\*net\_pkt\_get\_slab\_func\_t)(void);

183

184/\* The net\_pkt\_get\_pool\_func\_t is here in order to avoid circular

185 \* dependency between net\_pkt.h and net\_context.h

186 \*/

195typedef struct [net\_buf\_pool](structnet__buf__pool.md) \*(\*net\_pkt\_get\_pool\_func\_t)(void);

196

197struct net\_tcp;

198

199struct net\_conn\_handle;

200

[ 207](structnet__context.md)\_\_net\_socket struct [net\_context](structnet__context.md) {

[ 210](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7) void \*[fifo\_reserved](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7);

211

[ 214](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb) void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb);

215

[ 218](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [refcount](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a);

219

[ 222](structnet__context.md#a730e72866e94ed1695010b50c618a281) struct [k\_mutex](structk__mutex.md) [lock](structnet__context.md#a730e72866e94ed1695010b50c618a281);

223

[ 227](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955) struct sockaddr\_ptr [local](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955);

228

[ 232](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c) struct [sockaddr](structsockaddr.md) [remote](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c);

233

[ 235](structnet__context.md#abd8ff1b4826535df911d2af14b46e312) struct net\_conn\_handle \*[conn\_handler](structnet__context.md#abd8ff1b4826535df911d2af14b46e312);

236

[ 240](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4) [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) [recv\_cb](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4);

241

[ 245](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c) [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) [send\_cb](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c);

246

[ 250](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d) [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) [connect\_cb](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d);

251

252#if defined(CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL)

255 [net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770) tx\_slab;

256

259 [net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91) data\_pool;

260#endif /\* CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL \*/

261

262#if defined(CONFIG\_NET\_TCP)

[ 264](structnet__context.md#adee6e668bfae2749df9b986d0049f10b) void \*[tcp](structnet__context.md#adee6e668bfae2749df9b986d0049f10b);

265#endif /\* CONFIG\_NET\_TCP \*/

266

267#if defined(CONFIG\_NET\_CONTEXT\_SYNC\_RECV)

271 struct k\_sem recv\_data\_wait;

272#endif /\* CONFIG\_NET\_CONTEXT\_SYNC\_RECV \*/

273

274#if defined(CONFIG\_NET\_SOCKETS)

276 void \*socket\_data;

277

279 union {

280 struct [k\_fifo](structk__fifo.md) recv\_q;

281 struct [k\_fifo](structk__fifo.md) accept\_q;

282 };

283

284 struct {

286 struct [k\_condvar](structk__condvar.md) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40);

287

289 struct [k\_mutex](structk__mutex.md) \*lock;

290 } cond;

291#endif /\* CONFIG\_NET\_SOCKETS \*/

292

293#if defined(CONFIG\_NET\_OFFLOAD)

295 void \*offload\_context;

296#endif /\* CONFIG\_NET\_OFFLOAD \*/

297

298#if defined(CONFIG\_NET\_SOCKETS\_CAN)

299 int can\_filter\_id;

300#endif /\* CONFIG\_NET\_SOCKETS\_CAN \*/

301

303 struct {

304#if defined(CONFIG\_NET\_CONTEXT\_PRIORITY)

306 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority;

307#endif

308#if defined(CONFIG\_NET\_CONTEXT\_TXTIME)

310 bool txtime;

311#endif

312#if defined(CONFIG\_SOCKS)

314 struct {

315 struct sockaddr addr;

316 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen;

317 } proxy;

318#endif

319#if defined(CONFIG\_NET\_CONTEXT\_RCVTIMEO)

321 k\_timeout\_t rcvtimeo;

322#endif

323#if defined(CONFIG\_NET\_CONTEXT\_SNDTIMEO)

325 k\_timeout\_t sndtimeo;

326#endif

327#if defined(CONFIG\_NET\_CONTEXT\_RCVBUF)

329 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rcvbuf;

330#endif

331#if defined(CONFIG\_NET\_CONTEXT\_SNDBUF)

333 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sndbuf;

334#endif

335#if defined(CONFIG\_NET\_CONTEXT\_DSCP\_ECN)

340 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dscp\_ecn;

341#endif

342#if defined(CONFIG\_NET\_CONTEXT\_REUSEADDR)

344 bool reuseaddr;

345#endif

346#if defined(CONFIG\_NET\_CONTEXT\_REUSEPORT)

348 bool reuseport;

349#endif

350#if defined(CONFIG\_NET\_IPV4\_MAPPING\_TO\_IPV6)

352 bool ipv6\_v6only;

353#endif

354#if defined(CONFIG\_NET\_CONTEXT\_RECV\_PKTINFO)

356 bool recv\_pktinfo;

357#endif

358#if defined(CONFIG\_NET\_IPV6)

363 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr\_preferences;

364#endif

365#if defined(CONFIG\_NET\_CONTEXT\_TIMESTAMPING)

367 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) timestamping;

368#endif

[ 369](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07) } [options](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07);

370

[ 372](structnet__context.md#abfb04fc163636498f72b29aa12087e19) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19);

373

[ 375](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c);

376

[ 378](structnet__context.md#ad71d151e1e9e35b934949482066f1947) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947);

379

381 union {

382 struct {

[ 383](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4);

[ 384](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7);

385 };

386 struct {

[ 387](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb);

[ 388](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd);

389 };

390 };

391

392#if defined(CONFIG\_SOCKS)

394 bool proxy\_enabled;

395#endif

396

397};

398

[ 406](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)static inline bool [net\_context\_is\_used](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)(struct [net\_context](structnet__context.md) \*context)

407{

408 NET\_ASSERT(context);

409

410 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_IN\_USE](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29);

411}

412

[ 420](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)static inline bool [net\_context\_is\_bound\_to\_iface](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)(struct [net\_context](structnet__context.md) \*context)

421{

422 NET\_ASSERT(context);

423

424 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1);

425}

426

[ 434](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)static inline bool [net\_context\_is\_accepting](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)(struct [net\_context](structnet__context.md) \*context)

435{

436 NET\_ASSERT(context);

437

438 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

439}

440

[ 447](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)static inline void [net\_context\_set\_accepting](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)(struct [net\_context](structnet__context.md) \*context,

448 bool accepting)

449{

450 NET\_ASSERT(context);

451

452 if (accepting) {

453 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

454 } else {

455 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))~[NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

456 }

457}

458

[ 466](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)static inline bool [net\_context\_is\_closing](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)(struct [net\_context](structnet__context.md) \*context)

467{

468 NET\_ASSERT(context);

469

470 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

471}

472

[ 479](group__net__context.md#ga9941aa201206448b6b34789d252f6385)static inline void [net\_context\_set\_closing](group__net__context.md#ga9941aa201206448b6b34789d252f6385)(struct [net\_context](structnet__context.md) \*context,

480 bool closing)

481{

482 NET\_ASSERT(context);

483

484 if (closing) {

485 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

486 } else {

487 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))~[NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

488 }

489}

490

492

493#define NET\_CONTEXT\_STATE\_SHIFT 1

494#define NET\_CONTEXT\_STATE\_MASK 0x03

495

497

507static inline

[ 508](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)enum net\_context\_state [net\_context\_get\_state](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)(struct [net\_context](structnet__context.md) \*context)

509{

510 NET\_ASSERT(context);

511

512 return (enum net\_context\_state)

513 ((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) >> NET\_CONTEXT\_STATE\_SHIFT) &

514 NET\_CONTEXT\_STATE\_MASK);

515}

516

[ 525](group__net__context.md#gaac934209341db606a4d563b3c48cce45)static inline void [net\_context\_set\_state](group__net__context.md#gaac934209341db606a4d563b3c48cce45)(struct [net\_context](structnet__context.md) \*context,

526 enum net\_context\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

527{

528 NET\_ASSERT(context);

529

530 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= ~(NET\_CONTEXT\_STATE\_MASK << NET\_CONTEXT\_STATE\_SHIFT);

531 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= (([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) & NET\_CONTEXT\_STATE\_MASK) <<

532 NET\_CONTEXT\_STATE\_SHIFT);

533}

534

[ 545](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)static inline [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [net\_context\_get\_family](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)(struct [net\_context](structnet__context.md) \*context)

546{

547 NET\_ASSERT(context);

548

549 return ((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_FAMILY](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)) >> 3);

550}

551

[ 561](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)static inline void [net\_context\_set\_family](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)(struct [net\_context](structnet__context.md) \*context,

562 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family)

563{

564 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flag = 0U;

565

566 NET\_ASSERT(context);

567

568 if (family == [AF\_UNSPEC](group__ip__4__6.md#gae77ae24b14b7b7f294f3e04121173f12) || family == [AF\_INET](group__ip__4__6.md#ga9930604d0e32588eae76f43ca38e7826) || family == [AF\_INET6](group__ip__4__6.md#gaa03706b2738b9a58d4985dfbe99e1bac) ||

569 family == [AF\_PACKET](group__ip__4__6.md#gaa89aa4cd481fe17260c3f5d493cc23f5) || family == [AF\_CAN](group__ip__4__6.md#ga546620c7e758f003b24b7fdae4f97bd4)) {

570 /\* Family is in BIT(4), BIT(5) and BIT(6) \*/

571 flag = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(family << 3);

572 }

573

574 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= flag;

575}

576

587static inline

[ 588](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) [net\_context\_get\_type](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)(struct [net\_context](structnet__context.md) \*context)

589{

590 NET\_ASSERT(context);

591

592 return (enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c))((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_TYPE](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)) >> 6);

593}

594

[ 604](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277)static inline void [net\_context\_set\_type](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277)(struct [net\_context](structnet__context.md) \*context,

605 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type)

606{

607 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) flag = 0U;

608

609 NET\_ASSERT(context);

610

611 if (type == [SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc) || type == [SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) || type == [SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)) {

612 /\* Type is in BIT(6) and BIT(7)\*/

613 flag = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))(type << 6);

614 }

615

616 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= flag;

617}

618

627#if defined(CONFIG\_NET\_SOCKETS\_CAN)

628static inline void [net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)(struct [net\_context](structnet__context.md) \*context,

629 int filter\_id)

630{

631 NET\_ASSERT(context);

632

633 context->can\_filter\_id = filter\_id;

634}

635#else

[ 636](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)static inline void [net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)(struct [net\_context](structnet__context.md) \*context,

637 int filter\_id)

638{

639 ARG\_UNUSED(context);

640 ARG\_UNUSED(filter\_id);

641}

642#endif

643

653#if defined(CONFIG\_NET\_SOCKETS\_CAN)

654static inline int [net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)(struct [net\_context](structnet__context.md) \*context)

655{

656 NET\_ASSERT(context);

657

658 return context->can\_filter\_id;

659}

660#else

[ 661](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)static inline int [net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)(struct [net\_context](structnet__context.md) \*context)

662{

663 ARG\_UNUSED(context);

664

665 return -1;

666}

667#endif

668

[ 679](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_context\_get\_proto](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)(struct [net\_context](structnet__context.md) \*context)

680{

681 return context->[proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19);

682}

683

[ 694](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)static inline void [net\_context\_set\_proto](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)(struct [net\_context](structnet__context.md) \*context,

695 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) proto)

696{

697 context->[proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19) = proto;

698}

699

710static inline

[ 711](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)struct [net\_if](structnet__if.md) \*[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)(struct [net\_context](structnet__context.md) \*context)

712{

713 NET\_ASSERT(context);

714

715 return [net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)(context->[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

716}

717

[ 726](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)static inline void [net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)(struct [net\_context](structnet__context.md) \*context,

727 struct [net\_if](structnet__if.md) \*iface)

728{

729 NET\_ASSERT(iface);

730

731 context->[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)(iface);

732}

733

[ 742](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)static inline void [net\_context\_bind\_iface](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)(struct [net\_context](structnet__context.md) \*context,

743 struct [net\_if](structnet__if.md) \*iface)

744{

745 NET\_ASSERT(iface);

746

747 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1);

748 [net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)(context, iface);

749}

750

[ 761](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv4\_ttl](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)(struct [net\_context](structnet__context.md) \*context)

762{

763 return context->[ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb);

764}

765

[ 775](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)static inline void [net\_context\_set\_ipv4\_ttl](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)(struct [net\_context](structnet__context.md) \*context,

776 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

777{

778 context->[ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb) = ttl;

779}

780

[ 791](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv4\_mcast\_ttl](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)(struct [net\_context](structnet__context.md) \*context)

792{

793 return context->[ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd);

794}

795

[ 805](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)static inline void [net\_context\_set\_ipv4\_mcast\_ttl](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)(struct [net\_context](structnet__context.md) \*context,

806 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

807{

808 context->[ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd) = ttl;

809}

810

[ 821](group__net__context.md#ga977b08a77586e0e4752bff725139427c)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv6\_hop\_limit](group__net__context.md#ga977b08a77586e0e4752bff725139427c)(struct [net\_context](structnet__context.md) \*context)

822{

823 return context->[ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4);

824}

825

[ 834](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)static inline void [net\_context\_set\_ipv6\_hop\_limit](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)(struct [net\_context](structnet__context.md) \*context,

835 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

836{

837 context->[ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4) = hop\_limit;

838}

839

[ 850](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv6\_mcast\_hop\_limit](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)(struct [net\_context](structnet__context.md) \*context)

851{

852 return context->[ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7);

853}

854

[ 864](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)static inline void [net\_context\_set\_ipv6\_mcast\_hop\_limit](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)(struct [net\_context](structnet__context.md) \*context,

865 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

866{

867 context->[ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7) = hop\_limit;

868}

869

879#if defined(CONFIG\_SOCKS)

880static inline void [net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)(struct [net\_context](structnet__context.md) \*context,

881 bool enable)

882{

883 context->proxy\_enabled = enable;

884}

885#else

[ 886](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)static inline void [net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)(struct [net\_context](structnet__context.md) \*context,

887 bool enable)

888{

889 ARG\_UNUSED(context);

890 ARG\_UNUSED(enable);

891}

892#endif

893

904#if defined(CONFIG\_SOCKS)

905static inline bool [net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)(struct [net\_context](structnet__context.md) \*context)

906{

907 return context->proxy\_enabled;

908}

909#else

[ 910](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)static inline bool [net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)(struct [net\_context](structnet__context.md) \*context)

911{

912 ARG\_UNUSED(context);

913 return false;

914}

915#endif

916

[ 934](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)int [net\_context\_get](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

935 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

936 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ip\_proto,

937 struct [net\_context](structnet__context.md) \*\*context);

938

[ 952](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)int [net\_context\_put](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)(struct [net\_context](structnet__context.md) \*context);

953

[ 966](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)int [net\_context\_ref](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)(struct [net\_context](structnet__context.md) \*context);

967

[ 981](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)int [net\_context\_unref](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)(struct [net\_context](structnet__context.md) \*context);

982

993#if defined(CONFIG\_NET\_IPV4)

994int [net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)(struct [net\_context](structnet__context.md) \*context,

995 struct [net\_pkt](structnet__pkt.md) \*pkt,

996 const struct [in\_addr](structin__addr.md) \*src,

997 const struct [in\_addr](structin__addr.md) \*dst);

998#else

[ 999](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)static inline int [net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)(struct [net\_context](structnet__context.md) \*context,

1000 struct [net\_pkt](structnet__pkt.md) \*pkt,

1001 const struct [in\_addr](structin__addr.md) \*src,

1002 const struct [in\_addr](structin__addr.md) \*dst)

1003{

1004 return -1;

1005}

1006#endif /\* CONFIG\_NET\_IPV4 \*/

1007

1018#if defined(CONFIG\_NET\_IPV6)

1019int [net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)(struct [net\_context](structnet__context.md) \*context,

1020 struct [net\_pkt](structnet__pkt.md) \*pkt,

1021 const struct [in6\_addr](structin6__addr.md) \*src,

1022 const struct [in6\_addr](structin6__addr.md) \*dst);

1023#else

[ 1024](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)static inline int [net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)(struct [net\_context](structnet__context.md) \*context,

1025 struct [net\_pkt](structnet__pkt.md) \*pkt,

1026 const struct [in6\_addr](structin6__addr.md) \*src,

1027 const struct [in6\_addr](structin6__addr.md) \*dst)

1028{

1029 ARG\_UNUSED(context);

1030 ARG\_UNUSED(pkt);

1031 ARG\_UNUSED(src);

1032 ARG\_UNUSED(dst);

1033 return -1;

1034}

1035#endif /\* CONFIG\_NET\_IPV6 \*/

1036

[ 1048](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)int [net\_context\_bind](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)(struct [net\_context](structnet__context.md) \*context,

1049 const struct [sockaddr](structsockaddr.md) \*addr,

1050 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

1051

[ 1062](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)int [net\_context\_listen](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)(struct [net\_context](structnet__context.md) \*context,

1063 int backlog);

1064

[ 1093](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)int [net\_context\_connect](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)(struct [net\_context](structnet__context.md) \*context,

1094 const struct [sockaddr](structsockaddr.md) \*addr,

1095 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

1096 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

1097 [k\_timeout\_t](structk__timeout__t.md) timeout,

1098 void \*user\_data);

1099

[ 1125](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)int [net\_context\_accept](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)(struct [net\_context](structnet__context.md) \*context,

1126 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

1127 [k\_timeout\_t](structk__timeout__t.md) timeout,

1128 void \*user\_data);

1129

[ 1149](group__net__context.md#gac793e1def18200416e3f679067c56ab3)int [net\_context\_send](group__net__context.md#gac793e1def18200416e3f679067c56ab3)(struct [net\_context](structnet__context.md) \*context,

1150 const void \*buf,

1151 size\_t len,

1152 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1153 [k\_timeout\_t](structk__timeout__t.md) timeout,

1154 void \*user\_data);

1155

[ 1177](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)int [net\_context\_sendto](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)(struct [net\_context](structnet__context.md) \*context,

1178 const void \*buf,

1179 size\_t len,

1180 const struct [sockaddr](structsockaddr.md) \*dst\_addr,

1181 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

1182 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1183 [k\_timeout\_t](structk__timeout__t.md) timeout,

1184 void \*user\_data);

1185

[ 1204](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)int [net\_context\_sendmsg](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)(struct [net\_context](structnet__context.md) \*context,

1205 const struct [msghdr](structmsghdr.md) \*[msghdr](structmsghdr.md),

1206 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

1207 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1208 [k\_timeout\_t](structk__timeout__t.md) timeout,

1209 void \*user\_data);

1210

[ 1247](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)int [net\_context\_recv](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)(struct [net\_context](structnet__context.md) \*context,

1248 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

1249 [k\_timeout\_t](structk__timeout__t.md) timeout,

1250 void \*user\_data);

1251

[ 1272](group__net__context.md#gab3cc2a13e24f9c263bc40cc87d752a9f)int [net\_context\_update\_recv\_wnd](group__net__context.md#gab3cc2a13e24f9c263bc40cc87d752a9f)(struct [net\_context](structnet__context.md) \*context,

1273 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) delta);

1274

[ 1276](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d)enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) {

[ 1277](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c) [NET\_OPT\_PRIORITY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c) = 1,

[ 1278](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184) [NET\_OPT\_TXTIME](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184) = 2,

[ 1279](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c) [NET\_OPT\_SOCKS5](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c) = 3,

[ 1280](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076) [NET\_OPT\_RCVTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076) = 4,

[ 1281](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668) [NET\_OPT\_SNDTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668) = 5,

[ 1282](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1) [NET\_OPT\_RCVBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1) = 6,

[ 1283](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08) [NET\_OPT\_SNDBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08) = 7,

[ 1284](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c) [NET\_OPT\_DSCP\_ECN](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c) = 8,

[ 1285](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561) [NET\_OPT\_REUSEADDR](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561) = 9,

[ 1286](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4) [NET\_OPT\_REUSEPORT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4) = 10,

[ 1287](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c) [NET\_OPT\_IPV6\_V6ONLY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c) = 11,

[ 1288](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a) [NET\_OPT\_RECV\_PKTINFO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a) = 12,

[ 1289](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e) [NET\_OPT\_MCAST\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e) = 13,

[ 1290](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d) [NET\_OPT\_MCAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d) = 14,

[ 1291](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3) [NET\_OPT\_UNICAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3) = 15,

[ 1292](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184) [NET\_OPT\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184) = 16,

[ 1293](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d) [NET\_OPT\_ADDR\_PREFERENCES](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d) = 17,

[ 1294](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2) [NET\_OPT\_TIMESTAMPING](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2) = 18,

1295};

1296

[ 1307](group__net__context.md#gabd932d5ded649f9a8c8bab40810e9eae)int [net\_context\_set\_option](group__net__context.md#gabd932d5ded649f9a8c8bab40810e9eae)(struct [net\_context](structnet__context.md) \*context,

1308 enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) option,

1309 const void \*value, size\_t len);

1310

[ 1321](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)int [net\_context\_get\_option](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)(struct [net\_context](structnet__context.md) \*context,

1322 enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) option,

1323 void \*value, size\_t \*len);

1324

[ 1332](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba)typedef void (\*[net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba))(struct [net\_context](structnet__context.md) \*context, void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

1333

[ 1341](group__net__context.md#gabb751f7d213d00f8eec72a67f4ce3491)void [net\_context\_foreach](group__net__context.md#gabb751f7d213d00f8eec72a67f4ce3491)([net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba) cb, void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

1342

1363#if defined(CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL)

1364static inline void [net\_context\_setup\_pools](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)(struct [net\_context](structnet__context.md) \*context,

1365 [net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770) tx\_slab,

1366 [net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91) data\_pool)

1367{

1368 NET\_ASSERT(context);

1369

1370 context->tx\_slab = tx\_slab;

1371 context->data\_pool = data\_pool;

1372}

1373#else

[ 1374](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)#define net\_context\_setup\_pools(context, tx\_pool, data\_pool)

1375#endif

1376

[ 1390](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)bool [net\_context\_port\_in\_use](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)(enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

1391 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) local\_port, const struct [sockaddr](structsockaddr.md) \*local\_addr);

1392

1393#ifdef \_\_cplusplus

1394}

1395#endif

1396

1400

1401#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_CONTEXT\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:873

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:167

[AF\_CAN](group__ip__4__6.md#ga546620c7e758f003b24b7fdae4f97bd4)

#define AF\_CAN

Controller Area Network.

**Definition** net\_ip.h:58

[AF\_INET](group__ip__4__6.md#ga9930604d0e32588eae76f43ca38e7826)

#define AF\_INET

IP protocol family version 4.

**Definition** net\_ip.h:55

[AF\_INET6](group__ip__4__6.md#gaa03706b2738b9a58d4985dfbe99e1bac)

#define AF\_INET6

IP protocol family version 6.

**Definition** net\_ip.h:56

[AF\_PACKET](group__ip__4__6.md#gaa89aa4cd481fe17260c3f5d493cc23f5)

#define AF\_PACKET

Packet family.

**Definition** net\_ip.h:57

[net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)

net\_sock\_type

Socket type.

**Definition** net\_ip.h:87

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:171

[AF\_UNSPEC](group__ip__4__6.md#gae77ae24b14b7b7f294f3e04121173f12)

#define AF\_UNSPEC

Unspecified address family.

**Definition** net\_ip.h:54

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:64

[SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc)

@ SOCK\_DGRAM

Datagram socket type.

**Definition** net\_ip.h:89

[SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)

@ SOCK\_RAW

RAW socket type.

**Definition** net\_ip.h:90

[SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424)

@ SOCK\_STREAM

Stream socket type.

**Definition** net\_ip.h:88

[net\_context\_set\_type](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277)

static void net\_context\_set\_type(struct net\_context \*context, enum net\_sock\_type type)

Set context type for this network context.

**Definition** net\_context.h:604

[net\_context\_set\_ipv6\_hop\_limit](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)

static void net\_context\_set\_ipv6\_hop\_limit(struct net\_context \*context, uint8\_t hop\_limit)

Set IPv6 hop limit value for this context.

**Definition** net\_context.h:834

[net\_context\_unref](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)

int net\_context\_unref(struct net\_context \*context)

Decrement the reference count to a network context.

[net\_context\_bind](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)

int net\_context\_bind(struct net\_context \*context, const struct sockaddr \*addr, socklen\_t addrlen)

Assign a socket a local address.

[net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)

static void net\_context\_set\_iface(struct net\_context \*context, struct net\_if \*iface)

Set network interface for this context.

**Definition** net\_context.h:726

[net\_context\_set\_ipv4\_ttl](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)

static void net\_context\_set\_ipv4\_ttl(struct net\_context \*context, uint8\_t ttl)

Set IPv4 TTL (time-to-live) value for this context.

**Definition** net\_context.h:775

[net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)

void(\* net\_context\_connect\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Connection callback.

**Definition** net\_context.h:167

[net\_context\_accept](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)

int net\_context\_accept(struct net\_context \*context, net\_tcp\_accept\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Accept a network connection attempt.

[net\_context\_put](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)

int net\_context\_put(struct net\_context \*context)

Close and unref a network context.

[net\_context\_get\_type](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)

static enum net\_sock\_type net\_context\_get\_type(struct net\_context \*context)

Get context type for this network context.

**Definition** net\_context.h:588

[net\_context\_is\_accepting](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)

static bool net\_context\_is\_accepting(struct net\_context \*context)

Is this context is accepting data now.

**Definition** net\_context.h:434

[net\_context\_get\_family](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)

static sa\_family\_t net\_context\_get\_family(struct net\_context \*context)

Get address family for this network context.

**Definition** net\_context.h:545

[net\_context\_is\_bound\_to\_iface](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)

static bool net\_context\_is\_bound\_to\_iface(struct net\_context \*context)

Is this context bound to a network interface.

**Definition** net\_context.h:420

[net\_context\_bind\_iface](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)

static void net\_context\_bind\_iface(struct net\_context \*context, struct net\_if \*iface)

Bind network interface to this context.

**Definition** net\_context.h:742

[net\_context\_listen](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)

int net\_context\_listen(struct net\_context \*context, int backlog)

Mark the context as a listening one.

[net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770)

struct k\_mem\_slab \*(\* net\_pkt\_get\_slab\_func\_t)(void)

Function that is called to get the slab that is used for net\_pkt allocations.

**Definition** net\_context.h:182

[net\_context\_get\_ipv4\_mcast\_ttl](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)

static uint8\_t net\_context\_get\_ipv4\_mcast\_ttl(struct net\_context \*context)

Get IPv4 multicast TTL (time-to-live) value for this context.

**Definition** net\_context.h:791

[net\_context\_is\_used](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)

static bool net\_context\_is\_used(struct net\_context \*context)

Is this context used or not.

**Definition** net\_context.h:406

[net\_context\_sendmsg](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)

int net\_context\_sendmsg(struct net\_context \*context, const struct msghdr \*msghdr, int flags, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data in iovec to a peer specified in msghdr struct.

[net\_context\_ref](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)

int net\_context\_ref(struct net\_context \*context)

Take a reference count to a net\_context, preventing destruction.

[net\_context\_get\_state](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)

static enum net\_context\_state net\_context\_get\_state(struct net\_context \*context)

Get state for this network context.

**Definition** net\_context.h:508

[net\_context\_connect](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)

int net\_context\_connect(struct net\_context \*context, const struct sockaddr \*addr, socklen\_t addrlen, net\_context\_connect\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Create a network connection.

[net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)

static void net\_context\_set\_can\_filter\_id(struct net\_context \*context, int filter\_id)

Set CAN filter id for this network context.

**Definition** net\_context.h:636

[net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)

static bool net\_context\_is\_proxy\_enabled(struct net\_context \*context)

Is socks proxy support enabled or disabled for this context.

**Definition** net\_context.h:910

[NET\_CONTEXT\_IN\_USE](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29)

#define NET\_CONTEXT\_IN\_USE

Is this context used or not.

**Definition** net\_context.h:38

[net\_context\_set\_accepting](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)

static void net\_context\_set\_accepting(struct net\_context \*context, bool accepting)

Set this context to accept data now.

**Definition** net\_context.h:447

[net\_context\_port\_in\_use](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)

bool net\_context\_port\_in\_use(enum net\_ip\_protocol ip\_proto, uint16\_t local\_port, const struct sockaddr \*local\_addr)

Check if a port is in use (bound).

[net\_context\_set\_family](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)

static void net\_context\_set\_family(struct net\_context \*context, sa\_family\_t family)

Set address family for this network context.

**Definition** net\_context.h:561

[net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)

static int net\_context\_create\_ipv6\_new(struct net\_context \*context, struct net\_pkt \*pkt, const struct in6\_addr \*src, const struct in6\_addr \*dst)

Create IPv6 packet in provided net\_pkt from context.

**Definition** net\_context.h:1024

[net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)

static int net\_context\_create\_ipv4\_new(struct net\_context \*context, struct net\_pkt \*pkt, const struct in\_addr \*src, const struct in\_addr \*dst)

Create IPv4 packet in provided net\_pkt from context.

**Definition** net\_context.h:999

[net\_context\_recv](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)

int net\_context\_recv(struct net\_context \*context, net\_context\_recv\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Receive network data from a peer specified by context.

[net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)

static int net\_context\_get\_can\_filter\_id(struct net\_context \*context)

Get CAN filter id for this network context.

**Definition** net\_context.h:661

[NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865)

#define NET\_CONTEXT\_CLOSING\_SOCK

Is the socket closing / closed.

**Definition** net\_context.h:72

[net\_context\_get\_ipv6\_hop\_limit](group__net__context.md#ga977b08a77586e0e4752bff725139427c)

static uint8\_t net\_context\_get\_ipv6\_hop\_limit(struct net\_context \*context)

Get IPv6 hop limit value for this context.

**Definition** net\_context.h:821

[net\_context\_set\_closing](group__net__context.md#ga9941aa201206448b6b34789d252f6385)

static void net\_context\_set\_closing(struct net\_context \*context, bool closing)

Set this context to closing.

**Definition** net\_context.h:479

[net\_context\_get\_ipv6\_mcast\_hop\_limit](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)

static uint8\_t net\_context\_get\_ipv6\_mcast\_hop\_limit(struct net\_context \*context)

Get IPv6 multicast hop limit value for this context.

**Definition** net\_context.h:850

[net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)

static void net\_context\_set\_proxy\_enabled(struct net\_context \*context, bool enable)

Enable or disable socks proxy support for this context.

**Definition** net\_context.h:886

[net\_context\_get\_ipv4\_ttl](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)

static uint8\_t net\_context\_get\_ipv4\_ttl(struct net\_context \*context)

Get IPv4 TTL (time-to-live) value for this context.

**Definition** net\_context.h:761

[NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1)

#define NET\_CONTEXT\_BOUND\_TO\_IFACE

Context is bound to a specific interface.

**Definition** net\_context.h:75

[net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba)

void(\* net\_context\_cb\_t)(struct net\_context \*context, void \*user\_data)

Callback used while iterating over network contexts.

**Definition** net\_context.h:1332

[net\_context\_set\_state](group__net__context.md#gaac934209341db606a4d563b3c48cce45)

static void net\_context\_set\_state(struct net\_context \*context, enum net\_context\_state state)

Set state for this network context.

**Definition** net\_context.h:525

[net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d)

net\_context\_option

Network context options.

**Definition** net\_context.h:1276

[net\_context\_set\_ipv4\_mcast\_ttl](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)

static void net\_context\_set\_ipv4\_mcast\_ttl(struct net\_context \*context, uint8\_t ttl)

Set IPv4 multicast TTL (time-to-live) value for this context.

**Definition** net\_context.h:805

[net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)

void(\* net\_context\_send\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Network data send callback.

**Definition** net\_context.h:120

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

**Definition** net\_context.h:140

[net\_context\_send](group__net__context.md#gac793e1def18200416e3f679067c56ab3)

int net\_context\_send(struct net\_context \*context, const void \*buf, size\_t len, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data to a peer.

[net\_context\_is\_closing](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)

static bool net\_context\_is\_closing(struct net\_context \*context)

Is this context closing.

**Definition** net\_context.h:466

[NET\_CONTEXT\_FAMILY](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)

#define NET\_CONTEXT\_FAMILY

The address family, connection type and IP protocol are stored into a bit field to save space.

**Definition** net\_context.h:60

[NET\_CONTEXT\_TYPE](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)

#define NET\_CONTEXT\_TYPE

Type of the connection (datagram / stream / raw).

**Definition** net\_context.h:63

[net\_context\_set\_proto](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)

static void net\_context\_set\_proto(struct net\_context \*context, uint16\_t proto)

Set context IP protocol for this network context.

**Definition** net\_context.h:694

[net\_context\_setup\_pools](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)

#define net\_context\_setup\_pools(context, tx\_pool, data\_pool)

Set custom network buffer pools for context send operations.

**Definition** net\_context.h:1374

[net\_context\_get\_proto](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)

static uint16\_t net\_context\_get\_proto(struct net\_context \*context)

Get context IP protocol for this network context.

**Definition** net\_context.h:679

[net\_context\_get](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)

int net\_context\_get(sa\_family\_t family, enum net\_sock\_type type, uint16\_t ip\_proto, struct net\_context \*\*context)

Get network context.

[net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91)

struct net\_buf\_pool \*(\* net\_pkt\_get\_pool\_func\_t)(void)

Function that is called to get the pool that is used for net\_buf allocations.

**Definition** net\_context.h:195

[NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e)

#define NET\_CONTEXT\_ACCEPTING\_SOCK

Is the socket accepting connections.

**Definition** net\_context.h:69

[net\_context\_get\_option](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)

int net\_context\_get\_option(struct net\_context \*context, enum net\_context\_option option, void \*value, size\_t \*len)

Get connection option value for this context.

[net\_context\_set\_ipv6\_mcast\_hop\_limit](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)

static void net\_context\_set\_ipv6\_mcast\_hop\_limit(struct net\_context \*context, uint8\_t hop\_limit)

Set IPv6 multicast hop limit value for this context.

**Definition** net\_context.h:864

[net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)

void(\* net\_context\_recv\_cb\_t)(struct net\_context \*context, struct net\_pkt \*pkt, union net\_ip\_header \*ip\_hdr, union net\_proto\_header \*proto\_hdr, int status, void \*user\_data)

Network data receive callback.

**Definition** net\_context.h:99

[net\_context\_sendto](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)

int net\_context\_sendto(struct net\_context \*context, const void \*buf, size\_t len, const struct sockaddr \*dst\_addr, socklen\_t addrlen, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data to a peer specified by address.

[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)

static struct net\_if \* net\_context\_get\_iface(struct net\_context \*context)

Get network interface for this context.

**Definition** net\_context.h:711

[NET\_OPT\_ADDR\_PREFERENCES](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d)

@ NET\_OPT\_ADDR\_PREFERENCES

IPv6 address preference.

**Definition** net\_context.h:1293

[NET\_OPT\_MCAST\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e)

@ NET\_OPT\_MCAST\_TTL

IPv4 multicast TTL.

**Definition** net\_context.h:1289

[NET\_OPT\_REUSEADDR](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561)

@ NET\_OPT\_REUSEADDR

Re-use address.

**Definition** net\_context.h:1285

[NET\_OPT\_SNDBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08)

@ NET\_OPT\_SNDBUF

Send buffer.

**Definition** net\_context.h:1283

[NET\_OPT\_RECV\_PKTINFO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a)

@ NET\_OPT\_RECV\_PKTINFO

Receive packet information.

**Definition** net\_context.h:1288

[NET\_OPT\_PRIORITY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c)

@ NET\_OPT\_PRIORITY

Context priority.

**Definition** net\_context.h:1277

[NET\_OPT\_REUSEPORT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4)

@ NET\_OPT\_REUSEPORT

Re-use port.

**Definition** net\_context.h:1286

[NET\_OPT\_MCAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d)

@ NET\_OPT\_MCAST\_HOP\_LIMIT

IPv6 multicast hop limit.

**Definition** net\_context.h:1290

[NET\_OPT\_RCVTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076)

@ NET\_OPT\_RCVTIMEO

Receive timeout.

**Definition** net\_context.h:1280

[NET\_OPT\_TXTIME](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184)

@ NET\_OPT\_TXTIME

TX time.

**Definition** net\_context.h:1278

[NET\_OPT\_SNDTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668)

@ NET\_OPT\_SNDTIMEO

Send timeout.

**Definition** net\_context.h:1281

[NET\_OPT\_SOCKS5](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c)

@ NET\_OPT\_SOCKS5

SOCKS5.

**Definition** net\_context.h:1279

[NET\_OPT\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184)

@ NET\_OPT\_TTL

IPv4 unicast TTL.

**Definition** net\_context.h:1292

[NET\_OPT\_RCVBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1)

@ NET\_OPT\_RCVBUF

Receive buffer.

**Definition** net\_context.h:1282

[NET\_OPT\_UNICAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3)

@ NET\_OPT\_UNICAST\_HOP\_LIMIT

IPv6 unicast hop limit.

**Definition** net\_context.h:1291

[NET\_OPT\_DSCP\_ECN](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c)

@ NET\_OPT\_DSCP\_ECN

DSCP ECN.

**Definition** net\_context.h:1284

[NET\_OPT\_TIMESTAMPING](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2)

@ NET\_OPT\_TIMESTAMPING

Packet timestamping.

**Definition** net\_context.h:1294

[NET\_OPT\_IPV6\_V6ONLY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c)

@ NET\_OPT\_IPV6\_V6ONLY

Share IPv4 and IPv6 port space.

**Definition** net\_context.h:1287

[net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)

int net\_if\_get\_by\_iface(struct net\_if \*iface)

Get interface index according to pointer.

[net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)

struct net\_if \* net\_if\_get\_by\_index(int index)

Get interface according to index.

[kernel.h](kernel_8h.md)

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

**Definition** net\_ip.h:142

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:154

[k\_condvar](structk__condvar.md)

**Definition** kernel.h:3106

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2468

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[msghdr](structmsghdr.md)

Message struct.

**Definition** net\_ip.h:250

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** net\_buf.h:1078

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:207

[net\_context::refcount](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a)

atomic\_t refcount

Reference count.

**Definition** net\_context.h:218

[net\_context::user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb)

void \* user\_data

User data associated with a context.

**Definition** net\_context.h:214

[net\_context::fifo\_reserved](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7)

void \* fifo\_reserved

First member of the structure to allow to put contexts into a FIFO.

**Definition** net\_context.h:210

[net\_context::flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c)

uint16\_t flags

Flags for the context.

**Definition** net\_context.h:375

[net\_context::ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd)

uint8\_t ipv4\_mcast\_ttl

IPv4 multicast TTL.

**Definition** net\_context.h:388

[net\_context::send\_cb](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c)

net\_context\_send\_cb\_t send\_cb

Send callback to be called when the packet has been sent successfully.

**Definition** net\_context.h:245

[net\_context::remote](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c)

struct sockaddr remote

Remote endpoint address.

**Definition** net\_context.h:232

[net\_context::lock](structnet__context.md#a730e72866e94ed1695010b50c618a281)

struct k\_mutex lock

Internal lock for protecting this context from multiple access.

**Definition** net\_context.h:222

[net\_context::local](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955)

struct sockaddr\_ptr local

Local endpoint address.

**Definition** net\_context.h:227

[net\_context::ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb)

uint8\_t ipv4\_ttl

IPv4 TTL.

**Definition** net\_context.h:387

[net\_context::ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7)

uint8\_t ipv6\_mcast\_hop\_limit

IPv6 multicast hop limit.

**Definition** net\_context.h:384

[net\_context::connect\_cb](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d)

net\_context\_connect\_cb\_t connect\_cb

Connect callback to be called when a connection has been established.

**Definition** net\_context.h:250

[net\_context::conn\_handler](structnet__context.md#abd8ff1b4826535df911d2af14b46e312)

struct net\_conn\_handle \* conn\_handler

Connection handle.

**Definition** net\_context.h:235

[net\_context::proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19)

uint16\_t proto

Protocol (UDP, TCP or IEEE 802.3 protocol value).

**Definition** net\_context.h:372

[net\_context::iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)

int8\_t iface

Network interface assigned to this context.

**Definition** net\_context.h:378

[net\_context::tcp](structnet__context.md#adee6e668bfae2749df9b986d0049f10b)

void \* tcp

TCP connection information.

**Definition** net\_context.h:264

[net\_context::options](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07)

struct net\_context::@301222043044136136127251054270033130365030331345 options

Option values.

[net\_context::recv\_cb](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4)

net\_context\_recv\_cb\_t recv\_cb

Receive callback to be called when desired packet has been received.

**Definition** net\_context.h:240

[net\_context::ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4)

uint8\_t ipv6\_hop\_limit

IPv6 hop limit.

**Definition** net\_context.h:383

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:388

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_context.h](net__context_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
