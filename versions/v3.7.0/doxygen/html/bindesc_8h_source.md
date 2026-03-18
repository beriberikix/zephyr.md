---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bindesc_8h_source.html
original_path: doxygen/html/bindesc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

10#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif /\* \_\_cplusplus \*/

15

16/\*

17 \* Corresponds to the definitions in scripts/west\_commands/bindesc.py.

18 \* Do not change without syncing the definitions in both files!

19 \*/

[ 20](bindesc_8h.md#a8e7d54173280f72eb5f031d752c19197)#define BINDESC\_MAGIC 0xb9863e5a7ea46046

[ 21](bindesc_8h.md#a674bcf8c1d881131b5e82d5dec48ee33)#define BINDESC\_ALIGNMENT 4

[ 22](bindesc_8h.md#adac0fea8ab54ea428c533f509058b910)#define BINDESC\_TYPE\_UINT 0x0

[ 23](bindesc_8h.md#a68acc09b5e324134e5c83eeaa064fc41)#define BINDESC\_TYPE\_STR 0x1

[ 24](bindesc_8h.md#a24e6723b552f65cc1f143bcb7f66f125)#define BINDESC\_TYPE\_BYTES 0x2

[ 25](bindesc_8h.md#ac98ab7042b1b3f6654e910fa4d0c2d40)#define BINDESC\_TYPE\_DESCRIPTORS\_END 0xf

26

33

34/\*

35 \* Corresponds to the definitions in scripts/west\_commands/bindesc.py.

36 \* Do not change without syncing the definitions in both files!

37 \*/

38

[ 40](group__bindesc__define.md#ga8521a2005ed6ad5bdbd6ad27a0e26cfc)#define BINDESC\_ID\_APP\_VERSION\_STRING 0x800

41

[ 43](group__bindesc__define.md#ga94f405178c0139626718b143e6f22734)#define BINDESC\_ID\_APP\_VERSION\_MAJOR 0x801

44

[ 46](group__bindesc__define.md#gaab4f7cdf7ea4f766be1fa7779eef1bdb)#define BINDESC\_ID\_APP\_VERSION\_MINOR 0x802

47

[ 49](group__bindesc__define.md#ga90eb8f252c3484103eee18dbb1aabdc6)#define BINDESC\_ID\_APP\_VERSION\_PATCHLEVEL 0x803

50

[ 52](group__bindesc__define.md#ga66b25585ff23de9906814ddecb4ac4ea)#define BINDESC\_ID\_APP\_VERSION\_NUMBER 0x804

53

[ 55](group__bindesc__define.md#ga35fdf13eb11dd4eeca1bf2dc57782777)#define BINDESC\_ID\_KERNEL\_VERSION\_STRING 0x900

56

[ 58](group__bindesc__define.md#gabd5e9193c56495faa19f299371a02fd0)#define BINDESC\_ID\_KERNEL\_VERSION\_MAJOR 0x901

59

[ 61](group__bindesc__define.md#ga9ab56a8cef01c648a313bb4e5b7983e4)#define BINDESC\_ID\_KERNEL\_VERSION\_MINOR 0x902

62

[ 64](group__bindesc__define.md#ga2ef91c2cd49d61c9f3e95ac5292e6983)#define BINDESC\_ID\_KERNEL\_VERSION\_PATCHLEVEL 0x903

65

[ 67](group__bindesc__define.md#gad2c5489eaa1a191a49ffd409462b1af4)#define BINDESC\_ID\_KERNEL\_VERSION\_NUMBER 0x904

68

[ 70](group__bindesc__define.md#ga21fbd3ff6a408febdaf0f1a1f19f0fa3)#define BINDESC\_ID\_BUILD\_TIME\_YEAR 0xa00

71

[ 73](group__bindesc__define.md#ga8e68f8226d05415c040f6fb74bada6fc)#define BINDESC\_ID\_BUILD\_TIME\_MONTH 0xa01

74

[ 76](group__bindesc__define.md#ga5710e218f4f10e5049d039b17a376d0b)#define BINDESC\_ID\_BUILD\_TIME\_DAY 0xa02

77

[ 79](group__bindesc__define.md#gaeed1651e0d025ff74092a88b6d57e408)#define BINDESC\_ID\_BUILD\_TIME\_HOUR 0xa03

80

[ 82](group__bindesc__define.md#ga67f679968aeea5517e02da6e5e67d73e)#define BINDESC\_ID\_BUILD\_TIME\_MINUTE 0xa04

83

[ 85](group__bindesc__define.md#gacdff70f58c8098e23611327c1264a7dd)#define BINDESC\_ID\_BUILD\_TIME\_SECOND 0xa05

86

[ 88](group__bindesc__define.md#gab0eefe2d83294d6ebe4ca6299f05d785)#define BINDESC\_ID\_BUILD\_TIME\_UNIX 0xa06

89

[ 91](group__bindesc__define.md#gad8803e832ed0a42fd7033e277f8d8362)#define BINDESC\_ID\_BUILD\_DATE\_TIME\_STRING 0xa07

92

[ 94](group__bindesc__define.md#ga8bf6d98fb9495f2cca6b0403dffd0752)#define BINDESC\_ID\_BUILD\_DATE\_STRING 0xa08

95

[ 97](group__bindesc__define.md#gac4f75b876a81072e14bb39e3fb1c1f8a)#define BINDESC\_ID\_BUILD\_TIME\_STRING 0xa09

98

[ 100](group__bindesc__define.md#ga4cc66094d33709d9738b49e181a6eec3)#define BINDESC\_ID\_HOST\_NAME 0xb00

101

[ 103](group__bindesc__define.md#ga51b3fdd47d3dd94101134523c4dca144)#define BINDESC\_ID\_C\_COMPILER\_NAME 0xb01

104

[ 106](group__bindesc__define.md#gac4c6c9576b31cb2c26b085537648552b)#define BINDESC\_ID\_C\_COMPILER\_VERSION 0xb02

107

[ 109](group__bindesc__define.md#ga6f198590afdb2524b587e0194598b8eb)#define BINDESC\_ID\_CXX\_COMPILER\_NAME 0xb03

110

[ 112](group__bindesc__define.md#ga7ec0430daae1f99bdeeae6a636a263d8)#define BINDESC\_ID\_CXX\_COMPILER\_VERSION 0xb04

113

[ 114](group__bindesc__define.md#gac12b3cbf6d132fb54bbf702fd581373f)#define BINDESC\_TAG\_DESCRIPTORS\_END BINDESC\_TAG(DESCRIPTORS\_END, 0x0fff)

115

119

120/\*

121 \* Utility macro to generate a tag from a type and an ID

122 \*

123 \* type - Type of the descriptor, UINT, STR or BYTES

124 \* id - Unique ID for the descriptor, must fit in 12 bits

125 \*/

126#define BINDESC\_TAG(type, id) ((BINDESC\_TYPE\_##type & 0xf) << 12 | (id & 0x0fff))

127

131

132#if !defined(\_LINKER)

133

134#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

135

139

140/\*

141 \* Utility macro to get the name of a bindesc entry

142 \*/

143#define BINDESC\_NAME(name) bindesc\_entry\_##name

144

145/\* Convenience helper for declaring a binary descriptor entry. \*/

146#define \_\_BINDESC\_ENTRY\_DEFINE(name) \

147 \_\_aligned(BINDESC\_ALIGNMENT) const struct bindesc\_entry BINDESC\_NAME(name) \

148 \_\_in\_section(\_bindesc\_entry, static, name) \_\_used \_\_noasan

149

153

168#define BINDESC\_STR\_DEFINE(name, id, value) \

169 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

170 .tag = BINDESC\_TAG(STR, id), \

171 .len = (uint16\_t)sizeof(value), \

172 .data = value, \

173 }

174

189#define BINDESC\_UINT\_DEFINE(name, id, value) \

190 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

191 .tag = BINDESC\_TAG(UINT, id), \

192 .len = (uint16\_t)sizeof(uint32\_t), \

193 .data = sys\_uint32\_to\_array(value), \

194 }

195

214#define BINDESC\_BYTES\_DEFINE(name, id, value) \

215 \_\_BINDESC\_ENTRY\_DEFINE(name) = { \

216 .tag = BINDESC\_TAG(BYTES, id), \

217 .len = (uint16\_t)sizeof((uint8\_t [])\_\_DEBRACKET value), \

218 .data = \_\_DEBRACKET value, \

219 }

220

230#define BINDESC\_GET\_STR(name) BINDESC\_NAME(name).data

231

241#define BINDESC\_GET\_UINT(name) \*(uint32\_t \*)&(BINDESC\_NAME(name).data)

242

255#define BINDESC\_GET\_BYTES(name) BINDESC\_NAME(name).data

256

266#define BINDESC\_GET\_SIZE(name) BINDESC\_NAME(name).len

267

268/\*

269 \* An entry of the binary descriptor header. Each descriptor is

270 \* described by one of these entries.

271 \*/

272struct bindesc\_entry {

274 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag;

276 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len;

278 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[];

279} \_\_packed;

280

281/\*

282 \* We're assuming that `struct bindesc\_entry` has a specific layout in

283 \* memory, so it's worth making sure that the layout is really what we

284 \* think it is. If these assertions fail for your toolchain/platform,

285 \* please open a bug report.

286 \*/

287BUILD\_ASSERT(offsetof(struct bindesc\_entry, tag) == 0, "Incorrect memory layout");

288BUILD\_ASSERT(offsetof(struct bindesc\_entry, len) == 2, "Incorrect memory layout");

289BUILD\_ASSERT(offsetof(struct bindesc\_entry, data) == 4, "Incorrect memory layout");

290

291#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_STRING)

292extern const struct bindesc\_entry BINDESC\_NAME(kernel\_version\_string);

293#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_STRING) \*/

294

295#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_MAJOR)

296extern const struct bindesc\_entry BINDESC\_NAME(kernel\_version\_major);

297#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_MAJOR) \*/

298

299#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_MINOR)

300extern const struct bindesc\_entry BINDESC\_NAME(kernel\_version\_minor);

301#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_MINOR) \*/

302

303#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_PATCHLEVEL)

304extern const struct bindesc\_entry BINDESC\_NAME(kernel\_version\_patchlevel);

305#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_PATCHLEVEL) \*/

306

307#if defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_NUMBER)

308extern const struct bindesc\_entry BINDESC\_NAME(kernel\_version\_number);

309#endif /\* defined(CONFIG\_BINDESC\_KERNEL\_VERSION\_NUMBER) \*/

310

311#if defined(CONFIG\_BINDESC\_APP\_VERSION\_STRING)

312extern const struct bindesc\_entry BINDESC\_NAME(app\_version\_string);

313#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_STRING) \*/

314

315#if defined(CONFIG\_BINDESC\_APP\_VERSION\_MAJOR)

316extern const struct bindesc\_entry BINDESC\_NAME(app\_version\_major);

317#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_MAJOR) \*/

318

319#if defined(CONFIG\_BINDESC\_APP\_VERSION\_MINOR)

320extern const struct bindesc\_entry BINDESC\_NAME(app\_version\_minor);

321#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_MINOR) \*/

322

323#if defined(CONFIG\_BINDESC\_APP\_VERSION\_PATCHLEVEL)

324extern const struct bindesc\_entry BINDESC\_NAME(app\_version\_patchlevel);

325#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_PATCHLEVEL) \*/

326

327#if defined(CONFIG\_BINDESC\_APP\_VERSION\_NUMBER)

328extern const struct bindesc\_entry BINDESC\_NAME(app\_version\_number);

329#endif /\* defined(CONFIG\_BINDESC\_APP\_VERSION\_NUMBER) \*/

330

331#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_YEAR)

332extern const struct bindesc\_entry BINDESC\_NAME(build\_time\_year);

333#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_YEAR) \*/

334

335#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_MONTH)

336extern const struct bindesc\_entry BINDESC\_NAME(build\_time\_month);

337#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_MONTH) \*/

338

339#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_DAY)

340extern const struct bindesc\_entry BINDESC\_NAME(build\_time\_day);

341#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_DAY) \*/

342

343#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_HOUR)

344extern const struct bindesc\_entry BINDESC\_NAME(build\_time\_hour);

345#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_HOUR) \*/

346

347#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_MINUTE)

348extern const struct bindesc\_entry BINDESC\_NAME(build\_time\_minute);

349#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_MINUTE) \*/

350

351#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_SECOND)

352extern const struct bindesc\_entry BINDESC\_NAME(build\_time\_second);

353#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_SECOND) \*/

354

355#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_UNIX)

356extern const struct bindesc\_entry BINDESC\_NAME(build\_time\_unix);

357#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_UNIX) \*/

358

359#if defined(CONFIG\_BINDESC\_BUILD\_DATE\_TIME\_STRING)

360extern const struct bindesc\_entry BINDESC\_NAME(build\_date\_time\_string);

361#endif /\* defined(CONFIG\_BINDESC\_BUILD\_DATE\_TIME\_STRING) \*/

362

363#if defined(CONFIG\_BINDESC\_BUILD\_DATE\_STRING)

364extern const struct bindesc\_entry BINDESC\_NAME(build\_date\_string);

365#endif /\* defined(CONFIG\_BINDESC\_BUILD\_DATE\_STRING) \*/

366

367#if defined(CONFIG\_BINDESC\_BUILD\_TIME\_STRING)

368extern const struct bindesc\_entry BINDESC\_NAME(build\_time\_string);

369#endif /\* defined(CONFIG\_BINDESC\_BUILD\_TIME\_STRING) \*/

370

371#if defined(CONFIG\_BINDESC\_HOST\_NAME)

372extern const struct bindesc\_entry BINDESC\_NAME(host\_name);

373#endif /\* defined(CONFIG\_BINDESC\_HOST\_NAME) \*/

374

375#if defined(CONFIG\_BINDESC\_C\_COMPILER\_NAME)

376extern const struct bindesc\_entry BINDESC\_NAME(c\_compiler\_name);

377#endif /\* defined(CONFIG\_BINDESC\_C\_COMPILER\_NAME) \*/

378

379#if defined(CONFIG\_BINDESC\_C\_COMPILER\_VERSION)

380extern const struct bindesc\_entry BINDESC\_NAME(c\_compiler\_version);

381#endif /\* defined(CONFIG\_BINDESC\_C\_COMPILER\_VERSION) \*/

382

383#if defined(CONFIG\_BINDESC\_CXX\_COMPILER\_NAME)

384extern const struct bindesc\_entry BINDESC\_NAME(cxx\_compiler\_name);

385#endif /\* defined(CONFIG\_BINDESC\_CXX\_COMPILER\_NAME) \*/

386

387#if defined(CONFIG\_BINDESC\_CXX\_COMPILER\_VERSION)

388extern const struct bindesc\_entry BINDESC\_NAME(cxx\_compiler\_version);

389#endif /\* defined(CONFIG\_BINDESC\_CXX\_COMPILER\_VERSION) \*/

390

391#endif /\* !defined(\_LINKER) \*/

392

396

397#ifdef \_\_cplusplus

398}

399#endif

400

401#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_BINDESC\_H\_ \*/

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bindesc.h](bindesc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
