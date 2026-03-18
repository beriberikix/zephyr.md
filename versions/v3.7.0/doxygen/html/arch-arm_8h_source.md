---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch-arm_8h_source.html
original_path: doxygen/html/arch-arm_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch-arm.h

[Go to the documentation of this file.](arch-arm_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 \* arch-arm.h

5 \*

6 \* Guest OS interface to ARM Xen.

7 \*

8 \* Permission is hereby granted, free of charge, to any person obtaining a copy

9 \* of this software and associated documentation files (the "Software"), to

10 \* deal in the Software without restriction, including without limitation the

11 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

12 \* sell copies of the Software, and to permit persons to whom the Software is

13 \* furnished to do so, subject to the following conditions:

14 \*

15 \* The above copyright notice and this permission notice shall be included in

16 \* all copies or substantial portions of the Software.

17 \*

18 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

19 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

20 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

21 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

22 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

23 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

24 \* DEALINGS IN THE SOFTWARE.

25 \*

26 \* Copyright 2011 (C) Citrix Systems

27 \*/

28

29#ifndef \_\_XEN\_PUBLIC\_ARCH\_ARM\_H\_\_

30#define \_\_XEN\_PUBLIC\_ARCH\_ARM\_H\_\_

31

32#include <[zephyr/kernel.h](kernel_8h.md)>

33

34/\*

35 \* `incontents 50 arm\_abi Hypercall Calling Convention

36 \*

37 \* A hypercall is issued using the ARM HVC instruction.

38 \*

39 \* A hypercall can take up to 5 arguments. These are passed in

40 \* registers, the first argument in x0/r0 (for arm64/arm32 guests

41 \* respectively irrespective of whether the underlying hypervisor is

42 \* 32- or 64-bit), the second argument in x1/r1, the third in x2/r2,

43 \* the forth in x3/r3 and the fifth in x4/r4.

44 \*

45 \* The hypercall number is passed in r12 (arm) or x16 (arm64). In both

46 \* cases the relevant ARM procedure calling convention specifies this

47 \* is an inter-procedure-call scratch register (e.g. for use in linker

48 \* stubs). This use does not conflict with use during a hypercall.

49 \*

50 \* The HVC ISS must contain a Xen specific TAG: XEN\_HYPERCALL\_TAG.

51 \*

52 \* The return value is in x0/r0.

53 \*

54 \* The hypercall will clobber x16/r12 and the argument registers used

55 \* by that hypercall (except r0 which is the return value) i.e. in

56 \* addition to x16/r12 a 2 argument hypercall will clobber x1/r1 and a

57 \* 4 argument hypercall will clobber x1/r1, x2/r2 and x3/r3.

58 \*

59 \* Parameter structs passed to hypercalls are laid out according to

60 \* the Procedure Call Standard for the ARM Architecture (AAPCS, AKA

61 \* EABI) and Procedure Call Standard for the ARM 64-bit Architecture

62 \* (AAPCS64). Where there is a conflict the 64-bit standard should be

63 \* used regardless of guest type. Structures which are passed as

64 \* hypercall arguments are always little endian.

65 \*

66 \* All memory which is shared with other entities in the system

67 \* (including the hypervisor and other guests) must reside in memory

68 \* which is mapped as Normal Inner Write-Back Outer Write-Back Inner-Shareable.

69 \* This applies to:

70 \* - hypercall arguments passed via a pointer to guest memory.

71 \* - memory shared via the grant table mechanism (including PV I/O

72 \* rings etc).

73 \* - memory shared with the hypervisor (struct shared\_info, struct

74 \* vcpu\_info, the grant table, etc).

75 \*

76 \* Any cache allocation hints are acceptable.

77 \*/

78

79/\*

80 \* `incontents 55 arm\_hcall Supported Hypercalls

81 \*

82 \* Xen on ARM makes extensive use of hardware facilities and therefore

83 \* only a subset of the potential hypercalls are required.

84 \*

85 \* Since ARM uses second stage paging any machine/physical addresses

86 \* passed to hypercalls are Guest Physical Addresses (Intermediate

87 \* Physical Addresses) unless otherwise noted.

88 \*

89 \* The following hypercalls (and sub operations) are supported on the

90 \* ARM platform. Other hypercalls should be considered

91 \* unavailable/unsupported.

92 \*

93 \* HYPERVISOR\_memory\_op

94 \* All generic sub-operations

95 \*

96 \* HYPERVISOR\_domctl

97 \* All generic sub-operations, with the exception of:

98 \* \* XEN\_DOMCTL\_irq\_permission (not yet implemented)

99 \*

100 \* HYPERVISOR\_sched\_op

101 \* All generic sub-operations, with the exception of:

102 \* \* SCHEDOP\_block -- prefer wfi hardware instruction

103 \*

104 \* HYPERVISOR\_console\_io

105 \* All generic sub-operations

106 \*

107 \* HYPERVISOR\_xen\_version

108 \* All generic sub-operations

109 \*

110 \* HYPERVISOR\_event\_channel\_op

111 \* All generic sub-operations

112 \*

113 \* HYPERVISOR\_physdev\_op

114 \* No sub-operations are currently supported

115 \*

116 \* HYPERVISOR\_sysctl

117 \* All generic sub-operations, with the exception of:

118 \* \* XEN\_SYSCTL\_page\_offline\_op

119 \* \* XEN\_SYSCTL\_get\_pmstat

120 \* \* XEN\_SYSCTL\_pm\_op

121 \*

122 \* HYPERVISOR\_hvm\_op

123 \* Exactly these sub-operations are supported:

124 \* \* HVMOP\_set\_param

125 \* \* HVMOP\_get\_param

126 \*

127 \* HYPERVISOR\_grant\_table\_op

128 \* All generic sub-operations

129 \*

130 \* HYPERVISOR\_vcpu\_op

131 \* Exactly these sub-operations are supported:

132 \* \* VCPUOP\_register\_vcpu\_info

133 \* \* VCPUOP\_register\_runstate\_memory\_area

134 \*

135 \*

136 \* Other notes on the ARM ABI:

137 \*

138 \* - struct start\_info is not exported to ARM guests.

139 \*

140 \* - struct shared\_info is mapped by ARM guests using the

141 \* HYPERVISOR\_memory\_op sub-op XENMEM\_add\_to\_physmap, passing

142 \* XENMAPSPACE\_shared\_info as space parameter.

143 \*

144 \* - All the per-cpu struct vcpu\_info are mapped by ARM guests using the

145 \* HYPERVISOR\_vcpu\_op sub-op VCPUOP\_register\_vcpu\_info, including cpu0

146 \* struct vcpu\_info.

147 \*

148 \* - The grant table is mapped using the HYPERVISOR\_memory\_op sub-op

149 \* XENMEM\_add\_to\_physmap, passing XENMAPSPACE\_grant\_table as space

150 \* parameter. The memory range specified under the Xen compatible

151 \* hypervisor node on device tree can be used as target gpfn for the

152 \* mapping.

153 \*

154 \* - Xenstore is initialized by using the two hvm\_params

155 \* HVM\_PARAM\_STORE\_PFN and HVM\_PARAM\_STORE\_EVTCHN. They can be read

156 \* with the HYPERVISOR\_hvm\_op sub-op HVMOP\_get\_param.

157 \*

158 \* - The paravirtualized console is initialized by using the two

159 \* hvm\_params HVM\_PARAM\_CONSOLE\_PFN and HVM\_PARAM\_CONSOLE\_EVTCHN. They

160 \* can be read with the HYPERVISOR\_hvm\_op sub-op HVMOP\_get\_param.

161 \*

162 \* - Event channel notifications are delivered using the percpu GIC

163 \* interrupt specified under the Xen compatible hypervisor node on

164 \* device tree.

165 \*

166 \* - The device tree Xen compatible node is fully described under Linux

167 \* at Documentation/devicetree/bindings/arm/xen.txt.

168 \*/

169

[ 170](arch-arm_8h.md#aa5e158f6f21dcc54391239d9ac71f32b)#define XEN\_HYPERCALL\_TAG 0XEA1

171

[ 172](arch-arm_8h.md#a8e346fda4301d9806f5b97d796af4d0c)#define int64\_aligned\_t int64\_t \_\_aligned(8)

[ 173](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128)#define uint64\_aligned\_t uint64\_t \_\_aligned(8)

174

175#ifndef \_\_ASSEMBLY\_\_

176#define \_\_\_DEFINE\_XEN\_GUEST\_HANDLE(name, type) \

177 typedef union { type \*p; unsigned long q; } \

178 \_\_guest\_handle\_ ## name; \

179 typedef union { type \*p; uint64\_aligned\_t q; } \

180 \_\_guest\_handle\_64\_ ## name

181

182/\*

183 \* XEN\_GUEST\_HANDLE represents a guest pointer, when passed as a field

184 \* in a struct in memory. On ARM is always 8 bytes sizes and 8 bytes

185 \* aligned.

186 \* XEN\_GUEST\_HANDLE\_PARAM represents a guest pointer, when passed as an

187 \* hypercall argument. It is 4 bytes on aarch32 and 8 bytes on aarch64.

188 \*/

189#define \_\_DEFINE\_XEN\_GUEST\_HANDLE(name, type) \

190 \_\_\_DEFINE\_XEN\_GUEST\_HANDLE(name, type); \

191 \_\_\_DEFINE\_XEN\_GUEST\_HANDLE(const\_##name, const type)

[ 192](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)#define DEFINE\_XEN\_GUEST\_HANDLE(name) \_\_DEFINE\_XEN\_GUEST\_HANDLE(name, name)

193#define \_\_XEN\_GUEST\_HANDLE(name) \_\_guest\_handle\_64\_ ## name

[ 194](arch-arm_8h.md#a59eac5b471e486c9cdb4743017fdfc20)#define XEN\_GUEST\_HANDLE(name) \_\_XEN\_GUEST\_HANDLE(name)

[ 195](arch-arm_8h.md#a2d269ec4cb445d086e8fca4d4288f7ce)#define XEN\_GUEST\_HANDLE\_PARAM(name) \_\_guest\_handle\_ ## name

[ 196](arch-arm_8h.md#a3d4d2c27792e69e7f925e2a4e3390091)#define set\_xen\_guest\_handle\_raw(hnd, val) \

197 do { \

198 \_\_typeof\_\_(&(hnd)) \_sxghr\_tmp = &(hnd); \

199 \_sxghr\_tmp->q = 0; \

200 \_sxghr\_tmp->p = val; \

201 } while (0)

[ 202](arch-arm_8h.md#a393eef7cbafc7f0e2d64ba971e0c8079)#define set\_xen\_guest\_handle(hnd, val) set\_xen\_guest\_handle\_raw(hnd, val)

203

[ 204](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226);

[ 205](arch-arm_8h.md#a4a9cdcf7a527951f75cf8b8c2b6eb828)#define PRI\_xen\_pfn PRIx64

[ 206](arch-arm_8h.md#acc5c5e4cd20a58ea2246de620bed79fe)#define PRIu\_xen\_pfn PRIu64

207

208/\*

209 \* Maximum number of virtual CPUs in legacy multi-processor guests.

210 \* Only one. All other VCPUS must use VCPUOP\_register\_vcpu\_info.

211 \*/

[ 212](arch-arm_8h.md#a57246b966cc182f34ca4f9bfa101e449)#define XEN\_LEGACY\_MAX\_VCPUS 1

213

[ 214](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc);

[ 215](arch-arm_8h.md#ae5fed872d1684ca8fb200bd02927766c)#define PRI\_xen\_ulong PRIx64

216

217#ifdef CONFIG\_XEN\_DOM0

218#if defined(\_\_GNUC\_\_) && !defined(\_\_STRICT\_ANSI\_\_)

219/\* Anonymous union includes both 32- and 64-bit names (e.g., r0/x0). \*/

220# define \_\_DECL\_REG(n64, n32) union { \

221 uint64\_t n64; \

222 uint32\_t n32; \

223}

224#else

225/\* Non-gcc sources must always use the proper 64-bit name (e.g., x0). \*/

226#define \_\_DECL\_REG(n64, n32) uint64\_t n64

227#endif

228

229struct vcpu\_guest\_core\_regs {

230 /\* Aarch64 Aarch32 \*/

231 \_\_DECL\_REG(x0, r0\_usr);

232 \_\_DECL\_REG(x1, r1\_usr);

233 \_\_DECL\_REG(x2, r2\_usr);

234 \_\_DECL\_REG(x3, r3\_usr);

235 \_\_DECL\_REG(x4, r4\_usr);

236 \_\_DECL\_REG(x5, r5\_usr);

237 \_\_DECL\_REG(x6, r6\_usr);

238 \_\_DECL\_REG(x7, r7\_usr);

239 \_\_DECL\_REG(x8, r8\_usr);

240 \_\_DECL\_REG(x9, r9\_usr);

241 \_\_DECL\_REG(x10, r10\_usr);

242 \_\_DECL\_REG(x11, r11\_usr);

243 \_\_DECL\_REG(x12, r12\_usr);

244

245 \_\_DECL\_REG(x13, sp\_usr);

246 \_\_DECL\_REG(x14, lr\_usr);

247

248 \_\_DECL\_REG(x15, \_\_unused\_sp\_hyp);

249

250 \_\_DECL\_REG(x16, lr\_irq);

251 \_\_DECL\_REG(x17, sp\_irq);

252

253 \_\_DECL\_REG(x18, lr\_svc);

254 \_\_DECL\_REG(x19, sp\_svc);

255

256 \_\_DECL\_REG(x20, lr\_abt);

257 \_\_DECL\_REG(x21, sp\_abt);

258

259 \_\_DECL\_REG(x22, lr\_und);

260 \_\_DECL\_REG(x23, sp\_und);

261

262 \_\_DECL\_REG(x24, r8\_fiq);

263 \_\_DECL\_REG(x25, r9\_fiq);

264 \_\_DECL\_REG(x26, r10\_fiq);

265 \_\_DECL\_REG(x27, r11\_fiq);

266 \_\_DECL\_REG(x28, r12\_fiq);

267

268 \_\_DECL\_REG(x29, sp\_fiq);

269 \_\_DECL\_REG(x30, lr\_fiq);

270

271 /\* Return address and mode \*/

272 \_\_DECL\_REG(pc64, pc32); /\* ELR\_EL2 \*/

273 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cpsr; /\* SPSR\_EL2 \*/

274

275 union {

276 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsr\_el1; /\* AArch64 \*/

277 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsr\_svc; /\* AArch32 \*/

278 };

279

280 /\* AArch32 guests only \*/

281 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spsr\_fiq, spsr\_irq, spsr\_und, spsr\_abt;

282

283 /\* AArch64 guests only \*/

284 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sp\_el0;

285 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sp\_el1, elr\_el1;

286};

287typedef struct vcpu\_guest\_core\_regs vcpu\_guest\_core\_regs\_t;

288[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)(vcpu\_guest\_core\_regs\_t);

289

290#undef \_\_DECL\_REG

291

292struct vcpu\_guest\_context {

293#define \_VGCF\_online 0

294#define VGCF\_online (1 << \_VGCF\_online)

295 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* VGCF\_\* \*/

296

297 struct vcpu\_guest\_core\_regs user\_regs; /\* Core CPU registers \*/

298

299 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sctlr;

300 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ttbcr, ttbr0, ttbr1;

301};

302typedef struct vcpu\_guest\_context vcpu\_guest\_context\_t;

303[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)(vcpu\_guest\_context\_t);

304

305/\*

306 \* struct xen\_arch\_domainconfig's ABI is covered by

307 \* XEN\_DOMCTL\_INTERFACE\_VERSION.

308 \*/

309#define XEN\_DOMCTL\_CONFIG\_GIC\_NATIVE 0

310#define XEN\_DOMCTL\_CONFIG\_GIC\_V2 1

311#define XEN\_DOMCTL\_CONFIG\_GIC\_V3 2

312

313#define XEN\_DOMCTL\_CONFIG\_TEE\_NONE 0

314#define XEN\_DOMCTL\_CONFIG\_TEE\_OPTEE 1

315

316struct xen\_arch\_domainconfig {

317 /\* IN/OUT \*/

318 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gic\_version;

319 /\* IN \*/

320 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tee\_type;

321 /\* IN \*/

322 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nr\_spis;

323 /\*

324 \* OUT

325 \* Based on the property clock-frequency in the DT timer node.

326 \* The property may be present when the bootloader/firmware doesn't

327 \* set correctly CNTFRQ which hold the timer frequency.

328 \*

329 \* As it's not possible to trap this register, we have to replicate

330 \* the value in the guest DT.

331 \*

332 \* = 0 => property not present

333 \* > 0 => Value of the property

334 \*

335 \*/

336 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) clock\_frequency;

337};

338#endif /\* CONFIG\_XEN\_DOM0 \*/

339

[ 340](structarch__vcpu__info.md)struct [arch\_vcpu\_info](structarch__vcpu__info.md) {

341};

[ 342](arch-arm_8h.md#a396e630cfa073f7d4e9e983c43c7f7e3)typedef struct [arch\_vcpu\_info](structarch__vcpu__info.md) [arch\_vcpu\_info\_t](arch-arm_8h.md#a396e630cfa073f7d4e9e983c43c7f7e3);

343

[ 344](structarch__shared__info.md)struct [arch\_shared\_info](structarch__shared__info.md) {

345};

[ 346](arch-arm_8h.md#a7b797b4c17d2f2ec9fdf06f5dc69d016)typedef struct [arch\_shared\_info](structarch__shared__info.md) [arch\_shared\_info\_t](arch-arm_8h.md#a7b797b4c17d2f2ec9fdf06f5dc69d016);

[ 347](arch-arm_8h.md#a85d47e7eb51075f257e76067ef337526)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [xen\_callback\_t](arch-arm_8h.md#a85d47e7eb51075f257e76067ef337526);

348

349#endif /\* \_\_ASSEMBLY\_\_ \*/

350

351#ifdef CONFIG\_XEN\_DOM0

352

353/\* PSR bits (CPSR, SPSR) \*/

354#define PSR\_THUMB (1 << 5) /\* Thumb Mode enable \*/

355#define PSR\_FIQ\_MASK (1 << 6) /\* Fast Interrupt mask \*/

356#define PSR\_IRQ\_MASK (1 << 7) /\* Interrupt mask \*/

357#define PSR\_ABT\_MASK (1 << 8) /\* Asynchronous Abort mask \*/

358#define PSR\_BIG\_ENDIAN (1 << 9) /\* arm32: Big Endian Mode \*/

359#define PSR\_DBG\_MASK (1 << 9) /\* arm64: Debug Exception mask \*/

360#define PSR\_IT\_MASK (0x0600fc00) /\* Thumb If-Then Mask \*/

361#define PSR\_JAZELLE (1<<24) /\* Jazelle Mode \*/

362

363/\* 32 bit modes \*/

364#define PSR\_MODE\_USR 0x10

365#define PSR\_MODE\_FIQ 0x11

366#define PSR\_MODE\_IRQ 0x12

367#define PSR\_MODE\_SVC 0x13

368#define PSR\_MODE\_MON 0x16

369#define PSR\_MODE\_ABT 0x17

370#define PSR\_MODE\_HYP 0x1a

371#define PSR\_MODE\_UND 0x1b

372#define PSR\_MODE\_SYS 0x1f

373

374/\* 64 bit modes \*/

375#define PSR\_MODE\_BIT 0x10 /\* Set iff AArch32 \*/

376#define PSR\_MODE\_EL3h 0x0d

377#define PSR\_MODE\_EL3t 0x0c

378#define PSR\_MODE\_EL2h 0x09

379#define PSR\_MODE\_EL2t 0x08

380#define PSR\_MODE\_EL1h 0x05

381#define PSR\_MODE\_EL1t 0x04

382#define PSR\_MODE\_EL0t 0x00

383

384#define PSR\_GUEST32\_INIT (PSR\_ABT\_MASK|PSR\_FIQ\_MASK|PSR\_IRQ\_MASK|PSR\_MODE\_SVC)

385#define PSR\_GUEST64\_INIT (PSR\_ABT\_MASK|PSR\_FIQ\_MASK|PSR\_IRQ\_MASK|PSR\_MODE\_EL1h)

386

387#define SCTLR\_GUEST\_INIT xen\_mk\_ullong(0x00c50078)

388

389/\*

390 \* Virtual machine platform (memory layout, interrupts)

391 \*

392 \* These are defined for consistency between the tools and the

393 \* hypervisor. Guests must not rely on these hardcoded values but

394 \* should instead use the FDT.

395 \*/

396

397/\* Physical Address Space \*/

398

399/\*

400 \* vGIC mappings: Only one set of mapping is used by the guest.

401 \* Therefore they can overlap.

402 \*/

403

404/\* vGIC v2 mappings \*/

405#define GUEST\_GICD\_BASE xen\_mk\_ullong(0x03001000)

406#define GUEST\_GICD\_SIZE xen\_mk\_ullong(0x00001000)

407#define GUEST\_GICC\_BASE xen\_mk\_ullong(0x03002000)

408#define GUEST\_GICC\_SIZE xen\_mk\_ullong(0x00002000)

409

410/\* vGIC v3 mappings \*/

411#define GUEST\_GICV3\_GICD\_BASE xen\_mk\_ullong(0x03001000)

412#define GUEST\_GICV3\_GICD\_SIZE xen\_mk\_ullong(0x00010000)

413

414#define GUEST\_GICV3\_RDIST\_REGIONS 1

415

416#define GUEST\_GICV3\_GICR0\_BASE xen\_mk\_ullong(0x03020000) /\* vCPU0..127 \*/

417#define GUEST\_GICV3\_GICR0\_SIZE xen\_mk\_ullong(0x01000000)

418

419/\* ACPI tables physical address \*/

420#define GUEST\_ACPI\_BASE xen\_mk\_ullong(0x20000000)

421#define GUEST\_ACPI\_SIZE xen\_mk\_ullong(0x02000000)

422

423/\* PL011 mappings \*/

424#define GUEST\_PL011\_BASE xen\_mk\_ullong(0x22000000)

425#define GUEST\_PL011\_SIZE xen\_mk\_ullong(0x00001000)

426

427/\*

428 \* 16MB == 4096 pages reserved for guest to use as a region to map its

429 \* grant table in.

430 \*/

431#define GUEST\_GNTTAB\_BASE xen\_mk\_ullong(0x38000000)

432#define GUEST\_GNTTAB\_SIZE xen\_mk\_ullong(0x01000000)

433

434#define GUEST\_MAGIC\_BASE xen\_mk\_ullong(0x39000000)

435#define GUEST\_MAGIC\_SIZE xen\_mk\_ullong(0x01000000)

436

437#define GUEST\_RAM\_BANKS 2

438

439#define GUEST\_RAM0\_BASE xen\_mk\_ullong(0x40000000) /\* 3GB of low RAM @ 1GB \*/

440#define GUEST\_RAM0\_SIZE xen\_mk\_ullong(0xc0000000)

441

442#define GUEST\_RAM1\_BASE xen\_mk\_ullong(0x0200000000) /\* 1016GB of RAM @ 8GB \*/

443#define GUEST\_RAM1\_SIZE xen\_mk\_ullong(0xfe00000000)

444

445#define GUEST\_RAM\_BASE GUEST\_RAM0\_BASE /\* Lowest RAM address \*/

446/\* Largest amount of actual RAM, not including holes \*/

447#define GUEST\_RAM\_MAX (GUEST\_RAM0\_SIZE + GUEST\_RAM1\_SIZE)

448/\* Suitable for e.g. const uint64\_t ramfoo[] = GUEST\_RAM\_BANK\_FOOS; \*/

449#define GUEST\_RAM\_BANK\_BASES { GUEST\_RAM0\_BASE, GUEST\_RAM1\_BASE }

450#define GUEST\_RAM\_BANK\_SIZES { GUEST\_RAM0\_SIZE, GUEST\_RAM1\_SIZE }

451

452/\* Current supported guest VCPUs \*/

453#define GUEST\_MAX\_VCPUS 128

454

455/\* Interrupts \*/

456#define GUEST\_TIMER\_VIRT\_PPI 27

457#define GUEST\_TIMER\_PHYS\_S\_PPI 29

458#define GUEST\_TIMER\_PHYS\_NS\_PPI 30

459#define GUEST\_EVTCHN\_PPI 31

460

461#define GUEST\_VPL011\_SPI 32

462

463/\* PSCI functions \*/

464#define PSCI\_cpu\_suspend 0

465#define PSCI\_cpu\_off 1

466#define PSCI\_cpu\_on 2

467#define PSCI\_migrate 3

468

469#endif /\* CONFIG\_XEN\_DOM0 \*/

470

471#ifndef \_\_ASSEMBLY\_\_

472/\* Stub definition of PMU structure \*/

[ 473](structxen__pmu__arch.md#a31106705fed367def69e22f254098e89)typedef struct [xen\_pmu\_arch](structxen__pmu__arch.md) { [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dummy](structxen__pmu__arch.md#a31106705fed367def69e22f254098e89); } [xen\_pmu\_arch\_t](arch-arm_8h.md#a9d6716569cd8ef7c541527df22dd767c);

474#endif /\* \_\_ASSEMBLY\_\_ \*/

475

476#endif /\* \_\_XEN\_PUBLIC\_ARCH\_ARM\_H\_\_ \*/

[arch\_vcpu\_info\_t](arch-arm_8h.md#a396e630cfa073f7d4e9e983c43c7f7e3)

struct arch\_vcpu\_info arch\_vcpu\_info\_t

**Definition** arch-arm.h:342

[xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)

uint64\_t xen\_pfn\_t

**Definition** arch-arm.h:204

[arch\_shared\_info\_t](arch-arm_8h.md#a7b797b4c17d2f2ec9fdf06f5dc69d016)

struct arch\_shared\_info arch\_shared\_info\_t

**Definition** arch-arm.h:346

[xen\_callback\_t](arch-arm_8h.md#a85d47e7eb51075f257e76067ef337526)

uint64\_t xen\_callback\_t

**Definition** arch-arm.h:347

[xen\_pmu\_arch\_t](arch-arm_8h.md#a9d6716569cd8ef7c541527df22dd767c)

struct xen\_pmu\_arch xen\_pmu\_arch\_t

[xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)

uint64\_t xen\_ulong\_t

**Definition** arch-arm.h:214

[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)

#define DEFINE\_XEN\_GUEST\_HANDLE(name)

**Definition** arch-arm.h:192

[kernel.h](kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[arch\_shared\_info](structarch__shared__info.md)

**Definition** arch-arm.h:344

[arch\_vcpu\_info](structarch__vcpu__info.md)

**Definition** arch-arm.h:340

[xen\_pmu\_arch](structxen__pmu__arch.md)

**Definition** arch-arm.h:473

[xen\_pmu\_arch::dummy](structxen__pmu__arch.md#a31106705fed367def69e22f254098e89)

uint8\_t dummy

**Definition** arch-arm.h:473

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [arch-arm.h](arch-arm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
