---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2i2c_8h_source.html
original_path: doxygen/html/drivers_2i2c_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c.h

[Go to the documentation of this file.](drivers_2i2c_8h.md)

1

6

7/\*

8 \* Copyright (c) 2015 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_H\_

14

23

24#include <[errno.h](errno_8h.md)>

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[zephyr/device.h](device_8h.md)>

28#include <[zephyr/kernel.h](kernel_8h.md)>

29#include <[zephyr/sys/slist.h](slist_8h.md)>

30#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

36/\*

37 \* The following #defines are used to configure the I2C controller.

38 \*/

39

[ 41](group__i2c__interface.md#ga5ca8c5fbb2caa99ab0b7007ce2c11633)#define I2C\_SPEED\_STANDARD (0x1U)

42

[ 44](group__i2c__interface.md#gaef9d097ed2b58676498a33f3cf76f38d)#define I2C\_SPEED\_FAST (0x2U)

45

[ 47](group__i2c__interface.md#ga9c867195c4a99615ed9c0011293a2155)#define I2C\_SPEED\_FAST\_PLUS (0x3U)

48

[ 50](group__i2c__interface.md#gac7bce1bbfb422a123d3228e97e2cbb71)#define I2C\_SPEED\_HIGH (0x4U)

51

[ 53](group__i2c__interface.md#ga213468d14d1241632c957873cf2d9628)#define I2C\_SPEED\_ULTRA (0x5U)

54

[ 56](group__i2c__interface.md#gad38207f2e64b6ef3c08b17c8ccb3a836)#define I2C\_SPEED\_DT (0x7U)

57

[ 58](group__i2c__interface.md#ga6d0aaaec30d1e64e1b4ad674423d131f)#define I2C\_SPEED\_SHIFT (1U)

[ 59](group__i2c__interface.md#ga6d64fdac5a2d9008e7856e670b3c4305)#define I2C\_SPEED\_SET(speed) (((speed) << I2C\_SPEED\_SHIFT) \

60 & I2C\_SPEED\_MASK)

[ 61](group__i2c__interface.md#gade41614d9cb3efd61b22eda9c1715e4c)#define I2C\_SPEED\_MASK (0x7U << I2C\_SPEED\_SHIFT) /\* 3 bits \*/

[ 62](group__i2c__interface.md#ga0eda328bb70285895d09154f9a828040)#define I2C\_SPEED\_GET(cfg) (((cfg) & I2C\_SPEED\_MASK) \

63 >> I2C\_SPEED\_SHIFT)

64

[ 66](group__i2c__interface.md#ga66836d37196ce866681f506c44c8766d)#define I2C\_ADDR\_10\_BITS BIT(0)

67

[ 69](group__i2c__interface.md#ga6b03c8a7668528e2902073ffaa1d3a13)#define I2C\_MODE\_CONTROLLER BIT(4)

70

[ 77](structi2c__dt__spec.md)struct [i2c\_dt\_spec](structi2c__dt__spec.md) {

[ 78](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85) const struct [device](structdevice.md) \*[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85);

[ 79](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa);

80};

81

[ 92](group__i2c__interface.md#ga6479e2c8f807fc8c92646a87d1dcca84)#define I2C\_DT\_SPEC\_GET\_ON\_I3C(node\_id) \

93 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

94 .addr = DT\_PROP\_BY\_IDX(node\_id, reg, 0)

95

[ 106](group__i2c__interface.md#gafa81ab3407e8a1da368b729b31471af8)#define I2C\_DT\_SPEC\_GET\_ON\_I2C(node\_id) \

107 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

108 .addr = DT\_REG\_ADDR(node\_id)

109

[ 120](group__i2c__interface.md#gabb3ae5225cea677f3f3b36e4477ed045)#define I2C\_DT\_SPEC\_GET(node\_id) \

121 { \

122 COND\_CODE\_1(DT\_ON\_BUS(node\_id, i3c), \

123 (I2C\_DT\_SPEC\_GET\_ON\_I3C(node\_id)), \

124 (I2C\_DT\_SPEC\_GET\_ON\_I2C(node\_id))) \

125 }

126

[ 135](group__i2c__interface.md#ga2197cbc5122f0d8b2e0788113bcb5963)#define I2C\_DT\_SPEC\_INST\_GET(inst) \

136 I2C\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

137

138

139/\*

140 \* I2C\_MSG\_\* are I2C Message flags.

141 \*/

142

[ 144](group__i2c__interface.md#gaf622d3c4aa1c832f90fff7200bb33732)#define I2C\_MSG\_WRITE (0U << 0U)

145

[ 147](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95)#define I2C\_MSG\_READ BIT(0)

148

150#define I2C\_MSG\_RW\_MASK BIT(0)

152

[ 154](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa)#define I2C\_MSG\_STOP BIT(1)

155

[ 163](group__i2c__interface.md#ga8c6cf7be2a04979fdb9d0b7dd9c4f831)#define I2C\_MSG\_RESTART BIT(2)

164

[ 168](group__i2c__interface.md#ga5569e8a3e4f6660928dfe443067c472c)#define I2C\_MSG\_ADDR\_10\_BITS BIT(3)

169

[ 184](structi2c__msg.md)struct [i2c\_msg](structi2c__msg.md) {

[ 186](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37);

187

[ 189](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52);

190

[ 192](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c);

193};

194

[ 202](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc)typedef void (\*[i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc))(const struct [device](structdevice.md) \*dev, int result, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

203

210struct [i2c\_target\_config](structi2c__target__config.md);

211

212typedef int (\*i2c\_api\_configure\_t)(const struct [device](structdevice.md) \*dev,

213 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config);

214typedef int (\*i2c\_api\_get\_config\_t)(const struct [device](structdevice.md) \*dev,

215 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config);

216typedef int (\*i2c\_api\_full\_io\_t)(const struct [device](structdevice.md) \*dev,

217 struct [i2c\_msg](structi2c__msg.md) \*msgs,

218 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

219 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr);

220typedef int (\*i2c\_api\_target\_register\_t)(const struct [device](structdevice.md) \*dev,

221 struct [i2c\_target\_config](structi2c__target__config.md) \*cfg);

222typedef int (\*i2c\_api\_target\_unregister\_t)(const struct [device](structdevice.md) \*dev,

223 struct [i2c\_target\_config](structi2c__target__config.md) \*cfg);

224#ifdef CONFIG\_I2C\_CALLBACK

225typedef int (\*i2c\_api\_transfer\_cb\_t)(const struct [device](structdevice.md) \*dev,

226 struct [i2c\_msg](structi2c__msg.md) \*msgs,

227 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

228 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

229 [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb,

230 void \*userdata);

231#endif /\* CONFIG\_I2C\_CALLBACK \*/

232#if defined(CONFIG\_I2C\_RTIO) || defined(\_\_DOXYGEN\_\_)

233

238typedef void (\*i2c\_api\_iodev\_submit)(const struct [device](structdevice.md) \*dev,

239 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

240#endif /\* CONFIG\_I2C\_RTIO \*/

241

242typedef int (\*i2c\_api\_recover\_bus\_t)(const struct [device](structdevice.md) \*dev);

243

244\_\_subsystem struct i2c\_driver\_api {

245 i2c\_api\_configure\_t configure;

246 i2c\_api\_get\_config\_t get\_config;

247 i2c\_api\_full\_io\_t transfer;

248 i2c\_api\_target\_register\_t target\_register;

249 i2c\_api\_target\_unregister\_t target\_unregister;

250#ifdef CONFIG\_I2C\_CALLBACK

251 i2c\_api\_transfer\_cb\_t transfer\_cb;

252#endif

253#ifdef CONFIG\_I2C\_RTIO

254 i2c\_api\_iodev\_submit iodev\_submit;

255#endif

256 i2c\_api\_recover\_bus\_t recover\_bus;

257};

258

259typedef int (\*i2c\_target\_api\_register\_t)(const struct [device](structdevice.md) \*dev);

260typedef int (\*i2c\_target\_api\_unregister\_t)(const struct [device](structdevice.md) \*dev);

261

262\_\_subsystem struct i2c\_target\_driver\_api {

263 i2c\_target\_api\_register\_t driver\_register;

264 i2c\_target\_api\_unregister\_t driver\_unregister;

265};

266

270

[ 272](group__i2c__interface.md#ga9031b418a053f4fe0ace72fea91dec3d)#define I2C\_TARGET\_FLAGS\_ADDR\_10\_BITS BIT(0)

273

[ 289](group__i2c__interface.md#ga4cd9be521a6c7d088f15b88400624e4e)typedef int (\*[i2c\_target\_write\_requested\_cb\_t](group__i2c__interface.md#ga4cd9be521a6c7d088f15b88400624e4e))(

290 struct [i2c\_target\_config](structi2c__target__config.md) \*config);

291

[ 310](group__i2c__interface.md#ga619db7eea1c4400adcbea5dddf5cf2c5)typedef int (\*[i2c\_target\_write\_received\_cb\_t](group__i2c__interface.md#ga619db7eea1c4400adcbea5dddf5cf2c5))(

311 struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val);

312

[ 332](group__i2c__interface.md#ga244264ecdbd51210728ee92dcbebbc87)typedef int (\*[i2c\_target\_read\_requested\_cb\_t](group__i2c__interface.md#ga244264ecdbd51210728ee92dcbebbc87))(

333 struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val);

334

[ 354](group__i2c__interface.md#ga4cb0ae2cf41fc2105d1baa5e496e5dae)typedef int (\*[i2c\_target\_read\_processed\_cb\_t](group__i2c__interface.md#ga4cb0ae2cf41fc2105d1baa5e496e5dae))(

355 struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val);

356

357#ifdef CONFIG\_I2C\_TARGET\_BUFFER\_MODE

371typedef void (\*i2c\_target\_buf\_write\_received\_cb\_t)(

372 struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ptr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len);

373

396typedef int (\*i2c\_target\_buf\_read\_requested\_cb\_t)(

397 struct [i2c\_target\_config](structi2c__target__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ptr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*len);

398#endif

399

[ 414](group__i2c__interface.md#ga3c898d0bef364461a3502037cf3d40b0)typedef int (\*[i2c\_target\_stop\_cb\_t](group__i2c__interface.md#ga3c898d0bef364461a3502037cf3d40b0))(struct [i2c\_target\_config](structi2c__target__config.md) \*config);

415

[ 422](structi2c__target__callbacks.md)struct [i2c\_target\_callbacks](structi2c__target__callbacks.md) {

[ 423](structi2c__target__callbacks.md#a76260779cd35191ff64d5848e37b3134) [i2c\_target\_write\_requested\_cb\_t](group__i2c__interface.md#ga4cd9be521a6c7d088f15b88400624e4e) [write\_requested](structi2c__target__callbacks.md#a76260779cd35191ff64d5848e37b3134);

[ 424](structi2c__target__callbacks.md#a0e3922331e229461764951d93d8c2639) [i2c\_target\_read\_requested\_cb\_t](group__i2c__interface.md#ga244264ecdbd51210728ee92dcbebbc87) [read\_requested](structi2c__target__callbacks.md#a0e3922331e229461764951d93d8c2639);

[ 425](structi2c__target__callbacks.md#a1606a5b4767ecdc01798d39b63b32f32) [i2c\_target\_write\_received\_cb\_t](group__i2c__interface.md#ga619db7eea1c4400adcbea5dddf5cf2c5) [write\_received](structi2c__target__callbacks.md#a1606a5b4767ecdc01798d39b63b32f32);

[ 426](structi2c__target__callbacks.md#a7566eff7e15bcd0dc7d73bf94187e04e) [i2c\_target\_read\_processed\_cb\_t](group__i2c__interface.md#ga4cb0ae2cf41fc2105d1baa5e496e5dae) [read\_processed](structi2c__target__callbacks.md#a7566eff7e15bcd0dc7d73bf94187e04e);

427#ifdef CONFIG\_I2C\_TARGET\_BUFFER\_MODE

428 i2c\_target\_buf\_write\_received\_cb\_t buf\_write\_received;

429 i2c\_target\_buf\_read\_requested\_cb\_t buf\_read\_requested;

430#endif

[ 431](structi2c__target__callbacks.md#a81bea7375029c3651a8ecd09ea38c131) [i2c\_target\_stop\_cb\_t](group__i2c__interface.md#ga3c898d0bef364461a3502037cf3d40b0) [stop](structi2c__target__callbacks.md#a81bea7375029c3651a8ecd09ea38c131);

432};

433

[ 445](structi2c__target__config.md)struct [i2c\_target\_config](structi2c__target__config.md) {

[ 447](structi2c__target__config.md#ab2393d22d8e1fb12a389cd457d30933a) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structi2c__target__config.md#ab2393d22d8e1fb12a389cd457d30933a);

448

[ 450](structi2c__target__config.md#a25d6920d44abb1e1ce8f4c3aeb600bc5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structi2c__target__config.md#a25d6920d44abb1e1ce8f4c3aeb600bc5);

451

[ 453](structi2c__target__config.md#a5d531acec2b530a21b8d646ce321b6fd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [address](structi2c__target__config.md#a5d531acec2b530a21b8d646ce321b6fd);

454

[ 456](structi2c__target__config.md#ad6c9573e97ac2569455f43f022600f77) const struct [i2c\_target\_callbacks](structi2c__target__callbacks.md) \*[callbacks](structi2c__target__config.md#ad6c9573e97ac2569455f43f022600f77);

457};

458

[ 467](group__i2c__interface.md#gafc6799ac7a95eaa8e186cbe6981b1548)static inline bool [i2c\_is\_ready\_dt](group__i2c__interface.md#gafc6799ac7a95eaa8e186cbe6981b1548)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec)

468{

469 /\* Validate bus is ready \*/

470 return [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85));

471}

472

[ 480](group__i2c__interface.md#ga99288e3e995f8cdaebcbd3a38d22b2dc)static inline bool [i2c\_is\_read\_op](group__i2c__interface.md#ga99288e3e995f8cdaebcbd3a38d22b2dc)(const struct [i2c\_msg](structi2c__msg.md) \*msg)

481{

482 return (msg->[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) & [I2C\_MSG\_READ](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95)) == [I2C\_MSG\_READ](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95);

483}

484

[ 492](group__i2c__interface.md#ga3b43a14edbb1fa3918fb89195f6df91a)static inline bool [i2c\_is\_stop\_op](group__i2c__interface.md#ga3b43a14edbb1fa3918fb89195f6df91a)(const struct [i2c\_msg](structi2c__msg.md) \*msg)

493{

494 return (msg->[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) & [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa)) == [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa);

495}

496

[ 523](group__i2c__interface.md#ga2117056d6f6523627dda68f8ba32541e)void [i2c\_dump\_msgs\_rw](group__i2c__interface.md#ga2117056d6f6523627dda68f8ba32541e)(const struct [device](structdevice.md) \*dev, const struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

524 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, bool dump\_read);

525

[ 540](group__i2c__interface.md#gab305de2c97bb9aa3b6a8346a0210e7db)static inline void [i2c\_dump\_msgs](group__i2c__interface.md#gab305de2c97bb9aa3b6a8346a0210e7db)(const struct [device](structdevice.md) \*dev, const struct [i2c\_msg](structi2c__msg.md) \*msgs,

541 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr)

542{

543 [i2c\_dump\_msgs\_rw](group__i2c__interface.md#ga2117056d6f6523627dda68f8ba32541e)(dev, msgs, num\_msgs, addr, false);

544}

545

546#if defined(CONFIG\_I2C\_STATS) || defined(\_\_DOXYGEN\_\_)

547

548#include <[zephyr/stats/stats.h](stats_2stats_8h.md)>

549

551

552[STATS\_SECT\_START](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)(i2c)

553[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bytes\_read)

554[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(bytes\_written)

555[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(message\_count)

556[STATS\_SECT\_ENTRY32](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)(transfer\_call\_count)

557[STATS\_SECT\_END](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785);

558

559[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)(i2c)

560[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(i2c, bytes\_read)

561[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(i2c, bytes\_written)

562[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(i2c, message\_count)

563[STATS\_NAME](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)(i2c, transfer\_call\_count)

564[STATS\_NAME\_END](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)(i2c);

565

567

568

[ 572](structi2c__device__state.md)struct [i2c\_device\_state](structi2c__device__state.md) {

[ 573](structi2c__device__state.md#ad02c0d18dd2db2c35ccdc4c0913b0f0b) struct [device\_state](structdevice__state.md) [devstate](structi2c__device__state.md#ad02c0d18dd2db2c35ccdc4c0913b0f0b);

[ 574](structi2c__device__state.md#a2bc920f08c8c88a420d3f63ac55cad8c) struct stats\_i2c [stats](structi2c__device__state.md#a2bc920f08c8c88a420d3f63ac55cad8c);

575};

576

[ 584](group__i2c__interface.md#gab2a84398805e2be7662e9ae9cd4f9299)static inline void [i2c\_xfer\_stats](group__i2c__interface.md#gab2a84398805e2be7662e9ae9cd4f9299)(const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs,

585 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs)

586{

587 struct [i2c\_device\_state](structi2c__device__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) =

588 [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(dev->[state](structdevice.md#abe18f600adc4ab760963928477cc944e), struct [i2c\_device\_state](structi2c__device__state.md), [devstate](structi2c__device__state.md#ad02c0d18dd2db2c35ccdc4c0913b0f0b));

589 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bytes\_read = 0U;

590 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bytes\_written = 0U;

591

592 [STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, transfer\_call\_count);

593 [STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, message\_count, num\_msgs);

594 for ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i = 0U; i < num\_msgs; i++) {

595 if (msgs[i].[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [I2C\_MSG\_READ](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95)) {

596 bytes\_read += msgs[i].[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52);

597 } else {

598 bytes\_written += msgs[i].[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52);

599 }

600 }

601 [STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, bytes\_read, bytes\_read);

602 [STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->stats, bytes\_written, bytes\_written);

603}

604

606

610#define Z\_I2C\_DEVICE\_STATE\_DEFINE(dev\_id) \

611 static struct i2c\_device\_state Z\_DEVICE\_STATE\_NAME(dev\_id) \

612 \_\_attribute\_\_((\_\_section\_\_(".z\_devstate")))

613

620#define Z\_I2C\_INIT\_FN(dev\_id, init\_fn) \

621 static inline int UTIL\_CAT(dev\_id, \_init)(const struct device \*dev) \

622 { \

623 struct i2c\_device\_state \*state = \

624 CONTAINER\_OF(dev->state, struct i2c\_device\_state, devstate); \

625 stats\_init(&state->stats.s\_hdr, STATS\_SIZE\_32, 4, \

626 STATS\_NAME\_INIT\_PARMS(i2c)); \

627 stats\_register(dev->name, &(state->stats.s\_hdr)); \

628 if (!is\_null\_no\_warn(init\_fn)) { \

629 return init\_fn(dev); \

630 } \

631 \

632 return 0; \

633 }

634

636

[ 664](group__i2c__interface.md#ga47b9d476cc85d6f5b8081c73dd87064f)#define I2C\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

665 prio, api, ...) \

666 Z\_I2C\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

667 Z\_I2C\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

668 Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

669 DEVICE\_DT\_NAME(node\_id), \

670 &UTIL\_CAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

671 pm, data, config, level, prio, api, \

672 &(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

673 \_\_VA\_ARGS\_\_)

674

675#else /\* CONFIG\_I2C\_STATS \*/

676

677static inline void [i2c\_xfer\_stats](group__i2c__interface.md#gab2a84398805e2be7662e9ae9cd4f9299)(const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs,

678 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs)

679{

680 ARG\_UNUSED(dev);

681 ARG\_UNUSED(msgs);

682 ARG\_UNUSED(num\_msgs);

683}

684

685#define I2C\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

686 prio, api, ...) \

687 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

688 prio, api, \_\_VA\_ARGS\_\_)

689

690#endif /\* CONFIG\_I2C\_STATS \*/

691

[ 700](group__i2c__interface.md#gabfd94bccb99bd1a958cd8d7902b2072a)#define I2C\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

701 I2C\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

702

703

[ 714](group__i2c__interface.md#ga75326a6f38c011d35df9f3e72f2259e9)\_\_syscall int [i2c\_configure](group__i2c__interface.md#ga75326a6f38c011d35df9f3e72f2259e9)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config);

715

716static inline int z\_impl\_i2c\_configure(const struct [device](structdevice.md) \*dev,

717 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config)

718{

719 const struct i2c\_driver\_api \*api =

720 (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

721

722 return api->configure(dev, dev\_config);

723}

724

[ 745](group__i2c__interface.md#ga6858e0f1a942b22964105135c334baed)\_\_syscall int [i2c\_get\_config](group__i2c__interface.md#ga6858e0f1a942b22964105135c334baed)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config);

746

747static inline int z\_impl\_i2c\_get\_config(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config)

748{

749 const struct i2c\_driver\_api \*api = (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

750

751 if (api->get\_config == NULL) {

752 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

753 }

754

755 return api->get\_config(dev, dev\_config);

756}

757

[ 789](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e)\_\_syscall int [i2c\_transfer](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e)(const struct [device](structdevice.md) \*dev,

790 struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

791 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr);

792

793static inline int z\_impl\_i2c\_transfer(const struct [device](structdevice.md) \*dev,

794 struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

795 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr)

796{

797 const struct i2c\_driver\_api \*api =

798 (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

799

800 if (!num\_msgs) {

801 return 0;

802 }

803

804 if (![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_I2C\_ALLOW\_NO\_STOP\_TRANSACTIONS)) {

805 msgs[num\_msgs - 1].[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) |= [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa);

806 }

807

808 int res = api->transfer(dev, msgs, num\_msgs, addr);

809

810 [i2c\_xfer\_stats](group__i2c__interface.md#gab2a84398805e2be7662e9ae9cd4f9299)(dev, msgs, num\_msgs);

811

812 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_I2C\_DUMP\_MESSAGES)) {

813 [i2c\_dump\_msgs\_rw](group__i2c__interface.md#ga2117056d6f6523627dda68f8ba32541e)(dev, msgs, num\_msgs, addr, true);

814 }

815

816 return res;

817}

818

819#if defined(CONFIG\_I2C\_CALLBACK) || defined(\_\_DOXYGEN\_\_)

820

[ 843](group__i2c__interface.md#gaab152d5d68b6542019b77b244c239fee)static inline int [i2c\_transfer\_cb](group__i2c__interface.md#gaab152d5d68b6542019b77b244c239fee)(const struct [device](structdevice.md) \*dev,

844 struct [i2c\_msg](structi2c__msg.md) \*msgs,

845 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

846 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

847 [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb,

848 void \*userdata)

849{

850 const struct i2c\_driver\_api \*api =

851 (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

852

853 if (api->transfer\_cb == NULL) {

854 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

855 }

856

857 if (!num\_msgs) {

858 cb(dev, 0, userdata);

859 return 0;

860 }

861

862 if (![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_I2C\_ALLOW\_NO\_STOP\_TRANSACTIONS)) {

863 msgs[num\_msgs - 1].[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) |= [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa);

864 }

865

866 return api->transfer\_cb(dev, msgs, num\_msgs, addr, cb, userdata);

867}

868

[ 884](group__i2c__interface.md#ga08618803640f5520e0e4af4c31b122f5)static inline int [i2c\_transfer\_cb\_dt](group__i2c__interface.md#ga08618803640f5520e0e4af4c31b122f5)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

885 struct [i2c\_msg](structi2c__msg.md) \*msgs,

886 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

887 [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb,

888 void \*userdata)

889{

890 return [i2c\_transfer\_cb](group__i2c__interface.md#gaab152d5d68b6542019b77b244c239fee)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), msgs, num\_msgs, spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa), cb, userdata);

891}

892

[ 916](group__i2c__interface.md#ga39d1aa15d2f0fd03fc7e6cbaae26048c)static inline int [i2c\_write\_read\_cb](group__i2c__interface.md#ga39d1aa15d2f0fd03fc7e6cbaae26048c)(const struct [device](structdevice.md) \*dev, struct [i2c\_msg](structi2c__msg.md) \*msgs,

917 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const void \*write\_buf,

918 size\_t num\_write, void \*read\_buf, size\_t num\_read,

919 [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb, void \*userdata)

920{

921 if ((msgs == NULL) || (num\_msgs != 2)) {

922 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

923 }

924

925 msgs[0].[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)write\_buf;

926 msgs[0].[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) = num\_write;

927 msgs[0].[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) = [I2C\_MSG\_WRITE](group__i2c__interface.md#gaf622d3c4aa1c832f90fff7200bb33732);

928

929 msgs[1].[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)read\_buf;

930 msgs[1].[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) = num\_read;

931 msgs[1].[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) = [I2C\_MSG\_RESTART](group__i2c__interface.md#ga8c6cf7be2a04979fdb9d0b7dd9c4f831) | [I2C\_MSG\_READ](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95) | [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa);

932

933 return [i2c\_transfer\_cb](group__i2c__interface.md#gaab152d5d68b6542019b77b244c239fee)(dev, msgs, num\_msgs, addr, cb, userdata);

934}

935

[ 957](group__i2c__interface.md#ga837a2fd46243940ebd86b08d9d656571)static inline int [i2c\_write\_read\_cb\_dt](group__i2c__interface.md#ga837a2fd46243940ebd86b08d9d656571)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec, struct [i2c\_msg](structi2c__msg.md) \*msgs,

958 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, const void \*write\_buf, size\_t num\_write,

959 void \*read\_buf, size\_t num\_read, [i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc) cb,

960 void \*userdata)

961{

962 return [i2c\_write\_read\_cb](group__i2c__interface.md#ga39d1aa15d2f0fd03fc7e6cbaae26048c)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), msgs, num\_msgs, spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa), write\_buf, num\_write,

963 read\_buf, num\_read, cb, userdata);

964}

965

966#if defined(CONFIG\_POLL) || defined(\_\_DOXYGEN\_\_)

967

969void z\_i2c\_transfer\_signal\_cb(const struct [device](structdevice.md) \*dev, int result, void \*userdata);

971

[ 993](group__i2c__interface.md#gac02fcbebaef5368dbdae21407012e78e)static inline int [i2c\_transfer\_signal](group__i2c__interface.md#gac02fcbebaef5368dbdae21407012e78e)(const struct [device](structdevice.md) \*dev,

994 struct [i2c\_msg](structi2c__msg.md) \*msgs,

995 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

996 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

997 struct [k\_poll\_signal](structk__poll__signal.md) \*sig)

998{

999 const struct i2c\_driver\_api \*api = (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1000

1001 if (api->transfer\_cb == NULL) {

1002 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1003 }

1004

1005 return api->transfer\_cb(dev, msgs, num\_msgs, addr, z\_i2c\_transfer\_signal\_cb, sig);

1006}

1007

1008#endif /\* CONFIG\_POLL \*/

1009

1010#endif /\* CONFIG\_I2C\_CALLBACK \*/

1011

1012

1013#if defined(CONFIG\_I2C\_RTIO) || defined(\_\_DOXYGEN\_\_)

1014

[ 1025](group__i2c__interface.md#ga4e01759396817ca46244e6abd5186673)void [i2c\_iodev\_submit\_fallback](group__i2c__interface.md#ga4e01759396817ca46244e6abd5186673)(const struct [device](structdevice.md) \*dev, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

1026

[ 1033](group__i2c__interface.md#ga1d6d1d28f56a9c7c8fde1e6eb056e128)static inline void [i2c\_iodev\_submit](group__i2c__interface.md#ga1d6d1d28f56a9c7c8fde1e6eb056e128)(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe)

1034{

1035 const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*dt\_spec = (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*)iodev\_sqe->[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b).[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1036 const struct [device](structdevice.md) \*dev = dt\_spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85);

1037 const struct i2c\_driver\_api \*api = (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1038

1039 if (api->iodev\_submit == NULL) {

1040 [rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)(iodev\_sqe, -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b));

1041 return;

1042 }

1043 api->iodev\_submit(dt\_spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), iodev\_sqe);

1044}

1045

1046extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) [i2c\_iodev\_api](group__i2c__interface.md#gaea8f7eeb3ed41c260d7a6c3cf078c3ec);

1047

[ 1057](group__i2c__interface.md#ga304d3b906b5222a9b704f5b35641143d)#define I2C\_DT\_IODEV\_DEFINE(name, node\_id) \

1058 const struct i2c\_dt\_spec \_i2c\_dt\_spec\_##name = \

1059 I2C\_DT\_SPEC\_GET(node\_id); \

1060 RTIO\_IODEV\_DEFINE(name, &i2c\_iodev\_api, (void \*)&\_i2c\_dt\_spec\_##name)

1061

[ 1072](group__i2c__interface.md#ga451d0877ad5f4c2e9601dc2db8644924)#define I2C\_IODEV\_DEFINE(name, \_bus, \_addr) \

1073 const struct i2c\_dt\_spec \_i2c\_dt\_spec\_##name = { \

1074 .bus = DEVICE\_DT\_GET(\_bus), \

1075 .addr = \_addr, \

1076 }; \

1077 RTIO\_IODEV\_DEFINE(name, &i2c\_iodev\_api, (void \*)&\_i2c\_dt\_spec\_##name)

1078

[ 1090](group__i2c__interface.md#ga1fc6344eba89f6121c61172698c19093)struct [rtio\_sqe](structrtio__sqe.md) \*[i2c\_rtio\_copy](group__i2c__interface.md#ga1fc6344eba89f6121c61172698c19093)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

1091 struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc),

1092 const struct [i2c\_msg](structi2c__msg.md) \*msgs,

1093 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

1094

1095#endif /\* CONFIG\_I2C\_RTIO \*/

1096

[ 1110](group__i2c__interface.md#ga8dce931e2dd637d811ff651062cec17b)static inline int [i2c\_transfer\_dt](group__i2c__interface.md#ga8dce931e2dd637d811ff651062cec17b)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1111 struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs)

1112{

1113 return [i2c\_transfer](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), msgs, num\_msgs, spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa));

1114}

1115

[ 1128](group__i2c__interface.md#ga93117c531c39259d89ab69d52bbde85c)\_\_syscall int [i2c\_recover\_bus](group__i2c__interface.md#ga93117c531c39259d89ab69d52bbde85c)(const struct [device](structdevice.md) \*dev);

1129

1130static inline int z\_impl\_i2c\_recover\_bus(const struct [device](structdevice.md) \*dev)

1131{

1132 const struct i2c\_driver\_api \*api =

1133 (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1134

1135 if (api->recover\_bus == NULL) {

1136 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1137 }

1138

1139 return api->recover\_bus(dev);

1140}

1141

[ 1166](group__i2c__interface.md#gaa47c3fde397188fa126dcaa4a6e85b47)static inline int [i2c\_target\_register](group__i2c__interface.md#gaa47c3fde397188fa126dcaa4a6e85b47)(const struct [device](structdevice.md) \*dev,

1167 struct [i2c\_target\_config](structi2c__target__config.md) \*cfg)

1168{

1169 const struct i2c\_driver\_api \*api =

1170 (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1171

1172 if (api->target\_register == NULL) {

1173 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1174 }

1175

1176 return api->target\_register(dev, cfg);

1177}

1178

[ 1195](group__i2c__interface.md#ga11eada869173f6bd91db39c794dc8979)static inline int [i2c\_target\_unregister](group__i2c__interface.md#ga11eada869173f6bd91db39c794dc8979)(const struct [device](structdevice.md) \*dev,

1196 struct [i2c\_target\_config](structi2c__target__config.md) \*cfg)

1197{

1198 const struct i2c\_driver\_api \*api =

1199 (const struct i2c\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1200

1201 if (api->target\_unregister == NULL) {

1202 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1203 }

1204

1205 return api->target\_unregister(dev, cfg);

1206}

1207

[ 1221](group__i2c__interface.md#ga1ba4520e0c2a3ef19fcc52ba091d97d4)\_\_syscall int [i2c\_target\_driver\_register](group__i2c__interface.md#ga1ba4520e0c2a3ef19fcc52ba091d97d4)(const struct [device](structdevice.md) \*dev);

1222

1223static inline int z\_impl\_i2c\_target\_driver\_register(const struct [device](structdevice.md) \*dev)

1224{

1225 const struct i2c\_target\_driver\_api \*api =

1226 (const struct i2c\_target\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1227

1228 return api->driver\_register(dev);

1229}

1230

[ 1244](group__i2c__interface.md#ga099580e56cfaf800e14f23066db70515)\_\_syscall int [i2c\_target\_driver\_unregister](group__i2c__interface.md#ga099580e56cfaf800e14f23066db70515)(const struct [device](structdevice.md) \*dev);

1245

1246static inline int z\_impl\_i2c\_target\_driver\_unregister(const struct [device](structdevice.md) \*dev)

1247{

1248 const struct i2c\_target\_driver\_api \*api =

1249 (const struct i2c\_target\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1250

1251 return api->driver\_unregister(dev);

1252}

1253

1254/\*

1255 \* Derived i2c APIs -- all implemented in terms of i2c\_transfer()

1256 \*/

1257

[ 1272](group__i2c__interface.md#ga2cc5f49493dce89e128ccbfa9d6149a0)static inline int [i2c\_write](group__i2c__interface.md#ga2cc5f49493dce89e128ccbfa9d6149a0)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1273 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr)

1274{

1275 struct [i2c\_msg](structi2c__msg.md) msg;

1276

1277 msg.[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37);

1278 msg.[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) = num\_bytes;

1279 msg.[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) = [I2C\_MSG\_WRITE](group__i2c__interface.md#gaf622d3c4aa1c832f90fff7200bb33732) | [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa);

1280

1281 return [i2c\_transfer](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e)(dev, &msg, 1, addr);

1282}

1283

[ 1297](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f)static inline int [i2c\_write\_dt](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1298 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1299{

1300 return [i2c\_write](group__i2c__interface.md#ga2cc5f49493dce89e128ccbfa9d6149a0)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), [buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37), num\_bytes, spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa));

1301}

1302

[ 1317](group__i2c__interface.md#ga935d1fdcbf9a40c9a673aa8977048ee7)static inline int [i2c\_read](group__i2c__interface.md#ga935d1fdcbf9a40c9a673aa8977048ee7)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37),

1318 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr)

1319{

1320 struct [i2c\_msg](structi2c__msg.md) msg;

1321

1322 msg.[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) = [buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37);

1323 msg.[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) = num\_bytes;

1324 msg.[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) = [I2C\_MSG\_READ](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95) | [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa);

1325

1326 return [i2c\_transfer](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e)(dev, &msg, 1, addr);

1327}

1328

[ 1342](group__i2c__interface.md#ga5cf80d20dca0d5f1d16e16c151f57ef6)static inline int [i2c\_read\_dt](group__i2c__interface.md#ga5cf80d20dca0d5f1d16e16c151f57ef6)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1343 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1344{

1345 return [i2c\_read](group__i2c__interface.md#ga935d1fdcbf9a40c9a673aa8977048ee7)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), [buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37), num\_bytes, spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa));

1346}

1347

[ 1366](group__i2c__interface.md#ga1273a9f8bdb002e0d6ece3a8c893a709)static inline int [i2c\_write\_read](group__i2c__interface.md#ga1273a9f8bdb002e0d6ece3a8c893a709)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

1367 const void \*write\_buf, size\_t num\_write,

1368 void \*read\_buf, size\_t num\_read)

1369{

1370 struct [i2c\_msg](structi2c__msg.md) msg[2];

1371

1372 msg[0].[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)write\_buf;

1373 msg[0].[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) = num\_write;

1374 msg[0].[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) = [I2C\_MSG\_WRITE](group__i2c__interface.md#gaf622d3c4aa1c832f90fff7200bb33732);

1375

1376 msg[1].[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)read\_buf;

1377 msg[1].[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) = num\_read;

1378 msg[1].[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) = [I2C\_MSG\_RESTART](group__i2c__interface.md#ga8c6cf7be2a04979fdb9d0b7dd9c4f831) | [I2C\_MSG\_READ](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95) | [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa);

1379

1380 return [i2c\_transfer](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e)(dev, msg, 2, addr);

1381}

1382

[ 1400](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758)static inline int [i2c\_write\_read\_dt](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1401 const void \*write\_buf, size\_t num\_write,

1402 void \*read\_buf, size\_t num\_read)

1403{

1404 return [i2c\_write\_read](group__i2c__interface.md#ga1273a9f8bdb002e0d6ece3a8c893a709)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa),

1405 write\_buf, num\_write,

1406 read\_buf, num\_read);

1407}

1408

[ 1427](group__i2c__interface.md#ga4bbb79898f53d0a2fad1bd302369ae9e)static inline int [i2c\_burst\_read](group__i2c__interface.md#ga4bbb79898f53d0a2fad1bd302369ae9e)(const struct [device](structdevice.md) \*dev,

1428 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr,

1429 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

1430 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37),

1431 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1432{

1433 return [i2c\_write\_read](group__i2c__interface.md#ga1273a9f8bdb002e0d6ece3a8c893a709)(dev, dev\_addr,

1434 &start\_addr, sizeof(start\_addr),

1435 [buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37), num\_bytes);

1436}

1437

[ 1452](group__i2c__interface.md#ga9d2654bbf80f4d253532adaec8566fc3)static inline int [i2c\_burst\_read\_dt](group__i2c__interface.md#ga9d2654bbf80f4d253532adaec8566fc3)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1453 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

1454 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37),

1455 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1456{

1457 return [i2c\_burst\_read](group__i2c__interface.md#ga4bbb79898f53d0a2fad1bd302369ae9e)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa),

1458 start\_addr, [buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37), num\_bytes);

1459}

1460

[ 1482](group__i2c__interface.md#gaf995812f31e7bf1ea7f203905db13822)static inline int [i2c\_burst\_write](group__i2c__interface.md#gaf995812f31e7bf1ea7f203905db13822)(const struct [device](structdevice.md) \*dev,

1483 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr,

1484 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

1485 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37),

1486 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1487{

1488 struct [i2c\_msg](structi2c__msg.md) msg[2];

1489

1490 msg[0].[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) = &start\_addr;

1491 msg[0].[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) = 1U;

1492 msg[0].[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) = [I2C\_MSG\_WRITE](group__i2c__interface.md#gaf622d3c4aa1c832f90fff7200bb33732);

1493

1494 msg[1].[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37);

1495 msg[1].[len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52) = num\_bytes;

1496 msg[1].[flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c) = [I2C\_MSG\_WRITE](group__i2c__interface.md#gaf622d3c4aa1c832f90fff7200bb33732) | [I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa);

1497

1498 return [i2c\_transfer](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e)(dev, msg, 2, dev\_addr);

1499}

1500

[ 1515](group__i2c__interface.md#ga0e590c99d3b9c1a7dd8174a318ee5a7d)static inline int [i2c\_burst\_write\_dt](group__i2c__interface.md#ga0e590c99d3b9c1a7dd8174a318ee5a7d)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1516 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr,

1517 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37),

1518 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

1519{

1520 return [i2c\_burst\_write](group__i2c__interface.md#gaf995812f31e7bf1ea7f203905db13822)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa),

1521 start\_addr, [buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37), num\_bytes);

1522}

1523

[ 1539](group__i2c__interface.md#gaf8d1722ff4ebe97122293aef6ccf332a)static inline int [i2c\_reg\_read\_byte](group__i2c__interface.md#gaf8d1722ff4ebe97122293aef6ccf332a)(const struct [device](structdevice.md) \*dev,

1540 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr,

1541 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value)

1542{

1543 return [i2c\_write\_read](group__i2c__interface.md#ga1273a9f8bdb002e0d6ece3a8c893a709)(dev, dev\_addr,

1544 &reg\_addr, sizeof(reg\_addr),

1545 value, sizeof(\*value));

1546}

1547

[ 1561](group__i2c__interface.md#ga6fc14d75c41b8c8d9dd2f77c59533640)static inline int [i2c\_reg\_read\_byte\_dt](group__i2c__interface.md#ga6fc14d75c41b8c8d9dd2f77c59533640)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1562 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value)

1563{

1564 return [i2c\_reg\_read\_byte](group__i2c__interface.md#gaf8d1722ff4ebe97122293aef6ccf332a)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa), reg\_addr, value);

1565}

1566

[ 1585](group__i2c__interface.md#ga687a0da74c22b299b66db8198c6fdcb1)static inline int [i2c\_reg\_write\_byte](group__i2c__interface.md#ga687a0da74c22b299b66db8198c6fdcb1)(const struct [device](structdevice.md) \*dev,

1586 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_addr,

1587 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

1588{

1589 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_buf[2] = {reg\_addr, value};

1590

1591 return [i2c\_write](group__i2c__interface.md#ga2cc5f49493dce89e128ccbfa9d6149a0)(dev, tx\_buf, 2, dev\_addr);

1592}

1593

[ 1607](group__i2c__interface.md#ga664cd76bf4fae0dba848f5c284699a04)static inline int [i2c\_reg\_write\_byte\_dt](group__i2c__interface.md#ga664cd76bf4fae0dba848f5c284699a04)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1608 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

1609{

1610 return [i2c\_reg\_write\_byte](group__i2c__interface.md#ga687a0da74c22b299b66db8198c6fdcb1)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa), reg\_addr, value);

1611}

1612

[ 1632](group__i2c__interface.md#gad07710d37bf6bd4fa6ccfe62be625eb4)static inline int [i2c\_reg\_update\_byte](group__i2c__interface.md#gad07710d37bf6bd4fa6ccfe62be625eb4)(const struct [device](structdevice.md) \*dev,

1633 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr,

1634 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask,

1635 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

1636{

1637 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) old\_value, new\_value;

1638 int rc;

1639

1640 rc = [i2c\_reg\_read\_byte](group__i2c__interface.md#gaf8d1722ff4ebe97122293aef6ccf332a)(dev, dev\_addr, reg\_addr, &old\_value);

1641 if (rc != 0) {

1642 return rc;

1643 }

1644

1645 new\_value = (old\_value & ~mask) | (value & mask);

1646 if (new\_value == old\_value) {

1647 return 0;

1648 }

1649

1650 return [i2c\_reg\_write\_byte](group__i2c__interface.md#ga687a0da74c22b299b66db8198c6fdcb1)(dev, dev\_addr, reg\_addr, new\_value);

1651}

1652

[ 1667](group__i2c__interface.md#ga5000c5e49eabe712b5fd532d3842c3f5)static inline int [i2c\_reg\_update\_byte\_dt](group__i2c__interface.md#ga5000c5e49eabe712b5fd532d3842c3f5)(const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*spec,

1668 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask,

1669 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

1670{

1671 return [i2c\_reg\_update\_byte](group__i2c__interface.md#gad07710d37bf6bd4fa6ccfe62be625eb4)(spec->[bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85), spec->[addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa),

1672 reg\_addr, mask, value);

1673}

1674

1675#ifdef \_\_cplusplus

1676}

1677#endif

1678

1682

1683#include <zephyr/syscalls/i2c.h>

1684

1685#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_H\_ \*/

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb)

bool device\_is\_ready(const struct device \*dev)

Verify that a device is ready for use.

[i2c\_transfer\_cb\_dt](group__i2c__interface.md#ga08618803640f5520e0e4af4c31b122f5)

static int i2c\_transfer\_cb\_dt(const struct i2c\_dt\_spec \*spec, struct i2c\_msg \*msgs, uint8\_t num\_msgs, i2c\_callback\_t cb, void \*userdata)

Perform data transfer to another I2C device in master mode asynchronously.

**Definition** i2c.h:884

[i2c\_target\_driver\_unregister](group__i2c__interface.md#ga099580e56cfaf800e14f23066db70515)

int i2c\_target\_driver\_unregister(const struct device \*dev)

Instructs the I2C Target device to unregister itself from the I2C Controller.

[i2c\_burst\_write\_dt](group__i2c__interface.md#ga0e590c99d3b9c1a7dd8174a318ee5a7d)

static int i2c\_burst\_write\_dt(const struct i2c\_dt\_spec \*spec, uint8\_t start\_addr, const uint8\_t \*buf, uint32\_t num\_bytes)

Write multiple bytes to an internal address of an I2C device.

**Definition** i2c.h:1515

[i2c\_target\_unregister](group__i2c__interface.md#ga11eada869173f6bd91db39c794dc8979)

static int i2c\_target\_unregister(const struct device \*dev, struct i2c\_target\_config \*cfg)

Unregisters the provided config as Target device.

**Definition** i2c.h:1195

[i2c\_write\_read](group__i2c__interface.md#ga1273a9f8bdb002e0d6ece3a8c893a709)

static int i2c\_write\_read(const struct device \*dev, uint16\_t addr, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read)

Write then read data from an I2C device.

**Definition** i2c.h:1366

[i2c\_target\_driver\_register](group__i2c__interface.md#ga1ba4520e0c2a3ef19fcc52ba091d97d4)

int i2c\_target\_driver\_register(const struct device \*dev)

Instructs the I2C Target device to register itself to the I2C Controller.

[i2c\_iodev\_submit](group__i2c__interface.md#ga1d6d1d28f56a9c7c8fde1e6eb056e128)

static void i2c\_iodev\_submit(struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit request(s) to an I2C device with RTIO.

**Definition** i2c.h:1033

[i2c\_rtio\_copy](group__i2c__interface.md#ga1fc6344eba89f6121c61172698c19093)

struct rtio\_sqe \* i2c\_rtio\_copy(struct rtio \*r, struct rtio\_iodev \*iodev, const struct i2c\_msg \*msgs, uint8\_t num\_msgs)

Copy the i2c\_msgs into a set of RTIO requests.

[i2c\_dump\_msgs\_rw](group__i2c__interface.md#ga2117056d6f6523627dda68f8ba32541e)

void i2c\_dump\_msgs\_rw(const struct device \*dev, const struct i2c\_msg \*msgs, uint8\_t num\_msgs, uint16\_t addr, bool dump\_read)

Dump out an I2C message.

[i2c\_target\_read\_requested\_cb\_t](group__i2c__interface.md#ga244264ecdbd51210728ee92dcbebbc87)

int(\* i2c\_target\_read\_requested\_cb\_t)(struct i2c\_target\_config \*config, uint8\_t \*val)

Function called when a read from the device is initiated.

**Definition** i2c.h:332

[i2c\_transfer](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e)

int i2c\_transfer(const struct device \*dev, struct i2c\_msg \*msgs, uint8\_t num\_msgs, uint16\_t addr)

Perform data transfer to another I2C device in controller mode.

[i2c\_write](group__i2c__interface.md#ga2cc5f49493dce89e128ccbfa9d6149a0)

static int i2c\_write(const struct device \*dev, const uint8\_t \*buf, uint32\_t num\_bytes, uint16\_t addr)

Write a set amount of data to an I2C device.

**Definition** i2c.h:1272

[i2c\_write\_dt](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f)

static int i2c\_write\_dt(const struct i2c\_dt\_spec \*spec, const uint8\_t \*buf, uint32\_t num\_bytes)

Write a set amount of data to an I2C device.

**Definition** i2c.h:1297

[i2c\_write\_read\_dt](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758)

static int i2c\_write\_read\_dt(const struct i2c\_dt\_spec \*spec, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read)

Write then read data from an I2C device.

**Definition** i2c.h:1400

[i2c\_write\_read\_cb](group__i2c__interface.md#ga39d1aa15d2f0fd03fc7e6cbaae26048c)

static int i2c\_write\_read\_cb(const struct device \*dev, struct i2c\_msg \*msgs, uint8\_t num\_msgs, uint16\_t addr, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read, i2c\_callback\_t cb, void \*userdata)

Write then read data from an I2C device asynchronously.

**Definition** i2c.h:916

[i2c\_is\_stop\_op](group__i2c__interface.md#ga3b43a14edbb1fa3918fb89195f6df91a)

static bool i2c\_is\_stop\_op(const struct i2c\_msg \*msg)

Check if the current message includes a stop.

**Definition** i2c.h:492

[i2c\_target\_stop\_cb\_t](group__i2c__interface.md#ga3c898d0bef364461a3502037cf3d40b0)

int(\* i2c\_target\_stop\_cb\_t)(struct i2c\_target\_config \*config)

Function called when a stop condition is observed after a start condition addressed to a particular d...

**Definition** i2c.h:414

[i2c\_burst\_read](group__i2c__interface.md#ga4bbb79898f53d0a2fad1bd302369ae9e)

static int i2c\_burst\_read(const struct device \*dev, uint16\_t dev\_addr, uint8\_t start\_addr, uint8\_t \*buf, uint32\_t num\_bytes)

Read multiple bytes from an internal address of an I2C device.

**Definition** i2c.h:1427

[i2c\_target\_read\_processed\_cb\_t](group__i2c__interface.md#ga4cb0ae2cf41fc2105d1baa5e496e5dae)

int(\* i2c\_target\_read\_processed\_cb\_t)(struct i2c\_target\_config \*config, uint8\_t \*val)

Function called when a read from the device is continued.

**Definition** i2c.h:354

[i2c\_target\_write\_requested\_cb\_t](group__i2c__interface.md#ga4cd9be521a6c7d088f15b88400624e4e)

int(\* i2c\_target\_write\_requested\_cb\_t)(struct i2c\_target\_config \*config)

Function called when a write to the device is initiated.

**Definition** i2c.h:289

[i2c\_iodev\_submit\_fallback](group__i2c__interface.md#ga4e01759396817ca46244e6abd5186673)

void i2c\_iodev\_submit\_fallback(const struct device \*dev, struct rtio\_iodev\_sqe \*iodev\_sqe)

Fallback submit implementation.

[i2c\_reg\_update\_byte\_dt](group__i2c__interface.md#ga5000c5e49eabe712b5fd532d3842c3f5)

static int i2c\_reg\_update\_byte\_dt(const struct i2c\_dt\_spec \*spec, uint8\_t reg\_addr, uint8\_t mask, uint8\_t value)

Update internal register of an I2C device.

**Definition** i2c.h:1667

[i2c\_callback\_t](group__i2c__interface.md#ga590293ec0d90d3fb0d8cbfee097798fc)

void(\* i2c\_callback\_t)(const struct device \*dev, int result, void \*data)

I2C callback for asynchronous transfer requests.

**Definition** i2c.h:202

[i2c\_read\_dt](group__i2c__interface.md#ga5cf80d20dca0d5f1d16e16c151f57ef6)

static int i2c\_read\_dt(const struct i2c\_dt\_spec \*spec, uint8\_t \*buf, uint32\_t num\_bytes)

Read a set amount of data from an I2C device.

**Definition** i2c.h:1342

[i2c\_target\_write\_received\_cb\_t](group__i2c__interface.md#ga619db7eea1c4400adcbea5dddf5cf2c5)

int(\* i2c\_target\_write\_received\_cb\_t)(struct i2c\_target\_config \*config, uint8\_t val)

Function called when a write to the device is continued.

**Definition** i2c.h:310

[i2c\_reg\_write\_byte\_dt](group__i2c__interface.md#ga664cd76bf4fae0dba848f5c284699a04)

static int i2c\_reg\_write\_byte\_dt(const struct i2c\_dt\_spec \*spec, uint8\_t reg\_addr, uint8\_t value)

Write internal register of an I2C device.

**Definition** i2c.h:1607

[i2c\_get\_config](group__i2c__interface.md#ga6858e0f1a942b22964105135c334baed)

int i2c\_get\_config(const struct device \*dev, uint32\_t \*dev\_config)

Get configuration of a host controller.

[i2c\_reg\_write\_byte](group__i2c__interface.md#ga687a0da74c22b299b66db8198c6fdcb1)

static int i2c\_reg\_write\_byte(const struct device \*dev, uint16\_t dev\_addr, uint8\_t reg\_addr, uint8\_t value)

Write internal register of an I2C device.

**Definition** i2c.h:1585

[I2C\_MSG\_READ](group__i2c__interface.md#ga6c3042e882e6a817a6498b7a4e1f0a95)

#define I2C\_MSG\_READ

Read message from I2C bus.

**Definition** i2c.h:147

[i2c\_reg\_read\_byte\_dt](group__i2c__interface.md#ga6fc14d75c41b8c8d9dd2f77c59533640)

static int i2c\_reg\_read\_byte\_dt(const struct i2c\_dt\_spec \*spec, uint8\_t reg\_addr, uint8\_t \*value)

Read internal register of an I2C device.

**Definition** i2c.h:1561

[i2c\_configure](group__i2c__interface.md#ga75326a6f38c011d35df9f3e72f2259e9)

int i2c\_configure(const struct device \*dev, uint32\_t dev\_config)

Configure operation of a host controller.

[i2c\_write\_read\_cb\_dt](group__i2c__interface.md#ga837a2fd46243940ebd86b08d9d656571)

static int i2c\_write\_read\_cb\_dt(const struct i2c\_dt\_spec \*spec, struct i2c\_msg \*msgs, uint8\_t num\_msgs, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read, i2c\_callback\_t cb, void \*userdata)

Write then read data from an I2C device asynchronously.

**Definition** i2c.h:957

[I2C\_MSG\_RESTART](group__i2c__interface.md#ga8c6cf7be2a04979fdb9d0b7dd9c4f831)

#define I2C\_MSG\_RESTART

RESTART I2C transaction for this message.

**Definition** i2c.h:163

[i2c\_transfer\_dt](group__i2c__interface.md#ga8dce931e2dd637d811ff651062cec17b)

static int i2c\_transfer\_dt(const struct i2c\_dt\_spec \*spec, struct i2c\_msg \*msgs, uint8\_t num\_msgs)

Perform data transfer to another I2C device in controller mode.

**Definition** i2c.h:1110

[i2c\_recover\_bus](group__i2c__interface.md#ga93117c531c39259d89ab69d52bbde85c)

int i2c\_recover\_bus(const struct device \*dev)

Recover the I2C bus.

[i2c\_read](group__i2c__interface.md#ga935d1fdcbf9a40c9a673aa8977048ee7)

static int i2c\_read(const struct device \*dev, uint8\_t \*buf, uint32\_t num\_bytes, uint16\_t addr)

Read a set amount of data from an I2C device.

**Definition** i2c.h:1317

[i2c\_is\_read\_op](group__i2c__interface.md#ga99288e3e995f8cdaebcbd3a38d22b2dc)

static bool i2c\_is\_read\_op(const struct i2c\_msg \*msg)

Check if the current message is a read operation.

**Definition** i2c.h:480

[i2c\_burst\_read\_dt](group__i2c__interface.md#ga9d2654bbf80f4d253532adaec8566fc3)

static int i2c\_burst\_read\_dt(const struct i2c\_dt\_spec \*spec, uint8\_t start\_addr, uint8\_t \*buf, uint32\_t num\_bytes)

Read multiple bytes from an internal address of an I2C device.

**Definition** i2c.h:1452

[i2c\_target\_register](group__i2c__interface.md#gaa47c3fde397188fa126dcaa4a6e85b47)

static int i2c\_target\_register(const struct device \*dev, struct i2c\_target\_config \*cfg)

Registers the provided config as Target device of a controller.

**Definition** i2c.h:1166

[i2c\_transfer\_cb](group__i2c__interface.md#gaab152d5d68b6542019b77b244c239fee)

static int i2c\_transfer\_cb(const struct device \*dev, struct i2c\_msg \*msgs, uint8\_t num\_msgs, uint16\_t addr, i2c\_callback\_t cb, void \*userdata)

Perform data transfer to another I2C device in controller mode.

**Definition** i2c.h:843

[I2C\_MSG\_STOP](group__i2c__interface.md#gaad55262ad277ee60b786372c71f217aa)

#define I2C\_MSG\_STOP

Send STOP after this message.

**Definition** i2c.h:154

[i2c\_xfer\_stats](group__i2c__interface.md#gab2a84398805e2be7662e9ae9cd4f9299)

static void i2c\_xfer\_stats(const struct device \*dev, struct i2c\_msg \*msgs, uint8\_t num\_msgs)

Updates the i2c stats for i2c transfers.

**Definition** i2c.h:584

[i2c\_dump\_msgs](group__i2c__interface.md#gab305de2c97bb9aa3b6a8346a0210e7db)

static void i2c\_dump\_msgs(const struct device \*dev, const struct i2c\_msg \*msgs, uint8\_t num\_msgs, uint16\_t addr)

Dump out an I2C message, before it is executed.

**Definition** i2c.h:540

[i2c\_transfer\_signal](group__i2c__interface.md#gac02fcbebaef5368dbdae21407012e78e)

static int i2c\_transfer\_signal(const struct device \*dev, struct i2c\_msg \*msgs, uint8\_t num\_msgs, uint16\_t addr, struct k\_poll\_signal \*sig)

Perform data transfer to another I2C device in controller mode.

**Definition** i2c.h:993

[i2c\_reg\_update\_byte](group__i2c__interface.md#gad07710d37bf6bd4fa6ccfe62be625eb4)

static int i2c\_reg\_update\_byte(const struct device \*dev, uint8\_t dev\_addr, uint8\_t reg\_addr, uint8\_t mask, uint8\_t value)

Update internal register of an I2C device.

**Definition** i2c.h:1632

[i2c\_iodev\_api](group__i2c__interface.md#gaea8f7eeb3ed41c260d7a6c3cf078c3ec)

const struct rtio\_iodev\_api i2c\_iodev\_api

[I2C\_MSG\_WRITE](group__i2c__interface.md#gaf622d3c4aa1c832f90fff7200bb33732)

#define I2C\_MSG\_WRITE

Write message to I2C bus.

**Definition** i2c.h:144

[i2c\_reg\_read\_byte](group__i2c__interface.md#gaf8d1722ff4ebe97122293aef6ccf332a)

static int i2c\_reg\_read\_byte(const struct device \*dev, uint16\_t dev\_addr, uint8\_t reg\_addr, uint8\_t \*value)

Read internal register of an I2C device.

**Definition** i2c.h:1539

[i2c\_burst\_write](group__i2c__interface.md#gaf995812f31e7bf1ea7f203905db13822)

static int i2c\_burst\_write(const struct device \*dev, uint16\_t dev\_addr, uint8\_t start\_addr, const uint8\_t \*buf, uint32\_t num\_bytes)

Write multiple bytes to an internal address of an I2C device.

**Definition** i2c.h:1482

[i2c\_is\_ready\_dt](group__i2c__interface.md#gafc6799ac7a95eaa8e186cbe6981b1548)

static bool i2c\_is\_ready\_dt(const struct i2c\_dt\_spec \*spec)

Validate that I2C bus is ready.

**Definition** i2c.h:467

[rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f)

static void rtio\_iodev\_sqe\_err(struct rtio\_iodev\_sqe \*iodev\_sqe, int result)

Inform the executor of a submissions completion with error.

**Definition** rtio.h:1151

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:284

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[rtio.h](rtio_2rtio_8h.md)

Real-Time IO device API for moving bytes with low effort.

[slist.h](slist_8h.md)

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

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)

#define STATS\_INC(group\_\_, var\_\_)

**Definition** stats.h:364

[STATS\_NAME\_START](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)

#define STATS\_NAME\_START(name\_\_)

**Definition** stats.h:389

[STATS\_INCN](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)

#define STATS\_INCN(group\_\_, var\_\_, n\_\_)

**Definition** stats.h:363

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

[device::state](structdevice.md#abe18f600adc4ab760963928477cc944e)

struct device\_state \* state

Address of the common device state.

**Definition** device.h:420

[i2c\_device\_state](structi2c__device__state.md)

I2C specific device state which allows for i2c device class specific additions.

**Definition** i2c.h:572

[i2c\_device\_state::stats](structi2c__device__state.md#a2bc920f08c8c88a420d3f63ac55cad8c)

struct stats\_i2c stats

**Definition** i2c.h:574

[i2c\_device\_state::devstate](structi2c__device__state.md#ad02c0d18dd2db2c35ccdc4c0913b0f0b)

struct device\_state devstate

**Definition** i2c.h:573

[i2c\_dt\_spec](structi2c__dt__spec.md)

Complete I2C DT information.

**Definition** i2c.h:77

[i2c\_dt\_spec::bus](structi2c__dt__spec.md#a40d5c17c04910927c34eb69b173cbb85)

const struct device \* bus

**Definition** i2c.h:78

[i2c\_dt\_spec::addr](structi2c__dt__spec.md#a85242ab56b1e8633b7001353990392fa)

uint16\_t addr

**Definition** i2c.h:79

[i2c\_msg](structi2c__msg.md)

One I2C Message.

**Definition** i2c.h:184

[i2c\_msg::buf](structi2c__msg.md#ac4aa590487270589a51964b38f853a37)

uint8\_t \* buf

Data buffer in bytes.

**Definition** i2c.h:186

[i2c\_msg::len](structi2c__msg.md#ae122c36d1fdc0829321fa116921d7a52)

uint32\_t len

Length of buffer in bytes.

**Definition** i2c.h:189

[i2c\_msg::flags](structi2c__msg.md#ae6f9dc8a50b611adbca38e29b529ab9c)

uint8\_t flags

Flags for this message.

**Definition** i2c.h:192

[i2c\_target\_callbacks](structi2c__target__callbacks.md)

Structure providing callbacks to be implemented for devices that supports the I2C target API.

**Definition** i2c.h:422

[i2c\_target\_callbacks::read\_requested](structi2c__target__callbacks.md#a0e3922331e229461764951d93d8c2639)

i2c\_target\_read\_requested\_cb\_t read\_requested

**Definition** i2c.h:424

[i2c\_target\_callbacks::write\_received](structi2c__target__callbacks.md#a1606a5b4767ecdc01798d39b63b32f32)

i2c\_target\_write\_received\_cb\_t write\_received

**Definition** i2c.h:425

[i2c\_target\_callbacks::read\_processed](structi2c__target__callbacks.md#a7566eff7e15bcd0dc7d73bf94187e04e)

i2c\_target\_read\_processed\_cb\_t read\_processed

**Definition** i2c.h:426

[i2c\_target\_callbacks::write\_requested](structi2c__target__callbacks.md#a76260779cd35191ff64d5848e37b3134)

i2c\_target\_write\_requested\_cb\_t write\_requested

**Definition** i2c.h:423

[i2c\_target\_callbacks::stop](structi2c__target__callbacks.md#a81bea7375029c3651a8ecd09ea38c131)

i2c\_target\_stop\_cb\_t stop

**Definition** i2c.h:431

[i2c\_target\_config](structi2c__target__config.md)

Structure describing a device that supports the I2C target API.

**Definition** i2c.h:445

[i2c\_target\_config::flags](structi2c__target__config.md#a25d6920d44abb1e1ce8f4c3aeb600bc5)

uint8\_t flags

Flags for the target device defined by I2C\_TARGET\_FLAGS\_\* constants.

**Definition** i2c.h:450

[i2c\_target\_config::address](structi2c__target__config.md#a5d531acec2b530a21b8d646ce321b6fd)

uint16\_t address

Address for this target device.

**Definition** i2c.h:453

[i2c\_target\_config::node](structi2c__target__config.md#ab2393d22d8e1fb12a389cd457d30933a)

sys\_snode\_t node

Private, do not modify.

**Definition** i2c.h:447

[i2c\_target\_config::callbacks](structi2c__target__config.md#ad6c9573e97ac2569455f43f022600f77)

const struct i2c\_target\_callbacks \* callbacks

Callback functions.

**Definition** i2c.h:456

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5768

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:439

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:429

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:430

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:454

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:459

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:232

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:243

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:333

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c.h](drivers_2i2c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
