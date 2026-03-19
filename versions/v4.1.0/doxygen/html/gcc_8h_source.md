---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gcc_8h_source.html
original_path: doxygen/html/gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

177/\* Double indirection to ensure section names are expanded before

178 \* stringification

179 \*/

180#define \_\_GENERIC\_SECTION(segment) \_\_attribute\_\_((section(STRINGIFY(segment))))

181#define Z\_GENERIC\_SECTION(segment) \_\_GENERIC\_SECTION(segment)

182

183#define \_\_GENERIC\_DOT\_SECTION(segment) \

184 \_\_attribute\_\_((section("." STRINGIFY(segment))))

185#define Z\_GENERIC\_DOT\_SECTION(segment) \_\_GENERIC\_DOT\_SECTION(segment)

186

187#define \_\_\_in\_section(a, b, c) \

188 \_\_attribute\_\_((section("." Z\_STRINGIFY(a) \

189 "." Z\_STRINGIFY(b) \

190 "." Z\_STRINGIFY(c))))

191#define \_\_in\_section(a, b, c) \_\_\_in\_section(a, b, c)

192

193#ifndef \_\_in\_section\_unique

194#define \_\_in\_section\_unique(seg) \_\_\_in\_section(seg, \_\_FILE\_\_, \_\_COUNTER\_\_)

195#endif

196

197#ifndef \_\_in\_section\_unique\_named

198#define \_\_in\_section\_unique\_named(seg, name) \

199 \_\_\_in\_section(seg, \_\_FILE\_\_, name)

200#endif

201

202/\* When using XIP, using '\_\_ramfunc' places a function into RAM instead

203 \* of FLASH. Make sure '\_\_ramfunc' is defined only when

204 \* CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT is defined, so that the compiler can

205 \* report an error if '\_\_ramfunc' is used but the architecture does not

206 \* support it.

207 \*/

208#if !defined(CONFIG\_XIP)

209#define \_\_ramfunc

210#elif defined(CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT)

211#if defined(CONFIG\_ARM)

212#define \_\_ramfunc \_\_attribute\_\_((noinline)) \

213 \_\_attribute\_\_((long\_call, section(".ramfunc")))

214#else

215#define \_\_ramfunc \_\_attribute\_\_((noinline)) \

216 \_\_attribute\_\_((section(".ramfunc")))

217#endif

218#endif /\* !CONFIG\_XIP \*/

219

220#ifndef \_\_fallthrough

221#if \_\_GNUC\_\_ >= 7

222#define \_\_fallthrough \_\_attribute\_\_((fallthrough))

223#else

224#define \_\_fallthrough

225#endif /\* \_\_GNUC\_\_ >= 7 \*/

226#endif

227

228#ifndef \_\_packed

229#define \_\_packed \_\_attribute\_\_((\_\_packed\_\_))

230#endif

231

232#ifndef \_\_aligned

233#define \_\_aligned(x) \_\_attribute\_\_((\_\_aligned\_\_(x)))

234#endif

235

236#ifndef \_\_noinline

237#define \_\_noinline \_\_attribute\_\_((noinline))

238#endif

239

240#define \_\_may\_alias \_\_attribute\_\_((\_\_may\_alias\_\_))

241

242#ifndef \_\_printf\_like

243#ifdef CONFIG\_ENFORCE\_ZEPHYR\_STDINT

244#define \_\_printf\_like(f, a) \_\_attribute\_\_((format (printf, f, a)))

245#else

246/\*

247 \* The Zephyr stdint convention enforces int32\_t = int, int64\_t = long long,

248 \* and intptr\_t = long so that short string format length modifiers can be

249 \* used universally across ILP32 and LP64 architectures. Without that it

250 \* is possible for ILP32 toolchains to have int32\_t = long and intptr\_t = int

251 \* clashing with the Zephyr convention and generating pointless warnings

252 \* as they're still the same size. Inhibit the format argument type

253 \* validation in that case and let the other configs do it.

254 \*/

255#define \_\_printf\_like(f, a)

256#endif

257#endif

258

259#define \_\_used \_\_attribute\_\_((\_\_used\_\_))

260#define \_\_unused \_\_attribute\_\_((\_\_unused\_\_))

261#define \_\_maybe\_unused \_\_attribute\_\_((\_\_unused\_\_))

262

263#ifndef \_\_deprecated

264#define \_\_deprecated \_\_attribute\_\_((deprecated))

265/\* When adding this, remember to follow the instructions in

266 \* https://docs.zephyrproject.org/latest/develop/api/api\_lifecycle.html#deprecated

267 \*/

268#endif

269

270#ifndef \_\_attribute\_const\_\_

271#define \_\_attribute\_const\_\_ \_\_attribute\_\_((\_\_const\_\_))

272#endif

273

274#ifndef \_\_must\_check

275#define \_\_must\_check \_\_attribute\_\_((warn\_unused\_result))

276#endif

277

278#define ARG\_UNUSED(x) (void)(x)

279

280#define likely(x) (\_\_builtin\_expect((bool)!!(x), true) != 0L)

281#define unlikely(x) (\_\_builtin\_expect((bool)!!(x), false) != 0L)

282#define POPCOUNT(x) \_\_builtin\_popcount(x)

283

284#ifndef \_\_no\_optimization

285#define \_\_no\_optimization \_\_attribute\_\_((optimize("-O0")))

286#endif

287

288#ifndef \_\_weak

289#define \_\_weak \_\_attribute\_\_((\_\_weak\_\_))

290#endif

291

292#ifndef \_\_attribute\_nonnull

293#define \_\_attribute\_nonnull(...) \_\_attribute\_\_((nonnull(\_\_VA\_ARGS\_\_)))

294#endif

295

296/\* Builtins with availability that depend on the compiler version. \*/

297#if \_\_GNUC\_\_ >= 5

298#define HAS\_BUILTIN\_\_\_builtin\_add\_overflow 1

299#define HAS\_BUILTIN\_\_\_builtin\_sub\_overflow 1

300#define HAS\_BUILTIN\_\_\_builtin\_mul\_overflow 1

301#define HAS\_BUILTIN\_\_\_builtin\_div\_overflow 1

302#endif

303#if \_\_GNUC\_\_ >= 4

304#define HAS\_BUILTIN\_\_\_builtin\_clz 1

305#define HAS\_BUILTIN\_\_\_builtin\_clzl 1

306#define HAS\_BUILTIN\_\_\_builtin\_clzll 1

307#define HAS\_BUILTIN\_\_\_builtin\_ctz 1

308#define HAS\_BUILTIN\_\_\_builtin\_ctzl 1

309#define HAS\_BUILTIN\_\_\_builtin\_ctzll 1

310#endif

311

312/\*

313 \* Be \*very\* careful with these. You cannot filter out \_\_DEPRECATED\_MACRO with

314 \* -wno-deprecated, which has implications for -Werror.

315 \*/

316

317/\*

318 \* Expands to nothing and generates a warning. Used like

319 \*

320 \* #define FOO \_\_WARN("Please use BAR instead") ...

321 \*

322 \* The warning points to the location where the macro is expanded.

323 \*/

324#define \_\_WARN(msg) \_\_WARN1(GCC warning msg)

325#define \_\_WARN1(s) \_Pragma(#s)

326

327/\* Generic message \*/

328#ifndef \_\_DEPRECATED\_MACRO

329#define \_\_DEPRECATED\_MACRO \_\_WARN("Macro is deprecated")

330/\* When adding this, remember to follow the instructions in

331 \* https://docs.zephyrproject.org/latest/develop/api/api\_lifecycle.html#deprecated

332 \*/

333#endif

334

335/\* These macros allow having ARM asm functions callable from thumb \*/

336

337#if defined(\_ASMLANGUAGE)

338

339#if defined(CONFIG\_ARM)

340

341#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

342

343#define FUNC\_CODE() .thumb;

344#define FUNC\_INSTR(a)

345

346#else

347

348#define FUNC\_CODE() .code 32;

349#define FUNC\_INSTR(a)

350

351#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

352

353#else

354

355#define FUNC\_CODE()

356#define FUNC\_INSTR(a)

357

358#endif /\* CONFIG\_ARM \*/

359

360#endif /\* \_ASMLANGUAGE \*/

361

362/\*

363 \* These macros are used to declare assembly language symbols that need

364 \* to be typed properly(func or data) to be visible to the OMF tool.

365 \* So that the build tool could mark them as an entry point to be linked

366 \* correctly. This is an elfism. Use #if 0 for a.out.

367 \*/

368

369#if defined(\_ASMLANGUAGE)

370

371#if defined(CONFIG\_ARM) || defined(CONFIG\_NIOS2) || defined(CONFIG\_RISCV) \

372 || defined(CONFIG\_XTENSA) || defined(CONFIG\_ARM64) \

373 || defined(CONFIG\_MIPS)

374#define GTEXT(sym) .global sym; .type sym, %function

375#define GDATA(sym) .global sym; .type sym, %object

376#define WTEXT(sym) .weak sym; .type sym, %function

377#define WDATA(sym) .weak sym; .type sym, %object

378#elif defined(CONFIG\_ARC)

379/\*

380 \* Need to use assembly macros because ';' is interpreted as the start of

381 \* a single line comment in the ARC assembler.

382 \*/

383

384.macro glbl\_text symbol

385 .globl \symbol

386 .type \symbol, %function

387.endm

388

389.macro glbl\_data symbol

390 .globl \symbol

391 .type \symbol, %object

392.endm

393

394.macro weak\_data symbol

395 .weak \symbol

396 .type \symbol, %object

397.endm

398

399#define GTEXT(sym) glbl\_text sym

400#define GDATA(sym) glbl\_data sym

401#define WDATA(sym) weak\_data sym

402

403#else /\* !CONFIG\_ARM && !CONFIG\_ARC \*/

404#define GTEXT(sym) .globl sym; .type sym, @function

405#define GDATA(sym) .globl sym; .type sym, @object

406#endif

407

408/\*

409 \* These macros specify the section in which a given function or variable

410 \* resides.

411 \*

412 \* - SECTION\_FUNC allows only one function to reside in a sub-section

413 \* - SECTION\_SUBSEC\_FUNC allows multiple functions to reside in a sub-section

414 \* This ensures that garbage collection only discards the section

415 \* if all functions in the sub-section are not referenced.

416 \*/

417

418#if defined(CONFIG\_ARC)

419/\*

420 \* Need to use assembly macros because ';' is interpreted as the start of

421 \* a single line comment in the ARC assembler.

422 \*

423 \* Also, '\‍()' is needed in the .section directive of these macros for

424 \* correct substitution of the 'section' variable.

425 \*/

426

427.macro section\_var section, symbol

428 .section .\section\‍().\symbol

429 \symbol :

430.endm

431

432.macro section\_func section, symbol

433 .section .\section\().\symbol, "ax"

434 FUNC\_CODE()

435 PERFOPT\_ALIGN

436 \symbol :

437 FUNC\_INSTR(\symbol)

438.endm

439

440.macro section\_subsec\_func section, subsection, symbol

441 .section .\section\().\subsection, "ax"

442 PERFOPT\_ALIGN

443 \symbol :

444.endm

445

446#define SECTION\_VAR(sect, sym) section\_var sect, sym

447#define SECTION\_FUNC(sect, sym) section\_func sect, sym

448#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

449 section\_subsec\_func sect, subsec, sym

450#else /\* !CONFIG\_ARC \*/

451

452#define SECTION\_VAR(sect, sym) .section .sect.sym; sym:

453#define SECTION\_FUNC(sect, sym) \

454 .section .sect.sym, "ax"; \

455 FUNC\_CODE() \

456 PERFOPT\_ALIGN; sym : \

457 FUNC\_INSTR(sym)

458#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

459 .section .sect.subsec, "ax"; PERFOPT\_ALIGN; sym :

460

461#endif /\* CONFIG\_ARC \*/

462

463#endif /\* \_ASMLANGUAGE \*/

464

465#if defined(\_ASMLANGUAGE)

466#if defined(CONFIG\_ARM)

467#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

468/\* '.syntax unified' is a gcc-ism used in thumb-2 asm files \*/

469#define \_ASM\_FILE\_PROLOGUE .text; .syntax unified; .thumb

470#else

471#define \_ASM\_FILE\_PROLOGUE .text; .code 32

472#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

473#elif defined(CONFIG\_ARM64)

474#define \_ASM\_FILE\_PROLOGUE .text

475#endif /\* CONFIG\_ARM64 || CONFIG\_ARM \*/

476#endif /\* \_ASMLANGUAGE \*/

477

478/\*

479 \* These macros generate absolute symbols for GCC

480 \*/

481

482/\* create an extern reference to the absolute symbol \*/

483

484#define GEN\_OFFSET\_EXTERN(name) extern const char name[]

485

486#define GEN\_ABS\_SYM\_BEGIN(name) \

487 EXTERN\_C void name(void); \

488 void name(void) \

489 {

490

491#define GEN\_ABS\_SYM\_END }

492

493/\*

494 \* Note that GEN\_ABSOLUTE\_SYM(), depending on the architecture

495 \* and toolchain, may restrict the range of values permitted

496 \* for assignment to the named symbol.

497 \*

498 \* For example, on x86, "value" is interpreted as signed

499 \* 32-bit integer. Passing in an unsigned 32-bit integer

500 \* with MSB set would result in a negative integer.

501 \* Moreover, GCC would error out if an integer larger

502 \* than 2^32-1 is passed as "value".

503 \*/

504

505/\*

506 \* GEN\_ABSOLUTE\_SYM\_KCONFIG() is outputted by the build system

507 \* to generate named symbol/value pairs for kconfigs.

508 \*/

509

510#if defined(CONFIG\_ARM)

511

512/\*

513 \* GNU/ARM backend does not have a proper operand modifier which does not

514 \* produces prefix # followed by value, such as %0 for PowerPC, Intel, and

515 \* MIPS. The workaround performed here is using %B0 which converts

516 \* the value to ~(value). Thus "n"(~(value)) is set in operand constraint

517 \* to output (value) in the ARM specific GEN\_OFFSET macro.

518 \*/

519

520#define GEN\_ABSOLUTE\_SYM(name, value) \

521 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

522 ",%B0" \

523 "\n\t.type\t" #name ",%%object" : : "n"(~(value)))

524

525#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

526 \_\_asm\_\_(".globl\t" #name \

527 "\n\t.equ\t" #name "," #value \

528 "\n\t.type\t" #name ",%object")

529

530#elif defined(CONFIG\_X86)

531

532#define GEN\_ABSOLUTE\_SYM(name, value) \

533 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

534 ",%c0" \

535 "\n\t.type\t" #name ",@object" : : "n"(value))

536

537#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

538 \_\_asm\_\_(".globl\t" #name \

539 "\n\t.equ\t" #name "," #value \

540 "\n\t.type\t" #name ",@object")

541

542#elif defined(CONFIG\_ARC) || defined(CONFIG\_ARM64)

543

544#define GEN\_ABSOLUTE\_SYM(name, value) \

545 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

546 ",%c0" \

547 "\n\t.type\t" #name ",@object" : : "n"(value))

548

549#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

550 \_\_asm\_\_(".globl\t" #name \

551 "\n\t.equ\t" #name "," #value \

552 "\n\t.type\t" #name ",@object")

553

554#elif defined(CONFIG\_NIOS2) || defined(CONFIG\_RISCV) || \

555 defined(CONFIG\_XTENSA) || defined(CONFIG\_MIPS)

556

557/\* No special prefixes necessary for constants in this arch AFAICT \*/

558#define GEN\_ABSOLUTE\_SYM(name, value) \

559 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

560 ",%0" \

561 "\n\t.type\t" #name ",%%object" : : "n"(value))

562

563#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

564 \_\_asm\_\_(".globl\t" #name \

565 "\n\t.equ\t" #name "," #value \

566 "\n\t.type\t" #name ",%object")

567

568#elif defined(CONFIG\_ARCH\_POSIX)

569#define GEN\_ABSOLUTE\_SYM(name, value) \

570 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

571 ",%c0" \

572 "\n\t.type\t" #name ",@object" : : "n"(value))

573

574#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

575 \_\_asm\_\_(".globl\t" #name \

576 "\n\t.equ\t" #name "," #value \

577 "\n\t.type\t" #name ",@object")

578

579#elif defined(CONFIG\_SPARC)

580#define GEN\_ABSOLUTE\_SYM(name, value) \

581 \_\_asm\_\_(".global\t" #name "\n\t.equ\t" #name \

582 ",%0" \

583 "\n\t.type\t" #name ",#object" : : "n"(value))

584

585#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

586 \_\_asm\_\_(".globl\t" #name \

587 "\n\t.equ\t" #name "," #value \

588 "\n\t.type\t" #name ",#object")

589

590#else

591#error processor architecture not supported

592#endif

593

594#define compiler\_barrier() do { \

595 \_\_asm\_\_ \_\_volatile\_\_ ("" ::: "memory"); \

596} while (false)

597

607#define Z\_MAX(a, b) ({ \

608 /\* random suffix to avoid naming conflict \*/ \

609 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

610 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

611 (\_value\_a\_ > \_value\_b\_) ? \_value\_a\_ : \_value\_b\_; \

612 })

613

619#define Z\_MIN(a, b) ({ \

620 /\* random suffix to avoid naming conflict \*/ \

621 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

622 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

623 (\_value\_a\_ < \_value\_b\_) ? \_value\_a\_ : \_value\_b\_; \

624 })

625

631#define Z\_CLAMP(val, low, high) ({ \

632 /\* random suffix to avoid naming conflict \*/ \

633 \_\_typeof\_\_(val) \_value\_val\_ = (val); \

634 \_\_typeof\_\_(low) \_value\_low\_ = (low); \

635 \_\_typeof\_\_(high) \_value\_high\_ = (high); \

636 (\_value\_val\_ < \_value\_low\_) ? \_value\_low\_ : \

637 (\_value\_val\_ > \_value\_high\_) ? \_value\_high\_ : \

638 \_value\_val\_; \

639 })

640

647#define Z\_POW2\_CEIL(x) \

648 ((x) <= 2UL ? (x) : (1UL << (8 \* sizeof(long) - \_\_builtin\_clzl((x) - 1))))

649

656#define Z\_IS\_POW2(x) (((x) != 0) && (((x) & ((x)-1)) == 0))

657

658#if defined(CONFIG\_ASAN) && defined(\_\_clang\_\_)

659#define \_\_noasan \_\_attribute\_\_((no\_sanitize("address")))

660#else

661#define \_\_noasan /\*\*/

662#endif

663

664#if defined(CONFIG\_UBSAN)

665#define \_\_noubsan \_\_attribute\_\_((no\_sanitize("undefined")))

666#else

667#define \_\_noubsan

668#endif

669

675#if (TOOLCHAIN\_GCC\_VERSION >= 110000) || \

676 (defined(TOOLCHAIN\_CLANG\_VERSION) && (TOOLCHAIN\_CLANG\_VERSION >= 70000))

677#define FUNC\_NO\_STACK\_PROTECTOR \_\_attribute\_\_((no\_stack\_protector))

678#else

679#define FUNC\_NO\_STACK\_PROTECTOR

680#endif

681

682#define TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN \

683 \_Pragma("GCC diagnostic push") \

684 \_Pragma("GCC diagnostic ignored \"-Wshadow\"")

685

686#define TOOLCHAIN\_IGNORE\_WSHADOW\_END \

687 \_Pragma("GCC diagnostic pop")

688

689#endif /\* !\_LINKER \*/

690

691#define \_TOOLCHAIN\_DISABLE\_WARNING(compiler, warning) \

692 TOOLCHAIN\_PRAGMA(compiler diagnostic push) \

693 TOOLCHAIN\_PRAGMA(compiler diagnostic ignored warning)

694

695#define \_TOOLCHAIN\_ENABLE\_WARNING(compiler, warning) TOOLCHAIN\_PRAGMA(compiler diagnostic pop)

696

[ 697](gcc_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5)#define TOOLCHAIN\_DISABLE\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(GCC, warning)

[ 698](gcc_8h.md#a5365fdbb6323f48ddca9ab4149e9a561)#define TOOLCHAIN\_ENABLE\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(GCC, warning)

699

700#if defined(\_\_GNUC\_\_) && !defined(\_\_clang\_\_)

701#define TOOLCHAIN\_DISABLE\_GCC\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(GCC, warning)

702#define TOOLCHAIN\_ENABLE\_GCC\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(GCC, warning)

703#endif

704

705#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_GCC\_H\_ \*/

[common.h](include_2zephyr_2toolchain_2common_8h.md)

Common toolchain abstraction.

[posix\_trace.h](posix__trace_8h.md)

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [gcc.h](gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
