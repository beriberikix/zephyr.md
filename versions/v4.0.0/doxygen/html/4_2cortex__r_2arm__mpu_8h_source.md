---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/4_2cortex__r_2arm__mpu_8h_source.html
original_path: doxygen/html/4_2cortex__r_2arm__mpu_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu.h

[Go to the documentation of this file.](4_2cortex__r_2arm__mpu_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited.

3 \* Copyright (c) 2018 Nordic Semiconductor ASA.

4 \* Copyright (c) 2021-2023 Arm Limited (or its affiliates). All rights reserved.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CORTEX\_R\_MPU\_ARM\_MPU\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CORTEX\_R\_MPU\_ARM\_MPU\_H\_

10

11/\*

12 \* Convenience macros to represent the ARMv8-R64-specific configuration

13 \* for memory access permission and cache-ability attribution.

14 \*/

15/\* MPU MPUIR Register Definitions \*/

[ 16](4_2cortex__r_2arm__mpu_8h.md#a734d7c223353e973a104581b6e87d227)#define MPU\_IR\_REGION\_Msk (0xFFU)

17/\* MPU RBAR Register attribute msk Definitions \*/

[ 18](4_2cortex__r_2arm__mpu_8h.md#a73dbc6dcdf74ba9a411bc2670c17b7d0)#define MPU\_RBAR\_BASE\_Pos 6U

[ 19](4_2cortex__r_2arm__mpu_8h.md#a57f2217a12342e8e43c7ad6949a9a65b)#define MPU\_RBAR\_BASE\_Msk (0x3FFFFFFFFFFFFFFUL << MPU\_RBAR\_BASE\_Pos)

[ 20](4_2cortex__r_2arm__mpu_8h.md#a3150317eff21434c7ca4b24516603615)#define MPU\_RBAR\_SH\_Pos 4U

[ 21](4_2cortex__r_2arm__mpu_8h.md#aa014b1c92266313a3c1dc06e37e39aef)#define MPU\_RBAR\_SH\_Msk (0x3UL << MPU\_RBAR\_SH\_Pos)

[ 22](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)#define MPU\_RBAR\_AP\_Pos 2U

[ 23](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)#define MPU\_RBAR\_AP\_Msk (0x3UL << MPU\_RBAR\_AP\_Pos)

24/\* RBAR\_EL1 XN \*/

[ 25](4_2cortex__r_2arm__mpu_8h.md#a6db81ec93c662cb563f18ef61e4df669)#define MPU\_RBAR\_XN\_Pos 1U

[ 26](4_2cortex__r_2arm__mpu_8h.md#ae960690ad7849b21e6cd0c414075de1b)#define MPU\_RBAR\_XN\_Msk (0x1UL << MPU\_RBAR\_XN\_Pos)

27

28/\* MPU PLBAR\_ELx Register Definitions \*/

[ 29](4_2cortex__r_2arm__mpu_8h.md#a6e827ab46bc85f283867819889865a23)#define MPU\_RLAR\_LIMIT\_Pos 6U

[ 30](4_2cortex__r_2arm__mpu_8h.md#a9612abff664c827b36844fe42d8ee5cb)#define MPU\_RLAR\_LIMIT\_Msk (0x3FFFFFFFFFFFFFFUL << MPU\_RLAR\_LIMIT\_Pos)

[ 31](4_2cortex__r_2arm__mpu_8h.md#a467ebe320762d7d1067ffec939119bcd)#define MPU\_RLAR\_AttrIndx\_Pos 1U

[ 32](4_2cortex__r_2arm__mpu_8h.md#ab5ac20d186a58cc39a8d02a554d0868d)#define MPU\_RLAR\_AttrIndx\_Msk (0x7UL << MPU\_RLAR\_AttrIndx\_Pos)

[ 33](4_2cortex__r_2arm__mpu_8h.md#af1da1b8c76ac4a21ee44dbe8268073dd)#define MPU\_RLAR\_EN\_Msk (0x1UL)

34

35/\* PRBAR\_ELx: Attribute flag for not-allowing execution (eXecute Never) \*/

[ 36](4_2cortex__r_2arm__mpu_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)#define NOT\_EXEC MPU\_RBAR\_XN\_Msk /\* PRBAR\_EL1 \*/

37

38/\* PRBAR\_ELx: Attribute flag for access permissions \*/

39/\* Privileged Read Write, Unprivileged No Access \*/

[ 40](4_2cortex__r_2arm__mpu_8h.md#a6632f2c0eba4d5aee046a86258100215)#define P\_RW\_U\_NA 0x0U

[ 41](4_2cortex__r_2arm__mpu_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7)#define P\_RW\_U\_NA\_Msk ((P\_RW\_U\_NA << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

42/\* Privileged Read Write, Unprivileged Read Write \*/

[ 43](4_2cortex__r_2arm__mpu_8h.md#a8faee650ae8cc79e1d3605f251c3df34)#define P\_RW\_U\_RW 0x1U

[ 44](4_2cortex__r_2arm__mpu_8h.md#adc9ba826d1bf9a013724b7a24e9535db)#define P\_RW\_U\_RW\_Msk ((P\_RW\_U\_RW << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

45/\* Privileged Read Only, Unprivileged No Access \*/

[ 46](4_2cortex__r_2arm__mpu_8h.md#ad3012e82dde223bbe84c9e4d7c46e7fd)#define P\_RO\_U\_NA 0x2U

[ 47](4_2cortex__r_2arm__mpu_8h.md#aeec24407a5fffaf967a841a26ccf46ed)#define P\_RO\_U\_NA\_Msk ((P\_RO\_U\_NA << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

48/\* Privileged Read Only, Unprivileged Read Only \*/

[ 49](4_2cortex__r_2arm__mpu_8h.md#a75fd88fb93da28e84017d4ba6fcb4211)#define P\_RO\_U\_RO 0x3U

[ 50](4_2cortex__r_2arm__mpu_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46)#define P\_RO\_U\_RO\_Msk ((P\_RO\_U\_RO << MPU\_RBAR\_AP\_Pos) & MPU\_RBAR\_AP\_Msk)

51

52/\* PRBAR\_ELx: Attribute flags for share-ability \*/

[ 53](4_2cortex__r_2arm__mpu_8h.md#ad2047a4b8dae13c488a331b1691000b5)#define NON\_SHAREABLE 0x0U

[ 54](4_2cortex__r_2arm__mpu_8h.md#a5c302dfed348f344a036701d4b9c7ec8)#define NON\_SHAREABLE\_Msk \

55 ((NON\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

[ 56](4_2cortex__r_2arm__mpu_8h.md#a6d48175f63f47fcbe1fedbbdfcd56a85)#define OUTER\_SHAREABLE 0x2U

[ 57](4_2cortex__r_2arm__mpu_8h.md#aa4f924c424fc141ffa32a9b5c1180d56)#define OUTER\_SHAREABLE\_Msk \

58 ((OUTER\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

[ 59](4_2cortex__r_2arm__mpu_8h.md#a8c245b5c485b439790459255fc645131)#define INNER\_SHAREABLE 0x3U

[ 60](4_2cortex__r_2arm__mpu_8h.md#ab0d195350222b02d2d83ecd94a9ca395)#define INNER\_SHAREABLE\_Msk \

61 ((INNER\_SHAREABLE << MPU\_RBAR\_SH\_Pos) & MPU\_RBAR\_SH\_Msk)

62

63/\* MPIR\_ELx Attribute flags for cache-ability \*/

64

65/\* Memory Attributes for Device Memory

66 \* 1.Gathering (G/nG)

67 \* Determines whether multiple accesses can be merged into a single

68 \* bus transaction.

69 \* nG: Number/size of accesses on the bus = number/size of accesses

70 \* in code.

71 \*

72 \* 2.Reordering (R/nR)

73 \* Determines whether accesses to the same device can be reordered.

74 \* nR: Accesses to the same IMPLEMENTATION DEFINED block size will

75 \* appear on the bus in program order.

76 \*

77 \* 3 Early Write Acknowledgment (E/nE)

78 \* Indicates to the memory system whether a buffer can send

79 \* acknowledgements.

80 \* nE: The response should come from the end slave, not buffering in

81 \* the interconnect.

82 \*/

[ 83](4_2cortex__r_2arm__mpu_8h.md#a7e8d641f98b092387124bd1ecf2fdb53)#define DEVICE\_nGnRnE 0x0U

[ 84](4_2cortex__r_2arm__mpu_8h.md#a1fb228a36a14d8679f6d038c47f5f2e1)#define DEVICE\_nGnRE 0x4U

[ 85](4_2cortex__r_2arm__mpu_8h.md#a50d2ee15f01cc5379a74d23efd969051)#define DEVICE\_nGRE 0x8U

[ 86](4_2cortex__r_2arm__mpu_8h.md#a3d0243c563668b7358ce29d54f7f1afa)#define DEVICE\_GRE 0xCU

87

88/\* Read/Write Allocation Configurations for Cacheable Memory \*/

[ 89](4_2cortex__r_2arm__mpu_8h.md#a1160c997a66c9fd58dbc3dcfd65982a8)#define R\_NON\_W\_NON 0x0U /\* Do not allocate Read/Write \*/

[ 90](4_2cortex__r_2arm__mpu_8h.md#a0696dfbe29563622fe76970f9d146ff5)#define R\_NON\_W\_ALLOC 0x1U /\* Do not allocate Read, Allocate Write \*/

[ 91](4_2cortex__r_2arm__mpu_8h.md#a8476bb45227afc0236bc9f427793d6a9)#define R\_ALLOC\_W\_NON 0x2U /\* Allocate Read, Do not allocate Write \*/

[ 92](4_2cortex__r_2arm__mpu_8h.md#a1815e3622467845af3b3083fa76f3314)#define R\_ALLOC\_W\_ALLOC 0x3U /\* Allocate Read/Write \*/

93

94/\* Memory Attributes for Normal Memory \*/

[ 95](4_2cortex__r_2arm__mpu_8h.md#a4720c776e51ea52fc8cfa2c1dc935d47)#define NORMAL\_O\_WT\_NT 0x80U /\* Normal, Outer Write-through non-transient \*/

[ 96](4_2cortex__r_2arm__mpu_8h.md#a7d87ec111ffd79cddb9ce9f23e9f20d9)#define NORMAL\_O\_WB\_NT 0xC0U /\* Normal, Outer Write-back non-transient \*/

[ 97](4_2cortex__r_2arm__mpu_8h.md#ae36bc21dc922e88f8d5d4ff0657d80b6)#define NORMAL\_O\_NON\_C 0x40U /\* Normal, Outer Non-Cacheable \*/

98

[ 99](4_2cortex__r_2arm__mpu_8h.md#a2d60ab7f15ac71d451a73758315eff07)#define NORMAL\_I\_WT\_NT 0x08U /\* Normal, Inner Write-through non-transient \*/

[ 100](4_2cortex__r_2arm__mpu_8h.md#a28f31a1e2a47e2cafa7f41260780fd5f)#define NORMAL\_I\_WB\_NT 0x0CU /\* Normal, Inner Write-back non-transient \*/

[ 101](4_2cortex__r_2arm__mpu_8h.md#a8dda4d3d5f372f8ef3070fb492448992)#define NORMAL\_I\_NON\_C 0x04U /\* Normal, Inner Non-Cacheable \*/

102

103/\* Global MAIR configurations \*/

[ 104](4_2cortex__r_2arm__mpu_8h.md#a6ae855ff0c11d85dc72a1c45edaa7f75)#define MPU\_MAIR\_INDEX\_DEVICE 0U

[ 105](4_2cortex__r_2arm__mpu_8h.md#acfdb4baf0d7ec48fdc77e8e2973a1487)#define MPU\_MAIR\_ATTR\_DEVICE (DEVICE\_nGnRnE)

106

[ 107](4_2cortex__r_2arm__mpu_8h.md#ab1521fd2deea0bd6b88c73aed7159f8a)#define MPU\_MAIR\_INDEX\_FLASH 1U

[ 108](4_2cortex__r_2arm__mpu_8h.md#ad384c906ae7e1f4841c8ea98754acc1c)#define MPU\_MAIR\_ATTR\_FLASH \

109 ((NORMAL\_O\_WT\_NT | (R\_ALLOC\_W\_NON << 4)) | \

110 (NORMAL\_I\_WT\_NT | R\_ALLOC\_W\_NON))

111

[ 112](4_2cortex__r_2arm__mpu_8h.md#a386bbcc650a8313774651212bda40d03)#define MPU\_MAIR\_INDEX\_SRAM 2U

[ 113](4_2cortex__r_2arm__mpu_8h.md#aca50d2bc85d65c0ad231ecd7deb40c50)#define MPU\_MAIR\_ATTR\_SRAM \

114 ((NORMAL\_O\_WB\_NT | (R\_ALLOC\_W\_ALLOC << 4)) | \

115 (NORMAL\_I\_WB\_NT | R\_ALLOC\_W\_ALLOC))

116

[ 117](4_2cortex__r_2arm__mpu_8h.md#a03e37d7769647008655338fe8359d946)#define MPU\_MAIR\_INDEX\_SRAM\_NOCACHE 3U

[ 118](4_2cortex__r_2arm__mpu_8h.md#ab6bce12dbd72d216cbb6bc748d801ce0)#define MPU\_MAIR\_ATTR\_SRAM\_NOCACHE \

119 ((NORMAL\_O\_NON\_C | (R\_NON\_W\_NON << 4)) | \

120 (NORMAL\_I\_NON\_C | R\_NON\_W\_NON))

121

[ 122](4_2cortex__r_2arm__mpu_8h.md#a497d0db2bf062be1a466a1c7cab6a260)#define MPU\_MAIR\_ATTRS \

123 ((MPU\_MAIR\_ATTR\_DEVICE << (MPU\_MAIR\_INDEX\_DEVICE \* 8)) | \

124 (MPU\_MAIR\_ATTR\_FLASH << (MPU\_MAIR\_INDEX\_FLASH \* 8)) | \

125 (MPU\_MAIR\_ATTR\_SRAM << (MPU\_MAIR\_INDEX\_SRAM \* 8)) | \

126 (MPU\_MAIR\_ATTR\_SRAM\_NOCACHE << (MPU\_MAIR\_INDEX\_SRAM\_NOCACHE \* 8)))

127

128/\* Some helper defines for common regions.

129 \*

130 \* Note that the ARMv8-R MPU architecture requires that the

131 \* enabled MPU regions are non-overlapping. Therefore, it is

132 \* recommended to use these helper defines only for configuring

133 \* fixed MPU regions at build-time.

134 \*/

[ 135](4_2cortex__r_2arm__mpu_8h.md#a4ce0d123898b8cb22cb161c8d69c411f)#define REGION\_IO\_ATTR \

136 { \

137 /\* AP, XN, SH \*/ \

138 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, \

139 /\* Cache-ability \*/ \

140 .mair\_idx = MPU\_MAIR\_INDEX\_DEVICE, \

141 }

142

[ 143](4_2cortex__r_2arm__mpu_8h.md#a859d811feecb32c788b16a413e1b4781)#define REGION\_RAM\_ATTR \

144 { \

145 /\* AP, XN, SH \*/ \

146 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | OUTER\_SHAREABLE\_Msk, \

147 /\* Cache-ability \*/ \

148 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, \

149 }

150

[ 151](4_2cortex__r_2arm__mpu_8h.md#a89573cb3bde7b26846a3607276c843d9)#define REGION\_RAM\_NOCACHE\_ATTR \

152 { \

153 /\* AP, XN, SH \*/ \

154 .rbar = NOT\_EXEC | P\_RW\_U\_NA\_Msk | NON\_SHAREABLE\_Msk, \

155 /\* Cache-ability \*/ \

156 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM\_NOCACHE, \

157 }

158

[ 159](4_2cortex__r_2arm__mpu_8h.md#a00fb6882c3ff5d043e319be2ac04ea01)#define REGION\_RAM\_TEXT\_ATTR \

160 { \

161 /\* AP, XN, SH \*/ \

162 .rbar = P\_RO\_U\_RO\_Msk | INNER\_SHAREABLE\_Msk, \

163 /\* Cache-ability \*/ \

164 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, \

165 }

166

[ 167](4_2cortex__r_2arm__mpu_8h.md#a677d1642d4a105f9d5f81404e58b2cf4)#define REGION\_RAM\_RO\_ATTR \

168 { \

169 /\* AP, XN, SH \*/ \

170 .rbar = NOT\_EXEC | P\_RO\_U\_RO\_Msk | INNER\_SHAREABLE\_Msk, \

171 /\* Cache-ability \*/ \

172 .mair\_idx = MPU\_MAIR\_INDEX\_SRAM, \

173 }

174

175#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

176/\* Note that the access permissions allow for un-privileged writes

177 \*/

178#define REGION\_FLASH\_ATTR \

179 { \

180 .rbar = P\_RW\_U\_RW\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

181 /\* Cache-ability \*/ \

182 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, \

183 }

184#else /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

[ 185](4_2cortex__r_2arm__mpu_8h.md#aef333777108782979d84344af4bc51d6)#define REGION\_FLASH\_ATTR \

186 { \

187 .rbar = P\_RO\_U\_RO\_Msk | NON\_SHAREABLE\_Msk, /\* AP, XN, SH \*/ \

188 /\* Cache-ability \*/ \

189 .mair\_idx = MPU\_MAIR\_INDEX\_FLASH, \

190 }

191#endif /\* CONFIG\_MPU\_ALLOW\_FLASH\_WRITE \*/

192

193#ifndef \_ASMLANGUAGE

194

195struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) {

196 /\* Attributes belonging to PRBAR \*/

197 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rbar](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a) : 6;

198 /\* MAIR index for attribute indirection \*/

199 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mair\_idx](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e) : 3;

200};

201

202/\* Region definition data structure \*/

203struct [arm\_mpu\_region](structarm__mpu__region.md) {

204 /\* Region Base Address \*/

[ 205](structarm__mpu__region.md#a8713828bd9eab634f86b520a95ab102b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [base](structarm__mpu__region.md#a1639ea642561dc45d33774817e6a67b6);

206 /\* Region limit Address \*/

[ 207](structarm__mpu__region.md#a2a906f6ec90b76da7851016f706dd2d9) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [limit](structarm__mpu__region.md#a2a906f6ec90b76da7851016f706dd2d9);

208 /\* Region Name \*/

209 const char \*[name](structarm__mpu__region.md#a18f2dc7696fd55c1fdcce57ae16b46e4);

210 /\* Region Attributes \*/

[ 211](structarm__mpu__region.md#a1214b828c6ceedd70c31e9e251b661c8) struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) [attr](structarm__mpu__region.md#aa94b10ac6e6780c154c25cee91e7921e);

212};

213

214/\* MPU configuration data structure \*/

215struct [arm\_mpu\_config](structarm__mpu__config.md) {

216 /\* Number of regions \*/

217 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_regions](structarm__mpu__config.md#a13216be94d5dfea0e4eb069f24400fdc);

218 /\* Regions \*/

219 const struct [arm\_mpu\_region](structarm__mpu__region.md) \*[mpu\_regions](structarm__mpu__config.md#ac25f09decb52172736a1ab1e0327a6bc);

220};

221

[ 222](4_2cortex__r_2arm__mpu_8h.md#a05f77a35978ad9b60c8ba099d9a915f0)#define MPU\_REGION\_ENTRY(\_name, \_base, \_limit, \_attr) \

223 { \

224 .name = \_name, \

225 .base = \_base, \

226 .limit = \_limit, \

227 .attr = \_attr, \

228 }

229

[ 230](4_2cortex__r_2arm__mpu_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW ((k\_mem\_partition\_attr\_t) \

231 {(P\_RW\_U\_RW\_Msk), MPU\_MAIR\_INDEX\_SRAM})

[ 232](4_2cortex__r_2arm__mpu_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA ((k\_mem\_partition\_attr\_t) \

233 {(P\_RW\_U\_NA\_Msk), MPU\_MAIR\_INDEX\_SRAM})

[ 234](4_2cortex__r_2arm__mpu_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO ((k\_mem\_partition\_attr\_t) \

235 {(P\_RO\_U\_RO\_Msk), MPU\_MAIR\_INDEX\_SRAM})

[ 236](4_2cortex__r_2arm__mpu_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA ((k\_mem\_partition\_attr\_t) \

237 {(P\_RO\_U\_NA\_Msk), MPU\_MAIR\_INDEX\_SRAM})

238

[ 239](4_2cortex__r_2arm__mpu_8h.md#a6b3c416482c4d01cc12db5269886bb05)typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

240

241/\* Reference to the MPU configuration.

242 \*

243 \* This struct is defined and populated for each SoC (in the SoC definition),

244 \* and holds the build-time configuration information for the fixed MPU

245 \* regions enabled during kernel initialization. Dynamic MPU regions (e.g.

246 \* for Thread Stack, Stack Guards, etc.) are programmed during runtime, thus,

247 \* not kept here.

248 \*/

249extern const struct [arm\_mpu\_config](structarm__mpu__config.md) [mpu\_config](arc__mpu_8h.md#a347b2bb6c23b874d7a20d4b5ce4d23b1);

250

[ 251](structdynamic__region__info.md)struct [dynamic\_region\_info](structdynamic__region__info.md) {

[ 252](structdynamic__region__info.md#a5413f9316d8d49e569b928ff4fb017ba) int [index](structdynamic__region__info.md#a5413f9316d8d49e569b928ff4fb017ba);

[ 253](structdynamic__region__info.md#afb3082ae513afbf65db76d8ceed958e0) struct [arm\_mpu\_region](structarm__mpu__region.md) [region\_conf](structdynamic__region__info.md#afb3082ae513afbf65db76d8ceed958e0);

254};

255

[ 256](4_2cortex__r_2arm__mpu_8h.md#a6e954e6d9c6117210d857b360bf5fa51)#define ARM64\_MPU\_MAX\_DYNAMIC\_REGIONS \

257 1 + /\* data section \*/ \

258 (CONFIG\_MAX\_DOMAIN\_PARTITIONS + 2) + \

259 (IS\_ENABLED(CONFIG\_ARM64\_STACK\_PROTECTION) ? 2 : 0) + \

260 (IS\_ENABLED(CONFIG\_USERSPACE) ? 2 : 0)

261

262#endif /\* \_ASMLANGUAGE \*/

263

264#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CORTEX\_R\_MPU\_ARM\_MPU\_H\_ \*/

[mpu\_config](arc__mpu_8h.md#a347b2bb6c23b874d7a20d4b5ce4d23b1)

struct arc\_mpu\_config mpu\_config

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[arm\_mpu\_config](structarm__mpu__config.md)

**Definition** arm\_mpu.h:42

[arm\_mpu\_config::num\_regions](structarm__mpu__config.md#a13216be94d5dfea0e4eb069f24400fdc)

uint32\_t num\_regions

**Definition** arm\_mpu.h:44

[arm\_mpu\_config::mpu\_regions](structarm__mpu__config.md#ac25f09decb52172736a1ab1e0327a6bc)

const struct arm\_mpu\_region \* mpu\_regions

**Definition** arm\_mpu.h:46

[arm\_mpu\_region\_attr](structarm__mpu__region__attr.md)

**Definition** arm\_mpu\_v7m.h:152

[arm\_mpu\_region\_attr::rbar](structarm__mpu__region__attr.md#a02565921f84b5f03f9f86c67a935b17a)

uint8\_t rbar

**Definition** arm\_mpu\_v8.h:309

[arm\_mpu\_region\_attr::mair\_idx](structarm__mpu__region__attr.md#a791b4f41df0ed0cb3eb5e69d944f038e)

uint8\_t mair\_idx

**Definition** arm\_mpu\_v8.h:311

[arm\_mpu\_region](structarm__mpu__region.md)

**Definition** arm\_mpu.h:28

[arm\_mpu\_region::base](structarm__mpu__region.md#a1639ea642561dc45d33774817e6a67b6)

uint32\_t base

**Definition** arm\_mpu.h:30

[arm\_mpu\_region::name](structarm__mpu__region.md#a18f2dc7696fd55c1fdcce57ae16b46e4)

const char \* name

**Definition** arm\_mpu.h:32

[arm\_mpu\_region::limit](structarm__mpu__region.md#a2a906f6ec90b76da7851016f706dd2d9)

uint64\_t limit

**Definition** arm\_mpu.h:207

[arm\_mpu\_region::attr](structarm__mpu__region.md#aa94b10ac6e6780c154c25cee91e7921e)

arm\_mpu\_region\_attr\_t attr

**Definition** arm\_mpu.h:38

[dynamic\_region\_info](structdynamic__region__info.md)

**Definition** arm\_mpu.h:251

[dynamic\_region\_info::index](structdynamic__region__info.md#a5413f9316d8d49e569b928ff4fb017ba)

int index

**Definition** arm\_mpu.h:252

[dynamic\_region\_info::region\_conf](structdynamic__region__info.md#afb3082ae513afbf65db76d8ceed958e0)

struct arm\_mpu\_region region\_conf

**Definition** arm\_mpu.h:253

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [cortex\_r](dir_c43630f15275c571a36c3286c2e4d54b.md)
- [arm\_mpu.h](4_2cortex__r_2arm__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
