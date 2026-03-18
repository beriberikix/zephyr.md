---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ztest__test_8h_source.html
original_path: doxygen/html/ztest__test_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_test.h

[Go to the documentation of this file.](ztest__test_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_TESTSUITE\_ZTEST\_TEST\_H\_

14#define ZEPHYR\_TESTSUITE\_ZTEST\_TEST\_H\_

15

16#include <[zephyr/app\_memory/app\_memdomain.h](app__memdomain_8h.md)>

17#include <[zephyr/init.h](init_8h.md)>

18#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

19#include <[stdbool.h](stdbool_8h.md)>

20

21

31

32#if defined(CONFIG\_USERSPACE)

33#define \_\_USERSPACE\_FLAGS (K\_USER)

34#else

35#define \_\_USERSPACE\_FLAGS (0)

36#endif

37

38#ifdef \_\_cplusplus

39extern "C" {

40#endif

41

[ 48](group__ztest__test.md#gaf4dfaad1b5f1059e87f406979769aa26)enum [ztest\_expected\_result](group__ztest__test.md#gaf4dfaad1b5f1059e87f406979769aa26) {

[ 49](group__ztest__test.md#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d) [ZTEST\_EXPECTED\_RESULT\_FAIL](group__ztest__test.md#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d) = 0,

[ 50](group__ztest__test.md#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a) [ZTEST\_EXPECTED\_RESULT\_SKIP](group__ztest__test.md#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a),

51};

52

[ 59](structztest__expected__result__entry.md)struct [ztest\_expected\_result\_entry](structztest__expected__result__entry.md) {

[ 60](structztest__expected__result__entry.md#a37352688340aa1c49a7967d5b568c9a1) const char \*[test\_suite\_name](structztest__expected__result__entry.md#a37352688340aa1c49a7967d5b568c9a1);

[ 61](structztest__expected__result__entry.md#a92ada50dadf26e5c59e4e529afffd882) const char \*[test\_name](structztest__expected__result__entry.md#a92ada50dadf26e5c59e4e529afffd882);

[ 62](structztest__expected__result__entry.md#a74524b4da8fddbd64d526cfc5df72743) enum [ztest\_expected\_result](group__ztest__test.md#gaf4dfaad1b5f1059e87f406979769aa26) [expected\_result](structztest__expected__result__entry.md#a74524b4da8fddbd64d526cfc5df72743);

63};

64

65extern struct [ztest\_expected\_result\_entry](structztest__expected__result__entry.md) \_ztest\_expected\_result\_entry\_list\_start[];

66extern struct [ztest\_expected\_result\_entry](structztest__expected__result__entry.md) \_ztest\_expected\_result\_entry\_list\_end[];

67

68#define \_\_ZTEST\_EXPECT(\_suite\_name, \_test\_name, expectation) \

69 static const STRUCT\_SECTION\_ITERABLE( \

70 ztest\_expected\_result\_entry, \

71 UTIL\_CAT(UTIL\_CAT(z\_ztest\_expected\_result\_, \_suite\_name), \_test\_name)) = { \

72 .test\_suite\_name = STRINGIFY(\_suite\_name), \

73 .test\_name = STRINGIFY(\_test\_name), \

74 .expected\_result = expectation, \

75 }

76

[ 90](group__ztest__test.md#gaeaa5b96855dd45e015b9556212f8945a)#define ZTEST\_EXPECT\_FAIL(\_suite\_name, \_test\_name) \

91 \_\_ZTEST\_EXPECT(\_suite\_name, \_test\_name, ZTEST\_EXPECTED\_RESULT\_FAIL)

92

[ 106](group__ztest__test.md#gacb6f06920e522b9a9f6e7a98f0620f38)#define ZTEST\_EXPECT\_SKIP(\_suite\_name, \_test\_name) \

107 \_\_ZTEST\_EXPECT(\_suite\_name, \_test\_name, ZTEST\_EXPECTED\_RESULT\_SKIP)

108

[ 109](structztest__unit__test.md)struct [ztest\_unit\_test](structztest__unit__test.md) {

[ 110](structztest__unit__test.md#ac94283459e71728180420d66b3a4a53a) const char \*[test\_suite\_name](structztest__unit__test.md#ac94283459e71728180420d66b3a4a53a);

[ 111](structztest__unit__test.md#a1176caba02accac7bd2eb02c715a0d38) const char \*[name](structztest__unit__test.md#a1176caba02accac7bd2eb02c715a0d38);

[ 112](structztest__unit__test.md#a5fe0425dde921834acb2c0e387bcc524) void (\*[test](structztest__unit__test.md#a5fe0425dde921834acb2c0e387bcc524))(void \*data);

[ 113](structztest__unit__test.md#a9c151bd9e948788c861503b53c52b24d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [thread\_options](structztest__unit__test.md#a9c151bd9e948788c861503b53c52b24d);

114

[ 116](structztest__unit__test.md#a3b7014bbb299c4aeb6717806e602f38a) struct [ztest\_unit\_test\_stats](structztest__unit__test__stats.md) \*const [stats](structztest__unit__test.md#a3b7014bbb299c4aeb6717806e602f38a);

117};

118

119extern struct [ztest\_unit\_test](structztest__unit__test.md) \_ztest\_unit\_test\_list\_start[];

120extern struct [ztest\_unit\_test](structztest__unit__test.md) \_ztest\_unit\_test\_list\_end[];

[ 122](group__ztest__test.md#ga8777ca60bd21cc128f64833bd7921b9c)#define ZTEST\_TEST\_COUNT (\_ztest\_unit\_test\_list\_end - \_ztest\_unit\_test\_list\_start)

123

[ 127](structztest__suite__stats.md)struct [ztest\_suite\_stats](structztest__suite__stats.md) {

[ 129](structztest__suite__stats.md#a94a4d70901b2d2b57cbaf03b9c6d21a9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [run\_count](structztest__suite__stats.md#a94a4d70901b2d2b57cbaf03b9c6d21a9);

[ 131](structztest__suite__stats.md#a04d888a17a39bdf62f1b935968d58b92) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [skip\_count](structztest__suite__stats.md#a04d888a17a39bdf62f1b935968d58b92);

[ 133](structztest__suite__stats.md#a58f7c9379bc9bf18c2184fdcd2bbff8c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fail\_count](structztest__suite__stats.md#a58f7c9379bc9bf18c2184fdcd2bbff8c);

134};

135

[ 136](structztest__unit__test__stats.md)struct [ztest\_unit\_test\_stats](structztest__unit__test__stats.md) {

[ 138](structztest__unit__test__stats.md#a1f1cc422307e6bd7875e42c7205e47d7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [run\_count](structztest__unit__test__stats.md#a1f1cc422307e6bd7875e42c7205e47d7);

[ 140](structztest__unit__test__stats.md#a5370f1797292d3fe575166e161dee43f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [skip\_count](structztest__unit__test__stats.md#a5370f1797292d3fe575166e161dee43f);

[ 142](structztest__unit__test__stats.md#addbacc4315f502b2c69ee5ebf5884ad6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fail\_count](structztest__unit__test__stats.md#addbacc4315f502b2c69ee5ebf5884ad6);

[ 144](structztest__unit__test__stats.md#a21c2c8a05524e673567c7ee3d809ad25) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pass\_count](structztest__unit__test__stats.md#a21c2c8a05524e673567c7ee3d809ad25);

[ 146](structztest__unit__test__stats.md#ac24d475c52c4ea7a0de4e99f2d76d1a1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [duration\_worst\_ms](structztest__unit__test__stats.md#ac24d475c52c4ea7a0de4e99f2d76d1a1);

147};

148

[ 154](group__ztest__test.md#ga0063907dd70b9eb817ea472162693ee4)typedef void \*(\*ztest\_suite\_setup\_t)(void);

155

[ 161](group__ztest__test.md#gac8a204832c267fed047e7707b65be74d)typedef void (\*[ztest\_suite\_before\_t](group__ztest__test.md#gac8a204832c267fed047e7707b65be74d))(void \*fixture);

162

[ 168](group__ztest__test.md#ga0f9eeb8ddae455c1e7cc7a388a7b013c)typedef void (\*[ztest\_suite\_after\_t](group__ztest__test.md#ga0f9eeb8ddae455c1e7cc7a388a7b013c))(void \*fixture);

169

[ 175](group__ztest__test.md#ga7769b894fdac5283ac949ce8fceea0dd)typedef void (\*[ztest\_suite\_teardown\_t](group__ztest__test.md#ga7769b894fdac5283ac949ce8fceea0dd))(void \*fixture);

176

[ 184](group__ztest__test.md#gad5323aa82773dac33cf0930e9524420c)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[ztest\_suite\_predicate\_t](group__ztest__test.md#gad5323aa82773dac33cf0930e9524420c))(const void \*global\_state);

185

[ 190](structztest__suite__node.md)struct [ztest\_suite\_node](structztest__suite__node.md) {

[ 192](structztest__suite__node.md#a55f700029b3f6dbfd1bd9ce7df6808e4) const char \*const [name](structztest__suite__node.md#a55f700029b3f6dbfd1bd9ce7df6808e4);

193

[ 195](structztest__suite__node.md#a0a30e674f7a071e43e1ff1e190bf2020) const [ztest\_suite\_setup\_t](group__ztest__test.md#ga0063907dd70b9eb817ea472162693ee4) [setup](structztest__suite__node.md#a0a30e674f7a071e43e1ff1e190bf2020);

196

[ 198](structztest__suite__node.md#a0a1eeaa1f0b90918e6b87e1d37d84eef) const [ztest\_suite\_before\_t](group__ztest__test.md#gac8a204832c267fed047e7707b65be74d) [before](structztest__suite__node.md#a0a1eeaa1f0b90918e6b87e1d37d84eef);

199

[ 201](structztest__suite__node.md#a46ec271d4a7625b01daac27899d5eae4) const [ztest\_suite\_after\_t](group__ztest__test.md#ga0f9eeb8ddae455c1e7cc7a388a7b013c) [after](structztest__suite__node.md#a46ec271d4a7625b01daac27899d5eae4);

202

[ 204](structztest__suite__node.md#a97f7e248b5fe9548010d659816f8d295) const [ztest\_suite\_teardown\_t](group__ztest__test.md#ga7769b894fdac5283ac949ce8fceea0dd) [teardown](structztest__suite__node.md#a97f7e248b5fe9548010d659816f8d295);

205

[ 207](structztest__suite__node.md#ac0a66cf7eb644fbc7c161ee61c854385) const [ztest\_suite\_predicate\_t](group__ztest__test.md#gad5323aa82773dac33cf0930e9524420c) [predicate](structztest__suite__node.md#ac0a66cf7eb644fbc7c161ee61c854385);

208

[ 210](structztest__suite__node.md#a1d80587f1e1c841d6c4d43b5fe3c9b4d) struct [ztest\_suite\_stats](structztest__suite__stats.md) \*const [stats](structztest__suite__node.md#a1d80587f1e1c841d6c4d43b5fe3c9b4d);

211};

212

213extern struct [ztest\_suite\_node](structztest__suite__node.md) \_ztest\_suite\_node\_list\_start[];

214extern struct [ztest\_suite\_node](structztest__suite__node.md) \_ztest\_suite\_node\_list\_end[];

215

[ 217](group__ztest__test.md#ga678b4ae96879c029e6e567a326bbf027)#define ZTEST\_SUITE\_COUNT (\_ztest\_suite\_node\_list\_end - \_ztest\_suite\_node\_list\_start)

218

[ 233](group__ztest__test.md#gaef8892743e2d47c983efcb61beeedeb3)#define ZTEST\_SUITE(SUITE\_NAME, PREDICATE, setup\_fn, before\_fn, after\_fn, teardown\_fn) \

234 struct ztest\_suite\_stats UTIL\_CAT(z\_ztest\_suite\_node\_stats\_, SUITE\_NAME); \

235 static const STRUCT\_SECTION\_ITERABLE(ztest\_suite\_node, \

236 UTIL\_CAT(z\_ztest\_test\_node\_, SUITE\_NAME)) = { \

237 .name = STRINGIFY(SUITE\_NAME), \

238 .setup = (setup\_fn), \

239 .before = (before\_fn), \

240 .after = (after\_fn), \

241 .teardown = (teardown\_fn), \

242 .predicate = PREDICATE, \

243 .stats = &UTIL\_CAT(z\_ztest\_suite\_node\_stats\_, SUITE\_NAME), \

244 }

245

[ 253](group__ztest__test.md#gac6b1f8b820cd682094b7aaeebdaa106e)void [ztest\_run\_all](group__ztest__test.md#gac6b1f8b820cd682094b7aaeebdaa106e)(const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), bool shuffle, int suite\_iter, int case\_iter);

254

[ 259](group__ztest__test.md#gac2842295307e7286d256bb179be60b02)enum [ztest\_result](group__ztest__test.md#gac2842295307e7286d256bb179be60b02) {

[ 260](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc) [ZTEST\_RESULT\_PENDING](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc),

[ 261](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e) [ZTEST\_RESULT\_PASS](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e),

[ 262](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888) [ZTEST\_RESULT\_FAIL](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888),

[ 263](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4) [ZTEST\_RESULT\_SKIP](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4),

[ 264](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e) [ZTEST\_RESULT\_SUITE\_SKIP](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e),

[ 265](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55) [ZTEST\_RESULT\_SUITE\_FAIL](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55),

266};

267

[ 272](group__ztest__test.md#ga5dde8913cf45656bca8a48c825a95d59)enum [ztest\_phase](group__ztest__test.md#ga5dde8913cf45656bca8a48c825a95d59) {

[ 273](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf) [TEST\_PHASE\_SETUP](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf),

[ 274](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765) [TEST\_PHASE\_BEFORE](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765),

[ 275](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1) [TEST\_PHASE\_TEST](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1),

[ 276](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663) [TEST\_PHASE\_AFTER](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663),

[ 277](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901) [TEST\_PHASE\_TEARDOWN](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901),

[ 278](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971) [TEST\_PHASE\_FRAMEWORK](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971),

279};

280

290

291#ifdef ZTEST\_UNITTEST

292int z\_impl\_ztest\_run\_test\_suites(const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), bool shuffle,

293 int suite\_iter, int case\_iter);

294

295static inline int [ztest\_run\_test\_suites](group__ztest__test.md#gaafb3cba3a9637839952b2db2486ab88c)(const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), bool shuffle,

296 int suite\_iter, int case\_iter)

297{

298 return z\_impl\_ztest\_run\_test\_suites([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), shuffle, suite\_iter, case\_iter);

299}

300

301#else

[ 302](group__ztest__test.md#gaafb3cba3a9637839952b2db2486ab88c)\_\_syscall int [ztest\_run\_test\_suites](group__ztest__test.md#gaafb3cba3a9637839952b2db2486ab88c)(const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), bool shuffle,

303 int suite\_iter, int case\_iter);

304#endif

305

306#ifdef ZTEST\_UNITTEST

307void z\_impl\_\_\_ztest\_set\_test\_result(enum [ztest\_result](group__ztest__test.md#gac2842295307e7286d256bb179be60b02) new\_result);

308static inline void \_\_ztest\_set\_test\_result(enum [ztest\_result](group__ztest__test.md#gac2842295307e7286d256bb179be60b02) new\_result)

309{

310 z\_impl\_\_\_ztest\_set\_test\_result(new\_result);

311}

312

313void z\_impl\_\_\_ztest\_set\_test\_phase(enum [ztest\_phase](group__ztest__test.md#ga5dde8913cf45656bca8a48c825a95d59) new\_phase);

314static inline void \_\_ztest\_set\_test\_phase(enum [ztest\_phase](group__ztest__test.md#ga5dde8913cf45656bca8a48c825a95d59) new\_phase)

315{

316 z\_impl\_\_\_ztest\_set\_test\_phase(new\_phase);

317}

318#else

319\_\_syscall void \_\_ztest\_set\_test\_result(enum [ztest\_result](group__ztest__test.md#gac2842295307e7286d256bb179be60b02) new\_result);

320\_\_syscall void \_\_ztest\_set\_test\_phase(enum [ztest\_phase](group__ztest__test.md#ga5dde8913cf45656bca8a48c825a95d59) new\_phase);

321#endif

322

323

[ 333](group__ztest__test.md#ga349fda278dff713debfd2a3b94b8b1eb)void [ztest\_verify\_all\_test\_suites\_ran](group__ztest__test.md#ga349fda278dff713debfd2a3b94b8b1eb)(void);

334

347int z\_ztest\_run\_test\_suite(const char \*[name](structztest__suite__node.md#a55f700029b3f6dbfd1bd9ce7df6808e4), bool shuffle, int suite\_iter, int case\_iter);

348

357struct [ztest\_unit\_test](structztest__unit__test.md) \*z\_ztest\_get\_next\_test(const char \*suite, struct [ztest\_unit\_test](structztest__unit__test.md) \*prev);

358

359/\* definitions for use with testing application shared memory \*/

360#ifdef CONFIG\_USERSPACE

[ 364](group__ztest__test.md#ga2c7d0aa85e7f320d582395c5ded90133)#define ZTEST\_DMEM K\_APP\_DMEM(ztest\_mem\_partition)

[ 368](group__ztest__test.md#gac3de5965061b1164a8033712c9094e23)#define ZTEST\_BMEM K\_APP\_BMEM(ztest\_mem\_partition)

[ 372](group__ztest__test.md#ga44777f5011728bbff63fe3639c1b4aa8)#define ZTEST\_SECTION K\_APP\_DMEM\_SECTION(ztest\_mem\_partition)

373extern struct [k\_mem\_partition](structk__mem__partition.md) [ztest\_mem\_partition](group__ztest__test.md#ga3adced2fdda96833e6b1ecbf3d61d446);

374#else

375#define ZTEST\_DMEM

376#define ZTEST\_BMEM

377#define ZTEST\_SECTION .data

378#endif

379

[ 386](group__ztest__test.md#gacd6eb423f54dce8544f7c3b1618c0374)void [ztest\_test\_fail](group__ztest__test.md#gacd6eb423f54dce8544f7c3b1618c0374)(void);

387

[ 396](group__ztest__test.md#ga085d30a04102ebb8c3f2206020723ee0)void [ztest\_test\_pass](group__ztest__test.md#ga085d30a04102ebb8c3f2206020723ee0)(void);

397

[ 402](group__ztest__test.md#gada3b1fcfa71db1bf7787c03ff45256d5)void [ztest\_test\_skip](group__ztest__test.md#gada3b1fcfa71db1bf7787c03ff45256d5)(void);

403

404

[ 405](group__ztest__test.md#ga17537c79021fbc12e56b72ccec4b99c5)void [ztest\_skip\_failed\_assumption](group__ztest__test.md#ga17537c79021fbc12e56b72ccec4b99c5)(void);

406

407#define Z\_TEST(suite, fn, t\_options, use\_fixture) \

408 struct ztest\_unit\_test\_stats z\_ztest\_unit\_test\_stats\_##suite##\_##fn; \

409 static void \_##suite##\_##fn##\_wrapper(void \*data); \

410 static void suite##\_##fn( \

411 COND\_CODE\_1(use\_fixture, (struct suite##\_fixture \*fixture), (void))); \

412 static STRUCT\_SECTION\_ITERABLE(ztest\_unit\_test, z\_ztest\_unit\_test\_\_##suite##\_\_##fn) = { \

413 .test\_suite\_name = STRINGIFY(suite), \

414 .name = STRINGIFY(fn), \

415 .test = (\_##suite##\_##fn##\_wrapper), \

416 .thread\_options = t\_options, \

417 .stats = &z\_ztest\_unit\_test\_stats\_##suite##\_##fn \

418 }; \

419 static void \_##suite##\_##fn##\_wrapper(void \*wrapper\_data) \

420 { \

421 COND\_CODE\_1(use\_fixture, (suite##\_##fn((struct suite##\_fixture \*)wrapper\_data);), \

422 (ARG\_UNUSED(wrapper\_data); suite##\_##fn();)) \

423 } \

424 static inline void suite##\_##fn( \

425 COND\_CODE\_1(use\_fixture, (struct suite##\_fixture \*fixture), (void)))

426

427#define Z\_ZTEST(suite, fn, t\_options) Z\_TEST(suite, fn, t\_options, 0)

428#define Z\_ZTEST\_F(suite, fn, t\_options) Z\_TEST(suite, fn, t\_options, 1)

429

438#define Z\_TEST\_SKIP\_IFDEF(config) COND\_CODE\_1(config, (ztest\_test\_skip()), ())

439

449#define Z\_TEST\_SKIP\_IFNDEF(config) COND\_CODE\_1(config, (), (ztest\_test\_skip()))

450

[ 460](group__ztest__test.md#gac25858f76ea667d07de422a3b489cb15)#define ZTEST(suite, fn) Z\_ZTEST(suite, fn, 0)

461

[ 471](group__ztest__test.md#ga7121acc7ee00646cacefa773ff9631c8)#define ZTEST\_USER(suite, fn) Z\_ZTEST(suite, fn, K\_USER)

472

[ 482](group__ztest__test.md#gacd3ab522e0e5c8a270e86b0cb6bd81b2)#define ZTEST\_F(suite, fn) Z\_ZTEST\_F(suite, fn, 0)

483

[ 493](group__ztest__test.md#ga12ccce144e577cac6ba763982ad14def)#define ZTEST\_USER\_F(suite, fn) Z\_ZTEST\_F(suite, fn, K\_USER)

494

[ 504](group__ztest__test.md#ga2090c493018a95112b89c5f83b5d8162)typedef void (\*[ztest\_rule\_cb](group__ztest__test.md#ga2090c493018a95112b89c5f83b5d8162))(const struct [ztest\_unit\_test](structztest__unit__test.md) \*[test](structztest__unit__test.md#a5fe0425dde921834acb2c0e387bcc524), void \*data);

505

507struct ztest\_test\_rule {

508 [ztest\_rule\_cb](group__ztest__test.md#ga2090c493018a95112b89c5f83b5d8162) before\_each;

509 [ztest\_rule\_cb](group__ztest__test.md#ga2090c493018a95112b89c5f83b5d8162) after\_each;

510};

511

[ 531](group__ztest__test.md#ga2a0a5e3b6e8fa1c9a03e7600895d875f)#define ZTEST\_RULE(name, before\_each\_fn, after\_each\_fn) \

532 static STRUCT\_SECTION\_ITERABLE(ztest\_test\_rule, z\_ztest\_test\_rule\_##name) = { \

533 .before\_each = (before\_each\_fn), \

534 .after\_each = (after\_each\_fn), \

535 }

536

537extern struct ztest\_test\_rule \_ztest\_test\_rule\_list\_start[];

538extern struct ztest\_test\_rule \_ztest\_test\_rule\_list\_end[];

539

[ 547](group__ztest__test.md#gac7ddc33b5a0d11e2ffa0a564019c5e3d)void [ztest\_simple\_1cpu\_before](group__ztest__test.md#gac7ddc33b5a0d11e2ffa0a564019c5e3d)(void \*data);

548

[ 556](group__ztest__test.md#gaa53486873430dd8fa978745d8a1d0686)void [ztest\_simple\_1cpu\_after](group__ztest__test.md#gaa53486873430dd8fa978745d8a1d0686)(void \*data);

557

[ 566](group__ztest__test.md#ga29557673d07a87d5d4ace36521937848)#define ztest\_run\_test\_suite(suite, shuffle, suite\_iter, case\_iter) \

567 z\_ztest\_run\_test\_suite(STRINGIFY(suite), shuffle, suite\_iter, case\_iter)

568

[ 573](structztest__arch__api.md)struct [ztest\_arch\_api](structztest__arch__api.md) {

[ 574](structztest__arch__api.md#a005bcb042aee46de9088b7527df49f9f) void (\*[run\_all](structztest__arch__api.md#a005bcb042aee46de9088b7527df49f9f))(const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), bool shuffle, int suite\_iter, int case\_iter);

[ 575](structztest__arch__api.md#a427413d24056eb42d3a5302c28bd4329) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[should\_suite\_run](structztest__arch__api.md#a427413d24056eb42d3a5302c28bd4329))(const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [ztest\_suite\_node](structztest__suite__node.md) \*suite);

[ 576](structztest__arch__api.md#a8334b1ecc7efc93245fe35c7c1da728a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[should\_test\_run](structztest__arch__api.md#a8334b1ecc7efc93245fe35c7c1da728a))(const char \*suite, const char \*test);

577};

578

582

583\_\_syscall void z\_test\_1cpu\_start(void);

584\_\_syscall void z\_test\_1cpu\_stop(void);

585

[ 586](ztest__test_8h.md#a846fcbfbda9794cba2dcf1c34bd9be1b)\_\_syscall void [sys\_clock\_tick\_set](ztest__test_8h.md#a846fcbfbda9794cba2dcf1c34bd9be1b)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tick);

587

588#ifdef \_\_cplusplus

589}

590#endif

591

592#ifndef ZTEST\_UNITTEST

593#include <zephyr/syscalls/ztest\_test.h>

594#endif

595

596#endif /\* ZEPHYR\_TESTSUITE\_ZTEST\_TEST\_H\_ \*/

[app\_memdomain.h](app__memdomain_8h.md)

[ztest\_suite\_setup\_t](group__ztest__test.md#ga0063907dd70b9eb817ea472162693ee4)

void \*(\* ztest\_suite\_setup\_t)(void)

Setup function to run before running this suite.

**Definition** ztest\_test.h:154

[ztest\_test\_pass](group__ztest__test.md#ga085d30a04102ebb8c3f2206020723ee0)

void ztest\_test\_pass(void)

Pass the currently running test.

[ztest\_suite\_after\_t](group__ztest__test.md#ga0f9eeb8ddae455c1e7cc7a388a7b013c)

void(\* ztest\_suite\_after\_t)(void \*fixture)

Function to run after each test in this suite.

**Definition** ztest\_test.h:168

[ztest\_skip\_failed\_assumption](group__ztest__test.md#ga17537c79021fbc12e56b72ccec4b99c5)

void ztest\_skip\_failed\_assumption(void)

[ztest\_rule\_cb](group__ztest__test.md#ga2090c493018a95112b89c5f83b5d8162)

void(\* ztest\_rule\_cb)(const struct ztest\_unit\_test \*test, void \*data)

Test rule callback function signature.

**Definition** ztest\_test.h:504

[ztest\_verify\_all\_test\_suites\_ran](group__ztest__test.md#ga349fda278dff713debfd2a3b94b8b1eb)

void ztest\_verify\_all\_test\_suites\_ran(void)

Fails the test if any of the registered tests did not run.

[ztest\_mem\_partition](group__ztest__test.md#ga3adced2fdda96833e6b1ecbf3d61d446)

struct k\_mem\_partition ztest\_mem\_partition

[ztest\_phase](group__ztest__test.md#ga5dde8913cf45656bca8a48c825a95d59)

ztest\_phase

Each enum member represents a distinct phase of execution for the test binary.

**Definition** ztest\_test.h:272

[ztest\_suite\_teardown\_t](group__ztest__test.md#ga7769b894fdac5283ac949ce8fceea0dd)

void(\* ztest\_suite\_teardown\_t)(void \*fixture)

Teardown function to run after running this suite.

**Definition** ztest\_test.h:175

[ztest\_simple\_1cpu\_after](group__ztest__test.md#gaa53486873430dd8fa978745d8a1d0686)

void ztest\_simple\_1cpu\_after(void \*data)

A 'after' function to use in test suites that just need to stop 1cpu.

[ztest\_run\_test\_suites](group__ztest__test.md#gaafb3cba3a9637839952b2db2486ab88c)

int ztest\_run\_test\_suites(const void \*state, bool shuffle, int suite\_iter, int case\_iter)

Run the registered unit tests which return true from their predicate function.

[ztest\_result](group__ztest__test.md#gac2842295307e7286d256bb179be60b02)

ztest\_result

The result of the current running test.

**Definition** ztest\_test.h:259

[ztest\_run\_all](group__ztest__test.md#gac6b1f8b820cd682094b7aaeebdaa106e)

void ztest\_run\_all(const void \*state, bool shuffle, int suite\_iter, int case\_iter)

Default entry point for running or listing registered unit tests.

[ztest\_simple\_1cpu\_before](group__ztest__test.md#gac7ddc33b5a0d11e2ffa0a564019c5e3d)

void ztest\_simple\_1cpu\_before(void \*data)

A 'before' function to use in test suites that just need to start 1cpu.

[ztest\_suite\_before\_t](group__ztest__test.md#gac8a204832c267fed047e7707b65be74d)

void(\* ztest\_suite\_before\_t)(void \*fixture)

Function to run before each test in this suite.

**Definition** ztest\_test.h:161

[ztest\_test\_fail](group__ztest__test.md#gacd6eb423f54dce8544f7c3b1618c0374)

void ztest\_test\_fail(void)

Fail the currently running test.

[ztest\_suite\_predicate\_t](group__ztest__test.md#gad5323aa82773dac33cf0930e9524420c)

bool(\* ztest\_suite\_predicate\_t)(const void \*global\_state)

An optional predicate function to determine if the test should run.

**Definition** ztest\_test.h:184

[ztest\_test\_skip](group__ztest__test.md#gada3b1fcfa71db1bf7787c03ff45256d5)

void ztest\_test\_skip(void)

Skip the current test.

[ztest\_expected\_result](group__ztest__test.md#gaf4dfaad1b5f1059e87f406979769aa26)

ztest\_expected\_result

The expected result of a test.

**Definition** ztest\_test.h:48

[TEST\_PHASE\_TEST](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1)

@ TEST\_PHASE\_TEST

**Definition** ztest\_test.h:275

[TEST\_PHASE\_AFTER](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663)

@ TEST\_PHASE\_AFTER

**Definition** ztest\_test.h:276

[TEST\_PHASE\_BEFORE](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765)

@ TEST\_PHASE\_BEFORE

**Definition** ztest\_test.h:274

[TEST\_PHASE\_SETUP](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf)

@ TEST\_PHASE\_SETUP

**Definition** ztest\_test.h:273

[TEST\_PHASE\_TEARDOWN](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901)

@ TEST\_PHASE\_TEARDOWN

**Definition** ztest\_test.h:277

[TEST\_PHASE\_FRAMEWORK](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971)

@ TEST\_PHASE\_FRAMEWORK

**Definition** ztest\_test.h:278

[ZTEST\_RESULT\_SKIP](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4)

@ ZTEST\_RESULT\_SKIP

**Definition** ztest\_test.h:263

[ZTEST\_RESULT\_PENDING](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc)

@ ZTEST\_RESULT\_PENDING

**Definition** ztest\_test.h:260

[ZTEST\_RESULT\_PASS](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e)

@ ZTEST\_RESULT\_PASS

**Definition** ztest\_test.h:261

[ZTEST\_RESULT\_FAIL](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888)

@ ZTEST\_RESULT\_FAIL

**Definition** ztest\_test.h:262

[ZTEST\_RESULT\_SUITE\_FAIL](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55)

@ ZTEST\_RESULT\_SUITE\_FAIL

**Definition** ztest\_test.h:265

[ZTEST\_RESULT\_SUITE\_SKIP](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e)

@ ZTEST\_RESULT\_SUITE\_SKIP

**Definition** ztest\_test.h:264

[ZTEST\_EXPECTED\_RESULT\_FAIL](group__ztest__test.md#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d)

@ ZTEST\_EXPECTED\_RESULT\_FAIL

Expect a test to fail.

**Definition** ztest\_test.h:49

[ZTEST\_EXPECTED\_RESULT\_SKIP](group__ztest__test.md#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a)

@ ZTEST\_EXPECTED\_RESULT\_SKIP

Expect a test to pass.

**Definition** ztest\_test.h:50

[init.h](init_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[ztest\_arch\_api](structztest__arch__api.md)

Structure for architecture specific APIs.

**Definition** ztest\_test.h:573

[ztest\_arch\_api::run\_all](structztest__arch__api.md#a005bcb042aee46de9088b7527df49f9f)

void(\* run\_all)(const void \*state, bool shuffle, int suite\_iter, int case\_iter)

**Definition** ztest\_test.h:574

[ztest\_arch\_api::should\_suite\_run](structztest__arch__api.md#a427413d24056eb42d3a5302c28bd4329)

bool(\* should\_suite\_run)(const void \*state, struct ztest\_suite\_node \*suite)

**Definition** ztest\_test.h:575

[ztest\_arch\_api::should\_test\_run](structztest__arch__api.md#a8334b1ecc7efc93245fe35c7c1da728a)

bool(\* should\_test\_run)(const char \*suite, const char \*test)

**Definition** ztest\_test.h:576

[ztest\_expected\_result\_entry](structztest__expected__result__entry.md)

A single expectation entry allowing tests to fail/skip and be considered passing.

**Definition** ztest\_test.h:59

[ztest\_expected\_result\_entry::test\_suite\_name](structztest__expected__result__entry.md#a37352688340aa1c49a7967d5b568c9a1)

const char \* test\_suite\_name

The test suite's name for the expectation.

**Definition** ztest\_test.h:60

[ztest\_expected\_result\_entry::expected\_result](structztest__expected__result__entry.md#a74524b4da8fddbd64d526cfc5df72743)

enum ztest\_expected\_result expected\_result

The expectation.

**Definition** ztest\_test.h:62

[ztest\_expected\_result\_entry::test\_name](structztest__expected__result__entry.md#a92ada50dadf26e5c59e4e529afffd882)

const char \* test\_name

The test's name for the expectation.

**Definition** ztest\_test.h:61

[ztest\_suite\_node](structztest__suite__node.md)

A single node of test suite.

**Definition** ztest\_test.h:190

[ztest\_suite\_node::before](structztest__suite__node.md#a0a1eeaa1f0b90918e6b87e1d37d84eef)

const ztest\_suite\_before\_t before

Before function.

**Definition** ztest\_test.h:198

[ztest\_suite\_node::setup](structztest__suite__node.md#a0a30e674f7a071e43e1ff1e190bf2020)

const ztest\_suite\_setup\_t setup

Setup function.

**Definition** ztest\_test.h:195

[ztest\_suite\_node::stats](structztest__suite__node.md#a1d80587f1e1c841d6c4d43b5fe3c9b4d)

struct ztest\_suite\_stats \*const stats

Stats.

**Definition** ztest\_test.h:210

[ztest\_suite\_node::after](structztest__suite__node.md#a46ec271d4a7625b01daac27899d5eae4)

const ztest\_suite\_after\_t after

After function.

**Definition** ztest\_test.h:201

[ztest\_suite\_node::name](structztest__suite__node.md#a55f700029b3f6dbfd1bd9ce7df6808e4)

const char \*const name

The name of the test suite.

**Definition** ztest\_test.h:192

[ztest\_suite\_node::teardown](structztest__suite__node.md#a97f7e248b5fe9548010d659816f8d295)

const ztest\_suite\_teardown\_t teardown

Teardown function.

**Definition** ztest\_test.h:204

[ztest\_suite\_node::predicate](structztest__suite__node.md#ac0a66cf7eb644fbc7c161ee61c854385)

const ztest\_suite\_predicate\_t predicate

Optional predicate filter.

**Definition** ztest\_test.h:207

[ztest\_suite\_stats](structztest__suite__stats.md)

Stats about a ztest suite.

**Definition** ztest\_test.h:127

[ztest\_suite\_stats::skip\_count](structztest__suite__stats.md#a04d888a17a39bdf62f1b935968d58b92)

uint32\_t skip\_count

The number of times that the suite was skipped.

**Definition** ztest\_test.h:131

[ztest\_suite\_stats::fail\_count](structztest__suite__stats.md#a58f7c9379bc9bf18c2184fdcd2bbff8c)

uint32\_t fail\_count

The number of times that the suite failed.

**Definition** ztest\_test.h:133

[ztest\_suite\_stats::run\_count](structztest__suite__stats.md#a94a4d70901b2d2b57cbaf03b9c6d21a9)

uint32\_t run\_count

The number of times that the suite ran.

**Definition** ztest\_test.h:129

[ztest\_unit\_test\_stats](structztest__unit__test__stats.md)

**Definition** ztest\_test.h:136

[ztest\_unit\_test\_stats::run\_count](structztest__unit__test__stats.md#a1f1cc422307e6bd7875e42c7205e47d7)

uint32\_t run\_count

The number of times that the test ran.

**Definition** ztest\_test.h:138

[ztest\_unit\_test\_stats::pass\_count](structztest__unit__test__stats.md#a21c2c8a05524e673567c7ee3d809ad25)

uint32\_t pass\_count

The number of times that the test passed.

**Definition** ztest\_test.h:144

[ztest\_unit\_test\_stats::skip\_count](structztest__unit__test__stats.md#a5370f1797292d3fe575166e161dee43f)

uint32\_t skip\_count

The number of times that the test was skipped.

**Definition** ztest\_test.h:140

[ztest\_unit\_test\_stats::duration\_worst\_ms](structztest__unit__test__stats.md#ac24d475c52c4ea7a0de4e99f2d76d1a1)

uint32\_t duration\_worst\_ms

The longest duration of the test across multiple times.

**Definition** ztest\_test.h:146

[ztest\_unit\_test\_stats::fail\_count](structztest__unit__test__stats.md#addbacc4315f502b2c69ee5ebf5884ad6)

uint32\_t fail\_count

The number of times that the test failed.

**Definition** ztest\_test.h:142

[ztest\_unit\_test](structztest__unit__test.md)

**Definition** ztest\_test.h:109

[ztest\_unit\_test::name](structztest__unit__test.md#a1176caba02accac7bd2eb02c715a0d38)

const char \* name

**Definition** ztest\_test.h:111

[ztest\_unit\_test::stats](structztest__unit__test.md#a3b7014bbb299c4aeb6717806e602f38a)

struct ztest\_unit\_test\_stats \*const stats

Stats.

**Definition** ztest\_test.h:116

[ztest\_unit\_test::test](structztest__unit__test.md#a5fe0425dde921834acb2c0e387bcc524)

void(\* test)(void \*data)

**Definition** ztest\_test.h:112

[ztest\_unit\_test::thread\_options](structztest__unit__test.md#a9c151bd9e948788c861503b53c52b24d)

uint32\_t thread\_options

**Definition** ztest\_test.h:113

[ztest\_unit\_test::test\_suite\_name](structztest__unit__test.md#ac94283459e71728180420d66b3a4a53a)

const char \* test\_suite\_name

**Definition** ztest\_test.h:110

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[sys\_clock\_tick\_set](ztest__test_8h.md#a846fcbfbda9794cba2dcf1c34bd9be1b)

void sys\_clock\_tick\_set(uint64\_t tick)

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest\_test.h](ztest__test_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
