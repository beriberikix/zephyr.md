---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/irq__multilevel_8h_source.html
original_path: doxygen/html/irq__multilevel_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

[ 32](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)static inline unsigned int [irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)(unsigned int irq)

33{

34 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask2 = [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS) <<

35 CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS;

36 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask3 = [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_3RD\_LEVEL\_INTERRUPT\_BITS) <<

37 (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS);

38

39 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_3RD\_LEVEL\_INTERRUPTS) && (irq & mask3) != 0) {

40 return 3;

41 }

42

43 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_2ND\_LEVEL\_INTERRUPTS) && (irq & mask2) != 0) {

44 return 2;

45 }

46

47 return 1;

48}

49

[ 60](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)static inline unsigned int [irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)(unsigned int irq)

61{

62 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_3RD\_LEVEL\_INTERRUPTS)) {

63 return ((irq >> CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS) &

64 [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS)) - 1;

65 } else {

66 return (irq >> CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS) - 1;

67 }

68}

69

[ 77](irq__multilevel_8h.md#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)#define IRQ\_TO\_L2(irq) ((irq + 1) << CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS)

78

[ 91](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)static inline unsigned int [irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)(unsigned int irq)

92{

93 return [IRQ\_TO\_L2](irq__multilevel_8h.md#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)(irq);

94}

95

[ 106](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)static inline unsigned int [irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)(unsigned int irq)

107{

108 return irq & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS);

109}

110

[ 122](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)static inline unsigned int [irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)(unsigned int irq)

123{

124 return (irq >> (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS)) - 1;

125}

126

[ 134](irq__multilevel_8h.md#a1aa1eaa367e7c8baa250900de4eb0daf)#define IRQ\_TO\_L3(irq) \

135 ((irq + 1) << (CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS + CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS))

136

[ 149](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)static inline unsigned int [irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)(unsigned int irq)

150{

151 return [IRQ\_TO\_L3](irq__multilevel_8h.md#a1aa1eaa367e7c8baa250900de4eb0daf)(irq);

152}

153

[ 164](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)static inline unsigned int [irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)(unsigned int irq)

165{

166 return (irq >> CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS) &

167 [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS);

168}

169

[ 178](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)static inline unsigned int [irq\_from\_level](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)(unsigned int irq, unsigned int level)

179{

180 if (level == 1) {

181 return irq;

182 } else if (level == 2) {

183 return [irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)(irq);

184 } else if (level == 3) {

185 return [irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)(irq);

186 }

187

188 /\* level is higher than 3 \*/

189 \_\_ASSERT\_NO\_MSG(false);

190 return irq;

191}

192

[ 201](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)static inline unsigned int [irq\_to\_level](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)(unsigned int irq, unsigned int level)

202{

203 if (level == 1) {

204 return irq;

205 } else if (level == 2) {

206 return [irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)(irq);

207 } else if (level == 3) {

208 return [irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)(irq);

209 }

210

211 /\* level is higher than 3 \*/

212 \_\_ASSERT\_NO\_MSG(false);

213 return irq;

214}

215

[ 224](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)static inline unsigned int [irq\_parent\_level](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)(unsigned int irq, unsigned int level)

225{

226 if (level == 1) {

227 /\* doesn't really make sense, but return anyway \*/

228 return irq;

229 } else if (level == 2) {

230 return [irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)(irq);

231 } else if (level == 3) {

232 return [irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)(irq);

233 }

234

235 /\* level is higher than 3 \*/

236 \_\_ASSERT\_NO\_MSG(false);

237 return irq;

238}

239

[ 247](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)static inline unsigned int [irq\_get\_intc\_irq](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)(unsigned int irq)

248{

249 const unsigned int level = [irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)(irq);

250

251 \_\_ASSERT\_NO\_MSG(level > 1 && level <= 3);

252

253 return irq & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(CONFIG\_1ST\_LEVEL\_INTERRUPT\_BITS +

254 (level == 3 ? CONFIG\_2ND\_LEVEL\_INTERRUPT\_BITS : 0));

255}

256

257#endif /\* CONFIG\_MULTI\_LEVEL\_INTERRUPTS \*/

258#ifdef \_\_cplusplus

259}

260#endif

261

262#endif /\* \_ASMLANGUAGE \*/

263#endif /\* ZEPHYR\_INCLUDE\_IRQ\_MULTILEVEL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:68

[types.h](include_2zephyr_2types_8h.md)

[irq\_from\_level](irq__multilevel_8h.md#a07a9a77e0d09a05f81d73da2d3f3388a)

static unsigned int irq\_from\_level(unsigned int irq, unsigned int level)

Return the interrupt number for a given level.

**Definition** irq\_multilevel.h:178

[IRQ\_TO\_L3](irq__multilevel_8h.md#a1aa1eaa367e7c8baa250900de4eb0daf)

#define IRQ\_TO\_L3(irq)

Preprocessor macro to convert irq from level 1 to level 3 format.

**Definition** irq\_multilevel.h:134

[irq\_to\_level\_3](irq__multilevel_8h.md#a3b8df71a84ac972b89eb37684dcc7072)

static unsigned int irq\_to\_level\_3(unsigned int irq)

Converts irq from level 1 to level 3 format.

**Definition** irq\_multilevel.h:149

[irq\_from\_level\_3](irq__multilevel_8h.md#a401e5249731398fdec30f8e51437f2fb)

static unsigned int irq\_from\_level\_3(unsigned int irq)

Return the 3rd level interrupt number.

**Definition** irq\_multilevel.h:122

[irq\_from\_level\_2](irq__multilevel_8h.md#a4022e57572b3bffb694bf25eef090cec)

static unsigned int irq\_from\_level\_2(unsigned int irq)

Return the 2nd level interrupt number.

**Definition** irq\_multilevel.h:60

[irq\_get\_level](irq__multilevel_8h.md#a45afd68784e71521606e489d965b1c13)

static unsigned int irq\_get\_level(unsigned int irq)

Return IRQ level This routine returns the interrupt level number of the provided interrupt.

**Definition** irq\_multilevel.h:32

[irq\_to\_level\_2](irq__multilevel_8h.md#a79eb4433215c271fa61b9352855f93ca)

static unsigned int irq\_to\_level\_2(unsigned int irq)

Converts irq from level 1 to level 2 format.

**Definition** irq\_multilevel.h:91

[irq\_parent\_level](irq__multilevel_8h.md#a8f22ab28ed1da7312fcd716eea59e400)

static unsigned int irq\_parent\_level(unsigned int irq, unsigned int level)

Returns the parent IRQ of the given level raw IRQ number.

**Definition** irq\_multilevel.h:224

[IRQ\_TO\_L2](irq__multilevel_8h.md#a9a94c2cecb8c8d3394c1ff5ed3cc4db3)

#define IRQ\_TO\_L2(irq)

Preprocessor macro to convert irq from level 1 to level 2 format.

**Definition** irq\_multilevel.h:77

[irq\_get\_intc\_irq](irq__multilevel_8h.md#a9fb52147e972ee981050b47758dca73d)

static unsigned int irq\_get\_intc\_irq(unsigned int irq)

Returns the parent interrupt controller IRQ of the given IRQ number.

**Definition** irq\_multilevel.h:247

[irq\_parent\_level\_2](irq__multilevel_8h.md#ab1a4c5a542e4ad472dba609829c34bc4)

static unsigned int irq\_parent\_level\_2(unsigned int irq)

Returns the parent IRQ of the level 2 raw IRQ number.

**Definition** irq\_multilevel.h:106

[irq\_parent\_level\_3](irq__multilevel_8h.md#ae11c8cb9a832a5a8f514a52a12f133c4)

static unsigned int irq\_parent\_level\_3(unsigned int irq)

Returns the parent IRQ of the level 3 raw IRQ number.

**Definition** irq\_multilevel.h:164

[irq\_to\_level](irq__multilevel_8h.md#ae91094e0be680803d7bd79739029e390)

static unsigned int irq\_to\_level(unsigned int irq, unsigned int level)

Converts irq from level 1 to a given level.

**Definition** irq\_multilevel.h:201

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [irq\_multilevel.h](irq__multilevel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
