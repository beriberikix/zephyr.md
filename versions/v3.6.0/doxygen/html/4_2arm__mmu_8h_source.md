---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/4_2arm__mmu_8h_source.html
original_path: doxygen/html/4_2arm__mmu_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mmu.h

[Go to the documentation of this file.](4_2arm__mmu_8h.md)

1/\*

2 \* Copyright 2019 Broadcom

3 \* The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARM\_MMU\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARM\_MMU\_H\_

9

10#ifndef \_ASMLANGUAGE

11#include <[stdint.h](stdint_8h.md)>

12#include <[stdlib.h](stdlib_8h.md)>

13#endif

14

15/\* Following Memory types supported through MAIR encodings can be passed

16 \* by user through "attrs"(attributes) field of specified memory region.

17 \* As MAIR supports such 8 encodings, we will reserve attrs[2:0];

18 \* so that we can provide encodings upto 7 if needed in future.

19 \*/

[ 20](4_2arm__mmu_8h.md#aac0064c36c372d9a62d3a7a4fa8dc72c)#define MT\_TYPE\_MASK 0x7U

[ 21](4_2arm__mmu_8h.md#a9018634e807aa322da516bb70b9c5e3e)#define MT\_TYPE(attr) (attr & MT\_TYPE\_MASK)

[ 22](4_2arm__mmu_8h.md#a362a80b5a2f87e888d742ac4b1e8d7e1)#define MT\_DEVICE\_nGnRnE 0U

[ 23](4_2arm__mmu_8h.md#afb3dda3d3a2b1a147be7ee58366e3f87)#define MT\_DEVICE\_nGnRE 1U

[ 24](4_2arm__mmu_8h.md#ada441c0a6171dce9eef0875593ba5e56)#define MT\_DEVICE\_GRE 2U

[ 25](4_2arm__mmu_8h.md#a1a41f294343c4fcb9741c693fc107601)#define MT\_NORMAL\_NC 3U

[ 26](4_2arm__mmu_8h.md#a8b006dab179dfa8965dcef3ac302746d)#define MT\_NORMAL 4U

[ 27](4_2arm__mmu_8h.md#ad70c105c395f996ddd2628686e4e956f)#define MT\_NORMAL\_WT 5U

28

[ 29](4_2arm__mmu_8h.md#a8b7a2f1ea804a163917486b5e3d2a70a)#define MEMORY\_ATTRIBUTES ((0x00 << (MT\_DEVICE\_nGnRnE \* 8)) | \

30 (0x04 << (MT\_DEVICE\_nGnRE \* 8)) | \

31 (0x0c << (MT\_DEVICE\_GRE \* 8)) | \

32 (0x44 << (MT\_NORMAL\_NC \* 8)) | \

33 (0xffUL << (MT\_NORMAL \* 8)) | \

34 (0xbbUL << (MT\_NORMAL\_WT \* 8)))

35

36/\* More flags from user's perspective are supported using remaining bits

37 \* of "attrs" field, i.e. attrs[31:3], underlying code will take care

38 \* of setting PTE fields correctly.

39 \*

40 \* current usage of attrs[31:3] is:

41 \* attrs[3] : Access Permissions

42 \* attrs[4] : Memory access from secure/ns state

43 \* attrs[5] : Execute Permissions privileged mode (PXN)

44 \* attrs[6] : Execute Permissions unprivileged mode (UXN)

45 \* attrs[7] : Mirror RO/RW permissions to EL0

46 \* attrs[8] : Overwrite existing mapping if any

47 \* attrs[9] : non-Global mapping (nG)

48 \*

49 \*/

[ 50](4_2arm__mmu_8h.md#a4796895c7c90277cd1eae3c34fecd96c)#define MT\_PERM\_SHIFT 3U

[ 51](4_2arm__mmu_8h.md#a4e94c3f3e790bb5c1afaa6ffa1094c8d)#define MT\_SEC\_SHIFT 4U

[ 52](4_2arm__mmu_8h.md#ac01ddafde6fbc038bfa5994b7335429c)#define MT\_P\_EXECUTE\_SHIFT 5U

[ 53](4_2arm__mmu_8h.md#a431b40e024ff711208e286a68cc4a88a)#define MT\_U\_EXECUTE\_SHIFT 6U

[ 54](4_2arm__mmu_8h.md#afe1e276059306bc596102d8cc0eb0db6)#define MT\_RW\_AP\_SHIFT 7U

[ 55](4_2arm__mmu_8h.md#a099fcd188b2d8cb542ead3aff617632c)#define MT\_NO\_OVERWRITE\_SHIFT 8U

[ 56](4_2arm__mmu_8h.md#affc55d3de67afeb18b29b2e4070b12e0)#define MT\_NON\_GLOBAL\_SHIFT 9U

57

[ 58](4_2arm__mmu_8h.md#a596089f139287e4696c2fe9c9add4074)#define MT\_RO (0U << MT\_PERM\_SHIFT)

[ 59](4_2arm__mmu_8h.md#a2f968826efe83004f350f2264fc5b192)#define MT\_RW (1U << MT\_PERM\_SHIFT)

60

[ 61](4_2arm__mmu_8h.md#a06edb368943a5fffb03c362df5e00973)#define MT\_RW\_AP\_ELx (1U << MT\_RW\_AP\_SHIFT)

[ 62](4_2arm__mmu_8h.md#a9ee77575da6d9e81fc4ec5042b43932f)#define MT\_RW\_AP\_EL\_HIGHER (0U << MT\_RW\_AP\_SHIFT)

63

[ 64](4_2arm__mmu_8h.md#a9a2ae47063f7f1b105796d5e3114118f)#define MT\_SECURE (0U << MT\_SEC\_SHIFT)

[ 65](4_2arm__mmu_8h.md#a2b0dcb4b334e2fd3eb31eb7451dfc005)#define MT\_NS (1U << MT\_SEC\_SHIFT)

66

[ 67](4_2arm__mmu_8h.md#a465cd6685380ff25b2223b19844d730a)#define MT\_P\_EXECUTE (0U << MT\_P\_EXECUTE\_SHIFT)

[ 68](4_2arm__mmu_8h.md#a968668b91295729a7d462216e91c6d0c)#define MT\_P\_EXECUTE\_NEVER (1U << MT\_P\_EXECUTE\_SHIFT)

69

[ 70](4_2arm__mmu_8h.md#a5826032cb5c39b30b5727214c0856472)#define MT\_U\_EXECUTE (0U << MT\_U\_EXECUTE\_SHIFT)

[ 71](4_2arm__mmu_8h.md#a8ea94a35ceb0fc2dedd93a6eadadb68c)#define MT\_U\_EXECUTE\_NEVER (1U << MT\_U\_EXECUTE\_SHIFT)

72

[ 73](4_2arm__mmu_8h.md#ac636f36db1fba874b86869137adceb8a)#define MT\_NO\_OVERWRITE (1U << MT\_NO\_OVERWRITE\_SHIFT)

74

[ 75](4_2arm__mmu_8h.md#ada37826f9a2df34be98cc2e317d018d0)#define MT\_G (0U << MT\_NON\_GLOBAL\_SHIFT)

[ 76](4_2arm__mmu_8h.md#ab34aa4ce7681e17338d581bfd31ff5d1)#define MT\_NG (1U << MT\_NON\_GLOBAL\_SHIFT)

77

[ 78](4_2arm__mmu_8h.md#a7820c2334f7d257ea6bad7207576da7d)#define MT\_P\_RW\_U\_RW (MT\_RW | MT\_RW\_AP\_ELx | MT\_P\_EXECUTE\_NEVER | MT\_U\_EXECUTE\_NEVER)

[ 79](4_2arm__mmu_8h.md#a22971adcbb04ce5c5dd54c318c60b335)#define MT\_P\_RW\_U\_NA (MT\_RW | MT\_RW\_AP\_EL\_HIGHER | MT\_P\_EXECUTE\_NEVER | MT\_U\_EXECUTE\_NEVER)

[ 80](4_2arm__mmu_8h.md#acf29eaa48accc12214f86cf8c99cf04b)#define MT\_P\_RO\_U\_RO (MT\_RO | MT\_RW\_AP\_ELx | MT\_P\_EXECUTE\_NEVER | MT\_U\_EXECUTE\_NEVER)

[ 81](4_2arm__mmu_8h.md#a779a089d8fef5d7b544ef528d0355164)#define MT\_P\_RO\_U\_NA (MT\_RO | MT\_RW\_AP\_EL\_HIGHER | MT\_P\_EXECUTE\_NEVER | MT\_U\_EXECUTE\_NEVER)

[ 82](4_2arm__mmu_8h.md#a28187ebec00be9a34ce2a40f57337a3d)#define MT\_P\_RO\_U\_RX (MT\_RO | MT\_RW\_AP\_ELx | MT\_P\_EXECUTE\_NEVER | MT\_U\_EXECUTE)

[ 83](4_2arm__mmu_8h.md#a6964f6367d4687541502dc9d4bc3b00e)#define MT\_P\_RX\_U\_RX (MT\_RO | MT\_RW\_AP\_ELx | MT\_P\_EXECUTE | MT\_U\_EXECUTE)

[ 84](4_2arm__mmu_8h.md#a927c1d7900d9a38b800118a0751dfc9f)#define MT\_P\_RX\_U\_NA (MT\_RO | MT\_RW\_AP\_EL\_HIGHER | MT\_P\_EXECUTE | MT\_U\_EXECUTE\_NEVER)

85

86#ifdef CONFIG\_ARMV8\_A\_NS

87#define MT\_DEFAULT\_SECURE\_STATE MT\_NS

88#else

[ 89](4_2arm__mmu_8h.md#afc20034b86cd6fefcbc63668e08bf466)#define MT\_DEFAULT\_SECURE\_STATE MT\_SECURE

90#endif

91

92/\*

93 \* ARM guarantees at least 8 ASID bits.

94 \* We may have more available, but do not make use of them for the time being.

95 \*/

[ 96](4_2arm__mmu_8h.md#a9c2e741f0962da342556c5933dcb3e13)#define VM\_ASID\_BITS 8

[ 97](4_2arm__mmu_8h.md#a7a10d540248fccf48bdcaccac98f021c)#define TTBR\_ASID\_SHIFT 48

98

99/\*

100 \* PTE descriptor can be Block descriptor or Table descriptor

101 \* or Page descriptor.

102 \*/

[ 103](4_2arm__mmu_8h.md#a527750258496a95273157359f9a616cd)#define PTE\_DESC\_TYPE\_MASK 3U

[ 104](4_2arm__mmu_8h.md#a88d1df1c276037d073cda2a19ae18333)#define PTE\_BLOCK\_DESC 1U

[ 105](4_2arm__mmu_8h.md#a6bae275d781d6ed862ffcb4243793f78)#define PTE\_TABLE\_DESC 3U

[ 106](4_2arm__mmu_8h.md#ad06436454a4d3be738e45b49ebdece3a)#define PTE\_PAGE\_DESC 3U

[ 107](4_2arm__mmu_8h.md#a526197beecdcea0eec10e552a91093e6)#define PTE\_INVALID\_DESC 0U

108

109/\*

110 \* Block and Page descriptor attributes fields

111 \*/

[ 112](4_2arm__mmu_8h.md#a6c70c49e36e7086784aeb67190cb3fe1)#define PTE\_BLOCK\_DESC\_MEMTYPE(x) (x << 2)

[ 113](4_2arm__mmu_8h.md#a2e118ef56a9201b03f4a6c1aa714c7a7)#define PTE\_BLOCK\_DESC\_NS (1ULL << 5)

[ 114](4_2arm__mmu_8h.md#ab98726b07a80272d8c256b3a3fb0962e)#define PTE\_BLOCK\_DESC\_AP\_ELx (1ULL << 6)

[ 115](4_2arm__mmu_8h.md#a843a5d300e74d449654775e6f766b5af)#define PTE\_BLOCK\_DESC\_AP\_EL\_HIGHER (0ULL << 6)

[ 116](4_2arm__mmu_8h.md#a5856f4fe020995aad3806622d15d2658)#define PTE\_BLOCK\_DESC\_AP\_RO (1ULL << 7)

[ 117](4_2arm__mmu_8h.md#a76134e521bd7aca4e1d44e6580cc1664)#define PTE\_BLOCK\_DESC\_AP\_RW (0ULL << 7)

[ 118](4_2arm__mmu_8h.md#a81f8f7fe9bbd4d98ec549f79cacfc171)#define PTE\_BLOCK\_DESC\_NON\_SHARE (0ULL << 8)

[ 119](4_2arm__mmu_8h.md#a950be651c8f1c2f417e6720ce86ed965)#define PTE\_BLOCK\_DESC\_OUTER\_SHARE (2ULL << 8)

[ 120](4_2arm__mmu_8h.md#a2a66f774077bf08a56ab756e65a951f6)#define PTE\_BLOCK\_DESC\_INNER\_SHARE (3ULL << 8)

[ 121](4_2arm__mmu_8h.md#ac297c22c098e84375419e66642f7dd08)#define PTE\_BLOCK\_DESC\_AF (1ULL << 10)

[ 122](4_2arm__mmu_8h.md#aeaa1fc48a3425525e814a5757018bd02)#define PTE\_BLOCK\_DESC\_NG (1ULL << 11)

[ 123](4_2arm__mmu_8h.md#abd06d5802f589c9b5304fca4944e560b)#define PTE\_BLOCK\_DESC\_PXN (1ULL << 53)

[ 124](4_2arm__mmu_8h.md#a30cbc588212d7a17bf96033bf550b356)#define PTE\_BLOCK\_DESC\_UXN (1ULL << 54)

125

126/\*

127 \* TCR definitions.

128 \*/

[ 129](4_2arm__mmu_8h.md#afc474e5ad860c2ad3929cfb0e260bbd4)#define TCR\_EL1\_IPS\_SHIFT 32U

[ 130](4_2arm__mmu_8h.md#aec7d4ec2280b0a4bdda23bddf6906de1)#define TCR\_EL2\_PS\_SHIFT 16U

[ 131](4_2arm__mmu_8h.md#a877cc3e5688433a4054e6bf94da087fa)#define TCR\_EL3\_PS\_SHIFT 16U

132

[ 133](4_2arm__mmu_8h.md#ac1a5b8ca796786488092557cae6ee529)#define TCR\_T0SZ\_SHIFT 0U

[ 134](4_2arm__mmu_8h.md#a517e3ccc657482e5fb7c44f1968f4d47)#define TCR\_T0SZ(x) ((64 - (x)) << TCR\_T0SZ\_SHIFT)

135

[ 136](4_2arm__mmu_8h.md#a88aeb17c761edada2d6e3aaba7f86048)#define TCR\_IRGN\_NC (0ULL << 8)

[ 137](4_2arm__mmu_8h.md#a78c51335d078882f3252159b84d5fdb4)#define TCR\_IRGN\_WBWA (1ULL << 8)

[ 138](4_2arm__mmu_8h.md#aec3c547b075756c4d1aa78c831bc0e19)#define TCR\_IRGN\_WT (2ULL << 8)

[ 139](4_2arm__mmu_8h.md#ad57f8de92899f6bd54b6c898ce5c1c1e)#define TCR\_IRGN\_WBNWA (3ULL << 8)

[ 140](4_2arm__mmu_8h.md#a89f8bb0c67aee23a0b3c32642513557b)#define TCR\_IRGN\_MASK (3ULL << 8)

[ 141](4_2arm__mmu_8h.md#acabb0e302d9da4b9ba55ed0e0eea5843)#define TCR\_ORGN\_NC (0ULL << 10)

[ 142](4_2arm__mmu_8h.md#ae3c8d6de1e936b38893d324eb61f6759)#define TCR\_ORGN\_WBWA (1ULL << 10)

[ 143](4_2arm__mmu_8h.md#a9fc70a55aab31e25e944fc1fa9c9a2f7)#define TCR\_ORGN\_WT (2ULL << 10)

[ 144](4_2arm__mmu_8h.md#af693fdf5b28a70fa4f74e37f34bf69df)#define TCR\_ORGN\_WBNWA (3ULL << 10)

[ 145](4_2arm__mmu_8h.md#a266d922348791827670e045082cbecd4)#define TCR\_ORGN\_MASK (3ULL << 10)

[ 146](4_2arm__mmu_8h.md#ac9476792f28eed670e915a224487e56d)#define TCR\_SHARED\_NON (0ULL << 12)

[ 147](4_2arm__mmu_8h.md#a8b22083005fdf69673a230483cde6796)#define TCR\_SHARED\_OUTER (2ULL << 12)

[ 148](4_2arm__mmu_8h.md#ab9b64a7a88537b21703c8ed22a0faf3c)#define TCR\_SHARED\_INNER (3ULL << 12)

[ 149](4_2arm__mmu_8h.md#ae46a532f75ba7e47e002b6a87255d4b6)#define TCR\_TG0\_4K (0ULL << 14)

[ 150](4_2arm__mmu_8h.md#a82277d04ea5b90b9cd76a3878731f5a2)#define TCR\_TG0\_64K (1ULL << 14)

[ 151](4_2arm__mmu_8h.md#a5933d39b322e440d1d58f5b856bb646b)#define TCR\_TG0\_16K (2ULL << 14)

[ 152](4_2arm__mmu_8h.md#a906790e8cf432a7c37f49663154e2bd9)#define TCR\_EPD1\_DISABLE (1ULL << 23)

[ 153](4_2arm__mmu_8h.md#a73b851e99df71a05fed2c19fca94d871)#define TCR\_TG1\_16K (1ULL << 30)

[ 154](4_2arm__mmu_8h.md#aad679e64b09a1ab7e33804541416db78)#define TCR\_TG1\_4K (2ULL << 30)

[ 155](4_2arm__mmu_8h.md#a9eed7a785bd5191422317d2562294e88)#define TCR\_TG1\_64K (3ULL << 30)

156

[ 157](4_2arm__mmu_8h.md#a2e03342250af50f33b1936bd44eafd4c)#define TCR\_PS\_BITS\_4GB 0x0ULL

[ 158](4_2arm__mmu_8h.md#a88543861de395886feeb0ec348a397e9)#define TCR\_PS\_BITS\_64GB 0x1ULL

[ 159](4_2arm__mmu_8h.md#a31a276f07a891040b399a4f573dd0d16)#define TCR\_PS\_BITS\_1TB 0x2ULL

[ 160](4_2arm__mmu_8h.md#a3b30b0a4be3d34fcedc4bcd4ee77c0fd)#define TCR\_PS\_BITS\_4TB 0x3ULL

[ 161](4_2arm__mmu_8h.md#a1c6fe4b7dd9646549208af7eee92638b)#define TCR\_PS\_BITS\_16TB 0x4ULL

[ 162](4_2arm__mmu_8h.md#a5a7ab516dbd382c58dd408da6a22b88f)#define TCR\_PS\_BITS\_256TB 0x5ULL

163

164#ifndef \_ASMLANGUAGE

165

166/\* Region definition data structure \*/

167struct [arm\_mmu\_region](structarm__mmu__region.md) {

168 /\* Region Base Physical Address \*/

169 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [base\_pa](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78);

170 /\* Region Base Virtual Address \*/

171 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [base\_va](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3);

172 /\* Region size \*/

173 size\_t [size](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532);

174 /\* Region Name \*/

175 const char \*[name](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2);

176 /\* Region Attributes \*/

177 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attrs](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604);

178};

179

180/\* MMU configuration data structure \*/

181struct [arm\_mmu\_config](structarm__mmu__config.md) {

182 /\* Number of regions \*/

[ 183](structarm__mmu__config.md#aa2cc8f0491ed44a7f8db4db791598516) unsigned int [num\_regions](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a);

184 /\* Regions \*/

185 const struct [arm\_mmu\_region](structarm__mmu__region.md) \*[mmu\_regions](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5);

186};

187

[ 188](structarm__mmu__ptables.md)struct [arm\_mmu\_ptables](structarm__mmu__ptables.md) {

[ 189](structarm__mmu__ptables.md#a5d203fecef43d4a6430763489b15e5b5) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*[base\_xlat\_table](structarm__mmu__ptables.md#a5d203fecef43d4a6430763489b15e5b5);

[ 190](structarm__mmu__ptables.md#a215465999e8a8aa8ec45b0e47892d4b8) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ttbr0](structarm__mmu__ptables.md#a215465999e8a8aa8ec45b0e47892d4b8);

191};

192

193/\* Convenience macros to represent the ARMv8-A-specific

194 \* configuration for memory access permission and

195 \* cache-ability attribution.

196 \*/

197

[ 198](4_2arm__mmu_8h.md#a7ab46a0bcc5d7f2645f98067ed78ac8f)#define MMU\_REGION\_ENTRY(\_name, \_base\_pa, \_base\_va, \_size, \_attrs) \

199 {\

200 .name = \_name, \

201 .base\_pa = \_base\_pa, \

202 .base\_va = \_base\_va, \

203 .size = \_size, \

204 .attrs = \_attrs, \

205 }

206

[ 207](4_2arm__mmu_8h.md#a7a9f450388792a5c053dd227207d255f)#define MMU\_REGION\_FLAT\_ENTRY(name, adr, sz, attrs) \

208 MMU\_REGION\_ENTRY(name, adr, adr, sz, attrs)

209

210/\*

211 \* @brief Auto generate mmu region entry for node\_id

212 \*

213 \* Example usage:

214 \*

215 \* @code{.c}

216 \* DT\_FOREACH\_STATUS\_OKAY\_VARGS(nxp\_imx\_gpio,

217 \* MMU\_REGION\_DT\_FLAT\_ENTRY,

218 \* (MT\_DEVICE\_nGnRnE | MT\_P\_RW\_U\_NA | MT\_NS))

219 \* @endcode

220 \*

221 \* @note Since devicetree\_generated.h does not include

222 \* node\_id##\_P\_reg\_FOREACH\_PROP\_ELEM\* definitions,

223 \* we can't automate dts node with multiple reg

224 \* entries.

225 \*/

[ 226](4_2arm__mmu_8h.md#a345c9537de9d7439c853b7f5c275d0cf)#define MMU\_REGION\_DT\_FLAT\_ENTRY(node\_id, attrs) \

227 MMU\_REGION\_FLAT\_ENTRY(DT\_NODE\_FULL\_NAME(node\_id), \

228 DT\_REG\_ADDR(node\_id), \

229 DT\_REG\_SIZE(node\_id), \

230 attrs),

231

232/\*

233 \* @brief Auto generate mmu region entry for status = "okay"

234 \* nodes compatible to a driver

235 \*

236 \* Example usage:

237 \*

238 \* @code{.c}

239 \* MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY(nxp\_imx\_gpio,

240 \* (MT\_DEVICE\_nGnRnE | MT\_P\_RW\_U\_NA | MT\_NS))

241 \* @endcode

242 \*

243 \* @note This is a wrapper of @ref MMU\_REGION\_DT\_FLAT\_ENTRY

244 \*/

[ 245](4_2arm__mmu_8h.md#a3266a39e2c823047ab9a9162be60daf4)#define MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY(compat, attr) \

246 DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, \

247 MMU\_REGION\_DT\_FLAT\_ENTRY, attr)

248

249/\* Kernel macros for memory attribution

250 \* (access permissions and cache-ability).

251 \*

252 \* The macros are to be stored in k\_mem\_partition\_attr\_t

253 \* objects. The format of a k\_mem\_partition\_attr\_t object

254 \* is an uint32\_t composed by permission and attribute flags

255 \* located in include/arch/arm64/arm\_mmu.h

256 \*/

257

258/\* Read-Write access permission attributes \*/

[ 259](4_2arm__mmu_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW ((k\_mem\_partition\_attr\_t) \

260 {MT\_P\_RW\_U\_RW})

[ 261](4_2arm__mmu_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA ((k\_mem\_partition\_attr\_t) \

262 {MT\_P\_RW\_U\_NA})

[ 263](4_2arm__mmu_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO ((k\_mem\_partition\_attr\_t) \

264 {MT\_P\_RO\_U\_RO})

[ 265](4_2arm__mmu_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA ((k\_mem\_partition\_attr\_t) \

266 {MT\_P\_RO\_U\_NA})

267/\* Execution-allowed attributes \*/

[ 268](4_2arm__mmu_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t) \

269 {MT\_P\_RX\_U\_RX})

270/\* Typedef for the k\_mem\_partition attribute \*/

[ 271](structk__mem__partition__attr__t.md#a4e49930c31e896b9b52867d6b83e3ae7)typedef struct { [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attrs](structk__mem__partition__attr__t.md#a4e49930c31e896b9b52867d6b83e3ae7); } [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

272

273/\* Reference to the MMU configuration.

274 \*

275 \* This struct is defined and populated for each SoC (in the SoC definition),

276 \* and holds the build-time configuration information for the fixed MMU

277 \* regions enabled during kernel initialization.

278 \*/

279extern const struct [arm\_mmu\_config](structarm__mmu__config.md) [mmu\_config](mmu_2arm__mmu_8h.md#afb6753aab93fd940c3fc43c11a908216);

280

281#endif /\* \_ASMLANGUAGE \*/

282

283#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARM\_MMU\_H\_ \*/

[mmu\_config](mmu_2arm__mmu_8h.md#afb6753aab93fd940c3fc43c11a908216)

const struct arm\_mmu\_config mmu\_config

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[stdlib.h](stdlib_8h.md)

[arm\_mmu\_config](structarm__mmu__config.md)

**Definition** arm\_mmu.h:124

[arm\_mmu\_config::mmu\_regions](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5)

const struct arm\_mmu\_region \* mmu\_regions

**Definition** arm\_mmu.h:128

[arm\_mmu\_config::num\_regions](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a)

uint32\_t num\_regions

**Definition** arm\_mmu.h:126

[arm\_mmu\_ptables](structarm__mmu__ptables.md)

**Definition** arm\_mmu.h:188

[arm\_mmu\_ptables::ttbr0](structarm__mmu__ptables.md#a215465999e8a8aa8ec45b0e47892d4b8)

uint64\_t ttbr0

**Definition** arm\_mmu.h:190

[arm\_mmu\_ptables::base\_xlat\_table](structarm__mmu__ptables.md#a5d203fecef43d4a6430763489b15e5b5)

uint64\_t \* base\_xlat\_table

**Definition** arm\_mmu.h:189

[arm\_mmu\_region](structarm__mmu__region.md)

**Definition** arm\_mmu.h:110

[arm\_mmu\_region::base\_va](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3)

uintptr\_t base\_va

**Definition** arm\_mmu.h:114

[arm\_mmu\_region::size](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532)

size\_t size

**Definition** arm\_mmu.h:116

[arm\_mmu\_region::base\_pa](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78)

uintptr\_t base\_pa

**Definition** arm\_mmu.h:112

[arm\_mmu\_region::name](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2)

const char \* name

**Definition** arm\_mmu.h:118

[arm\_mmu\_region::attrs](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604)

uint32\_t attrs

**Definition** arm\_mmu.h:120

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[k\_mem\_partition\_attr\_t::attrs](structk__mem__partition__attr__t.md#a4e49930c31e896b9b52867d6b83e3ae7)

uint32\_t attrs

**Definition** arm\_mmu.h:271

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arm\_mmu.h](4_2arm__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
