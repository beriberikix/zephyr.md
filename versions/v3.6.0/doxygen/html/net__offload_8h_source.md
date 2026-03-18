---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__offload_8h_source.html
original_path: doxygen/html/net__offload_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

21

22#include <[zephyr/net/buf.h](net_2buf_8h.md)>

23#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

24#include <[zephyr/net/net\_context.h](net__context_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

30#if defined(CONFIG\_NET\_OFFLOAD)

31

33

34static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout\_to\_int32([k\_timeout\_t](structk__timeout__t.md) timeout)

35{

36 if ([K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f))) {

37 return 0;

38 } else if ([K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca))) {

39 return -1;

40 } else {

41 return [k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)(timeout.[ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa));

42 }

43}

44

46

50struct net\_offload {

54 int (\*get)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

55 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

56 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

57 struct net\_context \*\*context);

58

62 int (\*[bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9))(struct net\_context \*context,

63 const struct sockaddr \*addr,

64 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

65

70 int (\*[listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb))(struct net\_context \*context, int backlog);

71

76 int (\*[connect](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386))(struct net\_context \*context,

77 const struct sockaddr \*addr,

78 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

79 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

80 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

81 void \*user\_data);

82

87 int (\*[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb))(struct net\_context \*context,

88 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

89 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

90 void \*user\_data);

91

95 int (\*[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d))(struct net\_pkt \*pkt,

96 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

97 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

98 void \*user\_data);

99

103 int (\*[sendto](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035))(struct net\_pkt \*pkt,

104 const struct sockaddr \*dst\_addr,

105 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

106 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

107 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

108 void \*user\_data);

109

114 int (\*[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))(struct net\_context \*context,

115 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

116 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout,

117 void \*user\_data);

118

122 int (\*put)(struct net\_context \*context);

123};

124

142static inline int net\_offload\_get(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

143 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

144 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

145 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

146 struct [net\_context](structnet__context.md) \*\*context)

147{

148 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

149 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

150 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->get);

151

152 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->get(family, type, ip\_proto, context);

153}

154

168static inline int net\_offload\_bind(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

169 struct [net\_context](structnet__context.md) \*context,

170 const struct [sockaddr](structsockaddr.md) \*addr,

171 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

172{

173 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

174 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

175 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9));

176

177 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->bind(context, addr, addrlen);

178}

179

192static inline int net\_offload\_listen(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

193 struct [net\_context](structnet__context.md) \*context,

194 int backlog)

195{

196 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

197 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

198 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb));

199

200 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->listen(context, backlog);

201}

202

232static inline int net\_offload\_connect(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

233 struct [net\_context](structnet__context.md) \*context,

234 const struct [sockaddr](structsockaddr.md) \*addr,

235 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

236 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

237 [k\_timeout\_t](structk__timeout__t.md) timeout,

238 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

239{

240 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

241 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

242 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[connect](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386));

243

244 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->connect(

245 context, addr, addrlen, cb,

246 timeout\_to\_int32(timeout),

247 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

248}

249

277static inline int net\_offload\_accept(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

278 struct [net\_context](structnet__context.md) \*context,

279 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

280 [k\_timeout\_t](structk__timeout__t.md) timeout,

281 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

282{

283 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

284 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

285 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb));

286

287 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->accept(

288 context, cb,

289 timeout\_to\_int32(timeout),

290 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

291}

292

319static inline int net\_offload\_send(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

320 struct [net\_pkt](structnet__pkt.md) \*pkt,

321 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

322 [k\_timeout\_t](structk__timeout__t.md) timeout,

323 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

324{

325 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

326 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

327 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d));

328

329 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->send(

330 pkt, cb,

331 timeout\_to\_int32(timeout),

332 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

333}

334

363static inline int net\_offload\_sendto(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

364 struct [net\_pkt](structnet__pkt.md) \*pkt,

365 const struct [sockaddr](structsockaddr.md) \*dst\_addr,

366 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

367 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

368 [k\_timeout\_t](structk__timeout__t.md) timeout,

369 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

370{

371 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

372 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

373 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[sendto](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035));

374

375 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->sendto(

376 pkt, dst\_addr, addrlen, cb,

377 timeout\_to\_int32(timeout),

378 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

379}

380

414static inline int net\_offload\_recv(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

415 struct [net\_context](structnet__context.md) \*context,

416 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

417 [k\_timeout\_t](structk__timeout__t.md) timeout,

418 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

419{

420 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

421 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

422 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

423

424 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->recv(

425 context, cb,

426 timeout\_to\_int32(timeout),

427 [user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb));

428}

429

443static inline int net\_offload\_put(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

444 struct [net\_context](structnet__context.md) \*context)

445{

446 NET\_ASSERT([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947));

447 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)));

448 NET\_ASSERT([net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->put);

449

450 return [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)([iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947))->put(context);

451}

452

453#else

454

456

457static inline int net\_offload\_get(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

458 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

459 enum [net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c) type,

460 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) ip\_proto,

461 struct [net\_context](structnet__context.md) \*\*context)

462{

463 return 0;

464}

465

466static inline int net\_offload\_bind(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

467 struct [net\_context](structnet__context.md) \*context,

468 const struct [sockaddr](structsockaddr.md) \*addr,

469 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

470{

471 return 0;

472}

473

474static inline int net\_offload\_listen(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

475 struct [net\_context](structnet__context.md) \*context,

476 int backlog)

477{

478 return 0;

479}

480

481static inline int net\_offload\_connect(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

482 struct [net\_context](structnet__context.md) \*context,

483 const struct [sockaddr](structsockaddr.md) \*addr,

484 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

485 [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) cb,

486 [k\_timeout\_t](structk__timeout__t.md) timeout,

487 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

488{

489 return 0;

490}

491

492static inline int net\_offload\_accept(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

493 struct [net\_context](structnet__context.md) \*context,

494 [net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8) cb,

495 [k\_timeout\_t](structk__timeout__t.md) timeout,

496 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

497{

498 return 0;

499}

500

501static inline int net\_offload\_send(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

502 struct [net\_pkt](structnet__pkt.md) \*pkt,

503 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

504 [k\_timeout\_t](structk__timeout__t.md) timeout,

505 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

506{

507 return 0;

508}

509

510static inline int net\_offload\_sendto(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

511 struct [net\_pkt](structnet__pkt.md) \*pkt,

512 const struct [sockaddr](structsockaddr.md) \*dst\_addr,

513 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

514 [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) cb,

515 [k\_timeout\_t](structk__timeout__t.md) timeout,

516 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

517{

518 return 0;

519}

520

521static inline int net\_offload\_recv(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

522 struct [net\_context](structnet__context.md) \*context,

523 [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) cb,

524 [k\_timeout\_t](structk__timeout__t.md) timeout,

525 void \*[user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb))

526{

527 return 0;

528}

529

530static inline int net\_offload\_put(struct [net\_if](structnet__if.md) \*[iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947),

531 struct [net\_context](structnet__context.md) \*context)

532{

533 return 0;

534}

535

537

538#endif /\* CONFIG\_NET\_OFFLOAD \*/

539

540#ifdef \_\_cplusplus

541}

542#endif

543

547

548#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_OFFLOAD\_H\_ \*/

[bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9)

static int bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

POSIX wrapper for zsock\_bind.

**Definition** socket.h:857

[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)

static int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_accept.

**Definition** socket.h:876

[listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb)

static int listen(int sock, int backlog)

POSIX wrapper for zsock\_listen.

**Definition** socket.h:870

[sendto](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035)

static ssize\_t sendto(int sock, const void \*buf, size\_t len, int flags, const struct sockaddr \*dest\_addr, socklen\_t addrlen)

POSIX wrapper for zsock\_sendto.

**Definition** socket.h:926

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:882

[connect](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386)

static int connect(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

POSIX wrapper for zsock\_connect.

**Definition** socket.h:863

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:888

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1361

[K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)

#define K\_NO\_WAIT

Generate null timeout delay.

**Definition** kernel.h:1251

[K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)

#define K\_TIMEOUT\_EQ(a, b)

Compare timeouts for equality.

**Definition** sys\_clock.h:80

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[net\_sock\_type](group__ip__4__6.md#gaaab4268707dbe08348b98fb028e7aa5c)

net\_sock\_type

Socket type.

**Definition** net\_ip.h:84

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:62

[net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71)

void(\* net\_context\_connect\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Connection callback.

**Definition** net\_context.h:161

[net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93)

void(\* net\_context\_send\_cb\_t)(struct net\_context \*context, int status, void \*user\_data)

Network data send callback.

**Definition** net\_context.h:114

[net\_tcp\_accept\_cb\_t](group__net__context.md#gabf7bcbd5b7beec6766b22e59a8ca73c8)

void(\* net\_tcp\_accept\_cb\_t)(struct net\_context \*new\_context, struct sockaddr \*addr, socklen\_t addrlen, int status, void \*user\_data)

Accept callback.

**Definition** net\_context.h:134

[net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317)

void(\* net\_context\_recv\_cb\_t)(struct net\_context \*context, struct net\_pkt \*pkt, union net\_ip\_header \*ip\_hdr, union net\_proto\_header \*proto\_hdr, int status, void \*user\_data)

Network data receive callback.

**Definition** net\_context.h:93

[net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a)

static struct net\_offload \* net\_if\_offload(struct net\_if \*iface)

Return the IP offload plugin.

**Definition** net\_if.h:908

[k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)

#define k\_ticks\_to\_ms\_floor32(t)

Convert ticks to milliseconds.

**Definition** time\_units.h:1254

[buf.h](net_2buf_8h.md)

Buffer management.

[net\_context.h](net__context_8h.md)

Network context definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

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

**Definition** net\_context.h:201

[net\_context::user\_data](structnet__context.md#a1679e131dd6626bc210f23938df3fbcb)

void \* user\_data

User data associated with a context.

**Definition** net\_context.h:208

[net\_context::iface](structnet__context.md#ad71d151e1e9e35b934949482066f1947)

int8\_t iface

Network interface assigned to this context.

**Definition** net\_context.h:361

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
- [net\_offload.h](net__offload_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
