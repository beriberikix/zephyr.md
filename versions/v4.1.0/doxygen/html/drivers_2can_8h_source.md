---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2can_8h_source.html
original_path: doxygen/html/drivers_2can_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

48

[ 52](group__can__interface.md#ga15ee71e8abcf51008925585049125986)#define CAN\_EXT\_ID\_MASK 0x1FFFFFFFU

53

[ 57](group__can__interface.md#gadc209a027ee700faf10461e2417bee50)#define CAN\_MAX\_DLC 8U

58

[ 62](group__can__interface.md#gad4b7310536c7e3252c2056abe64c0333)#define CANFD\_MAX\_DLC 15U

63

68#ifndef CONFIG\_CAN\_FD\_MODE

69#define CAN\_MAX\_DLEN 8U

70#else

71#define CAN\_MAX\_DLEN 64U

72#endif /\* CONFIG\_CAN\_FD\_MODE \*/

73

75

77

84

[ 86](group__can__interface.md#ga89cd5ea2e9d70a51bc12b100be28ca3d)#define CAN\_MODE\_NORMAL 0

87

[ 89](group__can__interface.md#ga891031afc77974a041accb3d0ceb21bb)#define CAN\_MODE\_LOOPBACK BIT(0)

90

[ 92](group__can__interface.md#ga117d04b9118a1b3f839c557ef6b596cb)#define CAN\_MODE\_LISTENONLY BIT(1)

93

[ 95](group__can__interface.md#gabb4d99736d8386a5ab62a5e44374d13a)#define CAN\_MODE\_FD BIT(2)

96

[ 98](group__can__interface.md#ga033d7ade1966299c7e6249b945f38202)#define CAN\_MODE\_ONE\_SHOT BIT(3)

99

[ 101](group__can__interface.md#gaf0821983174ad781e1bb63a976a18fab)#define CAN\_MODE\_3\_SAMPLES BIT(4)

102

[ 104](group__can__interface.md#ga3d8675253125b2af2bd22f0b2cc60cdd)#define CAN\_MODE\_MANUAL\_RECOVERY BIT(5)

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

[ 165](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d);

[ 167](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47);

[ 169](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c);

170#if defined(CONFIG\_CAN\_RX\_TIMESTAMP) || defined(\_\_DOXYGEN\_\_)

[ 178](structcan__frame.md#ae46f8b0821c638517959274bbbda5932) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timestamp](structcan__frame.md#ae46f8b0821c638517959274bbbda5932);

179#else

182 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reserved;

184#endif

186 union {

[ 188](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)[CAN\_MAX\_DLEN];

[ 190](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_32](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a)[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(CAN\_MAX\_DLEN, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)))];

191 };

192};

193

200

[ 202](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)#define CAN\_FILTER\_IDE BIT(0)

203

205

[ 209](structcan__filter.md)struct [can\_filter](structcan__filter.md) {

[ 211](structcan__filter.md#adf2b18eab11d360780707478a1f624b9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9);

[ 215](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94);

[ 217](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de);

218};

219

[ 223](structcan__bus__err__cnt.md)struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) {

[ 225](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_err\_cnt](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98);

[ 227](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_err\_cnt](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a);

228};

229

[ 262](structcan__timing.md)struct [can\_timing](structcan__timing.md) {

[ 264](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sjw](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5);

[ 266](structcan__timing.md#ac009d40fee9788b663963978498b2ee9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [prop\_seg](structcan__timing.md#ac009d40fee9788b663963978498b2ee9);

[ 268](structcan__timing.md#a9941688e79fa4ce01c4b498433319089) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phase\_seg1](structcan__timing.md#a9941688e79fa4ce01c4b498433319089);

[ 270](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phase\_seg2](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6);

[ 272](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [prescaler](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a);

273};

274

[ 283](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)typedef void (\*[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca))(const struct [device](structdevice.md) \*dev, int error, void \*user\_data);

284

[ 292](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)typedef void (\*[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f))(const struct [device](structdevice.md) \*dev, struct [can\_frame](structcan__frame.md) \*frame,

293 void \*user\_data);

294

[ 303](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)typedef void (\*[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d))(const struct [device](structdevice.md) \*dev,

304 enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

305 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) err\_cnt,

306 void \*user\_data);

307

313

327#define CAN\_CALC\_TDCO(\_timing\_data, \_tdco\_min, \_tdco\_max) \

328 CLAMP((1U + \_timing\_data->prop\_seg + \_timing\_data->phase\_seg1) \* \_timing\_data->prescaler, \

329 \_tdco\_min, \_tdco\_max)

330

337struct can\_driver\_config {

339 const struct [device](structdevice.md) \*phy;

341 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) min\_bitrate;

343 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_bitrate;

345 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate;

347 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_point;

348#ifdef CONFIG\_CAN\_FD\_MODE

350 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_point\_data;

352 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate\_data;

353#endif /\* CONFIG\_CAN\_FD\_MODE \*/

354};

355

363#define CAN\_DT\_DRIVER\_CONFIG\_GET(node\_id, \_min\_bitrate, \_max\_bitrate) \

364 { \

365 .phy = DEVICE\_DT\_GET\_OR\_NULL(DT\_PHANDLE(node\_id, phys)), \

366 .min\_bitrate = DT\_CAN\_TRANSCEIVER\_MIN\_BITRATE(node\_id, \_min\_bitrate), \

367 .max\_bitrate = DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE(node\_id, \_max\_bitrate), \

368 .bitrate = DT\_PROP\_OR(node\_id, bitrate, \

369 DT\_PROP\_OR(node\_id, bus\_speed, CONFIG\_CAN\_DEFAULT\_BITRATE)), \

370 .sample\_point = DT\_PROP\_OR(node\_id, sample\_point, 0), \

371 IF\_ENABLED(CONFIG\_CAN\_FD\_MODE, \

372 (.bitrate\_data = DT\_PROP\_OR(node\_id, bitrate\_data, \

373 DT\_PROP\_OR(node\_id, bus\_speed\_data, CONFIG\_CAN\_DEFAULT\_BITRATE\_DATA)), \

374 .sample\_point\_data = DT\_PROP\_OR(node\_id, sample\_point\_data, 0),)) \

375 }

376

385#define CAN\_DT\_DRIVER\_CONFIG\_INST\_GET(inst, \_min\_bitrate, \_max\_bitrate) \

386 CAN\_DT\_DRIVER\_CONFIG\_GET(DT\_DRV\_INST(inst), \_min\_bitrate, \_max\_bitrate)

387

394struct can\_driver\_data {

396 [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode;

398 bool started;

400 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) state\_change\_cb;

402 void \*state\_change\_cb\_user\_data;

403};

404

409typedef int (\*can\_set\_timing\_t)(const struct [device](structdevice.md) \*dev,

410 const struct [can\_timing](structcan__timing.md) \*timing);

411

416typedef int (\*can\_set\_timing\_data\_t)(const struct [device](structdevice.md) \*dev,

417 const struct [can\_timing](structcan__timing.md) \*timing\_data);

418

423typedef int (\*can\_get\_capabilities\_t)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap);

424

429typedef int (\*can\_start\_t)(const struct [device](structdevice.md) \*dev);

430

435typedef int (\*can\_stop\_t)(const struct [device](structdevice.md) \*dev);

436

441typedef int (\*can\_set\_mode\_t)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

442

450typedef int (\*can\_send\_t)(const struct [device](structdevice.md) \*dev,

451 const struct [can\_frame](structcan__frame.md) \*frame,

452 [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback,

453 void \*user\_data);

454

459typedef int (\*can\_add\_rx\_filter\_t)(const struct [device](structdevice.md) \*dev,

460 [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback,

461 void \*user\_data,

462 const struct [can\_filter](structcan__filter.md) \*filter);

463

468typedef void (\*can\_remove\_rx\_filter\_t)(const struct [device](structdevice.md) \*dev, int filter\_id);

469

474typedef int (\*can\_recover\_t)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

475

480typedef int (\*can\_get\_state\_t)(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

481 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt);

482

487typedef void(\*can\_set\_state\_change\_callback\_t)(const struct [device](structdevice.md) \*dev,

488 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback,

489 void \*user\_data);

490

495typedef int (\*can\_get\_core\_clock\_t)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

496

501typedef int (\*can\_get\_max\_filters\_t)(const struct [device](structdevice.md) \*dev, bool ide);

502

503\_\_subsystem struct can\_driver\_api {

504 can\_get\_capabilities\_t get\_capabilities;

505 can\_start\_t start;

506 can\_stop\_t stop;

507 can\_set\_mode\_t set\_mode;

508 can\_set\_timing\_t set\_timing;

509 can\_send\_t [send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f);

510 can\_add\_rx\_filter\_t add\_rx\_filter;

511 can\_remove\_rx\_filter\_t remove\_rx\_filter;

512#if defined(CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE) || defined(\_\_DOXYGEN\_\_)

513 can\_recover\_t recover;

514#endif /\* CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE \*/

515 can\_get\_state\_t get\_state;

516 can\_set\_state\_change\_callback\_t set\_state\_change\_callback;

517 can\_get\_core\_clock\_t get\_core\_clock;

518 can\_get\_max\_filters\_t get\_max\_filters;

519 /\* Min values for the timing registers \*/

520 struct can\_timing timing\_min;

521 /\* Max values for the timing registers \*/

522 struct can\_timing timing\_max;

523#if defined(CONFIG\_CAN\_FD\_MODE) || defined(\_\_DOXYGEN\_\_)

524 can\_set\_timing\_data\_t set\_timing\_data;

525 /\* Min values for the timing registers during the data phase \*/

526 struct can\_timing timing\_data\_min;

527 /\* Max values for the timing registers during the data phase \*/

528 struct can\_timing timing\_data\_max;

529#endif /\* CONFIG\_CAN\_FD\_MODE \*/

530};

531

533

534#if defined(CONFIG\_CAN\_STATS) || defined(\_\_DOXYGEN\_\_)

535

536#include <[zephyr/stats/stats.h](stats_2stats_8h.md)>

537

539

540[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(can)

541[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit\_error)

542[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit0\_error)

543[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bit1\_error)

544[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(stuff\_error)

545[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(crc\_error)

546[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(form\_error)

547[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(ack\_error)

548[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(rx\_overrun)

549[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

550

551[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(can)

552[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit\_error)

553[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit0\_error)

554[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, bit1\_error)

555[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, stuff\_error)

556[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, crc\_error)

557[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, form\_error)

558[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, ack\_error)

559[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(can, rx\_overrun)

560[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(can);

561

563

[ 568](structcan__device__state.md)struct [can\_device\_state](structcan__device__state.md) {

[ 570](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec) struct [device\_state](structdevice__state.md) [devstate](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec);

[ 572](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47) struct stats\_can [stats](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47);

573};

574

576

580#define Z\_CAN\_GET\_STATS(dev\_) \

581 CONTAINER\_OF(dev\_->state, struct can\_device\_state, devstate)->stats

582

584

[ 601](group__can__interface.md#gaf6f7efa9d99f44af6f58352f558d7fec)#define CAN\_STATS\_BIT\_ERROR\_INC(dev\_) \

602 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit\_error)

603

[ 615](group__can__interface.md#ga120a37d5ae5064dcbf116e488f733764)#define CAN\_STATS\_BIT0\_ERROR\_INC(dev\_) \

616 do { \

617 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit0\_error); \

618 CAN\_STATS\_BIT\_ERROR\_INC(dev\_); \

619 } while (0)

620

[ 632](group__can__interface.md#ga678b74039632302efcb5ef80f0e3a90b)#define CAN\_STATS\_BIT1\_ERROR\_INC(dev\_) \

633 do { \

634 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit1\_error); \

635 CAN\_STATS\_BIT\_ERROR\_INC(dev\_); \

636 } while (0)

637

[ 646](group__can__interface.md#gae4146843944b7ffb1c96636e889282f7)#define CAN\_STATS\_STUFF\_ERROR\_INC(dev\_) \

647 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), stuff\_error)

648

[ 657](group__can__interface.md#ga125ce05d40881476f5f156ad5e28c664)#define CAN\_STATS\_CRC\_ERROR\_INC(dev\_) \

658 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), crc\_error)

659

[ 668](group__can__interface.md#gac5809b3f5e1a463822e76921cddc9909)#define CAN\_STATS\_FORM\_ERROR\_INC(dev\_) \

669 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), form\_error)

670

[ 679](group__can__interface.md#ga15f7ca18badbbe2fe24be68cacce6171)#define CAN\_STATS\_ACK\_ERROR\_INC(dev\_) \

680 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), ack\_error)

681

[ 691](group__can__interface.md#ga95fe455780b38c7202b48bc6004e6f4d)#define CAN\_STATS\_RX\_OVERRUN\_INC(dev\_) \

692 STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), rx\_overrun)

693

[ 702](group__can__interface.md#ga06a9058924901e2d960858fb9e3a4a02)#define CAN\_STATS\_RESET(dev\_) \

703 stats\_reset(&(Z\_CAN\_GET\_STATS(dev\_).s\_hdr))

704

706

710#define Z\_CAN\_DEVICE\_STATE\_DEFINE(dev\_id) \

711 static struct can\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_id) \

712 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

713

720#define Z\_CAN\_INIT\_FN(dev\_id, init\_fn) \

721 static inline int UTIL\_CAT(dev\_id, \_init)(const struct device \*dev) \

722 { \

723 struct can\_device\_state \*state = \

724 CONTAINER\_OF(dev->state, struct can\_device\_state, devstate); \

725 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 8, \

726 STATS\_NAME\_INIT\_PARMS(can)); \

727 stats\_register(dev->name, &(state->stats.s\_hdr)); \

728 if (!is\_null\_no\_warn(init\_fn)) { \

729 return init\_fn(dev); \

730 } \

731 \

732 return 0; \

733 }

734

736

[ 757](group__can__interface.md#ga599d0695abe481411660d7af2893f4a5)#define CAN\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

758 prio, api, ...) \

759 Z\_CAN\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

760 Z\_CAN\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

761 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

762 DEVICE\_DT\_NAME(node\_id), \

763 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

764 pm, data, config, level, prio, api, \

765 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

766 \_\_VA\_ARGS\_\_)

767

768#else /\* CONFIG\_CAN\_STATS \*/

769

770#define CAN\_STATS\_BIT\_ERROR\_INC(dev\_)

771#define CAN\_STATS\_BIT0\_ERROR\_INC(dev\_)

772#define CAN\_STATS\_BIT1\_ERROR\_INC(dev\_)

773#define CAN\_STATS\_STUFF\_ERROR\_INC(dev\_)

774#define CAN\_STATS\_CRC\_ERROR\_INC(dev\_)

775#define CAN\_STATS\_FORM\_ERROR\_INC(dev\_)

776#define CAN\_STATS\_ACK\_ERROR\_INC(dev\_)

777#define CAN\_STATS\_RX\_OVERRUN\_INC(dev\_)

778#define CAN\_STATS\_RESET(dev\_)

779

780#define CAN\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

781 prio, api, ...) \

782 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

783 prio, api, \_\_VA\_ARGS\_\_)

784

785#endif /\* CONFIG\_CAN\_STATS \*/

786

[ 794](group__can__interface.md#ga20266dc5e962922144e078b85ccb8351)#define CAN\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

795 CAN\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

796

802

[ 815](group__can__interface.md#ga4af6d0d9ab72b195909f511ac65cb8fa)\_\_syscall int [can\_get\_core\_clock](group__can__interface.md#ga4af6d0d9ab72b195909f511ac65cb8fa)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

816

817static inline int z\_impl\_can\_get\_core\_clock(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate)

818{

819 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

820

821 return api->get\_core\_clock(dev, rate);

822}

823

[ 840](group__can__interface.md#ga343456749eec6144a91bacae0d94b114)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_get\_bitrate\_min](group__can__interface.md#ga343456749eec6144a91bacae0d94b114)(const struct [device](structdevice.md) \*dev);

841

842static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_get\_bitrate\_min(const struct [device](structdevice.md) \*dev)

843{

844 const struct can\_driver\_config \*common = (const struct can\_driver\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

845

846 return common->min\_bitrate;

847}

848

[ 865](group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_get\_bitrate\_max](group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457)(const struct [device](structdevice.md) \*dev);

866

867static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_get\_bitrate\_max(const struct [device](structdevice.md) \*dev)

868{

869 const struct can\_driver\_config \*common = (const struct can\_driver\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

870

871 return common->max\_bitrate;

872}

873

[ 881](group__can__interface.md#ga5a57627de4764f0bd3b4bafe07f56e6f)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_min](group__can__interface.md#ga5a57627de4764f0bd3b4bafe07f56e6f)(const struct [device](structdevice.md) \*dev);

882

883static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_min(const struct [device](structdevice.md) \*dev)

884{

885 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

886

887 return &api->timing\_min;

888}

889

[ 897](group__can__interface.md#gabe385d0f003b1e990c78ef7a2a3f9616)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_max](group__can__interface.md#gabe385d0f003b1e990c78ef7a2a3f9616)(const struct [device](structdevice.md) \*dev);

898

899static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_max(const struct [device](structdevice.md) \*dev)

900{

901 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

902

903 return &api->timing\_max;

904}

905

[ 932](group__can__interface.md#gac27fe64142603f0d32d422594356b2d7)\_\_syscall int [can\_calc\_timing](group__can__interface.md#gac27fe64142603f0d32d422594356b2d7)(const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res,

933 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt);

934

[ 948](group__can__interface.md#ga6399ef0cefdab3da738136f8a5c59c2f)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_data\_min](group__can__interface.md#ga6399ef0cefdab3da738136f8a5c59c2f)(const struct [device](structdevice.md) \*dev);

949

950#ifdef CONFIG\_CAN\_FD\_MODE

951static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_data\_min(const struct [device](structdevice.md) \*dev)

952{

953 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

954

955 return &api->timing\_data\_min;

956}

957#endif /\* CONFIG\_CAN\_FD\_MODE \*/

958

[ 972](group__can__interface.md#ga47a2f6d6b42121b390aa92160c833b80)\_\_syscall const struct [can\_timing](structcan__timing.md) \*[can\_get\_timing\_data\_max](group__can__interface.md#ga47a2f6d6b42121b390aa92160c833b80)(const struct [device](structdevice.md) \*dev);

973

974#ifdef CONFIG\_CAN\_FD\_MODE

975static inline const struct [can\_timing](structcan__timing.md) \*z\_impl\_can\_get\_timing\_data\_max(const struct [device](structdevice.md) \*dev)

976{

977 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

978

979 return &api->timing\_data\_max;

980}

981#endif /\* CONFIG\_CAN\_FD\_MODE \*/

982

[ 1003](group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11)\_\_syscall int [can\_calc\_timing\_data](group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11)(const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res,

1004 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt);

1005

[ 1023](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2)\_\_syscall int [can\_set\_timing\_data](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2)(const struct [device](structdevice.md) \*dev,

1024 const struct [can\_timing](structcan__timing.md) \*timing\_data);

1025

[ 1054](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7)\_\_syscall int [can\_set\_bitrate\_data](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate\_data);

1055

[ 1069](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da)\_\_syscall int [can\_set\_timing](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da)(const struct [device](structdevice.md) \*dev,

1070 const struct [can\_timing](structcan__timing.md) \*timing);

1071

[ 1085](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168)\_\_syscall int [can\_get\_capabilities](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap);

1086

1087static inline int z\_impl\_can\_get\_capabilities(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap)

1088{

1089 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1090

1091 return api->get\_capabilities(dev, cap);

1092}

1093

[ 1103](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a)\_\_syscall const struct [device](structdevice.md) \*[can\_get\_transceiver](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a)(const struct [device](structdevice.md) \*dev);

1104

1105static const struct [device](structdevice.md) \*z\_impl\_can\_get\_transceiver(const struct [device](structdevice.md) \*dev)

1106{

1107 const struct can\_driver\_config \*common = (const struct can\_driver\_config \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1108

1109 return common->phy;

1110}

1111

[ 1129](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a)\_\_syscall int [can\_start](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a)(const struct [device](structdevice.md) \*dev);

1130

1131static inline int z\_impl\_can\_start(const struct [device](structdevice.md) \*dev)

1132{

1133 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1134

1135 return api->start(dev);

1136}

1137

[ 1153](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5)\_\_syscall int [can\_stop](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5)(const struct [device](structdevice.md) \*dev);

1154

1155static inline int z\_impl\_can\_stop(const struct [device](structdevice.md) \*dev)

1156{

1157 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1158

1159 return api->stop(dev);

1160}

1161

[ 1172](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f)\_\_syscall int [can\_set\_mode](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

1173

1174static inline int z\_impl\_can\_set\_mode(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode)

1175{

1176 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1177

1178 return api->set\_mode(dev, mode);

1179}

1180

[ 1188](group__can__interface.md#gabd201b5b1fca54048985a8a24dd51e55)\_\_syscall [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) [can\_get\_mode](group__can__interface.md#gabd201b5b1fca54048985a8a24dd51e55)(const struct [device](structdevice.md) \*dev);

1189

1190static inline [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) z\_impl\_can\_get\_mode(const struct [device](structdevice.md) \*dev)

1191{

1192 const struct can\_driver\_data \*common = (const struct can\_driver\_data \*)dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

1193

1194 return common->mode;

1195}

1196

[ 1222](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b)\_\_syscall int [can\_set\_bitrate](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate);

1223

1225

1231

[ 1276](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5)\_\_syscall int [can\_send](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5)(const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame,

1277 [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback,

1278 void \*user\_data);

1279

1281

1287

[ 1311](group__can__interface.md#gae9dd69a13b960f773ab07bb0bb13b5e9)int [can\_add\_rx\_filter](group__can__interface.md#gae9dd69a13b960f773ab07bb0bb13b5e9)(const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback,

1312 void \*user\_data, const struct [can\_filter](structcan__filter.md) \*filter);

1313

[ 1324](group__can__interface.md#ga7af0acdfbdad07fc3eba4cbd29bc090b)#define CAN\_MSGQ\_DEFINE(name, max\_frames) \

1325 K\_MSGQ\_DEFINE(name, sizeof(struct can\_frame), max\_frames, 4)

1326

[ 1353](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)\_\_syscall int [can\_add\_rx\_filter\_msgq](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)(const struct [device](structdevice.md) \*dev, struct [k\_msgq](structk__msgq.md) \*msgq,

1354 const struct [can\_filter](structcan__filter.md) \*filter);

1355

[ 1365](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847)\_\_syscall void [can\_remove\_rx\_filter](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847)(const struct [device](structdevice.md) \*dev, int filter\_id);

1366

1367static inline void z\_impl\_can\_remove\_rx\_filter(const struct [device](structdevice.md) \*dev, int filter\_id)

1368{

1369 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1370

1371 api->remove\_rx\_filter(dev, filter\_id);

1372}

1373

[ 1387](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc)\_\_syscall int [can\_get\_max\_filters](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc)(const struct [device](structdevice.md) \*dev, bool ide);

1388

1389static inline int z\_impl\_can\_get\_max\_filters(const struct [device](structdevice.md) \*dev, bool ide)

1390{

1391 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1392

1393 if (api->get\_max\_filters == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1394 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1395 }

1396

1397 return api->get\_max\_filters(dev, ide);

1398}

1399

1401

1407

[ 1421](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857)\_\_syscall int [can\_get\_state](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857)(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1422 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt);

1423

1424static inline int z\_impl\_can\_get\_state(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1425 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt)

1426{

1427 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1428

1429 return api->get\_state(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), err\_cnt);

1430}

1431

[ 1449](group__can__interface.md#gac474e56a50685736a1c25dca277aab5e)\_\_syscall int [can\_recover](group__can__interface.md#gac474e56a50685736a1c25dca277aab5e)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

1450

1451#ifdef CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE

1452static inline int z\_impl\_can\_recover(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout)

1453{

1454 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1455

1456 if (api->recover == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1457 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1458 }

1459

1460 return api->recover(dev, timeout);

1461}

1462#endif /\* CONFIG\_CAN\_MANUAL\_RECOVERY\_MODE \*/

1463

[ 1477](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e)static inline void [can\_set\_state\_change\_callback](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e)(const struct [device](structdevice.md) \*dev,

1478 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback,

1479 void \*user\_data)

1480{

1481 const struct can\_driver\_api \*api = (const struct can\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1482

1483 api->set\_state\_change\_callback(dev, callback, user\_data);

1484}

1485

1487

1493

[ 1506](group__can__interface.md#ga27b277f3b5146590f159171f602904db)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit\_errors](group__can__interface.md#ga27b277f3b5146590f159171f602904db)(const struct [device](structdevice.md) \*dev);

1507

1508#ifdef CONFIG\_CAN\_STATS

1509static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit\_errors(const struct [device](structdevice.md) \*dev)

1510{

1511 return Z\_CAN\_GET\_STATS(dev).bit\_error;

1512}

1513#endif /\* CONFIG\_CAN\_STATS \*/

1514

[ 1529](group__can__interface.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit0\_errors](group__can__interface.md#ga7c380f6c4a529e5b5e6010ab4e6c7680)(const struct [device](structdevice.md) \*dev);

1530

1531#ifdef CONFIG\_CAN\_STATS

1532static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit0\_errors(const struct [device](structdevice.md) \*dev)

1533{

1534 return Z\_CAN\_GET\_STATS(dev).bit0\_error;

1535}

1536#endif /\* CONFIG\_CAN\_STATS \*/

1537

[ 1552](group__can__interface.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_bit1\_errors](group__can__interface.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)(const struct [device](structdevice.md) \*dev);

1553

1554#ifdef CONFIG\_CAN\_STATS

1555static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_bit1\_errors(const struct [device](structdevice.md) \*dev)

1556{

1557 return Z\_CAN\_GET\_STATS(dev).bit1\_error;

1558}

1559#endif /\* CONFIG\_CAN\_STATS \*/

1560

[ 1573](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_stuff\_errors](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38)(const struct [device](structdevice.md) \*dev);

1574

1575#ifdef CONFIG\_CAN\_STATS

1576static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_stuff\_errors(const struct [device](structdevice.md) \*dev)

1577{

1578 return Z\_CAN\_GET\_STATS(dev).stuff\_error;

1579}

1580#endif /\* CONFIG\_CAN\_STATS \*/

1581

[ 1594](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_crc\_errors](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2)(const struct [device](structdevice.md) \*dev);

1595

1596#ifdef CONFIG\_CAN\_STATS

1597static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_crc\_errors(const struct [device](structdevice.md) \*dev)

1598{

1599 return Z\_CAN\_GET\_STATS(dev).crc\_error;

1600}

1601#endif /\* CONFIG\_CAN\_STATS \*/

1602

[ 1615](group__can__interface.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_form\_errors](group__can__interface.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)(const struct [device](structdevice.md) \*dev);

1616

1617#ifdef CONFIG\_CAN\_STATS

1618static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_form\_errors(const struct [device](structdevice.md) \*dev)

1619{

1620 return Z\_CAN\_GET\_STATS(dev).form\_error;

1621}

1622#endif /\* CONFIG\_CAN\_STATS \*/

1623

[ 1636](group__can__interface.md#ga4f8414d64b75d4d1ffb7a0feff36f698)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_ack\_errors](group__can__interface.md#ga4f8414d64b75d4d1ffb7a0feff36f698)(const struct [device](structdevice.md) \*dev);

1637

1638#ifdef CONFIG\_CAN\_STATS

1639static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_ack\_errors(const struct [device](structdevice.md) \*dev)

1640{

1641 return Z\_CAN\_GET\_STATS(dev).ack\_error;

1642}

1643#endif /\* CONFIG\_CAN\_STATS \*/

1644

[ 1658](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_stats\_get\_rx\_overruns](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)(const struct [device](structdevice.md) \*dev);

1659

1660#ifdef CONFIG\_CAN\_STATS

1661static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_can\_stats\_get\_rx\_overruns(const struct [device](structdevice.md) \*dev)

1662{

1663 return Z\_CAN\_GET\_STATS(dev).rx\_overrun;

1664}

1665#endif /\* CONFIG\_CAN\_STATS \*/

1666

1668

1674

[ 1682](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlc)

1683{

1684 static const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlc\_table[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 12,

1685 16, 20, 24, 32, 48, 64};

1686

1687 return dlc\_table[[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(dlc, [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(dlc\_table) - 1)];

1688}

1689

[ 1697](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [can\_bytes\_to\_dlc](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_bytes)

1698{

1699 return num\_bytes <= 8 ? num\_bytes :

1700 num\_bytes <= 12 ? 9 :

1701 num\_bytes <= 16 ? 10 :

1702 num\_bytes <= 20 ? 11 :

1703 num\_bytes <= 24 ? 12 :

1704 num\_bytes <= 32 ? 13 :

1705 num\_bytes <= 48 ? 14 :

1706 15;

1707}

1708

[ 1716](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)static inline bool [can\_frame\_matches\_filter](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)(const struct [can\_frame](structcan__frame.md) \*frame,

1717 const struct [can\_filter](structcan__filter.md) \*filter)

1718{

1719 if ((frame->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)) != 0 && (filter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) & [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)) == 0) {

1720 /\* Extended (29-bit) ID frame, standard (11-bit) filter \*/

1721 return false;

1722 }

1723

1724 if ((frame->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)) == 0 && (filter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) & [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)) != 0) {

1725 /\* Standard (11-bit) ID frame, extended (29-bit) filter \*/

1726 return false;

1727 }

1728

1729 if ((frame->[id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d) ^ filter->[id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9)) & filter->[mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94)) {

1730 /\* Masked ID mismatch \*/

1731 return false;

1732 }

1733

1734 return true;

1735}

1736

1738

1742

1743#ifdef \_\_cplusplus

1744}

1745#endif

1746

1747#include <zephyr/syscalls/can.h>

1748

1749#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)

void(\* can\_state\_change\_callback\_t)(const struct device \*dev, enum can\_state state, struct can\_bus\_err\_cnt err\_cnt, void \*user\_data)

Defines the state change callback handler function signature.

**Definition** can.h:303

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

[can\_remove\_rx\_filter](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847)

void can\_remove\_rx\_filter(const struct device \*dev, int filter\_id)

Remove a CAN RX filter.

[can\_bytes\_to\_dlc](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)

static uint8\_t can\_bytes\_to\_dlc(uint8\_t num\_bytes)

Convert from number of bytes to Data Length Code (DLC).

**Definition** can.h:1697

[can\_stats\_get\_rx\_overruns](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d)

uint32\_t can\_stats\_get\_rx\_overruns(const struct device \*dev)

Get the RX overrun counter for a CAN device.

[CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)

#define CAN\_FRAME\_IDE

Frame uses extended (29-bit) CAN ID.

**Definition** can.h:142

[can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)

static uint8\_t can\_dlc\_to\_bytes(uint8\_t dlc)

Convert from Data Length Code (DLC) to the number of data bytes.

**Definition** can.h:1682

[can\_add\_rx\_filter\_msgq](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c)

int can\_add\_rx\_filter\_msgq(const struct device \*dev, struct k\_msgq \*msgq, const struct can\_filter \*filter)

Simple wrapper function for adding a message queue for a given filter.

[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)

void(\* can\_rx\_callback\_t)(const struct device \*dev, struct can\_frame \*frame, void \*user\_data)

Defines the application callback handler function signature for receiving.

**Definition** can.h:292

[can\_frame\_matches\_filter](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8)

static bool can\_frame\_matches\_filter(const struct can\_frame \*frame, const struct can\_filter \*filter)

Check if a CAN frame matches a CAN filter.

**Definition** can.h:1716

[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)

void(\* can\_tx\_callback\_t)(const struct device \*dev, int error, void \*user\_data)

Defines the application callback handler function signature.

**Definition** can.h:283

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

**Definition** can.h:1477

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

[CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)

#define CAN\_FILTER\_IDE

Filter matches frames with extended (29-bit) CAN IDs.

**Definition** can.h:202

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

**Definition** util.h:401

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

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)

ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

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

**Definition** can.h:223

[can\_bus\_err\_cnt::tx\_err\_cnt](structcan__bus__err__cnt.md#a01bb2cb16656d0fd4f99cfbfa1f30e98)

uint8\_t tx\_err\_cnt

Value of the CAN controller transmit error counter.

**Definition** can.h:225

[can\_bus\_err\_cnt::rx\_err\_cnt](structcan__bus__err__cnt.md#a6be6ce6b592641ba0dce36fe1cd8902a)

uint8\_t rx\_err\_cnt

Value of the CAN controller receive error counter.

**Definition** can.h:227

[can\_device\_state](structcan__device__state.md)

CAN specific device state which allows for CAN device class specific additions.

**Definition** can.h:568

[can\_device\_state::devstate](structcan__device__state.md#a28061ff1193176dd01b7bb9a88f402ec)

struct device\_state devstate

Common device state.

**Definition** can.h:570

[can\_device\_state::stats](structcan__device__state.md#ae05c85eae4f6bee075ffdc4f0ab56f47)

struct stats\_can stats

CAN device statistics.

**Definition** can.h:572

[can\_filter](structcan__filter.md)

CAN filter structure.

**Definition** can.h:209

[can\_filter::mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94)

uint32\_t mask

CAN identifier matching mask.

**Definition** can.h:215

[can\_filter::flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de)

uint8\_t flags

Flags.

**Definition** can.h:217

[can\_filter::id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9)

uint32\_t id

CAN identifier to match.

**Definition** can.h:211

[can\_frame](structcan__frame.md)

CAN frame structure.

**Definition** can.h:163

[can\_frame::dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47)

uint8\_t dlc

Data Length Code (DLC) indicating data length in bytes.

**Definition** can.h:167

[can\_frame::flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c)

uint8\_t flags

Flags.

**Definition** can.h:169

[can\_frame::id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d)

uint32\_t id

Standard (11-bit) or extended (29-bit) CAN identifier.

**Definition** can.h:165

[can\_frame::data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)

uint8\_t data[CAN\_MAX\_DLEN]

Payload data accessed as unsigned 8 bit values.

**Definition** can.h:188

[can\_frame::data\_32](structcan__frame.md#ad88af93a2171e4c9d617b91b403d842a)

uint32\_t data\_32[DIV\_ROUND\_UP(CAN\_MAX\_DLEN, sizeof(uint32\_t))]

Payload data accessed as unsigned 32 bit values.

**Definition** can.h:190

[can\_frame::timestamp](structcan__frame.md#ae46f8b0821c638517959274bbbda5932)

uint16\_t timestamp

Captured value of the free-running timer in the CAN controller when this frame was received.

**Definition** can.h:178

[can\_timing](structcan__timing.md)

CAN bus timing structure.

**Definition** can.h:262

[can\_timing::sjw](structcan__timing.md#a5af76a4ee9c741642ec19265a47fceb5)

uint16\_t sjw

Synchronisation jump width.

**Definition** can.h:264

[can\_timing::phase\_seg2](structcan__timing.md#a6ca0caf618d28a761c3c8859ed3a68d6)

uint16\_t phase\_seg2

Phase segment 2.

**Definition** can.h:270

[can\_timing::prescaler](structcan__timing.md#a74fb8341cbb6d97721c9d0afbc7e1f3a)

uint16\_t prescaler

Prescaler value.

**Definition** can.h:272

[can\_timing::phase\_seg1](structcan__timing.md#a9941688e79fa4ce01c4b498433319089)

uint16\_t phase\_seg1

Phase segment 1.

**Definition** can.h:268

[can\_timing::prop\_seg](structcan__timing.md#ac009d40fee9788b663963978498b2ee9)

uint16\_t prop\_seg

Propagation segment.

**Definition** can.h:266

[device\_state](structdevice__state.md)

Runtime device dynamic structure (in RAM) per driver instance.

**Definition** device.h:421

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:457

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4552

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
