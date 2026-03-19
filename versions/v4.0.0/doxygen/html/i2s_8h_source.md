---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/i2s_8h_source.html
original_path: doxygen/html/i2s_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2s.h

[Go to the documentation of this file.](i2s_8h.md)

1/\*

2 \* Copyright (c) 2017 Piotr Mienkowski

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I2S\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_I2S\_H\_

14

27

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29#include <[zephyr/device.h](device_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

35/\*

36 \* The following #defines are used to configure the I2S controller.

37 \*/

38

[ 40](group__i2s__interface.md#ga0939a3ba04a233d9d637fba8a42b0bbb)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [i2s\_fmt\_t](group__i2s__interface.md#ga0939a3ba04a233d9d637fba8a42b0bbb);

41

[ 43](group__i2s__interface.md#gaa3f67c47874141782fbb7ec5a671b566)#define I2S\_FMT\_DATA\_FORMAT\_SHIFT 0

[ 45](group__i2s__interface.md#gaf3eb0116133dd3a041d9a80cb3397263)#define I2S\_FMT\_DATA\_FORMAT\_MASK (0x7 << I2S\_FMT\_DATA\_FORMAT\_SHIFT)

46

[ 64](group__i2s__interface.md#gaa1adc5e3b722e89f20f258b0fd53a2c5)#define I2S\_FMT\_DATA\_FORMAT\_I2S (0 << I2S\_FMT\_DATA\_FORMAT\_SHIFT)

65

[ 83](group__i2s__interface.md#ga70c7a19078a6f72e078b9c0488018b11)#define I2S\_FMT\_DATA\_FORMAT\_PCM\_SHORT (1 << I2S\_FMT\_DATA\_FORMAT\_SHIFT)

84

[ 103](group__i2s__interface.md#ga7032b1894faded14a174593a3f10ca3c)#define I2S\_FMT\_DATA\_FORMAT\_PCM\_LONG (2 << I2S\_FMT\_DATA\_FORMAT\_SHIFT)

104

[ 124](group__i2s__interface.md#gaabc5e62ed922b8c5834ed40c6af78022)#define I2S\_FMT\_DATA\_FORMAT\_LEFT\_JUSTIFIED (3 << I2S\_FMT\_DATA\_FORMAT\_SHIFT)

125

[ 145](group__i2s__interface.md#ga8ad25375c2f7344b2959bed2eec4be72)#define I2S\_FMT\_DATA\_FORMAT\_RIGHT\_JUSTIFIED (4 << I2S\_FMT\_DATA\_FORMAT\_SHIFT)

146

[ 148](group__i2s__interface.md#ga6a6c18e170333a56086f5bcf96e552a1)#define I2S\_FMT\_DATA\_ORDER\_MSB (0 << 3)

[ 150](group__i2s__interface.md#gacc2d0662903b2300b0e1009a8223ed7d)#define I2S\_FMT\_DATA\_ORDER\_LSB BIT(3)

[ 152](group__i2s__interface.md#ga052fa04f51ab96d90cdaf0d35f19a166)#define I2S\_FMT\_DATA\_ORDER\_INV I2S\_FMT\_DATA\_ORDER\_LSB

153

[ 155](group__i2s__interface.md#ga713fe1eb042953a315d1cb606a28d5ca)#define I2S\_FMT\_CLK\_FORMAT\_SHIFT 4

[ 157](group__i2s__interface.md#ga16e4b44cf7f4b2d11bbd2d50522d086d)#define I2S\_FMT\_CLK\_FORMAT\_MASK (0x3 << I2S\_FMT\_CLK\_FORMAT\_SHIFT)

158

[ 160](group__i2s__interface.md#ga1bbc3f0600b406691ce016bf7bf96a5f)#define I2S\_FMT\_BIT\_CLK\_INV BIT(4)

[ 162](group__i2s__interface.md#ga1cd356cbe68f622d0b3f5aee027d1f57)#define I2S\_FMT\_FRAME\_CLK\_INV BIT(5)

163

[ 165](group__i2s__interface.md#gad555437f250801cbc8970cd02d7b7cde)#define I2S\_FMT\_CLK\_NF\_NB (0 << I2S\_FMT\_CLK\_FORMAT\_SHIFT)

[ 167](group__i2s__interface.md#ga85714d803548509c6b41c2579b7f2a7f)#define I2S\_FMT\_CLK\_NF\_IB (1 << I2S\_FMT\_CLK\_FORMAT\_SHIFT)

[ 169](group__i2s__interface.md#ga5686ac4f8e3327d36f3f1293168330cd)#define I2S\_FMT\_CLK\_IF\_NB (2 << I2S\_FMT\_CLK\_FORMAT\_SHIFT)

[ 171](group__i2s__interface.md#gaaaf186e3265d2fea6c8dc43a8030272c)#define I2S\_FMT\_CLK\_IF\_IB (3 << I2S\_FMT\_CLK\_FORMAT\_SHIFT)

172

[ 174](group__i2s__interface.md#gad0ca475f9bf5edeecc7de65b4f56c119)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [i2s\_opt\_t](group__i2s__interface.md#gad0ca475f9bf5edeecc7de65b4f56c119);

175

[ 177](group__i2s__interface.md#ga039e7e244f7f1452dcd197c0a689d6e6)#define I2S\_OPT\_BIT\_CLK\_CONT (0 << 0)

[ 179](group__i2s__interface.md#ga4a68f73ee794684f68a02066ce1d632c)#define I2S\_OPT\_BIT\_CLK\_GATED BIT(0)

[ 181](group__i2s__interface.md#ga54aaaa7f0403e4f03574ffcc6141a67f)#define I2S\_OPT\_BIT\_CLK\_MASTER (0 << 1)

[ 183](group__i2s__interface.md#gaa76784ed4a645cb751b2c683bfa4be40)#define I2S\_OPT\_BIT\_CLK\_SLAVE BIT(1)

[ 185](group__i2s__interface.md#gaedfc35128aae5058a17ef5601bdc73d2)#define I2S\_OPT\_FRAME\_CLK\_MASTER (0 << 2)

[ 187](group__i2s__interface.md#ga138640dfb430fe0565840078a7b23ace)#define I2S\_OPT\_FRAME\_CLK\_SLAVE BIT(2)

188

[ 194](group__i2s__interface.md#ga093ed00a6081da8b4d958f80744fa09f)#define I2S\_OPT\_LOOPBACK BIT(7)

195

[ 204](group__i2s__interface.md#gadcb20e201a0fef1fe10f4cf916ff4b72)#define I2S\_OPT\_PINGPONG BIT(6)

205

[ 209](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f)enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) {

[ 211](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fac9f71d312c5d5ad7ef64af4217091aca) [I2S\_DIR\_RX](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fac9f71d312c5d5ad7ef64af4217091aca),

[ 213](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fab005c2cfee6206c2b5b596638e6c8443) [I2S\_DIR\_TX](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fab005c2cfee6206c2b5b596638e6c8443),

[ 215](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fa3cca349476d0dbe214111b9ef5d8b272) [I2S\_DIR\_BOTH](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fa3cca349476d0dbe214111b9ef5d8b272),

216};

217

[ 219](group__i2s__interface.md#ga975d09fe35ddf7942968155b62abc531)enum [i2s\_state](group__i2s__interface.md#ga975d09fe35ddf7942968155b62abc531) {

[ 226](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a7151755b31bbb614e7b668141a7ef43a) [I2S\_STATE\_NOT\_READY](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a7151755b31bbb614e7b668141a7ef43a),

[ 228](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531af6babeef999bfb034ea55366e9c59b13) [I2S\_STATE\_READY](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531af6babeef999bfb034ea55366e9c59b13),

[ 230](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531aa3d21ba793efa7d8f557774e8b330a42) [I2S\_STATE\_RUNNING](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531aa3d21ba793efa7d8f557774e8b330a42),

[ 232](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a972fd7e9da207b36e07731b996620a33) [I2S\_STATE\_STOPPING](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a972fd7e9da207b36e07731b996620a33),

[ 234](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a68c0a46589ae00045900a8f79675641a) [I2S\_STATE\_ERROR](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a68c0a46589ae00045900a8f79675641a),

235};

236

[ 238](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6)enum [i2s\_trigger\_cmd](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6) {

[ 245](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a6f4cacef6ee84256e6223a4bab3bc3ac) [I2S\_TRIGGER\_START](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a6f4cacef6ee84256e6223a4bab3bc3ac),

[ 255](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a37caf001d6ee6a263f3487f27952688b) [I2S\_TRIGGER\_STOP](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a37caf001d6ee6a263f3487f27952688b),

[ 264](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a7bdbdf37c5a6481faa1866be323bb9de) [I2S\_TRIGGER\_DRAIN](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a7bdbdf37c5a6481faa1866be323bb9de),

[ 271](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6ae8155a4d72875bd885dc987765d7628d) [I2S\_TRIGGER\_DROP](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6ae8155a4d72875bd885dc987765d7628d),

[ 277](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a61943bd287840e33bffd74bbc4a59e88) [I2S\_TRIGGER\_PREPARE](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a61943bd287840e33bffd74bbc4a59e88),

278};

279

[ 295](structi2s__config.md)struct [i2s\_config](structi2s__config.md) {

[ 297](structi2s__config.md#a5a38a75f0b4a3356ed85495fb45d0cd2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [word\_size](structi2s__config.md#a5a38a75f0b4a3356ed85495fb45d0cd2);

[ 299](structi2s__config.md#acd9ff8b9a0e79e95a8deb19df145478d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channels](structi2s__config.md#acd9ff8b9a0e79e95a8deb19df145478d);

[ 301](structi2s__config.md#a9ab2e8fa330473be99ce0713aec60daf) [i2s\_fmt\_t](group__i2s__interface.md#ga0939a3ba04a233d9d637fba8a42b0bbb) [format](structi2s__config.md#a9ab2e8fa330473be99ce0713aec60daf);

[ 303](structi2s__config.md#a56a9caaf8133ced8e47e3699e322fdab) [i2s\_opt\_t](group__i2s__interface.md#gad0ca475f9bf5edeecc7de65b4f56c119) [options](structi2s__config.md#a56a9caaf8133ced8e47e3699e322fdab);

[ 305](structi2s__config.md#ab5b0556fcd113c6c645e265af4846b45) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frame\_clk\_freq](structi2s__config.md#ab5b0556fcd113c6c645e265af4846b45);

[ 307](structi2s__config.md#a11991601fa180ead06a23b90a58136ff) struct k\_mem\_slab \*[mem\_slab](structi2s__config.md#a11991601fa180ead06a23b90a58136ff);

[ 309](structi2s__config.md#a62f504e954fc42c343d142513bbaf4ef) size\_t [block\_size](structi2s__config.md#a62f504e954fc42c343d142513bbaf4ef);

[ 313](structi2s__config.md#a9bf6c6cb96cc9c3acd8efc3fad0cbca9) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [timeout](structi2s__config.md#a9bf6c6cb96cc9c3acd8efc3fad0cbca9);

314};

315

321\_\_subsystem struct i2s\_driver\_api {

322 int (\*configure)(const struct [device](structdevice.md) \*dev, enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir,

323 const struct [i2s\_config](structi2s__config.md) \*cfg);

324 const struct [i2s\_config](structi2s__config.md) \*(\*config\_get)(const struct [device](structdevice.md) \*dev,

325 enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir);

326 int (\*read)(const struct [device](structdevice.md) \*dev, void \*\*mem\_block, size\_t \*size);

327 int (\*write)(const struct [device](structdevice.md) \*dev, void \*mem\_block, size\_t size);

328 int (\*trigger)(const struct [device](structdevice.md) \*dev, enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir,

329 enum [i2s\_trigger\_cmd](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

330};

334

[ 357](group__i2s__interface.md#ga299003d72146c127f88d7c12c08889cc)\_\_syscall int [i2s\_configure](group__i2s__interface.md#ga299003d72146c127f88d7c12c08889cc)(const struct [device](structdevice.md) \*dev, enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir,

358 const struct [i2s\_config](structi2s__config.md) \*cfg);

359

360static inline int z\_impl\_i2s\_configure(const struct [device](structdevice.md) \*dev,

361 enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir,

362 const struct [i2s\_config](structi2s__config.md) \*cfg)

363{

364 const struct i2s\_driver\_api \*api =

365 (const struct i2s\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

366

367 return api->configure(dev, dir, cfg);

368}

369

[ 378](group__i2s__interface.md#gacf4d51fcfd07573582858cd50a76785d)static inline const struct [i2s\_config](structi2s__config.md) \*[i2s\_config\_get](group__i2s__interface.md#gacf4d51fcfd07573582858cd50a76785d)(const struct [device](structdevice.md) \*dev,

379 enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir)

380{

381 const struct i2s\_driver\_api \*api =

382 (const struct i2s\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

383

384 return api->config\_get(dev, dir);

385}

386

[ 418](group__i2s__interface.md#ga7f23b7959280e1c4075a4305c3edd655)static inline int [i2s\_read](group__i2s__interface.md#ga7f23b7959280e1c4075a4305c3edd655)(const struct [device](structdevice.md) \*dev, void \*\*mem\_block,

419 size\_t \*size)

420{

421 const struct i2s\_driver\_api \*api =

422 (const struct i2s\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

423

424 return api->read(dev, mem\_block, size);

425}

426

[ 451](group__i2s__interface.md#ga5c8ca0bf6b394170ffbe031de8e37c28)\_\_syscall int [i2s\_buf\_read](group__i2s__interface.md#ga5c8ca0bf6b394170ffbe031de8e37c28)(const struct [device](structdevice.md) \*dev, void \*buf, size\_t \*size);

452

[ 479](group__i2s__interface.md#ga01edf23acc6c16bbaf718dab8061a7a0)static inline int [i2s\_write](group__i2s__interface.md#ga01edf23acc6c16bbaf718dab8061a7a0)(const struct [device](structdevice.md) \*dev, void \*mem\_block,

480 size\_t size)

481{

482 const struct i2s\_driver\_api \*api =

483 (const struct i2s\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

484

485 return api->write(dev, mem\_block, size);

486}

487

[ 507](group__i2s__interface.md#ga98cbfe351a8dd5db361f4667959d0b58)\_\_syscall int [i2s\_buf\_write](group__i2s__interface.md#ga98cbfe351a8dd5db361f4667959d0b58)(const struct [device](structdevice.md) \*dev, void \*buf, size\_t size);

508

[ 526](group__i2s__interface.md#gaaa153e6c325f8f34f2fd5d550e4d3297)\_\_syscall int [i2s\_trigger](group__i2s__interface.md#gaaa153e6c325f8f34f2fd5d550e4d3297)(const struct [device](structdevice.md) \*dev, enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir,

527 enum [i2s\_trigger\_cmd](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

528

529static inline int z\_impl\_i2s\_trigger(const struct [device](structdevice.md) \*dev,

530 enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir,

531 enum [i2s\_trigger\_cmd](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615))

532{

533 const struct i2s\_driver\_api \*api =

534 (const struct i2s\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

535

536 return api->trigger(dev, dir, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

537}

538

542

543#ifdef \_\_cplusplus

544}

545#endif

546

547#include <zephyr/syscalls/i2s.h>

548

549#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I2S\_H\_ \*/

[device.h](device_8h.md)

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[i2s\_write](group__i2s__interface.md#ga01edf23acc6c16bbaf718dab8061a7a0)

static int i2s\_write(const struct device \*dev, void \*mem\_block, size\_t size)

Write data to the TX queue.

**Definition** i2s.h:479

[i2s\_fmt\_t](group__i2s__interface.md#ga0939a3ba04a233d9d637fba8a42b0bbb)

uint8\_t i2s\_fmt\_t

I2S data stream format options.

**Definition** i2s.h:40

[i2s\_configure](group__i2s__interface.md#ga299003d72146c127f88d7c12c08889cc)

int i2s\_configure(const struct device \*dev, enum i2s\_dir dir, const struct i2s\_config \*cfg)

Configure operation of a host I2S controller.

[i2s\_buf\_read](group__i2s__interface.md#ga5c8ca0bf6b394170ffbe031de8e37c28)

int i2s\_buf\_read(const struct device \*dev, void \*buf, size\_t \*size)

Read data from the RX queue into a provided buffer.

[i2s\_read](group__i2s__interface.md#ga7f23b7959280e1c4075a4305c3edd655)

static int i2s\_read(const struct device \*dev, void \*\*mem\_block, size\_t \*size)

Read data from the RX queue.

**Definition** i2s.h:418

[i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f)

i2s\_dir

I2C Direction.

**Definition** i2s.h:209

[i2s\_state](group__i2s__interface.md#ga975d09fe35ddf7942968155b62abc531)

i2s\_state

Interface state.

**Definition** i2s.h:219

[i2s\_buf\_write](group__i2s__interface.md#ga98cbfe351a8dd5db361f4667959d0b58)

int i2s\_buf\_write(const struct device \*dev, void \*buf, size\_t size)

Write data to the TX queue from a provided buffer.

[i2s\_trigger](group__i2s__interface.md#gaaa153e6c325f8f34f2fd5d550e4d3297)

int i2s\_trigger(const struct device \*dev, enum i2s\_dir dir, enum i2s\_trigger\_cmd cmd)

Send a trigger command.

[i2s\_trigger\_cmd](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6)

i2s\_trigger\_cmd

Trigger command.

**Definition** i2s.h:238

[i2s\_config\_get](group__i2s__interface.md#gacf4d51fcfd07573582858cd50a76785d)

static const struct i2s\_config \* i2s\_config\_get(const struct device \*dev, enum i2s\_dir dir)

Fetch configuration information of a host I2S controller.

**Definition** i2s.h:378

[i2s\_opt\_t](group__i2s__interface.md#gad0ca475f9bf5edeecc7de65b4f56c119)

uint8\_t i2s\_opt\_t

I2S configuration options.

**Definition** i2s.h:174

[I2S\_DIR\_BOTH](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fa3cca349476d0dbe214111b9ef5d8b272)

@ I2S\_DIR\_BOTH

Both receive and transmit data.

**Definition** i2s.h:215

[I2S\_DIR\_TX](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fab005c2cfee6206c2b5b596638e6c8443)

@ I2S\_DIR\_TX

Transmit data.

**Definition** i2s.h:213

[I2S\_DIR\_RX](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fac9f71d312c5d5ad7ef64af4217091aca)

@ I2S\_DIR\_RX

Receive data.

**Definition** i2s.h:211

[I2S\_STATE\_ERROR](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a68c0a46589ae00045900a8f79675641a)

@ I2S\_STATE\_ERROR

TX buffer underrun or RX buffer overrun has occurred.

**Definition** i2s.h:234

[I2S\_STATE\_NOT\_READY](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a7151755b31bbb614e7b668141a7ef43a)

@ I2S\_STATE\_NOT\_READY

The interface is not ready.

**Definition** i2s.h:226

[I2S\_STATE\_STOPPING](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a972fd7e9da207b36e07731b996620a33)

@ I2S\_STATE\_STOPPING

The interface is draining its transmit queue.

**Definition** i2s.h:232

[I2S\_STATE\_RUNNING](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531aa3d21ba793efa7d8f557774e8b330a42)

@ I2S\_STATE\_RUNNING

The interface is receiving / transmitting data.

**Definition** i2s.h:230

[I2S\_STATE\_READY](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531af6babeef999bfb034ea55366e9c59b13)

@ I2S\_STATE\_READY

The interface is ready to receive / transmit data.

**Definition** i2s.h:228

[I2S\_TRIGGER\_STOP](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a37caf001d6ee6a263f3487f27952688b)

@ I2S\_TRIGGER\_STOP

Stop the transmission / reception of data.

**Definition** i2s.h:255

[I2S\_TRIGGER\_PREPARE](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a61943bd287840e33bffd74bbc4a59e88)

@ I2S\_TRIGGER\_PREPARE

Prepare the queues after underrun/overrun error has occurred.

**Definition** i2s.h:277

[I2S\_TRIGGER\_START](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a6f4cacef6ee84256e6223a4bab3bc3ac)

@ I2S\_TRIGGER\_START

Start the transmission / reception of data.

**Definition** i2s.h:245

[I2S\_TRIGGER\_DRAIN](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a7bdbdf37c5a6481faa1866be323bb9de)

@ I2S\_TRIGGER\_DRAIN

Empty the transmit queue.

**Definition** i2s.h:264

[I2S\_TRIGGER\_DROP](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6ae8155a4d72875bd885dc987765d7628d)

@ I2S\_TRIGGER\_DROP

Discard the transmit / receive queue.

**Definition** i2s.h:271

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[i2s\_config](structi2s__config.md)

Interface configuration options.

**Definition** i2s.h:295

[i2s\_config::mem\_slab](structi2s__config.md#a11991601fa180ead06a23b90a58136ff)

struct k\_mem\_slab \* mem\_slab

Memory slab to store RX/TX data.

**Definition** i2s.h:307

[i2s\_config::options](structi2s__config.md#a56a9caaf8133ced8e47e3699e322fdab)

i2s\_opt\_t options

Configuration options as defined by I2S\_OPT\_\* constants.

**Definition** i2s.h:303

[i2s\_config::word\_size](structi2s__config.md#a5a38a75f0b4a3356ed85495fb45d0cd2)

uint8\_t word\_size

Number of bits representing one data word.

**Definition** i2s.h:297

[i2s\_config::block\_size](structi2s__config.md#a62f504e954fc42c343d142513bbaf4ef)

size\_t block\_size

Size of one RX/TX memory block (buffer) in bytes.

**Definition** i2s.h:309

[i2s\_config::format](structi2s__config.md#a9ab2e8fa330473be99ce0713aec60daf)

i2s\_fmt\_t format

Data stream format as defined by I2S\_FMT\_\* constants.

**Definition** i2s.h:301

[i2s\_config::timeout](structi2s__config.md#a9bf6c6cb96cc9c3acd8efc3fad0cbca9)

int32\_t timeout

Read/Write timeout.

**Definition** i2s.h:313

[i2s\_config::frame\_clk\_freq](structi2s__config.md#ab5b0556fcd113c6c645e265af4846b45)

uint32\_t frame\_clk\_freq

Frame clock (WS) frequency, this is sampling rate.

**Definition** i2s.h:305

[i2s\_config::channels](structi2s__config.md#acd9ff8b9a0e79e95a8deb19df145478d)

uint8\_t channels

Number of words per frame.

**Definition** i2s.h:299

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2s.h](i2s_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
