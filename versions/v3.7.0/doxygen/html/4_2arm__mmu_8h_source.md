---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/4_2arm__mmu_8h_source.html
original_path: doxygen/html/4_2arm__mmu_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

92#ifndef \_ASMLANGUAGE

93

94/\* Region definition data structure \*/

95struct [arm\_mmu\_region](structarm__mmu__region.md) {

96 /\* Region Base Physical Address \*/

97 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [base\_pa](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78);

98 /\* Region Base Virtual Address \*/

99 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [base\_va](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3);

100 /\* Region size \*/

101 size\_t [size](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532);

102 /\* Region Name \*/

103 const char \*[name](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2);

104 /\* Region Attributes \*/

105 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attrs](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604);

106};

107

108/\* MMU configuration data structure \*/

109struct [arm\_mmu\_config](structarm__mmu__config.md) {

110 /\* Number of regions \*/

[ 111](structarm__mmu__config.md#aa2cc8f0491ed44a7f8db4db791598516) unsigned int [num\_regions](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a);

112 /\* Regions \*/

113 const struct [arm\_mmu\_region](structarm__mmu__region.md) \*[mmu\_regions](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5);

114};

115

[ 116](structarm__mmu__ptables.md)struct [arm\_mmu\_ptables](structarm__mmu__ptables.md) {

[ 117](structarm__mmu__ptables.md#a5d203fecef43d4a6430763489b15e5b5) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*[base\_xlat\_table](structarm__mmu__ptables.md#a5d203fecef43d4a6430763489b15e5b5);

[ 118](structarm__mmu__ptables.md#a215465999e8a8aa8ec45b0e47892d4b8) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ttbr0](structarm__mmu__ptables.md#a215465999e8a8aa8ec45b0e47892d4b8);

119};

120

121/\* Convenience macros to represent the ARMv8-A-specific

122 \* configuration for memory access permission and

123 \* cache-ability attribution.

124 \*/

125

[ 126](4_2arm__mmu_8h.md#a7ab46a0bcc5d7f2645f98067ed78ac8f)#define MMU\_REGION\_ENTRY(\_name, \_base\_pa, \_base\_va, \_size, \_attrs) \

127 {\

128 .name = \_name, \

129 .base\_pa = \_base\_pa, \

130 .base\_va = \_base\_va, \

131 .size = \_size, \

132 .attrs = \_attrs, \

133 }

134

[ 135](4_2arm__mmu_8h.md#a7a9f450388792a5c053dd227207d255f)#define MMU\_REGION\_FLAT\_ENTRY(name, adr, sz, attrs) \

136 MMU\_REGION\_ENTRY(name, adr, adr, sz, attrs)

137

138/\*

139 \* @brief Auto generate mmu region entry for node\_id

140 \*

141 \* Example usage:

142 \*

143 \* @code{.c}

144 \* DT\_FOREACH\_STATUS\_OKAY\_VARGS(nxp\_imx\_gpio,

145 \* MMU\_REGION\_DT\_FLAT\_ENTRY,

146 \* (MT\_DEVICE\_nGnRnE | MT\_P\_RW\_U\_NA | MT\_NS))

147 \* @endcode

148 \*

149 \* @note Since devicetree\_generated.h does not include

150 \* node\_id##\_P\_reg\_FOREACH\_PROP\_ELEM\* definitions,

151 \* we can't automate dts node with multiple reg

152 \* entries.

153 \*/

[ 154](4_2arm__mmu_8h.md#a345c9537de9d7439c853b7f5c275d0cf)#define MMU\_REGION\_DT\_FLAT\_ENTRY(node\_id, attrs) \

155 MMU\_REGION\_FLAT\_ENTRY(DT\_NODE\_FULL\_NAME(node\_id), \

156 DT\_REG\_ADDR(node\_id), \

157 DT\_REG\_SIZE(node\_id), \

158 attrs),

159

160/\*

161 \* @brief Auto generate mmu region entry for status = "okay"

162 \* nodes compatible to a driver

163 \*

164 \* Example usage:

165 \*

166 \* @code{.c}

167 \* MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY(nxp\_imx\_gpio,

168 \* (MT\_DEVICE\_nGnRnE | MT\_P\_RW\_U\_NA | MT\_NS))

169 \* @endcode

170 \*

171 \* @note This is a wrapper of @ref MMU\_REGION\_DT\_FLAT\_ENTRY

172 \*/

[ 173](4_2arm__mmu_8h.md#a3266a39e2c823047ab9a9162be60daf4)#define MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY(compat, attr) \

174 DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, \

175 MMU\_REGION\_DT\_FLAT\_ENTRY, attr)

176

177/\* Kernel macros for memory attribution

178 \* (access permissions and cache-ability).

179 \*

180 \* The macros are to be stored in k\_mem\_partition\_attr\_t

181 \* objects. The format of a k\_mem\_partition\_attr\_t object

182 \* is an uint32\_t composed by permission and attribute flags

183 \* located in include/arch/arm64/arm\_mmu.h

184 \*/

185

186/\* Read-Write access permission attributes \*/

[ 187](4_2arm__mmu_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW ((k\_mem\_partition\_attr\_t) \

188 {MT\_P\_RW\_U\_RW})

[ 189](4_2arm__mmu_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA ((k\_mem\_partition\_attr\_t) \

190 {MT\_P\_RW\_U\_NA})

[ 191](4_2arm__mmu_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO ((k\_mem\_partition\_attr\_t) \

192 {MT\_P\_RO\_U\_RO})

[ 193](4_2arm__mmu_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA ((k\_mem\_partition\_attr\_t) \

194 {MT\_P\_RO\_U\_NA})

195/\* Execution-allowed attributes \*/

[ 196](4_2arm__mmu_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t) \

197 {MT\_P\_RX\_U\_RX})

198/\* Typedef for the k\_mem\_partition attribute \*/

[ 199](structk__mem__partition__attr__t.md#a4e49930c31e896b9b52867d6b83e3ae7)typedef struct { [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attrs](structk__mem__partition__attr__t.md#a4e49930c31e896b9b52867d6b83e3ae7); } [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

200

201/\* Reference to the MMU configuration.

202 \*

203 \* This struct is defined and populated for each SoC (in the SoC definition),

204 \* and holds the build-time configuration information for the fixed MMU

205 \* regions enabled during kernel initialization.

206 \*/

207extern const struct [arm\_mmu\_config](structarm__mmu__config.md) [mmu\_config](mmu_2arm__mmu_8h.md#afb6753aab93fd940c3fc43c11a908216);

208

209#endif /\* \_ASMLANGUAGE \*/

210

211#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_ARM\_MMU\_H\_ \*/

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

**Definition** arm\_mmu.h:116

[arm\_mmu\_ptables::ttbr0](structarm__mmu__ptables.md#a215465999e8a8aa8ec45b0e47892d4b8)

uint64\_t ttbr0

**Definition** arm\_mmu.h:118

[arm\_mmu\_ptables::base\_xlat\_table](structarm__mmu__ptables.md#a5d203fecef43d4a6430763489b15e5b5)

uint64\_t \* base\_xlat\_table

**Definition** arm\_mmu.h:117

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

**Definition** arm\_mmu.h:199

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arm\_mmu.h](4_2arm__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
