---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2can_8h_source.html
original_path: doxygen/html/drivers_2can_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can.h

[Go to the documentation of this file.](drivers_2can_8h.md)

1/\*

2 \* Copyright (c) 2021 Vestas Wind Systems A/S

3 \* Copyright (c) 2018 Karsten Koenig

4 \* Copyright (c) 2018 Alexander Wachter

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_H\_

16

17#include <[errno.h](errno_8h.md)>

18

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <[zephyr/device.h](device_8h.md)>

21#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

22#include <[string.h](string_8h.md)>

23#include <[zephyr/sys\_clock.h](include_2zephyr_2sys__clock_8h.md)>

24#include <[zephyr/sys/util.h](util_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

36

41

[ 45](group__can__interface.md#ga4cd8ce34887b90baeeaa6a4aa048b398)#define CAN\_STD\_ID\_MASK 0x7FFU

[ 49](group__can__interface.md#ga7987c1d4089742f87a7ac611add1a286)#define CAN\_MAX\_STD\_ID CAN\_STD\_ID\_MASK

[ 53](group__can__interface.md#ga15ee71e8abcf51008925585049125986)#define CAN\_EXT\_ID\_MASK 0x1FFFFFFFU

[ 57](group__can__interface.md#ga0f3572940065f8f6d54099e7a4175f8f)#define CAN\_MAX\_EXT\_ID CAN\_EXT\_ID\_MASK

[ 61](group__can__interface.md#gadc209a027ee700faf10461e2417bee50)#define CAN\_MAX\_DLC 8U

[ 65](group__can__interface.md#gad4b7310536c7e3252c2056abe64c0333)#define CANFD\_MAX\_DLC 15U

66

71#ifndef CONFIG\_CAN\_FD\_MODE

72#define CAN\_MAX\_DLEN 8U

73#else

74#define CAN\_MAX\_DLEN 64U

75#endif /\* CONFIG\_CAN\_FD\_MODE \*/

76

78

80

87

[ 89](group__can__interface.md#ga89cd5ea2e9d70a51bc12b100be28ca3d)#define CAN\_MODE\_NORMAL 0

90

[ 92](group__can__interface.md#ga891031afc77974a041accb3d0ceb21bb)#define CAN\_MODE\_LOOPBACK BIT(0)

93

[ 95](group__can__interface.md#ga117d04b9118a1b3f839c557ef6b596cb)#define CAN\_MODE\_LISTENONLY BIT(1)

96

[ 98](group__can__interface.md#gabb4d99736d8386a5ab62a5e44374d13a)#define CAN\_MODE\_FD BIT(2)

99

[ 101](group__can__interface.md#ga033d7ade1966299c7e6249b945f38202)#define CAN\_MODE\_ONE\_SHOT BIT(3)

102

[ 104](group__can__interface.md#gaf0821983174ad781e1bb63a976a18fab)#define CAN\_MODE\_3\_SAMPLES BIT(4)

105

107

[ 116](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7);

117

[ 121](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7)enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) {

[ 123](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c) [CAN\_STATE\_ERROR\_ACTIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c),

[ 125](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff) [CAN\_STATE\_ERROR\_WARNING](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff),

[ 127](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae) [CAN\_STATE\_ERROR\_PASSIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae),

[ 129](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959) [CAN\_STATE\_BUS\_OFF](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959),

[ 131](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8) [CAN\_STATE\_STOPPED](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8),

132};

133

140

[ 142](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)#define CAN\_FRAME\_IDE BIT(0)

143

[ 145](group__can__interface.md#gaed376ef16b84cd1974255fbb26dc3d7f)#define CAN\_FRAME\_RTR BIT(1)

146

[ 148](group__can__interface.md#ga22f85e1d16b93e46200f9673abdbb589)#define CAN\_FRAME\_FDF BIT(2)

149

[ 151](group__can__interface.md#ga1fdf15ce4a3b333488f9b630ec836d52)#define CAN\_FRAME\_BRS BIT(3)

152

[ 156](group__can__interface.md#ga83f8b7af6eb45e43aaac355de3e69e52)#define CAN\_FRAME\_ESI BIT(4)

157

159

[ 163](structcan__frame.md)struct [can\_frame](structcan__frame.md) {

[ 165](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d) : 29;

167 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) res0 : 3; /\* reserved/padding. \*/

[ 170](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47);

[ 172](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c);

173#if defined(CONFIG\_CAN\_RX\_TIMESTAMP) || defined(\_\_DOXYGEN\_\_)

[ 181](structcan__frame.md#ae46f8b0821c638517959274bbbda5932) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timestamp](structcan__frame.md#ae46f8b0821c638517959274bbbda5932);

182#else

184 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res1; /\* reserved/padding. \*/

186#endif

188 union {

[ 190](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)[CAN\_MAX\_DLEN];

[ 192](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_32](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a)[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(CAN\_MAX\_DLEN, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)))];

193 };

194};

195

202

[ 204](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)#define CAN\_FILTER\_IDE BIT(0)

205

206

208

[ 212](structcan__filter.md)struct [can\_filter](structcan__filter.md) {

[ 214](structcan__filter.md#adf2b18eab11d360780707478a1f624b9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9) : 29;

216 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) res0 : 3;

[ 221](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94) : 29;

[ 223](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de);

224};

225

[ 229](structcan__bus__err__cnt.md)struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) {

[ 231](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_err\_cnt](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98);

[ 233](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_err\_cnt](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a);

234};

235

[ 268](structcan__timing.md)struct [can\_timing](structcan__timing.md) {

[ 270](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sjw](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5);

[ 272](structcan__timing.md#ac009d40fee9788b663963978498b2ee9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [prop\_seg](structcan__timing.md#ac009d40fee9788b663963978498b2ee9);

[ 274](structcan__timing.md#a9941688e79fa4ce01c4b498433319089) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phase\_seg1](structcan__timing.md#a9941688e79fa4ce01c4b498433319089);

[ 276](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phase\_seg2](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6);

[ 278](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [prescaler](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a);

279};

280

[ 289](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)typedef void (\*[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca))(const struct [device](structdevice.md) \*dev, int error, void \*user\_data);

290

[ 298](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)typedef void (\*[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f))(const struct [device](structdevice.md) \*dev, struct [can\_frame](structcan__frame.md) \*frame,

299 void \*user\_data);

300

[ 309](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)typedef void (\*[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d))(const struct [device](structdevice.md) \*dev,

310 enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

311 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) err\_cnt,

312 void \*user\_data);

313

319

326struct can\_driver\_config {

328 const struct [device](structdevice.md) \*phy;

330 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_bitrate;

332 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bus\_speed;

334 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_point;

335#ifdef CONFIG\_CAN\_FD\_MODE

337 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_point\_data;

339 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bus\_speed\_data;

340#endif /\* CONFIG\_CAN\_FD\_MODE \*/

341};

342

349#define CAN\_DT\_DRIVER\_CONFIG\_GET(node\_id, \_max\_bitrate) \

350 { \

351 .phy = DEVICE\_DT\_GET\_OR\_NULL(DT\_PHANDLE(node\_id, phys)), \

352 .max\_bitrate = DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE(node\_id, \_max\_bitrate), \

353 .bus\_speed = DT\_PROP(node\_id, bus\_speed), \

354 .sample\_point = DT\_PROP\_OR(node\_id, sample\_point, 0), \

355 IF\_ENABLED(CONFIG\_CAN\_FD\_MODE, \

356 (.bus\_speed\_data = DT\_PROP\_OR(node\_id, bus\_speed\_data, 0), \

357 .sample\_point\_data = DT\_PROP\_OR(node\_id, sample\_point\_data, 0),)) \

358 }

359

367#define CAN\_DT\_DRIVER\_CONFIG\_INST\_GET(inst, \_max\_bitrate) \

368 CAN\_DT\_DRIVER\_CONFIG\_GET(DT\_DRV\_INST(inst), \_max\_bitrate)

369

376struct can\_driver\_data {

378 [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode;

380 bool started;

382 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) state\_change\_cb;

384 void \*state\_change\_cb\_user\_data;

385};

386

391typedef int (\*can\_set\_timing\_t)(const struct [device](structdevice.md) \*dev,

392 const struct [can\_timing](structcan__timing.md) \*timing);

393

398typedef int (\*can\_set\_timing\_data\_t)(const struct [device](structdevice.md) \*dev,

399 const struct [can\_timing](structcan__timing.md) \*timing\_data);

400

405typedef int (\*can\_get\_capabilities\_t)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap);

406

411typedef int (\*can\_start\_t)(const struct [device](structdevice.md) \*dev);

412

417typedef int (\*can\_stop\_t)(const struct [device](structdevice.md) \*dev);

418

423typedef int (\*can\_set\_mode\_t)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

424

432typedef int (\*can\_send\_t)(const struct [device](structdevice.md) \*dev,

433 const struct [can\_frame](structcan__frame.md) \*frame,

434 [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback,

435 void \*user\_data);

436

441typedef int (\*can\_add\_rx\_filter\_t)(const struct [device](structdevice.md) \*dev,

442 [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback,

443 void \*user\_data,

444 const struct [can\_filter](structcan__filter.md) \*filter);

445

450typedef void (\*can\_remove\_rx\_filter\_t)(const struct [device](structdevice.md) \*dev, int filter\_id);

451

456typedef int (\*can\_recover\_t)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

457

462typedef int (\*can\_get\_state\_t)(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

463 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt);

464

469typedef void(\*can\_set\_state\_change\_callback\_t)(const struct [device](structdevice.md) \*dev,

470 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback,

471 void \*user\_data);

472

477typedef int (\*can\_get\_core\_clock\_t)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

478

483typedef int (\*can\_get\_max\_filters\_t)(const struct [device](structdevice.md) \*dev, bool ide);

484

485\_\_subsystem struct can\_driver\_api {

486 can\_get\_capabilities\_t get\_capabilities;

487 can\_start\_t start;

488 can\_stop\_t stop;

489 can\_set\_mode\_t set\_mode;

490 can\_set\_timing\_t set\_timing;

491 can\_send\_t [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d);

492 can\_add\_rx\_filter\_t add\_rx\_filter;

493 can\_remove\_rx\_filter\_t remove\_rx\_filter;

494#if !defined(CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY) || defined(\_\_DOXYGEN\_\_)

495 can\_recover\_t recover;

496#endif /\* CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY \*/

497 can\_get\_state\_t get\_state;

498 can\_set\_state\_change\_callback\_t set\_state\_change\_callback;

499 can\_get\_core\_clock\_t get\_core\_clock;

500 can\_get\_max\_filters\_t get\_max\_filters;

501 /\* Min values for the timing registers \*/

502 struct can\_timing timing\_min;

503 /\* Max values for the timing registers \*/

504 struct can\_timing timing\_max;

505#if defined(CONFIG\_CAN\_FD\_MODE) || defined(\_\_DOXYGEN\_\_)

506 can\_set\_timing\_data\_t set\_timing\_data;

507 /\* Min values for the timing registers during the data phase \*/

508 struct can\_timing timing\_data\_min;

509 /\* Max values for the timing registers during the data phase \*/

510 struct can\_timing timing\_data\_max;

511#endif /\* CONFIG\_CAN\_FD\_MODE \*/

512};

513

515

516#if defined(CONFIG\_CAN\_STATS) || defined(\_\_DOXYGEN\_\_)

517

518#include <[zephyr/stats/stats.h](stats_2stats_8h.md)>

519

521

522[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(can)

523[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit\_error)

524[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit0\_error)

525[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit1\_error)

526[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(stuff\_error)

527[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(crc\_error)

528[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(form\_error)

529[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(ack\_error)

530[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(rx\_overrun)

531[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

532

533[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(can)

534[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit\_error)

535[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit0\_error)

536[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit1\_error)

537[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, stuff\_error)

538[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, crc\_error)

539[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, form\_error)

540[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, ack\_error)

541[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, rx\_overrun)

542[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(can);

543

545

[ 550](structcan__device__state.md)struct [can\_device\_state](structcan__device__state.md) {

[ 552](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec) struct [device\_state](structdevice__state.md) [devstate](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec);

[ 554](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47) struct stats\_can [stats](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47);

555};

556

558

562#define Z\_CAN\_GET\_STATS(dev\_) \

563 CONTAINER\_OF(dev\_->state, struct can\_device\_state, devstate)->stats

564

566

[ 583](group__can__interface.md#gaf6f7efa9d99f44af6f58352f558d7fec)#define CAN\_STATS\_BIT\_ERROR\_INC(dev\_) \

584 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit\_error)

585

[ 597](group__can__interface.md#ga120a37d5ae5064dcbf116e488f733764)#define CAN\_STATS\_BIT0\_ERROR\_INC(dev\_) \

598 do { \

599 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit0\_error); \

600 CAN\_STATS\_BIT\_ERROR\_INC(dev\_); \

601 } while (0)

602

[ 614](group__can__interface.md#ga678b74039632302efcb5ef80f0e3a90b)#define CAN\_STATS\_BIT1\_ERROR\_INC(dev\_) \

615 do { \

616 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit1\_error); \

617 CAN\_STATS\_BIT\_ERROR\_INC(dev\_); \

618 } while (0)

619

[ 628](group__can__interface.md#gae4146843944b7ffb1c96636e889282f7)#define CAN\_STATS\_STUFF\_ERROR\_INC(dev\_) \

629 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), stuff\_error)

630

[ 639](group__can__interface.md#ga125ce05d40881476f5f156ad5e28c664)#define CAN\_STATS\_CRC\_ERROR\_INC(dev\_) \

640 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), crc\_error)

641

[ 650](group__can__interface.md#gac5809b3f5e1a463822e76921cddc9909)#define CAN\_STATS\_FORM\_ERROR\_INC(dev\_) \

651 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), form\_error)

652

[ 661](group__can__interface.md#ga15f7ca18badbbe2fe24be68cacce6171)#define CAN\_STATS\_ACK\_ERROR\_INC(dev\_) \

662 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), ack\_error)

663

[ 673](group__can__interface.md#ga95fe455780b38c7202b48bc6004e6f4d)#define CAN\_STATS\_RX\_OVERRUN\_INC(dev\_) \

674 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), rx\_overrun)

675

[ 684](group__can__interface.md#ga06a9058924901e2d960858fb9e3a4a02)#define CAN\_STATS\_RESET(dev\_) \

685 stats\_reset(&(Z\_CAN\_GET\_STATS(dev\_).s\_hdr))

686

688

692#define Z\_CAN\_DEVICE\_STATE\_DEFINE(dev\_id) \

693 static struct can\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_id) \

694 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

695

702#define Z\_CAN\_INIT\_FN(dev\_id, init\_fn) \

703 static inline int UTIL\_CAT(dev\_id, \_init)(const struct device \*dev) \

704 { \

705 struct can\_device\_state \*state = \

706 CONTAINER\_OF(dev->state, struct can\_device\_state, devstate); \

707 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 8, \

708 STATS\_NAME\_INIT\_PARMS(can)); \

709 stats\_register(dev->name, &(state->stats.s\_hdr)); \

710 if (init\_fn != NULL) { \

711 return init\_fn(dev); \

712 } \

713 \

714 return 0; \

715 }

716

718

[ 739](group__can__interface.md#ga599d0695abe481411660d7af2893f4a5)#define CAN\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

740 prio, api, ...) \

741 Z\_CAN\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

742 Z\_CAN\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

743 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

744 DEVICE\_DT\_NAME(node\_id), \

745 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

746 pm, data, config, level, prio, api, \

747 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

748 \_\_VA\_ARGS\_\_)

749

750#else /\* CONFIG\_CAN\_STATS \*/

751

752#define CAN\_STATS\_BIT\_ERROR\_INC(dev\_)

753#define CAN\_STATS\_BIT0\_ERROR\_INC(dev\_)

754#define CAN\_STATS\_BIT1\_ERROR\_INC(dev\_)

755#define CAN\_STATS\_STUFF\_ERROR\_INC(dev\_)

756#define CAN\_STATS\_CRC\_ERROR\_INC(dev\_)

757#define CAN\_STATS\_FORM\_ERROR\_INC(dev\_)

758#define CAN\_STATS\_ACK\_ERROR\_INC(dev\_)

759#define CAN\_STATS\_RX\_OVERRUN\_INC(dev\_)

760#define CAN\_STATS\_RESET(dev\_)

761

762#define CAN\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

763 prio, api, ...) \

764 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

765 prio, api, \_\_VA\_ARGS\_\_)

766

767#endif /\* CONFIG\_CAN\_STATS \*/

768

[ 776](group__can__interface.md#ga20266dc5e962922144e078b85ccb8351)#define CAN\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

777 CAN\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

778

784

[ 795](group__can__interface.md#ga4af6d0d9ab72b195909f511ac65cb8fa)\_\_syscall int [can\_get\_core\_clock](group__can__interface.md#ga4af6d0d9ab72b195909f511ac65cb8fa)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

796

797static inline int z\_impl\_can\_get\_core\_clock(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate)

798{

799 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

800

801 return api->get\_core\_clock(dev, rate);

802}

803

[ 816](group__can__interface.md#ga90fef54f61ac2a6244ef4ab36bde6e9b)\_\_syscall int [can\_get\_max\_bitrate](group__can__interface.md#ga90fef54f61ac2a6244ef4ab36bde6e9b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max\_bitrate);

817

818static inline int z\_impl\_can\_get\_max\_bitrate(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max\_bitrate)

819{

820 const struct can\_driver\_config \*common = (const struct can\_driver\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

821

822 if (common->max\_bitrate == 0U) {

823 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

824 }

825

826 \*max\_bitrate = common->max\_bitrate;

827

828 return 0;

829}

830

[ 838](group__can__interface.md#ga5a57627de4764f0bd3b4bafe07f56e6f)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_min](group__can__interface.md#ga5a57627de4764f0bd3b4bafe07f56e6f)(const struct [device](structdevice.md) \*dev);

839

840static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_min(const struct [device](structdevice.md) \*dev)

841{

842 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

843

844 return &api->timing\_min;

845}

846

[ 854](group__can__interface.md#gabe385d0f003b1e990c78ef7a2a3f9616)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_max](group__can__interface.md#gabe385d0f003b1e990c78ef7a2a3f9616)(const struct [device](structdevice.md) \*dev);

855

856static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_max(const struct [device](structdevice.md) \*dev)

857{

858 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

859

860 return &api->timing\_max;

861}

862

[ 884](group__can__interface.md#gac27fe64142603f0d32d422594356b2d7)\_\_syscall int [can\_calc\_timing](group__can__interface.md#gac27fe64142603f0d32d422594356b2d7)(const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res,

885 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt);

886

[ 900](group__can__interface.md#ga6399ef0cefdab3da738136f8a5c59c2f)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_data\_min](group__can__interface.md#ga6399ef0cefdab3da738136f8a5c59c2f)(const struct [device](structdevice.md) \*dev);

901

902#ifdef CONFIG\_CAN\_FD\_MODE

903static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_data\_min(const struct [device](structdevice.md) \*dev)

904{

905 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

906

907 return &api->timing\_data\_min;

908}

909#endif /\* CONFIG\_CAN\_FD\_MODE \*/

910

[ 924](group__can__interface.md#ga47a2f6d6b42121b390aa92160c833b80)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_data\_max](group__can__interface.md#ga47a2f6d6b42121b390aa92160c833b80)(const struct [device](structdevice.md) \*dev);

925

926#ifdef CONFIG\_CAN\_FD\_MODE

927static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_data\_max(const struct [device](structdevice.md) \*dev)

928{

929 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

930

931 return &api->timing\_data\_max;

932}

933#endif /\* CONFIG\_CAN\_FD\_MODE \*/

934

[ 954](group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11)\_\_syscall int [can\_calc\_timing\_data](group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11)(const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res,

955 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt);

956

[ 974](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2)\_\_syscall int [can\_set\_timing\_data](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2)(const struct [device](structdevice.md) \*dev,

975 const struct [can\_timing](structcan__timing.md) \*timing\_data);

976

[ 1005](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7)\_\_syscall int [can\_set\_bitrate\_data](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate\_data);

1006

[ 1023](group__can__interface.md#ga7ee7a3296995c09c7f35f54029ed26cd)int [can\_calc\_prescaler](group__can__interface.md#ga7ee7a3296995c09c7f35f54029ed26cd)(const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*timing,

1024 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate);

1025

[ 1039](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da)\_\_syscall int [can\_set\_timing](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da)(const struct [device](structdevice.md) \*dev,

1040 const struct [can\_timing](structcan__timing.md) \*timing);

1041

[ 1055](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168)\_\_syscall int [can\_get\_capabilities](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap);

1056

1057static inline int z\_impl\_can\_get\_capabilities(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap)

1058{

1059 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1060

1061 return api->get\_capabilities(dev, cap);

1062}

1063

[ 1073](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a)\_\_syscall const struct [device](structdevice.md) \*[can\_get\_transceiver](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a)(const struct [device](structdevice.md) \*dev);

1074

1075static const struct [device](structdevice.md) \*z\_impl\_can\_get\_transceiver(const struct [device](structdevice.md) \*dev)

1076{

1077 const struct can\_driver\_config \*common = (const struct can\_driver\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1078

1079 return common->phy;

1080}

1081

[ 1099](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a)\_\_syscall int [can\_start](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a)(const struct [device](structdevice.md) \*dev);

1100

1101static inline int z\_impl\_can\_start(const struct [device](structdevice.md) \*dev)

1102{

1103 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1104

1105 return api->start(dev);

1106}

1107

[ 1123](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5)\_\_syscall int [can\_stop](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5)(const struct [device](structdevice.md) \*dev);

1124

1125static inline int z\_impl\_can\_stop(const struct [device](structdevice.md) \*dev)

1126{

1127 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1128

1129 return api->stop(dev);

1130}

1131

[ 1142](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f)\_\_syscall int [can\_set\_mode](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

1143

1144static inline int z\_impl\_can\_set\_mode(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode)

1145{

1146 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1147

1148 return api->set\_mode(dev, mode);

1149}

1150

[ 1158](group__can__interface.md#gabd201b5b1fca54048985a8a24dd51e55)\_\_syscall [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) [can\_get\_mode](group__can__interface.md#gabd201b5b1fca54048985a8a24dd51e55)(const struct [device](structdevice.md) \*dev);

1159

1160static inline [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) z\_impl\_can\_get\_mode(const struct [device](structdevice.md) \*dev)

1161{

1162 const struct can\_driver\_data \*common = (const struct can\_driver\_data \*)dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1163

1164 return common->mode;

1165}

1166

[ 1192](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b)\_\_syscall int [can\_set\_bitrate](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate);

1193

1195

1201

[ 1246](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5)\_\_syscall int [can\_send](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5)(const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame,

1247 [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback,

1248 void \*user\_data);

1249

1251

1257

[ 1281](group__can__interface.md#ga0cf4baa2c4216d8515554d180ceb774a)static inline int [can\_add\_rx\_filter](group__can__interface.md#ga0cf4baa2c4216d8515554d180ceb774a)(const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback,

1282 void \*user\_data, const struct [can\_filter](structcan__filter.md) \*filter)

1283{

1284 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1285

1286 if (filter == NULL) {

1287 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

1288 }

1289

1290 return api->add\_rx\_filter(dev, callback, user\_data, filter);

1291}

1292

[ 1303](group__can__interface.md#ga7af0acdfbdad07fc3eba4cbd29bc090b)#define CAN\_MSGQ\_DEFINE(name, max\_frames) \

1304 K\_MSGQ\_DEFINE(name, sizeof(struct can\_frame), max\_frames, 4)

1305

[ 1332](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)\_\_syscall int [can\_add\_rx\_filter\_msgq](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)(const struct [device](structdevice.md) \*dev, struct [k\_msgq](structk__msgq.md) \*msgq,

1333 const struct [can\_filter](structcan__filter.md) \*filter);

1334

[ 1344](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847)\_\_syscall void [can\_remove\_rx\_filter](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847)(const struct [device](structdevice.md) \*dev, int filter\_id);

1345

1346static inline void z\_impl\_can\_remove\_rx\_filter(const struct [device](structdevice.md) \*dev, int filter\_id)

1347{

1348 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1349

1350 return api->remove\_rx\_filter(dev, filter\_id);

1351}

1352

[ 1366](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc)\_\_syscall int [can\_get\_max\_filters](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc)(const struct [device](structdevice.md) \*dev, bool ide);

1367

1368static inline int z\_impl\_can\_get\_max\_filters(const struct [device](structdevice.md) \*dev, bool ide)

1369{

1370 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1371

1372 if (api->get\_max\_filters == NULL) {

1373 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1374 }

1375

1376 return api->get\_max\_filters(dev, ide);

1377}

1378

1380

1386

[ 1400](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857)\_\_syscall int [can\_get\_state](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857)(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1401 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt);

1402

1403static inline int z\_impl\_can\_get\_state(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1404 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt)

1405{

1406 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1407

1408 return api->get\_state(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), err\_cnt);

1409}

1410

1426#if !defined(CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY) || defined(\_\_DOXYGEN\_\_)

[ 1427](group__can__interface.md#gac474e56a50685736a1c25dca277aab5e)\_\_syscall int [can\_recover](group__can__interface.md#gac474e56a50685736a1c25dca277aab5e)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

1428

1429static inline int z\_impl\_can\_recover(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout)

1430{

1431 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1432

1433 return api->recover(dev, timeout);

1434}

1435#else /\* CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY \*/

1436/\* This implementation prevents inking errors for auto recovery \*/

1437static inline int z\_impl\_can\_recover(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout)

1438{

1439 ARG\_UNUSED(dev);

1440 ARG\_UNUSED(timeout);

1441 return 0;

1442}

1443#endif /\* !CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY \*/

1444

[ 1458](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e)static inline void [can\_set\_state\_change\_callback](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e)(const struct [device](structdevice.md) \*dev,

1459 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback,

1460 void \*user\_data)

1461{

1462 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1463

1464 api->set\_state\_change\_callback(dev, callback, user\_data);

1465}

1466

1468

1474

[ 1487](group__can__interface.md#ga27b277f3b5146590f159171f602904db)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit\_errors](group__can__interface.md#ga27b277f3b5146590f159171f602904db)(const struct [device](structdevice.md) \*dev);

1488

1489#ifdef CONFIG\_CAN\_STATS

1490static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit\_errors(const struct [device](structdevice.md) \*dev)

1491{

1492 return Z\_CAN\_GET\_STATS(dev).bit\_error;

1493}

1494#endif /\* CONFIG\_CAN\_STATS \*/

1495

[ 1510](group__can__interface.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit0\_errors](group__can__interface.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)(const struct [device](structdevice.md) \*dev);

1511

1512#ifdef CONFIG\_CAN\_STATS

1513static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit0\_errors(const struct [device](structdevice.md) \*dev)

1514{

1515 return Z\_CAN\_GET\_STATS(dev).bit0\_error;

1516}

1517#endif /\* CONFIG\_CAN\_STATS \*/

1518

[ 1533](group__can__interface.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit1\_errors](group__can__interface.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)(const struct [device](structdevice.md) \*dev);

1534

1535#ifdef CONFIG\_CAN\_STATS

1536static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit1\_errors(const struct [device](structdevice.md) \*dev)

1537{

1538 return Z\_CAN\_GET\_STATS(dev).bit1\_error;

1539}

1540#endif /\* CONFIG\_CAN\_STATS \*/

1541

[ 1554](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_stuff\_errors](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38)(const struct [device](structdevice.md) \*dev);

1555

1556#ifdef CONFIG\_CAN\_STATS

1557static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_stuff\_errors(const struct [device](structdevice.md) \*dev)

1558{

1559 return Z\_CAN\_GET\_STATS(dev).stuff\_error;

1560}

1561#endif /\* CONFIG\_CAN\_STATS \*/

1562

[ 1575](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_crc\_errors](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2)(const struct [device](structdevice.md) \*dev);

1576

1577#ifdef CONFIG\_CAN\_STATS

1578static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_crc\_errors(const struct [device](structdevice.md) \*dev)

1579{

1580 return Z\_CAN\_GET\_STATS(dev).crc\_error;

1581}

1582#endif /\* CONFIG\_CAN\_STATS \*/

1583

[ 1596](group__can__interface.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_form\_errors](group__can__interface.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)(const struct [device](structdevice.md) \*dev);

1597

1598#ifdef CONFIG\_CAN\_STATS

1599static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_form\_errors(const struct [device](structdevice.md) \*dev)

1600{

1601 return Z\_CAN\_GET\_STATS(dev).form\_error;

1602}

1603#endif /\* CONFIG\_CAN\_STATS \*/

1604

[ 1617](group__can__interface.md#ga4f8414d64b75d4d1ffb7a0feff36f698)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_ack\_errors](group__can__interface.md#ga4f8414d64b75d4d1ffb7a0feff36f698)(const struct [device](structdevice.md) \*dev);

1618

1619#ifdef CONFIG\_CAN\_STATS

1620static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_ack\_errors(const struct [device](structdevice.md) \*dev)

1621{

1622 return Z\_CAN\_GET\_STATS(dev).ack\_error;

1623}

1624#endif /\* CONFIG\_CAN\_STATS \*/

1625

[ 1639](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_rx\_overruns](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)(const struct [device](structdevice.md) \*dev);

1640

1641#ifdef CONFIG\_CAN\_STATS

1642static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_rx\_overruns(const struct [device](structdevice.md) \*dev)

1643{

1644 return Z\_CAN\_GET\_STATS(dev).rx\_overrun;

1645}

1646#endif /\* CONFIG\_CAN\_STATS \*/

1647

1649

1655

[ 1663](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlc)

1664{

1665 static const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlc\_table[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 12,

1666 16, 20, 24, 32, 48, 64};

1667

1668 return dlc\_table[[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(dlc, [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(dlc\_table) - 1)];

1669}

1670

[ 1678](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [can\_bytes\_to\_dlc](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_bytes)

1679{

1680 return num\_bytes <= 8 ? num\_bytes :

1681 num\_bytes <= 12 ? 9 :

1682 num\_bytes <= 16 ? 10 :

1683 num\_bytes <= 20 ? 11 :

1684 num\_bytes <= 24 ? 12 :

1685 num\_bytes <= 32 ? 13 :

1686 num\_bytes <= 48 ? 14 :

1687 15;

1688}

1689

[ 1697](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)static inline bool [can\_frame\_matches\_filter](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)(const struct [can\_frame](structcan__frame.md) \*frame,

1698 const struct [can\_filter](structcan__filter.md) \*filter)

1699{

1700 if ((frame->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)) != 0 && (filter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) & [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)) == 0) {

1701 /\* Extended (29-bit) ID frame, standard (11-bit) filter \*/

1702 return false;

1703 }

1704

1705 if ((frame->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)) == 0 && (filter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) & [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)) != 0) {

1706 /\* Standard (11-bit) ID frame, extended (29-bit) filter \*/

1707 return false;

1708 }

1709

1710 if ((frame->[id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d) ^ filter->[id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9)) & filter->[mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94)) {

1711 /\* Masked ID mismatch \*/

1712 return false;

1713 }

1714

1715 return true;

1716}

1717

1719

1723

1724#ifdef \_\_cplusplus

1725}

1726#endif

1727

1728#include <syscalls/can.h>

1729

1730#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:882

[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)

void(\* can\_state\_change\_callback\_t)(const struct device \*dev, enum can\_state state, struct can\_bus\_err\_cnt err\_cnt, void \*user\_data)

Defines the state change callback handler function signature.

**Definition** can.h:309

[can\_set\_bitrate](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b)

int can\_set\_bitrate(const struct device \*dev, uint32\_t bitrate)

Set the bitrate of the CAN controller.

[can\_set\_bitrate\_data](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7)

int can\_set\_bitrate\_data(const struct device \*dev, uint32\_t bitrate\_data)

Set the bitrate for the data phase of the CAN FD controller.

[can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)

uint32\_t can\_mode\_t

Provides a type to hold CAN controller configuration flags.

**Definition** can.h:116

[can\_add\_rx\_filter](group__can__interface.md#ga0cf4baa2c4216d8515554d180ceb774a)

static int can\_add\_rx\_filter(const struct device \*dev, can\_rx\_callback\_t callback, void \*user\_data, const struct can\_filter \*filter)

Add a callback function for a given CAN filter.

**Definition** can.h:1281

[can\_stats\_get\_stuff\_errors](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38)

uint32\_t can\_stats\_get\_stuff\_errors(const struct device \*dev)

Get the stuffing error counter for a CAN device.

[can\_stop](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5)

int can\_stop(const struct device \*dev)

Stop the CAN controller.

[can\_set\_timing](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da)

int can\_set\_timing(const struct device \*dev, const struct can\_timing \*timing)

Configure the bus timing of a CAN controller.

[can\_stats\_get\_bit\_errors](group__can__interface.md#ga27b277f3b5146590f159171f602904db)

uint32\_t can\_stats\_get\_bit\_errors(const struct device \*dev)

Get the bit error counter for a CAN device.

[can\_stats\_get\_crc\_errors](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2)

uint32\_t can\_stats\_get\_crc\_errors(const struct device \*dev)

Get the CRC error counter for a CAN device.

[can\_calc\_timing\_data](group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11)

int can\_calc\_timing\_data(const struct device \*dev, struct can\_timing \*res, uint32\_t bitrate, uint16\_t sample\_pnt)

Calculate timing parameters for the data phase.

[can\_send](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5)

int can\_send(const struct device \*dev, const struct can\_frame \*frame, k\_timeout\_t timeout, can\_tx\_callback\_t callback, void \*user\_data)

Queue a CAN frame for transmission on the CAN bus.

[can\_get\_timing\_data\_max](group__can__interface.md#ga47a2f6d6b42121b390aa92160c833b80)

const struct can\_timing \* can\_get\_timing\_data\_max(const struct device \*dev)

Get the maximum supported timing parameter values for the data phase.

[can\_get\_core\_clock](group__can__interface.md#ga4af6d0d9ab72b195909f511ac65cb8fa)

int can\_get\_core\_clock(const struct device \*dev, uint32\_t \*rate)

Get the CAN core clock rate.

[can\_get\_capabilities](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168)

int can\_get\_capabilities(const struct device \*dev, can\_mode\_t \*cap)

Get the supported modes of the CAN controller.

[can\_stats\_get\_bit1\_errors](group__can__interface.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)

uint32\_t can\_stats\_get\_bit1\_errors(const struct device \*dev)

Get the bit1 error counter for a CAN device.

[can\_stats\_get\_ack\_errors](group__can__interface.md#ga4f8414d64b75d4d1ffb7a0feff36f698)

uint32\_t can\_stats\_get\_ack\_errors(const struct device \*dev)

Get the acknowledge error counter for a CAN device.

[can\_get\_max\_filters](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc)

int can\_get\_max\_filters(const struct device \*dev, bool ide)

Get maximum number of RX filters.

[can\_get\_timing\_min](group__can__interface.md#ga5a57627de4764f0bd3b4bafe07f56e6f)

const struct can\_timing \* can\_get\_timing\_min(const struct device \*dev)

Get the minimum supported timing parameter values.

[can\_set\_timing\_data](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2)

int can\_set\_timing\_data(const struct device \*dev, const struct can\_timing \*timing\_data)

Configure the bus timing for the data phase of a CAN FD controller.

[can\_get\_timing\_data\_min](group__can__interface.md#ga6399ef0cefdab3da738136f8a5c59c2f)

const struct can\_timing \* can\_get\_timing\_data\_min(const struct device \*dev)

Get the minimum supported timing parameter values for the data phase.

[can\_stats\_get\_bit0\_errors](group__can__interface.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)

uint32\_t can\_stats\_get\_bit0\_errors(const struct device \*dev)

Get the bit0 error counter for a CAN device.

[can\_calc\_prescaler](group__can__interface.md#ga7ee7a3296995c09c7f35f54029ed26cd)

int can\_calc\_prescaler(const struct device \*dev, struct can\_timing \*timing, uint32\_t bitrate)

Fill in the prescaler value for a given bitrate and timing.

[can\_remove\_rx\_filter](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847)

void can\_remove\_rx\_filter(const struct device \*dev, int filter\_id)

Remove a CAN RX filter.

[can\_bytes\_to\_dlc](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)

static uint8\_t can\_bytes\_to\_dlc(uint8\_t num\_bytes)

Convert from number of bytes to Data Length Code (DLC).

**Definition** can.h:1678

[can\_stats\_get\_rx\_overruns](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)

uint32\_t can\_stats\_get\_rx\_overruns(const struct device \*dev)

Get the RX overrun counter for a CAN device.

[can\_get\_max\_bitrate](group__can__interface.md#ga90fef54f61ac2a6244ef4ab36bde6e9b)

int can\_get\_max\_bitrate(const struct device \*dev, uint32\_t \*max\_bitrate)

Get maximum supported bitrate.

[CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)

#define CAN\_FRAME\_IDE

Frame uses extended (29-bit) CAN ID.

**Definition** can.h:142

[can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)

static uint8\_t can\_dlc\_to\_bytes(uint8\_t dlc)

Convert from Data Length Code (DLC) to the number of data bytes.

**Definition** can.h:1663

[can\_add\_rx\_filter\_msgq](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)

int can\_add\_rx\_filter\_msgq(const struct device \*dev, struct k\_msgq \*msgq, const struct can\_filter \*filter)

Simple wrapper function for adding a message queue for a given filter.

[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)

void(\* can\_rx\_callback\_t)(const struct device \*dev, struct can\_frame \*frame, void \*user\_data)

Defines the application callback handler function signature for receiving.

**Definition** can.h:298

[can\_frame\_matches\_filter](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)

static bool can\_frame\_matches\_filter(const struct can\_frame \*frame, const struct can\_filter \*filter)

Check if a CAN frame matches a CAN filter.

**Definition** can.h:1697

[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)

void(\* can\_tx\_callback\_t)(const struct device \*dev, int error, void \*user\_data)

Defines the application callback handler function signature.

**Definition** can.h:289

[can\_get\_state](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857)

int can\_get\_state(const struct device \*dev, enum can\_state \*state, struct can\_bus\_err\_cnt \*err\_cnt)

Get current CAN controller state.

[can\_get\_mode](group__can__interface.md#gabd201b5b1fca54048985a8a24dd51e55)

can\_mode\_t can\_get\_mode(const struct device \*dev)

Get the operation mode of the CAN controller.

[can\_get\_timing\_max](group__can__interface.md#gabe385d0f003b1e990c78ef7a2a3f9616)

const struct can\_timing \* can\_get\_timing\_max(const struct device \*dev)

Get the maximum supported timing parameter values.

[can\_stats\_get\_form\_errors](group__can__interface.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)

uint32\_t can\_stats\_get\_form\_errors(const struct device \*dev)

Get the form error counter for a CAN device.

[can\_calc\_timing](group__can__interface.md#gac27fe64142603f0d32d422594356b2d7)

int can\_calc\_timing(const struct device \*dev, struct can\_timing \*res, uint32\_t bitrate, uint16\_t sample\_pnt)

Calculate timing parameters from bitrate and sample point.

[can\_recover](group__can__interface.md#gac474e56a50685736a1c25dca277aab5e)

int can\_recover(const struct device \*dev, k\_timeout\_t timeout)

Recover from bus-off state.

[can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7)

can\_state

Defines the state of the CAN controller.

**Definition** can.h:121

[can\_set\_state\_change\_callback](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e)

static void can\_set\_state\_change\_callback(const struct device \*dev, can\_state\_change\_callback\_t callback, void \*user\_data)

Set a callback for CAN controller state change events.

**Definition** can.h:1458

[can\_get\_transceiver](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a)

const struct device \* can\_get\_transceiver(const struct device \*dev)

Get the CAN transceiver associated with the CAN controller.

[can\_set\_mode](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f)

int can\_set\_mode(const struct device \*dev, can\_mode\_t mode)

Set the CAN controller to the given operation mode.

[can\_start](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a)

int can\_start(const struct device \*dev)

Start the CAN controller.

[CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)

#define CAN\_FILTER\_IDE

Filter matches frames with extended (29-bit) CAN IDs.

**Definition** can.h:204

[CAN\_STATE\_ERROR\_ACTIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c)

@ CAN\_STATE\_ERROR\_ACTIVE

Error-active state (RX/TX error count < 96).

**Definition** can.h:123

[CAN\_STATE\_ERROR\_WARNING](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff)

@ CAN\_STATE\_ERROR\_WARNING

Error-warning state (RX/TX error count < 128).

**Definition** can.h:125

[CAN\_STATE\_STOPPED](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)

@ CAN\_STATE\_STOPPED

CAN controller is stopped and does not participate in CAN communication.

**Definition** can.h:131

[CAN\_STATE\_BUS\_OFF](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959)

@ CAN\_STATE\_BUS\_OFF

Bus-off state (RX/TX error count >= 256).

**Definition** can.h:129

[CAN\_STATE\_ERROR\_PASSIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae)

@ CAN\_STATE\_ERROR\_PASSIVE

Error-passive state (RX/TX error count < 256).

**Definition** can.h:127

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)

#define MIN(a, b)

Obtain the minimum of two values.

**Definition** util.h:373

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:124

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:318

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

[sys\_clock.h](include_2zephyr_2sys__clock_8h.md)

Variables needed for system clock.

[types.h](include_2zephyr_2types_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stats.h](stats_2stats_8h.md)

Statistics.

[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)

#define STATS\_NAME\_END(name\_\_)

**Definition** stats.h:391

[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)

#define STATS\_NAME(name\_\_, entry\_\_)

**Definition** stats.h:390

[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785)

#define STATS\_SECT\_END

Ends a stats group struct definition.

**Definition** stats.h:89

[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)

#define STATS\_SECT\_ENTRY32(var\_\_)

**Definition** stats.h:359

[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)

#define STATS\_NAME\_START(name\_\_)

**Definition** stats.h:389

[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)

#define STATS\_SECT\_START(group\_\_)

**Definition** stats.h:354

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[string.h](string_8h.md)

[can\_bus\_err\_cnt](structcan__bus__err__cnt.md)

CAN controller error counters.

**Definition** can.h:229

[can\_bus\_err\_cnt::tx\_err\_cnt](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98)

uint8\_t tx\_err\_cnt

Value of the CAN controller transmit error counter.

**Definition** can.h:231

[can\_bus\_err\_cnt::rx\_err\_cnt](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a)

uint8\_t rx\_err\_cnt

Value of the CAN controller receive error counter.

**Definition** can.h:233

[can\_device\_state](structcan__device__state.md)

CAN specific device state which allows for CAN device class specific additions.

**Definition** can.h:550

[can\_device\_state::devstate](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec)

struct device\_state devstate

Common device state.

**Definition** can.h:552

[can\_device\_state::stats](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47)

struct stats\_can stats

CAN device statistics.

**Definition** can.h:554

[can\_filter](structcan__filter.md)

CAN filter structure.

**Definition** can.h:212

[can\_filter::mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94)

uint32\_t mask

CAN identifier matching mask.

**Definition** can.h:221

[can\_filter::flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de)

uint8\_t flags

Flags.

**Definition** can.h:223

[can\_filter::id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9)

uint32\_t id

CAN identifier to match.

**Definition** can.h:214

[can\_frame](structcan__frame.md)

CAN frame structure.

**Definition** can.h:163

[can\_frame::dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47)

uint8\_t dlc

Data Length Code (DLC) indicating data length in bytes.

**Definition** can.h:170

[can\_frame::flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c)

uint8\_t flags

Flags.

**Definition** can.h:172

[can\_frame::id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d)

uint32\_t id

Standard (11-bit) or extended (29-bit) CAN identifier.

**Definition** can.h:165

[can\_frame::data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)

uint8\_t data[CAN\_MAX\_DLEN]

Payload data accessed as unsigned 8 bit values.

**Definition** can.h:190

[can\_frame::data\_32](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a)

uint32\_t data\_32[DIV\_ROUND\_UP(CAN\_MAX\_DLEN, sizeof(uint32\_t))]

Payload data accessed as unsigned 32 bit values.

**Definition** can.h:192

[can\_frame::timestamp](structcan__frame.md#ae46f8b0821c638517959274bbbda5932)

uint16\_t timestamp

Captured value of the free-running timer in the CAN controller when this frame was received.

**Definition** can.h:181

[can\_timing](structcan__timing.md)

CAN bus timing structure.

**Definition** can.h:268

[can\_timing::sjw](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5)

uint16\_t sjw

Synchronisation jump width.

**Definition** can.h:270

[can\_timing::phase\_seg2](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6)

uint16\_t phase\_seg2

Phase segment 2.

**Definition** can.h:276

[can\_timing::prescaler](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a)

uint16\_t prescaler

Prescaler value.

**Definition** can.h:278

[can\_timing::phase\_seg1](structcan__timing.md#a9941688e79fa4ce01c4b498433319089)

uint16\_t phase\_seg1

Phase segment 1.

**Definition** can.h:274

[can\_timing::prop\_seg](structcan__timing.md#ac009d40fee9788b663963978498b2ee9)

uint16\_t prop\_seg

Propagation segment.

**Definition** can.h:272

[device\_state](structdevice__state.md)

Runtime device dynamic structure (in RAM) per driver instance.

**Definition** device.h:358

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:391

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4402

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can.h](drivers_2can_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
