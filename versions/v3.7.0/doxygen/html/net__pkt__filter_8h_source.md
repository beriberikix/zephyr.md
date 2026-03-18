---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__pkt__filter_8h_source.html
original_path: doxygen/html/net__pkt__filter_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

111

112/\* convenience shortcuts \*/

113#define npf\_insert\_send\_rule(rule) npf\_insert\_rule(&npf\_send\_rules, rule)

114#define npf\_insert\_recv\_rule(rule) npf\_insert\_rule(&npf\_recv\_rules, rule)

115#define npf\_append\_send\_rule(rule) npf\_append\_rule(&npf\_send\_rules, rule)

116#define npf\_append\_recv\_rule(rule) npf\_append\_rule(&npf\_recv\_rules, rule)

117#define npf\_remove\_send\_rule(rule) npf\_remove\_rule(&npf\_send\_rules, rule)

118#define npf\_remove\_recv\_rule(rule) npf\_remove\_rule(&npf\_recv\_rules, rule)

119#define npf\_remove\_all\_send\_rules() npf\_remove\_all\_rules(&npf\_send\_rules)

120#define npf\_remove\_all\_recv\_rules() npf\_remove\_all\_rules(&npf\_recv\_rules)

121

122#ifdef CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK

123#define npf\_insert\_local\_in\_recv\_rule(rule) npf\_insert\_rule(&npf\_local\_in\_recv\_rules, rule)

124#define npf\_append\_local\_in\_recv\_rule(rule) npf\_append\_rule(&npf\_local\_in\_recv\_rules, rule)

125#define npf\_remove\_local\_in\_recv\_rule(rule) npf\_remove\_rule(&npf\_local\_in\_recv\_rules, rule)

126#define npf\_remove\_all\_local\_in\_recv\_rules() npf\_remove\_all\_rules(&npf\_local\_in\_recv\_rules)

127#endif /\* CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK \*/

128

129#ifdef CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK

130#define npf\_insert\_ipv4\_recv\_rule(rule) npf\_insert\_rule(&npf\_ipv4\_recv\_rules, rule)

131#define npf\_append\_ipv4\_recv\_rule(rule) npf\_append\_rule(&npf\_ipv4\_recv\_rules, rule)

132#define npf\_remove\_ipv4\_recv\_rule(rule) npf\_remove\_rule(&npf\_ipv4\_recv\_rules, rule)

133#define npf\_remove\_all\_ipv4\_recv\_rules() npf\_remove\_all\_rules(&npf\_ipv4\_recv\_rules)

134#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK \*/

135

136#ifdef CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK

137#define npf\_insert\_ipv6\_recv\_rule(rule) npf\_insert\_rule(&npf\_ipv6\_recv\_rules, rule)

138#define npf\_append\_ipv6\_recv\_rule(rule) npf\_append\_rule(&npf\_ipv6\_recv\_rules, rule)

139#define npf\_remove\_ipv6\_recv\_rule(rule) npf\_remove\_rule(&npf\_ipv6\_recv\_rules, rule)

140#define npf\_remove\_all\_ipv6\_recv\_rules() npf\_remove\_all\_rules(&npf\_ipv6\_recv\_rules)

141#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK \*/

142

144

[ 199](group__net__pkt__filter.md#ga2f45093d5ad164d5c51a8996f7f04d32)#define NPF\_RULE(\_name, \_result, ...) \

200 struct npf\_rule \_name = { \

201 .result = (\_result), \

202 .nb\_tests = NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_) + 1, \

203 .tests = { FOR\_EACH(Z\_NPF\_TEST\_ADDR, (,), \_\_VA\_ARGS\_\_) }, \

204 }

205

206#define Z\_NPF\_TEST\_ADDR(arg) &arg.test

207

209

215

217

218struct npf\_test\_iface {

219 struct [npf\_test](structnpf__test.md) test;

220 struct [net\_if](structnet__if.md) \*iface;

221};

222

223extern npf\_test\_fn\_t npf\_iface\_match;

224extern npf\_test\_fn\_t npf\_iface\_unmatch;

225extern npf\_test\_fn\_t npf\_orig\_iface\_match;

226extern npf\_test\_fn\_t npf\_orig\_iface\_unmatch;

227

229

[ 236](group__npf__basic__cond.md#ga465578272b616c6267ecd13fd86ca73b)#define NPF\_IFACE\_MATCH(\_name, \_iface) \

237 struct npf\_test\_iface \_name = { \

238 .iface = (\_iface), \

239 .test.fn = npf\_iface\_match, \

240 }

241

[ 248](group__npf__basic__cond.md#gac3607a6736d70b0ea044a2ec7ab6d313)#define NPF\_IFACE\_UNMATCH(\_name, \_iface) \

249 struct npf\_test\_iface \_name = { \

250 .iface = (\_iface), \

251 .test.fn = npf\_iface\_unmatch, \

252 }

253

[ 260](group__npf__basic__cond.md#ga55021acd131e4684568aaf6434b08789)#define NPF\_ORIG\_IFACE\_MATCH(\_name, \_iface) \

261 struct npf\_test\_iface \_name = { \

262 .iface = (\_iface), \

263 .test.fn = npf\_orig\_iface\_match, \

264 }

265

[ 272](group__npf__basic__cond.md#gad959dc62d47ca3b4d2f24a6c862c7623)#define NPF\_ORIG\_IFACE\_UNMATCH(\_name, \_iface) \

273 struct npf\_test\_iface \_name = { \

274 .iface = (\_iface), \

275 .test.fn = npf\_orig\_iface\_unmatch, \

276 }

277

279

280struct npf\_test\_size\_bounds {

281 struct [npf\_test](structnpf__test.md) test;

282 size\_t min;

283 size\_t max;

284};

285

286extern npf\_test\_fn\_t npf\_size\_inbounds;

287

289

[ 296](group__npf__basic__cond.md#gaf142455f9bea3dea8faa0a913072b63e)#define NPF\_SIZE\_MIN(\_name, \_size) \

297 struct npf\_test\_size\_bounds \_name = { \

298 .min = (\_size), \

299 .max = SIZE\_MAX, \

300 .test.fn = npf\_size\_inbounds, \

301 }

302

[ 309](group__npf__basic__cond.md#gacd56b9bcf2b2ba4759402650a9bff67a)#define NPF\_SIZE\_MAX(\_name, \_size) \

310 struct npf\_test\_size\_bounds \_name = { \

311 .min = 0, \

312 .max = (\_size), \

313 .test.fn = npf\_size\_inbounds, \

314 }

315

[ 323](group__npf__basic__cond.md#gab402bb13c7899d57532d3dcf8a36ed4b)#define NPF\_SIZE\_BOUNDS(\_name, \_min\_size, \_max\_size) \

324 struct npf\_test\_size\_bounds \_name = { \

325 .min = (\_min\_size), \

326 .max = (\_max\_size), \

327 .test.fn = npf\_size\_inbounds, \

328 }

329

331

332struct npf\_test\_ip {

333 struct [npf\_test](structnpf__test.md) test;

334 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr\_family;

335 void \*ipaddr;

336 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ipaddr\_num;

337};

338

339extern npf\_test\_fn\_t npf\_ip\_src\_addr\_match;

340extern npf\_test\_fn\_t npf\_ip\_src\_addr\_unmatch;

341

343

[ 356](group__npf__basic__cond.md#ga4dd013f0fb92eb0433f174cf40e89e00)#define NPF\_IP\_SRC\_ADDR\_ALLOWLIST(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) \

357 struct npf\_test\_ip \_name = { \

358 .addr\_family = \_af, \

359 .ipaddr = (\_ip\_addr\_array), \

360 .ipaddr\_num = \_ip\_addr\_num, \

361 .test.fn = npf\_ip\_src\_addr\_match, \

362 }

363

[ 376](group__npf__basic__cond.md#ga57fe28a992b1afaf33581292fe5015bd)#define NPF\_IP\_SRC\_ADDR\_BLOCKLIST(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) \

377 struct npf\_test\_ip \_name = { \

378 .addr\_family = \_af, \

379 .ipaddr = (\_ip\_addr\_array), \

380 .ipaddr\_num = \_ip\_addr\_num, \

381 .test.fn = npf\_ip\_src\_addr\_unmatch, \

382 }

383

385

391

393

394struct npf\_test\_eth\_addr {

395 struct [npf\_test](structnpf__test.md) test;

396 unsigned int nb\_addresses;

397 struct [net\_eth\_addr](structnet__eth__addr.md) \*addresses;

398 struct [net\_eth\_addr](structnet__eth__addr.md) mask;

399};

400

401extern npf\_test\_fn\_t npf\_eth\_src\_addr\_match;

402extern npf\_test\_fn\_t npf\_eth\_src\_addr\_unmatch;

403extern npf\_test\_fn\_t npf\_eth\_dst\_addr\_match;

404extern npf\_test\_fn\_t npf\_eth\_dst\_addr\_unmatch;

405

407

[ 417](group__npf__eth__cond.md#gad2141ad8d6639c9b92569d55130ca1b1)#define NPF\_ETH\_SRC\_ADDR\_MATCH(\_name, \_addr\_array) \

418 struct npf\_test\_eth\_addr \_name = { \

419 .addresses = (\_addr\_array), \

420 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

421 .test.fn = npf\_eth\_src\_addr\_match, \

422 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

423 }

424

[ 434](group__npf__eth__cond.md#ga228eaa3784f663d8f2e2711e26409043)#define NPF\_ETH\_SRC\_ADDR\_UNMATCH(\_name, \_addr\_array) \

435 struct npf\_test\_eth\_addr \_name = { \

436 .addresses = (\_addr\_array), \

437 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

438 .test.fn = npf\_eth\_src\_addr\_unmatch, \

439 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

440 }

441

[ 451](group__npf__eth__cond.md#ga3d22d687bcd56b7727c51c7bc7f36cac)#define NPF\_ETH\_DST\_ADDR\_MATCH(\_name, \_addr\_array) \

452 struct npf\_test\_eth\_addr \_name = { \

453 .addresses = (\_addr\_array), \

454 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

455 .test.fn = npf\_eth\_dst\_addr\_match, \

456 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

457 }

458

[ 468](group__npf__eth__cond.md#ga3b8a8a22eb992c0e02223f70723c3641)#define NPF\_ETH\_DST\_ADDR\_UNMATCH(\_name, \_addr\_array) \

469 struct npf\_test\_eth\_addr \_name = { \

470 .addresses = (\_addr\_array), \

471 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

472 .test.fn = npf\_eth\_dst\_addr\_unmatch, \

473 .mask.addr = { 0xff, 0xff, 0xff, 0xff, 0xff, 0xff }, \

474 }

475

[ 486](group__npf__eth__cond.md#ga0e06ebc4c9a1a960651be1ba89eeb2fd)#define NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH(\_name, \_addr\_array, ...) \

487 struct npf\_test\_eth\_addr \_name = { \

488 .addresses = (\_addr\_array), \

489 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

490 .mask.addr = { \_\_VA\_ARGS\_\_ }, \

491 .test.fn = npf\_eth\_src\_addr\_match, \

492 }

493

[ 504](group__npf__eth__cond.md#ga7cf793af7b91eccc6e675ff19ed59a14)#define NPF\_ETH\_DST\_ADDR\_MASK\_MATCH(\_name, \_addr\_array, ...) \

505 struct npf\_test\_eth\_addr \_name = { \

506 .addresses = (\_addr\_array), \

507 .nb\_addresses = ARRAY\_SIZE(\_addr\_array), \

508 .mask.addr = { \_\_VA\_ARGS\_\_ }, \

509 .test.fn = npf\_eth\_dst\_addr\_match, \

510 }

511

513

514struct npf\_test\_eth\_type {

515 struct [npf\_test](structnpf__test.md) test;

516 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type; /\* type in network order \*/

517};

518

519extern npf\_test\_fn\_t npf\_eth\_type\_match;

520extern npf\_test\_fn\_t npf\_eth\_type\_unmatch;

521

523

[ 530](group__npf__eth__cond.md#gace7de72d4c64e128a825f28f94d8b1b2)#define NPF\_ETH\_TYPE\_MATCH(\_name, \_type) \

531 struct npf\_test\_eth\_type \_name = { \

532 .type = htons(\_type), \

533 .test.fn = npf\_eth\_type\_match, \

534 }

535

[ 542](group__npf__eth__cond.md#gab9bf6d58433e273220c5fab76f608545)#define NPF\_ETH\_TYPE\_UNMATCH(\_name, \_type) \

543 struct npf\_test\_eth\_type \_name = { \

544 .type = htons(\_type), \

545 .test.fn = npf\_eth\_type\_unmatch, \

546 }

547

549

550#ifdef \_\_cplusplus

551}

552#endif

553

554#endif /\* ZEPHYR\_INCLUDE\_NET\_PKT\_FILTER\_H\_ \*/

[ethernet.h](ethernet_8h.md)

Ethernet.

[net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)

net\_verdict

Net Verdict.

**Definition** net\_core.h:100

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

[net\_eth\_addr](structnet__eth__addr.md)

Ethernet address.

**Definition** ethernet.h:51

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[npf\_rule\_list](structnpf__rule__list.md)

rule set for a given test location

**Definition** net\_pkt\_filter.h:61

[npf\_rule\_list::rule\_head](structnpf__rule__list.md#ab6aadf2d3479853c28e94972e7862931)

sys\_slist\_t rule\_head

List head.

**Definition** net\_pkt\_filter.h:62

[npf\_rule\_list::lock](structnpf__rule__list.md#af4d539d930acb257b1496761219d26cd)

struct k\_spinlock lock

Lock protecting the list access.

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

Slist rule list node.

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
