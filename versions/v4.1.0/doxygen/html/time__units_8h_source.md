---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/time__units_8h_source.html
original_path: doxygen/html/time__units_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

time\_units.h

[Go to the documentation of this file.](time__units_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TIME\_UNITS\_H\_

8#define ZEPHYR\_INCLUDE\_TIME\_UNITS\_H\_

9

10#include <[zephyr/toolchain.h](toolchain_8h.md)>

11#include <[zephyr/sys/util.h](sys_2util_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

25

[ 33](group__timeutil__unit__apis.md#ga9f9c4c41f62c7578a30209475201efed)#define SYS\_FOREVER\_MS (-1)

34

[ 39](group__timeutil__unit__apis.md#gad8743aaa97d3b2650908020ffb76ef0e)#define SYS\_FOREVER\_US (-1)

40

[ 44](group__timeutil__unit__apis.md#gaca39a49322d7498accbdfa872b274a34)#define SYS\_TIMEOUT\_MS\_INIT(ms) \

45 Z\_TIMEOUT\_TICKS\_INIT((ms) == SYS\_FOREVER\_MS ? \

46 K\_TICKS\_FOREVER : Z\_TIMEOUT\_MS\_TICKS(ms))

47

[ 50](group__timeutil__unit__apis.md#ga6504e9e6fe4955e0bc31eccd4cfc01b7)#define SYS\_TIMEOUT\_MS(ms) ((k\_timeout\_t) SYS\_TIMEOUT\_MS\_INIT(ms))

51

52/\* Exhaustively enumerated, highly optimized time unit conversion API \*/

53

54#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

55\_\_syscall int sys\_clock\_hw\_cycles\_per\_sec\_runtime\_get(void);

56

57static inline int z\_impl\_sys\_clock\_hw\_cycles\_per\_sec\_runtime\_get(void)

58{

59 extern int z\_clock\_hw\_cycles\_per\_sec;

60

61 return z\_clock\_hw\_cycles\_per\_sec;

62}

63#endif /\* CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME \*/

64

65#if defined(\_\_cplusplus) && (\_\_cplusplus >= 201402L)

66 #if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

67 #define TIME\_CONSTEXPR

68 #else

69 #define TIME\_CONSTEXPR constexpr

70 #endif

71#else

[ 72](group__timeutil__unit__apis.md#ga387f15169fe1c0c58745548eceae1556) #define TIME\_CONSTEXPR

73#endif

74

79#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

80#define sys\_clock\_hw\_cycles\_per\_sec() sys\_clock\_hw\_cycles\_per\_sec\_runtime\_get()

81#else

[ 82](group__timeutil__unit__apis.md#gafe3ef19636d5002350794fa01b480d16)#define sys\_clock\_hw\_cycles\_per\_sec() CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC

83#endif

84

96#define z\_tmcvt\_use\_fast\_algo(from\_hz, to\_hz) \

97 ((DIV\_ROUND\_UP(CONFIG\_SYS\_CLOCK\_MAX\_TIMEOUT\_DAYS \* 24ULL \* 3600ULL \* from\_hz, \

98 UINT32\_MAX) \* to\_hz) <= UINT32\_MAX)

99

100/\* Time converter generator gadget. Selects from one of three

101 \* conversion algorithms: ones that take advantage when the

102 \* frequencies are an integer ratio (in either direction), or a full

103 \* precision conversion. Clever use of extra arguments causes all the

104 \* selection logic to be optimized out, and the generated code even

105 \* reduces to 32 bit only if a ratio conversion is available and the

106 \* result is 32 bits.

107 \*

108 \* This isn't intended to be used directly, instead being wrapped

109 \* appropriately in a user-facing API. The boolean arguments are:

110 \*

111 \* const\_hz - The hz arguments are known to be compile-time

112 \* constants (because otherwise the modulus test would

113 \* have to be done at runtime)

114 \* result32 - The result will be truncated to 32 bits on use

115 \* round\_up - Return the ceiling of the resulting fraction

116 \* round\_off - Return the nearest value to the resulting fraction

117 \* (pass both round\_up/off as false to get "round\_down")

118 \*

119 \* All of this must be implemented as expressions so that, when constant,

120 \* the results may be used to initialize global variables.

121 \*/

122

123/\* true if the conversion is the identity \*/

124#define z\_tmcvt\_is\_identity(\_\_from\_hz, \_\_to\_hz) \

125 ((\_\_to\_hz) == (\_\_from\_hz))

126

127/\* true if the conversion requires a simple integer multiply \*/

128#define z\_tmcvt\_is\_int\_mul(\_\_from\_hz, \_\_to\_hz) \

129 ((\_\_to\_hz) > (\_\_from\_hz) && (\_\_to\_hz) % (\_\_from\_hz) == 0U)

130

131/\* true if the conversion requires a simple integer division \*/

132#define z\_tmcvt\_is\_int\_div(\_\_from\_hz, \_\_to\_hz) \

133 ((\_\_from\_hz) > (\_\_to\_hz) && (\_\_from\_hz) % (\_\_to\_hz) == 0U)

134

135/\*

136 \* Compute the offset needed to round the result correctly when

137 \* the conversion requires a simple integer division

138 \*/

139#define z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

140 ((\_\_round\_off) ? ((\_\_from\_hz) / (\_\_to\_hz)) / 2 : \

141 (\_\_round\_up) ? ((\_\_from\_hz) / (\_\_to\_hz)) - 1 : \

142 0)

143

144/\*

145 \* All users of this macro MUST ensure its output is never used when a/b

146 \* is zero because it incorrectly but by design never returns zero.

147 \*

148 \* Some compiler versions emit a divide-by-zero warning for this code:

149 \* "false ? 42/0 : 43". Dealing with (generated) dead code is hard:

150 \* https://github.com/zephyrproject-rtos/zephyr/issues/63564

151 \* https://blog.llvm.org/2011/05/what-every-c-programmer-should-know\_21.html

152 \*

153 \* To silence such divide-by-zero warnings, "cheat" and never return

154 \* zero. Return 1 instead. Use octal "01u" as a breadcrumb to ease a

155 \* little bit the huge pain of "reverse-engineering" pre-processor

156 \* output.

157 \*

158 \* The "Elvis" operator "a/b ?: 1" is tempting because it avoids

159 \* evaluating the same expression twice. However: 1. it's a non-standard

160 \* GNU extension; 2. everything in this file is designed to be computed

161 \* at compile time anyway.

162 \*/

163#define z\_tmcvt\_divisor(a, b) ((a)/(b) ? (a)/(b) : 01u)

164

165/\*

166 \* Compute the offset needed to round the result correctly when

167 \* the conversion requires a full mul/div

168 \*/

169#define z\_tmcvt\_off\_gen(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

170 ((\_\_round\_off) ? (\_\_from\_hz) / 2 : \

171 (\_\_round\_up) ? (\_\_from\_hz) - 1 : \

172 0)

173

174/\* Integer division 32-bit conversion \*/

175#define z\_tmcvt\_int\_div\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

176 ((uint64\_t) (\_\_t) <= 0xffffffffU - \

177 z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) ? \

178 ((uint32\_t)((\_\_t) + \

179 z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \

180 \_\_round\_up, \_\_round\_off)) / \

181 z\_tmcvt\_divisor(\_\_from\_hz, \_\_to\_hz)) \

182 : \

183 (uint32\_t) (((uint64\_t) (\_\_t) + \

184 z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \

185 \_\_round\_up, \_\_round\_off)) / \

186 z\_tmcvt\_divisor(\_\_from\_hz, \_\_to\_hz)) \

187 )

188

189/\* Integer multiplication 32-bit conversion \*/

190#define z\_tmcvt\_int\_mul\_32(\_\_t, \_\_from\_hz, \_\_to\_hz) \

191 (uint32\_t) (\_\_t)\*((\_\_to\_hz) / (\_\_from\_hz))

192

193/\* General 32-bit conversion \*/

194#define z\_tmcvt\_gen\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

195 ((uint32\_t) (((uint64\_t) (\_\_t)\*(\_\_to\_hz) + \

196 z\_tmcvt\_off\_gen(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off)) / (\_\_from\_hz)))

197

198/\* Integer division 64-bit conversion \*/

199#define z\_tmcvt\_int\_div\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

200 (((uint64\_t) (\_\_t) + z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \

201 \_\_round\_up, \_\_round\_off)) / \

202 z\_tmcvt\_divisor(\_\_from\_hz, \_\_to\_hz))

203

204/\* Integer multiplication 64-bit conversion \*/

205#define z\_tmcvt\_int\_mul\_64(\_\_t, \_\_from\_hz, \_\_to\_hz) \

206 (uint64\_t) (\_\_t)\*((\_\_to\_hz) / (\_\_from\_hz))

207

208/\* Fast 64-bit conversion. This relies on the multiply not overflowing \*/

209#define z\_tmcvt\_gen\_64\_fast(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

210 (((uint64\_t) (\_\_t)\*(\_\_to\_hz) + \

211 z\_tmcvt\_off\_gen(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off)) / (\_\_from\_hz))

212

213/\* Slow 64-bit conversion. This avoids overflowing the multiply \*/

214#define z\_tmcvt\_gen\_64\_slow(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

215 (((uint64\_t) (\_\_t) / (\_\_from\_hz))\*(\_\_to\_hz) + \

216 (((uint64\_t) (\_\_t) % (\_\_from\_hz))\*(\_\_to\_hz) + \

217 z\_tmcvt\_off\_gen(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off)) / (\_\_from\_hz))

218

219/\* General 64-bit conversion. Uses one of the two above macros \*/

220#define z\_tmcvt\_gen\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

221 (z\_tmcvt\_use\_fast\_algo(\_\_from\_hz, \_\_to\_hz) ? \

222 z\_tmcvt\_gen\_64\_fast(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) : \

223 z\_tmcvt\_gen\_64\_slow(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off))

224

225/\* Convert, generating a 32-bit result \*/

226#define z\_tmcvt\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_round\_up, \_\_round\_off) \

227 ((\_\_const\_hz) ? \

228 ( \

229 z\_tmcvt\_is\_identity(\_\_from\_hz, \_\_to\_hz) ? \

230 (uint32\_t) (\_\_t) \

231 : \

232 z\_tmcvt\_is\_int\_div(\_\_from\_hz, \_\_to\_hz) ? \

233 z\_tmcvt\_int\_div\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

234 : \

235 z\_tmcvt\_is\_int\_mul(\_\_from\_hz, \_\_to\_hz) ? \

236 z\_tmcvt\_int\_mul\_32(\_\_t, \_\_from\_hz, \_\_to\_hz) \

237 : \

238 z\_tmcvt\_gen\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

239 ) \

240 : \

241 z\_tmcvt\_gen\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

242 )

243

244/\* Convert, generating a 64-bit result \*/

245#define z\_tmcvt\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_round\_up, \_\_round\_off) \

246 ((\_\_const\_hz) ? \

247 ( \

248 z\_tmcvt\_is\_identity(\_\_from\_hz, \_\_to\_hz) ? \

249 (uint64\_t) (\_\_t) \

250 : \

251 z\_tmcvt\_is\_int\_div(\_\_from\_hz, \_\_to\_hz) ? \

252 z\_tmcvt\_int\_div\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

253 : \

254 z\_tmcvt\_is\_int\_mul(\_\_from\_hz, \_\_to\_hz) ? \

255 z\_tmcvt\_int\_mul\_64(\_\_t, \_\_from\_hz, \_\_to\_hz) \

256 : \

257 z\_tmcvt\_gen\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

258 ) \

259 : \

260 z\_tmcvt\_gen\_64\_slow(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

261 )

262

263#define z\_tmcvt(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_result32, \_\_round\_up, \_\_round\_off) \

264 ((\_\_result32) ? \

265 z\_tmcvt\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_round\_up, \_\_round\_off) : \

266 z\_tmcvt\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_round\_up, \_\_round\_off))

267

268/\* The following code is programmatically generated using this perl

269 \* code, which enumerates all possible combinations of units, rounding

270 \* modes and precision. Do not edit directly.

271 \*

272 \* Note that nano/microsecond conversions are only defined with 64 bit

273 \* precision. These units conversions were not available in 32 bit

274 \* variants historically, and doing 32 bit math with units that small

275 \* has precision traps that we probably don't want to support in an

276 \* official API.

277 \*

278 \* #!/usr/bin/perl -w

279 \* use strict;

280 \*

281 \* my %human = ("sec" => "seconds",

282 \* "ms" => "milliseconds",

283 \* "us" => "microseconds",

284 \* "ns" => "nanoseconds",

285 \* "cyc" => "hardware cycles",

286 \* "ticks" => "ticks");

287 \* my %human\_round = ("ceil" => "Rounds up",

288 \* "near" => "Round nearest",

289 \* "floor" => "Truncates");

290 \*

291 \* sub big { return $\_[0] eq "us" || $\_[0] eq "ns"; }

292 \* sub prefix { return $\_[0] eq "sec" || $\_[0] eq "ms" || $\_[0] eq "us" || $\_[0] eq "ns"; }

293 \*

294 \* for my $from\_unit ("sec", "ms", "us", "ns", "cyc", "ticks") {

295 \* for my $to\_unit ("sec", "ms", "us", "ns", "cyc", "ticks") {

296 \* next if $from\_unit eq $to\_unit;

297 \* next if prefix($from\_unit) && prefix($to\_unit);

298 \* for my $round ("floor", "near", "ceil") {

299 \* for(my $big=0; $big <= 1; $big++) {

300 \* my $sz = $big ? 64 : 32;

301 \* my $sym = "k\_${from\_unit}\_to\_${to\_unit}\_$round$sz";

302 \* my $type = "uint${sz}\_t";

303 \* my $const\_hz = ($from\_unit eq "cyc" || $to\_unit eq "cyc")

304 \* ? "Z\_CCYC" : "true";

305 \* my $ret32 = $big ? "64" : "32";

306 \* my $rup = $round eq "ceil" ? "true" : "false";

307 \* my $roff = $round eq "near" ? "true" : "false";

308 \*

309 \* my $hfrom = $human{$from\_unit};

310 \* my $hto = $human{$to\_unit};

311 \* my $hround = $human\_round{$round};

312 \* print "/", "\*\* \@brief Convert $hfrom to $hto. $ret32 bits. $hround.\n";

313 \* print " \*\n";

314 \* print " \* Converts time values in $hfrom to $hto.\n";

315 \* print " \* Computes result in $sz bit precision.\n";

316 \* if ($round eq "ceil") {

317 \* print " \* Rounds up to the next highest output unit.\n";

318 \* } elsif ($round eq "near") {

319 \* print " \* Rounds to the nearest output unit.\n";

320 \* } else {

321 \* print " \* Truncates to the next lowest output unit.\n";

322 \* }

323 \* print " \*\n";

324 \* print " \* \@warning Generated. Do not edit. See above.\n";

325 \* print " \*\n";

326 \* print " \* \@param t Source time in $hfrom. uint64\_t\n";

327 \* print " \*\n";

328 \* print " \* \@return The converted time value in $hto. $type\n";

329 \* print " \*", "/\n";

330 \* print "#define $sym(t) \\\n";

331 \* print "\tz\_tmcvt\_$ret32(t, Z\_HZ\_$from\_unit, Z\_HZ\_$to\_unit,";

332 \* print " $const\_hz, $rup, $roff)\n";

333 \* print "\n\n";

334 \* }

335 \* }

336 \* }

337 \* }

338 \*/

339

340/\* Some more concise declarations to simplify the generator script and

341 \* save bytes below

342 \*/

343#define Z\_HZ\_sec 1

344#define Z\_HZ\_ms 1000

345#define Z\_HZ\_us 1000000

346#define Z\_HZ\_ns 1000000000

347#define Z\_HZ\_cyc sys\_clock\_hw\_cycles\_per\_sec()

348#define Z\_HZ\_ticks CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC

349#define Z\_CCYC (!IS\_ENABLED(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME))

350

[ 363](group__timeutil__unit__apis.md#ga38efeb3c71b28e98c6f18f63a2c59334)#define k\_sec\_to\_cyc\_floor32(t) \

364 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, false)

365

366

[ 379](group__timeutil__unit__apis.md#gaa9b2ed48e2b68d509a4eee305cdcd2fe)#define k\_sec\_to\_cyc\_floor64(t) \

380 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, false)

381

382

[ 395](group__timeutil__unit__apis.md#ga5a6ec23bd5644867f211eb5f47d81a3e)#define k\_sec\_to\_cyc\_near32(t) \

396 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, true)

397

398

[ 411](group__timeutil__unit__apis.md#gab1722b870ef8c9ed1084f104974c83a3)#define k\_sec\_to\_cyc\_near64(t) \

412 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, true)

413

414

[ 427](group__timeutil__unit__apis.md#ga197fe61819a3c51802f080187a39f2d5)#define k\_sec\_to\_cyc\_ceil32(t) \

428 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, true, false)

429

430

[ 443](group__timeutil__unit__apis.md#ga363ec5ce8d2365d25107e4c630222a9a)#define k\_sec\_to\_cyc\_ceil64(t) \

444 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, true, false)

445

446

[ 459](group__timeutil__unit__apis.md#gab6a57f08409edf9fba80837c3da34fb8)#define k\_sec\_to\_ticks\_floor32(t) \

460 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, false)

461

462

[ 475](group__timeutil__unit__apis.md#gafee9fc110890fba84640acac74af6717)#define k\_sec\_to\_ticks\_floor64(t) \

476 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, false)

477

478

[ 491](group__timeutil__unit__apis.md#ga4fbbf706ce9a69ab8b2b09bd3b0d4a3e)#define k\_sec\_to\_ticks\_near32(t) \

492 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, true)

493

494

[ 507](group__timeutil__unit__apis.md#gafbdfa2986e27ea95b0347319e8a23c68)#define k\_sec\_to\_ticks\_near64(t) \

508 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, true)

509

510

[ 523](group__timeutil__unit__apis.md#ga20d46aec38239513826d5d5259b5836c)#define k\_sec\_to\_ticks\_ceil32(t) \

524 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, true, false)

525

526

[ 539](group__timeutil__unit__apis.md#gad382b2d98f84705c4c4e7a775bb549e8)#define k\_sec\_to\_ticks\_ceil64(t) \

540 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, true, false)

541

542

[ 555](group__timeutil__unit__apis.md#ga2d60494645102034a7864ab0235bbfe4)#define k\_ms\_to\_cyc\_floor32(t) \

556 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, false)

557

558

[ 571](group__timeutil__unit__apis.md#ga4d3e1ec8eed229a08072aea744d40bba)#define k\_ms\_to\_cyc\_floor64(t) \

572 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, false)

573

574

[ 587](group__timeutil__unit__apis.md#ga8a0d31e998f1a19a3ee8200c173eb7c9)#define k\_ms\_to\_cyc\_near32(t) \

588 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, true)

589

590

[ 603](group__timeutil__unit__apis.md#gab2bcf34a4899619fcf083819a078a09e)#define k\_ms\_to\_cyc\_near64(t) \

604 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, true)

605

606

[ 619](group__timeutil__unit__apis.md#gab4636150867df2c4e918c12ec2e9bc5f)#define k\_ms\_to\_cyc\_ceil32(t) \

620 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, true, false)

621

622

[ 635](group__timeutil__unit__apis.md#ga82829fc9e99658faf91e5925c9545c9f)#define k\_ms\_to\_cyc\_ceil64(t) \

636 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, true, false)

637

638

[ 651](group__timeutil__unit__apis.md#gaf41d7ca19e5bb47824374698ce409ea1)#define k\_ms\_to\_ticks\_floor32(t) \

652 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, false)

653

654

[ 667](group__timeutil__unit__apis.md#gaa6ea6977308dfd2f092ba0ac4e779a31)#define k\_ms\_to\_ticks\_floor64(t) \

668 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, false)

669

670

[ 683](group__timeutil__unit__apis.md#ga0a61385f187c7c2a0f5288b17873b3db)#define k\_ms\_to\_ticks\_near32(t) \

684 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, true)

685

686

[ 699](group__timeutil__unit__apis.md#gab2f6dd223151224cd9fa0491f196c1f6)#define k\_ms\_to\_ticks\_near64(t) \

700 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, true)

701

702

[ 715](group__timeutil__unit__apis.md#gac74a319bcb69cc714818413ae15af7a2)#define k\_ms\_to\_ticks\_ceil32(t) \

716 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, true, false)

717

718

[ 731](group__timeutil__unit__apis.md#gaa623d51d51b18a2e54b20d36d2f81c42)#define k\_ms\_to\_ticks\_ceil64(t) \

732 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, true, false)

733

734

[ 747](group__timeutil__unit__apis.md#ga66c1ea8197e7adc01c837163e0aa4b62)#define k\_us\_to\_cyc\_floor32(t) \

748 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, false)

749

750

[ 763](group__timeutil__unit__apis.md#gac78731d5891b2389dc227608decf28dd)#define k\_us\_to\_cyc\_floor64(t) \

764 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, false)

765

766

[ 779](group__timeutil__unit__apis.md#ga01dabb87e1a4864e47fcd39cc4bce869)#define k\_us\_to\_cyc\_near32(t) \

780 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, true)

781

782

[ 795](group__timeutil__unit__apis.md#ga49a64e1f11cf450fdd770d67617cbe23)#define k\_us\_to\_cyc\_near64(t) \

796 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, true)

797

798

[ 811](group__timeutil__unit__apis.md#ga689a3f97643be5362c8c70c6d9d81051)#define k\_us\_to\_cyc\_ceil32(t) \

812 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, true, false)

813

814

[ 827](group__timeutil__unit__apis.md#ga2f65f04acc1daf019470beb04f16e276)#define k\_us\_to\_cyc\_ceil64(t) \

828 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, true, false)

829

830

[ 843](group__timeutil__unit__apis.md#ga96f32803affb56c366cbab5967c6b76c)#define k\_us\_to\_ticks\_floor32(t) \

844 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, false)

845

846

[ 859](group__timeutil__unit__apis.md#gaf6b4fb83131e5a52d9be875e5466d022)#define k\_us\_to\_ticks\_floor64(t) \

860 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, false)

861

862

[ 875](group__timeutil__unit__apis.md#ga5b0286cc82370178c852c3fa290eb61d)#define k\_us\_to\_ticks\_near32(t) \

876 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, true)

877

878

[ 891](group__timeutil__unit__apis.md#gaf2aae5316fcb5e99f4a77b99a5db27f9)#define k\_us\_to\_ticks\_near64(t) \

892 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, true)

893

894

[ 907](group__timeutil__unit__apis.md#ga950ac5ce654ec92e0af61e000de884a7)#define k\_us\_to\_ticks\_ceil32(t) \

908 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, true, false)

909

910

[ 923](group__timeutil__unit__apis.md#ga1a977f93dc94ce9db54b3c9fdf9ba2f9)#define k\_us\_to\_ticks\_ceil64(t) \

924 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, true, false)

925

926

[ 939](group__timeutil__unit__apis.md#ga46013e42990cfa561da06fb2bffaa261)#define k\_ns\_to\_cyc\_floor32(t) \

940 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, false)

941

942

[ 955](group__timeutil__unit__apis.md#gafc4ff458df5f4d1f221bcf0799d25335)#define k\_ns\_to\_cyc\_floor64(t) \

956 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, false)

957

958

[ 971](group__timeutil__unit__apis.md#gac8e586ebc94174ccdabf6f49dd0251e6)#define k\_ns\_to\_cyc\_near32(t) \

972 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, true)

973

974

[ 987](group__timeutil__unit__apis.md#gae6ec742a39a72b0a3dd7bc3da4a98403)#define k\_ns\_to\_cyc\_near64(t) \

988 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, true)

989

990

[ 1003](group__timeutil__unit__apis.md#ga928ace6a14c0c2eb6aaa027f545601a7)#define k\_ns\_to\_cyc\_ceil32(t) \

1004 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, true, false)

1005

1006

[ 1019](group__timeutil__unit__apis.md#ga82264e42744defb8acf69caa8612e476)#define k\_ns\_to\_cyc\_ceil64(t) \

1020 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, true, false)

1021

1022

[ 1035](group__timeutil__unit__apis.md#ga4b0a61273dfbebd9273c0dc71ea74c65)#define k\_ns\_to\_ticks\_floor32(t) \

1036 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, false)

1037

1038

[ 1051](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)#define k\_ns\_to\_ticks\_floor64(t) \

1052 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, false)

1053

1054

[ 1067](group__timeutil__unit__apis.md#ga308b172f1fb6e1452c14db444ad7e75e)#define k\_ns\_to\_ticks\_near32(t) \

1068 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, true)

1069

1070

[ 1083](group__timeutil__unit__apis.md#ga50c08351970ea8e62a0509b68898901a)#define k\_ns\_to\_ticks\_near64(t) \

1084 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, true)

1085

1086

[ 1099](group__timeutil__unit__apis.md#gad958afbd9f86f94ccd5c9569e7587fad)#define k\_ns\_to\_ticks\_ceil32(t) \

1100 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, true, false)

1101

1102

[ 1115](group__timeutil__unit__apis.md#ga1078f0f8764f7bad744cfb1ffd675c70)#define k\_ns\_to\_ticks\_ceil64(t) \

1116 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, true, false)

1117

1118

[ 1131](group__timeutil__unit__apis.md#ga7a83cefe2d1e0828c6cdf949d4be9674)#define k\_cyc\_to\_sec\_floor32(t) \

1132 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, false)

1133

1134

[ 1147](group__timeutil__unit__apis.md#gadb48b4c005c8e4f1a30f018192fe4ae5)#define k\_cyc\_to\_sec\_floor64(t) \

1148 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, false)

1149

1150

[ 1163](group__timeutil__unit__apis.md#ga41d9d97ae4abc59eb235626682b767c9)#define k\_cyc\_to\_sec\_near32(t) \

1164 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, true)

1165

1166

[ 1179](group__timeutil__unit__apis.md#ga8dccd0c590fb4c2c399b0e0a120a5753)#define k\_cyc\_to\_sec\_near64(t) \

1180 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, true)

1181

1182

[ 1195](group__timeutil__unit__apis.md#gaeaf83a64009e2a834b0d65ead788e856)#define k\_cyc\_to\_sec\_ceil32(t) \

1196 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, true, false)

1197

1198

[ 1211](group__timeutil__unit__apis.md#ga2c64ffb238dd5047413d394b39900d61)#define k\_cyc\_to\_sec\_ceil64(t) \

1212 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, true, false)

1213

1214

[ 1227](group__timeutil__unit__apis.md#ga5f9f903e6e4eba5415cae3f337d565ed)#define k\_cyc\_to\_ms\_floor32(t) \

1228 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, false)

1229

1230

[ 1243](group__timeutil__unit__apis.md#gaeaa9339beec5b82b924302bbc57923f6)#define k\_cyc\_to\_ms\_floor64(t) \

1244 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, false)

1245

1246

[ 1259](group__timeutil__unit__apis.md#gaba2f18bc00740fb0411371d2d2f3d949)#define k\_cyc\_to\_ms\_near32(t) \

1260 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, true)

1261

1262

[ 1275](group__timeutil__unit__apis.md#ga217f0b8bf86a24654419c3ccfd6e7822)#define k\_cyc\_to\_ms\_near64(t) \

1276 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, true)

1277

1278

[ 1291](group__timeutil__unit__apis.md#ga40bf11b01ba76673c67569e8d1e55d92)#define k\_cyc\_to\_ms\_ceil32(t) \

1292 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, true, false)

1293

1294

[ 1307](group__timeutil__unit__apis.md#gaf85474dc07ce8165379415f4977aa44f)#define k\_cyc\_to\_ms\_ceil64(t) \

1308 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, true, false)

1309

1310

[ 1323](group__timeutil__unit__apis.md#ga86392f2bddfbb7c895c08becf9c8c485)#define k\_cyc\_to\_us\_floor32(t) \

1324 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, false)

1325

1326

[ 1339](group__timeutil__unit__apis.md#gad3376aa7ab36b6b7f5a1f9c9977cee4a)#define k\_cyc\_to\_us\_floor64(t) \

1340 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, false)

1341

1342

[ 1355](group__timeutil__unit__apis.md#ga1314249a8a404f00c8a03d6c77e0c752)#define k\_cyc\_to\_us\_near32(t) \

1356 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, true)

1357

1358

[ 1371](group__timeutil__unit__apis.md#ga869ccaf50e83712d0bafe0f8e238fc61)#define k\_cyc\_to\_us\_near64(t) \

1372 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, true)

1373

1374

[ 1387](group__timeutil__unit__apis.md#ga051fbec0b352b4fb3116544c8c33250a)#define k\_cyc\_to\_us\_ceil32(t) \

1388 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, true, false)

1389

1390

[ 1403](group__timeutil__unit__apis.md#ga90b09be4536f6877f67a60b3c33f5299)#define k\_cyc\_to\_us\_ceil64(t) \

1404 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, true, false)

1405

1406

[ 1419](group__timeutil__unit__apis.md#ga775c4d72bd0ecb9a6ad947f34c479754)#define k\_cyc\_to\_ns\_floor32(t) \

1420 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, false)

1421

1422

[ 1435](group__timeutil__unit__apis.md#ga665d5fc98ffe8bd1cf78ca994f58724a)#define k\_cyc\_to\_ns\_floor64(t) \

1436 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, false)

1437

1438

[ 1451](group__timeutil__unit__apis.md#gabd5378a62e480fc1b79b3326c8f02d5f)#define k\_cyc\_to\_ns\_near32(t) \

1452 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, true)

1453

1454

[ 1467](group__timeutil__unit__apis.md#gad36269d0d63bee37e09da46cfe516c8c)#define k\_cyc\_to\_ns\_near64(t) \

1468 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, true)

1469

1470

[ 1483](group__timeutil__unit__apis.md#ga19526c845440ed793068fa8d8d5088ff)#define k\_cyc\_to\_ns\_ceil32(t) \

1484 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, true, false)

1485

1486

[ 1499](group__timeutil__unit__apis.md#gab2889da75f359d248a6eb61fdc3d53c0)#define k\_cyc\_to\_ns\_ceil64(t) \

1500 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, true, false)

1501

1502

[ 1515](group__timeutil__unit__apis.md#ga2efd0e2611cbeb696778eb73cf24b7ee)#define k\_cyc\_to\_ticks\_floor32(t) \

1516 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, false)

1517

1518

[ 1531](group__timeutil__unit__apis.md#gaad0256d9429dfa5c5a194f1419691cfc)#define k\_cyc\_to\_ticks\_floor64(t) \

1532 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, false)

1533

1534

[ 1547](group__timeutil__unit__apis.md#ga4601ea99148307043d2d47a2e9fccb8e)#define k\_cyc\_to\_ticks\_near32(t) \

1548 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, true)

1549

1550

[ 1563](group__timeutil__unit__apis.md#gafa97757f07a5048d67d6eca4a72cf39c)#define k\_cyc\_to\_ticks\_near64(t) \

1564 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, true)

1565

1566

[ 1579](group__timeutil__unit__apis.md#gae7653e92b9b44accaa9ee2764237f595)#define k\_cyc\_to\_ticks\_ceil32(t) \

1580 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, true, false)

1581

1582

[ 1595](group__timeutil__unit__apis.md#ga0fa410ff13d0cd467d160c1c14cf24a6)#define k\_cyc\_to\_ticks\_ceil64(t) \

1596 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, true, false)

1597

1598

[ 1611](group__timeutil__unit__apis.md#ga824ffc9857fa2d4bccb3a9f4a56b8f18)#define k\_ticks\_to\_sec\_floor32(t) \

1612 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, false)

1613

1614

[ 1627](group__timeutil__unit__apis.md#ga6e9ef943c78cbb5963d8eece896b6189)#define k\_ticks\_to\_sec\_floor64(t) \

1628 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, false)

1629

1630

[ 1643](group__timeutil__unit__apis.md#ga15284161d40816f06b2bbf4cd03a0fed)#define k\_ticks\_to\_sec\_near32(t) \

1644 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, true)

1645

1646

[ 1659](group__timeutil__unit__apis.md#gab6b9b6d752ec3c8b69d9f27ca5f7b85e)#define k\_ticks\_to\_sec\_near64(t) \

1660 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, true)

1661

1662

[ 1675](group__timeutil__unit__apis.md#ga3986215ef060ab2ff9cc7c576eb05b01)#define k\_ticks\_to\_sec\_ceil32(t) \

1676 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, true, false)

1677

1678

[ 1691](group__timeutil__unit__apis.md#ga02493c454fbbbf6787b036ca7f739073)#define k\_ticks\_to\_sec\_ceil64(t) \

1692 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, true, false)

1693

1694

[ 1707](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)#define k\_ticks\_to\_ms\_floor32(t) \

1708 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, false)

1709

1710

[ 1723](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)#define k\_ticks\_to\_ms\_floor64(t) \

1724 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, false)

1725

1726

[ 1739](group__timeutil__unit__apis.md#ga8f1133f69f154d593fc127d2b00931c8)#define k\_ticks\_to\_ms\_near32(t) \

1740 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, true)

1741

1742

[ 1755](group__timeutil__unit__apis.md#gac3578501567233a7576c61cfd6cf28cb)#define k\_ticks\_to\_ms\_near64(t) \

1756 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, true)

1757

1758

[ 1771](group__timeutil__unit__apis.md#ga3f2c3cf86ef1d243b43f29958a108088)#define k\_ticks\_to\_ms\_ceil32(t) \

1772 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, true, false)

1773

1774

[ 1787](group__timeutil__unit__apis.md#gabee58122304820b36d601268eb4598e2)#define k\_ticks\_to\_ms\_ceil64(t) \

1788 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, true, false)

1789

1790

[ 1803](group__timeutil__unit__apis.md#ga86767fd65071fc7c57f25434386caeed)#define k\_ticks\_to\_us\_floor32(t) \

1804 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, false)

1805

1806

[ 1819](group__timeutil__unit__apis.md#ga27cac5d9974320ef12c6bcacdae8b47c)#define k\_ticks\_to\_us\_floor64(t) \

1820 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, false)

1821

1822

[ 1835](group__timeutil__unit__apis.md#ga328649dd1ec1fae9c69eb3a75709a9f2)#define k\_ticks\_to\_us\_near32(t) \

1836 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, true)

1837

1838

[ 1851](group__timeutil__unit__apis.md#ga5735cb347e01fa391368d2fb54d6d965)#define k\_ticks\_to\_us\_near64(t) \

1852 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, true)

1853

1854

[ 1867](group__timeutil__unit__apis.md#gadd968c2033d548c03072e46c895375bc)#define k\_ticks\_to\_us\_ceil32(t) \

1868 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, true, false)

1869

1870

[ 1883](group__timeutil__unit__apis.md#gad1c6d9e60835c6c00960778395cdbacc)#define k\_ticks\_to\_us\_ceil64(t) \

1884 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, true, false)

1885

1886

[ 1899](group__timeutil__unit__apis.md#ga5c2a1ae6f66fcf22971c40301e78be8a)#define k\_ticks\_to\_ns\_floor32(t) \

1900 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, false)

1901

1902

[ 1915](group__timeutil__unit__apis.md#ga8c8c4d713c5716e5b0d41b014b394edf)#define k\_ticks\_to\_ns\_floor64(t) \

1916 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, false)

1917

1918

[ 1931](group__timeutil__unit__apis.md#ga26c20d96c08dc26d4664f3d66507e0bb)#define k\_ticks\_to\_ns\_near32(t) \

1932 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, true)

1933

1934

[ 1947](group__timeutil__unit__apis.md#ga3b0a2f92a3d61be64d4b80101129bc83)#define k\_ticks\_to\_ns\_near64(t) \

1948 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, true)

1949

1950

[ 1963](group__timeutil__unit__apis.md#gae28b7099ffbda7617f4049cd730921f8)#define k\_ticks\_to\_ns\_ceil32(t) \

1964 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, true, false)

1965

1966

[ 1979](group__timeutil__unit__apis.md#ga0221878e17c689e7f40940a201c4fdd7)#define k\_ticks\_to\_ns\_ceil64(t) \

1980 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, true, false)

1981

1982

[ 1995](group__timeutil__unit__apis.md#ga629a18a817e4b0240dc6bc9018d8809a)#define k\_ticks\_to\_cyc\_floor32(t) \

1996 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, false)

1997

1998

[ 2011](group__timeutil__unit__apis.md#ga5593c0751ec707a63ce25aed1567b2de)#define k\_ticks\_to\_cyc\_floor64(t) \

2012 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, false)

2013

2014

[ 2027](group__timeutil__unit__apis.md#gaf8d7352f4d2325ddb3aec3111cc8e124)#define k\_ticks\_to\_cyc\_near32(t) \

2028 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, true)

2029

2030

[ 2043](group__timeutil__unit__apis.md#ga7eed234908b9db5236de6c7543f40da1)#define k\_ticks\_to\_cyc\_near64(t) \

2044 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, true)

2045

2046

[ 2059](group__timeutil__unit__apis.md#ga00f31f894f66dde999714fe0cbab2178)#define k\_ticks\_to\_cyc\_ceil32(t) \

2060 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, true, false)

2061

2062

[ 2075](group__timeutil__unit__apis.md#ga4fa97b6aa81457142fc82cc73ef6c7a5)#define k\_ticks\_to\_cyc\_ceil64(t) \

2076 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, true, false)

2077

2078#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

2079#include <zephyr/syscalls/time\_units.h>

2080#endif

2081

2082#undef TIME\_CONSTEXPR

2083

2087

2088#ifdef \_\_cplusplus

2089} /\* extern "C" \*/

2090#endif

2091

2092#endif /\* ZEPHYR\_INCLUDE\_TIME\_UNITS\_H\_ \*/

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [time\_units.h](time__units_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
