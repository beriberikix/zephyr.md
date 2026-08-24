---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/sw__isr__table_8h_source.html
original_path: doxygen/html/sw__isr__table_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

47extern

48#ifndef CONFIG\_DYNAMIC\_INTERRUPTS

49const

50#endif

51struct \_isr\_table\_entry \_sw\_isr\_table[];

52

53struct \_irq\_parent\_entry {

54 const struct device \*dev;

55 unsigned int level;

56 unsigned int irq;

57 unsigned int offset;

58};

59

63

64/\* Mapping between aggregator level to order \*/

65#define Z\_STR\_L2 2ND

66#define Z\_STR\_L3 3RD

75#define Z\_SW\_ISR\_TBL\_KCONFIG\_BY\_ALVL(l) CONCAT(CONFIG\_, CONCAT(Z\_STR\_L, l), \_LVL\_ISR\_TBL\_OFFSET)

76

80

[ 89](sw__isr__table_8h.md#a9b130c84dbe718bcb89f7a83eb3a1d04)#define INTC\_BASE\_ISR\_TBL\_OFFSET(node\_id) \

90 Z\_SW\_ISR\_TBL\_KCONFIG\_BY\_ALVL(DT\_INTC\_GET\_AGGREGATOR\_LEVEL(node\_id))

91

[ 99](sw__isr__table_8h.md#a810f9314f0a6d8a902593d0521660176)#define INTC\_INST\_ISR\_TBL\_OFFSET(inst) \

100 (INTC\_BASE\_ISR\_TBL\_OFFSET(DT\_DRV\_INST(inst)) + (inst \* CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR))

101

[ 112](sw__isr__table_8h.md#a433c2b13315bd1fa93057a48b3b30122)#define INTC\_CHILD\_ISR\_TBL\_OFFSET(node\_id) \

113 (INTC\_BASE\_ISR\_TBL\_OFFSET(node\_id) + \

114 (DT\_NODE\_CHILD\_IDX(node\_id) \* CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR))

115

[ 125](sw__isr__table_8h.md#aaa922e8bad35d8f5a25d889cd14fd915)#define IRQ\_PARENT\_ENTRY\_DEFINE(\_name, \_dev, \_irq, \_offset, \_level) \

126 static const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(intc\_table, \_irq\_parent\_entry, \_name) = { \

127 .dev = \_dev, \

128 .level = \_level, \

129 .irq = \_irq, \

130 .offset = \_offset, \

131 }

132

133/\*

134 \* Data structure created in a special binary .intlist section for each

135 \* configured interrupt. gen\_irq\_tables.py pulls this out of the binary and

136 \* uses it to create the IRQ vector table and the \_sw\_isr\_table.

137 \*

138 \* More discussion in include/linker/intlist.ld

139 \*

140 \* This is a version used when CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION is disabled.

141 \* See \_isr\_list\_sname used otherwise.

142 \*/

143struct \_isr\_list {

145 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) irq;

147 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

149 void \*func;

151 const void \*param;

152};

153

154/\*

155 \* Data structure created in a special binary .intlist section for each

156 \* configured interrupt. gen\_isr\_tables.py pulls this out of the binary and

157 \* uses it to create linker script chunks that would place interrupt table entries

158 \* in the right place in the memory.

159 \*

160 \* This is a version used when CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION is enabled.

161 \* See \_isr\_list used otherwise.

162 \*/

163struct \_isr\_list\_sname {

165 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) irq;

167 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) flags;

169 const char sname[];

170};

171

172#ifdef CONFIG\_SHARED\_INTERRUPTS

173struct z\_shared\_isr\_table\_entry {

174 struct \_isr\_table\_entry clients[CONFIG\_SHARED\_IRQ\_MAX\_NUM\_CLIENTS];

175 size\_t client\_num;

176};

177

178void z\_shared\_isr(const void \*data);

179

180extern

181#ifndef CONFIG\_DYNAMIC\_INTERRUPTS

182const

183#endif

184struct z\_shared\_isr\_table\_entry z\_shared\_sw\_isr\_table[];

185#endif /\* CONFIG\_SHARED\_INTERRUPTS \*/

186

[ 188](sw__isr__table_8h.md#a1376eec61303fcd20e7656175ddbaf19)#define ISR\_FLAG\_DIRECT BIT(0)

189

190#define \_MK\_ISR\_NAME(x, y) \_\_MK\_ISR\_NAME(x, y)

191#define \_\_MK\_ISR\_NAME(x, y) \_\_isr\_ ## x ## \_irq\_ ## y

192

193

194#if defined(CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION)

195

196#define \_MK\_ISR\_ELEMENT\_NAME(func, id) \_\_MK\_ISR\_ELEMENT\_NAME(func, id)

197#define \_\_MK\_ISR\_ELEMENT\_NAME(func, id) \_\_isr\_table\_entry\_ ## func ## \_irq\_ ## id

198

199#define \_MK\_IRQ\_ELEMENT\_NAME(func, id) \_\_MK\_ISR\_ELEMENT\_NAME(func, id)

200#define \_\_MK\_IRQ\_ELEMENT\_NAME(func, id) \_\_irq\_table\_entry\_ ## func ## \_irq\_ ## id

201

202#define \_MK\_ISR\_SECTION\_NAME(prefix, file, counter) \

203 "." Z\_STRINGIFY(prefix) "." file "." Z\_STRINGIFY(counter)

204

205#define \_MK\_ISR\_ELEMENT\_SECTION(counter) \_MK\_ISR\_SECTION\_NAME(irq, \_\_FILE\_\_, counter)

206#define \_MK\_IRQ\_ELEMENT\_SECTION(counter) \_MK\_ISR\_SECTION\_NAME(isr, \_\_FILE\_\_, counter)

207

208/\* Separated macro to create ISR table entry only.

209 \* Used by Z\_ISR\_DECLARE and ISR tables generation script.

210 \*/

211#define \_Z\_ISR\_TABLE\_ENTRY(irq, func, param, sect) \

212 static Z\_DECL\_ALIGN(struct \_isr\_table\_entry) \

213 \_\_attribute\_\_((section(sect))) \

214 \_\_used \_MK\_ISR\_ELEMENT\_NAME(func, \_\_COUNTER\_\_) = { \

215 .arg = (const void \*)(param), \

216 .isr = (void (\*)(const void \*))(void \*)(func) \

217 }

218

219#define Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter) \

220 \_Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter)

221

222#define \_Z\_ISR\_DECLARE\_C(irq, flags, func, param, counter) \

223 \_Z\_ISR\_TABLE\_ENTRY(irq, func, param, \_MK\_ISR\_ELEMENT\_SECTION(counter)); \

224 static Z\_DECL\_ALIGN(struct \_isr\_list\_sname) Z\_GENERIC\_SECTION(.intList) \_\_used \

225 \_MK\_ISR\_NAME(func, counter) = {irq, flags, {\_MK\_ISR\_ELEMENT\_SECTION(counter)}}

226

227/\* Create an entry for \_isr\_table to be then placed by the linker.

228 \* An instance of struct \_isr\_list which gets put in the .intList

229 \* section is created with the name of the section where \_isr\_table entry is placed to be then

230 \* used by isr generation script to create linker script chunk.

231 \*/

232#define Z\_ISR\_DECLARE(irq, flags, func, param) \

233 BUILD\_ASSERT(((flags) & ISR\_FLAG\_DIRECT) == 0, "Use Z\_ISR\_DECLARE\_DIRECT macro"); \

234 Z\_ISR\_DECLARE\_C(irq, flags, func, param, \_\_COUNTER\_\_)

235

236

237/\* Separated macro to create ISR Direct table entry only.

238 \* Used by Z\_ISR\_DECLARE\_DIRECT and ISR tables generation script.

239 \*/

240#define \_Z\_ISR\_DIRECT\_TABLE\_ENTRY(irq, func, sect) \

241 COND\_CODE\_1(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_ADDRESS, ( \

242 static Z\_DECL\_ALIGN(uintptr\_t) \

243 \_\_attribute\_\_((section(sect))) \

244 \_\_used \_MK\_IRQ\_ELEMENT\_NAME(func, \_\_COUNTER\_\_) = ((uintptr\_t)(func)); \

245 ), ( \

246 void \_\_attribute\_\_((section(sect))) \_\_attribute\_\_((naked)) \

247 /\* clang-format off \*/ \

248 \_\_used \_MK\_IRQ\_ELEMENT\_NAME(func, \_\_COUNTER\_\_) (void) { \

249 \_\_asm(ARCH\_IRQ\_VECTOR\_JUMP\_CODE(func)); \

250 } \

251 /\* clang-format on \*/ \

252 ))

253

254#define Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter) \

255 \_Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter)

256

257#define \_Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, counter) \

258 \_Z\_ISR\_DIRECT\_TABLE\_ENTRY(irq, func, \_MK\_IRQ\_ELEMENT\_SECTION(counter)); \

259 static Z\_DECL\_ALIGN(struct \_isr\_list\_sname) Z\_GENERIC\_SECTION(.intList) \

260 \_\_used \_MK\_ISR\_NAME(func, counter) = { \

261 irq, \

262 ISR\_FLAG\_DIRECT | (flags), \

263 \_MK\_IRQ\_ELEMENT\_SECTION(counter)}

264

265/\* Create an entry to irq table and place it in specific section which name is then placed

266 \* in an instance of struct \_isr\_list to be then used by the isr generation script to create

267 \* the linker script chunks.

268 \*/

269#define Z\_ISR\_DECLARE\_DIRECT(irq, flags, func) \

270 BUILD\_ASSERT(IS\_ENABLED(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_ADDRESS) || \

271 IS\_ENABLED(CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_CODE), \

272 "CONFIG\_IRQ\_VECTOR\_TABLE\_JUMP\_BY\_{ADDRESS,CODE} not set"); \

273 Z\_ISR\_DECLARE\_DIRECT\_C(irq, flags, func, \_\_COUNTER\_\_)

274

275

276#else /\* defined(CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION) \*/

277

278/\* Create an instance of struct \_isr\_list which gets put in the .intList

279 \* section. This gets consumed by gen\_isr\_tables.py which creates the vector

280 \* and/or SW ISR tables.

281 \*/

282#define Z\_ISR\_DECLARE(irq, flags, func, param) \

283 static Z\_DECL\_ALIGN(struct \_isr\_list) Z\_GENERIC\_SECTION(.intList) \

284 \_\_used \_MK\_ISR\_NAME(func, \_\_COUNTER\_\_) = \

285 {irq, flags, (void \*)&func, (const void \*)param}

286

287/\* The version of the Z\_ISR\_DECLARE that should be used for direct ISR declaration.

288 \* It is here for the API match the version with CONFIG\_ISR\_TABLES\_LOCAL\_DECLARATION enabled.

289 \*/

290#define Z\_ISR\_DECLARE\_DIRECT(irq, flags, func) \

291 Z\_ISR\_DECLARE(irq, ISR\_FLAG\_DIRECT | (flags), func, NULL)

292

293#endif

294

[ 295](sw__isr__table_8h.md#af36594d0586be77420bfe6eaf9f96a2c)#define IRQ\_TABLE\_SIZE (CONFIG\_NUM\_IRQS - CONFIG\_GEN\_IRQ\_START\_VECTOR)

296

297#ifdef CONFIG\_DYNAMIC\_INTERRUPTS

298void z\_isr\_install(unsigned int irq, void (\*routine)(const void \*),

299 const void \*param);

300

301#ifdef CONFIG\_SHARED\_INTERRUPTS

302int z\_isr\_uninstall(unsigned int irq, void (\*routine)(const void \*),

303 const void \*param);

304#endif /\* CONFIG\_SHARED\_INTERRUPTS \*/

305#endif

306

307#ifdef \_\_cplusplus

308}

309#endif

310

311#endif /\* \_ASMLANGUAGE \*/

312

313#endif /\* ZEPHYR\_INCLUDE\_SW\_ISR\_TABLE\_H\_ \*/

[device.h](device_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

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
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
