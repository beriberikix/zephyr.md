---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/irq__multilevel_8h_source.html
original_path: doxygen/html/irq__multilevel_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

35 /\* Third level interrupt bits \*/

36 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) l3: CONFIG\_3RD\_LEVEL\_INTERRUPT\_BITS;

37 } bits;

38

39 /\* Third level IRQ's interrupt controller \*/

40 struct {

41 /\* IRQ of the third level interrupt aggregator \*/

42 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) irq: CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS;

43 } l3\_intc;

44

45 /\* Second level IRQ's interrupt controller \*/

46 struct {

47 /\* IRQ of the second level interrupt aggregator \*/

48 [uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e) irq: CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS;

49 } l2\_intc;

50} \_z\_irq\_t;

51

[ 52](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e)BUILD\_ASSERT(sizeof(\_z\_irq\_t) == sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)), "Size of `\_z\_irq\_t` must equal to `uint32\_t`");

53

54static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_z\_l1\_irq(\_z\_irq\_t irq)

55{

56 return irq.bits.l1;

57}

58

59static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_z\_l2\_irq(\_z\_irq\_t irq)

60{

61 return irq.bits.l2 - 1;

62}

63

64static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_z\_l3\_irq(\_z\_irq\_t irq)

65{

66 return irq.bits.l3 - 1;

67}

68

69static inline unsigned int \_z\_irq\_get\_level(\_z\_irq\_t z\_irq)

70{

71 if (z\_irq.bits.l3 != 0) {

72 return 3;

73 }

74

75 if (z\_irq.bits.l2 != 0) {

76 return 2;

77 }

78

79 return 1;

80}

81

[ 90](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)static inline unsigned int [irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)(unsigned int irq)

91{

92 \_z\_irq\_t z\_irq = {

93 .irq = irq,

94 };

95

96 return \_z\_irq\_get\_level(z\_irq);

97}

98

[ 109](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)static inline unsigned int [irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)(unsigned int irq)

110{

111 \_z\_irq\_t z\_irq = {

112 .irq = irq,

113 };

114

115 return \_z\_l2\_irq(z\_irq);

116}

117

[ 125](irq__multilevel_8h.md#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)#define IRQ\_TO\_L2(irq) ((irq + 1) << CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS)

126

[ 139](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)static inline unsigned int [irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)(unsigned int irq)

140{

141 \_z\_irq\_t z\_irq = {

142 .bits = {

143 .l1 = 0,

144 .l2 = irq + 1,

145 .l3 = 0,

146 },

147 };

148

149 return z\_irq.irq;

150}

151

[ 162](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)static inline unsigned int [irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)(unsigned int irq)

163{

164 \_z\_irq\_t z\_irq = {

165 .irq = irq,

166 };

167

168 return \_z\_l1\_irq(z\_irq);

169}

170

[ 182](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)static inline unsigned int [irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)(unsigned int irq)

183{

184 \_z\_irq\_t z\_irq = {

185 .irq = irq,

186 };

187

188 return \_z\_l3\_irq(z\_irq);

189}

190

[ 198](irq__multilevel_8h.md#a1aa1eaa367e7c8baa250900de4eb0daf)#define IRQ\_TO\_L3(irq) \

199 ((irq + 1) << (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS))

200

[ 213](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)static inline unsigned int [irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)(unsigned int irq)

214{

215 \_z\_irq\_t z\_irq = {

216 .bits = {

217 .l1 = 0,

218 .l2 = 0,

219 .l3 = irq + 1,

220 },

221 };

222

223 return z\_irq.irq;

224}

225

[ 236](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)static inline unsigned int [irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)(unsigned int irq)

237{

238 \_z\_irq\_t z\_irq = {

239 .irq = irq,

240 };

241

242 return \_z\_l2\_irq(z\_irq);

243}

244

[ 253](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)static inline unsigned int [irq\_from\_level](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)(unsigned int irq, unsigned int level)

254{

255 if (level == 1) {

256 return irq;

257 } else if (level == 2) {

258 return [irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)(irq);

259 } else if (level == 3) {

260 return [irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)(irq);

261 }

262

263 /\* level is higher than 3 \*/

264 \_\_ASSERT\_NO\_MSG(false);

265 return irq;

266}

267

[ 276](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)static inline unsigned int [irq\_to\_level](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)(unsigned int irq, unsigned int level)

277{

278 if (level == 1) {

279 return irq;

280 } else if (level == 2) {

281 return [irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)(irq);

282 } else if (level == 3) {

283 return [irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)(irq);

284 }

285

286 /\* level is higher than 3 \*/

287 \_\_ASSERT\_NO\_MSG(false);

288 return irq;

289}

290

[ 299](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)static inline unsigned int [irq\_parent\_level](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)(unsigned int irq, unsigned int level)

300{

301 if (level == 1) {

302 /\* doesn't really make sense, but return anyway \*/

303 return irq;

304 } else if (level == 2) {

305 return [irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)(irq);

306 } else if (level == 3) {

307 return [irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)(irq);

308 }

309

310 /\* level is higher than 3 \*/

311 \_\_ASSERT\_NO\_MSG(false);

312 return irq;

313}

314

[ 322](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)static inline unsigned int [irq\_get\_intc\_irq](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)(unsigned int irq)

323{

324 const unsigned int level = [irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)(irq);

325

326 \_\_ASSERT\_NO\_MSG(level <= 3);

327 \_z\_irq\_t z\_irq = {

328 .irq = irq,

329 };

330

331 if (level == 3) {

332 return z\_irq.l3\_intc.irq;

333 } else if (level == 2) {

334 return z\_irq.l2\_intc.irq;

335 } else {

336 return irq;

337 }

338}

339

[ 348](irq__multilevel_8h.md#a4b5e1b801ea817b0432a5c5e74f6bff7)static inline unsigned int [irq\_increment](irq__multilevel_8h.md#a4b5e1b801ea817b0432a5c5e74f6bff7)(unsigned int irq, unsigned int val)

349{

350 \_z\_irq\_t z\_irq = {

351 .irq = irq,

352 };

353

354 if (z\_irq.bits.l3 != 0) {

355 z\_irq.bits.l3 += val;

356 } else if (z\_irq.bits.l2 != 0) {

357 z\_irq.bits.l2 += val;

358 } else {

359 z\_irq.bits.l1 += val;

360 }

361

362 return z\_irq.irq;

363}

364

365#endif /\* CONFIG\_MULTI\_LEVEL\_INTERRUPTS \*/

366#ifdef \_\_cplusplus

367}

368#endif

369

370#endif /\* \_ASMLANGUAGE \*/

371#endif /\* ZEPHYR\_INCLUDE\_IRQ\_MULTILEVEL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[irq\_from\_level](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)

static unsigned int irq\_from\_level(unsigned int irq, unsigned int level)

Return the interrupt number for a given level.

**Definition** irq\_multilevel.h:253

[irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)

static unsigned int irq\_to\_level\_3(unsigned int irq)

Converts irq from level 1 to level 3 format.

**Definition** irq\_multilevel.h:213

[irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)

static unsigned int irq\_from\_level\_3(unsigned int irq)

Return the 3rd level interrupt number.

**Definition** irq\_multilevel.h:182

[irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)

static unsigned int irq\_from\_level\_2(unsigned int irq)

Return the 2nd level interrupt number.

**Definition** irq\_multilevel.h:109

[irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)

static unsigned int irq\_get\_level(unsigned int irq)

Return IRQ level This routine returns the interrupt level number of the provided interrupt.

**Definition** irq\_multilevel.h:90

[irq\_increment](irq__multilevel_8h.md#a4b5e1b801ea817b0432a5c5e74f6bff7)

static unsigned int irq\_increment(unsigned int irq, unsigned int val)

Increments the multilevel-encoded irq by val.

**Definition** irq\_multilevel.h:348

[uint32\_t](irq__multilevel_8h.md#a6b77d32212a1febe3b9e3366eb84580e)

Size of \_z\_irq\_t must equal to uint32\_t

**Definition** irq\_multilevel.h:52

[irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)

static unsigned int irq\_to\_level\_2(unsigned int irq)

Converts irq from level 1 to level 2 format.

**Definition** irq\_multilevel.h:139

[irq\_parent\_level](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)

static unsigned int irq\_parent\_level(unsigned int irq, unsigned int level)

Returns the parent IRQ of the given level raw IRQ number.

**Definition** irq\_multilevel.h:299

[irq\_get\_intc\_irq](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)

static unsigned int irq\_get\_intc\_irq(unsigned int irq)

Returns the parent interrupt controller IRQ of the given IRQ number.

**Definition** irq\_multilevel.h:322

[irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)

static unsigned int irq\_parent\_level\_2(unsigned int irq)

Returns the parent IRQ of the level 2 raw IRQ number.

**Definition** irq\_multilevel.h:162

[irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)

static unsigned int irq\_parent\_level\_3(unsigned int irq)

Returns the parent IRQ of the level 3 raw IRQ number.

**Definition** irq\_multilevel.h:236

[irq\_to\_level](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)

static unsigned int irq\_to\_level(unsigned int irq, unsigned int level)

Converts irq from level 1 to a given level.

**Definition** irq\_multilevel.h:276

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_multilevel.h](irq__multilevel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
