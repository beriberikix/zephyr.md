---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/linker-defs_8h_source.html
original_path: doxygen/html/linker-defs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

23#include <[zephyr/toolchain/common.h](common_8h.md)>

24#include <[zephyr/linker/sections.h](sections_8h.md)>

25#include <[zephyr/sys/util.h](util_8h.md)>

26#include <[offsets.h](offsets_8h.md)>

27

28/\* We need to dummy out DT\_NODE\_HAS\_STATUS when building the unittests.

29 \* Including devicetree.h would require generating dummy header files

30 \* to match what gen\_defines creates, so it's easier to just dummy out

31 \* DT\_NODE\_HAS\_STATUS.

32 \*/

33#ifdef ZTEST\_UNITTEST

34#define DT\_NODE\_HAS\_STATUS(node, status) 0

35#else

36#include <[zephyr/devicetree.h](devicetree_8h.md)>

37#endif

38

39#ifdef \_LINKER

40/\*

41 \* generate a symbol to mark the start of the objects array for

42 \* the specified object and level, then link all of those objects

43 \* (sorted by priority). Ensure the objects aren't discarded if there is

44 \* no direct reference to them

45 \*/

[ 46](linker-defs_8h.md#a7401dc3cb7ae4d3bb3afcb99c79a50c2)#define CREATE\_OBJ\_LEVEL(object, level) \

47 \_\_##object##\_##level##\_start = .; \

48 KEEP(\*(SORT(.z\_##object##\_##level?\_\*))); \

49 KEEP(\*(SORT(.z\_##object##\_##level??\_\*)));

50

51/\*

52 \* link in shell initialization objects for all modules that use shell and

53 \* their shell commands are automatically initialized by the kernel.

54 \*/

55

56#elif defined(\_ASMLANGUAGE)

57

58/\* Assembly FILES: declaration defined by the linker script \*/

59GDATA(\_\_bss\_start)

60GDATA(\_\_bss\_num\_words)

61#ifdef CONFIG\_XIP

62GDATA(\_\_data\_region\_load\_start)

63GDATA(\_\_data\_region\_start)

64GDATA(\_\_data\_region\_num\_words)

65#endif

66

67#else /\* ! \_ASMLANGUAGE \*/

68

69#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

70/\*

71 \* Memory owned by the kernel, to be used as shared memory between

72 \* application threads.

73 \*

74 \* The following are extern symbols from the linker. This enables

75 \* the dynamic k\_mem\_domain and k\_mem\_partition creation and alignment

76 \* to the section produced in the linker.

77

78 \* The policy for this memory will be to initially configure all of it as

79 \* kernel / supervisor thread accessible.

80 \*/

81extern char \_app\_smem\_start[];

82extern char \_app\_smem\_end[];

83extern char \_app\_smem\_size[];

84extern char \_app\_smem\_rom\_start[];

85extern char \_app\_smem\_num\_words[];

86

87#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

88extern char \_app\_smem\_pinned\_start[];

89extern char \_app\_smem\_pinned\_end[];

90extern char \_app\_smem\_pinned\_size[];

91extern char \_app\_smem\_pinned\_num\_words[];

92#endif

93

94/\* Memory owned by the kernel. Start and end will be aligned for memory

95 \* management/protection hardware for the target architecture.

96 \*

97 \* Consists of all kernel-side globals, all kernel objects, all thread stacks,

98 \* and all currently unused RAM.

99 \*

100 \* Except for the stack of the currently executing thread, none of this memory

101 \* is normally accessible to user threads unless specifically granted at

102 \* runtime.

103 \*/

104extern char \_\_kernel\_ram\_start[];

105extern char \_\_kernel\_ram\_end[];

106extern char \_\_kernel\_ram\_size[];

107

108/\* Used by z\_bss\_zero or arch-specific implementation \*/

109extern char \_\_bss\_start[];

110extern char \_\_bss\_end[];

111

112/\* Used by z\_data\_copy() or arch-specific implementation \*/

113#ifdef CONFIG\_XIP

114extern char \_\_data\_region\_load\_start[];

115extern char \_\_data\_region\_start[];

116extern char \_\_data\_region\_end[];

117#endif /\* CONFIG\_XIP \*/

118

119#ifdef CONFIG\_MMU

120/\* Virtual addresses of page-aligned kernel image mapped into RAM at boot \*/

121extern char z\_mapped\_start[];

122extern char z\_mapped\_end[];

123#endif /\* CONFIG\_MMU \*/

124

125/\* Includes text and rodata \*/

126extern char \_\_rom\_region\_start[];

127extern char \_\_rom\_region\_end[];

128extern char \_\_rom\_region\_size[];

129

130/\* Includes all ROMable data, i.e. the size of the output image file. \*/

131extern char \_flash\_used[];

132

133/\* datas, bss, noinit \*/

134extern char \_image\_ram\_start[];

135extern char \_image\_ram\_end[];

136extern char \_image\_ram\_size[];

137

138extern char \_\_text\_region\_start[];

139extern char \_\_text\_region\_end[];

140extern char \_\_text\_region\_size[];

141

142extern char \_\_rodata\_region\_start[];

143extern char \_\_rodata\_region\_end[];

144extern char \_\_rodata\_region\_size[];

145

146extern char \_vector\_start[];

147extern char \_vector\_end[];

148

149#ifdef CONFIG\_SW\_VECTOR\_RELAY

150extern char \_\_vector\_relay\_table[];

151#endif

152

153#ifdef CONFIG\_COVERAGE\_GCOV

154extern char \_\_gcov\_bss\_start[];

155extern char \_\_gcov\_bss\_end[];

156extern char \_\_gcov\_bss\_size[];

157#endif /\* CONFIG\_COVERAGE\_GCOV \*/

158

159/\* end address of image, used by newlib for the heap \*/

160extern char \_end[];

161

162#if DT\_NODE\_HAS\_STATUS(DT\_CHOSEN(zephyr\_ccm), okay)

163extern char \_\_ccm\_data\_rom\_start[];

164extern char \_\_ccm\_start[];

165extern char \_\_ccm\_data\_start[];

166extern char \_\_ccm\_data\_end[];

167extern char \_\_ccm\_bss\_start[];

168extern char \_\_ccm\_bss\_end[];

169extern char \_\_ccm\_noinit\_start[];

170extern char \_\_ccm\_noinit\_end[];

171extern char \_\_ccm\_end[];

172#endif

173

174#if DT\_NODE\_HAS\_STATUS(DT\_CHOSEN(zephyr\_itcm), okay)

175extern char \_\_itcm\_start[];

176extern char \_\_itcm\_end[];

177extern char \_\_itcm\_size[];

178extern char \_\_itcm\_load\_start[];

179#endif

180

181#if DT\_NODE\_HAS\_STATUS(DT\_CHOSEN(zephyr\_dtcm), okay)

182extern char \_\_dtcm\_data\_start[];

183extern char \_\_dtcm\_data\_end[];

184extern char \_\_dtcm\_bss\_start[];

185extern char \_\_dtcm\_bss\_end[];

186extern char \_\_dtcm\_noinit\_start[];

187extern char \_\_dtcm\_noinit\_end[];

188extern char \_\_dtcm\_data\_load\_start[];

189extern char \_\_dtcm\_start[];

190extern char \_\_dtcm\_end[];

191#endif

192

193#if DT\_NODE\_HAS\_STATUS(DT\_CHOSEN(zephyr\_ocm), okay)

194extern char \_\_ocm\_data\_start[];

195extern char \_\_ocm\_data\_end[];

196extern char \_\_ocm\_bss\_start[];

197extern char \_\_ocm\_bss\_end[];

198extern char \_\_ocm\_start[];

199extern char \_\_ocm\_end[];

200extern char \_\_ocm\_size[];

201#endif

202

203/\* Used by the Security Attribution Unit to configure the

204 \* Non-Secure Callable region.

205 \*/

206#ifdef CONFIG\_ARM\_FIRMWARE\_HAS\_SECURE\_ENTRY\_FUNCS

207extern char \_\_sg\_start[];

208extern char \_\_sg\_end[];

209extern char \_\_sg\_size[];

210#endif /\* CONFIG\_ARM\_FIRMWARE\_HAS\_SECURE\_ENTRY\_FUNCS \*/

211

212/\*

213 \* Non-cached kernel memory region, currently only available on ARM Cortex-M7

214 \* with a MPU. Start and end will be aligned for memory management/protection

215 \* hardware for the target architecture.

216 \*

217 \* All the functions with '\_\_nocache' keyword will be placed into this

218 \* section.

219 \*/

220#ifdef CONFIG\_NOCACHE\_MEMORY

221extern char \_nocache\_ram\_start[];

222extern char \_nocache\_ram\_end[];

223extern char \_nocache\_ram\_size[];

224#endif /\* CONFIG\_NOCACHE\_MEMORY \*/

225

226/\* Memory owned by the kernel. Start and end will be aligned for memory

227 \* management/protection hardware for the target architecture.

228 \*

229 \* All the functions with '\_\_ramfunc' keyword will be placed into this

230 \* section, stored in RAM instead of FLASH.

231 \*/

232#ifdef CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT

233extern char \_\_ramfunc\_start[];

234extern char \_\_ramfunc\_end[];

235extern char \_\_ramfunc\_size[];

236extern char \_\_ramfunc\_load\_start[];

237#endif /\* CONFIG\_ARCH\_HAS\_RAMFUNC\_SUPPORT \*/

238

239/\* Memory owned by the kernel. Memory region for thread privilege stack buffers,

240 \* currently only applicable on ARM Cortex-M architecture when building with

241 \* support for User Mode.

242 \*

243 \* All thread privilege stack buffers will be placed into this section.

244 \*/

245#ifdef CONFIG\_USERSPACE

246extern char z\_priv\_stacks\_ram\_start[];

247extern char z\_priv\_stacks\_ram\_end[];

248extern char z\_user\_stacks\_start[];

249extern char z\_user\_stacks\_end[];

250extern char z\_kobject\_data\_begin[];

251#endif /\* CONFIG\_USERSPACE \*/

252

253#ifdef CONFIG\_THREAD\_LOCAL\_STORAGE

254extern char \_\_tdata\_start[];

255extern char \_\_tdata\_end[];

256extern char \_\_tdata\_size[];

257extern char \_\_tdata\_align[];

258extern char \_\_tbss\_start[];

259extern char \_\_tbss\_end[];

260extern char \_\_tbss\_size[];

261extern char \_\_tbss\_align[];

262extern char \_\_tls\_start[];

263extern char \_\_tls\_end[];

264extern char \_\_tls\_size[];

265#endif /\* CONFIG\_THREAD\_LOCAL\_STORAGE \*/

266

267#ifdef CONFIG\_LINKER\_USE\_BOOT\_SECTION

268/\* lnkr\_boot\_start[] and lnkr\_boot\_end[]

269 \* must encapsulate all the boot sections.

270 \*/

271extern char lnkr\_boot\_start[];

272extern char lnkr\_boot\_end[];

273

274extern char lnkr\_boot\_text\_start[];

275extern char lnkr\_boot\_text\_end[];

276extern char lnkr\_boot\_text\_size[];

277extern char lnkr\_boot\_data\_start[];

278extern char lnkr\_boot\_data\_end[];

279extern char lnkr\_boot\_data\_size[];

280extern char lnkr\_boot\_rodata\_start[];

281extern char lnkr\_boot\_rodata\_end[];

282extern char lnkr\_boot\_rodata\_size[];

283extern char lnkr\_boot\_bss\_start[];

284extern char lnkr\_boot\_bss\_end[];

285extern char lnkr\_boot\_bss\_size[];

286extern char lnkr\_boot\_noinit\_start[];

287extern char lnkr\_boot\_noinit\_end[];

288extern char lnkr\_boot\_noinit\_size[];

289#endif /\* CONFIG\_LINKER\_USE\_BOOT\_SECTION \*/

290

291#ifdef CONFIG\_LINKER\_USE\_PINNED\_SECTION

292/\* lnkr\_pinned\_start[] and lnkr\_pinned\_end[] must encapsulate

293 \* all the pinned sections as these are used by

294 \* the MMU code to mark the physical page frames with

295 \* Z\_PAGE\_FRAME\_PINNED.

296 \*/

297extern char lnkr\_pinned\_start[];

298extern char lnkr\_pinned\_end[];

299

300extern char lnkr\_pinned\_text\_start[];

301extern char lnkr\_pinned\_text\_end[];

302extern char lnkr\_pinned\_text\_size[];

303extern char lnkr\_pinned\_data\_start[];

304extern char lnkr\_pinned\_data\_end[];

305extern char lnkr\_pinned\_data\_size[];

306extern char lnkr\_pinned\_rodata\_start[];

307extern char lnkr\_pinned\_rodata\_end[];

308extern char lnkr\_pinned\_rodata\_size[];

309extern char lnkr\_pinned\_bss\_start[];

310extern char lnkr\_pinned\_bss\_end[];

311extern char lnkr\_pinned\_bss\_size[];

312extern char lnkr\_pinned\_noinit\_start[];

313extern char lnkr\_pinned\_noinit\_end[];

314extern char lnkr\_pinned\_noinit\_size[];

315

316\_\_pinned\_func

317static inline bool lnkr\_is\_pinned([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr)

318{

319 if ((addr >= ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_start) &&

320 (addr < ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_end)) {

321 return true;

322 } else {

323 return false;

324 }

325}

326

327\_\_pinned\_func

328static inline bool lnkr\_is\_region\_pinned([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, size\_t sz)

329{

330 if ((addr >= ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_start) &&

331 ((addr + sz) < ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)lnkr\_pinned\_end)) {

332 return true;

333 } else {

334 return false;

335 }

336}

337

338#endif /\* CONFIG\_LINKER\_USE\_PINNED\_SECTION \*/

339

340#endif /\* ! \_ASMLANGUAGE \*/

341

342#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEFS\_H\_ \*/

[common.h](common_8h.md)

Common toolchain abstraction.

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[types.h](include_2zephyr_2types_8h.md)

[offsets.h](offsets_8h.md)

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-defs.h](linker-defs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
