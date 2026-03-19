---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__offload_8h_source.html
original_path: doxygen/html/net__offload_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_offload.h

[Go to the documentation of this file.](net__offload_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_OFFLOAD\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_NET\_OFFLOAD\_H\_

14

23

24#include <[zephyr/net\_buf.h](net__buf_8h.md)>

25#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

26#include <[zephyr/net/net\_context.h](net__context_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

32#if defined(CONFIG\_NET\_OFFLOAD)

33

35

36static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout\_to\_int32([k\_timeout\_t](structk__timeout__t.md) timeout)

37{

38 if ([K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f))) {

39 return 0;

40 } else if ([K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca))) {

41 return -1;

42 } else {

43 return [k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)(timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa));

44 }

45}

46

48

52struct net\_offload {

56 int (\*get)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

57 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

58 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

59 struct net\_context \*\*context);

60

64 int (\*[bind](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8))(struct net\_context \*context,

65 const struct sockaddr \*addr,

66 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

67

72 int (\*[listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028))(struct net\_context \*context, int backlog);

73

78 int (\*[connect](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb))(struct net\_context \*context,

79 const struct sockaddr \*addr,

80 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

81 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

82 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

83 void \*user\_data);

84

89 int (\*[accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864))(struct net\_context \*context,

90 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

91 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

92 void \*user\_data);

93

97 int (\*[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f))(struct net\_pkt \*pkt,

98 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

99 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

100 void \*user\_data);

101

105 int (\*[sendto](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8))(struct net\_pkt \*pkt,

106 const struct sockaddr \*dst\_addr,

107 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

108 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

109 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

110 void \*user\_data);

111

116 int (\*[recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276))(struct net\_context \*context,

117 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

118 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

119 void \*user\_data);

120

124 int (\*put)(struct net\_context \*context);

125};

126

144static inline int net\_offload\_get(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

145 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

146 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

147 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

148 struct [net\_context](structnet__context.md) \*\*context)

149{

150 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

151 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

152 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->get);

153

154 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->get(family, type, ip\_proto, context);

155}

156

170static inline int net\_offload\_bind(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

171 struct [net\_context](structnet__context.md) \*context,

172 const struct [sockaddr](structsockaddr.md) \*addr,

173 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

174{

175 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

176 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

177 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[bind](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8));

178

179 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->bind(context, addr, addrlen);

180}

181

194static inline int net\_offload\_listen(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

195 struct [net\_context](structnet__context.md) \*context,

196 int backlog)

197{

198 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

199 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

200 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028));

201

202 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->listen(context, backlog);

203}

204

234static inline int net\_offload\_connect(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

235 struct [net\_context](structnet__context.md) \*context,

236 const struct [sockaddr](structsockaddr.md) \*addr,

237 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

238 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

239 [k\_timeout\_t](structk__timeout__t.md) timeout,

240 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

241{

242 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

243 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

244 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[connect](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb));

245

246 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->connect(

247 context, addr, addrlen, cb,

248 timeout\_to\_int32(timeout),

249 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

250}

251

279static inline int net\_offload\_accept(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

280 struct [net\_context](structnet__context.md) \*context,

281 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

282 [k\_timeout\_t](structk__timeout__t.md) timeout,

283 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

284{

285 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

286 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

287 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864));

288

289 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->accept(

290 context, cb,

291 timeout\_to\_int32(timeout),

292 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

293}

294

321static inline int net\_offload\_send(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

322 struct [net\_pkt](structnet__pkt.md) \*pkt,

323 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

324 [k\_timeout\_t](structk__timeout__t.md) timeout,

325 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

326{

327 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

328 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

329 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f));

330

331 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->send(

332 pkt, cb,

333 timeout\_to\_int32(timeout),

334 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

335}

336

365static inline int net\_offload\_sendto(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

366 struct [net\_pkt](structnet__pkt.md) \*pkt,

367 const struct [sockaddr](structsockaddr.md) \*dst\_addr,

368 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

369 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

370 [k\_timeout\_t](structk__timeout__t.md) timeout,

371 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

372{

373 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

374 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

375 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[sendto](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8));

376

377 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->sendto(

378 pkt, dst\_addr, addrlen, cb,

379 timeout\_to\_int32(timeout),

380 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

381}

382

416static inline int net\_offload\_recv(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

417 struct [net\_context](structnet__context.md) \*context,

418 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

419 [k\_timeout\_t](structk__timeout__t.md) timeout,

420 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

421{

422 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

423 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

424 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276));

425

426 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->recv(

427 context, cb,

428 timeout\_to\_int32(timeout),

429 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

430}

431

445static inline int net\_offload\_put(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

446 struct [net\_context](structnet__context.md) \*context)

447{

448 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

449 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

450 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->put);

451

452 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->put(context);

453}

454

455#else

456

458

459static inline int net\_offload\_get(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

460 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

461 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

462 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

463 struct [net\_context](structnet__context.md) \*\*context)

464{

465 return 0;

466}

467

468static inline int net\_offload\_bind(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

469 struct [net\_context](structnet__context.md) \*context,

470 const struct [sockaddr](structsockaddr.md) \*addr,

471 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

472{

473 return 0;

474}

475

476static inline int net\_offload\_listen(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

477 struct [net\_context](structnet__context.md) \*context,

478 int backlog)

479{

480 return 0;

481}

482

483static inline int net\_offload\_connect(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

484 struct [net\_context](structnet__context.md) \*context,

485 const struct [sockaddr](structsockaddr.md) \*addr,

486 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

487 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

488 [k\_timeout\_t](structk__timeout__t.md) timeout,

489 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

490{

491 return 0;

492}

493

494static inline int net\_offload\_accept(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

495 struct [net\_context](structnet__context.md) \*context,

496 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

497 [k\_timeout\_t](structk__timeout__t.md) timeout,

498 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

499{

500 return 0;

501}

502

503static inline int net\_offload\_send(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

504 struct [net\_pkt](structnet__pkt.md) \*pkt,

505 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

506 [k\_timeout\_t](structk__timeout__t.md) timeout,

507 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

508{

509 return 0;

510}

511

512static inline int net\_offload\_sendto(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

513 struct [net\_pkt](structnet__pkt.md) \*pkt,

514 const struct [sockaddr](structsockaddr.md) \*dst\_addr,

515 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

516 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

517 [k\_timeout\_t](structk__timeout__t.md) timeout,

518 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

519{

520 return 0;

521}

522

523static inline int net\_offload\_recv(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

524 struct [net\_context](structnet__context.md) \*context,

525 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

526 [k\_timeout\_t](structk__timeout__t.md) timeout,

527 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

528{

529 return 0;

530}

531

532static inline int net\_offload\_put(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

533 struct [net\_context](structnet__context.md) \*context)

534{

535 return 0;

536}

537

539

540#endif /\* CONFIG\_NET\_OFFLOAD \*/

541

542#ifdef \_\_cplusplus

543}

544#endif

545

549

550#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_OFFLOAD\_H\_ \*/

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1467

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1357

[K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)

#define K\_TIMEOUT\_EQ(a, b)

Compare timeouts for equality.

**Definition** sys\_clock.h:80

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)

net\_sock\_type

Socket type.

**Definition** net\_ip.h:88

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:64

[net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)

void(\* net\_context\_connect\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Connection callback.

**Definition** net\_context.h:167

[net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)

void(\* net\_context\_send\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Network data send callback.

**Definition** net\_context.h:120

[net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8)

void(\* net\_tcp\_accept\_cb\_t)(struct net\_context \*new\_context, struct sockaddr \*addr, socklen\_t addrlen, int status, void \*user\_data)

Accept callback.

**Definition** net\_context.h:140

[net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)

void(\* net\_context\_recv\_cb\_t)(struct net\_context \*context, struct net\_pkt \*pkt, union net\_ip\_header \*ip\_hdr, union net\_proto\_header \*proto\_hdr, int status, void \*user\_data)

Network data receive callback.

**Definition** net\_context.h:99

[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)

static struct net\_offload \* net\_if\_offload(struct net\_if \*iface)

Return the IP offload plugin.

**Definition** net\_if.h:1038

[k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)

#define k\_ticks\_to\_ms\_floor32(t)

Convert ticks to milliseconds.

**Definition** time\_units.h:1707

[net\_buf.h](net__buf_8h.md)

Buffer management.

[net\_context.h](net__context_8h.md)

Network context definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[bind](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8)

int bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)

ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

[accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864)

int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028)

int listen(int sock, int backlog)

[connect](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)

int connect(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

[sendto](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8)

ssize\_t sendto(int sock, const void \*buf, size\_t len, int flags, const struct sockaddr \*dest\_addr, socklen\_t addrlen)

[recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)

ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[k\_timeout\_t::ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa)

k\_ticks\_t ticks

**Definition** sys\_clock.h:66

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:207

[net\_context::user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb)

void \* user\_data

User data associated with a context.

**Definition** net\_context.h:214

[net\_context::iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)

int8\_t iface

Network interface assigned to this context.

**Definition** net\_context.h:408

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:408

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_offload.h](net__offload_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
