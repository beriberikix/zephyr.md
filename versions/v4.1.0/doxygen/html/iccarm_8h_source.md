---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/iccarm_8h_source.html
original_path: doxygen/html/iccarm_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iccarm.h

[Go to the documentation of this file.](iccarm_8h.md)

1/\*

2 \* Copyright (c) 2025 IAR Systems AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_ICCARM\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_ICCARM\_H\_

9

16

17/\* ICCARM supports its own #pragma diag\_{warning,default,error,warning}. \*/

18/\* #define TOOLCHAIN\_HAS\_PRAGMA\_DIAG 0 \*/

19

[ 20](iccarm_8h.md#a49263980cf39cd330a9e9976dccb4c90)#define TOOLCHAIN\_HAS\_C\_GENERIC 1

21

[ 22](iccarm_8h.md#a9502cad506e0dfb7c3a7b51b5eeb5eeb)#define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE 1

23

24/\* #define TOOLCHAIN\_HAS\_ZLA 1 \*/

25

26/\*

27 \* IAR do not define \_\_BYTE\_ORDER\_\_, so it must be manually

28 \* detected and defined using arch-specific definitions.

29 \*/

30

31#ifndef \_LINKER

32

33#ifndef \_\_ORDER\_BIG\_ENDIAN\_\_

34#define \_\_ORDER\_BIG\_ENDIAN\_\_ (1)

35#endif /\* \_\_ORDER\_BIG\_ENDIAN\_\_ \*/

36

37#ifndef \_\_ORDER\_LITTLE\_ENDIAN\_\_

38#define \_\_ORDER\_LITTLE\_ENDIAN\_\_ (2)

39#endif /\* \_\_ORDER\_LITTLE\_ENDIAN\_\_ \*/

40

41#ifndef \_\_ORDER\_PDP\_ENDIAN\_\_

42#define \_\_ORDER\_PDP\_ENDIAN\_\_ (3)

43#endif /\* \_\_ORDER\_PDP\_ENDIAN\_\_ \*/

44

45#ifndef \_\_BYTE\_ORDER\_\_

46

47#if \_\_LITTLE\_ENDIAN\_\_ == 1

48#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_LITTLE\_ENDIAN\_\_

49#else

50#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_BIG\_ENDIAN\_\_

51#endif /\* \_\_LITTLE\_ENDIAN\_\_ == 1 \*/

52

53#endif /\* \_\_BYTE\_ORDER\_\_ \*/

54

55

56#if defined(\_\_cplusplus) && (\_\_cplusplus >= 201103L)

57#define BUILD\_ASSERT(EXPR, MSG...) static\_assert(EXPR, "" MSG)

58#elif defined(\_\_ICCARM\_\_)

59#define BUILD\_ASSERT(EXPR, MSG...) \_Static\_assert(EXPR, "" MSG)

60#endif

61

62/\* Zephyr makes use of \_\_ATOMIC\_SEQ\_CST \*/

63#ifdef \_\_STDC\_NO\_ATOMICS\_\_

64#ifndef \_\_ATOMIC\_SEQ\_CST

65#define \_\_MEMORY\_ORDER\_SEQ\_CST\_\_ 5

66#endif

67#endif

68#ifndef \_\_ATOMIC\_SEQ\_CST

69#define \_\_ATOMIC\_SEQ\_CST \_\_MEMORY\_ORDER\_SEQ\_CST\_\_

70#endif

71

72/\* By default, restrict is recognized in Standard C

73 \* \_\_restrict is always recognized

74 \*/

75#define ZRESTRICT \_\_restrict

76

77#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h.md)>

78#include <[stdbool.h](stdbool_8h.md)>

79

80#define ALIAS\_OF(of) \_\_attribute\_\_((alias(#of)))

81

82#define FUNC\_ALIAS(real\_func, new\_alias, return\_type) \

83 return\_type new\_alias() ALIAS\_OF(real\_func)

84

85#define CODE\_UNREACHABLE \_\_builtin\_unreachable()

86#define FUNC\_NORETURN \_\_attribute\_\_((\_\_noreturn\_\_))

87

88#define \_NODATA\_SECTION(segment) \_\_attribute\_\_((section(#segment)))

89

90/\* Unaligned access \*/

91#define UNALIGNED\_GET(p) \

92\_\_extension\_\_ ({ \

93 struct \_\_attribute\_\_((\_\_packed\_\_)) { \

94 \_\_typeof\_\_(\*(p)) \_\_v; \

95 } \*\_\_p = (\_\_typeof\_\_(\_\_p)) (p); \

96 \_\_p->\_\_v; \

97})

98

99#define UNALIGNED\_PUT(v, p) \

100do { \

101 struct \_\_attribute\_\_((\_\_packed\_\_)) { \

102 \_\_typeof\_\_(\*p) \_\_v; \

103 } \*\_\_p = (\_\_typeof\_\_(\_\_p)) (p); \

104 \_\_p->\_\_v = (v); \

105} while (false)

106

107

108/\* Double indirection to ensure section names are expanded before

109 \* stringification

110 \*/

111#define \_\_GENERIC\_SECTION(segment) \_\_attribute\_\_((section(STRINGIFY(segment))))

112#define Z\_GENERIC\_SECTION(segment) \_\_GENERIC\_SECTION(segment)

113

114#define \_\_GENERIC\_DOT\_SECTION(segment) \

115 \_\_attribute\_\_((section("." STRINGIFY(segment))))

116#define Z\_GENERIC\_DOT\_SECTION(segment) \_\_GENERIC\_DOT\_SECTION(segment)

117

118#define \_\_\_in\_section(a, b, c) \

119 \_\_attribute\_\_((section("." Z\_STRINGIFY(a) \

120 "." Z\_STRINGIFY(b) \

121 "." Z\_STRINGIFY(c))))

122#define \_\_in\_section(a, b, c) \_\_\_in\_section(a, b, c)

123

124#define \_\_in\_section\_unique(seg) \_\_\_in\_section(seg, \_\_FILE\_\_, \_\_COUNTER\_\_)

125

126#define \_\_in\_section\_unique\_named(seg, name) \

127 \_\_\_in\_section(seg, \_\_FILE\_\_, name)

128

129/\* When using XIP, using '\_\_ramfunc' places a function into RAM instead

130 \* of FLASH. Make sure '\_\_ramfunc' is defined only when

131 \* CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT is defined, so that the compiler can

132 \* report an error if '\_\_ramfunc' is used but the architecture does not

133 \* support it.

134 \*/

135#if !defined(CONFIG\_XIP)

136#define \_\_ramfunc

137#elif defined(CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT)

138/\* Use this instead of the IAR keyword \_\_ramfunc to make sure it

139 \* ends up in the correct section.

140 \*/

141#define \_\_ramfunc \_\_attribute\_\_((noinline, section(".ramfunc")))

142#endif /\* !CONFIG\_XIP \*/

143

144/\* TG-WG: ICCARM does not support \_\_fallthrough \*/

145#define \_\_fallthrough [[fallthrough]]

146

147#ifndef \_\_packed

148#define \_\_packed \_\_attribute\_\_((\_\_packed\_\_))

149#endif

150

151#ifndef \_\_aligned

152#define \_\_aligned(x) \_\_attribute\_\_((\_\_aligned\_\_(x)))

153#endif

154

155#ifndef \_\_noinline

156#define \_\_noinline \_\_attribute\_\_((noinline))

157#endif

158

159#if defined(\_\_cplusplus)

160#define \_\_alignof(x) alignof(x)

161#else

162#define \_\_alignof(x) \_Alignof(x)

163#endif

164

165#define \_\_may\_alias \_\_attribute\_\_((\_\_may\_alias\_\_))

166

167#ifndef \_\_printf\_like

168/\*

169 \* The Zephyr stdint convention enforces int32\_t = int, int64\_t = long long,

170 \* and intptr\_t = long so that short string format length modifiers can be

171 \* used universally across ILP32 and LP64 architectures. Without that it

172 \* is possible for ILP32 toolchains to have int32\_t = long and intptr\_t = int

173 \* clashing with the Zephyr convention and generating pointless warnings

174 \* as they're still the same size. Inhibit the format argument type

175 \* validation in that case and let the other configs do it.

176 \*/

177#define \_\_printf\_like(f, a)

178#endif

179

180#define \_\_used \_\_attribute\_\_((\_\_used\_\_))

181#define \_\_unused \_\_attribute\_\_((\_\_unused\_\_))

182#define \_\_maybe\_unused \_\_attribute\_\_((\_\_unused\_\_))

183

184#ifndef \_\_deprecated

185#define \_\_deprecated \_\_attribute\_\_((deprecated))

186#endif

187

188#define FUNC\_NO\_STACK\_PROTECTOR \_Pragma("no\_stack\_protect")

189

190#ifndef \_\_attribute\_const\_\_

191#if \_\_VER\_\_ > 0x09000000

192#define \_\_attribute\_const\_\_ \_\_attribute\_\_((const))

193#else

194#define \_\_attribute\_const\_\_

195#endif

196#endif

197

198#ifndef \_\_must\_check

199/\* #warning "The attribute \_\_warn\_unused\_result is not supported in ICCARM". \*/

200#define \_\_must\_check

201/\* #define \_\_must\_check \_\_attribute\_\_((warn\_unused\_result)) \*/

202#endif

203

204#define \_\_PRAGMA(...) \_Pragma(#\_\_VA\_ARGS\_\_)

205#define ARG\_UNUSED(x) (void)(x)

206

207#define likely(x) (\_\_builtin\_expect((bool)!!(x), true) != 0L)

208#define unlikely(x) (\_\_builtin\_expect((bool)!!(x), false) != 0L)

209#define POPCOUNT(x) \_\_builtin\_popcount(x)

210

211#ifndef \_\_no\_optimization

212#define \_\_no\_optimization \_\_PRAGMA(optimize = none)

213#endif

214

215#ifndef \_\_attribute\_nonnull

216 #define \_\_attribute\_nonnull(...) \_\_attribute\_\_((nonnull(\_\_VA\_ARGS\_\_)))

217#endif

218

219/\* \_\_weak is an ICCARM built-in, but it doesn't work in all positions \*/

220/\* the Zephyr uses it so we replace it with an attribute((weak)) \*/

221#define \_\_weak \_\_attribute\_\_((\_\_weak\_\_))

222

223/\* Builtins \*/

224

225#include <intrinsics.h>

226

227/\*

228 \* Be \*very\* careful with these. You cannot filter out \_\_DEPRECATED\_MACRO with

229 \* -wno-deprecated, which has implications for -Werror.

230 \*/

231

232

233/\*

234 \* Expands to nothing and generates a warning. Used like

235 \*

236 \* #define FOO \_\_WARN("Please use BAR instead") ...

237 \*

238 \* The warning points to the location where the macro is expanded.

239 \*/

240#define \_\_WARN(s) \_\_PRAGMA(message = #s)

241#define \_\_WARN1(s) \_\_PRAGMA(message = #s)

242

243/\* Generic message \*/

244#ifndef \_\_DEPRECATED\_MACRO

245#define \_\_DEPRECATED\_MACRO \_\_WARN("Macro is deprecated")

246#endif

247

248/\* These macros allow having ARM asm functions callable from thumb \*/

249

250#if defined(\_ASMLANGUAGE)

251

252#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

253#define FUNC\_CODE() .code 32

254#define FUNC\_INSTR(a)

255/\* '.syntax unified' is a gcc-ism used in thumb-2 asm files \*/

256#define \_ASM\_FILE\_PROLOGUE .text; .syntax unified; .thumb

257#else

258#define FUNC\_CODE()

259#define FUNC\_INSTR(a)

260#define \_ASM\_FILE\_PROLOGUE .text; .code 32

261#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

262

263/\*

264 \* These macros are used to declare assembly language symbols that need

265 \* to be typed properly(func or data) to be visible to the OMF tool.

266 \* So that the build tool could mark them as an entry point to be linked

267 \* correctly. This is an elfism. Use #if 0 for a.out.

268 \*/

269

270/\* This is not implemented yet for IAR \*/

271#define GTEXT(sym)

272#define GDATA(sym)

273#define WTEXT(sym)

274#define WDATA(sym)

275

276#define SECTION\_VAR(sect, sym)

277#define SECTION\_FUNC(sect, sym)

278#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym)

279

280#endif /\* \_ASMLANGUAGE \*/

281

282

283/\*

284 \* These macros generate absolute symbols for IAR

285 \*/

286

287/\* create an extern reference to the absolute symbol \*/

288

289#define GEN\_OFFSET\_EXTERN(name) extern const char name[]

290

291#define GEN\_ABS\_SYM\_BEGIN(name) \

292 EXTERN\_C void name(void); \

293 void name(void) \

294 {

295

296#define GEN\_ABS\_SYM\_END }

297

298/\*

299 \* Note that GEN\_ABSOLUTE\_SYM(), depending on the architecture

300 \* and toolchain, may restrict the range of values permitted

301 \* for assignment to the named symbol.

302 \*/

303#define GEN\_ABSOLUTE\_SYM(name, value) \

304 \_\_PRAGMA(public\_equ = #name, (unsigned int)value)

305

306/\*

307 \* GEN\_ABSOLUTE\_SYM\_KCONFIG() is outputted by the build system

308 \* to generate named symbol/value pairs for kconfigs.

309 \*/

310#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

311 \_\_PRAGMA(public\_equ = #name, (unsigned int)value)

312

313#define compiler\_barrier() do { \

314 \_\_asm volatile("" ::: "memory"); \

315} while (false)

316

326#define Z\_MAX(a, b) ({ \

327 /\* random suffix to avoid naming conflict \*/ \

328 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

329 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

330 \_value\_a\_ > \_value\_b\_ ? \_value\_a\_ : \_value\_b\_; \

331 })

332

338#define Z\_MIN(a, b) ({ \

339 /\* random suffix to avoid naming conflict \*/ \

340 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

341 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

342 \_value\_a\_ < \_value\_b\_ ? \_value\_a\_ : \_value\_b\_; \

343 })

344

350#define Z\_CLAMP(val, low, high) ({ \

351 /\* random suffix to avoid naming conflict \*/ \

352 \_\_typeof\_\_(val) \_value\_val\_ = (val); \

353 \_\_typeof\_\_(low) \_value\_low\_ = (low); \

354 \_\_typeof\_\_(high) \_value\_high\_ = (high); \

355 (\_value\_val\_ < \_value\_low\_) ? \_value\_low\_ : \

356 (\_value\_val\_ > \_value\_high\_) ? \_value\_high\_ : \

357 \_value\_val\_; \

358 })

359

366#define Z\_POW2\_CEIL(x) \

367 ((x) <= 2UL ? (x) : (1UL << (8 \* sizeof(long) - \_\_builtin\_clzl((x) - 1))))

368

375#define Z\_IS\_POW2(x) (((x) != 0) && (((x) & ((x)-1)) == 0))

376

377#ifndef \_\_INT8\_C

378#define \_\_INT8\_C(x) x

379#endif

380

381#ifndef INT8\_C

382#define INT8\_C(x) \_\_INT8\_C(x)

383#endif

384

385#ifndef \_\_UINT8\_C

386#define \_\_UINT8\_C(x) x ## U

387#endif

388

389#ifndef UINT8\_C

390#define UINT8\_C(x) \_\_UINT8\_C(x)

391#endif

392

393#ifndef \_\_INT16\_C

394#define \_\_INT16\_C(x) x

395#endif

396

397#ifndef INT16\_C

398#define INT16\_C(x) \_\_INT16\_C(x)

399#endif

400

401#ifndef \_\_UINT16\_C

402#define \_\_UINT16\_C(x) x ## U

403#endif

404

405#ifndef UINT16\_C

406#define UINT16\_C(x) \_\_UINT16\_C(x)

407#endif

408

409#ifndef \_\_INT32\_C

410#define \_\_INT32\_C(x) x

411#endif

412

413#ifndef INT32\_C

414#define INT32\_C(x) \_\_INT32\_C(x)

415#endif

416

417#ifndef \_\_UINT32\_C

418#define \_\_UINT32\_C(x) x ## U

419#endif

420

421#ifndef UINT32\_C

422#define UINT32\_C(x) \_\_UINT32\_C(x)

423#endif

424

425#ifndef \_\_INT64\_C

426#define \_\_INT64\_C(x) x ## LL

427#endif

428

429#ifndef INT64\_C

430#define INT64\_C(x) \_\_INT64\_C(x)

431#endif

432

433#ifndef \_\_UINT64\_C

434#define \_\_UINT64\_C(x) x ## ULL

435#endif

436

437#ifndef UINT64\_C

438#define UINT64\_C(x) \_\_UINT64\_C(x)

439#endif

440

441/\* Convenience macros \*/

442#undef \_GLUE\_B

443#undef \_GLUE

444#define \_GLUE\_B(x, y) x##y

445#define \_GLUE(x, y) \_GLUE\_B(x, y)

446

447#ifndef INTMAX\_C

448#define INTMAX\_C(x) \_GLUE(x, \_\_INTMAX\_C\_SUFFIX\_\_)

449#endif

450

451#ifndef UINTMAX\_C

452#define UINTMAX\_C(x) \_GLUE(x, \_\_UINTMAX\_C\_SUFFIX\_\_)

453#endif

454

455#endif /\* !\_LINKER \*/

456#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_ICCARM\_H\_ \*/

[common.h](include_2zephyr_2toolchain_2common_8h.md)

Common toolchain abstraction.

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [iar](dir_cb961a4998504dcfcaac26ca40155226.md)
- [iccarm.h](iccarm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
