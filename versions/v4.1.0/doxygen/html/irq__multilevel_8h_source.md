---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/irq__multilevel_8h_source.html
original_path: doxygen/html/irq__multilevel_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq\_multilevel.h

[Go to the documentation of this file.](irq__multilevel_8h.md)

1/\*

2 \* Copyright (c) 2023 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11#ifndef ZEPHYR\_INCLUDE\_IRQ\_MULTILEVEL\_H\_

12#define ZEPHYR\_INCLUDE\_IRQ\_MULTILEVEL\_H\_

13

14#ifndef \_ASMLANGUAGE

15#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

16#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23#if defined(CONFIG\_MULTI\_LEVEL\_INTERRUPTS) || defined(\_\_DOXYGEN\_\_)

24

25typedef union \_z\_irq {

26 /\* Zephyr multilevel-encoded IRQ \*/

27 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) irq;

28

29 /\* Interrupt bits \*/

30 struct {

31 /\* First level interrupt bits \*/

32 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) l1: CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS;

33 /\* Second level interrupt bits \*/

34 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) l2: CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS;

35#if defined(CONFIG\_3RD\_LEVEL\_INTERRUPTS) || defined(\_\_DOXYGEN\_\_)

36 /\* Third level interrupt bits \*/

37 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) l3: CONFIG\_3RD\_LEVEL\_INTERRUPT\_BITS;

38#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

39 } bits;

40

41#if defined(CONFIG\_3RD\_LEVEL\_INTERRUPTS) || defined(\_\_DOXYGEN\_\_)

42 /\* Third level IRQ's interrupt controller \*/

43 struct {

44 /\* IRQ of the third level interrupt aggregator \*/

45 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) irq: CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS;

46 } l3\_intc;

47#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

48

49 /\* Second level IRQ's interrupt controller \*/

50 struct {

51 /\* IRQ of the second level interrupt aggregator \*/

52 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) irq: CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS;

53 } l2\_intc;

54} \_z\_irq\_t;

55

[ 56](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e)BUILD\_ASSERT(sizeof(\_z\_irq\_t) == sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)), "Size of `\_z\_irq\_t` must equal to `uint32\_t`");

57

58static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_z\_l1\_irq(\_z\_irq\_t irq)

59{

60 return irq.bits.l1;

61}

62

63static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_z\_l2\_irq(\_z\_irq\_t irq)

64{

65 return irq.bits.l2 - 1;

66}

67

68#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

69static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_z\_l3\_irq(\_z\_irq\_t irq)

70{

71 return irq.bits.l3 - 1;

72}

73#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

74

75static inline unsigned int \_z\_irq\_get\_level(\_z\_irq\_t z\_irq)

76{

77#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

78 if (z\_irq.bits.l3 != 0) {

79 return 3;

80 }

81#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

82

83 if (z\_irq.bits.l2 != 0) {

84 return 2;

85 }

86

87 return 1;

88}

89

[ 98](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)static inline unsigned int [irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)(unsigned int irq)

99{

100 \_z\_irq\_t z\_irq = {

101 .irq = irq,

102 };

103

104 return \_z\_irq\_get\_level(z\_irq);

105}

106

[ 117](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)static inline unsigned int [irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)(unsigned int irq)

118{

119 \_z\_irq\_t z\_irq = {

120 .irq = irq,

121 };

122

123 return \_z\_l2\_irq(z\_irq);

124}

125

[ 133](irq__multilevel_8h.md#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)#define IRQ\_TO\_L2(irq) ((irq + 1) << CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS)

134

[ 147](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)static inline unsigned int [irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)(unsigned int irq)

148{

149 \_z\_irq\_t z\_irq = {

150 .bits = {

151 .l1 = 0,

152 .l2 = irq + 1,

153#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

154 .l3 = 0,

155#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

156 },

157 };

158

159 return z\_irq.irq;

160}

161

[ 172](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)static inline unsigned int [irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)(unsigned int irq)

173{

174 \_z\_irq\_t z\_irq = {

175 .irq = irq,

176 };

177

178 return \_z\_l1\_irq(z\_irq);

179}

180

181#if defined(CONFIG\_3RD\_LEVEL\_INTERRUPTS) || defined(\_\_DOXYGEN\_\_)

[ 193](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)static inline unsigned int [irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)(unsigned int irq)

194{

195 \_z\_irq\_t z\_irq = {

196 .irq = irq,

197 };

198

199 return \_z\_l3\_irq(z\_irq);

200}

201

[ 209](irq__multilevel_8h.md#a1aa1eaa367e7c8baa250900de4eb0daf)#define IRQ\_TO\_L3(irq) \

210 ((irq + 1) << (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS))

211

[ 224](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)static inline unsigned int [irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)(unsigned int irq)

225{

226 \_z\_irq\_t z\_irq = {

227 .bits = {

228 .l1 = 0,

229 .l2 = 0,

230 .l3 = irq + 1,

231 },

232 };

233

234 return z\_irq.irq;

235}

236

[ 247](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)static inline unsigned int [irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)(unsigned int irq)

248{

249 \_z\_irq\_t z\_irq = {

250 .irq = irq,

251 };

252

253 return \_z\_l2\_irq(z\_irq);

254}

255#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

256

[ 265](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)static inline unsigned int [irq\_from\_level](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)(unsigned int irq, unsigned int level)

266{

267 if (level == 1) {

268 return irq;

269 } else if (level == 2) {

270 return [irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)(irq);

271 }

272#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

273 else if (level == 3) {

274 return [irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)(irq);

275 }

276#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

277

278 /\* level is higher than what's supported \*/

279 \_\_ASSERT\_NO\_MSG(false);

280 return irq;

281}

282

[ 291](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)static inline unsigned int [irq\_to\_level](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)(unsigned int irq, unsigned int level)

292{

293 if (level == 1) {

294 return irq;

295 } else if (level == 2) {

296 return [irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)(irq);

297 }

298#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

299 else if (level == 3) {

300 return [irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)(irq);

301 }

302#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

303

304 /\* level is higher than what's supported \*/

305 \_\_ASSERT\_NO\_MSG(false);

306 return irq;

307}

308

[ 317](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)static inline unsigned int [irq\_parent\_level](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)(unsigned int irq, unsigned int level)

318{

319 if (level == 1) {

320 /\* doesn't really make sense, but return anyway \*/

321 return irq;

322 } else if (level == 2) {

323 return [irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)(irq);

324 }

325#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

326 else if (level == 3) {

327 return [irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)(irq);

328 }

329#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

330

331 /\* level is higher than what's supported \*/

332 \_\_ASSERT\_NO\_MSG(false);

333 return irq;

334}

335

[ 343](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)static inline unsigned int [irq\_get\_intc\_irq](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)(unsigned int irq)

344{

345 const unsigned int level = [irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)(irq);

346 \_z\_irq\_t z\_irq = {

347 .irq = irq,

348 };

349

350#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

351 \_\_ASSERT\_NO\_MSG(level <= 3);

352 if (level == 3) {

353 return z\_irq.l3\_intc.irq;

354 }

355#else

356 \_\_ASSERT\_NO\_MSG(level <= 2);

357#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

358

359 if (level == 2) {

360 return z\_irq.l2\_intc.irq;

361 }

362

363 return irq;

364}

365

[ 374](irq__multilevel_8h.md#a4b5e1b801ea817b0432a5c5e74f6bff7)static inline unsigned int [irq\_increment](irq__multilevel_8h.md#a4b5e1b801ea817b0432a5c5e74f6bff7)(unsigned int irq, unsigned int val)

375{

376 \_z\_irq\_t z\_irq = {

377 .irq = irq,

378 };

379

380 if (false) {

381 /\* so that it evaluates the next condition \*/

382#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

383 } else if (z\_irq.bits.l3 != 0) {

384 z\_irq.bits.l3 += val;

385#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

386 } else if (z\_irq.bits.l2 != 0) {

387 z\_irq.bits.l2 += val;

388 } else {

389 z\_irq.bits.l1 += val;

390 }

391

392 return z\_irq.irq;

393}

394

395#endif /\* CONFIG\_MULTI\_LEVEL\_INTERRUPTS \*/

396#ifdef \_\_cplusplus

397}

398#endif

399

400#endif /\* \_ASMLANGUAGE \*/

401#endif /\* ZEPHYR\_INCLUDE\_IRQ\_MULTILEVEL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[irq\_from\_level](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)

static unsigned int irq\_from\_level(unsigned int irq, unsigned int level)

Return the interrupt number for a given level.

**Definition** irq\_multilevel.h:265

[irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)

static unsigned int irq\_to\_level\_3(unsigned int irq)

Converts irq from level 1 to level 3 format.

**Definition** irq\_multilevel.h:224

[irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)

static unsigned int irq\_from\_level\_3(unsigned int irq)

Return the 3rd level interrupt number.

**Definition** irq\_multilevel.h:193

[irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)

static unsigned int irq\_from\_level\_2(unsigned int irq)

Return the 2nd level interrupt number.

**Definition** irq\_multilevel.h:117

[irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)

static unsigned int irq\_get\_level(unsigned int irq)

Return IRQ level This routine returns the interrupt level number of the provided interrupt.

**Definition** irq\_multilevel.h:98

[irq\_increment](irq__multilevel_8h.md#a4b5e1b801ea817b0432a5c5e74f6bff7)

static unsigned int irq\_increment(unsigned int irq, unsigned int val)

Increments the multilevel-encoded irq by val.

**Definition** irq\_multilevel.h:374

[uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e)

Size of \_z\_irq\_t must equal to uint32\_t

**Definition** irq\_multilevel.h:56

[irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)

static unsigned int irq\_to\_level\_2(unsigned int irq)

Converts irq from level 1 to level 2 format.

**Definition** irq\_multilevel.h:147

[irq\_parent\_level](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)

static unsigned int irq\_parent\_level(unsigned int irq, unsigned int level)

Returns the parent IRQ of the given level raw IRQ number.

**Definition** irq\_multilevel.h:317

[irq\_get\_intc\_irq](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)

static unsigned int irq\_get\_intc\_irq(unsigned int irq)

Returns the parent interrupt controller IRQ of the given IRQ number.

**Definition** irq\_multilevel.h:343

[irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)

static unsigned int irq\_parent\_level\_2(unsigned int irq)

Returns the parent IRQ of the level 2 raw IRQ number.

**Definition** irq\_multilevel.h:172

[irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)

static unsigned int irq\_parent\_level\_3(unsigned int irq)

Returns the parent IRQ of the level 3 raw IRQ number.

**Definition** irq\_multilevel.h:247

[irq\_to\_level](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)

static unsigned int irq\_to\_level(unsigned int irq, unsigned int level)

Converts irq from level 1 to a given level.

**Definition** irq\_multilevel.h:291

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_multilevel.h](irq__multilevel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
