---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/regulator_8h_source.html
original_path: doxygen/html/regulator_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

19

20#include <[errno.h](errno_8h.md)>

21#include <[stdint.h](stdint_8h.md)>

22

23#include <[zephyr/device.h](device_8h.md)>

24#include <[zephyr/devicetree.h](devicetree_8h.md)>

25#ifdef CONFIG\_REGULATOR\_THREAD\_SAFE\_REFCNT

26#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

27#endif

28#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 35](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd);

36

[ 38](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03);

39

[ 41](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90);

42

48

[ 50](group__regulator__interface.md#ga5e17eb919086ea6e5239a240a6ac5aa1)#define REGULATOR\_ERROR\_OVER\_VOLTAGE BIT(0)

[ 52](group__regulator__interface.md#ga8705a7a63b8f187d66cda98d66372b5d)#define REGULATOR\_ERROR\_OVER\_CURRENT BIT(1)

[ 54](group__regulator__interface.md#ga9570dd992355afa6ecef9610c8c45eda)#define REGULATOR\_ERROR\_OVER\_TEMP BIT(2)

55

57

59

60typedef int (\*regulator\_dvs\_state\_set\_t)(const struct [device](structdevice.md) \*dev,

61 [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

62

63typedef int (\*regulator\_ship\_mode\_t)(const struct [device](structdevice.md) \*dev);

64

66\_\_subsystem struct regulator\_parent\_driver\_api {

67 regulator\_dvs\_state\_set\_t dvs\_state\_set;

68 regulator\_ship\_mode\_t ship\_mode;

69};

70

71typedef int (\*regulator\_enable\_t)(const struct [device](structdevice.md) \*dev);

72typedef int (\*regulator\_disable\_t)(const struct [device](structdevice.md) \*dev);

73typedef unsigned int (\*regulator\_count\_voltages\_t)(const struct [device](structdevice.md) \*dev);

74typedef int (\*regulator\_list\_voltage\_t)(const struct [device](structdevice.md) \*dev,

75 unsigned int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv);

76typedef int (\*regulator\_set\_voltage\_t)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv,

77 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv);

78typedef int (\*regulator\_get\_voltage\_t)(const struct [device](structdevice.md) \*dev,

79 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv);

80typedef unsigned int (\*regulator\_count\_current\_limits\_t)(const struct [device](structdevice.md) \*dev);

81typedef int (\*regulator\_list\_current\_limit\_t)(const struct [device](structdevice.md) \*dev,

82 unsigned int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*current\_ua);

83typedef int (\*regulator\_set\_current\_limit\_t)(const struct [device](structdevice.md) \*dev,

84 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_ua, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_ua);

85typedef int (\*regulator\_get\_current\_limit\_t)(const struct [device](structdevice.md) \*dev,

86 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*curr\_ua);

87typedef int (\*regulator\_set\_mode\_t)(const struct [device](structdevice.md) \*dev,

88 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) mode);

89typedef int (\*regulator\_get\_mode\_t)(const struct [device](structdevice.md) \*dev,

90 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*mode);

91typedef int (\*regulator\_set\_active\_discharge\_t)(const struct [device](structdevice.md) \*dev,

92 bool active\_discharge);

93typedef int (\*regulator\_get\_active\_discharge\_t)(const struct [device](structdevice.md) \*dev,

94 bool \*active\_discharge);

95typedef int (\*regulator\_get\_error\_flags\_t)(

96 const struct [device](structdevice.md) \*dev, [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

97

99\_\_subsystem struct regulator\_driver\_api {

100 regulator\_enable\_t enable;

101 regulator\_disable\_t disable;

102 regulator\_count\_voltages\_t count\_voltages;

103 regulator\_list\_voltage\_t list\_voltage;

104 regulator\_set\_voltage\_t set\_voltage;

105 regulator\_get\_voltage\_t get\_voltage;

106 regulator\_count\_current\_limits\_t count\_current\_limits;

107 regulator\_list\_current\_limit\_t list\_current\_limit;

108 regulator\_set\_current\_limit\_t set\_current\_limit;

109 regulator\_get\_current\_limit\_t get\_current\_limit;

110 regulator\_set\_mode\_t set\_mode;

111 regulator\_get\_mode\_t get\_mode;

112 regulator\_set\_active\_discharge\_t set\_active\_discharge;

113 regulator\_get\_active\_discharge\_t get\_active\_discharge;

114 regulator\_get\_error\_flags\_t get\_error\_flags;

115};

116

123#define REGULATOR\_ALWAYS\_ON BIT(0)

125#define REGULATOR\_BOOT\_ON BIT(1)

127#define REGULATOR\_INIT\_ENABLED (REGULATOR\_ALWAYS\_ON | REGULATOR\_BOOT\_ON)

129#define REGULATOR\_ACTIVE\_DISCHARGE\_MASK GENMASK(3, 2)

131#define REGULATOR\_ACTIVE\_DISCHARGE\_POS 2

133#define REGULATOR\_ACTIVE\_DISCHARGE\_DISABLE 0

135#define REGULATOR\_ACTIVE\_DISCHARGE\_ENABLE 1

137#define REGULATOR\_ACTIVE\_DISCHARGE\_DEFAULT 2

139#define REGULATOR\_ACTIVE\_DISCHARGE\_SET\_BITS(x) \

140 (((x) << REGULATOR\_ACTIVE\_DISCHARGE\_POS) & REGULATOR\_ACTIVE\_DISCHARGE\_MASK)

142#define REGULATOR\_ACTIVE\_DISCHARGE\_GET\_BITS(x) \

143 (((x) & REGULATOR\_ACTIVE\_DISCHARGE\_MASK) >> REGULATOR\_ACTIVE\_DISCHARGE\_POS)

144

146

148#define REGULATOR\_INITIAL\_MODE\_UNKNOWN UINT8\_MAX

149

155struct regulator\_common\_config {

157 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv;

159 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv;

161 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) init\_uv;

163 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_ua;

165 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_ua;

167 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) init\_ua;

169 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) startup\_delay\_us;

171 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) off\_on\_delay\_us;

173 const [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*allowed\_modes;

175 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) allowed\_modes\_cnt;

177 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) initial\_mode;

179 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

180};

181

187#define REGULATOR\_DT\_COMMON\_CONFIG\_INIT(node\_id) \

188 { \

189 .min\_uv = DT\_PROP\_OR(node\_id, regulator\_min\_microvolt, \

190 INT32\_MIN), \

191 .max\_uv = DT\_PROP\_OR(node\_id, regulator\_max\_microvolt, \

192 INT32\_MAX), \

193 .init\_uv = DT\_PROP\_OR(node\_id, regulator\_init\_microvolt, \

194 INT32\_MIN), \

195 .min\_ua = DT\_PROP\_OR(node\_id, regulator\_min\_microamp, \

196 INT32\_MIN), \

197 .max\_ua = DT\_PROP\_OR(node\_id, regulator\_max\_microamp, \

198 INT32\_MAX), \

199 .init\_ua = DT\_PROP\_OR(node\_id, regulator\_init\_microamp, \

200 INT32\_MIN), \

201 .startup\_delay\_us = DT\_PROP\_OR(node\_id, startup\_delay\_us, 0), \

202 .off\_on\_delay\_us = DT\_PROP\_OR(node\_id, off\_on\_delay\_us, 0), \

203 .allowed\_modes = (const regulator\_mode\_t []) \

204 DT\_PROP\_OR(node\_id, regulator\_allowed\_modes, {}), \

205 .allowed\_modes\_cnt = \

206 DT\_PROP\_LEN\_OR(node\_id, regulator\_allowed\_modes, 0), \

207 .initial\_mode = DT\_PROP\_OR(node\_id, regulator\_initial\_mode, \

208 REGULATOR\_INITIAL\_MODE\_UNKNOWN), \

209 .flags = ((DT\_PROP\_OR(node\_id, regulator\_always\_on, 0U) \* \

210 REGULATOR\_ALWAYS\_ON) | \

211 (DT\_PROP\_OR(node\_id, regulator\_boot\_on, 0U) \* \

212 REGULATOR\_BOOT\_ON) | \

213 (REGULATOR\_ACTIVE\_DISCHARGE\_SET\_BITS( \

214 DT\_PROP\_OR(node\_id, regulator\_active\_discharge, \

215 REGULATOR\_ACTIVE\_DISCHARGE\_DEFAULT)))), \

216 }

217

223#define REGULATOR\_DT\_INST\_COMMON\_CONFIG\_INIT(inst) \

224 REGULATOR\_DT\_COMMON\_CONFIG\_INIT(DT\_DRV\_INST(inst))

225

231struct regulator\_common\_data {

232#if defined(CONFIG\_REGULATOR\_THREAD\_SAFE\_REFCNT) || defined(\_\_DOXYGEN\_\_)

234 struct k\_mutex lock;

235#endif

237 int refcnt;

238};

239

247void regulator\_common\_data\_init(const struct [device](structdevice.md) \*dev);

248

270int regulator\_common\_init(const struct [device](structdevice.md) \*dev, bool is\_enabled);

271

279static inline bool regulator\_common\_is\_init\_enabled(const struct [device](structdevice.md) \*dev)

280{

281 const struct regulator\_common\_config \*config =

282 (const struct regulator\_common\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

283

284 return (config->flags & REGULATOR\_INIT\_ENABLED) != 0U;

285}

286

296static inline int regulator\_common\_get\_min\_voltage(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*min\_uv)

297{

298 const struct regulator\_common\_config \*config =

299 (const struct regulator\_common\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

300

301 if (config->min\_uv == [INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe)) {

302 return -[ENOENT](group__system__errno.md#ga03e689f378f643d16ea7537918528a48);

303 }

304

305 \*min\_uv = config->min\_uv;

306 return 0;

307}

308

310

316

[ 336](group__regulator__parent__interface.md#ga980feabe8415a9643eb66c8566d700bf)static inline int [regulator\_parent\_dvs\_state\_set](group__regulator__parent__interface.md#ga980feabe8415a9643eb66c8566d700bf)(const struct [device](structdevice.md) \*dev,

337 [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

338{

339 const struct regulator\_parent\_driver\_api \*api =

340 (const struct regulator\_parent\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

341

342 if (api->dvs\_state\_set == NULL) {

343 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

344 }

345

346 return api->dvs\_state\_set(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

347}

348

[ 363](group__regulator__parent__interface.md#gaa65d0a8d792256818a2ba06ad67a4f02)static inline int [regulator\_parent\_ship\_mode](group__regulator__parent__interface.md#gaa65d0a8d792256818a2ba06ad67a4f02)(const struct [device](structdevice.md) \*dev)

364{

365 const struct regulator\_parent\_driver\_api \*api =

366 (const struct regulator\_parent\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

367

368 if (api->ship\_mode == NULL) {

369 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

370 }

371

372 return api->ship\_mode(dev);

373}

374

376

[ 391](group__regulator__interface.md#ga06e3109b9607521fe07686c6d601e460)int [regulator\_enable](group__regulator__interface.md#ga06e3109b9607521fe07686c6d601e460)(const struct [device](structdevice.md) \*dev);

392

[ 401](group__regulator__interface.md#ga28744a6cabadfe5a22bc96792c8ad124)bool [regulator\_is\_enabled](group__regulator__interface.md#ga28744a6cabadfe5a22bc96792c8ad124)(const struct [device](structdevice.md) \*dev);

402

[ 419](group__regulator__interface.md#gaac417fbf6e30bbbfbd5ea5029a8ef298)int [regulator\_disable](group__regulator__interface.md#gaac417fbf6e30bbbfbd5ea5029a8ef298)(const struct [device](structdevice.md) \*dev);

420

[ 432](group__regulator__interface.md#ga96bf136ff2deca774931ca27300b03a6)static inline unsigned int [regulator\_count\_voltages](group__regulator__interface.md#ga96bf136ff2deca774931ca27300b03a6)(const struct [device](structdevice.md) \*dev)

433{

434 const struct regulator\_driver\_api \*api =

435 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

436

437 if (api->count\_voltages == NULL) {

438 return 0U;

439 }

440

441 return api->count\_voltages(dev);

442}

443

[ 459](group__regulator__interface.md#ga62d9ea1d7dc2987101cf31b324ca7c51)static inline int [regulator\_list\_voltage](group__regulator__interface.md#ga62d9ea1d7dc2987101cf31b324ca7c51)(const struct [device](structdevice.md) \*dev,

460 unsigned int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv)

461{

462 const struct regulator\_driver\_api \*api =

463 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

464

465 if (api->list\_voltage == NULL) {

466 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

467 }

468

469 return api->list\_voltage(dev, idx, volt\_uv);

470}

471

[ 482](group__regulator__interface.md#ga31b42ddfe94fee47158632f355ad864c)bool [regulator\_is\_supported\_voltage](group__regulator__interface.md#ga31b42ddfe94fee47158632f355ad864c)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv,

483 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv);

484

[ 503](group__regulator__interface.md#ga2c2b345da9029013edbf59fd8c565d85)int [regulator\_set\_voltage](group__regulator__interface.md#ga2c2b345da9029013edbf59fd8c565d85)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_uv,

504 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_uv);

505

[ 516](group__regulator__interface.md#gaa0114ee43a137ee98f98f5bce93d8579)static inline int [regulator\_get\_voltage](group__regulator__interface.md#gaa0114ee43a137ee98f98f5bce93d8579)(const struct [device](structdevice.md) \*dev,

517 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*volt\_uv)

518{

519 const struct regulator\_driver\_api \*api =

520 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

521

522 if (api->get\_voltage == NULL) {

523 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

524 }

525

526 return api->get\_voltage(dev, volt\_uv);

527}

528

[ 540](group__regulator__interface.md#ga27de51302b5222f860457c5b8bd494d6)static inline unsigned int [regulator\_count\_current\_limits](group__regulator__interface.md#ga27de51302b5222f860457c5b8bd494d6)(const struct [device](structdevice.md) \*dev)

541{

542 const struct regulator\_driver\_api \*api =

543 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

544

545 if (api->count\_current\_limits == NULL) {

546 return 0U;

547 }

548

549 return api->count\_current\_limits(dev);

550}

551

[ 567](group__regulator__interface.md#gaf12002954c6fc0ab9689f4dd2ec39518)static inline int [regulator\_list\_current\_limit](group__regulator__interface.md#gaf12002954c6fc0ab9689f4dd2ec39518)(const struct [device](structdevice.md) \*dev,

568 unsigned int idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*current\_ua)

569{

570 const struct regulator\_driver\_api \*api =

571 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

572

573 if (api->list\_current\_limit == NULL) {

574 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

575 }

576

577 return api->list\_current\_limit(dev, idx, current\_ua);

578}

579

[ 597](group__regulator__interface.md#ga2ccf66175b37754e2c21f341ecb2acbd)int [regulator\_set\_current\_limit](group__regulator__interface.md#ga2ccf66175b37754e2c21f341ecb2acbd)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) min\_ua,

598 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) max\_ua);

599

[ 610](group__regulator__interface.md#ga88c3ddeed962b5368713ad8fef0e7d7a)static inline int [regulator\_get\_current\_limit](group__regulator__interface.md#ga88c3ddeed962b5368713ad8fef0e7d7a)(const struct [device](structdevice.md) \*dev,

611 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*curr\_ua)

612{

613 const struct regulator\_driver\_api \*api =

614 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

615

616 if (api->get\_current\_limit == NULL) {

617 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

618 }

619

620 return api->get\_current\_limit(dev, curr\_ua);

621}

622

[ 639](group__regulator__interface.md#ga1877bac62c2b81ee37deb86bfae302af)int [regulator\_set\_mode](group__regulator__interface.md#ga1877bac62c2b81ee37deb86bfae302af)(const struct [device](structdevice.md) \*dev, [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) mode);

640

[ 651](group__regulator__interface.md#ga9bc0fc7ba4bd2ed2548bff25cf4badfe)static inline int [regulator\_get\_mode](group__regulator__interface.md#ga9bc0fc7ba4bd2ed2548bff25cf4badfe)(const struct [device](structdevice.md) \*dev,

652 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*mode)

653{

654 const struct regulator\_driver\_api \*api =

655 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

656

657 if (api->get\_mode == NULL) {

658 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

659 }

660

661 return api->get\_mode(dev, mode);

662}

663

[ 674](group__regulator__interface.md#ga8fb061502d0e94c4fe7a18c5a84d4af3)static inline int [regulator\_set\_active\_discharge](group__regulator__interface.md#ga8fb061502d0e94c4fe7a18c5a84d4af3)(const struct [device](structdevice.md) \*dev,

675 bool active\_discharge)

676{

677 const struct regulator\_driver\_api \*api =

678 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

679

680 if (api->set\_active\_discharge == NULL) {

681 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

682 }

683

684 return api->set\_active\_discharge(dev, active\_discharge);

685}

686

[ 697](group__regulator__interface.md#ga58d9e06c6da52a9733b3979d72915ab3)static inline int [regulator\_get\_active\_discharge](group__regulator__interface.md#ga58d9e06c6da52a9733b3979d72915ab3)(const struct [device](structdevice.md) \*dev,

698 bool \*active\_discharge)

699{

700 const struct regulator\_driver\_api \*api =

701 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

702

703 if (api->get\_active\_discharge == NULL) {

704 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

705 }

706

707 return api->get\_active\_discharge(dev, active\_discharge);

708}

709

[ 720](group__regulator__interface.md#ga9133662844a20eaf703d6d075347c62f)static inline int [regulator\_get\_error\_flags](group__regulator__interface.md#ga9133662844a20eaf703d6d075347c62f)(const struct [device](structdevice.md) \*dev,

721 [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

722{

723 const struct regulator\_driver\_api \*api =

724 (const struct regulator\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

725

726 if (api->get\_error\_flags == NULL) {

727 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

728 }

729

730 return api->get\_error\_flags(dev, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

731}

732

733#ifdef \_\_cplusplus

734}

735#endif

736

738

739#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_REGULATOR\_H\_ \*/

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

**Definition** regulator.h:38

[regulator\_count\_current\_limits](group__regulator__interface.md#ga27de51302b5222f860457c5b8bd494d6)

static unsigned int regulator\_count\_current\_limits(const struct device \*dev)

Obtain the number of supported current limit levels.

**Definition** regulator.h:540

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

**Definition** regulator.h:41

[regulator\_get\_active\_discharge](group__regulator__interface.md#ga58d9e06c6da52a9733b3979d72915ab3)

static int regulator\_get\_active\_discharge(const struct device \*dev, bool \*active\_discharge)

Get active discharge setting.

**Definition** regulator.h:697

[regulator\_list\_voltage](group__regulator__interface.md#ga62d9ea1d7dc2987101cf31b324ca7c51)

static int regulator\_list\_voltage(const struct device \*dev, unsigned int idx, int32\_t \*volt\_uv)

Obtain the value of a voltage given an index.

**Definition** regulator.h:459

[regulator\_get\_current\_limit](group__regulator__interface.md#ga88c3ddeed962b5368713ad8fef0e7d7a)

static int regulator\_get\_current\_limit(const struct device \*dev, int32\_t \*curr\_ua)

Get output current limit.

**Definition** regulator.h:610

[regulator\_set\_active\_discharge](group__regulator__interface.md#ga8fb061502d0e94c4fe7a18c5a84d4af3)

static int regulator\_set\_active\_discharge(const struct device \*dev, bool active\_discharge)

Set active discharge setting.

**Definition** regulator.h:674

[regulator\_get\_error\_flags](group__regulator__interface.md#ga9133662844a20eaf703d6d075347c62f)

static int regulator\_get\_error\_flags(const struct device \*dev, regulator\_error\_flags\_t \*flags)

Get active error flags.

**Definition** regulator.h:720

[regulator\_count\_voltages](group__regulator__interface.md#ga96bf136ff2deca774931ca27300b03a6)

static unsigned int regulator\_count\_voltages(const struct device \*dev)

Obtain the number of supported voltage levels.

**Definition** regulator.h:432

[regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd)

uint8\_t regulator\_dvs\_state\_t

Opaque type to store regulator DVS states.

**Definition** regulator.h:35

[regulator\_get\_mode](group__regulator__interface.md#ga9bc0fc7ba4bd2ed2548bff25cf4badfe)

static int regulator\_get\_mode(const struct device \*dev, regulator\_mode\_t \*mode)

Get mode.

**Definition** regulator.h:651

[regulator\_get\_voltage](group__regulator__interface.md#gaa0114ee43a137ee98f98f5bce93d8579)

static int regulator\_get\_voltage(const struct device \*dev, int32\_t \*volt\_uv)

Obtain output voltage.

**Definition** regulator.h:516

[regulator\_disable](group__regulator__interface.md#gaac417fbf6e30bbbfbd5ea5029a8ef298)

int regulator\_disable(const struct device \*dev)

Disable a regulator.

[regulator\_list\_current\_limit](group__regulator__interface.md#gaf12002954c6fc0ab9689f4dd2ec39518)

static int regulator\_list\_current\_limit(const struct device \*dev, unsigned int idx, int32\_t \*current\_ua)

Obtain the value of a current limit given an index.

**Definition** regulator.h:567

[regulator\_parent\_dvs\_state\_set](group__regulator__parent__interface.md#ga980feabe8415a9643eb66c8566d700bf)

static int regulator\_parent\_dvs\_state\_set(const struct device \*dev, regulator\_dvs\_state\_t state)

Set a DVS state.

**Definition** regulator.h:336

[regulator\_parent\_ship\_mode](group__regulator__parent__interface.md#gaa65d0a8d792256818a2ba06ad67a4f02)

static int regulator\_parent\_ship\_mode(const struct device \*dev)

Enter ship mode.

**Definition** regulator.h:363

[ENOENT](group__system__errno.md#ga03e689f378f643d16ea7537918528a48)

#define ENOENT

No such file or directory.

**Definition** errno.h:41

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[kernel.h](include_2zephyr_2kernel_8h.md)

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

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe)

#define INT32\_MIN

**Definition** stdint.h:24

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:391

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [regulator.h](regulator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
