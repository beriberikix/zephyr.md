---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/linker-defs_8h_source.html
original_path: doxygen/html/linker-defs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-defs.h

[Go to the documentation of this file.](linker-defs_8h.md)

1/\*

2 \* Copyright (c) 2013-2014, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* DESCRIPTION

9 \* Platform independent, commonly used macros and defines related to linker

10 \* script.

11 \*

12 \* This file may be included by:

13 \* - Linker script files: for linker section declarations

14 \* - C files: for external declaration of address or size of linker section

15 \* - Assembly files: for external declaration of address or size of linker

16 \* section

17 \*/

18

19#ifndef ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEFS\_H\_

20#define ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEFS\_H\_

21

22#include <[zephyr/toolchain.h](toolchain_8h.md)>

23#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h.md)>

24#include <[zephyr/linker/sections.h](sections_8h.md)>

25#include <[zephyr/sys/util.h](sys_2util_8h.md)>

26#include <zephyr/offsets.h>

27

28/\* We need to dummy out DT\_NODE\_HAS\_STATUS when building the unittests.

29 \* Including devicetree.h would require generating dummy header files

30 \* to match what gen\_defines creates, so it's easier to just dummy out

31 \* DT\_NODE\_HAS\_STATUS. These are undefined at the end of the file.

32 \*/

33#ifdef ZTEST\_UNITTEST

34#define DT\_NODE\_HAS\_STATUS(node, status) 0

35#define DT\_NODE\_HAS\_STATUS\_OKAY(node) 0

36#else

37#include <[zephyr/devicetree.h](devicetree_8h.md)>

38#endif

39

40#ifdef \_LINKER

41/\*

42 \* generate a symbol to mark the start of the objects array for

43 \* the specified object and level, then link all of those objects

44 \* (sorted by priority). Ensure the objects aren't discarded if there is

45 \* no direct reference to them

46 \*/

[ 47](linker-defs_8h.md#a7401dc3cb7ae4d3bb3afcb99c79a50c2)#define CREATE\_OBJ\_LEVEL(object, level) \

48 \_\_##object##\_##level##\_start = .; \

49 KEEP(\*(SORT(.z\_##object##\_##level?\_\*))); \

50 KEEP(\*(SORT(.z\_##object##\_##level??\_\*)));

51

52/\*

53 \* link in shell initialization objects for all modules that use shell and

54 \* their shell commands are automatically initialized by the kernel.

55 \*/

56

57#elif defined(\_ASMLANGUAGE)

58

59/\* Assembly FILES: declaration defined by the linker script \*/

60GDATA(\_\_bss\_start)

61GDATA(\_\_bss\_num\_words)

62#ifdef CONFIG\_XIP

63GDATA(\_\_data\_region\_load\_start)

64GDATA(\_\_data\_region\_start)

65GDATA(\_\_data\_region\_num\_words)

66#endif

67

68#else /\* ! \_ASMLANGUAGE \*/

69

70#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

71/\*

72 \* Memory owned by the kernel, to be used as shared memory between

73 \* application threads.

74 \*

75 \* The following are extern symbols from the linker. This enables

76 \* the dynamic k\_mem\_domain and k\_mem\_partition creation and alignment

77 \* to the section produced in the linker.

78

79 \* The policy for this memory will be to initially configure all of it as

80 \* kernel / supervisor thread accessible.

81 \*/

82extern char \_app\_smem\_start[];

83extern char \_app\_smem\_end[];

84extern char \_app\_smem\_size[];

85extern char \_app\_smem\_rom\_start[];

86extern char \_app\_smem\_num\_words[];

87

88#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

89extern char \_app\_smem\_pinned\_start[];

90extern char \_app\_smem\_pinned\_end[];

91extern char \_app\_smem\_pinned\_size[];

92extern char \_app\_smem\_pinned\_num\_words[];

93#endif

94

95/\* Memory owned by the kernel. Start and end will be aligned for memory

96 \* management/protection hardware for the target architecture.

97 \*

98 \* Consists of all kernel-side globals, all kernel objects, all thread stacks,

99 \* and all currently unused RAM.

100 \*

101 \* Except for the stack of the currently executing thread, none of this memory

102 \* is normally accessible to user threads unless specifically granted at

103 \* runtime.

104 \*/

105extern char \_\_kernel\_ram\_start[];

106extern char \_\_kernel\_ram\_end[];

107extern char \_\_kernel\_ram\_size[];

108

109/\* Used by z\_bss\_zero or arch-specific implementation \*/

110extern char \_\_bss\_start[];

111extern char \_\_bss\_end[];

112

113/\* Used by z\_data\_copy() or arch-specific implementation \*/

114#ifdef CONFIG\_XIP

115extern char \_\_data\_region\_load\_start[];

116extern char \_\_data\_region\_start[];

117extern char \_\_data\_region\_end[];

118#endif /\* CONFIG\_XIP \*/

119

120#ifdef CONFIG\_MMU

121/\* Virtual addresses of page-aligned kernel image mapped into RAM at boot \*/

122extern char z\_mapped\_start[];

123extern char z\_mapped\_end[];

124#endif /\* CONFIG\_MMU \*/

125

126/\* Includes text and rodata \*/

127extern char \_\_rom\_region\_start[];

128extern char \_\_rom\_region\_end[];

129extern char \_\_rom\_region\_size[];

130

131/\* Includes all ROMable data, i.e. the size of the output image file. \*/

132extern char \_flash\_used[];

133

134/\* datas, bss, noinit \*/

135extern char \_image\_ram\_start[];

136extern char \_image\_ram\_end[];

137extern char \_image\_ram\_size[];

138

139extern char \_\_text\_region\_start[];

140extern char \_\_text\_region\_end[];

141extern char \_\_text\_region\_size[];

142

143extern char \_\_rodata\_region\_start[];

144extern char \_\_rodata\_region\_end[];

145extern char \_\_rodata\_region\_size[];

146

147extern char \_vector\_start[];

148extern char \_vector\_end[];

149

150#ifdef CONFIG\_SW\_VECTOR\_RELAY

151extern char \_\_vector\_relay\_table[];

152#endif

153

154#ifdef CONFIG\_COVERAGE\_GCOV

155extern char \_\_gcov\_bss\_start[];

156extern char \_\_gcov\_bss\_end[];

157extern char \_\_gcov\_bss\_size[];

158#endif /\* CONFIG\_COVERAGE\_GCOV \*/

159

160/\* end address of image, used by newlib for the heap \*/

161extern char \_end[];

162

163#if (DT\_NODE\_HAS\_STATUS\_OKAY(DT\_CHOSEN(zephyr\_ccm)))

164extern char \_\_ccm\_data\_rom\_start[];

165extern char \_\_ccm\_start[];

166extern char \_\_ccm\_data\_start[];

167extern char \_\_ccm\_data\_end[];

168extern char \_\_ccm\_bss\_start[];

169extern char \_\_ccm\_bss\_end[];

170extern char \_\_ccm\_noinit\_start[];

171extern char \_\_ccm\_noinit\_end[];

172extern char \_\_ccm\_end[];

173#endif

174

175#if (DT\_NODE\_HAS\_STATUS\_OKAY(DT\_CHOSEN(zephyr\_itcm)))

176extern char \_\_itcm\_start[];

177extern char \_\_itcm\_end[];

178extern char \_\_itcm\_size[];

179extern char \_\_itcm\_load\_start[];

180#endif

181

182#if (DT\_NODE\_HAS\_STATUS\_OKAY(DT\_CHOSEN(zephyr\_dtcm)))

183extern char \_\_dtcm\_data\_start[];

184extern char \_\_dtcm\_data\_end[];

185extern char \_\_dtcm\_bss\_start[];

186extern char \_\_dtcm\_bss\_end[];

187extern char \_\_dtcm\_noinit\_start[];

188extern char \_\_dtcm\_noinit\_end[];

189extern char \_\_dtcm\_data\_load\_start[];

190extern char \_\_dtcm\_start[];

191extern char \_\_dtcm\_end[];

192#endif

193

194#if (DT\_NODE\_HAS\_STATUS\_OKAY(DT\_CHOSEN(zephyr\_ocm)))

195extern char \_\_ocm\_data\_start[];

196extern char \_\_ocm\_data\_end[];

197extern char \_\_ocm\_bss\_start[];

198extern char \_\_ocm\_bss\_end[];

199extern char \_\_ocm\_start[];

200extern char \_\_ocm\_end[];

201extern char \_\_ocm\_size[];

202#endif

203

204/\* Used by the Security Attribution Unit to configure the

205 \* Non-Secure Callable region.

206 \*/

207#ifdef CONFIG\_ARM\_FIRMWARE\_HAS\_SECURE\_ENTRY\_FUNCS

208extern char \_\_sg\_start[];

209extern char \_\_sg\_end[];

210extern char \_\_sg\_size[];

211#endif /\* CONFIG\_ARM\_FIRMWARE\_HAS\_SECURE\_ENTRY\_FUNCS \*/

212

213/\*

214 \* Non-cached kernel memory region, currently only available on ARM Cortex-M7

215 \* with a MPU. Start and end will be aligned for memory management/protection

216 \* hardware for the target architecture.

217 \*

218 \* All the functions with '\_\_nocache' keyword will be placed into this

219 \* section.

220 \*/

221#ifdef CONFIG\_NOCACHE\_MEMORY

222extern char \_nocache\_ram\_start[];

223extern char \_nocache\_ram\_end[];

224extern char \_nocache\_ram\_size[];

225#endif /\* CONFIG\_NOCACHE\_MEMORY \*/

226

227/\* Memory owned by the kernel. Start and end will be aligned for memory

228 \* management/protection hardware for the target architecture.

229 \*

230 \* All the functions with '\_\_ramfunc' keyword will be placed into this

231 \* section, stored in RAM instead of FLASH.

232 \*/

233#ifdef CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT

234extern char \_\_ramfunc\_region\_start[];

235extern char \_\_ramfunc\_start[];

236extern char \_\_ramfunc\_end[];

237extern char \_\_ramfunc\_size[];

238extern char \_\_ramfunc\_load\_start[];

239#endif /\* CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT \*/

240

241/\* Memory owned by the kernel. Memory region for thread privilege stack buffers,

242 \* currently only applicable on ARM Cortex-M architecture when building with

243 \* support for User Mode.

244 \*

245 \* All thread privilege stack buffers will be placed into this section.

246 \*/

247#ifdef CONFIG\_USERSPACE

248extern char z\_priv\_stacks\_ram\_start[];

249extern char z\_priv\_stacks\_ram\_end[];

250extern char z\_user\_stacks\_start[];

251extern char z\_user\_stacks\_end[];

252extern char z\_kobject\_data\_begin[];

253#endif /\* CONFIG\_USERSPACE \*/

254

255#ifdef CONFIG\_THREAD\_LOCAL\_STORAGE

256extern char \_\_tdata\_start[];

257extern char \_\_tdata\_end[];

258extern char \_\_tdata\_size[];

259extern char \_\_tdata\_align[];

260extern char \_\_tbss\_start[];

261extern char \_\_tbss\_end[];

262extern char \_\_tbss\_size[];

263extern char \_\_tbss\_align[];

264extern char \_\_tls\_start[];

265extern char \_\_tls\_end[];

266extern char \_\_tls\_size[];

267#endif /\* CONFIG\_THREAD\_LOCAL\_STORAGE \*/

268

269#ifdef CONFIG\_LINKER\_USE\_BOOT\_SECTION

270/\* lnkr\_boot\_start[] and lnkr\_boot\_end[]

271 \* must encapsulate all the boot sections.

272 \*/

273extern char lnkr\_boot\_start[];

274extern char lnkr\_boot\_end[];

275

276extern char lnkr\_boot\_text\_start[];

277extern char lnkr\_boot\_text\_end[];

278extern char lnkr\_boot\_text\_size[];

279extern char lnkr\_boot\_data\_start[];

280extern char lnkr\_boot\_data\_end[];

281extern char lnkr\_boot\_data\_size[];

282extern char lnkr\_boot\_rodata\_start[];

283extern char lnkr\_boot\_rodata\_end[];

284extern char lnkr\_boot\_rodata\_size[];

285extern char lnkr\_boot\_bss\_start[];

286extern char lnkr\_boot\_bss\_end[];

287extern char lnkr\_boot\_bss\_size[];

288extern char lnkr\_boot\_noinit\_start[];

289extern char lnkr\_boot\_noinit\_end[];

290extern char lnkr\_boot\_noinit\_size[];

291#endif /\* CONFIG\_LINKER\_USE\_BOOT\_SECTION \*/

292

293#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

294/\* lnkr\_pinned\_start[] and lnkr\_pinned\_end[] must encapsulate

295 \* all the pinned sections as these are used by

296 \* the MMU code to mark the physical page frames with

297 \* K\_MEM\_PAGE\_FRAME\_PINNED.

298 \*/

299extern char lnkr\_pinned\_start[];

300extern char lnkr\_pinned\_end[];

301

302extern char lnkr\_pinned\_text\_start[];

303extern char lnkr\_pinned\_text\_end[];

304extern char lnkr\_pinned\_text\_size[];

305extern char lnkr\_pinned\_data\_start[];

306extern char lnkr\_pinned\_data\_end[];

307extern char lnkr\_pinned\_data\_size[];

308extern char lnkr\_pinned\_rodata\_start[];

309extern char lnkr\_pinned\_rodata\_end[];

310extern char lnkr\_pinned\_rodata\_size[];

311extern char lnkr\_pinned\_bss\_start[];

312extern char lnkr\_pinned\_bss\_end[];

313extern char lnkr\_pinned\_bss\_size[];

314extern char lnkr\_pinned\_noinit\_start[];

315extern char lnkr\_pinned\_noinit\_end[];

316extern char lnkr\_pinned\_noinit\_size[];

317

318\_\_pinned\_func

319static inline bool lnkr\_is\_pinned([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr)

320{

321 if ((addr >= ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_start) &&

322 (addr < ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_end)) {

323 return true;

324 } else {

325 return false;

326 }

327}

328

329\_\_pinned\_func

330static inline bool lnkr\_is\_region\_pinned([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, size\_t sz)

331{

332 if ((addr >= ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_start) &&

333 ((addr + sz) < ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_end)) {

334 return true;

335 } else {

336 return false;

337 }

338}

339

340#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

341

342#ifdef CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION

343/\* lnkr\_ondemand\_start[] and lnkr\_ondemand\_end[] must encapsulate

344 \* all the on-demand sections as these are used by

345 \* the MMU code to mark the virtual pages with the appropriate backing store

346 \* location token to have them be paged in on demand.

347 \*/

348extern char lnkr\_ondemand\_start[];

349extern char lnkr\_ondemand\_end[];

350extern char lnkr\_ondemand\_load\_start[];

351

352extern char lnkr\_ondemand\_text\_start[];

353extern char lnkr\_ondemand\_text\_end[];

354extern char lnkr\_ondemand\_text\_size[];

355extern char lnkr\_ondemand\_rodata\_start[];

356extern char lnkr\_ondemand\_rodata\_end[];

357extern char lnkr\_ondemand\_rodata\_size[];

358

359#endif /\* CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION \*/

360#endif /\* ! \_ASMLANGUAGE \*/

361

362#ifdef ZTEST\_UNITTEST

363#undef DT\_NODE\_HAS\_STATUS

364#undef DT\_NODE\_HAS\_STATUS\_OKAY

365#endif

366

367#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEFS\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[common.h](include_2zephyr_2toolchain_2common_8h.md)

Common toolchain abstraction.

[types.h](include_2zephyr_2types_8h.md)

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-defs.h](linker-defs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
