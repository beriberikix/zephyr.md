---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm__mpu__v8_8h_source.html
original_path: doxygen/html/arm__mpu__v8_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu\_v8.h

[Go to the documentation of this file.](arm__mpu__v8_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited.

3 \* Copyright (c) 2018 Nordic Semiconductor ASA.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef \_ASMLANGUAGE

9

10/\* Convenience macros to represent the ARMv8-M-specific

11 \* configuration for memory access permission and

12 \* cache-ability attribution.

13 \*/

14#if defined(CONFIG\_AARCH32\_ARMV8\_R)

15#define MPU\_IR\_REGION\_Msk (0xFFU)

16#define MPU\_IR\_REGION\_Pos 8U

17/\* MPU RBAR Register attribute msk Definitions \*/

18#define MPU\_RBAR\_BASE\_Pos 6U

19#define MPU\_RBAR\_BASE\_Msk (0x3FFFFFFFFFFFFFFUL << MPU\_RBAR\_BASE\_Pos)

20#define MPU\_RBAR\_SH\_Pos 3U

21#define MPU\_RBAR\_SH\_Msk (0x3UL << MPU\_RBAR\_SH\_Pos)

22#define MPU\_RBAR\_AP\_Pos 1U

23#define MPU\_RBAR\_AP\_Msk (0x3UL << MPU\_RBAR\_AP\_Pos)

24/\* RBAR XN \*/

25#define MPU\_RBAR\_XN\_Pos 0U

26#define MPU\_RBAR\_XN\_Msk (0x1UL << MPU\_RBAR\_XN\_Pos)

27

28/\* MPU PLBAR Register Definitions \*/

29#define MPU\_RLAR\_LIMIT\_Pos 6U

30#define MPU\_RLAR\_LIMIT\_Msk (0x3FFFFFFFFFFFFFFUL << MPU\_RLAR\_LIMIT\_Pos)

31#define MPU\_RLAR\_AttrIndx\_Pos 1U

32#define MPU\_RLAR\_AttrIndx\_Msk (0x7UL << MPU\_RLAR\_AttrIndx\_Pos)

33#define MPU\_RLAR\_EN\_Msk (0x1UL)

34#else

35#include <cmsis\_core.h>

36#endif

37

38/\* Privileged No Access, Unprivileged No Access \*/

39/\*#define NO\_ACCESS 0x0 \*/

40/\*#define NO\_ACCESS\_Msk ((NO\_ACCESS << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk) \*/

41/\* Privileged No Access, Unprivileged No Access \*/

42/\*#define P\_NA\_U\_NA 0x0 \*/

43/\*#define P\_NA\_U\_NA\_Msk ((P\_NA\_U\_NA << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk) \*/

44/\* Privileged Read Write, Unprivileged No Access \*/

[ 45](arm__mpu__v8_8h.md#a6632f2c0eba4d5aee046a86258100215)#define P\_RW\_U\_NA 0x0

[ 46](arm__mpu__v8_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7)#define P\_RW\_U\_NA\_Msk ((P\_RW\_U\_NA << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

47/\* Privileged Read Write, Unprivileged Read Only \*/

48/\*#define P\_RW\_U\_RO 0x2 \*/

49/\*#define P\_RW\_U\_RO\_Msk ((P\_RW\_U\_RO << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)\*/

50/\* Privileged Read Write, Unprivileged Read Write \*/

[ 51](arm__mpu__v8_8h.md#a8faee650ae8cc79e1d3605f251c3df34)#define P\_RW\_U\_RW 0x1

[ 52](arm__mpu__v8_8h.md#adc9ba826d1bf9a013724b7a24e9535db)#define P\_RW\_U\_RW\_Msk ((P\_RW\_U\_RW << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

53/\* Privileged Read Write, Unprivileged Read Write \*/

[ 54](arm__mpu__v8_8h.md#a4da15c917ab4e26cd3e5e39dbec83000)#define FULL\_ACCESS 0x1

[ 55](arm__mpu__v8_8h.md#a1da8e3113a0446b3d2acbe78b4e40b0c)#define FULL\_ACCESS\_Msk ((FULL\_ACCESS << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

56/\* Privileged Read Only, Unprivileged No Access \*/

[ 57](arm__mpu__v8_8h.md#ad3012e82dde223bbe84c9e4d7c46e7fd)#define P\_RO\_U\_NA 0x2

[ 58](arm__mpu__v8_8h.md#aeec24407a5fffaf967a841a26ccf46ed)#define P\_RO\_U\_NA\_Msk ((P\_RO\_U\_NA << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

59/\* Privileged Read Only, Unprivileged Read Only \*/

[ 60](arm__mpu__v8_8h.md#a75fd88fb93da28e84017d4ba6fcb4211)#define P\_RO\_U\_RO 0x3

[ 61](arm__mpu__v8_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46)#define P\_RO\_U\_RO\_Msk ((P\_RO\_U\_RO << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

62/\* Privileged Read Only, Unprivileged Read Only \*/

[ 63](arm__mpu__v8_8h.md#a628642b04c07236ae1e986c248a79ae5)#define RO 0x3

[ 64](arm__mpu__v8_8h.md#a35e3f724856c6947c52885def2e3c0d6)#define RO\_Msk ((RO << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

65

66/\* Attribute flag for not-allowing execution (eXecute Never) \*/

[ 67](arm__mpu__v8_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)#define NOT\_EXEC MPU\_RBAR\_XN\_Msk

68

69/\* Attribute flags for share-ability \*/

[ 70](arm__mpu__v8_8h.md#ad2047a4b8dae13c488a331b1691000b5)#define NON\_SHAREABLE 0x0

[ 71](arm__mpu__v8_8h.md#a5c302dfed348f344a036701d4b9c7ec8)#define NON\_SHAREABLE\_Msk \

72 ((NON\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

[ 73](arm__mpu__v8_8h.md#a6d48175f63f47fcbe1fedbbdfcd56a85)#define OUTER\_SHAREABLE 0x2

[ 74](arm__mpu__v8_8h.md#aa4f924c424fc141ffa32a9b5c1180d56)#define OUTER\_SHAREABLE\_Msk \

75 ((OUTER\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

[ 76](arm__mpu__v8_8h.md#a8c245b5c485b439790459255fc645131)#define INNER\_SHAREABLE 0x3

[ 77](arm__mpu__v8_8h.md#ab0d195350222b02d2d83ecd94a9ca395)#define INNER\_SHAREABLE\_Msk \

78 ((INNER\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

79

80/\* Helper define to calculate the region limit address. \*/

[ 81](arm__mpu__v8_8h.md#adc21e54d67b5ad7688c15784e8b0459c)#define REGION\_LIMIT\_ADDR(base, size) \

82 (((base & MPU\_RBAR\_BASE\_Msk) + size - 1) & MPU\_RLAR\_LIMIT\_Msk)

83

84/\* Attribute flags for cache-ability \*/

85

86/\* Memory Attributes for Device Memory

87 \* 1.Gathering (G/nG)

88 \* Determines whether multiple accesses can be merged into a single

89 \* bus transaction.

90 \* nG: Number/size of accesses on the bus = number/size of accesses

91 \* in code.

92 \*

93 \* 2.Reordering (R/nR)

94 \* Determines whether accesses to the same device can be reordered.

95 \* nR: Accesses to the same IMPLEMENTATION DEFINED block size will

96 \* appear on the bus in program order.

97 \*

98 \* 3 Early Write Acknowledgment (E/nE)

99 \* Indicates to the memory system whether a buffer can send

100 \* acknowledgements.

101 \* nE: The response should come from the end slave, not buffering in

102 \* the interconnect.

103 \*/

[ 104](arm__mpu__v8_8h.md#a7e8d641f98b092387124bd1ecf2fdb53)#define DEVICE\_nGnRnE 0x0U

[ 105](arm__mpu__v8_8h.md#a1fb228a36a14d8679f6d038c47f5f2e1)#define DEVICE\_nGnRE 0x4U

[ 106](arm__mpu__v8_8h.md#a50d2ee15f01cc5379a74d23efd969051)#define DEVICE\_nGRE 0x8U

[ 107](arm__mpu__v8_8h.md#a3d0243c563668b7358ce29d54f7f1afa)#define DEVICE\_GRE 0xCU

108

109/\* Read/Write Allocation Configurations for Cacheable Memory \*/

[ 110](arm__mpu__v8_8h.md#a1160c997a66c9fd58dbc3dcfd65982a8)#define R\_NON\_W\_NON 0x0 /\* Do not allocate Read/Write \*/

[ 111](arm__mpu__v8_8h.md#a0696dfbe29563622fe76970f9d146ff5)#define R\_NON\_W\_ALLOC 0x1 /\* Do not allocate Read, Allocate Write \*/

[ 112](arm__mpu__v8_8h.md#a8476bb45227afc0236bc9f427793d6a9)#define R\_ALLOC\_W\_NON 0x2 /\* Allocate Read, Do not allocate Write \*/

[ 113](arm__mpu__v8_8h.md#a1815e3622467845af3b3083fa76f3314)#define R\_ALLOC\_W\_ALLOC 0x3 /\* Allocate Read/Write \*/

114

115/\* Memory Attributes for Normal Memory \*/

[ 116](arm__mpu__v8_8h.md#a4720c776e51ea52fc8cfa2c1dc935d47)#define NORMAL\_O\_WT\_NT 0x80 /\* Normal, Outer Write-through non-transient \*/

[ 117](arm__mpu__v8_8h.md#a7d87ec111ffd79cddb9ce9f23e9f20d9)#define NORMAL\_O\_WB\_NT 0xC0 /\* Normal, Outer Write-back non-transient \*/

[ 118](arm__mpu__v8_8h.md#ae36bc21dc922e88f8d5d4ff0657d80b6)#define NORMAL\_O\_NON\_C 0x40 /\* Normal, Outer Non-Cacheable \*/

119

[ 120](arm__mpu__v8_8h.md#a2d60ab7f15ac71d451a73758315eff07)#define NORMAL\_I\_WT\_NT 0x08 /\* Normal, Inner Write-through non-transient \*/

[ 121](arm__mpu__v8_8h.md#a28f31a1e2a47e2cafa7f41260780fd5f)#define NORMAL\_I\_WB\_NT 0x0C /\* Normal, Inner Write-back non-transient \*/

[ 122](arm__mpu__v8_8h.md#a8dda4d3d5f372f8ef3070fb492448992)#define NORMAL\_I\_NON\_C 0x04 /\* Normal, Inner Non-Cacheable \*/

123

[ 124](arm__mpu__v8_8h.md#a08d01129e0f1606f274cccd64c8560ef)#define NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS \

125 ((NORMAL\_O\_WT\_NT | (R\_ALLOC\_W\_NON << 4)) \

126 | \

127 (NORMAL\_I\_WT\_NT | R\_ALLOC\_W\_NON)) \

128

[ 129](arm__mpu__v8_8h.md#ad99764b02ad6122b1a952d0f4e79c37f)#define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS \

130 ((NORMAL\_O\_WB\_NT | (R\_ALLOC\_W\_ALLOC << 4)) \

131 | \

132 (NORMAL\_I\_WB\_NT | R\_ALLOC\_W\_ALLOC))

133

[ 134](arm__mpu__v8_8h.md#a45568f5e60950fbdb89b6e837b87aaac)#define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE \

135 ((NORMAL\_O\_NON\_C | (R\_NON\_W\_NON << 4)) \

136 | \

137 (NORMAL\_I\_NON\_C | R\_NON\_W\_NON))

138

139/\* Common cache-ability configuration for Flash, SRAM regions \*/

[ 140](arm__mpu__v8_8h.md#acc7f5f300029c52f64a585be8c18876b)#define MPU\_CACHE\_ATTRIBUTES\_FLASH \

141 NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS

[ 142](arm__mpu__v8_8h.md#aaf4cfc11f9981eac67ea432c18edc384)#define MPU\_CACHE\_ATTRIBUTES\_SRAM \

143 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS

[ 144](arm__mpu__v8_8h.md#a9637e9763b6b09741be5589eeceb3873)#define MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE \

145 NORMAL\_OUTER\_INNER\_NON\_CACHEABLE

146

147/\* Global MAIR configurations \*/

[ 148](arm__mpu__v8_8h.md#ad384c906ae7e1f4841c8ea98754acc1c)#define MPU\_MAIR\_ATTR\_FLASH MPU\_CACHE\_ATTRIBUTES\_FLASH

[ 149](arm__mpu__v8_8h.md#ab1521fd2deea0bd6b88c73aed7159f8a)#define MPU\_MAIR\_INDEX\_FLASH 0

[ 150](arm__mpu__v8_8h.md#aca50d2bc85d65c0ad231ecd7deb40c50)#define MPU\_MAIR\_ATTR\_SRAM MPU\_CACHE\_ATTRIBUTES\_SRAM

[ 151](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03)#define MPU\_MAIR\_INDEX\_SRAM 1

[ 152](arm__mpu__v8_8h.md#ab6bce12dbd72d216cbb6bc748d801ce0)#define MPU\_MAIR\_ATTR\_SRAM\_NOCACHE MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE

[ 153](arm__mpu__v8_8h.md#a03e37d7769647008655338fe8359d946)#define MPU\_MAIR\_INDEX\_SRAM\_NOCACHE 2

[ 154](arm__mpu__v8_8h.md#acfdb4baf0d7ec48fdc77e8e2973a1487)#define MPU\_MAIR\_ATTR\_DEVICE DEVICE\_nGnRnE

[ 155](arm__mpu__v8_8h.md#a6ae855ff0c11d85dc72a1c45edaa7f75)#define MPU\_MAIR\_INDEX\_DEVICE 3

156/\* Flash region(s): Attribute-0

157 \* SRAM region(s): Attribute-1

158 \* SRAM no cache-able regions(s): Attribute-2

159 \* DEVICE no cache-able regions(s): Attribute-3

160 \*/

[ 161](arm__mpu__v8_8h.md#a497d0db2bf062be1a466a1c7cab6a260)#define MPU\_MAIR\_ATTRS \

162 ((MPU\_MAIR\_ATTR\_FLASH << (MPU\_MAIR\_INDEX\_FLASH \* 8)) | \

163 (MPU\_MAIR\_ATTR\_SRAM << (MPU\_MAIR\_INDEX\_SRAM \* 8)) | \

164 (MPU\_MAIR\_ATTR\_SRAM\_NOCACHE << (MPU\_MAIR\_INDEX\_SRAM\_NOCACHE \* 8)) | \

165 (MPU\_MAIR\_ATTR\_DEVICE << (MPU\_MAIR\_INDEX\_DEVICE \* 8)))

166

167/\* Some helper defines for common regions.

168 \*

169 \* Note that the ARMv8-M/R MPU architecture requires that the

170 \* enabled MPU regions are non-overlapping. Therefore, it is

171 \* recommended to use these helper defines only for configuring

172 \* fixed MPU regions at build-time (i.e. regions that are not

173 \* expected to be re-programmed or re-adjusted at run-time so

174 \* that they do not overlap with other MPU regions).

175 \*/

176#if defined(CONFIG\_AARCH32\_ARMV8\_R)

177

178#define ARM\_MPU\_REGION\_INIT(p\_name, p\_base, p\_size, p\_attr) \

179 { .name = p\_name, \

180 .base = p\_base, \

181 .attr = p\_attr(p\_base + p\_size), \

182 }

183

184#define REGION\_RAM\_ATTR(limit) \

185 { \

186 .rbar = NOT\_EXEC | \

187 P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

188 /\* Cache-ability \*/ \

189 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, \

190 .r\_limit = limit - 1, /\* Region Limit \*/ \

191 }

192

193#define REGION\_RAM\_TEXT\_ATTR(limit) \

194 { \

195 .rbar = P\_RO\_U\_RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

196 /\* Cache-ability \*/ \

197 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, \

198 .r\_limit = limit - 1, /\* Region Limit \*/ \

199 }

200

201#define REGION\_RAM\_RO\_ATTR(limit) \

202 { \

203 .rbar = NOT\_EXEC | \

204 P\_RO\_U\_RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

205 /\* Cache-ability \*/ \

206 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, \

207 .r\_limit = limit - 1, /\* Region Limit \*/ \

208 }

209#define REGION\_RAM\_NOCACHE\_ATTR(limit) \

210 { \

211 .rbar = NOT\_EXEC | \

212 P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

213 /\* Cache-ability \*/ \

214 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM\_NOCACHE, \

215 .r\_limit = limit - 1, /\* Region Limit \*/ \

216 }

217#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

218/\* Note that the access permissions allow for un-privileged writes, contrary

219 \* to ARMv7-M where un-privileged code has Read-Only permissions.

220 \*/

221#define REGION\_FLASH\_ATTR(limit) \

222 { \

223 .rbar = P\_RW\_U\_RW\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

224 /\* Cache-ability \*/ \

225 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, \

226 .r\_limit = limit - 1, /\* Region Limit \*/ \

227 }

228#else /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

229#define REGION\_FLASH\_ATTR(limit) \

230 { \

231 .rbar = RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

232 /\* Cache-ability \*/ \

233 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, \

234 .r\_limit = limit - 1, /\* Region Limit \*/ \

235 }

236#endif /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

237

238#define REGION\_DEVICE\_ATTR(limit) \

239 { \

240 /\* AP, XN, SH \*/ \

241 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, \

242 /\* Cache-ability \*/ \

243 .mair\_idx = MPU\_MAIR\_INDEX\_DEVICE, \

244 /\* Region Limit \*/ \

245 .r\_limit = limit - 1, \

246 }

247#else

248

[ 249](arm__mpu__v8_8h.md#a2ec2a5ebe99ddac405570be52bc3a728)#define ARM\_MPU\_REGION\_INIT(p\_name, p\_base, p\_size, p\_attr) \

250 { .name = p\_name, \

251 .base = p\_base, \

252 .attr = p\_attr(p\_base, p\_size), \

253 }

254

255/\* On Cortex-M, we can only set the XN bit when CONFIG\_XIP=y. When

256 \* CONFIG\_XIP=n, the entire image will be linked to SRAM, so we need to keep

257 \* the SRAM region XN bit clear or the application code will not be executable.

258 \*/

[ 259](arm__mpu__v8_8h.md#a6017a9ca9983921e946771ea57dc4201)#define REGION\_RAM\_ATTR(base, size) \

260 {\

261 .rbar = IF\_ENABLED(CONFIG\_XIP, (NOT\_EXEC |)) \

262 P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

263 /\* Cache-ability \*/ \

264 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, \

265 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

266 }

267

[ 268](arm__mpu__v8_8h.md#a8b4189f8ce0221dc34b199f3961aaf66)#define REGION\_RAM\_NOCACHE\_ATTR(base, size) \

269 {\

270 .rbar = NOT\_EXEC | \

271 P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

272 /\* Cache-ability \*/ \

273 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM\_NOCACHE, \

274 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

275 }

276

277#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

278/\* Note that the access permissions allow for un-privileged writes, contrary

279 \* to ARMv7-M where un-privileged code has Read-Only permissions.

280 \*/

281#define REGION\_FLASH\_ATTR(base, size) \

282 {\

283 .rbar = P\_RW\_U\_RW\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

284 /\* Cache-ability \*/ \

285 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, \

286 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

287 }

288#else /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

[ 289](arm__mpu__v8_8h.md#a0293a2955ef2b9772d2ef4e1aaf9b24c)#define REGION\_FLASH\_ATTR(base, size) \

290 {\

291 .rbar = RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

292 /\* Cache-ability \*/ \

293 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, \

294 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

295 }

296#endif /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

297

[ 298](arm__mpu__v8_8h.md#a3d1bfca872cb0bc3a4e010c3e518ce91)#define REGION\_DEVICE\_ATTR(base, size) \

299 { \

300 /\* AP, XN, SH \*/ \

301 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* Cache-ability \*/ \

302 .mair\_idx = MPU\_MAIR\_INDEX\_DEVICE, \

303 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

304 }

305#endif

306

307struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) {

308 /\* Attributes belonging to RBAR \*/

[ 309](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rbar](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a): 5;

310 /\* MAIR index for attribute indirection \*/

[ 311](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mair\_idx](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e): 3;

312 /\* Region Limit Address value to be written to the RLAR register. \*/

[ 313](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r\_limit](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37);

314};

315

316typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) [arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6);

317

318/\* Typedef for the k\_mem\_partition attribute \*/

319typedef struct {

[ 320](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rbar](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f);

[ 321](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mair\_idx](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c);

322} [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

323

324/\* Kernel macros for memory attribution

325 \* (access permissions and cache-ability).

326 \*

327 \* The macros are to be stored in k\_mem\_partition\_attr\_t

328 \* objects. The format of a k\_mem\_partition\_attr\_t object

329 \* is as follows: field <rbar> contains a direct mapping

330 \* of the <XN> and <AP> bit-fields of the RBAR register;

331 \* field <mair\_idx> contains a direct mapping of AttrIdx

332 \* bit-field, stored in RLAR register.

333 \*/

334

335/\* Read-Write access permission attributes \*/

[ 336](arm__mpu__v8_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW ((k\_mem\_partition\_attr\_t) \

337 {(P\_RW\_U\_RW\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 338](arm__mpu__v8_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA ((k\_mem\_partition\_attr\_t) \

339 {(P\_RW\_U\_NA\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 340](arm__mpu__v8_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO ((k\_mem\_partition\_attr\_t) \

341 {(P\_RO\_U\_RO\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 342](arm__mpu__v8_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA ((k\_mem\_partition\_attr\_t) \

343 {(P\_RO\_U\_NA\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

344

345/\* Execution-allowed attributes \*/

[ 346](arm__mpu__v8_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX ((k\_mem\_partition\_attr\_t) \

347 {(P\_RW\_U\_RW\_Msk), MPU\_MAIR\_INDEX\_SRAM})

[ 348](arm__mpu__v8_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t) \

349 {(P\_RO\_U\_RO\_Msk), MPU\_MAIR\_INDEX\_SRAM})

350

351/\*

352 \* @brief Evaluate Write-ability

353 \*

354 \* Evaluate whether the access permissions include write-ability.

355 \*

356 \* @param attr The k\_mem\_partition\_attr\_t object holding the

357 \* MPU attributes to be checked against write-ability.

358 \*/

[ 359](arm__mpu__v8_8h.md#a7879968909ce2f0e33763ae1e2fc9d84)#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) \

360 ({ \

361 int \_\_is\_writable\_\_; \

362 switch (attr.rbar & MPU\_RBAR\_AP\_Msk) { \

363 case P\_RW\_U\_RW\_Msk: \

364 case P\_RW\_U\_NA\_Msk: \

365 \_\_is\_writable\_\_ = 1; \

366 break; \

367 default: \

368 \_\_is\_writable\_\_ = 0; \

369 } \

370 \_\_is\_writable\_\_; \

371 })

372

373/\*

374 \* @brief Evaluate Execution allowance

375 \*

376 \* Evaluate whether the access permissions include execution.

377 \*

378 \* @param attr The k\_mem\_partition\_attr\_t object holding the

379 \* MPU attributes to be checked against execution

380 \* allowance.

381 \*/

[ 382](arm__mpu__v8_8h.md#ab6fb9b9c6c1c968a11ae80bfd70fec26)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) \

383 (!((attr.rbar) & (NOT\_EXEC)))

384

385/\* Attributes for no-cache enabling (share-ability is selected by default) \*/

386

387/\* Read-Write access permission attributes \*/

[ 388](arm__mpu__v8_8h.md#afb811f7933ed0147b255c170427e0fb6)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE ((k\_mem\_partition\_attr\_t) \

389 {(P\_RW\_U\_RW\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

390 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 391](arm__mpu__v8_8h.md#a8c982ab9a12ea1da0b7505c915832e89)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE ((k\_mem\_partition\_attr\_t) \

392 {(P\_RW\_U\_NA\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

393 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 394](arm__mpu__v8_8h.md#a840d782e977d03ed4f9ca5858f61d1a5)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE ((k\_mem\_partition\_attr\_t) \

395 {(P\_RO\_U\_RO\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

396 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 397](arm__mpu__v8_8h.md#ae47c158f93de002298e0c46a47c6337e)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE ((k\_mem\_partition\_attr\_t) \

398 {(P\_RO\_U\_NA\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

399 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

400

401/\* Execution-allowed attributes \*/

[ 402](arm__mpu__v8_8h.md#a5bcd5603dda3c2825a0eca8a7d994d83)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE ((k\_mem\_partition\_attr\_t) \

403 {(P\_RW\_U\_RW\_Msk | OUTER\_SHAREABLE\_Msk), MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 404](arm__mpu__v8_8h.md#a0b22795be27057cc03e6f49d1e1e455d)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE ((k\_mem\_partition\_attr\_t) \

405 {(P\_RO\_U\_RO\_Msk | OUTER\_SHAREABLE\_Msk), MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

406

407#endif /\* \_ASMLANGUAGE \*/

408

409#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

410 BUILD\_ASSERT((size > 0) && ((uint32\_t)start % \

411 CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0U) && \

412 ((size) % CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0), \

413 " the start and size of the partition must align " \

414 "with the minimum MPU region size.")

[arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6)

struct arm\_mpu\_region\_attr arm\_mpu\_region\_attr\_t

**Definition** arm\_mpu\_v7m.h:157

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[arm\_mpu\_region\_attr](structarm__mpu__region__attr.md)

**Definition** arm\_mpu\_v7m.h:152

[arm\_mpu\_region\_attr::rbar](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a)

uint8\_t rbar

**Definition** arm\_mpu\_v8.h:309

[arm\_mpu\_region\_attr::r\_limit](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37)

uint32\_t r\_limit

**Definition** arm\_mpu\_v8.h:313

[arm\_mpu\_region\_attr::mair\_idx](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e)

uint8\_t mair\_idx

**Definition** arm\_mpu\_v8.h:311

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[k\_mem\_partition\_attr\_t::rbar](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f)

uint16\_t rbar

**Definition** arm\_mpu\_v8.h:320

[k\_mem\_partition\_attr\_t::mair\_idx](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c)

uint16\_t mair\_idx

**Definition** arm\_mpu\_v8.h:321

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [arm\_mpu\_v8.h](arm__mpu__v8_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
