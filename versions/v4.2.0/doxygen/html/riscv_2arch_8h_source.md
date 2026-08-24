---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/riscv_2arch_8h_source.html
original_path: doxygen/html/riscv_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](riscv_2arch_8h.md)

1/\*

2 \* Copyright (c) 2016 Jean-Paul Etienne <fractalclone@gmail.com>

3 \* Contributors: 2018 Antmicro <www.antmicro.com>

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

16

17#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ARCH\_H\_

18#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ARCH\_H\_

19

20#include <[zephyr/arch/riscv/thread.h](arch_2riscv_2thread_8h.md)>

21#include <[zephyr/arch/riscv/exception.h](riscv_2exception_8h.md)>

22#include <[zephyr/arch/riscv/irq.h](arch_2riscv_2irq_8h.md)>

23#include <[zephyr/arch/riscv/sys\_io.h](arch_2riscv_2sys__io_8h.md)>

24#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

25#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

26#if defined(CONFIG\_USERSPACE)

27#include <[zephyr/arch/riscv/syscall.h](arch_2riscv_2syscall_8h.md)>

28#endif /\* CONFIG\_USERSPACE \*/

29#include <[zephyr/irq.h](irq_8h.md)>

30#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

31#include <[zephyr/devicetree.h](devicetree_8h.md)>

32#include <[zephyr/arch/riscv/csr.h](csr_8h.md)>

33#include <[zephyr/arch/riscv/exception.h](riscv_2exception_8h.md)>

34

35/\* stacks, for RISCV architecture stack should be 16byte-aligned \*/

[ 36](riscv_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 16

37

38#define Z\_RISCV\_STACK\_PMP\_ALIGN \

39 MAX(CONFIG\_PMP\_GRANULARITY, ARCH\_STACK\_PTR\_ALIGN)

40

41#ifdef CONFIG\_PMP\_STACK\_GUARD

42/\*

43 \* The StackGuard is an area at the bottom of the kernel-mode stack made to

44 \* fault when accessed. It is \_not\_ faulting when in exception mode as we rely

45 \* on that area to save the exception stack frame and to process said fault.

46 \* Therefore the guard area must be large enough to hold the esf, plus some

47 \* configurable stack wiggle room to execute the fault handling code off of,

48 \* as well as some guard size to cover possible sudden stack pointer

49 \* displacement before the fault.

50 \*/

51#ifdef CONFIG\_PMP\_POWER\_OF\_TWO\_ALIGNMENT

52#define Z\_RISCV\_STACK\_GUARD\_SIZE \

53 Z\_POW2\_CEIL(MAX(sizeof(struct arch\_esf) + CONFIG\_PMP\_STACK\_GUARD\_MIN\_SIZE, \

54 Z\_RISCV\_STACK\_PMP\_ALIGN))

55#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN Z\_RISCV\_STACK\_GUARD\_SIZE

56#else

57#define Z\_RISCV\_STACK\_GUARD\_SIZE \

58 ROUND\_UP(sizeof(struct arch\_esf) + CONFIG\_PMP\_STACK\_GUARD\_MIN\_SIZE, \

59 Z\_RISCV\_STACK\_PMP\_ALIGN)

60#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN Z\_RISCV\_STACK\_PMP\_ALIGN

61#endif

62

63/\* Kernel-only stacks have the following layout if a stack guard is enabled:

64 \*

65 \* +------------+ <- thread.stack\_obj

66 \* | Guard | } Z\_RISCV\_STACK\_GUARD\_SIZE

67 \* +------------+ <- thread.stack\_info.start

68 \* | Kernel |

69 \* | stack |

70 \* | |

71 \* +............|

72 \* | TLS | } thread.stack\_info.delta

73 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

74 \*/

75#define ARCH\_KERNEL\_STACK\_RESERVED Z\_RISCV\_STACK\_GUARD\_SIZE

76

77#else /\* !CONFIG\_PMP\_STACK\_GUARD \*/

78#define Z\_RISCV\_STACK\_GUARD\_SIZE 0

79#endif

80

81#ifdef CONFIG\_PMP\_POWER\_OF\_TWO\_ALIGNMENT

82/\* The privilege elevation stack is located in another area of memory

83 \* generated at build time by gen\_kobject\_list.py

84 \*

85 \* +------------+ <- thread.arch.priv\_stack\_start

86 \* | Guard | } Z\_RISCV\_STACK\_GUARD\_SIZE

87 \* +------------+

88 \* | Priv Stack | } CONFIG\_PRIVILEGED\_STACK\_SIZE

89 \* +------------+ <- thread.arch.priv\_stack\_start +

90 \* CONFIG\_PRIVILEGED\_STACK\_SIZE +

91 \* Z\_RISCV\_STACK\_GUARD\_SIZE

92 \*

93 \* The main stack will be initially (or potentially only) used by kernel

94 \* mode so we need to make room for a possible stack guard area when enabled:

95 \*

96 \* +------------+ <- thread.stack\_obj

97 \* | Guard | } Z\_RISCV\_STACK\_GUARD\_SIZE

98 \* +............| <- thread.stack\_info.start

99 \* | Thread |

100 \* | stack |

101 \* | |

102 \* +............|

103 \* | TLS | } thread.stack\_info.delta

104 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

105 \*

106 \* When transitioning to user space, the guard area will be removed from

107 \* the main stack. Any thread running in user mode will have full access

108 \* to the region denoted by thread.stack\_info. Make it PMP-NAPOT compatible.

109 \*

110 \* +------------+ <- thread.stack\_obj = thread.stack\_info.start

111 \* | Thread |

112 \* | stack |

113 \* | |

114 \* +............|

115 \* | TLS | } thread.stack\_info.delta

116 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

117 \*/

118#define ARCH\_THREAD\_STACK\_RESERVED Z\_RISCV\_STACK\_GUARD\_SIZE

119#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

120 Z\_POW2\_CEIL(MAX(MAX(size, CONFIG\_PRIVILEGED\_STACK\_SIZE), \

121 Z\_RISCV\_STACK\_PMP\_ALIGN))

122#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) \

123 ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size)

124

125#else /\* !CONFIG\_PMP\_POWER\_OF\_TWO\_ALIGNMENT \*/

126

127/\* The stack object will contain the PMP guard, the privilege stack, and then

128 \* the usermode stack buffer in that order:

129 \*

130 \* +------------+ <- thread.stack\_obj

131 \* | Guard | } Z\_RISCV\_STACK\_GUARD\_SIZE

132 \* +------------+

133 \* | Priv Stack | } CONFIG\_PRIVILEGED\_STACK\_SIZE

134 \* +------------+ <- thread.stack\_info.start

135 \* | Thread |

136 \* | stack |

137 \* | |

138 \* +............|

139 \* | TLS | } thread.stack\_info.delta

140 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

141 \*/

[ 142](riscv_2arch_8h.md#ace8831316d471ccfb06eeddb6d69d817)#define ARCH\_THREAD\_STACK\_RESERVED \

143 ROUND\_UP(Z\_RISCV\_STACK\_GUARD\_SIZE + CONFIG\_PRIVILEGED\_STACK\_SIZE, \

144 Z\_RISCV\_STACK\_PMP\_ALIGN)

[ 145](riscv_2arch_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

146 ROUND\_UP(size, Z\_RISCV\_STACK\_PMP\_ALIGN)

[ 147](riscv_2arch_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_RISCV\_STACK\_PMP\_ALIGN

148#endif /\* CONFIG\_PMP\_POWER\_OF\_TWO\_ALIGNMENT \*/

149

150#ifdef CONFIG\_64BIT

151#define RV\_REGSIZE 8

152#define RV\_REGSHIFT 3

153#else

[ 154](riscv_2arch_8h.md#a2e02af37a1fa1fa6b5df7e7e150dcbf3)#define RV\_REGSIZE 4

[ 155](riscv_2arch_8h.md#a0175995fb1dea1feffa8ba200245395c)#define RV\_REGSHIFT 2

156#endif

157

158/\* Common mstatus bits. All supported cores today have the same

159 \* layouts.

160 \*/

161

[ 162](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267)#define MSTATUS\_IEN (1UL << 3)

[ 163](riscv_2arch_8h.md#aa6621785868a067469e73ac9babeed99)#define MSTATUS\_MPP\_M (3UL << 11)

[ 164](riscv_2arch_8h.md#a6ef6d2229ec2a9328ff08de7dea7cc9c)#define MSTATUS\_MPIE\_EN (1UL << 7)

165

[ 166](riscv_2arch_8h.md#a6ebe8a2c82f48216c528cc0cc25122c0)#define MSTATUS\_FS\_OFF (0UL << 13)

[ 167](riscv_2arch_8h.md#a6ca1c1c2ce04e484e7d146febf167dac)#define MSTATUS\_FS\_INIT (1UL << 13)

[ 168](riscv_2arch_8h.md#aef9ff6d95030e46ca86237a320898ca3)#define MSTATUS\_FS\_CLEAN (2UL << 13)

[ 169](riscv_2arch_8h.md#aa704a5aece9149a30cefae0a0f77f034)#define MSTATUS\_FS\_DIRTY (3UL << 13)

170

171/\* This comes from openisa\_rv32m1, but doesn't seem to hurt on other

172 \* platforms:

173 \* - Preserve machine privileges in MPP. If you see any documentation

174 \* telling you that MPP is read-only on this SoC, don't believe its

175 \* lies.

176 \* - Enable interrupts when exiting from exception into a new thread

177 \* by setting MPIE now, so it will be copied into IE on mret.

178 \*/

[ 179](riscv_2arch_8h.md#a0d401e5c8d9231016dfc0b2b8d53e0e6)#define MSTATUS\_DEF\_RESTORE (MSTATUS\_MPP\_M | MSTATUS\_MPIE\_EN)

180

181#ifndef \_ASMLANGUAGE

182#include <[zephyr/sys/util.h](sys_2util_8h.md)>

183

184#ifdef \_\_cplusplus

185extern "C" {

186#endif

187

188#ifdef CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_CODE

189#define ARCH\_IRQ\_VECTOR\_JUMP\_CODE(v) "j " STRINGIFY(v)

190#endif

191

192/\* Kernel macros for memory attribution

193 \* (access permissions and cache-ability).

194 \*

195 \* The macros are to be stored in k\_mem\_partition\_attr\_t

196 \* objects. The format of a k\_mem\_partition\_attr\_t object

197 \* is an uint8\_t composed by configuration register flags

198 \* located in arch/riscv/include/core\_pmp.h

199 \*/

200

201/\* Read-Write access permission attributes \*/

[ 202](riscv_2arch_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW ((k\_mem\_partition\_attr\_t) \

203 {PMP\_R | PMP\_W})

[ 204](riscv_2arch_8h.md#a6636a59c913e035646a1a9e5ed61559d)#define K\_MEM\_PARTITION\_P\_RW\_U\_RO ((k\_mem\_partition\_attr\_t) \

205 {PMP\_R})

[ 206](riscv_2arch_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA ((k\_mem\_partition\_attr\_t) \

207 {0})

[ 208](riscv_2arch_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO ((k\_mem\_partition\_attr\_t) \

209 {PMP\_R})

[ 210](riscv_2arch_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA ((k\_mem\_partition\_attr\_t) \

211 {0})

[ 212](riscv_2arch_8h.md#a73bc6803ccf24aad395089a4395bd22f)#define K\_MEM\_PARTITION\_P\_NA\_U\_NA ((k\_mem\_partition\_attr\_t) \

213 {0})

214

215/\* Execution-allowed attributes \*/

[ 216](riscv_2arch_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX ((k\_mem\_partition\_attr\_t) \

217 {PMP\_R | PMP\_W | PMP\_X})

[ 218](riscv_2arch_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t) \

219 {PMP\_R | PMP\_X})

220

221/\* Typedef for the k\_mem\_partition attribute \*/

222typedef struct {

[ 223](structk__mem__partition__attr__t.md#aa1b529cb23bc5b4060da29d8ac52a124) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pmp\_attr](structk__mem__partition__attr__t.md#aa1b529cb23bc5b4060da29d8ac52a124);

224} [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

225

226struct [arch\_mem\_domain](structarch__mem__domain.md) {

[ 227](structarch__mem__domain.md#a21c2efb6fbef9d829bba2eb76ba0ef83) unsigned int [pmp\_update\_nr](structarch__mem__domain.md#a21c2efb6fbef9d829bba2eb76ba0ef83);

228};

229

230extern void z\_irq\_spurious(const void \*unused);

231

232/\*

233 \* use atomic instruction csrrc to lock global irq

234 \* csrrc: atomic read and clear bits in CSR register

235 \*/

[ 236](riscv_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

237{

238#ifdef CONFIG\_RISCV\_SOC\_HAS\_CUSTOM\_IRQ\_LOCK\_OPS

239 return z\_soc\_irq\_lock();

240#else

241 unsigned int key;

242

243 \_\_asm\_\_ volatile ("csrrc %0, mstatus, %1"

244 : "=r" (key)

245 : "rK" ([MSTATUS\_IEN](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267))

246 : "memory");

247

248 return key;

249#endif

250}

251

252/\*

253 \* use atomic instruction csrs to unlock global irq

254 \* csrs: atomic set bits in CSR register

255 \*/

[ 256](riscv_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

257{

258#ifdef CONFIG\_RISCV\_SOC\_HAS\_CUSTOM\_IRQ\_LOCK\_OPS

259 z\_soc\_irq\_unlock(key);

260#else

261 \_\_asm\_\_ volatile ("csrs mstatus, %0"

262 :

263 : "r" (key & [MSTATUS\_IEN](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267))

264 : "memory");

265#endif

266}

267

[ 268](riscv_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

269{

270#ifdef CONFIG\_RISCV\_SOC\_HAS\_CUSTOM\_IRQ\_LOCK\_OPS

271 return z\_soc\_irq\_unlocked(key);

272#else

273 return (key & [MSTATUS\_IEN](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267)) != 0;

274#endif

275}

276

[ 277](riscv_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

278{

279 \_\_asm\_\_ volatile("nop");

280}

281

[ 282](riscv_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

283

[ 284](riscv_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

285{

286 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

287}

288

[ 289](riscv_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

290

[ 291](riscv_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

292{

293 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

294}

295

296#include <[zephyr/arch/riscv/error.h](include_2zephyr_2arch_2riscv_2error_8h.md)>

297

298#ifdef \_\_cplusplus

299}

300#endif

301

302#endif /\*\_ASMLANGUAGE \*/

303

304#if defined(CONFIG\_RISCV\_PRIVILEGED)

305#include <[zephyr/arch/riscv/riscv-privileged/asm\_inline.h](riscv_2riscv-privileged_2asm__inline_8h.md)>

306#endif

307

308

309#endif

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[irq.h](arch_2riscv_2irq_8h.md)

RISC-V public interrupt handling.

[sys\_io.h](arch_2riscv_2sys__io_8h.md)

[syscall.h](arch_2riscv_2syscall_8h.md)

RISCV specific syscall header.

[thread.h](arch_2riscv_2thread_8h.md)

Per-arch thread definition.

[csr.h](csr_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[error.h](include_2zephyr_2arch_2riscv_2error_8h.md)

RISCV public error handling.

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:72

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

[MSTATUS\_IEN](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267)

#define MSTATUS\_IEN

**Definition** arch.h:162

[exception.h](riscv_2exception_8h.md)

RISCV public exception handling.

[asm\_inline.h](riscv_2riscv-privileged_2asm__inline_8h.md)

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

[arch\_mem\_domain::pmp\_update\_nr](structarch__mem__domain.md#a21c2efb6fbef9d829bba2eb76ba0ef83)

unsigned int pmp\_update\_nr

**Definition** arch.h:227

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:142

[k\_mem\_partition\_attr\_t::pmp\_attr](structk__mem__partition__attr__t.md#aa1b529cb23bc5b4060da29d8ac52a124)

uint8\_t pmp\_attr

**Definition** arch.h:223

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[util.h](sys_2util_8h.md)

Misc utilities.

[sys\_bitops.h](sys__bitops_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [arch.h](riscv_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
