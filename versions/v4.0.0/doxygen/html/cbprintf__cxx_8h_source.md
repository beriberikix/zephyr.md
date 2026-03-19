---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cbprintf__cxx_8h_source.html
original_path: doxygen/html/cbprintf__cxx_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

84 \_Pragma("GCC diagnostic push")

85 \_Pragma("GCC diagnostic ignored \"-Wpointer-arith\"")

86 ARG\_UNUSED(const\_as\_fixed);

87 return 0;

88 \_Pragma("GCC diagnostic pop")

89}

90

91/\* C++ version for determining if variable type is numeric and fits in 32 bit word. \*/

92static inline int z\_cbprintf\_cxx\_is\_word\_num(char)

93{

94 return 1;

95}

96

97static inline int z\_cbprintf\_cxx\_is\_word\_num(unsigned char)

98{

99 return 1;

100}

101

102static inline int z\_cbprintf\_cxx\_is\_word\_num(short)

103{

104 return 1;

105}

106

107static inline int z\_cbprintf\_cxx\_is\_word\_num(unsigned short)

108{

109 return 1;

110}

111

112static inline int z\_cbprintf\_cxx\_is\_word\_num(int)

113{

114 return 1;

115}

116

117static inline int z\_cbprintf\_cxx\_is\_word\_num(unsigned int)

118{

119 return 1;

120}

121

122static inline int z\_cbprintf\_cxx\_is\_word\_num(long)

123{

124 return (sizeof(long) <= sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) ? 1 : 0;

125}

126

127static inline int z\_cbprintf\_cxx\_is\_word\_num(unsigned long)

128{

129 return (sizeof(long) <= sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) ? 1 : 0;

130}

131

132template < typename T >

133static inline int z\_cbprintf\_cxx\_is\_word\_num(T arg)

134{

135 ARG\_UNUSED(arg);

136 \_Pragma("GCC diagnostic push")

137 \_Pragma("GCC diagnostic ignored \"-Wpointer-arith\"")

138 return 0;

139 \_Pragma("GCC diagnostic pop")

140}

141

142/\* C++ version for determining if argument is a none character pointer. \*/

143static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(char)

144{

145 return 0;

146}

147

148static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned char)

149{

150 return 0;

151}

152

153static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(short)

154{

155 return 0;

156}

157

158static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned short)

159{

160 return 0;

161}

162

163static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(int)

164{

165 return 0;

166}

167

168static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned int)

169{

170 return 0;

171}

172

173static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(long)

174{

175 return 0;

176}

177

178static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned long)

179{

180 return 0;

181}

182

183static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(long long)

184{

185 return 0;

186}

187

188static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned long long)

189{

190 return 0;

191}

192

193static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(float)

194{

195 return 0;

196}

197

198static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(double)

199{

200 return 0;

201}

202

203static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(char \*)

204{

205 return 0;

206}

207

208static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(volatile char \*)

209{

210 return 0;

211}

212

213static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(const char \*)

214{

215 return 0;

216}

217

218static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(const volatile char \*)

219{

220 return 0;

221}

222

223static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(unsigned char \*)

224{

225 return 0;

226}

227

228static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(volatile unsigned char \*)

229{

230 return 0;

231}

232

233static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(const unsigned char \*)

234{

235 return 0;

236}

237

238static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(const volatile unsigned char \*)

239{

240 return 0;

241}

242

243template < typename T >

244static inline int z\_cbprintf\_cxx\_is\_none\_char\_ptr(T arg)

245{

246 ARG\_UNUSED(arg);

247

248 return 1;

249}

250

251/\* C++ version for calculating argument size. \*/

252static inline size\_t z\_cbprintf\_cxx\_arg\_size(float f)

253{

254 ARG\_UNUSED(f);

255

256 return sizeof(double);

257}

258

259template < typename T >

260static inline size\_t z\_cbprintf\_cxx\_arg\_size(T arg)

261{

262 ARG\_UNUSED(arg);

263

264 return [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(sizeof(T), sizeof(int));

265}

266

267/\* C++ version for storing arguments. \*/

268static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, float arg)

269{

270 double [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) = (double)arg;

271 void \*p = &[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417);

272

273 z\_cbprintf\_wcpy((int \*)dst, (int \*)p, sizeof([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) / sizeof(int));

274}

275

276static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, void \*p)

277{

278 z\_cbprintf\_wcpy((int \*)dst, (int \*)&p, sizeof(p) / sizeof(int));

279}

280

281static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, char arg)

282{

283 int tmp = arg + 0;

284

285 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

286}

287

288static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, unsigned char arg)

289{

290 int tmp = arg + 0;

291

292 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

293}

294

295static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, signed char arg)

296{

297 int tmp = arg + 0;

298

299 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

300}

301

302static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, short arg)

303{

304 int tmp = arg + 0;

305

306 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

307}

308

309static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, unsigned short arg)

310{

311 int tmp = arg + 0;

312

313 z\_cbprintf\_wcpy((int \*)dst, &tmp, 1);

314}

315

316template < typename T >

317static inline void z\_cbprintf\_cxx\_store\_arg([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, T arg)

318{

319 size\_t wlen = z\_cbprintf\_cxx\_arg\_size(arg) / sizeof(int);

320 void \*p = &arg;

321

322 z\_cbprintf\_wcpy((int \*)dst, (int \*)p, wlen);

323}

324

325/\* C++ version for long double detection. \*/

326static inline int z\_cbprintf\_cxx\_is\_longdouble(long double arg)

327{

328 ARG\_UNUSED(arg);

329 return 1;

330}

331

332template < typename T >

333static inline int z\_cbprintf\_cxx\_is\_longdouble(T arg)

334{

335 ARG\_UNUSED(arg);

336

337 return 0;

338}

339

340/\* C++ version for calculating argument alignment. \*/

341static inline size\_t z\_cbprintf\_cxx\_alignment(float arg)

342{

343 ARG\_UNUSED(arg);

344

345 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(double);

346}

347

348static inline size\_t z\_cbprintf\_cxx\_alignment(double arg)

349{

350 ARG\_UNUSED(arg);

351

352 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(double);

353}

354

355static inline size\_t z\_cbprintf\_cxx\_alignment(long double arg)

356{

357 ARG\_UNUSED(arg);

358

359 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(long double);

360}

361

362static inline size\_t z\_cbprintf\_cxx\_alignment(long long arg)

363{

364 ARG\_UNUSED(arg);

365

366 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(long long);

367}

368

369static inline size\_t z\_cbprintf\_cxx\_alignment(unsigned long long arg)

370{

371 ARG\_UNUSED(arg);

372

373 return [VA\_STACK\_ALIGN](cbprintf__internal_8h.md#acfc4e20989d254f61e85b8e2e5e6701a)(long long);

374}

375

376template < typename T >

377static inline size\_t z\_cbprintf\_cxx\_alignment(T arg)

378{

379 return [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(\_\_alignof\_\_(arg), [VA\_STACK\_MIN\_ALIGN](cbprintf__internal_8h.md#a0ec36f3c06add6c091c8f552ef3736e1));

380}

381

382/\* C++ version for checking if two arguments are same type \*/

383template < typename T1, typename T2 >

384struct z\_cbprintf\_cxx\_is\_same\_type {

385 enum {

386 value = false

387 };

388};

389

390template < typename T >

391struct z\_cbprintf\_cxx\_is\_same\_type < T, T > {

392 enum {

393 value = true

394 };

395};

396

397template < typename T >

398struct z\_cbprintf\_cxx\_remove\_reference {

399 typedef T type;

400};

401

402template < typename T >

403struct z\_cbprintf\_cxx\_remove\_reference < T & > {

404 typedef T type;

405};

406

407#if \_\_cplusplus >= 201103L

408template < typename T >

409struct z\_cbprintf\_cxx\_remove\_reference < T && > {

410 typedef T type;

411};

412#endif

413

414template < typename T >

415struct z\_cbprintf\_cxx\_remove\_cv {

416 typedef T type;

417};

418

419template < typename T >

420struct z\_cbprintf\_cxx\_remove\_cv < const T > {

421 typedef T type;

422};

423

424template < typename T >

425struct z\_cbprintf\_cxx\_remove\_cv < volatile T > {

426 typedef T type;

427};

428

429template < typename T >

430struct z\_cbprintf\_cxx\_remove\_cv < const volatile T > {

431 typedef T type;

432};

433

434/\* Determine if a type is an array \*/

435template < typename T >

436struct z\_cbprintf\_cxx\_is\_array {

437 enum {

438 value = false

439 };

440};

441

442template < typename T >

443struct z\_cbprintf\_cxx\_is\_array < T[] > {

444 enum {

445 value = true

446 };

447};

448

449template < typename T, size\_t N >

450struct z\_cbprintf\_cxx\_is\_array < T[N] > {

451 enum {

452 value = true

453 };

454};

455

456/\* Determine the type of elements in an array \*/

457template < typename T >

458struct z\_cbprintf\_cxx\_remove\_extent {

459 typedef T type;

460};

461

462template < typename T >

463struct z\_cbprintf\_cxx\_remove\_extent < T[] > {

464 typedef T type;

465};

466

467template < typename T, size\_t N >

468struct z\_cbprintf\_cxx\_remove\_extent < T[N] > {

469 typedef T type;

470};

471

472#endif /\* \_\_cplusplus \*/

473#endif /\* ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_CXX\_H\_ \*/

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

**Definition** util.h:385

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [cbprintf\_cxx.h](cbprintf__cxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
