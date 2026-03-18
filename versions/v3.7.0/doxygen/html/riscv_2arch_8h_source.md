---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/riscv_2arch_8h_source.html
original_path: doxygen/html/riscv_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ARCH\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ARCH\_H\_

17

18#include <[zephyr/arch/riscv/thread.h](arch_2riscv_2thread_8h.md)>

19#include <[zephyr/arch/riscv/exception.h](riscv_2exception_8h.md)>

20#include <[zephyr/arch/riscv/irq.h](arch_2riscv_2irq_8h.md)>

21#include <[zephyr/arch/riscv/sys\_io.h](arch_2riscv_2sys__io_8h.md)>

22#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

23#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

24#if defined(CONFIG\_USERSPACE)

25#include <[zephyr/arch/riscv/syscall.h](arch_2riscv_2syscall_8h.md)>

26#endif /\* CONFIG\_USERSPACE \*/

27#include <[zephyr/irq.h](irq_8h.md)>

28#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

29#include <[zephyr/devicetree.h](devicetree_8h.md)>

30#include <[zephyr/arch/riscv/csr.h](csr_8h.md)>

31#include <[zephyr/arch/riscv/exception.h](riscv_2exception_8h.md)>

32

33/\* stacks, for RISCV architecture stack should be 16byte-aligned \*/

[ 34](riscv_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 16

35

36#define Z\_RISCV\_STACK\_PMP\_ALIGN \

37 MAX(CONFIG\_PMP\_GRANULARITY, ARCH\_STACK\_PTR\_ALIGN)

38

39#ifdef CONFIG\_PMP\_STACK\_GUARD

40/\*

41 \* The StackGuard is an area at the bottom of the kernel-mode stack made to

42 \* fault when accessed. It is \_not\_ faulting when in exception mode as we rely

43 \* on that area to save the exception stack frame and to process said fault.

44 \* Therefore the guard area must be large enough to hold the esf, plus some

45 \* configurable stack wiggle room to execute the fault handling code off of,

46 \* as well as some guard size to cover possible sudden stack pointer

47 \* displacement before the fault.

48 \*/

49#ifdef CONFIG\_PMP\_POWER\_OF\_TWO\_ALIGNMENT

50#define Z\_RISCV\_STACK\_GUARD\_SIZE \

51 Z\_POW2\_CEIL(MAX(sizeof(struct arch\_esf) + CONFIG\_PMP\_STACK\_GUARD\_MIN\_SIZE, \

52 Z\_RISCV\_STACK\_PMP\_ALIGN))

53#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN Z\_RISCV\_STACK\_GUARD\_SIZE

54#else

55#define Z\_RISCV\_STACK\_GUARD\_SIZE \

56 ROUND\_UP(sizeof(struct arch\_esf) + CONFIG\_PMP\_STACK\_GUARD\_MIN\_SIZE, \

57 Z\_RISCV\_STACK\_PMP\_ALIGN)

58#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN Z\_RISCV\_STACK\_PMP\_ALIGN

59#endif

60

61/\* Kernel-only stacks have the following layout if a stack guard is enabled:

62 \*

63 \* +------------+ <- thread.stack\_obj

64 \* | Guard | } Z\_RISCV\_STACK\_GUARD\_SIZE

65 \* +------------+ <- thread.stack\_info.start

66 \* | Kernel |

67 \* | stack |

68 \* | |

69 \* +............|

70 \* | TLS | } thread.stack\_info.delta

71 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

72 \*/

73#define ARCH\_KERNEL\_STACK\_RESERVED Z\_RISCV\_STACK\_GUARD\_SIZE

74

75#else /\* !CONFIG\_PMP\_STACK\_GUARD \*/

76#define Z\_RISCV\_STACK\_GUARD\_SIZE 0

77#endif

78

79#ifdef CONFIG\_PMP\_POWER\_OF\_TWO\_ALIGNMENT

80/\* The privilege elevation stack is located in another area of memory

81 \* generated at build time by gen\_kobject\_list.py

82 \*

83 \* +------------+ <- thread.arch.priv\_stack\_start

84 \* | Guard | } Z\_RISCV\_STACK\_GUARD\_SIZE

85 \* +------------+

86 \* | Priv Stack | } CONFIG\_PRIVILEGED\_STACK\_SIZE

87 \* +------------+ <- thread.arch.priv\_stack\_start +

88 \* CONFIG\_PRIVILEGED\_STACK\_SIZE +

89 \* Z\_RISCV\_STACK\_GUARD\_SIZE

90 \*

91 \* The main stack will be initially (or potentially only) used by kernel

92 \* mode so we need to make room for a possible stack guard area when enabled:

93 \*

94 \* +------------+ <- thread.stack\_obj

95 \* | Guard | } Z\_RISCV\_STACK\_GUARD\_SIZE

96 \* +............| <- thread.stack\_info.start

97 \* | Thread |

98 \* | stack |

99 \* | |

100 \* +............|

101 \* | TLS | } thread.stack\_info.delta

102 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

103 \*

104 \* When transitioning to user space, the guard area will be removed from

105 \* the main stack. Any thread running in user mode will have full access

106 \* to the region denoted by thread.stack\_info. Make it PMP-NAPOT compatible.

107 \*

108 \* +------------+ <- thread.stack\_obj = thread.stack\_info.start

109 \* | Thread |

110 \* | stack |

111 \* | |

112 \* +............|

113 \* | TLS | } thread.stack\_info.delta

114 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

115 \*/

116#define ARCH\_THREAD\_STACK\_RESERVED Z\_RISCV\_STACK\_GUARD\_SIZE

117#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

118 Z\_POW2\_CEIL(MAX(MAX(size, CONFIG\_PRIVILEGED\_STACK\_SIZE), \

119 Z\_RISCV\_STACK\_PMP\_ALIGN))

120#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) \

121 ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size)

122

123#else /\* !CONFIG\_PMP\_POWER\_OF\_TWO\_ALIGNMENT \*/

124

125/\* The stack object will contain the PMP guard, the privilege stack, and then

126 \* the usermode stack buffer in that order:

127 \*

128 \* +------------+ <- thread.stack\_obj

129 \* | Guard | } Z\_RISCV\_STACK\_GUARD\_SIZE

130 \* +------------+

131 \* | Priv Stack | } CONFIG\_PRIVILEGED\_STACK\_SIZE

132 \* +------------+ <- thread.stack\_info.start

133 \* | Thread |

134 \* | stack |

135 \* | |

136 \* +............|

137 \* | TLS | } thread.stack\_info.delta

138 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

139 \*/

[ 140](riscv_2arch_8h.md#ace8831316d471ccfb06eeddb6d69d817)#define ARCH\_THREAD\_STACK\_RESERVED \

141 ROUND\_UP(Z\_RISCV\_STACK\_GUARD\_SIZE + CONFIG\_PRIVILEGED\_STACK\_SIZE, \

142 Z\_RISCV\_STACK\_PMP\_ALIGN)

[ 143](riscv_2arch_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

144 ROUND\_UP(size, Z\_RISCV\_STACK\_PMP\_ALIGN)

[ 145](riscv_2arch_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_RISCV\_STACK\_PMP\_ALIGN

146#endif /\* CONFIG\_PMP\_POWER\_OF\_TWO\_ALIGNMENT \*/

147

148#ifdef CONFIG\_64BIT

149#define RV\_REGSIZE 8

150#define RV\_REGSHIFT 3

151#else

[ 152](riscv_2arch_8h.md#a2e02af37a1fa1fa6b5df7e7e150dcbf3)#define RV\_REGSIZE 4

[ 153](riscv_2arch_8h.md#a0175995fb1dea1feffa8ba200245395c)#define RV\_REGSHIFT 2

154#endif

155

156/\* Common mstatus bits. All supported cores today have the same

157 \* layouts.

158 \*/

159

[ 160](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267)#define MSTATUS\_IEN (1UL << 3)

[ 161](riscv_2arch_8h.md#aa6621785868a067469e73ac9babeed99)#define MSTATUS\_MPP\_M (3UL << 11)

[ 162](riscv_2arch_8h.md#a6ef6d2229ec2a9328ff08de7dea7cc9c)#define MSTATUS\_MPIE\_EN (1UL << 7)

163

[ 164](riscv_2arch_8h.md#a6ebe8a2c82f48216c528cc0cc25122c0)#define MSTATUS\_FS\_OFF (0UL << 13)

[ 165](riscv_2arch_8h.md#a6ca1c1c2ce04e484e7d146febf167dac)#define MSTATUS\_FS\_INIT (1UL << 13)

[ 166](riscv_2arch_8h.md#aef9ff6d95030e46ca86237a320898ca3)#define MSTATUS\_FS\_CLEAN (2UL << 13)

[ 167](riscv_2arch_8h.md#aa704a5aece9149a30cefae0a0f77f034)#define MSTATUS\_FS\_DIRTY (3UL << 13)

168

169/\* This comes from openisa\_rv32m1, but doesn't seem to hurt on other

170 \* platforms:

171 \* - Preserve machine privileges in MPP. If you see any documentation

172 \* telling you that MPP is read-only on this SoC, don't believe its

173 \* lies.

174 \* - Enable interrupts when exiting from exception into a new thread

175 \* by setting MPIE now, so it will be copied into IE on mret.

176 \*/

[ 177](riscv_2arch_8h.md#a0d401e5c8d9231016dfc0b2b8d53e0e6)#define MSTATUS\_DEF\_RESTORE (MSTATUS\_MPP\_M | MSTATUS\_MPIE\_EN)

178

179#ifndef \_ASMLANGUAGE

180#include <[zephyr/sys/util.h](util_8h.md)>

181

182#ifdef \_\_cplusplus

183extern "C" {

184#endif

185

186#ifdef CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_CODE

187#define ARCH\_IRQ\_VECTOR\_JUMP\_CODE(v) "j " STRINGIFY(v)

188#endif

189

190/\* Kernel macros for memory attribution

191 \* (access permissions and cache-ability).

192 \*

193 \* The macros are to be stored in k\_mem\_partition\_attr\_t

194 \* objects. The format of a k\_mem\_partition\_attr\_t object

195 \* is an uint8\_t composed by configuration register flags

196 \* located in arch/riscv/include/core\_pmp.h

197 \*/

198

199/\* Read-Write access permission attributes \*/

[ 200](riscv_2arch_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW ((k\_mem\_partition\_attr\_t) \

201 {PMP\_R | PMP\_W})

[ 202](riscv_2arch_8h.md#a6636a59c913e035646a1a9e5ed61559d)#define K\_MEM\_PARTITION\_P\_RW\_U\_RO ((k\_mem\_partition\_attr\_t) \

203 {PMP\_R})

[ 204](riscv_2arch_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA ((k\_mem\_partition\_attr\_t) \

205 {0})

[ 206](riscv_2arch_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO ((k\_mem\_partition\_attr\_t) \

207 {PMP\_R})

[ 208](riscv_2arch_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA ((k\_mem\_partition\_attr\_t) \

209 {0})

[ 210](riscv_2arch_8h.md#a73bc6803ccf24aad395089a4395bd22f)#define K\_MEM\_PARTITION\_P\_NA\_U\_NA ((k\_mem\_partition\_attr\_t) \

211 {0})

212

213/\* Execution-allowed attributes \*/

[ 214](riscv_2arch_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX ((k\_mem\_partition\_attr\_t) \

215 {PMP\_R | PMP\_W | PMP\_X})

[ 216](riscv_2arch_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t) \

217 {PMP\_R | PMP\_X})

218

219/\* Typedef for the k\_mem\_partition attribute \*/

220typedef struct {

[ 221](structk__mem__partition__attr__t.md#aa1b529cb23bc5b4060da29d8ac52a124) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pmp\_attr](structk__mem__partition__attr__t.md#aa1b529cb23bc5b4060da29d8ac52a124);

222} [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

223

224struct [arch\_mem\_domain](structarch__mem__domain.md) {

[ 225](structarch__mem__domain.md#a21c2efb6fbef9d829bba2eb76ba0ef83) unsigned int [pmp\_update\_nr](structarch__mem__domain.md#a21c2efb6fbef9d829bba2eb76ba0ef83);

226};

227

228extern void z\_irq\_spurious(const void \*unused);

229

230/\*

231 \* use atomic instruction csrrc to lock global irq

232 \* csrrc: atomic read and clear bits in CSR register

233 \*/

[ 234](riscv_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

235{

236#ifdef CONFIG\_RISCV\_SOC\_HAS\_CUSTOM\_IRQ\_LOCK\_OPS

237 return z\_soc\_irq\_lock();

238#else

239 unsigned int key;

240

241 \_\_asm\_\_ volatile ("csrrc %0, mstatus, %1"

242 : "=r" (key)

243 : "rK" ([MSTATUS\_IEN](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267))

244 : "memory");

245

246 return key;

247#endif

248}

249

250/\*

251 \* use atomic instruction csrs to unlock global irq

252 \* csrs: atomic set bits in CSR register

253 \*/

[ 254](riscv_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

255{

256#ifdef CONFIG\_RISCV\_SOC\_HAS\_CUSTOM\_IRQ\_LOCK\_OPS

257 z\_soc\_irq\_unlock(key);

258#else

259 \_\_asm\_\_ volatile ("csrs mstatus, %0"

260 :

261 : "r" (key & [MSTATUS\_IEN](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267))

262 : "memory");

263#endif

264}

265

[ 266](riscv_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

267{

268#ifdef CONFIG\_RISCV\_SOC\_HAS\_CUSTOM\_IRQ\_LOCK\_OPS

269 return z\_soc\_irq\_unlocked(key);

270#else

271 return (key & [MSTATUS\_IEN](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267)) != 0;

272#endif

273}

274

[ 275](riscv_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

276{

277 \_\_asm\_\_ volatile("nop");

278}

279

[ 280](riscv_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

281

[ 282](riscv_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

283{

284 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

285}

286

[ 287](riscv_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

288

[ 289](riscv_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

290{

291 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

292}

293

294#include <[zephyr/arch/riscv/error.h](riscv_2error_8h.md)>

295

296#ifdef \_\_cplusplus

297}

298#endif

299

300#endif /\*\_ASMLANGUAGE \*/

301

302#if defined(CONFIG\_RISCV\_PRIVILEGED)

303#include <[zephyr/arch/riscv/riscv-privileged/asm\_inline.h](riscv_2riscv-privileged_2asm__inline_8h.md)>

304#endif

305

306

307#endif

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

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[csr.h](csr_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:63

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

[MSTATUS\_IEN](riscv_2arch_8h.md#a190f193ea2099625861fb58c6e725267)

#define MSTATUS\_IEN

**Definition** arch.h:160

[error.h](riscv_2error_8h.md)

RISCV public error handling.

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

**Definition** arch.h:225

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[k\_mem\_partition\_attr\_t::pmp\_attr](structk__mem__partition__attr__t.md#aa1b529cb23bc5b4060da29d8ac52a124)

uint8\_t pmp\_attr

**Definition** arch.h:221

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[sys\_bitops.h](sys__bitops_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [arch.h](riscv_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
