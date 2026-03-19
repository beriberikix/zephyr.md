---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm__mpu__v8_8h_source.html
original_path: doxygen/html/arm__mpu__v8_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 71](arm__mpu__v8_8h.md#a5c302dfed348f344a036701d4b9c7ec8)#define NON\_SHAREABLE\_Msk ((NON\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

[ 72](arm__mpu__v8_8h.md#a6d48175f63f47fcbe1fedbbdfcd56a85)#define OUTER\_SHAREABLE 0x2

[ 73](arm__mpu__v8_8h.md#aa4f924c424fc141ffa32a9b5c1180d56)#define OUTER\_SHAREABLE\_Msk ((OUTER\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

[ 74](arm__mpu__v8_8h.md#a8c245b5c485b439790459255fc645131)#define INNER\_SHAREABLE 0x3

[ 75](arm__mpu__v8_8h.md#ab0d195350222b02d2d83ecd94a9ca395)#define INNER\_SHAREABLE\_Msk ((INNER\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

76

77/\* Helper define to calculate the region limit address. \*/

[ 78](arm__mpu__v8_8h.md#adc21e54d67b5ad7688c15784e8b0459c)#define REGION\_LIMIT\_ADDR(base, size) (((base & MPU\_RBAR\_BASE\_Msk) + size - 1) & MPU\_RLAR\_LIMIT\_Msk)

79

80/\* Attribute flags for cache-ability \*/

81

82/\* Memory Attributes for Device Memory

83 \* 1.Gathering (G/nG)

84 \* Determines whether multiple accesses can be merged into a single

85 \* bus transaction.

86 \* nG: Number/size of accesses on the bus = number/size of accesses

87 \* in code.

88 \*

89 \* 2.Reordering (R/nR)

90 \* Determines whether accesses to the same device can be reordered.

91 \* nR: Accesses to the same IMPLEMENTATION DEFINED block size will

92 \* appear on the bus in program order.

93 \*

94 \* 3 Early Write Acknowledgment (E/nE)

95 \* Indicates to the memory system whether a buffer can send

96 \* acknowledgements.

97 \* nE: The response should come from the end slave, not buffering in

98 \* the interconnect.

99 \*/

[ 100](arm__mpu__v8_8h.md#a7e8d641f98b092387124bd1ecf2fdb53)#define DEVICE\_nGnRnE 0x0U

[ 101](arm__mpu__v8_8h.md#a1fb228a36a14d8679f6d038c47f5f2e1)#define DEVICE\_nGnRE 0x4U

[ 102](arm__mpu__v8_8h.md#a50d2ee15f01cc5379a74d23efd969051)#define DEVICE\_nGRE 0x8U

[ 103](arm__mpu__v8_8h.md#a3d0243c563668b7358ce29d54f7f1afa)#define DEVICE\_GRE 0xCU

104

105/\* Read/Write Allocation Configurations for Cacheable Memory \*/

[ 106](arm__mpu__v8_8h.md#a1160c997a66c9fd58dbc3dcfd65982a8)#define R\_NON\_W\_NON 0x0 /\* Do not allocate Read/Write \*/

[ 107](arm__mpu__v8_8h.md#a0696dfbe29563622fe76970f9d146ff5)#define R\_NON\_W\_ALLOC 0x1 /\* Do not allocate Read, Allocate Write \*/

[ 108](arm__mpu__v8_8h.md#a8476bb45227afc0236bc9f427793d6a9)#define R\_ALLOC\_W\_NON 0x2 /\* Allocate Read, Do not allocate Write \*/

[ 109](arm__mpu__v8_8h.md#a1815e3622467845af3b3083fa76f3314)#define R\_ALLOC\_W\_ALLOC 0x3 /\* Allocate Read/Write \*/

110

111/\* Memory Attributes for Normal Memory \*/

[ 112](arm__mpu__v8_8h.md#a4720c776e51ea52fc8cfa2c1dc935d47)#define NORMAL\_O\_WT\_NT 0x80 /\* Normal, Outer Write-through non-transient \*/

[ 113](arm__mpu__v8_8h.md#a7d87ec111ffd79cddb9ce9f23e9f20d9)#define NORMAL\_O\_WB\_NT 0xC0 /\* Normal, Outer Write-back non-transient \*/

[ 114](arm__mpu__v8_8h.md#ae36bc21dc922e88f8d5d4ff0657d80b6)#define NORMAL\_O\_NON\_C 0x40 /\* Normal, Outer Non-Cacheable \*/

115

[ 116](arm__mpu__v8_8h.md#a2d60ab7f15ac71d451a73758315eff07)#define NORMAL\_I\_WT\_NT 0x08 /\* Normal, Inner Write-through non-transient \*/

[ 117](arm__mpu__v8_8h.md#a28f31a1e2a47e2cafa7f41260780fd5f)#define NORMAL\_I\_WB\_NT 0x0C /\* Normal, Inner Write-back non-transient \*/

[ 118](arm__mpu__v8_8h.md#a8dda4d3d5f372f8ef3070fb492448992)#define NORMAL\_I\_NON\_C 0x04 /\* Normal, Inner Non-Cacheable \*/

119

[ 120](arm__mpu__v8_8h.md#a08d01129e0f1606f274cccd64c8560ef)#define NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS \

121 ((NORMAL\_O\_WT\_NT | (R\_ALLOC\_W\_NON << 4)) | (NORMAL\_I\_WT\_NT | R\_ALLOC\_W\_NON))

122

[ 123](arm__mpu__v8_8h.md#ad99764b02ad6122b1a952d0f4e79c37f)#define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS \

124 ((NORMAL\_O\_WB\_NT | (R\_ALLOC\_W\_ALLOC << 4)) | (NORMAL\_I\_WB\_NT | R\_ALLOC\_W\_ALLOC))

125

[ 126](arm__mpu__v8_8h.md#a45568f5e60950fbdb89b6e837b87aaac)#define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE \

127 ((NORMAL\_O\_NON\_C | (R\_NON\_W\_NON << 4)) | (NORMAL\_I\_NON\_C | R\_NON\_W\_NON))

128

129/\* Common cache-ability configuration for Flash, SRAM regions \*/

[ 130](arm__mpu__v8_8h.md#acc7f5f300029c52f64a585be8c18876b)#define MPU\_CACHE\_ATTRIBUTES\_FLASH NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS

131/\* clang-format off \*/

[ 132](arm__mpu__v8_8h.md#aaf4cfc11f9981eac67ea432c18edc384)#define MPU\_CACHE\_ATTRIBUTES\_SRAM \

133 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS

134/\* clang-format on \*/

[ 135](arm__mpu__v8_8h.md#a9637e9763b6b09741be5589eeceb3873)#define MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE NORMAL\_OUTER\_INNER\_NON\_CACHEABLE

136

137/\* Global MAIR configurations \*/

[ 138](arm__mpu__v8_8h.md#ad384c906ae7e1f4841c8ea98754acc1c)#define MPU\_MAIR\_ATTR\_FLASH MPU\_CACHE\_ATTRIBUTES\_FLASH

[ 139](arm__mpu__v8_8h.md#ab1521fd2deea0bd6b88c73aed7159f8a)#define MPU\_MAIR\_INDEX\_FLASH 0

[ 140](arm__mpu__v8_8h.md#aca50d2bc85d65c0ad231ecd7deb40c50)#define MPU\_MAIR\_ATTR\_SRAM MPU\_CACHE\_ATTRIBUTES\_SRAM

[ 141](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03)#define MPU\_MAIR\_INDEX\_SRAM 1

[ 142](arm__mpu__v8_8h.md#ab6bce12dbd72d216cbb6bc748d801ce0)#define MPU\_MAIR\_ATTR\_SRAM\_NOCACHE MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE

[ 143](arm__mpu__v8_8h.md#a03e37d7769647008655338fe8359d946)#define MPU\_MAIR\_INDEX\_SRAM\_NOCACHE 2

[ 144](arm__mpu__v8_8h.md#acfdb4baf0d7ec48fdc77e8e2973a1487)#define MPU\_MAIR\_ATTR\_DEVICE DEVICE\_nGnRnE

[ 145](arm__mpu__v8_8h.md#a6ae855ff0c11d85dc72a1c45edaa7f75)#define MPU\_MAIR\_INDEX\_DEVICE 3

146/\* Flash region(s): Attribute-0

147 \* SRAM region(s): Attribute-1

148 \* SRAM no cache-able regions(s): Attribute-2

149 \* DEVICE no cache-able regions(s): Attribute-3

150 \*/

[ 151](arm__mpu__v8_8h.md#a497d0db2bf062be1a466a1c7cab6a260)#define MPU\_MAIR\_ATTRS \

152 ((MPU\_MAIR\_ATTR\_FLASH << (MPU\_MAIR\_INDEX\_FLASH \* 8)) | \

153 (MPU\_MAIR\_ATTR\_SRAM << (MPU\_MAIR\_INDEX\_SRAM \* 8)) | \

154 (MPU\_MAIR\_ATTR\_SRAM\_NOCACHE << (MPU\_MAIR\_INDEX\_SRAM\_NOCACHE \* 8)) | \

155 (MPU\_MAIR\_ATTR\_DEVICE << (MPU\_MAIR\_INDEX\_DEVICE \* 8)))

156

157/\* Some helper defines for common regions.

158 \*

159 \* Note that the ARMv8-M/R MPU architecture requires that the

160 \* enabled MPU regions are non-overlapping. Therefore, it is

161 \* recommended to use these helper defines only for configuring

162 \* fixed MPU regions at build-time (i.e. regions that are not

163 \* expected to be re-programmed or re-adjusted at run-time so

164 \* that they do not overlap with other MPU regions).

165 \*/

166#if defined(CONFIG\_AARCH32\_ARMV8\_R)

167

168#define ARM\_MPU\_REGION\_INIT(p\_name, p\_base, p\_size, p\_attr) \

169 { \

170 .name = p\_name, \

171 .base = p\_base, \

172 .attr = p\_attr(p\_base + p\_size), \

173 }

174

175#define REGION\_RAM\_ATTR(limit) \

176 { \

177 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

178 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

179 .r\_limit = limit - 1, /\* Region Limit \*/ \

180 }

181

182#define REGION\_RAM\_TEXT\_ATTR(limit) \

183 { \

184 .rbar = P\_RO\_U\_RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

185 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

186 .r\_limit = limit - 1, /\* Region Limit \*/ \

187 }

188

189#define REGION\_RAM\_RO\_ATTR(limit) \

190 { \

191 .rbar = NOT\_EXEC | P\_RO\_U\_RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

192 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

193 .r\_limit = limit - 1, /\* Region Limit \*/ \

194 }

195#define REGION\_RAM\_NOCACHE\_ATTR(limit) \

196 { \

197 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

198 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM\_NOCACHE, /\* Cache-ability \*/ \

199 .r\_limit = limit - 1, /\* Region Limit \*/ \

200 }

201#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

202/\* Note that the access permissions allow for un-privileged writes, contrary

203 \* to ARMv7-M where un-privileged code has Read-Only permissions.

204 \*/

205#define REGION\_FLASH\_ATTR(limit) \

206 { \

207 .rbar = P\_RW\_U\_RW\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

208 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, /\* Cache-ability \*/ \

209 .r\_limit = limit - 1, /\* Region Limit \*/ \

210 }

211#else /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

212#define REGION\_FLASH\_ATTR(limit) \

213 { \

214 .rbar = RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

215 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, /\* Cache-ability \*/ \

216 .r\_limit = limit - 1, /\* Region Limit \*/ \

217 }

218#endif /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

219

220#define REGION\_DEVICE\_ATTR(limit) \

221 { \

222 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

223 .mair\_idx = MPU\_MAIR\_INDEX\_DEVICE, /\* Cache-ability \*/ \

224 .r\_limit = limit - 1, /\* Region Limit \*/ \

225 }

226#else

227

[ 228](arm__mpu__v8_8h.md#a2ec2a5ebe99ddac405570be52bc3a728)#define ARM\_MPU\_REGION\_INIT(p\_name, p\_base, p\_size, p\_attr) \

229 { \

230 .name = p\_name, \

231 .base = p\_base, \

232 .attr = p\_attr(p\_base, p\_size), \

233 }

234

235/\* On Cortex-M, we can only set the XN bit when CONFIG\_XIP=y. When

236 \* CONFIG\_XIP=n, the entire image will be linked to SRAM, so we need to keep

237 \* the SRAM region XN bit clear or the application code will not be executable.

238 \*/

239/\* clang-format off \*/

[ 240](arm__mpu__v8_8h.md#a6017a9ca9983921e946771ea57dc4201)#define REGION\_RAM\_ATTR(base, size) \

241 { \

242 .rbar = IF\_ENABLED(CONFIG\_XIP, (NOT\_EXEC |)) P\_RW\_U\_NA\_Msk | \

243 NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

244 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, /\* Cache-ability \*/ \

245 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

246 }

247/\* clang-format on \*/

248

[ 249](arm__mpu__v8_8h.md#a8b4189f8ce0221dc34b199f3961aaf66)#define REGION\_RAM\_NOCACHE\_ATTR(base, size) \

250 { \

251 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

252 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM\_NOCACHE, /\* Cache-ability \*/ \

253 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

254 }

255

256#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

257/\* Note that the access permissions allow for un-privileged writes, contrary

258 \* to ARMv7-M where un-privileged code has Read-Only permissions.

259 \*/

260#define REGION\_FLASH\_ATTR(base, size) \

261 { \

262 .rbar = P\_RW\_U\_RW\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

263 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, /\* Cache-ability \*/ \

264 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

265 }

266#else /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

[ 267](arm__mpu__v8_8h.md#a0293a2955ef2b9772d2ef4e1aaf9b24c)#define REGION\_FLASH\_ATTR(base, size) \

268 { \

269 .rbar = RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

270 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, /\* Cache-ability \*/ \

271 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

272 }

273#endif /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

274

[ 275](arm__mpu__v8_8h.md#a3d1bfca872cb0bc3a4e010c3e518ce91)#define REGION\_DEVICE\_ATTR(base, size) \

276 { \

277 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

278 .mair\_idx = MPU\_MAIR\_INDEX\_DEVICE, /\* Cache-ability \*/ \

279 .r\_limit = REGION\_LIMIT\_ADDR(base, size), /\* Region Limit \*/ \

280 }

281#endif

282

283struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) {

284 /\* Attributes belonging to RBAR \*/

[ 285](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rbar](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a): 5;

286 /\* MAIR index for attribute indirection \*/

[ 287](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mair\_idx](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e): 3;

288 /\* Region Limit Address value to be written to the RLAR register. \*/

[ 289](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [r\_limit](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37);

290};

291

292typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) [arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6);

293

294/\* Typedef for the k\_mem\_partition attribute \*/

295typedef struct {

[ 296](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rbar](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f);

[ 297](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mair\_idx](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c);

298} [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

299

300/\* Kernel macros for memory attribution

301 \* (access permissions and cache-ability).

302 \*

303 \* The macros are to be stored in k\_mem\_partition\_attr\_t

304 \* objects. The format of a k\_mem\_partition\_attr\_t object

305 \* is as follows: field <rbar> contains a direct mapping

306 \* of the <XN> and <AP> bit-fields of the RBAR register;

307 \* field <mair\_idx> contains a direct mapping of AttrIdx

308 \* bit-field, stored in RLAR register.

309 \*/

310

311/\* Read-Write access permission attributes \*/

[ 312](arm__mpu__v8_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW \

313 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_RW\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 314](arm__mpu__v8_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA \

315 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_NA\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 316](arm__mpu__v8_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO \

317 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

[ 318](arm__mpu__v8_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA \

319 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_NA\_Msk | NOT\_EXEC), MPU\_MAIR\_INDEX\_SRAM})

320

321/\* Execution-allowed attributes \*/

[ 322](arm__mpu__v8_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_RW\_Msk), MPU\_MAIR\_INDEX\_SRAM})

[ 323](arm__mpu__v8_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk), MPU\_MAIR\_INDEX\_SRAM})

324

325/\*

326 \* @brief Evaluate Write-ability

327 \*

328 \* Evaluate whether the access permissions include write-ability.

329 \*

330 \* @param attr The k\_mem\_partition\_attr\_t object holding the

331 \* MPU attributes to be checked against write-ability.

332 \*/

[ 333](arm__mpu__v8_8h.md#a7879968909ce2f0e33763ae1e2fc9d84)#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) \

334 ({ \

335 int \_\_is\_writable\_\_; \

336 switch (attr.rbar & MPU\_RBAR\_AP\_Msk) { \

337 case P\_RW\_U\_RW\_Msk: \

338 case P\_RW\_U\_NA\_Msk: \

339 \_\_is\_writable\_\_ = 1; \

340 break; \

341 default: \

342 \_\_is\_writable\_\_ = 0; \

343 } \

344 \_\_is\_writable\_\_; \

345 })

346

347/\*

348 \* @brief Evaluate Execution allowance

349 \*

350 \* Evaluate whether the access permissions include execution.

351 \*

352 \* @param attr The k\_mem\_partition\_attr\_t object holding the

353 \* MPU attributes to be checked against execution

354 \* allowance.

355 \*/

[ 356](arm__mpu__v8_8h.md#ab6fb9b9c6c1c968a11ae80bfd70fec26)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) (!((attr.rbar) & (NOT\_EXEC)))

357

358/\* Attributes for no-cache enabling (share-ability is selected by default) \*/

359

360/\* Read-Write access permission attributes \*/

[ 361](arm__mpu__v8_8h.md#afb811f7933ed0147b255c170427e0fb6)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE \

362 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_RW\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

363 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 364](arm__mpu__v8_8h.md#a8c982ab9a12ea1da0b7505c915832e89)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE \

365 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_NA\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

366 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 367](arm__mpu__v8_8h.md#a840d782e977d03ed4f9ca5858f61d1a5)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE \

368 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

369 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 370](arm__mpu__v8_8h.md#ae47c158f93de002298e0c46a47c6337e)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE \

371 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_NA\_Msk | NOT\_EXEC | OUTER\_SHAREABLE\_Msk), \

372 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

373

374/\* Execution-allowed attributes \*/

[ 375](arm__mpu__v8_8h.md#a5bcd5603dda3c2825a0eca8a7d994d83)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE \

376 ((k\_mem\_partition\_attr\_t){(P\_RW\_U\_RW\_Msk | OUTER\_SHAREABLE\_Msk), \

377 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

[ 378](arm__mpu__v8_8h.md#a0b22795be27057cc03e6f49d1e1e455d)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE \

379 ((k\_mem\_partition\_attr\_t){(P\_RO\_U\_RO\_Msk | OUTER\_SHAREABLE\_Msk), \

380 MPU\_MAIR\_INDEX\_SRAM\_NOCACHE})

381

382#endif /\* \_ASMLANGUAGE \*/

383

384#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

385 BUILD\_ASSERT((size > 0) && \

386 ((uint32\_t)start % CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0U) && \

387 ((size) % CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0), \

388 "The start and size of the partition must align with the minimum MPU " \

389 "region size.")

[arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6)

struct arm\_mpu\_region\_attr arm\_mpu\_region\_attr\_t

**Definition** arm\_mpu\_v7m.h:140

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

**Definition** arm\_mpu\_v7m.h:135

[arm\_mpu\_region\_attr::rbar](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a)

uint8\_t rbar

**Definition** arm\_mpu\_v8.h:285

[arm\_mpu\_region\_attr::r\_limit](structarm__mpu__region__attr.md#a77b05b42da47d398373dd747112def37)

uint32\_t r\_limit

**Definition** arm\_mpu\_v8.h:289

[arm\_mpu\_region\_attr::mair\_idx](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e)

uint8\_t mair\_idx

**Definition** arm\_mpu\_v8.h:287

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:143

[k\_mem\_partition\_attr\_t::rbar](structk__mem__partition__attr__t.md#a015f590fd186c7042386cbcce25b134f)

uint16\_t rbar

**Definition** arm\_mpu\_v8.h:296

[k\_mem\_partition\_attr\_t::mair\_idx](structk__mem__partition__attr__t.md#acf7bbe6773a1273b29df31618602ed3c)

uint16\_t mair\_idx

**Definition** arm\_mpu\_v8.h:297

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [arm\_mpu\_v8.h](arm__mpu__v8_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
