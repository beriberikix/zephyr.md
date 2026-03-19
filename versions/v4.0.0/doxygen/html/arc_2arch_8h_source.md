---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arc_2arch_8h_source.html
original_path: doxygen/html/arc_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](arc_2arch_8h.md)

1/\*

2 \* Copyright (c) 2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_ARCH\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_ARCH\_H\_

18

19#include <[zephyr/devicetree.h](devicetree_8h.md)>

20#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

21#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

22#include <[zephyr/arch/arc/thread.h](arch_2arc_2thread_8h.md)>

23#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

24#include "[sys-io-common.h](sys-io-common_8h.md)"

25

26#include <[zephyr/arch/arc/v2/exception.h](arc_2v2_2exception_8h.md)>

27#include <[zephyr/arch/arc/v2/irq.h](arch_2arc_2v2_2irq_8h.md)>

28#include <[zephyr/arch/arc/v2/misc.h](arc_2v2_2misc_8h.md)>

29#include <[zephyr/arch/arc/v2/aux\_regs.h](aux__regs_8h.md)>

30#include <[zephyr/arch/arc/v2/arcv2\_irq\_unit.h](arcv2__irq__unit_8h.md)>

31#include <[zephyr/arch/arc/v2/asm\_inline.h](arc_2v2_2asm__inline_8h.md)>

32#include <[zephyr/arch/arc/arc\_addr\_types.h](arc__addr__types_8h.md)>

33#include <[zephyr/arch/arc/v2/error.h](include_2zephyr_2arch_2arc_2v2_2error_8h.md)>

34

35#ifdef CONFIG\_ARC\_CONNECT

36#include <[zephyr/arch/arc/v2/arc\_connect.h](arc__connect_8h.md)>

37#endif

38

39#ifdef CONFIG\_ISA\_ARCV2

40#include "[v2/sys\_io.h](arch_2arc_2v2_2sys__io_8h.md)"

41#ifdef CONFIG\_ARC\_HAS\_SECURE

42#include <[zephyr/arch/arc/v2/secureshield/arc\_secure.h](arc__secure_8h.md)>

43#endif

44#endif

45

46#if defined(CONFIG\_ARC\_FIRQ) && defined(CONFIG\_ISA\_ARCV3)

47#error "Unsupported configuration: ARC\_FIRQ and ISA\_ARCV3"

48#endif

49

50/\*

51 \* We don't allow the configuration with FIRQ enabled and only one interrupt priority level

52 \* (so all interrupts are FIRQ). Such configuration isn't supported in software and it is not

53 \* beneficial from the performance point of view.

54 \*/

55#if defined(CONFIG\_ARC\_FIRQ) && CONFIG\_NUM\_IRQ\_PRIO\_LEVELS < 2

56#error "Unsupported configuration: ARC\_FIRQ and (NUM\_IRQ\_PRIO\_LEVELS < 2)"

57#endif

58

59#if CONFIG\_RGF\_NUM\_BANKS > 1 && !defined(CONFIG\_ARC\_FIRQ)

60#error "Unsupported configuration: (RGF\_NUM\_BANKS > 1) and !ARC\_FIRQ"

61#endif

62

63/\*

64 \* It's required to have more than one interrupt priority level to use second register bank

65 \* - otherwise all interrupts will use same register bank. Such configuration isn't supported in

66 \* software and it is not beneficial from the performance point of view.

67 \*/

68#if CONFIG\_RGF\_NUM\_BANKS > 1 && CONFIG\_NUM\_IRQ\_PRIO\_LEVELS < 2

69#error "Unsupported configuration: (RGF\_NUM\_BANKS > 1) and (NUM\_IRQ\_PRIO\_LEVELS < 2)"

70#endif

71

72#if defined(CONFIG\_ARC\_FIRQ\_STACK) && !defined(CONFIG\_ARC\_FIRQ)

73#error "Unsupported configuration: ARC\_FIRQ\_STACK and !ARC\_FIRQ"

74#endif

75

76#if defined(CONFIG\_ARC\_FIRQ\_STACK) && CONFIG\_RGF\_NUM\_BANKS < 2

77#error "Unsupported configuration: ARC\_FIRQ\_STACK and (RGF\_NUM\_BANKS < 2)"

78#endif

79

80/\* In case of ARC 2+2 secure mode enabled the firq are not supported by HW \*/

81#if defined(CONFIG\_ARC\_FIRQ) && defined(CONFIG\_ARC\_HAS\_SECURE)

82#error "Unsupported configuration: ARC\_FIRQ and ARC\_HAS\_SECURE"

83#endif

84

85#if defined(CONFIG\_SMP) && !defined(CONFIG\_MULTITHREADING)

86#error "Non-multithreading mode isn't supported on SMP targets"

87#endif

88

89#ifndef \_ASMLANGUAGE

90

91#ifdef \_\_cplusplus

92extern "C" {

93#endif

94

95#ifdef CONFIG\_64BIT

96#define ARCH\_STACK\_PTR\_ALIGN 8

97#else

[ 98](arc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 4

99#endif /\* CONFIG\_64BIT \*/

100

101BUILD\_ASSERT(CONFIG\_ISR\_STACK\_SIZE % [ARCH\_STACK\_PTR\_ALIGN](arc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3) == 0,

102 "CONFIG\_ISR\_STACK\_SIZE must be a multiple of ARCH\_STACK\_PTR\_ALIGN");

103

104BUILD\_ASSERT(CONFIG\_ARC\_EXCEPTION\_STACK\_SIZE % [ARCH\_STACK\_PTR\_ALIGN](arc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3) == 0,

105 "CONFIG\_ARC\_EXCEPTION\_STACK\_SIZE must be a multiple of ARCH\_STACK\_PTR\_ALIGN");

106

107/\* Indicate, for a minimally sized MPU region, how large it must be and what

108 \* its base address must be aligned to.

109 \*

110 \* For regions that are NOT the minimum size, this define has no semantics

111 \* on ARC MPUv2 as its regions must be power of two size and aligned to their

112 \* own size. On ARC MPUv4, region sizes are arbitrary and this just indicates

113 \* the required size granularity.

114 \*/

115#ifdef CONFIG\_ARC\_CORE\_MPU

116#if CONFIG\_ARC\_MPU\_VER == 2

117#define Z\_ARC\_MPU\_ALIGN 2048

118#elif (CONFIG\_ARC\_MPU\_VER == 3) || (CONFIG\_ARC\_MPU\_VER == 4) || \

119 (CONFIG\_ARC\_MPU\_VER == 6) || (CONFIG\_ARC\_MPU\_VER == 8)

120#define Z\_ARC\_MPU\_ALIGN 32

121#else

122#error "Unsupported MPU version"

123#endif

124#endif

125

126#ifdef CONFIG\_MPU\_STACK\_GUARD

127#define Z\_ARC\_STACK\_GUARD\_SIZE Z\_ARC\_MPU\_ALIGN

128#else

129#define Z\_ARC\_STACK\_GUARD\_SIZE 0

130#endif

131

132/\* Kernel-only stacks have the following layout if a stack guard is enabled:

133 \*

134 \* +------------+ <- thread.stack\_obj

135 \* | Guard | } Z\_ARC\_STACK\_GUARD\_SIZE

136 \* +------------+ <- thread.stack\_info.start

137 \* | Kernel |

138 \* | stack |

139 \* | |

140 \* +............|

141 \* | TLS | } thread.stack\_info.delta

142 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

143 \*/

144#ifdef CONFIG\_MPU\_STACK\_GUARD

145#define ARCH\_KERNEL\_STACK\_RESERVED Z\_ARC\_STACK\_GUARD\_SIZE

146#define ARCH\_KERNEL\_STACK\_OBJ\_ALIGN Z\_ARC\_MPU\_ALIGN

147#endif

148

149#ifdef CONFIG\_USERSPACE

150/\* Any thread running In user mode will have full access to the region denoted

151 \* by thread.stack\_info.

152 \*

153 \* Thread-local storage is at the very highest memory locations of this area.

154 \* Memory for TLS and any initial random stack pointer offset is captured

155 \* in thread.stack\_info.delta.

156 \*/

157#ifdef CONFIG\_MPU\_STACK\_GUARD

158/\* MPU guards are only supported with V3 MPU and later. In this configuration

159 \* the stack object will contain the MPU guard, the privilege stack, and then

160 \* the stack buffer in that order:

161 \*

162 \* +------------+ <- thread.stack\_obj

163 \* | Guard | } Z\_ARC\_STACK\_GUARD\_SIZE

164 \* +------------+ <- thread.arch.priv\_stack\_start

165 \* | Priv Stack | } CONFIG\_PRIVILEGED\_STACK\_SIZE

166 \* +------------+ <- thread.stack\_info.start

167 \* | Thread |

168 \* | stack |

169 \* | |

170 \* +............|

171 \* | TLS | } thread.stack\_info.delta

172 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

173 \*/

174#define ARCH\_THREAD\_STACK\_RESERVED (Z\_ARC\_STACK\_GUARD\_SIZE + \

175 CONFIG\_PRIVILEGED\_STACK\_SIZE)

176#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_ARC\_MPU\_ALIGN

177/\* We need to be able to exactly cover the stack buffer with an MPU region,

178 \* so round its size up to the required granularity of the MPU

179 \*/

180#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

181 (ROUND\_UP((size), Z\_ARC\_MPU\_ALIGN))

182BUILD\_ASSERT(CONFIG\_PRIVILEGED\_STACK\_SIZE % Z\_ARC\_MPU\_ALIGN == 0,

183 "improper privilege stack size");

184#else /\* !CONFIG\_MPU\_STACK\_GUARD \*/

185/\* Userspace enabled, but supervisor stack guards are not in use \*/

186#ifdef CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT

187/\* Use defaults for everything. The privilege elevation stack is located

188 \* in another area of memory generated at build time by gen\_kobject\_list.py

189 \*

190 \* +------------+ <- thread.arch.priv\_stack\_start

191 \* | Priv Stack | } K\_KERNEL\_STACK\_LEN(CONFIG\_PRIVILEGED\_STACK\_SIZE)

192 \* +------------+

193 \*

194 \* +------------+ <- thread.stack\_obj = thread.stack\_info.start

195 \* | Thread |

196 \* | stack |

197 \* | |

198 \* +............|

199 \* | TLS | } thread.stack\_info.delta

200 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

201 \*/

202#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

203 Z\_POW2\_CEIL(ROUND\_UP((size), Z\_ARC\_MPU\_ALIGN))

204#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) \

205 ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size)

206#define ARCH\_THREAD\_STACK\_RESERVED 0

207#else /\* !CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT \*/

208/\* Reserved area of the thread object just contains the privilege stack:

209 \*

210 \* +------------+ <- thread.stack\_obj = thread.arch.priv\_stack\_start

211 \* | Priv Stack | } CONFIG\_PRIVILEGED\_STACK\_SIZE

212 \* +------------+ <- thread.stack\_info.start

213 \* | Thread |

214 \* | stack |

215 \* | |

216 \* +............|

217 \* | TLS | } thread.stack\_info.delta

218 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

219 \*/

[ 220](arc_2arch_8h.md#ace8831316d471ccfb06eeddb6d69d817)#define ARCH\_THREAD\_STACK\_RESERVED CONFIG\_PRIVILEGED\_STACK\_SIZE

[ 221](arc_2arch_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8)#define ARCH\_THREAD\_STACK\_SIZE\_ADJUST(size) \

222 (ROUND\_UP((size), Z\_ARC\_MPU\_ALIGN))

[ 223](arc_2arch_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7)#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_ARC\_MPU\_ALIGN

224

225BUILD\_ASSERT(CONFIG\_PRIVILEGED\_STACK\_SIZE % Z\_ARC\_MPU\_ALIGN == 0,

226 "improper privilege stack size");

227#endif /\* CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT \*/

228#endif /\* CONFIG\_MPU\_STACK\_GUARD \*/

229

230#else /\* !CONFIG\_USERSPACE \*/

231

232#ifdef CONFIG\_MPU\_STACK\_GUARD

233/\* Only supported on ARC MPU V3 and higher. Reserve some memory for the stack

234 \* guard. This is just a minimally-sized region at the beginning of the stack

235 \* object, which is programmed to produce an exception if written to.

236 \*

237 \* +------------+ <- thread.stack\_obj

238 \* | Guard | } Z\_ARC\_STACK\_GUARD\_SIZE

239 \* +------------+ <- thread.stack\_info.start

240 \* | Thread |

241 \* | stack |

242 \* | |

243 \* +............|

244 \* | TLS | } thread.stack\_info.delta

245 \* +------------+ <- thread.stack\_info.start + thread.stack\_info.size

246 \*/

247#define ARCH\_THREAD\_STACK\_RESERVED Z\_ARC\_STACK\_GUARD\_SIZE

248#define ARCH\_THREAD\_STACK\_OBJ\_ALIGN(size) Z\_ARC\_MPU\_ALIGN

249/\* Default for ARCH\_THREAD\_STACK\_SIZE\_ADJUST \*/

250#else /\* !CONFIG\_MPU\_STACK\_GUARD \*/

251/\* No stack guard, no userspace, Use defaults for everything. \*/

252#endif /\* CONFIG\_MPU\_STACK\_GUARD \*/

253#endif /\* CONFIG\_USERSPACE \*/

254

255#ifdef CONFIG\_ARC\_MPU

256

257/\* Legacy case: retain containing extern "C" with C++ \*/

258#include <[zephyr/arch/arc/v2/mpu/arc\_mpu.h](arc__mpu_8h.md)>

259

260#define K\_MEM\_PARTITION\_P\_NA\_U\_NA AUX\_MPU\_ATTR\_N

261#define K\_MEM\_PARTITION\_P\_RW\_U\_RW (AUX\_MPU\_ATTR\_UW | AUX\_MPU\_ATTR\_UR | \

262 AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR)

263#define K\_MEM\_PARTITION\_P\_RW\_U\_RO (AUX\_MPU\_ATTR\_UR | \

264 AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR)

265#define K\_MEM\_PARTITION\_P\_RW\_U\_NA (AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR)

266#define K\_MEM\_PARTITION\_P\_RO\_U\_RO (AUX\_MPU\_ATTR\_UR | AUX\_MPU\_ATTR\_KR)

267#define K\_MEM\_PARTITION\_P\_RO\_U\_NA (AUX\_MPU\_ATTR\_KR)

268

269/\* Execution-allowed attributes \*/

270#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX (AUX\_MPU\_ATTR\_UW | AUX\_MPU\_ATTR\_UR | \

271 AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR | \

272 AUX\_MPU\_ATTR\_KE | AUX\_MPU\_ATTR\_UE)

273#define K\_MEM\_PARTITION\_P\_RWX\_U\_RX (AUX\_MPU\_ATTR\_UR | \

274 AUX\_MPU\_ATTR\_KW | AUX\_MPU\_ATTR\_KR | \

275 AUX\_MPU\_ATTR\_KE | AUX\_MPU\_ATTR\_UE)

276#define K\_MEM\_PARTITION\_P\_RX\_U\_RX (AUX\_MPU\_ATTR\_UR | \

277 AUX\_MPU\_ATTR\_KR | \

278 AUX\_MPU\_ATTR\_KE | AUX\_MPU\_ATTR\_UE)

279

280#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) \

281 ({ \

282 int \_\_is\_writable\_\_; \

283 switch (attr & (AUX\_MPU\_ATTR\_UW | AUX\_MPU\_ATTR\_KW)) { \

284 case (AUX\_MPU\_ATTR\_UW | AUX\_MPU\_ATTR\_KW): \

285 case AUX\_MPU\_ATTR\_UW: \

286 case AUX\_MPU\_ATTR\_KW: \

287 \_\_is\_writable\_\_ = 1; \

288 break; \

289 default: \

290 \_\_is\_writable\_\_ = 0; \

291 break; \

292 } \

293 \_\_is\_writable\_\_; \

294 })

295#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) \

296 ((attr) & (AUX\_MPU\_ATTR\_KE | AUX\_MPU\_ATTR\_UE))

297

298/\*

299 \* BUILD\_ASSERT in case of MWDT is a bit more picky in performing compile-time check.

300 \* For example it can't evaluate variable address at build time like GCC toolchain can do.

301 \* That's why we provide custom \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK implementation for MWDT toolchain

302 \* with additional check for arguments availability in compile time.

303 \*/

304#ifdef \_\_CCAC\_\_

305#define IS\_BUILTIN\_MWDT(val) \_\_builtin\_constant\_p((uintptr\_t)(val))

306#if CONFIG\_ARC\_MPU\_VER == 2 || CONFIG\_ARC\_MPU\_VER == 3 || CONFIG\_ARC\_MPU\_VER == 6

307#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

308 BUILD\_ASSERT(IS\_BUILTIN\_MWDT(size) ? !((size) & ((size) - 1)) : 1, \

309 "partition size must be power of 2"); \

310 BUILD\_ASSERT(IS\_BUILTIN\_MWDT(size) ? (size) >= Z\_ARC\_MPU\_ALIGN : 1, \

311 "partition size must be >= mpu address alignment."); \

312 BUILD\_ASSERT(IS\_BUILTIN\_MWDT(size) ? IS\_BUILTIN\_MWDT(start) ? \

313 !((uintptr\_t)(start) & ((size) - 1)) : 1 : 1, \

314 "partition start address must align with size.")

315#elif CONFIG\_ARC\_MPU\_VER == 4 || CONFIG\_ARC\_MPU\_VER == 8

316#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

317 BUILD\_ASSERT(IS\_BUILTIN\_MWDT(size) ? (size) % Z\_ARC\_MPU\_ALIGN == 0 : 1, \

318 "partition size must align with " STRINGIFY(Z\_ARC\_MPU\_ALIGN)); \

319 BUILD\_ASSERT(IS\_BUILTIN\_MWDT(size) ? (size) >= Z\_ARC\_MPU\_ALIGN : 1, \

320 "partition size must be >= " STRINGIFY(Z\_ARC\_MPU\_ALIGN)); \

321 BUILD\_ASSERT(IS\_BUILTIN\_MWDT(start) ? (uintptr\_t)(start) % Z\_ARC\_MPU\_ALIGN == 0 : 1, \

322 "partition start address must align with " STRINGIFY(Z\_ARC\_MPU\_ALIGN))

323#endif

324#else /\* \_\_CCAC\_\_ \*/

325#if CONFIG\_ARC\_MPU\_VER == 2 || CONFIG\_ARC\_MPU\_VER == 3 || CONFIG\_ARC\_MPU\_VER == 6

326#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

327 BUILD\_ASSERT(!((size) & ((size) - 1)), \

328 "partition size must be power of 2"); \

329 BUILD\_ASSERT((size) >= Z\_ARC\_MPU\_ALIGN, \

330 "partition size must be >= mpu address alignment."); \

331 BUILD\_ASSERT(!((uintptr\_t)(start) & ((size) - 1)), \

332 "partition start address must align with size.")

333#elif CONFIG\_ARC\_MPU\_VER == 4 || CONFIG\_ARC\_MPU\_VER == 8

334#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

335 BUILD\_ASSERT((size) % Z\_ARC\_MPU\_ALIGN == 0, \

336 "partition size must align with " STRINGIFY(Z\_ARC\_MPU\_ALIGN)); \

337 BUILD\_ASSERT((size) >= Z\_ARC\_MPU\_ALIGN, \

338 "partition size must be >= " STRINGIFY(Z\_ARC\_MPU\_ALIGN)); \

339 BUILD\_ASSERT((uintptr\_t)(start) % Z\_ARC\_MPU\_ALIGN == 0, \

340 "partition start address must align with " STRINGIFY(Z\_ARC\_MPU\_ALIGN))

341#endif

342#endif /\* \_\_CCAC\_\_ \*/

343#endif /\* CONFIG\_ARC\_MPU\*/

344

345/\* Typedef for the k\_mem\_partition attribute\*/

[ 346](group__xtensa__mpu__apis.md#ga58f790e348e5e1c4a3962a134cfb505f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

347

[ 348](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

349{

350 \_\_builtin\_arc\_nop();

351}

352

353#ifndef CONFIG\_XIP

354extern char \_\_arc\_rw\_sram\_size[];

355#endif /\* CONFIG\_XIP \*/

356

357#endif /\* \_ASMLANGUAGE \*/

358

359#ifdef \_\_cplusplus

360}

361#endif

362#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_ARCH\_H\_ \*/

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[ARCH\_STACK\_PTR\_ALIGN](arc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)

#define ARCH\_STACK\_PTR\_ALIGN

**Definition** arch.h:98

[asm\_inline.h](arc_2v2_2asm__inline_8h.md)

[exception.h](arc_2v2_2exception_8h.md)

ARCv2 public exception handling.

[misc.h](arc_2v2_2misc_8h.md)

ARCv2 public kernel miscellaneous.

[arc\_addr\_types.h](arc__addr__types_8h.md)

[arc\_connect.h](arc__connect_8h.md)

ARCv2 ARC Connect driver.

[arc\_mpu.h](arc__mpu_8h.md)

[arc\_secure.h](arc__secure_8h.md)

[thread.h](arch_2arc_2thread_8h.md)

Per-arch thread definition.

[irq.h](arch_2arc_2v2_2irq_8h.md)

ARCv2 public interrupt handling.

[sys\_io.h](arch_2arc_2v2_2sys__io_8h.md)

[arcv2\_irq\_unit.h](arcv2__irq__unit_8h.md)

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[error.h](include_2zephyr_2arch_2arc_2v2_2error_8h.md)

ARCv2 public error handling.

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[sys-io-common.h](sys-io-common_8h.md)

[sys\_bitops.h](sys__bitops_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [arch.h](arc_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
