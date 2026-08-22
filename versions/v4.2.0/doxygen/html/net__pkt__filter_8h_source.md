---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net__pkt__filter_8h_source.html
original_path: doxygen/html/net__pkt__filter_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_pkt\_filter.h

[Go to the documentation of this file.](net__pkt__filter_8h.md)

1

7

8/\*

9 \* Copyright (c) 2021 BayLibre SAS

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_PKT\_FILTER\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_PKT\_FILTER\_H\_

16

17#include <[limits.h](limits_8h.md)>

18#include <[stdbool.h](stdbool_8h.md)>

19#include <[zephyr/sys/slist.h](slist_8h.md)>

20#include <[zephyr/net/net\_core.h](net__core_8h.md)>

21#include <[zephyr/net/ethernet.h](ethernet_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

35

37

38struct [npf\_test](structnpf__test.md);

39

40typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (npf\_test\_fn\_t)(struct [npf\_test](structnpf__test.md) \*test, struct [net\_pkt](structnet__pkt.md) \*pkt);

41

42enum npf\_test\_type {

43 NPF\_TEST\_TYPE\_UNKNOWN = 0,

44 NPF\_TEST\_TYPE\_IFACE\_MATCH,

45 NPF\_TEST\_TYPE\_IFACE\_UNMATCH,

46 NPF\_TEST\_TYPE\_ORIG\_IFACE\_MATCH,

47 NPF\_TEST\_TYPE\_ORIG\_IFACE\_UNMATCH,

48 NPF\_TEST\_TYPE\_SIZE\_MIN,

49 NPF\_TEST\_TYPE\_SIZE\_MAX,

50 NPF\_TEST\_TYPE\_SIZE\_BOUNDS,

51 NPF\_TEST\_TYPE\_IP\_SRC\_ADDR\_ALLOWLIST,

52 NPF\_TEST\_TYPE\_IP\_SRC\_ADDR\_BLOCKLIST,

53 NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_MATCH,

54 NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_UNMATCH,

55 NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_MATCH,

56 NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_UNMATCH,

57 NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_MASK\_MATCH,

58 NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_MASK\_MATCH,

59 NPF\_TEST\_TYPE\_ETH\_TYPE\_MATCH,

60 NPF\_TEST\_TYPE\_ETH\_TYPE\_UNMATCH,

61 NPF\_TEST\_TYPE\_ETH\_VLAN\_TYPE\_MATCH,

62 NPF\_TEST\_TYPE\_ETH\_VLAN\_TYPE\_UNMATCH,

63};

64

65#if defined(CONFIG\_NET\_PKT\_FILTER\_LOG\_LEVEL\_DBG) || \

66 defined(CONFIG\_NET\_SHELL\_PKT\_FILTER\_SUPPORTED)

67#define NPF\_TEST\_ENABLE\_NAME 1

68#elif defined(NPF\_TEST\_ENABLE\_NAME)

69#undef NPF\_TEST\_ENABLE\_NAME

70#endif

71

73

[ 75](structnpf__test.md)struct [npf\_test](structnpf__test.md) {

[ 76](structnpf__test.md#ac49921514690a71986ca4d07245cfe7d) npf\_test\_fn\_t \*[fn](structnpf__test.md#ac49921514690a71986ca4d07245cfe7d);

77

79 [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(NPF\_TEST\_ENABLE\_NAME,

80 (const char \*name;))

81 [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(NPF\_TEST\_ENABLE\_NAME,

82 (enum npf\_test\_type type;))

84};

85

[ 87](structnpf__rule.md)struct [npf\_rule](structnpf__rule.md) {

[ 88](structnpf__rule.md#ad5ae58fbcee5112e2defde1d7f4320dc) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnpf__rule.md#ad5ae58fbcee5112e2defde1d7f4320dc);

[ 89](structnpf__rule.md#a872daf53310dd8e20477eafd6808481f) enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [result](structnpf__rule.md#a872daf53310dd8e20477eafd6808481f);

[ 90](structnpf__rule.md#a06045c693cf06e6ebfc5a74b8c3f5ef7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_tests](structnpf__rule.md#a06045c693cf06e6ebfc5a74b8c3f5ef7);

[ 91](structnpf__rule.md#a72c032c55535c82f365b2cd1229cb1e0) struct [npf\_test](structnpf__test.md) \*[tests](structnpf__rule.md#a72c032c55535c82f365b2cd1229cb1e0)[];

92};

93

95extern struct [npf\_rule](structnpf__rule.md) [npf\_default\_ok](group__net__pkt__filter.md#gaac489d75c023952243589cba7ff7367a);

97extern struct [npf\_rule](structnpf__rule.md) [npf\_default\_drop](group__net__pkt__filter.md#ga8fc592feedeceb5172f8747a29697dd7);

98

[ 100](structnpf__rule__list.md)struct [npf\_rule\_list](structnpf__rule__list.md) {

[ 101](structnpf__rule__list.md#ab6aadf2d3479853c28e94972e7862931) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [rule\_head](structnpf__rule__list.md#ab6aadf2d3479853c28e94972e7862931);

[ 102](structnpf__rule__list.md#af4d539d930acb257b1496761219d26cd) struct [k\_spinlock](structk__spinlock.md) [lock](structnpf__rule__list.md#af4d539d930acb257b1496761219d26cd);

103};

104

106extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_send\_rules](group__net__pkt__filter.md#ga8017a041d3168c76e39bdfac011b9315);

108extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_recv\_rules](group__net__pkt__filter.md#ga9714529658625e906264a46ad1a9be6f);

110extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_local\_in\_recv\_rules](group__net__pkt__filter.md#ga571e9fb34eb4e3cbf38f885b5e786021);

112extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_ipv4\_recv\_rules](group__net__pkt__filter.md#gad521d7ac3270970833aec48d8a517d85);

114extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_ipv6\_recv\_rules](group__net__pkt__filter.md#gab91ca81aab2da48066538d72caf0c8ae);

115

[ 122](group__net__pkt__filter.md#ga3b2a85558b6756e76760d9a40c780e28)void [npf\_insert\_rule](group__net__pkt__filter.md#ga3b2a85558b6756e76760d9a40c780e28)(struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule);

123

[ 130](group__net__pkt__filter.md#gadfa956e4af3c45460846fc22f863e697)void [npf\_append\_rule](group__net__pkt__filter.md#gadfa956e4af3c45460846fc22f863e697)(struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule);

131

[ 139](group__net__pkt__filter.md#ga4d7426db901debff35e1de5805e06c71)bool [npf\_remove\_rule](group__net__pkt__filter.md#ga4d7426db901debff35e1de5805e06c71)(struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule);

140

[ 147](group__net__pkt__filter.md#ga54916eb4943e4b47cd31eb23827d0dd5)bool [npf\_remove\_all\_rules](group__net__pkt__filter.md#ga54916eb4943e4b47cd31eb23827d0dd5)(struct [npf\_rule\_list](structnpf__rule__list.md) \*rules);

148

150

151/\* convenience shortcuts \*/

152#define npf\_insert\_send\_rule(rule) npf\_insert\_rule(&npf\_send\_rules, rule)

153#define npf\_insert\_recv\_rule(rule) npf\_insert\_rule(&npf\_recv\_rules, rule)

154#define npf\_append\_send\_rule(rule) npf\_append\_rule(&npf\_send\_rules, rule)

155#define npf\_append\_recv\_rule(rule) npf\_append\_rule(&npf\_recv\_rules, rule)

156#define npf\_remove\_send\_rule(rule) npf\_remove\_rule(&npf\_send\_rules, rule)

157#define npf\_remove\_recv\_rule(rule) npf\_remove\_rule(&npf\_recv\_rules, rule)

158#define npf\_remove\_all\_send\_rules() npf\_remove\_all\_rules(&npf\_send\_rules)

159#define npf\_remove\_all\_recv\_rules() npf\_remove\_all\_rules(&npf\_recv\_rules)

160

161#ifdef CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK

162#define npf\_insert\_local\_in\_recv\_rule(rule) npf\_insert\_rule(&npf\_local\_in\_recv\_rules, rule)

163#define npf\_append\_local\_in\_recv\_rule(rule) npf\_append\_rule(&npf\_local\_in\_recv\_rules, rule)

164#define npf\_remove\_local\_in\_recv\_rule(rule) npf\_remove\_rule(&npf\_local\_in\_recv\_rules, rule)

165#define npf\_remove\_all\_local\_in\_recv\_rules() npf\_remove\_all\_rules(&npf\_local\_in\_recv\_rules)

166#endif /\* CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK \*/

167

168#ifdef CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK

169#define npf\_insert\_ipv4\_recv\_rule(rule) npf\_insert\_rule(&npf\_ipv4\_recv\_rules, rule)

170#define npf\_append\_ipv4\_recv\_rule(rule) npf\_append\_rule(&npf\_ipv4\_recv\_rules, rule)

171#define npf\_remove\_ipv4\_recv\_rule(rule) npf\_remove\_rule(&npf\_ipv4\_recv\_rules, rule)

172#define npf\_remove\_all\_ipv4\_recv\_rules() npf\_remove\_all\_rules(&npf\_ipv4\_recv\_rules)

173#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK \*/

174

175#ifdef CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK

176#define npf\_insert\_ipv6\_recv\_rule(rule) npf\_insert\_rule(&npf\_ipv6\_recv\_rules, rule)

177#define npf\_append\_ipv6\_recv\_rule(rule) npf\_append\_rule(&npf\_ipv6\_recv\_rules, rule)

178#define npf\_remove\_ipv6\_recv\_rule(rule) npf\_remove\_rule(&npf\_ipv6\_recv\_rules, rule)

179#define npf\_remove\_all\_ipv6\_recv\_rules() npf\_remove\_all\_rules(&npf\_ipv6\_recv\_rules)

180#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK \*/

181

183

[ 238](group__net__pkt__filter.md#ga2f45093d5ad164d5c51a8996f7f04d32)#define NPF\_RULE(\_name, \_result, ...) \

239 struct npf\_rule \_name = { \

240 .result = (\_result), \

241 .nb\_tests = NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_) + 1, \

242 .tests = { FOR\_EACH(Z\_NPF\_TEST\_ADDR, (,), \_\_VA\_ARGS\_\_) }, \

243 }

244

245#define Z\_NPF\_TEST\_ADDR(arg) &arg.test

246

248

256

258

259struct npf\_test\_iface {

260 struct [npf\_test](structnpf__test.md) test;

261 struct [net\_if](structnet__if.md) \*iface;

262};

263

264extern npf\_test\_fn\_t npf\_iface\_match;

265extern npf\_test\_fn\_t npf\_iface\_unmatch;

266extern npf\_test\_fn\_t npf\_orig\_iface\_match;

267extern npf\_test\_fn\_t npf\_orig\_iface\_unmatch;

268

270

[ 277](group__npf__basic__cond.md#ga465578272b616c6267ecd13fd86ca73b)#define NPF\_IFACE\_MATCH(\_name, \_iface) \

278 struct npf\_test\_iface \_name = { \

279 .iface = (\_iface), \

280 .test.fn = npf\_iface\_match, \

281 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

282 (.test.name = "iface", \

283 .test.type = NPF\_TEST\_TYPE\_IFACE\_MATCH,)) \

284 }

285

[ 292](group__npf__basic__cond.md#gac3607a6736d70b0ea044a2ec7ab6d313)#define NPF\_IFACE\_UNMATCH(\_name, \_iface) \

293 struct npf\_test\_iface \_name = { \

294 .iface = (\_iface), \

295 .test.fn = npf\_iface\_unmatch, \

296 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

297 (.test.name = "!iface", \

298 .test.type = NPF\_TEST\_TYPE\_IFACE\_UNMATCH,)) \

299 }

300

[ 307](group__npf__basic__cond.md#ga55021acd131e4684568aaf6434b08789)#define NPF\_ORIG\_IFACE\_MATCH(\_name, \_iface) \

308 struct npf\_test\_iface \_name = { \

309 .iface = (\_iface), \

310 .test.fn = npf\_orig\_iface\_match, \

311 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

312 (.test.name = "orig iface", \

313 .test.type = NPF\_TEST\_TYPE\_ORIG\_IFACE\_MATCH,)) \

314 }

315

[ 322](group__npf__basic__cond.md#gad959dc62d47ca3b4d2f24a6c862c7623)#define NPF\_ORIG\_IFACE\_UNMATCH(\_name, \_iface) \

323 struct npf\_test\_iface \_name = { \

324 .iface = (\_iface), \

325 .test.fn = npf\_orig\_iface\_unmatch, \

326 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

327 (.test.name = "!orig iface", \

328 .test.type = NPF\_TEST\_TYPE\_ORIG\_IFACE\_UNMATCH,)) \

329 }

330

332

333struct npf\_test\_size\_bounds {

334 struct [npf\_test](structnpf__test.md) test;

335 size\_t min;

336 size\_t max;

337};

338

339extern npf\_test\_fn\_t npf\_size\_inbounds;

340

342

[ 349](group__npf__basic__cond.md#gaf142455f9bea3dea8faa0a913072b63e)#define NPF\_SIZE\_MIN(\_name, \_size) \

350 struct npf\_test\_size\_bounds \_name = { \

351 .min = (\_size), \

352 .max = SIZE\_MAX, \

353 .test.fn = npf\_size\_inbounds, \

354 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

355 (.test.name = "size min", \

356 .test.type = NPF\_TEST\_TYPE\_SIZE\_MIN,)) \

357 }

358

[ 365](group__npf__basic__cond.md#gacd56b9bcf2b2ba4759402650a9bff67a)#define NPF\_SIZE\_MAX(\_name, \_size) \

366 struct npf\_test\_size\_bounds \_name = { \

367 .min = 0, \

368 .max = (\_size), \

369 .test.fn = npf\_size\_inbounds, \

370 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

371 (.test.name = "size max", \

372 .test.type = NPF\_TEST\_TYPE\_SIZE\_MAX,)) \

373 }

374

[ 382](group__npf__basic__cond.md#gab402bb13c7899d57532d3dcf8a36ed4b)#define NPF\_SIZE\_BOUNDS(\_name, \_min\_size, \_max\_size) \

383 struct npf\_test\_size\_bounds \_name = { \

384 .min = (\_min\_size), \

385 .max = (\_max\_size), \

386 .test.fn = npf\_size\_inbounds, \

387 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

388 (.test.name = "size bounds", \

389 .test.type = NPF\_TEST\_TYPE\_SIZE\_BOUNDS,)) \

390 }

391

393

394struct npf\_test\_ip {

395 struct [npf\_test](structnpf__test.md) test;

396 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr\_family;

397 void \*ipaddr;

398 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ipaddr\_num;

399};

400

401extern npf\_test\_fn\_t npf\_ip\_src\_addr\_match;

402extern npf\_test\_fn\_t npf\_ip\_src\_addr\_unmatch;

403

405

[ 418](group__npf__basic__cond.md#ga4dd013f0fb92eb0433f174cf40e89e00)#define NPF\_IP\_SRC\_ADDR\_ALLOWLIST(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) \

419 struct npf\_test\_ip \_name = { \

420 .addr\_family = \_af, \

421 .ipaddr = (\_ip\_addr\_array), \

422 .ipaddr\_num = \_ip\_addr\_num, \

423 .test.fn = npf\_ip\_src\_addr\_match, \

424 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

425 (.test.name = "ip src allow", \

426 .test.type = NPF\_TEST\_TYPE\_IP\_SRC\_ADDR\_ALLOWLIST,)) \

427 }

428

[ 441](group__npf__basic__cond.md#ga57fe28a992b1afaf33581292fe5015bd)#define NPF\_IP\_SRC\_ADDR\_BLOCKLIST(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) \

442 struct npf\_test\_ip \_name = { \

443 .addr\_family = \_af, \

444 .ipaddr = (\_ip\_addr\_array), \

445 .ipaddr\_num = \_ip\_addr\_num, \

446 .test.fn = npf\_ip\_src\_addr\_unmatch, \

447 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

448 (.test.name = "ip src block", \

449 .test.type = NPF\_TEST\_TYPE\_IP\_SRC\_ADDR\_BLOCKLIST,)) \

450 }

451

453

461

463

464struct npf\_test\_eth\_addr {

465 struct [npf\_test](structnpf__test.md) test;

466 unsigned int nb\_addresses;

467 struct [net\_eth\_addr](structnet__eth__addr.md) \*addresses;

468 struct [net\_eth\_addr](structnet__eth__addr.md) mask;

469};

470

471extern npf\_test\_fn\_t npf\_eth\_src\_addr\_match;

472extern npf\_test\_fn\_t npf\_eth\_src\_addr\_unmatch;

473extern npf\_test\_fn\_t npf\_eth\_dst\_addr\_match;

474extern npf\_test\_fn\_t npf\_eth\_dst\_addr\_unmatch;

475

477

[ 487](group__npf__eth__cond.md#gad2141ad8d6639c9b92569d55130ca1b1)#define NPF\_ETH\_SRC\_ADDR\_MATCH(\_name, \_addr\_array) \

488 struct npf\_test\_eth\_addr \_name = { \

489 .addresses = (\_addr\_array), \

490 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

491 .test.fn = npf\_eth\_src\_addr\_match, \

492 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

493 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

494 (.test.name = "eth src", \

495 .test.type = NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_MATCH,)) \

496 }

497

[ 507](group__npf__eth__cond.md#ga228eaa3784f663d8f2e2711e26409043)#define NPF\_ETH\_SRC\_ADDR\_UNMATCH(\_name, \_addr\_array) \

508 struct npf\_test\_eth\_addr \_name = { \

509 .addresses = (\_addr\_array), \

510 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

511 .test.fn = npf\_eth\_src\_addr\_unmatch, \

512 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

513 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

514 (.test.name = "!eth src", \

515 .test.type = NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_UNMATCH,)) \

516 }

517

[ 527](group__npf__eth__cond.md#ga3d22d687bcd56b7727c51c7bc7f36cac)#define NPF\_ETH\_DST\_ADDR\_MATCH(\_name, \_addr\_array) \

528 struct npf\_test\_eth\_addr \_name = { \

529 .addresses = (\_addr\_array), \

530 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

531 .test.fn = npf\_eth\_dst\_addr\_match, \

532 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

533 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

534 (.test.name = "eth dst", \

535 .test.type = NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_MATCH,)) \

536 }

537

[ 547](group__npf__eth__cond.md#ga3b8a8a22eb992c0e02223f70723c3641)#define NPF\_ETH\_DST\_ADDR\_UNMATCH(\_name, \_addr\_array) \

548 struct npf\_test\_eth\_addr \_name = { \

549 .addresses = (\_addr\_array), \

550 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

551 .test.fn = npf\_eth\_dst\_addr\_unmatch, \

552 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

553 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

554 (.test.name = "!eth dst", \

555 .test.type = NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_UNMATCH,)) \

556 }

557

[ 568](group__npf__eth__cond.md#ga0e06ebc4c9a1a960651be1ba89eeb2fd)#define NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH(\_name, \_addr\_array, ...) \

569 struct npf\_test\_eth\_addr \_name = { \

570 .addresses = (\_addr\_array), \

571 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

572 .mask.addr = { \_\_VA\_ARGS\_\_ }, \

573 .test.fn = npf\_eth\_src\_addr\_match, \

574 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

575 (.test.name = "eth src mask", \

576 .test.type = NPF\_TEST\_TYPE\_ETH\_SRC\_ADDR\_MASK\_MATCH,)) \

577 }

578

[ 589](group__npf__eth__cond.md#ga7cf793af7b91eccc6e675ff19ed59a14)#define NPF\_ETH\_DST\_ADDR\_MASK\_MATCH(\_name, \_addr\_array, ...) \

590 struct npf\_test\_eth\_addr \_name = { \

591 .addresses = (\_addr\_array), \

592 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

593 .mask.addr = { \_\_VA\_ARGS\_\_ }, \

594 .test.fn = npf\_eth\_dst\_addr\_match, \

595 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

596 (.test.name = "eth dst mask", \

597 .test.type = NPF\_TEST\_TYPE\_ETH\_DST\_ADDR\_MASK\_MATCH,)) \

598 }

599

601

602struct npf\_test\_eth\_type {

603 struct [npf\_test](structnpf__test.md) test;

604 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type; /\* type in network order \*/

605};

606

607extern npf\_test\_fn\_t npf\_eth\_type\_match;

608extern npf\_test\_fn\_t npf\_eth\_type\_unmatch;

609extern npf\_test\_fn\_t npf\_eth\_vlan\_type\_match;

610extern npf\_test\_fn\_t npf\_eth\_vlan\_type\_unmatch;

611

613

[ 620](group__npf__eth__cond.md#gace7de72d4c64e128a825f28f94d8b1b2)#define NPF\_ETH\_TYPE\_MATCH(\_name, \_type) \

621 struct npf\_test\_eth\_type \_name = { \

622 .type = htons(\_type), \

623 .test.fn = npf\_eth\_type\_match, \

624 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

625 (.test.name = "eth type", \

626 .test.type = NPF\_TEST\_TYPE\_ETH\_TYPE\_MATCH,)) \

627 }

628

[ 635](group__npf__eth__cond.md#gab9bf6d58433e273220c5fab76f608545)#define NPF\_ETH\_TYPE\_UNMATCH(\_name, \_type) \

636 struct npf\_test\_eth\_type \_name = { \

637 .type = htons(\_type), \

638 .test.fn = npf\_eth\_type\_unmatch, \

639 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

640 (.test.name = "!eth type", \

641 .test.type = NPF\_TEST\_TYPE\_ETH\_TYPE\_UNMATCH,)) \

642 }

643

[ 651](group__npf__eth__cond.md#ga2d67631c0fdd659a8e9db62c6f0a87bf)#define NPF\_ETH\_VLAN\_TYPE\_MATCH(\_name, \_type) \

652 struct npf\_test\_eth\_type \_name = { \

653 .type = htons(\_type), \

654 .test.fn = npf\_eth\_vlan\_type\_match, \

655 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

656 (.test.name = "eth vlan type", \

657 .test.type = NPF\_TEST\_TYPE\_ETH\_VLAN\_TYPE\_MATCH,)) \

658 }

659

[ 667](group__npf__eth__cond.md#ga49af5d0231e15932607da955ca7e4b34)#define NPF\_ETH\_VLAN\_TYPE\_UNMATCH(\_name, \_type) \

668 struct npf\_test\_eth\_type \_name = { \

669 .type = htons(\_type), \

670 .test.fn = npf\_eth\_vlan\_type\_unmatch, \

671 IF\_ENABLED(NPF\_TEST\_ENABLE\_NAME, \

672 (.test.name = "!eth vlan type", \

673 .test.type = NPF\_TEST\_TYPE\_ETH\_VLAN\_TYPE\_UNMATCH,)) \

674 }

675

[ 677](group__npf__eth__cond.md#gaad4624a8e6c9491572e2a89739304530)enum [npf\_rule\_type](group__npf__eth__cond.md#gaad4624a8e6c9491572e2a89739304530) {

[ 678](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca) [NPF\_RULE\_TYPE\_UNKNOWN](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca) = 0,

[ 679](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81) [NPF\_RULE\_TYPE\_SEND](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81),

[ 680](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f) [NPF\_RULE\_TYPE\_RECV](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f),

[ 681](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b) [NPF\_RULE\_TYPE\_LOCAL\_IN\_RECV](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b),

[ 682](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc) [NPF\_RULE\_TYPE\_IPV4\_RECV](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc),

[ 683](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2) [NPF\_RULE\_TYPE\_IPV6\_RECV](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2),

684};

685

[ 694](group__npf__eth__cond.md#ga7522a5a2188f7afbdc1a0528782ce0ef)typedef void (\*[npf\_rule\_cb\_t](group__npf__eth__cond.md#ga7522a5a2188f7afbdc1a0528782ce0ef))(struct [npf\_rule](structnpf__rule.md) \*rule,

695 enum [npf\_rule\_type](group__npf__eth__cond.md#gaad4624a8e6c9491572e2a89739304530) type,

696 void \*user\_data);

697

[ 705](group__npf__eth__cond.md#ga188b9d73f47a77ce05d728250606e7ec)void [npf\_rules\_foreach](group__npf__eth__cond.md#ga188b9d73f47a77ce05d728250606e7ec)([npf\_rule\_cb\_t](group__npf__eth__cond.md#ga7522a5a2188f7afbdc1a0528782ce0ef) cb, void \*user\_data);

706

708const char \*npf\_test\_get\_str(struct [npf\_test](structnpf__test.md) \*test, char \*buf,

709 size\_t len);

711

713

714#ifdef \_\_cplusplus

715}

716#endif

717

718#endif /\* ZEPHYR\_INCLUDE\_NET\_PKT\_FILTER\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:103

[npf\_insert\_rule](group__net__pkt__filter.md#ga3b2a85558b6756e76760d9a40c780e28)

void npf\_insert\_rule(struct npf\_rule\_list \*rules, struct npf\_rule \*rule)

Insert a rule at the front of given rule list.

[npf\_remove\_rule](group__net__pkt__filter.md#ga4d7426db901debff35e1de5805e06c71)

bool npf\_remove\_rule(struct npf\_rule\_list \*rules, struct npf\_rule \*rule)

Remove a rule from the given rule list.

[npf\_remove\_all\_rules](group__net__pkt__filter.md#ga54916eb4943e4b47cd31eb23827d0dd5)

bool npf\_remove\_all\_rules(struct npf\_rule\_list \*rules)

Remove all rules from the given rule list.

[npf\_local\_in\_recv\_rules](group__net__pkt__filter.md#ga571e9fb34eb4e3cbf38f885b5e786021)

struct npf\_rule\_list npf\_local\_in\_recv\_rules

rule list applied for local incoming packets

[npf\_send\_rules](group__net__pkt__filter.md#ga8017a041d3168c76e39bdfac011b9315)

struct npf\_rule\_list npf\_send\_rules

rule list applied to outgoing packets

[npf\_default\_drop](group__net__pkt__filter.md#ga8fc592feedeceb5172f8747a29697dd7)

struct npf\_rule npf\_default\_drop

Default rule list termination for rejecting a packet.

[npf\_recv\_rules](group__net__pkt__filter.md#ga9714529658625e906264a46ad1a9be6f)

struct npf\_rule\_list npf\_recv\_rules

rule list applied to incoming packets

[npf\_default\_ok](group__net__pkt__filter.md#gaac489d75c023952243589cba7ff7367a)

struct npf\_rule npf\_default\_ok

Default rule list termination for accepting a packet.

[npf\_ipv6\_recv\_rules](group__net__pkt__filter.md#gab91ca81aab2da48066538d72caf0c8ae)

struct npf\_rule\_list npf\_ipv6\_recv\_rules

rule list applied for IPv6 incoming packets

[npf\_ipv4\_recv\_rules](group__net__pkt__filter.md#gad521d7ac3270970833aec48d8a517d85)

struct npf\_rule\_list npf\_ipv4\_recv\_rules

rule list applied for IPv4 incoming packets

[npf\_append\_rule](group__net__pkt__filter.md#gadfa956e4af3c45460846fc22f863e697)

void npf\_append\_rule(struct npf\_rule\_list \*rules, struct npf\_rule \*rule)

Append a rule at the end of given rule list.

[npf\_rules\_foreach](group__npf__eth__cond.md#ga188b9d73f47a77ce05d728250606e7ec)

void npf\_rules\_foreach(npf\_rule\_cb\_t cb, void \*user\_data)

Go through all the network packet filter rules and call callback for each of them.

[npf\_rule\_cb\_t](group__npf__eth__cond.md#ga7522a5a2188f7afbdc1a0528782ce0ef)

void(\* npf\_rule\_cb\_t)(struct npf\_rule \*rule, enum npf\_rule\_type type, void \*user\_data)

Callback used while iterating over network packet filter rules.

**Definition** net\_pkt\_filter.h:694

[npf\_rule\_type](group__npf__eth__cond.md#gaad4624a8e6c9491572e2a89739304530)

npf\_rule\_type

Type of the packet filter rule.

**Definition** net\_pkt\_filter.h:677

[NPF\_RULE\_TYPE\_UNKNOWN](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a0c66a2772501fbaf5e8521c19e1378ca)

@ NPF\_RULE\_TYPE\_UNKNOWN

Unknown rule type.

**Definition** net\_pkt\_filter.h:678

[NPF\_RULE\_TYPE\_RECV](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a0ecff39e652e912433e3dd36739eb41f)

@ NPF\_RULE\_TYPE\_RECV

Rule for incoming packets.

**Definition** net\_pkt\_filter.h:680

[NPF\_RULE\_TYPE\_LOCAL\_IN\_RECV](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a15eb4c6dbd1c855a24154243ca91b49b)

@ NPF\_RULE\_TYPE\_LOCAL\_IN\_RECV

Rule for local incoming packets.

**Definition** net\_pkt\_filter.h:681

[NPF\_RULE\_TYPE\_SEND](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a2817a29d560b9ff6cfbc6bd69a99fd81)

@ NPF\_RULE\_TYPE\_SEND

Rule for outgoing packets.

**Definition** net\_pkt\_filter.h:679

[NPF\_RULE\_TYPE\_IPV4\_RECV](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530a9ca4ae82040d060855db63ff193854fc)

@ NPF\_RULE\_TYPE\_IPV4\_RECV

Rule for IPv4 incoming packets.

**Definition** net\_pkt\_filter.h:682

[NPF\_RULE\_TYPE\_IPV6\_RECV](group__npf__eth__cond.md#ggaad4624a8e6c9491572e2a89739304530acb0785310ca00b7fc0030c5ee0115db2)

@ NPF\_RULE\_TYPE\_IPV6\_RECV

Rule for IPv6 incoming packets.

**Definition** net\_pkt\_filter.h:683

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:247

[limits.h](limits_8h.md)

[net\_core.h](net__core_8h.md)

Network core definitions.

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[net\_eth\_addr](structnet__eth__addr.md)

Ethernet address.

**Definition** ethernet.h:55

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[npf\_rule\_list](structnpf__rule__list.md)

rule set for a given test location

**Definition** net\_pkt\_filter.h:100

[npf\_rule\_list::rule\_head](structnpf__rule__list.md#ab6aadf2d3479853c28e94972e7862931)

sys\_slist\_t rule\_head

List head.

**Definition** net\_pkt\_filter.h:101

[npf\_rule\_list::lock](structnpf__rule__list.md#af4d539d930acb257b1496761219d26cd)

struct k\_spinlock lock

Lock protecting the list access.

**Definition** net\_pkt\_filter.h:102

[npf\_rule](structnpf__rule.md)

filter rule structure

**Definition** net\_pkt\_filter.h:87

[npf\_rule::nb\_tests](structnpf__rule.md#a06045c693cf06e6ebfc5a74b8c3f5ef7)

uint32\_t nb\_tests

number of tests for this rule

**Definition** net\_pkt\_filter.h:90

[npf\_rule::tests](structnpf__rule.md#a72c032c55535c82f365b2cd1229cb1e0)

struct npf\_test \* tests[]

pointers to npf\_test instances

**Definition** net\_pkt\_filter.h:91

[npf\_rule::result](structnpf__rule.md#a872daf53310dd8e20477eafd6808481f)

enum net\_verdict result

result if all tests pass

**Definition** net\_pkt\_filter.h:89

[npf\_rule::node](structnpf__rule.md#ad5ae58fbcee5112e2defde1d7f4320dc)

sys\_snode\_t node

Slist rule list node.

**Definition** net\_pkt\_filter.h:88

[npf\_test](structnpf__test.md)

common filter test structure to be embedded into larger structures

**Definition** net\_pkt\_filter.h:75

[npf\_test::fn](structnpf__test.md#ac49921514690a71986ca4d07245cfe7d)

npf\_test\_fn\_t \* fn

packet condition test function

**Definition** net\_pkt\_filter.h:76

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_pkt\_filter.h](net__pkt__filter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
