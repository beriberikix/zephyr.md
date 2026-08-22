---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arm__mpu__v8_8h_source.html
original_path: doxygen/html/arm__mpu__v8_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu\_v8.h

[Go to the documentation of this file.](arm__mpu__v8_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited.

3 \* Copyright (c) 2018 Nordic Semiconductor ASA.

4 \* Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef \_ASMLANGUAGE

10

11/\* Convenience macros to represent the ARMv8-M-specific

12 \* configuration for memory access permission and

13 \* cache-ability attribution.

14 \*/

15#if defined(CONFIG\_AARCH32\_ARMV8\_R)

16#define MPU\_IR\_REGION\_Msk (0xFFU)

17#define MPU\_IR\_REGION\_Pos 8U

18/\* MPU RBAR Register attribute msk Definitions \*/

19#define MPU\_RBAR\_BASE\_Pos 6U

20#define MPU\_RBAR\_BASE\_Msk (0x3FFFFFFFFFFFFFFUL << MPU\_RBAR\_BASE\_Pos)

21#define MPU\_RBAR\_SH\_Pos 3U

22#define MPU\_RBAR\_SH\_Msk (0x3UL << MPU\_RBAR\_SH\_Pos)

23#define MPU\_RBAR\_AP\_Pos 1U

24#define MPU\_RBAR\_AP\_Msk (0x3UL << MPU\_RBAR\_AP\_Pos)

25/\* RBAR XN \*/

26#define MPU\_RBAR\_XN\_Pos 0U

27#define MPU\_RBAR\_XN\_Msk (0x1UL << MPU\_RBAR\_XN\_Pos)

28

29/\* MPU PLBAR Register Definitions \*/

30#define MPU\_RLAR\_LIMIT\_Pos 6U

31#define MPU\_RLAR\_LIMIT\_Msk (0x3FFFFFFFFFFFFFFUL << MPU\_RLAR\_LIMIT\_Pos)

32#define MPU\_RLAR\_AttrIndx\_Pos 1U

33#define MPU\_RLAR\_AttrIndx\_Msk (0x7UL << MPU\_RLAR\_AttrIndx\_Pos)

34#define MPU\_RLAR\_EN\_Msk (0x1UL)

35#else

36#include <cmsis\_core.h>

37#endif

38

39/\* Privileged No Access, Unprivileged No Access \*/

40/\*#define NO\_ACCESS 0x0 \*/

41/\*#define NO\_ACCESS\_Msk ((NO\_ACCESS << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk) \*/

42/\* Privileged No Access, Unprivileged No Access \*/

43/\*#define P\_NA\_U\_NA 0x0 \*/

44/\*#define P\_NA\_U\_NA\_Msk ((P\_NA\_U\_NA << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk) \*/

45/\* Privileged Read Write, Unprivileged No Access \*/

[ 46](arm__mpu__v8_8h.md#a6632f2c0eba4d5aee046a86258100215)#define P\_RW\_U\_NA 0x0

[ 47](arm__mpu__v8_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7)#define P\_RW\_U\_NA\_Msk ((P\_RW\_U\_NA << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

48/\* Privileged Read Write, Unprivileged Read Only \*/

49/\*#define P\_RW\_U\_RO 0x2 \*/

50/\*#define P\_RW\_U\_RO\_Msk ((P\_RW\_U\_RO << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)\*/

51/\* Privileged Read Write, Unprivileged Read Write \*/

[ 52](arm__mpu__v8_8h.md#a8faee650ae8cc79e1d3605f251c3df34)#define P\_RW\_U\_RW 0x1

[ 53](arm__mpu__v8_8h.md#adc9ba826d1bf9a013724b7a24e9535db)#define P\_RW\_U\_RW\_Msk ((P\_RW\_U\_RW << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

54/\* Privileged Read Write, Unprivileged Read Write \*/

[ 55](arm__mpu__v8_8h.md#a4da15c917ab4e26cd3e5e39dbec83000)#define FULL\_ACCESS 0x1

[ 56](arm__mpu__v8_8h.md#a1da8e3113a0446b3d2acbe78b4e40b0c)#define FULL\_ACCESS\_Msk ((FULL\_ACCESS << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

57/\* Privileged Read Only, Unprivileged No Access \*/

[ 58](arm__mpu__v8_8h.md#ad3012e82dde223bbe84c9e4d7c46e7fd)#define P\_RO\_U\_NA 0x2

[ 59](arm__mpu__v8_8h.md#aeec24407a5fffaf967a841a26ccf46ed)#define P\_RO\_U\_NA\_Msk ((P\_RO\_U\_NA << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

60/\* Privileged Read Only, Unprivileged Read Only \*/

[ 61](arm__mpu__v8_8h.md#a75fd88fb93da28e84017d4ba6fcb4211)#define P\_RO\_U\_RO 0x3

[ 62](arm__mpu__v8_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46)#define P\_RO\_U\_RO\_Msk ((P\_RO\_U\_RO << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

63/\* Privileged Read Only, Unprivileged Read Only \*/

[ 64](arm__mpu__v8_8h.md#a628642b04c07236ae1e986c248a79ae5)#define RO 0x3

[ 65](arm__mpu__v8_8h.md#a35e3f724856c6947c52885def2e3c0d6)#define RO\_Msk ((RO << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

66

67/\* Attribute flag for not-allowing execution (eXecute Never) \*/

[ 68](arm__mpu__v8_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)#define NOT\_EXEC MPU\_RBAR\_XN\_Msk

69

70/\* To prevent execution of MPU region in privileged mode \*/

[ 71](arm__mpu__v8_8h.md#a9c5f045bd671e1161b6662440b49d479)#define PRIV\_EXEC\_NEVER (1)

72

73/\* Attribute flags for share-ability \*/

[ 74](arm__mpu__v8_8h.md#ad2047a4b8dae13c488a331b1691000b5)#define NON\_SHAREABLE 0x0

[ 75](arm__mpu__v8_8h.md#a5c302dfed348f344a036701d4b9c7ec8)#define NON\_SHAREABLE\_Msk ((NON\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

[ 76](arm__mpu__v8_8h.md#a6d48175f63f47fcbe1fedbbdfcd56a85)#define OUTER\_SHAREABLE 0x2

[ 77](arm__mpu__v8_8h.md#aa4f924c424fc141ffa32a9b5c1180d56)#define OUTER\_SHAREABLE\_Msk ((OUTER\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

[ 78](arm__mpu__v8_8h.md#a8c245b5c485b439790459255fc645131)#define INNER\_SHAREABLE 0x3

[ 79](arm__mpu__v8_8h.md#ab0d195350222b02d2d83ecd94a9ca395)#define INNER\_SHAREABLE\_Msk ((INNER\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

80

81/\* Helper define to calculate the region limit address. \*/

[ 82](arm__mpu__v8_8h.md#adc21e54d67b5ad7688c15784e8b0459c)#define REGION\_LIMIT\_ADDR(base, size) (((base & MPU\_RBAR\_BASE\_Msk) + size - 1) & MPU\_RLAR\_LIMIT\_Msk)

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

125 ((NORMAL\_O\_WT\_NT | (R\_ALLOC\_W\_NON << 4)) | (NORMAL\_I\_WT\_NT | R\_ALLOC\_W\_NON))

126

[ 127](arm__mpu__v8_8h.md#ad99764b02ad6122b1a952d0f4e79c37f)#define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS \

128 ((NORMAL\_O\_WB\_NT | (R\_ALLOC\_W\_ALLOC << 4)) | (NORMAL\_I\_WB\_NT | R\_ALLOC\_W\_ALLOC))

129

[ 130](arm__mpu__v8_8h.md#a45568f5e60950fbdb89b6e837b87aaac)#define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE \

131 ((NORMAL\_O\_NON\_C | (R\_NON\_W\_NON << 4)) | (NORMAL\_I\_NON\_C | R\_NON\_W\_NON))

132

133/\* Common cache-ability configuration for Flash, SRAM regions \*/

[ 134](arm__mpu__v8_8h.md#acc7f5f300029c52f64a585be8c18876b)#define MPU\_CACHE\_ATTRIBUTES\_FLASH NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS

135/\* clang-format off \*/

[ 136](arm__mpu__v8_8h.md#aaf4cfc11f9981eac67ea432c18edc384)#define MPU\_CACHE\_ATTRIBUTES\_SRAM \

137 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS

138/\* clang-format on \*/

[ 139](arm__mpu__v8_8h.md#a9637e9763b6b09741be5589eeceb3873)#define MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE NORMAL\_OUTER\_INNER\_NON\_CACHEABLE

140

141/\* Global MAIR configurations \*/

[ 142](arm__mpu__v8_8h.md#ad384c906ae7e1f4841c8ea98754acc1c)#define MPU\_MAIR\_ATTR\_FLASH MPU\_CACHE\_ATTRIBUTES\_FLASH

[ 143](arm__mpu__v8_8h.md#ab1521fd2deea0bd6b88c73aed7159f8a)#define MPU\_MAIR\_INDEX\_FLASH 0

[ 144](arm__mpu__v8_8h.md#aca50d2bc85d65c0ad231ecd7deb40c50)#define MPU\_MAIR\_ATTR\_SRAM MPU\_CACHE\_ATTRIBUTES\_SRAM

[ 145](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03)#define MPU\_MAIR\_INDEX\_SRAM 1

[ 146](arm__mpu__v8_8h.md#ab6bce12dbd72d216cbb6bc748d801ce0)#define MPU\_MAIR\_ATTR\_SRAM\_NOCACHE MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE

[ 147](arm__mpu__v8_8h.md#a03e37d7769647008655338fe8359d946)#define MPU\_MAIR\_INDEX\_SRAM\_NOCACHE 2

[ 148](arm__mpu__v8_8h.md#acfdb4baf0d7ec48fdc77e8e2973a1487)#define MPU\_MAIR\_ATTR\_DEVICE DEVICE\_nGnRnE

[ 149](arm__mpu__v8_8h.md#a6ae855ff0c11d85dc72a1c45edaa7f75)#define MPU\_MAIR\_INDEX\_DEVICE 3

150/\* Flash region(s): Attribute-0

151 \* SRAM region(s): Attribute-1

152 \* SRAM no cache-able regions(s): Attribute-2

153 \* DEVICE no cache-able regions(s): Attribute-3

154 \*/

[ 155](arm__mpu__v8_8h.md#a497d0db2bf062be1a466a1c7cab6a260)#define MPU\_MAIR\_ATTRS \

156 ((MPU\_MAIR\_ATTR\_FLASH << (MPU\_MAIR\_INDEX\_FLASH \* 8)) | \

157 (MPU\_MAIR\_ATTR\_SRAM << (MPU\_MAIR\_INDEX\_SRAM \* 8)) | \

158 (MPU\_MAIR\_ATTR\_SRAM\_NOCACHE << (MPU\_MAIR\_INDEX\_SRAM\_NOCACHE \* 8)) | \

159 (MPU\_MAIR\_ATTR\_DEVICE << (MPU\_MAIR\_INDEX\_DEVICE \* 8)))

160

161/\* Some helper defines for common regions.

162 \*

163 \* Note that the ARMv8-M/R MPU architecture requires that the

164 \* enabled MPU regions are non-overlapping. Therefore, it is

165 \* recommended to use these helper defines only for configuring

166 \* fixed MPU regions at build-time (i.e. regions that are not

167 \* expected to be re-programmed or re-adjusted at run-time so

168 \* that they do not overlap with other MPU regions).

169 \*/

170#if defined(CONFIG\_AARCH32\_ARMV8\_R)

171

172#define ARM\_MPU\_REGION\_INIT(p\_name, p\_base, p\_size, p\_attr) \

173 { \

174 .name = p\_name, \

175 .base = p\_base, \

176 .attr = p\_attr(p\_base + p\_size), \

177 }

178

179#define REGION\_RAM\_ATTR(limit) \

180 { \

181 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

182 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

183 .r\_limit = limit - 1, /\* Region Limit \*/ \

184 }

185

186#define REGION\_RAM\_TEXT\_ATTR(limit) \

187 { \

188 .rbar = P\_RO\_U\_RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

189 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

190 .r\_limit = limit - 1, /\* Region Limit \*/ \

191 }

192

193#define REGION\_RAM\_RO\_ATTR(limit) \

194 { \

195 .rbar = NOT\_EXEC | P\_RO\_U\_RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

196 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

197 .r\_limit = limit - 1, /\* Region Limit \*/ \

198 }

199#define REGION\_RAM\_NOCACHE\_ATTR(limit) \

200 { \

201 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

202 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM\_NOCACHE, /\* Cache-ability \*/ \

203 .r\_limit = limit - 1, /\* Region Limit \*/ \

204 }

205#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

206/\* Note that the access permissions allow for un-privileged writes, contrary

207 \* to ARMv7-M where un-privileged code has Read-Only permissions.

208 \*/

209#define REGION\_FLASH\_ATTR(limit) \

210 { \

211 .rbar = P\_RW\_U\_RW\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

212 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, /\* Cache-ability \*/ \

213 .r\_limit = limit - 1, /\* Region Limit \*/ \

214 }

215#else /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

216#define REGION\_FLASH\_ATTR(limit) \

217 { \

218 .rbar = RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

219 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, /\* Cache-ability \*/ \

220 .r\_limit = limit - 1, /\* Region Limit \*/ \

221 }

222#endif /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

223

224#define REGION\_DEVICE\_ATTR(limit) \

225 { \

226 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

227 .mair\_idx = MPU\_MAIR\_INDEX\_DEVICE, /\* Cache-ability \*/ \

228 .r\_limit = limit - 1, /\* Region Limit \*/ \

229 }

230#else

231

[ 232](arm__mpu__v8_8h.md#a2ec2a5ebe99ddac405570be52bc3a728)#define ARM\_MPU\_REGION\_INIT(p\_name, p\_base, p\_size, p\_attr) \

233 { \

234 .name = p\_name, \

235 .base = p\_base, \

236 .attr = p\_attr(p\_base, p\_size), \

237 }

238

239/\* On Cortex-M, we can only set the XN bit when CONFIG\_XIP=y. When

240 \* CONFIG\_XIP=n, the entire image will be linked to SRAM, so we need to keep

241 \* the SRAM region XN bit clear or the application code will not be executable.

242 \*/

243/\* clang-format off \*/

[ 244](arm__mpu__v8_8h.md#a6017a9ca9983921e946771ea57dc4201)#define REGION\_RAM\_ATTR(base, size) \

245 { \

246 .rbar = IF\_ENABLED(CONFIG\_XIP, (NOT\_EXEC |)) P\_RW\_U\_NA\_Msk | \

247 NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

248 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

249 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

250 IF\_ENABLED(CONFIG\_ARM\_MPU\_PXN, (.pxn = !PRIV\_EXEC\_NEVER,)) \

251 }

252

253#if defined(CONFIG\_ARM\_MPU\_PXN)

254/\* Use this attr to define an MPU region in RAM that has code intended to be executed in

255 \* un-privileged mode but not in privileged mode.

256 \*/

257#define REGION\_RAM\_ATTR\_PXN(base, size) \

258 { \

259 .rbar = P\_RO\_U\_RO\_Msk | NON\_SHAREABLE\_Msk,/\* AP, XN, SH \*/ \

260 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

261 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

262 .pxn = PRIV\_EXEC\_NEVER, \

263 }

264#endif

265

[ 266](arm__mpu__v8_8h.md#a8b4189f8ce0221dc34b199f3961aaf66)#define REGION\_RAM\_NOCACHE\_ATTR(base, size) \

267 { \

268 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

269 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM\_NOCACHE, /\* Cache-ability \*/ \

270 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

271 IF\_ENABLED(CONFIG\_ARM\_MPU\_PXN, (.pxn = PRIV\_EXEC\_NEVER,)) \

272 }

273

274#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

275/\* Note that the access permissions allow for un-privileged writes, contrary

276 \* to ARMv7-M where un-privileged code has Read-Only permissions.

277 \*/

278#define REGION\_FLASH\_ATTR(base, size) \

279 { \

280 .rbar = P\_RW\_U\_RW\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

281 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, /\* Cache-ability \*/ \

282 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

283 IF\_ENABLED(CONFIG\_ARM\_MPU\_PXN, (.pxn = !PRIV\_EXEC\_NEVER,)) \

284 }

285

286#else /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

[ 287](arm__mpu__v8_8h.md#a0293a2955ef2b9772d2ef4e1aaf9b24c)#define REGION\_FLASH\_ATTR(base, size) \

288 { \

289 .rbar = RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

290 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, /\* Cache-ability \*/ \

291 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

292 IF\_ENABLED(CONFIG\_ARM\_MPU\_PXN, (.pxn = !PRIV\_EXEC\_NEVER,)) \

293 }

294

295#endif /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

296

[ 297](arm__mpu__v8_8h.md#a3d1bfca872cb0bc3a4e010c3e518ce91)#define REGION\_DEVICE\_ATTR(base, size) \

298 { \

299 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

300 .mair\_idx = MPU\_MAIR\_INDEX\_DEVICE, /\* Cache-ability \*/ \

301 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

302 IF\_ENABLED(CONFIG\_ARM\_MPU\_PXN, (.pxn = PRIV\_EXEC\_NEVER,)) \

303 }

304

305/\* clang-format on \*/

306#endif

307

308struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) {

309 /\* Attributes belonging to RBAR \*/

[ 310](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rbar](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a): 5;

311 /\* MAIR index for attribute indirection \*/

[ 312](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mair\_idx](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e): 3;

313 /\* Region Limit Address value to be written to the RLAR register. \*/

[ 314](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r\_limit](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37);

315#ifdef CONFIG\_ARM\_MPU\_PXN

316 /\* To prevent execution of MPU region in privileged mode (Privileged Execute Never) \*/

317 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pxn;

318#endif

319};

320

321typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) [arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6);

322

323/\* Typedef for the k\_mem\_partition attribute \*/

324typedef struct {

[ 325](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rbar](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f);

[ 326](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mair\_idx](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c);

327#ifdef CONFIG\_ARM\_MPU\_PXN

328 /\* To prevent execution of MPU region in privileged mode (Privileged Execute Never) \*/

329 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pxn;

330#endif

331} [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

332

333/\* Kernel macros for memory attribution

334 \* (access permissions and cache-ability).

335 \*

336 \* The macros are to be stored in k\_mem\_partition\_attr\_t

337 \* objects. The format of a k\_mem\_partition\_attr\_t object

338 \* is as follows: field <rbar> contains a direct mapping

339 \* of the <XN> and <AP> bit-fields of the RBAR register;

340 \* field <mair\_idx> contains a direct mapping of AttrIdx

341 \* bit-field, stored in RLAR register.

342 \*/

343

344/\* Read-Write access permission attributes \*/

[ 345](arm__mpu__v8_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW \

346 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_RW\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 347](arm__mpu__v8_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA \

348 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_NA\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 349](arm__mpu__v8_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO \

350 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 351](arm__mpu__v8_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA \

352 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_NA\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

353

354/\* Execution-allowed attributes \*/

[ 355](arm__mpu__v8_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_RW\_Msk), MPU\_MAIR\_INDEX\_SRAM})

[ 356](arm__mpu__v8_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk), MPU\_MAIR\_INDEX\_SRAM})

357

358#ifdef CONFIG\_ARM\_MPU\_PXN

359#define K\_MEM\_PARTITION\_P\_R\_U\_RX \

360 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk), MPU\_MAIR\_INDEX\_SRAM, PRIV\_EXEC\_NEVER})

361#endif

362

363/\*

364 \* @brief Evaluate Write-ability

365 \*

366 \* Evaluate whether the access permissions include write-ability.

367 \*

368 \* @param attr The k\_mem\_partition\_attr\_t object holding the

369 \* MPU attributes to be checked against write-ability.

370 \*/

[ 371](arm__mpu__v8_8h.md#a7879968909ce2f0e33763ae1e2fc9d84)#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) \

372 ({ \

373 int \_\_is\_writable\_\_; \

374 switch (attr.rbar & MPU\_RBAR\_AP\_Msk) { \

375 case P\_RW\_U\_RW\_Msk: \

376 case P\_RW\_U\_NA\_Msk: \

377 \_\_is\_writable\_\_ = 1; \

378 break; \

379 default: \

380 \_\_is\_writable\_\_ = 0; \

381 } \

382 \_\_is\_writable\_\_; \

383 })

384

385/\*

386 \* @brief Evaluate Execution allowance

387 \*

388 \* Evaluate whether the access permissions include execution.

389 \*

390 \* @param attr The k\_mem\_partition\_attr\_t object holding the

391 \* MPU attributes to be checked against execution

392 \* allowance.

393 \*/

[ 394](arm__mpu__v8_8h.md#ab6fb9b9c6c1c968a11ae80bfd70fec26)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) (!((attr.rbar) & (NOT\_EXEC)))

395

396/\* Attributes for no-cache enabling (share-ability is selected by default) \*/

397

398/\* Read-Write access permission attributes \*/

[ 399](arm__mpu__v8_8h.md#afb811f7933ed0147b255c170427e0fb6)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE \

400 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_RW\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

401 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 402](arm__mpu__v8_8h.md#a8c982ab9a12ea1da0b7505c915832e89)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE \

403 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_NA\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

404 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 405](arm__mpu__v8_8h.md#a840d782e977d03ed4f9ca5858f61d1a5)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE \

406 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

407 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 408](arm__mpu__v8_8h.md#ae47c158f93de002298e0c46a47c6337e)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE \

409 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_NA\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

410 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

411

412/\* Execution-allowed attributes \*/

[ 413](arm__mpu__v8_8h.md#a5bcd5603dda3c2825a0eca8a7d994d83)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE \

414 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_RW\_Msk | OUTER\_SHAREABLE\_Msk), \

415 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 416](arm__mpu__v8_8h.md#a0b22795be27057cc03e6f49d1e1e455d)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE \

417 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk | OUTER\_SHAREABLE\_Msk), \

418 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

419

420#endif /\* \_ASMLANGUAGE \*/

421

422

423/\* Some compilers do not handle casts on pointers in constant expressions \*/

424#if defined(\_\_IAR\_SYSTEMS\_ICC\_\_)

425#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

426 BUILD\_ASSERT( \

427 (size > 0) && \

428 ((size) % CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0), \

429 "The start and size of the partition must align with the minimum MPU " \

430 "region size.")

431#else

432#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

433 BUILD\_ASSERT((size > 0) && \

434 ((uint32\_t)start % CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0U) && \

435 ((size) % CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0), \

436 "The start and size of the partition must align with the minimum MPU " \

437 "region size.")

438#endif /\* defined(\_\_IAR\_SYSTEMS\_ICC\_\_) \*/

[arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6)

struct arm\_mpu\_region\_attr arm\_mpu\_region\_attr\_t

**Definition** arm\_mpu\_v7m.h:139

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

**Definition** arm\_mpu\_v7m.h:134

[arm\_mpu\_region\_attr::rbar](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a)

uint8\_t rbar

**Definition** arm\_mpu\_v8.h:310

[arm\_mpu\_region\_attr::r\_limit](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37)

uint32\_t r\_limit

**Definition** arm\_mpu\_v8.h:314

[arm\_mpu\_region\_attr::mair\_idx](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e)

uint8\_t mair\_idx

**Definition** arm\_mpu\_v8.h:312

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:142

[k\_mem\_partition\_attr\_t::rbar](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f)

uint16\_t rbar

**Definition** arm\_mpu\_v8.h:325

[k\_mem\_partition\_attr\_t::mair\_idx](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c)

uint16\_t mair\_idx

**Definition** arm\_mpu\_v8.h:326

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [arm\_mpu\_v8.h](arm__mpu__v8_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
