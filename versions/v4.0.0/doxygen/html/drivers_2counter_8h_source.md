---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2counter_8h_source.html
original_path: doxygen/html/drivers_2counter_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter.h

[Go to the documentation of this file.](drivers_2counter_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \* Copyright (c) 2016 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_COUNTER\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_COUNTER\_H\_

15

24

25#include <[errno.h](errno_8h.md)>

26

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <stddef.h>

29#include <[zephyr/device.h](device_8h.md)>

30#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

31#include <[stdbool.h](stdbool_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

42

[ 46](group__counter__interface.md#ga8fa40ff6404936e5b05bb9c67871f70c)#define COUNTER\_CONFIG\_INFO\_COUNT\_UP BIT(0)

47

49

55

[ 62](group__counter__interface.md#ga9a30c647361912c2ce8e0566cf53dea7)#define COUNTER\_TOP\_CFG\_DONT\_RESET BIT(0)

63

[ 70](group__counter__interface.md#ga45562a4ddd743f74213a03d83a774b11)#define COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE BIT(1)

71

73

80

[ 87](group__counter__interface.md#ga4842d212424f92c5a3b39116ec6c2fd2)#define COUNTER\_ALARM\_CFG\_ABSOLUTE BIT(0)

88

[ 95](group__counter__interface.md#ga87dffd2a1cadedfc30e7d39af547c336)#define COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE BIT(1)

96

98

106

[ 111](group__counter__interface.md#ga6d955e603067b5c50e0fd9761e2e611d)#define COUNTER\_GUARD\_PERIOD\_LATE\_TO\_SET BIT(0)

112

114

[ 122](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77)typedef void (\*[counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77))(const struct [device](structdevice.md) \*dev,

123 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks,

124 void \*user\_data);

125

[ 128](structcounter__alarm__cfg.md)struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) {

[ 132](structcounter__alarm__cfg.md#aeef670ee73dd4d7d65e02a66313b092d) [counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77) [callback](structcounter__alarm__cfg.md#aeef670ee73dd4d7d65e02a66313b092d);

[ 149](structcounter__alarm__cfg.md#a85b6b86d7a82f2e238000dd31ff1f779) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ticks](structcounter__alarm__cfg.md#a85b6b86d7a82f2e238000dd31ff1f779);

[ 153](structcounter__alarm__cfg.md#aeaf2bd9042a28b626e0972aff4ad09e5) void \*[user\_data](structcounter__alarm__cfg.md#aeaf2bd9042a28b626e0972aff4ad09e5);

[ 157](structcounter__alarm__cfg.md#ab043cd1ea9be54449bb75c4a5affe620) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structcounter__alarm__cfg.md#ab043cd1ea9be54449bb75c4a5affe620);

158};

159

[ 165](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf)typedef void (\*[counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf))(const struct [device](structdevice.md) \*dev,

166 void \*user\_data);

167

[ 170](structcounter__top__cfg.md)struct [counter\_top\_cfg](structcounter__top__cfg.md) {

[ 174](structcounter__top__cfg.md#abb60a9d468fa6d6802ba56a02a515751) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ticks](structcounter__top__cfg.md#abb60a9d468fa6d6802ba56a02a515751);

[ 178](structcounter__top__cfg.md#adf1cf3a9c67278f5f5f1cba72f6dd934) [counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf) [callback](structcounter__top__cfg.md#adf1cf3a9c67278f5f5f1cba72f6dd934);

[ 182](structcounter__top__cfg.md#af033941769c710e82cf9dd9f12ff011c) void \*[user\_data](structcounter__top__cfg.md#af033941769c710e82cf9dd9f12ff011c);

[ 186](structcounter__top__cfg.md#ad5caa9f1c80badf14c2c313e60e3e8e6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structcounter__top__cfg.md#ad5caa9f1c80badf14c2c313e60e3e8e6);

187};

188

[ 191](structcounter__config__info.md)struct [counter\_config\_info](structcounter__config__info.md) {

[ 195](structcounter__config__info.md#a0465be87680d1a50e1ae7a68c61caaac) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_top\_value](structcounter__config__info.md#a0465be87680d1a50e1ae7a68c61caaac);

[ 199](structcounter__config__info.md#a4cae02b246a92e5d207d5b654d059322) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [freq](structcounter__config__info.md#a4cae02b246a92e5d207d5b654d059322);

[ 203](structcounter__config__info.md#ab38d95647388c700de372882db372d6c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structcounter__config__info.md#ab38d95647388c700de372882db372d6c);

[ 209](structcounter__config__info.md#afe2281d1909fa85978077558d6f4b71f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channels](structcounter__config__info.md#afe2281d1909fa85978077558d6f4b71f);

210};

211

[ 212](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81)typedef int (\*[counter\_api\_start](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81))(const struct [device](structdevice.md) \*dev);

[ 213](group__counter__interface.md#ga25ac7589f6501dada1e10b1980fca7de)typedef int (\*[counter\_api\_stop](group__counter__interface.md#ga25ac7589f6501dada1e10b1980fca7de))(const struct [device](structdevice.md) \*dev);

[ 214](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f)typedef int (\*[counter\_api\_get\_value](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f))(const struct [device](structdevice.md) \*dev,

215 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks);

[ 216](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e)typedef int (\*[counter\_api\_get\_value\_64](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e))(const struct [device](structdevice.md) \*dev,

217 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks);

[ 218](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387)typedef int (\*[counter\_api\_set\_alarm](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387))(const struct [device](structdevice.md) \*dev,

219 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id,

220 const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg);

[ 221](group__counter__interface.md#gac368afac6de0fe1f782fdb90e6f7c266)typedef int (\*[counter\_api\_cancel\_alarm](group__counter__interface.md#gac368afac6de0fe1f782fdb90e6f7c266))(const struct [device](structdevice.md) \*dev,

222 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id);

[ 223](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8)typedef int (\*[counter\_api\_set\_top\_value](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8))(const struct [device](structdevice.md) \*dev,

224 const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg);

[ 225](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[counter\_api\_get\_pending\_int](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba))(const struct [device](structdevice.md) \*dev);

[ 226](group__counter__interface.md#ga08ca9b32fbc96da83b75844f7b6218b2)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[counter\_api\_get\_top\_value](group__counter__interface.md#ga08ca9b32fbc96da83b75844f7b6218b2))(const struct [device](structdevice.md) \*dev);

[ 227](group__counter__interface.md#ga90b573190980a935d3984029831739a9)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[counter\_api\_get\_guard\_period](group__counter__interface.md#ga90b573190980a935d3984029831739a9))(const struct [device](structdevice.md) \*dev,

228 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 229](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d)typedef int (\*[counter\_api\_set\_guard\_period](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d))(const struct [device](structdevice.md) \*dev,

230 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks,

231 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 232](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[counter\_api\_get\_freq](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024))(const struct [device](structdevice.md) \*dev);

233

[ 234](structcounter__driver__api.md)\_\_subsystem struct [counter\_driver\_api](structcounter__driver__api.md) {

[ 235](structcounter__driver__api.md#aa8fd91ec6e2357ece10c9e8ea37f9336) [counter\_api\_start](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81) [start](structcounter__driver__api.md#aa8fd91ec6e2357ece10c9e8ea37f9336);

[ 236](structcounter__driver__api.md#a9d1b590187c0eccd11f8c7c80da967ce) [counter\_api\_stop](group__counter__interface.md#ga25ac7589f6501dada1e10b1980fca7de) [stop](structcounter__driver__api.md#a9d1b590187c0eccd11f8c7c80da967ce);

[ 237](structcounter__driver__api.md#a7d7b07f9d6e63ef931d81ad52076b2e1) [counter\_api\_get\_value](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f) [get\_value](structcounter__driver__api.md#a7d7b07f9d6e63ef931d81ad52076b2e1);

[ 238](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1) [counter\_api\_get\_value\_64](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e) [get\_value\_64](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1);

[ 239](structcounter__driver__api.md#a67a3939d4c25b49abdf6f34929ed00a0) [counter\_api\_set\_alarm](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387) [set\_alarm](structcounter__driver__api.md#a67a3939d4c25b49abdf6f34929ed00a0);

[ 240](structcounter__driver__api.md#af002080c967fa3a2e2eaadd0b4ee35ae) [counter\_api\_cancel\_alarm](group__counter__interface.md#gac368afac6de0fe1f782fdb90e6f7c266) [cancel\_alarm](structcounter__driver__api.md#af002080c967fa3a2e2eaadd0b4ee35ae);

[ 241](structcounter__driver__api.md#a5479ccee1057fecacddfbbf49edc0537) [counter\_api\_set\_top\_value](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8) [set\_top\_value](structcounter__driver__api.md#a5479ccee1057fecacddfbbf49edc0537);

[ 242](structcounter__driver__api.md#a8daec24721653215df3b36afc7c21168) [counter\_api\_get\_pending\_int](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba) [get\_pending\_int](structcounter__driver__api.md#a8daec24721653215df3b36afc7c21168);

[ 243](structcounter__driver__api.md#a3571f7310b7aed43df6e620f93aa1521) [counter\_api\_get\_top\_value](group__counter__interface.md#ga08ca9b32fbc96da83b75844f7b6218b2) [get\_top\_value](structcounter__driver__api.md#a3571f7310b7aed43df6e620f93aa1521);

[ 244](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4) [counter\_api\_get\_guard\_period](group__counter__interface.md#ga90b573190980a935d3984029831739a9) [get\_guard\_period](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4);

[ 245](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3) [counter\_api\_set\_guard\_period](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d) [set\_guard\_period](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3);

[ 246](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df) [counter\_api\_get\_freq](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024) [get\_freq](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df);

247};

248

[ 257](group__counter__interface.md#gab95ae0e8d89e35e477cbf7d67e18016d)\_\_syscall bool [counter\_is\_counting\_up](group__counter__interface.md#gab95ae0e8d89e35e477cbf7d67e18016d)(const struct [device](structdevice.md) \*dev);

258

259static inline bool z\_impl\_counter\_is\_counting\_up(const struct [device](structdevice.md) \*dev)

260{

261 const struct [counter\_config\_info](structcounter__config__info.md) \*config =

262 (const struct [counter\_config\_info](structcounter__config__info.md) \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

263

264 return config->flags & [COUNTER\_CONFIG\_INFO\_COUNT\_UP](group__counter__interface.md#ga8fa40ff6404936e5b05bb9c67871f70c);

265}

266

[ 274](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)\_\_syscall [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [counter\_get\_num\_of\_channels](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)(const struct [device](structdevice.md) \*dev);

275

276static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) z\_impl\_counter\_get\_num\_of\_channels(const struct [device](structdevice.md) \*dev)

277{

278 const struct [counter\_config\_info](structcounter__config__info.md) \*config =

279 (const struct [counter\_config\_info](structcounter__config__info.md) \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

280

281 return config->channels;

282}

283

[ 292](group__counter__interface.md#ga8d3d6f856eef27a80cc2697931341af2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_get\_frequency](group__counter__interface.md#ga8d3d6f856eef27a80cc2697931341af2)(const struct [device](structdevice.md) \*dev);

293

294static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_get\_frequency(const struct [device](structdevice.md) \*dev)

295{

296 const struct [counter\_config\_info](structcounter__config__info.md) \*config =

297 (const struct [counter\_config\_info](structcounter__config__info.md) \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

298 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

299 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->api;

300

301 return api->[get\_freq](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df) ? api->[get\_freq](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df)(dev) : config->freq;

302}

303

[ 312](group__counter__interface.md#gab73238b8d52ed763ff7abf91013b601b)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_us\_to\_ticks](group__counter__interface.md#gab73238b8d52ed763ff7abf91013b601b)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) us);

313

314static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_us\_to\_ticks(const struct [device](structdevice.md) \*dev,

315 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) us)

316{

317 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ticks = (us \* z\_impl\_counter\_get\_frequency(dev)) / [USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1);

318

319 return (ticks > ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)) ? [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd) : ticks;

320}

321

[ 330](group__counter__interface.md#ga9fbcb710091084e638c45f62c25d954c)\_\_syscall [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [counter\_ticks\_to\_us](group__counter__interface.md#ga9fbcb710091084e638c45f62c25d954c)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks);

331

332static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_impl\_counter\_ticks\_to\_us(const struct [device](structdevice.md) \*dev,

333 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks)

334{

335 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))ticks \* [USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)) / z\_impl\_counter\_get\_frequency(dev);

336}

337

[ 345](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_get\_max\_top\_value](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3)(const struct [device](structdevice.md) \*dev);

346

347static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_get\_max\_top\_value(const struct [device](structdevice.md) \*dev)

348{

349 const struct [counter\_config\_info](structcounter__config__info.md) \*config =

350 (const struct [counter\_config\_info](structcounter__config__info.md) \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

351

352 return config->max\_top\_value;

353}

354

[ 363](group__counter__interface.md#ga103e0673e31475adcd173601058c72cd)\_\_syscall int [counter\_start](group__counter__interface.md#ga103e0673e31475adcd173601058c72cd)(const struct [device](structdevice.md) \*dev);

364

365static inline int z\_impl\_counter\_start(const struct [device](structdevice.md) \*dev)

366{

367 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

368 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

369

370 return api->[start](structcounter__driver__api.md#aa8fd91ec6e2357ece10c9e8ea37f9336)(dev);

371}

372

[ 382](group__counter__interface.md#gafaa8198ccff5ffc0491a1424d090c82d)\_\_syscall int [counter\_stop](group__counter__interface.md#gafaa8198ccff5ffc0491a1424d090c82d)(const struct [device](structdevice.md) \*dev);

383

384static inline int z\_impl\_counter\_stop(const struct [device](structdevice.md) \*dev)

385{

386 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

387 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

388

389 return api->[stop](structcounter__driver__api.md#a9d1b590187c0eccd11f8c7c80da967ce)(dev);

390}

391

[ 400](group__counter__interface.md#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d)\_\_syscall int [counter\_get\_value](group__counter__interface.md#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks);

401

402static inline int z\_impl\_counter\_get\_value(const struct [device](structdevice.md) \*dev,

403 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks)

404{

405 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

406 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

407

408 return api->[get\_value](structcounter__driver__api.md#a7d7b07f9d6e63ef931d81ad52076b2e1)(dev, ticks);

409}

410

[ 419](group__counter__interface.md#ga2dcd0eb10d49c4e5e5024ed75a8e3e86)\_\_syscall int [counter\_get\_value\_64](group__counter__interface.md#ga2dcd0eb10d49c4e5e5024ed75a8e3e86)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks);

420

421static inline int z\_impl\_counter\_get\_value\_64(const struct [device](structdevice.md) \*dev,

422 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks)

423{

424 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

425 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

426

427 if (!api->[get\_value\_64](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1)) {

428 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

429 }

430

431 return api->[get\_value\_64](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1)(dev, ticks);

432}

433

[ 454](group__counter__interface.md#ga00a2857d993a84a56e8e222727f3d85e)\_\_syscall int [counter\_set\_channel\_alarm](group__counter__interface.md#ga00a2857d993a84a56e8e222727f3d85e)(const struct [device](structdevice.md) \*dev,

455 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id,

456 const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg);

457

458static inline int z\_impl\_counter\_set\_channel\_alarm(const struct [device](structdevice.md) \*dev,

459 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id,

460 const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg)

461{

462 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

463 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

464

465 if (chan\_id >= [counter\_get\_num\_of\_channels](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)(dev)) {

466 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

467 }

468

469 return api->[set\_alarm](structcounter__driver__api.md#a67a3939d4c25b49abdf6f34929ed00a0)(dev, chan\_id, alarm\_cfg);

470}

471

[ 484](group__counter__interface.md#gade0bb97c0dfa03676d11ee47601d4cee)\_\_syscall int [counter\_cancel\_channel\_alarm](group__counter__interface.md#gade0bb97c0dfa03676d11ee47601d4cee)(const struct [device](structdevice.md) \*dev,

485 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id);

486

487static inline int z\_impl\_counter\_cancel\_channel\_alarm(const struct [device](structdevice.md) \*dev,

488 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id)

489{

490 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

491 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

492

493 if (chan\_id >= [counter\_get\_num\_of\_channels](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)(dev)) {

494 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

495 }

496

497 return api->[cancel\_alarm](structcounter__driver__api.md#af002080c967fa3a2e2eaadd0b4ee35ae)(dev, chan\_id);

498}

499

[ 524](group__counter__interface.md#ga2d92f5564cdd1ecc56029c3a45e666f0)\_\_syscall int [counter\_set\_top\_value](group__counter__interface.md#ga2d92f5564cdd1ecc56029c3a45e666f0)(const struct [device](structdevice.md) \*dev,

525 const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg);

526

527static inline int z\_impl\_counter\_set\_top\_value(const struct [device](structdevice.md) \*dev,

528 const struct [counter\_top\_cfg](structcounter__top__cfg.md)

529 \*cfg)

530{

531 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

532 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

533

534 if (cfg->ticks > [counter\_get\_max\_top\_value](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3)(dev)) {

535 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

536 }

537

538 return api->[set\_top\_value](structcounter__driver__api.md#a5479ccee1057fecacddfbbf49edc0537)(dev, cfg);

539}

540

[ 554](group__counter__interface.md#ga3b74a79a09cbe3849658a746e7417a06)\_\_syscall int [counter\_get\_pending\_int](group__counter__interface.md#ga3b74a79a09cbe3849658a746e7417a06)(const struct [device](structdevice.md) \*dev);

555

556static inline int z\_impl\_counter\_get\_pending\_int(const struct [device](structdevice.md) \*dev)

557{

558 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

559 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

560

561 return api->[get\_pending\_int](structcounter__driver__api.md#a8daec24721653215df3b36afc7c21168)(dev);

562}

563

[ 571](group__counter__interface.md#ga13d14903a03ab10062002a81b8302424)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_get\_top\_value](group__counter__interface.md#ga13d14903a03ab10062002a81b8302424)(const struct [device](structdevice.md) \*dev);

572

573static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_get\_top\_value(const struct [device](structdevice.md) \*dev)

574{

575 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

576 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

577

578 return api->[get\_top\_value](structcounter__driver__api.md#a3571f7310b7aed43df6e620f93aa1521)(dev);

579}

580

[ 633](group__counter__interface.md#gab6851411dabf191d3391715d632111b0)\_\_syscall int [counter\_set\_guard\_period](group__counter__interface.md#gab6851411dabf191d3391715d632111b0)(const struct [device](structdevice.md) \*dev,

634 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks,

635 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

636

637static inline int z\_impl\_counter\_set\_guard\_period(const struct [device](structdevice.md) \*dev,

638 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

639{

640 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

641 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

642

643 if (!api->[set\_guard\_period](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3)) {

644 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

645 }

646

647 return api->[set\_guard\_period](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3)(dev, ticks, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

648}

649

[ 661](group__counter__interface.md#ga55a101d237c8472ad5cacf65363c536f)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_get\_guard\_period](group__counter__interface.md#ga55a101d237c8472ad5cacf65363c536f)(const struct [device](structdevice.md) \*dev,

662 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

663

664static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_get\_guard\_period(const struct [device](structdevice.md) \*dev,

665 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

666{

667 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

668 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

669

670 return (api->[get\_guard\_period](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4)) ? api->[get\_guard\_period](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4)(dev, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) : 0;

671}

672

673#ifdef \_\_cplusplus

674}

675#endif

676

680

681#include <zephyr/syscalls/counter.h>

682

683#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_COUNTER\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)

#define USEC\_PER\_SEC

number of microseconds per second

**Definition** sys\_clock.h:104

[counter\_set\_channel\_alarm](group__counter__interface.md#ga00a2857d993a84a56e8e222727f3d85e)

int counter\_set\_channel\_alarm(const struct device \*dev, uint8\_t chan\_id, const struct counter\_alarm\_cfg \*alarm\_cfg)

Set a single shot alarm on a channel.

[counter\_api\_get\_top\_value](group__counter__interface.md#ga08ca9b32fbc96da83b75844f7b6218b2)

uint32\_t(\* counter\_api\_get\_top\_value)(const struct device \*dev)

**Definition** counter.h:226

[counter\_get\_num\_of\_channels](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)

uint8\_t counter\_get\_num\_of\_channels(const struct device \*dev)

Function to get number of alarm channels.

[counter\_start](group__counter__interface.md#ga103e0673e31475adcd173601058c72cd)

int counter\_start(const struct device \*dev)

Start counter device in free running mode.

[counter\_get\_top\_value](group__counter__interface.md#ga13d14903a03ab10062002a81b8302424)

uint32\_t counter\_get\_top\_value(const struct device \*dev)

Function to retrieve current top value.

[counter\_api\_stop](group__counter__interface.md#ga25ac7589f6501dada1e10b1980fca7de)

int(\* counter\_api\_stop)(const struct device \*dev)

**Definition** counter.h:213

[counter\_set\_top\_value](group__counter__interface.md#ga2d92f5564cdd1ecc56029c3a45e666f0)

int counter\_set\_top\_value(const struct device \*dev, const struct counter\_top\_cfg \*cfg)

Set counter top value.

[counter\_get\_value\_64](group__counter__interface.md#ga2dcd0eb10d49c4e5e5024ed75a8e3e86)

int counter\_get\_value\_64(const struct device \*dev, uint64\_t \*ticks)

Get current counter 64-bit value.

[counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf)

void(\* counter\_top\_callback\_t)(const struct device \*dev, void \*user\_data)

Callback called when counter turns around.

**Definition** counter.h:165

[counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77)

void(\* counter\_alarm\_callback\_t)(const struct device \*dev, uint8\_t chan\_id, uint32\_t ticks, void \*user\_data)

Alarm callback.

**Definition** counter.h:122

[counter\_get\_pending\_int](group__counter__interface.md#ga3b74a79a09cbe3849658a746e7417a06)

int counter\_get\_pending\_int(const struct device \*dev)

Function to get pending interrupts.

[counter\_get\_guard\_period](group__counter__interface.md#ga55a101d237c8472ad5cacf65363c536f)

uint32\_t counter\_get\_guard\_period(const struct device \*dev, uint32\_t flags)

Return guard period.

[counter\_api\_set\_guard\_period](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d)

int(\* counter\_api\_set\_guard\_period)(const struct device \*dev, uint32\_t ticks, uint32\_t flags)

**Definition** counter.h:229

[counter\_get\_frequency](group__counter__interface.md#ga8d3d6f856eef27a80cc2697931341af2)

uint32\_t counter\_get\_frequency(const struct device \*dev)

Function to get counter frequency.

[counter\_get\_value](group__counter__interface.md#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d)

int counter\_get\_value(const struct device \*dev, uint32\_t \*ticks)

Get current counter value.

[COUNTER\_CONFIG\_INFO\_COUNT\_UP](group__counter__interface.md#ga8fa40ff6404936e5b05bb9c67871f70c)

#define COUNTER\_CONFIG\_INFO\_COUNT\_UP

Counter count up flag.

**Definition** counter.h:46

[counter\_api\_get\_guard\_period](group__counter__interface.md#ga90b573190980a935d3984029831739a9)

uint32\_t(\* counter\_api\_get\_guard\_period)(const struct device \*dev, uint32\_t flags)

**Definition** counter.h:227

[counter\_api\_get\_pending\_int](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba)

uint32\_t(\* counter\_api\_get\_pending\_int)(const struct device \*dev)

**Definition** counter.h:225

[counter\_api\_get\_freq](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024)

uint32\_t(\* counter\_api\_get\_freq)(const struct device \*dev)

**Definition** counter.h:232

[counter\_ticks\_to\_us](group__counter__interface.md#ga9fbcb710091084e638c45f62c25d954c)

uint64\_t counter\_ticks\_to\_us(const struct device \*dev, uint32\_t ticks)

Function to convert ticks to microseconds.

[counter\_api\_set\_top\_value](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8)

int(\* counter\_api\_set\_top\_value)(const struct device \*dev, const struct counter\_top\_cfg \*cfg)

**Definition** counter.h:223

[counter\_api\_start](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81)

int(\* counter\_api\_start)(const struct device \*dev)

**Definition** counter.h:212

[counter\_set\_guard\_period](group__counter__interface.md#gab6851411dabf191d3391715d632111b0)

int counter\_set\_guard\_period(const struct device \*dev, uint32\_t ticks, uint32\_t flags)

Set guard period in counter ticks.

[counter\_us\_to\_ticks](group__counter__interface.md#gab73238b8d52ed763ff7abf91013b601b)

uint32\_t counter\_us\_to\_ticks(const struct device \*dev, uint64\_t us)

Function to convert microseconds to ticks.

[counter\_is\_counting\_up](group__counter__interface.md#gab95ae0e8d89e35e477cbf7d67e18016d)

bool counter\_is\_counting\_up(const struct device \*dev)

Function to check if counter is counting up.

[counter\_api\_cancel\_alarm](group__counter__interface.md#gac368afac6de0fe1f782fdb90e6f7c266)

int(\* counter\_api\_cancel\_alarm)(const struct device \*dev, uint8\_t chan\_id)

**Definition** counter.h:221

[counter\_api\_get\_value\_64](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e)

int(\* counter\_api\_get\_value\_64)(const struct device \*dev, uint64\_t \*ticks)

**Definition** counter.h:216

[counter\_api\_get\_value](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f)

int(\* counter\_api\_get\_value)(const struct device \*dev, uint32\_t \*ticks)

**Definition** counter.h:214

[counter\_cancel\_channel\_alarm](group__counter__interface.md#gade0bb97c0dfa03676d11ee47601d4cee)

int counter\_cancel\_channel\_alarm(const struct device \*dev, uint8\_t chan\_id)

Cancel an alarm on a channel.

[counter\_api\_set\_alarm](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387)

int(\* counter\_api\_set\_alarm)(const struct device \*dev, uint8\_t chan\_id, const struct counter\_alarm\_cfg \*alarm\_cfg)

**Definition** counter.h:218

[counter\_stop](group__counter__interface.md#gafaa8198ccff5ffc0491a1424d090c82d)

int counter\_stop(const struct device \*dev)

Stop counter device.

[counter\_get\_max\_top\_value](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3)

uint32\_t counter\_get\_max\_top\_value(const struct device \*dev)

Function to retrieve maximum top value that can be set.

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)

#define UINT32\_MAX

**Definition** stdint.h:29

[counter\_alarm\_cfg](structcounter__alarm__cfg.md)

Alarm callback structure.

**Definition** counter.h:128

[counter\_alarm\_cfg::ticks](structcounter__alarm__cfg.md#a85b6b86d7a82f2e238000dd31ff1f779)

uint32\_t ticks

Number of ticks that triggers the alarm.

**Definition** counter.h:149

[counter\_alarm\_cfg::flags](structcounter__alarm__cfg.md#ab043cd1ea9be54449bb75c4a5affe620)

uint32\_t flags

Alarm flags (see COUNTER\_ALARM\_FLAGS).

**Definition** counter.h:157

[counter\_alarm\_cfg::user\_data](structcounter__alarm__cfg.md#aeaf2bd9042a28b626e0972aff4ad09e5)

void \* user\_data

User data returned in callback.

**Definition** counter.h:153

[counter\_alarm\_cfg::callback](structcounter__alarm__cfg.md#aeef670ee73dd4d7d65e02a66313b092d)

counter\_alarm\_callback\_t callback

Callback called on alarm (cannot be NULL).

**Definition** counter.h:132

[counter\_config\_info](structcounter__config__info.md)

Structure with generic counter features.

**Definition** counter.h:191

[counter\_config\_info::max\_top\_value](structcounter__config__info.md#a0465be87680d1a50e1ae7a68c61caaac)

uint32\_t max\_top\_value

Maximal (default) top value on which counter is reset (cleared or reloaded).

**Definition** counter.h:195

[counter\_config\_info::freq](structcounter__config__info.md#a4cae02b246a92e5d207d5b654d059322)

uint32\_t freq

Frequency of the source clock if synchronous events are counted.

**Definition** counter.h:199

[counter\_config\_info::flags](structcounter__config__info.md#ab38d95647388c700de372882db372d6c)

uint8\_t flags

Flags (see COUNTER\_FLAGS).

**Definition** counter.h:203

[counter\_config\_info::channels](structcounter__config__info.md#afe2281d1909fa85978077558d6f4b71f)

uint8\_t channels

Number of channels that can be used for setting alarm.

**Definition** counter.h:209

[counter\_driver\_api](structcounter__driver__api.md)

**Definition** counter.h:234

[counter\_driver\_api::get\_value\_64](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1)

counter\_api\_get\_value\_64 get\_value\_64

**Definition** counter.h:238

[counter\_driver\_api::get\_top\_value](structcounter__driver__api.md#a3571f7310b7aed43df6e620f93aa1521)

counter\_api\_get\_top\_value get\_top\_value

**Definition** counter.h:243

[counter\_driver\_api::set\_top\_value](structcounter__driver__api.md#a5479ccee1057fecacddfbbf49edc0537)

counter\_api\_set\_top\_value set\_top\_value

**Definition** counter.h:241

[counter\_driver\_api::set\_alarm](structcounter__driver__api.md#a67a3939d4c25b49abdf6f34929ed00a0)

counter\_api\_set\_alarm set\_alarm

**Definition** counter.h:239

[counter\_driver\_api::get\_value](structcounter__driver__api.md#a7d7b07f9d6e63ef931d81ad52076b2e1)

counter\_api\_get\_value get\_value

**Definition** counter.h:237

[counter\_driver\_api::get\_pending\_int](structcounter__driver__api.md#a8daec24721653215df3b36afc7c21168)

counter\_api\_get\_pending\_int get\_pending\_int

**Definition** counter.h:242

[counter\_driver\_api::stop](structcounter__driver__api.md#a9d1b590187c0eccd11f8c7c80da967ce)

counter\_api\_stop stop

**Definition** counter.h:236

[counter\_driver\_api::set\_guard\_period](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3)

counter\_api\_set\_guard\_period set\_guard\_period

**Definition** counter.h:245

[counter\_driver\_api::start](structcounter__driver__api.md#aa8fd91ec6e2357ece10c9e8ea37f9336)

counter\_api\_start start

**Definition** counter.h:235

[counter\_driver\_api::get\_guard\_period](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4)

counter\_api\_get\_guard\_period get\_guard\_period

**Definition** counter.h:244

[counter\_driver\_api::cancel\_alarm](structcounter__driver__api.md#af002080c967fa3a2e2eaadd0b4ee35ae)

counter\_api\_cancel\_alarm cancel\_alarm

**Definition** counter.h:240

[counter\_driver\_api::get\_freq](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df)

counter\_api\_get\_freq get\_freq

**Definition** counter.h:246

[counter\_top\_cfg](structcounter__top__cfg.md)

Top value configuration structure.

**Definition** counter.h:170

[counter\_top\_cfg::ticks](structcounter__top__cfg.md#abb60a9d468fa6d6802ba56a02a515751)

uint32\_t ticks

Top value.

**Definition** counter.h:174

[counter\_top\_cfg::flags](structcounter__top__cfg.md#ad5caa9f1c80badf14c2c313e60e3e8e6)

uint32\_t flags

Flags (see COUNTER\_TOP\_FLAGS).

**Definition** counter.h:186

[counter\_top\_cfg::callback](structcounter__top__cfg.md#adf1cf3a9c67278f5f5f1cba72f6dd934)

counter\_top\_callback\_t callback

Callback function (can be NULL).

**Definition** counter.h:178

[counter\_top\_cfg::user\_data](structcounter__top__cfg.md#af033941769c710e82cf9dd9f12ff011c)

void \* user\_data

User data passed to callback function (not valid if callback is NULL).

**Definition** counter.h:182

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

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [counter.h](drivers_2counter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
