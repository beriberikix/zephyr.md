---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/xtensa_2arch_8h_source.html
original_path: doxygen/html/xtensa_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

38#include <[zephyr/arch/xtensa/xtensa\_mmu.h](xtensa__mmu_8h.md)>

39

50

51#include <[zephyr/arch/xtensa/exception.h](xtensa_2exception_8h.md)>

52

53#ifdef \_\_cplusplus

54extern "C" {

55#endif

56

57struct [arch\_mem\_domain](structarch__mem__domain.md) {

58#ifdef CONFIG\_XTENSA\_MMU

59 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[ptables](structarch__mem__domain.md#a6807078806451f4512078917e76c52b6) \_\_aligned(CONFIG\_MMU\_PAGE\_SIZE);

60 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) asid;

61 bool dirty;

62#endif

63 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structarch__mem__domain.md#a0929bee2d20221e55c0fa05ca321c9d5);

64};

65

[ 73](xtensa_2arch_8h.md#a789f894256925071f3448cda889abcf5)extern void [xtensa\_arch\_except](xtensa_2arch_8h.md#a789f894256925071f3448cda889abcf5)(int reason\_p);

74

[ 83](xtensa_2arch_8h.md#a31f0ccadfc2a2afa0e985d74a0e4c2e9)extern void [xtensa\_arch\_kernel\_oops](xtensa_2arch_8h.md#a31f0ccadfc2a2afa0e985d74a0e4c2e9)(int reason\_p, void \*ssf);

84

85#ifdef CONFIG\_USERSPACE

86

[ 87](xtensa_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

88 if (k\_is\_user\_context()) { \

89 arch\_syscall\_invoke1(reason\_p, \

90 K\_SYSCALL\_XTENSA\_USER\_FAULT); \

91 } else { \

92 xtensa\_arch\_except(reason\_p); \

93 } \

94 CODE\_UNREACHABLE; \

95} while (false)

96

97#else

98

99#define ARCH\_EXCEPT(reason\_p) do { \

100 xtensa\_arch\_except(reason\_p); \

101 CODE\_UNREACHABLE; \

102 } while (false)

103

104#endif

105

[ 106](xtensa_2arch_8h.md#a0890b1717c7f7b93644c69a3293b7da8)\_\_syscall void [xtensa\_user\_fault](xtensa_2arch_8h.md#a0890b1717c7f7b93644c69a3293b7da8)(unsigned int reason);

107

108#include <syscalls/arch.h>

109

110/\* internal routine documented in C file, needed by IRQ\_CONNECT() macro \*/

111extern void z\_irq\_priority\_set([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

112

[ 113](xtensa_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

114 { \

115 Z\_ISR\_DECLARE(irq\_p, flags\_p, isr\_p, isr\_param\_p); \

116 }

117

[ 119](xtensa_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

120{

121 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

122}

123

[ 125](xtensa_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

126{

127 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

128}

129

[ 131](xtensa_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

132{

133 \_\_asm\_\_ volatile("nop");

134}

135

[ 144](xtensa_2arch_8h.md#ac14ee42f2f373cf48fa30a60f3aafc39)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [xtensa\_vecbase\_lock](xtensa_2arch_8h.md#ac14ee42f2f373cf48fa30a60f3aafc39)(void)

145{

146 int vecbase;

147

148 \_\_asm\_\_ volatile("rsr.vecbase %0" : "=r" (vecbase));

149 \_\_asm\_\_ volatile("wsr.vecbase %0; rsync" : : "r" (vecbase | 1));

150}

151

152#if defined(CONFIG\_XTENSA\_RPO\_CACHE) || defined(\_\_DOXYGEN\_\_)

153#if defined(CONFIG\_ARCH\_HAS\_COHERENCE) || defined(\_\_DOXYGEN\_\_)

[ 155](xtensa_2arch_8h.md#a8c6bb0f6730c115689452b016ac1761f)static inline bool [arch\_mem\_coherent](xtensa_2arch_8h.md#a8c6bb0f6730c115689452b016ac1761f)(void \*ptr)

156{

157 size\_t addr = ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) ptr;

158

159 return (addr >> 29) == CONFIG\_XTENSA\_UNCACHED\_REGION;

160}

161#endif

162

163

164/\* Utility to generate an unrolled and optimal[1] code sequence to set

165 \* the RPO TLB registers (contra the HAL cacheattr macros, which

166 \* generate larger code and can't be called from C), based on the

167 \* KERNEL\_COHERENCE configuration in use. Selects RPO attribute "2"

168 \* for regions (including MMIO registers in region zero) which want to

169 \* bypass L1, "4" for the cached region which wants writeback, and

170 \* "15" (invalid) elsewhere.

171 \*

172 \* Note that on cores that have the "translation" option set, we need

173 \* to put an identity mapping in the high bits. Also per spec

174 \* changing the current code region (by definition cached) requires

175 \* that WITLB be followed by an ISYNC and that both instructions live

176 \* in the same cache line (two 3-byte instructions fit in an 8-byte

177 \* aligned region, so that's guaranteed not to cross a cache line

178 \* boundary).

179 \*

180 \* [1] With the sole exception of gcc's infuriating insistence on

181 \* emitting a precomputed literal for addr + addrincr instead of

182 \* computing it with a single ADD instruction from values it already

183 \* has in registers. Explicitly assigning the variables to registers

184 \* via an attribute works, but then emits needless MOV instructions

185 \* instead. I tell myself it's just 32 bytes of .text, but... Sigh.

186 \*/

187#define \_REGION\_ATTR(r) \

188 ((r) == 0 ? 2 : \

189 ((r) == CONFIG\_XTENSA\_CACHED\_REGION ? 4 : \

190 ((r) == CONFIG\_XTENSA\_UNCACHED\_REGION ? 2 : 15)))

191

192#define \_SET\_ONE\_TLB(region) do { \

193 uint32\_t attr = \_REGION\_ATTR(region); \

194 if (XCHAL\_HAVE\_XLT\_CACHEATTR) { \

195 attr |= addr; /\* RPO with translation \*/ \

196 } \

197 if (region != CONFIG\_XTENSA\_CACHED\_REGION) { \

198 \_\_asm\_\_ volatile("wdtlb %0, %1; witlb %0, %1" \

199 :: "r"(attr), "r"(addr)); \

200 } else { \

201 \_\_asm\_\_ volatile("wdtlb %0, %1" \

202 :: "r"(attr), "r"(addr)); \

203 \_\_asm\_\_ volatile("j 1f; .align 8; 1:"); \

204 \_\_asm\_\_ volatile("witlb %0, %1; isync" \

205 :: "r"(attr), "r"(addr)); \

206 } \

207 addr += addrincr; \

208} while (0)

209

[ 213](xtensa_2arch_8h.md#a835f1838cf0cec9c6a16bacc62436f0f)#define ARCH\_XTENSA\_SET\_RPO\_TLB() \

214 do { \

215 register uint32\_t addr = 0, addrincr = 0x20000000; \

216 FOR\_EACH(\_SET\_ONE\_TLB, (;), 0, 1, 2, 3, 4, 5, 6, 7); \

217 } while (0)

218#endif /\* CONFIG\_XTENSA\_RPO\_CACHE \*/

219

220#if defined(CONFIG\_XTENSA\_MMU) || defined(\_\_DOXYGEN\_\_)

[ 231](xtensa_2arch_8h.md#a9f03623f0f77593e60195483ac6b07f9)extern void [arch\_xtensa\_mmu\_post\_init](xtensa_2arch_8h.md#a9f03623f0f77593e60195483ac6b07f9)(bool is\_core0);

232#endif

233

234#ifdef \_\_cplusplus

235}

236#endif

237

238#endif /\* !defined(\_ASMLANGUAGE) && !defined(\_\_ASSEMBLER\_\_) \*/

239

240#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_ARCH\_H\_ \*/

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

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

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

**Definition** mmustructs.h:75

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

**Definition** arch.h:155

[arch\_xtensa\_mmu\_post\_init](xtensa_2arch_8h.md#a9f03623f0f77593e60195483ac6b07f9)

void arch\_xtensa\_mmu\_post\_init(bool is\_core0)

Peform additional steps after MMU initialization.

[xtensa\_vecbase\_lock](xtensa_2arch_8h.md#ac14ee42f2f373cf48fa30a60f3aafc39)

static ALWAYS\_INLINE void xtensa\_vecbase\_lock(void)

Lock VECBASE if supported by hardware.

**Definition** arch.h:144

[exception.h](xtensa_2exception_8h.md)

Xtensa public exception handling.

[xtensa\_mmu.h](xtensa__mmu_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [arch.h](xtensa_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
