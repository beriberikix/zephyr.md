---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/time__units_8h_source.html
original_path: doxygen/html/time__units_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

11#include <[zephyr/sys/util.h](util_8h.md)>

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

[ 43](group__timeutil__unit__apis.md#ga6504e9e6fe4955e0bc31eccd4cfc01b7)#define SYS\_TIMEOUT\_MS(ms) Z\_TIMEOUT\_TICKS((ms) == SYS\_FOREVER\_MS ? \

44 K\_TICKS\_FOREVER : Z\_TIMEOUT\_MS\_TICKS(ms))

45

46/\* Exhaustively enumerated, highly optimized time unit conversion API \*/

47

48#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

49\_\_syscall int sys\_clock\_hw\_cycles\_per\_sec\_runtime\_get(void);

50

51static inline int z\_impl\_sys\_clock\_hw\_cycles\_per\_sec\_runtime\_get(void)

52{

53 extern int z\_clock\_hw\_cycles\_per\_sec;

54

55 return z\_clock\_hw\_cycles\_per\_sec;

56}

57#endif /\* CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME \*/

58

59#if defined(\_\_cplusplus) && \_\_cplusplus >= 201402L

60 #if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

61 #define TIME\_CONSTEXPR

62 #else

63 #define TIME\_CONSTEXPR constexpr

64 #endif

65#else

[ 66](group__timeutil__unit__apis.md#ga387f15169fe1c0c58745548eceae1556) #define TIME\_CONSTEXPR

67#endif

68

73#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

74#define sys\_clock\_hw\_cycles\_per\_sec() sys\_clock\_hw\_cycles\_per\_sec\_runtime\_get()

75#else

[ 76](group__timeutil__unit__apis.md#gafe3ef19636d5002350794fa01b480d16)#define sys\_clock\_hw\_cycles\_per\_sec() CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC

77#endif

78

90#define z\_tmcvt\_use\_fast\_algo(from\_hz, to\_hz) \

91 ((DIV\_ROUND\_UP(CONFIG\_SYS\_CLOCK\_MAX\_TIMEOUT\_DAYS \* 24ULL \* 3600ULL \* from\_hz, \

92 UINT32\_MAX) \* to\_hz) <= UINT32\_MAX)

93

94/\* Time converter generator gadget. Selects from one of three

95 \* conversion algorithms: ones that take advantage when the

96 \* frequencies are an integer ratio (in either direction), or a full

97 \* precision conversion. Clever use of extra arguments causes all the

98 \* selection logic to be optimized out, and the generated code even

99 \* reduces to 32 bit only if a ratio conversion is available and the

100 \* result is 32 bits.

101 \*

102 \* This isn't intended to be used directly, instead being wrapped

103 \* appropriately in a user-facing API. The boolean arguments are:

104 \*

105 \* const\_hz - The hz arguments are known to be compile-time

106 \* constants (because otherwise the modulus test would

107 \* have to be done at runtime)

108 \* result32 - The result will be truncated to 32 bits on use

109 \* round\_up - Return the ceiling of the resulting fraction

110 \* round\_off - Return the nearest value to the resulting fraction

111 \* (pass both round\_up/off as false to get "round\_down")

112 \*

113 \* All of this must be implemented as expressions so that, when constant,

114 \* the results may be used to initialize global variables.

115 \*/

116

117/\* true if the conversion is the identity \*/

118#define z\_tmcvt\_is\_identity(\_\_from\_hz, \_\_to\_hz) \

119 ((\_\_to\_hz) == (\_\_from\_hz))

120

121/\* true if the conversion requires a simple integer multiply \*/

122#define z\_tmcvt\_is\_int\_mul(\_\_from\_hz, \_\_to\_hz) \

123 ((\_\_to\_hz) > (\_\_from\_hz) && (\_\_to\_hz) % (\_\_from\_hz) == 0U)

124

125/\* true if the conversion requires a simple integer division \*/

126#define z\_tmcvt\_is\_int\_div(\_\_from\_hz, \_\_to\_hz) \

127 ((\_\_from\_hz) > (\_\_to\_hz) && (\_\_from\_hz) % (\_\_to\_hz) == 0U)

128

129/\*

130 \* Compute the offset needed to round the result correctly when

131 \* the conversion requires a simple integer division

132 \*/

133#define z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

134 ((\_\_round\_off) ? ((\_\_from\_hz) / (\_\_to\_hz)) / 2 : \

135 (\_\_round\_up) ? ((\_\_from\_hz) / (\_\_to\_hz)) - 1 : \

136 0)

137

138/\*

139 \* All users of this macro MUST ensure its output is never used when a/b

140 \* is zero because it incorrectly but by design never returns zero.

141 \*

142 \* Some compiler versions emit a divide-by-zero warning for this code:

143 \* "false ? 42/0 : 43". Dealing with (generated) dead code is hard:

144 \* https://github.com/zephyrproject-rtos/zephyr/issues/63564

145 \* https://blog.llvm.org/2011/05/what-every-c-programmer-should-know\_21.html

146 \*

147 \* To silence such divide-by-zero warnings, "cheat" and never return

148 \* zero. Return 1 instead. Use octal "01u" as a breadcrumb to ease a

149 \* little bit the huge pain of "reverse-engineering" pre-processor

150 \* output.

151 \*

152 \* The "Elvis" operator "a/b ?: 1" is tempting because it avoids

153 \* evaluating the same expression twice. However: 1. it's a non-standard

154 \* GNU extension; 2. everything in this file is designed to be computed

155 \* at compile time anyway.

156 \*/

157#define z\_tmcvt\_divisor(a, b) ((a)/(b) ? (a)/(b) : 01u)

158

159/\*

160 \* Compute the offset needed to round the result correctly when

161 \* the conversion requires a full mul/div

162 \*/

163#define z\_tmcvt\_off\_gen(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

164 ((\_\_round\_off) ? (\_\_from\_hz) / 2 : \

165 (\_\_round\_up) ? (\_\_from\_hz) - 1 : \

166 0)

167

168/\* Integer division 32-bit conversion \*/

169#define z\_tmcvt\_int\_div\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

170 ((uint64\_t) (\_\_t) <= 0xffffffffU - \

171 z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) ? \

172 ((uint32\_t)((\_\_t) + \

173 z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \

174 \_\_round\_up, \_\_round\_off)) / \

175 z\_tmcvt\_divisor(\_\_from\_hz, \_\_to\_hz)) \

176 : \

177 (uint32\_t) (((uint64\_t) (\_\_t) + \

178 z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \

179 \_\_round\_up, \_\_round\_off)) / \

180 z\_tmcvt\_divisor(\_\_from\_hz, \_\_to\_hz)) \

181 )

182

183/\* Integer multiplication 32-bit conversion \*/

184#define z\_tmcvt\_int\_mul\_32(\_\_t, \_\_from\_hz, \_\_to\_hz) \

185 (uint32\_t) (\_\_t)\*((\_\_to\_hz) / (\_\_from\_hz))

186

187/\* General 32-bit conversion \*/

188#define z\_tmcvt\_gen\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

189 ((uint32\_t) (((uint64\_t) (\_\_t)\*(\_\_to\_hz) + \

190 z\_tmcvt\_off\_gen(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off)) / (\_\_from\_hz)))

191

192/\* Integer division 64-bit conversion \*/

193#define z\_tmcvt\_int\_div\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

194 (((uint64\_t) (\_\_t) + z\_tmcvt\_off\_div(\_\_from\_hz, \_\_to\_hz, \

195 \_\_round\_up, \_\_round\_off)) / \

196 z\_tmcvt\_divisor(\_\_from\_hz, \_\_to\_hz))

197

198/\* Integer multiplcation 64-bit conversion \*/

199#define z\_tmcvt\_int\_mul\_64(\_\_t, \_\_from\_hz, \_\_to\_hz) \

200 (uint64\_t) (\_\_t)\*((\_\_to\_hz) / (\_\_from\_hz))

201

202/\* Fast 64-bit conversion. This relies on the multiply not overflowing \*/

203#define z\_tmcvt\_gen\_64\_fast(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

204 (((uint64\_t) (\_\_t)\*(\_\_to\_hz) + \

205 z\_tmcvt\_off\_gen(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off)) / (\_\_from\_hz))

206

207/\* Slow 64-bit conversion. This avoids overflowing the multiply \*/

208#define z\_tmcvt\_gen\_64\_slow(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

209 (((uint64\_t) (\_\_t) / (\_\_from\_hz))\*(\_\_to\_hz) + \

210 (((uint64\_t) (\_\_t) % (\_\_from\_hz))\*(\_\_to\_hz) + \

211 z\_tmcvt\_off\_gen(\_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off)) / (\_\_from\_hz))

212

213/\* General 64-bit conversion. Uses one of the two above macros \*/

214#define z\_tmcvt\_gen\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

215 (z\_tmcvt\_use\_fast\_algo(\_\_from\_hz, \_\_to\_hz) ? \

216 z\_tmcvt\_gen\_64\_fast(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) : \

217 z\_tmcvt\_gen\_64\_slow(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off))

218

219/\* Convert, generating a 32-bit result \*/

220#define z\_tmcvt\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_round\_up, \_\_round\_off) \

221 ((\_\_const\_hz) ? \

222 ( \

223 z\_tmcvt\_is\_identity(\_\_from\_hz, \_\_to\_hz) ? \

224 (uint32\_t) (\_\_t) \

225 : \

226 z\_tmcvt\_is\_int\_div(\_\_from\_hz, \_\_to\_hz) ? \

227 z\_tmcvt\_int\_div\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

228 : \

229 z\_tmcvt\_is\_int\_mul(\_\_from\_hz, \_\_to\_hz) ? \

230 z\_tmcvt\_int\_mul\_32(\_\_t, \_\_from\_hz, \_\_to\_hz) \

231 : \

232 z\_tmcvt\_gen\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

233 ) \

234 : \

235 z\_tmcvt\_gen\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

236 )

237

238/\* Convert, generating a 64-bit result \*/

239#define z\_tmcvt\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_round\_up, \_\_round\_off) \

240 ((\_\_const\_hz) ? \

241 ( \

242 z\_tmcvt\_is\_identity(\_\_from\_hz, \_\_to\_hz) ? \

243 (uint64\_t) (\_\_t) \

244 : \

245 z\_tmcvt\_is\_int\_div(\_\_from\_hz, \_\_to\_hz) ? \

246 z\_tmcvt\_int\_div\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

247 : \

248 z\_tmcvt\_is\_int\_mul(\_\_from\_hz, \_\_to\_hz) ? \

249 z\_tmcvt\_int\_mul\_64(\_\_t, \_\_from\_hz, \_\_to\_hz) \

250 : \

251 z\_tmcvt\_gen\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

252 ) \

253 : \

254 z\_tmcvt\_gen\_64\_slow(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_round\_up, \_\_round\_off) \

255 )

256

257#define z\_tmcvt(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_result32, \_\_round\_up, \_\_round\_off) \

258 ((\_\_result32) ? \

259 z\_tmcvt\_32(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_round\_up, \_\_round\_off) : \

260 z\_tmcvt\_64(\_\_t, \_\_from\_hz, \_\_to\_hz, \_\_const\_hz, \_\_round\_up, \_\_round\_off))

261

262/\* The following code is programmatically generated using this perl

263 \* code, which enumerates all possible combinations of units, rounding

264 \* modes and precision. Do not edit directly.

265 \*

266 \* Note that nano/microsecond conversions are only defined with 64 bit

267 \* precision. These units conversions were not available in 32 bit

268 \* variants historically, and doing 32 bit math with units that small

269 \* has precision traps that we probably don't want to support in an

270 \* official API.

271 \*

272 \* #!/usr/bin/perl -w

273 \* use strict;

274 \*

275 \* my %human = ("ms" => "milliseconds",

276 \* "us" => "microseconds",

277 \* "ns" => "nanoseconds",

278 \* "cyc" => "hardware cycles",

279 \* "ticks" => "ticks");

280 \* my %human\_round = ("ceil" => "Rounds up",

281 \* "near" => "Round nearest",

282 \* "floor" => "Truncates");

283 \*

284 \* sub big { return $\_[0] eq "us" || $\_[0] eq "ns"; }

285 \* sub prefix { return $\_[0] eq "ms" || $\_[0] eq "us" || $\_[0] eq "ns"; }

286 \*

287 \* for my $from\_unit ("ms", "us", "ns", "cyc", "ticks") {

288 \* for my $to\_unit ("ms", "us", "ns", "cyc", "ticks") {

289 \* next if $from\_unit eq $to\_unit;

290 \* next if prefix($from\_unit) && prefix($to\_unit);

291 \* for my $round ("floor", "near", "ceil") {

292 \* for(my $big=0; $big <= 1; $big++) {

293 \* my $sz = $big ? 64 : 32;

294 \* my $sym = "k\_${from\_unit}\_to\_${to\_unit}\_$round$sz";

295 \* my $type = "uint${sz}\_t";

296 \* my $const\_hz = ($from\_unit eq "cyc" || $to\_unit eq "cyc")

297 \* ? "Z\_CCYC" : "true";

298 \* my $ret32 = $big ? "64" : "32";

299 \* my $rup = $round eq "ceil" ? "true" : "false";

300 \* my $roff = $round eq "near" ? "true" : "false";

301 \*

302 \* my $hfrom = $human{$from\_unit};

303 \* my $hto = $human{$to\_unit};

304 \* my $hround = $human\_round{$round};

305 \* print "/", "\*\* \@brief Convert $hfrom to $hto. $ret32 bits. $hround.\n";

306 \* print " \*\n";

307 \* print " \* Converts time values in $hfrom to $hto.\n";

308 \* print " \* Computes result in $sz bit precision.\n";

309 \* if ($round eq "ceil") {

310 \* print " \* Rounds up to the next highest output unit.\n";

311 \* } elsif ($round eq "near") {

312 \* print " \* Rounds to the nearest output unit.\n";

313 \* } else {

314 \* print " \* Truncates to the next lowest output unit.\n";

315 \* }

316 \* print " \*\n";

317 \* print " \* \@param t Source time in $hfrom. uint64\_t\n";

318 \* print " \*\n";

319 \* print " \* \@return The converted time value in $hto. $type\n";

320 \* print " \*", "/\n";

321 \*

322 \* print "/", "\* Generated. Do not edit. See above. \*", "/\n";

323 \* print "#define $sym(t) \\\n";

324 \* print "\tz\_tmcvt\_$ret32(t, Z\_HZ\_$from\_unit, Z\_HZ\_$to\_unit,";

325 \* print " $const\_hz, $rup, $roff)\n";

326 \* print "\n\n";

327 \* }

328 \* }

329 \* }

330 \* }

331 \*/

332

333/\* Some more concise declarations to simplify the generator script and

334 \* save bytes below

335 \*/

336#define Z\_HZ\_ms 1000

337#define Z\_HZ\_us 1000000

338#define Z\_HZ\_ns 1000000000

339#define Z\_HZ\_cyc sys\_clock\_hw\_cycles\_per\_sec()

340#define Z\_HZ\_ticks CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC

341#define Z\_CCYC (!IS\_ENABLED(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME))

342

353/\* Generated. Do not edit. See above. \*/

[ 354](group__timeutil__unit__apis.md#ga2d60494645102034a7864ab0235bbfe4)#define k\_ms\_to\_cyc\_floor32(t) \

355 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, false)

356

357

368/\* Generated. Do not edit. See above. \*/

[ 369](group__timeutil__unit__apis.md#ga4d3e1ec8eed229a08072aea744d40bba)#define k\_ms\_to\_cyc\_floor64(t) \

370 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, false)

371

372

383/\* Generated. Do not edit. See above. \*/

[ 384](group__timeutil__unit__apis.md#ga8a0d31e998f1a19a3ee8200c173eb7c9)#define k\_ms\_to\_cyc\_near32(t) \

385 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, true)

386

387

398/\* Generated. Do not edit. See above. \*/

[ 399](group__timeutil__unit__apis.md#gab2bcf34a4899619fcf083819a078a09e)#define k\_ms\_to\_cyc\_near64(t) \

400 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, true)

401

402

413/\* Generated. Do not edit. See above. \*/

[ 414](group__timeutil__unit__apis.md#gab4636150867df2c4e918c12ec2e9bc5f)#define k\_ms\_to\_cyc\_ceil32(t) \

415 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, true, false)

416

417

428/\* Generated. Do not edit. See above. \*/

[ 429](group__timeutil__unit__apis.md#ga82829fc9e99658faf91e5925c9545c9f)#define k\_ms\_to\_cyc\_ceil64(t) \

430 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, true, false)

431

432

443/\* Generated. Do not edit. See above. \*/

[ 444](group__timeutil__unit__apis.md#gaf41d7ca19e5bb47824374698ce409ea1)#define k\_ms\_to\_ticks\_floor32(t) \

445 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, false)

446

447

458/\* Generated. Do not edit. See above. \*/

[ 459](group__timeutil__unit__apis.md#gaa6ea6977308dfd2f092ba0ac4e779a31)#define k\_ms\_to\_ticks\_floor64(t) \

460 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, false)

461

462

473/\* Generated. Do not edit. See above. \*/

[ 474](group__timeutil__unit__apis.md#ga0a61385f187c7c2a0f5288b17873b3db)#define k\_ms\_to\_ticks\_near32(t) \

475 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, true)

476

477

488/\* Generated. Do not edit. See above. \*/

[ 489](group__timeutil__unit__apis.md#gab2f6dd223151224cd9fa0491f196c1f6)#define k\_ms\_to\_ticks\_near64(t) \

490 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, true)

491

492

503/\* Generated. Do not edit. See above. \*/

[ 504](group__timeutil__unit__apis.md#gac74a319bcb69cc714818413ae15af7a2)#define k\_ms\_to\_ticks\_ceil32(t) \

505 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, true, false)

506

507

518/\* Generated. Do not edit. See above. \*/

[ 519](group__timeutil__unit__apis.md#gaa623d51d51b18a2e54b20d36d2f81c42)#define k\_ms\_to\_ticks\_ceil64(t) \

520 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, true, false)

521

522

533/\* Generated. Do not edit. See above. \*/

[ 534](group__timeutil__unit__apis.md#ga66c1ea8197e7adc01c837163e0aa4b62)#define k\_us\_to\_cyc\_floor32(t) \

535 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, false)

536

537

548/\* Generated. Do not edit. See above. \*/

[ 549](group__timeutil__unit__apis.md#gac78731d5891b2389dc227608decf28dd)#define k\_us\_to\_cyc\_floor64(t) \

550 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, false)

551

552

563/\* Generated. Do not edit. See above. \*/

[ 564](group__timeutil__unit__apis.md#ga01dabb87e1a4864e47fcd39cc4bce869)#define k\_us\_to\_cyc\_near32(t) \

565 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, true)

566

567

578/\* Generated. Do not edit. See above. \*/

[ 579](group__timeutil__unit__apis.md#ga49a64e1f11cf450fdd770d67617cbe23)#define k\_us\_to\_cyc\_near64(t) \

580 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, true)

581

582

593/\* Generated. Do not edit. See above. \*/

[ 594](group__timeutil__unit__apis.md#ga689a3f97643be5362c8c70c6d9d81051)#define k\_us\_to\_cyc\_ceil32(t) \

595 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, true, false)

596

597

608/\* Generated. Do not edit. See above. \*/

[ 609](group__timeutil__unit__apis.md#ga2f65f04acc1daf019470beb04f16e276)#define k\_us\_to\_cyc\_ceil64(t) \

610 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, true, false)

611

612

623/\* Generated. Do not edit. See above. \*/

[ 624](group__timeutil__unit__apis.md#ga96f32803affb56c366cbab5967c6b76c)#define k\_us\_to\_ticks\_floor32(t) \

625 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, false)

626

627

638/\* Generated. Do not edit. See above. \*/

[ 639](group__timeutil__unit__apis.md#gaf6b4fb83131e5a52d9be875e5466d022)#define k\_us\_to\_ticks\_floor64(t) \

640 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, false)

641

642

653/\* Generated. Do not edit. See above. \*/

[ 654](group__timeutil__unit__apis.md#ga5b0286cc82370178c852c3fa290eb61d)#define k\_us\_to\_ticks\_near32(t) \

655 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, true)

656

657

668/\* Generated. Do not edit. See above. \*/

[ 669](group__timeutil__unit__apis.md#gaf2aae5316fcb5e99f4a77b99a5db27f9)#define k\_us\_to\_ticks\_near64(t) \

670 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, true)

671

672

683/\* Generated. Do not edit. See above. \*/

[ 684](group__timeutil__unit__apis.md#ga950ac5ce654ec92e0af61e000de884a7)#define k\_us\_to\_ticks\_ceil32(t) \

685 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, true, false)

686

687

698/\* Generated. Do not edit. See above. \*/

[ 699](group__timeutil__unit__apis.md#ga1a977f93dc94ce9db54b3c9fdf9ba2f9)#define k\_us\_to\_ticks\_ceil64(t) \

700 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, true, false)

701

702

713/\* Generated. Do not edit. See above. \*/

[ 714](group__timeutil__unit__apis.md#ga46013e42990cfa561da06fb2bffaa261)#define k\_ns\_to\_cyc\_floor32(t) \

715 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, false)

716

717

728/\* Generated. Do not edit. See above. \*/

[ 729](group__timeutil__unit__apis.md#gafc4ff458df5f4d1f221bcf0799d25335)#define k\_ns\_to\_cyc\_floor64(t) \

730 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, false)

731

732

743/\* Generated. Do not edit. See above. \*/

[ 744](group__timeutil__unit__apis.md#gac8e586ebc94174ccdabf6f49dd0251e6)#define k\_ns\_to\_cyc\_near32(t) \

745 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, true)

746

747

758/\* Generated. Do not edit. See above. \*/

[ 759](group__timeutil__unit__apis.md#gae6ec742a39a72b0a3dd7bc3da4a98403)#define k\_ns\_to\_cyc\_near64(t) \

760 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, true)

761

762

773/\* Generated. Do not edit. See above. \*/

[ 774](group__timeutil__unit__apis.md#ga928ace6a14c0c2eb6aaa027f545601a7)#define k\_ns\_to\_cyc\_ceil32(t) \

775 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, true, false)

776

777

788/\* Generated. Do not edit. See above. \*/

[ 789](group__timeutil__unit__apis.md#ga82264e42744defb8acf69caa8612e476)#define k\_ns\_to\_cyc\_ceil64(t) \

790 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, true, false)

791

792

803/\* Generated. Do not edit. See above. \*/

[ 804](group__timeutil__unit__apis.md#ga4b0a61273dfbebd9273c0dc71ea74c65)#define k\_ns\_to\_ticks\_floor32(t) \

805 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, false)

806

807

818/\* Generated. Do not edit. See above. \*/

[ 819](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)#define k\_ns\_to\_ticks\_floor64(t) \

820 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, false)

821

822

833/\* Generated. Do not edit. See above. \*/

[ 834](group__timeutil__unit__apis.md#ga308b172f1fb6e1452c14db444ad7e75e)#define k\_ns\_to\_ticks\_near32(t) \

835 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, true)

836

837

848/\* Generated. Do not edit. See above. \*/

[ 849](group__timeutil__unit__apis.md#ga50c08351970ea8e62a0509b68898901a)#define k\_ns\_to\_ticks\_near64(t) \

850 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, true)

851

852

863/\* Generated. Do not edit. See above. \*/

[ 864](group__timeutil__unit__apis.md#gad958afbd9f86f94ccd5c9569e7587fad)#define k\_ns\_to\_ticks\_ceil32(t) \

865 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, true, false)

866

867

878/\* Generated. Do not edit. See above. \*/

[ 879](group__timeutil__unit__apis.md#ga1078f0f8764f7bad744cfb1ffd675c70)#define k\_ns\_to\_ticks\_ceil64(t) \

880 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, true, false)

881

882

893/\* Generated. Do not edit. See above. \*/

[ 894](group__timeutil__unit__apis.md#ga5f9f903e6e4eba5415cae3f337d565ed)#define k\_cyc\_to\_ms\_floor32(t) \

895 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, false)

896

897

908/\* Generated. Do not edit. See above. \*/

[ 909](group__timeutil__unit__apis.md#gaeaa9339beec5b82b924302bbc57923f6)#define k\_cyc\_to\_ms\_floor64(t) \

910 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, false)

911

912

923/\* Generated. Do not edit. See above. \*/

[ 924](group__timeutil__unit__apis.md#gaba2f18bc00740fb0411371d2d2f3d949)#define k\_cyc\_to\_ms\_near32(t) \

925 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, true)

926

927

938/\* Generated. Do not edit. See above. \*/

[ 939](group__timeutil__unit__apis.md#ga217f0b8bf86a24654419c3ccfd6e7822)#define k\_cyc\_to\_ms\_near64(t) \

940 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, true)

941

942

953/\* Generated. Do not edit. See above. \*/

[ 954](group__timeutil__unit__apis.md#ga40bf11b01ba76673c67569e8d1e55d92)#define k\_cyc\_to\_ms\_ceil32(t) \

955 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, true, false)

956

957

968/\* Generated. Do not edit. See above. \*/

[ 969](group__timeutil__unit__apis.md#gaf85474dc07ce8165379415f4977aa44f)#define k\_cyc\_to\_ms\_ceil64(t) \

970 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, true, false)

971

972

983/\* Generated. Do not edit. See above. \*/

[ 984](group__timeutil__unit__apis.md#ga86392f2bddfbb7c895c08becf9c8c485)#define k\_cyc\_to\_us\_floor32(t) \

985 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, false)

986

987

998/\* Generated. Do not edit. See above. \*/

[ 999](group__timeutil__unit__apis.md#gad3376aa7ab36b6b7f5a1f9c9977cee4a)#define k\_cyc\_to\_us\_floor64(t) \

1000 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, false)

1001

1002

1013/\* Generated. Do not edit. See above. \*/

[ 1014](group__timeutil__unit__apis.md#ga1314249a8a404f00c8a03d6c77e0c752)#define k\_cyc\_to\_us\_near32(t) \

1015 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, true)

1016

1017

1028/\* Generated. Do not edit. See above. \*/

[ 1029](group__timeutil__unit__apis.md#ga869ccaf50e83712d0bafe0f8e238fc61)#define k\_cyc\_to\_us\_near64(t) \

1030 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, true)

1031

1032

1043/\* Generated. Do not edit. See above. \*/

[ 1044](group__timeutil__unit__apis.md#ga051fbec0b352b4fb3116544c8c33250a)#define k\_cyc\_to\_us\_ceil32(t) \

1045 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, true, false)

1046

1047

1058/\* Generated. Do not edit. See above. \*/

[ 1059](group__timeutil__unit__apis.md#ga90b09be4536f6877f67a60b3c33f5299)#define k\_cyc\_to\_us\_ceil64(t) \

1060 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, true, false)

1061

1062

1073/\* Generated. Do not edit. See above. \*/

[ 1074](group__timeutil__unit__apis.md#ga775c4d72bd0ecb9a6ad947f34c479754)#define k\_cyc\_to\_ns\_floor32(t) \

1075 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, false)

1076

1077

1088/\* Generated. Do not edit. See above. \*/

[ 1089](group__timeutil__unit__apis.md#ga665d5fc98ffe8bd1cf78ca994f58724a)#define k\_cyc\_to\_ns\_floor64(t) \

1090 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, false)

1091

1092

1103/\* Generated. Do not edit. See above. \*/

[ 1104](group__timeutil__unit__apis.md#gabd5378a62e480fc1b79b3326c8f02d5f)#define k\_cyc\_to\_ns\_near32(t) \

1105 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, true)

1106

1107

1118/\* Generated. Do not edit. See above. \*/

[ 1119](group__timeutil__unit__apis.md#gad36269d0d63bee37e09da46cfe516c8c)#define k\_cyc\_to\_ns\_near64(t) \

1120 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, true)

1121

1122

1133/\* Generated. Do not edit. See above. \*/

[ 1134](group__timeutil__unit__apis.md#ga19526c845440ed793068fa8d8d5088ff)#define k\_cyc\_to\_ns\_ceil32(t) \

1135 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, true, false)

1136

1137

1148/\* Generated. Do not edit. See above. \*/

[ 1149](group__timeutil__unit__apis.md#gab2889da75f359d248a6eb61fdc3d53c0)#define k\_cyc\_to\_ns\_ceil64(t) \

1150 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, true, false)

1151

1152

1163/\* Generated. Do not edit. See above. \*/

[ 1164](group__timeutil__unit__apis.md#ga2efd0e2611cbeb696778eb73cf24b7ee)#define k\_cyc\_to\_ticks\_floor32(t) \

1165 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, false)

1166

1167

1178/\* Generated. Do not edit. See above. \*/

[ 1179](group__timeutil__unit__apis.md#gaad0256d9429dfa5c5a194f1419691cfc)#define k\_cyc\_to\_ticks\_floor64(t) \

1180 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, false)

1181

1182

1193/\* Generated. Do not edit. See above. \*/

[ 1194](group__timeutil__unit__apis.md#ga4601ea99148307043d2d47a2e9fccb8e)#define k\_cyc\_to\_ticks\_near32(t) \

1195 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, true)

1196

1197

1208/\* Generated. Do not edit. See above. \*/

[ 1209](group__timeutil__unit__apis.md#gafa97757f07a5048d67d6eca4a72cf39c)#define k\_cyc\_to\_ticks\_near64(t) \

1210 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, true)

1211

1212

1223/\* Generated. Do not edit. See above. \*/

[ 1224](group__timeutil__unit__apis.md#gae7653e92b9b44accaa9ee2764237f595)#define k\_cyc\_to\_ticks\_ceil32(t) \

1225 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, true, false)

1226

1227

1238/\* Generated. Do not edit. See above. \*/

[ 1239](group__timeutil__unit__apis.md#ga0fa410ff13d0cd467d160c1c14cf24a6)#define k\_cyc\_to\_ticks\_ceil64(t) \

1240 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, true, false)

1241

1242

1253/\* Generated. Do not edit. See above. \*/

[ 1254](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)#define k\_ticks\_to\_ms\_floor32(t) \

1255 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, false)

1256

1257

1268/\* Generated. Do not edit. See above. \*/

[ 1269](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)#define k\_ticks\_to\_ms\_floor64(t) \

1270 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, false)

1271

1272

1283/\* Generated. Do not edit. See above. \*/

[ 1284](group__timeutil__unit__apis.md#ga8f1133f69f154d593fc127d2b00931c8)#define k\_ticks\_to\_ms\_near32(t) \

1285 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, true)

1286

1287

1298/\* Generated. Do not edit. See above. \*/

[ 1299](group__timeutil__unit__apis.md#gac3578501567233a7576c61cfd6cf28cb)#define k\_ticks\_to\_ms\_near64(t) \

1300 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, true)

1301

1302

1313/\* Generated. Do not edit. See above. \*/

[ 1314](group__timeutil__unit__apis.md#ga3f2c3cf86ef1d243b43f29958a108088)#define k\_ticks\_to\_ms\_ceil32(t) \

1315 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, true, false)

1316

1317

1328/\* Generated. Do not edit. See above. \*/

[ 1329](group__timeutil__unit__apis.md#gabee58122304820b36d601268eb4598e2)#define k\_ticks\_to\_ms\_ceil64(t) \

1330 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, true, false)

1331

1332

1343/\* Generated. Do not edit. See above. \*/

[ 1344](group__timeutil__unit__apis.md#ga86767fd65071fc7c57f25434386caeed)#define k\_ticks\_to\_us\_floor32(t) \

1345 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, false)

1346

1347

1358/\* Generated. Do not edit. See above. \*/

[ 1359](group__timeutil__unit__apis.md#ga27cac5d9974320ef12c6bcacdae8b47c)#define k\_ticks\_to\_us\_floor64(t) \

1360 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, false)

1361

1362

1373/\* Generated. Do not edit. See above. \*/

[ 1374](group__timeutil__unit__apis.md#ga328649dd1ec1fae9c69eb3a75709a9f2)#define k\_ticks\_to\_us\_near32(t) \

1375 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, true)

1376

1377

1388/\* Generated. Do not edit. See above. \*/

[ 1389](group__timeutil__unit__apis.md#ga5735cb347e01fa391368d2fb54d6d965)#define k\_ticks\_to\_us\_near64(t) \

1390 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, true)

1391

1392

1403/\* Generated. Do not edit. See above. \*/

[ 1404](group__timeutil__unit__apis.md#gadd968c2033d548c03072e46c895375bc)#define k\_ticks\_to\_us\_ceil32(t) \

1405 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, true, false)

1406

1407

1418/\* Generated. Do not edit. See above. \*/

[ 1419](group__timeutil__unit__apis.md#gad1c6d9e60835c6c00960778395cdbacc)#define k\_ticks\_to\_us\_ceil64(t) \

1420 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, true, false)

1421

1422

1433/\* Generated. Do not edit. See above. \*/

[ 1434](group__timeutil__unit__apis.md#ga5c2a1ae6f66fcf22971c40301e78be8a)#define k\_ticks\_to\_ns\_floor32(t) \

1435 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, false)

1436

1437

1448/\* Generated. Do not edit. See above. \*/

[ 1449](group__timeutil__unit__apis.md#ga8c8c4d713c5716e5b0d41b014b394edf)#define k\_ticks\_to\_ns\_floor64(t) \

1450 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, false)

1451

1452

1463/\* Generated. Do not edit. See above. \*/

[ 1464](group__timeutil__unit__apis.md#ga26c20d96c08dc26d4664f3d66507e0bb)#define k\_ticks\_to\_ns\_near32(t) \

1465 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, true)

1466

1467

1478/\* Generated. Do not edit. See above. \*/

[ 1479](group__timeutil__unit__apis.md#ga3b0a2f92a3d61be64d4b80101129bc83)#define k\_ticks\_to\_ns\_near64(t) \

1480 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, true)

1481

1482

1493/\* Generated. Do not edit. See above. \*/

[ 1494](group__timeutil__unit__apis.md#gae28b7099ffbda7617f4049cd730921f8)#define k\_ticks\_to\_ns\_ceil32(t) \

1495 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, true, false)

1496

1497

1508/\* Generated. Do not edit. See above. \*/

[ 1509](group__timeutil__unit__apis.md#ga0221878e17c689e7f40940a201c4fdd7)#define k\_ticks\_to\_ns\_ceil64(t) \

1510 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, true, false)

1511

1512

1523/\* Generated. Do not edit. See above. \*/

[ 1524](group__timeutil__unit__apis.md#ga629a18a817e4b0240dc6bc9018d8809a)#define k\_ticks\_to\_cyc\_floor32(t) \

1525 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, false)

1526

1527

1538/\* Generated. Do not edit. See above. \*/

[ 1539](group__timeutil__unit__apis.md#ga5593c0751ec707a63ce25aed1567b2de)#define k\_ticks\_to\_cyc\_floor64(t) \

1540 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, false)

1541

1542

1553/\* Generated. Do not edit. See above. \*/

[ 1554](group__timeutil__unit__apis.md#gaf8d7352f4d2325ddb3aec3111cc8e124)#define k\_ticks\_to\_cyc\_near32(t) \

1555 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, true)

1556

1557

1568/\* Generated. Do not edit. See above. \*/

[ 1569](group__timeutil__unit__apis.md#ga7eed234908b9db5236de6c7543f40da1)#define k\_ticks\_to\_cyc\_near64(t) \

1570 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, true)

1571

1572

1583/\* Generated. Do not edit. See above. \*/

[ 1584](group__timeutil__unit__apis.md#ga00f31f894f66dde999714fe0cbab2178)#define k\_ticks\_to\_cyc\_ceil32(t) \

1585 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, true, false)

1586

1587

1598/\* Generated. Do not edit. See above. \*/

[ 1599](group__timeutil__unit__apis.md#ga4fa97b6aa81457142fc82cc73ef6c7a5)#define k\_ticks\_to\_cyc\_ceil64(t) \

1600 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, true, false)

1601

1602#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

1603#include <syscalls/time\_units.h>

1604#endif

1605

1606#undef TIME\_CONSTEXPR

1607

1611

1612#ifdef \_\_cplusplus

1613} /\* extern "C" \*/

1614#endif

1615

1616#endif /\* ZEPHYR\_INCLUDE\_TIME\_UNITS\_H\_ \*/

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [time\_units.h](time__units_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
