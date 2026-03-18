---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/x86_2arch_8h_source.html
original_path: doxygen/html/x86_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_H\_

8

9#include <[zephyr/devicetree.h](devicetree_8h.md)>

10

11/\* Changing this value will require manual changes to exception and IDT setup

12 \* in locore.S for intel64

13 \*/

14#define Z\_X86\_OOPS\_VECTOR 32

15

16#if !defined(\_ASMLANGUAGE)

17

18#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <stddef.h>

21#include <[stdbool.h](stdbool_8h.md)>

22#include <[zephyr/irq.h](irq_8h.md)>

23#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h.md)>

24#include <[zephyr/arch/x86/thread\_stack.h](arch_2x86_2thread__stack_8h.md)>

25#include <[zephyr/linker/sections.h](sections_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

31#ifdef CONFIG\_PCIE\_MSI

32

33struct x86\_msi\_vector {

34 unsigned int irq;

35 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vector;

36#ifdef CONFIG\_INTEL\_VTD\_ICTL

37 bool remap;

38 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte;

39#endif

40};

41

42typedef struct x86\_msi\_vector arch\_msi\_vector\_t;

43

44#endif /\* CONFIG\_PCIE\_MSI \*/

45

[ 46](x86_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

47{

48 if ((key & 0x00000200U) != 0U) { /\* 'IF' bit \*/

49 \_\_asm\_\_ volatile ("sti" ::: "memory");

50 }

51}

52

[ 53](x86_2arch_8h.md#a4eb1822b6af401aef41646d01f900733)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_out8](x86_2arch_8h.md#a4eb1822b6af401aef41646d01f900733)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

54{

55 \_\_asm\_\_ volatile("outb %b0, %w1" :: "a"(data), "Nd"(port));

56}

57

[ 58](x86_2arch_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_in8](x86_2arch_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

59{

60 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ret;

61

62 \_\_asm\_\_ volatile("inb %w1, %b0" : "=a"(ret) : "Nd"(port));

63

64 return ret;

65}

66

[ 67](x86_2arch_8h.md#a8700f40b9c9951083b9a729b7e50f47d)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_out16](x86_2arch_8h.md#a8700f40b9c9951083b9a729b7e50f47d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

68{

69 \_\_asm\_\_ volatile("outw %w0, %w1" :: "a"(data), "Nd"(port));

70}

71

[ 72](x86_2arch_8h.md#ab9823ccf71d78cbb0316e9c335081f6d)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_in16](x86_2arch_8h.md#ab9823ccf71d78cbb0316e9c335081f6d)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

73{

74 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret;

75

76 \_\_asm\_\_ volatile("inw %w1, %w0" : "=a"(ret) : "Nd"(port));

77

78 return ret;

79}

80

[ 81](x86_2arch_8h.md#ae60822b265f38b57b70a2925996aaa88)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_out32](x86_2arch_8h.md#ae60822b265f38b57b70a2925996aaa88)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

82{

83 \_\_asm\_\_ volatile("outl %0, %w1" :: "a"(data), "Nd"(port));

84}

85

[ 86](x86_2arch_8h.md#af89948c04bd432f5fa14319f29d06968)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_in32](x86_2arch_8h.md#af89948c04bd432f5fa14319f29d06968)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

87{

88 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

89

90 \_\_asm\_\_ volatile("inl %w1, %0" : "=a"(ret) : "Nd"(port));

91

92 return ret;

93}

94

[ 95](x86_2arch_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write8](x86_2arch_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

96{

97 \_\_asm\_\_ volatile("movb %0, %1"

98 :

99 : "q"(data), "m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

100 : "memory");

101}

102

[ 103](x86_2arch_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_read8](x86_2arch_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

104{

105 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ret;

106

107 \_\_asm\_\_ volatile("movb %1, %0"

108 : "=q"(ret)

109 : "m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

110 : "memory");

111

112 return ret;

113}

114

[ 115](x86_2arch_8h.md#abacfedeea46690ae169b9636a94cfa5a)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write16](x86_2arch_8h.md#abacfedeea46690ae169b9636a94cfa5a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

116{

117 \_\_asm\_\_ volatile("movw %0, %1"

118 :

119 : "r"(data), "m" (\*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

120 : "memory");

121}

122

[ 123](x86_2arch_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_read16](x86_2arch_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

124{

125 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret;

126

127 \_\_asm\_\_ volatile("movw %1, %0"

128 : "=r"(ret)

129 : "m" (\*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

130 : "memory");

131

132 return ret;

133}

134

[ 135](x86_2arch_8h.md#ae9b07f6441d8496a44a189b88cf061c6)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write32](x86_2arch_8h.md#ae9b07f6441d8496a44a189b88cf061c6)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

136{

137 \_\_asm\_\_ volatile("movl %0, %1"

138 :

139 : "r"(data), "m" (\*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

140 : "memory");

141}

142

[ 143](x86_2arch_8h.md#a63b36c1442f805db4d1bc5a51a035c42)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_read32](x86_2arch_8h.md#a63b36c1442f805db4d1bc5a51a035c42)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

144{

145 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

146

147 \_\_asm\_\_ volatile("movl %1, %0"

148 : "=r"(ret)

149 : "m" (\*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

150 : "memory");

151

152 return ret;

153}

154

[ 155](x86_2arch_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_set\_bit](x86_2arch_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

156{

157 \_\_asm\_\_ volatile("btsl %1, %0"

158 : "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

159 : "Ir" (bit)

160 : "memory");

161}

162

[ 163](x86_2arch_8h.md#a3a7b18493a4a34f82c9409453277265d)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_clear\_bit](x86_2arch_8h.md#a3a7b18493a4a34f82c9409453277265d)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

164{

165 \_\_asm\_\_ volatile("btrl %1, %0"

166 : "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

167 : "Ir" (bit));

168}

169

[ 170](x86_2arch_8h.md#a43a2682b576dd69995dfdd203134f2a6)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_test\_bit](x86_2arch_8h.md#a43a2682b576dd69995dfdd203134f2a6)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, unsigned int bit)

171{

172 int ret;

173

174 \_\_asm\_\_ volatile("btl %2, %1;"

175 "sbb %0, %0"

176 : "=r" (ret), "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

177 : "Ir" (bit));

178

179 return ret;

180}

181

[ 182](x86_2arch_8h.md#a036f93e32f1d1cc34cb2df3193650d48)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_test\_and\_set\_bit](x86_2arch_8h.md#a036f93e32f1d1cc34cb2df3193650d48)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr,

183 unsigned int bit)

184{

185 int ret;

186

187 \_\_asm\_\_ volatile("btsl %2, %1;"

188 "sbb %0, %0"

189 : "=r" (ret), "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

190 : "Ir" (bit));

191

192 return ret;

193}

194

[ 195](x86_2arch_8h.md#accf2bc65402198dda9d43ccd788163c6)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int [sys\_test\_and\_clear\_bit](x86_2arch_8h.md#accf2bc65402198dda9d43ccd788163c6)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr,

196 unsigned int bit)

197{

198 int ret;

199

200 \_\_asm\_\_ volatile("btrl %2, %1;"

201 "sbb %0, %0"

202 : "=r" (ret), "+m" (\*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*) (addr))

203 : "Ir" (bit));

204

205 return ret;

206}

207

[ 208](x86_2arch_8h.md#a185a9d6bf53f3e815f6385c3f500f4fc)#define sys\_bitfield\_set\_bit sys\_set\_bit

[ 209](x86_2arch_8h.md#a7167fa52e3fb5416c93527fea091c446)#define sys\_bitfield\_clear\_bit sys\_clear\_bit

[ 210](x86_2arch_8h.md#a6547612936cc24eae4ff0217ea654c4d)#define sys\_bitfield\_test\_bit sys\_test\_bit

[ 211](x86_2arch_8h.md#aa770dbc8057ea68ed43b5eac0db9b390)#define sys\_bitfield\_test\_and\_set\_bit sys\_test\_and\_set\_bit

[ 212](x86_2arch_8h.md#ab27f26cae6ce9e528d078fd49b9b4952)#define sys\_bitfield\_test\_and\_clear\_bit sys\_test\_and\_clear\_bit

213

214/\*

215 \* Map of IRQ numbers to their assigned vectors. On IA32, this is generated

216 \* at build time and defined via the linker script. On Intel64, it's an array.

217 \*/

218

219extern unsigned char \_irq\_to\_interrupt\_vector[];

220

221#define Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq) \

222 ((unsigned int) \_irq\_to\_interrupt\_vector[irq])

223

224

225#endif /\* \_ASMLANGUAGE \*/

226

227#ifdef \_\_cplusplus

228}

229#endif

230

231#include <[zephyr/drivers/interrupt\_controller/sysapic.h](sysapic_8h.md)>

232

233#ifdef CONFIG\_X86\_64

234#include <[zephyr/arch/x86/intel64/arch.h](x86_2intel64_2arch_8h.md)>

235#else

236#include <[zephyr/arch/x86/ia32/arch.h](x86_2ia32_2arch_8h.md)>

237#endif

238

239#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

240

241#ifdef \_\_cplusplus

242extern "C" {

243#endif

244

245#ifndef \_ASMLANGUAGE

246

[ 247](x86_2arch_8h.md#aa278d630653b33cb339621d725ed295a)extern void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 248](x86_2arch_8h.md#a216d692e87bfba955a60f8e570e127df)extern void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

249

[ 250](x86_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

251

252\_\_pinned\_func

[ 253](x86_2arch_8h.md#ad9de4b80c686a0cef1275e79fa755281)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

254{

255 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

256}

257

[ 258](x86_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

259

260\_\_pinned\_func

[ 261](x86_2arch_8h.md#a5f1c7486a4a76135dcec432198238167)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

262{

263 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

264}

265

[ 266](x86_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

267{

268 return (key & 0x200) != 0;

269}

270

274

275static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_do\_read\_cpu\_timestamp32(void)

276{

277 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rv;

278

279 \_\_asm\_\_ volatile("rdtsc" : "=a" (rv) : : "%edx");

280

281 return rv;

282}

283

287

288\_\_pinned\_func

289static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) z\_tsc\_read(void)

290{

291 union {

292 struct {

293 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lo;

294 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hi](asm-macro-32-bit-gnu_8h.md#a0ef89636f8d03ae88717291e66d59527);

295 };

296 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value;

297 } rv;

298

299#ifdef CONFIG\_X86\_64

300 /\*

301 \* According to Intel 64 and IA-32 Architectures Software

302 \* Developer’s Manual, volume 3, chapter 8.2.5, LFENCE provides

303 \* a more efficient method of controlling memory ordering than

304 \* the CPUID instruction. So use LFENCE here, as all 64-bit

305 \* CPUs have LFENCE.

306 \*/

307 \_\_asm\_\_ volatile ("lfence");

308#else

309 /\* rdtsc & cpuid clobbers eax, ebx, ecx and edx registers \*/

310 \_\_asm\_\_ volatile (/\* serialize \*/

311 "xorl %%eax,%%eax;"

312 "cpuid"

313 :

314 :

315 : "%eax", "%ebx", "%ecx", "%edx"

316 );

317#endif

318

319#ifdef CONFIG\_X86\_64

320 /\*

321 \* We cannot use "=A", since this would use %rax on x86\_64 and

322 \* return only the lower 32bits of the TSC

323 \*/

324 \_\_asm\_\_ volatile ("rdtsc" : "=a" (rv.lo), "=d" (rv.hi));

325#else

326 /\* "=A" means that value is in eax:edx pair. \*/

327 \_\_asm\_\_ volatile ("rdtsc" : "=A" (rv.value));

328#endif

329

330 return rv.value;

331}

332

[ 333](x86_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

334{

335 \_\_asm\_\_ volatile("nop");

336}

337

338#endif /\* \_ASMLANGUAGE \*/

339

340#ifdef \_\_cplusplus

341}

342#endif

343

344#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_ARCH\_H\_ \*/

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[thread\_stack.h](arch_2x86_2thread__stack_8h.md)

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:107

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:106

[hi](asm-macro-32-bit-gnu_8h.md#a0ef89636f8d03ae88717291e66d59527)

irp hi

**Definition** asm-macro-32-bit-gnu.h:10

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** arch.h:74

[sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)

uint64\_t sys\_clock\_cycle\_get\_64(void)

[sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)

uint32\_t sys\_clock\_cycle\_get\_32(void)

[arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

**Definition** arch.h:99

[arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

**Definition** arch.h:106

[arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** arch.h:87

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

**Definition** arch.h:182

[sys\_set\_bit](x86_2arch_8h.md#a04ab5115c17cc5ddfe2d788cb7bdcbbe)

static ALWAYS\_INLINE void sys\_set\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:155

[sys\_in8](x86_2arch_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174)

static ALWAYS\_INLINE uint8\_t sys\_in8(io\_port\_t port)

**Definition** arch.h:58

[sys\_write8](x86_2arch_8h.md#a3a565a29eb41eaf472034c9aaf49cc19)

static ALWAYS\_INLINE void sys\_write8(uint8\_t data, mm\_reg\_t addr)

**Definition** arch.h:95

[sys\_clear\_bit](x86_2arch_8h.md#a3a7b18493a4a34f82c9409453277265d)

static ALWAYS\_INLINE void sys\_clear\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:163

[sys\_test\_bit](x86_2arch_8h.md#a43a2682b576dd69995dfdd203134f2a6)

static ALWAYS\_INLINE int sys\_test\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:170

[sys\_out8](x86_2arch_8h.md#a4eb1822b6af401aef41646d01f900733)

static ALWAYS\_INLINE void sys\_out8(uint8\_t data, io\_port\_t port)

**Definition** arch.h:53

[sys\_read32](x86_2arch_8h.md#a63b36c1442f805db4d1bc5a51a035c42)

static ALWAYS\_INLINE uint32\_t sys\_read32(mm\_reg\_t addr)

**Definition** arch.h:143

[sys\_out16](x86_2arch_8h.md#a8700f40b9c9951083b9a729b7e50f47d)

static ALWAYS\_INLINE void sys\_out16(uint16\_t data, io\_port\_t port)

**Definition** arch.h:67

[sys\_read16](x86_2arch_8h.md#ab64ad3252d531096bc6ee1e1282d7e72)

static ALWAYS\_INLINE uint16\_t sys\_read16(mm\_reg\_t addr)

**Definition** arch.h:123

[sys\_in16](x86_2arch_8h.md#ab9823ccf71d78cbb0316e9c335081f6d)

static ALWAYS\_INLINE uint16\_t sys\_in16(io\_port\_t port)

**Definition** arch.h:72

[sys\_write16](x86_2arch_8h.md#abacfedeea46690ae169b9636a94cfa5a)

static ALWAYS\_INLINE void sys\_write16(uint16\_t data, mm\_reg\_t addr)

**Definition** arch.h:115

[sys\_test\_and\_clear\_bit](x86_2arch_8h.md#accf2bc65402198dda9d43ccd788163c6)

static ALWAYS\_INLINE int sys\_test\_and\_clear\_bit(mem\_addr\_t addr, unsigned int bit)

**Definition** arch.h:195

[sys\_read8](x86_2arch_8h.md#ae0bbb10d24303e1d8505cbf373a1bcfb)

static ALWAYS\_INLINE uint8\_t sys\_read8(mm\_reg\_t addr)

**Definition** arch.h:103

[sys\_out32](x86_2arch_8h.md#ae60822b265f38b57b70a2925996aaa88)

static ALWAYS\_INLINE void sys\_out32(uint32\_t data, io\_port\_t port)

**Definition** arch.h:81

[sys\_write32](x86_2arch_8h.md#ae9b07f6441d8496a44a189b88cf061c6)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mm\_reg\_t addr)

**Definition** arch.h:135

[sys\_in32](x86_2arch_8h.md#af89948c04bd432f5fa14319f29d06968)

static ALWAYS\_INLINE uint32\_t sys\_in32(io\_port\_t port)

**Definition** arch.h:86

[arch.h](x86_2ia32_2arch_8h.md)

IA-32 specific kernel interface header This header contains the IA-32 specific kernel interface.

[arch.h](x86_2intel64_2arch_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [arch.h](x86_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
