---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/cbprintf__cxx_8h_source.html
original_path: doxygen/html/cbprintf__cxx_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cbprintf\_cxx.h

[Go to the documentation of this file.](cbprintf__cxx_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_CXX\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_CXX\_H\_

9#ifdef \_\_cplusplus

10

11/\* C++ version for detecting a pointer to a string. \*/

12static inline int z\_cbprintf\_cxx\_is\_pchar(char \*, bool const\_as\_fixed)

13{

14 ARG\_UNUSED(const\_as\_fixed);

15 return 1;

16}

17

18static inline int z\_cbprintf\_cxx\_is\_pchar(const char \*, bool const\_as\_fixed)

19{

20 return const\_as\_fixed ? 0 : 1;

21}

22

23static inline int z\_cbprintf\_cxx\_is\_pchar(volatile char \*, bool const\_as\_fixed)

24{

25 ARG\_UNUSED(const\_as\_fixed);

26 return 1;

27}

28

29static inline int z\_cbprintf\_cxx\_is\_pchar(const volatile char \*, bool const\_as\_fixed)

30{

31 ARG\_UNUSED(const\_as\_fixed);

32 return 1;

33}

34

35static inline int z\_cbprintf\_cxx\_is\_pchar(unsigned char \*, bool const\_as\_fixed)

36{

37 ARG\_UNUSED(const\_as\_fixed);

38 return 1;

39}

40

41static inline int z\_cbprintf\_cxx\_is\_pchar(const unsigned char \*, bool const\_as\_fixed)

42{

43 return const\_as\_fixed ? 0 : 1;

44}

45

46static inline int z\_cbprintf\_cxx\_is\_pchar(volatile unsigned char \*, bool const\_as\_fixed)

47{

48 ARG\_UNUSED(const\_as\_fixed);

49 return 1;

50}

51

52static inline int z\_cbprintf\_cxx\_is\_pchar(const volatile unsigned char \*, bool const\_as\_fixed)

53{

54 ARG\_UNUSED(const\_as\_fixed);

55 return 1;

56}

57static inline int z\_cbprintf\_cxx\_is\_pchar(wchar\_t \*, bool const\_as\_fixed)

58{

59 ARG\_UNUSED(const\_as\_fixed);

60 return 1;

61}

62

63static inline int z\_cbprintf\_cxx\_is\_pchar(const wchar\_t \*, bool const\_as\_fixed)

64{

65 return const\_as\_fixed ? 0 : 1;

66}

67

68static inline int z\_cbprintf\_cxx\_is\_pchar(volatile wchar\_t \*, bool const\_as\_fixed)

69{

70 ARG\_UNUSED(const\_as\_fixed);

71 return 1;

72}

73

74static inline int z\_cbprintf\_cxx\_is\_pchar(const volatile wchar\_t \*, bool const\_as\_fixed)

75{

76 ARG\_UNUSED(const\_as\_fixed);

77 return 1;

78}

79

80template < typename T >

81static inline int z\_cbprintf\_cxx\_is\_pchar(T arg, bool const\_as\_fixed)

82{

83 ARG\_UNUSED(arg);

84 [TOOLCHAIN\_DISABLE\_GCC\_WARNING](toolchain_8h.md#a245aa1544cf704ac88da3904e0982f05)([TOOLCHAIN\_WARNING\_POINTER\_ARITH](toolchain_8h.md#a9c83552055a1817801dedc6655fc0cbf));

85 ARG\_UNUSED(const\_as\_fixed);

86 return 0;

87 [TOOLCHAIN\_ENABLE\_GCC\_WARNING](toolchain_8h.md#a57a000da2786521299f7bc9460977c60)([TOOLCHAIN\_WARNING\_POINTER\_ARITH](toolchain_8h.md#a9c83552055a1817801dedc6655fc0cbf));

88}

89

90/\* C++ version for determining if variable type is numeric and fits in 32 bit word. \*/

91static inline int z\_cbprintf\_cxx\_is\_word\_num(char)

92{

93 return 1;

94}

95

96static inline int z\_cbprintf\_cxx\_is\_word\_num(unsigned char)

97{

98 return 1;

99}

100

101static inline int z\_cbprintf\_cxx\_is\_word\_num(short)

102{

103 return 1;

104}

105

106static inline int z\_cbprintf\_cxx\_is\_word\_num(unsigned short)

107{

108 return 1;

109}

110

111static inline int z\_cbprintf\_cxx\_is\_word\_num(int)

112{

113 return 1;

114}

115

116static inline int z\_cbprintf\_cxx\_is\_word\_num(unsigned int)

117{

118 return 1;

119}

120

121static inline int z\_cbprintf\_cxx\_is\_word\_num(long)

122{

123 return (sizeof(long) <= sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) ? 1 : 0;

124}

125

126static inline int z\_cbprintf\_cxx\_is\_word\_num(unsigned long)

127{

128 return (sizeof(long) <= sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) ? 1 : 0;

129}

130

131template < typename T >

132static inline int z\_cbprintf\_cxx\_is\_word\_num(T arg)

133{

134 ARG\_UNUSED(arg);

135 [TOOLCHAIN\_DISABLE\_GCC\_WARNING](toolchain_8h.md#a245aa1544cf704ac88da3904e0982f05)([TOOLCHAIN\_WARNING\_POINTER\_ARITH](toolchain_8h.md#a9c83552055a1817801dedc6655fc0cbf));

136 return 0;

137 [TOOLCHAIN\_ENABLE\_GCC\_WARNING](toolchain_8h.md#a57a000da2786521299f7bc9460977c60)([TOOLCHAIN\_WARNING\_POINTER\_ARITH](toolchain_8h.md#a9c83552055a1817801dedc6655fc0cbf));

138}

139

140/\* C++ version for determining if argument is a none character pointer. \*/

141static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(char)

142{

143 return 0;

144}

145

146static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned char)

147{

148 return 0;

149}

150

151static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(short)

152{

153 return 0;

154}

155

156static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned short)

157{

158 return 0;

159}

160

161static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(int)

162{

163 return 0;

164}

165

166static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned int)

167{

168 return 0;

169}

170

171static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(long)

172{

173 return 0;

174}

175

176static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned long)

177{

178 return 0;

179}

180

181static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(long long)

182{

183 return 0;

184}

185

186static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned long long)

187{

188 return 0;

189}

190

191static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(float)

192{

193 return 0;

194}

195

196static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(double)

197{

198 return 0;

199}

200

201static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(char \*)

202{

203 return 0;

204}

205

206static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(volatile char \*)

207{

208 return 0;

209}

210

211static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(const char \*)

212{

213 return 0;

214}

215

216static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(const volatile char \*)

217{

218 return 0;

219}

220

221static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned char \*)

222{

223 return 0;

224}

225

226static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(volatile unsigned char \*)

227{

228 return 0;

229}

230

231static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(const unsigned char \*)

232{

233 return 0;

234}

235

236static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(const volatile unsigned char \*)

237{

238 return 0;

239}

240

241template < typename T >

242static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(T arg)

243{

244 ARG\_UNUSED(arg);

245

246 return 1;

247}

248

249/\* C++ version for calculating argument size. \*/

250static inline size\_t z\_cbprintf\_cxx\_arg\_size(float f)

251{

252 ARG\_UNUSED(f);

253

254 return sizeof(double);

255}

256

257template < typename T >

258static inline size\_t z\_cbprintf\_cxx\_arg\_size(T arg)

259{

260 ARG\_UNUSED(arg);

261

262 return [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(sizeof(T), sizeof(int));

263}

264

265/\* C++ version for storing arguments. \*/

266static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, float arg)

267{

268 double [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) = (double)arg;

269 void \*p = &[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417);

270

271 z\_cbprintf\_wcpy((int \*)dst, (int \*)p, sizeof([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) / sizeof(int));

272}

273

274static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, void \*p)

275{

276 z\_cbprintf\_wcpy((int \*)dst, (int \*)&p, sizeof(p) / sizeof(int));

277}

278

279static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, char arg)

280{

281 int tmp = arg + 0;

282

283 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

284}

285

286static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, unsigned char arg)

287{

288 int tmp = arg + 0;

289

290 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

291}

292

293static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, signed char arg)

294{

295 int tmp = arg + 0;

296

297 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

298}

299

300static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, short arg)

301{

302 int tmp = arg + 0;

303

304 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

305}

306

307static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, unsigned short arg)

308{

309 int tmp = arg + 0;

310

311 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

312}

313

314template < typename T >

315static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, T arg)

316{

317 size\_t wlen = z\_cbprintf\_cxx\_arg\_size(arg) / sizeof(int);

318 void \*p = &arg;

319

320 z\_cbprintf\_wcpy((int \*)dst, (int \*)p, wlen);

321}

322

323/\* C++ version for long double detection. \*/

324static inline int z\_cbprintf\_cxx\_is\_longdouble(long double arg)

325{

326 ARG\_UNUSED(arg);

327 return 1;

328}

329

330template < typename T >

331static inline int z\_cbprintf\_cxx\_is\_longdouble(T arg)

332{

333 ARG\_UNUSED(arg);

334

335 return 0;

336}

337

338/\* C++ version for calculating argument alignment. \*/

339static inline size\_t z\_cbprintf\_cxx\_alignment(float arg)

340{

341 ARG\_UNUSED(arg);

342

343 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(double);

344}

345

346static inline size\_t z\_cbprintf\_cxx\_alignment(double arg)

347{

348 ARG\_UNUSED(arg);

349

350 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(double);

351}

352

353static inline size\_t z\_cbprintf\_cxx\_alignment(long double arg)

354{

355 ARG\_UNUSED(arg);

356

357 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(long double);

358}

359

360static inline size\_t z\_cbprintf\_cxx\_alignment(long long arg)

361{

362 ARG\_UNUSED(arg);

363

364 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(long long);

365}

366

367static inline size\_t z\_cbprintf\_cxx\_alignment(unsigned long long arg)

368{

369 ARG\_UNUSED(arg);

370

371 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(long long);

372}

373

374template < typename T >

375static inline size\_t z\_cbprintf\_cxx\_alignment(T arg)

376{

377 return [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(\_\_alignof\_\_(arg), [VA\_STACK\_MIN\_ALIGN](cbprintf__internal_8h.md#a0ec36f3c06add6c091c8f552ef3736e1));

378}

379

380/\* C++ version for checking if two arguments are same type \*/

381template < typename T1, typename T2 >

382struct z\_cbprintf\_cxx\_is\_same\_type {

383 enum {

384 value = false

385 };

386};

387

388template < typename T >

389struct z\_cbprintf\_cxx\_is\_same\_type < T, T > {

390 enum {

391 value = true

392 };

393};

394

395template < typename T >

396struct z\_cbprintf\_cxx\_remove\_reference {

397 typedef T type;

398};

399

400template < typename T >

401struct z\_cbprintf\_cxx\_remove\_reference < T & > {

402 typedef T type;

403};

404

405#if \_\_cplusplus >= 201103L

406template < typename T >

407struct z\_cbprintf\_cxx\_remove\_reference < T && > {

408 typedef T type;

409};

410#endif

411

412template < typename T >

413struct z\_cbprintf\_cxx\_remove\_cv {

414 typedef T type;

415};

416

417template < typename T >

418struct z\_cbprintf\_cxx\_remove\_cv < const T > {

419 typedef T type;

420};

421

422template < typename T >

423struct z\_cbprintf\_cxx\_remove\_cv < volatile T > {

424 typedef T type;

425};

426

427template < typename T >

428struct z\_cbprintf\_cxx\_remove\_cv < const volatile T > {

429 typedef T type;

430};

431

432/\* Determine if a type is an array \*/

433template < typename T >

434struct z\_cbprintf\_cxx\_is\_array {

435 enum {

436 value = false

437 };

438};

439

440template < typename T >

441struct z\_cbprintf\_cxx\_is\_array < T[] > {

442 enum {

443 value = true

444 };

445};

446

447template < typename T, size\_t N >

448struct z\_cbprintf\_cxx\_is\_array < T[N] > {

449 enum {

450 value = true

451 };

452};

453

454/\* Determine the type of elements in an array \*/

455template < typename T >

456struct z\_cbprintf\_cxx\_remove\_extent {

457 typedef T type;

458};

459

460template < typename T >

461struct z\_cbprintf\_cxx\_remove\_extent < T[] > {

462 typedef T type;

463};

464

465template < typename T, size\_t N >

466struct z\_cbprintf\_cxx\_remove\_extent < T[N] > {

467 typedef T type;

468};

469

470#endif /\* \_\_cplusplus \*/

471#endif /\* ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_CXX\_H\_ \*/

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[VA\_STACK\_MIN\_ALIGN](cbprintf__internal_8h.md#a0ec36f3c06add6c091c8f552ef3736e1)

#define VA\_STACK\_MIN\_ALIGN

**Definition** cbprintf\_internal.h:48

[VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)

#define VA\_STACK\_ALIGN(type)

**Definition** cbprintf\_internal.h:52

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

#define MAX(a, b)

Obtain the maximum of two values.

**Definition** util.h:387

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[TOOLCHAIN\_DISABLE\_GCC\_WARNING](toolchain_8h.md#a245aa1544cf704ac88da3904e0982f05)

#define TOOLCHAIN\_DISABLE\_GCC\_WARNING(warning)

Disable the specified compiler warning for gcc.

**Definition** toolchain.h:290

[TOOLCHAIN\_ENABLE\_GCC\_WARNING](toolchain_8h.md#a57a000da2786521299f7bc9460977c60)

#define TOOLCHAIN\_ENABLE\_GCC\_WARNING(warning)

Re-enable the specified compiler warning for gcc.

**Definition** toolchain.h:300

[TOOLCHAIN\_WARNING\_POINTER\_ARITH](toolchain_8h.md#a9c83552055a1817801dedc6655fc0cbf)

#define TOOLCHAIN\_WARNING\_POINTER\_ARITH

Toolchain-specific warning for pointer arithmetic.

**Definition** toolchain.h:213

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [cbprintf\_cxx.h](cbprintf__cxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
