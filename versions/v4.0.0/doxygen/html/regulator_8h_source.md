---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/regulator_8h_source.html
original_path: doxygen/html/regulator_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

regulator.h

[Go to the documentation of this file.](regulator_8h.md)

1/\*

2 \* Copyright (c) 2019-2020 Peter Bigot Consulting, LLC

3 \* Copyright (c) 2021 NXP

4 \* Copyright (c) 2022 Nordic Semiconductor ASA

5 \* Copyright (c) 2023 EPAM Systems

6 \* Copyright (c) 2023 Meta Platforms

7 \* SPDX-License-Identifier: Apache-2.0

8 \*/

9

10#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_REGULATOR\_H\_

11#define ZEPHYR\_INCLUDE\_DRIVERS\_REGULATOR\_H\_

12

21

22#include <[errno.h](errno_8h.md)>

23#include <[stdint.h](stdint_8h.md)>

24

25#include <[zephyr/device.h](device_8h.md)>

26#include <[zephyr/devicetree.h](devicetree_8h.md)>

27#ifdef CONFIG\_REGULATOR\_THREAD\_SAFE\_REFCNT

28#include <[zephyr/kernel.h](kernel_8h.md)>

29#endif

30#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 37](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd);

38

[ 40](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03);

41

[ 43](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90);

44

50

[ 52](group__regulator__interface.md#ga5e17eb919086ea6e5239a240a6ac5aa1)#define REGULATOR\_ERROR\_OVER\_VOLTAGE BIT(0)

[ 54](group__regulator__interface.md#ga8705a7a63b8f187d66cda98d66372b5d)#define REGULATOR\_ERROR\_OVER\_CURRENT BIT(1)

[ 56](group__regulator__interface.md#ga9570dd992355afa6ecef9610c8c45eda)#define REGULATOR\_ERROR\_OVER\_TEMP BIT(2)

57

59

61

62typedef int (\*regulator\_dvs\_state\_set\_t)(const struct [device](structdevice.md) \*dev,

63 [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

64

65typedef int (\*regulator\_ship\_mode\_t)(const struct [device](structdevice.md) \*dev);

66

68\_\_subsystem struct regulator\_parent\_driver\_api {

69 regulator\_dvs\_state\_set\_t dvs\_state\_set;

70 regulator\_ship\_mode\_t ship\_mode;

71};

72

73typedef int (\*regulator\_enable\_t)(const struct [device](structdevice.md) \*dev);

74typedef int (\*regulator\_disable\_t)(const struct [device](structdevice.md) \*dev);

75typedef unsigned int (\*regulator\_count\_voltages\_t)(const struct [device](structdevice.md) \*dev);

76typedef int (\*regulator\_list\_voltage\_t)(const struct [device](structdevice.md) \*dev,

77 unsigned int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv);

78typedef int (\*regulator\_set\_voltage\_t)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv,

79 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv);

80typedef int (\*regulator\_get\_voltage\_t)(const struct [device](structdevice.md) \*dev,

81 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv);

82typedef unsigned int (\*regulator\_count\_current\_limits\_t)(const struct [device](structdevice.md) \*dev);

83typedef int (\*regulator\_list\_current\_limit\_t)(const struct [device](structdevice.md) \*dev,

84 unsigned int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*current\_ua);

85typedef int (\*regulator\_set\_current\_limit\_t)(const struct [device](structdevice.md) \*dev,

86 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_ua, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_ua);

87typedef int (\*regulator\_get\_current\_limit\_t)(const struct [device](structdevice.md) \*dev,

88 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*curr\_ua);

89typedef int (\*regulator\_set\_mode\_t)(const struct [device](structdevice.md) \*dev,

90 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) mode);

91typedef int (\*regulator\_get\_mode\_t)(const struct [device](structdevice.md) \*dev,

92 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*mode);

93typedef int (\*regulator\_set\_active\_discharge\_t)(const struct [device](structdevice.md) \*dev,

94 bool active\_discharge);

95typedef int (\*regulator\_get\_active\_discharge\_t)(const struct [device](structdevice.md) \*dev,

96 bool \*active\_discharge);

97typedef int (\*regulator\_get\_error\_flags\_t)(

98 const struct [device](structdevice.md) \*dev, [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

99

101\_\_subsystem struct regulator\_driver\_api {

102 regulator\_enable\_t enable;

103 regulator\_disable\_t disable;

104 regulator\_count\_voltages\_t count\_voltages;

105 regulator\_list\_voltage\_t list\_voltage;

106 regulator\_set\_voltage\_t set\_voltage;

107 regulator\_get\_voltage\_t get\_voltage;

108 regulator\_count\_current\_limits\_t count\_current\_limits;

109 regulator\_list\_current\_limit\_t list\_current\_limit;

110 regulator\_set\_current\_limit\_t set\_current\_limit;

111 regulator\_get\_current\_limit\_t get\_current\_limit;

112 regulator\_set\_mode\_t set\_mode;

113 regulator\_get\_mode\_t get\_mode;

114 regulator\_set\_active\_discharge\_t set\_active\_discharge;

115 regulator\_get\_active\_discharge\_t get\_active\_discharge;

116 regulator\_get\_error\_flags\_t get\_error\_flags;

117};

118

125#define REGULATOR\_ALWAYS\_ON BIT(0)

127#define REGULATOR\_BOOT\_ON BIT(1)

129#define REGULATOR\_INIT\_ENABLED (REGULATOR\_ALWAYS\_ON | REGULATOR\_BOOT\_ON)

131#define REGULATOR\_ACTIVE\_DISCHARGE\_MASK GENMASK(3, 2)

133#define REGULATOR\_ACTIVE\_DISCHARGE\_POS 2

135#define REGULATOR\_ACTIVE\_DISCHARGE\_DISABLE 0

137#define REGULATOR\_ACTIVE\_DISCHARGE\_ENABLE 1

139#define REGULATOR\_ACTIVE\_DISCHARGE\_DEFAULT 2

141#define REGULATOR\_ACTIVE\_DISCHARGE\_SET\_BITS(x) \

142 (((x) << REGULATOR\_ACTIVE\_DISCHARGE\_POS) & REGULATOR\_ACTIVE\_DISCHARGE\_MASK)

144#define REGULATOR\_ACTIVE\_DISCHARGE\_GET\_BITS(x) \

145 (((x) & REGULATOR\_ACTIVE\_DISCHARGE\_MASK) >> REGULATOR\_ACTIVE\_DISCHARGE\_POS)

147#define REGULATOR\_BOOT\_OFF BIT(4)

148

150

152#define REGULATOR\_INITIAL\_MODE\_UNKNOWN UINT8\_MAX

153

159struct regulator\_common\_config {

161 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv;

163 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv;

165 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) init\_uv;

167 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_ua;

169 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_ua;

171 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) init\_ua;

173 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) startup\_delay\_us;

175 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) off\_on\_delay\_us;

177 const [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*allowed\_modes;

179 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) allowed\_modes\_cnt;

181 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) initial\_mode;

183 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

184};

185

191#define REGULATOR\_DT\_COMMON\_CONFIG\_INIT(node\_id) \

192 { \

193 .min\_uv = DT\_PROP\_OR(node\_id, regulator\_min\_microvolt, \

194 INT32\_MIN), \

195 .max\_uv = DT\_PROP\_OR(node\_id, regulator\_max\_microvolt, \

196 INT32\_MAX), \

197 .init\_uv = DT\_PROP\_OR(node\_id, regulator\_init\_microvolt, \

198 INT32\_MIN), \

199 .min\_ua = DT\_PROP\_OR(node\_id, regulator\_min\_microamp, \

200 INT32\_MIN), \

201 .max\_ua = DT\_PROP\_OR(node\_id, regulator\_max\_microamp, \

202 INT32\_MAX), \

203 .init\_ua = DT\_PROP\_OR(node\_id, regulator\_init\_microamp, \

204 INT32\_MIN), \

205 .startup\_delay\_us = DT\_PROP\_OR(node\_id, startup\_delay\_us, 0), \

206 .off\_on\_delay\_us = DT\_PROP\_OR(node\_id, off\_on\_delay\_us, 0), \

207 .allowed\_modes = (const regulator\_mode\_t []) \

208 DT\_PROP\_OR(node\_id, regulator\_allowed\_modes, {}), \

209 .allowed\_modes\_cnt = \

210 DT\_PROP\_LEN\_OR(node\_id, regulator\_allowed\_modes, 0), \

211 .initial\_mode = DT\_PROP\_OR(node\_id, regulator\_initial\_mode, \

212 REGULATOR\_INITIAL\_MODE\_UNKNOWN), \

213 .flags = ((DT\_PROP\_OR(node\_id, regulator\_always\_on, 0U) \* \

214 REGULATOR\_ALWAYS\_ON) | \

215 (DT\_PROP\_OR(node\_id, regulator\_boot\_on, 0U) \* \

216 REGULATOR\_BOOT\_ON) | \

217 (REGULATOR\_ACTIVE\_DISCHARGE\_SET\_BITS( \

218 DT\_PROP\_OR(node\_id, regulator\_active\_discharge, \

219 REGULATOR\_ACTIVE\_DISCHARGE\_DEFAULT))) | \

220 (DT\_PROP\_OR(node\_id, regulator\_boot\_off, 0U) \* \

221 REGULATOR\_BOOT\_OFF)), \

222 }

223

229#define REGULATOR\_DT\_INST\_COMMON\_CONFIG\_INIT(inst) \

230 REGULATOR\_DT\_COMMON\_CONFIG\_INIT(DT\_DRV\_INST(inst))

231

237struct regulator\_common\_data {

238#if defined(CONFIG\_REGULATOR\_THREAD\_SAFE\_REFCNT) || defined(\_\_DOXYGEN\_\_)

240 struct k\_mutex lock;

241#endif

243 int refcnt;

244};

245

253void regulator\_common\_data\_init(const struct [device](structdevice.md) \*dev);

254

277int regulator\_common\_init(const struct [device](structdevice.md) \*dev, bool is\_enabled);

278

286static inline bool regulator\_common\_is\_init\_enabled(const struct [device](structdevice.md) \*dev)

287{

288 const struct regulator\_common\_config \*config =

289 (const struct regulator\_common\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

290

291 return (config->flags & REGULATOR\_INIT\_ENABLED) != 0U;

292}

293

303static inline int regulator\_common\_get\_min\_voltage(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*min\_uv)

304{

305 const struct regulator\_common\_config \*config =

306 (const struct regulator\_common\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

307

308 if (config->min\_uv == [INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe)) {

309 return -[ENOENT](group__system__errno.md#ga03e689f378f643d16ea7537918528a48);

310 }

311

312 \*min\_uv = config->min\_uv;

313 return 0;

314}

315

325static inline int regulator\_common\_get\_max\_voltage(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*max\_uv)

326{

327 const struct regulator\_common\_config \*config =

328 (const struct regulator\_common\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

329

330 if (config->max\_uv == [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) {

331 return -[ENOENT](group__system__errno.md#ga03e689f378f643d16ea7537918528a48);

332 }

333

334 \*max\_uv = config->max\_uv;

335 return 0;

336}

337

339

345

[ 365](group__regulator__parent__interface.md#ga980feabe8415a9643eb66c8566d700bf)static inline int [regulator\_parent\_dvs\_state\_set](group__regulator__parent__interface.md#ga980feabe8415a9643eb66c8566d700bf)(const struct [device](structdevice.md) \*dev,

366 [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

367{

368 const struct regulator\_parent\_driver\_api \*api =

369 (const struct regulator\_parent\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

370

371 if (api->dvs\_state\_set == NULL) {

372 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

373 }

374

375 return api->dvs\_state\_set(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

376}

377

[ 392](group__regulator__parent__interface.md#gaa65d0a8d792256818a2ba06ad67a4f02)static inline int [regulator\_parent\_ship\_mode](group__regulator__parent__interface.md#gaa65d0a8d792256818a2ba06ad67a4f02)(const struct [device](structdevice.md) \*dev)

393{

394 const struct regulator\_parent\_driver\_api \*api =

395 (const struct regulator\_parent\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

396

397 if (api->ship\_mode == NULL) {

398 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

399 }

400

401 return api->ship\_mode(dev);

402}

403

405

[ 420](group__regulator__interface.md#ga06e3109b9607521fe07686c6d601e460)int [regulator\_enable](group__regulator__interface.md#ga06e3109b9607521fe07686c6d601e460)(const struct [device](structdevice.md) \*dev);

421

[ 430](group__regulator__interface.md#ga28744a6cabadfe5a22bc96792c8ad124)bool [regulator\_is\_enabled](group__regulator__interface.md#ga28744a6cabadfe5a22bc96792c8ad124)(const struct [device](structdevice.md) \*dev);

431

[ 448](group__regulator__interface.md#gaac417fbf6e30bbbfbd5ea5029a8ef298)int [regulator\_disable](group__regulator__interface.md#gaac417fbf6e30bbbfbd5ea5029a8ef298)(const struct [device](structdevice.md) \*dev);

449

[ 461](group__regulator__interface.md#ga96bf136ff2deca774931ca27300b03a6)static inline unsigned int [regulator\_count\_voltages](group__regulator__interface.md#ga96bf136ff2deca774931ca27300b03a6)(const struct [device](structdevice.md) \*dev)

462{

463 const struct regulator\_driver\_api \*api =

464 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

465

466 if (api->count\_voltages == NULL) {

467 return 0U;

468 }

469

470 return api->count\_voltages(dev);

471}

472

[ 488](group__regulator__interface.md#ga62d9ea1d7dc2987101cf31b324ca7c51)static inline int [regulator\_list\_voltage](group__regulator__interface.md#ga62d9ea1d7dc2987101cf31b324ca7c51)(const struct [device](structdevice.md) \*dev,

489 unsigned int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv)

490{

491 const struct regulator\_driver\_api \*api =

492 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

493

494 if (api->list\_voltage == NULL) {

495 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

496 }

497

498 return api->list\_voltage(dev, idx, volt\_uv);

499}

500

[ 511](group__regulator__interface.md#ga31b42ddfe94fee47158632f355ad864c)bool [regulator\_is\_supported\_voltage](group__regulator__interface.md#ga31b42ddfe94fee47158632f355ad864c)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv,

512 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv);

513

[ 532](group__regulator__interface.md#ga2c2b345da9029013edbf59fd8c565d85)int [regulator\_set\_voltage](group__regulator__interface.md#ga2c2b345da9029013edbf59fd8c565d85)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv,

533 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv);

534

[ 545](group__regulator__interface.md#gaa0114ee43a137ee98f98f5bce93d8579)static inline int [regulator\_get\_voltage](group__regulator__interface.md#gaa0114ee43a137ee98f98f5bce93d8579)(const struct [device](structdevice.md) \*dev,

546 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv)

547{

548 const struct regulator\_driver\_api \*api =

549 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

550

551 if (api->get\_voltage == NULL) {

552 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

553 }

554

555 return api->get\_voltage(dev, volt\_uv);

556}

557

[ 569](group__regulator__interface.md#ga27de51302b5222f860457c5b8bd494d6)static inline unsigned int [regulator\_count\_current\_limits](group__regulator__interface.md#ga27de51302b5222f860457c5b8bd494d6)(const struct [device](structdevice.md) \*dev)

570{

571 const struct regulator\_driver\_api \*api =

572 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

573

574 if (api->count\_current\_limits == NULL) {

575 return 0U;

576 }

577

578 return api->count\_current\_limits(dev);

579}

580

[ 596](group__regulator__interface.md#gaf12002954c6fc0ab9689f4dd2ec39518)static inline int [regulator\_list\_current\_limit](group__regulator__interface.md#gaf12002954c6fc0ab9689f4dd2ec39518)(const struct [device](structdevice.md) \*dev,

597 unsigned int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*current\_ua)

598{

599 const struct regulator\_driver\_api \*api =

600 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

601

602 if (api->list\_current\_limit == NULL) {

603 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

604 }

605

606 return api->list\_current\_limit(dev, idx, current\_ua);

607}

608

[ 626](group__regulator__interface.md#ga2ccf66175b37754e2c21f341ecb2acbd)int [regulator\_set\_current\_limit](group__regulator__interface.md#ga2ccf66175b37754e2c21f341ecb2acbd)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_ua,

627 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_ua);

628

[ 639](group__regulator__interface.md#ga88c3ddeed962b5368713ad8fef0e7d7a)static inline int [regulator\_get\_current\_limit](group__regulator__interface.md#ga88c3ddeed962b5368713ad8fef0e7d7a)(const struct [device](structdevice.md) \*dev,

640 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*curr\_ua)

641{

642 const struct regulator\_driver\_api \*api =

643 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

644

645 if (api->get\_current\_limit == NULL) {

646 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

647 }

648

649 return api->get\_current\_limit(dev, curr\_ua);

650}

651

[ 668](group__regulator__interface.md#ga1877bac62c2b81ee37deb86bfae302af)int [regulator\_set\_mode](group__regulator__interface.md#ga1877bac62c2b81ee37deb86bfae302af)(const struct [device](structdevice.md) \*dev, [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) mode);

669

[ 680](group__regulator__interface.md#ga9bc0fc7ba4bd2ed2548bff25cf4badfe)static inline int [regulator\_get\_mode](group__regulator__interface.md#ga9bc0fc7ba4bd2ed2548bff25cf4badfe)(const struct [device](structdevice.md) \*dev,

681 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*mode)

682{

683 const struct regulator\_driver\_api \*api =

684 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

685

686 if (api->get\_mode == NULL) {

687 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

688 }

689

690 return api->get\_mode(dev, mode);

691}

692

[ 703](group__regulator__interface.md#ga8fb061502d0e94c4fe7a18c5a84d4af3)static inline int [regulator\_set\_active\_discharge](group__regulator__interface.md#ga8fb061502d0e94c4fe7a18c5a84d4af3)(const struct [device](structdevice.md) \*dev,

704 bool active\_discharge)

705{

706 const struct regulator\_driver\_api \*api =

707 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

708

709 if (api->set\_active\_discharge == NULL) {

710 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

711 }

712

713 return api->set\_active\_discharge(dev, active\_discharge);

714}

715

[ 726](group__regulator__interface.md#ga58d9e06c6da52a9733b3979d72915ab3)static inline int [regulator\_get\_active\_discharge](group__regulator__interface.md#ga58d9e06c6da52a9733b3979d72915ab3)(const struct [device](structdevice.md) \*dev,

727 bool \*active\_discharge)

728{

729 const struct regulator\_driver\_api \*api =

730 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

731

732 if (api->get\_active\_discharge == NULL) {

733 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

734 }

735

736 return api->get\_active\_discharge(dev, active\_discharge);

737}

738

[ 749](group__regulator__interface.md#ga9133662844a20eaf703d6d075347c62f)static inline int [regulator\_get\_error\_flags](group__regulator__interface.md#ga9133662844a20eaf703d6d075347c62f)(const struct [device](structdevice.md) \*dev,

750 [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

751{

752 const struct regulator\_driver\_api \*api =

753 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

754

755 if (api->get\_error\_flags == NULL) {

756 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

757 }

758

759 return api->get\_error\_flags(dev, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

760}

761

762#ifdef \_\_cplusplus

763}

764#endif

765

767

768#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_REGULATOR\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[errno.h](errno_8h.md)

System error numbers.

[regulator\_enable](group__regulator__interface.md#ga06e3109b9607521fe07686c6d601e460)

int regulator\_enable(const struct device \*dev)

Enable a regulator.

[regulator\_set\_mode](group__regulator__interface.md#ga1877bac62c2b81ee37deb86bfae302af)

int regulator\_set\_mode(const struct device \*dev, regulator\_mode\_t mode)

Set mode.

[regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03)

uint8\_t regulator\_mode\_t

Opaque type to store regulator modes.

**Definition** regulator.h:40

[regulator\_count\_current\_limits](group__regulator__interface.md#ga27de51302b5222f860457c5b8bd494d6)

static unsigned int regulator\_count\_current\_limits(const struct device \*dev)

Obtain the number of supported current limit levels.

**Definition** regulator.h:569

[regulator\_is\_enabled](group__regulator__interface.md#ga28744a6cabadfe5a22bc96792c8ad124)

bool regulator\_is\_enabled(const struct device \*dev)

Check if a regulator is enabled.

[regulator\_set\_voltage](group__regulator__interface.md#ga2c2b345da9029013edbf59fd8c565d85)

int regulator\_set\_voltage(const struct device \*dev, int32\_t min\_uv, int32\_t max\_uv)

Set the output voltage.

[regulator\_set\_current\_limit](group__regulator__interface.md#ga2ccf66175b37754e2c21f341ecb2acbd)

int regulator\_set\_current\_limit(const struct device \*dev, int32\_t min\_ua, int32\_t max\_ua)

Set output current limit.

[regulator\_is\_supported\_voltage](group__regulator__interface.md#ga31b42ddfe94fee47158632f355ad864c)

bool regulator\_is\_supported\_voltage(const struct device \*dev, int32\_t min\_uv, int32\_t max\_uv)

Check if a voltage within a window is supported.

[regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90)

uint8\_t regulator\_error\_flags\_t

Opaque bit map for regulator error flags (see REGULATOR\_ERRORS).

**Definition** regulator.h:43

[regulator\_get\_active\_discharge](group__regulator__interface.md#ga58d9e06c6da52a9733b3979d72915ab3)

static int regulator\_get\_active\_discharge(const struct device \*dev, bool \*active\_discharge)

Get active discharge setting.

**Definition** regulator.h:726

[regulator\_list\_voltage](group__regulator__interface.md#ga62d9ea1d7dc2987101cf31b324ca7c51)

static int regulator\_list\_voltage(const struct device \*dev, unsigned int idx, int32\_t \*volt\_uv)

Obtain the value of a voltage given an index.

**Definition** regulator.h:488

[regulator\_get\_current\_limit](group__regulator__interface.md#ga88c3ddeed962b5368713ad8fef0e7d7a)

static int regulator\_get\_current\_limit(const struct device \*dev, int32\_t \*curr\_ua)

Get output current limit.

**Definition** regulator.h:639

[regulator\_set\_active\_discharge](group__regulator__interface.md#ga8fb061502d0e94c4fe7a18c5a84d4af3)

static int regulator\_set\_active\_discharge(const struct device \*dev, bool active\_discharge)

Set active discharge setting.

**Definition** regulator.h:703

[regulator\_get\_error\_flags](group__regulator__interface.md#ga9133662844a20eaf703d6d075347c62f)

static int regulator\_get\_error\_flags(const struct device \*dev, regulator\_error\_flags\_t \*flags)

Get active error flags.

**Definition** regulator.h:749

[regulator\_count\_voltages](group__regulator__interface.md#ga96bf136ff2deca774931ca27300b03a6)

static unsigned int regulator\_count\_voltages(const struct device \*dev)

Obtain the number of supported voltage levels.

**Definition** regulator.h:461

[regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd)

uint8\_t regulator\_dvs\_state\_t

Opaque type to store regulator DVS states.

**Definition** regulator.h:37

[regulator\_get\_mode](group__regulator__interface.md#ga9bc0fc7ba4bd2ed2548bff25cf4badfe)

static int regulator\_get\_mode(const struct device \*dev, regulator\_mode\_t \*mode)

Get mode.

**Definition** regulator.h:680

[regulator\_get\_voltage](group__regulator__interface.md#gaa0114ee43a137ee98f98f5bce93d8579)

static int regulator\_get\_voltage(const struct device \*dev, int32\_t \*volt\_uv)

Obtain output voltage.

**Definition** regulator.h:545

[regulator\_disable](group__regulator__interface.md#gaac417fbf6e30bbbfbd5ea5029a8ef298)

int regulator\_disable(const struct device \*dev)

Disable a regulator.

[regulator\_list\_current\_limit](group__regulator__interface.md#gaf12002954c6fc0ab9689f4dd2ec39518)

static int regulator\_list\_current\_limit(const struct device \*dev, unsigned int idx, int32\_t \*current\_ua)

Obtain the value of a current limit given an index.

**Definition** regulator.h:596

[regulator\_parent\_dvs\_state\_set](group__regulator__parent__interface.md#ga980feabe8415a9643eb66c8566d700bf)

static int regulator\_parent\_dvs\_state\_set(const struct device \*dev, regulator\_dvs\_state\_t state)

Set a DVS state.

**Definition** regulator.h:365

[regulator\_parent\_ship\_mode](group__regulator__parent__interface.md#gaa65d0a8d792256818a2ba06ad67a4f02)

static int regulator\_parent\_ship\_mode(const struct device \*dev)

Enter ship mode.

**Definition** regulator.h:392

[ENOENT](group__system__errno.md#ga03e689f378f643d16ea7537918528a48)

#define ENOENT

No such file or directory.

**Definition** errno.h:40

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[kernel.h](kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)

#define INT32\_MAX

**Definition** stdint.h:18

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe)

#define INT32\_MIN

**Definition** stdint.h:24

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:416

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [regulator.h](regulator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
