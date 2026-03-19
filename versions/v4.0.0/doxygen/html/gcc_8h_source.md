---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gcc_8h_source.html
original_path: doxygen/html/gcc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

141#if (\_\_GNUC\_\_ >= 7) && (defined(CONFIG\_ARM) || defined(CONFIG\_ARM64))

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

253/\* When adding this, remember to follow the instructions in

254 \* https://docs.zephyrproject.org/latest/develop/api/api\_lifecycle.html#deprecated

255 \*/

256#endif

257

258#ifndef \_\_attribute\_const\_\_

259#define \_\_attribute\_const\_\_ \_\_attribute\_\_((\_\_const\_\_))

260#endif

261

262#ifndef \_\_must\_check

263#define \_\_must\_check \_\_attribute\_\_((warn\_unused\_result))

264#endif

265

266#define ARG\_UNUSED(x) (void)(x)

267

268#define likely(x) (\_\_builtin\_expect((bool)!!(x), true) != 0L)

269#define unlikely(x) (\_\_builtin\_expect((bool)!!(x), false) != 0L)

270#define POPCOUNT(x) \_\_builtin\_popcount(x)

271

272#ifndef \_\_no\_optimization

273#define \_\_no\_optimization \_\_attribute\_\_((optimize("-O0")))

274#endif

275

276#ifndef \_\_weak

277#define \_\_weak \_\_attribute\_\_((\_\_weak\_\_))

278#endif

279

280#ifndef \_\_attribute\_nonnull

281#define \_\_attribute\_nonnull(...) \_\_attribute\_\_((nonnull(\_\_VA\_ARGS\_\_)))

282#endif

283

284/\* Builtins with availability that depend on the compiler version. \*/

285#if \_\_GNUC\_\_ >= 5

286#define HAS\_BUILTIN\_\_\_builtin\_add\_overflow 1

287#define HAS\_BUILTIN\_\_\_builtin\_sub\_overflow 1

288#define HAS\_BUILTIN\_\_\_builtin\_mul\_overflow 1

289#define HAS\_BUILTIN\_\_\_builtin\_div\_overflow 1

290#endif

291#if \_\_GNUC\_\_ >= 4

292#define HAS\_BUILTIN\_\_\_builtin\_clz 1

293#define HAS\_BUILTIN\_\_\_builtin\_clzl 1

294#define HAS\_BUILTIN\_\_\_builtin\_clzll 1

295#define HAS\_BUILTIN\_\_\_builtin\_ctz 1

296#define HAS\_BUILTIN\_\_\_builtin\_ctzl 1

297#define HAS\_BUILTIN\_\_\_builtin\_ctzll 1

298#endif

299

300/\*

301 \* Be \*very\* careful with these. You cannot filter out \_\_DEPRECATED\_MACRO with

302 \* -wno-deprecated, which has implications for -Werror.

303 \*/

304

305/\*

306 \* Expands to nothing and generates a warning. Used like

307 \*

308 \* #define FOO \_\_WARN("Please use BAR instead") ...

309 \*

310 \* The warning points to the location where the macro is expanded.

311 \*/

312#define \_\_WARN(msg) \_\_WARN1(GCC warning msg)

313#define \_\_WARN1(s) \_Pragma(#s)

314

315/\* Generic message \*/

316#ifndef \_\_DEPRECATED\_MACRO

317#define \_\_DEPRECATED\_MACRO \_\_WARN("Macro is deprecated")

318/\* When adding this, remember to follow the instructions in

319 \* https://docs.zephyrproject.org/latest/develop/api/api\_lifecycle.html#deprecated

320 \*/

321#endif

322

323/\* These macros allow having ARM asm functions callable from thumb \*/

324

325#if defined(\_ASMLANGUAGE)

326

327#if defined(CONFIG\_ARM)

328

329#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

330

331#define FUNC\_CODE() .thumb;

332#define FUNC\_INSTR(a)

333

334#else

335

336#define FUNC\_CODE() .code 32;

337#define FUNC\_INSTR(a)

338

339#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

340

341#else

342

343#define FUNC\_CODE()

344#define FUNC\_INSTR(a)

345

346#endif /\* CONFIG\_ARM \*/

347

348#endif /\* \_ASMLANGUAGE \*/

349

350/\*

351 \* These macros are used to declare assembly language symbols that need

352 \* to be typed properly(func or data) to be visible to the OMF tool.

353 \* So that the build tool could mark them as an entry point to be linked

354 \* correctly. This is an elfism. Use #if 0 for a.out.

355 \*/

356

357#if defined(\_ASMLANGUAGE)

358

359#if defined(CONFIG\_ARM) || defined(CONFIG\_NIOS2) || defined(CONFIG\_RISCV) \

360 || defined(CONFIG\_XTENSA) || defined(CONFIG\_ARM64) \

361 || defined(CONFIG\_MIPS)

362#define GTEXT(sym) .global sym; .type sym, %function

363#define GDATA(sym) .global sym; .type sym, %object

364#define WTEXT(sym) .weak sym; .type sym, %function

365#define WDATA(sym) .weak sym; .type sym, %object

366#elif defined(CONFIG\_ARC)

367/\*

368 \* Need to use assembly macros because ';' is interpreted as the start of

369 \* a single line comment in the ARC assembler.

370 \*/

371

372.macro glbl\_text symbol

373 .globl \symbol

374 .type \symbol, %function

375.endm

376

377.macro glbl\_data symbol

378 .globl \symbol

379 .type \symbol, %object

380.endm

381

382.macro weak\_data symbol

383 .weak \symbol

384 .type \symbol, %object

385.endm

386

387#define GTEXT(sym) glbl\_text sym

388#define GDATA(sym) glbl\_data sym

389#define WDATA(sym) weak\_data sym

390

391#else /\* !CONFIG\_ARM && !CONFIG\_ARC \*/

392#define GTEXT(sym) .globl sym; .type sym, @function

393#define GDATA(sym) .globl sym; .type sym, @object

394#endif

395

396/\*

397 \* These macros specify the section in which a given function or variable

398 \* resides.

399 \*

400 \* - SECTION\_FUNC allows only one function to reside in a sub-section

401 \* - SECTION\_SUBSEC\_FUNC allows multiple functions to reside in a sub-section

402 \* This ensures that garbage collection only discards the section

403 \* if all functions in the sub-section are not referenced.

404 \*/

405

406#if defined(CONFIG\_ARC)

407/\*

408 \* Need to use assembly macros because ';' is interpreted as the start of

409 \* a single line comment in the ARC assembler.

410 \*

411 \* Also, '\‍()' is needed in the .section directive of these macros for

412 \* correct substitution of the 'section' variable.

413 \*/

414

415.macro section\_var section, symbol

416 .section .\section\‍().\symbol

417 \symbol :

418.endm

419

420.macro section\_func section, symbol

421 .section .\section\().\symbol, "ax"

422 FUNC\_CODE()

423 PERFOPT\_ALIGN

424 \symbol :

425 FUNC\_INSTR(\symbol)

426.endm

427

428.macro section\_subsec\_func section, subsection, symbol

429 .section .\section\().\subsection, "ax"

430 PERFOPT\_ALIGN

431 \symbol :

432.endm

433

434#define SECTION\_VAR(sect, sym) section\_var sect, sym

435#define SECTION\_FUNC(sect, sym) section\_func sect, sym

436#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

437 section\_subsec\_func sect, subsec, sym

438#else /\* !CONFIG\_ARC \*/

439

440#define SECTION\_VAR(sect, sym) .section .sect.sym; sym:

441#define SECTION\_FUNC(sect, sym) \

442 .section .sect.sym, "ax"; \

443 FUNC\_CODE() \

444 PERFOPT\_ALIGN; sym : \

445 FUNC\_INSTR(sym)

446#define SECTION\_SUBSEC\_FUNC(sect, subsec, sym) \

447 .section .sect.subsec, "ax"; PERFOPT\_ALIGN; sym :

448

449#endif /\* CONFIG\_ARC \*/

450

451#endif /\* \_ASMLANGUAGE \*/

452

453#if defined(\_ASMLANGUAGE)

454#if defined(CONFIG\_ARM)

455#if defined(CONFIG\_ASSEMBLER\_ISA\_THUMB2)

456/\* '.syntax unified' is a gcc-ism used in thumb-2 asm files \*/

457#define \_ASM\_FILE\_PROLOGUE .text; .syntax unified; .thumb

458#else

459#define \_ASM\_FILE\_PROLOGUE .text; .code 32

460#endif /\* CONFIG\_ASSEMBLER\_ISA\_THUMB2 \*/

461#elif defined(CONFIG\_ARM64)

462#define \_ASM\_FILE\_PROLOGUE .text

463#endif /\* CONFIG\_ARM64 || CONFIG\_ARM \*/

464#endif /\* \_ASMLANGUAGE \*/

465

466/\*

467 \* These macros generate absolute symbols for GCC

468 \*/

469

470/\* create an extern reference to the absolute symbol \*/

471

472#define GEN\_OFFSET\_EXTERN(name) extern const char name[]

473

474#define GEN\_ABS\_SYM\_BEGIN(name) \

475 EXTERN\_C void name(void); \

476 void name(void) \

477 {

478

479#define GEN\_ABS\_SYM\_END }

480

481/\*

482 \* Note that GEN\_ABSOLUTE\_SYM(), depending on the architecture

483 \* and toolchain, may restrict the range of values permitted

484 \* for assignment to the named symbol.

485 \*

486 \* For example, on x86, "value" is interpreted as signed

487 \* 32-bit integer. Passing in an unsigned 32-bit integer

488 \* with MSB set would result in a negative integer.

489 \* Moreover, GCC would error out if an integer larger

490 \* than 2^32-1 is passed as "value".

491 \*/

492

493/\*

494 \* GEN\_ABSOLUTE\_SYM\_KCONFIG() is outputted by the build system

495 \* to generate named symbol/value pairs for kconfigs.

496 \*/

497

498#if defined(CONFIG\_ARM)

499

500/\*

501 \* GNU/ARM backend does not have a proper operand modifier which does not

502 \* produces prefix # followed by value, such as %0 for PowerPC, Intel, and

503 \* MIPS. The workaround performed here is using %B0 which converts

504 \* the value to ~(value). Thus "n"(~(value)) is set in operand constraint

505 \* to output (value) in the ARM specific GEN\_OFFSET macro.

506 \*/

507

508#define GEN\_ABSOLUTE\_SYM(name, value) \

509 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

510 ",%B0" \

511 "\n\t.type\t" #name ",%%object" : : "n"(~(value)))

512

513#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

514 \_\_asm\_\_(".globl\t" #name \

515 "\n\t.equ\t" #name "," #value \

516 "\n\t.type\t" #name ",%object")

517

518#elif defined(CONFIG\_X86)

519

520#define GEN\_ABSOLUTE\_SYM(name, value) \

521 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

522 ",%c0" \

523 "\n\t.type\t" #name ",@object" : : "n"(value))

524

525#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

526 \_\_asm\_\_(".globl\t" #name \

527 "\n\t.equ\t" #name "," #value \

528 "\n\t.type\t" #name ",@object")

529

530#elif defined(CONFIG\_ARC) || defined(CONFIG\_ARM64)

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

542#elif defined(CONFIG\_NIOS2) || defined(CONFIG\_RISCV) || \

543 defined(CONFIG\_XTENSA) || defined(CONFIG\_MIPS)

544

545/\* No special prefixes necessary for constants in this arch AFAICT \*/

546#define GEN\_ABSOLUTE\_SYM(name, value) \

547 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

548 ",%0" \

549 "\n\t.type\t" #name ",%%object" : : "n"(value))

550

551#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

552 \_\_asm\_\_(".globl\t" #name \

553 "\n\t.equ\t" #name "," #value \

554 "\n\t.type\t" #name ",%object")

555

556#elif defined(CONFIG\_ARCH\_POSIX)

557#define GEN\_ABSOLUTE\_SYM(name, value) \

558 \_\_asm\_\_(".globl\t" #name "\n\t.equ\t" #name \

559 ",%c0" \

560 "\n\t.type\t" #name ",@object" : : "n"(value))

561

562#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

563 \_\_asm\_\_(".globl\t" #name \

564 "\n\t.equ\t" #name "," #value \

565 "\n\t.type\t" #name ",@object")

566

567#elif defined(CONFIG\_SPARC)

568#define GEN\_ABSOLUTE\_SYM(name, value) \

569 \_\_asm\_\_(".global\t" #name "\n\t.equ\t" #name \

570 ",%0" \

571 "\n\t.type\t" #name ",#object" : : "n"(value))

572

573#define GEN\_ABSOLUTE\_SYM\_KCONFIG(name, value) \

574 \_\_asm\_\_(".globl\t" #name \

575 "\n\t.equ\t" #name "," #value \

576 "\n\t.type\t" #name ",#object")

577

578#else

579#error processor architecture not supported

580#endif

581

582#define compiler\_barrier() do { \

583 \_\_asm\_\_ \_\_volatile\_\_ ("" ::: "memory"); \

584} while (false)

585

595#define Z\_MAX(a, b) ({ \

596 /\* random suffix to avoid naming conflict \*/ \

597 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

598 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

599 (\_value\_a\_ > \_value\_b\_) ? \_value\_a\_ : \_value\_b\_; \

600 })

601

607#define Z\_MIN(a, b) ({ \

608 /\* random suffix to avoid naming conflict \*/ \

609 \_\_typeof\_\_(a) \_value\_a\_ = (a); \

610 \_\_typeof\_\_(b) \_value\_b\_ = (b); \

611 (\_value\_a\_ < \_value\_b\_) ? \_value\_a\_ : \_value\_b\_; \

612 })

613

619#define Z\_CLAMP(val, low, high) ({ \

620 /\* random suffix to avoid naming conflict \*/ \

621 \_\_typeof\_\_(val) \_value\_val\_ = (val); \

622 \_\_typeof\_\_(low) \_value\_low\_ = (low); \

623 \_\_typeof\_\_(high) \_value\_high\_ = (high); \

624 (\_value\_val\_ < \_value\_low\_) ? \_value\_low\_ : \

625 (\_value\_val\_ > \_value\_high\_) ? \_value\_high\_ : \

626 \_value\_val\_; \

627 })

628

635#define Z\_POW2\_CEIL(x) \

636 ((x) <= 2UL ? (x) : (1UL << (8 \* sizeof(long) - \_\_builtin\_clzl((x) - 1))))

637

644#define Z\_IS\_POW2(x) (((x) != 0) && (((x) & ((x)-1)) == 0))

645

646#if defined(CONFIG\_ASAN) && defined(\_\_clang\_\_)

647#define \_\_noasan \_\_attribute\_\_((no\_sanitize("address")))

648#else

649#define \_\_noasan /\*\*/

650#endif

651

652#if defined(CONFIG\_UBSAN)

653#define \_\_noubsan \_\_attribute\_\_((no\_sanitize("undefined")))

654#else

655#define \_\_noubsan

656#endif

657

663#if (TOOLCHAIN\_GCC\_VERSION >= 110000) || \

664 (defined(TOOLCHAIN\_CLANG\_VERSION) && (TOOLCHAIN\_CLANG\_VERSION >= 70000))

665#define FUNC\_NO\_STACK\_PROTECTOR \_\_attribute\_\_((no\_stack\_protector))

666#else

667#define FUNC\_NO\_STACK\_PROTECTOR

668#endif

669

670#define TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN \

671 \_Pragma("GCC diagnostic push") \

672 \_Pragma("GCC diagnostic ignored \"-Wshadow\"")

673

674#define TOOLCHAIN\_IGNORE\_WSHADOW\_END \

675 \_Pragma("GCC diagnostic pop")

676

677#endif /\* !\_LINKER \*/

678#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_GCC\_H\_ \*/

[common.h](include_2zephyr_2toolchain_2common_8h.md)

Common toolchain abstraction.

[posix\_trace.h](posix__trace_8h.md)

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [gcc.h](gcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
