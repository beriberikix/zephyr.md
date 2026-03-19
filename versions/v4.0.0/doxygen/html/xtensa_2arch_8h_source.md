---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/xtensa_2arch_8h_source.html
original_path: doxygen/html/xtensa_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](xtensa_2arch_8h.md)

1/\*

2 \* Copyright (c) 2016 Cadence Design Systems, Inc.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

12

13#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_ARCH\_H\_

14#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_ARCH\_H\_

15

16#include <[zephyr/irq.h](irq_8h.md)>

17

18#include <[zephyr/devicetree.h](devicetree_8h.md)>

19#if !defined(\_ASMLANGUAGE) && !defined(\_\_ASSEMBLER\_\_)

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21#include <[zephyr/toolchain.h](toolchain_8h.md)>

22#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

23#include <[zephyr/arch/common/sys\_io.h](arch_2common_2sys__io_8h.md)>

24#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

25#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

26#include <[zephyr/arch/xtensa/syscall.h](arch_2xtensa_2syscall_8h.md)>

27#include <[zephyr/arch/xtensa/thread.h](arch_2xtensa_2thread_8h.md)>

28#include <[zephyr/arch/xtensa/irq.h](arch_2xtensa_2irq_8h.md)>

29#include <xtensa/config/core.h>

30#include <[zephyr/arch/common/addr\_types.h](addr__types_8h.md)>

31#include <[zephyr/arch/xtensa/gdbstub.h](arch_2xtensa_2gdbstub_8h.md)>

32#include <[zephyr/debug/sparse.h](sparse_8h.md)>

33#include <[zephyr/arch/xtensa/thread\_stack.h](arch_2xtensa_2thread__stack_8h.md)>

34#include <[zephyr/sys/slist.h](slist_8h.md)>

35

36#include <[zephyr/drivers/timer/system\_timer.h](system__timer_8h.md)>

37

38#ifdef CONFIG\_XTENSA\_MMU

39#include <[zephyr/arch/xtensa/xtensa\_mmu.h](xtensa__mmu_8h.md)>

40#endif

41

42#ifdef CONFIG\_XTENSA\_MPU

43#include <[zephyr/arch/xtensa/mpu.h](xtensa_2mpu_8h.md)>

44#endif

45

57

58#include <[zephyr/arch/xtensa/exception.h](xtensa_2exception_8h.md)>

59

60#ifdef \_\_cplusplus

61extern "C" {

62#endif

63

64struct [arch\_mem\_domain](structarch__mem__domain.md) {

65#ifdef CONFIG\_XTENSA\_MMU

66 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[ptables](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6);

67 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) asid;

68 bool dirty;

69#endif

70#ifdef CONFIG\_XTENSA\_MPU

71 struct xtensa\_mpu\_map mpu\_map;

72#endif

73 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5);

74};

75

[ 83](xtensa_2arch_8h.md#a789f894256925071f3448cda889abcf5)void [xtensa\_arch\_except](xtensa_2arch_8h.md#a789f894256925071f3448cda889abcf5)(int reason\_p);

84

[ 93](xtensa_2arch_8h.md#a31f0ccadfc2a2afa0e985d74a0e4c2e9)void [xtensa\_arch\_kernel\_oops](xtensa_2arch_8h.md#a31f0ccadfc2a2afa0e985d74a0e4c2e9)(int reason\_p, void \*ssf);

94

95#ifdef CONFIG\_USERSPACE

96

[ 97](xtensa_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

98 if (k\_is\_user\_context()) { \

99 arch\_syscall\_invoke1(reason\_p, \

100 K\_SYSCALL\_XTENSA\_USER\_FAULT); \

101 } else { \

102 xtensa\_arch\_except(reason\_p); \

103 } \

104 CODE\_UNREACHABLE; \

105} while (false)

106

107#else

108

109#define ARCH\_EXCEPT(reason\_p) do { \

110 xtensa\_arch\_except(reason\_p); \

111 CODE\_UNREACHABLE; \

112 } while (false)

113

114#endif

115

[ 116](xtensa_2arch_8h.md#a0890b1717c7f7b93644c69a3293b7da8)\_\_syscall void [xtensa\_user\_fault](xtensa_2arch_8h.md#a0890b1717c7f7b93644c69a3293b7da8)(unsigned int reason);

117

118#include <zephyr/syscalls/arch.h>

119

120/\* internal routine documented in C file, needed by IRQ\_CONNECT() macro \*/

121void z\_irq\_priority\_set([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

122

[ 123](xtensa_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

124 { \

125 Z\_ISR\_DECLARE(irq\_p, flags\_p, isr\_p, isr\_param\_p); \

126 }

127

[ 129](xtensa_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

130{

131 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

132}

133

[ 135](xtensa_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

136{

137 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

138}

139

[ 141](xtensa_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

142{

143 \_\_asm\_\_ volatile("nop");

144}

145

[ 154](xtensa_2arch_8h.md#ac14ee42f2f373cf48fa30a60f3aafc39)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [xtensa\_vecbase\_lock](xtensa_2arch_8h.md#ac14ee42f2f373cf48fa30a60f3aafc39)(void)

155{

156 int vecbase;

157

158 \_\_asm\_\_ volatile("rsr.vecbase %0" : "=r" (vecbase));

159 \_\_asm\_\_ volatile("wsr.vecbase %0; rsync" : : "r" (vecbase | 1));

160}

161

162#if defined(CONFIG\_XTENSA\_RPO\_CACHE) || defined(\_\_DOXYGEN\_\_)

163#if defined(CONFIG\_ARCH\_HAS\_COHERENCE) || defined(\_\_DOXYGEN\_\_)

[ 165](xtensa_2arch_8h.md#a8c6bb0f6730c115689452b016ac1761f)static inline bool [arch\_mem\_coherent](xtensa_2arch_8h.md#a8c6bb0f6730c115689452b016ac1761f)(void \*ptr)

166{

167 size\_t addr = ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) ptr;

168

169 return (addr >> 29) == CONFIG\_XTENSA\_UNCACHED\_REGION;

170}

171#endif

172

173

174/\* Utility to generate an unrolled and optimal[1] code sequence to set

175 \* the RPO TLB registers (contra the HAL cacheattr macros, which

176 \* generate larger code and can't be called from C), based on the

177 \* KERNEL\_COHERENCE configuration in use. Selects RPO attribute "2"

178 \* for regions (including MMIO registers in region zero) which want to

179 \* bypass L1, "4" for the cached region which wants writeback, and

180 \* "15" (invalid) elsewhere.

181 \*

182 \* Note that on cores that have the "translation" option set, we need

183 \* to put an identity mapping in the high bits. Also per spec

184 \* changing the current code region (by definition cached) requires

185 \* that WITLB be followed by an ISYNC and that both instructions live

186 \* in the same cache line (two 3-byte instructions fit in an 8-byte

187 \* aligned region, so that's guaranteed not to cross a cache line

188 \* boundary).

189 \*

190 \* [1] With the sole exception of gcc's infuriating insistence on

191 \* emitting a precomputed literal for addr + addrincr instead of

192 \* computing it with a single ADD instruction from values it already

193 \* has in registers. Explicitly assigning the variables to registers

194 \* via an attribute works, but then emits needless MOV instructions

195 \* instead. I tell myself it's just 32 bytes of .text, but... Sigh.

196 \*/

197#define \_REGION\_ATTR(r) \

198 ((r) == 0 ? 2 : \

199 ((r) == CONFIG\_XTENSA\_CACHED\_REGION ? 4 : \

200 ((r) == CONFIG\_XTENSA\_UNCACHED\_REGION ? 2 : 15)))

201

202#define \_SET\_ONE\_TLB(region) do { \

203 uint32\_t attr = \_REGION\_ATTR(region); \

204 if (XCHAL\_HAVE\_XLT\_CACHEATTR) { \

205 attr |= addr; /\* RPO with translation \*/ \

206 } \

207 if (region != CONFIG\_XTENSA\_CACHED\_REGION) { \

208 \_\_asm\_\_ volatile("wdtlb %0, %1; witlb %0, %1" \

209 :: "r"(attr), "r"(addr)); \

210 } else { \

211 \_\_asm\_\_ volatile("wdtlb %0, %1" \

212 :: "r"(attr), "r"(addr)); \

213 \_\_asm\_\_ volatile("j 1f; .align 8; 1:"); \

214 \_\_asm\_\_ volatile("witlb %0, %1; isync" \

215 :: "r"(attr), "r"(addr)); \

216 } \

217 addr += addrincr; \

218} while (0)

219

[ 223](xtensa_2arch_8h.md#a835f1838cf0cec9c6a16bacc62436f0f)#define ARCH\_XTENSA\_SET\_RPO\_TLB() \

224 do { \

225 register uint32\_t addr = 0, addrincr = 0x20000000; \

226 FOR\_EACH(\_SET\_ONE\_TLB, (;), 0, 1, 2, 3, 4, 5, 6, 7); \

227 } while (0)

228#endif /\* CONFIG\_XTENSA\_RPO\_CACHE \*/

229

230#if defined(CONFIG\_XTENSA\_MMU) || defined(\_\_DOXYGEN\_\_)

[ 241](xtensa_2arch_8h.md#a9f03623f0f77593e60195483ac6b07f9)void [arch\_xtensa\_mmu\_post\_init](xtensa_2arch_8h.md#a9f03623f0f77593e60195483ac6b07f9)(bool is\_core0);

242#endif

243

244#ifdef \_\_cplusplus

245}

246#endif

247

248#endif /\* !defined(\_ASMLANGUAGE) && !defined(\_\_ASSEMBLER\_\_) \*/

249

250#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_ARCH\_H\_ \*/

[addr\_types.h](addr__types_8h.md)

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[sys\_io.h](arch_2common_2sys__io_8h.md)

[gdbstub.h](arch_2xtensa_2gdbstub_8h.md)

[irq.h](arch_2xtensa_2irq_8h.md)

[syscall.h](arch_2xtensa_2syscall_8h.md)

Xtensa specific syscall header.

[thread.h](arch_2xtensa_2thread_8h.md)

[thread\_stack.h](arch_2xtensa_2thread__stack_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

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

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[slist.h](slist_8h.md)

[sparse.h](sparse_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[arch\_mem\_domain](structarch__mem__domain.md)

**Definition** arch.h:46

[arch\_mem\_domain::node](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5)

sys\_snode\_t node

**Definition** arch.h:50

[arch\_mem\_domain::ptables](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6)

pentry\_t \* ptables

**Definition** mmustructs.h:89

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[sys\_bitops.h](sys__bitops_8h.md)

[system\_timer.h](system__timer_8h.md)

Timer driver API.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[xtensa\_user\_fault](xtensa_2arch_8h.md#a0890b1717c7f7b93644c69a3293b7da8)

void xtensa\_user\_fault(unsigned int reason)

[xtensa\_arch\_kernel\_oops](xtensa_2arch_8h.md#a31f0ccadfc2a2afa0e985d74a0e4c2e9)

void xtensa\_arch\_kernel\_oops(int reason\_p, void \*ssf)

Generate kernel oops.

[xtensa\_arch\_except](xtensa_2arch_8h.md#a789f894256925071f3448cda889abcf5)

void xtensa\_arch\_except(int reason\_p)

Generate hardware exception.

[arch\_mem\_coherent](xtensa_2arch_8h.md#a8c6bb0f6730c115689452b016ac1761f)

static bool arch\_mem\_coherent(void \*ptr)

Implementation of arch\_mem\_coherent.

**Definition** arch.h:165

[arch\_xtensa\_mmu\_post\_init](xtensa_2arch_8h.md#a9f03623f0f77593e60195483ac6b07f9)

void arch\_xtensa\_mmu\_post\_init(bool is\_core0)

Perform additional steps after MMU initialization.

[xtensa\_vecbase\_lock](xtensa_2arch_8h.md#ac14ee42f2f373cf48fa30a60f3aafc39)

static ALWAYS\_INLINE void xtensa\_vecbase\_lock(void)

Lock VECBASE if supported by hardware.

**Definition** arch.h:154

[exception.h](xtensa_2exception_8h.md)

Xtensa public exception handling.

[mpu.h](xtensa_2mpu_8h.md)

[xtensa\_mmu.h](xtensa__mmu_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [arch.h](xtensa_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
