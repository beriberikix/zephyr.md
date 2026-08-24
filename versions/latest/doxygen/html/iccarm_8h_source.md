---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/iccarm_8h_source.html
original_path: doxygen/html/iccarm_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

144#ifndef \_\_fallthrough

145/\* TG-WG: ICCARM does not support \_\_fallthrough \*/

146#define \_\_fallthrough [[fallthrough]]

147#endif

148

149#ifndef \_\_packed

150#define \_\_packed \_\_attribute\_\_((\_\_packed\_\_))

151#endif

152

153#ifndef \_\_aligned

154#define \_\_aligned(x) \_\_attribute\_\_((\_\_aligned\_\_(x)))

155#endif

156

157#ifndef \_\_noinline

158#define \_\_noinline \_\_attribute\_\_((noinline))

159#endif

160

161#if defined(\_\_cplusplus)

162#define \_\_alignof(x) alignof(x)

163#else

164#define \_\_alignof(x) \_Alignof(x)

165#endif

166

167#define \_\_may\_alias \_\_attribute\_\_((\_\_may\_alias\_\_))

168

169#ifndef \_\_printf\_like

170/\*

171 \* The Zephyr stdint convention enforces int32\_t = int, int64\_t = long long,

172 \* and intptr\_t = long so that short string format length modifiers can be

173 \* used universally across ILP32 and LP64 architectures. Without that it

174 \* is possible for ILP32 toolchains to have int32\_t = long and intptr\_t = int

175 \* clashing with the Zephyr convention and generating pointless warnings

176 \* as they're still the same size. Inhibit the format argument type

177 \* validation in that case and let the other configs do it.

178 \*/

179#define \_\_printf\_like(f, a)

180#endif

181

182#define \_\_used \_\_attribute\_\_((\_\_used\_\_))

183#define \_\_unused \_\_attribute\_\_((\_\_unused\_\_))

184#define \_\_maybe\_unused \_\_attribute\_\_((\_\_unused\_\_))

185

186#ifndef \_\_deprecated

187#define \_\_deprecated \_\_attribute\_\_((deprecated))

188#endif

189

190#define FUNC\_NO\_STACK\_PROTECTOR \_Pragma("no\_stack\_protect")

191

192#ifndef \_\_attribute\_const\_\_

193#if \_\_VER\_\_ > 0x09000000

194#define \_\_attribute\_const\_\_ \_\_attribute\_\_((const))

195#else

196#define \_\_attribute\_const\_\_

197#endif

198#endif

199

200#ifndef \_\_must\_check

201/\* #warning "The attribute \_\_warn\_unused\_result is not supported in ICCARM". \*/

202#define \_\_must\_check

203/\* #define \_\_must\_check \_\_attribute\_\_((warn\_unused\_result)) \*/

204#endif

205

206#define \_\_PRAGMA(...) \_Pragma(#\_\_VA\_ARGS\_\_)

207#define ARG\_UNUSED(x) (void)(x)

208

209#define likely(x) (\_\_builtin\_expect((bool)!!(x), true) != 0L)

210#define unlikely(x) (\_\_builtin\_expect((bool)!!(x), false) != 0L)

211#define POPCOUNT(x) \_\_builtin\_popcount(x)

212

213#ifndef \_\_no\_optimization

214#define \_\_no\_optimization \_\_PRAGMA(optimize = none)

215#endif

216

217#ifndef \_\_attribute\_nonnull

218 #define \_\_attribute\_nonnull(...) \_\_attribute\_\_((nonnull(\_\_VA\_ARGS\_\_)))

219#endif

220

221/\* \_\_weak is an ICCARM built-in, but it doesn't work in all positions \*/

222/\* the Zephyr uses it so we replace it with an attribute((weak)) \*/

223#define \_\_weak \_\_attribute\_\_((\_\_weak\_\_))

224

225/\* Builtins \*/

226

227#include <intrinsics.h>

228

229/\*

230 \* Be \*very\* careful with these. You cannot filter out \_\_DEPRECATED\_MACRO with

231 \* -wno-deprecated, which has implications for -Werror.

232 \*/

233

234

235/\*

236 \* Expands to nothing and generates a warning. Used like

237 \*

238 \* #define FOO \_\_WARN("Please use BAR instead") ...

239 \*

240 \* The warning points to the location where the macro is expanded.

241 \*/

242#define \_\_WARN(s) \_\_PRAGMA(message = #s)

243#define \_\_WARN1(s) \_\_PRAGMA(message = #s)

244

245/\* Generic message \*/

246#ifndef CONFIG\_DEPRECATION\_TEST

247#define \_\_DEPRECATED\_MACRO \_\_WARN("Macro is deprecated")

248#else

249#define \_\_DEPRECATED\_MACRO

250#endif

251

252

253

254/\* These macros allow having ARM asm functions callable from thumb \*/

255

256#if defined(\_ASMLANGUAGE)

257

258#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

259#define FUNC\_CODE() .code 32

260#define FUNC\_INSTR(a)

261/\* '.syntax unified' is a gcc-ism used in thumb-2 asm files \*/

262#define \_ASM\_FILE\_PROLOGUE .text; .syntax unified; .thumb

263#else

264#define FUNC\_CODE()

265#define FUNC\_INSTR(a)

266#define \_ASM\_FILE\_PROLOGUE .text; .code 32

267#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

268

269/\*

270 \* These macros are used to declare assembly language symbols that need

271 \* to be typed properly(func or data) to be visible to the OMF tool.

272 \* So that the build tool could mark them as an entry point to be linked

273 \* correctly. This is an elfism. Use #if 0 for a.out.

274 \*/

275

276/\* This is not implemented yet for IAR \*/

277#define GTEXT(sym)

278#define GDATA(sym)

279#define WTEXT(sym)

280#define WDATA(sym)

281

282#define SECTION\_VAR(sect, sym)

283#define SECTION\_FUNC(sect, sym)

284#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym)

285

286#endif /\* \_ASMLANGUAGE \*/

287

288

289/\*

290 \* These macros generate absolute symbols for IAR

291 \*/

292

293/\* create an extern reference to the absolute symbol \*/

294

295#define GEN\_OFFSET\_EXTERN(name) extern const char name[]

296

297#define GEN\_ABS\_SYM\_BEGIN(name) \

298 EXTERN\_C void name(void); \

299 void name(void) \

300 {

301

302#define GEN\_ABS\_SYM\_END }

303

304/\*

305 \* Note that GEN\_ABSOLUTE\_SYM(), depending on the architecture

306 \* and toolchain, may restrict the range of values permitted

307 \* for assignment to the named symbol.

308 \*/

309#define GEN\_ABSOLUTE\_SYM(name, value) \

310 \_\_PRAGMA(public\_equ = #name, (unsigned int)value)

311

312/\*

313 \* GEN\_ABSOLUTE\_SYM\_KCONFIG() is outputted by the build system

314 \* to generate named symbol/value pairs for kconfigs.

315 \*/

316#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

317 \_\_PRAGMA(public\_equ = #name, (unsigned int)value)

318

319#define compiler\_barrier() do { \

320 \_\_asm volatile("" ::: "memory"); \

321} while (false)

322

332#define Z\_MAX(a, b) ({ \

333 /\* random suffix to avoid naming conflict \*/ \

334 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

335 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

336 \_value\_a\_ > \_value\_b\_ ? \_value\_a\_ : \_value\_b\_; \

337 })

338

344#define Z\_MIN(a, b) ({ \

345 /\* random suffix to avoid naming conflict \*/ \

346 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

347 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

348 \_value\_a\_ < \_value\_b\_ ? \_value\_a\_ : \_value\_b\_; \

349 })

350

356#define Z\_CLAMP(val, low, high) ({ \

357 /\* random suffix to avoid naming conflict \*/ \

358 \_\_typeof\_\_(val) \_value\_val\_ = (val); \

359 \_\_typeof\_\_(low) \_value\_low\_ = (low); \

360 \_\_typeof\_\_(high) \_value\_high\_ = (high); \

361 (\_value\_val\_ < \_value\_low\_) ? \_value\_low\_ : \

362 (\_value\_val\_ > \_value\_high\_) ? \_value\_high\_ : \

363 \_value\_val\_; \

364 })

365

372#define Z\_POW2\_CEIL(x) \

373 ((x) <= 2UL ? (x) : (1UL << (8 \* sizeof(long) - \_\_builtin\_clzl((x) - 1))))

374

381#define Z\_IS\_POW2(x) (((x) != 0) && (((x) & ((x)-1)) == 0))

382

383#ifndef \_\_INT8\_C

384#define \_\_INT8\_C(x) x

385#endif

386

387#ifndef INT8\_C

388#define INT8\_C(x) \_\_INT8\_C(x)

389#endif

390

391#ifndef \_\_UINT8\_C

392#define \_\_UINT8\_C(x) x ## U

393#endif

394

395#ifndef UINT8\_C

396#define UINT8\_C(x) \_\_UINT8\_C(x)

397#endif

398

399#ifndef \_\_INT16\_C

400#define \_\_INT16\_C(x) x

401#endif

402

403#ifndef INT16\_C

404#define INT16\_C(x) \_\_INT16\_C(x)

405#endif

406

407#ifndef \_\_UINT16\_C

408#define \_\_UINT16\_C(x) x ## U

409#endif

410

411#ifndef UINT16\_C

412#define UINT16\_C(x) \_\_UINT16\_C(x)

413#endif

414

415#ifndef \_\_INT32\_C

416#define \_\_INT32\_C(x) x

417#endif

418

419#ifndef INT32\_C

420#define INT32\_C(x) \_\_INT32\_C(x)

421#endif

422

423#ifndef \_\_UINT32\_C

424#define \_\_UINT32\_C(x) x ## U

425#endif

426

427#ifndef UINT32\_C

428#define UINT32\_C(x) \_\_UINT32\_C(x)

429#endif

430

431#ifndef \_\_INT64\_C

432#define \_\_INT64\_C(x) x ## LL

433#endif

434

435#ifndef INT64\_C

436#define INT64\_C(x) \_\_INT64\_C(x)

437#endif

438

439#ifndef \_\_UINT64\_C

440#define \_\_UINT64\_C(x) x ## ULL

441#endif

442

443#ifndef UINT64\_C

444#define UINT64\_C(x) \_\_UINT64\_C(x)

445#endif

446

447/\* Convenience macros \*/

448#undef \_GLUE\_B

449#undef \_GLUE

450#define \_GLUE\_B(x, y) x##y

451#define \_GLUE(x, y) \_GLUE\_B(x, y)

452

453#ifndef INTMAX\_C

454#define INTMAX\_C(x) \_GLUE(x, \_\_INTMAX\_C\_SUFFIX\_\_)

455#endif

456

457#ifndef UINTMAX\_C

458#define UINTMAX\_C(x) \_GLUE(x, \_\_UINTMAX\_C\_SUFFIX\_\_)

459#endif

460

461#endif /\* !\_LINKER \*/

462#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_ICCARM\_H\_ \*/

[common.h](include_2zephyr_2toolchain_2common_8h.md)

Common toolchain abstraction.

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [iar](dir_cb961a4998504dcfcaac26ca40155226.md)
- [iccarm.h](iccarm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
