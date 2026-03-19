---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sw__isr__table_8h_source.html
original_path: doxygen/html/sw__isr__table_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sw\_isr\_table.h

[Go to the documentation of this file.](sw__isr__table_8h.md)

1/\*

2 \* Copyright (c) 2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_SW\_ISR\_TABLE\_H\_

15#define ZEPHYR\_INCLUDE\_SW\_ISR\_TABLE\_H\_

16

17#if !defined(\_ASMLANGUAGE)

18#include <[zephyr/device.h](device_8h.md)>

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21#include <[zephyr/toolchain.h](toolchain_8h.md)>

22#include <[zephyr/sys/util.h](sys_2util_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

28/\* Default vector for the IRQ vector table \*/

29void \_isr\_wrapper(void);

30

31/\* Spurious interrupt handler. Throws an error if called \*/

32void z\_irq\_spurious(const void \*unused);

33

34/\*

35 \* Note the order: arg first, then ISR. This allows a table entry to be

36 \* loaded arg -> r0, isr -> r3 in \_isr\_wrapper with one ldmia instruction,

37 \* on ARM Cortex-M (Thumb2).

38 \*/

39struct \_isr\_table\_entry {

40 const void \*arg;

41 void (\*isr)(const void \*);

42};

43

44/\* The software ISR table itself, an array of these structures indexed by the

45 \* irq line

46 \*/

47extern struct \_isr\_table\_entry \_sw\_isr\_table[];

48

49struct \_irq\_parent\_entry {

50 const struct device \*dev;

51 unsigned int level;

52 unsigned int irq;

53 unsigned int offset;

54};

55

59

60/\* Mapping between aggregator level to order \*/

61#define Z\_STR\_L2 2ND

62#define Z\_STR\_L3 3RD

71#define Z\_SW\_ISR\_TBL\_KCONFIG\_BY\_ALVL(l) CONCAT(CONFIG\_, CONCAT(Z\_STR\_L, l), \_LVL\_ISR\_TBL\_OFFSET)

72

76

[ 85](sw__isr__table_8h.md#a9b130c84dbe718bcb89f7a83eb3a1d04)#define INTC\_BASE\_ISR\_TBL\_OFFSET(node\_id) \

86 Z\_SW\_ISR\_TBL\_KCONFIG\_BY\_ALVL(DT\_INTC\_GET\_AGGREGATOR\_LEVEL(node\_id))

87

[ 95](sw__isr__table_8h.md#a810f9314f0a6d8a902593d0521660176)#define INTC\_INST\_ISR\_TBL\_OFFSET(inst) \

96 (INTC\_BASE\_ISR\_TBL\_OFFSET(DT\_DRV\_INST(inst)) + (inst \* CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR))

97

[ 108](sw__isr__table_8h.md#a433c2b13315bd1fa93057a48b3b30122)#define INTC\_CHILD\_ISR\_TBL\_OFFSET(node\_id) \

109 (INTC\_BASE\_ISR\_TBL\_OFFSET(node\_id) + \

110 (DT\_NODE\_CHILD\_IDX(node\_id) \* CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR))

111

[ 121](sw__isr__table_8h.md#aaa922e8bad35d8f5a25d889cd14fd915)#define IRQ\_PARENT\_ENTRY\_DEFINE(\_name, \_dev, \_irq, \_offset, \_level) \

122 static const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(intc\_table, \_irq\_parent\_entry, \_name) = { \

123 .dev = \_dev, \

124 .level = \_level, \

125 .irq = \_irq, \

126 .offset = \_offset, \

127 }

128

129/\*

130 \* Data structure created in a special binary .intlist section for each

131 \* configured interrupt. gen\_irq\_tables.py pulls this out of the binary and

132 \* uses it to create the IRQ vector table and the \_sw\_isr\_table.

133 \*

134 \* More discussion in include/linker/intlist.ld

135 \*

136 \* This is a version used when CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION is disabled.

137 \* See \_isr\_list\_sname used otherwise.

138 \*/

139struct \_isr\_list {

141 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) irq;

143 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

145 void \*func;

147 const void \*param;

148};

149

150/\*

151 \* Data structure created in a special binary .intlist section for each

152 \* configured interrupt. gen\_isr\_tables.py pulls this out of the binary and

153 \* uses it to create linker script chunks that would place interrupt table entries

154 \* in the right place in the memory.

155 \*

156 \* This is a version used when CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION is enabled.

157 \* See \_isr\_list used otherwise.

158 \*/

159struct \_isr\_list\_sname {

161 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) irq;

163 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) flags;

165 const char sname[];

166};

167

168#ifdef CONFIG\_SHARED\_INTERRUPTS

169struct z\_shared\_isr\_table\_entry {

170 struct \_isr\_table\_entry clients[CONFIG\_SHARED\_IRQ\_MAX\_NUM\_CLIENTS];

171 size\_t client\_num;

172};

173

174void z\_shared\_isr(const void \*data);

175

176extern struct z\_shared\_isr\_table\_entry z\_shared\_sw\_isr\_table[];

177#endif /\* CONFIG\_SHARED\_INTERRUPTS \*/

178

[ 180](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19)#define ISR\_FLAG\_DIRECT BIT(0)

181

182#define \_MK\_ISR\_NAME(x, y) \_\_MK\_ISR\_NAME(x, y)

183#define \_\_MK\_ISR\_NAME(x, y) \_\_isr\_ ## x ## \_irq\_ ## y

184

185

186#if defined(CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION)

187

188#define \_MK\_ISR\_ELEMENT\_NAME(func, id) \_\_MK\_ISR\_ELEMENT\_NAME(func, id)

189#define \_\_MK\_ISR\_ELEMENT\_NAME(func, id) \_\_isr\_table\_entry\_ ## func ## \_irq\_ ## id

190

191#define \_MK\_IRQ\_ELEMENT\_NAME(func, id) \_\_MK\_ISR\_ELEMENT\_NAME(func, id)

192#define \_\_MK\_IRQ\_ELEMENT\_NAME(func, id) \_\_irq\_table\_entry\_ ## func ## \_irq\_ ## id

193

194#define \_MK\_ISR\_SECTION\_NAME(prefix, file, counter) \

195 "." Z\_STRINGIFY(prefix)"."file"." Z\_STRINGIFY(counter)

196

197#define \_MK\_ISR\_ELEMENT\_SECTION(counter) \_MK\_ISR\_SECTION\_NAME(irq, \_\_FILE\_\_, counter)

198#define \_MK\_IRQ\_ELEMENT\_SECTION(counter) \_MK\_ISR\_SECTION\_NAME(isr, \_\_FILE\_\_, counter)

199

200/\* Separated macro to create ISR table entry only.

201 \* Used by Z\_ISR\_DECLARE and ISR tables generation script.

202 \*/

203#define \_Z\_ISR\_TABLE\_ENTRY(irq, func, param, sect) \

204 static Z\_DECL\_ALIGN(struct \_isr\_table\_entry) \

205 \_\_attribute\_\_((section(sect))) \

206 \_\_used \_MK\_ISR\_ELEMENT\_NAME(func, \_\_COUNTER\_\_) = { \

207 .arg = (const void \*)(param), \

208 .isr = (void (\*)(const void \*))(void \*)(func) \

209 }

210

211#define Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter) \

212 \_Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter)

213

214#define \_Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter) \

215 \_Z\_ISR\_TABLE\_ENTRY(irq, func, param, \_MK\_ISR\_ELEMENT\_SECTION(counter)); \

216 static struct \_isr\_list\_sname Z\_GENERIC\_SECTION(.intList) \

217 \_\_used \_MK\_ISR\_NAME(func, counter) = \

218 {irq, flags, \_MK\_ISR\_ELEMENT\_SECTION(counter)}

219

220/\* Create an entry for \_isr\_table to be then placed by the linker.

221 \* An instance of struct \_isr\_list which gets put in the .intList

222 \* section is created with the name of the section where \_isr\_table entry is placed to be then

223 \* used by isr generation script to create linker script chunk.

224 \*/

225#define Z\_ISR\_DECLARE(irq, flags, func, param) \

226 BUILD\_ASSERT(((flags) & ISR\_FLAG\_DIRECT) == 0, "Use Z\_ISR\_DECLARE\_DIRECT macro"); \

227 Z\_ISR\_DECLARE\_C(irq, flags, func, param, \_\_COUNTER\_\_)

228

229

230/\* Separated macro to create ISR Direct table entry only.

231 \* Used by Z\_ISR\_DECLARE\_DIRECT and ISR tables generation script.

232 \*/

233#define \_Z\_ISR\_DIRECT\_TABLE\_ENTRY(irq, func, sect) \

234 COND\_CODE\_1(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_ADDRESS, ( \

235 static Z\_DECL\_ALIGN(uintptr\_t) \

236 \_\_attribute\_\_((section(sect))) \

237 \_\_used \_MK\_IRQ\_ELEMENT\_NAME(func, \_\_COUNTER\_\_) = ((uintptr\_t)(func)); \

238 ), ( \

239 static void \_\_attribute\_\_((section(sect))) \_\_attribute\_\_((naked)) \

240 \_\_used \_MK\_IRQ\_ELEMENT\_NAME(func, \_\_COUNTER\_\_)(void) { \

241 \_\_asm(ARCH\_IRQ\_VECTOR\_JUMP\_CODE(func)); \

242 } \

243 ))

244

245#define Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter) \

246 \_Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter)

247

248#define \_Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter) \

249 \_Z\_ISR\_DIRECT\_TABLE\_ENTRY(irq, func, \_MK\_IRQ\_ELEMENT\_SECTION(counter)); \

250 static struct \_isr\_list\_sname Z\_GENERIC\_SECTION(.intList) \

251 \_\_used \_MK\_ISR\_NAME(func, counter) = { \

252 irq, \

253 ISR\_FLAG\_DIRECT | (flags), \

254 \_MK\_IRQ\_ELEMENT\_SECTION(counter)}

255

256/\* Create an entry to irq table and place it in specific section which name is then placed

257 \* in an instance of struct \_isr\_list to be then used by the isr generation script to create

258 \* the linker script chunks.

259 \*/

260#define Z\_ISR\_DECLARE\_DIRECT(irq, flags, func) \

261 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_ADDRESS) || \

262 IS\_ENABLED(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_CODE), \

263 "CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_{ADDRESS,CODE} not set"); \

264 Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, \_\_COUNTER\_\_)

265

266

267#else /\* defined(CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION) \*/

268

269/\* Create an instance of struct \_isr\_list which gets put in the .intList

270 \* section. This gets consumed by gen\_isr\_tables.py which creates the vector

271 \* and/or SW ISR tables.

272 \*/

273#define Z\_ISR\_DECLARE(irq, flags, func, param) \

274 static Z\_DECL\_ALIGN(struct \_isr\_list) Z\_GENERIC\_SECTION(.intList) \

275 \_\_used \_MK\_ISR\_NAME(func, \_\_COUNTER\_\_) = \

276 {irq, flags, (void \*)&func, (const void \*)param}

277

278/\* The version of the Z\_ISR\_DECLARE that should be used for direct ISR declaration.

279 \* It is here for the API match the version with CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION enabled.

280 \*/

281#define Z\_ISR\_DECLARE\_DIRECT(irq, flags, func) \

282 Z\_ISR\_DECLARE(irq, ISR\_FLAG\_DIRECT | (flags), func, NULL)

283

284#endif

285

[ 286](sw__isr__table_8h.md#af36594d0586be77420bfe6eaf9f96a2c)#define IRQ\_TABLE\_SIZE (CONFIG\_NUM\_IRQS - CONFIG\_GEN\_IRQ\_START\_VECTOR)

287

288#ifdef CONFIG\_DYNAMIC\_INTERRUPTS

289void z\_isr\_install(unsigned int irq, void (\*routine)(const void \*),

290 const void \*param);

291

292#ifdef CONFIG\_SHARED\_INTERRUPTS

293int z\_isr\_uninstall(unsigned int irq, void (\*routine)(const void \*),

294 const void \*param);

295#endif /\* CONFIG\_SHARED\_INTERRUPTS \*/

296#endif

297

298#ifdef \_\_cplusplus

299}

300#endif

301

302#endif /\* \_ASMLANGUAGE \*/

303

304#endif /\* ZEPHYR\_INCLUDE\_SW\_ISR\_TABLE\_H\_ \*/

[device.h](device_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sw\_isr\_table.h](sw__isr__table_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
