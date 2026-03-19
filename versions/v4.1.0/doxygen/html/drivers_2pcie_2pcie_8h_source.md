---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2pcie_2pcie_8h_source.html
original_path: doxygen/html/drivers_2pcie_2pcie_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie.h

[Go to the documentation of this file.](drivers_2pcie_2pcie_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_PCIE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_PCIE\_H\_

9

16

17#include <stddef.h>

18#include <[zephyr/devicetree.h](devicetree_8h.md)>

19#include <[zephyr/dt-bindings/pcie/pcie.h](dt-bindings_2pcie_2pcie_8h.md)>

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21#include <[zephyr/kernel.h](kernel_8h.md)>

22#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 37](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb);

38

[ 47](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04);

48

49/\* Helper macro to exclude invalid PCIe identifiers. We should really only

50 \* need to look for PCIE\_ID\_NONE, but because of some broken PCI host controllers

51 \* we have try cases where both VID & DID are zero or just one of them is

52 \* zero (0x0000) and the other is all ones (0xFFFF).

53 \*/

[ 54](group__pcie__host__interface.md#gac7d5c41ea3c8999126d89d95961b430b)#define PCIE\_ID\_IS\_VALID(id) ((id != PCIE\_ID\_NONE) && \

55 (id != PCIE\_ID(0x0000, 0x0000)) && \

56 (id != PCIE\_ID(0xFFFF, 0x0000)) && \

57 (id != PCIE\_ID(0x0000, 0xFFFF)))

58

[ 59](structpcie__dev.md)struct [pcie\_dev](structpcie__dev.md) {

[ 60](structpcie__dev.md#a7cc2f61e85b1d9c4985115b91fc6e832) [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) [bdf](structpcie__dev.md#a7cc2f61e85b1d9c4985115b91fc6e832);

[ 61](structpcie__dev.md#a5709ef678d9e81d4d3a61f6c26371076) [pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04) [id](structpcie__dev.md#a5709ef678d9e81d4d3a61f6c26371076);

[ 62](structpcie__dev.md#abedf281cdce4961dd02abba849747f45) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [class\_rev](structpcie__dev.md#abedf281cdce4961dd02abba849747f45);

[ 63](structpcie__dev.md#a798e25696997a74ed01f8df6cec64489) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [class\_rev\_mask](structpcie__dev.md#a798e25696997a74ed01f8df6cec64489);

64};

65

66#define Z\_DEVICE\_PCIE\_NAME(node\_id) \_CONCAT(pcie\_dev\_, DT\_DEP\_ORD(node\_id))

67

[ 74](group__pcie__host__interface.md#ga304228150cd8ec56aa24be468e9d79bf)#define PCIE\_DT\_ID(node\_id) PCIE\_ID(DT\_PROP\_OR(node\_id, vendor\_id, 0xffff), \

75 DT\_PROP\_OR(node\_id, device\_id, 0xffff))

76

[ 86](group__pcie__host__interface.md#ga3e89194346fa9b945f1873380c527cee)#define PCIE\_DT\_INST\_ID(inst) PCIE\_DT\_ID(DT\_DRV\_INST(inst))

87

[ 96](group__pcie__host__interface.md#gad0b870d891458c4ebd7ab2ac1c372eec)#define DEVICE\_PCIE\_DECLARE(node\_id) \

97 STRUCT\_SECTION\_ITERABLE(pcie\_dev, Z\_DEVICE\_PCIE\_NAME(node\_id)) = { \

98 .bdf = PCIE\_BDF\_NONE, \

99 .id = PCIE\_DT\_ID(node\_id), \

100 .class\_rev = DT\_PROP\_OR(node\_id, class\_rev, 0), \

101 .class\_rev\_mask = DT\_PROP\_OR(node\_id, class\_rev\_mask, 0), \

102 }

103

[ 112](group__pcie__host__interface.md#gade2f1f53701b1d80b5593045e977e4d6)#define DEVICE\_PCIE\_INST\_DECLARE(inst) DEVICE\_PCIE\_DECLARE(DT\_DRV\_INST(inst))

113

[ 138](group__pcie__host__interface.md#gab6c472838e13293980cd53c65aaa3c47)#define DEVICE\_PCIE\_INIT(node\_id, name) .name = &Z\_DEVICE\_PCIE\_NAME(node\_id)

139

[ 149](group__pcie__host__interface.md#gac175df702e85f599b28b7a567c64d146)#define DEVICE\_PCIE\_INST\_INIT(inst, name) \

150 DEVICE\_PCIE\_INIT(DT\_DRV\_INST(inst), name)

151

[ 152](structpcie__bar.md)struct [pcie\_bar](structpcie__bar.md) {

[ 153](structpcie__bar.md#a75ed340a7d80a6825f3c60469194dae8) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [phys\_addr](structpcie__bar.md#a75ed340a7d80a6825f3c60469194dae8);

[ 154](structpcie__bar.md#ab68c921f2993c94d2ae65684568bf770) size\_t [size](structpcie__bar.md#ab68c921f2993c94d2ae65684568bf770);

155};

156

157/\*

158 \* These functions are arch-, board-, or SoC-specific.

159 \*/

160

[ 170](group__pcie__host__interface.md#ga10ecc667c564548e4ddf3ca4374242b5)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_conf\_read](group__pcie__host__interface.md#ga10ecc667c564548e4ddf3ca4374242b5)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, unsigned int reg);

171

[ 181](group__pcie__host__interface.md#ga47a2e88935e04330d449db5463d9f21a)extern void [pcie\_conf\_write](group__pcie__host__interface.md#ga47a2e88935e04330d449db5463d9f21a)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, unsigned int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

182

[ 191](group__pcie__host__interface.md#ga922580e4fb6200ef75425bb54801ceda)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[pcie\_scan\_cb\_t](group__pcie__host__interface.md#ga922580e4fb6200ef75425bb54801ceda))([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04) id, void \*cb\_data);

192

193enum {

[ 195](group__pcie__host__interface.md#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4) [PCIE\_SCAN\_RECURSIVE](group__pcie__host__interface.md#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 197](group__pcie__host__interface.md#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072) [PCIE\_SCAN\_CB\_ALL](group__pcie__host__interface.md#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

198};

199

[ 201](structpcie__scan__opt.md)struct [pcie\_scan\_opt](structpcie__scan__opt.md) {

[ 203](structpcie__scan__opt.md#a036225c7a5730ba2040e03cab491b9da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bus](structpcie__scan__opt.md#a036225c7a5730ba2040e03cab491b9da);

204

[ 206](structpcie__scan__opt.md#a28ad6c4993eed7bdf08ce682692bf306) [pcie\_scan\_cb\_t](group__pcie__host__interface.md#ga922580e4fb6200ef75425bb54801ceda) [cb](structpcie__scan__opt.md#a28ad6c4993eed7bdf08ce682692bf306);

207

[ 209](structpcie__scan__opt.md#a11b39138d2a2b6b1e8e1bd80216a8da6) void \*[cb\_data](structpcie__scan__opt.md#a11b39138d2a2b6b1e8e1bd80216a8da6);

210

[ 212](structpcie__scan__opt.md#a7e485fb824dea16f9d5fdcb7079ebb7e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structpcie__scan__opt.md#a7e485fb824dea16f9d5fdcb7079ebb7e);

213};

214

[ 222](group__pcie__host__interface.md#ga9a7b3c202f91d37fe8445d5016f4c6ab)int [pcie\_scan](group__pcie__host__interface.md#ga9a7b3c202f91d37fe8445d5016f4c6ab)(const struct [pcie\_scan\_opt](structpcie__scan__opt.md) \*opt);

223

[ 231](group__pcie__host__interface.md#gadeb891fbb5b900eb60de22d40afe355e)extern bool [pcie\_get\_mbar](group__pcie__host__interface.md#gadeb891fbb5b900eb60de22d40afe355e)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

232 unsigned int bar\_index,

233 struct [pcie\_bar](structpcie__bar.md) \*mbar);

234

[ 248](group__pcie__host__interface.md#gad8463013e51c4ddcca7b5f805f918685)extern bool [pcie\_probe\_mbar](group__pcie__host__interface.md#gad8463013e51c4ddcca7b5f805f918685)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

249 unsigned int index,

250 struct [pcie\_bar](structpcie__bar.md) \*mbar);

251

[ 259](group__pcie__host__interface.md#ga3523bbdfd67d4b56cf6cd86c98c830bf)extern bool [pcie\_get\_iobar](group__pcie__host__interface.md#ga3523bbdfd67d4b56cf6cd86c98c830bf)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

260 unsigned int bar\_index,

261 struct [pcie\_bar](structpcie__bar.md) \*iobar);

262

[ 276](group__pcie__host__interface.md#gaa81d98a9ee58062c02be576fb0dfefd9)extern bool [pcie\_probe\_iobar](group__pcie__host__interface.md#gaa81d98a9ee58062c02be576fb0dfefd9)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

277 unsigned int index,

278 struct [pcie\_bar](structpcie__bar.md) \*iobar);

279

[ 287](group__pcie__host__interface.md#ga3516fec89df75eb3d77f54193059fc5c)extern void [pcie\_set\_cmd](group__pcie__host__interface.md#ga3516fec89df75eb3d77f54193059fc5c)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bits, bool on);

288

289#ifndef CONFIG\_PCIE\_CONTROLLER

[ 303](group__pcie__host__interface.md#gad69ae431e5f91992f071dee9d7fa9110)extern unsigned int [pcie\_alloc\_irq](group__pcie__host__interface.md#gad69ae431e5f91992f071dee9d7fa9110)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf);

304#endif /\* CONFIG\_PCIE\_CONTROLLER \*/

305

[ 312](group__pcie__host__interface.md#gaed7fef462ba02a22b5875b1a2c0d965a)extern unsigned int [pcie\_get\_irq](group__pcie__host__interface.md#gaed7fef462ba02a22b5875b1a2c0d965a)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf);

313

[ 326](group__pcie__host__interface.md#gafb69216f9224a9040b1f0b58eb286196)extern void [pcie\_irq\_enable](group__pcie__host__interface.md#gafb69216f9224a9040b1f0b58eb286196)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, unsigned int irq);

327

[ 335](group__pcie__host__interface.md#ga56e724c9bfd7f44c550ccff1b46978a8)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_get\_cap](group__pcie__host__interface.md#ga56e724c9bfd7f44c550ccff1b46978a8)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cap\_id);

336

[ 344](group__pcie__host__interface.md#ga5db0d2a5946d20406070b47a1a7acf21)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_get\_ext\_cap](group__pcie__host__interface.md#ga5db0d2a5946d20406070b47a1a7acf21)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cap\_id);

345

[ 357](group__pcie__host__interface.md#ga14970194de1024a1a4669b69f932a4f5)extern bool [pcie\_connect\_dynamic\_irq](group__pcie__host__interface.md#ga14970194de1024a1a4669b69f932a4f5)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf,

358 unsigned int irq,

359 unsigned int priority,

360 void (\*routine)(const void \*parameter),

361 const void \*parameter,

362 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

363

[ 374](group__pcie__host__interface.md#ga7b500200f090dc95322fe670bf64628d)#define PCIE\_HOST\_CONTROLLER(n) PCIE\_BDF(0, 0, n)

375

376/\*

377 \* Configuration word 13 contains the head of the capabilities list.

378 \*/

379

[ 380](group__pcie__host__interface.md#gaad23a180cf411bd8fa10027b9f16eb91)#define PCIE\_CONF\_CAPPTR 13U /\* capabilities pointer \*/

[ 381](group__pcie__host__interface.md#gabe5832ddf2b8399e8f672564ce85ad7e)#define PCIE\_CONF\_CAPPTR\_FIRST(w) (((w) >> 2) & 0x3FU)

382

383/\*

384 \* The first word of every capability contains a capability identifier,

385 \* and a link to the next capability (or 0) in configuration space.

386 \*/

387

[ 388](group__pcie__host__interface.md#gaa888f548db209011f1cf5c87b1f351b8)#define PCIE\_CONF\_CAP\_ID(w) ((w) & 0xFFU)

[ 389](group__pcie__host__interface.md#ga98476f56fe7d46b6bee505e0db1c1906)#define PCIE\_CONF\_CAP\_NEXT(w) (((w) >> 10) & 0x3FU)

390

391/\*

392 \* The extended PCI Express capabilities lie at the end of the PCI configuration space

393 \*/

394

[ 395](group__pcie__host__interface.md#gabeb1434679b73c98f2ada475c8502e32)#define PCIE\_CONF\_EXT\_CAPPTR 64U

396

397/\*

398 \* The first word of every capability contains an extended capability identifier,

399 \* and a link to the next capability (or 0) in the extended configuration space.

400 \*/

401

[ 402](group__pcie__host__interface.md#ga491d796e2477816c8f8aac4c7b753e3d)#define PCIE\_CONF\_EXT\_CAP\_ID(w) ((w) & 0xFFFFU)

[ 403](group__pcie__host__interface.md#gaf22a73f116325d3509cde1f83b3d7900)#define PCIE\_CONF\_EXT\_CAP\_VER(w) (((w) >> 16) & 0xFU)

[ 404](group__pcie__host__interface.md#gad0fa4f22781b85d06321192338088073)#define PCIE\_CONF\_EXT\_CAP\_NEXT(w) (((w) >> 20) & 0xFFFU)

405

406/\*

407 \* Configuration word 0 aligns directly with pcie\_id\_t.

408 \*/

409

[ 410](group__pcie__host__interface.md#ga2b694e339f9be5982605ed53e022ae06)#define PCIE\_CONF\_ID 0U

411

412/\*

413 \* Configuration word 1 contains command and status bits.

414 \*/

415

[ 416](group__pcie__host__interface.md#ga2fc046f15e216337194e41480518c982)#define PCIE\_CONF\_CMDSTAT 1U /\* command/status register \*/

417

[ 418](group__pcie__host__interface.md#ga6a9008421671f66ea9a6f11f87edd514)#define PCIE\_CONF\_CMDSTAT\_IO 0x00000001U /\* I/O access enable \*/

[ 419](group__pcie__host__interface.md#ga24661608e9f66f79bbdcde9304b24820)#define PCIE\_CONF\_CMDSTAT\_MEM 0x00000002U /\* mem access enable \*/

[ 420](group__pcie__host__interface.md#ga8a770450f03bfb020f223e0fea96189d)#define PCIE\_CONF\_CMDSTAT\_MASTER 0x00000004U /\* bus master enable \*/

[ 421](group__pcie__host__interface.md#ga4712b7b75d9bf0098e6c80c69587ef86)#define PCIE\_CONF\_CMDSTAT\_INTERRUPT 0x00080000U /\* interrupt status \*/

[ 422](group__pcie__host__interface.md#ga7127f82d9c9b093b1056125ca1bb9d65)#define PCIE\_CONF\_CMDSTAT\_CAPS 0x00100000U /\* capabilities list \*/

423

424/\*

425 \* Configuration word 2 has additional function identification that

426 \* we only care about for debug output (PCIe shell commands).

427 \*/

428

[ 429](group__pcie__host__interface.md#ga6946589a87e364c4710fba1dded553dc)#define PCIE\_CONF\_CLASSREV 2U /\* class/revision register \*/

430

[ 431](group__pcie__host__interface.md#gace40af940c01af2876e6fe8d599677bc)#define PCIE\_CONF\_CLASSREV\_CLASS(w) (((w) >> 24) & 0xFFU)

[ 432](group__pcie__host__interface.md#ga769e486c00a8ceda4ddb3f3eebc09c59)#define PCIE\_CONF\_CLASSREV\_SUBCLASS(w) (((w) >> 16) & 0xFFU)

[ 433](group__pcie__host__interface.md#ga36f77d220a11a9a30c4656e7f616ec05)#define PCIE\_CONF\_CLASSREV\_PROGIF(w) (((w) >> 8) & 0xFFU)

[ 434](group__pcie__host__interface.md#gae102d89e2fb359c3c9dda6b35d9ecd4f)#define PCIE\_CONF\_CLASSREV\_REV(w) ((w) & 0xFFU)

435

436/\*

437 \* The only part of configuration word 3 that is of interest to us is

438 \* the header type, as we use it to distinguish functional endpoints

439 \* from bridges (which are, for our purposes, transparent).

440 \*/

441

[ 442](group__pcie__host__interface.md#ga43ad620ae5a3041f0d7553de03c6da84)#define PCIE\_CONF\_TYPE 3U

443

[ 444](group__pcie__host__interface.md#ga9462e002a9d4b49ef7e7c97942765215)#define PCIE\_CONF\_MULTIFUNCTION(w) (((w) & 0x00800000U) != 0U)

[ 445](group__pcie__host__interface.md#gab7c494d71f6490e483b642a02ef90930)#define PCIE\_CONF\_TYPE\_BRIDGE(w) (((w) & 0x007F0000U) != 0U)

[ 446](group__pcie__host__interface.md#ga0580b798e6498097573c1eb0f2c6d2b1)#define PCIE\_CONF\_TYPE\_GET(w) (((w) >> 16) & 0x7F)

447

[ 448](group__pcie__host__interface.md#ga8b76fee3c256914a5044313ff9805969)#define PCIE\_CONF\_TYPE\_STANDARD 0x0U

[ 449](group__pcie__host__interface.md#ga90e8a996bf491fda870ff29b119a5242)#define PCIE\_CONF\_TYPE\_PCI\_BRIDGE 0x1U

[ 450](group__pcie__host__interface.md#gae9587843cac6247fcfb72f985ff4b030)#define PCIE\_CONF\_TYPE\_CARDBUS\_BRIDGE 0x2U

451

452/\*

453 \* Words 4-9 are BARs are I/O or memory decoders. Memory decoders may

454 \* be 64-bit decoders, in which case the next configuration word holds

455 \* the high-order bits (and is, thus, not a BAR itself).

456 \*/

457

[ 458](group__pcie__host__interface.md#gadfd21197ccd78d7bfb549fbb6f7070ff)#define PCIE\_CONF\_BAR0 4U

[ 459](group__pcie__host__interface.md#ga77e43c6060febf8a5b8439c7fc940a1f)#define PCIE\_CONF\_BAR1 5U

[ 460](group__pcie__host__interface.md#ga90040a3b78c5f5563f2f123e9fb05dd8)#define PCIE\_CONF\_BAR2 6U

[ 461](group__pcie__host__interface.md#ga05b9be5537cf1a4f3994c1a2c82282a1)#define PCIE\_CONF\_BAR3 7U

[ 462](group__pcie__host__interface.md#ga51dbf953128b6a464bf50cfa459626e7)#define PCIE\_CONF\_BAR4 8U

[ 463](group__pcie__host__interface.md#ga84fb2d49dd14438a9ff12a8eeb5bca60)#define PCIE\_CONF\_BAR5 9U

464

[ 465](group__pcie__host__interface.md#ga2f4020ce7fec0e3b5c9b121951468b70)#define PCIE\_CONF\_BAR\_IO(w) (((w) & 0x00000001U) == 0x00000001U)

[ 466](group__pcie__host__interface.md#ga6018ef2d851fd6a64a1ad4dde956f4c9)#define PCIE\_CONF\_BAR\_MEM(w) (((w) & 0x00000001U) != 0x00000001U)

[ 467](group__pcie__host__interface.md#ga6d2644d85b7bfbf9a526e6d54096982d)#define PCIE\_CONF\_BAR\_64(w) (((w) & 0x00000006U) == 0x00000004U)

[ 468](group__pcie__host__interface.md#gaf163a00f52cc96bc7694e4e7e7a8d1fe)#define PCIE\_CONF\_BAR\_ADDR(w) ((w) & ~0xfUL)

[ 469](group__pcie__host__interface.md#gabe49cc62101a531ca9e26b0290218797)#define PCIE\_CONF\_BAR\_IO\_ADDR(w) ((w) & ~0x3UL)

[ 470](group__pcie__host__interface.md#ga23c45457ec77c6fd2e1977710f6edf28)#define PCIE\_CONF\_BAR\_FLAGS(w) ((w) & 0xfUL)

[ 471](group__pcie__host__interface.md#ga296141fc89700213899b6463e1166477)#define PCIE\_CONF\_BAR\_NONE 0U

472

[ 473](group__pcie__host__interface.md#ga65e8ddebc6d25b51940ae647f81deca1)#define PCIE\_CONF\_BAR\_INVAL 0xFFFFFFF0U

[ 474](group__pcie__host__interface.md#ga8e1968a28791ed0529d622f32e6fad6c)#define PCIE\_CONF\_BAR\_INVAL64 0xFFFFFFFFFFFFFFF0UL

475

[ 476](group__pcie__host__interface.md#gafd74fe08ef11c685775433236d0fd734)#define PCIE\_CONF\_BAR\_INVAL\_FLAGS(w) \

477 ((((w) & 0x00000006U) == 0x00000006U) || \

478 (((w) & 0x00000006U) == 0x00000002U))

479

480/\*

481 \* Type 1 Header has files related to bus management

482 \*/

[ 483](group__pcie__host__interface.md#gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e)#define PCIE\_BUS\_NUMBER 6U

484

[ 485](group__pcie__host__interface.md#ga4c0dbee39acf51c94b5ececba150f8d0)#define PCIE\_BUS\_PRIMARY\_NUMBER(w) ((w) & 0xffUL)

[ 486](group__pcie__host__interface.md#ga61cd874c47de3545ca2ffa1eecd7eb42)#define PCIE\_BUS\_SECONDARY\_NUMBER(w) (((w) >> 8) & 0xffUL)

[ 487](group__pcie__host__interface.md#ga0be93727f18869b7a486e42eac47fa2d)#define PCIE\_BUS\_SUBORDINATE\_NUMBER(w) (((w) >> 16) & 0xffUL)

[ 488](group__pcie__host__interface.md#gaa05e49d0cafbe51b7742354470d07bd0)#define PCIE\_SECONDARY\_LATENCY\_TIMER(w) (((w) >> 24) & 0xffUL)

489

[ 490](group__pcie__host__interface.md#ga784bc42d77fec195d794c29067bd988c)#define PCIE\_BUS\_NUMBER\_VAL(prim, sec, sub, lat) \

491 (((prim) & 0xffUL) | \

492 (((sec) & 0xffUL) << 8) | \

493 (((sub) & 0xffUL) << 16) | \

494 (((lat) & 0xffUL) << 24))

495

496/\*

497 \* Type 1 words 7 to 12 setups Bridge Memory base and limits

498 \*/

[ 499](group__pcie__host__interface.md#ga111eab92400e240ec5b7f08caf1b8a87)#define PCIE\_IO\_SEC\_STATUS 7U

500

[ 501](group__pcie__host__interface.md#ga34f56e87ececf58b285e91341cd27d23)#define PCIE\_IO\_BASE(w) ((w) & 0xffUL)

[ 502](group__pcie__host__interface.md#ga4629a222d00917b2e3cad6aadbfd2ec1)#define PCIE\_IO\_LIMIT(w) (((w) >> 8) & 0xffUL)

[ 503](group__pcie__host__interface.md#ga804b34fd47ba065287e0257fac84ac35)#define PCIE\_SEC\_STATUS(w) (((w) >> 16) & 0xffffUL)

504

[ 505](group__pcie__host__interface.md#ga61f05b2c4cd5c672af43960b320e33bc)#define PCIE\_IO\_SEC\_STATUS\_VAL(iob, iol, sec\_status) \

506 (((iob) & 0xffUL) | \

507 (((iol) & 0xffUL) << 8) | \

508 (((sec\_status) & 0xffffUL) << 16))

509

[ 510](group__pcie__host__interface.md#ga6fbcd3f523deb069aa31bcd31973d00b)#define PCIE\_MEM\_BASE\_LIMIT 8U

511

[ 512](group__pcie__host__interface.md#gacd6be1e38666a6a137b1654007cf293a)#define PCIE\_MEM\_BASE(w) ((w) & 0xffffUL)

[ 513](group__pcie__host__interface.md#ga9f5d23ad0674aed0bf5c1869621de303)#define PCIE\_MEM\_LIMIT(w) (((w) >> 16) & 0xffffUL)

514

[ 515](group__pcie__host__interface.md#ga93a6dbe27d3d11be29397ae80c58a589)#define PCIE\_MEM\_BASE\_LIMIT\_VAL(memb, meml) \

516 (((memb) & 0xffffUL) | \

517 (((meml) & 0xffffUL) << 16))

518

[ 519](group__pcie__host__interface.md#ga8dd5906e8d735210d9f8ca25d39684b4)#define PCIE\_PREFETCH\_BASE\_LIMIT 9U

520

[ 521](group__pcie__host__interface.md#ga5f7aa0fc063ec072bf7e89fca603c825)#define PCIE\_PREFETCH\_BASE(w) ((w) & 0xffffUL)

[ 522](group__pcie__host__interface.md#gaf0a18504a4eb2061d1afc90fc7b8ee21)#define PCIE\_PREFETCH\_LIMIT(w) (((w) >> 16) & 0xffffUL)

523

[ 524](group__pcie__host__interface.md#ga02b269663488e7c7469415622390ce55)#define PCIE\_PREFETCH\_BASE\_LIMIT\_VAL(pmemb, pmeml) \

525 (((pmemb) & 0xffffUL) | \

526 (((pmeml) & 0xffffUL) << 16))

527

[ 528](group__pcie__host__interface.md#ga6ebdd02e0599f33becb6cf413be0a8cd)#define PCIE\_PREFETCH\_BASE\_UPPER 10U

529

[ 530](group__pcie__host__interface.md#gab0eda55fd8c2c4025dc4350ef946a61b)#define PCIE\_PREFETCH\_LIMIT\_UPPER 11U

531

[ 532](group__pcie__host__interface.md#gafc1acf0ac9b46629497c7a552f5650ce)#define PCIE\_IO\_BASE\_LIMIT\_UPPER 12U

533

[ 534](group__pcie__host__interface.md#ga8bf9a619d6d83cbb009a7f18b501db92)#define PCIE\_IO\_BASE\_UPPER(w) ((w) & 0xffffUL)

[ 535](group__pcie__host__interface.md#ga76a59c926f2760a04c4d8439cb227fe2)#define PCIE\_IO\_LIMIT\_UPPER(w) (((w) >> 16) & 0xffffUL)

536

[ 537](group__pcie__host__interface.md#ga88669a9ca40294cee41bb163a908737f)#define PCIE\_IO\_BASE\_LIMIT\_UPPER\_VAL(iobu, iolu) \

538 (((iobu) & 0xffffUL) | \

539 (((iolu) & 0xffffUL) << 16))

540

541/\*

542 \* Word 15 contains information related to interrupts.

543 \*

544 \* We're only interested in the low byte, which is [supposed to be] set by

545 \* the firmware to indicate which wire IRQ the device interrupt is routed to.

546 \*/

547

[ 548](group__pcie__host__interface.md#gaa5a2c8849e4cac05ee584827aedbfb93)#define PCIE\_CONF\_INTR 15U

549

[ 550](group__pcie__host__interface.md#ga5c2f2d310dc6a73530b6909ce2c2536e)#define PCIE\_CONF\_INTR\_IRQ(w) ((w) & 0xFFU)

[ 551](group__pcie__host__interface.md#ga995ca5b5146669c9234d3cdd596b715c)#define PCIE\_CONF\_INTR\_IRQ\_NONE 0xFFU /\* no interrupt routed \*/

552

[ 553](group__pcie__host__interface.md#ga1ce9e061b5a773f3ee74f78893174f9e)#define PCIE\_MAX\_BUS (0xFFFFFFFFU & PCIE\_BDF\_BUS\_MASK)

[ 554](group__pcie__host__interface.md#ga8809359a58c787a939d01f25e12ac51a)#define PCIE\_MAX\_DEV (0xFFFFFFFFU & PCIE\_BDF\_DEV\_MASK)

[ 555](group__pcie__host__interface.md#gaee8ddb7b7b1354fd5c835b67321f286b)#define PCIE\_MAX\_FUNC (0xFFFFFFFFU & PCIE\_BDF\_FUNC\_MASK)

556

[ 571](group__pcie__host__interface.md#ga6616499a7be31d40af31bb8134aa4a51)#define PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, \

572 isr\_p, isr\_param\_p, flags\_p) \

573 ARCH\_PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, \

574 isr\_p, isr\_param\_p, flags\_p)

575

576#ifdef \_\_cplusplus

577}

578#endif

579

583

584#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_PCIE\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[pcie.h](dt-bindings_2pcie_2pcie_8h.md)

[pcie\_conf\_read](group__pcie__host__interface.md#ga10ecc667c564548e4ddf3ca4374242b5)

uint32\_t pcie\_conf\_read(pcie\_bdf\_t bdf, unsigned int reg)

Read a 32-bit word from an endpoint's configuration space.

[pcie\_connect\_dynamic\_irq](group__pcie__host__interface.md#ga14970194de1024a1a4669b69f932a4f5)

bool pcie\_connect\_dynamic\_irq(pcie\_bdf\_t bdf, unsigned int irq, unsigned int priority, void(\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)

Dynamically connect a PCIe endpoint IRQ to an ISR handler.

[pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04)

uint32\_t pcie\_id\_t

A unique PCI(e) identifier (vendor ID, device ID).

**Definition** pcie.h:47

[pcie\_set\_cmd](group__pcie__host__interface.md#ga3516fec89df75eb3d77f54193059fc5c)

void pcie\_set\_cmd(pcie\_bdf\_t bdf, uint32\_t bits, bool on)

Set or reset bits in the endpoint command/status register.

[pcie\_get\_iobar](group__pcie__host__interface.md#ga3523bbdfd67d4b56cf6cd86c98c830bf)

bool pcie\_get\_iobar(pcie\_bdf\_t bdf, unsigned int bar\_index, struct pcie\_bar \*iobar)

Get the I/O BAR at a specific BAR index.

[pcie\_conf\_write](group__pcie__host__interface.md#ga47a2e88935e04330d449db5463d9f21a)

void pcie\_conf\_write(pcie\_bdf\_t bdf, unsigned int reg, uint32\_t data)

Write a 32-bit word to an endpoint's configuration space.

[pcie\_get\_cap](group__pcie__host__interface.md#ga56e724c9bfd7f44c550ccff1b46978a8)

uint32\_t pcie\_get\_cap(pcie\_bdf\_t bdf, uint32\_t cap\_id)

Find a PCI(e) capability in an endpoint's configuration space.

[pcie\_get\_ext\_cap](group__pcie__host__interface.md#ga5db0d2a5946d20406070b47a1a7acf21)

uint32\_t pcie\_get\_ext\_cap(pcie\_bdf\_t bdf, uint32\_t cap\_id)

Find an Extended PCI(e) capability in an endpoint's configuration space.

[pcie\_scan\_cb\_t](group__pcie__host__interface.md#ga922580e4fb6200ef75425bb54801ceda)

bool(\* pcie\_scan\_cb\_t)(pcie\_bdf\_t bdf, pcie\_id\_t id, void \*cb\_data)

Callback type used for scanning for PCI endpoints.

**Definition** pcie.h:191

[pcie\_scan](group__pcie__host__interface.md#ga9a7b3c202f91d37fe8445d5016f4c6ab)

int pcie\_scan(const struct pcie\_scan\_opt \*opt)

Scan for PCIe devices.

[pcie\_probe\_iobar](group__pcie__host__interface.md#gaa81d98a9ee58062c02be576fb0dfefd9)

bool pcie\_probe\_iobar(pcie\_bdf\_t bdf, unsigned int index, struct pcie\_bar \*iobar)

Probe the nth I/O BAR address assigned to an endpoint.

[pcie\_alloc\_irq](group__pcie__host__interface.md#gad69ae431e5f91992f071dee9d7fa9110)

unsigned int pcie\_alloc\_irq(pcie\_bdf\_t bdf)

Allocate an IRQ for an endpoint.

[pcie\_probe\_mbar](group__pcie__host__interface.md#gad8463013e51c4ddcca7b5f805f918685)

bool pcie\_probe\_mbar(pcie\_bdf\_t bdf, unsigned int index, struct pcie\_bar \*mbar)

Probe the nth MMIO address assigned to an endpoint.

[pcie\_get\_mbar](group__pcie__host__interface.md#gadeb891fbb5b900eb60de22d40afe355e)

bool pcie\_get\_mbar(pcie\_bdf\_t bdf, unsigned int bar\_index, struct pcie\_bar \*mbar)

Get the MBAR at a specific BAR index.

[pcie\_get\_irq](group__pcie__host__interface.md#gaed7fef462ba02a22b5875b1a2c0d965a)

unsigned int pcie\_get\_irq(pcie\_bdf\_t bdf)

Return the IRQ assigned by the firmware/board to an endpoint.

[pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb)

uint32\_t pcie\_bdf\_t

A unique PCI(e) endpoint (bus, device, function).

**Definition** pcie.h:37

[pcie\_irq\_enable](group__pcie__host__interface.md#gafb69216f9224a9040b1f0b58eb286196)

void pcie\_irq\_enable(pcie\_bdf\_t bdf, unsigned int irq)

Enable the PCI(e) endpoint to generate the specified IRQ.

[PCIE\_SCAN\_RECURSIVE](group__pcie__host__interface.md#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4)

@ PCIE\_SCAN\_RECURSIVE

Scan all available PCI host controllers and sub-busses.

**Definition** pcie.h:195

[PCIE\_SCAN\_CB\_ALL](group__pcie__host__interface.md#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072)

@ PCIE\_SCAN\_CB\_ALL

Do the callback for all endpoint types, including bridges.

**Definition** pcie.h:197

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[pcie\_bar](structpcie__bar.md)

**Definition** pcie.h:152

[pcie\_bar::phys\_addr](structpcie__bar.md#a75ed340a7d80a6825f3c60469194dae8)

uintptr\_t phys\_addr

**Definition** pcie.h:153

[pcie\_bar::size](structpcie__bar.md#ab68c921f2993c94d2ae65684568bf770)

size\_t size

**Definition** pcie.h:154

[pcie\_dev](structpcie__dev.md)

**Definition** pcie.h:59

[pcie\_dev::id](structpcie__dev.md#a5709ef678d9e81d4d3a61f6c26371076)

pcie\_id\_t id

**Definition** pcie.h:61

[pcie\_dev::class\_rev\_mask](structpcie__dev.md#a798e25696997a74ed01f8df6cec64489)

uint32\_t class\_rev\_mask

**Definition** pcie.h:63

[pcie\_dev::bdf](structpcie__dev.md#a7cc2f61e85b1d9c4985115b91fc6e832)

pcie\_bdf\_t bdf

**Definition** pcie.h:60

[pcie\_dev::class\_rev](structpcie__dev.md#abedf281cdce4961dd02abba849747f45)

uint32\_t class\_rev

**Definition** pcie.h:62

[pcie\_scan\_opt](structpcie__scan__opt.md)

Options for performing a scan for PCI devices.

**Definition** pcie.h:201

[pcie\_scan\_opt::bus](structpcie__scan__opt.md#a036225c7a5730ba2040e03cab491b9da)

uint8\_t bus

Initial bus number to scan.

**Definition** pcie.h:203

[pcie\_scan\_opt::cb\_data](structpcie__scan__opt.md#a11b39138d2a2b6b1e8e1bd80216a8da6)

void \* cb\_data

Custom data to pass to the scan callback.

**Definition** pcie.h:209

[pcie\_scan\_opt::cb](structpcie__scan__opt.md#a28ad6c4993eed7bdf08ce682692bf306)

pcie\_scan\_cb\_t cb

Function to call for each found endpoint.

**Definition** pcie.h:206

[pcie\_scan\_opt::flags](structpcie__scan__opt.md#a7e485fb824dea16f9d5fdcb7079ebb7e)

uint32\_t flags

Scan flags.

**Definition** pcie.h:212

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [pcie.h](drivers_2pcie_2pcie_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
