---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__context_8h_source.html
original_path: doxygen/html/net__context_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

24#include <[zephyr/kernel.h](kernel_8h.md)>

25#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

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

39

41enum net\_context\_state {

42 NET\_CONTEXT\_IDLE = 0,

43 NET\_CONTEXT\_UNCONNECTED = 0,

44 NET\_CONTEXT\_CONFIGURING = 1,

45 NET\_CONTEXT\_CONNECTING = 1,

46 NET\_CONTEXT\_READY = 2,

47 NET\_CONTEXT\_CONNECTED = 2,

48 NET\_CONTEXT\_LISTENING = 3,

49};

50

52

[ 58](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)#define NET\_CONTEXT\_FAMILY (BIT(3) | BIT(4) | BIT(5))

59

[ 61](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)#define NET\_CONTEXT\_TYPE (BIT(6) | BIT(7))

62

[ 64](group__net__context.md#ga84206421e8f2e1eb114d393f0c81428b)#define NET\_CONTEXT\_REMOTE\_ADDR\_SET BIT(8)

65

[ 67](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e)#define NET\_CONTEXT\_ACCEPTING\_SOCK BIT(9)

68

[ 70](group__net__context.md#ga90385e51999494c0d530c97b57a01865)#define NET\_CONTEXT\_CLOSING\_SOCK BIT(10)

71

[ 73](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1)#define NET\_CONTEXT\_BOUND\_TO\_IFACE BIT(11)

74

75struct [net\_context](structnet__context.md);

76

[ 97](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)typedef void (\*[net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317))(struct [net\_context](structnet__context.md) \*context,

98 struct [net\_pkt](structnet__pkt.md) \*pkt,

99 union net\_ip\_header \*ip\_hdr,

100 union net\_proto\_header \*proto\_hdr,

101 int status,

102 void \*user\_data);

103

[ 118](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)typedef void (\*[net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93))(struct [net\_context](structnet__context.md) \*context,

119 int status,

120 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

121

[ 138](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8)typedef void (\*[net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8))(struct [net\_context](structnet__context.md) \*new\_context,

139 struct [sockaddr](structsockaddr.md) \*addr,

140 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

141 int status,

142 void \*user\_data);

143

[ 165](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)typedef void (\*[net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71))(struct [net\_context](structnet__context.md) \*context,

166 int status,

167 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

168

169/\* The net\_pkt\_get\_slab\_func\_t is here in order to avoid circular

170 \* dependency between net\_pkt.h and net\_context.h

171 \*/

180typedef struct k\_mem\_slab \*(\*net\_pkt\_get\_slab\_func\_t)(void);

181

182/\* The net\_pkt\_get\_pool\_func\_t is here in order to avoid circular

183 \* dependency between net\_pkt.h and net\_context.h

184 \*/

193typedef struct [net\_buf\_pool](structnet__buf__pool.md) \*(\*net\_pkt\_get\_pool\_func\_t)(void);

194

195struct net\_tcp;

196

197struct net\_conn\_handle;

198

[ 205](structnet__context.md)\_\_net\_socket struct [net\_context](structnet__context.md) {

[ 208](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7) void \*[fifo\_reserved](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7);

209

[ 212](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb) void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb);

213

[ 216](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [refcount](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a);

217

[ 220](structnet__context.md#a730e72866e94ed1695010b50c618a281) struct [k\_mutex](structk__mutex.md) [lock](structnet__context.md#a730e72866e94ed1695010b50c618a281);

221

[ 225](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955) struct sockaddr\_ptr [local](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955);

226

[ 230](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c) struct [sockaddr](structsockaddr.md) [remote](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c);

231

[ 233](structnet__context.md#abd8ff1b4826535df911d2af14b46e312) struct net\_conn\_handle \*[conn\_handler](structnet__context.md#abd8ff1b4826535df911d2af14b46e312);

234

[ 238](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4) [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) [recv\_cb](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4);

239

[ 243](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c) [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) [send\_cb](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c);

244

[ 248](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d) [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) [connect\_cb](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d);

249

250#if defined(CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL)

253 [net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770) tx\_slab;

254

257 [net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91) data\_pool;

258#endif /\* CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL \*/

259

260#if defined(CONFIG\_NET\_TCP)

[ 262](structnet__context.md#adee6e668bfae2749df9b986d0049f10b) void \*[tcp](structnet__context.md#adee6e668bfae2749df9b986d0049f10b);

263#endif /\* CONFIG\_NET\_TCP \*/

264

265#if defined(CONFIG\_NET\_CONTEXT\_SYNC\_RECV)

269 struct k\_sem recv\_data\_wait;

270#endif /\* CONFIG\_NET\_CONTEXT\_SYNC\_RECV \*/

271

272#if defined(CONFIG\_NET\_SOCKETS)

274 void \*socket\_data;

275

277 union {

278 struct [k\_fifo](structk__fifo.md) recv\_q;

279 struct [k\_fifo](structk__fifo.md) accept\_q;

280 };

281

282 struct {

284 struct [k\_condvar](structk__condvar.md) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40);

285

287 struct [k\_mutex](structk__mutex.md) \*lock;

288 } cond;

289#endif /\* CONFIG\_NET\_SOCKETS \*/

290

291#if defined(CONFIG\_NET\_OFFLOAD)

293 void \*offload\_context;

294#endif /\* CONFIG\_NET\_OFFLOAD \*/

295

296#if defined(CONFIG\_NET\_SOCKETS\_CAN)

297 int can\_filter\_id;

298#endif /\* CONFIG\_NET\_SOCKETS\_CAN \*/

299

301 struct {

302#if defined(CONFIG\_NET\_CONTEXT\_PRIORITY)

304 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority;

305#endif

306#if defined(CONFIG\_NET\_CONTEXT\_TXTIME)

308 bool txtime;

309#endif

310#if defined(CONFIG\_SOCKS)

312 struct {

313 struct sockaddr addr;

314 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen;

315 } proxy;

316#endif

317#if defined(CONFIG\_NET\_CONTEXT\_RCVTIMEO)

319 k\_timeout\_t rcvtimeo;

320#endif

321#if defined(CONFIG\_NET\_CONTEXT\_SNDTIMEO)

323 k\_timeout\_t sndtimeo;

324#endif

325#if defined(CONFIG\_NET\_CONTEXT\_RCVBUF)

327 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rcvbuf;

328#endif

329#if defined(CONFIG\_NET\_CONTEXT\_SNDBUF)

331 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sndbuf;

332#endif

333#if defined(CONFIG\_NET\_CONTEXT\_DSCP\_ECN)

338 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dscp\_ecn;

339#endif

340#if defined(CONFIG\_NET\_CONTEXT\_REUSEADDR)

342 bool reuseaddr;

343#endif

344#if defined(CONFIG\_NET\_CONTEXT\_REUSEPORT)

346 bool reuseport;

347#endif

348#if defined(CONFIG\_NET\_IPV4\_MAPPING\_TO\_IPV6)

350 bool ipv6\_v6only;

351#endif

352#if defined(CONFIG\_NET\_CONTEXT\_RECV\_PKTINFO)

354 bool recv\_pktinfo;

355#endif

356#if defined(CONFIG\_NET\_IPV6)

361 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr\_preferences;

362#endif

363#if defined(CONFIG\_NET\_CONTEXT\_TIMESTAMPING)

365 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) timestamping;

366#endif

[ 367](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07) } [options](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07);

368

[ 370](structnet__context.md#abfb04fc163636498f72b29aa12087e19) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19);

371

[ 373](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c);

374

[ 376](structnet__context.md#ad71d151e1e9e35b934949482066f1947) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947);

377

379 union {

380 struct {

[ 381](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4);

[ 382](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7);

383 };

384 struct {

[ 385](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb);

[ 386](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd);

387 };

388 };

389

390#if defined(CONFIG\_SOCKS)

392 bool proxy\_enabled;

393#endif

394

395};

396

[ 404](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)static inline bool [net\_context\_is\_used](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)(struct [net\_context](structnet__context.md) \*context)

405{

406 NET\_ASSERT(context);

407

408 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_IN\_USE](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29);

409}

410

[ 418](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)static inline bool [net\_context\_is\_bound\_to\_iface](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)(struct [net\_context](structnet__context.md) \*context)

419{

420 NET\_ASSERT(context);

421

422 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1);

423}

424

[ 432](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)static inline bool [net\_context\_is\_accepting](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)(struct [net\_context](structnet__context.md) \*context)

433{

434 NET\_ASSERT(context);

435

436 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

437}

438

[ 445](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)static inline void [net\_context\_set\_accepting](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)(struct [net\_context](structnet__context.md) \*context,

446 bool accepting)

447{

448 NET\_ASSERT(context);

449

450 if (accepting) {

451 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

452 } else {

453 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))~[NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e);

454 }

455}

456

[ 464](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)static inline bool [net\_context\_is\_closing](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)(struct [net\_context](structnet__context.md) \*context)

465{

466 NET\_ASSERT(context);

467

468 return context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

469}

470

[ 477](group__net__context.md#ga9941aa201206448b6b34789d252f6385)static inline void [net\_context\_set\_closing](group__net__context.md#ga9941aa201206448b6b34789d252f6385)(struct [net\_context](structnet__context.md) \*context,

478 bool closing)

479{

480 NET\_ASSERT(context);

481

482 if (closing) {

483 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

484 } else {

485 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))~[NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865);

486 }

487}

488

490

491#define NET\_CONTEXT\_STATE\_SHIFT 1

492#define NET\_CONTEXT\_STATE\_MASK 0x03

493

495

505static inline

[ 506](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)enum net\_context\_state [net\_context\_get\_state](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)(struct [net\_context](structnet__context.md) \*context)

507{

508 NET\_ASSERT(context);

509

510 return (enum net\_context\_state)

511 ((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) >> NET\_CONTEXT\_STATE\_SHIFT) &

512 NET\_CONTEXT\_STATE\_MASK);

513}

514

[ 523](group__net__context.md#gaac934209341db606a4d563b3c48cce45)static inline void [net\_context\_set\_state](group__net__context.md#gaac934209341db606a4d563b3c48cce45)(struct [net\_context](structnet__context.md) \*context,

524 enum net\_context\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

525{

526 NET\_ASSERT(context);

527

528 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) &= ~(NET\_CONTEXT\_STATE\_MASK << NET\_CONTEXT\_STATE\_SHIFT);

529 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= (([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) & NET\_CONTEXT\_STATE\_MASK) <<

530 NET\_CONTEXT\_STATE\_SHIFT);

531}

532

[ 543](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)static inline [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) [net\_context\_get\_family](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)(struct [net\_context](structnet__context.md) \*context)

544{

545 NET\_ASSERT(context);

546

547 return ((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_FAMILY](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)) >> 3);

548}

549

[ 559](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)static inline void [net\_context\_set\_family](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)(struct [net\_context](structnet__context.md) \*context,

560 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family)

561{

562 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flag = 0U;

563

564 NET\_ASSERT(context);

565

566 if (family == [AF\_UNSPEC](group__ip__4__6.md#gae77ae24b14b7b7f294f3e04121173f12) || family == [AF\_INET](group__ip__4__6.md#ga9930604d0e32588eae76f43ca38e7826) || family == [AF\_INET6](group__ip__4__6.md#gaa03706b2738b9a58d4985dfbe99e1bac) ||

567 family == [AF\_PACKET](group__ip__4__6.md#gaa89aa4cd481fe17260c3f5d493cc23f5) || family == [AF\_CAN](group__ip__4__6.md#ga546620c7e758f003b24b7fdae4f97bd4)) {

568 /\* Family is in BIT(4), BIT(5) and BIT(6) \*/

569 flag = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(family << 3);

570 }

571

572 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= flag;

573}

574

585static inline

[ 586](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) [net\_context\_get\_type](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)(struct [net\_context](structnet__context.md) \*context)

587{

588 NET\_ASSERT(context);

589

590 return (enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c))((context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) & [NET\_CONTEXT\_TYPE](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)) >> 6);

591}

592

[ 602](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277)static inline void [net\_context\_set\_type](group__net__context.md#ga01c11c1dfce101df046df9ade00ed277)(struct [net\_context](structnet__context.md) \*context,

603 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type)

604{

605 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) flag = 0U;

606

607 NET\_ASSERT(context);

608

609 if (type == [SOCK\_DGRAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5ca006b373a518eeeb717573f91e70d7fcc) || type == [SOCK\_STREAM](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cae3b7fb9487113a31d403b23aaeaad424) || type == [SOCK\_RAW](group__ip__4__6.md#ggaaab4268707dbe08348b98fb028e7aa5cad78d54561daf9c4a7cda0ce115e3f231)) {

610 /\* Type is in BIT(6) and BIT(7)\*/

611 flag = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))(type << 6);

612 }

613

614 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= flag;

615}

616

625#if defined(CONFIG\_NET\_SOCKETS\_CAN)

626static inline void [net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)(struct [net\_context](structnet__context.md) \*context,

627 int filter\_id)

628{

629 NET\_ASSERT(context);

630

631 context->can\_filter\_id = filter\_id;

632}

633#else

[ 634](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)static inline void [net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)(struct [net\_context](structnet__context.md) \*context,

635 int filter\_id)

636{

637 ARG\_UNUSED(context);

638 ARG\_UNUSED(filter\_id);

639}

640#endif

641

651#if defined(CONFIG\_NET\_SOCKETS\_CAN)

652static inline int [net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)(struct [net\_context](structnet__context.md) \*context)

653{

654 NET\_ASSERT(context);

655

656 return context->can\_filter\_id;

657}

658#else

[ 659](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)static inline int [net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)(struct [net\_context](structnet__context.md) \*context)

660{

661 ARG\_UNUSED(context);

662

663 return -1;

664}

665#endif

666

[ 677](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_context\_get\_proto](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)(struct [net\_context](structnet__context.md) \*context)

678{

679 return context->[proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19);

680}

681

[ 692](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)static inline void [net\_context\_set\_proto](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)(struct [net\_context](structnet__context.md) \*context,

693 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) proto)

694{

695 context->[proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19) = proto;

696}

697

708static inline

[ 709](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)struct [net\_if](structnet__if.md) \*[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)(struct [net\_context](structnet__context.md) \*context)

710{

711 NET\_ASSERT(context);

712

713 return [net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516)(context->[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

714}

715

[ 724](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)static inline void [net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)(struct [net\_context](structnet__context.md) \*context,

725 struct [net\_if](structnet__if.md) \*iface)

726{

727 NET\_ASSERT(iface);

728

729 context->[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630)(iface);

730}

731

[ 740](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)static inline void [net\_context\_bind\_iface](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)(struct [net\_context](structnet__context.md) \*context,

741 struct [net\_if](structnet__if.md) \*iface)

742{

743 NET\_ASSERT(iface);

744

745 context->[flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c) |= [NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1);

746 [net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)(context, iface);

747}

748

[ 759](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv4\_ttl](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)(struct [net\_context](structnet__context.md) \*context)

760{

761 return context->[ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb);

762}

763

[ 773](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)static inline void [net\_context\_set\_ipv4\_ttl](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)(struct [net\_context](structnet__context.md) \*context,

774 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

775{

776 context->[ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb) = ttl;

777}

778

[ 789](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv4\_mcast\_ttl](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)(struct [net\_context](structnet__context.md) \*context)

790{

791 return context->[ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd);

792}

793

[ 803](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)static inline void [net\_context\_set\_ipv4\_mcast\_ttl](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)(struct [net\_context](structnet__context.md) \*context,

804 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

805{

806 context->[ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd) = ttl;

807}

808

[ 819](group__net__context.md#ga977b08a77586e0e4752bff725139427c)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv6\_hop\_limit](group__net__context.md#ga977b08a77586e0e4752bff725139427c)(struct [net\_context](structnet__context.md) \*context)

820{

821 return context->[ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4);

822}

823

[ 832](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)static inline void [net\_context\_set\_ipv6\_hop\_limit](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)(struct [net\_context](structnet__context.md) \*context,

833 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

834{

835 context->[ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4) = hop\_limit;

836}

837

[ 848](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_context\_get\_ipv6\_mcast\_hop\_limit](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)(struct [net\_context](structnet__context.md) \*context)

849{

850 return context->[ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7);

851}

852

[ 862](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)static inline void [net\_context\_set\_ipv6\_mcast\_hop\_limit](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)(struct [net\_context](structnet__context.md) \*context,

863 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

864{

865 context->[ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7) = hop\_limit;

866}

867

877#if defined(CONFIG\_SOCKS)

878static inline void [net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)(struct [net\_context](structnet__context.md) \*context,

879 bool enable)

880{

881 context->proxy\_enabled = enable;

882}

883#else

[ 884](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)static inline void [net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)(struct [net\_context](structnet__context.md) \*context,

885 bool enable)

886{

887 ARG\_UNUSED(context);

888 ARG\_UNUSED(enable);

889}

890#endif

891

902#if defined(CONFIG\_SOCKS)

903static inline bool [net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)(struct [net\_context](structnet__context.md) \*context)

904{

905 return context->proxy\_enabled;

906}

907#else

[ 908](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)static inline bool [net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)(struct [net\_context](structnet__context.md) \*context)

909{

910 ARG\_UNUSED(context);

911 return false;

912}

913#endif

914

[ 932](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)int [net\_context\_get](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

933 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

934 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ip\_proto,

935 struct [net\_context](structnet__context.md) \*\*context);

936

[ 950](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)int [net\_context\_put](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)(struct [net\_context](structnet__context.md) \*context);

951

[ 964](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)int [net\_context\_ref](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)(struct [net\_context](structnet__context.md) \*context);

965

[ 979](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)int [net\_context\_unref](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)(struct [net\_context](structnet__context.md) \*context);

980

991#if defined(CONFIG\_NET\_IPV4)

992int [net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)(struct [net\_context](structnet__context.md) \*context,

993 struct [net\_pkt](structnet__pkt.md) \*pkt,

994 const struct [in\_addr](structin__addr.md) \*src,

995 const struct [in\_addr](structin__addr.md) \*dst);

996#else

[ 997](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)static inline int [net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)(struct [net\_context](structnet__context.md) \*context,

998 struct [net\_pkt](structnet__pkt.md) \*pkt,

999 const struct [in\_addr](structin__addr.md) \*src,

1000 const struct [in\_addr](structin__addr.md) \*dst)

1001{

1002 return -1;

1003}

1004#endif /\* CONFIG\_NET\_IPV4 \*/

1005

1016#if defined(CONFIG\_NET\_IPV6)

1017int [net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)(struct [net\_context](structnet__context.md) \*context,

1018 struct [net\_pkt](structnet__pkt.md) \*pkt,

1019 const struct [in6\_addr](structin6__addr.md) \*src,

1020 const struct [in6\_addr](structin6__addr.md) \*dst);

1021#else

[ 1022](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)static inline int [net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)(struct [net\_context](structnet__context.md) \*context,

1023 struct [net\_pkt](structnet__pkt.md) \*pkt,

1024 const struct [in6\_addr](structin6__addr.md) \*src,

1025 const struct [in6\_addr](structin6__addr.md) \*dst)

1026{

1027 ARG\_UNUSED(context);

1028 ARG\_UNUSED(pkt);

1029 ARG\_UNUSED(src);

1030 ARG\_UNUSED(dst);

1031 return -1;

1032}

1033#endif /\* CONFIG\_NET\_IPV6 \*/

1034

[ 1046](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)int [net\_context\_bind](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)(struct [net\_context](structnet__context.md) \*context,

1047 const struct [sockaddr](structsockaddr.md) \*addr,

1048 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

1049

[ 1060](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)int [net\_context\_listen](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)(struct [net\_context](structnet__context.md) \*context,

1061 int backlog);

1062

[ 1091](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)int [net\_context\_connect](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)(struct [net\_context](structnet__context.md) \*context,

1092 const struct [sockaddr](structsockaddr.md) \*addr,

1093 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

1094 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

1095 [k\_timeout\_t](structk__timeout__t.md) timeout,

1096 void \*user\_data);

1097

[ 1123](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)int [net\_context\_accept](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)(struct [net\_context](structnet__context.md) \*context,

1124 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

1125 [k\_timeout\_t](structk__timeout__t.md) timeout,

1126 void \*user\_data);

1127

[ 1147](group__net__context.md#gac793e1def18200416e3f679067c56ab3)int [net\_context\_send](group__net__context.md#gac793e1def18200416e3f679067c56ab3)(struct [net\_context](structnet__context.md) \*context,

1148 const void \*buf,

1149 size\_t len,

1150 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1151 [k\_timeout\_t](structk__timeout__t.md) timeout,

1152 void \*user\_data);

1153

[ 1175](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)int [net\_context\_sendto](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)(struct [net\_context](structnet__context.md) \*context,

1176 const void \*buf,

1177 size\_t len,

1178 const struct [sockaddr](structsockaddr.md) \*dst\_addr,

1179 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

1180 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1181 [k\_timeout\_t](structk__timeout__t.md) timeout,

1182 void \*user\_data);

1183

[ 1202](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)int [net\_context\_sendmsg](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)(struct [net\_context](structnet__context.md) \*context,

1203 const struct [msghdr](structmsghdr.md) \*[msghdr](structmsghdr.md),

1204 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

1205 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

1206 [k\_timeout\_t](structk__timeout__t.md) timeout,

1207 void \*user\_data);

1208

[ 1245](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)int [net\_context\_recv](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)(struct [net\_context](structnet__context.md) \*context,

1246 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

1247 [k\_timeout\_t](structk__timeout__t.md) timeout,

1248 void \*user\_data);

1249

[ 1270](group__net__context.md#gab3cc2a13e24f9c263bc40cc87d752a9f)int [net\_context\_update\_recv\_wnd](group__net__context.md#gab3cc2a13e24f9c263bc40cc87d752a9f)(struct [net\_context](structnet__context.md) \*context,

1271 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) delta);

1272

[ 1274](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d)enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) {

[ 1275](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c) [NET\_OPT\_PRIORITY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c) = 1,

[ 1276](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184) [NET\_OPT\_TXTIME](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184) = 2,

[ 1277](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c) [NET\_OPT\_SOCKS5](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c) = 3,

[ 1278](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076) [NET\_OPT\_RCVTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076) = 4,

[ 1279](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668) [NET\_OPT\_SNDTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668) = 5,

[ 1280](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1) [NET\_OPT\_RCVBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1) = 6,

[ 1281](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08) [NET\_OPT\_SNDBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08) = 7,

[ 1282](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c) [NET\_OPT\_DSCP\_ECN](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c) = 8,

[ 1283](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561) [NET\_OPT\_REUSEADDR](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561) = 9,

[ 1284](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4) [NET\_OPT\_REUSEPORT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4) = 10,

[ 1285](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c) [NET\_OPT\_IPV6\_V6ONLY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c) = 11,

[ 1286](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a) [NET\_OPT\_RECV\_PKTINFO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a) = 12,

[ 1287](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e) [NET\_OPT\_MCAST\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e) = 13,

[ 1288](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d) [NET\_OPT\_MCAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d) = 14,

[ 1289](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3) [NET\_OPT\_UNICAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3) = 15,

[ 1290](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184) [NET\_OPT\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184) = 16,

[ 1291](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d) [NET\_OPT\_ADDR\_PREFERENCES](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d) = 17,

[ 1292](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2) [NET\_OPT\_TIMESTAMPING](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2) = 18,

1293};

1294

[ 1305](group__net__context.md#gabd932d5ded649f9a8c8bab40810e9eae)int [net\_context\_set\_option](group__net__context.md#gabd932d5ded649f9a8c8bab40810e9eae)(struct [net\_context](structnet__context.md) \*context,

1306 enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) option,

1307 const void \*value, size\_t len);

1308

[ 1319](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)int [net\_context\_get\_option](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)(struct [net\_context](structnet__context.md) \*context,

1320 enum [net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d) option,

1321 void \*value, size\_t \*len);

1322

[ 1330](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba)typedef void (\*[net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba))(struct [net\_context](structnet__context.md) \*context, void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

1331

[ 1339](group__net__context.md#gabb751f7d213d00f8eec72a67f4ce3491)void [net\_context\_foreach](group__net__context.md#gabb751f7d213d00f8eec72a67f4ce3491)([net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba) cb, void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

1340

1361#if defined(CONFIG\_NET\_CONTEXT\_NET\_PKT\_POOL)

1362static inline void [net\_context\_setup\_pools](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)(struct [net\_context](structnet__context.md) \*context,

1363 [net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770) tx\_slab,

1364 [net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91) data\_pool)

1365{

1366 NET\_ASSERT(context);

1367

1368 context->tx\_slab = tx\_slab;

1369 context->data\_pool = data\_pool;

1370}

1371#else

[ 1372](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)#define net\_context\_setup\_pools(context, tx\_pool, data\_pool)

1373#endif

1374

[ 1388](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)bool [net\_context\_port\_in\_use](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)(enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

1389 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) local\_port, const struct [sockaddr](structsockaddr.md) \*local\_addr);

1390

1391#ifdef \_\_cplusplus

1392}

1393#endif

1394

1398

1399#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_CONTEXT\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:922

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

**Definition** net\_context.h:602

[net\_context\_set\_ipv6\_hop\_limit](group__net__context.md#ga0cbf8377e7757881033aab3e718b1a61)

static void net\_context\_set\_ipv6\_hop\_limit(struct net\_context \*context, uint8\_t hop\_limit)

Set IPv6 hop limit value for this context.

**Definition** net\_context.h:832

[net\_context\_unref](group__net__context.md#ga0d391690d9d6972ce6f4baedeab64b11)

int net\_context\_unref(struct net\_context \*context)

Decrement the reference count to a network context.

[net\_context\_bind](group__net__context.md#ga0fb749331a4f21148ca5a7f364f241b9)

int net\_context\_bind(struct net\_context \*context, const struct sockaddr \*addr, socklen\_t addrlen)

Assign a socket a local address.

[net\_context\_set\_iface](group__net__context.md#ga10399e3f3d159de9325ac7632ce25c51)

static void net\_context\_set\_iface(struct net\_context \*context, struct net\_if \*iface)

Set network interface for this context.

**Definition** net\_context.h:724

[net\_context\_set\_ipv4\_ttl](group__net__context.md#ga11672ca3ebdae63b0013ad76959304d5)

static void net\_context\_set\_ipv4\_ttl(struct net\_context \*context, uint8\_t ttl)

Set IPv4 TTL (time-to-live) value for this context.

**Definition** net\_context.h:773

[net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)

void(\* net\_context\_connect\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Connection callback.

**Definition** net\_context.h:165

[net\_context\_accept](group__net__context.md#ga1b056999d9ab8f2d3b3c0f4788f36cdd)

int net\_context\_accept(struct net\_context \*context, net\_tcp\_accept\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Accept a network connection attempt.

[net\_context\_put](group__net__context.md#ga1d6b64e302c546db589c661f4b6bda98)

int net\_context\_put(struct net\_context \*context)

Close and unref a network context.

[net\_context\_get\_type](group__net__context.md#ga24b4d99dddc4fabf383f5d8079650337)

static enum net\_sock\_type net\_context\_get\_type(struct net\_context \*context)

Get context type for this network context.

**Definition** net\_context.h:586

[net\_context\_is\_accepting](group__net__context.md#ga26aa811e18a6808b6255713ac89c5773)

static bool net\_context\_is\_accepting(struct net\_context \*context)

Is this context is accepting data now.

**Definition** net\_context.h:432

[net\_context\_get\_family](group__net__context.md#ga2c55e45a4ff4d4898766d7c391f63f3c)

static sa\_family\_t net\_context\_get\_family(struct net\_context \*context)

Get address family for this network context.

**Definition** net\_context.h:543

[net\_context\_is\_bound\_to\_iface](group__net__context.md#ga2f6d614158c999fa68e518393c0a9c35)

static bool net\_context\_is\_bound\_to\_iface(struct net\_context \*context)

Is this context bound to a network interface.

**Definition** net\_context.h:418

[net\_context\_bind\_iface](group__net__context.md#ga2f8fccd2453227706e313ac056f1c6ef)

static void net\_context\_bind\_iface(struct net\_context \*context, struct net\_if \*iface)

Bind network interface to this context.

**Definition** net\_context.h:740

[net\_context\_listen](group__net__context.md#ga3803c0d738fbb9d786f401aacc10a4d3)

int net\_context\_listen(struct net\_context \*context, int backlog)

Mark the context as a listening one.

[net\_pkt\_get\_slab\_func\_t](group__net__context.md#ga3bb4bbd522ede36213bafe86f2d1d770)

struct k\_mem\_slab \*(\* net\_pkt\_get\_slab\_func\_t)(void)

Function that is called to get the slab that is used for net\_pkt allocations.

**Definition** net\_context.h:180

[net\_context\_get\_ipv4\_mcast\_ttl](group__net__context.md#ga3db832f40b6a0b975a282ef354a7bffc)

static uint8\_t net\_context\_get\_ipv4\_mcast\_ttl(struct net\_context \*context)

Get IPv4 multicast TTL (time-to-live) value for this context.

**Definition** net\_context.h:789

[net\_context\_is\_used](group__net__context.md#ga423103d5c386b602737e23ee81f2a961)

static bool net\_context\_is\_used(struct net\_context \*context)

Is this context used or not.

**Definition** net\_context.h:404

[net\_context\_sendmsg](group__net__context.md#ga437f04b1629542d2fcf43a15003dcac0)

int net\_context\_sendmsg(struct net\_context \*context, const struct msghdr \*msghdr, int flags, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data in iovec to a peer specified in msghdr struct.

[net\_context\_ref](group__net__context.md#ga4c0ef9540a0d7e800c4529274f5c22f4)

int net\_context\_ref(struct net\_context \*context)

Take a reference count to a net\_context, preventing destruction.

[net\_context\_get\_state](group__net__context.md#ga53bd5f35a142f1d43f90d3bde99778e0)

static enum net\_context\_state net\_context\_get\_state(struct net\_context \*context)

Get state for this network context.

**Definition** net\_context.h:506

[net\_context\_connect](group__net__context.md#ga56b2c5fc3f6a97664944cae1c1eb5dad)

int net\_context\_connect(struct net\_context \*context, const struct sockaddr \*addr, socklen\_t addrlen, net\_context\_connect\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Create a network connection.

[net\_context\_set\_can\_filter\_id](group__net__context.md#ga581582c0461b36088d21d0fd433cc284)

static void net\_context\_set\_can\_filter\_id(struct net\_context \*context, int filter\_id)

Set CAN filter id for this network context.

**Definition** net\_context.h:634

[net\_context\_is\_proxy\_enabled](group__net__context.md#ga5c3a841ff54ddb53cedcccefde5a7d7a)

static bool net\_context\_is\_proxy\_enabled(struct net\_context \*context)

Is socks proxy support enabled or disabled for this context.

**Definition** net\_context.h:908

[NET\_CONTEXT\_IN\_USE](group__net__context.md#ga5e2f5fcc08863a4090bc04040ee88d29)

#define NET\_CONTEXT\_IN\_USE

Is this context used or not.

**Definition** net\_context.h:36

[net\_context\_set\_accepting](group__net__context.md#ga5fac6b26abfff86f29c087f6cddcceed)

static void net\_context\_set\_accepting(struct net\_context \*context, bool accepting)

Set this context to accept data now.

**Definition** net\_context.h:445

[net\_context\_port\_in\_use](group__net__context.md#ga64c7442eeaa3ed82e54f50d2b30d67a0)

bool net\_context\_port\_in\_use(enum net\_ip\_protocol ip\_proto, uint16\_t local\_port, const struct sockaddr \*local\_addr)

Check if a port is in use (bound).

[net\_context\_set\_family](group__net__context.md#ga6ef48a4b15c086167d44a8ed6a82478f)

static void net\_context\_set\_family(struct net\_context \*context, sa\_family\_t family)

Set address family for this network context.

**Definition** net\_context.h:559

[net\_context\_create\_ipv6\_new](group__net__context.md#ga71263ea6e2788d67fa2ac77e309aba2a)

static int net\_context\_create\_ipv6\_new(struct net\_context \*context, struct net\_pkt \*pkt, const struct in6\_addr \*src, const struct in6\_addr \*dst)

Create IPv6 packet in provided net\_pkt from context.

**Definition** net\_context.h:1022

[net\_context\_create\_ipv4\_new](group__net__context.md#ga742a09074bf286ac016f17bcbeb4ef68)

static int net\_context\_create\_ipv4\_new(struct net\_context \*context, struct net\_pkt \*pkt, const struct in\_addr \*src, const struct in\_addr \*dst)

Create IPv4 packet in provided net\_pkt from context.

**Definition** net\_context.h:997

[net\_context\_recv](group__net__context.md#ga74f919185f8af074c2d90aa04733dd2a)

int net\_context\_recv(struct net\_context \*context, net\_context\_recv\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Receive network data from a peer specified by context.

[net\_context\_get\_can\_filter\_id](group__net__context.md#ga7f4d732a99cb9e86fcd5226fbbb727f4)

static int net\_context\_get\_can\_filter\_id(struct net\_context \*context)

Get CAN filter id for this network context.

**Definition** net\_context.h:659

[NET\_CONTEXT\_CLOSING\_SOCK](group__net__context.md#ga90385e51999494c0d530c97b57a01865)

#define NET\_CONTEXT\_CLOSING\_SOCK

Is the socket closing / closed.

**Definition** net\_context.h:70

[net\_context\_get\_ipv6\_hop\_limit](group__net__context.md#ga977b08a77586e0e4752bff725139427c)

static uint8\_t net\_context\_get\_ipv6\_hop\_limit(struct net\_context \*context)

Get IPv6 hop limit value for this context.

**Definition** net\_context.h:819

[net\_context\_set\_closing](group__net__context.md#ga9941aa201206448b6b34789d252f6385)

static void net\_context\_set\_closing(struct net\_context \*context, bool closing)

Set this context to closing.

**Definition** net\_context.h:477

[net\_context\_get\_ipv6\_mcast\_hop\_limit](group__net__context.md#ga99b5f0ded5d56b735e051ede5651f435)

static uint8\_t net\_context\_get\_ipv6\_mcast\_hop\_limit(struct net\_context \*context)

Get IPv6 multicast hop limit value for this context.

**Definition** net\_context.h:848

[net\_context\_set\_proxy\_enabled](group__net__context.md#ga9bd6b5e9429b6e845d41f6cbf242c092)

static void net\_context\_set\_proxy\_enabled(struct net\_context \*context, bool enable)

Enable or disable socks proxy support for this context.

**Definition** net\_context.h:884

[net\_context\_get\_ipv4\_ttl](group__net__context.md#ga9cdb3e5849a5b2663e0a38ac2a39a427)

static uint8\_t net\_context\_get\_ipv4\_ttl(struct net\_context \*context)

Get IPv4 TTL (time-to-live) value for this context.

**Definition** net\_context.h:759

[NET\_CONTEXT\_BOUND\_TO\_IFACE](group__net__context.md#gaa337bccec2c1df42540f236bb33a70e1)

#define NET\_CONTEXT\_BOUND\_TO\_IFACE

Context is bound to a specific interface.

**Definition** net\_context.h:73

[net\_context\_cb\_t](group__net__context.md#gaa82d80fa18693b98dc363c35104075ba)

void(\* net\_context\_cb\_t)(struct net\_context \*context, void \*user\_data)

Callback used while iterating over network contexts.

**Definition** net\_context.h:1330

[net\_context\_set\_state](group__net__context.md#gaac934209341db606a4d563b3c48cce45)

static void net\_context\_set\_state(struct net\_context \*context, enum net\_context\_state state)

Set state for this network context.

**Definition** net\_context.h:523

[net\_context\_option](group__net__context.md#gab03a354899ff68f6b9d127bc3bb5e17d)

net\_context\_option

Network context options.

**Definition** net\_context.h:1274

[net\_context\_set\_ipv4\_mcast\_ttl](group__net__context.md#gab2a2064fa33613a60ad40597d0971774)

static void net\_context\_set\_ipv4\_mcast\_ttl(struct net\_context \*context, uint8\_t ttl)

Set IPv4 multicast TTL (time-to-live) value for this context.

**Definition** net\_context.h:803

[net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)

void(\* net\_context\_send\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Network data send callback.

**Definition** net\_context.h:118

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

**Definition** net\_context.h:138

[net\_context\_send](group__net__context.md#gac793e1def18200416e3f679067c56ab3)

int net\_context\_send(struct net\_context \*context, const void \*buf, size\_t len, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data to a peer.

[net\_context\_is\_closing](group__net__context.md#gac8acf87f9b405df923a258c9f163e38b)

static bool net\_context\_is\_closing(struct net\_context \*context)

Is this context closing.

**Definition** net\_context.h:464

[NET\_CONTEXT\_FAMILY](group__net__context.md#gac8f6e3a16d52e8e376c38eec0ed8a940)

#define NET\_CONTEXT\_FAMILY

The address family, connection type and IP protocol are stored into a bit field to save space.

**Definition** net\_context.h:58

[NET\_CONTEXT\_TYPE](group__net__context.md#gac9b4cf9beecaac5bf05db3111c803678)

#define NET\_CONTEXT\_TYPE

Type of the connection (datagram / stream / raw).

**Definition** net\_context.h:61

[net\_context\_set\_proto](group__net__context.md#gadcd0049229580244ea89fbc98bf23a81)

static void net\_context\_set\_proto(struct net\_context \*context, uint16\_t proto)

Set context IP protocol for this network context.

**Definition** net\_context.h:692

[net\_context\_setup\_pools](group__net__context.md#gadde93ce383a4c5b0f450db1eaa0dfd4d)

#define net\_context\_setup\_pools(context, tx\_pool, data\_pool)

Set custom network buffer pools for context send operations.

**Definition** net\_context.h:1372

[net\_context\_get\_proto](group__net__context.md#gadf41291ca5be067e830d121000ca3f51)

static uint16\_t net\_context\_get\_proto(struct net\_context \*context)

Get context IP protocol for this network context.

**Definition** net\_context.h:677

[net\_context\_get](group__net__context.md#gae21d27ce120ab72b58b1c20ec1d7ceff)

int net\_context\_get(sa\_family\_t family, enum net\_sock\_type type, uint16\_t ip\_proto, struct net\_context \*\*context)

Get network context.

[net\_pkt\_get\_pool\_func\_t](group__net__context.md#gae3082af116955d4175c025a02b296c91)

struct net\_buf\_pool \*(\* net\_pkt\_get\_pool\_func\_t)(void)

Function that is called to get the pool that is used for net\_buf allocations.

**Definition** net\_context.h:193

[NET\_CONTEXT\_ACCEPTING\_SOCK](group__net__context.md#gae4bfc7d561f99a5c50fa725496dfd69e)

#define NET\_CONTEXT\_ACCEPTING\_SOCK

Is the socket accepting connections.

**Definition** net\_context.h:67

[net\_context\_get\_option](group__net__context.md#gaeec55aee0a2029f8877a953ea137f39c)

int net\_context\_get\_option(struct net\_context \*context, enum net\_context\_option option, void \*value, size\_t \*len)

Get connection option value for this context.

[net\_context\_set\_ipv6\_mcast\_hop\_limit](group__net__context.md#gaf29d5ee244c552d78171938a903fbaca)

static void net\_context\_set\_ipv6\_mcast\_hop\_limit(struct net\_context \*context, uint8\_t hop\_limit)

Set IPv6 multicast hop limit value for this context.

**Definition** net\_context.h:862

[net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)

void(\* net\_context\_recv\_cb\_t)(struct net\_context \*context, struct net\_pkt \*pkt, union net\_ip\_header \*ip\_hdr, union net\_proto\_header \*proto\_hdr, int status, void \*user\_data)

Network data receive callback.

**Definition** net\_context.h:97

[net\_context\_sendto](group__net__context.md#gafb0230083b9bdc85c21752d9efb6fb10)

int net\_context\_sendto(struct net\_context \*context, const void \*buf, size\_t len, const struct sockaddr \*dst\_addr, socklen\_t addrlen, net\_context\_send\_cb\_t cb, k\_timeout\_t timeout, void \*user\_data)

Send data to a peer specified by address.

[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)

static struct net\_if \* net\_context\_get\_iface(struct net\_context \*context)

Get network interface for this context.

**Definition** net\_context.h:709

[NET\_OPT\_ADDR\_PREFERENCES](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da1f07858aaff6ad3563b55f259a86aa1d)

@ NET\_OPT\_ADDR\_PREFERENCES

IPv6 address preference.

**Definition** net\_context.h:1291

[NET\_OPT\_MCAST\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da269ca33f7a00e7f06eac37590760a99e)

@ NET\_OPT\_MCAST\_TTL

IPv4 multicast TTL.

**Definition** net\_context.h:1287

[NET\_OPT\_REUSEADDR](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da31aa3bc733899047d20cc8dfec432561)

@ NET\_OPT\_REUSEADDR

Re-use address.

**Definition** net\_context.h:1283

[NET\_OPT\_SNDBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3542360bf19c689e2e4d840f84821d08)

@ NET\_OPT\_SNDBUF

Send buffer.

**Definition** net\_context.h:1281

[NET\_OPT\_RECV\_PKTINFO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da3b8dc8cf712bd53ce71a8a24ef97774a)

@ NET\_OPT\_RECV\_PKTINFO

Receive packet information.

**Definition** net\_context.h:1286

[NET\_OPT\_PRIORITY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5aa24385cbf7da64f7187e03273acb6c)

@ NET\_OPT\_PRIORITY

Context priority.

**Definition** net\_context.h:1275

[NET\_OPT\_REUSEPORT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5d9632b0ff54c2e0aeff9f9e4fdbc6a4)

@ NET\_OPT\_REUSEPORT

Re-use port.

**Definition** net\_context.h:1284

[NET\_OPT\_MCAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da5e44b3bf8253de4c17d7a6d4ffc89d7d)

@ NET\_OPT\_MCAST\_HOP\_LIMIT

IPv6 multicast hop limit.

**Definition** net\_context.h:1288

[NET\_OPT\_RCVTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da629f8f361f17083b3629de8f94020076)

@ NET\_OPT\_RCVTIMEO

Receive timeout.

**Definition** net\_context.h:1278

[NET\_OPT\_TXTIME](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da6d0b17e0b623eaefeb0ef9b35f8ec184)

@ NET\_OPT\_TXTIME

TX time.

**Definition** net\_context.h:1276

[NET\_OPT\_SNDTIMEO](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17da7a8d12a1a628d785e07c811e9132d668)

@ NET\_OPT\_SNDTIMEO

Send timeout.

**Definition** net\_context.h:1279

[NET\_OPT\_SOCKS5](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daa0b8e154dcb188b840f37db1c6af505c)

@ NET\_OPT\_SOCKS5

SOCKS5.

**Definition** net\_context.h:1277

[NET\_OPT\_TTL](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daca77bcaeb320f80b2c72c3b658171184)

@ NET\_OPT\_TTL

IPv4 unicast TTL.

**Definition** net\_context.h:1290

[NET\_OPT\_RCVBUF](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dacc0865b355a3c2c09fc2a222a63b27c1)

@ NET\_OPT\_RCVBUF

Receive buffer.

**Definition** net\_context.h:1280

[NET\_OPT\_UNICAST\_HOP\_LIMIT](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dade9965d38db776fb3a9b577663717ac3)

@ NET\_OPT\_UNICAST\_HOP\_LIMIT

IPv6 unicast hop limit.

**Definition** net\_context.h:1289

[NET\_OPT\_DSCP\_ECN](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17dae3b24711effb8e952fadd3280516399c)

@ NET\_OPT\_DSCP\_ECN

DSCP ECN.

**Definition** net\_context.h:1282

[NET\_OPT\_TIMESTAMPING](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daeb8e032333fe0b7fb40c5be1ba91c3c2)

@ NET\_OPT\_TIMESTAMPING

Packet timestamping.

**Definition** net\_context.h:1292

[NET\_OPT\_IPV6\_V6ONLY](group__net__context.md#ggab03a354899ff68f6b9d127bc3bb5e17daf421f7f2f5cf66b3079ef99c27ba701c)

@ NET\_OPT\_IPV6\_V6ONLY

Share IPv4 and IPv6 port space.

**Definition** net\_context.h:1285

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

**Definition** net\_ip.h:139

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[k\_condvar](structk__condvar.md)

**Definition** kernel.h:3029

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2391

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2917

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[msghdr](structmsghdr.md)

Message struct.

**Definition** net\_ip.h:247

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:1076

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:205

[net\_context::refcount](structnet__context.md#a0ae23462dcc7f84c95e0cc69dfeb6d5a)

atomic\_t refcount

Reference count.

**Definition** net\_context.h:216

[net\_context::user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb)

void \* user\_data

User data associated with a context.

**Definition** net\_context.h:212

[net\_context::fifo\_reserved](structnet__context.md#a2c6f6d484e8744ec97aa966d6f0079c7)

void \* fifo\_reserved

First member of the structure to allow to put contexts into a FIFO.

**Definition** net\_context.h:208

[net\_context::flags](structnet__context.md#a300e382f78b20f220fc1b450784bbd3c)

uint16\_t flags

Flags for the context.

**Definition** net\_context.h:373

[net\_context::ipv4\_mcast\_ttl](structnet__context.md#a329f737a3eaf0a57aa6700c59f3733dd)

uint8\_t ipv4\_mcast\_ttl

IPv4 multicast TTL.

**Definition** net\_context.h:386

[net\_context::send\_cb](structnet__context.md#a38c83746c8b2fcddf187a20299d6eb3c)

net\_context\_send\_cb\_t send\_cb

Send callback to be called when the packet has been sent successfully.

**Definition** net\_context.h:243

[net\_context::remote](structnet__context.md#a4a58fc21990e3c3ddb5ebf77c8212b9c)

struct sockaddr remote

Remote endpoint address.

**Definition** net\_context.h:230

[net\_context::lock](structnet__context.md#a730e72866e94ed1695010b50c618a281)

struct k\_mutex lock

Internal lock for protecting this context from multiple access.

**Definition** net\_context.h:220

[net\_context::local](structnet__context.md#a7ed765f4d8b9cdc0fbd080287215f955)

struct sockaddr\_ptr local

Local endpoint address.

**Definition** net\_context.h:225

[net\_context::ipv4\_ttl](structnet__context.md#a9a9116844b52dc0366f770f3e6c572eb)

uint8\_t ipv4\_ttl

IPv4 TTL.

**Definition** net\_context.h:385

[net\_context::ipv6\_mcast\_hop\_limit](structnet__context.md#ab6d310ba4253933448584fa40e6ff4b7)

uint8\_t ipv6\_mcast\_hop\_limit

IPv6 multicast hop limit.

**Definition** net\_context.h:382

[net\_context::connect\_cb](structnet__context.md#abc30f85e6016901b1d6fbb771b07370d)

net\_context\_connect\_cb\_t connect\_cb

Connect callback to be called when a connection has been established.

**Definition** net\_context.h:248

[net\_context::conn\_handler](structnet__context.md#abd8ff1b4826535df911d2af14b46e312)

struct net\_conn\_handle \* conn\_handler

Connection handle.

**Definition** net\_context.h:233

[net\_context::proto](structnet__context.md#abfb04fc163636498f72b29aa12087e19)

uint16\_t proto

Protocol (UDP, TCP or IEEE 802.3 protocol value).

**Definition** net\_context.h:370

[net\_context::iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)

int8\_t iface

Network interface assigned to this context.

**Definition** net\_context.h:376

[net\_context::tcp](structnet__context.md#adee6e668bfae2749df9b986d0049f10b)

void \* tcp

TCP connection information.

**Definition** net\_context.h:262

[net\_context::options](structnet__context.md#ae3d6ad67411b3e590fe8a627437c1d07)

struct net\_context::@301222043044136136127251054270033130365030331345 options

Option values.

[net\_context::recv\_cb](structnet__context.md#af551b252faf29ee6018d4bd783c5f2b4)

net\_context\_recv\_cb\_t recv\_cb

Receive callback to be called when desired packet has been received.

**Definition** net\_context.h:238

[net\_context::ipv6\_hop\_limit](structnet__context.md#af9801980b3f2bb16f5ea2126a6e18cb4)

uint8\_t ipv6\_hop\_limit

IPv6 hop limit.

**Definition** net\_context.h:381

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_context.h](net__context_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
