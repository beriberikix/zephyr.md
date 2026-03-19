---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/time__units_8h_source.html
original_path: doxygen/html/time__units_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

59#if defined(\_\_cplusplus) && (\_\_cplusplus >= 201402L)

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

198/\* Integer multiplication 64-bit conversion \*/

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

275 \* my %human = ("sec" => "seconds",

276 \* "ms" => "milliseconds",

277 \* "us" => "microseconds",

278 \* "ns" => "nanoseconds",

279 \* "cyc" => "hardware cycles",

280 \* "ticks" => "ticks");

281 \* my %human\_round = ("ceil" => "Rounds up",

282 \* "near" => "Round nearest",

283 \* "floor" => "Truncates");

284 \*

285 \* sub big { return $\_[0] eq "us" || $\_[0] eq "ns"; }

286 \* sub prefix { return $\_[0] eq "sec" || $\_[0] eq "ms" || $\_[0] eq "us" || $\_[0] eq "ns"; }

287 \*

288 \* for my $from\_unit ("sec", "ms", "us", "ns", "cyc", "ticks") {

289 \* for my $to\_unit ("sec", "ms", "us", "ns", "cyc", "ticks") {

290 \* next if $from\_unit eq $to\_unit;

291 \* next if prefix($from\_unit) && prefix($to\_unit);

292 \* for my $round ("floor", "near", "ceil") {

293 \* for(my $big=0; $big <= 1; $big++) {

294 \* my $sz = $big ? 64 : 32;

295 \* my $sym = "k\_${from\_unit}\_to\_${to\_unit}\_$round$sz";

296 \* my $type = "uint${sz}\_t";

297 \* my $const\_hz = ($from\_unit eq "cyc" || $to\_unit eq "cyc")

298 \* ? "Z\_CCYC" : "true";

299 \* my $ret32 = $big ? "64" : "32";

300 \* my $rup = $round eq "ceil" ? "true" : "false";

301 \* my $roff = $round eq "near" ? "true" : "false";

302 \*

303 \* my $hfrom = $human{$from\_unit};

304 \* my $hto = $human{$to\_unit};

305 \* my $hround = $human\_round{$round};

306 \* print "/", "\*\* \@brief Convert $hfrom to $hto. $ret32 bits. $hround.\n";

307 \* print " \*\n";

308 \* print " \* Converts time values in $hfrom to $hto.\n";

309 \* print " \* Computes result in $sz bit precision.\n";

310 \* if ($round eq "ceil") {

311 \* print " \* Rounds up to the next highest output unit.\n";

312 \* } elsif ($round eq "near") {

313 \* print " \* Rounds to the nearest output unit.\n";

314 \* } else {

315 \* print " \* Truncates to the next lowest output unit.\n";

316 \* }

317 \* print " \*\n";

318 \* print " \* \@warning Generated. Do not edit. See above.\n";

319 \* print " \*\n";

320 \* print " \* \@param t Source time in $hfrom. uint64\_t\n";

321 \* print " \*\n";

322 \* print " \* \@return The converted time value in $hto. $type\n";

323 \* print " \*", "/\n";

324 \* print "#define $sym(t) \\\n";

325 \* print "\tz\_tmcvt\_$ret32(t, Z\_HZ\_$from\_unit, Z\_HZ\_$to\_unit,";

326 \* print " $const\_hz, $rup, $roff)\n";

327 \* print "\n\n";

328 \* }

329 \* }

330 \* }

331 \* }

332 \*/

333

334/\* Some more concise declarations to simplify the generator script and

335 \* save bytes below

336 \*/

337#define Z\_HZ\_sec 1

338#define Z\_HZ\_ms 1000

339#define Z\_HZ\_us 1000000

340#define Z\_HZ\_ns 1000000000

341#define Z\_HZ\_cyc sys\_clock\_hw\_cycles\_per\_sec()

342#define Z\_HZ\_ticks CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC

343#define Z\_CCYC (!IS\_ENABLED(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME))

344

[ 357](group__timeutil__unit__apis.md#ga38efeb3c71b28e98c6f18f63a2c59334)#define k\_sec\_to\_cyc\_floor32(t) \

358 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, false)

359

360

[ 373](group__timeutil__unit__apis.md#gaa9b2ed48e2b68d509a4eee305cdcd2fe)#define k\_sec\_to\_cyc\_floor64(t) \

374 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, false)

375

376

[ 389](group__timeutil__unit__apis.md#ga5a6ec23bd5644867f211eb5f47d81a3e)#define k\_sec\_to\_cyc\_near32(t) \

390 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, true)

391

392

[ 405](group__timeutil__unit__apis.md#gab1722b870ef8c9ed1084f104974c83a3)#define k\_sec\_to\_cyc\_near64(t) \

406 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, true)

407

408

[ 421](group__timeutil__unit__apis.md#ga197fe61819a3c51802f080187a39f2d5)#define k\_sec\_to\_cyc\_ceil32(t) \

422 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, true, false)

423

424

[ 437](group__timeutil__unit__apis.md#ga363ec5ce8d2365d25107e4c630222a9a)#define k\_sec\_to\_cyc\_ceil64(t) \

438 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, true, false)

439

440

[ 453](group__timeutil__unit__apis.md#gab6a57f08409edf9fba80837c3da34fb8)#define k\_sec\_to\_ticks\_floor32(t) \

454 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, false)

455

456

[ 469](group__timeutil__unit__apis.md#gafee9fc110890fba84640acac74af6717)#define k\_sec\_to\_ticks\_floor64(t) \

470 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, false)

471

472

[ 485](group__timeutil__unit__apis.md#ga4fbbf706ce9a69ab8b2b09bd3b0d4a3e)#define k\_sec\_to\_ticks\_near32(t) \

486 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, true)

487

488

[ 501](group__timeutil__unit__apis.md#gafbdfa2986e27ea95b0347319e8a23c68)#define k\_sec\_to\_ticks\_near64(t) \

502 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, true)

503

504

[ 517](group__timeutil__unit__apis.md#ga20d46aec38239513826d5d5259b5836c)#define k\_sec\_to\_ticks\_ceil32(t) \

518 z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, true, false)

519

520

[ 533](group__timeutil__unit__apis.md#gad382b2d98f84705c4c4e7a775bb549e8)#define k\_sec\_to\_ticks\_ceil64(t) \

534 z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, true, false)

535

536

[ 549](group__timeutil__unit__apis.md#ga2d60494645102034a7864ab0235bbfe4)#define k\_ms\_to\_cyc\_floor32(t) \

550 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, false)

551

552

[ 565](group__timeutil__unit__apis.md#ga4d3e1ec8eed229a08072aea744d40bba)#define k\_ms\_to\_cyc\_floor64(t) \

566 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, false)

567

568

[ 581](group__timeutil__unit__apis.md#ga8a0d31e998f1a19a3ee8200c173eb7c9)#define k\_ms\_to\_cyc\_near32(t) \

582 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, true)

583

584

[ 597](group__timeutil__unit__apis.md#gab2bcf34a4899619fcf083819a078a09e)#define k\_ms\_to\_cyc\_near64(t) \

598 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, true)

599

600

[ 613](group__timeutil__unit__apis.md#gab4636150867df2c4e918c12ec2e9bc5f)#define k\_ms\_to\_cyc\_ceil32(t) \

614 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, true, false)

615

616

[ 629](group__timeutil__unit__apis.md#ga82829fc9e99658faf91e5925c9545c9f)#define k\_ms\_to\_cyc\_ceil64(t) \

630 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, true, false)

631

632

[ 645](group__timeutil__unit__apis.md#gaf41d7ca19e5bb47824374698ce409ea1)#define k\_ms\_to\_ticks\_floor32(t) \

646 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, false)

647

648

[ 661](group__timeutil__unit__apis.md#gaa6ea6977308dfd2f092ba0ac4e779a31)#define k\_ms\_to\_ticks\_floor64(t) \

662 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, false)

663

664

[ 677](group__timeutil__unit__apis.md#ga0a61385f187c7c2a0f5288b17873b3db)#define k\_ms\_to\_ticks\_near32(t) \

678 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, true)

679

680

[ 693](group__timeutil__unit__apis.md#gab2f6dd223151224cd9fa0491f196c1f6)#define k\_ms\_to\_ticks\_near64(t) \

694 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, true)

695

696

[ 709](group__timeutil__unit__apis.md#gac74a319bcb69cc714818413ae15af7a2)#define k\_ms\_to\_ticks\_ceil32(t) \

710 z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, true, false)

711

712

[ 725](group__timeutil__unit__apis.md#gaa623d51d51b18a2e54b20d36d2f81c42)#define k\_ms\_to\_ticks\_ceil64(t) \

726 z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, true, false)

727

728

[ 741](group__timeutil__unit__apis.md#ga66c1ea8197e7adc01c837163e0aa4b62)#define k\_us\_to\_cyc\_floor32(t) \

742 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, false)

743

744

[ 757](group__timeutil__unit__apis.md#gac78731d5891b2389dc227608decf28dd)#define k\_us\_to\_cyc\_floor64(t) \

758 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, false)

759

760

[ 773](group__timeutil__unit__apis.md#ga01dabb87e1a4864e47fcd39cc4bce869)#define k\_us\_to\_cyc\_near32(t) \

774 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, true)

775

776

[ 789](group__timeutil__unit__apis.md#ga49a64e1f11cf450fdd770d67617cbe23)#define k\_us\_to\_cyc\_near64(t) \

790 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, true)

791

792

[ 805](group__timeutil__unit__apis.md#ga689a3f97643be5362c8c70c6d9d81051)#define k\_us\_to\_cyc\_ceil32(t) \

806 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, true, false)

807

808

[ 821](group__timeutil__unit__apis.md#ga2f65f04acc1daf019470beb04f16e276)#define k\_us\_to\_cyc\_ceil64(t) \

822 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, true, false)

823

824

[ 837](group__timeutil__unit__apis.md#ga96f32803affb56c366cbab5967c6b76c)#define k\_us\_to\_ticks\_floor32(t) \

838 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, false)

839

840

[ 853](group__timeutil__unit__apis.md#gaf6b4fb83131e5a52d9be875e5466d022)#define k\_us\_to\_ticks\_floor64(t) \

854 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, false)

855

856

[ 869](group__timeutil__unit__apis.md#ga5b0286cc82370178c852c3fa290eb61d)#define k\_us\_to\_ticks\_near32(t) \

870 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, true)

871

872

[ 885](group__timeutil__unit__apis.md#gaf2aae5316fcb5e99f4a77b99a5db27f9)#define k\_us\_to\_ticks\_near64(t) \

886 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, true)

887

888

[ 901](group__timeutil__unit__apis.md#ga950ac5ce654ec92e0af61e000de884a7)#define k\_us\_to\_ticks\_ceil32(t) \

902 z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, true, false)

903

904

[ 917](group__timeutil__unit__apis.md#ga1a977f93dc94ce9db54b3c9fdf9ba2f9)#define k\_us\_to\_ticks\_ceil64(t) \

918 z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, true, false)

919

920

[ 933](group__timeutil__unit__apis.md#ga46013e42990cfa561da06fb2bffaa261)#define k\_ns\_to\_cyc\_floor32(t) \

934 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, false)

935

936

[ 949](group__timeutil__unit__apis.md#gafc4ff458df5f4d1f221bcf0799d25335)#define k\_ns\_to\_cyc\_floor64(t) \

950 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, false)

951

952

[ 965](group__timeutil__unit__apis.md#gac8e586ebc94174ccdabf6f49dd0251e6)#define k\_ns\_to\_cyc\_near32(t) \

966 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, true)

967

968

[ 981](group__timeutil__unit__apis.md#gae6ec742a39a72b0a3dd7bc3da4a98403)#define k\_ns\_to\_cyc\_near64(t) \

982 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, true)

983

984

[ 997](group__timeutil__unit__apis.md#ga928ace6a14c0c2eb6aaa027f545601a7)#define k\_ns\_to\_cyc\_ceil32(t) \

998 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, true, false)

999

1000

[ 1013](group__timeutil__unit__apis.md#ga82264e42744defb8acf69caa8612e476)#define k\_ns\_to\_cyc\_ceil64(t) \

1014 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, true, false)

1015

1016

[ 1029](group__timeutil__unit__apis.md#ga4b0a61273dfbebd9273c0dc71ea74c65)#define k\_ns\_to\_ticks\_floor32(t) \

1030 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, false)

1031

1032

[ 1045](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)#define k\_ns\_to\_ticks\_floor64(t) \

1046 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, false)

1047

1048

[ 1061](group__timeutil__unit__apis.md#ga308b172f1fb6e1452c14db444ad7e75e)#define k\_ns\_to\_ticks\_near32(t) \

1062 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, true)

1063

1064

[ 1077](group__timeutil__unit__apis.md#ga50c08351970ea8e62a0509b68898901a)#define k\_ns\_to\_ticks\_near64(t) \

1078 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, true)

1079

1080

[ 1093](group__timeutil__unit__apis.md#gad958afbd9f86f94ccd5c9569e7587fad)#define k\_ns\_to\_ticks\_ceil32(t) \

1094 z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, true, false)

1095

1096

[ 1109](group__timeutil__unit__apis.md#ga1078f0f8764f7bad744cfb1ffd675c70)#define k\_ns\_to\_ticks\_ceil64(t) \

1110 z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, true, false)

1111

1112

[ 1125](group__timeutil__unit__apis.md#ga7a83cefe2d1e0828c6cdf949d4be9674)#define k\_cyc\_to\_sec\_floor32(t) \

1126 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, false)

1127

1128

[ 1141](group__timeutil__unit__apis.md#gadb48b4c005c8e4f1a30f018192fe4ae5)#define k\_cyc\_to\_sec\_floor64(t) \

1142 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, false)

1143

1144

[ 1157](group__timeutil__unit__apis.md#ga41d9d97ae4abc59eb235626682b767c9)#define k\_cyc\_to\_sec\_near32(t) \

1158 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, true)

1159

1160

[ 1173](group__timeutil__unit__apis.md#ga8dccd0c590fb4c2c399b0e0a120a5753)#define k\_cyc\_to\_sec\_near64(t) \

1174 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, true)

1175

1176

[ 1189](group__timeutil__unit__apis.md#gaeaf83a64009e2a834b0d65ead788e856)#define k\_cyc\_to\_sec\_ceil32(t) \

1190 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, true, false)

1191

1192

[ 1205](group__timeutil__unit__apis.md#ga2c64ffb238dd5047413d394b39900d61)#define k\_cyc\_to\_sec\_ceil64(t) \

1206 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, true, false)

1207

1208

[ 1221](group__timeutil__unit__apis.md#ga5f9f903e6e4eba5415cae3f337d565ed)#define k\_cyc\_to\_ms\_floor32(t) \

1222 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, false)

1223

1224

[ 1237](group__timeutil__unit__apis.md#gaeaa9339beec5b82b924302bbc57923f6)#define k\_cyc\_to\_ms\_floor64(t) \

1238 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, false)

1239

1240

[ 1253](group__timeutil__unit__apis.md#gaba2f18bc00740fb0411371d2d2f3d949)#define k\_cyc\_to\_ms\_near32(t) \

1254 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, true)

1255

1256

[ 1269](group__timeutil__unit__apis.md#ga217f0b8bf86a24654419c3ccfd6e7822)#define k\_cyc\_to\_ms\_near64(t) \

1270 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, true)

1271

1272

[ 1285](group__timeutil__unit__apis.md#ga40bf11b01ba76673c67569e8d1e55d92)#define k\_cyc\_to\_ms\_ceil32(t) \

1286 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, true, false)

1287

1288

[ 1301](group__timeutil__unit__apis.md#gaf85474dc07ce8165379415f4977aa44f)#define k\_cyc\_to\_ms\_ceil64(t) \

1302 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, true, false)

1303

1304

[ 1317](group__timeutil__unit__apis.md#ga86392f2bddfbb7c895c08becf9c8c485)#define k\_cyc\_to\_us\_floor32(t) \

1318 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, false)

1319

1320

[ 1333](group__timeutil__unit__apis.md#gad3376aa7ab36b6b7f5a1f9c9977cee4a)#define k\_cyc\_to\_us\_floor64(t) \

1334 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, false)

1335

1336

[ 1349](group__timeutil__unit__apis.md#ga1314249a8a404f00c8a03d6c77e0c752)#define k\_cyc\_to\_us\_near32(t) \

1350 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, true)

1351

1352

[ 1365](group__timeutil__unit__apis.md#ga869ccaf50e83712d0bafe0f8e238fc61)#define k\_cyc\_to\_us\_near64(t) \

1366 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, true)

1367

1368

[ 1381](group__timeutil__unit__apis.md#ga051fbec0b352b4fb3116544c8c33250a)#define k\_cyc\_to\_us\_ceil32(t) \

1382 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, true, false)

1383

1384

[ 1397](group__timeutil__unit__apis.md#ga90b09be4536f6877f67a60b3c33f5299)#define k\_cyc\_to\_us\_ceil64(t) \

1398 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, true, false)

1399

1400

[ 1413](group__timeutil__unit__apis.md#ga775c4d72bd0ecb9a6ad947f34c479754)#define k\_cyc\_to\_ns\_floor32(t) \

1414 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, false)

1415

1416

[ 1429](group__timeutil__unit__apis.md#ga665d5fc98ffe8bd1cf78ca994f58724a)#define k\_cyc\_to\_ns\_floor64(t) \

1430 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, false)

1431

1432

[ 1445](group__timeutil__unit__apis.md#gabd5378a62e480fc1b79b3326c8f02d5f)#define k\_cyc\_to\_ns\_near32(t) \

1446 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, true)

1447

1448

[ 1461](group__timeutil__unit__apis.md#gad36269d0d63bee37e09da46cfe516c8c)#define k\_cyc\_to\_ns\_near64(t) \

1462 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, true)

1463

1464

[ 1477](group__timeutil__unit__apis.md#ga19526c845440ed793068fa8d8d5088ff)#define k\_cyc\_to\_ns\_ceil32(t) \

1478 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, true, false)

1479

1480

[ 1493](group__timeutil__unit__apis.md#gab2889da75f359d248a6eb61fdc3d53c0)#define k\_cyc\_to\_ns\_ceil64(t) \

1494 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, true, false)

1495

1496

[ 1509](group__timeutil__unit__apis.md#ga2efd0e2611cbeb696778eb73cf24b7ee)#define k\_cyc\_to\_ticks\_floor32(t) \

1510 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, false)

1511

1512

[ 1525](group__timeutil__unit__apis.md#gaad0256d9429dfa5c5a194f1419691cfc)#define k\_cyc\_to\_ticks\_floor64(t) \

1526 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, false)

1527

1528

[ 1541](group__timeutil__unit__apis.md#ga4601ea99148307043d2d47a2e9fccb8e)#define k\_cyc\_to\_ticks\_near32(t) \

1542 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, true)

1543

1544

[ 1557](group__timeutil__unit__apis.md#gafa97757f07a5048d67d6eca4a72cf39c)#define k\_cyc\_to\_ticks\_near64(t) \

1558 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, true)

1559

1560

[ 1573](group__timeutil__unit__apis.md#gae7653e92b9b44accaa9ee2764237f595)#define k\_cyc\_to\_ticks\_ceil32(t) \

1574 z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, true, false)

1575

1576

[ 1589](group__timeutil__unit__apis.md#ga0fa410ff13d0cd467d160c1c14cf24a6)#define k\_cyc\_to\_ticks\_ceil64(t) \

1590 z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, true, false)

1591

1592

[ 1605](group__timeutil__unit__apis.md#ga824ffc9857fa2d4bccb3a9f4a56b8f18)#define k\_ticks\_to\_sec\_floor32(t) \

1606 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, false)

1607

1608

[ 1621](group__timeutil__unit__apis.md#ga6e9ef943c78cbb5963d8eece896b6189)#define k\_ticks\_to\_sec\_floor64(t) \

1622 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, false)

1623

1624

[ 1637](group__timeutil__unit__apis.md#ga15284161d40816f06b2bbf4cd03a0fed)#define k\_ticks\_to\_sec\_near32(t) \

1638 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, true)

1639

1640

[ 1653](group__timeutil__unit__apis.md#gab6b9b6d752ec3c8b69d9f27ca5f7b85e)#define k\_ticks\_to\_sec\_near64(t) \

1654 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, true)

1655

1656

[ 1669](group__timeutil__unit__apis.md#ga3986215ef060ab2ff9cc7c576eb05b01)#define k\_ticks\_to\_sec\_ceil32(t) \

1670 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, true, false)

1671

1672

[ 1685](group__timeutil__unit__apis.md#ga02493c454fbbbf6787b036ca7f739073)#define k\_ticks\_to\_sec\_ceil64(t) \

1686 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, true, false)

1687

1688

[ 1701](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)#define k\_ticks\_to\_ms\_floor32(t) \

1702 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, false)

1703

1704

[ 1717](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)#define k\_ticks\_to\_ms\_floor64(t) \

1718 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, false)

1719

1720

[ 1733](group__timeutil__unit__apis.md#ga8f1133f69f154d593fc127d2b00931c8)#define k\_ticks\_to\_ms\_near32(t) \

1734 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, true)

1735

1736

[ 1749](group__timeutil__unit__apis.md#gac3578501567233a7576c61cfd6cf28cb)#define k\_ticks\_to\_ms\_near64(t) \

1750 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, true)

1751

1752

[ 1765](group__timeutil__unit__apis.md#ga3f2c3cf86ef1d243b43f29958a108088)#define k\_ticks\_to\_ms\_ceil32(t) \

1766 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, true, false)

1767

1768

[ 1781](group__timeutil__unit__apis.md#gabee58122304820b36d601268eb4598e2)#define k\_ticks\_to\_ms\_ceil64(t) \

1782 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, true, false)

1783

1784

[ 1797](group__timeutil__unit__apis.md#ga86767fd65071fc7c57f25434386caeed)#define k\_ticks\_to\_us\_floor32(t) \

1798 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, false)

1799

1800

[ 1813](group__timeutil__unit__apis.md#ga27cac5d9974320ef12c6bcacdae8b47c)#define k\_ticks\_to\_us\_floor64(t) \

1814 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, false)

1815

1816

[ 1829](group__timeutil__unit__apis.md#ga328649dd1ec1fae9c69eb3a75709a9f2)#define k\_ticks\_to\_us\_near32(t) \

1830 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, true)

1831

1832

[ 1845](group__timeutil__unit__apis.md#ga5735cb347e01fa391368d2fb54d6d965)#define k\_ticks\_to\_us\_near64(t) \

1846 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, true)

1847

1848

[ 1861](group__timeutil__unit__apis.md#gadd968c2033d548c03072e46c895375bc)#define k\_ticks\_to\_us\_ceil32(t) \

1862 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, true, false)

1863

1864

[ 1877](group__timeutil__unit__apis.md#gad1c6d9e60835c6c00960778395cdbacc)#define k\_ticks\_to\_us\_ceil64(t) \

1878 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, true, false)

1879

1880

[ 1893](group__timeutil__unit__apis.md#ga5c2a1ae6f66fcf22971c40301e78be8a)#define k\_ticks\_to\_ns\_floor32(t) \

1894 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, false)

1895

1896

[ 1909](group__timeutil__unit__apis.md#ga8c8c4d713c5716e5b0d41b014b394edf)#define k\_ticks\_to\_ns\_floor64(t) \

1910 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, false)

1911

1912

[ 1925](group__timeutil__unit__apis.md#ga26c20d96c08dc26d4664f3d66507e0bb)#define k\_ticks\_to\_ns\_near32(t) \

1926 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, true)

1927

1928

[ 1941](group__timeutil__unit__apis.md#ga3b0a2f92a3d61be64d4b80101129bc83)#define k\_ticks\_to\_ns\_near64(t) \

1942 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, true)

1943

1944

[ 1957](group__timeutil__unit__apis.md#gae28b7099ffbda7617f4049cd730921f8)#define k\_ticks\_to\_ns\_ceil32(t) \

1958 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, true, false)

1959

1960

[ 1973](group__timeutil__unit__apis.md#ga0221878e17c689e7f40940a201c4fdd7)#define k\_ticks\_to\_ns\_ceil64(t) \

1974 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, true, false)

1975

1976

[ 1989](group__timeutil__unit__apis.md#ga629a18a817e4b0240dc6bc9018d8809a)#define k\_ticks\_to\_cyc\_floor32(t) \

1990 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, false)

1991

1992

[ 2005](group__timeutil__unit__apis.md#ga5593c0751ec707a63ce25aed1567b2de)#define k\_ticks\_to\_cyc\_floor64(t) \

2006 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, false)

2007

2008

[ 2021](group__timeutil__unit__apis.md#gaf8d7352f4d2325ddb3aec3111cc8e124)#define k\_ticks\_to\_cyc\_near32(t) \

2022 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, true)

2023

2024

[ 2037](group__timeutil__unit__apis.md#ga7eed234908b9db5236de6c7543f40da1)#define k\_ticks\_to\_cyc\_near64(t) \

2038 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, true)

2039

2040

[ 2053](group__timeutil__unit__apis.md#ga00f31f894f66dde999714fe0cbab2178)#define k\_ticks\_to\_cyc\_ceil32(t) \

2054 z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, true, false)

2055

2056

[ 2069](group__timeutil__unit__apis.md#ga4fa97b6aa81457142fc82cc73ef6c7a5)#define k\_ticks\_to\_cyc\_ceil64(t) \

2070 z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, true, false)

2071

2072#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME)

2073#include <zephyr/syscalls/time\_units.h>

2074#endif

2075

2076#undef TIME\_CONSTEXPR

2077

2081

2082#ifdef \_\_cplusplus

2083} /\* extern "C" \*/

2084#endif

2085

2086#endif /\* ZEPHYR\_INCLUDE\_TIME\_UNITS\_H\_ \*/

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [time\_units.h](time__units_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
