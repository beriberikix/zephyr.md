---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2toolchain_2gcc_8h_source.html
original_path: doxygen/html/include_2zephyr_2toolchain_2gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gcc.h

[Go to the documentation of this file.](include_2zephyr_2toolchain_2gcc_8h.md)

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

[ 21](include_2zephyr_2toolchain_2gcc_8h.md#acbf8a21b471b2086cbe276789c5061d5)#define TOOLCHAIN\_GCC\_VERSION \

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

[ 37](include_2zephyr_2toolchain_2gcc_8h.md#a90e5fd6ed234d1494c7f156635c2e6e1)#define TOOLCHAIN\_HAS\_ZLA 1

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

85 (((\_\_GNUC\_\_ > 4) || ((\_\_GNUC\_\_ == 4) && (\_\_GNUC\_MINOR\_\_ >= 6))) || \

86 (\_\_STDC\_VERSION\_\_) >= 201100)

87#define BUILD\_ASSERT(EXPR, MSG...) \_Static\_assert((EXPR), "" MSG)

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

98#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h.md)>

99#include <[stdbool.h](stdbool_8h.md)>

100

101#define ALIAS\_OF(of) \_\_attribute\_\_((alias(#of)))

102

103#define FUNC\_ALIAS(real\_func, new\_alias, return\_type) \

104 return\_type new\_alias() ALIAS\_OF(real\_func)

105

106#if TOOLCHAIN\_GCC\_VERSION < 40500

107#define \_\_builtin\_unreachable() \_\_builtin\_trap()

108#endif

109

110#if defined(CONFIG\_ARCH\_POSIX) && !defined(\_ASMLANGUAGE)

111#include <[zephyr/arch/posix/posix\_trace.h](posix__trace_8h.md)>

112

113/\*let's not segfault if this were to happen for some reason\*/

114#define CODE\_UNREACHABLE \

115{\

116 posix\_print\_error\_and\_exit("CODE\_UNREACHABLE reached from %s:%d\n",\

117 \_\_FILE\_\_, \_\_LINE\_\_);\

118 \_\_builtin\_unreachable(); \

119}

120#else

121#define CODE\_UNREACHABLE \_\_builtin\_unreachable()

122#endif

123#define FUNC\_NORETURN \_\_attribute\_\_((\_\_noreturn\_\_))

124

125/\* The GNU assembler for Cortex-M3 uses # for immediate values, not

126 \* comments, so the @nobits# trick does not work.

127 \*/

128#if defined(CONFIG\_ARM) || defined(CONFIG\_ARM64)

129#define \_NODATA\_SECTION(segment) \_\_attribute\_\_((section(#segment)))

130#else

131#define \_NODATA\_SECTION(segment) \

132 \_\_attribute\_\_((section(#segment ",\"wa\",@nobits#")))

133#endif

134

135/\* Unaligned access \*/

136#define UNALIGNED\_GET(g) \

137\_\_extension\_\_ ({ \

138 struct \_\_attribute\_\_((\_\_packed\_\_)) { \

139 \_\_typeof\_\_(\*(g)) \_\_v; \

140 } \*\_\_g = (\_\_typeof\_\_(\_\_g)) (g); \

141 \_\_g->\_\_v; \

142})

143

144

145#if (\_\_GNUC\_\_ >= 7) && (defined(CONFIG\_ARM) || defined(CONFIG\_ARM64))

146

147/\* Version of UNALIGNED\_PUT() which issues a compiler\_barrier() after

148 \* the store. It is required to workaround an apparent optimization

149 \* bug in GCC for ARM Cortex-M3 and higher targets, when multiple

150 \* byte, half-word and word stores (strb, strh, str instructions),

151 \* which support unaligned access, can be coalesced into store double

152 \* (strd) instruction, which doesn't support unaligned access (the

153 \* compilers in question do this optimization ignoring \_\_packed\_\_

154 \* attribute).

155 \*/

156#define UNALIGNED\_PUT(v, p) \

157do { \

158 struct \_\_attribute\_\_((\_\_packed\_\_)) { \

159 \_\_typeof\_\_(\*p) \_\_v; \

160 } \*\_\_p = (\_\_typeof\_\_(\_\_p)) (p); \

161 \_\_p->\_\_v = (v); \

162 compiler\_barrier(); \

163} while (false)

164

165#else

166

167#define UNALIGNED\_PUT(v, p) \

168do { \

169 struct \_\_attribute\_\_((\_\_packed\_\_)) { \

170 \_\_typeof\_\_(\*p) \_\_v; \

171 } \*\_\_p = (\_\_typeof\_\_(\_\_p)) (p); \

172 \_\_p->\_\_v = (v); \

173} while (false)

174

175#endif

176

177/\*

178 \* Get the address of a structure member even if the member may not be properly

179 \* aligned. Note that accessing such an address must be done with care (for

180 \* example with UNALIGNED\_GET/PUT) and cannot be in general de-referenced to

181 \* access the member directly, as that would cause a fault in architectures

182 \* which have alignment requirements.

183 \*/

184#define UNALIGNED\_MEMBER\_ADDR(\_p, \_member) ((\_\_typeof\_\_(\_p->\_member) \*) \

185 (((intptr\_t)(\_p)) + offsetof(\_\_typeof\_\_(\*\_p), \_member)))

186

187/\* Double indirection to ensure section names are expanded before

188 \* stringification

189 \*/

190#define \_\_GENERIC\_SECTION(segment) \_\_attribute\_\_((section(STRINGIFY(segment))))

191#define Z\_GENERIC\_SECTION(segment) \_\_GENERIC\_SECTION(segment)

192

193#define \_\_GENERIC\_DOT\_SECTION(segment) \

194 \_\_attribute\_\_((section("." STRINGIFY(segment))))

195#define Z\_GENERIC\_DOT\_SECTION(segment) \_\_GENERIC\_DOT\_SECTION(segment)

196

197#define \_\_\_in\_section(a, b, c) \

198 \_\_attribute\_\_((section("." Z\_STRINGIFY(a) \

199 "." Z\_STRINGIFY(b) \

200 "." Z\_STRINGIFY(c))))

201#define \_\_in\_section(a, b, c) \_\_\_in\_section(a, b, c)

202

203#ifndef \_\_in\_section\_unique

204#define \_\_in\_section\_unique(seg) \_\_\_in\_section(seg, \_\_FILE\_\_, \_\_COUNTER\_\_)

205#endif

206

207#ifndef \_\_in\_section\_unique\_named

208#define \_\_in\_section\_unique\_named(seg, name) \

209 \_\_\_in\_section(seg, \_\_FILE\_\_, name)

210#endif

211

212/\* When using XIP, using '\_\_ramfunc' places a function into RAM instead

213 \* of FLASH. Make sure '\_\_ramfunc' is defined only when

214 \* CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT is defined, so that the compiler can

215 \* report an error if '\_\_ramfunc' is used but the architecture does not

216 \* support it.

217 \*/

218#if !defined(CONFIG\_XIP)

219#define \_\_ramfunc

220#elif defined(CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT)

221#if defined(CONFIG\_ARM)

222#if defined(\_\_clang\_\_)

223/\* No long\_call attribute for Clang.

224 \* Rely on linker to place required veneers.

225 \* https://github.com/llvm/llvm-project/issues/39969

226 \*/

227#define \_\_ramfunc \_\_attribute\_\_((noinline)) \_\_attribute\_\_((section(".ramfunc")))

228#else

229/\* GCC version \*/

230#define \_\_ramfunc \_\_attribute\_\_((noinline)) \

231 \_\_attribute\_\_((long\_call, section(".ramfunc")))

232#endif

233#else

234#define \_\_ramfunc \_\_attribute\_\_((noinline)) \

235 \_\_attribute\_\_((section(".ramfunc")))

236#endif

237#endif /\* !CONFIG\_XIP \*/

238

239#ifndef \_\_fallthrough

240#if \_\_GNUC\_\_ >= 7

241#define \_\_fallthrough \_\_attribute\_\_((fallthrough))

242#else

243#define \_\_fallthrough

244#endif /\* \_\_GNUC\_\_ >= 7 \*/

245#endif

246

247#ifndef \_\_packed

248#define \_\_packed \_\_attribute\_\_((\_\_packed\_\_))

249#endif

250

251#ifndef \_\_aligned

252#define \_\_aligned(x) \_\_attribute\_\_((\_\_aligned\_\_(x)))

253#endif

254

255#ifndef \_\_noinline

256#define \_\_noinline \_\_attribute\_\_((noinline))

257#endif

258

259#define \_\_may\_alias \_\_attribute\_\_((\_\_may\_alias\_\_))

260

261#ifndef \_\_printf\_like

262#ifdef CONFIG\_ENFORCE\_ZEPHYR\_STDINT

263#define \_\_printf\_like(f, a) \_\_attribute\_\_((format (printf, f, a)))

264#else

265/\*

266 \* The Zephyr stdint convention enforces int32\_t = int, int64\_t = long long,

267 \* and intptr\_t = long so that short string format length modifiers can be

268 \* used universally across ILP32 and LP64 architectures. Without that it

269 \* is possible for ILP32 toolchains to have int32\_t = long and intptr\_t = int

270 \* clashing with the Zephyr convention and generating pointless warnings

271 \* as they're still the same size. Inhibit the format argument type

272 \* validation in that case and let the other configs do it.

273 \*/

274#define \_\_printf\_like(f, a)

275#endif

276#endif

277

278#define \_\_used \_\_attribute\_\_((\_\_used\_\_))

279#define \_\_unused \_\_attribute\_\_((\_\_unused\_\_))

280#define \_\_maybe\_unused \_\_attribute\_\_((\_\_unused\_\_))

281

282#ifndef \_\_deprecated

283#define \_\_deprecated \_\_attribute\_\_((deprecated))

284/\* When adding this, remember to follow the instructions in

285 \* https://docs.zephyrproject.org/latest/develop/api/api\_lifecycle.html#deprecated

286 \*/

287#endif

288

289#ifndef \_\_attribute\_const\_\_

290#define \_\_attribute\_const\_\_ \_\_attribute\_\_((\_\_const\_\_))

291#endif

292

293#ifndef \_\_must\_check

294#define \_\_must\_check \_\_attribute\_\_((warn\_unused\_result))

295#endif

296

297#define ARG\_UNUSED(x) (void)(x)

298

299#define likely(x) (\_\_builtin\_expect((bool)!!(x), true) != 0L)

300#define unlikely(x) (\_\_builtin\_expect((bool)!!(x), false) != 0L)

301#define POPCOUNT(x) \_\_builtin\_popcount(x)

302

303#ifndef \_\_no\_optimization

304#define \_\_no\_optimization \_\_attribute\_\_((optimize("-O0")))

305#endif

306

307#ifndef \_\_weak

308#define \_\_weak \_\_attribute\_\_((\_\_weak\_\_))

309#endif

310

311#ifndef \_\_attribute\_nonnull

312#define \_\_attribute\_nonnull(...) \_\_attribute\_\_((nonnull(\_\_VA\_ARGS\_\_)))

313#endif

314

315/\* Builtins with availability that depend on the compiler version. \*/

316#if \_\_GNUC\_\_ >= 5

317#define HAS\_BUILTIN\_\_\_builtin\_add\_overflow 1

318#define HAS\_BUILTIN\_\_\_builtin\_sub\_overflow 1

319#define HAS\_BUILTIN\_\_\_builtin\_mul\_overflow 1

320#define HAS\_BUILTIN\_\_\_builtin\_div\_overflow 1

321#endif

322#if \_\_GNUC\_\_ >= 4

323#define HAS\_BUILTIN\_\_\_builtin\_clz 1

324#define HAS\_BUILTIN\_\_\_builtin\_clzl 1

325#define HAS\_BUILTIN\_\_\_builtin\_clzll 1

326#define HAS\_BUILTIN\_\_\_builtin\_ctz 1

327#define HAS\_BUILTIN\_\_\_builtin\_ctzl 1

328#define HAS\_BUILTIN\_\_\_builtin\_ctzll 1

329#endif

330

331/\*

332 \* Be \*very\* careful with these. You cannot filter out \_\_DEPRECATED\_MACRO with

333 \* -wno-deprecated, which has implications for -Werror.

334 \*/

335

336/\*

337 \* Expands to nothing and generates a warning. Used like

338 \*

339 \* #define FOO \_\_WARN("Please use BAR instead") ...

340 \*

341 \* The warning points to the location where the macro is expanded.

342 \*/

343#define \_\_WARN(msg) \_\_WARN1(GCC warning msg)

344#define \_\_WARN1(s) \_Pragma(#s)

345

346/\* Generic message \*/

347#ifndef CONFIG\_DEPRECATION\_TEST

348#define \_\_DEPRECATED\_MACRO \_\_WARN("Macro is deprecated")

349/\* When adding this, remember to follow the instructions in

350 \* https://docs.zephyrproject.org/latest/develop/api/api\_lifecycle.html#deprecated

351 \*/

352#else

353#define \_\_DEPRECATED\_MACRO

354#endif

355

356/\* These macros allow having ARM asm functions callable from thumb \*/

357

358#if defined(\_ASMLANGUAGE)

359

360#if defined(CONFIG\_ARM)

361

362#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

363

364#define FUNC\_CODE() .thumb;

365#define FUNC\_INSTR(a)

366

367#else

368

369#define FUNC\_CODE() .code 32;

370#define FUNC\_INSTR(a)

371

372#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

373

374#else

375

376#define FUNC\_CODE()

377#define FUNC\_INSTR(a)

378

379#endif /\* CONFIG\_ARM \*/

380

381#endif /\* \_ASMLANGUAGE \*/

382

383/\*

384 \* These macros are used to declare assembly language symbols that need

385 \* to be typed properly(func or data) to be visible to the OMF tool.

386 \* So that the build tool could mark them as an entry point to be linked

387 \* correctly. This is an elfism. Use #if 0 for a.out.

388 \*/

389

390#if defined(\_ASMLANGUAGE)

391

392#if defined(CONFIG\_ARM) || defined(CONFIG\_RISCV) \

393 || defined(CONFIG\_XTENSA) || defined(CONFIG\_ARM64) \

394 || defined(CONFIG\_MIPS) || defined(CONFIG\_RX)

395#define GTEXT(sym) .global sym; .type sym, %function

396#define GDATA(sym) .global sym; .type sym, %object

397#define WTEXT(sym) .weak sym; .type sym, %function

398#define WDATA(sym) .weak sym; .type sym, %object

399#elif defined(CONFIG\_ARC)

400/\*

401 \* Need to use assembly macros because ';' is interpreted as the start of

402 \* a single line comment in the ARC assembler.

403 \*/

404

405.macro glbl\_text symbol

406 .globl \symbol

407 .type \symbol, %function

408.endm

409

410.macro glbl\_data symbol

411 .globl \symbol

412 .type \symbol, %object

413.endm

414

415.macro weak\_data symbol

416 .weak \symbol

417 .type \symbol, %object

418.endm

419

420#define GTEXT(sym) glbl\_text sym

421#define GDATA(sym) glbl\_data sym

422#define WDATA(sym) weak\_data sym

423

424#else /\* !CONFIG\_ARM && !CONFIG\_ARC \*/

425#define GTEXT(sym) .globl sym; .type sym, @function

426#define GDATA(sym) .globl sym; .type sym, @object

427#endif

428

429/\*

430 \* These macros specify the section in which a given function or variable

431 \* resides.

432 \*

433 \* - SECTION\_FUNC allows only one function to reside in a sub-section

434 \* - SECTION\_SUBSEC\_FUNC allows multiple functions to reside in a sub-section

435 \* This ensures that garbage collection only discards the section

436 \* if all functions in the sub-section are not referenced.

437 \*/

438

439#if defined(CONFIG\_ARC)

440/\*

441 \* Need to use assembly macros because ';' is interpreted as the start of

442 \* a single line comment in the ARC assembler.

443 \*

444 \* Also, '\‍()' is needed in the .section directive of these macros for

445 \* correct substitution of the 'section' variable.

446 \*/

447

448.macro section\_var section, symbol

449 .section .\section\‍().\symbol

450 \symbol :

451.endm

452

453.macro section\_func section, symbol

454 .section .\section\().\symbol, "ax"

455 FUNC\_CODE()

456 PERFOPT\_ALIGN

457 \symbol :

458 FUNC\_INSTR(\symbol)

459.endm

460

461.macro section\_subsec\_func section, subsection, symbol

462 .section .\section\().\subsection, "ax"

463 PERFOPT\_ALIGN

464 \symbol :

465.endm

466

467#define SECTION\_VAR(sect, sym) section\_var sect, sym

468#define SECTION\_FUNC(sect, sym) section\_func sect, sym

469#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

470 section\_subsec\_func sect, subsec, sym

471#else /\* !CONFIG\_ARC \*/

472

473#define SECTION\_VAR(sect, sym) .section .sect.sym; sym:

474#define SECTION\_FUNC(sect, sym) \

475 .section .sect.sym, "ax"; \

476 FUNC\_CODE() \

477 PERFOPT\_ALIGN; sym : \

478 FUNC\_INSTR(sym)

479#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

480 .section .sect.subsec, "ax"; PERFOPT\_ALIGN; sym :

481

482#endif /\* CONFIG\_ARC \*/

483

484#endif /\* \_ASMLANGUAGE \*/

485

486#if defined(\_ASMLANGUAGE)

487#if defined(CONFIG\_ARM)

488#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

489/\* '.syntax unified' is a gcc-ism used in thumb-2 asm files \*/

490#define \_ASM\_FILE\_PROLOGUE .text; .syntax unified; .thumb

491#else

492#define \_ASM\_FILE\_PROLOGUE .text; .code 32

493#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

494#elif defined(CONFIG\_ARM64)

495#define \_ASM\_FILE\_PROLOGUE .text

496#endif /\* CONFIG\_ARM64 || CONFIG\_ARM \*/

497#endif /\* \_ASMLANGUAGE \*/

498

499/\*

500 \* These macros generate absolute symbols for GCC

501 \*/

502

503/\* create an extern reference to the absolute symbol \*/

504

505#define GEN\_OFFSET\_EXTERN(name) extern const char name[]

506

507#define GEN\_ABS\_SYM\_BEGIN(name) \

508 EXTERN\_C void name(void); \

509 void name(void) \

510 {

511

512#define GEN\_ABS\_SYM\_END }

513

514/\*

515 \* Note that GEN\_ABSOLUTE\_SYM(), depending on the architecture

516 \* and toolchain, may restrict the range of values permitted

517 \* for assignment to the named symbol.

518 \*

519 \* For example, on x86, "value" is interpreted as signed

520 \* 32-bit integer. Passing in an unsigned 32-bit integer

521 \* with MSB set would result in a negative integer.

522 \* Moreover, GCC would error out if an integer larger

523 \* than 2^32-1 is passed as "value".

524 \*/

525

526/\*

527 \* GEN\_ABSOLUTE\_SYM\_KCONFIG() is outputted by the build system

528 \* to generate named symbol/value pairs for kconfigs.

529 \*/

530

531#if defined(CONFIG\_ARM)

532

533/\*

534 \* GNU/ARM backend does not have a proper operand modifier which does not

535 \* produces prefix # followed by value, such as %0 for PowerPC, Intel, and

536 \* MIPS. The workaround performed here is using %B0 which converts

537 \* the value to ~(value). Thus "n"(~(value)) is set in operand constraint

538 \* to output (value) in the ARM specific GEN\_OFFSET macro.

539 \*/

540

541#define GEN\_ABSOLUTE\_SYM(name, value) \

542 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

543 ",%B0" \

544 "\n\t.type\t" #name ",%%object" : : "n"(~(value)))

545

546#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

547 \_\_asm\_\_(".globl\t" #name \

548 "\n\t.equ\t" #name "," #value \

549 "\n\t.type\t" #name ",%object")

550

551#elif defined(CONFIG\_X86)

552

553#define GEN\_ABSOLUTE\_SYM(name, value) \

554 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

555 ",%c0" \

556 "\n\t.type\t" #name ",@object" : : "n"(value))

557

558#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

559 \_\_asm\_\_(".globl\t" #name \

560 "\n\t.equ\t" #name "," #value \

561 "\n\t.type\t" #name ",@object")

562

563#elif defined(CONFIG\_ARC) || defined(CONFIG\_ARM64)

564

565#define GEN\_ABSOLUTE\_SYM(name, value) \

566 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

567 ",%c0" \

568 "\n\t.type\t" #name ",@object" : : "n"(value))

569

570#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

571 \_\_asm\_\_(".globl\t" #name \

572 "\n\t.equ\t" #name "," #value \

573 "\n\t.type\t" #name ",@object")

574

575#elif defined(CONFIG\_RISCV) || defined(CONFIG\_XTENSA) || defined(CONFIG\_MIPS)

576

577/\* No special prefixes necessary for constants in this arch AFAICT \*/

578#define GEN\_ABSOLUTE\_SYM(name, value) \

579 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

580 ",%0" \

581 "\n\t.type\t" #name ",%%object" : : "n"(value))

582

583#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

584 \_\_asm\_\_(".globl\t" #name \

585 "\n\t.equ\t" #name "," #value \

586 "\n\t.type\t" #name ",%object")

587

588#elif defined(CONFIG\_ARCH\_POSIX)

589#define GEN\_ABSOLUTE\_SYM(name, value) \

590 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

591 ",%c0" \

592 "\n\t.type\t" #name ",@object" : : "n"(value))

593

594#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

595 \_\_asm\_\_(".globl\t" #name \

596 "\n\t.equ\t" #name "," #value \

597 "\n\t.type\t" #name ",@object")

598

599#elif defined(CONFIG\_SPARC)

600#define GEN\_ABSOLUTE\_SYM(name, value) \

601 \_\_asm\_\_(".global\t" #name "\n\t.equ\t" #name \

602 ",%0" \

603 "\n\t.type\t" #name ",#object" : : "n"(value))

604

605#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

606 \_\_asm\_\_(".globl\t" #name \

607 "\n\t.equ\t" #name "," #value \

608 "\n\t.type\t" #name ",#object")

609

610#elif defined(CONFIG\_RX)

611#define GEN\_ABSOLUTE\_SYM(name, value) \

612 \_\_asm\_\_(".global\t" #name "\n\t.equ\t" #name \

613 ",%c0" \

614 "\n\t.type\t" #name ",%%object" : : "n"(value))

615

616#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

617 \_\_asm\_\_(".global\t" #name \

618 "\n\t.equ\t" #name "," #value \

619 "\n\t.type\t" #name ",#object")

620

621#else

622#error processor architecture not supported

623#endif

624

625#define compiler\_barrier() do { \

626 \_\_asm\_\_ \_\_volatile\_\_ ("" ::: "memory"); \

627} while (false)

628

638#define Z\_MAX(a, b) ({ \

639 /\* random suffix to avoid naming conflict \*/ \

640 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

641 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

642 (\_value\_a\_ > \_value\_b\_) ? \_value\_a\_ : \_value\_b\_; \

643 })

644

650#define Z\_MIN(a, b) ({ \

651 /\* random suffix to avoid naming conflict \*/ \

652 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

653 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

654 (\_value\_a\_ < \_value\_b\_) ? \_value\_a\_ : \_value\_b\_; \

655 })

656

662#define Z\_CLAMP(val, low, high) ({ \

663 /\* random suffix to avoid naming conflict \*/ \

664 \_\_typeof\_\_(val) \_value\_val\_ = (val); \

665 \_\_typeof\_\_(low) \_value\_low\_ = (low); \

666 \_\_typeof\_\_(high) \_value\_high\_ = (high); \

667 (\_value\_val\_ < \_value\_low\_) ? \_value\_low\_ : \

668 (\_value\_val\_ > \_value\_high\_) ? \_value\_high\_ : \

669 \_value\_val\_; \

670 })

671

678#define Z\_POW2\_CEIL(x) \

679 ((x) <= 2UL ? (x) : (1UL << (8 \* sizeof(long) - \_\_builtin\_clzl((x) - 1))))

680

687#define Z\_IS\_POW2(x) (((x) != 0) && (((x) & ((x)-1)) == 0))

688

689#if defined(CONFIG\_ASAN) && defined(\_\_clang\_\_)

690#define \_\_noasan \_\_attribute\_\_((no\_sanitize("address")))

691#else

692#define \_\_noasan /\*\*/

693#endif

694

695#if defined(CONFIG\_UBSAN)

696#define \_\_noubsan \_\_attribute\_\_((no\_sanitize("undefined")))

697#else

698#define \_\_noubsan

699#endif

700

706#if (TOOLCHAIN\_GCC\_VERSION >= 110000) || \

707 (defined(TOOLCHAIN\_CLANG\_VERSION) && (TOOLCHAIN\_CLANG\_VERSION >= 70000))

708#define FUNC\_NO\_STACK\_PROTECTOR \_\_attribute\_\_((no\_stack\_protector))

709#else

710#define FUNC\_NO\_STACK\_PROTECTOR

711#endif

712

713#endif /\* !\_LINKER \*/

714

[ 715](include_2zephyr_2toolchain_2gcc_8h.md#aef9c3722dc2b189226eb2e6223c080bf)#define TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER "-Waddress-of-packed-member"

[ 716](include_2zephyr_2toolchain_2gcc_8h.md#a8b81dbfdc3dde900a58540709a4f1dff)#define TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS "-Warray-bounds"

[ 717](include_2zephyr_2toolchain_2gcc_8h.md#a5f5fef9bda4762c368f26c9028cdd34a)#define TOOLCHAIN\_WARNING\_ATTRIBUTES "-Wattributes"

[ 718](include_2zephyr_2toolchain_2gcc_8h.md#a003b55bfd0a8b95a4e57e419eb980a39)#define TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR "-Wdelete-non-virtual-dtor"

[ 719](include_2zephyr_2toolchain_2gcc_8h.md#a64d8f26c21ee3639e82d93783e09387e)#define TOOLCHAIN\_WARNING\_EXTRA "-Wextra"

[ 720](include_2zephyr_2toolchain_2gcc_8h.md#af990df9b277505b97d4c9c2549fffa9f)#define TOOLCHAIN\_WARNING\_NONNULL "-Wnonnull"

[ 721](include_2zephyr_2toolchain_2gcc_8h.md#ae917ae1adad468956fa5d28a50d10670)#define TOOLCHAIN\_WARNING\_SHADOW "-Wshadow"

[ 722](include_2zephyr_2toolchain_2gcc_8h.md#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9)#define TOOLCHAIN\_WARNING\_UNUSED\_LABEL "-Wunused-label"

[ 723](include_2zephyr_2toolchain_2gcc_8h.md#ac567335f987f8f89640e22bd8e3e9385)#define TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE "-Wunused-variable"

724

725/\* GCC-specific warnings that aren't in clang. \*/

726#if defined(\_\_GNUC\_\_) && !defined(\_\_clang\_\_)

727#define TOOLCHAIN\_WARNING\_POINTER\_ARITH "-Wpointer-arith"

728#define TOOLCHAIN\_WARNING\_STRINGOP\_OVERREAD "-Wstringop-overread"

729#endif

730

731#define \_TOOLCHAIN\_DISABLE\_WARNING(compiler, warning) \

732 TOOLCHAIN\_PRAGMA(compiler diagnostic push) \

733 TOOLCHAIN\_PRAGMA(compiler diagnostic ignored warning)

734

735#define \_TOOLCHAIN\_ENABLE\_WARNING(compiler, warning) TOOLCHAIN\_PRAGMA(compiler diagnostic pop)

736

[ 737](include_2zephyr_2toolchain_2gcc_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5)#define TOOLCHAIN\_DISABLE\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(GCC, warning)

[ 738](include_2zephyr_2toolchain_2gcc_8h.md#a5365fdbb6323f48ddca9ab4149e9a561)#define TOOLCHAIN\_ENABLE\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(GCC, warning)

739

740#if defined(\_\_GNUC\_\_) && !defined(\_\_clang\_\_)

741#define TOOLCHAIN\_DISABLE\_GCC\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(GCC, warning)

742#define TOOLCHAIN\_ENABLE\_GCC\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(GCC, warning)

743#endif

744

745#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_GCC\_H\_ \*/

[common.h](include_2zephyr_2toolchain_2common_8h.md)

Common toolchain abstraction.

[posix\_trace.h](posix__trace_8h.md)

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [gcc.h](include_2zephyr_2toolchain_2gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
