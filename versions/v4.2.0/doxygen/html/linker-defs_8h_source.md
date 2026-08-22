---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/linker-defs_8h_source.html
original_path: doxygen/html/linker-defs_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

40/\* The GCC for Renesas RX processors adds leading underscores to C-symbols

41 \* by default. As a workaroud for symbols defined in linker scripts to be

42 \* available in C code, an alias with a leading underscore has to be provided.

43 \*/

44#if defined(CONFIG\_RX)

45#define PLACE\_SYMBOL\_HERE(symbol) \

46 symbol = .; \

47 PROVIDE(\_CONCAT(\_, symbol) = symbol)

48#else

[ 49](linker-defs_8h.md#a9a8b405bbdbdd1e16d7298b1b0b101fb)#define PLACE\_SYMBOL\_HERE(symbol) symbol = .

50#endif

51

52#ifdef \_LINKER

53/\*

54 \* generate a symbol to mark the start of the objects array for

55 \* the specified object and level, then link all of those objects

56 \* (sorted by priority). Ensure the objects aren't discarded if there is

57 \* no direct reference to them

58 \*/

59

60/\* clang-format off \*/

[ 61](linker-defs_8h.md#a7401dc3cb7ae4d3bb3afcb99c79a50c2)#define CREATE\_OBJ\_LEVEL(object, level) \

62 PLACE\_SYMBOL\_HERE(\_\_##object##\_##level##\_start);\

63 KEEP(\*(SORT(.z\_##object##\_##level##\_P\_?\_\*))); \

64 KEEP(\*(SORT(.z\_##object##\_##level##\_P\_??\_\*))); \

65 KEEP(\*(SORT(.z\_##object##\_##level##\_P\_???\_\*)));

66/\* clang-format on \*/

67

68/\*

69 \* link in shell initialization objects for all modules that use shell and

70 \* their shell commands are automatically initialized by the kernel.

71 \*/

72

73#elif defined(\_ASMLANGUAGE)

74

75/\* Assembly FILES: declaration defined by the linker script \*/

76GDATA(\_\_bss\_start)

77GDATA(\_\_bss\_num\_words)

78#ifdef CONFIG\_XIP

79GDATA(\_\_data\_region\_load\_start)

80GDATA(\_\_data\_region\_start)

81GDATA(\_\_data\_region\_num\_words)

82#endif

83

84#else /\* ! \_ASMLANGUAGE \*/

85

86#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

87/\*

88 \* Memory owned by the kernel, to be used as shared memory between

89 \* application threads.

90 \*

91 \* The following are extern symbols from the linker. This enables

92 \* the dynamic k\_mem\_domain and k\_mem\_partition creation and alignment

93 \* to the section produced in the linker.

94

95 \* The policy for this memory will be to initially configure all of it as

96 \* kernel / supervisor thread accessible.

97 \*/

98extern char \_app\_smem\_start[];

99extern char \_app\_smem\_end[];

100extern char \_app\_smem\_size[];

101extern char \_app\_smem\_rom\_start[];

102extern char \_app\_smem\_num\_words[];

103

104#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

105extern char \_app\_smem\_pinned\_start[];

106extern char \_app\_smem\_pinned\_end[];

107extern char \_app\_smem\_pinned\_size[];

108extern char \_app\_smem\_pinned\_num\_words[];

109#endif

110

111/\* Memory owned by the kernel. Start and end will be aligned for memory

112 \* management/protection hardware for the target architecture.

113 \*

114 \* Consists of all kernel-side globals, all kernel objects, all thread stacks,

115 \* and all currently unused RAM.

116 \*

117 \* Except for the stack of the currently executing thread, none of this memory

118 \* is normally accessible to user threads unless specifically granted at

119 \* runtime.

120 \*/

121extern char \_\_kernel\_ram\_start[];

122extern char \_\_kernel\_ram\_end[];

123extern char \_\_kernel\_ram\_size[];

124

125/\* Used by z\_bss\_zero or arch-specific implementation \*/

126extern char \_\_bss\_start[];

127extern char \_\_bss\_end[];

128

129/\* Used by z\_data\_copy() or arch-specific implementation \*/

130#ifdef CONFIG\_XIP

131extern char \_\_data\_region\_load\_start[];

132extern char \_\_data\_region\_start[];

133extern char \_\_data\_region\_end[];

134#endif /\* CONFIG\_XIP \*/

135

136#ifdef CONFIG\_MMU

137/\* Virtual addresses of page-aligned kernel image mapped into RAM at boot \*/

138extern char z\_mapped\_start[];

139extern char z\_mapped\_end[];

140#endif /\* CONFIG\_MMU \*/

141

142/\* Includes text and rodata \*/

143extern char \_\_rom\_region\_start[];

144extern char \_\_rom\_region\_end[];

145extern char \_\_rom\_region\_size[];

146

147/\* Includes all ROMable data, i.e. the size of the output image file. \*/

148extern char \_flash\_used[];

149

150/\* datas, bss, noinit \*/

151extern char \_image\_ram\_start[];

152extern char \_image\_ram\_end[];

153extern char \_image\_ram\_size[];

154

155extern char \_\_text\_region\_start[];

156extern char \_\_text\_region\_end[];

157extern char \_\_text\_region\_size[];

158

159extern char \_\_rodata\_region\_start[];

160extern char \_\_rodata\_region\_end[];

161extern char \_\_rodata\_region\_size[];

162

163extern char \_vector\_start[];

164extern char \_vector\_end[];

165

166#ifdef CONFIG\_SW\_VECTOR\_RELAY

167extern char \_\_vector\_relay\_table[];

168#endif

169

170#ifdef CONFIG\_SRAM\_VECTOR\_TABLE

171extern char \_sram\_vector\_start[];

172extern char \_sram\_vector\_end[];

173extern char \_sram\_vector\_size[];

174#endif

175

176#ifdef CONFIG\_COVERAGE\_GCOV

177extern char \_\_gcov\_bss\_start[];

178extern char \_\_gcov\_bss\_end[];

179extern char \_\_gcov\_bss\_size[];

180#endif /\* CONFIG\_COVERAGE\_GCOV \*/

181

182/\* end address of image, used by newlib for the heap \*/

183extern char \_end[];

184

185#if (DT\_NODE\_HAS\_STATUS\_OKAY(DT\_CHOSEN(zephyr\_ccm)))

186extern char \_\_ccm\_data\_load\_start[];

187extern char \_\_ccm\_start[];

188extern char \_\_ccm\_data\_start[];

189extern char \_\_ccm\_data\_end[];

190extern char \_\_ccm\_bss\_start[];

191extern char \_\_ccm\_bss\_end[];

192extern char \_\_ccm\_noinit\_start[];

193extern char \_\_ccm\_noinit\_end[];

194extern char \_\_ccm\_end[];

195#endif

196

197#if (DT\_NODE\_HAS\_STATUS\_OKAY(DT\_CHOSEN(zephyr\_itcm)))

198extern char \_\_itcm\_start[];

199extern char \_\_itcm\_end[];

200extern char \_\_itcm\_size[];

201extern char \_\_itcm\_load\_start[];

202#endif

203

204#if (DT\_NODE\_HAS\_STATUS\_OKAY(DT\_CHOSEN(zephyr\_dtcm)))

205extern char \_\_dtcm\_data\_start[];

206extern char \_\_dtcm\_data\_end[];

207extern char \_\_dtcm\_bss\_start[];

208extern char \_\_dtcm\_bss\_end[];

209extern char \_\_dtcm\_noinit\_start[];

210extern char \_\_dtcm\_noinit\_end[];

211extern char \_\_dtcm\_data\_load\_start[];

212extern char \_\_dtcm\_start[];

213extern char \_\_dtcm\_end[];

214#endif

215

216#if (DT\_NODE\_HAS\_STATUS\_OKAY(DT\_CHOSEN(zephyr\_ocm)))

217extern char \_\_ocm\_data\_start[];

218extern char \_\_ocm\_data\_end[];

219extern char \_\_ocm\_bss\_start[];

220extern char \_\_ocm\_bss\_end[];

221extern char \_\_ocm\_start[];

222extern char \_\_ocm\_end[];

223extern char \_\_ocm\_size[];

224#endif

225

226/\* Used by the Security Attribution Unit to configure the

227 \* Non-Secure Callable region.

228 \*/

229#ifdef CONFIG\_ARM\_FIRMWARE\_HAS\_SECURE\_ENTRY\_FUNCS

230extern char \_\_sg\_start[];

231extern char \_\_sg\_end[];

232extern char \_\_sg\_size[];

233#endif /\* CONFIG\_ARM\_FIRMWARE\_HAS\_SECURE\_ENTRY\_FUNCS \*/

234

235/\*

236 \* Non-cached kernel memory region, currently only available on ARM Cortex-M7

237 \* with a MPU. Start and end will be aligned for memory management/protection

238 \* hardware for the target architecture.

239 \*

240 \* All the functions with '\_\_nocache' keyword will be placed into this

241 \* section.

242 \*/

243#ifdef CONFIG\_NOCACHE\_MEMORY

244extern char \_nocache\_ram\_start[];

245extern char \_nocache\_ram\_end[];

246extern char \_nocache\_ram\_size[];

247extern char \_nocache\_load\_start[];

248#endif /\* CONFIG\_NOCACHE\_MEMORY \*/

249

250/\* Memory owned by the kernel. Start and end will be aligned for memory

251 \* management/protection hardware for the target architecture.

252 \*

253 \* All the functions with '\_\_ramfunc' keyword will be placed into this

254 \* section, stored in RAM instead of FLASH.

255 \*/

256#ifdef CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT

257extern char \_\_ramfunc\_region\_start[];

258extern char \_\_ramfunc\_start[];

259extern char \_\_ramfunc\_end[];

260extern char \_\_ramfunc\_size[];

261extern char \_\_ramfunc\_load\_start[];

262#endif /\* CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT \*/

263

264/\* Memory owned by the kernel. Memory region for thread privilege stack buffers,

265 \* currently only applicable on ARM Cortex-M architecture when building with

266 \* support for User Mode.

267 \*

268 \* All thread privilege stack buffers will be placed into this section.

269 \*/

270#ifdef CONFIG\_USERSPACE

271extern char z\_priv\_stacks\_ram\_start[];

272extern char z\_priv\_stacks\_ram\_end[];

273extern char z\_user\_stacks\_start[];

274extern char z\_user\_stacks\_end[];

275extern char z\_kobject\_data\_begin[];

276#endif /\* CONFIG\_USERSPACE \*/

277

278#ifdef CONFIG\_THREAD\_LOCAL\_STORAGE

279extern char \_\_tdata\_start[];

280extern char \_\_tdata\_end[];

281extern char \_\_tdata\_size[];

282extern char \_\_tdata\_align[];

283extern char \_\_tbss\_start[];

284extern char \_\_tbss\_end[];

285extern char \_\_tbss\_size[];

286extern char \_\_tbss\_align[];

287extern char \_\_tls\_start[];

288extern char \_\_tls\_end[];

289extern char \_\_tls\_size[];

290#endif /\* CONFIG\_THREAD\_LOCAL\_STORAGE \*/

291

292#ifdef CONFIG\_LINKER\_USE\_BOOT\_SECTION

293/\* lnkr\_boot\_start[] and lnkr\_boot\_end[]

294 \* must encapsulate all the boot sections.

295 \*/

296extern char lnkr\_boot\_start[];

297extern char lnkr\_boot\_end[];

298

299extern char lnkr\_boot\_text\_start[];

300extern char lnkr\_boot\_text\_end[];

301extern char lnkr\_boot\_text\_size[];

302extern char lnkr\_boot\_data\_start[];

303extern char lnkr\_boot\_data\_end[];

304extern char lnkr\_boot\_data\_size[];

305extern char lnkr\_boot\_rodata\_start[];

306extern char lnkr\_boot\_rodata\_end[];

307extern char lnkr\_boot\_rodata\_size[];

308extern char lnkr\_boot\_bss\_start[];

309extern char lnkr\_boot\_bss\_end[];

310extern char lnkr\_boot\_bss\_size[];

311extern char lnkr\_boot\_noinit\_start[];

312extern char lnkr\_boot\_noinit\_end[];

313extern char lnkr\_boot\_noinit\_size[];

314#endif /\* CONFIG\_LINKER\_USE\_BOOT\_SECTION \*/

315

316#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

317/\* lnkr\_pinned\_start[] and lnkr\_pinned\_end[] must encapsulate

318 \* all the pinned sections as these are used by

319 \* the MMU code to mark the physical page frames with

320 \* K\_MEM\_PAGE\_FRAME\_PINNED.

321 \*/

322extern char lnkr\_pinned\_start[];

323extern char lnkr\_pinned\_end[];

324

325extern char lnkr\_pinned\_text\_start[];

326extern char lnkr\_pinned\_text\_end[];

327extern char lnkr\_pinned\_text\_size[];

328extern char lnkr\_pinned\_data\_start[];

329extern char lnkr\_pinned\_data\_end[];

330extern char lnkr\_pinned\_data\_size[];

331extern char lnkr\_pinned\_rodata\_start[];

332extern char lnkr\_pinned\_rodata\_end[];

333extern char lnkr\_pinned\_rodata\_size[];

334extern char lnkr\_pinned\_bss\_start[];

335extern char lnkr\_pinned\_bss\_end[];

336extern char lnkr\_pinned\_bss\_size[];

337extern char lnkr\_pinned\_noinit\_start[];

338extern char lnkr\_pinned\_noinit\_end[];

339extern char lnkr\_pinned\_noinit\_size[];

340

341\_\_pinned\_func

342static inline bool lnkr\_is\_pinned([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr)

343{

344 if ((addr >= ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_start) &&

345 (addr < ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_end)) {

346 return true;

347 } else {

348 return false;

349 }

350}

351

352\_\_pinned\_func

353static inline bool lnkr\_is\_region\_pinned([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, size\_t sz)

354{

355 if ((addr >= ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_start) &&

356 ((addr + sz) < ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_end)) {

357 return true;

358 } else {

359 return false;

360 }

361}

362

363#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

364

365#ifdef CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION

366/\* lnkr\_ondemand\_start[] and lnkr\_ondemand\_end[] must encapsulate

367 \* all the on-demand sections as these are used by

368 \* the MMU code to mark the virtual pages with the appropriate backing store

369 \* location token to have them be paged in on demand.

370 \*/

371extern char lnkr\_ondemand\_start[];

372extern char lnkr\_ondemand\_end[];

373extern char lnkr\_ondemand\_load\_start[];

374

375extern char lnkr\_ondemand\_text\_start[];

376extern char lnkr\_ondemand\_text\_end[];

377extern char lnkr\_ondemand\_text\_size[];

378extern char lnkr\_ondemand\_rodata\_start[];

379extern char lnkr\_ondemand\_rodata\_end[];

380extern char lnkr\_ondemand\_rodata\_size[];

381

382#endif /\* CONFIG\_LINKER\_USE\_ONDEMAND\_SECTION \*/

383#endif /\* ! \_ASMLANGUAGE \*/

384

385#ifdef ZTEST\_UNITTEST

386#undef DT\_NODE\_HAS\_STATUS

387#undef DT\_NODE\_HAS\_STATUS\_OKAY

388#endif

389

390#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEFS\_H\_ \*/

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
