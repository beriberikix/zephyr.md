---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/cbprintf__internal_8h_source.html
original_path: doxygen/html/cbprintf__internal_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cbprintf\_internal.h

[Go to the documentation of this file.](cbprintf__internal_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_INTERNAL\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_INTERNAL\_H\_

9

10#include <[errno.h](errno_8h.md)>

11#include <stdarg.h>

12#include <stddef.h>

13#include <[stdint.h](stdint_8h.md)>

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15#include <[zephyr/sys/util.h](sys_2util_8h.md)>

16#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

17#include <[zephyr/arch/cpu.h](arch_2cpu_8h.md)>

18

19/\*

20 \* Special alignment cases

21 \*/

22

23#if defined(\_\_i386\_\_)

24/\* there are no gaps on the stack \*/

25#define VA\_STACK\_ALIGN(type) 1

26#elif defined(\_\_sparc\_\_)

27/\* there are no gaps on the stack \*/

28#define VA\_STACK\_ALIGN(type) 1

29#elif defined(\_\_x86\_64\_\_)

30#define VA\_STACK\_MIN\_ALIGN 8

31#elif defined(\_\_aarch64\_\_)

32#define VA\_STACK\_MIN\_ALIGN 8

33#elif defined(CONFIG\_ARC)

34#define VA\_STACK\_MIN\_ALIGN ARCH\_STACK\_PTR\_ALIGN

35#elif defined(\_\_riscv)

36#ifdef CONFIG\_RISCV\_ISA\_RV32E

37#define VA\_STACK\_ALIGN(type) 4

38#else

39#define VA\_STACK\_MIN\_ALIGN (\_\_riscv\_xlen / 8)

40#endif /\* CONFIG\_RISCV\_ISA\_RV32E \*/

41#endif

42

43/\*

44 \* Default alignment values if not specified by architecture config

45 \*/

46

47#ifndef VA\_STACK\_MIN\_ALIGN

[ 48](cbprintf__internal_8h.md#a0ec36f3c06add6c091c8f552ef3736e1)#define VA\_STACK\_MIN\_ALIGN 1

49#endif

50

51#ifndef VA\_STACK\_ALIGN

[ 52](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)#define VA\_STACK\_ALIGN(type) MAX(VA\_STACK\_MIN\_ALIGN, \_\_alignof\_\_(type))

53#endif

54

55static inline void z\_cbprintf\_wcpy(int \*dst, int \*src, size\_t len)

56{

57 for (size\_t i = 0; i < len; i++) {

58 dst[i] = src[i];

59 }

60}

61

62#include <[zephyr/sys/cbprintf\_cxx.h](cbprintf__cxx_8h.md)>

63

64#ifdef \_\_cplusplus

65extern "C" {

66#endif

67

68

69#if defined(\_\_sparc\_\_)

70/\* The SPARC V8 ABI guarantees that the arguments of a variable argument

71 \* list function are stored on the stack at addresses which are 32-bit

72 \* aligned. It means that variables of type unit64\_t and double may not

73 \* be properly aligned on the stack.

74 \*

75 \* The compiler is aware of the ABI and takes care of this. However,

76 \* as we are directly accessing the variable argument list here, we need

77 \* to take the alignment into consideration and copy 64-bit arguments

78 \* as 32-bit words.

79 \*/

80#define Z\_CBPRINTF\_VA\_STACK\_LL\_DBL\_MEMCPY 1

81#else

82#define Z\_CBPRINTF\_VA\_STACK\_LL\_DBL\_MEMCPY 0

83#endif

84

89#define Z\_ARGIFY(arg) ((0) ? (arg) : (arg))

90

97#ifdef \_\_cplusplus

98#define Z\_CBPRINTF\_IS\_PCHAR(x, flags) \

99 z\_cbprintf\_cxx\_is\_pchar(x, (flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO)

100#else

101/\* NOLINTBEGIN(misc-redundant-expression) \*/

102#define Z\_CBPRINTF\_IS\_PCHAR(x, flags) \

103 \_Generic(Z\_ARGIFY(x), \

104 /\* char \* \*/ \

105 char \* : 1, \

106 const char \* : ((flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO) ? 0 : 1, \

107 volatile char \* : 1, \

108 const volatile char \* : 1, \

109 /\* unsigned char \* \*/ \

110 unsigned char \* : 1, \

111 const unsigned char \* : ((flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO) ? 0 : 1, \

112 volatile unsigned char \* : 1, \

113 const volatile unsigned char \* : 1,\

114 /\* wchar\_t \* \*/ \

115 wchar\_t \* : 1, \

116 const wchar\_t \* : ((flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO) ? 0 : 1, \

117 volatile wchar\_t \* : 1, \

118 const volatile wchar\_t \* : 1, \

119 default : \

120 0)

121/\* NOLINTEND(misc-redundant-expression) \*/

122#endif

123

131#ifdef \_\_cplusplus

132#define Z\_CBPRINTF\_IS\_WORD\_NUM(x) \

133 z\_cbprintf\_cxx\_is\_word\_num(x)

134#else

135#define Z\_CBPRINTF\_IS\_WORD\_NUM(x) \

136 \_Generic(x, \

137 char : 1, \

138 unsigned char : 1, \

139 short : 1, \

140 unsigned short : 1, \

141 int : 1, \

142 unsigned int : 1, \

143 long : sizeof(long) <= 4, \

144 unsigned long : sizeof(long) <= 4, \

145 default : \

146 0)

147#endif

148

159#ifdef \_\_cplusplus

160#define Z\_CBPRINTF\_IS\_NONE\_CHAR\_PTR(x) z\_cbprintf\_cxx\_is\_none\_char\_ptr(x)

161#else

162#define Z\_CBPRINTF\_IS\_NONE\_CHAR\_PTR(x) \

163 \_Generic(Z\_ARGIFY(x), \

164 char \* : 0, \

165 volatile char \* : 0, \

166 const char \* : 0, \

167 const volatile char \* : 0, \

168 unsigned char \* : 0, \

169 volatile unsigned char \* : 0, \

170 const unsigned char \* : 0, \

171 const volatile unsigned char \* : 0, \

172 char: 0, \

173 unsigned char: 0, \

174 short: 0, \

175 unsigned short: 0, \

176 int: 0, \

177 unsigned int: 0,\

178 long: 0, \

179 unsigned long: 0,\

180 long long: 0, \

181 unsigned long long: 0, \

182 float: 0, \

183 double: 0, \

184 default : \

185 1)

186#endif

187

194#define Z\_CBPRINTF\_NONE\_CHAR\_PTR\_ARGS(...) \

195 (FOR\_EACH(Z\_CBPRINTF\_IS\_NONE\_CHAR\_PTR, (+), \_\_VA\_ARGS\_\_)) \

196

203#define Z\_CBPRINTF\_NONE\_CHAR\_PTR\_COUNT(...) \

204 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

205 (0), \

206 (Z\_CBPRINTF\_NONE\_CHAR\_PTR\_ARGS(GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))))

207

221#define Z\_CBPRINTF\_P\_COUNT(fmt, ...) \

222 ((sizeof(fmt) >= 2 && fmt[0] == '%' && fmt[1] == 'p') ? 1 : 0) + \

223 ((sizeof(fmt) >= 3 && fmt[0] != '%' && fmt[1] == '%' && fmt[2] == 'p') ? 1 : 0) + \

224 ((sizeof(fmt) >= 4 && fmt[1] != '%' && fmt[2] == '%' && fmt[3] == 'p') ? 1 : 0) + \

225 ((sizeof(fmt) >= 5 && fmt[2] != '%' && fmt[3] == '%' && fmt[4] == 'p') ? 1 : 0) + \

226 ((sizeof(fmt) >= 6 && fmt[3] != '%' && fmt[4] == '%' && fmt[5] == 'p') ? 1 : 0) + \

227 ((sizeof(fmt) >= 7 && fmt[4] != '%' && fmt[5] == '%' && fmt[6] == 'p') ? 1 : 0) + \

228 ((sizeof(fmt) >= 8 && fmt[5] != '%' && fmt[6] == '%' && fmt[7] == 'p') ? 1 : 0) + \

229 ((sizeof(fmt) >= 9 && fmt[6] != '%' && fmt[7] == '%' && fmt[8] == 'p') ? 1 : 0) + \

230 ((sizeof(fmt) >= 10 && fmt[7] != '%' && fmt[8] == '%' && fmt[9] == 'p') ? 1 : 0) + \

231 ((sizeof(fmt) >= 11 && fmt[8] != '%' && fmt[9] == '%' && fmt[10] == 'p') ? 1 : 0) + \

232 ((sizeof(fmt) >= 12 && fmt[9] != '%' && fmt[10] == '%' && fmt[11] == 'p') ? 1 : 0) + \

233 ((sizeof(fmt) >= 13 && fmt[10] != '%' && fmt[11] == '%' && fmt[12] == 'p') ? 1 : 0) + \

234 ((sizeof(fmt) >= 14 && fmt[11] != '%' && fmt[12] == '%' && fmt[13] == 'p') ? 1 : 0) + \

235 ((sizeof(fmt) >= 15 && fmt[12] != '%' && fmt[13] == '%' && fmt[14] == 'p') ? 1 : 0) + \

236 ((sizeof(fmt) >= 16 && fmt[13] != '%' && fmt[14] == '%' && fmt[15] == 'p') ? 1 : 0) + \

237 ((sizeof(fmt) >= 17 && fmt[14] != '%' && fmt[15] == '%' && fmt[16] == 'p') ? 1 : 0) + \

238 ((sizeof(fmt) >= 18 && fmt[15] != '%' && fmt[16] == '%' && fmt[17] == 'p') ? 1 : 0) + \

239 ((sizeof(fmt) >= 19 && fmt[16] != '%' && fmt[17] == '%' && fmt[18] == 'p') ? 1 : 0) + \

240 ((sizeof(fmt) >= 20 && fmt[17] != '%' && fmt[18] == '%' && fmt[19] == 'p') ? 1 : 0) + \

241 ((sizeof(fmt) >= 21 && fmt[18] != '%' && fmt[19] == '%' && fmt[20] == 'p') ? 1 : 0) + \

242 ((sizeof(fmt) >= 22 && fmt[19] != '%' && fmt[20] == '%' && fmt[21] == 'p') ? 1 : 0) + \

243 ((sizeof(fmt) >= 23 && fmt[20] != '%' && fmt[21] == '%' && fmt[22] == 'p') ? 1 : 0) + \

244 ((sizeof(fmt) >= 24 && fmt[21] != '%' && fmt[22] == '%' && fmt[23] == 'p') ? 1 : 0) + \

245 ((sizeof(fmt) >= 25 && fmt[22] != '%' && fmt[23] == '%' && fmt[24] == 'p') ? 1 : 0) + \

246 ((sizeof(fmt) >= 26 && fmt[23] != '%' && fmt[24] == '%' && fmt[25] == 'p') ? 1 : 0) + \

247 ((sizeof(fmt) >= 27 && fmt[24] != '%' && fmt[25] == '%' && fmt[26] == 'p') ? 1 : 0) + \

248 ((sizeof(fmt) >= 28 && fmt[25] != '%' && fmt[26] == '%' && fmt[27] == 'p') ? 1 : 0) + \

249 ((sizeof(fmt) >= 29 && fmt[26] != '%' && fmt[27] == '%' && fmt[28] == 'p') ? 1 : 0) + \

250 ((sizeof(fmt) >= 30 && fmt[27] != '%' && fmt[28] == '%' && fmt[29] == 'p') ? 1 : 0) + \

251 ((sizeof(fmt) >= 31 && fmt[28] != '%' && fmt[29] == '%' && fmt[30] == 'p') ? 1 : 0) + \

252 ((sizeof(fmt) >= 32 && fmt[29] != '%' && fmt[30] == '%' && fmt[31] == 'p') ? 1 : 0) + \

253 ((sizeof(fmt) >= 33 && fmt[30] != '%' && fmt[31] == '%' && fmt[32] == 'p') ? 1 : 0) + \

254 ((sizeof(fmt) >= 34 && fmt[31] != '%' && fmt[32] == '%' && fmt[33] == 'p') ? 1 : 0) + \

255 ((sizeof(fmt) >= 35 && fmt[32] != '%' && fmt[33] == '%' && fmt[34] == 'p') ? 1 : 0) + \

256 ((sizeof(fmt) >= 36 && fmt[33] != '%' && fmt[34] == '%' && fmt[35] == 'p') ? 1 : 0) + \

257 ((sizeof(fmt) >= 37 && fmt[34] != '%' && fmt[35] == '%' && fmt[36] == 'p') ? 1 : 0) + \

258 ((sizeof(fmt) >= 38 && fmt[35] != '%' && fmt[36] == '%' && fmt[37] == 'p') ? 1 : 0) + \

259 ((sizeof(fmt) >= 39 && fmt[36] != '%' && fmt[37] == '%' && fmt[38] == 'p') ? 1 : 0) + \

260 ((sizeof(fmt) >= 40 && fmt[37] != '%' && fmt[38] == '%' && fmt[39] == 'p') ? 1 : 0) + \

261 ((sizeof(fmt) >= 41 && fmt[38] != '%' && fmt[39] == '%' && fmt[40] == 'p') ? 1 : 0) + \

262 ((sizeof(fmt) >= 42 && fmt[39] != '%' && fmt[40] == '%' && fmt[41] == 'p') ? 1 : 0) + \

263 ((sizeof(fmt) >= 43 && fmt[40] != '%' && fmt[41] == '%' && fmt[42] == 'p') ? 1 : 0) + \

264 ((sizeof(fmt) >= 44 && fmt[41] != '%' && fmt[42] == '%' && fmt[43] == 'p') ? 1 : 0) + \

265 ((sizeof(fmt) >= 45 && fmt[42] != '%' && fmt[43] == '%' && fmt[44] == 'p') ? 1 : 0) + \

266 ((sizeof(fmt) >= 46 && fmt[43] != '%' && fmt[44] == '%' && fmt[45] == 'p') ? 1 : 0) + \

267 ((sizeof(fmt) >= 47 && fmt[44] != '%' && fmt[45] == '%' && fmt[46] == 'p') ? 1 : 0) + \

268 ((sizeof(fmt) >= 48 && fmt[45] != '%' && fmt[46] == '%' && fmt[47] == 'p') ? 1 : 0) + \

269 ((sizeof(fmt) >= 49 && fmt[46] != '%' && fmt[47] == '%' && fmt[48] == 'p') ? 1 : 0) + \

270 ((sizeof(fmt) >= 50 && fmt[47] != '%' && fmt[48] == '%' && fmt[49] == 'p') ? 1 : 0) + \

271 ((sizeof(fmt) >= 51 && fmt[48] != '%' && fmt[49] == '%' && fmt[50] == 'p') ? 1 : 0) + \

272 ((sizeof(fmt) >= 52 && fmt[49] != '%' && fmt[50] == '%' && fmt[51] == 'p') ? 1 : 0) + \

273 ((sizeof(fmt) >= 53 && fmt[50] != '%' && fmt[51] == '%' && fmt[52] == 'p') ? 1 : 0) + \

274 ((sizeof(fmt) >= 54 && fmt[51] != '%' && fmt[52] == '%' && fmt[53] == 'p') ? 1 : 0) + \

275 ((sizeof(fmt) >= 55 && fmt[52] != '%' && fmt[53] == '%' && fmt[54] == 'p') ? 1 : 0) + \

276 ((sizeof(fmt) >= 56 && fmt[53] != '%' && fmt[54] == '%' && fmt[55] == 'p') ? 1 : 0) + \

277 ((sizeof(fmt) >= 57 && fmt[54] != '%' && fmt[55] == '%' && fmt[56] == 'p') ? 1 : 0) + \

278 ((sizeof(fmt) >= 58 && fmt[55] != '%' && fmt[56] == '%' && fmt[57] == 'p') ? 1 : 0) + \

279 ((sizeof(fmt) >= 59 && fmt[56] != '%' && fmt[57] == '%' && fmt[58] == 'p') ? 1 : 0) + \

280 ((sizeof(fmt) >= 60 && fmt[57] != '%' && fmt[58] == '%' && fmt[59] == 'p') ? 1 : 0) + \

281 ((sizeof(fmt) >= 61 && fmt[58] != '%' && fmt[59] == '%' && fmt[60] == 'p') ? 1 : 0) + \

282 ((sizeof(fmt) >= 62 && fmt[59] != '%' && fmt[60] == '%' && fmt[61] == 'p') ? 1 : 0) + \

283 ((sizeof(fmt) >= 63 && fmt[60] != '%' && fmt[61] == '%' && fmt[62] == 'p') ? 1 : 0) + \

284 ((sizeof(fmt) >= 64 && fmt[61] != '%' && fmt[62] == '%' && fmt[63] == 'p') ? 1 : 0) + \

285 ((sizeof(fmt) >= 65 && fmt[62] != '%' && fmt[63] == '%' && fmt[64] == 'p') ? 1 : 0) + \

286 ((sizeof(fmt) >= 66 && fmt[63] != '%' && fmt[64] == '%' && fmt[65] == 'p') ? 1 : 0) + \

287 ((sizeof(fmt) >= 67 && fmt[64] != '%' && fmt[65] == '%' && fmt[66] == 'p') ? 1 : 0) + \

288 ((sizeof(fmt) >= 68 && fmt[65] != '%' && fmt[66] == '%' && fmt[67] == 'p') ? 1 : 0) + \

289 ((sizeof(fmt) >= 69 && fmt[66] != '%' && fmt[67] == '%' && fmt[68] == 'p') ? 1 : 0) + \

290 ((sizeof(fmt) >= 70 && fmt[67] != '%' && fmt[68] == '%' && fmt[69] == 'p') ? 1 : 0) + \

291 ((sizeof(fmt) >= 71 && fmt[68] != '%' && fmt[69] == '%' && fmt[70] == 'p') ? 1 : 0) + \

292 ((sizeof(fmt) >= 72 && fmt[69] != '%' && fmt[70] == '%' && fmt[71] == 'p') ? 1 : 0) + \

293 ((sizeof(fmt) >= 73 && fmt[70] != '%' && fmt[71] == '%' && fmt[72] == 'p') ? 1 : 0) + \

294 ((sizeof(fmt) >= 74 && fmt[71] != '%' && fmt[72] == '%' && fmt[73] == 'p') ? 1 : 0) + \

295 ((sizeof(fmt) >= 75 && fmt[72] != '%' && fmt[73] == '%' && fmt[74] == 'p') ? 1 : 0) + \

296 ((sizeof(fmt) >= 76 && fmt[73] != '%' && fmt[74] == '%' && fmt[75] == 'p') ? 1 : 0) + \

297 ((sizeof(fmt) >= 77 && fmt[74] != '%' && fmt[75] == '%' && fmt[76] == 'p') ? 1 : 0) + \

298 ((sizeof(fmt) >= 78 && fmt[75] != '%' && fmt[76] == '%' && fmt[77] == 'p') ? 1 : 0) + \

299 ((sizeof(fmt) >= 79 && fmt[76] != '%' && fmt[77] == '%' && fmt[78] == 'p') ? 1 : 0) + \

300 ((sizeof(fmt) >= 80 && fmt[77] != '%' && fmt[78] == '%' && fmt[79] == 'p') ? 1 : 0) + \

301 ((sizeof(fmt) >= 81 && fmt[78] != '%' && fmt[79] == '%' && fmt[80] == 'p') ? 1 : 0) + \

302 ((sizeof(fmt) >= 82 && fmt[79] != '%' && fmt[80] == '%' && fmt[81] == 'p') ? 1 : 0) + \

303 ((sizeof(fmt) >= 83 && fmt[80] != '%' && fmt[81] == '%' && fmt[82] == 'p') ? 1 : 0) + \

304 ((sizeof(fmt) >= 84 && fmt[81] != '%' && fmt[82] == '%' && fmt[83] == 'p') ? 1 : 0) + \

305 ((sizeof(fmt) >= 85 && fmt[82] != '%' && fmt[83] == '%' && fmt[84] == 'p') ? 1 : 0) + \

306 ((sizeof(fmt) >= 86 && fmt[83] != '%' && fmt[84] == '%' && fmt[85] == 'p') ? 1 : 0) + \

307 ((sizeof(fmt) >= 87 && fmt[84] != '%' && fmt[85] == '%' && fmt[86] == 'p') ? 1 : 0) + \

308 ((sizeof(fmt) >= 88 && fmt[85] != '%' && fmt[86] == '%' && fmt[87] == 'p') ? 1 : 0) + \

309 ((sizeof(fmt) >= 89 && fmt[86] != '%' && fmt[87] == '%' && fmt[88] == 'p') ? 1 : 0) + \

310 ((sizeof(fmt) >= 90 && fmt[87] != '%' && fmt[88] == '%' && fmt[89] == 'p') ? 1 : 0) + \

311 ((sizeof(fmt) >= 91 && fmt[88] != '%' && fmt[89] == '%' && fmt[90] == 'p') ? 1 : 0) + \

312 ((sizeof(fmt) >= 92 && fmt[89] != '%' && fmt[90] == '%' && fmt[91] == 'p') ? 1 : 0) + \

313 ((sizeof(fmt) >= 93 && fmt[90] != '%' && fmt[91] == '%' && fmt[92] == 'p') ? 1 : 0) + \

314 ((sizeof(fmt) >= 94 && fmt[91] != '%' && fmt[92] == '%' && fmt[93] == 'p') ? 1 : 0) + \

315 ((sizeof(fmt) >= 95 && fmt[92] != '%' && fmt[93] == '%' && fmt[94] == 'p') ? 1 : 0) + \

316 ((sizeof(fmt) >= 96 && fmt[93] != '%' && fmt[94] == '%' && fmt[95] == 'p') ? 1 : 0) + \

317 ((sizeof(fmt) >= 97 && fmt[94] != '%' && fmt[95] == '%' && fmt[96] == 'p') ? 1 : 0) + \

318 ((sizeof(fmt) >= 98 && fmt[95] != '%' && fmt[96] == '%' && fmt[97] == 'p') ? 1 : 0) + \

319 ((sizeof(fmt) >= 99 && fmt[96] != '%' && fmt[97] == '%' && fmt[98] == 'p') ? 1 : 0) + \

320 ((sizeof(fmt) >= 100 && fmt[97] != '%' && fmt[98] == '%' && fmt[99] == 'p') ? 1 : 0) + \

321 ((sizeof(fmt) >= 101 && fmt[98] != '%' && fmt[99] == '%' && fmt[100] == 'p') ? 1 : 0) + \

322 ((sizeof(fmt) >= 102 && fmt[99] != '%' && fmt[100] == '%' && fmt[101] == 'p') ? 1 : 0) + \

323 ((sizeof(fmt) >= 103 && fmt[100] != '%' && fmt[101] == '%' && fmt[102] == 'p') ? 1 : 0) + \

324 ((sizeof(fmt) >= 104 && fmt[101] != '%' && fmt[102] == '%' && fmt[103] == 'p') ? 1 : 0) + \

325 ((sizeof(fmt) >= 105 && fmt[102] != '%' && fmt[103] == '%' && fmt[104] == 'p') ? 1 : 0) + \

326 ((sizeof(fmt) >= 106 && fmt[103] != '%' && fmt[104] == '%' && fmt[105] == 'p') ? 1 : 0) + \

327 ((sizeof(fmt) >= 107 && fmt[104] != '%' && fmt[105] == '%' && fmt[106] == 'p') ? 1 : 0) + \

328 ((sizeof(fmt) >= 108 && fmt[105] != '%' && fmt[106] == '%' && fmt[107] == 'p') ? 1 : 0) + \

329 ((sizeof(fmt) >= 109 && fmt[106] != '%' && fmt[107] == '%' && fmt[108] == 'p') ? 1 : 0) + \

330 ((sizeof(fmt) >= 110 && fmt[107] != '%' && fmt[108] == '%' && fmt[109] == 'p') ? 1 : 0) + \

331 ((sizeof(fmt) >= 111 && fmt[108] != '%' && fmt[109] == '%' && fmt[110] == 'p') ? 1 : 0) + \

332 ((sizeof(fmt) >= 112 && fmt[109] != '%' && fmt[110] == '%' && fmt[111] == 'p') ? 1 : 0) + \

333 ((sizeof(fmt) >= 113 && fmt[110] != '%' && fmt[111] == '%' && fmt[112] == 'p') ? 1 : 0) + \

334 ((sizeof(fmt) >= 114 && fmt[111] != '%' && fmt[112] == '%' && fmt[113] == 'p') ? 1 : 0) + \

335 ((sizeof(fmt) >= 115 && fmt[112] != '%' && fmt[113] == '%' && fmt[114] == 'p') ? 1 : 0) + \

336 ((sizeof(fmt) >= 116 && fmt[113] != '%' && fmt[114] == '%' && fmt[115] == 'p') ? 1 : 0) + \

337 ((sizeof(fmt) >= 117 && fmt[114] != '%' && fmt[115] == '%' && fmt[116] == 'p') ? 1 : 0) + \

338 ((sizeof(fmt) >= 118 && fmt[115] != '%' && fmt[116] == '%' && fmt[117] == 'p') ? 1 : 0) + \

339 ((sizeof(fmt) >= 119 && fmt[116] != '%' && fmt[117] == '%' && fmt[118] == 'p') ? 1 : 0) + \

340 ((sizeof(fmt) >= 120 && fmt[117] != '%' && fmt[118] == '%' && fmt[119] == 'p') ? 1 : 0) + \

341 ((sizeof(fmt) >= 121 && fmt[118] != '%' && fmt[119] == '%' && fmt[120] == 'p') ? 1 : 0) + \

342 ((sizeof(fmt) >= 122 && fmt[119] != '%' && fmt[120] == '%' && fmt[121] == 'p') ? 1 : 0) + \

343 ((sizeof(fmt) >= 123 && fmt[120] != '%' && fmt[121] == '%' && fmt[122] == 'p') ? 1 : 0) + \

344 ((sizeof(fmt) >= 124 && fmt[121] != '%' && fmt[122] == '%' && fmt[123] == 'p') ? 1 : 0) + \

345 ((sizeof(fmt) >= 125 && fmt[122] != '%' && fmt[123] == '%' && fmt[124] == 'p') ? 1 : 0) + \

346 ((sizeof(fmt) >= 126 && fmt[123] != '%' && fmt[124] == '%' && fmt[125] == 'p') ? 1 : 0) + \

347 ((sizeof(fmt) >= 127 && fmt[124] != '%' && fmt[125] == '%' && fmt[126] == 'p') ? 1 : 0) + \

348 ((sizeof(fmt) >= 128 && fmt[125] != '%' && fmt[126] == '%' && fmt[127] == 'p') ? 1 : 0) + \

349 ((sizeof(fmt) >= 129 && fmt[126] != '%' && fmt[127] == '%' && fmt[128] == 'p') ? 1 : 0) + \

350 ((sizeof(fmt) >= 130 && fmt[127] != '%' && fmt[128] == '%' && fmt[129] == 'p') ? 1 : 0) + \

351 ((sizeof(fmt) >= 131 && fmt[128] != '%' && fmt[129] == '%' && fmt[130] == 'p') ? 1 : 0) + \

352 ((sizeof(fmt) >= 132 && fmt[129] != '%' && fmt[130] == '%' && fmt[131] == 'p') ? 1 : 0) + \

353 ((sizeof(fmt) >= 133 && fmt[130] != '%' && fmt[131] == '%' && fmt[132] == 'p') ? 1 : 0) + \

354 ((sizeof(fmt) >= 134 && fmt[131] != '%' && fmt[132] == '%' && fmt[133] == 'p') ? 1 : 0) + \

355 ((sizeof(fmt) >= 135 && fmt[132] != '%' && fmt[133] == '%' && fmt[134] == 'p') ? 1 : 0) + \

356 ((sizeof(fmt) >= 136 && fmt[133] != '%' && fmt[134] == '%' && fmt[135] == 'p') ? 1 : 0) + \

357 ((sizeof(fmt) >= 137 && fmt[134] != '%' && fmt[135] == '%' && fmt[136] == 'p') ? 1 : 0) + \

358 ((sizeof(fmt) >= 138 && fmt[135] != '%' && fmt[136] == '%' && fmt[137] == 'p') ? 1 : 0) + \

359 ((sizeof(fmt) >= 139 && fmt[136] != '%' && fmt[137] == '%' && fmt[138] == 'p') ? 1 : 0) + \

360 ((sizeof(fmt) >= 140 && fmt[137] != '%' && fmt[138] == '%' && fmt[139] == 'p') ? 1 : 0) + \

361 ((sizeof(fmt) >= 141 && fmt[138] != '%' && fmt[139] == '%' && fmt[140] == 'p') ? 1 : 0) + \

362 ((sizeof(fmt) >= 142 && fmt[139] != '%' && fmt[140] == '%' && fmt[141] == 'p') ? 1 : 0) + \

363 ((sizeof(fmt) >= 143 && fmt[140] != '%' && fmt[141] == '%' && fmt[142] == 'p') ? 1 : 0) + \

364 ((sizeof(fmt) >= 144 && fmt[141] != '%' && fmt[142] == '%' && fmt[143] == 'p') ? 1 : 0) + \

365 ((sizeof(fmt) >= 145 && fmt[142] != '%' && fmt[143] == '%' && fmt[144] == 'p') ? 1 : 0) + \

366 ((sizeof(fmt) >= 146 && fmt[143] != '%' && fmt[144] == '%' && fmt[145] == 'p') ? 1 : 0) + \

367 ((sizeof(fmt) >= 147 && fmt[144] != '%' && fmt[145] == '%' && fmt[146] == 'p') ? 1 : 0) + \

368 ((sizeof(fmt) >= 148 && fmt[145] != '%' && fmt[146] == '%' && fmt[147] == 'p') ? 1 : 0) + \

369 ((sizeof(fmt) >= 149 && fmt[146] != '%' && fmt[147] == '%' && fmt[148] == 'p') ? 1 : 0) + \

370 ((sizeof(fmt) >= 150 && fmt[147] != '%' && fmt[148] == '%' && fmt[149] == 'p') ? 1 : 0) + \

371 ((sizeof(fmt) >= 151 && fmt[148] != '%' && fmt[149] == '%' && fmt[150] == 'p') ? 1 : 0) + \

372 ((sizeof(fmt) >= 152 && fmt[149] != '%' && fmt[150] == '%' && fmt[151] == 'p') ? 1 : 0) + \

373 ((sizeof(fmt) >= 153 && fmt[150] != '%' && fmt[151] == '%' && fmt[152] == 'p') ? 1 : 0) + \

374 ((sizeof(fmt) >= 154 && fmt[151] != '%' && fmt[152] == '%' && fmt[153] == 'p') ? 1 : 0) + \

375 ((sizeof(fmt) >= 155 && fmt[152] != '%' && fmt[153] == '%' && fmt[154] == 'p') ? 1 : 0) + \

376 ((sizeof(fmt) >= 156 && fmt[153] != '%' && fmt[154] == '%' && fmt[155] == 'p') ? 1 : 0) + \

377 ((sizeof(fmt) >= 157 && fmt[154] != '%' && fmt[155] == '%' && fmt[156] == 'p') ? 1 : 0) + \

378 ((sizeof(fmt) >= 158 && fmt[155] != '%' && fmt[156] == '%' && fmt[157] == 'p') ? 1 : 0) + \

379 ((sizeof(fmt) >= 159 && fmt[156] != '%' && fmt[157] == '%' && fmt[158] == 'p') ? 1 : 0) + \

380 ((sizeof(fmt) >= 160 && fmt[157] != '%' && fmt[158] == '%' && fmt[159] == 'p') ? 1 : 0) + \

381 ((sizeof(fmt) >= 161 && fmt[158] != '%' && fmt[159] == '%' && fmt[160] == 'p') ? 1 : 0) + \

382 ((sizeof(fmt) >= 162 && fmt[159] != '%' && fmt[160] == '%' && fmt[161] == 'p') ? 1 : 0) + \

383 ((sizeof(fmt) >= 163 && fmt[160] != '%' && fmt[161] == '%' && fmt[162] == 'p') ? 1 : 0) + \

384 ((sizeof(fmt) >= 164 && fmt[161] != '%' && fmt[162] == '%' && fmt[163] == 'p') ? 1 : 0) + \

385 ((sizeof(fmt) >= 165 && fmt[162] != '%' && fmt[163] == '%' && fmt[164] == 'p') ? 1 : 0) + \

386 ((sizeof(fmt) >= 166 && fmt[163] != '%' && fmt[164] == '%' && fmt[165] == 'p') ? 1 : 0) + \

387 ((sizeof(fmt) >= 167 && fmt[164] != '%' && fmt[165] == '%' && fmt[166] == 'p') ? 1 : 0) + \

388 ((sizeof(fmt) >= 168 && fmt[165] != '%' && fmt[166] == '%' && fmt[167] == 'p') ? 1 : 0) + \

389 ((sizeof(fmt) >= 169 && fmt[166] != '%' && fmt[167] == '%' && fmt[168] == 'p') ? 1 : 0) + \

390 ((sizeof(fmt) >= 170 && fmt[167] != '%' && fmt[168] == '%' && fmt[169] == 'p') ? 1 : 0) + \

391 ((sizeof(fmt) >= 171 && fmt[168] != '%' && fmt[169] == '%' && fmt[170] == 'p') ? 1 : 0) + \

392 ((sizeof(fmt) >= 172 && fmt[169] != '%' && fmt[170] == '%' && fmt[171] == 'p') ? 1 : 0) + \

393 ((sizeof(fmt) >= 173 && fmt[170] != '%' && fmt[171] == '%' && fmt[172] == 'p') ? 1 : 0) + \

394 ((sizeof(fmt) >= 174 && fmt[171] != '%' && fmt[172] == '%' && fmt[173] == 'p') ? 1 : 0) + \

395 ((sizeof(fmt) >= 175 && fmt[172] != '%' && fmt[173] == '%' && fmt[174] == 'p') ? 1 : 0) + \

396 ((sizeof(fmt) >= 176 && fmt[173] != '%' && fmt[174] == '%' && fmt[175] == 'p') ? 1 : 0) + \

397 ((sizeof(fmt) >= 177 && fmt[174] != '%' && fmt[175] == '%' && fmt[176] == 'p') ? 1 : 0) + \

398 ((sizeof(fmt) >= 178 && fmt[175] != '%' && fmt[176] == '%' && fmt[177] == 'p') ? 1 : 0) + \

399 ((sizeof(fmt) >= 179 && fmt[176] != '%' && fmt[177] == '%' && fmt[178] == 'p') ? 1 : 0) + \

400 ((sizeof(fmt) >= 180 && fmt[177] != '%' && fmt[178] == '%' && fmt[179] == 'p') ? 1 : 0) + \

401 ((sizeof(fmt) >= 181 && fmt[178] != '%' && fmt[179] == '%' && fmt[180] == 'p') ? 1 : 0) + \

402 ((sizeof(fmt) >= 182 && fmt[179] != '%' && fmt[180] == '%' && fmt[181] == 'p') ? 1 : 0) + \

403 ((sizeof(fmt) >= 183 && fmt[180] != '%' && fmt[181] == '%' && fmt[182] == 'p') ? 1 : 0) + \

404 ((sizeof(fmt) >= 184 && fmt[181] != '%' && fmt[182] == '%' && fmt[183] == 'p') ? 1 : 0) + \

405 ((sizeof(fmt) >= 185 && fmt[182] != '%' && fmt[183] == '%' && fmt[184] == 'p') ? 1 : 0) + \

406 ((sizeof(fmt) >= 186 && fmt[183] != '%' && fmt[184] == '%' && fmt[185] == 'p') ? 1 : 0) + \

407 ((sizeof(fmt) >= 187 && fmt[184] != '%' && fmt[185] == '%' && fmt[186] == 'p') ? 1 : 0) + \

408 ((sizeof(fmt) >= 188 && fmt[185] != '%' && fmt[186] == '%' && fmt[187] == 'p') ? 1 : 0) + \

409 ((sizeof(fmt) >= 189 && fmt[186] != '%' && fmt[187] == '%' && fmt[188] == 'p') ? 1 : 0) + \

410 ((sizeof(fmt) >= 190 && fmt[187] != '%' && fmt[188] == '%' && fmt[189] == 'p') ? 1 : 0) + \

411 ((sizeof(fmt) >= 191 && fmt[188] != '%' && fmt[189] == '%' && fmt[190] == 'p') ? 1 : 0) + \

412 ((sizeof(fmt) >= 192 && fmt[189] != '%' && fmt[190] == '%' && fmt[191] == 'p') ? 1 : 0) + \

413 ((sizeof(fmt) >= 193 && fmt[190] != '%' && fmt[191] == '%' && fmt[192] == 'p') ? 1 : 0) + \

414 ((sizeof(fmt) >= 194 && fmt[191] != '%' && fmt[192] == '%' && fmt[193] == 'p') ? 1 : 0) + \

415 ((sizeof(fmt) >= 195 && fmt[192] != '%' && fmt[193] == '%' && fmt[194] == 'p') ? 1 : 0) + \

416 ((sizeof(fmt) >= 196 && fmt[193] != '%' && fmt[194] == '%' && fmt[195] == 'p') ? 1 : 0) + \

417 ((sizeof(fmt) >= 197 && fmt[194] != '%' && fmt[195] == '%' && fmt[196] == 'p') ? 1 : 0) + \

418 ((sizeof(fmt) >= 198 && fmt[195] != '%' && fmt[196] == '%' && fmt[197] == 'p') ? 1 : 0) + \

419 ((sizeof(fmt) >= 199 && fmt[196] != '%' && fmt[197] == '%' && fmt[198] == 'p') ? 1 : 0) + \

420 ((sizeof(fmt) >= 200 && fmt[197] != '%' && fmt[198] == '%' && fmt[199] == 'p') ? 1 : 0) + \

421 ((sizeof(fmt) >= 201 && fmt[198] != '%' && fmt[199] == '%' && fmt[200] == 'p') ? 1 : 0) + \

422 ((sizeof(fmt) >= 202 && fmt[199] != '%' && fmt[200] == '%' && fmt[201] == 'p') ? 1 : 0) + \

423 ((sizeof(fmt) >= 203 && fmt[200] != '%' && fmt[201] == '%' && fmt[202] == 'p') ? 1 : 0) + \

424 ((sizeof(fmt) >= 204 && fmt[201] != '%' && fmt[202] == '%' && fmt[203] == 'p') ? 1 : 0) + \

425 ((sizeof(fmt) >= 205 && fmt[202] != '%' && fmt[203] == '%' && fmt[204] == 'p') ? 1 : 0) + \

426 ((sizeof(fmt) >= 206 && fmt[203] != '%' && fmt[204] == '%' && fmt[205] == 'p') ? 1 : 0) + \

427 ((sizeof(fmt) >= 207 && fmt[204] != '%' && fmt[205] == '%' && fmt[206] == 'p') ? 1 : 0) + \

428 ((sizeof(fmt) >= 208 && fmt[205] != '%' && fmt[206] == '%' && fmt[207] == 'p') ? 1 : 0) + \

429 ((sizeof(fmt) >= 209 && fmt[206] != '%' && fmt[207] == '%' && fmt[208] == 'p') ? 1 : 0) + \

430 ((sizeof(fmt) >= 210 && fmt[207] != '%' && fmt[208] == '%' && fmt[209] == 'p') ? 1 : 0) + \

431 ((sizeof(fmt) >= 211 && fmt[208] != '%' && fmt[209] == '%' && fmt[210] == 'p') ? 1 : 0) + \

432 ((sizeof(fmt) >= 212 && fmt[209] != '%' && fmt[210] == '%' && fmt[211] == 'p') ? 1 : 0) + \

433 ((sizeof(fmt) >= 213 && fmt[210] != '%' && fmt[211] == '%' && fmt[212] == 'p') ? 1 : 0) + \

434 ((sizeof(fmt) >= 214 && fmt[211] != '%' && fmt[212] == '%' && fmt[213] == 'p') ? 1 : 0) + \

435 ((sizeof(fmt) >= 215 && fmt[212] != '%' && fmt[213] == '%' && fmt[214] == 'p') ? 1 : 0) + \

436 ((sizeof(fmt) >= 216 && fmt[213] != '%' && fmt[214] == '%' && fmt[215] == 'p') ? 1 : 0) + \

437 ((sizeof(fmt) >= 217 && fmt[214] != '%' && fmt[215] == '%' && fmt[216] == 'p') ? 1 : 0) + \

438 ((sizeof(fmt) >= 218 && fmt[215] != '%' && fmt[216] == '%' && fmt[217] == 'p') ? 1 : 0) + \

439 ((sizeof(fmt) >= 219 && fmt[216] != '%' && fmt[217] == '%' && fmt[218] == 'p') ? 1 : 0) + \

440 ((sizeof(fmt) >= 220 && fmt[217] != '%' && fmt[218] == '%' && fmt[219] == 'p') ? 1 : 0) + \

441 ((sizeof(fmt) >= 221 && fmt[218] != '%' && fmt[219] == '%' && fmt[220] == 'p') ? 1 : 0) + \

442 ((sizeof(fmt) >= 222 && fmt[219] != '%' && fmt[220] == '%' && fmt[221] == 'p') ? 1 : 0) + \

443 ((sizeof(fmt) >= 223 && fmt[220] != '%' && fmt[221] == '%' && fmt[222] == 'p') ? 1 : 0) + \

444 ((sizeof(fmt) >= 224 && fmt[221] != '%' && fmt[222] == '%' && fmt[223] == 'p') ? 1 : 0) + \

445 ((sizeof(fmt) >= 225 && fmt[222] != '%' && fmt[223] == '%' && fmt[224] == 'p') ? 1 : 0) + \

446 ((sizeof(fmt) >= 226 && fmt[223] != '%' && fmt[224] == '%' && fmt[225] == 'p') ? 1 : 0) + \

447 ((sizeof(fmt) >= 227 && fmt[224] != '%' && fmt[225] == '%' && fmt[226] == 'p') ? 1 : 0) + \

448 ((sizeof(fmt) >= 228 && fmt[225] != '%' && fmt[226] == '%' && fmt[227] == 'p') ? 1 : 0) + \

449 ((sizeof(fmt) >= 229 && fmt[226] != '%' && fmt[227] == '%' && fmt[228] == 'p') ? 1 : 0) + \

450 ((sizeof(fmt) >= 230 && fmt[227] != '%' && fmt[228] == '%' && fmt[229] == 'p') ? 1 : 0) + \

451 ((sizeof(fmt) >= 231 && fmt[228] != '%' && fmt[229] == '%' && fmt[230] == 'p') ? 1 : 0) + \

452 ((sizeof(fmt) >= 232 && fmt[229] != '%' && fmt[230] == '%' && fmt[231] == 'p') ? 1 : 0) + \

453 ((sizeof(fmt) >= 233 && fmt[230] != '%' && fmt[231] == '%' && fmt[232] == 'p') ? 1 : 0) + \

454 ((sizeof(fmt) >= 234 && fmt[231] != '%' && fmt[232] == '%' && fmt[233] == 'p') ? 1 : 0) + \

455 ((sizeof(fmt) >= 235 && fmt[232] != '%' && fmt[233] == '%' && fmt[234] == 'p') ? 1 : 0) + \

456 ((sizeof(fmt) >= 236 && fmt[233] != '%' && fmt[234] == '%' && fmt[235] == 'p') ? 1 : 0) + \

457 ((sizeof(fmt) >= 237 && fmt[234] != '%' && fmt[235] == '%' && fmt[236] == 'p') ? 1 : 0) + \

458 ((sizeof(fmt) >= 238 && fmt[235] != '%' && fmt[236] == '%' && fmt[237] == 'p') ? 1 : 0) + \

459 ((sizeof(fmt) >= 239 && fmt[236] != '%' && fmt[237] == '%' && fmt[238] == 'p') ? 1 : 0) + \

460 ((sizeof(fmt) >= 240 && fmt[237] != '%' && fmt[238] == '%' && fmt[239] == 'p') ? 1 : 0) + \

461 ((sizeof(fmt) >= 241 && fmt[238] != '%' && fmt[239] == '%' && fmt[240] == 'p') ? 1 : 0) + \

462 ((sizeof(fmt) >= 242 && fmt[239] != '%' && fmt[240] == '%' && fmt[241] == 'p') ? 1 : 0) + \

463 ((sizeof(fmt) >= 243 && fmt[240] != '%' && fmt[241] == '%' && fmt[242] == 'p') ? 1 : 0) + \

464 ((sizeof(fmt) >= 244 && fmt[241] != '%' && fmt[242] == '%' && fmt[243] == 'p') ? 1 : 0) + \

465 ((sizeof(fmt) >= 245 && fmt[242] != '%' && fmt[243] == '%' && fmt[244] == 'p') ? 1 : 0) + \

466 ((sizeof(fmt) >= 246 && fmt[243] != '%' && fmt[244] == '%' && fmt[245] == 'p') ? 1 : 0) + \

467 ((sizeof(fmt) >= 247 && fmt[244] != '%' && fmt[245] == '%' && fmt[246] == 'p') ? 1 : 0) + \

468 ((sizeof(fmt) >= 248 && fmt[245] != '%' && fmt[246] == '%' && fmt[247] == 'p') ? 1 : 0) + \

469 ((sizeof(fmt) >= 249 && fmt[246] != '%' && fmt[247] == '%' && fmt[248] == 'p') ? 1 : 0) + \

470 ((sizeof(fmt) >= 250 && fmt[247] != '%' && fmt[248] == '%' && fmt[249] == 'p') ? 1 : 0) + \

471 ((sizeof(fmt) >= 251 && fmt[248] != '%' && fmt[249] == '%' && fmt[250] == 'p') ? 1 : 0) + \

472 ((sizeof(fmt) >= 252 && fmt[249] != '%' && fmt[250] == '%' && fmt[251] == 'p') ? 1 : 0) + \

473 ((sizeof(fmt) >= 253 && fmt[250] != '%' && fmt[251] == '%' && fmt[252] == 'p') ? 1 : 0) + \

474 ((sizeof(fmt) >= 254 && fmt[251] != '%' && fmt[252] == '%' && fmt[253] == 'p') ? 1 : 0) + \

475 ((sizeof(fmt) >= 255 && fmt[252] != '%' && fmt[253] == '%' && fmt[254] == 'p') ? 1 : 0) + \

476 ((sizeof(fmt) >= 256 && fmt[253] != '%' && fmt[254] == '%' && fmt[255] == 'p') ? 1 : 0)

477

495#define Z\_CBPRINTF\_POINTERS\_VALIDATE(...) \

496 (Z\_CBPRINTF\_NONE\_CHAR\_PTR\_COUNT(\_\_VA\_ARGS\_\_) == \

497 Z\_CBPRINTF\_P\_COUNT(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)))

498

499/\* @brief Check if argument is a certain type of char pointer. What exactly is checked

500 \* depends on @p flags. If flags is 0 then 1 is returned if @p x is a char pointer.

501 \*

502 \* @param idx Argument index.

503 \* @param x Argument.

504 \* @param flags Flags. See @p CBPRINTF\_PACKAGE\_FLAGS.

505 \*

506 \* @retval 1 if @p x is char pointer meeting criteria identified by @p flags.

507 \* @retval 0 otherwise.

508 \*/

509#define Z\_CBPRINTF\_IS\_X\_PCHAR(idx, x, flags) \

510 (idx < Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT\_GET(flags) ? \

511 0 : Z\_CBPRINTF\_IS\_PCHAR(x, flags))

512

521#define Z\_CBPRINTF\_HAS\_PCHAR\_ARGS(flags, fmt, ...) \

522 (FOR\_EACH\_IDX\_FIXED\_ARG(Z\_CBPRINTF\_IS\_X\_PCHAR, (+), flags, \_\_VA\_ARGS\_\_))

523

524#define Z\_CBPRINTF\_PCHAR\_COUNT(flags, ...) \

525 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

526 (0), \

527 (Z\_CBPRINTF\_HAS\_PCHAR\_ARGS(flags, \_\_VA\_ARGS\_\_)))

528

537#if Z\_C\_GENERIC

538#define Z\_CBPRINTF\_MUST\_RUNTIME\_PACKAGE(flags, ...) ({\

539 int \_rv; \

540 if ((flags) & CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS) { \

541 \_rv = 0; \

542 } else { \

543 \_rv = Z\_CBPRINTF\_PCHAR\_COUNT(flags, \_\_VA\_ARGS\_\_) > 0 ? 1 : 0; \

544 } \

545 \_rv; \

546})

547#else

548#define Z\_CBPRINTF\_MUST\_RUNTIME\_PACKAGE(flags, ...) 1

549#endif

550

560#ifdef \_\_cplusplus

561#define Z\_CBPRINTF\_ARG\_SIZE(v) z\_cbprintf\_cxx\_arg\_size(v)

562#else

563#define Z\_CONSTIFY(v) ({ \

564 \_\_auto\_type \_uv = (v); \

565 \_\_typeof\_\_(\_uv) const \_cv = \_uv; \

566 \_cv; \

567})

568#define Z\_CBPRINTF\_ARG\_SIZE(v) ({\

569 \_\_auto\_type \_\_v = Z\_ARGIFY(Z\_CONSTIFY(v)); \

570 /\* Static code analysis may complain about unused variable. \*/ \

571 (void)\_\_v; \

572 size\_t \_\_arg\_size = \_Generic((v), \

573 float : sizeof(double), \

574 default : \

575 sizeof((\_\_v)) /\* NOLINT(bugprone-sizeof-expression) \*/ \

576 ); \

577 \_\_arg\_size; \

578})

579#endif

580

587#ifdef \_\_cplusplus

588#define Z\_CBPRINTF\_STORE\_ARG(buf, arg) z\_cbprintf\_cxx\_store\_arg(buf, arg)

589#else

590#define Z\_CBPRINTF\_STORE\_ARG(buf, arg) do { \

591 if (Z\_CBPRINTF\_VA\_STACK\_LL\_DBL\_MEMCPY) { \

592 /\* If required, copy arguments by word to avoid unaligned access.\*/ \

593 \_\_auto\_type \_v = Z\_ARGIFY(Z\_CONSTIFY(arg)); \

594 double \_d = \_Generic(Z\_ARGIFY(arg), \

595 float : Z\_ARGIFY(arg), \

596 default : \

597 0.0); \

598 /\* Static code analysis may complain about unused variable. \*/ \

599 (void)\_v; \

600 (void)\_d; \

601 size\_t arg\_size = Z\_CBPRINTF\_ARG\_SIZE(arg); \

602 size\_t \_wsize = arg\_size / sizeof(int); \

603 z\_cbprintf\_wcpy((int \*)(buf), \

604 (int \*) \_Generic(Z\_ARGIFY(arg), float : &\_d, default : &\_v), \

605 \_wsize); \

606 } else { \

607 \*\_Generic(Z\_ARGIFY(arg), \

608 char : (int \*)(buf), \

609 unsigned char: (int \*)(buf), \

610 short : (int \*)(buf), \

611 unsigned short : (int \*)(buf), \

612 int : (int \*)(buf), \

613 unsigned int : (unsigned int \*)(buf), \

614 long : (long \*)(buf), \

615 unsigned long : (unsigned long \*)(buf), \

616 long long : (long long \*)(buf), \

617 unsigned long long : (unsigned long long \*)(buf), \

618 float : (double \*)(buf), \

619 double : (double \*)(buf), \

620 long double : (long double \*)(buf), \

621 default : \

622 (const void \*\*)(buf)) = (arg); \

623 } \

624} while (false)

625#endif

626

633#ifdef \_\_cplusplus

634#define Z\_CBPRINTF\_ALIGNMENT(\_arg) z\_cbprintf\_cxx\_alignment(\_arg)

635#else

636#define Z\_CBPRINTF\_ALIGNMENT(\_arg) \

637 MAX(\_Generic(Z\_ARGIFY(\_arg), \

638 float : VA\_STACK\_ALIGN(double), \

639 double : VA\_STACK\_ALIGN(double), \

640 long double : VA\_STACK\_ALIGN(long double), \

641 long long : VA\_STACK\_ALIGN(long long), \

642 unsigned long long : VA\_STACK\_ALIGN(long long), \

643 default : \

644 \_\_alignof\_\_(Z\_ARGIFY(\_arg))), VA\_STACK\_MIN\_ALIGN)

645#endif

646

657#ifdef \_\_cplusplus

658#if defined(\_\_x86\_64\_\_) || defined(\_\_riscv) || defined(\_\_aarch64\_\_)

659#define Z\_CBPRINTF\_IS\_LONGDOUBLE(x) 0

660#else

661#define Z\_CBPRINTF\_IS\_LONGDOUBLE(x) z\_cbprintf\_cxx\_is\_longdouble(x)

662#endif

663#else

664#define Z\_CBPRINTF\_IS\_LONGDOUBLE(x) \

665 \_Generic(Z\_ARGIFY(x), long double : 1, default : 0)

666#endif

667

683#define Z\_CBPRINTF\_PACK\_ARG2(arg\_idx, \_buf, \_idx, \_align\_offset, \_max, \_arg) \

684do { \

685 BUILD\_ASSERT(!((sizeof(double) < VA\_STACK\_ALIGN(long double)) && \

686 Z\_CBPRINTF\_IS\_LONGDOUBLE(\_arg) && \

687 !IS\_ENABLED(CONFIG\_CBPRINTF\_PACKAGE\_LONGDOUBLE)),\

688 "Packaging of long double not enabled in Kconfig."); \

689 while (((\_align\_offset) % Z\_CBPRINTF\_ALIGNMENT(\_arg)) != 0UL) { \

690 (\_idx) += sizeof(int); \

691 (\_align\_offset) += sizeof(int); \

692 } \

693 uint32\_t \_arg\_size = Z\_CBPRINTF\_ARG\_SIZE(\_arg); \

694 uint8\_t \_loc = (uint8\_t)(\_idx / sizeof(int)); \

695 if (arg\_idx < 1 + \_fros\_cnt) { \

696 if (\_ros\_pos\_en) { \

697 \_ros\_pos\_buf[\_ros\_pos\_idx++] = \_loc; \

698 } \

699 } else if (Z\_CBPRINTF\_IS\_PCHAR(\_arg, 0)) { \

700 if (\_cros\_en) { \

701 if (Z\_CBPRINTF\_IS\_X\_PCHAR(arg\_idx, \_arg, \_flags)) { \

702 if (\_rws\_pos\_en) { \

703 \_rws\_buffer[\_rws\_pos\_idx++] = arg\_idx - 1; \

704 \_rws\_buffer[\_rws\_pos\_idx++] = \_loc; \

705 } \

706 } else { \

707 if (\_ros\_pos\_en) { \

708 \_ros\_pos\_buf[\_ros\_pos\_idx++] = \_loc; \

709 } \

710 } \

711 } else if (\_rws\_pos\_en) { \

712 \_rws\_buffer[\_rws\_pos\_idx++] = arg\_idx - 1; \

713 \_rws\_buffer[\_rws\_pos\_idx++] = (uint8\_t)(\_idx / sizeof(int)); \

714 } \

715 } \

716 if ((\_buf) && (\_idx) < (int)(\_max)) { \

717 Z\_CBPRINTF\_STORE\_ARG(&(\_buf)[(\_idx)], \_arg); \

718 } \

719 (\_idx) += (\_arg\_size); \

720 (\_align\_offset) += (\_arg\_size); \

721} while (false)

722

729#define Z\_CBPRINTF\_PACK\_ARG(arg\_idx, arg) \

730 Z\_CBPRINTF\_PACK\_ARG2(arg\_idx, \_pbuf, \_pkg\_len, \_pkg\_offset, \_pmax, arg)

731

732/\* Allocation to avoid using VLA and alloca. Alloc frees space when leaving

733 \* a function which can lead to increased stack usage if logging is used

734 \* multiple times. VLA is not always available.

735 \*

736 \* Use large array when optimization is off to avoid increased stack usage.

737 \*/

738#ifdef CONFIG\_NO\_OPTIMIZATIONS

739#define Z\_CBPRINTF\_ON\_STACK\_ALLOC(\_name, \_len) \

740 \_\_ASSERT(\_len <= 32, "Too many string arguments."); \

741 uint8\_t \_name##\_buf32[32]; \

742 \_name = \_name##\_buf32

743#else

744#define Z\_CBPRINTF\_ON\_STACK\_ALLOC(\_name, \_len) \

745 \_\_ASSERT(\_len <= 32, "Too many string arguments."); \

746 uint8\_t \_name##\_buf4[4]; \

747 uint8\_t \_name##\_buf8[8]; \

748 uint8\_t \_name##\_buf12[12]; \

749 uint8\_t \_name##\_buf16[16]; \

750 uint8\_t \_name##\_buf32[32]; \

751 \_name = (\_len) <= 4 ? \_name##\_buf4 : \

752 ((\_len) <= 8 ? \_name##\_buf8 : \

753 ((\_len) <= 12 ? \_name##\_buf12 : \

754 ((\_len) <= 16 ? \_name##\_buf16 : \

755 \_name##\_buf32)))

756#endif

757

758/\* On Xtensa the cbprintf\_package\_desc requires

759 \* an additional alignment array. This creates an

760 \* initial value to hush the compiler when compiling

761 \* with C++.

762 \*/

763#if defined(CONFIG\_XTENSA) && defined(\_\_cplusplus)

764#define Z\_CBPRINTF\_XTENSA\_PKG\_DESC\_PADDING\_INITIALIZER .xtensa\_padding = { },

765#else

766#define Z\_CBPRINTF\_XTENSA\_PKG\_DESC\_PADDING\_INITIALIZER

767#endif

768

784#define Z\_CBPRINTF\_STATIC\_PACKAGE\_GENERIC(buf, \_inlen, \_outlen, \_align\_offset, \

785 flags, ... /\* fmt, ... \*/) \

786do { \

787 BUILD\_ASSERT(!IS\_ENABLED(CONFIG\_XTENSA) || \

788 (IS\_ENABLED(CONFIG\_XTENSA) && \

789 !((\_align\_offset) % CBPRINTF\_PACKAGE\_ALIGNMENT)), \

790 "Xtensa requires aligned package."); \

791 BUILD\_ASSERT(((\_align\_offset) % sizeof(int)) == 0, \

792 "Alignment offset must be multiply of a word."); \

793 IF\_ENABLED(CONFIG\_CBPRINTF\_STATIC\_PACKAGE\_CHECK\_ALIGNMENT, \

794 (\_\_ASSERT(!((uintptr\_t)buf & (CBPRINTF\_PACKAGE\_ALIGNMENT - 1)), \

795 "Buffer must be aligned.");)) \

796 uint32\_t \_flags = flags; \

797 bool \_ros\_pos\_en = (\_flags) & CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS; \

798 bool \_rws\_pos\_en = (\_flags) & CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS; \

799 bool \_cros\_en = (\_flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO; \

800 uint8\_t \*\_pbuf = (buf); \

801 uint8\_t \_rws\_pos\_idx = 0; \

802 uint8\_t \_ros\_pos\_idx = 0; \

803 /\* Variable holds count of all string pointer arguments. \*/ \

804 uint8\_t \_alls\_cnt = Z\_CBPRINTF\_PCHAR\_COUNT(0, \_\_VA\_ARGS\_\_); \

805 uint8\_t \_fros\_cnt = Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT\_GET(\_flags); \

806 /\* Variable holds count of non const string pointers. \*/ \

807 uint8\_t \_rws\_cnt = \_cros\_en ? \

808 Z\_CBPRINTF\_PCHAR\_COUNT(\_flags, \_\_VA\_ARGS\_\_) : \_alls\_cnt - \_fros\_cnt; \

809 uint8\_t \_ros\_cnt = \_ros\_pos\_en ? (1 + \_alls\_cnt - \_rws\_cnt) : 0; \

810 uint8\_t \*\_ros\_pos\_buf; \

811 Z\_CBPRINTF\_ON\_STACK\_ALLOC(\_ros\_pos\_buf, \_ros\_cnt); \

812 uint8\_t \*\_rws\_buffer; \

813 Z\_CBPRINTF\_ON\_STACK\_ALLOC(\_rws\_buffer, 2 \* \_rws\_cnt); \

814 size\_t \_pmax = !is\_null\_no\_warn(buf) ? \_inlen : INT32\_MAX; \

815 int \_pkg\_len = 0; \

816 int \_total\_len = 0; \

817 int \_pkg\_offset = (\_align\_offset); \

818 union cbprintf\_package\_hdr \*\_len\_loc; \

819 /\* If string has rw string arguments CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS is a must. \*/ \

820 if (\_rws\_cnt && !((\_flags) & CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS)) { \

821 \_outlen = -EINVAL; \

822 break; \

823 } \

824 /\* package starts with string address and field with length \*/ \

825 if (\_pmax < sizeof(\*\_len\_loc)) { \

826 (\_outlen) = -ENOSPC; \

827 break; \

828 } \

829 \_len\_loc = (union cbprintf\_package\_hdr \*)\_pbuf; \

830 \_pkg\_len += sizeof(\*\_len\_loc); \

831 \_pkg\_offset += sizeof(\*\_len\_loc); \

832 /\* Pack remaining arguments \*/\

833 FOR\_EACH\_IDX(Z\_CBPRINTF\_PACK\_ARG, (;), \_\_VA\_ARGS\_\_);\

834 \_total\_len = \_pkg\_len; \

835 /\* Append string indexes to the package. \*/ \

836 \_total\_len += \_ros\_cnt; \

837 \_total\_len += 2 \* \_rws\_cnt; \

838 if (\_pbuf != NULL) { \

839 /\* Append string locations. \*/ \

840 uint8\_t \*\_pbuf\_loc = &\_pbuf[\_pkg\_len]; \

841 for (size\_t \_ros\_idx = 0; \_ros\_idx < \_ros\_cnt; \_ros\_idx++) { \

842 \*\_pbuf\_loc++ = \_ros\_pos\_buf[\_ros\_idx]; \

843 } \

844 for (size\_t \_rws\_idx = 0; \_rws\_idx < (2 \* \_rws\_cnt); \_rws\_idx++) { \

845 \*\_pbuf\_loc++ = \_rws\_buffer[\_rws\_idx]; \

846 } \

847 } \

848 /\* Store length \*/ \

849 (\_outlen) = (\_total\_len > (int)\_pmax) ? -ENOSPC : \_total\_len; \

850 /\* Store length in the header, set number of dumped strings to 0 \*/ \

851 if (\_pbuf != NULL) { \

852 union cbprintf\_package\_hdr pkg\_hdr = { \

853 .desc = { \

854 .len = (uint8\_t)(\_pkg\_len / sizeof(int)), \

855 .str\_cnt = 0, \

856 .ro\_str\_cnt = \_ros\_cnt, \

857 .rw\_str\_cnt = \_rws\_cnt, \

858 Z\_CBPRINTF\_XTENSA\_PKG\_DESC\_PADDING\_INITIALIZER \

859 } \

860 }; \

861 IF\_ENABLED(CONFIG\_CBPRINTF\_PACKAGE\_HEADER\_STORE\_CREATION\_FLAGS, \

862 (pkg\_hdr.desc.pkg\_flags = flags)); \

863 \*\_len\_loc = pkg\_hdr; \

864 } \

865} while (false)

866

867#if Z\_C\_GENERIC

868#define Z\_CBPRINTF\_STATIC\_PACKAGE(packaged, inlen, outlen, align\_offset, flags, \

869 ... /\* fmt, ... \*/) \

870 Z\_CBPRINTF\_STATIC\_PACKAGE\_GENERIC(packaged, inlen, outlen, \

871 align\_offset, flags, \_\_VA\_ARGS\_\_)

872#else

873#define Z\_CBPRINTF\_STATIC\_PACKAGE(packaged, inlen, outlen, align\_offset, flags, \

874 ... /\* fmt, ... \*/) \

875do { \

876 /\* Small trick needed to avoid warning on always true \*/ \

877 if (((uintptr\_t)packaged + 1) != 1) { \

878 outlen = cbprintf\_package(packaged, inlen, flags, \_\_VA\_ARGS\_\_); \

879 } else { \

880 outlen = cbprintf\_package(NULL, align\_offset, flags, \_\_VA\_ARGS\_\_); \

881 } \

882} while (false)

883#endif /\* Z\_C\_GENERIC \*/

884

885#ifdef \_\_cplusplus

886}

887#endif

888

889#ifdef CONFIG\_CBPRINTF\_PACKAGE\_SUPPORT\_TAGGED\_ARGUMENTS

890#ifdef \_\_cplusplus

891/\*

892 \* Remove qualifiers like const, volatile. And also transform

893 \* C++ argument reference back to its basic type.

894 \*/

895#define Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg) \

896 z\_cbprintf\_cxx\_remove\_cv < \

897 z\_cbprintf\_cxx\_remove\_reference < decltype(arg) > ::type \

898 > ::type

899

900/\*

901 \* Get the type of elements in an array.

902 \*/

903#define Z\_CBPRINTF\_CXX\_ARG\_ARRAY\_TYPE(arg) \

904 z\_cbprintf\_cxx\_remove\_cv < \

905 z\_cbprintf\_cxx\_remove\_extent < decltype(arg) > ::type \

906 > ::type

907

908/\*

909 \* Determine if incoming type is char.

910 \*/

911#define Z\_CBPRINTF\_CXX\_ARG\_IS\_TYPE\_CHAR(type) \

912 (z\_cbprintf\_cxx\_is\_same\_type < type, \

913 char > :: value ? \

914 true : \

915 (z\_cbprintf\_cxx\_is\_same\_type < type, \

916 const char > :: value ? \

917 true : \

918 (z\_cbprintf\_cxx\_is\_same\_type < type, \

919 volatile char > :: value ? \

920 true : \

921 (z\_cbprintf\_cxx\_is\_same\_type < type, \

922 const volatile char > :: value ? \

923 true : \

924 false))))

925

926/\*

927 \* Figure out if this is a char array since (char \*) and (char[])

928 \* are of different types in C++.

929 \*/

930#define Z\_CBPRINTF\_CXX\_ARG\_IS\_CHAR\_ARRAY(arg) \

931 (z\_cbprintf\_cxx\_is\_array < decltype(arg) > :: value ? \

932 (Z\_CBPRINTF\_CXX\_ARG\_IS\_TYPE\_CHAR(Z\_CBPRINTF\_CXX\_ARG\_ARRAY\_TYPE(arg)) ? \

933 true : \

934 false) : \

935 false)

936

937/\*

938 \* Note that qualifiers of char \* must be explicitly matched

939 \* due to type matching in C++, where remove\_cv() does not work.

940 \*/

941#define Z\_CBPRINTF\_ARG\_TYPE(arg) \

942 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

943 char > ::value ? \

944 CBPRINTF\_PACKAGE\_ARG\_TYPE\_CHAR : \

945 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

946 unsigned char > ::value ? \

947 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_CHAR : \

948 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

949 short > ::value ? \

950 CBPRINTF\_PACKAGE\_ARG\_TYPE\_SHORT : \

951 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

952 unsigned short > ::value ? \

953 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_SHORT : \

954 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

955 int > ::value ? \

956 CBPRINTF\_PACKAGE\_ARG\_TYPE\_INT : \

957 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

958 unsigned int > ::value ? \

959 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_INT : \

960 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

961 long > ::value ? \

962 CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG : \

963 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

964 unsigned long > ::value ? \

965 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG : \

966 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

967 long long > ::value ? \

968 CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_LONG : \

969 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

970 unsigned long long > ::value ? \

971 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG\_LONG : \

972 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

973 float > ::value ? \

974 CBPRINTF\_PACKAGE\_ARG\_TYPE\_FLOAT : \

975 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

976 double > ::value ? \

977 CBPRINTF\_PACKAGE\_ARG\_TYPE\_DOUBLE : \

978 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

979 long double > ::value ? \

980 CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_DOUBLE : \

981 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

982 char \* > :: value ? \

983 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

984 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

985 const char \* > :: value ? \

986 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

987 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

988 volatile char \* > :: value ? \

989 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

990 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

991 const volatile char \* > :: value ? \

992 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

993 (Z\_CBPRINTF\_CXX\_ARG\_IS\_CHAR\_ARRAY(arg) ? \

994 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

995 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID))))))))))))))))))

996#else

997#define Z\_CBPRINTF\_ARG\_TYPE(arg) \

998 \_Generic(arg, \

999 char : CBPRINTF\_PACKAGE\_ARG\_TYPE\_CHAR, \

1000 unsigned char : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_CHAR, \

1001 short : CBPRINTF\_PACKAGE\_ARG\_TYPE\_SHORT, \

1002 unsigned short : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_SHORT, \

1003 int : CBPRINTF\_PACKAGE\_ARG\_TYPE\_INT, \

1004 unsigned int : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_INT, \

1005 long : CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG, \

1006 unsigned long : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG, \

1007 long long : CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_LONG, \

1008 unsigned long long : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG\_LONG, \

1009 float : CBPRINTF\_PACKAGE\_ARG\_TYPE\_FLOAT, \

1010 double : CBPRINTF\_PACKAGE\_ARG\_TYPE\_DOUBLE, \

1011 long double : CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_DOUBLE, \

1012 char \* : CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR, \

1013 const char \* : CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR, \

1014 void \* : CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID, \

1015 default : \

1016 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID \

1017 )

1018#endif /\* \_cplusplus \*/

1019

1020#define Z\_CBPRINTF\_TAGGED\_EMPTY\_ARGS(...) \

1021 CBPRINTF\_PACKAGE\_ARG\_TYPE\_END

1022

1023#define Z\_CBPRINTF\_TAGGED\_ARGS\_3(arg) \

1024 Z\_CBPRINTF\_ARG\_TYPE(arg), arg

1025

1026#define Z\_CBPRINTF\_TAGGED\_ARGS\_2(...) \

1027 FOR\_EACH(Z\_CBPRINTF\_TAGGED\_ARGS\_3, (,), \_\_VA\_ARGS\_\_), \

1028 CBPRINTF\_PACKAGE\_ARG\_TYPE\_END

1029

1030#define Z\_CBPRINTF\_TAGGED\_ARGS(\_num\_args, ...) \

1031 COND\_CODE\_0(\_num\_args, \

1032 (CBPRINTF\_PACKAGE\_ARG\_TYPE\_END), \

1033 (Z\_CBPRINTF\_TAGGED\_ARGS\_2(\_\_VA\_ARGS\_\_)))

1034

1035#endif /\* CONFIG\_CBPRINTF\_PACKAGE\_SUPPORT\_TAGGED\_ARGUMENTS \*/

1036

1037#endif /\* ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_INTERNAL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[cpu.h](arch_2cpu_8h.md)

[cbprintf\_cxx.h](cbprintf__cxx_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[stdint.h](stdint_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [cbprintf\_internal.h](cbprintf__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
