---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gcc_8h_source.html
original_path: doxygen/html/gcc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gcc.h

[Go to the documentation of this file.](gcc_8h.md)

1/\*

2 \* Copyright (c) 2010-2014,2017 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_GCC\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_GCC\_H\_

9

10#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_H\_

11#error Please do not include toolchain-specific headers directly, use <zephyr/toolchain.h> instead

12#endif

13

20

[ 21](gcc_8h.md#acbf8a21b471b2086cbe276789c5061d5)#define TOOLCHAIN\_GCC\_VERSION \

22 ((\_\_GNUC\_\_ \* 10000) + (\_\_GNUC\_MINOR\_\_ \* 100) + \_\_GNUC\_PATCHLEVEL\_\_)

23

24/\* GCC supports #pragma diagnostics since 4.6.0 \*/

25#if !defined(TOOLCHAIN\_HAS\_PRAGMA\_DIAG) && (TOOLCHAIN\_GCC\_VERSION >= 40600)

26#define TOOLCHAIN\_HAS\_PRAGMA\_DIAG 1

27#endif

28

29#if !defined(TOOLCHAIN\_HAS\_C\_GENERIC) && (TOOLCHAIN\_GCC\_VERSION >= 40900)

30#define TOOLCHAIN\_HAS\_C\_GENERIC 1

31#endif

32

33#if !defined(TOOLCHAIN\_HAS\_C\_AUTO\_TYPE) && (TOOLCHAIN\_GCC\_VERSION >= 40900)

34#define TOOLCHAIN\_HAS\_C\_AUTO\_TYPE 1

35#endif

36

[ 37](gcc_8h.md#a90e5fd6ed234d1494c7f156635c2e6e1)#define TOOLCHAIN\_HAS\_ZLA 1

38

39/\*

40 \* Older versions of GCC do not define \_\_BYTE\_ORDER\_\_, so it must be manually

41 \* detected and defined using arch-specific definitions.

42 \*/

43

44#ifndef \_LINKER

45

46#ifndef \_\_ORDER\_BIG\_ENDIAN\_\_

47#define \_\_ORDER\_BIG\_ENDIAN\_\_ (1)

48#endif

49

50#ifndef \_\_ORDER\_LITTLE\_ENDIAN\_\_

51#define \_\_ORDER\_LITTLE\_ENDIAN\_\_ (2)

52#endif

53

54#ifndef \_\_BYTE\_ORDER\_\_

55#if defined(\_\_BIG\_ENDIAN\_\_) || defined(\_\_ARMEB\_\_) || \

56 defined(\_\_THUMBEB\_\_) || defined(\_\_AARCH64EB\_\_) || \

57 defined(\_\_MIPSEB\_\_) || defined(\_\_TC32EB\_\_)

58

59#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_BIG\_ENDIAN\_\_

60

61#elif defined(\_\_LITTLE\_ENDIAN\_\_) || defined(\_\_ARMEL\_\_) || \

62 defined(\_\_THUMBEL\_\_) || defined(\_\_AARCH64EL\_\_) || \

63 defined(\_\_MIPSEL\_\_) || defined(\_\_TC32EL\_\_)

64

65#define \_\_BYTE\_ORDER\_\_ \_\_ORDER\_LITTLE\_ENDIAN\_\_

66

67#else

68#error "\_\_BYTE\_ORDER\_\_ is not defined and cannot be automatically resolved"

69#endif

70#endif

71

72

73#undef BUILD\_ASSERT /\* clear out common version \*/

74/\* C++11 has static\_assert built in \*/

75#if defined(\_\_cplusplus) && (\_\_cplusplus >= 201103L)

76#define BUILD\_ASSERT(EXPR, MSG...) static\_assert(EXPR, "" MSG)

77

78/\*

79 \* GCC 4.6 and higher have the C11 \_Static\_assert built in and its

80 \* output is easier to understand than the common BUILD\_ASSERT macros.

81 \* Don't use this in C++98 mode though (which we can hit, as

82 \* static\_assert() is not available)

83 \*/

84#elif !defined(\_\_cplusplus) && \

85 ((\_\_GNUC\_\_ > 4 || (\_\_GNUC\_\_ == 4 && \_\_GNUC\_MINOR\_\_ >= 6)) || \

86 (\_\_STDC\_VERSION\_\_) >= 201100)

87#define BUILD\_ASSERT(EXPR, MSG...) \_Static\_assert(EXPR, "" MSG)

88#else

89#define BUILD\_ASSERT(EXPR, MSG...)

90#endif

91

92#ifdef \_\_cplusplus

93#define ZRESTRICT \_\_restrict

94#else

95#define ZRESTRICT restrict

96#endif

97

98#include <[zephyr/toolchain/common.h](common_8h.md)>

99#include <[stdbool.h](stdbool_8h.md)>

100

101#define ALIAS\_OF(of) \_\_attribute\_\_((alias(#of)))

102

103#define FUNC\_ALIAS(real\_func, new\_alias, return\_type) \

104 return\_type new\_alias() ALIAS\_OF(real\_func)

105

106#if defined(CONFIG\_ARCH\_POSIX) && !defined(\_ASMLANGUAGE)

107#include <[zephyr/arch/posix/posix\_trace.h](posix__trace_8h.md)>

108

109/\*let's not segfault if this were to happen for some reason\*/

110#define CODE\_UNREACHABLE \

111{\

112 posix\_print\_error\_and\_exit("CODE\_UNREACHABLE reached from %s:%d\n",\

113 \_\_FILE\_\_, \_\_LINE\_\_);\

114 \_\_builtin\_unreachable(); \

115}

116#else

117#define CODE\_UNREACHABLE \_\_builtin\_unreachable()

118#endif

119#define FUNC\_NORETURN \_\_attribute\_\_((\_\_noreturn\_\_))

120

121/\* The GNU assembler for Cortex-M3 uses # for immediate values, not

122 \* comments, so the @nobits# trick does not work.

123 \*/

124#if defined(CONFIG\_ARM) || defined(CONFIG\_ARM64)

125#define \_NODATA\_SECTION(segment) \_\_attribute\_\_((section(#segment)))

126#else

127#define \_NODATA\_SECTION(segment) \

128 \_\_attribute\_\_((section(#segment ",\"wa\",@nobits#")))

129#endif

130

131/\* Unaligned access \*/

132#define UNALIGNED\_GET(g) \

133\_\_extension\_\_ ({ \

134 struct \_\_attribute\_\_((\_\_packed\_\_)) { \

135 \_\_typeof\_\_(\*(g)) \_\_v; \

136 } \*\_\_g = (\_\_typeof\_\_(\_\_g)) (g); \

137 \_\_g->\_\_v; \

138})

139

140

141#if \_\_GNUC\_\_ >= 7 && (defined(CONFIG\_ARM) || defined(CONFIG\_ARM64))

142

143/\* Version of UNALIGNED\_PUT() which issues a compiler\_barrier() after

144 \* the store. It is required to workaround an apparent optimization

145 \* bug in GCC for ARM Cortex-M3 and higher targets, when multiple

146 \* byte, half-word and word stores (strb, strh, str instructions),

147 \* which support unaligned access, can be coalesced into store double

148 \* (strd) instruction, which doesn't support unaligned access (the

149 \* compilers in question do this optimization ignoring \_\_packed\_\_

150 \* attribute).

151 \*/

152#define UNALIGNED\_PUT(v, p) \

153do { \

154 struct \_\_attribute\_\_((\_\_packed\_\_)) { \

155 \_\_typeof\_\_(\*p) \_\_v; \

156 } \*\_\_p = (\_\_typeof\_\_(\_\_p)) (p); \

157 \_\_p->\_\_v = (v); \

158 compiler\_barrier(); \

159} while (false)

160

161#else

162

163#define UNALIGNED\_PUT(v, p) \

164do { \

165 struct \_\_attribute\_\_((\_\_packed\_\_)) { \

166 \_\_typeof\_\_(\*p) \_\_v; \

167 } \*\_\_p = (\_\_typeof\_\_(\_\_p)) (p); \

168 \_\_p->\_\_v = (v); \

169} while (false)

170

171#endif

172

173/\* Double indirection to ensure section names are expanded before

174 \* stringification

175 \*/

176#define \_\_GENERIC\_SECTION(segment) \_\_attribute\_\_((section(STRINGIFY(segment))))

177#define Z\_GENERIC\_SECTION(segment) \_\_GENERIC\_SECTION(segment)

178

179#define \_\_GENERIC\_DOT\_SECTION(segment) \

180 \_\_attribute\_\_((section("." STRINGIFY(segment))))

181#define Z\_GENERIC\_DOT\_SECTION(segment) \_\_GENERIC\_DOT\_SECTION(segment)

182

183#define \_\_\_in\_section(a, b, c) \

184 \_\_attribute\_\_((section("." Z\_STRINGIFY(a) \

185 "." Z\_STRINGIFY(b) \

186 "." Z\_STRINGIFY(c))))

187#define \_\_in\_section(a, b, c) \_\_\_in\_section(a, b, c)

188

189#define \_\_in\_section\_unique(seg) \_\_\_in\_section(seg, \_\_FILE\_\_, \_\_COUNTER\_\_)

190

191#define \_\_in\_section\_unique\_named(seg, name) \

192 \_\_\_in\_section(seg, \_\_FILE\_\_, name)

193

194/\* When using XIP, using '\_\_ramfunc' places a function into RAM instead

195 \* of FLASH. Make sure '\_\_ramfunc' is defined only when

196 \* CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT is defined, so that the compiler can

197 \* report an error if '\_\_ramfunc' is used but the architecture does not

198 \* support it.

199 \*/

200#if !defined(CONFIG\_XIP)

201#define \_\_ramfunc

202#elif defined(CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT)

203#if defined(CONFIG\_ARM)

204#define \_\_ramfunc \_\_attribute\_\_((noinline)) \

205 \_\_attribute\_\_((long\_call, section(".ramfunc")))

206#else

207#define \_\_ramfunc \_\_attribute\_\_((noinline)) \

208 \_\_attribute\_\_((section(".ramfunc")))

209#endif

210#endif /\* !CONFIG\_XIP \*/

211

212#ifndef \_\_fallthrough

213#if \_\_GNUC\_\_ >= 7

214#define \_\_fallthrough \_\_attribute\_\_((fallthrough))

215#else

216#define \_\_fallthrough

217#endif /\* \_\_GNUC\_\_ >= 7 \*/

218#endif

219

220#ifndef \_\_packed

221#define \_\_packed \_\_attribute\_\_((\_\_packed\_\_))

222#endif

223

224#ifndef \_\_aligned

225#define \_\_aligned(x) \_\_attribute\_\_((\_\_aligned\_\_(x)))

226#endif

227

228#define \_\_may\_alias \_\_attribute\_\_((\_\_may\_alias\_\_))

229

230#ifndef \_\_printf\_like

231#ifdef CONFIG\_ENFORCE\_ZEPHYR\_STDINT

232#define \_\_printf\_like(f, a) \_\_attribute\_\_((format (printf, f, a)))

233#else

234/\*

235 \* The Zephyr stdint convention enforces int32\_t = int, int64\_t = long long,

236 \* and intptr\_t = long so that short string format length modifiers can be

237 \* used universally across ILP32 and LP64 architectures. Without that it

238 \* is possible for ILP32 toolchains to have int32\_t = long and intptr\_t = int

239 \* clashing with the Zephyr convention and generating pointless warnings

240 \* as they're still the same size. Inhibit the format argument type

241 \* validation in that case and let the other configs do it.

242 \*/

243#define \_\_printf\_like(f, a)

244#endif

245#endif

246

247#define \_\_used \_\_attribute\_\_((\_\_used\_\_))

248#define \_\_unused \_\_attribute\_\_((\_\_unused\_\_))

249#define \_\_maybe\_unused \_\_attribute\_\_((\_\_unused\_\_))

250

251#ifndef \_\_deprecated

252#define \_\_deprecated \_\_attribute\_\_((deprecated))

253#endif

254

255#ifndef \_\_attribute\_const\_\_

256#define \_\_attribute\_const\_\_ \_\_attribute\_\_((\_\_const\_\_))

257#endif

258

259#ifndef \_\_must\_check

260#define \_\_must\_check \_\_attribute\_\_((warn\_unused\_result))

261#endif

262

263#define ARG\_UNUSED(x) (void)(x)

264

265#define likely(x) (\_\_builtin\_expect((bool)!!(x), true) != 0L)

266#define unlikely(x) (\_\_builtin\_expect((bool)!!(x), false) != 0L)

267#define POPCOUNT(x) \_\_builtin\_popcount(x)

268

269#ifndef \_\_no\_optimization

270#define \_\_no\_optimization \_\_attribute\_\_((optimize("-O0")))

271#endif

272

273#ifndef \_\_weak

274#define \_\_weak \_\_attribute\_\_((\_\_weak\_\_))

275#endif

276

277#ifndef \_\_attribute\_nonnull

278#define \_\_attribute\_nonnull(...) \_\_attribute\_\_((nonnull(\_\_VA\_ARGS\_\_)))

279#endif

280

281/\* Builtins with availability that depend on the compiler version. \*/

282#if \_\_GNUC\_\_ >= 5

283#define HAS\_BUILTIN\_\_\_builtin\_add\_overflow 1

284#define HAS\_BUILTIN\_\_\_builtin\_sub\_overflow 1

285#define HAS\_BUILTIN\_\_\_builtin\_mul\_overflow 1

286#define HAS\_BUILTIN\_\_\_builtin\_div\_overflow 1

287#endif

288#if \_\_GNUC\_\_ >= 4

289#define HAS\_BUILTIN\_\_\_builtin\_clz 1

290#define HAS\_BUILTIN\_\_\_builtin\_clzl 1

291#define HAS\_BUILTIN\_\_\_builtin\_clzll 1

292#define HAS\_BUILTIN\_\_\_builtin\_ctz 1

293#define HAS\_BUILTIN\_\_\_builtin\_ctzl 1

294#define HAS\_BUILTIN\_\_\_builtin\_ctzll 1

295#endif

296

297/\*

298 \* Be \*very\* careful with these. You cannot filter out \_\_DEPRECATED\_MACRO with

299 \* -wno-deprecated, which has implications for -Werror.

300 \*/

301

302/\*

303 \* Expands to nothing and generates a warning. Used like

304 \*

305 \* #define FOO \_\_WARN("Please use BAR instead") ...

306 \*

307 \* The warning points to the location where the macro is expanded.

308 \*/

309#define \_\_WARN(msg) \_\_WARN1(GCC warning msg)

310#define \_\_WARN1(s) \_Pragma(#s)

311

312/\* Generic message \*/

313#ifndef \_\_DEPRECATED\_MACRO

314#define \_\_DEPRECATED\_MACRO \_\_WARN("Macro is deprecated")

315#endif

316

317/\* These macros allow having ARM asm functions callable from thumb \*/

318

319#if defined(\_ASMLANGUAGE)

320

321#if defined(CONFIG\_ARM)

322

323#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

324

325#define FUNC\_CODE() .thumb;

326#define FUNC\_INSTR(a)

327

328#else

329

330#define FUNC\_CODE() .code 32;

331#define FUNC\_INSTR(a)

332

333#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

334

335#else

336

337#define FUNC\_CODE()

338#define FUNC\_INSTR(a)

339

340#endif /\* CONFIG\_ARM \*/

341

342#endif /\* \_ASMLANGUAGE \*/

343

344/\*

345 \* These macros are used to declare assembly language symbols that need

346 \* to be typed properly(func or data) to be visible to the OMF tool.

347 \* So that the build tool could mark them as an entry point to be linked

348 \* correctly. This is an elfism. Use #if 0 for a.out.

349 \*/

350

351#if defined(\_ASMLANGUAGE)

352

353#if defined(CONFIG\_ARM) || defined(CONFIG\_NIOS2) || defined(CONFIG\_RISCV) \

354 || defined(CONFIG\_XTENSA) || defined(CONFIG\_ARM64) \

355 || defined(CONFIG\_MIPS)

356#define GTEXT(sym) .global sym; .type sym, %function

357#define GDATA(sym) .global sym; .type sym, %object

358#define WTEXT(sym) .weak sym; .type sym, %function

359#define WDATA(sym) .weak sym; .type sym, %object

360#elif defined(CONFIG\_ARC)

361/\*

362 \* Need to use assembly macros because ';' is interpreted as the start of

363 \* a single line comment in the ARC assembler.

364 \*/

365

366.macro glbl\_text symbol

367 .globl \symbol

368 .type \symbol, %function

369.endm

370

371.macro glbl\_data symbol

372 .globl \symbol

373 .type \symbol, %object

374.endm

375

376.macro weak\_data symbol

377 .weak \symbol

378 .type \symbol, %object

379.endm

380

381#define GTEXT(sym) glbl\_text sym

382#define GDATA(sym) glbl\_data sym

383#define WDATA(sym) weak\_data sym

384

385#else /\* !CONFIG\_ARM && !CONFIG\_ARC \*/

386#define GTEXT(sym) .globl sym; .type sym, @function

387#define GDATA(sym) .globl sym; .type sym, @object

388#endif

389

390/\*

391 \* These macros specify the section in which a given function or variable

392 \* resides.

393 \*

394 \* - SECTION\_FUNC allows only one function to reside in a sub-section

395 \* - SECTION\_SUBSEC\_FUNC allows multiple functions to reside in a sub-section

396 \* This ensures that garbage collection only discards the section

397 \* if all functions in the sub-section are not referenced.

398 \*/

399

400#if defined(CONFIG\_ARC)

401/\*

402 \* Need to use assembly macros because ';' is interpreted as the start of

403 \* a single line comment in the ARC assembler.

404 \*

405 \* Also, '\‍()' is needed in the .section directive of these macros for

406 \* correct substitution of the 'section' variable.

407 \*/

408

409.macro section\_var section, symbol

410 .section .\section\‍().\symbol

411 \symbol :

412.endm

413

414.macro section\_func section, symbol

415 .section .\section\().\symbol, "ax"

416 FUNC\_CODE()

417 PERFOPT\_ALIGN

418 \symbol :

419 FUNC\_INSTR(\symbol)

420.endm

421

422.macro section\_subsec\_func section, subsection, symbol

423 .section .\section\().\subsection, "ax"

424 PERFOPT\_ALIGN

425 \symbol :

426.endm

427

428#define SECTION\_VAR(sect, sym) section\_var sect, sym

429#define SECTION\_FUNC(sect, sym) section\_func sect, sym

430#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

431 section\_subsec\_func sect, subsec, sym

432#else /\* !CONFIG\_ARC \*/

433

434#define SECTION\_VAR(sect, sym) .section .sect.sym; sym:

435#define SECTION\_FUNC(sect, sym) \

436 .section .sect.sym, "ax"; \

437 FUNC\_CODE() \

438 PERFOPT\_ALIGN; sym : \

439 FUNC\_INSTR(sym)

440#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

441 .section .sect.subsec, "ax"; PERFOPT\_ALIGN; sym :

442

443#endif /\* CONFIG\_ARC \*/

444

445#endif /\* \_ASMLANGUAGE \*/

446

447#if defined(\_ASMLANGUAGE)

448#if defined(CONFIG\_ARM)

449#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

450/\* '.syntax unified' is a gcc-ism used in thumb-2 asm files \*/

451#define \_ASM\_FILE\_PROLOGUE .text; .syntax unified; .thumb

452#else

453#define \_ASM\_FILE\_PROLOGUE .text; .code 32

454#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

455#elif defined(CONFIG\_ARM64)

456#define \_ASM\_FILE\_PROLOGUE .text

457#endif /\* CONFIG\_ARM64 || CONFIG\_ARM \*/

458#endif /\* \_ASMLANGUAGE \*/

459

460/\*

461 \* These macros generate absolute symbols for GCC

462 \*/

463

464/\* create an extern reference to the absolute symbol \*/

465

466#define GEN\_OFFSET\_EXTERN(name) extern const char name[]

467

468#define GEN\_ABS\_SYM\_BEGIN(name) \

469 EXTERN\_C void name(void); \

470 void name(void) \

471 {

472

473#define GEN\_ABS\_SYM\_END }

474

475/\*

476 \* Note that GEN\_ABSOLUTE\_SYM(), depending on the architecture

477 \* and toolchain, may restrict the range of values permitted

478 \* for assignment to the named symbol.

479 \*

480 \* For example, on x86, "value" is interpreted as signed

481 \* 32-bit integer. Passing in an unsigned 32-bit integer

482 \* with MSB set would result in a negative integer.

483 \* Moreover, GCC would error out if an integer larger

484 \* than 2^32-1 is passed as "value".

485 \*/

486

487/\*

488 \* GEN\_ABSOLUTE\_SYM\_KCONFIG() is outputted by the build system

489 \* to generate named symbol/value pairs for kconfigs.

490 \*/

491

492#if defined(CONFIG\_ARM)

493

494/\*

495 \* GNU/ARM backend does not have a proper operand modifier which does not

496 \* produces prefix # followed by value, such as %0 for PowerPC, Intel, and

497 \* MIPS. The workaround performed here is using %B0 which converts

498 \* the value to ~(value). Thus "n"(~(value)) is set in operand constraint

499 \* to output (value) in the ARM specific GEN\_OFFSET macro.

500 \*/

501

502#define GEN\_ABSOLUTE\_SYM(name, value) \

503 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

504 ",%B0" \

505 "\n\t.type\t" #name ",%%object" : : "n"(~(value)))

506

507#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

508 \_\_asm\_\_(".globl\t" #name \

509 "\n\t.equ\t" #name "," #value \

510 "\n\t.type\t" #name ",%object")

511

512#elif defined(CONFIG\_X86)

513

514#define GEN\_ABSOLUTE\_SYM(name, value) \

515 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

516 ",%c0" \

517 "\n\t.type\t" #name ",@object" : : "n"(value))

518

519#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

520 \_\_asm\_\_(".globl\t" #name \

521 "\n\t.equ\t" #name "," #value \

522 "\n\t.type\t" #name ",@object")

523

524#elif defined(CONFIG\_ARC) || defined(CONFIG\_ARM64)

525

526#define GEN\_ABSOLUTE\_SYM(name, value) \

527 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

528 ",%c0" \

529 "\n\t.type\t" #name ",@object" : : "n"(value))

530

531#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

532 \_\_asm\_\_(".globl\t" #name \

533 "\n\t.equ\t" #name "," #value \

534 "\n\t.type\t" #name ",@object")

535

536#elif defined(CONFIG\_NIOS2) || defined(CONFIG\_RISCV) || \

537 defined(CONFIG\_XTENSA) || defined(CONFIG\_MIPS)

538

539/\* No special prefixes necessary for constants in this arch AFAICT \*/

540#define GEN\_ABSOLUTE\_SYM(name, value) \

541 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

542 ",%0" \

543 "\n\t.type\t" #name ",%%object" : : "n"(value))

544

545#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

546 \_\_asm\_\_(".globl\t" #name \

547 "\n\t.equ\t" #name "," #value \

548 "\n\t.type\t" #name ",%object")

549

550#elif defined(CONFIG\_ARCH\_POSIX)

551#define GEN\_ABSOLUTE\_SYM(name, value) \

552 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

553 ",%c0" \

554 "\n\t.type\t" #name ",@object" : : "n"(value))

555

556#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

557 \_\_asm\_\_(".globl\t" #name \

558 "\n\t.equ\t" #name "," #value \

559 "\n\t.type\t" #name ",@object")

560

561#elif defined(CONFIG\_SPARC)

562#define GEN\_ABSOLUTE\_SYM(name, value) \

563 \_\_asm\_\_(".global\t" #name "\n\t.equ\t" #name \

564 ",%0" \

565 "\n\t.type\t" #name ",#object" : : "n"(value))

566

567#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

568 \_\_asm\_\_(".globl\t" #name \

569 "\n\t.equ\t" #name "," #value \

570 "\n\t.type\t" #name ",#object")

571

572#else

573#error processor architecture not supported

574#endif

575

576#define compiler\_barrier() do { \

577 \_\_asm\_\_ \_\_volatile\_\_ ("" ::: "memory"); \

578} while (false)

579

589#define Z\_MAX(a, b) ({ \

590 /\* random suffix to avoid naming conflict \*/ \

591 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

592 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

593 \_value\_a\_ > \_value\_b\_ ? \_value\_a\_ : \_value\_b\_; \

594 })

595

601#define Z\_MIN(a, b) ({ \

602 /\* random suffix to avoid naming conflict \*/ \

603 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

604 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

605 \_value\_a\_ < \_value\_b\_ ? \_value\_a\_ : \_value\_b\_; \

606 })

607

613#define Z\_CLAMP(val, low, high) ({ \

614 /\* random suffix to avoid naming conflict \*/ \

615 \_\_typeof\_\_(val) \_value\_val\_ = (val); \

616 \_\_typeof\_\_(low) \_value\_low\_ = (low); \

617 \_\_typeof\_\_(high) \_value\_high\_ = (high); \

618 (\_value\_val\_ < \_value\_low\_) ? \_value\_low\_ : \

619 (\_value\_val\_ > \_value\_high\_) ? \_value\_high\_ : \

620 \_value\_val\_; \

621 })

622

629#define Z\_POW2\_CEIL(x) \

630 ((x) <= 2UL ? (x) : (1UL << (8 \* sizeof(long) - \_\_builtin\_clzl((x) - 1))))

631

638#define Z\_IS\_POW2(x) (((x) != 0) && (((x) & ((x)-1)) == 0))

639

640#if defined(CONFIG\_ASAN) && defined(\_\_clang\_\_)

641#define \_\_noasan \_\_attribute\_\_((no\_sanitize("address")))

642#else

643#define \_\_noasan /\*\*/

644#endif

645

651#if (TOOLCHAIN\_GCC\_VERSION >= 110000) || \

652 (defined(TOOLCHAIN\_CLANG\_VERSION) && (TOOLCHAIN\_CLANG\_VERSION >= 70000))

653#define FUNC\_NO\_STACK\_PROTECTOR \_\_attribute\_\_((no\_stack\_protector))

654#else

655#define FUNC\_NO\_STACK\_PROTECTOR

656#endif

657

658#define TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN \

659 \_Pragma("GCC diagnostic push") \

660 \_Pragma("GCC diagnostic ignored \"-Wshadow\"")

661

662#define TOOLCHAIN\_IGNORE\_WSHADOW\_END \

663 \_Pragma("GCC diagnostic pop")

664

665#endif /\* !\_LINKER \*/

666#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_GCC\_H\_ \*/

[common.h](common_8h.md)

Common toolchain abstraction.

[posix\_trace.h](posix__trace_8h.md)

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [gcc.h](gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
