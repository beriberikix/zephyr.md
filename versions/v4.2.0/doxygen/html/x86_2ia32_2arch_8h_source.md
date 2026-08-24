---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/x86_2ia32_2arch_8h_source.html
original_path: doxygen/html/x86_2ia32_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](x86_2ia32_2arch_8h.md)

1/\*

2 \* Copyright (c) 2010-2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ARCH\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ARCH\_H\_

17

18#include "[sys\_io.h](arch_2x86_2ia32_2sys__io_8h.md)"

19#include <[stdbool.h](stdbool_8h.md)>

20#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

21#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

22#include <[zephyr/sys/util.h](sys_2util_8h.md)>

23#include <[zephyr/arch/x86/ia32/exception.h](x86_2ia32_2exception_8h.md)>

24#include <[zephyr/arch/x86/ia32/gdbstub.h](arch_2x86_2ia32_2gdbstub_8h.md)>

25#include <[zephyr/arch/x86/ia32/thread.h](arch_2x86_2ia32_2thread_8h.md)>

26#include <[zephyr/arch/x86/ia32/syscall.h](arch_2x86_2ia32_2syscall_8h.md)>

27

28#ifndef \_ASMLANGUAGE

29#include <stddef.h> /\* for size\_t \*/

30

31#include <[zephyr/arch/common/addr\_types.h](addr__types_8h.md)>

32#include <[zephyr/arch/x86/ia32/segmentation.h](segmentation_8h.md)>

33#include <[zephyr/pm/pm.h](pm_8h.md)>

34

35#endif /\* \_ASMLANGUAGE \*/

36

37/\* GDT layout \*/

[ 38](x86_2ia32_2arch_8h.md#a01cd8f711fd0961b75a23e9d4642d7c3)#define CODE\_SEG 0x08

[ 39](x86_2ia32_2arch_8h.md#aee584332ca956b4e1167180bf9a456bb)#define DATA\_SEG 0x10

[ 40](x86_2ia32_2arch_8h.md#a5817f0b628919c0d0b092b2a961187e6)#define MAIN\_TSS 0x18

[ 41](x86_2ia32_2arch_8h.md#a8f9b184e3ebb59e9ec8c62b187b5ad4d)#define DF\_TSS 0x20

42

43/\*

44 \* Use for thread local storage.

45 \* Match these to gen\_gdt.py.

46 \* The 0x03 is added to limit privilege.

47 \*/

48#if defined(CONFIG\_USERSPACE)

[ 49](x86_2ia32_2arch_8h.md#abe9fa73b285cb69f2d541fbfd62923fc)#define GS\_TLS\_SEG (0x38 | 0x03)

50#elif defined(CONFIG\_X86\_STACK\_PROTECTION)

51#define GS\_TLS\_SEG (0x28 | 0x03)

52#else

53#define GS\_TLS\_SEG (0x18 | 0x03)

54#endif

55

[ 60](x86_2ia32_2arch_8h.md#a9de710989afc64c692b4366e89c42e9b)#define MK\_ISR\_NAME(x) \_\_isr\_\_##x

61

62#define Z\_DYN\_STUB\_SIZE 4

63#define Z\_DYN\_STUB\_OFFSET 0

64#define Z\_DYN\_STUB\_LONG\_JMP\_EXTRA\_SIZE 3

65#define Z\_DYN\_STUB\_PER\_BLOCK 32

66

67

68#ifndef \_ASMLANGUAGE

69

70#ifdef \_\_cplusplus

71extern "C" {

72#endif

73

74/\* interrupt/exception/error related definitions \*/

75

[ 76](structs__isrList.md)typedef struct [s\_isrList](structs__isrList.md) {

[ 78](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03) void \*[fnc](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03);

[ 83](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c) unsigned int [irq](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c);

[ 85](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9) unsigned int [priority](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9);

[ 89](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3) unsigned int [vec](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3);

[ 91](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e) unsigned int [dpl](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e);

92

[ 97](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd) unsigned int [tss](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd);

[ 98](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378)} [ISR\_LIST](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378);

99

100

121

[ 122](x86_2ia32_2arch_8h.md#aa4db2c24f5de7f8bae4a0f290fb70456)#define NANO\_CPU\_INT\_REGISTER(r, n, p, v, d) \

123 static ISR\_LIST \_\_attribute\_\_((section(".intList"))) \

124 \_\_attribute\_\_((used)) MK\_ISR\_NAME(r) = \

125 { \

126 .fnc = &(r), \

127 .irq = (n), \

128 .priority = (p), \

129 .vec = (v), \

130 .dpl = (d), \

131 .tss = 0 \

132 }

133

147#define \_X86\_IDT\_TSS\_REGISTER(tss\_p, irq\_p, priority\_p, vec\_p, dpl\_p) \

148 static ISR\_LIST \_\_attribute\_\_((section(".intList"))) \

149 \_\_attribute\_\_((used)) MK\_ISR\_NAME(vec\_p) = \

150 { \

151 .fnc = NULL, \

152 .irq = (irq\_p), \

153 .priority = (priority\_p), \

154 .vec = (vec\_p), \

155 .dpl = (dpl\_p), \

156 .tss = (tss\_p) \

157 }

158

173#define \_VECTOR\_ARG(irq\_p) (-1)

174

175#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

176#define IRQSTUBS\_TEXT\_SECTION ".pinned\_text.irqstubs"

177#else

[ 178](x86_2ia32_2arch_8h.md#a745054d50f7d95a9cfdb394521cb407f)#define IRQSTUBS\_TEXT\_SECTION ".text.irqstubs"

179#endif

180

181/\* Internally this function does a few things:

182 \*

183 \* 1. There is a declaration of the interrupt parameters in the .intList

184 \* section, used by gen\_idt to create the IDT. This does the same thing

185 \* as the NANO\_CPU\_INT\_REGISTER() macro, but is done in assembly as we

186 \* need to populate the .fnc member with the address of the assembly

187 \* IRQ stub that we generate immediately afterwards.

188 \*

189 \* 2. The IRQ stub itself is declared. The code will go in its own named

190 \* section .text.irqstubs section (which eventually gets linked into 'text')

191 \* and the stub shall be named (isr\_name)\_irq(irq\_line)\_stub

192 \*

193 \* 3. The IRQ stub pushes the ISR routine and its argument onto the stack

194 \* and then jumps to the common interrupt handling code in \_interrupt\_enter().

195 \*

196 \* 4. z\_irq\_controller\_irq\_config() is called at runtime to set the mapping

197 \* between the vector and the IRQ line as well as triggering flags

198 \*/

[ 199](x86_2ia32_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

200{ \

201 \_\_asm\_\_ \_\_volatile\_\_( \

202 ".pushsection .intList\n\t" \

203 ".long %c[isr]\_irq%c[irq]\_stub\n\t" /\* ISR\_LIST.fnc \*/ \

204 ".long %c[irq]\n\t" /\* ISR\_LIST.irq \*/ \

205 ".long %c[priority]\n\t" /\* ISR\_LIST.priority \*/ \

206 ".long %c[vector]\n\t" /\* ISR\_LIST.vec \*/ \

207 ".long 0\n\t" /\* ISR\_LIST.dpl \*/ \

208 ".long 0\n\t" /\* ISR\_LIST.tss \*/ \

209 ".popsection\n\t" \

210 ".pushsection " IRQSTUBS\_TEXT\_SECTION "\n\t" \

211 ".global %c[isr]\_irq%c[irq]\_stub\n\t" \

212 "%c[isr]\_irq%c[irq]\_stub:\n\t" \

213 "pushl %[isr\_param]\n\t" \

214 "pushl %[isr]\n\t" \

215 "jmp \_interrupt\_enter\n\t" \

216 ".popsection\n\t" \

217 : \

218 : [isr] "i" (isr\_p), \

219 [isr\_param] "i" (isr\_param\_p), \

220 [priority] "i" (priority\_p), \

221 [vector] "i" \_VECTOR\_ARG(irq\_p), \

222 [irq] "i" (irq\_p)); \

223 z\_irq\_controller\_irq\_config(Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq\_p), (irq\_p), \

224 (flags\_p)); \

225}

226

227#ifdef CONFIG\_PCIE

228

229#define ARCH\_PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, \

230 isr\_p, isr\_param\_p, flags\_p) \

231 ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p)

232

233#endif /\* CONFIG\_PCIE \*/

234

235/\* Direct interrupts won't work as expected with KPTI turned on, because

236 \* all non-user accessible pages in the page table are marked non-present.

237 \* It's likely possible to add logic to ARCH\_ISR\_DIRECT\_HEADER/FOOTER to do

238 \* the necessary trampolining to switch page tables / stacks, but this

239 \* probably loses all the latency benefits that direct interrupts provide

240 \* and one might as well use a regular interrupt anyway.

241 \*/

242#ifndef CONFIG\_X86\_KPTI

[ 243](x86_2ia32_2arch_8h.md#a875f2b1ca924721fe3854796bd96c2db)#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

244{ \

245 NANO\_CPU\_INT\_REGISTER(isr\_p, irq\_p, priority\_p, -1, 0); \

246 z\_irq\_controller\_irq\_config(Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq\_p), (irq\_p), \

247 (flags\_p)); \

248}

249

250#ifdef CONFIG\_PM

251static inline void arch\_irq\_direct\_pm(void)

252{

253 if (\_kernel.idle) {

254 \_kernel.idle = 0;

255 [pm\_system\_resume](group__subsys__pm__sys.md#ga40a040996ab6746aa7714499b41d500e)();

256 }

257}

258

259#define ARCH\_ISR\_DIRECT\_PM() arch\_irq\_direct\_pm()

260#else

[ 261](x86_2ia32_2arch_8h.md#a491cb79acec18c83b9a61b0b45dfab69)#define ARCH\_ISR\_DIRECT\_PM() do { } while (false)

262#endif

263

[ 264](x86_2ia32_2arch_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() arch\_isr\_direct\_header()

[ 265](x86_2ia32_2arch_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)#define ARCH\_ISR\_DIRECT\_FOOTER(swap) arch\_isr\_direct\_footer(swap)

266

267/\* FIXME:

268 \* tracing/tracing.h cannot be included here due to circular dependency

269 \*/

270#if defined(CONFIG\_TRACING)

271void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

272void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

273#endif

274

[ 275](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)static inline void [arch\_isr\_direct\_header](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)(void)

276{

277#if defined(CONFIG\_TRACING)

278 [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)();

279#endif

280

281 /\* We're not going to unlock IRQs, but we still need to increment this

282 \* so that arch\_is\_in\_isr() works

283 \*/

284 ++\_kernel.cpus[0].nested;

285}

286

287/\*

288 \* FIXME: z\_swap\_irqlock is an inline function declared in a private header and

289 \* cannot be referenced from a public header, so we move it to an

290 \* external function.

291 \*/

[ 292](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)void [arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)(unsigned int key);

293

[ 294](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)static inline void [arch\_isr\_direct\_footer](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)(int swap)

295{

296 z\_irq\_controller\_eoi();

297#if defined(CONFIG\_TRACING)

298 [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)();

299#endif

300 --\_kernel.cpus[0].nested;

301

302 /\* Call swap if all the following is true:

303 \*

304 \* 1) swap argument was enabled to this function

305 \* 2) We are not in a nested interrupt

306 \* 3) Next thread to run in the ready queue is not this thread

307 \*/

308 if (swap != 0 && \_kernel.cpus[0].nested == 0 &&

309 \_kernel.ready\_q.cache != \_current) {

310 unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

311

312 /\* Fetch EFLAGS argument to z\_swap() \*/

313 \_\_asm\_\_ volatile (

314 "pushfl\n\t"

315 "popl %0\n\t"

316 : "=g" ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

317 :

318 : "memory"

319 );

320

321 [arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

322 }

323}

324

[ 325](x86_2ia32_2arch_8h.md#a5279598e93dd914614a2ae52557be1a5)#define ARCH\_ISR\_DIRECT\_DECLARE(name) \

326 static inline int name##\_body(void); \

327 \_\_attribute\_\_ ((interrupt)) void name(void \*stack\_frame) \

328 { \

329 ARG\_UNUSED(stack\_frame); \

330 int check\_reschedule; \

331 ISR\_DIRECT\_HEADER(); \

332 check\_reschedule = name##\_body(); \

333 ISR\_DIRECT\_FOOTER(check\_reschedule); \

334 } \

335 static inline int name##\_body(void)

336#endif /\* !CONFIG\_X86\_KPTI \*/

337

[ 338](x86_2ia32_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

339{

340 unsigned int key;

341

342 \_\_asm\_\_ volatile ("pushfl; cli; popl %0" : "=g" (key) :: "memory");

343

344 return key;

345}

346

347

[ 353](x86_2ia32_2arch_8h.md#ae52cccc5fa73fafe5a7fb60accb11e35)#define NANO\_SOFT\_IRQ ((unsigned int) (-1))

354

355#ifdef CONFIG\_X86\_ENABLE\_TSS

356extern struct [task\_state\_segment](structtask__state__segment.md) \_main\_tss;

357#endif

358

[ 359](x86_2ia32_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

360 \_\_asm\_\_ volatile( \

361 "push %[reason]\n\t" \

362 "int %[vector]\n\t" \

363 : \

364 : [vector] "i" (Z\_X86\_OOPS\_VECTOR), \

365 [reason] "i" (reason\_p)); \

366 CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

367} while (false)

368

369/\*

370 \* Dynamic thread object memory alignment.

371 \*

372 \* If support for SSEx extensions is enabled a 16 byte boundary is required,

373 \* since the 'fxsave' and 'fxrstor' instructions require this. In all other

374 \* cases a 4 byte boundary is sufficient.

375 \*/

376#if defined(CONFIG\_EAGER\_FPU\_SHARING) || defined(CONFIG\_LAZY\_FPU\_SHARING)

377#ifdef CONFIG\_SSE

378#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT 16

379#else

380#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT (sizeof(void \*))

381#endif

382#else

383/\* No special alignment requirements, simply align on pointer size. \*/

[ 384](x86_2ia32_2arch_8h.md#ad0a10d482624ef8d91859f5bcdc2f647)#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT (sizeof(void \*))

385#endif /\* CONFIG\_\*\_FP\_SHARING \*/

386

387

388#ifdef \_\_cplusplus

389}

390#endif

391

392#endif /\* !\_ASMLANGUAGE \*/

393

394#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ARCH\_H\_ \*/

[addr\_types.h](addr__types_8h.md)

[gdbstub.h](arch_2x86_2ia32_2gdbstub_8h.md)

IA-32 specific gdbstub interface header.

[sys\_io.h](arch_2x86_2ia32_2sys__io_8h.md)

[syscall.h](arch_2x86_2ia32_2syscall_8h.md)

x86 (IA32) specific syscall header

[thread.h](arch_2x86_2ia32_2thread_8h.md)

Per-arch thread definition.

[ffs.h](ffs_8h.md)

[pm\_system\_resume](group__subsys__pm__sys.md#ga40a040996ab6746aa7714499b41d500e)

void pm\_system\_resume(void)

Notify exit from kernel sleep.

[sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)

void sys\_trace\_isr\_enter(void)

Called when entering an ISR.

[sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)

void sys\_trace\_isr\_exit(void)

Called when exiting an ISR.

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[kernel\_structs.h](kernel__structs_8h.md)

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:72

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[pm.h](pm_8h.md)

[segmentation.h](segmentation_8h.md)

[stdbool.h](stdbool_8h.md)

[s\_isrList](structs__isrList.md)

**Definition** arch.h:76

[s\_isrList::tss](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd)

unsigned int tss

If nonzero, specifies a TSS segment selector.

**Definition** arch.h:97

[s\_isrList::fnc](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03)

void \* fnc

Address of ISR/stub.

**Definition** arch.h:78

[s\_isrList::dpl](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e)

unsigned int dpl

Privilege level associated with ISR/stub.

**Definition** arch.h:91

[s\_isrList::irq](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c)

unsigned int irq

IRQ associated with the ISR/stub, or -1 if this is not associated with a real interrupt; in this case...

**Definition** arch.h:83

[s\_isrList::vec](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3)

unsigned int vec

Vector number associated with ISR/stub, or -1 to assign based on priority.

**Definition** arch.h:89

[s\_isrList::priority](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9)

unsigned int priority

Priority associated with the IRQ.

**Definition** arch.h:85

[task\_state\_segment](structtask__state__segment.md)

**Definition** segmentation.h:54

[util.h](sys_2util_8h.md)

Misc utilities.

[arch\_isr\_direct\_footer](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)

static void arch\_isr\_direct\_footer(int swap)

**Definition** arch.h:294

[arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)

void arch\_isr\_direct\_footer\_swap(unsigned int key)

[ISR\_LIST](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378)

struct s\_isrList ISR\_LIST

[arch\_isr\_direct\_header](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)

static void arch\_isr\_direct\_header(void)

**Definition** arch.h:275

[exception.h](x86_2ia32_2exception_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [arch.h](x86_2ia32_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
