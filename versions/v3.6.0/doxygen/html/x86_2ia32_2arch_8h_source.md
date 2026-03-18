---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/x86_2ia32_2arch_8h_source.html
original_path: doxygen/html/x86_2ia32_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

22#include <[zephyr/arch/x86/ia32/gdbstub.h](arch_2x86_2ia32_2gdbstub_8h.md)>

23#include <[zephyr/arch/x86/ia32/thread.h](arch_2x86_2ia32_2thread_8h.md)>

24#include <[zephyr/arch/x86/ia32/syscall.h](arch_2x86_2ia32_2syscall_8h.md)>

25

26#ifndef \_ASMLANGUAGE

27#include <stddef.h> /\* for size\_t \*/

28

29#include <[zephyr/arch/common/addr\_types.h](addr__types_8h.md)>

30#include <[zephyr/arch/x86/ia32/segmentation.h](segmentation_8h.md)>

31#include <[zephyr/pm/pm.h](pm_8h.md)>

32

33#endif /\* \_ASMLANGUAGE \*/

34

35/\* GDT layout \*/

[ 36](x86_2ia32_2arch_8h.md#a01cd8f711fd0961b75a23e9d4642d7c3)#define CODE\_SEG 0x08

[ 37](x86_2ia32_2arch_8h.md#aee584332ca956b4e1167180bf9a456bb)#define DATA\_SEG 0x10

[ 38](x86_2ia32_2arch_8h.md#a5817f0b628919c0d0b092b2a961187e6)#define MAIN\_TSS 0x18

[ 39](x86_2ia32_2arch_8h.md#a8f9b184e3ebb59e9ec8c62b187b5ad4d)#define DF\_TSS 0x20

40

41/\*

42 \* Use for thread local storage.

43 \* Match these to gen\_gdt.py.

44 \* The 0x03 is added to limit privilege.

45 \*/

46#if defined(CONFIG\_USERSPACE)

[ 47](x86_2ia32_2arch_8h.md#abe9fa73b285cb69f2d541fbfd62923fc)#define GS\_TLS\_SEG (0x38 | 0x03)

48#elif defined(CONFIG\_HW\_STACK\_PROTECTION)

49#define GS\_TLS\_SEG (0x28 | 0x03)

50#else

51#define GS\_TLS\_SEG (0x18 | 0x03)

52#endif

53

[ 58](x86_2ia32_2arch_8h.md#a9de710989afc64c692b4366e89c42e9b)#define MK\_ISR\_NAME(x) \_\_isr\_\_##x

59

60#define Z\_DYN\_STUB\_SIZE 4

61#define Z\_DYN\_STUB\_OFFSET 0

62#define Z\_DYN\_STUB\_LONG\_JMP\_EXTRA\_SIZE 3

63#define Z\_DYN\_STUB\_PER\_BLOCK 32

64

65

66#ifndef \_ASMLANGUAGE

67

68#ifdef \_\_cplusplus

69extern "C" {

70#endif

71

72/\* interrupt/exception/error related definitions \*/

73

[ 74](structs__isrList.md)typedef struct [s\_isrList](structs__isrList.md) {

[ 76](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03) void \*[fnc](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03);

[ 81](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c) unsigned int [irq](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c);

[ 83](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9) unsigned int [priority](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9);

[ 87](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3) unsigned int [vec](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3);

[ 89](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e) unsigned int [dpl](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e);

90

[ 95](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd) unsigned int [tss](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd);

[ 96](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378)} [ISR\_LIST](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378);

97

98

119

[ 120](x86_2ia32_2arch_8h.md#aa4db2c24f5de7f8bae4a0f290fb70456)#define NANO\_CPU\_INT\_REGISTER(r, n, p, v, d) \

121 static ISR\_LIST \_\_attribute\_\_((section(".intList"))) \

122 \_\_attribute\_\_((used)) MK\_ISR\_NAME(r) = \

123 { \

124 .fnc = &(r), \

125 .irq = (n), \

126 .priority = (p), \

127 .vec = (v), \

128 .dpl = (d), \

129 .tss = 0 \

130 }

131

145#define \_X86\_IDT\_TSS\_REGISTER(tss\_p, irq\_p, priority\_p, vec\_p, dpl\_p) \

146 static ISR\_LIST \_\_attribute\_\_((section(".intList"))) \

147 \_\_attribute\_\_((used)) MK\_ISR\_NAME(vec\_p) = \

148 { \

149 .fnc = NULL, \

150 .irq = (irq\_p), \

151 .priority = (priority\_p), \

152 .vec = (vec\_p), \

153 .dpl = (dpl\_p), \

154 .tss = (tss\_p) \

155 }

156

171#define \_VECTOR\_ARG(irq\_p) (-1)

172

173#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

174#define IRQSTUBS\_TEXT\_SECTION ".pinned\_text.irqstubs"

175#else

[ 176](x86_2ia32_2arch_8h.md#a745054d50f7d95a9cfdb394521cb407f)#define IRQSTUBS\_TEXT\_SECTION ".text.irqstubs"

177#endif

178

179/\* Internally this function does a few things:

180 \*

181 \* 1. There is a declaration of the interrupt parameters in the .intList

182 \* section, used by gen\_idt to create the IDT. This does the same thing

183 \* as the NANO\_CPU\_INT\_REGISTER() macro, but is done in assembly as we

184 \* need to populate the .fnc member with the address of the assembly

185 \* IRQ stub that we generate immediately afterwards.

186 \*

187 \* 2. The IRQ stub itself is declared. The code will go in its own named

188 \* section .text.irqstubs section (which eventually gets linked into 'text')

189 \* and the stub shall be named (isr\_name)\_irq(irq\_line)\_stub

190 \*

191 \* 3. The IRQ stub pushes the ISR routine and its argument onto the stack

192 \* and then jumps to the common interrupt handling code in \_interrupt\_enter().

193 \*

194 \* 4. z\_irq\_controller\_irq\_config() is called at runtime to set the mapping

195 \* between the vector and the IRQ line as well as triggering flags

196 \*/

[ 197](x86_2ia32_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

198{ \

199 \_\_asm\_\_ \_\_volatile\_\_( \

200 ".pushsection .intList\n\t" \

201 ".long %c[isr]\_irq%c[irq]\_stub\n\t" /\* ISR\_LIST.fnc \*/ \

202 ".long %c[irq]\n\t" /\* ISR\_LIST.irq \*/ \

203 ".long %c[priority]\n\t" /\* ISR\_LIST.priority \*/ \

204 ".long %c[vector]\n\t" /\* ISR\_LIST.vec \*/ \

205 ".long 0\n\t" /\* ISR\_LIST.dpl \*/ \

206 ".long 0\n\t" /\* ISR\_LIST.tss \*/ \

207 ".popsection\n\t" \

208 ".pushsection " IRQSTUBS\_TEXT\_SECTION "\n\t" \

209 ".global %c[isr]\_irq%c[irq]\_stub\n\t" \

210 "%c[isr]\_irq%c[irq]\_stub:\n\t" \

211 "pushl %[isr\_param]\n\t" \

212 "pushl %[isr]\n\t" \

213 "jmp \_interrupt\_enter\n\t" \

214 ".popsection\n\t" \

215 : \

216 : [isr] "i" (isr\_p), \

217 [isr\_param] "i" (isr\_param\_p), \

218 [priority] "i" (priority\_p), \

219 [vector] "i" \_VECTOR\_ARG(irq\_p), \

220 [irq] "i" (irq\_p)); \

221 z\_irq\_controller\_irq\_config(Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq\_p), (irq\_p), \

222 (flags\_p)); \

223}

224

225#ifdef CONFIG\_PCIE

226

227#define ARCH\_PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, \

228 isr\_p, isr\_param\_p, flags\_p) \

229 ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p)

230

231#endif /\* CONFIG\_PCIE \*/

232

233/\* Direct interrupts won't work as expected with KPTI turned on, because

234 \* all non-user accessible pages in the page table are marked non-present.

235 \* It's likely possible to add logic to ARCH\_ISR\_DIRECT\_HEADER/FOOTER to do

236 \* the necessary trampolining to switch page tables / stacks, but this

237 \* probably loses all the latency benefits that direct interrupts provide

238 \* and one might as well use a regular interrupt anyway.

239 \*/

240#ifndef CONFIG\_X86\_KPTI

[ 241](x86_2ia32_2arch_8h.md#a875f2b1ca924721fe3854796bd96c2db)#define ARCH\_IRQ\_DIRECT\_CONNECT(irq\_p, priority\_p, isr\_p, flags\_p) \

242{ \

243 NANO\_CPU\_INT\_REGISTER(isr\_p, irq\_p, priority\_p, -1, 0); \

244 z\_irq\_controller\_irq\_config(Z\_IRQ\_TO\_INTERRUPT\_VECTOR(irq\_p), (irq\_p), \

245 (flags\_p)); \

246}

247

248#ifdef CONFIG\_PM

249static inline void arch\_irq\_direct\_pm(void)

250{

251 if (\_kernel.idle) {

252 \_kernel.idle = 0;

253 z\_pm\_save\_idle\_exit();

254 }

255}

256

257#define ARCH\_ISR\_DIRECT\_PM() arch\_irq\_direct\_pm()

258#else

[ 259](x86_2ia32_2arch_8h.md#a491cb79acec18c83b9a61b0b45dfab69)#define ARCH\_ISR\_DIRECT\_PM() do { } while (false)

260#endif

261

[ 262](x86_2ia32_2arch_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() arch\_isr\_direct\_header()

[ 263](x86_2ia32_2arch_8h.md#aa7c471213fa28b3685f153ea2a72cf9d)#define ARCH\_ISR\_DIRECT\_FOOTER(swap) arch\_isr\_direct\_footer(swap)

264

265/\* FIXME:

266 \* tracing/tracing.h cannot be included here due to circular dependency

267 \*/

268#if defined(CONFIG\_TRACING)

269extern void [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)(void);

270extern void [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)(void);

271#endif

272

[ 273](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)static inline void [arch\_isr\_direct\_header](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)(void)

274{

275#if defined(CONFIG\_TRACING)

276 [sys\_trace\_isr\_enter](group__subsys__tracing__apis.md#ga37f43a02961a847af3b7de6c474a8da4)();

277#endif

278

279 /\* We're not going to unlock IRQs, but we still need to increment this

280 \* so that arch\_is\_in\_isr() works

281 \*/

282 ++\_kernel.cpus[0].nested;

283}

284

285/\*

286 \* FIXME: z\_swap\_irqlock is an inline function declared in a private header and

287 \* cannot be referenced from a public header, so we move it to an

288 \* external function.

289 \*/

[ 290](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)extern void [arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)(unsigned int key);

291

[ 292](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)static inline void [arch\_isr\_direct\_footer](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)(int swap)

293{

294 z\_irq\_controller\_eoi();

295#if defined(CONFIG\_TRACING)

296 [sys\_trace\_isr\_exit](group__subsys__tracing__apis.md#ga7113e2760b1a7ffb1bfa108ad9bfb4be)();

297#endif

298 --\_kernel.cpus[0].nested;

299

300 /\* Call swap if all the following is true:

301 \*

302 \* 1) swap argument was enabled to this function

303 \* 2) We are not in a nested interrupt

304 \* 3) Next thread to run in the ready queue is not this thread

305 \*/

306 if (swap != 0 && \_kernel.cpus[0].nested == 0 &&

307 \_kernel.ready\_q.cache != \_current) {

308 unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

309

310 /\* Fetch EFLAGS argument to z\_swap() \*/

311 \_\_asm\_\_ volatile (

312 "pushfl\n\t"

313 "popl %0\n\t"

314 : "=g" ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

315 :

316 : "memory"

317 );

318

319 [arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

320 }

321}

322

[ 323](x86_2ia32_2arch_8h.md#a5279598e93dd914614a2ae52557be1a5)#define ARCH\_ISR\_DIRECT\_DECLARE(name) \

324 static inline int name##\_body(void); \

325 \_\_attribute\_\_ ((interrupt)) void name(void \*stack\_frame) \

326 { \

327 ARG\_UNUSED(stack\_frame); \

328 int check\_reschedule; \

329 ISR\_DIRECT\_HEADER(); \

330 check\_reschedule = name##\_body(); \

331 ISR\_DIRECT\_FOOTER(check\_reschedule); \

332 } \

333 static inline int name##\_body(void)

334#endif /\* !CONFIG\_X86\_KPTI \*/

335

348

[ 349](structnanoEsf.md)typedef struct [nanoEsf](structnanoEsf.md) {

350#ifdef CONFIG\_GDBSTUB

[ 351](structnanoEsf.md#a4ae87af42cd376c493dccd3fd257e823) unsigned int [ss](structnanoEsf.md#a4ae87af42cd376c493dccd3fd257e823);

[ 352](structnanoEsf.md#a6f38a14fc76ee0ef99ef9ce5b7eb10fe) unsigned int [gs](structnanoEsf.md#a6f38a14fc76ee0ef99ef9ce5b7eb10fe);

[ 353](structnanoEsf.md#a8e2788e018d8ceb3b83cd889d86723d9) unsigned int [fs](structnanoEsf.md#a8e2788e018d8ceb3b83cd889d86723d9);

[ 354](structnanoEsf.md#a61d97934f9586b15ef9082ff57317362) unsigned int [es](structnanoEsf.md#a61d97934f9586b15ef9082ff57317362);

[ 355](structnanoEsf.md#a6d5b8f4e7c220b804de0951294aaab95) unsigned int [ds](structnanoEsf.md#a6d5b8f4e7c220b804de0951294aaab95);

356#endif

[ 357](structnanoEsf.md#ab872f78692b5e2145fc891880558238d) unsigned int [esp](structnanoEsf.md#ab872f78692b5e2145fc891880558238d);

[ 358](structnanoEsf.md#a4a4c4ec64e8f01e8a6e3e14bde63aa8c) unsigned int [ebp](structnanoEsf.md#a4a4c4ec64e8f01e8a6e3e14bde63aa8c);

[ 359](structnanoEsf.md#afe46163b57c39529c3dce5284b0a7eb8) unsigned int [ebx](structnanoEsf.md#afe46163b57c39529c3dce5284b0a7eb8);

[ 360](structnanoEsf.md#aff8554d808df765988252674e89d7bef) unsigned int [esi](structnanoEsf.md#aff8554d808df765988252674e89d7bef);

[ 361](structnanoEsf.md#a483a384f835722c4c99a70e3c690e37a) unsigned int [edi](structnanoEsf.md#a483a384f835722c4c99a70e3c690e37a);

[ 362](structnanoEsf.md#a92a995abd01f4a5fd1a4f04a4e6400a4) unsigned int [edx](structnanoEsf.md#a92a995abd01f4a5fd1a4f04a4e6400a4);

[ 363](structnanoEsf.md#a1e72ac245fae9d8454ea572780fe6845) unsigned int [eax](structnanoEsf.md#a1e72ac245fae9d8454ea572780fe6845);

[ 364](structnanoEsf.md#a4741e6bc706a7489fe2b45c34f7bdbb6) unsigned int [ecx](structnanoEsf.md#a4741e6bc706a7489fe2b45c34f7bdbb6);

[ 365](structnanoEsf.md#ae3b485a947962361d91ee59786d46b93) unsigned int [errorCode](structnanoEsf.md#ae3b485a947962361d91ee59786d46b93);

[ 366](structnanoEsf.md#af1f3d43a394af43c49caf59a8bd384ab) unsigned int [eip](structnanoEsf.md#af1f3d43a394af43c49caf59a8bd384ab);

[ 367](structnanoEsf.md#a8ed38e432a8ef09ee219d062802bcb78) unsigned int [cs](structnanoEsf.md#a8ed38e432a8ef09ee219d062802bcb78);

[ 368](structnanoEsf.md#acfb5ead961181e179f31f92393517420) unsigned int [eflags](structnanoEsf.md#acfb5ead961181e179f31f92393517420);

369} z\_arch\_esf\_t;

370

371extern unsigned int z\_x86\_exception\_vector;

372

373struct \_x86\_syscall\_stack\_frame {

374 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) eip;

375 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cs;

376 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) eflags;

377

378 /\* These are only present if cs = USER\_CODE\_SEG \*/

379 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) esp;

380 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ss;

381};

382

[ 383](x86_2ia32_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

384{

385 unsigned int key;

386

387 \_\_asm\_\_ volatile ("pushfl; cli; popl %0" : "=g" (key) :: "memory");

388

389 return key;

390}

391

392

[ 398](x86_2ia32_2arch_8h.md#ae52cccc5fa73fafe5a7fb60accb11e35)#define NANO\_SOFT\_IRQ ((unsigned int) (-1))

399

400#ifdef CONFIG\_X86\_ENABLE\_TSS

401extern struct [task\_state\_segment](structtask__state__segment.md) \_main\_tss;

402#endif

403

[ 404](x86_2ia32_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

405 \_\_asm\_\_ volatile( \

406 "push %[reason]\n\t" \

407 "int %[vector]\n\t" \

408 : \

409 : [vector] "i" (Z\_X86\_OOPS\_VECTOR), \

410 [reason] "i" (reason\_p)); \

411 CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

412} while (false)

413

414/\*

415 \* Dynamic thread object memory alignment.

416 \*

417 \* If support for SSEx extensions is enabled a 16 byte boundary is required,

418 \* since the 'fxsave' and 'fxrstor' instructions require this. In all other

419 \* cases a 4 byte boundary is sufficient.

420 \*/

421#if defined(CONFIG\_EAGER\_FPU\_SHARING) || defined(CONFIG\_LAZY\_FPU\_SHARING)

422#ifdef CONFIG\_SSE

423#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT 16

424#else

425#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT (sizeof(void \*))

426#endif

427#else

428/\* No special alignment requirements, simply align on pointer size. \*/

[ 429](x86_2ia32_2arch_8h.md#ad0a10d482624ef8d91859f5bcdc2f647)#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT (sizeof(void \*))

430#endif /\* CONFIG\_\*\_FP\_SHARING \*/

431

432

433#ifdef \_\_cplusplus

434}

435#endif

436

437#endif /\* !\_ASMLANGUAGE \*/

438

439#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_ARCH\_H\_ \*/

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

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[nanoEsf](structnanoEsf.md)

Exception Stack Frame.

**Definition** arch.h:349

[nanoEsf::eax](structnanoEsf.md#a1e72ac245fae9d8454ea572780fe6845)

unsigned int eax

**Definition** arch.h:363

[nanoEsf::ecx](structnanoEsf.md#a4741e6bc706a7489fe2b45c34f7bdbb6)

unsigned int ecx

**Definition** arch.h:364

[nanoEsf::edi](structnanoEsf.md#a483a384f835722c4c99a70e3c690e37a)

unsigned int edi

**Definition** arch.h:361

[nanoEsf::ebp](structnanoEsf.md#a4a4c4ec64e8f01e8a6e3e14bde63aa8c)

unsigned int ebp

**Definition** arch.h:358

[nanoEsf::ss](structnanoEsf.md#a4ae87af42cd376c493dccd3fd257e823)

unsigned int ss

**Definition** arch.h:351

[nanoEsf::es](structnanoEsf.md#a61d97934f9586b15ef9082ff57317362)

unsigned int es

**Definition** arch.h:354

[nanoEsf::ds](structnanoEsf.md#a6d5b8f4e7c220b804de0951294aaab95)

unsigned int ds

**Definition** arch.h:355

[nanoEsf::gs](structnanoEsf.md#a6f38a14fc76ee0ef99ef9ce5b7eb10fe)

unsigned int gs

**Definition** arch.h:352

[nanoEsf::fs](structnanoEsf.md#a8e2788e018d8ceb3b83cd889d86723d9)

unsigned int fs

**Definition** arch.h:353

[nanoEsf::cs](structnanoEsf.md#a8ed38e432a8ef09ee219d062802bcb78)

unsigned int cs

**Definition** arch.h:367

[nanoEsf::edx](structnanoEsf.md#a92a995abd01f4a5fd1a4f04a4e6400a4)

unsigned int edx

**Definition** arch.h:362

[nanoEsf::esp](structnanoEsf.md#ab872f78692b5e2145fc891880558238d)

unsigned int esp

**Definition** arch.h:357

[nanoEsf::eflags](structnanoEsf.md#acfb5ead961181e179f31f92393517420)

unsigned int eflags

**Definition** arch.h:368

[nanoEsf::errorCode](structnanoEsf.md#ae3b485a947962361d91ee59786d46b93)

unsigned int errorCode

**Definition** arch.h:365

[nanoEsf::eip](structnanoEsf.md#af1f3d43a394af43c49caf59a8bd384ab)

unsigned int eip

**Definition** arch.h:366

[nanoEsf::ebx](structnanoEsf.md#afe46163b57c39529c3dce5284b0a7eb8)

unsigned int ebx

**Definition** arch.h:359

[nanoEsf::esi](structnanoEsf.md#aff8554d808df765988252674e89d7bef)

unsigned int esi

**Definition** arch.h:360

[s\_isrList](structs__isrList.md)

**Definition** arch.h:74

[s\_isrList::tss](structs__isrList.md#a2278f1081695c526ba30fa5f9f8aaecd)

unsigned int tss

If nonzero, specifies a TSS segment selector.

**Definition** arch.h:95

[s\_isrList::fnc](structs__isrList.md#a62299be9af7bf7d395c5ad34fdcc4f03)

void \* fnc

Address of ISR/stub.

**Definition** arch.h:76

[s\_isrList::dpl](structs__isrList.md#a6e70d162cb57609281f497ea5eb0321e)

unsigned int dpl

Privilege level associated with ISR/stub.

**Definition** arch.h:89

[s\_isrList::irq](structs__isrList.md#a885d8d1a26e11d2b6fb6b951da96550c)

unsigned int irq

IRQ associated with the ISR/stub, or -1 if this is not associated with a real interrupt; in this case...

**Definition** arch.h:81

[s\_isrList::vec](structs__isrList.md#af1bc7016fb72489f391db03a9fdf0fd3)

unsigned int vec

Vector number associated with ISR/stub, or -1 to assign based on priority.

**Definition** arch.h:87

[s\_isrList::priority](structs__isrList.md#af8bdba11e6c31f4920b18c117bb93bf9)

unsigned int priority

Priority associated with the IRQ.

**Definition** arch.h:83

[task\_state\_segment](structtask__state__segment.md)

**Definition** segmentation.h:54

[util.h](util_8h.md)

Misc utilities.

[arch\_isr\_direct\_footer](x86_2ia32_2arch_8h.md#a13a88acdff251283bf6f364e4393adaf)

static void arch\_isr\_direct\_footer(int swap)

**Definition** arch.h:292

[arch\_isr\_direct\_footer\_swap](x86_2ia32_2arch_8h.md#a4ced4d5bdb1d0f3d069d9384615ed394)

void arch\_isr\_direct\_footer\_swap(unsigned int key)

[ISR\_LIST](x86_2ia32_2arch_8h.md#abd14415ccf779280bd7eac3974b6a378)

struct s\_isrList ISR\_LIST

[arch\_isr\_direct\_header](x86_2ia32_2arch_8h.md#ac8579cbf5edce72a6a4bfbbed3166683)

static void arch\_isr\_direct\_header(void)

**Definition** arch.h:273

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [arch.h](x86_2ia32_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
