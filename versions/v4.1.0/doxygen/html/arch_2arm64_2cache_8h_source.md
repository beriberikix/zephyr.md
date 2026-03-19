---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arch_2arm64_2cache_8h_source.html
original_path: doxygen/html/arch_2arm64_2cache_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h

[Go to the documentation of this file.](arch_2arm64_2cache_8h.md)

1/\*

2 \* Copyright 2022 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CACHE\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CACHE\_H\_

8

9#ifndef \_ASMLANGUAGE

10

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12#include <[zephyr/sys/util.h](sys_2util_8h.md)>

13#include <[zephyr/sys/barrier.h](sys_2barrier_8h.md)>

14#include <[zephyr/arch/cpu.h](cpu_8h.md)>

15#include <[errno.h](errno_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 21](arch_2arm64_2cache_8h.md#a67c04995b5bfa5270cc9aa15f927cdad)#define K\_CACHE\_WB BIT(0)

[ 22](arch_2arm64_2cache_8h.md#a58178f26d7c006f3219cb63d175c0480)#define K\_CACHE\_INVD BIT(1)

[ 23](arch_2arm64_2cache_8h.md#ad6ef90303e280c90786c684c839ec1e7)#define K\_CACHE\_WB\_INVD (K\_CACHE\_WB | K\_CACHE\_INVD)

24

25#if defined(CONFIG\_DCACHE)

26

27#define CTR\_EL0\_DMINLINE\_SHIFT 16

28#define CTR\_EL0\_DMINLINE\_MASK BIT\_MASK(4)

29#define CTR\_EL0\_CWG\_SHIFT 24

30#define CTR\_EL0\_CWG\_MASK BIT\_MASK(4)

31

32/\* clidr\_el1 \*/

33#define CLIDR\_EL1\_LOC\_SHIFT 24

34#define CLIDR\_EL1\_LOC\_MASK BIT\_MASK(3)

35#define CLIDR\_EL1\_CTYPE\_SHIFT(level) ((level) \* 3)

36#define CLIDR\_EL1\_CTYPE\_MASK BIT\_MASK(3)

37

38/\* ccsidr\_el1 \*/

39#define CCSIDR\_EL1\_LN\_SZ\_SHIFT 0

40#define CCSIDR\_EL1\_LN\_SZ\_MASK BIT\_MASK(3)

41#define CCSIDR\_EL1\_WAYS\_SHIFT 3

42#define CCSIDR\_EL1\_WAYS\_MASK BIT\_MASK(10)

43#define CCSIDR\_EL1\_SETS\_SHIFT 13

44#define CCSIDR\_EL1\_SETS\_MASK BIT\_MASK(15)

45

46#define dc\_ops(op, val) \

47({ \

48 \_\_asm\_\_ volatile ("dc " op ", %0" :: "r" (val) : "memory"); \

49})

50

51static size\_t dcache\_line\_size;

52

53static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) size\_t [arch\_dcache\_line\_size\_get](group__cache__arch__interface.md#ga559156a12e712c641ca62dab7433e93e)(void)

54{

55 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ctr\_el0;

56 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dminline;

57

58 if (dcache\_line\_size) {

59 return dcache\_line\_size;

60 }

61

62 ctr\_el0 = [read\_sysreg](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)(CTR\_EL0);

63

64 dminline = (ctr\_el0 >> CTR\_EL0\_DMINLINE\_SHIFT) & CTR\_EL0\_DMINLINE\_MASK;

65

66 dcache\_line\_size = 4 << dminline;

67

68 return dcache\_line\_size;

69}

70

71/\*

72 \* operation for data cache by virtual address to PoC

73 \* ops: K\_CACHE\_INVD: invalidate

74 \* K\_CACHE\_WB: clean

75 \* K\_CACHE\_WB\_INVD: clean and invalidate

76 \*/

77static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int arm64\_dcache\_range(void \*addr, size\_t size, int op)

78{

79 size\_t line\_size;

80 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start\_addr = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))addr;

81 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end\_addr = start\_addr + size;

82

83 if (op != [K\_CACHE\_INVD](arch_2arm64_2cache_8h.md#a58178f26d7c006f3219cb63d175c0480) && op != [K\_CACHE\_WB](arch_2arm64_2cache_8h.md#a67c04995b5bfa5270cc9aa15f927cdad) && op != [K\_CACHE\_WB\_INVD](arch_2arm64_2cache_8h.md#ad6ef90303e280c90786c684c839ec1e7)) {

84 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

85 }

86

87 line\_size = [arch\_dcache\_line\_size\_get](group__cache__arch__interface.md#ga559156a12e712c641ca62dab7433e93e)();

88

89 /\*

90 \* For the data cache invalidate operation, clean and invalidate

91 \* the partial cache lines at both ends of the given range to

92 \* prevent data corruption.

93 \*

94 \* For example (assume cache line size is 64 bytes):

95 \* There are 2 consecutive 32-byte buffers, which can be cached in

96 \* one line like below.

97 \* +------------------+------------------+

98 \* Cache line: | buffer 0 (dirty) | buffer 1 |

99 \* +------------------+------------------+

100 \* For the start address not aligned case, when invalidate the

101 \* buffer 1, the full cache line will be invalidated, if the buffer

102 \* 0 is dirty, its data will be lost.

103 \* The same logic applies to the not aligned end address.

104 \*/

105 if (op == [K\_CACHE\_INVD](arch_2arm64_2cache_8h.md#a58178f26d7c006f3219cb63d175c0480)) {

106 if (end\_addr & (line\_size - 1)) {

107 end\_addr &= ~(line\_size - 1);

108 dc\_ops("civac", end\_addr);

109 }

110

111 if (start\_addr & (line\_size - 1)) {

112 start\_addr &= ~(line\_size - 1);

113 if (start\_addr == end\_addr) {

114 goto done;

115 }

116 dc\_ops("civac", start\_addr);

117 start\_addr += line\_size;

118 }

119 }

120

121 /\* Align address to line size \*/

122 start\_addr &= ~(line\_size - 1);

123

124 while (start\_addr < end\_addr) {

125 if (op == [K\_CACHE\_INVD](arch_2arm64_2cache_8h.md#a58178f26d7c006f3219cb63d175c0480)) {

126 dc\_ops("ivac", start\_addr);

127 } else if (op == [K\_CACHE\_WB](arch_2arm64_2cache_8h.md#a67c04995b5bfa5270cc9aa15f927cdad)) {

128 dc\_ops("cvac", start\_addr);

129 } else if (op == [K\_CACHE\_WB\_INVD](arch_2arm64_2cache_8h.md#ad6ef90303e280c90786c684c839ec1e7)) {

130 dc\_ops("civac", start\_addr);

131 }

132

133 start\_addr += line\_size;

134 }

135

136done:

137 [barrier\_dsync\_fence\_full](group__barrier__apis.md#gaaa6909c1410bc371f59ad3eec21ee5ef)();

138

139 return 0;

140}

141

142static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4)(void)

143{

144 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

145}

146

147static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097)(void)

148{

149 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

150}

151

152static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9)(void)

153{

154 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

155}

156

157static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_flush\_range](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8)(void \*addr, size\_t size)

158{

159 return arm64\_dcache\_range(addr, size, [K\_CACHE\_WB](arch_2arm64_2cache_8h.md#a67c04995b5bfa5270cc9aa15f927cdad));

160}

161

162static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_invd\_range](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)(void \*addr, size\_t size)

163{

164 return arm64\_dcache\_range(addr, size, [K\_CACHE\_INVD](arch_2arm64_2cache_8h.md#a58178f26d7c006f3219cb63d175c0480));

165}

166

167static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_dcache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122)(void \*addr, size\_t size)

168{

169 return arm64\_dcache\_range(addr, size, [K\_CACHE\_WB\_INVD](arch_2arm64_2cache_8h.md#ad6ef90303e280c90786c684c839ec1e7));

170}

171

172static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce)(void)

173{

174 /\* nothing \*/

175}

176

177static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80)(void)

178{

179 /\* nothing \*/

180}

181

182#endif /\* CONFIG\_DCACHE \*/

183

184#if defined(CONFIG\_ICACHE)

185

186static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) size\_t [arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841)(void)

187{

188 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

189}

190

191static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7)(void)

192{

193 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

194}

195

196static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093)(void)

197{

198 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

199}

200

201static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d)(void)

202{

203 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

204}

205

206static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_flush\_range](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b)(void \*addr, size\_t size)

207{

208 ARG\_UNUSED(addr);

209 ARG\_UNUSED(size);

210 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

211}

212

213static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_invd\_range](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa)(void \*addr, size\_t size)

214{

215 ARG\_UNUSED(addr);

216 ARG\_UNUSED(size);

217 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

218}

219

220static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [arch\_icache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0)(void \*addr, size\_t size)

221{

222 ARG\_UNUSED(addr);

223 ARG\_UNUSED(size);

224 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

225}

226

227static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050)(void)

228{

229 /\* nothing \*/

230}

231

232static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971)(void)

233{

234 /\* nothing \*/

235}

236

237#endif /\* CONFIG\_ICACHE \*/

238

[ 239](arch_2arm64_2cache_8h.md#a183fd26e5a8a478562d39c6fbe6a85bc)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_cache\_init](arch_2arm64_2cache_8h.md#a183fd26e5a8a478562d39c6fbe6a85bc)(void)

240{

241}

242

243#ifdef \_\_cplusplus

244}

245#endif

246

247#endif /\* \_ASMLANGUAGE \*/

248

249#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_CACHE\_H\_ \*/

[arch\_cache\_init](arch_2arm64_2cache_8h.md#a183fd26e5a8a478562d39c6fbe6a85bc)

static ALWAYS\_INLINE void arch\_cache\_init(void)

**Definition** cache.h:239

[K\_CACHE\_INVD](arch_2arm64_2cache_8h.md#a58178f26d7c006f3219cb63d175c0480)

#define K\_CACHE\_INVD

**Definition** cache.h:22

[K\_CACHE\_WB](arch_2arm64_2cache_8h.md#a67c04995b5bfa5270cc9aa15f927cdad)

#define K\_CACHE\_WB

**Definition** cache.h:21

[K\_CACHE\_WB\_INVD](arch_2arm64_2cache_8h.md#ad6ef90303e280c90786c684c839ec1e7)

#define K\_CACHE\_WB\_INVD

**Definition** cache.h:23

[read\_sysreg](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)

#define read\_sysreg(reg)

**Definition** lib\_helpers.h:100

[cpu.h](cpu_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[barrier\_dsync\_fence\_full](group__barrier__apis.md#gaaa6909c1410bc371f59ad3eec21ee5ef)

static ALWAYS\_INLINE void barrier\_dsync\_fence\_full(void)

Full/sequentially-consistent data synchronization barrier.

**Definition** barrier.h:59

[arch\_dcache\_disable](group__cache__arch__interface.md#ga01f917f9125a5fb38d9ec4b256630a80)

void arch\_dcache\_disable(void)

Disable the d-cache.

[arch\_icache\_disable](group__cache__arch__interface.md#ga03c14fd66267240460b0a37d72a3a971)

void arch\_icache\_disable(void)

Disable the i-cache.

[arch\_dcache\_invd\_range](group__cache__arch__interface.md#ga1e12e643ba5855dd0cb67d2cc7fbb9ef)

int arch\_dcache\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the d-cache.

[arch\_icache\_flush\_and\_invd\_all](group__cache__arch__interface.md#ga29ae28d6e04ea0b136bcba5e461a7d6d)

int arch\_icache\_flush\_and\_invd\_all(void)

Flush and Invalidate the i-cache.

[arch\_icache\_flush\_all](group__cache__arch__interface.md#ga29fd1d9d9ba54306e00b6b3a393446a7)

int arch\_icache\_flush\_all(void)

Flush the i-cache.

[arch\_icache\_invd\_all](group__cache__arch__interface.md#ga2bfbf102e413fc8af43f1fd15a79a093)

int arch\_icache\_invd\_all(void)

Invalidate the i-cache.

[arch\_dcache\_flush\_range](group__cache__arch__interface.md#ga3a5b7426358790e7c54df7556bf2e6b8)

int arch\_dcache\_flush\_range(void \*addr, size\_t size)

Flush an address range in the d-cache.

[arch\_dcache\_line\_size\_get](group__cache__arch__interface.md#ga559156a12e712c641ca62dab7433e93e)

size\_t arch\_dcache\_line\_size\_get(void)

Get the d-cache line size.

[arch\_icache\_line\_size\_get](group__cache__arch__interface.md#ga717d37451103b7680bb54044d6ab1841)

size\_t arch\_icache\_line\_size\_get(void)

Get the i-cache line size.

[arch\_icache\_flush\_range](group__cache__arch__interface.md#ga7f6af61969ce97179f60ec483803500b)

int arch\_icache\_flush\_range(void \*addr, size\_t size)

Flush an address range in the i-cache.

[arch\_icache\_invd\_range](group__cache__arch__interface.md#ga84e877997349df3e53eed11be6fc3caa)

int arch\_icache\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the i-cache.

[arch\_dcache\_flush\_all](group__cache__arch__interface.md#ga9ec6cbe750133540d8f0460bfb8ca9d4)

int arch\_dcache\_flush\_all(void)

Flush the d-cache.

[arch\_icache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaa6caab419ca57523db54eb9125e7e1d0)

int arch\_icache\_flush\_and\_invd\_range(void \*addr, size\_t size)

Flush and Invalidate an address range in the i-cache.

[arch\_dcache\_flush\_and\_invd\_all](group__cache__arch__interface.md#gac58493d5f3726d7e4131c48e9a6c75f9)

int arch\_dcache\_flush\_and\_invd\_all(void)

Flush and Invalidate the d-cache.

[arch\_dcache\_invd\_all](group__cache__arch__interface.md#gacd9eed889dacd5dd42dab15b2dcc4097)

int arch\_dcache\_invd\_all(void)

Invalidate the d-cache.

[arch\_icache\_enable](group__cache__arch__interface.md#gadb5dec5f9597565f597ba5592a330050)

void arch\_icache\_enable(void)

Enable the i-cache.

[arch\_dcache\_flush\_and\_invd\_range](group__cache__arch__interface.md#gaf3afa0d36939f30a1995bf0755047122)

int arch\_dcache\_flush\_and\_invd\_range(void \*addr, size\_t size)

Flush and Invalidate an address range in the d-cache.

[arch\_dcache\_enable](group__cache__arch__interface.md#gaf616ce5134f8fd3a0fe0f690069915ce)

void arch\_dcache\_enable(void)

Enable the d-cache.

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[barrier.h](sys_2barrier_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [cache.h](arch_2arm64_2cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
