---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/x86_2ia32_2arch_8h_source.html
original_path: doxygen/html/x86_2ia32_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ARCH\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ARCH\_H\_

16

17#include "[sys\_io.h](arch_2x86_2ia32_2sys__io_8h.md)"

18#include <[stdbool.h](stdbool_8h.md)>

19#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

20#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

21#include <[zephyr/sys/util.h](util_8h.md)>

22#include <[zephyr/arch/x86/ia32/exception.h](x86_2ia32_2exception_8h.md)>

23#include <[zephyr/arch/x86/ia32/gdbstub.h](arch_2x86_2ia32_2gdbstub_8h.md)>

24#include <[zephyr/arch/x86/ia32/thread.h](arch_2x86_2ia32_2thread_8h.md)>

25#include <[zephyr/arch/x86/ia32/syscall.h](arch_2x86_2ia32_2syscall_8h.md)>

26

27#ifndef \_ASMLANGUAGE

28#include <stddef.h> /\* for size\_t \*/

29

30#include <[zephyr/arch/common/addr\_types.h](addr__types_8h.md)>

31#include <[zephyr/arch/x86/ia32/segmentation.h](segmentation_8h.md)>

32#include <[zephyr/pm/pm.h](pm_8h.md)>

33

34#endif /\* \_ASMLANGUAGE \*/

35

36/\* GDT layout \*/

[ 37](x86_2ia32_2arch_8h.md#a01cd8f711fd0961b75a23e9d4642d7c3)#define CODE\_SEG 0x08

[ 38](x86_2ia32_2arch_8h.md#aee584332ca956b4e1167180bf9a456bb)#define DATA\_SEG 0x10

[ 39](x86_2ia32_2arch_8h.md#a5817f0b628919c0d0b092b2a961187e6)#define MAIN\_TSS 0x18

[ 40](x86_2ia32_2arch_8h.md#a8f9b184e3ebb59e9ec8c62b187b5ad4d)#define DF\_TSS 0x20

41

42/\*

43 \* Use for thread local storage.

44 \* Match these to gen\_gdt.py.

45 \* The 0x03 is added to limit privilege.

46 \*/

47#if defined(CONFIG\_USERSPACE)

[ 48](x86_2ia32_2arch_8h.md#abe9fa73b285cb69f2d541fbfd62923fc)#define GS\_TLS\_SEG (0x38 | 0x03)

49#elif defined(CONFIG\_X86\_STACK\_PROTECTION)

50#define GS\_TLS\_SEG (0x28 | 0x03)

51#else

52#define GS\_TLS\_SEG (0x18 | 0x03)

53#endif

54

[ 59](x86_2ia32_2arch_8h.md#a9de710989afc64c692b4366e89c42e9b)#define MK\_ISR\_NAME(x) \_\_isr\_\_##x

60

61#define Z\_DYN\_STUB\_SIZE 4

62#define Z\_DYN\_STUB\_OFFSET 0

63#define Z\_DYN\_STUB\_LONG\_JMP\_EXTRA\_SIZE 3

64#define Z\_DYN\_STUB\_PER\_BLOCK 32

65

66

67#ifndef \_ASMLANGUAGE

68

69#ifdef \_\_cplusplus

70extern "C" {

71#endif

72

73/\* interrupt/exception/error related definitions \*/

74

[ 75](structs__isrList.md)typedef struct [s\_isrList](structs__isrList.md) {

[ 77](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03) void \*[fnc](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03);

[ 82](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c) unsigned int [irq](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c);

[ 84](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9) unsigned int [priority](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9);

[ 88](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3) unsigned int [vec](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3);

[ 90](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e) unsigned int [dpl](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e);

91

[ 96](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd) unsigned int [tss](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd);

[ 97](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378)} [ISR\_LIST](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378);

98

99

120

[ 121](x86_2ia32_2arch_8h.md#aa4db2c24f5de7f8bae4a0f290fb70456)#define NANO\_CPU\_INT\_REGISTER(r, n, p, v, d) \

122 static ISR\_LIST \_\_attribute\_\_((section(".intList"))) \

123 \_\_attribute\_\_((used)) MK\_ISR\_NAME(r) = \

124 { \

125 .fnc = &(r), \

126 .irq = (n), \

127 .priority = (p), \

128 .vec = (v), \

129 .dpl = (d), \

130 .tss = 0 \

131 }

132

146#define \_X86\_IDT\_TSS\_REGISTER(tss\_p, irq\_p, priority\_p, vec\_p, dpl\_p) \

147 static ISR\_LIST \_\_attribute\_\_((section(".intList"))) \

148 \_\_attribute\_\_((used)) MK\_ISR\_NAME(vec\_p) = \

149 { \

150 .fnc = NULL, \

151 .irq = (irq\_p), \

152 .priority = (priority\_p), \

153 .vec = (vec\_p), \

154 .dpl = (dpl\_p), \

155 .tss = (tss\_p) \

156 }

157

172#define \_VECTOR\_ARG(irq\_p) (-1)

173

174#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

175#define IRQSTUBS\_TEXT\_SECTION ".pinned\_text.irqstubs"

176#else

[ 177](x86_2ia32_2arch_8h.md#a745054d50f7d95a9cfdb394521cb407f)#define IRQSTUBS\_TEXT\_SECTION ".text.irqstubs"

178#endif

179

180/\* Internally this function does a few things:

181 \*

182 \* 1. There is a declaration of the interrupt parameters in the .intList

183 \* section, used by gen\_idt to create the IDT. This does the same thing

184 \* as the NANO\_CPU\_INT\_REGISTER() macro, but is done in assembly as we

185 \* need to populate the .fnc member with the address of the assembly

186 \* IRQ stub that we generate immediately afterwards.

187 \*

188 \* 2. The IRQ stub itself is declared. The code will go in its own named

189 \* section .text.irqstubs section (which eventually gets linked into 'text')

190 \* and the stub shall be named (isr\_name)\_irq(irq\_line)\_stub

191 \*

192 \* 3. The IRQ stub pushes the ISR routine and its argument onto the stack

193 \* and then jumps to the common interrupt handling code in \_interrupt\_enter().

194 \*

195 \* 4. z\_irq\_controller\_irq\_config() is called at runtime to set the mapping

196 \* between the vector and the IRQ line as well as triggering flags

197 \*/

[ 198](x86_2ia32_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

199{ \

200 \_\_asm\_\_ \_\_volatile\_\_( \

201 ".pushsection .intList\n\t" \

202 ".long %c[isr]\_irq%c[irq]\_stub\n\t" /\* ISR\_LIST.fnc \*/ \

203 ".long %c[irq]\n\t" /\* ISR\_LIST.irq \*/ \

204 ".long %c[priority]\n\t" /\* ISR\_LIST.priority \*/ \

205 ".long %c[vector]\n\t" /\* ISR\_LIST.vec \*/ \

206 ".long 0\n\t" /\* ISR\_LIST.dpl \*/ \

207 ".long 0\n\t" /\* ISR\_LIST.tss \*/ \

208 ".popsection\n\t" \

209 ".pushsection " IRQSTUBS\_TEXT\_SECTION "\n\t" \

210 ".global %c[isr]\_irq%c[irq]\_stub\n\t" \

211 "%c[isr]\_irq%c[irq]\_stub:\n\t" \

212 "pushl %[isr\_param]\n\t" \

213 "pushl %[isr]\n\t" \

214 "jmp \_interrupt\_enter\n\t" \

215 ".popsection\n\t" \

216 : \

217 : [isr] "i" (isr\_p), \

218 [isr\_param] "i" (isr\_param\_p), \

219 [priority] "i" (priority\_p), \

220 [vector] "i" \_VECTOR\_ARG(irq\_p), \

221 [irq] "i" (irq\_p)); \

222 z\_irq\_controller\_irq\_config(Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq\_p), (irq\_p), \

223 (flags\_p)); \

224}

225

226#ifdef CONFIG\_PCIE

227

228#define ARCH\_PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, \

229 isr\_p, isr\_param\_p, flags\_p) \

230 ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p)

231

232#endif /\* CONFIG\_PCIE \*/

233

234/\* Direct interrupts won't work as expected with KPTI turned on, because

235 \* all non-user accessible pages in the page table are marked non-present.

236 \* It's likely possible to add logic to ARCH\_ISR\_DIRECT\_HEADER/FOOTER to do

237 \* the necessary trampolining to switch page tables / stacks, but this

238 \* probably loses all the latency benefits that direct interrupts provide

239 \* and one might as well use a regular interrupt anyway.

240 \*/

241#ifndef CONFIG\_X86\_KPTI

[ 242](x86_2ia32_2arch_8h.md#a875f2b1ca924721fe3854796bd96c2db)#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

243{ \

244 NANO\_CPU\_INT\_REGISTER(isr\_p, irq\_p, priority\_p, -1, 0); \

245 z\_irq\_controller\_irq\_config(Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq\_p), (irq\_p), \

246 (flags\_p)); \

247}

248

249#ifdef CONFIG\_PM

250static inline void arch\_irq\_direct\_pm(void)

251{

252 if (\_kernel.idle) {

253 \_kernel.idle = 0;

254 [pm\_system\_resume](group__subsys__pm__sys.md#ga40a040996ab6746aa7714499b41d500e)();

255 }

256}

257

258#define ARCH\_ISR\_DIRECT\_PM() arch\_irq\_direct\_pm()

259#else

[ 260](x86_2ia32_2arch_8h.md#a491cb79acec18c83b9a61b0b45dfab69)#define ARCH\_ISR\_DIRECT\_PM() do { } while (false)

261#endif

262

[ 263](x86_2ia32_2arch_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() arch\_isr\_direct\_header()

[ 264](x86_2ia32_2arch_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)#define ARCH\_ISR\_DIRECT\_FOOTER(swap) arch\_isr\_direct\_footer(swap)

265

266/\* FIXME:

267 \* tracing/tracing.h cannot be included here due to circular dependency

268 \*/

269#if defined(CONFIG\_TRACING)

270void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

271void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

272#endif

273

[ 274](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)static inline void [arch\_isr\_direct\_header](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)(void)

275{

276#if defined(CONFIG\_TRACING)

277 [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)();

278#endif

279

280 /\* We're not going to unlock IRQs, but we still need to increment this

281 \* so that arch\_is\_in\_isr() works

282 \*/

283 ++\_kernel.cpus[0].nested;

284}

285

286/\*

287 \* FIXME: z\_swap\_irqlock is an inline function declared in a private header and

288 \* cannot be referenced from a public header, so we move it to an

289 \* external function.

290 \*/

[ 291](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)void [arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)(unsigned int key);

292

[ 293](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)static inline void [arch\_isr\_direct\_footer](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)(int swap)

294{

295 z\_irq\_controller\_eoi();

296#if defined(CONFIG\_TRACING)

297 [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)();

298#endif

299 --\_kernel.cpus[0].nested;

300

301 /\* Call swap if all the following is true:

302 \*

303 \* 1) swap argument was enabled to this function

304 \* 2) We are not in a nested interrupt

305 \* 3) Next thread to run in the ready queue is not this thread

306 \*/

307 if (swap != 0 && \_kernel.cpus[0].nested == 0 &&

308 \_kernel.ready\_q.cache != \_current) {

309 unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

310

311 /\* Fetch EFLAGS argument to z\_swap() \*/

312 \_\_asm\_\_ volatile (

313 "pushfl\n\t"

314 "popl %0\n\t"

315 : "=g" ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

316 :

317 : "memory"

318 );

319

320 [arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

321 }

322}

323

[ 324](x86_2ia32_2arch_8h.md#a5279598e93dd914614a2ae52557be1a5)#define ARCH\_ISR\_DIRECT\_DECLARE(name) \

325 static inline int name##\_body(void); \

326 \_\_attribute\_\_ ((interrupt)) void name(void \*stack\_frame) \

327 { \

328 ARG\_UNUSED(stack\_frame); \

329 int check\_reschedule; \

330 ISR\_DIRECT\_HEADER(); \

331 check\_reschedule = name##\_body(); \

332 ISR\_DIRECT\_FOOTER(check\_reschedule); \

333 } \

334 static inline int name##\_body(void)

335#endif /\* !CONFIG\_X86\_KPTI \*/

336

[ 337](x86_2ia32_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

338{

339 unsigned int key;

340

341 \_\_asm\_\_ volatile ("pushfl; cli; popl %0" : "=g" (key) :: "memory");

342

343 return key;

344}

345

346

[ 352](x86_2ia32_2arch_8h.md#ae52cccc5fa73fafe5a7fb60accb11e35)#define NANO\_SOFT\_IRQ ((unsigned int) (-1))

353

354#ifdef CONFIG\_X86\_ENABLE\_TSS

355extern struct [task\_state\_segment](structtask__state__segment.md) \_main\_tss;

356#endif

357

[ 358](x86_2ia32_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

359 \_\_asm\_\_ volatile( \

360 "push %[reason]\n\t" \

361 "int %[vector]\n\t" \

362 : \

363 : [vector] "i" (Z\_X86\_OOPS\_VECTOR), \

364 [reason] "i" (reason\_p)); \

365 CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

366} while (false)

367

368/\*

369 \* Dynamic thread object memory alignment.

370 \*

371 \* If support for SSEx extensions is enabled a 16 byte boundary is required,

372 \* since the 'fxsave' and 'fxrstor' instructions require this. In all other

373 \* cases a 4 byte boundary is sufficient.

374 \*/

375#if defined(CONFIG\_EAGER\_FPU\_SHARING) || defined(CONFIG\_LAZY\_FPU\_SHARING)

376#ifdef CONFIG\_SSE

377#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT 16

378#else

379#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT (sizeof(void \*))

380#endif

381#else

382/\* No special alignment requirements, simply align on pointer size. \*/

[ 383](x86_2ia32_2arch_8h.md#ad0a10d482624ef8d91859f5bcdc2f647)#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT (sizeof(void \*))

384#endif /\* CONFIG\_\*\_FP\_SHARING \*/

385

386

387#ifdef \_\_cplusplus

388}

389#endif

390

391#endif /\* !\_ASMLANGUAGE \*/

392

393#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ARCH\_H\_ \*/

[addr\_types.h](addr__types_8h.md)

[gdbstub.h](arch_2x86_2ia32_2gdbstub_8h.md)

IA-32 specific gdbstub interface header.

[sys\_io.h](arch_2x86_2ia32_2sys__io_8h.md)

[syscall.h](arch_2x86_2ia32_2syscall_8h.md)

x86 (IA32) specific syscall header

[thread.h](arch_2x86_2ia32_2thread_8h.md)

Per-arch thread definition.

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

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

[kernel\_structs.h](kernel__structs_8h.md)

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:63

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[pm.h](pm_8h.md)

[segmentation.h](segmentation_8h.md)

[stdbool.h](stdbool_8h.md)

[s\_isrList](structs__isrList.md)

**Definition** arch.h:75

[s\_isrList::tss](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd)

unsigned int tss

If nonzero, specifies a TSS segment selector.

**Definition** arch.h:96

[s\_isrList::fnc](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03)

void \* fnc

Address of ISR/stub.

**Definition** arch.h:77

[s\_isrList::dpl](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e)

unsigned int dpl

Privilege level associated with ISR/stub.

**Definition** arch.h:90

[s\_isrList::irq](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c)

unsigned int irq

IRQ associated with the ISR/stub, or -1 if this is not associated with a real interrupt; in this case...

**Definition** arch.h:82

[s\_isrList::vec](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3)

unsigned int vec

Vector number associated with ISR/stub, or -1 to assign based on priority.

**Definition** arch.h:88

[s\_isrList::priority](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9)

unsigned int priority

Priority associated with the IRQ.

**Definition** arch.h:84

[task\_state\_segment](structtask__state__segment.md)

**Definition** segmentation.h:54

[util.h](util_8h.md)

Misc utilities.

[arch\_isr\_direct\_footer](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)

static void arch\_isr\_direct\_footer(int swap)

**Definition** arch.h:293

[arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)

void arch\_isr\_direct\_footer\_swap(unsigned int key)

[ISR\_LIST](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378)

struct s\_isrList ISR\_LIST

[arch\_isr\_direct\_header](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)

static void arch\_isr\_direct\_header(void)

**Definition** arch.h:274

[exception.h](x86_2ia32_2exception_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [arch.h](x86_2ia32_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
