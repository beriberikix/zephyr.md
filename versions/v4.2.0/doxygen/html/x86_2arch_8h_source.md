---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/x86_2arch_8h_source.html
original_path: doxygen/html/x86_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](x86_2arch_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corp.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_H\_

17

18#include <[zephyr/devicetree.h](devicetree_8h.md)>

19

20/\* Changing this value will require manual changes to exception and IDT setup

21 \* in locore.S for intel64

22 \*/

23#define Z\_X86\_OOPS\_VECTOR 32

24

25#if !defined(\_ASMLANGUAGE)

26

27#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29#include <stddef.h>

30#include <[stdbool.h](stdbool_8h.md)>

31#include <[zephyr/irq.h](irq_8h.md)>

32#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h.md)>

33#include <[zephyr/arch/x86/thread\_stack.h](arch_2x86_2thread__stack_8h.md)>

34#include <[zephyr/linker/sections.h](sections_8h.md)>

35

36#ifdef \_\_cplusplus

37extern "C" {

38#endif

39

40#ifdef CONFIG\_PCIE\_MSI

41

42struct x86\_msi\_vector {

43 unsigned int irq;

44 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vector;

45#ifdef CONFIG\_INTEL\_VTD\_ICTL

46 bool remap;

47 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte;

48#endif

49};

50

51typedef struct x86\_msi\_vector arch\_msi\_vector\_t;

52

53#endif /\* CONFIG\_PCIE\_MSI \*/

54

[ 55](x86_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

56{

57 if ((key & 0x00000200U) != 0U) { /\* 'IF' bit \*/

58 \_\_asm\_\_ volatile ("sti" ::: "memory");

59 }

60}

61

[ 62](x86_2arch_8h.md#a4eb1822b6af401aef41646d01f900733)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_out8](x86_2arch_8h.md#a4eb1822b6af401aef41646d01f900733)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

63{

64 \_\_asm\_\_ volatile("outb %b0, %w1" :: "a"(data), "Nd"(port));

65}

66

[ 67](x86_2arch_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_in8](x86_2arch_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

68{

69 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ret;

70

71 \_\_asm\_\_ volatile("inb %w1, %b0" : "=a"(ret) : "Nd"(port));

72

73 return ret;

74}

75

[ 76](x86_2arch_8h.md#a8700f40b9c9951083b9a729b7e50f47d)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_out16](x86_2arch_8h.md#a8700f40b9c9951083b9a729b7e50f47d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

77{

78 \_\_asm\_\_ volatile("outw %w0, %w1" :: "a"(data), "Nd"(port));

79}

80

[ 81](x86_2arch_8h.md#ab9823ccf71d78cbb0316e9c335081f6d)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_in16](x86_2arch_8h.md#ab9823ccf71d78cbb0316e9c335081f6d)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

82{

83 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret;

84

85 \_\_asm\_\_ volatile("inw %w1, %w0" : "=a"(ret) : "Nd"(port));

86

87 return ret;

88}

89

[ 90](x86_2arch_8h.md#ae60822b265f38b57b70a2925996aaa88)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_out32](x86_2arch_8h.md#ae60822b265f38b57b70a2925996aaa88)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

91{

92 \_\_asm\_\_ volatile("outl %0, %w1" :: "a"(data), "Nd"(port));

93}

94

[ 95](x86_2arch_8h.md#af89948c04bd432f5fa14319f29d06968)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_in32](x86_2arch_8h.md#af89948c04bd432f5fa14319f29d06968)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

96{

97 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

98

99 \_\_asm\_\_ volatile("inl %w1, %0" : "=a"(ret) : "Nd"(port));

100

101 return ret;

102}

103

[ 104](x86_2arch_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write8](x86_2arch_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

105{

106 \_\_asm\_\_ volatile("movb %0, %1"

107 :

108 : "q"(data), "m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

109 : "memory");

110}

111

[ 112](x86_2arch_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_read8](x86_2arch_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

113{

114 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ret;

115

116 \_\_asm\_\_ volatile("movb %1, %0"

117 : "=q"(ret)

118 : "m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

119 : "memory");

120

121 return ret;

122}

123

[ 124](x86_2arch_8h.md#abacfedeea46690ae169b9636a94cfa5a)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write16](x86_2arch_8h.md#abacfedeea46690ae169b9636a94cfa5a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

125{

126 \_\_asm\_\_ volatile("movw %0, %1"

127 :

128 : "r"(data), "m" (\*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

129 : "memory");

130}

131

[ 132](x86_2arch_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_read16](x86_2arch_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

133{

134 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret;

135

136 \_\_asm\_\_ volatile("movw %1, %0"

137 : "=r"(ret)

138 : "m" (\*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

139 : "memory");

140

141 return ret;

142}

143

[ 144](x86_2arch_8h.md#ae9b07f6441d8496a44a189b88cf061c6)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write32](x86_2arch_8h.md#ae9b07f6441d8496a44a189b88cf061c6)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

145{

146 \_\_asm\_\_ volatile("movl %0, %1"

147 :

148 : "r"(data), "m" (\*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

149 : "memory");

150}

151

[ 152](x86_2arch_8h.md#a63b36c1442f805db4d1bc5a51a035c42)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_read32](x86_2arch_8h.md#a63b36c1442f805db4d1bc5a51a035c42)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

153{

154 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

155

156 \_\_asm\_\_ volatile("movl %1, %0"

157 : "=r"(ret)

158 : "m" (\*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

159 : "memory");

160

161 return ret;

162}

163

[ 164](x86_2arch_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_set\_bit](x86_2arch_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

165{

166 \_\_asm\_\_ volatile("btsl %1, %0"

167 : "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

168 : "Ir" (bit)

169 : "memory");

170}

171

[ 172](x86_2arch_8h.md#a3a7b18493a4a34f82c9409453277265d)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_clear\_bit](x86_2arch_8h.md#a3a7b18493a4a34f82c9409453277265d)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

173{

174 \_\_asm\_\_ volatile("btrl %1, %0"

175 : "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

176 : "Ir" (bit));

177}

178

[ 179](x86_2arch_8h.md#a43a2682b576dd69995dfdd203134f2a6)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_test\_bit](x86_2arch_8h.md#a43a2682b576dd69995dfdd203134f2a6)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

180{

181 int ret;

182

183 \_\_asm\_\_ volatile("btl %2, %1;"

184 "sbb %0, %0"

185 : "=r" (ret), "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

186 : "Ir" (bit));

187

188 return ret;

189}

190

[ 191](x86_2arch_8h.md#a036f93e32f1d1cc34cb2df3193650d48)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_test\_and\_set\_bit](x86_2arch_8h.md#a036f93e32f1d1cc34cb2df3193650d48)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr,

192 unsigned int bit)

193{

194 int ret;

195

196 \_\_asm\_\_ volatile("btsl %2, %1;"

197 "sbb %0, %0"

198 : "=r" (ret), "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

199 : "Ir" (bit));

200

201 return ret;

202}

203

[ 204](x86_2arch_8h.md#accf2bc65402198dda9d43ccd788163c6)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_test\_and\_clear\_bit](x86_2arch_8h.md#accf2bc65402198dda9d43ccd788163c6)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr,

205 unsigned int bit)

206{

207 int ret;

208

209 \_\_asm\_\_ volatile("btrl %2, %1;"

210 "sbb %0, %0"

211 : "=r" (ret), "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

212 : "Ir" (bit));

213

214 return ret;

215}

216

[ 217](x86_2arch_8h.md#a185a9d6bf53f3e815f6385c3f500f4fc)#define sys\_bitfield\_set\_bit sys\_set\_bit

[ 218](x86_2arch_8h.md#a7167fa52e3fb5416c93527fea091c446)#define sys\_bitfield\_clear\_bit sys\_clear\_bit

[ 219](x86_2arch_8h.md#a6547612936cc24eae4ff0217ea654c4d)#define sys\_bitfield\_test\_bit sys\_test\_bit

[ 220](x86_2arch_8h.md#aa770dbc8057ea68ed43b5eac0db9b390)#define sys\_bitfield\_test\_and\_set\_bit sys\_test\_and\_set\_bit

[ 221](x86_2arch_8h.md#ab27f26cae6ce9e528d078fd49b9b4952)#define sys\_bitfield\_test\_and\_clear\_bit sys\_test\_and\_clear\_bit

222

223/\*

224 \* Map of IRQ numbers to their assigned vectors. On IA32, this is generated

225 \* at build time and defined via the linker script. On Intel64, it's an array.

226 \*/

227

228extern unsigned char \_irq\_to\_interrupt\_vector[CONFIG\_MAX\_IRQ\_LINES];

229

230#define Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq) \

231 ((unsigned int) \_irq\_to\_interrupt\_vector[(irq)])

232

233

234#endif /\* \_ASMLANGUAGE \*/

235

236#ifdef \_\_cplusplus

237}

238#endif

239

240#include <[zephyr/drivers/interrupt\_controller/sysapic.h](sysapic_8h.md)>

241

242#ifdef CONFIG\_X86\_64

243#include <[zephyr/arch/x86/intel64/arch.h](x86_2intel64_2arch_8h.md)>

244#else

245#include <[zephyr/arch/x86/ia32/arch.h](x86_2ia32_2arch_8h.md)>

246#endif

247

248#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

249

250#ifdef \_\_cplusplus

251extern "C" {

252#endif

253

254#ifndef \_ASMLANGUAGE

255

[ 256](x86_2arch_8h.md#aa278d630653b33cb339621d725ed295a)void [arch\_irq\_enable](arch_2arm_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 257](x86_2arch_8h.md#a216d692e87bfba955a60f8e570e127df)void [arch\_irq\_disable](arch_2arm_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

258

[ 259](x86_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

260

261\_\_pinned\_func

[ 262](x86_2arch_8h.md#ad9de4b80c686a0cef1275e79fa755281)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

263{

264 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

265}

266

[ 267](x86_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

268

269\_\_pinned\_func

[ 270](x86_2arch_8h.md#a5f1c7486a4a76135dcec432198238167)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

271{

272 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

273}

274

[ 275](x86_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

276{

277 return (key & 0x200) != 0;

278}

279

283

284static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_do\_read\_cpu\_timestamp32(void)

285{

286 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rv;

287

288 \_\_asm\_\_ volatile("rdtsc" : "=a" (rv) : : "%edx");

289

290 return rv;

291}

292

296

297\_\_pinned\_func

298static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_tsc\_read(void)

299{

300 union {

301 struct {

302 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lo;

303 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hi](asm-macro-32-bit-gnu_8h.md#a0ef89636f8d03ae88717291e66d59527);

304 };

305 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value;

306 } rv;

307

308#ifdef CONFIG\_X86\_64

309 /\*

310 \* According to Intel 64 and IA-32 Architectures Software

311 \* Developer’s Manual, volume 3, chapter 8.2.5, LFENCE provides

312 \* a more efficient method of controlling memory ordering than

313 \* the CPUID instruction. So use LFENCE here, as all 64-bit

314 \* CPUs have LFENCE.

315 \*/

316 \_\_asm\_\_ volatile ("lfence");

317#else

318 /\* rdtsc & cpuid clobbers eax, ebx, ecx and edx registers \*/

319 \_\_asm\_\_ volatile (/\* serialize \*/

320 "xorl %%eax,%%eax;"

321 "cpuid"

322 :

323 :

324 : "%eax", "%ebx", "%ecx", "%edx"

325 );

326#endif

327

328#ifdef CONFIG\_X86\_64

329 /\*

330 \* We cannot use "=A", since this would use %rax on x86\_64 and

331 \* return only the lower 32bits of the TSC

332 \*/

333 \_\_asm\_\_ volatile ("rdtsc" : "=a" (rv.lo), "=d" (rv.hi));

334#else

335 /\* "=A" means that value is in eax:edx pair. \*/

336 \_\_asm\_\_ volatile ("rdtsc" : "=A" (rv.value));

337#endif

338

339 return rv.value;

340}

341

[ 342](x86_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

343{

344 \_\_asm\_\_ volatile("nop");

345}

346

347#endif /\* \_ASMLANGUAGE \*/

348

349#ifdef \_\_cplusplus

350}

351#endif

352

353#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_H\_ \*/

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[arch\_irq\_disable](arch_2arm_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:44

[arch\_irq\_enable](arch_2arm_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:43

[thread\_stack.h](arch_2x86_2thread__stack_8h.md)

[hi](asm-macro-32-bit-gnu_8h.md#a0ef89636f8d03ae88717291e66d59527)

irp hi

**Definition** asm-macro-32-bit-gnu.h:10

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[types.h](include_2zephyr_2types_8h.md)

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** arch.h:83

[sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)

uint64\_t sys\_clock\_cycle\_get\_64(void)

[sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)

uint32\_t sys\_clock\_cycle\_get\_32(void)

[arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

**Definition** arch.h:108

[arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

**Definition** arch.h:115

[arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** arch.h:96

[mmustructs.h](mmustructs_8h.md)

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[sys\_io.h](sys_2sys__io_8h.md)

[io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86)

uint32\_t io\_port\_t

**Definition** sys\_io.h:19

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

[mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d)

uintptr\_t mem\_addr\_t

**Definition** sys\_io.h:21

[sysapic.h](sysapic_8h.md)

[sys\_test\_and\_set\_bit](x86_2arch_8h.md#a036f93e32f1d1cc34cb2df3193650d48)

static ALWAYS\_INLINE int sys\_test\_and\_set\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:191

[sys\_set\_bit](x86_2arch_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)

static ALWAYS\_INLINE void sys\_set\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:164

[sys\_in8](x86_2arch_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174)

static ALWAYS\_INLINE uint8\_t sys\_in8(io\_port\_t port)

**Definition** arch.h:67

[sys\_write8](x86_2arch_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)

static ALWAYS\_INLINE void sys\_write8(uint8\_t data, mm\_reg\_t addr)

**Definition** arch.h:104

[sys\_clear\_bit](x86_2arch_8h.md#a3a7b18493a4a34f82c9409453277265d)

static ALWAYS\_INLINE void sys\_clear\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:172

[sys\_test\_bit](x86_2arch_8h.md#a43a2682b576dd69995dfdd203134f2a6)

static ALWAYS\_INLINE int sys\_test\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:179

[sys\_out8](x86_2arch_8h.md#a4eb1822b6af401aef41646d01f900733)

static ALWAYS\_INLINE void sys\_out8(uint8\_t data, io\_port\_t port)

**Definition** arch.h:62

[sys\_read32](x86_2arch_8h.md#a63b36c1442f805db4d1bc5a51a035c42)

static ALWAYS\_INLINE uint32\_t sys\_read32(mm\_reg\_t addr)

**Definition** arch.h:152

[sys\_out16](x86_2arch_8h.md#a8700f40b9c9951083b9a729b7e50f47d)

static ALWAYS\_INLINE void sys\_out16(uint16\_t data, io\_port\_t port)

**Definition** arch.h:76

[sys\_read16](x86_2arch_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)

static ALWAYS\_INLINE uint16\_t sys\_read16(mm\_reg\_t addr)

**Definition** arch.h:132

[sys\_in16](x86_2arch_8h.md#ab9823ccf71d78cbb0316e9c335081f6d)

static ALWAYS\_INLINE uint16\_t sys\_in16(io\_port\_t port)

**Definition** arch.h:81

[sys\_write16](x86_2arch_8h.md#abacfedeea46690ae169b9636a94cfa5a)

static ALWAYS\_INLINE void sys\_write16(uint16\_t data, mm\_reg\_t addr)

**Definition** arch.h:124

[sys\_test\_and\_clear\_bit](x86_2arch_8h.md#accf2bc65402198dda9d43ccd788163c6)

static ALWAYS\_INLINE int sys\_test\_and\_clear\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:204

[sys\_read8](x86_2arch_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)

static ALWAYS\_INLINE uint8\_t sys\_read8(mm\_reg\_t addr)

**Definition** arch.h:112

[sys\_out32](x86_2arch_8h.md#ae60822b265f38b57b70a2925996aaa88)

static ALWAYS\_INLINE void sys\_out32(uint32\_t data, io\_port\_t port)

**Definition** arch.h:90

[sys\_write32](x86_2arch_8h.md#ae9b07f6441d8496a44a189b88cf061c6)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mm\_reg\_t addr)

**Definition** arch.h:144

[sys\_in32](x86_2arch_8h.md#af89948c04bd432f5fa14319f29d06968)

static ALWAYS\_INLINE uint32\_t sys\_in32(io\_port\_t port)

**Definition** arch.h:95

[arch.h](x86_2ia32_2arch_8h.md)

IA-32 specific kernel interface header.

[arch.h](x86_2intel64_2arch_8h.md)

Intel-64 specific kernel interface header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [arch.h](x86_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
