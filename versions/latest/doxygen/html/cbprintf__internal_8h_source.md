---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cbprintf__internal_8h_source.html
original_path: doxygen/html/cbprintf__internal_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

15#include <[zephyr/sys/util.h](util_8h.md)>

16#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

17#include <zephyr/arch/cpu.h>

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

91#ifdef \_\_cplusplus

92#define Z\_CBPRINTF\_IS\_PCHAR(x, flags) \

93 z\_cbprintf\_cxx\_is\_pchar(x, (flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO)

94#else

95#define Z\_CBPRINTF\_IS\_PCHAR(x, flags) \

96 \_Generic((x) + 0, \

97 /\* char \* \*/ \

98 char \* : 1, \

99 const char \* : ((flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO) ? 0 : 1, \

100 volatile char \* : 1, \

101 const volatile char \* : 1, \

102 /\* unsigned char \* \*/ \

103 unsigned char \* : 1, \

104 const unsigned char \* : ((flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO) ? 0 : 1, \

105 volatile unsigned char \* : 1, \

106 const volatile unsigned char \* : 1,\

107 /\* wchar\_t \* \*/ \

108 wchar\_t \* : 1, \

109 const wchar\_t \* : ((flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO) ? 0 : 1, \

110 volatile wchar\_t \* : 1, \

111 const volatile wchar\_t \* : 1, \

112 default : \

113 0)

114#endif

115

123#ifdef \_\_cplusplus

124#define Z\_CBPRINTF\_IS\_WORD\_NUM(x) \

125 z\_cbprintf\_cxx\_is\_word\_num(x)

126#else

127#define Z\_CBPRINTF\_IS\_WORD\_NUM(x) \

128 \_Generic(x, \

129 char : 1, \

130 unsigned char : 1, \

131 short : 1, \

132 unsigned short : 1, \

133 int : 1, \

134 unsigned int : 1, \

135 long : sizeof(long) <= 4, \

136 unsigned long : sizeof(long) <= 4, \

137 default : \

138 0)

139#endif

140

151#ifdef \_\_cplusplus

152#define Z\_CBPRINTF\_IS\_NONE\_CHAR\_PTR(x) z\_cbprintf\_cxx\_is\_none\_char\_ptr(x)

153#else

154#define Z\_CBPRINTF\_IS\_NONE\_CHAR\_PTR(x) \

155 \_Generic((x) + 0, \

156 char \* : 0, \

157 volatile char \* : 0, \

158 const char \* : 0, \

159 const volatile char \* : 0, \

160 unsigned char \* : 0, \

161 volatile unsigned char \* : 0, \

162 const unsigned char \* : 0, \

163 const volatile unsigned char \* : 0, \

164 char: 0, \

165 unsigned char: 0, \

166 short: 0, \

167 unsigned short: 0, \

168 int: 0, \

169 unsigned int: 0,\

170 long: 0, \

171 unsigned long: 0,\

172 long long: 0, \

173 unsigned long long: 0, \

174 float: 0, \

175 double: 0, \

176 default : \

177 1)

178#endif

179

186#define Z\_CBPRINTF\_NONE\_CHAR\_PTR\_ARGS(...) \

187 (FOR\_EACH(Z\_CBPRINTF\_IS\_NONE\_CHAR\_PTR, (+), \_\_VA\_ARGS\_\_)) \

188

195#define Z\_CBPRINTF\_NONE\_CHAR\_PTR\_COUNT(...) \

196 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

197 (0), \

198 (Z\_CBPRINTF\_NONE\_CHAR\_PTR\_ARGS(GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))))

199

213#define Z\_CBPRINTF\_P\_COUNT(fmt, ...) \

214 ((sizeof(fmt) >= 2 && fmt[0] == '%' && fmt[1] == 'p') ? 1 : 0) + \

215 ((sizeof(fmt) >= 3 && fmt[0] != '%' && fmt[1] == '%' && fmt[2] == 'p') ? 1 : 0) + \

216 ((sizeof(fmt) >= 4 && fmt[1] != '%' && fmt[2] == '%' && fmt[3] == 'p') ? 1 : 0) + \

217 ((sizeof(fmt) >= 5 && fmt[2] != '%' && fmt[3] == '%' && fmt[4] == 'p') ? 1 : 0) + \

218 ((sizeof(fmt) >= 6 && fmt[3] != '%' && fmt[4] == '%' && fmt[5] == 'p') ? 1 : 0) + \

219 ((sizeof(fmt) >= 7 && fmt[4] != '%' && fmt[5] == '%' && fmt[6] == 'p') ? 1 : 0) + \

220 ((sizeof(fmt) >= 8 && fmt[5] != '%' && fmt[6] == '%' && fmt[7] == 'p') ? 1 : 0) + \

221 ((sizeof(fmt) >= 9 && fmt[6] != '%' && fmt[7] == '%' && fmt[8] == 'p') ? 1 : 0) + \

222 ((sizeof(fmt) >= 10 && fmt[7] != '%' && fmt[8] == '%' && fmt[9] == 'p') ? 1 : 0) + \

223 ((sizeof(fmt) >= 11 && fmt[8] != '%' && fmt[9] == '%' && fmt[10] == 'p') ? 1 : 0) + \

224 ((sizeof(fmt) >= 12 && fmt[9] != '%' && fmt[10] == '%' && fmt[11] == 'p') ? 1 : 0) + \

225 ((sizeof(fmt) >= 13 && fmt[10] != '%' && fmt[11] == '%' && fmt[12] == 'p') ? 1 : 0) + \

226 ((sizeof(fmt) >= 14 && fmt[11] != '%' && fmt[12] == '%' && fmt[13] == 'p') ? 1 : 0) + \

227 ((sizeof(fmt) >= 15 && fmt[12] != '%' && fmt[13] == '%' && fmt[14] == 'p') ? 1 : 0) + \

228 ((sizeof(fmt) >= 16 && fmt[13] != '%' && fmt[14] == '%' && fmt[15] == 'p') ? 1 : 0) + \

229 ((sizeof(fmt) >= 17 && fmt[14] != '%' && fmt[15] == '%' && fmt[16] == 'p') ? 1 : 0) + \

230 ((sizeof(fmt) >= 18 && fmt[15] != '%' && fmt[16] == '%' && fmt[17] == 'p') ? 1 : 0) + \

231 ((sizeof(fmt) >= 19 && fmt[16] != '%' && fmt[17] == '%' && fmt[18] == 'p') ? 1 : 0) + \

232 ((sizeof(fmt) >= 20 && fmt[17] != '%' && fmt[18] == '%' && fmt[19] == 'p') ? 1 : 0) + \

233 ((sizeof(fmt) >= 21 && fmt[18] != '%' && fmt[19] == '%' && fmt[20] == 'p') ? 1 : 0) + \

234 ((sizeof(fmt) >= 22 && fmt[19] != '%' && fmt[20] == '%' && fmt[21] == 'p') ? 1 : 0) + \

235 ((sizeof(fmt) >= 23 && fmt[20] != '%' && fmt[21] == '%' && fmt[22] == 'p') ? 1 : 0) + \

236 ((sizeof(fmt) >= 24 && fmt[21] != '%' && fmt[22] == '%' && fmt[23] == 'p') ? 1 : 0) + \

237 ((sizeof(fmt) >= 25 && fmt[22] != '%' && fmt[23] == '%' && fmt[24] == 'p') ? 1 : 0) + \

238 ((sizeof(fmt) >= 26 && fmt[23] != '%' && fmt[24] == '%' && fmt[25] == 'p') ? 1 : 0) + \

239 ((sizeof(fmt) >= 27 && fmt[24] != '%' && fmt[25] == '%' && fmt[26] == 'p') ? 1 : 0) + \

240 ((sizeof(fmt) >= 28 && fmt[25] != '%' && fmt[26] == '%' && fmt[27] == 'p') ? 1 : 0) + \

241 ((sizeof(fmt) >= 29 && fmt[26] != '%' && fmt[27] == '%' && fmt[28] == 'p') ? 1 : 0) + \

242 ((sizeof(fmt) >= 30 && fmt[27] != '%' && fmt[28] == '%' && fmt[29] == 'p') ? 1 : 0) + \

243 ((sizeof(fmt) >= 31 && fmt[28] != '%' && fmt[29] == '%' && fmt[30] == 'p') ? 1 : 0) + \

244 ((sizeof(fmt) >= 32 && fmt[29] != '%' && fmt[30] == '%' && fmt[31] == 'p') ? 1 : 0) + \

245 ((sizeof(fmt) >= 33 && fmt[30] != '%' && fmt[31] == '%' && fmt[32] == 'p') ? 1 : 0) + \

246 ((sizeof(fmt) >= 34 && fmt[31] != '%' && fmt[32] == '%' && fmt[33] == 'p') ? 1 : 0) + \

247 ((sizeof(fmt) >= 35 && fmt[32] != '%' && fmt[33] == '%' && fmt[34] == 'p') ? 1 : 0) + \

248 ((sizeof(fmt) >= 36 && fmt[33] != '%' && fmt[34] == '%' && fmt[35] == 'p') ? 1 : 0) + \

249 ((sizeof(fmt) >= 37 && fmt[34] != '%' && fmt[35] == '%' && fmt[36] == 'p') ? 1 : 0) + \

250 ((sizeof(fmt) >= 38 && fmt[35] != '%' && fmt[36] == '%' && fmt[37] == 'p') ? 1 : 0) + \

251 ((sizeof(fmt) >= 39 && fmt[36] != '%' && fmt[37] == '%' && fmt[38] == 'p') ? 1 : 0) + \

252 ((sizeof(fmt) >= 40 && fmt[37] != '%' && fmt[38] == '%' && fmt[39] == 'p') ? 1 : 0) + \

253 ((sizeof(fmt) >= 41 && fmt[38] != '%' && fmt[39] == '%' && fmt[40] == 'p') ? 1 : 0) + \

254 ((sizeof(fmt) >= 42 && fmt[39] != '%' && fmt[40] == '%' && fmt[41] == 'p') ? 1 : 0) + \

255 ((sizeof(fmt) >= 43 && fmt[40] != '%' && fmt[41] == '%' && fmt[42] == 'p') ? 1 : 0) + \

256 ((sizeof(fmt) >= 44 && fmt[41] != '%' && fmt[42] == '%' && fmt[43] == 'p') ? 1 : 0) + \

257 ((sizeof(fmt) >= 45 && fmt[42] != '%' && fmt[43] == '%' && fmt[44] == 'p') ? 1 : 0) + \

258 ((sizeof(fmt) >= 46 && fmt[43] != '%' && fmt[44] == '%' && fmt[45] == 'p') ? 1 : 0) + \

259 ((sizeof(fmt) >= 47 && fmt[44] != '%' && fmt[45] == '%' && fmt[46] == 'p') ? 1 : 0) + \

260 ((sizeof(fmt) >= 48 && fmt[45] != '%' && fmt[46] == '%' && fmt[47] == 'p') ? 1 : 0) + \

261 ((sizeof(fmt) >= 49 && fmt[46] != '%' && fmt[47] == '%' && fmt[48] == 'p') ? 1 : 0) + \

262 ((sizeof(fmt) >= 50 && fmt[47] != '%' && fmt[48] == '%' && fmt[49] == 'p') ? 1 : 0) + \

263 ((sizeof(fmt) >= 51 && fmt[48] != '%' && fmt[49] == '%' && fmt[50] == 'p') ? 1 : 0) + \

264 ((sizeof(fmt) >= 52 && fmt[49] != '%' && fmt[50] == '%' && fmt[51] == 'p') ? 1 : 0) + \

265 ((sizeof(fmt) >= 53 && fmt[50] != '%' && fmt[51] == '%' && fmt[52] == 'p') ? 1 : 0) + \

266 ((sizeof(fmt) >= 54 && fmt[51] != '%' && fmt[52] == '%' && fmt[53] == 'p') ? 1 : 0) + \

267 ((sizeof(fmt) >= 55 && fmt[52] != '%' && fmt[53] == '%' && fmt[54] == 'p') ? 1 : 0) + \

268 ((sizeof(fmt) >= 56 && fmt[53] != '%' && fmt[54] == '%' && fmt[55] == 'p') ? 1 : 0) + \

269 ((sizeof(fmt) >= 57 && fmt[54] != '%' && fmt[55] == '%' && fmt[56] == 'p') ? 1 : 0) + \

270 ((sizeof(fmt) >= 58 && fmt[55] != '%' && fmt[56] == '%' && fmt[57] == 'p') ? 1 : 0) + \

271 ((sizeof(fmt) >= 59 && fmt[56] != '%' && fmt[57] == '%' && fmt[58] == 'p') ? 1 : 0) + \

272 ((sizeof(fmt) >= 60 && fmt[57] != '%' && fmt[58] == '%' && fmt[59] == 'p') ? 1 : 0) + \

273 ((sizeof(fmt) >= 61 && fmt[58] != '%' && fmt[59] == '%' && fmt[60] == 'p') ? 1 : 0) + \

274 ((sizeof(fmt) >= 62 && fmt[59] != '%' && fmt[60] == '%' && fmt[61] == 'p') ? 1 : 0) + \

275 ((sizeof(fmt) >= 63 && fmt[60] != '%' && fmt[61] == '%' && fmt[62] == 'p') ? 1 : 0) + \

276 ((sizeof(fmt) >= 64 && fmt[61] != '%' && fmt[62] == '%' && fmt[63] == 'p') ? 1 : 0) + \

277 ((sizeof(fmt) >= 65 && fmt[62] != '%' && fmt[63] == '%' && fmt[64] == 'p') ? 1 : 0) + \

278 ((sizeof(fmt) >= 66 && fmt[63] != '%' && fmt[64] == '%' && fmt[65] == 'p') ? 1 : 0) + \

279 ((sizeof(fmt) >= 67 && fmt[64] != '%' && fmt[65] == '%' && fmt[66] == 'p') ? 1 : 0) + \

280 ((sizeof(fmt) >= 68 && fmt[65] != '%' && fmt[66] == '%' && fmt[67] == 'p') ? 1 : 0) + \

281 ((sizeof(fmt) >= 69 && fmt[66] != '%' && fmt[67] == '%' && fmt[68] == 'p') ? 1 : 0) + \

282 ((sizeof(fmt) >= 70 && fmt[67] != '%' && fmt[68] == '%' && fmt[69] == 'p') ? 1 : 0) + \

283 ((sizeof(fmt) >= 71 && fmt[68] != '%' && fmt[69] == '%' && fmt[70] == 'p') ? 1 : 0) + \

284 ((sizeof(fmt) >= 72 && fmt[69] != '%' && fmt[70] == '%' && fmt[71] == 'p') ? 1 : 0) + \

285 ((sizeof(fmt) >= 73 && fmt[70] != '%' && fmt[71] == '%' && fmt[72] == 'p') ? 1 : 0) + \

286 ((sizeof(fmt) >= 74 && fmt[71] != '%' && fmt[72] == '%' && fmt[73] == 'p') ? 1 : 0) + \

287 ((sizeof(fmt) >= 75 && fmt[72] != '%' && fmt[73] == '%' && fmt[74] == 'p') ? 1 : 0) + \

288 ((sizeof(fmt) >= 76 && fmt[73] != '%' && fmt[74] == '%' && fmt[75] == 'p') ? 1 : 0) + \

289 ((sizeof(fmt) >= 77 && fmt[74] != '%' && fmt[75] == '%' && fmt[76] == 'p') ? 1 : 0) + \

290 ((sizeof(fmt) >= 78 && fmt[75] != '%' && fmt[76] == '%' && fmt[77] == 'p') ? 1 : 0) + \

291 ((sizeof(fmt) >= 79 && fmt[76] != '%' && fmt[77] == '%' && fmt[78] == 'p') ? 1 : 0) + \

292 ((sizeof(fmt) >= 80 && fmt[77] != '%' && fmt[78] == '%' && fmt[79] == 'p') ? 1 : 0) + \

293 ((sizeof(fmt) >= 81 && fmt[78] != '%' && fmt[79] == '%' && fmt[80] == 'p') ? 1 : 0) + \

294 ((sizeof(fmt) >= 82 && fmt[79] != '%' && fmt[80] == '%' && fmt[81] == 'p') ? 1 : 0) + \

295 ((sizeof(fmt) >= 83 && fmt[80] != '%' && fmt[81] == '%' && fmt[82] == 'p') ? 1 : 0) + \

296 ((sizeof(fmt) >= 84 && fmt[81] != '%' && fmt[82] == '%' && fmt[83] == 'p') ? 1 : 0) + \

297 ((sizeof(fmt) >= 85 && fmt[82] != '%' && fmt[83] == '%' && fmt[84] == 'p') ? 1 : 0) + \

298 ((sizeof(fmt) >= 86 && fmt[83] != '%' && fmt[84] == '%' && fmt[85] == 'p') ? 1 : 0) + \

299 ((sizeof(fmt) >= 87 && fmt[84] != '%' && fmt[85] == '%' && fmt[86] == 'p') ? 1 : 0) + \

300 ((sizeof(fmt) >= 88 && fmt[85] != '%' && fmt[86] == '%' && fmt[87] == 'p') ? 1 : 0) + \

301 ((sizeof(fmt) >= 89 && fmt[86] != '%' && fmt[87] == '%' && fmt[88] == 'p') ? 1 : 0) + \

302 ((sizeof(fmt) >= 90 && fmt[87] != '%' && fmt[88] == '%' && fmt[89] == 'p') ? 1 : 0) + \

303 ((sizeof(fmt) >= 91 && fmt[88] != '%' && fmt[89] == '%' && fmt[90] == 'p') ? 1 : 0) + \

304 ((sizeof(fmt) >= 92 && fmt[89] != '%' && fmt[90] == '%' && fmt[91] == 'p') ? 1 : 0) + \

305 ((sizeof(fmt) >= 93 && fmt[90] != '%' && fmt[91] == '%' && fmt[92] == 'p') ? 1 : 0) + \

306 ((sizeof(fmt) >= 94 && fmt[91] != '%' && fmt[92] == '%' && fmt[93] == 'p') ? 1 : 0) + \

307 ((sizeof(fmt) >= 95 && fmt[92] != '%' && fmt[93] == '%' && fmt[94] == 'p') ? 1 : 0) + \

308 ((sizeof(fmt) >= 96 && fmt[93] != '%' && fmt[94] == '%' && fmt[95] == 'p') ? 1 : 0) + \

309 ((sizeof(fmt) >= 97 && fmt[94] != '%' && fmt[95] == '%' && fmt[96] == 'p') ? 1 : 0) + \

310 ((sizeof(fmt) >= 98 && fmt[95] != '%' && fmt[96] == '%' && fmt[97] == 'p') ? 1 : 0) + \

311 ((sizeof(fmt) >= 99 && fmt[96] != '%' && fmt[97] == '%' && fmt[98] == 'p') ? 1 : 0) + \

312 ((sizeof(fmt) >= 100 && fmt[97] != '%' && fmt[98] == '%' && fmt[99] == 'p') ? 1 : 0) + \

313 ((sizeof(fmt) >= 101 && fmt[98] != '%' && fmt[99] == '%' && fmt[100] == 'p') ? 1 : 0) + \

314 ((sizeof(fmt) >= 102 && fmt[99] != '%' && fmt[100] == '%' && fmt[101] == 'p') ? 1 : 0) + \

315 ((sizeof(fmt) >= 103 && fmt[100] != '%' && fmt[101] == '%' && fmt[102] == 'p') ? 1 : 0) + \

316 ((sizeof(fmt) >= 104 && fmt[101] != '%' && fmt[102] == '%' && fmt[103] == 'p') ? 1 : 0) + \

317 ((sizeof(fmt) >= 105 && fmt[102] != '%' && fmt[103] == '%' && fmt[104] == 'p') ? 1 : 0) + \

318 ((sizeof(fmt) >= 106 && fmt[103] != '%' && fmt[104] == '%' && fmt[105] == 'p') ? 1 : 0) + \

319 ((sizeof(fmt) >= 107 && fmt[104] != '%' && fmt[105] == '%' && fmt[106] == 'p') ? 1 : 0) + \

320 ((sizeof(fmt) >= 108 && fmt[105] != '%' && fmt[106] == '%' && fmt[107] == 'p') ? 1 : 0) + \

321 ((sizeof(fmt) >= 109 && fmt[106] != '%' && fmt[107] == '%' && fmt[108] == 'p') ? 1 : 0) + \

322 ((sizeof(fmt) >= 110 && fmt[107] != '%' && fmt[108] == '%' && fmt[109] == 'p') ? 1 : 0) + \

323 ((sizeof(fmt) >= 111 && fmt[108] != '%' && fmt[109] == '%' && fmt[110] == 'p') ? 1 : 0) + \

324 ((sizeof(fmt) >= 112 && fmt[109] != '%' && fmt[110] == '%' && fmt[111] == 'p') ? 1 : 0) + \

325 ((sizeof(fmt) >= 113 && fmt[110] != '%' && fmt[111] == '%' && fmt[112] == 'p') ? 1 : 0) + \

326 ((sizeof(fmt) >= 114 && fmt[111] != '%' && fmt[112] == '%' && fmt[113] == 'p') ? 1 : 0) + \

327 ((sizeof(fmt) >= 115 && fmt[112] != '%' && fmt[113] == '%' && fmt[114] == 'p') ? 1 : 0) + \

328 ((sizeof(fmt) >= 116 && fmt[113] != '%' && fmt[114] == '%' && fmt[115] == 'p') ? 1 : 0) + \

329 ((sizeof(fmt) >= 117 && fmt[114] != '%' && fmt[115] == '%' && fmt[116] == 'p') ? 1 : 0) + \

330 ((sizeof(fmt) >= 118 && fmt[115] != '%' && fmt[116] == '%' && fmt[117] == 'p') ? 1 : 0) + \

331 ((sizeof(fmt) >= 119 && fmt[116] != '%' && fmt[117] == '%' && fmt[118] == 'p') ? 1 : 0) + \

332 ((sizeof(fmt) >= 120 && fmt[117] != '%' && fmt[118] == '%' && fmt[119] == 'p') ? 1 : 0) + \

333 ((sizeof(fmt) >= 121 && fmt[118] != '%' && fmt[119] == '%' && fmt[120] == 'p') ? 1 : 0) + \

334 ((sizeof(fmt) >= 122 && fmt[119] != '%' && fmt[120] == '%' && fmt[121] == 'p') ? 1 : 0) + \

335 ((sizeof(fmt) >= 123 && fmt[120] != '%' && fmt[121] == '%' && fmt[122] == 'p') ? 1 : 0) + \

336 ((sizeof(fmt) >= 124 && fmt[121] != '%' && fmt[122] == '%' && fmt[123] == 'p') ? 1 : 0) + \

337 ((sizeof(fmt) >= 125 && fmt[122] != '%' && fmt[123] == '%' && fmt[124] == 'p') ? 1 : 0) + \

338 ((sizeof(fmt) >= 126 && fmt[123] != '%' && fmt[124] == '%' && fmt[125] == 'p') ? 1 : 0) + \

339 ((sizeof(fmt) >= 127 && fmt[124] != '%' && fmt[125] == '%' && fmt[126] == 'p') ? 1 : 0) + \

340 ((sizeof(fmt) >= 128 && fmt[125] != '%' && fmt[126] == '%' && fmt[127] == 'p') ? 1 : 0) + \

341 ((sizeof(fmt) >= 129 && fmt[126] != '%' && fmt[127] == '%' && fmt[128] == 'p') ? 1 : 0) + \

342 ((sizeof(fmt) >= 130 && fmt[127] != '%' && fmt[128] == '%' && fmt[129] == 'p') ? 1 : 0) + \

343 ((sizeof(fmt) >= 131 && fmt[128] != '%' && fmt[129] == '%' && fmt[130] == 'p') ? 1 : 0) + \

344 ((sizeof(fmt) >= 132 && fmt[129] != '%' && fmt[130] == '%' && fmt[131] == 'p') ? 1 : 0) + \

345 ((sizeof(fmt) >= 133 && fmt[130] != '%' && fmt[131] == '%' && fmt[132] == 'p') ? 1 : 0) + \

346 ((sizeof(fmt) >= 134 && fmt[131] != '%' && fmt[132] == '%' && fmt[133] == 'p') ? 1 : 0) + \

347 ((sizeof(fmt) >= 135 && fmt[132] != '%' && fmt[133] == '%' && fmt[134] == 'p') ? 1 : 0) + \

348 ((sizeof(fmt) >= 136 && fmt[133] != '%' && fmt[134] == '%' && fmt[135] == 'p') ? 1 : 0) + \

349 ((sizeof(fmt) >= 137 && fmt[134] != '%' && fmt[135] == '%' && fmt[136] == 'p') ? 1 : 0) + \

350 ((sizeof(fmt) >= 138 && fmt[135] != '%' && fmt[136] == '%' && fmt[137] == 'p') ? 1 : 0) + \

351 ((sizeof(fmt) >= 139 && fmt[136] != '%' && fmt[137] == '%' && fmt[138] == 'p') ? 1 : 0) + \

352 ((sizeof(fmt) >= 140 && fmt[137] != '%' && fmt[138] == '%' && fmt[139] == 'p') ? 1 : 0) + \

353 ((sizeof(fmt) >= 141 && fmt[138] != '%' && fmt[139] == '%' && fmt[140] == 'p') ? 1 : 0) + \

354 ((sizeof(fmt) >= 142 && fmt[139] != '%' && fmt[140] == '%' && fmt[141] == 'p') ? 1 : 0) + \

355 ((sizeof(fmt) >= 143 && fmt[140] != '%' && fmt[141] == '%' && fmt[142] == 'p') ? 1 : 0) + \

356 ((sizeof(fmt) >= 144 && fmt[141] != '%' && fmt[142] == '%' && fmt[143] == 'p') ? 1 : 0) + \

357 ((sizeof(fmt) >= 145 && fmt[142] != '%' && fmt[143] == '%' && fmt[144] == 'p') ? 1 : 0) + \

358 ((sizeof(fmt) >= 146 && fmt[143] != '%' && fmt[144] == '%' && fmt[145] == 'p') ? 1 : 0) + \

359 ((sizeof(fmt) >= 147 && fmt[144] != '%' && fmt[145] == '%' && fmt[146] == 'p') ? 1 : 0) + \

360 ((sizeof(fmt) >= 148 && fmt[145] != '%' && fmt[146] == '%' && fmt[147] == 'p') ? 1 : 0) + \

361 ((sizeof(fmt) >= 149 && fmt[146] != '%' && fmt[147] == '%' && fmt[148] == 'p') ? 1 : 0) + \

362 ((sizeof(fmt) >= 150 && fmt[147] != '%' && fmt[148] == '%' && fmt[149] == 'p') ? 1 : 0) + \

363 ((sizeof(fmt) >= 151 && fmt[148] != '%' && fmt[149] == '%' && fmt[150] == 'p') ? 1 : 0) + \

364 ((sizeof(fmt) >= 152 && fmt[149] != '%' && fmt[150] == '%' && fmt[151] == 'p') ? 1 : 0) + \

365 ((sizeof(fmt) >= 153 && fmt[150] != '%' && fmt[151] == '%' && fmt[152] == 'p') ? 1 : 0) + \

366 ((sizeof(fmt) >= 154 && fmt[151] != '%' && fmt[152] == '%' && fmt[153] == 'p') ? 1 : 0) + \

367 ((sizeof(fmt) >= 155 && fmt[152] != '%' && fmt[153] == '%' && fmt[154] == 'p') ? 1 : 0) + \

368 ((sizeof(fmt) >= 156 && fmt[153] != '%' && fmt[154] == '%' && fmt[155] == 'p') ? 1 : 0) + \

369 ((sizeof(fmt) >= 157 && fmt[154] != '%' && fmt[155] == '%' && fmt[156] == 'p') ? 1 : 0) + \

370 ((sizeof(fmt) >= 158 && fmt[155] != '%' && fmt[156] == '%' && fmt[157] == 'p') ? 1 : 0) + \

371 ((sizeof(fmt) >= 159 && fmt[156] != '%' && fmt[157] == '%' && fmt[158] == 'p') ? 1 : 0) + \

372 ((sizeof(fmt) >= 160 && fmt[157] != '%' && fmt[158] == '%' && fmt[159] == 'p') ? 1 : 0) + \

373 ((sizeof(fmt) >= 161 && fmt[158] != '%' && fmt[159] == '%' && fmt[160] == 'p') ? 1 : 0) + \

374 ((sizeof(fmt) >= 162 && fmt[159] != '%' && fmt[160] == '%' && fmt[161] == 'p') ? 1 : 0) + \

375 ((sizeof(fmt) >= 163 && fmt[160] != '%' && fmt[161] == '%' && fmt[162] == 'p') ? 1 : 0) + \

376 ((sizeof(fmt) >= 164 && fmt[161] != '%' && fmt[162] == '%' && fmt[163] == 'p') ? 1 : 0) + \

377 ((sizeof(fmt) >= 165 && fmt[162] != '%' && fmt[163] == '%' && fmt[164] == 'p') ? 1 : 0) + \

378 ((sizeof(fmt) >= 166 && fmt[163] != '%' && fmt[164] == '%' && fmt[165] == 'p') ? 1 : 0) + \

379 ((sizeof(fmt) >= 167 && fmt[164] != '%' && fmt[165] == '%' && fmt[166] == 'p') ? 1 : 0) + \

380 ((sizeof(fmt) >= 168 && fmt[165] != '%' && fmt[166] == '%' && fmt[167] == 'p') ? 1 : 0) + \

381 ((sizeof(fmt) >= 169 && fmt[166] != '%' && fmt[167] == '%' && fmt[168] == 'p') ? 1 : 0) + \

382 ((sizeof(fmt) >= 170 && fmt[167] != '%' && fmt[168] == '%' && fmt[169] == 'p') ? 1 : 0) + \

383 ((sizeof(fmt) >= 171 && fmt[168] != '%' && fmt[169] == '%' && fmt[170] == 'p') ? 1 : 0) + \

384 ((sizeof(fmt) >= 172 && fmt[169] != '%' && fmt[170] == '%' && fmt[171] == 'p') ? 1 : 0) + \

385 ((sizeof(fmt) >= 173 && fmt[170] != '%' && fmt[171] == '%' && fmt[172] == 'p') ? 1 : 0) + \

386 ((sizeof(fmt) >= 174 && fmt[171] != '%' && fmt[172] == '%' && fmt[173] == 'p') ? 1 : 0) + \

387 ((sizeof(fmt) >= 175 && fmt[172] != '%' && fmt[173] == '%' && fmt[174] == 'p') ? 1 : 0) + \

388 ((sizeof(fmt) >= 176 && fmt[173] != '%' && fmt[174] == '%' && fmt[175] == 'p') ? 1 : 0) + \

389 ((sizeof(fmt) >= 177 && fmt[174] != '%' && fmt[175] == '%' && fmt[176] == 'p') ? 1 : 0) + \

390 ((sizeof(fmt) >= 178 && fmt[175] != '%' && fmt[176] == '%' && fmt[177] == 'p') ? 1 : 0) + \

391 ((sizeof(fmt) >= 179 && fmt[176] != '%' && fmt[177] == '%' && fmt[178] == 'p') ? 1 : 0) + \

392 ((sizeof(fmt) >= 180 && fmt[177] != '%' && fmt[178] == '%' && fmt[179] == 'p') ? 1 : 0) + \

393 ((sizeof(fmt) >= 181 && fmt[178] != '%' && fmt[179] == '%' && fmt[180] == 'p') ? 1 : 0) + \

394 ((sizeof(fmt) >= 182 && fmt[179] != '%' && fmt[180] == '%' && fmt[181] == 'p') ? 1 : 0) + \

395 ((sizeof(fmt) >= 183 && fmt[180] != '%' && fmt[181] == '%' && fmt[182] == 'p') ? 1 : 0) + \

396 ((sizeof(fmt) >= 184 && fmt[181] != '%' && fmt[182] == '%' && fmt[183] == 'p') ? 1 : 0) + \

397 ((sizeof(fmt) >= 185 && fmt[182] != '%' && fmt[183] == '%' && fmt[184] == 'p') ? 1 : 0) + \

398 ((sizeof(fmt) >= 186 && fmt[183] != '%' && fmt[184] == '%' && fmt[185] == 'p') ? 1 : 0) + \

399 ((sizeof(fmt) >= 187 && fmt[184] != '%' && fmt[185] == '%' && fmt[186] == 'p') ? 1 : 0) + \

400 ((sizeof(fmt) >= 188 && fmt[185] != '%' && fmt[186] == '%' && fmt[187] == 'p') ? 1 : 0) + \

401 ((sizeof(fmt) >= 189 && fmt[186] != '%' && fmt[187] == '%' && fmt[188] == 'p') ? 1 : 0) + \

402 ((sizeof(fmt) >= 190 && fmt[187] != '%' && fmt[188] == '%' && fmt[189] == 'p') ? 1 : 0) + \

403 ((sizeof(fmt) >= 191 && fmt[188] != '%' && fmt[189] == '%' && fmt[190] == 'p') ? 1 : 0) + \

404 ((sizeof(fmt) >= 192 && fmt[189] != '%' && fmt[190] == '%' && fmt[191] == 'p') ? 1 : 0) + \

405 ((sizeof(fmt) >= 193 && fmt[190] != '%' && fmt[191] == '%' && fmt[192] == 'p') ? 1 : 0) + \

406 ((sizeof(fmt) >= 194 && fmt[191] != '%' && fmt[192] == '%' && fmt[193] == 'p') ? 1 : 0) + \

407 ((sizeof(fmt) >= 195 && fmt[192] != '%' && fmt[193] == '%' && fmt[194] == 'p') ? 1 : 0) + \

408 ((sizeof(fmt) >= 196 && fmt[193] != '%' && fmt[194] == '%' && fmt[195] == 'p') ? 1 : 0) + \

409 ((sizeof(fmt) >= 197 && fmt[194] != '%' && fmt[195] == '%' && fmt[196] == 'p') ? 1 : 0) + \

410 ((sizeof(fmt) >= 198 && fmt[195] != '%' && fmt[196] == '%' && fmt[197] == 'p') ? 1 : 0) + \

411 ((sizeof(fmt) >= 199 && fmt[196] != '%' && fmt[197] == '%' && fmt[198] == 'p') ? 1 : 0) + \

412 ((sizeof(fmt) >= 200 && fmt[197] != '%' && fmt[198] == '%' && fmt[199] == 'p') ? 1 : 0) + \

413 ((sizeof(fmt) >= 201 && fmt[198] != '%' && fmt[199] == '%' && fmt[200] == 'p') ? 1 : 0) + \

414 ((sizeof(fmt) >= 202 && fmt[199] != '%' && fmt[200] == '%' && fmt[201] == 'p') ? 1 : 0) + \

415 ((sizeof(fmt) >= 203 && fmt[200] != '%' && fmt[201] == '%' && fmt[202] == 'p') ? 1 : 0) + \

416 ((sizeof(fmt) >= 204 && fmt[201] != '%' && fmt[202] == '%' && fmt[203] == 'p') ? 1 : 0) + \

417 ((sizeof(fmt) >= 205 && fmt[202] != '%' && fmt[203] == '%' && fmt[204] == 'p') ? 1 : 0) + \

418 ((sizeof(fmt) >= 206 && fmt[203] != '%' && fmt[204] == '%' && fmt[205] == 'p') ? 1 : 0) + \

419 ((sizeof(fmt) >= 207 && fmt[204] != '%' && fmt[205] == '%' && fmt[206] == 'p') ? 1 : 0) + \

420 ((sizeof(fmt) >= 208 && fmt[205] != '%' && fmt[206] == '%' && fmt[207] == 'p') ? 1 : 0) + \

421 ((sizeof(fmt) >= 209 && fmt[206] != '%' && fmt[207] == '%' && fmt[208] == 'p') ? 1 : 0) + \

422 ((sizeof(fmt) >= 210 && fmt[207] != '%' && fmt[208] == '%' && fmt[209] == 'p') ? 1 : 0) + \

423 ((sizeof(fmt) >= 211 && fmt[208] != '%' && fmt[209] == '%' && fmt[210] == 'p') ? 1 : 0) + \

424 ((sizeof(fmt) >= 212 && fmt[209] != '%' && fmt[210] == '%' && fmt[211] == 'p') ? 1 : 0) + \

425 ((sizeof(fmt) >= 213 && fmt[210] != '%' && fmt[211] == '%' && fmt[212] == 'p') ? 1 : 0) + \

426 ((sizeof(fmt) >= 214 && fmt[211] != '%' && fmt[212] == '%' && fmt[213] == 'p') ? 1 : 0) + \

427 ((sizeof(fmt) >= 215 && fmt[212] != '%' && fmt[213] == '%' && fmt[214] == 'p') ? 1 : 0) + \

428 ((sizeof(fmt) >= 216 && fmt[213] != '%' && fmt[214] == '%' && fmt[215] == 'p') ? 1 : 0) + \

429 ((sizeof(fmt) >= 217 && fmt[214] != '%' && fmt[215] == '%' && fmt[216] == 'p') ? 1 : 0) + \

430 ((sizeof(fmt) >= 218 && fmt[215] != '%' && fmt[216] == '%' && fmt[217] == 'p') ? 1 : 0) + \

431 ((sizeof(fmt) >= 219 && fmt[216] != '%' && fmt[217] == '%' && fmt[218] == 'p') ? 1 : 0) + \

432 ((sizeof(fmt) >= 220 && fmt[217] != '%' && fmt[218] == '%' && fmt[219] == 'p') ? 1 : 0) + \

433 ((sizeof(fmt) >= 221 && fmt[218] != '%' && fmt[219] == '%' && fmt[220] == 'p') ? 1 : 0) + \

434 ((sizeof(fmt) >= 222 && fmt[219] != '%' && fmt[220] == '%' && fmt[221] == 'p') ? 1 : 0) + \

435 ((sizeof(fmt) >= 223 && fmt[220] != '%' && fmt[221] == '%' && fmt[222] == 'p') ? 1 : 0) + \

436 ((sizeof(fmt) >= 224 && fmt[221] != '%' && fmt[222] == '%' && fmt[223] == 'p') ? 1 : 0) + \

437 ((sizeof(fmt) >= 225 && fmt[222] != '%' && fmt[223] == '%' && fmt[224] == 'p') ? 1 : 0) + \

438 ((sizeof(fmt) >= 226 && fmt[223] != '%' && fmt[224] == '%' && fmt[225] == 'p') ? 1 : 0) + \

439 ((sizeof(fmt) >= 227 && fmt[224] != '%' && fmt[225] == '%' && fmt[226] == 'p') ? 1 : 0) + \

440 ((sizeof(fmt) >= 228 && fmt[225] != '%' && fmt[226] == '%' && fmt[227] == 'p') ? 1 : 0) + \

441 ((sizeof(fmt) >= 229 && fmt[226] != '%' && fmt[227] == '%' && fmt[228] == 'p') ? 1 : 0) + \

442 ((sizeof(fmt) >= 230 && fmt[227] != '%' && fmt[228] == '%' && fmt[229] == 'p') ? 1 : 0) + \

443 ((sizeof(fmt) >= 231 && fmt[228] != '%' && fmt[229] == '%' && fmt[230] == 'p') ? 1 : 0) + \

444 ((sizeof(fmt) >= 232 && fmt[229] != '%' && fmt[230] == '%' && fmt[231] == 'p') ? 1 : 0) + \

445 ((sizeof(fmt) >= 233 && fmt[230] != '%' && fmt[231] == '%' && fmt[232] == 'p') ? 1 : 0) + \

446 ((sizeof(fmt) >= 234 && fmt[231] != '%' && fmt[232] == '%' && fmt[233] == 'p') ? 1 : 0) + \

447 ((sizeof(fmt) >= 235 && fmt[232] != '%' && fmt[233] == '%' && fmt[234] == 'p') ? 1 : 0) + \

448 ((sizeof(fmt) >= 236 && fmt[233] != '%' && fmt[234] == '%' && fmt[235] == 'p') ? 1 : 0) + \

449 ((sizeof(fmt) >= 237 && fmt[234] != '%' && fmt[235] == '%' && fmt[236] == 'p') ? 1 : 0) + \

450 ((sizeof(fmt) >= 238 && fmt[235] != '%' && fmt[236] == '%' && fmt[237] == 'p') ? 1 : 0) + \

451 ((sizeof(fmt) >= 239 && fmt[236] != '%' && fmt[237] == '%' && fmt[238] == 'p') ? 1 : 0) + \

452 ((sizeof(fmt) >= 240 && fmt[237] != '%' && fmt[238] == '%' && fmt[239] == 'p') ? 1 : 0) + \

453 ((sizeof(fmt) >= 241 && fmt[238] != '%' && fmt[239] == '%' && fmt[240] == 'p') ? 1 : 0) + \

454 ((sizeof(fmt) >= 242 && fmt[239] != '%' && fmt[240] == '%' && fmt[241] == 'p') ? 1 : 0) + \

455 ((sizeof(fmt) >= 243 && fmt[240] != '%' && fmt[241] == '%' && fmt[242] == 'p') ? 1 : 0) + \

456 ((sizeof(fmt) >= 244 && fmt[241] != '%' && fmt[242] == '%' && fmt[243] == 'p') ? 1 : 0) + \

457 ((sizeof(fmt) >= 245 && fmt[242] != '%' && fmt[243] == '%' && fmt[244] == 'p') ? 1 : 0) + \

458 ((sizeof(fmt) >= 246 && fmt[243] != '%' && fmt[244] == '%' && fmt[245] == 'p') ? 1 : 0) + \

459 ((sizeof(fmt) >= 247 && fmt[244] != '%' && fmt[245] == '%' && fmt[246] == 'p') ? 1 : 0) + \

460 ((sizeof(fmt) >= 248 && fmt[245] != '%' && fmt[246] == '%' && fmt[247] == 'p') ? 1 : 0) + \

461 ((sizeof(fmt) >= 249 && fmt[246] != '%' && fmt[247] == '%' && fmt[248] == 'p') ? 1 : 0) + \

462 ((sizeof(fmt) >= 250 && fmt[247] != '%' && fmt[248] == '%' && fmt[249] == 'p') ? 1 : 0) + \

463 ((sizeof(fmt) >= 251 && fmt[248] != '%' && fmt[249] == '%' && fmt[250] == 'p') ? 1 : 0) + \

464 ((sizeof(fmt) >= 252 && fmt[249] != '%' && fmt[250] == '%' && fmt[251] == 'p') ? 1 : 0) + \

465 ((sizeof(fmt) >= 253 && fmt[250] != '%' && fmt[251] == '%' && fmt[252] == 'p') ? 1 : 0) + \

466 ((sizeof(fmt) >= 254 && fmt[251] != '%' && fmt[252] == '%' && fmt[253] == 'p') ? 1 : 0) + \

467 ((sizeof(fmt) >= 255 && fmt[252] != '%' && fmt[253] == '%' && fmt[254] == 'p') ? 1 : 0) + \

468 ((sizeof(fmt) >= 256 && fmt[253] != '%' && fmt[254] == '%' && fmt[255] == 'p') ? 1 : 0)

469

487#define Z\_CBPRINTF\_POINTERS\_VALIDATE(...) \

488 (Z\_CBPRINTF\_NONE\_CHAR\_PTR\_COUNT(\_\_VA\_ARGS\_\_) == \

489 Z\_CBPRINTF\_P\_COUNT(GET\_ARG\_N(1, \_\_VA\_ARGS\_\_)))

490

491/\* @brief Check if argument is a certain type of char pointer. What exectly is checked

492 \* depends on @p flags. If flags is 0 then 1 is returned if @p x is a char pointer.

493 \*

494 \* @param idx Argument index.

495 \* @param x Argument.

496 \* @param flags Flags. See @p CBPRINTF\_PACKAGE\_FLAGS.

497 \*

498 \* @retval 1 if @p x is char pointer meeting criteria identified by @p flags.

499 \* @retval 0 otherwise.

500 \*/

501#define Z\_CBPRINTF\_IS\_X\_PCHAR(idx, x, flags) \

502 (idx < Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT\_GET(flags) ? \

503 0 : Z\_CBPRINTF\_IS\_PCHAR(x, flags))

504

513#define Z\_CBPRINTF\_HAS\_PCHAR\_ARGS(flags, fmt, ...) \

514 (FOR\_EACH\_IDX\_FIXED\_ARG(Z\_CBPRINTF\_IS\_X\_PCHAR, (+), flags, \_\_VA\_ARGS\_\_))

515

516#define Z\_CBPRINTF\_PCHAR\_COUNT(flags, ...) \

517 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

518 (0), \

519 (Z\_CBPRINTF\_HAS\_PCHAR\_ARGS(flags, \_\_VA\_ARGS\_\_)))

520

529#if Z\_C\_GENERIC

530#define Z\_CBPRINTF\_MUST\_RUNTIME\_PACKAGE(flags, ...) ({\

531 \_Pragma("GCC diagnostic push") \

532 \_Pragma("GCC diagnostic ignored \"-Wpointer-arith\"") \

533 int \_rv; \

534 if ((flags) & CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS) { \

535 \_rv = 0; \

536 } else { \

537 \_rv = Z\_CBPRINTF\_PCHAR\_COUNT(flags, \_\_VA\_ARGS\_\_) > 0 ? 1 : 0; \

538 } \

539 \_Pragma("GCC diagnostic pop")\

540 \_rv; \

541})

542#else

543#define Z\_CBPRINTF\_MUST\_RUNTIME\_PACKAGE(flags, ...) 1

544#endif

545

555#ifdef \_\_cplusplus

556#define Z\_CBPRINTF\_ARG\_SIZE(v) z\_cbprintf\_cxx\_arg\_size(v)

557#else

558#define Z\_CBPRINTF\_ARG\_SIZE(v) ({\

559 \_\_auto\_type \_\_v = (v) + 0; \

560 /\* Static code analysis may complain about unused variable. \*/ \

561 (void)\_\_v; \

562 size\_t \_\_arg\_size = \_Generic((v), \

563 float : sizeof(double), \

564 default : \

565 sizeof((\_\_v)) \

566 ); \

567 \_\_arg\_size; \

568})

569#endif

570

577#ifdef \_\_cplusplus

578#define Z\_CBPRINTF\_STORE\_ARG(buf, arg) z\_cbprintf\_cxx\_store\_arg(buf, arg)

579#else

580#define Z\_CBPRINTF\_STORE\_ARG(buf, arg) do { \

581 if (Z\_CBPRINTF\_VA\_STACK\_LL\_DBL\_MEMCPY) { \

582 /\* If required, copy arguments by word to avoid unaligned access.\*/ \

583 \_\_auto\_type \_v = (arg) + 0; \

584 double \_d = \_Generic((arg) + 0, \

585 float : (arg) + 0, \

586 default : \

587 0.0); \

588 /\* Static code analysis may complain about unused variable. \*/ \

589 (void)\_v; \

590 (void)\_d; \

591 size\_t arg\_size = Z\_CBPRINTF\_ARG\_SIZE(arg); \

592 size\_t \_wsize = arg\_size / sizeof(int); \

593 z\_cbprintf\_wcpy((int \*)buf, \

594 (int \*) \_Generic((arg) + 0, float : &\_d, default : &\_v), \

595 \_wsize); \

596 } else { \

597 \*\_Generic((arg) + 0, \

598 char : (int \*)buf, \

599 unsigned char: (int \*)buf, \

600 short : (int \*)buf, \

601 unsigned short : (int \*)buf, \

602 int : (int \*)buf, \

603 unsigned int : (unsigned int \*)buf, \

604 long : (long \*)buf, \

605 unsigned long : (unsigned long \*)buf, \

606 long long : (long long \*)buf, \

607 unsigned long long : (unsigned long long \*)buf, \

608 float : (double \*)buf, \

609 double : (double \*)buf, \

610 long double : (long double \*)buf, \

611 default : \

612 (const void \*\*)buf) = arg; \

613 } \

614} while (false)

615#endif

616

623#ifdef \_\_cplusplus

624#define Z\_CBPRINTF\_ALIGNMENT(\_arg) z\_cbprintf\_cxx\_alignment(\_arg)

625#else

626#define Z\_CBPRINTF\_ALIGNMENT(\_arg) \

627 MAX(\_Generic((\_arg) + 0, \

628 float : VA\_STACK\_ALIGN(double), \

629 double : VA\_STACK\_ALIGN(double), \

630 long double : VA\_STACK\_ALIGN(long double), \

631 long long : VA\_STACK\_ALIGN(long long), \

632 unsigned long long : VA\_STACK\_ALIGN(long long), \

633 default : \

634 \_\_alignof\_\_((\_arg) + 0)), VA\_STACK\_MIN\_ALIGN)

635#endif

636

647#ifdef \_\_cplusplus

648#if defined(\_\_x86\_64\_\_) || defined(\_\_riscv) || defined(\_\_aarch64\_\_)

649#define Z\_CBPRINTF\_IS\_LONGDOUBLE(x) 0

650#else

651#define Z\_CBPRINTF\_IS\_LONGDOUBLE(x) z\_cbprintf\_cxx\_is\_longdouble(x)

652#endif

653#else

654#define Z\_CBPRINTF\_IS\_LONGDOUBLE(x) \

655 \_Generic((x) + 0, long double : 1, default : 0)

656#endif

657

673#define Z\_CBPRINTF\_PACK\_ARG2(arg\_idx, \_buf, \_idx, \_align\_offset, \_max, \_arg) \

674do { \

675 BUILD\_ASSERT(!((sizeof(double) < VA\_STACK\_ALIGN(long double)) && \

676 Z\_CBPRINTF\_IS\_LONGDOUBLE(\_arg) && \

677 !IS\_ENABLED(CONFIG\_CBPRINTF\_PACKAGE\_LONGDOUBLE)),\

678 "Packaging of long double not enabled in Kconfig."); \

679 while (\_align\_offset % Z\_CBPRINTF\_ALIGNMENT(\_arg) != 0UL) { \

680 \_idx += sizeof(int); \

681 \_align\_offset += sizeof(int); \

682 } \

683 uint32\_t \_arg\_size = Z\_CBPRINTF\_ARG\_SIZE(\_arg); \

684 uint32\_t \_loc = \_idx / sizeof(int); \

685 if (arg\_idx < 1 + \_fros\_cnt) { \

686 if (\_ros\_pos\_en) { \

687 \_ros\_pos\_buf[\_ros\_pos\_idx++] = \_loc; \

688 } \

689 } else if (Z\_CBPRINTF\_IS\_PCHAR(\_arg, 0)) { \

690 if (\_cros\_en) { \

691 if (Z\_CBPRINTF\_IS\_X\_PCHAR(arg\_idx, \_arg, \_flags)) { \

692 if (\_rws\_pos\_en) { \

693 \_rws\_buffer[\_rws\_pos\_idx++] = arg\_idx - 1; \

694 \_rws\_buffer[\_rws\_pos\_idx++] = \_loc; \

695 } \

696 } else { \

697 if (\_ros\_pos\_en) { \

698 \_ros\_pos\_buf[\_ros\_pos\_idx++] = \_loc; \

699 } \

700 } \

701 } else if (\_rws\_pos\_en) { \

702 \_rws\_buffer[\_rws\_pos\_idx++] = arg\_idx - 1; \

703 \_rws\_buffer[\_rws\_pos\_idx++] = \_idx / sizeof(int); \

704 } \

705 } \

706 if (\_buf && \_idx < (int)\_max) { \

707 Z\_CBPRINTF\_STORE\_ARG(&\_buf[\_idx], \_arg); \

708 } \

709 \_idx += \_arg\_size; \

710 \_align\_offset += \_arg\_size; \

711} while (false)

712

719#define Z\_CBPRINTF\_PACK\_ARG(arg\_idx, arg) \

720 Z\_CBPRINTF\_PACK\_ARG2(arg\_idx, \_pbuf, \_pkg\_len, \_pkg\_offset, \_pmax, arg)

721

722/\* When using clang additional warning needs to be suppressed since each

723 \* argument of fmt string is used for sizeof() which results in the warning

724 \* if argument is a string literal. Suppression is added here instead of

725 \* the macro which generates the warning to not slow down the compiler.

726 \*/

727#ifdef \_\_clang\_\_

728#define Z\_CBPRINTF\_SUPPRESS\_SIZEOF\_ARRAY\_DECAY \

729 \_Pragma("GCC diagnostic ignored \"-Wsizeof-array-decay\"")

730#else

731#define Z\_CBPRINTF\_SUPPRESS\_SIZEOF\_ARRAY\_DECAY

732#endif

733

734/\* Allocation to avoid using VLA and alloca. Alloc frees space when leaving

735 \* a function which can lead to increased stack usage if logging is used

736 \* multiple times. VLA is not always available.

737 \*

738 \* Use large array when optimization is off to avoid increased stack usage.

739 \*/

740#ifdef CONFIG\_NO\_OPTIMIZATIONS

741#define Z\_CBPRINTF\_ON\_STACK\_ALLOC(\_name, \_len) \

742 \_\_ASSERT(\_len <= 32, "Too many string arguments."); \

743 uint8\_t \_name##\_buf32[32]; \

744 \_name = \_name##\_buf32

745#else

746#define Z\_CBPRINTF\_ON\_STACK\_ALLOC(\_name, \_len) \

747 \_\_ASSERT(\_len <= 32, "Too many string arguments."); \

748 uint8\_t \_name##\_buf4[4]; \

749 uint8\_t \_name##\_buf8[8]; \

750 uint8\_t \_name##\_buf12[12]; \

751 uint8\_t \_name##\_buf16[16]; \

752 uint8\_t \_name##\_buf32[32]; \

753 \_name = (\_len) <= 4 ? \_name##\_buf4 : \

754 ((\_len) <= 8 ? \_name##\_buf8 : \

755 ((\_len) <= 12 ? \_name##\_buf12 : \

756 ((\_len) <= 16 ? \_name##\_buf16 : \

757 \_name##\_buf32)))

758#endif

759

760/\* When the first argument of Z\_CBPRINTF\_STATIC\_PACKAGE\_GENERIC() is a

761 \* static memory location, some compiler warns you if you compare the

762 \* location against NULL. \_\_\_is\_null() is used to kill this warning.

763 \*

764 \* The warnings would be visible when you built with -save-temps=obj,

765 \* our standard debugging tip for macro problems.

766 \*

767 \* https://github.com/zephyrproject-rtos/zephyr/issues/51528

768 \*/

769static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool \_\_\_is\_null(void \*p)

770{

771 return p == NULL;

772}

773

789#define Z\_CBPRINTF\_STATIC\_PACKAGE\_GENERIC(buf, \_inlen, \_outlen, \_align\_offset, \

790 flags, ... /\* fmt, ... \*/) \

791do { \

792 \_Pragma("GCC diagnostic push") \

793 \_Pragma("GCC diagnostic ignored \"-Wpointer-arith\"") \

794 Z\_CBPRINTF\_SUPPRESS\_SIZEOF\_ARRAY\_DECAY \

795 BUILD\_ASSERT(!IS\_ENABLED(CONFIG\_XTENSA) || \

796 (IS\_ENABLED(CONFIG\_XTENSA) && \

797 !(\_align\_offset % CBPRINTF\_PACKAGE\_ALIGNMENT)), \

798 "Xtensa requires aligned package."); \

799 BUILD\_ASSERT((\_align\_offset % sizeof(int)) == 0, \

800 "Alignment offset must be multiply of a word."); \

801 IF\_ENABLED(CONFIG\_CBPRINTF\_STATIC\_PACKAGE\_CHECK\_ALIGNMENT, \

802 (\_\_ASSERT(!((uintptr\_t)buf & (CBPRINTF\_PACKAGE\_ALIGNMENT - 1)), \

803 "Buffer must be aligned.");)) \

804 uint32\_t \_flags = flags; \

805 bool \_ros\_pos\_en = (\_flags) & CBPRINTF\_PACKAGE\_ADD\_RO\_STR\_POS; \

806 bool \_rws\_pos\_en = (\_flags) & CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS; \

807 bool \_cros\_en = (\_flags) & CBPRINTF\_PACKAGE\_CONST\_CHAR\_RO; \

808 uint8\_t \*\_pbuf = buf; \

809 uint8\_t \_rws\_pos\_idx = 0; \

810 uint8\_t \_ros\_pos\_idx = 0; \

811 /\* Variable holds count of all string pointer arguments. \*/ \

812 uint8\_t \_alls\_cnt = Z\_CBPRINTF\_PCHAR\_COUNT(0, \_\_VA\_ARGS\_\_); \

813 uint8\_t \_fros\_cnt = Z\_CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT\_GET(\_flags); \

814 /\* Variable holds count of non const string pointers. \*/ \

815 uint8\_t \_rws\_cnt = \_cros\_en ? \

816 Z\_CBPRINTF\_PCHAR\_COUNT(\_flags, \_\_VA\_ARGS\_\_) : \_alls\_cnt - \_fros\_cnt; \

817 uint8\_t \_ros\_cnt = \_ros\_pos\_en ? (1 + \_alls\_cnt - \_rws\_cnt) : 0; \

818 uint8\_t \*\_ros\_pos\_buf; \

819 Z\_CBPRINTF\_ON\_STACK\_ALLOC(\_ros\_pos\_buf, \_ros\_cnt); \

820 uint8\_t \*\_rws\_buffer; \

821 Z\_CBPRINTF\_ON\_STACK\_ALLOC(\_rws\_buffer, 2 \* \_rws\_cnt); \

822 size\_t \_pmax = !\_\_\_is\_null(buf) ? \_inlen : INT32\_MAX; \

823 int \_pkg\_len = 0; \

824 int \_total\_len = 0; \

825 int \_pkg\_offset = \_align\_offset; \

826 union cbprintf\_package\_hdr \*\_len\_loc; \

827 /\* If string has rw string arguments CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS is a must. \*/ \

828 if (\_rws\_cnt && !((\_flags) & CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS)) { \

829 \_outlen = -EINVAL; \

830 break; \

831 } \

832 /\* package starts with string address and field with length \*/ \

833 if (\_pmax < sizeof(\*\_len\_loc)) { \

834 \_outlen = -ENOSPC; \

835 break; \

836 } \

837 \_len\_loc = (union cbprintf\_package\_hdr \*)\_pbuf; \

838 \_pkg\_len += sizeof(\*\_len\_loc); \

839 \_pkg\_offset += sizeof(\*\_len\_loc); \

840 /\* Pack remaining arguments \*/\

841 FOR\_EACH\_IDX(Z\_CBPRINTF\_PACK\_ARG, (;), \_\_VA\_ARGS\_\_);\

842 \_total\_len = \_pkg\_len; \

843 /\* Append string indexes to the package. \*/ \

844 \_total\_len += \_ros\_cnt; \

845 \_total\_len += 2 \* \_rws\_cnt; \

846 if (\_pbuf != NULL) { \

847 /\* Append string locations. \*/ \

848 uint8\_t \*\_pbuf\_loc = &\_pbuf[\_pkg\_len]; \

849 for (size\_t \_ros\_idx = 0; \_ros\_idx < \_ros\_cnt; \_ros\_idx++) { \

850 \*\_pbuf\_loc++ = \_ros\_pos\_buf[\_ros\_idx]; \

851 } \

852 for (size\_t \_rws\_idx = 0; \_rws\_idx < (2 \* \_rws\_cnt); \_rws\_idx++) { \

853 \*\_pbuf\_loc++ = \_rws\_buffer[\_rws\_idx]; \

854 } \

855 } \

856 /\* Store length \*/ \

857 \_outlen = (\_total\_len > (int)\_pmax) ? -ENOSPC : \_total\_len; \

858 /\* Store length in the header, set number of dumped strings to 0 \*/ \

859 if (\_pbuf != NULL) { \

860 union cbprintf\_package\_hdr pkg\_hdr = { \

861 .desc = { \

862 .len = (uint8\_t)(\_pkg\_len / sizeof(int)), \

863 .str\_cnt = 0, \

864 .ro\_str\_cnt = \_ros\_cnt, \

865 .rw\_str\_cnt = \_rws\_cnt, \

866 } \

867 }; \

868 IF\_ENABLED(CONFIG\_CBPRINTF\_PACKAGE\_HEADER\_STORE\_CREATION\_FLAGS, \

869 (pkg\_hdr.desc.pkg\_flags = flags)); \

870 \*\_len\_loc = pkg\_hdr; \

871 } \

872 \_Pragma("GCC diagnostic pop") \

873} while (false)

874

875#if Z\_C\_GENERIC

876#define Z\_CBPRINTF\_STATIC\_PACKAGE(packaged, inlen, outlen, align\_offset, flags, \

877 ... /\* fmt, ... \*/) \

878 Z\_CBPRINTF\_STATIC\_PACKAGE\_GENERIC(packaged, inlen, outlen, \

879 align\_offset, flags, \_\_VA\_ARGS\_\_)

880#else

881#define Z\_CBPRINTF\_STATIC\_PACKAGE(packaged, inlen, outlen, align\_offset, flags, \

882 ... /\* fmt, ... \*/) \

883do { \

884 /\* Small trick needed to avoid warning on always true \*/ \

885 if (((uintptr\_t)packaged + 1) != 1) { \

886 outlen = cbprintf\_package(packaged, inlen, flags, \_\_VA\_ARGS\_\_); \

887 } else { \

888 outlen = cbprintf\_package(NULL, align\_offset, flags, \_\_VA\_ARGS\_\_); \

889 } \

890} while (false)

891#endif /\* Z\_C\_GENERIC \*/

892

893#ifdef \_\_cplusplus

894}

895#endif

896

897#ifdef CONFIG\_CBPRINTF\_PACKAGE\_SUPPORT\_TAGGED\_ARGUMENTS

898#ifdef \_\_cplusplus

899/\*

900 \* Remove qualifiers like const, volatile. And also transform

901 \* C++ argument reference back to its basic type.

902 \*/

903#define Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg) \

904 z\_cbprintf\_cxx\_remove\_cv < \

905 z\_cbprintf\_cxx\_remove\_reference < decltype(arg) > ::type \

906 > ::type

907

908/\*

909 \* Get the type of elements in an array.

910 \*/

911#define Z\_CBPRINTF\_CXX\_ARG\_ARRAY\_TYPE(arg) \

912 z\_cbprintf\_cxx\_remove\_cv < \

913 z\_cbprintf\_cxx\_remove\_extent < decltype(arg) > ::type \

914 > ::type

915

916/\*

917 \* Determine if incoming type is char.

918 \*/

919#define Z\_CBPRINTF\_CXX\_ARG\_IS\_TYPE\_CHAR(type) \

920 (z\_cbprintf\_cxx\_is\_same\_type < type, \

921 char > :: value ? \

922 true : \

923 (z\_cbprintf\_cxx\_is\_same\_type < type, \

924 const char > :: value ? \

925 true : \

926 (z\_cbprintf\_cxx\_is\_same\_type < type, \

927 volatile char > :: value ? \

928 true : \

929 (z\_cbprintf\_cxx\_is\_same\_type < type, \

930 const volatile char > :: value ? \

931 true : \

932 false))))

933

934/\*

935 \* Figure out if this is a char array since (char \*) and (char[])

936 \* are of different types in C++.

937 \*/

938#define Z\_CBPRINTF\_CXX\_ARG\_IS\_CHAR\_ARRAY(arg) \

939 (z\_cbprintf\_cxx\_is\_array < decltype(arg) > :: value ? \

940 (Z\_CBPRINTF\_CXX\_ARG\_IS\_TYPE\_CHAR(Z\_CBPRINTF\_CXX\_ARG\_ARRAY\_TYPE(arg)) ? \

941 true : \

942 false) : \

943 false)

944

945/\*

946 \* Note that qualifiers of char \* must be explicitly matched

947 \* due to type matching in C++, where remove\_cv() does not work.

948 \*/

949#define Z\_CBPRINTF\_ARG\_TYPE(arg) \

950 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

951 char > ::value ? \

952 CBPRINTF\_PACKAGE\_ARG\_TYPE\_CHAR : \

953 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

954 unsigned char > ::value ? \

955 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_CHAR : \

956 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

957 short > ::value ? \

958 CBPRINTF\_PACKAGE\_ARG\_TYPE\_SHORT : \

959 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

960 unsigned short > ::value ? \

961 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_SHORT : \

962 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

963 int > ::value ? \

964 CBPRINTF\_PACKAGE\_ARG\_TYPE\_INT : \

965 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

966 unsigned int > ::value ? \

967 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_INT : \

968 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

969 long > ::value ? \

970 CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG : \

971 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

972 unsigned long > ::value ? \

973 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG : \

974 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

975 long long > ::value ? \

976 CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_LONG : \

977 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

978 unsigned long long > ::value ? \

979 CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG\_LONG : \

980 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

981 float > ::value ? \

982 CBPRINTF\_PACKAGE\_ARG\_TYPE\_FLOAT : \

983 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

984 double > ::value ? \

985 CBPRINTF\_PACKAGE\_ARG\_TYPE\_DOUBLE : \

986 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

987 long double > ::value ? \

988 CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_DOUBLE : \

989 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

990 char \* > :: value ? \

991 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

992 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

993 const char \* > :: value ? \

994 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

995 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

996 volatile char \* > :: value ? \

997 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

998 (z\_cbprintf\_cxx\_is\_same\_type < Z\_CBPRINTF\_ARG\_REMOVE\_QUAL(arg), \

999 const volatile char \* > :: value ? \

1000 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

1001 (Z\_CBPRINTF\_CXX\_ARG\_IS\_CHAR\_ARRAY(arg) ? \

1002 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR : \

1003 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID))))))))))))))))))

1004#else

1005#define Z\_CBPRINTF\_ARG\_TYPE(arg) \

1006 \_Generic(arg, \

1007 char : CBPRINTF\_PACKAGE\_ARG\_TYPE\_CHAR, \

1008 unsigned char : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_CHAR, \

1009 short : CBPRINTF\_PACKAGE\_ARG\_TYPE\_SHORT, \

1010 unsigned short : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_SHORT, \

1011 int : CBPRINTF\_PACKAGE\_ARG\_TYPE\_INT, \

1012 unsigned int : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_INT, \

1013 long : CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG, \

1014 unsigned long : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG, \

1015 long long : CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_LONG, \

1016 unsigned long long : CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG\_LONG, \

1017 float : CBPRINTF\_PACKAGE\_ARG\_TYPE\_FLOAT, \

1018 double : CBPRINTF\_PACKAGE\_ARG\_TYPE\_DOUBLE, \

1019 long double : CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_DOUBLE, \

1020 char \* : CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR, \

1021 const char \* : CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR, \

1022 void \* : CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID, \

1023 default : \

1024 CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID \

1025 )

1026#endif /\* \_cplusplus \*/

1027

1028#define Z\_CBPRINTF\_TAGGED\_EMPTY\_ARGS(...) \

1029 CBPRINTF\_PACKAGE\_ARG\_TYPE\_END

1030

1031#define Z\_CBPRINTF\_TAGGED\_ARGS\_3(arg) \

1032 Z\_CBPRINTF\_ARG\_TYPE(arg), arg

1033

1034#define Z\_CBPRINTF\_TAGGED\_ARGS\_2(...) \

1035 FOR\_EACH(Z\_CBPRINTF\_TAGGED\_ARGS\_3, (,), \_\_VA\_ARGS\_\_), \

1036 CBPRINTF\_PACKAGE\_ARG\_TYPE\_END

1037

1038#define Z\_CBPRINTF\_TAGGED\_ARGS(\_num\_args, ...) \

1039 COND\_CODE\_0(\_num\_args, \

1040 (CBPRINTF\_PACKAGE\_ARG\_TYPE\_END), \

1041 (Z\_CBPRINTF\_TAGGED\_ARGS\_2(\_\_VA\_ARGS\_\_)))

1042

1043#endif /\* CONFIG\_CBPRINTF\_PACKAGE\_SUPPORT\_TAGGED\_ARGUMENTS \*/

1044

1045#endif /\* ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_INTERNAL\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[cbprintf\_cxx.h](cbprintf__cxx_8h.md)

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[errno.h](errno_8h.md)

System error numbers.

[stdint.h](stdint_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [cbprintf\_internal.h](cbprintf__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
