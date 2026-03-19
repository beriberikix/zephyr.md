---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2can_8h_source.html
original_path: doxygen/html/drivers_2can_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

21#include <[zephyr/kernel.h](kernel_8h.md)>

22#include <[string.h](string_8h.md)>

23#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

24#include <[zephyr/sys/util.h](sys_2util_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

38

43

[ 47](group__can__interface.md#ga4cd8ce34887b90baeeaa6a4aa048b398)#define CAN\_STD\_ID\_MASK 0x7FFU

[ 53](group__can__interface.md#ga7987c1d4089742f87a7ac611add1a286)#define CAN\_MAX\_STD\_ID CAN\_STD\_ID\_MASK \_\_DEPRECATED\_MACRO

[ 57](group__can__interface.md#ga15ee71e8abcf51008925585049125986)#define CAN\_EXT\_ID\_MASK 0x1FFFFFFFU

[ 63](group__can__interface.md#ga0f3572940065f8f6d54099e7a4175f8f)#define CAN\_MAX\_EXT\_ID CAN\_EXT\_ID\_MASK \_\_DEPRECATED\_MACRO

[ 67](group__can__interface.md#gadc209a027ee700faf10461e2417bee50)#define CAN\_MAX\_DLC 8U

[ 71](group__can__interface.md#gad4b7310536c7e3252c2056abe64c0333)#define CANFD\_MAX\_DLC 15U

72

77#ifndef CONFIG\_CAN\_FD\_MODE

78#define CAN\_MAX\_DLEN 8U

79#else

80#define CAN\_MAX\_DLEN 64U

81#endif /\* CONFIG\_CAN\_FD\_MODE \*/

82

84

86

93

[ 95](group__can__interface.md#ga89cd5ea2e9d70a51bc12b100be28ca3d)#define CAN\_MODE\_NORMAL 0

96

[ 98](group__can__interface.md#ga891031afc77974a041accb3d0ceb21bb)#define CAN\_MODE\_LOOPBACK BIT(0)

99

[ 101](group__can__interface.md#ga117d04b9118a1b3f839c557ef6b596cb)#define CAN\_MODE\_LISTENONLY BIT(1)

102

[ 104](group__can__interface.md#gabb4d99736d8386a5ab62a5e44374d13a)#define CAN\_MODE\_FD BIT(2)

105

[ 107](group__can__interface.md#ga033d7ade1966299c7e6249b945f38202)#define CAN\_MODE\_ONE\_SHOT BIT(3)

108

[ 110](group__can__interface.md#gaf0821983174ad781e1bb63a976a18fab)#define CAN\_MODE\_3\_SAMPLES BIT(4)

111

[ 113](group__can__interface.md#ga3d8675253125b2af2bd22f0b2cc60cdd)#define CAN\_MODE\_MANUAL\_RECOVERY BIT(5)

114

116

[ 125](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7);

126

[ 130](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7)enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) {

[ 132](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c) [CAN\_STATE\_ERROR\_ACTIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c),

[ 134](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff) [CAN\_STATE\_ERROR\_WARNING](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff),

[ 136](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae) [CAN\_STATE\_ERROR\_PASSIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae),

[ 138](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959) [CAN\_STATE\_BUS\_OFF](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959),

[ 140](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8) [CAN\_STATE\_STOPPED](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8),

141};

142

149

[ 151](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)#define CAN\_FRAME\_IDE BIT(0)

152

[ 154](group__can__interface.md#gaed376ef16b84cd1974255fbb26dc3d7f)#define CAN\_FRAME\_RTR BIT(1)

155

[ 157](group__can__interface.md#ga22f85e1d16b93e46200f9673abdbb589)#define CAN\_FRAME\_FDF BIT(2)

158

[ 160](group__can__interface.md#ga1fdf15ce4a3b333488f9b630ec836d52)#define CAN\_FRAME\_BRS BIT(3)

161

[ 165](group__can__interface.md#ga83f8b7af6eb45e43aaac355de3e69e52)#define CAN\_FRAME\_ESI BIT(4)

166

168

[ 172](structcan__frame.md)struct [can\_frame](structcan__frame.md) {

[ 174](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d);

[ 176](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47);

[ 178](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c);

179#if defined(CONFIG\_CAN\_RX\_TIMESTAMP) || defined(\_\_DOXYGEN\_\_)

[ 187](structcan__frame.md#ae46f8b0821c638517959274bbbda5932) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timestamp](structcan__frame.md#ae46f8b0821c638517959274bbbda5932);

188#else

191 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reserved;

193#endif

195 union {

[ 197](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)[CAN\_MAX\_DLEN];

[ 199](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_32](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a)[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(CAN\_MAX\_DLEN, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)))];

200 };

201};

202

209

[ 211](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)#define CAN\_FILTER\_IDE BIT(0)

212

214

[ 218](structcan__filter.md)struct [can\_filter](structcan__filter.md) {

[ 220](structcan__filter.md#adf2b18eab11d360780707478a1f624b9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9);

[ 224](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94);

[ 226](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de);

227};

228

[ 232](structcan__bus__err__cnt.md)struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) {

[ 234](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_err\_cnt](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98);

[ 236](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_err\_cnt](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a);

237};

238

[ 271](structcan__timing.md)struct [can\_timing](structcan__timing.md) {

[ 273](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sjw](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5);

[ 275](structcan__timing.md#ac009d40fee9788b663963978498b2ee9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [prop\_seg](structcan__timing.md#ac009d40fee9788b663963978498b2ee9);

[ 277](structcan__timing.md#a9941688e79fa4ce01c4b498433319089) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phase\_seg1](structcan__timing.md#a9941688e79fa4ce01c4b498433319089);

[ 279](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phase\_seg2](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6);

[ 281](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [prescaler](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a);

282};

283

[ 292](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)typedef void (\*[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca))(const struct [device](structdevice.md) \*dev, int error, void \*user\_data);

293

[ 301](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)typedef void (\*[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f))(const struct [device](structdevice.md) \*dev, struct [can\_frame](structcan__frame.md) \*frame,

302 void \*user\_data);

303

[ 312](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)typedef void (\*[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d))(const struct [device](structdevice.md) \*dev,

313 enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

314 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) err\_cnt,

315 void \*user\_data);

316

322

336#define CAN\_CALC\_TDCO(\_timing\_data, \_tdco\_min, \_tdco\_max) \

337 CLAMP((1U + \_timing\_data->prop\_seg + \_timing\_data->phase\_seg1) \* \_timing\_data->prescaler, \

338 \_tdco\_min, \_tdco\_max)

339

346struct can\_driver\_config {

348 const struct [device](structdevice.md) \*phy;

350 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) min\_bitrate;

352 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_bitrate;

354 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate;

356 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_point;

357#ifdef CONFIG\_CAN\_FD\_MODE

359 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_point\_data;

361 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate\_data;

362#endif /\* CONFIG\_CAN\_FD\_MODE \*/

363};

364

372#define CAN\_DT\_DRIVER\_CONFIG\_GET(node\_id, \_min\_bitrate, \_max\_bitrate) \

373 { \

374 .phy = DEVICE\_DT\_GET\_OR\_NULL(DT\_PHANDLE(node\_id, phys)), \

375 .min\_bitrate = DT\_CAN\_TRANSCEIVER\_MIN\_BITRATE(node\_id, \_min\_bitrate), \

376 .max\_bitrate = DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE(node\_id, \_max\_bitrate), \

377 .bitrate = DT\_PROP\_OR(node\_id, bitrate, \

378 DT\_PROP\_OR(node\_id, bus\_speed, CONFIG\_CAN\_DEFAULT\_BITRATE)), \

379 .sample\_point = DT\_PROP\_OR(node\_id, sample\_point, 0), \

380 IF\_ENABLED(CONFIG\_CAN\_FD\_MODE, \

381 (.bitrate\_data = DT\_PROP\_OR(node\_id, bitrate\_data, \

382 DT\_PROP\_OR(node\_id, bus\_speed\_data, CONFIG\_CAN\_DEFAULT\_BITRATE\_DATA)), \

383 .sample\_point\_data = DT\_PROP\_OR(node\_id, sample\_point\_data, 0),)) \

384 }

385

394#define CAN\_DT\_DRIVER\_CONFIG\_INST\_GET(inst, \_min\_bitrate, \_max\_bitrate) \

395 CAN\_DT\_DRIVER\_CONFIG\_GET(DT\_DRV\_INST(inst), \_min\_bitrate, \_max\_bitrate)

396

403struct can\_driver\_data {

405 [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode;

407 bool started;

409 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) state\_change\_cb;

411 void \*state\_change\_cb\_user\_data;

412};

413

418typedef int (\*can\_set\_timing\_t)(const struct [device](structdevice.md) \*dev,

419 const struct [can\_timing](structcan__timing.md) \*timing);

420

425typedef int (\*can\_set\_timing\_data\_t)(const struct [device](structdevice.md) \*dev,

426 const struct [can\_timing](structcan__timing.md) \*timing\_data);

427

432typedef int (\*can\_get\_capabilities\_t)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap);

433

438typedef int (\*can\_start\_t)(const struct [device](structdevice.md) \*dev);

439

444typedef int (\*can\_stop\_t)(const struct [device](structdevice.md) \*dev);

445

450typedef int (\*can\_set\_mode\_t)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

451

459typedef int (\*can\_send\_t)(const struct [device](structdevice.md) \*dev,

460 const struct [can\_frame](structcan__frame.md) \*frame,

461 [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback,

462 void \*user\_data);

463

468typedef int (\*can\_add\_rx\_filter\_t)(const struct [device](structdevice.md) \*dev,

469 [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback,

470 void \*user\_data,

471 const struct [can\_filter](structcan__filter.md) \*filter);

472

477typedef void (\*can\_remove\_rx\_filter\_t)(const struct [device](structdevice.md) \*dev, int filter\_id);

478

483typedef int (\*can\_recover\_t)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

484

489typedef int (\*can\_get\_state\_t)(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

490 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt);

491

496typedef void(\*can\_set\_state\_change\_callback\_t)(const struct [device](structdevice.md) \*dev,

497 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback,

498 void \*user\_data);

499

504typedef int (\*can\_get\_core\_clock\_t)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

505

510typedef int (\*can\_get\_max\_filters\_t)(const struct [device](structdevice.md) \*dev, bool ide);

511

512\_\_subsystem struct can\_driver\_api {

513 can\_get\_capabilities\_t get\_capabilities;

514 can\_start\_t start;

515 can\_stop\_t stop;

516 can\_set\_mode\_t set\_mode;

517 can\_set\_timing\_t set\_timing;

518 can\_send\_t [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d);

519 can\_add\_rx\_filter\_t add\_rx\_filter;

520 can\_remove\_rx\_filter\_t remove\_rx\_filter;

521#if defined(CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE) || defined(\_\_DOXYGEN\_\_)

522 can\_recover\_t recover;

523#endif /\* CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE \*/

524 can\_get\_state\_t get\_state;

525 can\_set\_state\_change\_callback\_t set\_state\_change\_callback;

526 can\_get\_core\_clock\_t get\_core\_clock;

527 can\_get\_max\_filters\_t get\_max\_filters;

528 /\* Min values for the timing registers \*/

529 struct can\_timing timing\_min;

530 /\* Max values for the timing registers \*/

531 struct can\_timing timing\_max;

532#if defined(CONFIG\_CAN\_FD\_MODE) || defined(\_\_DOXYGEN\_\_)

533 can\_set\_timing\_data\_t set\_timing\_data;

534 /\* Min values for the timing registers during the data phase \*/

535 struct can\_timing timing\_data\_min;

536 /\* Max values for the timing registers during the data phase \*/

537 struct can\_timing timing\_data\_max;

538#endif /\* CONFIG\_CAN\_FD\_MODE \*/

539};

540

542

543#if defined(CONFIG\_CAN\_STATS) || defined(\_\_DOXYGEN\_\_)

544

545#include <[zephyr/stats/stats.h](stats_2stats_8h.md)>

546

548

549[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(can)

550[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit\_error)

551[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit0\_error)

552[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit1\_error)

553[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(stuff\_error)

554[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(crc\_error)

555[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(form\_error)

556[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(ack\_error)

557[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(rx\_overrun)

558[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

559

560[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(can)

561[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit\_error)

562[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit0\_error)

563[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit1\_error)

564[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, stuff\_error)

565[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, crc\_error)

566[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, form\_error)

567[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, ack\_error)

568[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, rx\_overrun)

569[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(can);

570

572

[ 577](structcan__device__state.md)struct [can\_device\_state](structcan__device__state.md) {

[ 579](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec) struct [device\_state](structdevice__state.md) [devstate](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec);

[ 581](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47) struct stats\_can [stats](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47);

582};

583

585

589#define Z\_CAN\_GET\_STATS(dev\_) \

590 CONTAINER\_OF(dev\_->state, struct can\_device\_state, devstate)->stats

591

593

[ 610](group__can__interface.md#gaf6f7efa9d99f44af6f58352f558d7fec)#define CAN\_STATS\_BIT\_ERROR\_INC(dev\_) \

611 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit\_error)

612

[ 624](group__can__interface.md#ga120a37d5ae5064dcbf116e488f733764)#define CAN\_STATS\_BIT0\_ERROR\_INC(dev\_) \

625 do { \

626 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit0\_error); \

627 CAN\_STATS\_BIT\_ERROR\_INC(dev\_); \

628 } while (0)

629

[ 641](group__can__interface.md#ga678b74039632302efcb5ef80f0e3a90b)#define CAN\_STATS\_BIT1\_ERROR\_INC(dev\_) \

642 do { \

643 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit1\_error); \

644 CAN\_STATS\_BIT\_ERROR\_INC(dev\_); \

645 } while (0)

646

[ 655](group__can__interface.md#gae4146843944b7ffb1c96636e889282f7)#define CAN\_STATS\_STUFF\_ERROR\_INC(dev\_) \

656 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), stuff\_error)

657

[ 666](group__can__interface.md#ga125ce05d40881476f5f156ad5e28c664)#define CAN\_STATS\_CRC\_ERROR\_INC(dev\_) \

667 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), crc\_error)

668

[ 677](group__can__interface.md#gac5809b3f5e1a463822e76921cddc9909)#define CAN\_STATS\_FORM\_ERROR\_INC(dev\_) \

678 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), form\_error)

679

[ 688](group__can__interface.md#ga15f7ca18badbbe2fe24be68cacce6171)#define CAN\_STATS\_ACK\_ERROR\_INC(dev\_) \

689 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), ack\_error)

690

[ 700](group__can__interface.md#ga95fe455780b38c7202b48bc6004e6f4d)#define CAN\_STATS\_RX\_OVERRUN\_INC(dev\_) \

701 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), rx\_overrun)

702

[ 711](group__can__interface.md#ga06a9058924901e2d960858fb9e3a4a02)#define CAN\_STATS\_RESET(dev\_) \

712 stats\_reset(&(Z\_CAN\_GET\_STATS(dev\_).s\_hdr))

713

715

719#define Z\_CAN\_DEVICE\_STATE\_DEFINE(dev\_id) \

720 static struct can\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_id) \

721 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

722

729#define Z\_CAN\_INIT\_FN(dev\_id, init\_fn) \

730 static inline int UTIL\_CAT(dev\_id, \_init)(const struct device \*dev) \

731 { \

732 struct can\_device\_state \*state = \

733 CONTAINER\_OF(dev->state, struct can\_device\_state, devstate); \

734 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 8, \

735 STATS\_NAME\_INIT\_PARMS(can)); \

736 stats\_register(dev->name, &(state->stats.s\_hdr)); \

737 if (!is\_null\_no\_warn(init\_fn)) { \

738 return init\_fn(dev); \

739 } \

740 \

741 return 0; \

742 }

743

745

[ 766](group__can__interface.md#ga599d0695abe481411660d7af2893f4a5)#define CAN\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

767 prio, api, ...) \

768 Z\_CAN\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

769 Z\_CAN\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

770 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

771 DEVICE\_DT\_NAME(node\_id), \

772 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

773 pm, data, config, level, prio, api, \

774 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

775 \_\_VA\_ARGS\_\_)

776

777#else /\* CONFIG\_CAN\_STATS \*/

778

779#define CAN\_STATS\_BIT\_ERROR\_INC(dev\_)

780#define CAN\_STATS\_BIT0\_ERROR\_INC(dev\_)

781#define CAN\_STATS\_BIT1\_ERROR\_INC(dev\_)

782#define CAN\_STATS\_STUFF\_ERROR\_INC(dev\_)

783#define CAN\_STATS\_CRC\_ERROR\_INC(dev\_)

784#define CAN\_STATS\_FORM\_ERROR\_INC(dev\_)

785#define CAN\_STATS\_ACK\_ERROR\_INC(dev\_)

786#define CAN\_STATS\_RX\_OVERRUN\_INC(dev\_)

787#define CAN\_STATS\_RESET(dev\_)

788

789#define CAN\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

790 prio, api, ...) \

791 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

792 prio, api, \_\_VA\_ARGS\_\_)

793

794#endif /\* CONFIG\_CAN\_STATS \*/

795

[ 803](group__can__interface.md#ga20266dc5e962922144e078b85ccb8351)#define CAN\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

804 CAN\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

805

811

[ 824](group__can__interface.md#ga4af6d0d9ab72b195909f511ac65cb8fa)\_\_syscall int [can\_get\_core\_clock](group__can__interface.md#ga4af6d0d9ab72b195909f511ac65cb8fa)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

825

826static inline int z\_impl\_can\_get\_core\_clock(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate)

827{

828 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

829

830 return api->get\_core\_clock(dev, rate);

831}

832

[ 849](group__can__interface.md#ga343456749eec6144a91bacae0d94b114)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_get\_bitrate\_min](group__can__interface.md#ga343456749eec6144a91bacae0d94b114)(const struct [device](structdevice.md) \*dev);

850

851static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_get\_bitrate\_min(const struct [device](structdevice.md) \*dev)

852{

853 const struct can\_driver\_config \*common = (const struct can\_driver\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

854

855 return common->min\_bitrate;

856}

857

[ 880](group__can__interface.md#gaef00151aad8c47fef798d53140ea7296)\_\_deprecated static inline int [can\_get\_min\_bitrate](group__can__interface.md#gaef00151aad8c47fef798d53140ea7296)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*min\_bitrate)

881{

882 \*min\_bitrate = [can\_get\_bitrate\_min](group__can__interface.md#ga343456749eec6144a91bacae0d94b114)(dev);

883

884 return 0;

885}

886

[ 903](group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_get\_bitrate\_max](group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457)(const struct [device](structdevice.md) \*dev);

904

905static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_get\_bitrate\_max(const struct [device](structdevice.md) \*dev)

906{

907 const struct can\_driver\_config \*common = (const struct can\_driver\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

908

909 return common->max\_bitrate;

910}

911

[ 934](group__can__interface.md#gad3f929b2170f27b1cbe37a1caccb2e37)\_\_deprecated static inline int [can\_get\_max\_bitrate](group__can__interface.md#gad3f929b2170f27b1cbe37a1caccb2e37)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max\_bitrate)

935{

936 \*max\_bitrate = [can\_get\_bitrate\_max](group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457)(dev);

937

938 return 0;

939}

940

[ 948](group__can__interface.md#ga5a57627de4764f0bd3b4bafe07f56e6f)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_min](group__can__interface.md#ga5a57627de4764f0bd3b4bafe07f56e6f)(const struct [device](structdevice.md) \*dev);

949

950static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_min(const struct [device](structdevice.md) \*dev)

951{

952 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

953

954 return &api->timing\_min;

955}

956

[ 964](group__can__interface.md#gabe385d0f003b1e990c78ef7a2a3f9616)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_max](group__can__interface.md#gabe385d0f003b1e990c78ef7a2a3f9616)(const struct [device](structdevice.md) \*dev);

965

966static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_max(const struct [device](structdevice.md) \*dev)

967{

968 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

969

970 return &api->timing\_max;

971}

972

[ 999](group__can__interface.md#gac27fe64142603f0d32d422594356b2d7)\_\_syscall int [can\_calc\_timing](group__can__interface.md#gac27fe64142603f0d32d422594356b2d7)(const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res,

1000 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt);

1001

[ 1015](group__can__interface.md#ga6399ef0cefdab3da738136f8a5c59c2f)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_data\_min](group__can__interface.md#ga6399ef0cefdab3da738136f8a5c59c2f)(const struct [device](structdevice.md) \*dev);

1016

1017#ifdef CONFIG\_CAN\_FD\_MODE

1018static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_data\_min(const struct [device](structdevice.md) \*dev)

1019{

1020 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1021

1022 return &api->timing\_data\_min;

1023}

1024#endif /\* CONFIG\_CAN\_FD\_MODE \*/

1025

[ 1039](group__can__interface.md#ga47a2f6d6b42121b390aa92160c833b80)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_data\_max](group__can__interface.md#ga47a2f6d6b42121b390aa92160c833b80)(const struct [device](structdevice.md) \*dev);

1040

1041#ifdef CONFIG\_CAN\_FD\_MODE

1042static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_data\_max(const struct [device](structdevice.md) \*dev)

1043{

1044 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1045

1046 return &api->timing\_data\_max;

1047}

1048#endif /\* CONFIG\_CAN\_FD\_MODE \*/

1049

[ 1070](group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11)\_\_syscall int [can\_calc\_timing\_data](group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11)(const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res,

1071 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt);

1072

[ 1090](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2)\_\_syscall int [can\_set\_timing\_data](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2)(const struct [device](structdevice.md) \*dev,

1091 const struct [can\_timing](structcan__timing.md) \*timing\_data);

1092

[ 1121](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7)\_\_syscall int [can\_set\_bitrate\_data](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate\_data);

1122

[ 1143](group__can__interface.md#ga7ee7a3296995c09c7f35f54029ed26cd)\_\_deprecated int [can\_calc\_prescaler](group__can__interface.md#ga7ee7a3296995c09c7f35f54029ed26cd)(const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*timing,

1144 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate);

1145

[ 1159](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da)\_\_syscall int [can\_set\_timing](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da)(const struct [device](structdevice.md) \*dev,

1160 const struct [can\_timing](structcan__timing.md) \*timing);

1161

[ 1175](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168)\_\_syscall int [can\_get\_capabilities](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap);

1176

1177static inline int z\_impl\_can\_get\_capabilities(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap)

1178{

1179 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1180

1181 return api->get\_capabilities(dev, cap);

1182}

1183

[ 1193](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a)\_\_syscall const struct [device](structdevice.md) \*[can\_get\_transceiver](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a)(const struct [device](structdevice.md) \*dev);

1194

1195static const struct [device](structdevice.md) \*z\_impl\_can\_get\_transceiver(const struct [device](structdevice.md) \*dev)

1196{

1197 const struct can\_driver\_config \*common = (const struct can\_driver\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1198

1199 return common->phy;

1200}

1201

[ 1219](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a)\_\_syscall int [can\_start](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a)(const struct [device](structdevice.md) \*dev);

1220

1221static inline int z\_impl\_can\_start(const struct [device](structdevice.md) \*dev)

1222{

1223 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1224

1225 return api->start(dev);

1226}

1227

[ 1243](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5)\_\_syscall int [can\_stop](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5)(const struct [device](structdevice.md) \*dev);

1244

1245static inline int z\_impl\_can\_stop(const struct [device](structdevice.md) \*dev)

1246{

1247 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1248

1249 return api->stop(dev);

1250}

1251

[ 1262](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f)\_\_syscall int [can\_set\_mode](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

1263

1264static inline int z\_impl\_can\_set\_mode(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode)

1265{

1266 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1267

1268 return api->set\_mode(dev, mode);

1269}

1270

[ 1278](group__can__interface.md#gabd201b5b1fca54048985a8a24dd51e55)\_\_syscall [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) [can\_get\_mode](group__can__interface.md#gabd201b5b1fca54048985a8a24dd51e55)(const struct [device](structdevice.md) \*dev);

1279

1280static inline [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) z\_impl\_can\_get\_mode(const struct [device](structdevice.md) \*dev)

1281{

1282 const struct can\_driver\_data \*common = (const struct can\_driver\_data \*)dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1283

1284 return common->mode;

1285}

1286

[ 1312](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b)\_\_syscall int [can\_set\_bitrate](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate);

1313

1315

1321

[ 1366](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5)\_\_syscall int [can\_send](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5)(const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame,

1367 [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback,

1368 void \*user\_data);

1369

1371

1377

[ 1401](group__can__interface.md#gae9dd69a13b960f773ab07bb0bb13b5e9)int [can\_add\_rx\_filter](group__can__interface.md#gae9dd69a13b960f773ab07bb0bb13b5e9)(const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback,

1402 void \*user\_data, const struct [can\_filter](structcan__filter.md) \*filter);

1403

[ 1414](group__can__interface.md#ga7af0acdfbdad07fc3eba4cbd29bc090b)#define CAN\_MSGQ\_DEFINE(name, max\_frames) \

1415 K\_MSGQ\_DEFINE(name, sizeof(struct can\_frame), max\_frames, 4)

1416

[ 1443](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)\_\_syscall int [can\_add\_rx\_filter\_msgq](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)(const struct [device](structdevice.md) \*dev, struct [k\_msgq](structk__msgq.md) \*msgq,

1444 const struct [can\_filter](structcan__filter.md) \*filter);

1445

[ 1455](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847)\_\_syscall void [can\_remove\_rx\_filter](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847)(const struct [device](structdevice.md) \*dev, int filter\_id);

1456

1457static inline void z\_impl\_can\_remove\_rx\_filter(const struct [device](structdevice.md) \*dev, int filter\_id)

1458{

1459 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1460

1461 api->remove\_rx\_filter(dev, filter\_id);

1462}

1463

[ 1477](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc)\_\_syscall int [can\_get\_max\_filters](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc)(const struct [device](structdevice.md) \*dev, bool ide);

1478

1479static inline int z\_impl\_can\_get\_max\_filters(const struct [device](structdevice.md) \*dev, bool ide)

1480{

1481 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1482

1483 if (api->get\_max\_filters == NULL) {

1484 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1485 }

1486

1487 return api->get\_max\_filters(dev, ide);

1488}

1489

1491

1497

[ 1511](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857)\_\_syscall int [can\_get\_state](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857)(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1512 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt);

1513

1514static inline int z\_impl\_can\_get\_state(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1515 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt)

1516{

1517 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1518

1519 return api->get\_state(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), err\_cnt);

1520}

1521

[ 1539](group__can__interface.md#gac474e56a50685736a1c25dca277aab5e)\_\_syscall int [can\_recover](group__can__interface.md#gac474e56a50685736a1c25dca277aab5e)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

1540

1541#ifdef CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE

1542static inline int z\_impl\_can\_recover(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout)

1543{

1544 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1545

1546 if (api->recover == NULL) {

1547 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1548 }

1549

1550 return api->recover(dev, timeout);

1551}

1552#endif /\* CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE \*/

1553

[ 1567](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e)static inline void [can\_set\_state\_change\_callback](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e)(const struct [device](structdevice.md) \*dev,

1568 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback,

1569 void \*user\_data)

1570{

1571 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1572

1573 api->set\_state\_change\_callback(dev, callback, user\_data);

1574}

1575

1577

1583

[ 1596](group__can__interface.md#ga27b277f3b5146590f159171f602904db)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit\_errors](group__can__interface.md#ga27b277f3b5146590f159171f602904db)(const struct [device](structdevice.md) \*dev);

1597

1598#ifdef CONFIG\_CAN\_STATS

1599static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit\_errors(const struct [device](structdevice.md) \*dev)

1600{

1601 return Z\_CAN\_GET\_STATS(dev).bit\_error;

1602}

1603#endif /\* CONFIG\_CAN\_STATS \*/

1604

[ 1619](group__can__interface.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit0\_errors](group__can__interface.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)(const struct [device](structdevice.md) \*dev);

1620

1621#ifdef CONFIG\_CAN\_STATS

1622static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit0\_errors(const struct [device](structdevice.md) \*dev)

1623{

1624 return Z\_CAN\_GET\_STATS(dev).bit0\_error;

1625}

1626#endif /\* CONFIG\_CAN\_STATS \*/

1627

[ 1642](group__can__interface.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit1\_errors](group__can__interface.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)(const struct [device](structdevice.md) \*dev);

1643

1644#ifdef CONFIG\_CAN\_STATS

1645static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit1\_errors(const struct [device](structdevice.md) \*dev)

1646{

1647 return Z\_CAN\_GET\_STATS(dev).bit1\_error;

1648}

1649#endif /\* CONFIG\_CAN\_STATS \*/

1650

[ 1663](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_stuff\_errors](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38)(const struct [device](structdevice.md) \*dev);

1664

1665#ifdef CONFIG\_CAN\_STATS

1666static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_stuff\_errors(const struct [device](structdevice.md) \*dev)

1667{

1668 return Z\_CAN\_GET\_STATS(dev).stuff\_error;

1669}

1670#endif /\* CONFIG\_CAN\_STATS \*/

1671

[ 1684](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_crc\_errors](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2)(const struct [device](structdevice.md) \*dev);

1685

1686#ifdef CONFIG\_CAN\_STATS

1687static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_crc\_errors(const struct [device](structdevice.md) \*dev)

1688{

1689 return Z\_CAN\_GET\_STATS(dev).crc\_error;

1690}

1691#endif /\* CONFIG\_CAN\_STATS \*/

1692

[ 1705](group__can__interface.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_form\_errors](group__can__interface.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)(const struct [device](structdevice.md) \*dev);

1706

1707#ifdef CONFIG\_CAN\_STATS

1708static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_form\_errors(const struct [device](structdevice.md) \*dev)

1709{

1710 return Z\_CAN\_GET\_STATS(dev).form\_error;

1711}

1712#endif /\* CONFIG\_CAN\_STATS \*/

1713

[ 1726](group__can__interface.md#ga4f8414d64b75d4d1ffb7a0feff36f698)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_ack\_errors](group__can__interface.md#ga4f8414d64b75d4d1ffb7a0feff36f698)(const struct [device](structdevice.md) \*dev);

1727

1728#ifdef CONFIG\_CAN\_STATS

1729static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_ack\_errors(const struct [device](structdevice.md) \*dev)

1730{

1731 return Z\_CAN\_GET\_STATS(dev).ack\_error;

1732}

1733#endif /\* CONFIG\_CAN\_STATS \*/

1734

[ 1748](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_rx\_overruns](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)(const struct [device](structdevice.md) \*dev);

1749

1750#ifdef CONFIG\_CAN\_STATS

1751static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_rx\_overruns(const struct [device](structdevice.md) \*dev)

1752{

1753 return Z\_CAN\_GET\_STATS(dev).rx\_overrun;

1754}

1755#endif /\* CONFIG\_CAN\_STATS \*/

1756

1758

1764

[ 1772](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlc)

1773{

1774 static const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlc\_table[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 12,

1775 16, 20, 24, 32, 48, 64};

1776

1777 return dlc\_table[[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(dlc, [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(dlc\_table) - 1)];

1778}

1779

[ 1787](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [can\_bytes\_to\_dlc](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_bytes)

1788{

1789 return num\_bytes <= 8 ? num\_bytes :

1790 num\_bytes <= 12 ? 9 :

1791 num\_bytes <= 16 ? 10 :

1792 num\_bytes <= 20 ? 11 :

1793 num\_bytes <= 24 ? 12 :

1794 num\_bytes <= 32 ? 13 :

1795 num\_bytes <= 48 ? 14 :

1796 15;

1797}

1798

[ 1806](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)static inline bool [can\_frame\_matches\_filter](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)(const struct [can\_frame](structcan__frame.md) \*frame,

1807 const struct [can\_filter](structcan__filter.md) \*filter)

1808{

1809 if ((frame->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)) != 0 && (filter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) & [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)) == 0) {

1810 /\* Extended (29-bit) ID frame, standard (11-bit) filter \*/

1811 return false;

1812 }

1813

1814 if ((frame->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)) == 0 && (filter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) & [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)) != 0) {

1815 /\* Standard (11-bit) ID frame, extended (29-bit) filter \*/

1816 return false;

1817 }

1818

1819 if ((frame->[id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d) ^ filter->[id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9)) & filter->[mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94)) {

1820 /\* Masked ID mismatch \*/

1821 return false;

1822 }

1823

1824 return true;

1825}

1826

1828

1832

1833#ifdef \_\_cplusplus

1834}

1835#endif

1836

1837#include <zephyr/syscalls/can.h>

1838

1839#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:867

[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)

void(\* can\_state\_change\_callback\_t)(const struct device \*dev, enum can\_state state, struct can\_bus\_err\_cnt err\_cnt, void \*user\_data)

Defines the state change callback handler function signature.

**Definition** can.h:312

[can\_set\_bitrate](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b)

int can\_set\_bitrate(const struct device \*dev, uint32\_t bitrate)

Set the bitrate of the CAN controller.

[can\_set\_bitrate\_data](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7)

int can\_set\_bitrate\_data(const struct device \*dev, uint32\_t bitrate\_data)

Set the bitrate for the data phase of the CAN FD controller.

[can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)

uint32\_t can\_mode\_t

Provides a type to hold CAN controller configuration flags.

**Definition** can.h:125

[can\_stats\_get\_stuff\_errors](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38)

uint32\_t can\_stats\_get\_stuff\_errors(const struct device \*dev)

Get the stuffing error counter for a CAN device.

[can\_stop](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5)

int can\_stop(const struct device \*dev)

Stop the CAN controller.

[can\_set\_timing](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da)

int can\_set\_timing(const struct device \*dev, const struct can\_timing \*timing)

Configure the bus timing of a CAN controller.

[can\_get\_bitrate\_max](group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457)

uint32\_t can\_get\_bitrate\_max(const struct device \*dev)

Get maximum supported bitrate.

[can\_stats\_get\_bit\_errors](group__can__interface.md#ga27b277f3b5146590f159171f602904db)

uint32\_t can\_stats\_get\_bit\_errors(const struct device \*dev)

Get the bit error counter for a CAN device.

[can\_stats\_get\_crc\_errors](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2)

uint32\_t can\_stats\_get\_crc\_errors(const struct device \*dev)

Get the CRC error counter for a CAN device.

[can\_get\_bitrate\_min](group__can__interface.md#ga343456749eec6144a91bacae0d94b114)

uint32\_t can\_get\_bitrate\_min(const struct device \*dev)

Get minimum supported bitrate.

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

**Definition** can.h:1787

[can\_stats\_get\_rx\_overruns](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)

uint32\_t can\_stats\_get\_rx\_overruns(const struct device \*dev)

Get the RX overrun counter for a CAN device.

[CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)

#define CAN\_FRAME\_IDE

Frame uses extended (29-bit) CAN ID.

**Definition** can.h:151

[can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)

static uint8\_t can\_dlc\_to\_bytes(uint8\_t dlc)

Convert from Data Length Code (DLC) to the number of data bytes.

**Definition** can.h:1772

[can\_add\_rx\_filter\_msgq](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)

int can\_add\_rx\_filter\_msgq(const struct device \*dev, struct k\_msgq \*msgq, const struct can\_filter \*filter)

Simple wrapper function for adding a message queue for a given filter.

[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)

void(\* can\_rx\_callback\_t)(const struct device \*dev, struct can\_frame \*frame, void \*user\_data)

Defines the application callback handler function signature for receiving.

**Definition** can.h:301

[can\_frame\_matches\_filter](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)

static bool can\_frame\_matches\_filter(const struct can\_frame \*frame, const struct can\_filter \*filter)

Check if a CAN frame matches a CAN filter.

**Definition** can.h:1806

[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)

void(\* can\_tx\_callback\_t)(const struct device \*dev, int error, void \*user\_data)

Defines the application callback handler function signature.

**Definition** can.h:292

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

**Definition** can.h:130

[can\_set\_state\_change\_callback](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e)

static void can\_set\_state\_change\_callback(const struct device \*dev, can\_state\_change\_callback\_t callback, void \*user\_data)

Set a callback for CAN controller state change events.

**Definition** can.h:1567

[can\_get\_max\_bitrate](group__can__interface.md#gad3f929b2170f27b1cbe37a1caccb2e37)

static int can\_get\_max\_bitrate(const struct device \*dev, uint32\_t \*max\_bitrate)

Get maximum supported bitrate.

**Definition** can.h:934

[can\_get\_transceiver](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a)

const struct device \* can\_get\_transceiver(const struct device \*dev)

Get the CAN transceiver associated with the CAN controller.

[can\_set\_mode](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f)

int can\_set\_mode(const struct device \*dev, can\_mode\_t mode)

Set the CAN controller to the given operation mode.

[can\_start](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a)

int can\_start(const struct device \*dev)

Start the CAN controller.

[can\_add\_rx\_filter](group__can__interface.md#gae9dd69a13b960f773ab07bb0bb13b5e9)

int can\_add\_rx\_filter(const struct device \*dev, can\_rx\_callback\_t callback, void \*user\_data, const struct can\_filter \*filter)

Add a callback function for a given CAN filter.

[can\_get\_min\_bitrate](group__can__interface.md#gaef00151aad8c47fef798d53140ea7296)

static int can\_get\_min\_bitrate(const struct device \*dev, uint32\_t \*min\_bitrate)

Get minimum supported bitrate.

**Definition** can.h:880

[CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)

#define CAN\_FILTER\_IDE

Filter matches frames with extended (29-bit) CAN IDs.

**Definition** can.h:211

[CAN\_STATE\_ERROR\_ACTIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c)

@ CAN\_STATE\_ERROR\_ACTIVE

Error-active state (RX/TX error count < 96).

**Definition** can.h:132

[CAN\_STATE\_ERROR\_WARNING](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff)

@ CAN\_STATE\_ERROR\_WARNING

Error-warning state (RX/TX error count < 128).

**Definition** can.h:134

[CAN\_STATE\_STOPPED](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)

@ CAN\_STATE\_STOPPED

CAN controller is stopped and does not participate in CAN communication.

**Definition** can.h:140

[CAN\_STATE\_BUS\_OFF](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959)

@ CAN\_STATE\_BUS\_OFF

Bus-off state (RX/TX error count >= 256).

**Definition** can.h:138

[CAN\_STATE\_ERROR\_PASSIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae)

@ CAN\_STATE\_ERROR\_PASSIVE

Error-passive state (RX/TX error count < 256).

**Definition** can.h:136

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)

#define MIN(a, b)

Obtain the minimum of two values.

**Definition** util.h:400

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:352

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

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

**Definition** can.h:232

[can\_bus\_err\_cnt::tx\_err\_cnt](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98)

uint8\_t tx\_err\_cnt

Value of the CAN controller transmit error counter.

**Definition** can.h:234

[can\_bus\_err\_cnt::rx\_err\_cnt](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a)

uint8\_t rx\_err\_cnt

Value of the CAN controller receive error counter.

**Definition** can.h:236

[can\_device\_state](structcan__device__state.md)

CAN specific device state which allows for CAN device class specific additions.

**Definition** can.h:577

[can\_device\_state::devstate](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec)

struct device\_state devstate

Common device state.

**Definition** can.h:579

[can\_device\_state::stats](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47)

struct stats\_can stats

CAN device statistics.

**Definition** can.h:581

[can\_filter](structcan__filter.md)

CAN filter structure.

**Definition** can.h:218

[can\_filter::mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94)

uint32\_t mask

CAN identifier matching mask.

**Definition** can.h:224

[can\_filter::flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de)

uint8\_t flags

Flags.

**Definition** can.h:226

[can\_filter::id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9)

uint32\_t id

CAN identifier to match.

**Definition** can.h:220

[can\_frame](structcan__frame.md)

CAN frame structure.

**Definition** can.h:172

[can\_frame::dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47)

uint8\_t dlc

Data Length Code (DLC) indicating data length in bytes.

**Definition** can.h:176

[can\_frame::flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c)

uint8\_t flags

Flags.

**Definition** can.h:178

[can\_frame::id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d)

uint32\_t id

Standard (11-bit) or extended (29-bit) CAN identifier.

**Definition** can.h:174

[can\_frame::data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)

uint8\_t data[CAN\_MAX\_DLEN]

Payload data accessed as unsigned 8 bit values.

**Definition** can.h:197

[can\_frame::data\_32](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a)

uint32\_t data\_32[DIV\_ROUND\_UP(CAN\_MAX\_DLEN, sizeof(uint32\_t))]

Payload data accessed as unsigned 32 bit values.

**Definition** can.h:199

[can\_frame::timestamp](structcan__frame.md#ae46f8b0821c638517959274bbbda5932)

uint16\_t timestamp

Captured value of the free-running timer in the CAN controller when this frame was received.

**Definition** can.h:187

[can\_timing](structcan__timing.md)

CAN bus timing structure.

**Definition** can.h:271

[can\_timing::sjw](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5)

uint16\_t sjw

Synchronisation jump width.

**Definition** can.h:273

[can\_timing::phase\_seg2](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6)

uint16\_t phase\_seg2

Phase segment 2.

**Definition** can.h:279

[can\_timing::prescaler](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a)

uint16\_t prescaler

Prescaler value.

**Definition** can.h:281

[can\_timing::phase\_seg1](structcan__timing.md#a9941688e79fa4ce01c4b498433319089)

uint16\_t phase\_seg1

Phase segment 1.

**Definition** can.h:277

[can\_timing::prop\_seg](structcan__timing.md#ac009d40fee9788b663963978498b2ee9)

uint16\_t prop\_seg

Propagation segment.

**Definition** can.h:275

[device\_state](structdevice__state.md)

Runtime device dynamic structure (in RAM) per driver instance.

**Definition** device.h:380

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:422

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:416

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4503

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[util.h](sys_2util_8h.md)

Misc utilities.

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can.h](drivers_2can_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
