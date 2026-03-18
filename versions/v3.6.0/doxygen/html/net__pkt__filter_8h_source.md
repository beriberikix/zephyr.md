---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__pkt__filter_8h_source.html
original_path: doxygen/html/net__pkt__filter_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

33

35

36struct [npf\_test](structnpf__test.md);

37

38typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (npf\_test\_fn\_t)(struct [npf\_test](structnpf__test.md) \*test, struct [net\_pkt](structnet__pkt.md) \*pkt);

39

41

[ 43](structnpf__test.md)struct [npf\_test](structnpf__test.md) {

[ 44](structnpf__test.md#ac49921514690a71986ca4d07245cfe7d) npf\_test\_fn\_t \*[fn](structnpf__test.md#ac49921514690a71986ca4d07245cfe7d);

45};

46

[ 48](structnpf__rule.md)struct [npf\_rule](structnpf__rule.md) {

[ 49](structnpf__rule.md#ad5ae58fbcee5112e2defde1d7f4320dc) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnpf__rule.md#ad5ae58fbcee5112e2defde1d7f4320dc);

[ 50](structnpf__rule.md#a872daf53310dd8e20477eafd6808481f) enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) [result](structnpf__rule.md#a872daf53310dd8e20477eafd6808481f);

[ 51](structnpf__rule.md#a06045c693cf06e6ebfc5a74b8c3f5ef7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nb\_tests](structnpf__rule.md#a06045c693cf06e6ebfc5a74b8c3f5ef7);

[ 52](structnpf__rule.md#a72c032c55535c82f365b2cd1229cb1e0) struct [npf\_test](structnpf__test.md) \*[tests](structnpf__rule.md#a72c032c55535c82f365b2cd1229cb1e0)[];

53};

54

56extern struct [npf\_rule](structnpf__rule.md) [npf\_default\_ok](group__net__pkt__filter.md#gaac489d75c023952243589cba7ff7367a);

58extern struct [npf\_rule](structnpf__rule.md) [npf\_default\_drop](group__net__pkt__filter.md#ga8fc592feedeceb5172f8747a29697dd7);

59

[ 61](structnpf__rule__list.md)struct [npf\_rule\_list](structnpf__rule__list.md) {

[ 62](structnpf__rule__list.md#ab6aadf2d3479853c28e94972e7862931) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [rule\_head](structnpf__rule__list.md#ab6aadf2d3479853c28e94972e7862931);

[ 63](structnpf__rule__list.md#af4d539d930acb257b1496761219d26cd) struct [k\_spinlock](structk__spinlock.md) [lock](structnpf__rule__list.md#af4d539d930acb257b1496761219d26cd);

64};

65

67extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_send\_rules](group__net__pkt__filter.md#ga8017a041d3168c76e39bdfac011b9315);

69extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_recv\_rules](group__net__pkt__filter.md#ga9714529658625e906264a46ad1a9be6f);

71extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_local\_in\_recv\_rules](group__net__pkt__filter.md#ga571e9fb34eb4e3cbf38f885b5e786021);

73extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_ipv4\_recv\_rules](group__net__pkt__filter.md#gad521d7ac3270970833aec48d8a517d85);

75extern struct [npf\_rule\_list](structnpf__rule__list.md) [npf\_ipv6\_recv\_rules](group__net__pkt__filter.md#gab91ca81aab2da48066538d72caf0c8ae);

76

[ 83](group__net__pkt__filter.md#ga3b2a85558b6756e76760d9a40c780e28)void [npf\_insert\_rule](group__net__pkt__filter.md#ga3b2a85558b6756e76760d9a40c780e28)(struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule);

84

[ 91](group__net__pkt__filter.md#gadfa956e4af3c45460846fc22f863e697)void [npf\_append\_rule](group__net__pkt__filter.md#gadfa956e4af3c45460846fc22f863e697)(struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule);

92

[ 100](group__net__pkt__filter.md#ga4d7426db901debff35e1de5805e06c71)bool [npf\_remove\_rule](group__net__pkt__filter.md#ga4d7426db901debff35e1de5805e06c71)(struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule);

101

[ 108](group__net__pkt__filter.md#ga54916eb4943e4b47cd31eb23827d0dd5)bool [npf\_remove\_all\_rules](group__net__pkt__filter.md#ga54916eb4943e4b47cd31eb23827d0dd5)(struct [npf\_rule\_list](structnpf__rule__list.md) \*rules);

109

110/\* convenience shortcuts \*/

[ 111](group__net__pkt__filter.md#ga4d3592647f81cd44a84ded4fff8edcf5)#define npf\_insert\_send\_rule(rule) npf\_insert\_rule(&npf\_send\_rules, rule)

[ 112](group__net__pkt__filter.md#ga3f6ecadc4842b61731984968ab4c6b89)#define npf\_insert\_recv\_rule(rule) npf\_insert\_rule(&npf\_recv\_rules, rule)

[ 113](group__net__pkt__filter.md#ga8cd06cba4360c1b56709e59ff06dbeb3)#define npf\_append\_send\_rule(rule) npf\_append\_rule(&npf\_send\_rules, rule)

[ 114](group__net__pkt__filter.md#ga263c7ee6e3c860353b5720c613690b0a)#define npf\_append\_recv\_rule(rule) npf\_append\_rule(&npf\_recv\_rules, rule)

[ 115](group__net__pkt__filter.md#ga43f03a0ce73d6dee52f43fd3577aa240)#define npf\_remove\_send\_rule(rule) npf\_remove\_rule(&npf\_send\_rules, rule)

[ 116](group__net__pkt__filter.md#gae78cb092522564303a665d1a5d3596b9)#define npf\_remove\_recv\_rule(rule) npf\_remove\_rule(&npf\_recv\_rules, rule)

[ 117](group__net__pkt__filter.md#gaea48284508ee244bce6d78b29bc2f471)#define npf\_remove\_all\_send\_rules() npf\_remove\_all\_rules(&npf\_send\_rules)

[ 118](group__net__pkt__filter.md#gac08801a6e8bd14bfd6eeaf2f28a1ed1a)#define npf\_remove\_all\_recv\_rules() npf\_remove\_all\_rules(&npf\_recv\_rules)

119

120#ifdef CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK

121#define npf\_insert\_local\_in\_recv\_rule(rule) npf\_insert\_rule(&npf\_local\_in\_recv\_rules, rule)

122#define npf\_append\_local\_in\_recv\_rule(rule) npf\_append\_rule(&npf\_local\_in\_recv\_rules, rule)

123#define npf\_remove\_local\_in\_recv\_rule(rule) npf\_remove\_rule(&npf\_local\_in\_recv\_rules, rule)

124#define npf\_remove\_all\_local\_in\_recv\_rules() npf\_remove\_all\_rules(&npf\_local\_in\_recv\_rules)

125#endif /\* CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK \*/

126

127#ifdef CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK

128#define npf\_insert\_ipv4\_recv\_rule(rule) npf\_insert\_rule(&npf\_ipv4\_recv\_rules, rule)

129#define npf\_append\_ipv4\_recv\_rule(rule) npf\_append\_rule(&npf\_ipv4\_recv\_rules, rule)

130#define npf\_remove\_ipv4\_recv\_rule(rule) npf\_remove\_rule(&npf\_ipv4\_recv\_rules, rule)

131#define npf\_remove\_all\_ipv4\_recv\_rules() npf\_remove\_all\_rules(&npf\_ipv4\_recv\_rules)

132#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK \*/

133

134#ifdef CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK

135#define npf\_insert\_ipv6\_recv\_rule(rule) npf\_insert\_rule(&npf\_ipv6\_recv\_rules, rule)

136#define npf\_append\_ipv6\_recv\_rule(rule) npf\_append\_rule(&npf\_ipv6\_recv\_rules, rule)

137#define npf\_remove\_ipv6\_recv\_rule(rule) npf\_remove\_rule(&npf\_ipv6\_recv\_rules, rule)

138#define npf\_remove\_all\_ipv6\_recv\_rules() npf\_remove\_all\_rules(&npf\_ipv6\_recv\_rules)

139#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK \*/

140

[ 195](group__net__pkt__filter.md#ga2f45093d5ad164d5c51a8996f7f04d32)#define NPF\_RULE(\_name, \_result, ...) \

196 struct npf\_rule \_name = { \

197 .result = (\_result), \

198 .nb\_tests = NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_) + 1, \

199 .tests = { FOR\_EACH(Z\_NPF\_TEST\_ADDR, (,), \_\_VA\_ARGS\_\_) }, \

200 }

201

202#define Z\_NPF\_TEST\_ADDR(arg) &arg.test

203

205

211

213

214struct npf\_test\_iface {

215 struct [npf\_test](structnpf__test.md) test;

216 struct [net\_if](structnet__if.md) \*iface;

217};

218

219extern npf\_test\_fn\_t npf\_iface\_match;

220extern npf\_test\_fn\_t npf\_iface\_unmatch;

221extern npf\_test\_fn\_t npf\_orig\_iface\_match;

222extern npf\_test\_fn\_t npf\_orig\_iface\_unmatch;

223

225

[ 232](group__npf__basic__cond.md#ga465578272b616c6267ecd13fd86ca73b)#define NPF\_IFACE\_MATCH(\_name, \_iface) \

233 struct npf\_test\_iface \_name = { \

234 .iface = (\_iface), \

235 .test.fn = npf\_iface\_match, \

236 }

237

[ 244](group__npf__basic__cond.md#gac3607a6736d70b0ea044a2ec7ab6d313)#define NPF\_IFACE\_UNMATCH(\_name, \_iface) \

245 struct npf\_test\_iface \_name = { \

246 .iface = (\_iface), \

247 .test.fn = npf\_iface\_unmatch, \

248 }

249

[ 256](group__npf__basic__cond.md#ga55021acd131e4684568aaf6434b08789)#define NPF\_ORIG\_IFACE\_MATCH(\_name, \_iface) \

257 struct npf\_test\_iface \_name = { \

258 .iface = (\_iface), \

259 .test.fn = npf\_orig\_iface\_match, \

260 }

261

[ 268](group__npf__basic__cond.md#gad959dc62d47ca3b4d2f24a6c862c7623)#define NPF\_ORIG\_IFACE\_UNMATCH(\_name, \_iface) \

269 struct npf\_test\_iface \_name = { \

270 .iface = (\_iface), \

271 .test.fn = npf\_orig\_iface\_unmatch, \

272 }

273

275

276struct npf\_test\_size\_bounds {

277 struct [npf\_test](structnpf__test.md) test;

278 size\_t min;

279 size\_t max;

280};

281

282extern npf\_test\_fn\_t npf\_size\_inbounds;

283

285

[ 292](group__npf__basic__cond.md#gaf142455f9bea3dea8faa0a913072b63e)#define NPF\_SIZE\_MIN(\_name, \_size) \

293 struct npf\_test\_size\_bounds \_name = { \

294 .min = (\_size), \

295 .max = SIZE\_MAX, \

296 .test.fn = npf\_size\_inbounds, \

297 }

298

[ 305](group__npf__basic__cond.md#gacd56b9bcf2b2ba4759402650a9bff67a)#define NPF\_SIZE\_MAX(\_name, \_size) \

306 struct npf\_test\_size\_bounds \_name = { \

307 .min = 0, \

308 .max = (\_size), \

309 .test.fn = npf\_size\_inbounds, \

310 }

311

[ 319](group__npf__basic__cond.md#gab402bb13c7899d57532d3dcf8a36ed4b)#define NPF\_SIZE\_BOUNDS(\_name, \_min\_size, \_max\_size) \

320 struct npf\_test\_size\_bounds \_name = { \

321 .min = (\_min\_size), \

322 .max = (\_max\_size), \

323 .test.fn = npf\_size\_inbounds, \

324 }

325

327

328struct npf\_test\_ip {

329 struct [npf\_test](structnpf__test.md) test;

330 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr\_family;

331 void \*ipaddr;

332 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ipaddr\_num;

333};

334

335extern npf\_test\_fn\_t npf\_ip\_src\_addr\_match;

336extern npf\_test\_fn\_t npf\_ip\_src\_addr\_unmatch;

337

339

[ 352](group__npf__basic__cond.md#ga4dd013f0fb92eb0433f174cf40e89e00)#define NPF\_IP\_SRC\_ADDR\_ALLOWLIST(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) \

353 struct npf\_test\_ip \_name = { \

354 .addr\_family = \_af, \

355 .ipaddr = (\_ip\_addr\_array), \

356 .ipaddr\_num = \_ip\_addr\_num, \

357 .test.fn = npf\_ip\_src\_addr\_match, \

358 }

359

[ 372](group__npf__basic__cond.md#ga57fe28a992b1afaf33581292fe5015bd)#define NPF\_IP\_SRC\_ADDR\_BLOCKLIST(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) \

373 struct npf\_test\_ip \_name = { \

374 .addr\_family = \_af, \

375 .ipaddr = (\_ip\_addr\_array), \

376 .ipaddr\_num = \_ip\_addr\_num, \

377 .test.fn = npf\_ip\_src\_addr\_unmatch, \

378 }

379

381

387

389

390struct npf\_test\_eth\_addr {

391 struct [npf\_test](structnpf__test.md) test;

392 unsigned int nb\_addresses;

393 struct net\_eth\_addr \*addresses;

394 struct net\_eth\_addr mask;

395};

396

397extern npf\_test\_fn\_t npf\_eth\_src\_addr\_match;

398extern npf\_test\_fn\_t npf\_eth\_src\_addr\_unmatch;

399extern npf\_test\_fn\_t npf\_eth\_dst\_addr\_match;

400extern npf\_test\_fn\_t npf\_eth\_dst\_addr\_unmatch;

401

403

[ 413](group__npf__eth__cond.md#gad2141ad8d6639c9b92569d55130ca1b1)#define NPF\_ETH\_SRC\_ADDR\_MATCH(\_name, \_addr\_array) \

414 struct npf\_test\_eth\_addr \_name = { \

415 .addresses = (\_addr\_array), \

416 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

417 .test.fn = npf\_eth\_src\_addr\_match, \

418 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

419 }

420

[ 430](group__npf__eth__cond.md#ga228eaa3784f663d8f2e2711e26409043)#define NPF\_ETH\_SRC\_ADDR\_UNMATCH(\_name, \_addr\_array) \

431 struct npf\_test\_eth\_addr \_name = { \

432 .addresses = (\_addr\_array), \

433 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

434 .test.fn = npf\_eth\_src\_addr\_unmatch, \

435 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

436 }

437

[ 447](group__npf__eth__cond.md#ga3d22d687bcd56b7727c51c7bc7f36cac)#define NPF\_ETH\_DST\_ADDR\_MATCH(\_name, \_addr\_array) \

448 struct npf\_test\_eth\_addr \_name = { \

449 .addresses = (\_addr\_array), \

450 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

451 .test.fn = npf\_eth\_dst\_addr\_match, \

452 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

453 }

454

[ 464](group__npf__eth__cond.md#ga3b8a8a22eb992c0e02223f70723c3641)#define NPF\_ETH\_DST\_ADDR\_UNMATCH(\_name, \_addr\_array) \

465 struct npf\_test\_eth\_addr \_name = { \

466 .addresses = (\_addr\_array), \

467 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

468 .test.fn = npf\_eth\_dst\_addr\_unmatch, \

469 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

470 }

471

[ 482](group__npf__eth__cond.md#ga0e06ebc4c9a1a960651be1ba89eeb2fd)#define NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH(\_name, \_addr\_array, ...) \

483 struct npf\_test\_eth\_addr \_name = { \

484 .addresses = (\_addr\_array), \

485 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

486 .mask.addr = { \_\_VA\_ARGS\_\_ }, \

487 .test.fn = npf\_eth\_src\_addr\_match, \

488 }

489

[ 500](group__npf__eth__cond.md#ga7cf793af7b91eccc6e675ff19ed59a14)#define NPF\_ETH\_DST\_ADDR\_MASK\_MATCH(\_name, \_addr\_array, ...) \

501 struct npf\_test\_eth\_addr \_name = { \

502 .addresses = (\_addr\_array), \

503 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

504 .mask.addr = { \_\_VA\_ARGS\_\_ }, \

505 .test.fn = npf\_eth\_dst\_addr\_match, \

506 }

507

509

510struct npf\_test\_eth\_type {

511 struct [npf\_test](structnpf__test.md) test;

512 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type; /\* type in network order \*/

513};

514

515extern npf\_test\_fn\_t npf\_eth\_type\_match;

516extern npf\_test\_fn\_t npf\_eth\_type\_unmatch;

517

519

[ 526](group__npf__eth__cond.md#gace7de72d4c64e128a825f28f94d8b1b2)#define NPF\_ETH\_TYPE\_MATCH(\_name, \_type) \

527 struct npf\_test\_eth\_type \_name = { \

528 .type = htons(\_type), \

529 .test.fn = npf\_eth\_type\_match, \

530 }

531

[ 538](group__npf__eth__cond.md#gab9bf6d58433e273220c5fab76f608545)#define NPF\_ETH\_TYPE\_UNMATCH(\_name, \_type) \

539 struct npf\_test\_eth\_type \_name = { \

540 .type = htons(\_type), \

541 .test.fn = npf\_eth\_type\_unmatch, \

542 }

543

545

546#ifdef \_\_cplusplus

547}

548#endif

549

550#endif /\* ZEPHYR\_INCLUDE\_NET\_PKT\_FILTER\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:98

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

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

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

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

[npf\_rule\_list](structnpf__rule__list.md)

rule set for a given test location

**Definition** net\_pkt\_filter.h:61

[npf\_rule\_list::rule\_head](structnpf__rule__list.md#ab6aadf2d3479853c28e94972e7862931)

sys\_slist\_t rule\_head

**Definition** net\_pkt\_filter.h:62

[npf\_rule\_list::lock](structnpf__rule__list.md#af4d539d930acb257b1496761219d26cd)

struct k\_spinlock lock

**Definition** net\_pkt\_filter.h:63

[npf\_rule](structnpf__rule.md)

filter rule structure

**Definition** net\_pkt\_filter.h:48

[npf\_rule::nb\_tests](structnpf__rule.md#a06045c693cf06e6ebfc5a74b8c3f5ef7)

uint32\_t nb\_tests

number of tests for this rule

**Definition** net\_pkt\_filter.h:51

[npf\_rule::tests](structnpf__rule.md#a72c032c55535c82f365b2cd1229cb1e0)

struct npf\_test \* tests[]

pointers to npf\_test instances

**Definition** net\_pkt\_filter.h:52

[npf\_rule::result](structnpf__rule.md#a872daf53310dd8e20477eafd6808481f)

enum net\_verdict result

result if all tests pass

**Definition** net\_pkt\_filter.h:50

[npf\_rule::node](structnpf__rule.md#ad5ae58fbcee5112e2defde1d7f4320dc)

sys\_snode\_t node

**Definition** net\_pkt\_filter.h:49

[npf\_test](structnpf__test.md)

common filter test structure to be embedded into larger structures

**Definition** net\_pkt\_filter.h:43

[npf\_test::fn](structnpf__test.md#ac49921514690a71986ca4d07245cfe7d)

npf\_test\_fn\_t \* fn

packet condition test function

**Definition** net\_pkt\_filter.h:44

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_pkt\_filter.h](net__pkt__filter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
