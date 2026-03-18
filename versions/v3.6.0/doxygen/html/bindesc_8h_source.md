---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bindesc_8h_source.html
original_path: doxygen/html/bindesc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bindesc.h

[Go to the documentation of this file.](bindesc_8h.md)

1/\*

2 \* Copyright (c) 2023 Yonatan Schachter

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_BINDESC\_H\_

8#define ZEPHYR\_INCLUDE\_ZEPHYR\_BINDESC\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif /\* \_\_cplusplus \*/

13

14/\*

15 \* Corresponds to the definitions in scripts/west\_commands/bindesc.py.

16 \* Do not change without syncing the definitions in both files!

17 \*/

[ 18](bindesc_8h.md#a8e7d54173280f72eb5f031d752c19197)#define BINDESC\_MAGIC 0xb9863e5a7ea46046

[ 19](bindesc_8h.md#a674bcf8c1d881131b5e82d5dec48ee33)#define BINDESC\_ALIGNMENT 4

[ 20](bindesc_8h.md#adac0fea8ab54ea428c533f509058b910)#define BINDESC\_TYPE\_UINT 0x0

[ 21](bindesc_8h.md#a68acc09b5e324134e5c83eeaa064fc41)#define BINDESC\_TYPE\_STR 0x1

[ 22](bindesc_8h.md#a24e6723b552f65cc1f143bcb7f66f125)#define BINDESC\_TYPE\_BYTES 0x2

[ 23](bindesc_8h.md#ac98ab7042b1b3f6654e910fa4d0c2d40)#define BINDESC\_TYPE\_DESCRIPTORS\_END 0xf

24

30

31/\*

32 \* Corresponds to the definitions in scripts/west\_commands/bindesc.py.

33 \* Do not change without syncing the definitions in both files!

34 \*/

35

[ 37](group__bindesc__define.md#ga8521a2005ed6ad5bdbd6ad27a0e26cfc)#define BINDESC\_ID\_APP\_VERSION\_STRING 0x800

38

[ 40](group__bindesc__define.md#ga94f405178c0139626718b143e6f22734)#define BINDESC\_ID\_APP\_VERSION\_MAJOR 0x801

41

[ 43](group__bindesc__define.md#gaab4f7cdf7ea4f766be1fa7779eef1bdb)#define BINDESC\_ID\_APP\_VERSION\_MINOR 0x802

44

[ 46](group__bindesc__define.md#ga90eb8f252c3484103eee18dbb1aabdc6)#define BINDESC\_ID\_APP\_VERSION\_PATCHLEVEL 0x803

47

[ 49](group__bindesc__define.md#ga66b25585ff23de9906814ddecb4ac4ea)#define BINDESC\_ID\_APP\_VERSION\_NUMBER 0x804

50

[ 52](group__bindesc__define.md#ga35fdf13eb11dd4eeca1bf2dc57782777)#define BINDESC\_ID\_KERNEL\_VERSION\_STRING 0x900

53

[ 55](group__bindesc__define.md#gabd5e9193c56495faa19f299371a02fd0)#define BINDESC\_ID\_KERNEL\_VERSION\_MAJOR 0x901

56

[ 58](group__bindesc__define.md#ga9ab56a8cef01c648a313bb4e5b7983e4)#define BINDESC\_ID\_KERNEL\_VERSION\_MINOR 0x902

59

[ 61](group__bindesc__define.md#ga2ef91c2cd49d61c9f3e95ac5292e6983)#define BINDESC\_ID\_KERNEL\_VERSION\_PATCHLEVEL 0x903

62

[ 64](group__bindesc__define.md#gad2c5489eaa1a191a49ffd409462b1af4)#define BINDESC\_ID\_KERNEL\_VERSION\_NUMBER 0x904

65

[ 67](group__bindesc__define.md#ga21fbd3ff6a408febdaf0f1a1f19f0fa3)#define BINDESC\_ID\_BUILD\_TIME\_YEAR 0xa00

68

[ 70](group__bindesc__define.md#ga8e68f8226d05415c040f6fb74bada6fc)#define BINDESC\_ID\_BUILD\_TIME\_MONTH 0xa01

71

[ 73](group__bindesc__define.md#ga5710e218f4f10e5049d039b17a376d0b)#define BINDESC\_ID\_BUILD\_TIME\_DAY 0xa02

74

[ 76](group__bindesc__define.md#gaeed1651e0d025ff74092a88b6d57e408)#define BINDESC\_ID\_BUILD\_TIME\_HOUR 0xa03

77

[ 79](group__bindesc__define.md#ga67f679968aeea5517e02da6e5e67d73e)#define BINDESC\_ID\_BUILD\_TIME\_MINUTE 0xa04

80

[ 82](group__bindesc__define.md#gacdff70f58c8098e23611327c1264a7dd)#define BINDESC\_ID\_BUILD\_TIME\_SECOND 0xa05

83

[ 85](group__bindesc__define.md#gab0eefe2d83294d6ebe4ca6299f05d785)#define BINDESC\_ID\_BUILD\_TIME\_UNIX 0xa06

86

[ 88](group__bindesc__define.md#gad8803e832ed0a42fd7033e277f8d8362)#define BINDESC\_ID\_BUILD\_DATE\_TIME\_STRING 0xa07

89

[ 91](group__bindesc__define.md#ga8bf6d98fb9495f2cca6b0403dffd0752)#define BINDESC\_ID\_BUILD\_DATE\_STRING 0xa08

92

[ 94](group__bindesc__define.md#gac4f75b876a81072e14bb39e3fb1c1f8a)#define BINDESC\_ID\_BUILD\_TIME\_STRING 0xa09

95

[ 97](group__bindesc__define.md#ga4cc66094d33709d9738b49e181a6eec3)#define BINDESC\_ID\_HOST\_NAME 0xb00

98

[ 100](group__bindesc__define.md#ga51b3fdd47d3dd94101134523c4dca144)#define BINDESC\_ID\_C\_COMPILER\_NAME 0xb01

101

[ 103](group__bindesc__define.md#gac4c6c9576b31cb2c26b085537648552b)#define BINDESC\_ID\_C\_COMPILER\_VERSION 0xb02

104

[ 106](group__bindesc__define.md#ga6f198590afdb2524b587e0194598b8eb)#define BINDESC\_ID\_CXX\_COMPILER\_NAME 0xb03

107

[ 109](group__bindesc__define.md#ga7ec0430daae1f99bdeeae6a636a263d8)#define BINDESC\_ID\_CXX\_COMPILER\_VERSION 0xb04

110

[ 111](group__bindesc__define.md#gac12b3cbf6d132fb54bbf702fd581373f)#define BINDESC\_TAG\_DESCRIPTORS\_END BINDESC\_TAG(DESCRIPTORS\_END, 0x0fff)

112

116

117/\*

118 \* Utility macro to generate a tag from a type and an ID

119 \*

120 \* type - Type of the descriptor, UINT, STR or BYTES

121 \* id - Unique ID for the descriptor, must fit in 12 bits

122 \*/

123#define BINDESC\_TAG(type, id) ((BINDESC\_TYPE\_##type & 0xf) << 12 | (id & 0x0fff))

124

128

129#if !IS\_ENABLED(\_LINKER)

130

131#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

132

136

137/\*

138 \* Utility macro to get the name of a bindesc entry

139 \*/

140#define BINDESC\_NAME(name) bindesc\_entry\_##name

141

142/\* Convenience helper for declaring a binary descriptor entry. \*/

143#define \_\_BINDESC\_ENTRY\_DEFINE(name) \

144 \_\_aligned(BINDESC\_ALIGNMENT) const struct bindesc\_entry BINDESC\_NAME(name) \

145 \_\_in\_section(\_bindesc\_entry, static, name) \_\_used \_\_noasan

146

150

[ 165](group__bindesc__define.md#gacfba0fe843c53a86271e685394078b22)#define BINDESC\_STR\_DEFINE(name, id, value) \

166 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

167 .tag = BINDESC\_TAG(STR, id), \

168 .len = (uint16\_t)sizeof(value), \

169 .data = value, \

170 }

171

[ 186](group__bindesc__define.md#gac603068b1abdac72d5f668fea3b3cdff)#define BINDESC\_UINT\_DEFINE(name, id, value) \

187 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

188 .tag = BINDESC\_TAG(UINT, id), \

189 .len = (uint16\_t)sizeof(uint32\_t), \

190 .data = sys\_uint32\_to\_array(value), \

191 }

192

[ 211](group__bindesc__define.md#ga137cc1f8fcc0e36e71c8ea4b8c0e8885)#define BINDESC\_BYTES\_DEFINE(name, id, value) \

212 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

213 .tag = BINDESC\_TAG(BYTES, id), \

214 .len = (uint16\_t)sizeof((uint8\_t [])\_\_DEBRACKET value), \

215 .data = \_\_DEBRACKET value, \

216 }

217

[ 227](group__bindesc__define.md#gaf7628498209bc6729a6abf36a92d0cbd)#define BINDESC\_GET\_STR(name) BINDESC\_NAME(name).data

228

[ 238](group__bindesc__define.md#ga8f738fd9f99f52f0c7ce81011c8e7b98)#define BINDESC\_GET\_UINT(name) \*(uint32\_t \*)&(BINDESC\_NAME(name).data)

239

[ 252](group__bindesc__define.md#ga1fbf08f04e66c250aecdd70045242a37)#define BINDESC\_GET\_BYTES(name) BINDESC\_NAME(name).data

253

[ 263](group__bindesc__define.md#gace8f89f0a8d25a12503c1b337f74dd30)#define BINDESC\_GET\_SIZE(name) BINDESC\_NAME(name).len

264

268

269/\*

270 \* An entry of the binary descriptor header. Each descriptor is

271 \* described by one of these entries.

272 \*/

[ 273](structbindesc__entry.md)struct [bindesc\_entry](structbindesc__entry.md) {

[ 275](structbindesc__entry.md#ab040a2e6d5370498f2a689ba172e4112) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tag](structbindesc__entry.md#ab040a2e6d5370498f2a689ba172e4112);

[ 277](structbindesc__entry.md#ad756a440a8dfa9d396258707a1f681e4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbindesc__entry.md#ad756a440a8dfa9d396258707a1f681e4);

[ 279](structbindesc__entry.md#a8cc383c8f7e11caff91912c8c2cc6b41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbindesc__entry.md#a8cc383c8f7e11caff91912c8c2cc6b41)[];

280} \_\_packed;

281

282/\*

283 \* We're assuming that `struct bindesc\_entry` has a specific layout in

284 \* memory, so it's worth making sure that the layout is really what we

285 \* think it is. If these assertions fail for your toolchain/platform,

286 \* please open a bug report.

287 \*/

[ 288](bindesc_8h.md#af8174bbae9567135fe17f1e55621f641)BUILD\_ASSERT(offsetof(struct [bindesc\_entry](structbindesc__entry.md), tag) == 0, "Incorrect memory layout");

289BUILD\_ASSERT(offsetof(struct [bindesc\_entry](structbindesc__entry.md), len) == 2, "Incorrect memory layout");

290BUILD\_ASSERT(offsetof(struct [bindesc\_entry](structbindesc__entry.md), data) == 4, "Incorrect memory layout");

291

292#if IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_STRING)

293extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_string);

294#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_STRING) \*/

295

296#if IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_MAJOR)

297extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_major);

298#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_MAJOR) \*/

299

300#if IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_MINOR)

301extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_minor);

302#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_MINOR) \*/

303

304#if IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_PATCHLEVEL)

305extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_patchlevel);

306#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_PATCHLEVEL) \*/

307

308#if IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_NUMBER)

309extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(kernel\_version\_number);

310#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_KERNEL\_VERSION\_NUMBER) \*/

311

312#if IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_STRING)

313extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_string);

314#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_STRING) \*/

315

316#if IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_MAJOR)

317extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_major);

318#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_MAJOR) \*/

319

320#if IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_MINOR)

321extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_minor);

322#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_MINOR) \*/

323

324#if IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_PATCHLEVEL)

325extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_patchlevel);

326#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_PATCHLEVEL) \*/

327

328#if IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_NUMBER)

329extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(app\_version\_number);

330#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_APP\_VERSION\_NUMBER) \*/

331

332#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_YEAR)

333extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_year);

334#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_YEAR) \*/

335

336#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_MONTH)

337extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_month);

338#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_MONTH) \*/

339

340#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_DAY)

341extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_day);

342#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_DAY) \*/

343

344#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_HOUR)

345extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_hour);

346#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_HOUR) \*/

347

348#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_MINUTE)

349extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_minute);

350#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_MINUTE) \*/

351

352#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_SECOND)

353extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_second);

354#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_SECOND) \*/

355

356#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_UNIX)

357extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_unix);

358#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_UNIX) \*/

359

360#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_DATE\_TIME\_STRING)

361extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_date\_time\_string);

362#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_DATE\_TIME\_STRING) \*/

363

364#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_DATE\_STRING)

365extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_date\_string);

366#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_DATE\_STRING) \*/

367

368#if IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_STRING)

369extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(build\_time\_string);

370#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_BUILD\_TIME\_STRING) \*/

371

372#if IS\_ENABLED(CONFIG\_BINDESC\_HOST\_NAME)

373extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(host\_name);

374#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_HOST\_NAME) \*/

375

376#if IS\_ENABLED(CONFIG\_BINDESC\_C\_COMPILER\_NAME)

377extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(c\_compiler\_name);

378#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_C\_COMPILER\_NAME) \*/

379

380#if IS\_ENABLED(CONFIG\_BINDESC\_C\_COMPILER\_VERSION)

381extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(c\_compiler\_version);

382#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_C\_COMPILER\_VERSION) \*/

383

384#if IS\_ENABLED(CONFIG\_BINDESC\_CXX\_COMPILER\_NAME)

385extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(cxx\_compiler\_name);

386#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_CXX\_COMPILER\_NAME) \*/

387

388#if IS\_ENABLED(CONFIG\_BINDESC\_CXX\_COMPILER\_VERSION)

389extern const struct [bindesc\_entry](structbindesc__entry.md) BINDESC\_NAME(cxx\_compiler\_version);

390#endif /\* IS\_ENABLED(CONFIG\_BINDESC\_CXX\_COMPILER\_VERSION) \*/

391

392#endif /\* !IS\_ENABLED(\_LINKER) \*/

393

394#ifdef \_\_cplusplus

395}

396#endif

397

398#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_BINDESC\_H\_ \*/

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bindesc\_entry](structbindesc__entry.md)

**Definition** bindesc.h:273

[bindesc\_entry::data](structbindesc__entry.md#a8cc383c8f7e11caff91912c8c2cc6b41)

uint8\_t data[]

Value of the entry.

**Definition** bindesc.h:279

[bindesc\_entry::tag](structbindesc__entry.md#ab040a2e6d5370498f2a689ba172e4112)

uint16\_t tag

Tag of the entry.

**Definition** bindesc.h:275

[bindesc\_entry::len](structbindesc__entry.md#ad756a440a8dfa9d396258707a1f681e4)

uint16\_t len

Length of the descriptor data.

**Definition** bindesc.h:277

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bindesc.h](bindesc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
