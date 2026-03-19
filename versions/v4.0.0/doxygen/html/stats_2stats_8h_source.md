---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stats_2stats_8h_source.html
original_path: doxygen/html/stats_2stats_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stats.h

[Go to the documentation of this file.](stats_2stats_8h.md)

1/\*

2 \* Copyright Runtime.io 2018. All rights reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

50

51#ifndef ZEPHYR\_INCLUDE\_STATS\_STATS\_H\_

52#define ZEPHYR\_INCLUDE\_STATS\_STATS\_H\_

53

54#include <stddef.h>

55#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

56

57#ifdef \_\_cplusplus

58extern "C" {

59#endif

60

[ 61](structstats__name__map.md)struct [stats\_name\_map](structstats__name__map.md) {

[ 62](structstats__name__map.md#aa7f6799c19e062f267d5061bcd9eb420) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [snm\_off](structstats__name__map.md#aa7f6799c19e062f267d5061bcd9eb420);

[ 63](structstats__name__map.md#a653bd2d04cf979badf4d4bebc18f5f05) const char \*[snm\_name](structstats__name__map.md#a653bd2d04cf979badf4d4bebc18f5f05);

64} \_\_attribute\_\_((packed));

65

[ 66](structstats__hdr.md)struct [stats\_hdr](structstats__hdr.md) {

[ 67](structstats__hdr.md#a4e26392d878aa388ff83f49acd6a537a) const char \*[s\_name](structstats__hdr.md#a4e26392d878aa388ff83f49acd6a537a);

[ 68](structstats__hdr.md#a0fd7b023184a4179a48fa51d86472ac6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [s\_size](structstats__hdr.md#a0fd7b023184a4179a48fa51d86472ac6);

[ 69](structstats__hdr.md#a2fc8670c0d121afba4eedebc001a778a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [s\_cnt](structstats__hdr.md#a2fc8670c0d121afba4eedebc001a778a);

[ 70](structstats__hdr.md#a6587e670055d9ea2c0673a215bb424cf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [s\_pad1](structstats__hdr.md#a6587e670055d9ea2c0673a215bb424cf);

71#ifdef CONFIG\_STATS\_NAMES

72 const struct [stats\_name\_map](structstats__name__map.md) \*s\_map;

73 int s\_map\_cnt;

74#endif

[ 75](structstats__hdr.md#aeee657d6f963cee18ea0b96b620b8af7) struct [stats\_hdr](structstats__hdr.md) \*[s\_next](structstats__hdr.md#aeee657d6f963cee18ea0b96b620b8af7);

76};

77

[ 83](stats_2stats_8h.md#a21af7c98ccb9abb9464b9ef9358be880)#define STATS\_SECT\_DECL(group\_\_) \

84 struct stats\_ ## group\_\_

85

[ 89](stats_2stats_8h.md#a4124f8c0a9ffb78d8be608a780676785)#define STATS\_SECT\_END }

90

91/\* The following macros depend on whether CONFIG\_STATS is defined. If it is

92 \* not defined, then invocations of these macros get compiled out.

93 \*/

94#ifdef CONFIG\_STATS

95

101#define STATS\_SECT\_START(group\_\_) \

102 STATS\_SECT\_DECL(group\_\_) { \

103 struct stats\_hdr s\_hdr;

104

110#define STATS\_SECT\_ENTRY(var\_\_) uint32\_t var\_\_;

111

117#define STATS\_SECT\_ENTRY16(var\_\_) uint16\_t var\_\_;

118

124#define STATS\_SECT\_ENTRY32(var\_\_) uint32\_t var\_\_;

125

131#define STATS\_SECT\_ENTRY64(var\_\_) uint64\_t var\_\_;

132

143#define STATS\_INCN(group\_\_, var\_\_, n\_\_) \

144 ((group\_\_).var\_\_ += (n\_\_))

145

155#define STATS\_INC(group\_\_, var\_\_) \

156 STATS\_INCN(group\_\_, var\_\_, 1)

157

168#define STATS\_SET(group\_\_, var\_\_, n\_\_) \

169 ((group\_\_).var\_\_ = (n\_\_))

170

180#define STATS\_CLEAR(group\_\_, var\_\_) \

181 ((group\_\_).var\_\_ = 0)

182

183#define STATS\_SIZE\_16 (sizeof(uint16\_t))

184#define STATS\_SIZE\_32 (sizeof(uint32\_t))

185#define STATS\_SIZE\_64 (sizeof(uint64\_t))

186

187#define STATS\_SIZE\_INIT\_PARMS(group\_\_, size\_\_) \

188 (size\_\_), \

189 ((sizeof(group\_\_)) - sizeof(struct stats\_hdr)) / (size\_\_)

190

205#define STATS\_INIT\_AND\_REG(group\_\_, size\_\_, name\_\_) \

206 stats\_init\_and\_reg( \

207 &(group\_\_).s\_hdr, \

208 (size\_\_), \

209 (sizeof(group\_\_) - sizeof(struct stats\_hdr)) / (size\_\_), \

210 STATS\_NAME\_INIT\_PARMS(group\_\_), \

211 (name\_\_))

212

230void stats\_init(struct [stats\_hdr](structstats__hdr.md) \*shdr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cnt,

231 const struct [stats\_name\_map](structstats__name__map.md) \*map, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) map\_cnt);

232

245int stats\_register(const char \*name, struct [stats\_hdr](structstats__hdr.md) \*shdr);

246

271int stats\_init\_and\_reg(struct [stats\_hdr](structstats__hdr.md) \*hdr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cnt,

272 const struct [stats\_name\_map](structstats__name__map.md) \*map, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) map\_cnt,

273 const char \*name);

274

280void stats\_reset(struct [stats\_hdr](structstats__hdr.md) \*shdr);

281

294typedef int stats\_walk\_fn(struct [stats\_hdr](structstats__hdr.md) \*hdr, void \*arg,

295 const char \*name, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394));

296

307int stats\_walk(struct [stats\_hdr](structstats__hdr.md) \*hdr, stats\_walk\_fn \*walk\_cb, void \*arg);

308

318typedef int stats\_group\_walk\_fn(struct [stats\_hdr](structstats__hdr.md) \*hdr, void \*arg);

319

329int stats\_group\_walk(stats\_group\_walk\_fn \*walk\_cb, void \*arg);

330

340struct [stats\_hdr](structstats__hdr.md) \*stats\_group\_get\_next(const struct [stats\_hdr](structstats__hdr.md) \*cur);

341

350struct [stats\_hdr](structstats__hdr.md) \*stats\_group\_find(const char \*name);

351

352#else /\* CONFIG\_STATS \*/

353

[ 354](stats_2stats_8h.md#ae8e85c3ce2d901f4668d7237b19999fe)#define STATS\_SECT\_START(group\_\_) \

355 STATS\_SECT\_DECL(group\_\_) {

356

[ 357](stats_2stats_8h.md#afe8558503af10039b08a11f89c722783)#define STATS\_SECT\_ENTRY(var\_\_)

[ 358](stats_2stats_8h.md#a681ab1b4b39cb753e362eedbd78943a9)#define STATS\_SECT\_ENTRY16(var\_\_)

[ 359](stats_2stats_8h.md#a592329613cc77cfa5dee3e1d3b16dd93)#define STATS\_SECT\_ENTRY32(var\_\_)

[ 360](stats_2stats_8h.md#a589764c7a1e7d60fe0285b839c6c36b4)#define STATS\_SECT\_ENTRY64(var\_\_)

[ 361](stats_2stats_8h.md#ae0ec8d3d690545650c06db95bea1a9c7)#define STATS\_RESET(var\_\_)

[ 362](stats_2stats_8h.md#a9fdb886ee0a9b207a89ccd56a727f6b3)#define STATS\_SIZE\_INIT\_PARMS(group\_\_, size\_\_)

[ 363](stats_2stats_8h.md#ac5d5050e8684027a3efb5a8e7a830be6)#define STATS\_INCN(group\_\_, var\_\_, n\_\_)

[ 364](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)#define STATS\_INC(group\_\_, var\_\_)

[ 365](stats_2stats_8h.md#a106def612fe69b2d4cbc2e5c3e6f1993)#define STATS\_SET(group\_\_, var\_\_)

[ 366](stats_2stats_8h.md#a1cce9ba94338a7fb027c78b32e638da5)#define STATS\_CLEAR(group\_\_, var\_\_)

[ 367](stats_2stats_8h.md#a7a3f6d5dc044e6948998b8bc19efa493)#define STATS\_INIT\_AND\_REG(group\_\_, size\_\_, name\_\_) (0)

368

369#endif /\* !CONFIG\_STATS \*/

370

371#ifdef CONFIG\_STATS\_NAMES

372

373#define STATS\_NAME\_MAP\_NAME(sectname\_\_) stats\_map\_ ## sectname\_\_

374

375#define STATS\_NAME\_START(sectname\_\_) \

376 static const struct stats\_name\_map STATS\_NAME\_MAP\_NAME(sectname\_\_)[] = {

377

378#define STATS\_NAME(sectname\_\_, entry\_\_) \

379 { offsetof(STATS\_SECT\_DECL(sectname\_\_), entry\_\_), #entry\_\_ },

380

381#define STATS\_NAME\_END(sectname\_\_) }

382

383#define STATS\_NAME\_INIT\_PARMS(name\_\_) \

384 &(STATS\_NAME\_MAP\_NAME(name\_\_)[0]), \

385 (sizeof(STATS\_NAME\_MAP\_NAME(name\_\_)) / sizeof(struct stats\_name\_map))

386

387#else /\* CONFIG\_STATS\_NAMES \*/

388

[ 389](stats_2stats_8h.md#abd76143ad82eea7aded01af8cb7bc9ae)#define STATS\_NAME\_START(name\_\_)

[ 390](stats_2stats_8h.md#a30648b154e6da64aa39551fac123dd1b)#define STATS\_NAME(name\_\_, entry\_\_)

[ 391](stats_2stats_8h.md#a0de61377bb7c254b68cb39a9b5105e4f)#define STATS\_NAME\_END(name\_\_)

[ 392](stats_2stats_8h.md#ad1a94bded5ab34ac48c0dfd4cbdc168f)#define STATS\_NAME\_INIT\_PARMS(name\_\_) NULL, 0

393

394#endif /\* CONFIG\_STATS\_NAMES \*/

395

396#ifdef \_\_cplusplus

397}

398#endif

399

400#endif /\* ZEPHYR\_INCLUDE\_STATS\_STATS\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[stats\_hdr](structstats__hdr.md)

**Definition** stats.h:66

[stats\_hdr::s\_size](structstats__hdr.md#a0fd7b023184a4179a48fa51d86472ac6)

uint8\_t s\_size

**Definition** stats.h:68

[stats\_hdr::s\_cnt](structstats__hdr.md#a2fc8670c0d121afba4eedebc001a778a)

uint16\_t s\_cnt

**Definition** stats.h:69

[stats\_hdr::s\_name](structstats__hdr.md#a4e26392d878aa388ff83f49acd6a537a)

const char \* s\_name

**Definition** stats.h:67

[stats\_hdr::s\_pad1](structstats__hdr.md#a6587e670055d9ea2c0673a215bb424cf)

uint8\_t s\_pad1

**Definition** stats.h:70

[stats\_hdr::s\_next](structstats__hdr.md#aeee657d6f963cee18ea0b96b620b8af7)

struct stats\_hdr \* s\_next

**Definition** stats.h:75

[stats\_name\_map](structstats__name__map.md)

**Definition** stats.h:61

[stats\_name\_map::snm\_name](structstats__name__map.md#a653bd2d04cf979badf4d4bebc18f5f05)

const char \* snm\_name

**Definition** stats.h:63

[stats\_name\_map::snm\_off](structstats__name__map.md#aa7f6799c19e062f267d5061bcd9eb420)

uint16\_t snm\_off

**Definition** stats.h:62

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [stats](dir_5f661b5f7a66b36130669509de91835d.md)
- [stats.h](stats_2stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
