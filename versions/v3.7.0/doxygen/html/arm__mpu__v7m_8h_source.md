---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arm__mpu__v7m_8h_source.html
original_path: doxygen/html/arm__mpu__v7m_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu\_v7m.h

[Go to the documentation of this file.](arm__mpu__v7m_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited.

3 \* Copyright (c) 2018 Nordic Semiconductor ASA.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef \_ASMLANGUAGE

9

10#include <cmsis\_core.h>

11

12/\* Convenience macros to represent the ARMv7-M-specific

13 \* configuration for memory access permission and

14 \* cache-ability attribution.

15 \*/

16

17/\* Privileged No Access, Unprivileged No Access \*/

[ 18](arm__mpu__v7m_8h.md#adb0cdfabc13b3915c548413e3bdae0dd)#define NO\_ACCESS 0x0

[ 19](arm__mpu__v7m_8h.md#ab6960e0c54d19d3180d2f89a69f94ac7)#define NO\_ACCESS\_Msk ((NO\_ACCESS << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

20/\* Privileged No Access, Unprivileged No Access \*/

[ 21](arm__mpu__v7m_8h.md#a07a285af1f0c83b06a49b3b7b8751dca)#define P\_NA\_U\_NA 0x0

[ 22](arm__mpu__v7m_8h.md#ab47b49bf96328887c7e2b548170c9d88)#define P\_NA\_U\_NA\_Msk ((P\_NA\_U\_NA << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

23/\* Privileged Read Write, Unprivileged No Access \*/

[ 24](arm__mpu__v7m_8h.md#a6632f2c0eba4d5aee046a86258100215)#define P\_RW\_U\_NA 0x1

[ 25](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7)#define P\_RW\_U\_NA\_Msk ((P\_RW\_U\_NA << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

26/\* Privileged Read Write, Unprivileged Read Only \*/

[ 27](arm__mpu__v7m_8h.md#a723850f2bb2947b771d4a967efc86de3)#define P\_RW\_U\_RO 0x2

[ 28](arm__mpu__v7m_8h.md#abccd688a7c1aa1302bfec6f9ea98b9b8)#define P\_RW\_U\_RO\_Msk ((P\_RW\_U\_RO << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

29/\* Privileged Read Write, Unprivileged Read Write \*/

[ 30](arm__mpu__v7m_8h.md#a8faee650ae8cc79e1d3605f251c3df34)#define P\_RW\_U\_RW 0x3U

[ 31](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db)#define P\_RW\_U\_RW\_Msk ((P\_RW\_U\_RW << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

32/\* Privileged Read Write, Unprivileged Read Write \*/

[ 33](arm__mpu__v7m_8h.md#a4da15c917ab4e26cd3e5e39dbec83000)#define FULL\_ACCESS 0x3

[ 34](arm__mpu__v7m_8h.md#a1da8e3113a0446b3d2acbe78b4e40b0c)#define FULL\_ACCESS\_Msk ((FULL\_ACCESS << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

35/\* Privileged Read Only, Unprivileged No Access \*/

[ 36](arm__mpu__v7m_8h.md#ad3012e82dde223bbe84c9e4d7c46e7fd)#define P\_RO\_U\_NA 0x5

[ 37](arm__mpu__v7m_8h.md#aeec24407a5fffaf967a841a26ccf46ed)#define P\_RO\_U\_NA\_Msk ((P\_RO\_U\_NA << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

38/\* Privileged Read Only, Unprivileged Read Only \*/

[ 39](arm__mpu__v7m_8h.md#a75fd88fb93da28e84017d4ba6fcb4211)#define P\_RO\_U\_RO 0x6

[ 40](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46)#define P\_RO\_U\_RO\_Msk ((P\_RO\_U\_RO << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

41/\* Privileged Read Only, Unprivileged Read Only \*/

[ 42](arm__mpu__v7m_8h.md#a628642b04c07236ae1e986c248a79ae5)#define RO 0x7

[ 43](arm__mpu__v7m_8h.md#a35e3f724856c6947c52885def2e3c0d6)#define RO\_Msk ((RO << MPU\_RASR\_AP\_Pos) & MPU\_RASR\_AP\_Msk)

44

45/\* Attribute flag for not-allowing execution (eXecute Never) \*/

[ 46](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)#define NOT\_EXEC MPU\_RASR\_XN\_Msk

47

48/\* The following definitions are for internal use in arm\_mpu.h. \*/

[ 49](arm__mpu__v7m_8h.md#ae48be083a1ebbb7d3378b319830486f4)#define STRONGLY\_ORDERED\_SHAREABLE MPU\_RASR\_S\_Msk

[ 50](arm__mpu__v7m_8h.md#a274cfa7f4a2f1f1e799d70c28db866ff)#define DEVICE\_SHAREABLE (MPU\_RASR\_B\_Msk | MPU\_RASR\_S\_Msk)

[ 51](arm__mpu__v7m_8h.md#a918f12d12d1248fdedf627880868f92b)#define NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_SHAREABLE \

52 (MPU\_RASR\_C\_Msk | MPU\_RASR\_S\_Msk)

[ 53](arm__mpu__v7m_8h.md#a25ba780869ac5ae4d9267d6e0c0a31c0)#define NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE MPU\_RASR\_C\_Msk

[ 54](arm__mpu__v7m_8h.md#a98ca2a3b1e78f1032b211d1815cc37db)#define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_SHAREABLE \

55 (MPU\_RASR\_C\_Msk | MPU\_RASR\_B\_Msk | MPU\_RASR\_S\_Msk)

[ 56](arm__mpu__v7m_8h.md#abcce878498db83cd7be9704ec6cff918)#define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_NON\_SHAREABLE \

57 (MPU\_RASR\_C\_Msk | MPU\_RASR\_B\_Msk)

[ 58](arm__mpu__v7m_8h.md#a313a77cea9e62aa04620f88bbb1d784b)#define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE \

59 ((1 << MPU\_RASR\_TEX\_Pos) | MPU\_RASR\_S\_Msk)

[ 60](arm__mpu__v7m_8h.md#a16b75f4910b2a70d5517b093d48aaafc)#define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_NON\_SHAREABLE \

61 (1 << MPU\_RASR\_TEX\_Pos)

[ 62](arm__mpu__v7m_8h.md#a89f98f53169e8eb0f232287f2e839991)#define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_SHAREABLE \

63 ((1 << MPU\_RASR\_TEX\_Pos) |\

64 MPU\_RASR\_C\_Msk | MPU\_RASR\_B\_Msk | MPU\_RASR\_S\_Msk)

[ 65](arm__mpu__v7m_8h.md#ab5e00d6a3a95abd2a1b3ab1744117d9c)#define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE \

66 ((1 << MPU\_RASR\_TEX\_Pos) | MPU\_RASR\_C\_Msk | MPU\_RASR\_B\_Msk)

[ 67](arm__mpu__v7m_8h.md#a27a7c7934b8cb593aa2653a828bcd6ca)#define DEVICE\_NON\_SHAREABLE (2 << MPU\_RASR\_TEX\_Pos)

68

69/\* Bit-masks to disable sub-regions. \*/

[ 70](arm__mpu__v7m_8h.md#ad97f565065c8e799b72494ffd2d057cd)#define SUB\_REGION\_0\_DISABLED ((0x01 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk)

[ 71](arm__mpu__v7m_8h.md#ad7f3c3c3cc4de407f0885a2d26930d1a)#define SUB\_REGION\_1\_DISABLED ((0x02 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk)

[ 72](arm__mpu__v7m_8h.md#a4939cd3e0ae7cd570a2aeef7c35e6bdc)#define SUB\_REGION\_2\_DISABLED ((0x04 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk)

[ 73](arm__mpu__v7m_8h.md#a24a64a4fb8bdf8af5422b6896f5215ab)#define SUB\_REGION\_3\_DISABLED ((0x08 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk)

[ 74](arm__mpu__v7m_8h.md#ae1e5b3747711b1b0e26b8be9d8ee1e73)#define SUB\_REGION\_4\_DISABLED ((0x10 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk)

[ 75](arm__mpu__v7m_8h.md#ae2810b78a1826f0660dfe07c3e23d493)#define SUB\_REGION\_5\_DISABLED ((0x20 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk)

[ 76](arm__mpu__v7m_8h.md#a67fcfd53ed1d703d0636d0807fc9c05e)#define SUB\_REGION\_6\_DISABLED ((0x40 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk)

[ 77](arm__mpu__v7m_8h.md#ad31907a27479655d251d170c66feee4b)#define SUB\_REGION\_7\_DISABLED ((0x80 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk)

78

79

[ 80](arm__mpu__v7m_8h.md#acbb181cf8ed1acc7fd43431321e94ee4)#define REGION\_SIZE(size) ((ARM\_MPU\_REGION\_SIZE\_ ## size \

81 << MPU\_RASR\_SIZE\_Pos) & MPU\_RASR\_SIZE\_Msk)

82

[ 83](arm__mpu__v7m_8h.md#a5cb4dfcb39c8cddde7d00be07abbf186)#define REGION\_32B REGION\_SIZE(32B)

[ 84](arm__mpu__v7m_8h.md#af0032361a1f7303ea36d4a78484ed991)#define REGION\_64B REGION\_SIZE(64B)

[ 85](arm__mpu__v7m_8h.md#af93290eb28d2d1eafaa1cad375cb994e)#define REGION\_128B REGION\_SIZE(128B)

[ 86](arm__mpu__v7m_8h.md#ae4a7b8266e1048e53ab72a96af99dfa9)#define REGION\_256B REGION\_SIZE(256B)

[ 87](arm__mpu__v7m_8h.md#abef640d835bc8fe9e49ebb23fed5eacc)#define REGION\_512B REGION\_SIZE(512B)

[ 88](arm__mpu__v7m_8h.md#a9216de2e7190dedac57efc79367a6c49)#define REGION\_1K REGION\_SIZE(1KB)

[ 89](arm__mpu__v7m_8h.md#aa22b0f233ecd96b8097e45260110845e)#define REGION\_2K REGION\_SIZE(2KB)

[ 90](arm__mpu__v7m_8h.md#a0dd685b0698d16ea2bed3b7ac3038a41)#define REGION\_4K REGION\_SIZE(4KB)

[ 91](arm__mpu__v7m_8h.md#a0d4b53088d0e9e4e4552c5b4a496731d)#define REGION\_8K REGION\_SIZE(8KB)

[ 92](arm__mpu__v7m_8h.md#a1f382e52ddd7a8c50571664736cb2b27)#define REGION\_16K REGION\_SIZE(16KB)

[ 93](arm__mpu__v7m_8h.md#a5354ce614160f66300ac71616f708a61)#define REGION\_32K REGION\_SIZE(32KB)

[ 94](arm__mpu__v7m_8h.md#ab75ccffbfbc1389e1303bb2415dc7c24)#define REGION\_64K REGION\_SIZE(64KB)

[ 95](arm__mpu__v7m_8h.md#ab6ee612fe19a00c67fba398da06f6f09)#define REGION\_128K REGION\_SIZE(128KB)

[ 96](arm__mpu__v7m_8h.md#a8a949eee20d66206a9c700eb68f4a614)#define REGION\_256K REGION\_SIZE(256KB)

[ 97](arm__mpu__v7m_8h.md#ae5fc1f5ea7a3bbbc85dce33cee2aa85b)#define REGION\_512K REGION\_SIZE(512KB)

[ 98](arm__mpu__v7m_8h.md#a1ad0013ace85d499c8d554602066c7e1)#define REGION\_1M REGION\_SIZE(1MB)

[ 99](arm__mpu__v7m_8h.md#a1bc46af188d58128dce0e7f6bf851515)#define REGION\_2M REGION\_SIZE(2MB)

[ 100](arm__mpu__v7m_8h.md#a4837e15ddf1dfa198442883d705d5eb1)#define REGION\_4M REGION\_SIZE(4MB)

[ 101](arm__mpu__v7m_8h.md#a464e54c991784aed5061b93adcfc387e)#define REGION\_8M REGION\_SIZE(8MB)

[ 102](arm__mpu__v7m_8h.md#ace038f88373aec532761c3c4f5193be3)#define REGION\_16M REGION\_SIZE(16MB)

[ 103](arm__mpu__v7m_8h.md#a2dacd02f000be694c6e4e1bcfe4e6d6e)#define REGION\_32M REGION\_SIZE(32MB)

[ 104](arm__mpu__v7m_8h.md#a66785668a244bc13dd0c5553a68384d2)#define REGION\_64M REGION\_SIZE(64MB)

[ 105](arm__mpu__v7m_8h.md#a2f0bf4c7ad62232ed5a185cb65708be0)#define REGION\_128M REGION\_SIZE(128MB)

[ 106](arm__mpu__v7m_8h.md#a81428ec21df3db24dee2b09c5f2c3ad5)#define REGION\_256M REGION\_SIZE(256MB)

[ 107](arm__mpu__v7m_8h.md#a4f61982635b2ed4099836c61811a8ce6)#define REGION\_512M REGION\_SIZE(512MB)

[ 108](arm__mpu__v7m_8h.md#ac959b468a34a1b202e3682f15bcd26fe)#define REGION\_1G REGION\_SIZE(1GB)

[ 109](arm__mpu__v7m_8h.md#a97835cec29142060938be2d53438e9f6)#define REGION\_2G REGION\_SIZE(2GB)

[ 110](arm__mpu__v7m_8h.md#ac14cdd5594b034fa65f3baf6b2e2bde9)#define REGION\_4G REGION\_SIZE(4GB)

111

[ 112](arm__mpu__v7m_8h.md#a2ec2a5ebe99ddac405570be52bc3a728)#define ARM\_MPU\_REGION\_INIT(p\_name, p\_base, p\_size, p\_attr) \

113 { .name = p\_name, \

114 .base = p\_base, \

115 .attr = p\_attr(size\_to\_mpu\_rasr\_size(p\_size)), \

116 }

117

118/\* Some helper defines for common regions \*/

119

120/\* On Cortex-M, we can only set the XN bit when CONFIG\_XIP=y. When

121 \* CONFIG\_XIP=n, the entire image will be linked to SRAM, so we need to keep

122 \* the SRAM region XN bit clear or the application code will not be executable.

123 \*/

[ 124](arm__mpu__v7m_8h.md#a6398aeba1eacd0df079a35ab3cd69e76)#define REGION\_RAM\_ATTR(size) \

125{ \

126 (NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE | \

127 IF\_ENABLED(CONFIG\_XIP, (MPU\_RASR\_XN\_Msk |)) size | P\_RW\_U\_NA\_Msk) \

128}

[ 129](arm__mpu__v7m_8h.md#a0f03b499ca2a55d2a5ae725b98d8ecbf)#define REGION\_RAM\_NOCACHE\_ATTR(size) \

130{ \

131 (NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_NON\_SHAREABLE | \

132 MPU\_RASR\_XN\_Msk | size | P\_RW\_U\_NA\_Msk) \

133}

134#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

135#define REGION\_FLASH\_ATTR(size) \

136{ \

137 (NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE | size | \

138 P\_RW\_U\_RO\_Msk) \

139}

140#else

[ 141](arm__mpu__v7m_8h.md#a27f4a4d075d6c2ecd477c48f0455fe6f)#define REGION\_FLASH\_ATTR(size) \

142{ \

143 (NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE | size | RO\_Msk) \

144}

145#endif

[ 146](arm__mpu__v7m_8h.md#a4d9881dc6866259e26659132277f6c9c)#define REGION\_PPB\_ATTR(size) { (STRONGLY\_ORDERED\_SHAREABLE | size | \

147 P\_RW\_U\_NA\_Msk) }

[ 148](arm__mpu__v7m_8h.md#ae8d8bc85a76a356e67c858b7667b75ff)#define REGION\_IO\_ATTR(size) { (DEVICE\_NON\_SHAREABLE | size | P\_RW\_U\_NA\_Msk) }

[ 149](arm__mpu__v7m_8h.md#aecd4c6b6a33d0ecf4a03d3226f88eba8)#define REGION\_EXTMEM\_ATTR(size) { (STRONGLY\_ORDERED\_SHAREABLE | size | \

150 NO\_ACCESS\_Msk) }

151

[ 152](structarm__mpu__region__attr.md)struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) {

153 /\* Attributes belonging to RASR (including the encoded region size) \*/

[ 154](structarm__mpu__region__attr.md#a8e38b1257bba7f67148bd7868f7cde23) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rasr](structarm__mpu__region__attr.md#a8e38b1257bba7f67148bd7868f7cde23);

155};

156

[ 157](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6)typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) [arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6);

158

159/\* Typedef for the k\_mem\_partition attribute \*/

[ 160](structk__mem__partition__attr__t.md)typedef struct {

[ 161](structk__mem__partition__attr__t.md#a04b3fd9acde8acc4eac37a1354bd7789) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rasr\_attr](structk__mem__partition__attr__t.md#a04b3fd9acde8acc4eac37a1354bd7789);

162} [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

163

164/\* Read-Write access permission attributes \*/

165#define \_K\_MEM\_PARTITION\_P\_NA\_U\_NA (NO\_ACCESS\_Msk | NOT\_EXEC)

166#define \_K\_MEM\_PARTITION\_P\_RW\_U\_RW (P\_RW\_U\_RW\_Msk | NOT\_EXEC)

167#define \_K\_MEM\_PARTITION\_P\_RW\_U\_RO (P\_RW\_U\_RO\_Msk | NOT\_EXEC)

168#define \_K\_MEM\_PARTITION\_P\_RW\_U\_NA (P\_RW\_U\_NA\_Msk | NOT\_EXEC)

169#define \_K\_MEM\_PARTITION\_P\_RO\_U\_RO (P\_RO\_U\_RO\_Msk | NOT\_EXEC)

170#define \_K\_MEM\_PARTITION\_P\_RO\_U\_NA (P\_RO\_U\_NA\_Msk | NOT\_EXEC)

171

172/\* Execution-allowed attributes \*/

173#define \_K\_MEM\_PARTITION\_P\_RWX\_U\_RWX (P\_RW\_U\_RW\_Msk)

174#define \_K\_MEM\_PARTITION\_P\_RWX\_U\_RX (P\_RW\_U\_RO\_Msk)

175#define \_K\_MEM\_PARTITION\_P\_RX\_U\_RX (P\_RO\_U\_RO\_Msk)

176

177/\* Kernel macros for memory attribution

178 \* (access permissions and cache-ability).

179 \*

180 \* The macros are to be stored in k\_mem\_partition\_attr\_t

181 \* objects. The format of k\_mem\_partition\_attr\_t is an

182 \* "1-1" mapping of the ARMv7-M MPU RASR attribute register

183 \* fields (excluding the <size> and <enable> bit-fields).

184 \*/

185

186/\* Read-Write access permission attributes (default cache-ability) \*/

[ 187](arm__mpu__v7m_8h.md#a73bc6803ccf24aad395089a4395bd22f)#define K\_MEM\_PARTITION\_P\_NA\_U\_NA ((k\_mem\_partition\_attr\_t) \

188 { \_K\_MEM\_PARTITION\_P\_NA\_U\_NA | \

189 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

[ 190](arm__mpu__v7m_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW ((k\_mem\_partition\_attr\_t) \

191 { \_K\_MEM\_PARTITION\_P\_RW\_U\_RW | \

192 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

[ 193](arm__mpu__v7m_8h.md#a6636a59c913e035646a1a9e5ed61559d)#define K\_MEM\_PARTITION\_P\_RW\_U\_RO ((k\_mem\_partition\_attr\_t) \

194 { \_K\_MEM\_PARTITION\_P\_RW\_U\_RO | \

195 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

[ 196](arm__mpu__v7m_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA ((k\_mem\_partition\_attr\_t) \

197 { \_K\_MEM\_PARTITION\_P\_RW\_U\_NA | \

198 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

[ 199](arm__mpu__v7m_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO ((k\_mem\_partition\_attr\_t) \

200 { \_K\_MEM\_PARTITION\_P\_RO\_U\_RO | \

201 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

[ 202](arm__mpu__v7m_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA ((k\_mem\_partition\_attr\_t) \

203 { \_K\_MEM\_PARTITION\_P\_RO\_U\_NA | \

204 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

205

206/\* Execution-allowed attributes (default-cacheability) \*/

[ 207](arm__mpu__v7m_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX ((k\_mem\_partition\_attr\_t) \

208 { \_K\_MEM\_PARTITION\_P\_RWX\_U\_RWX | \

209 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

[ 210](arm__mpu__v7m_8h.md#a81878d7a3177ef4c37ea3046da004c9a)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RX ((k\_mem\_partition\_attr\_t) \

211 { \_K\_MEM\_PARTITION\_P\_RWX\_U\_RX | \

212 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

[ 213](arm__mpu__v7m_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t) \

214 { \_K\_MEM\_PARTITION\_P\_RX\_U\_RX | \

215 NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE})

216

217/\*

218 \* @brief Evaluate Write-ability

219 \*

220 \* Evaluate whether the access permissions include write-ability.

221 \*

222 \* @param attr The k\_mem\_partition\_attr\_t object holding the

223 \* MPU attributes to be checked against write-ability.

224 \*/

[ 225](arm__mpu__v7m_8h.md#a7879968909ce2f0e33763ae1e2fc9d84)#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) \

226 ({ \

227 int \_\_is\_writable\_\_; \

228 switch (attr.rasr\_attr & MPU\_RASR\_AP\_Msk) { \

229 case P\_RW\_U\_RW\_Msk: \

230 case P\_RW\_U\_RO\_Msk: \

231 case P\_RW\_U\_NA\_Msk: \

232 \_\_is\_writable\_\_ = 1; \

233 break; \

234 default: \

235 \_\_is\_writable\_\_ = 0; \

236 } \

237 \_\_is\_writable\_\_; \

238 })

239

240/\*

241 \* @brief Evaluate Execution allowance

242 \*

243 \* Evaluate whether the access permissions include execution.

244 \*

245 \* @param attr The k\_mem\_partition\_attr\_t object holding the

246 \* MPU attributes to be checked against execution

247 \* allowance.

248 \*/

[ 249](arm__mpu__v7m_8h.md#ab6fb9b9c6c1c968a11ae80bfd70fec26)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) \

250 (!((attr.rasr\_attr) & (NOT\_EXEC)))

251

252/\* Attributes for no-cache enabling (share-ability is selected by default) \*/

253

[ 254](arm__mpu__v7m_8h.md#a0abe69d327f9f9e04781785cd1bfb634)#define K\_MEM\_PARTITION\_P\_NA\_U\_NA\_NOCACHE ((k\_mem\_partition\_attr\_t) \

255 {(\_K\_MEM\_PARTITION\_P\_NA\_U\_NA \

256 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

[ 257](arm__mpu__v7m_8h.md#afb811f7933ed0147b255c170427e0fb6)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE ((k\_mem\_partition\_attr\_t) \

258 {(\_K\_MEM\_PARTITION\_P\_RW\_U\_RW \

259 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

[ 260](arm__mpu__v7m_8h.md#acb4a60ca2e609aa9b2d4dca10d6a5fee)#define K\_MEM\_PARTITION\_P\_RW\_U\_RO\_NOCACHE ((k\_mem\_partition\_attr\_t) \

261 {(\_K\_MEM\_PARTITION\_P\_RW\_U\_RO \

262 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

[ 263](arm__mpu__v7m_8h.md#a8c982ab9a12ea1da0b7505c915832e89)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE ((k\_mem\_partition\_attr\_t) \

264 {(\_K\_MEM\_PARTITION\_P\_RW\_U\_NA \

265 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

[ 266](arm__mpu__v7m_8h.md#a840d782e977d03ed4f9ca5858f61d1a5)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE ((k\_mem\_partition\_attr\_t) \

267 {(\_K\_MEM\_PARTITION\_P\_RO\_U\_RO \

268 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

[ 269](arm__mpu__v7m_8h.md#ae47c158f93de002298e0c46a47c6337e)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE ((k\_mem\_partition\_attr\_t) \

270 {(\_K\_MEM\_PARTITION\_P\_RO\_U\_NA \

271 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

272

[ 273](arm__mpu__v7m_8h.md#a5bcd5603dda3c2825a0eca8a7d994d83)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE ((k\_mem\_partition\_attr\_t) \

274 {(\_K\_MEM\_PARTITION\_P\_RWX\_U\_RWX \

275 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

[ 276](arm__mpu__v7m_8h.md#a738443a56ab0abe8d04efa98c65763fb)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RX\_NOCACHE ((k\_mem\_partition\_attr\_t) \

277 {(\_K\_MEM\_PARTITION\_P\_RWX\_U\_RX \

278 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

[ 279](arm__mpu__v7m_8h.md#a0b22795be27057cc03e6f49d1e1e455d)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE ((k\_mem\_partition\_attr\_t) \

280 {(\_K\_MEM\_PARTITION\_P\_RX\_U\_RX \

281 | NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE)})

282

283#endif /\* \_ASMLANGUAGE \*/

284

285#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

286 BUILD\_ASSERT(!(((size) & ((size) - 1))) && \

287 (size) >= CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE && \

288 !((uint32\_t)(start) & ((size) - 1)), \

289 "the size of the partition must be power of 2" \

290 " and greater than or equal to the minimum MPU region size." \

291 "start address of the partition must align with size.")

[arm\_mpu\_region\_attr\_t](arm__mpu__v7m_8h.md#a1bf1c09c9012aa693f7ce40b7af2dae6)

struct arm\_mpu\_region\_attr arm\_mpu\_region\_attr\_t

**Definition** arm\_mpu\_v7m.h:157

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arm\_mpu\_region\_attr](structarm__mpu__region__attr.md)

**Definition** arm\_mpu\_v7m.h:152

[arm\_mpu\_region\_attr::rasr](structarm__mpu__region__attr.md#a8e38b1257bba7f67148bd7868f7cde23)

uint32\_t rasr

**Definition** arm\_mpu\_v7m.h:154

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[k\_mem\_partition\_attr\_t::rasr\_attr](structk__mem__partition__attr__t.md#a04b3fd9acde8acc4eac37a1354bd7789)

uint32\_t rasr\_attr

**Definition** arm\_mpu\_v7m.h:161

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [arm\_mpu\_v7m.h](arm__mpu__v7m_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
