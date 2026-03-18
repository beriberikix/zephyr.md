---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/counter_8h_source.html
original_path: doxygen/html/counter_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter.h

[Go to the documentation of this file.](counter_8h.md)

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

22

23#include <[errno.h](errno_8h.md)>

24

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <stddef.h>

27#include <[zephyr/device.h](device_8h.md)>

28#include <[zephyr/sys\_clock.h](include_2zephyr_2sys__clock_8h.md)>

29#include <[stdbool.h](stdbool_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

40

[ 44](group__counter__interface.md#ga8fa40ff6404936e5b05bb9c67871f70c)#define COUNTER\_CONFIG\_INFO\_COUNT\_UP BIT(0)

45

47

53

[ 60](group__counter__interface.md#ga9a30c647361912c2ce8e0566cf53dea7)#define COUNTER\_TOP\_CFG\_DONT\_RESET BIT(0)

61

[ 68](group__counter__interface.md#ga45562a4ddd743f74213a03d83a774b11)#define COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE BIT(1)

69

71

78

[ 85](group__counter__interface.md#ga4842d212424f92c5a3b39116ec6c2fd2)#define COUNTER\_ALARM\_CFG\_ABSOLUTE BIT(0)

86

[ 93](group__counter__interface.md#ga87dffd2a1cadedfc30e7d39af547c336)#define COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE BIT(1)

94

96

104

[ 109](group__counter__interface.md#ga6d955e603067b5c50e0fd9761e2e611d)#define COUNTER\_GUARD\_PERIOD\_LATE\_TO\_SET BIT(0)

110

112

[ 120](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77)typedef void (\*[counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77))(const struct [device](structdevice.md) \*dev,

121 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks,

122 void \*user\_data);

123

[ 126](structcounter__alarm__cfg.md)struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) {

[ 130](structcounter__alarm__cfg.md#aeef670ee73dd4d7d65e02a66313b092d) [counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77) [callback](structcounter__alarm__cfg.md#aeef670ee73dd4d7d65e02a66313b092d);

[ 147](structcounter__alarm__cfg.md#a85b6b86d7a82f2e238000dd31ff1f779) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ticks](structcounter__alarm__cfg.md#a85b6b86d7a82f2e238000dd31ff1f779);

[ 151](structcounter__alarm__cfg.md#aeaf2bd9042a28b626e0972aff4ad09e5) void \*[user\_data](structcounter__alarm__cfg.md#aeaf2bd9042a28b626e0972aff4ad09e5);

[ 155](structcounter__alarm__cfg.md#ab043cd1ea9be54449bb75c4a5affe620) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structcounter__alarm__cfg.md#ab043cd1ea9be54449bb75c4a5affe620);

156};

157

[ 163](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf)typedef void (\*[counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf))(const struct [device](structdevice.md) \*dev,

164 void \*user\_data);

165

[ 168](structcounter__top__cfg.md)struct [counter\_top\_cfg](structcounter__top__cfg.md) {

[ 172](structcounter__top__cfg.md#abb60a9d468fa6d6802ba56a02a515751) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ticks](structcounter__top__cfg.md#abb60a9d468fa6d6802ba56a02a515751);

[ 176](structcounter__top__cfg.md#adf1cf3a9c67278f5f5f1cba72f6dd934) [counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf) [callback](structcounter__top__cfg.md#adf1cf3a9c67278f5f5f1cba72f6dd934);

[ 180](structcounter__top__cfg.md#af033941769c710e82cf9dd9f12ff011c) void \*[user\_data](structcounter__top__cfg.md#af033941769c710e82cf9dd9f12ff011c);

[ 184](structcounter__top__cfg.md#ad5caa9f1c80badf14c2c313e60e3e8e6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structcounter__top__cfg.md#ad5caa9f1c80badf14c2c313e60e3e8e6);

185};

186

[ 189](structcounter__config__info.md)struct [counter\_config\_info](structcounter__config__info.md) {

[ 193](structcounter__config__info.md#a0465be87680d1a50e1ae7a68c61caaac) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_top\_value](structcounter__config__info.md#a0465be87680d1a50e1ae7a68c61caaac);

[ 197](structcounter__config__info.md#a4cae02b246a92e5d207d5b654d059322) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [freq](structcounter__config__info.md#a4cae02b246a92e5d207d5b654d059322);

[ 201](structcounter__config__info.md#ab38d95647388c700de372882db372d6c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structcounter__config__info.md#ab38d95647388c700de372882db372d6c);

[ 207](structcounter__config__info.md#afe2281d1909fa85978077558d6f4b71f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channels](structcounter__config__info.md#afe2281d1909fa85978077558d6f4b71f);

208};

209

[ 210](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81)typedef int (\*[counter\_api\_start](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81))(const struct [device](structdevice.md) \*dev);

[ 211](group__counter__interface.md#ga25ac7589f6501dada1e10b1980fca7de)typedef int (\*[counter\_api\_stop](group__counter__interface.md#ga25ac7589f6501dada1e10b1980fca7de))(const struct [device](structdevice.md) \*dev);

[ 212](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f)typedef int (\*[counter\_api\_get\_value](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f))(const struct [device](structdevice.md) \*dev,

213 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks);

[ 214](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e)typedef int (\*[counter\_api\_get\_value\_64](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e))(const struct [device](structdevice.md) \*dev,

215 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks);

[ 216](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387)typedef int (\*[counter\_api\_set\_alarm](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387))(const struct [device](structdevice.md) \*dev,

217 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id,

218 const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg);

[ 219](group__counter__interface.md#gac368afac6de0fe1f782fdb90e6f7c266)typedef int (\*[counter\_api\_cancel\_alarm](group__counter__interface.md#gac368afac6de0fe1f782fdb90e6f7c266))(const struct [device](structdevice.md) \*dev,

220 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id);

[ 221](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8)typedef int (\*[counter\_api\_set\_top\_value](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8))(const struct [device](structdevice.md) \*dev,

222 const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg);

[ 223](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[counter\_api\_get\_pending\_int](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba))(const struct [device](structdevice.md) \*dev);

[ 224](group__counter__interface.md#ga08ca9b32fbc96da83b75844f7b6218b2)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[counter\_api\_get\_top\_value](group__counter__interface.md#ga08ca9b32fbc96da83b75844f7b6218b2))(const struct [device](structdevice.md) \*dev);

[ 225](group__counter__interface.md#ga90b573190980a935d3984029831739a9)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[counter\_api\_get\_guard\_period](group__counter__interface.md#ga90b573190980a935d3984029831739a9))(const struct [device](structdevice.md) \*dev,

226 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 227](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d)typedef int (\*[counter\_api\_set\_guard\_period](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d))(const struct [device](structdevice.md) \*dev,

228 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks,

229 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 230](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[counter\_api\_get\_freq](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024))(const struct [device](structdevice.md) \*dev);

231

[ 232](structcounter__driver__api.md)\_\_subsystem struct [counter\_driver\_api](structcounter__driver__api.md) {

[ 233](structcounter__driver__api.md#aa8fd91ec6e2357ece10c9e8ea37f9336) [counter\_api\_start](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81) [start](structcounter__driver__api.md#aa8fd91ec6e2357ece10c9e8ea37f9336);

[ 234](structcounter__driver__api.md#a9d1b590187c0eccd11f8c7c80da967ce) [counter\_api\_stop](group__counter__interface.md#ga25ac7589f6501dada1e10b1980fca7de) [stop](structcounter__driver__api.md#a9d1b590187c0eccd11f8c7c80da967ce);

[ 235](structcounter__driver__api.md#a7d7b07f9d6e63ef931d81ad52076b2e1) [counter\_api\_get\_value](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f) [get\_value](structcounter__driver__api.md#a7d7b07f9d6e63ef931d81ad52076b2e1);

[ 236](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1) [counter\_api\_get\_value\_64](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e) [get\_value\_64](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1);

[ 237](structcounter__driver__api.md#a67a3939d4c25b49abdf6f34929ed00a0) [counter\_api\_set\_alarm](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387) [set\_alarm](structcounter__driver__api.md#a67a3939d4c25b49abdf6f34929ed00a0);

[ 238](structcounter__driver__api.md#af002080c967fa3a2e2eaadd0b4ee35ae) [counter\_api\_cancel\_alarm](group__counter__interface.md#gac368afac6de0fe1f782fdb90e6f7c266) [cancel\_alarm](structcounter__driver__api.md#af002080c967fa3a2e2eaadd0b4ee35ae);

[ 239](structcounter__driver__api.md#a5479ccee1057fecacddfbbf49edc0537) [counter\_api\_set\_top\_value](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8) [set\_top\_value](structcounter__driver__api.md#a5479ccee1057fecacddfbbf49edc0537);

[ 240](structcounter__driver__api.md#a8daec24721653215df3b36afc7c21168) [counter\_api\_get\_pending\_int](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba) [get\_pending\_int](structcounter__driver__api.md#a8daec24721653215df3b36afc7c21168);

[ 241](structcounter__driver__api.md#a3571f7310b7aed43df6e620f93aa1521) [counter\_api\_get\_top\_value](group__counter__interface.md#ga08ca9b32fbc96da83b75844f7b6218b2) [get\_top\_value](structcounter__driver__api.md#a3571f7310b7aed43df6e620f93aa1521);

[ 242](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4) [counter\_api\_get\_guard\_period](group__counter__interface.md#ga90b573190980a935d3984029831739a9) [get\_guard\_period](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4);

[ 243](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3) [counter\_api\_set\_guard\_period](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d) [set\_guard\_period](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3);

[ 244](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df) [counter\_api\_get\_freq](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024) [get\_freq](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df);

245};

246

[ 255](group__counter__interface.md#gab95ae0e8d89e35e477cbf7d67e18016d)\_\_syscall bool [counter\_is\_counting\_up](group__counter__interface.md#gab95ae0e8d89e35e477cbf7d67e18016d)(const struct [device](structdevice.md) \*dev);

256

257static inline bool z\_impl\_counter\_is\_counting\_up(const struct [device](structdevice.md) \*dev)

258{

259 const struct [counter\_config\_info](structcounter__config__info.md) \*config =

260 (const struct [counter\_config\_info](structcounter__config__info.md) \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

261

262 return config->flags & [COUNTER\_CONFIG\_INFO\_COUNT\_UP](group__counter__interface.md#ga8fa40ff6404936e5b05bb9c67871f70c);

263}

264

[ 272](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)\_\_syscall [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [counter\_get\_num\_of\_channels](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)(const struct [device](structdevice.md) \*dev);

273

274static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) z\_impl\_counter\_get\_num\_of\_channels(const struct [device](structdevice.md) \*dev)

275{

276 const struct [counter\_config\_info](structcounter__config__info.md) \*config =

277 (const struct [counter\_config\_info](structcounter__config__info.md) \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

278

279 return config->channels;

280}

281

[ 290](group__counter__interface.md#ga8d3d6f856eef27a80cc2697931341af2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_get\_frequency](group__counter__interface.md#ga8d3d6f856eef27a80cc2697931341af2)(const struct [device](structdevice.md) \*dev);

291

292static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_get\_frequency(const struct [device](structdevice.md) \*dev)

293{

294 const struct [counter\_config\_info](structcounter__config__info.md) \*config =

295 (const struct [counter\_config\_info](structcounter__config__info.md) \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

296 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

297 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->api;

298

299 return api->[get\_freq](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df) ? api->[get\_freq](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df)(dev) : config->freq;

300}

301

[ 310](group__counter__interface.md#gab73238b8d52ed763ff7abf91013b601b)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_us\_to\_ticks](group__counter__interface.md#gab73238b8d52ed763ff7abf91013b601b)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) us);

311

312static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_us\_to\_ticks(const struct [device](structdevice.md) \*dev,

313 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) us)

314{

315 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ticks = (us \* z\_impl\_counter\_get\_frequency(dev)) / [USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1);

316

317 return (ticks > ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))[UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)) ? [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd) : ticks;

318}

319

[ 328](group__counter__interface.md#ga9fbcb710091084e638c45f62c25d954c)\_\_syscall [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [counter\_ticks\_to\_us](group__counter__interface.md#ga9fbcb710091084e638c45f62c25d954c)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks);

329

330static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_impl\_counter\_ticks\_to\_us(const struct [device](structdevice.md) \*dev,

331 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks)

332{

333 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))ticks \* [USEC\_PER\_SEC](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)) / z\_impl\_counter\_get\_frequency(dev);

334}

335

[ 343](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_get\_max\_top\_value](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3)(const struct [device](structdevice.md) \*dev);

344

345static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_get\_max\_top\_value(const struct [device](structdevice.md) \*dev)

346{

347 const struct [counter\_config\_info](structcounter__config__info.md) \*config =

348 (const struct [counter\_config\_info](structcounter__config__info.md) \*)dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

349

350 return config->max\_top\_value;

351}

352

[ 361](group__counter__interface.md#ga103e0673e31475adcd173601058c72cd)\_\_syscall int [counter\_start](group__counter__interface.md#ga103e0673e31475adcd173601058c72cd)(const struct [device](structdevice.md) \*dev);

362

363static inline int z\_impl\_counter\_start(const struct [device](structdevice.md) \*dev)

364{

365 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

366 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

367

368 return api->[start](structcounter__driver__api.md#aa8fd91ec6e2357ece10c9e8ea37f9336)(dev);

369}

370

[ 380](group__counter__interface.md#gafaa8198ccff5ffc0491a1424d090c82d)\_\_syscall int [counter\_stop](group__counter__interface.md#gafaa8198ccff5ffc0491a1424d090c82d)(const struct [device](structdevice.md) \*dev);

381

382static inline int z\_impl\_counter\_stop(const struct [device](structdevice.md) \*dev)

383{

384 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

385 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

386

387 return api->[stop](structcounter__driver__api.md#a9d1b590187c0eccd11f8c7c80da967ce)(dev);

388}

389

[ 398](group__counter__interface.md#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d)\_\_syscall int [counter\_get\_value](group__counter__interface.md#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks);

399

400static inline int z\_impl\_counter\_get\_value(const struct [device](structdevice.md) \*dev,

401 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ticks)

402{

403 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

404 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

405

406 return api->[get\_value](structcounter__driver__api.md#a7d7b07f9d6e63ef931d81ad52076b2e1)(dev, ticks);

407}

408

[ 417](group__counter__interface.md#ga2dcd0eb10d49c4e5e5024ed75a8e3e86)\_\_syscall int [counter\_get\_value\_64](group__counter__interface.md#ga2dcd0eb10d49c4e5e5024ed75a8e3e86)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks);

418

419static inline int z\_impl\_counter\_get\_value\_64(const struct [device](structdevice.md) \*dev,

420 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ticks)

421{

422 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

423 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

424

425 if (!api->[get\_value\_64](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1)) {

426 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

427 }

428

429 return api->[get\_value\_64](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1)(dev, ticks);

430}

431

[ 452](group__counter__interface.md#ga00a2857d993a84a56e8e222727f3d85e)\_\_syscall int [counter\_set\_channel\_alarm](group__counter__interface.md#ga00a2857d993a84a56e8e222727f3d85e)(const struct [device](structdevice.md) \*dev,

453 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id,

454 const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg);

455

456static inline int z\_impl\_counter\_set\_channel\_alarm(const struct [device](structdevice.md) \*dev,

457 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id,

458 const struct [counter\_alarm\_cfg](structcounter__alarm__cfg.md) \*alarm\_cfg)

459{

460 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

461 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

462

463 if (chan\_id >= [counter\_get\_num\_of\_channels](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)(dev)) {

464 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

465 }

466

467 return api->[set\_alarm](structcounter__driver__api.md#a67a3939d4c25b49abdf6f34929ed00a0)(dev, chan\_id, alarm\_cfg);

468}

469

[ 482](group__counter__interface.md#gade0bb97c0dfa03676d11ee47601d4cee)\_\_syscall int [counter\_cancel\_channel\_alarm](group__counter__interface.md#gade0bb97c0dfa03676d11ee47601d4cee)(const struct [device](structdevice.md) \*dev,

483 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id);

484

485static inline int z\_impl\_counter\_cancel\_channel\_alarm(const struct [device](structdevice.md) \*dev,

486 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_id)

487{

488 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

489 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

490

491 if (chan\_id >= [counter\_get\_num\_of\_channels](group__counter__interface.md#ga0c9801b13275de0e1b93650bb1ca6a9d)(dev)) {

492 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

493 }

494

495 return api->[cancel\_alarm](structcounter__driver__api.md#af002080c967fa3a2e2eaadd0b4ee35ae)(dev, chan\_id);

496}

497

[ 522](group__counter__interface.md#ga2d92f5564cdd1ecc56029c3a45e666f0)\_\_syscall int [counter\_set\_top\_value](group__counter__interface.md#ga2d92f5564cdd1ecc56029c3a45e666f0)(const struct [device](structdevice.md) \*dev,

523 const struct [counter\_top\_cfg](structcounter__top__cfg.md) \*cfg);

524

525static inline int z\_impl\_counter\_set\_top\_value(const struct [device](structdevice.md) \*dev,

526 const struct [counter\_top\_cfg](structcounter__top__cfg.md)

527 \*cfg)

528{

529 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

530 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

531

532 if (cfg->ticks > [counter\_get\_max\_top\_value](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3)(dev)) {

533 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

534 }

535

536 return api->[set\_top\_value](structcounter__driver__api.md#a5479ccee1057fecacddfbbf49edc0537)(dev, cfg);

537}

538

[ 552](group__counter__interface.md#ga3b74a79a09cbe3849658a746e7417a06)\_\_syscall int [counter\_get\_pending\_int](group__counter__interface.md#ga3b74a79a09cbe3849658a746e7417a06)(const struct [device](structdevice.md) \*dev);

553

554static inline int z\_impl\_counter\_get\_pending\_int(const struct [device](structdevice.md) \*dev)

555{

556 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

557 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

558

559 return api->[get\_pending\_int](structcounter__driver__api.md#a8daec24721653215df3b36afc7c21168)(dev);

560}

561

[ 569](group__counter__interface.md#ga13d14903a03ab10062002a81b8302424)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_get\_top\_value](group__counter__interface.md#ga13d14903a03ab10062002a81b8302424)(const struct [device](structdevice.md) \*dev);

570

571static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_get\_top\_value(const struct [device](structdevice.md) \*dev)

572{

573 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

574 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

575

576 return api->[get\_top\_value](structcounter__driver__api.md#a3571f7310b7aed43df6e620f93aa1521)(dev);

577}

578

[ 631](group__counter__interface.md#gab6851411dabf191d3391715d632111b0)\_\_syscall int [counter\_set\_guard\_period](group__counter__interface.md#gab6851411dabf191d3391715d632111b0)(const struct [device](structdevice.md) \*dev,

632 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks,

633 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

634

635static inline int z\_impl\_counter\_set\_guard\_period(const struct [device](structdevice.md) \*dev,

636 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

637{

638 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

639 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

640

641 if (!api->[set\_guard\_period](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3)) {

642 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

643 }

644

645 return api->[set\_guard\_period](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3)(dev, ticks, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

646}

647

[ 659](group__counter__interface.md#ga55a101d237c8472ad5cacf65363c536f)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [counter\_get\_guard\_period](group__counter__interface.md#ga55a101d237c8472ad5cacf65363c536f)(const struct [device](structdevice.md) \*dev,

660 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

661

662static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_counter\_get\_guard\_period(const struct [device](structdevice.md) \*dev,

663 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

664{

665 const struct [counter\_driver\_api](structcounter__driver__api.md) \*api =

666 (struct [counter\_driver\_api](structcounter__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

667

668 return (api->[get\_guard\_period](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4)) ? api->[get\_guard\_period](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4)(dev, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) : 0;

669}

670

671#ifdef \_\_cplusplus

672}

673#endif

674

678

679#include <syscalls/counter.h>

680

681#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_COUNTER\_H\_ \*/

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

**Definition** counter.h:224

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

**Definition** counter.h:211

[counter\_set\_top\_value](group__counter__interface.md#ga2d92f5564cdd1ecc56029c3a45e666f0)

int counter\_set\_top\_value(const struct device \*dev, const struct counter\_top\_cfg \*cfg)

Set counter top value.

[counter\_get\_value\_64](group__counter__interface.md#ga2dcd0eb10d49c4e5e5024ed75a8e3e86)

int counter\_get\_value\_64(const struct device \*dev, uint64\_t \*ticks)

Get current counter 64-bit value.

[counter\_top\_callback\_t](group__counter__interface.md#ga3686fe1f86a53469659f79897e4e1baf)

void(\* counter\_top\_callback\_t)(const struct device \*dev, void \*user\_data)

Callback called when counter turns around.

**Definition** counter.h:163

[counter\_alarm\_callback\_t](group__counter__interface.md#ga36c570c3e57e635753d163400e437b77)

void(\* counter\_alarm\_callback\_t)(const struct device \*dev, uint8\_t chan\_id, uint32\_t ticks, void \*user\_data)

Alarm callback.

**Definition** counter.h:120

[counter\_get\_pending\_int](group__counter__interface.md#ga3b74a79a09cbe3849658a746e7417a06)

int counter\_get\_pending\_int(const struct device \*dev)

Function to get pending interrupts.

[counter\_get\_guard\_period](group__counter__interface.md#ga55a101d237c8472ad5cacf65363c536f)

uint32\_t counter\_get\_guard\_period(const struct device \*dev, uint32\_t flags)

Return guard period.

[counter\_api\_set\_guard\_period](group__counter__interface.md#ga89822ff9da840421bbd59ab13664245d)

int(\* counter\_api\_set\_guard\_period)(const struct device \*dev, uint32\_t ticks, uint32\_t flags)

**Definition** counter.h:227

[counter\_get\_frequency](group__counter__interface.md#ga8d3d6f856eef27a80cc2697931341af2)

uint32\_t counter\_get\_frequency(const struct device \*dev)

Function to get counter frequency.

[counter\_get\_value](group__counter__interface.md#ga8f6b1b4ee7dc20e6230a22bfcb0e6f9d)

int counter\_get\_value(const struct device \*dev, uint32\_t \*ticks)

Get current counter value.

[COUNTER\_CONFIG\_INFO\_COUNT\_UP](group__counter__interface.md#ga8fa40ff6404936e5b05bb9c67871f70c)

#define COUNTER\_CONFIG\_INFO\_COUNT\_UP

Counter count up flag.

**Definition** counter.h:44

[counter\_api\_get\_guard\_period](group__counter__interface.md#ga90b573190980a935d3984029831739a9)

uint32\_t(\* counter\_api\_get\_guard\_period)(const struct device \*dev, uint32\_t flags)

**Definition** counter.h:225

[counter\_api\_get\_pending\_int](group__counter__interface.md#ga9224eba6be975e0747b4e13479b103ba)

uint32\_t(\* counter\_api\_get\_pending\_int)(const struct device \*dev)

**Definition** counter.h:223

[counter\_api\_get\_freq](group__counter__interface.md#ga939a7b305379577b3e10b315b89a4024)

uint32\_t(\* counter\_api\_get\_freq)(const struct device \*dev)

**Definition** counter.h:230

[counter\_ticks\_to\_us](group__counter__interface.md#ga9fbcb710091084e638c45f62c25d954c)

uint64\_t counter\_ticks\_to\_us(const struct device \*dev, uint32\_t ticks)

Function to convert ticks to microseconds.

[counter\_api\_set\_top\_value](group__counter__interface.md#gaa41eff3e6546583cc526830f9419aea8)

int(\* counter\_api\_set\_top\_value)(const struct device \*dev, const struct counter\_top\_cfg \*cfg)

**Definition** counter.h:221

[counter\_api\_start](group__counter__interface.md#gab06ed037f6b0fb78ce04b7e7da989e81)

int(\* counter\_api\_start)(const struct device \*dev)

**Definition** counter.h:210

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

**Definition** counter.h:219

[counter\_api\_get\_value\_64](group__counter__interface.md#gac7a403978e24becda59727790ba3ee8e)

int(\* counter\_api\_get\_value\_64)(const struct device \*dev, uint64\_t \*ticks)

**Definition** counter.h:214

[counter\_api\_get\_value](group__counter__interface.md#gac7a80581c4bda7dc76baeb6f6949ae5f)

int(\* counter\_api\_get\_value)(const struct device \*dev, uint32\_t \*ticks)

**Definition** counter.h:212

[counter\_cancel\_channel\_alarm](group__counter__interface.md#gade0bb97c0dfa03676d11ee47601d4cee)

int counter\_cancel\_channel\_alarm(const struct device \*dev, uint8\_t chan\_id)

Cancel an alarm on a channel.

[counter\_api\_set\_alarm](group__counter__interface.md#gae3821860fa8a5c1197d6e304d2a4f387)

int(\* counter\_api\_set\_alarm)(const struct device \*dev, uint8\_t chan\_id, const struct counter\_alarm\_cfg \*alarm\_cfg)

**Definition** counter.h:216

[counter\_stop](group__counter__interface.md#gafaa8198ccff5ffc0491a1424d090c82d)

int counter\_stop(const struct device \*dev)

Stop counter device.

[counter\_get\_max\_top\_value](group__counter__interface.md#gafab2a55048349e33c821a7f826615ea3)

uint32\_t counter\_get\_max\_top\_value(const struct device \*dev)

Function to retrieve maximum top value that can be set.

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[sys\_clock.h](include_2zephyr_2sys__clock_8h.md)

Variables needed for system clock.

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

**Definition** counter.h:126

[counter\_alarm\_cfg::ticks](structcounter__alarm__cfg.md#a85b6b86d7a82f2e238000dd31ff1f779)

uint32\_t ticks

Number of ticks that triggers the alarm.

**Definition** counter.h:147

[counter\_alarm\_cfg::flags](structcounter__alarm__cfg.md#ab043cd1ea9be54449bb75c4a5affe620)

uint32\_t flags

Alarm flags (see COUNTER\_ALARM\_FLAGS).

**Definition** counter.h:155

[counter\_alarm\_cfg::user\_data](structcounter__alarm__cfg.md#aeaf2bd9042a28b626e0972aff4ad09e5)

void \* user\_data

User data returned in callback.

**Definition** counter.h:151

[counter\_alarm\_cfg::callback](structcounter__alarm__cfg.md#aeef670ee73dd4d7d65e02a66313b092d)

counter\_alarm\_callback\_t callback

Callback called on alarm (cannot be NULL).

**Definition** counter.h:130

[counter\_config\_info](structcounter__config__info.md)

Structure with generic counter features.

**Definition** counter.h:189

[counter\_config\_info::max\_top\_value](structcounter__config__info.md#a0465be87680d1a50e1ae7a68c61caaac)

uint32\_t max\_top\_value

Maximal (default) top value on which counter is reset (cleared or reloaded).

**Definition** counter.h:193

[counter\_config\_info::freq](structcounter__config__info.md#a4cae02b246a92e5d207d5b654d059322)

uint32\_t freq

Frequency of the source clock if synchronous events are counted.

**Definition** counter.h:197

[counter\_config\_info::flags](structcounter__config__info.md#ab38d95647388c700de372882db372d6c)

uint8\_t flags

Flags (see COUNTER\_FLAGS).

**Definition** counter.h:201

[counter\_config\_info::channels](structcounter__config__info.md#afe2281d1909fa85978077558d6f4b71f)

uint8\_t channels

Number of channels that can be used for setting alarm.

**Definition** counter.h:207

[counter\_driver\_api](structcounter__driver__api.md)

**Definition** counter.h:232

[counter\_driver\_api::get\_value\_64](structcounter__driver__api.md#a133ea6233304d2360eac9b656a1bc8b1)

counter\_api\_get\_value\_64 get\_value\_64

**Definition** counter.h:236

[counter\_driver\_api::get\_top\_value](structcounter__driver__api.md#a3571f7310b7aed43df6e620f93aa1521)

counter\_api\_get\_top\_value get\_top\_value

**Definition** counter.h:241

[counter\_driver\_api::set\_top\_value](structcounter__driver__api.md#a5479ccee1057fecacddfbbf49edc0537)

counter\_api\_set\_top\_value set\_top\_value

**Definition** counter.h:239

[counter\_driver\_api::set\_alarm](structcounter__driver__api.md#a67a3939d4c25b49abdf6f34929ed00a0)

counter\_api\_set\_alarm set\_alarm

**Definition** counter.h:237

[counter\_driver\_api::get\_value](structcounter__driver__api.md#a7d7b07f9d6e63ef931d81ad52076b2e1)

counter\_api\_get\_value get\_value

**Definition** counter.h:235

[counter\_driver\_api::get\_pending\_int](structcounter__driver__api.md#a8daec24721653215df3b36afc7c21168)

counter\_api\_get\_pending\_int get\_pending\_int

**Definition** counter.h:240

[counter\_driver\_api::stop](structcounter__driver__api.md#a9d1b590187c0eccd11f8c7c80da967ce)

counter\_api\_stop stop

**Definition** counter.h:234

[counter\_driver\_api::set\_guard\_period](structcounter__driver__api.md#aa116448b2309da016184c9222ad6c1f3)

counter\_api\_set\_guard\_period set\_guard\_period

**Definition** counter.h:243

[counter\_driver\_api::start](structcounter__driver__api.md#aa8fd91ec6e2357ece10c9e8ea37f9336)

counter\_api\_start start

**Definition** counter.h:233

[counter\_driver\_api::get\_guard\_period](structcounter__driver__api.md#aee77697602a0464dee87287fa08845a4)

counter\_api\_get\_guard\_period get\_guard\_period

**Definition** counter.h:242

[counter\_driver\_api::cancel\_alarm](structcounter__driver__api.md#af002080c967fa3a2e2eaadd0b4ee35ae)

counter\_api\_cancel\_alarm cancel\_alarm

**Definition** counter.h:238

[counter\_driver\_api::get\_freq](structcounter__driver__api.md#af9bfa4cdf0073c1699d6b613e3e9a8df)

counter\_api\_get\_freq get\_freq

**Definition** counter.h:244

[counter\_top\_cfg](structcounter__top__cfg.md)

Top value configuration structure.

**Definition** counter.h:168

[counter\_top\_cfg::ticks](structcounter__top__cfg.md#abb60a9d468fa6d6802ba56a02a515751)

uint32\_t ticks

Top value.

**Definition** counter.h:172

[counter\_top\_cfg::flags](structcounter__top__cfg.md#ad5caa9f1c80badf14c2c313e60e3e8e6)

uint32\_t flags

Flags (see COUNTER\_TOP\_FLAGS).

**Definition** counter.h:184

[counter\_top\_cfg::callback](structcounter__top__cfg.md#adf1cf3a9c67278f5f5f1cba72f6dd934)

counter\_top\_callback\_t callback

Callback function (can be NULL).

**Definition** counter.h:176

[counter\_top\_cfg::user\_data](structcounter__top__cfg.md#af033941769c710e82cf9dd9f12ff011c)

void \* user\_data

User data passed to callback function (not valid if callback is NULL).

**Definition** counter.h:180

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [counter.h](counter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
