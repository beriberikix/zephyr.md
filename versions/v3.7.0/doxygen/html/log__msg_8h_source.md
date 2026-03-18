---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/log__msg_8h_source.html
original_path: doxygen/html/log__msg_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_msg.h

[Go to the documentation of this file.](log__msg_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_MSG\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_MSG\_H\_

8

9#include <[zephyr/logging/log\_instance.h](log__instance_8h.md)>

10#include <[zephyr/sys/mpsc\_packet.h](mpsc__packet_8h.md)>

11#include <[zephyr/sys/cbprintf.h](cbprintf_8h.md)>

12#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

13#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

14#include <[zephyr/sys/util.h](util_8h.md)>

15#include <[string.h](string_8h.md)>

16#include <[zephyr/toolchain.h](toolchain_8h.md)>

17

18#ifdef \_\_GNUC\_\_

19#ifndef alloca

20#define alloca \_\_builtin\_alloca

21#endif

22#else

23#include <alloca.h>

24#endif

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 30](log__msg_8h.md#aac56158f6f644d26a5aa11cfe67d6ed6)#define LOG\_MSG\_DEBUG 0

[ 31](log__msg_8h.md#ad5fae12ef133c7e7a2622c46dd22fb1c)#define LOG\_MSG\_DBG(...) IF\_ENABLED(LOG\_MSG\_DEBUG, (printk(\_\_VA\_ARGS\_\_)))

32

33#ifdef CONFIG\_LOG\_TIMESTAMP\_64BIT

34typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8);

35#else

[ 36](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8);

37#endif

38

45

46#define Z\_LOG\_MSG\_LOG 0

47

48#define Z\_LOG\_MSG\_PACKAGE\_BITS 11

49

50#define Z\_LOG\_MSG\_MAX\_PACKAGE BIT\_MASK(Z\_LOG\_MSG\_PACKAGE\_BITS)

51

[ 52](group__log__msg.md#gaba2b53ea6e29c20d452322d664ed4f18)#define LOG\_MSG\_GENERIC\_HDR \

53 MPSC\_PBUF\_HDR;\

54 uint32\_t type:1

55

[ 56](structlog__msg__desc.md)struct [log\_msg\_desc](structlog__msg__desc.md) {

[ 57](structlog__msg__desc.md#adf93cabaf90a5104ff1100cb727ee06c) [LOG\_MSG\_GENERIC\_HDR](group__log__msg.md#gaba2b53ea6e29c20d452322d664ed4f18);

[ 58](structlog__msg__desc.md#a2636fe29ddba79450689b90beff3c3c7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [domain](structlog__msg__desc.md#a2636fe29ddba79450689b90beff3c3c7):3;

[ 59](structlog__msg__desc.md#a8cc3ca0930b892a6a9b7b73d20f8628e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [level](structlog__msg__desc.md#a8cc3ca0930b892a6a9b7b73d20f8628e):3;

[ 60](structlog__msg__desc.md#a3b9fb3a9e612ec8642e5e595d6478ac3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [package\_len](structlog__msg__desc.md#a3b9fb3a9e612ec8642e5e595d6478ac3):Z\_LOG\_MSG\_PACKAGE\_BITS;

[ 61](structlog__msg__desc.md#aff700ad436ba87af141268e8f7aa5f6f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_len](structlog__msg__desc.md#aff700ad436ba87af141268e8f7aa5f6f):12;

62};

63

[ 64](unionlog__msg__source.md)union [log\_msg\_source](unionlog__msg__source.md) {

[ 65](unionlog__msg__source.md#a19ced11229bfe3c6d93c22828e8cb1c8) const struct [log\_source\_const\_data](structlog__source__const__data.md) \*[fixed](unionlog__msg__source.md#a19ced11229bfe3c6d93c22828e8cb1c8);

[ 66](unionlog__msg__source.md#a38427fdbef5b2d35ae2ad75a8db88d37) struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) \*[dynamic](unionlog__msg__source.md#a38427fdbef5b2d35ae2ad75a8db88d37);

[ 67](unionlog__msg__source.md#aceb87931abda0ca5b7f2532df99fcaf6) void \*[raw](unionlog__msg__source.md#aceb87931abda0ca5b7f2532df99fcaf6);

68};

69

[ 70](structlog__msg__hdr.md)struct [log\_msg\_hdr](structlog__msg__hdr.md) {

[ 71](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895) struct [log\_msg\_desc](structlog__msg__desc.md) [desc](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895);

72/\* Attempting to keep best alignment. When address is 64 bit and timestamp 32

73 \* swap the order to have 16 byte header instead of 24 byte.

74 \*/

75#if (INTPTR\_MAX > INT32\_MAX) && !defined(CONFIG\_LOG\_TIMESTAMP\_64BIT)

76 [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) [timestamp](structlog__msg__hdr.md#a48ba27c6897377fafda1a980422fb2f4);

77 const void \*[source](structlog__msg__hdr.md#aab20cd4267d37793299a2ed3a5e75236);

78#else

[ 79](structlog__msg__hdr.md#aab20cd4267d37793299a2ed3a5e75236) const void \*[source](structlog__msg__hdr.md#aab20cd4267d37793299a2ed3a5e75236);

[ 80](structlog__msg__hdr.md#a48ba27c6897377fafda1a980422fb2f4) [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) [timestamp](structlog__msg__hdr.md#a48ba27c6897377fafda1a980422fb2f4);

81#endif

82#if defined(CONFIG\_LOG\_THREAD\_ID\_PREFIX)

83 void \*tid;

84#endif

85};

86/\* Messages are aligned to alignment required by cbprintf package. \*/

87#define Z\_LOG\_MSG\_ALIGNMENT CBPRINTF\_PACKAGE\_ALIGNMENT

88

89#define Z\_LOG\_MSG\_PADDING \

90 ((sizeof(struct log\_msg\_hdr) % Z\_LOG\_MSG\_ALIGNMENT) > 0 ? \

91 (Z\_LOG\_MSG\_ALIGNMENT - (sizeof(struct log\_msg\_hdr) % Z\_LOG\_MSG\_ALIGNMENT)) : \

92 0)

93

[ 94](structlog__msg.md)struct [log\_msg](structlog__msg.md) {

[ 95](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a) struct [log\_msg\_hdr](structlog__msg__hdr.md) [hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a);

96 /\* Adding padding to ensure that cbprintf package that follows is

97 \* properly aligned.

98 \*/

[ 99](structlog__msg.md#a539123bce09e55516406cf2a25610e8d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [padding](structlog__msg.md#a539123bce09e55516406cf2a25610e8d)[Z\_LOG\_MSG\_PADDING];

[ 100](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e)[];

101};

102

106BUILD\_ASSERT(sizeof(struct [log\_msg](structlog__msg.md)) % Z\_LOG\_MSG\_ALIGNMENT == 0,

107 "Log msg size must aligned");

111

112

[ 113](structlog__msg__generic__hdr.md)struct [log\_msg\_generic\_hdr](structlog__msg__generic__hdr.md) {

[ 114](structlog__msg__generic__hdr.md#a258f97f0f0b9586d85febfee36101467) [LOG\_MSG\_GENERIC\_HDR](group__log__msg.md#gaba2b53ea6e29c20d452322d664ed4f18);

115};

116

[ 117](unionlog__msg__generic.md)union [log\_msg\_generic](unionlog__msg__generic.md) {

[ 118](unionlog__msg__generic.md#a74b4fa4fff98e914f8e7536fe0be568d) union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) [buf](unionlog__msg__generic.md#a74b4fa4fff98e914f8e7536fe0be568d);

[ 119](unionlog__msg__generic.md#ad1d622e11a94fb14cbb4bd13871751d5) struct [log\_msg\_generic\_hdr](structlog__msg__generic__hdr.md) [generic](unionlog__msg__generic.md#ad1d622e11a94fb14cbb4bd13871751d5);

[ 120](unionlog__msg__generic.md#a9a030d553e2104e674d2495b674aa158) struct [log\_msg](structlog__msg.md) [log](unionlog__msg__generic.md#a9a030d553e2104e674d2495b674aa158);

121};

122

127enum z\_log\_msg\_mode {

128 /\* Runtime mode is least efficient but supports all cases thus it is

129 \* treated as a fallback method when others cannot be used.

130 \*/

131 Z\_LOG\_MSG\_MODE\_RUNTIME,

132 /\* Mode creates statically a string package on stack and calls a

133 \* function for creating a message. It takes code size than

134 \* Z\_LOG\_MSG\_MODE\_ZERO\_COPY but is a bit slower.

135 \*/

136 Z\_LOG\_MSG\_MODE\_FROM\_STACK,

137

138 /\* Mode calculates size of the message and allocates it and writes

139 \* directly to the message space. It is the fastest method but requires

140 \* more code size.

141 \*/

142 Z\_LOG\_MSG\_MODE\_ZERO\_COPY,

143

144 /\* Mode optimized for simple messages with 0 to 2 32 bit word arguments.\*/

145 Z\_LOG\_MSG\_MODE\_SIMPLE,

146};

147

148#define Z\_LOG\_MSG\_DESC\_INITIALIZER(\_domain\_id, \_level, \_plen, \_dlen) \

149{ \

150 .valid = 0, \

151 .busy = 0, \

152 .type = Z\_LOG\_MSG\_LOG, \

153 .domain = (\_domain\_id), \

154 .level = (\_level), \

155 .package\_len = (\_plen), \

156 .data\_len = (\_dlen), \

157}

158

159#define Z\_LOG\_MSG\_CBPRINTF\_FLAGS(\_cstr\_cnt) \

160 (CBPRINTF\_PACKAGE\_FIRST\_RO\_STR\_CNT(\_cstr\_cnt) | \

161 (IS\_ENABLED(CONFIG\_LOG\_MSG\_APPEND\_RO\_STRING\_LOC) ? \

162 CBPRINTF\_PACKAGE\_ADD\_STRING\_IDXS : 0))

163

164#ifdef CONFIG\_LOG\_USE\_VLA

165#define Z\_LOG\_MSG\_ON\_STACK\_ALLOC(ptr, len) \

166 long long \_ll\_buf[DIV\_ROUND\_UP(len, sizeof(long long))]; \

167 long double \_ld\_buf[DIV\_ROUND\_UP(len, sizeof(long double))]; \

168 (ptr) = (sizeof(long double) == Z\_LOG\_MSG\_ALIGNMENT) ? \

169 (struct log\_msg \*)\_ld\_buf : (struct log\_msg \*)\_ll\_buf; \

170 if (IS\_ENABLED(CONFIG\_LOG\_TEST\_CLEAR\_MESSAGE\_SPACE)) { \

171 /\* During test fill with 0's to simplify message comparison \*/ \

172 memset((ptr), 0, (len)); \

173 }

174#else /\* Z\_LOG\_MSG\_USE\_VLA \*/

175/\* When VLA cannot be used we need to trick compiler a bit and create multiple

176 \* fixed size arrays and take the smallest one that will fit the message.

177 \* Compiler will remove unused arrays and stack usage will be kept similar

178 \* to vla case, rounded to the size of the used buffer.

179 \*/

180#define Z\_LOG\_MSG\_ON\_STACK\_ALLOC(ptr, len) \

181 long long \_ll\_buf32[32 / sizeof(long long)]; \

182 long long \_ll\_buf48[48 / sizeof(long long)]; \

183 long long \_ll\_buf64[64 / sizeof(long long)]; \

184 long long \_ll\_buf128[128 / sizeof(long long)]; \

185 long long \_ll\_buf256[256 / sizeof(long long)]; \

186 long double \_ld\_buf32[32 / sizeof(long double)]; \

187 long double \_ld\_buf48[48 / sizeof(long double)]; \

188 long double \_ld\_buf64[64 / sizeof(long double)]; \

189 long double \_ld\_buf128[128 / sizeof(long double)]; \

190 long double \_ld\_buf256[256 / sizeof(long double)]; \

191 if (sizeof(long double) == Z\_LOG\_MSG\_ALIGNMENT) { \

192 ptr = (len > 128) ? (struct log\_msg \*)\_ld\_buf256 : \

193 ((len > 64) ? (struct log\_msg \*)\_ld\_buf128 : \

194 ((len > 48) ? (struct log\_msg \*)\_ld\_buf64 : \

195 ((len > 32) ? (struct log\_msg \*)\_ld\_buf48 : \

196 (struct log\_msg \*)\_ld\_buf32)));\

197 } else { \

198 ptr = (len > 128) ? (struct log\_msg \*)\_ll\_buf256 : \

199 ((len > 64) ? (struct log\_msg \*)\_ll\_buf128 : \

200 ((len > 48) ? (struct log\_msg \*)\_ll\_buf64 : \

201 ((len > 32) ? (struct log\_msg \*)\_ll\_buf48 : \

202 (struct log\_msg \*)\_ll\_buf32)));\

203 } \

204 if (IS\_ENABLED(CONFIG\_LOG\_TEST\_CLEAR\_MESSAGE\_SPACE)) { \

205 /\* During test fill with 0's to simplify message comparison \*/ \

206 memset((ptr), 0, (len)); \

207 }

208#endif /\* Z\_LOG\_MSG\_USE\_VLA \*/

209

210#define Z\_LOG\_MSG\_ALIGN\_OFFSET \

211 offsetof(struct log\_msg, data)

212

213#define Z\_LOG\_MSG\_LEN(pkg\_len, data\_len) \

214 (offsetof(struct log\_msg, data) + (pkg\_len) + (data\_len))

215

216#define Z\_LOG\_MSG\_ALIGNED\_WLEN(pkg\_len, data\_len) \

217 DIV\_ROUND\_UP(ROUND\_UP(Z\_LOG\_MSG\_LEN(pkg\_len, data\_len), \

218 Z\_LOG\_MSG\_ALIGNMENT), \

219 sizeof(uint32\_t))

220

221/\*

222 \* With Zephyr SDK 0.14.2, aarch64-zephyr-elf-gcc (10.3.0) fails to ensure $sp

223 \* is below the active memory during message construction. As a result,

224 \* interrupts happening in the middle of that process can end up smashing active

225 \* data and causing a logging fault. Work around this by inserting a compiler

226 \* barrier after the allocation and before any use to make sure GCC moves the

227 \* stack pointer soon enough

228 \*/

229

230#define Z\_LOG\_ARM64\_VLA\_PROTECT() compiler\_barrier()

231

232#define \_LOG\_MSG\_SIMPLE\_XXXX0 1

233#define \_LOG\_MSG\_SIMPLE\_XXXX1 1

234#define \_LOG\_MSG\_SIMPLE\_XXXX2 1

235

236/\* Determine if amount of arguments (less than 3) qualifies to simple message. \*/

[ 237](group__log__msg.md#ga92c57ed7438185ade7d2aaf6fc13f218)#define LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK(...) \

238 COND\_CODE\_1(UTIL\_CAT(\_LOG\_MSG\_SIMPLE\_XXXX, NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_)), (1), (0))

239

240/\* Set of marcos used to determine if arguments type allows simplified message creation mode. \*/

[ 241](group__log__msg.md#ga930a906d0564298231f04d0290d7079f)#define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_0(fmt) 1

[ 242](group__log__msg.md#gaddf1c7085315ef0154d0d4d9fe04a742)#define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_1(fmt, arg) Z\_CBPRINTF\_IS\_WORD\_NUM(arg)

[ 243](group__log__msg.md#gaf416ebb73b5b66df011024b9284cec12)#define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_2(fmt, arg0, arg1) \

244 Z\_CBPRINTF\_IS\_WORD\_NUM(arg0) && Z\_CBPRINTF\_IS\_WORD\_NUM(arg1)

245

[ 250](group__log__msg.md#gafe4a2adbb6cf19bf4df58311ad6beac8)#define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK(...) \

251 UTIL\_CAT(LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_, NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_))(\_\_VA\_ARGS\_\_)

252

[ 265](group__log__msg.md#ga90e5d1e83ce78f638f35add7b98bf7ae)#define LOG\_MSG\_SIMPLE\_CHECK(...) \

266 COND\_CODE\_1(CONFIG\_64BIT, (0), (\

267 COND\_CODE\_1(LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK(\_\_VA\_ARGS\_\_), ( \

268 LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK(\_\_VA\_ARGS\_\_)), (0))))

269

270/\* Helper macro for handing log with one argument. Macro casts the first argument to uint32\_t. \*/

271#define Z\_LOG\_MSG\_SIMPLE\_CREATE\_1(\_source, \_level, ...) \

272 z\_log\_msg\_simple\_create\_1(\_source, \_level, GET\_ARG\_N(1, \_\_VA\_ARGS\_\_), \

273 (uint32\_t)(uintptr\_t)GET\_ARG\_N(2, \_\_VA\_ARGS\_\_))

274

275/\* Helper macro for handing log with two arguments. Macro casts arguments to uint32\_t.

276 \*/

277#define Z\_LOG\_MSG\_SIMPLE\_CREATE\_2(\_source, \_level, ...) \

278 z\_log\_msg\_simple\_create\_2(\_source, \_level, GET\_ARG\_N(1, \_\_VA\_ARGS\_\_), \

279 (uint32\_t)(uintptr\_t)GET\_ARG\_N(2, \_\_VA\_ARGS\_\_), \

280 (uint32\_t)(uintptr\_t)GET\_ARG\_N(3, \_\_VA\_ARGS\_\_))

281

282/\* Call specific function based on the number of arguments.

283 \* Since up 2 to arguments are supported COND\_CODE\_0 and COND\_CODE\_1 can be used to

284 \* handle all cases (0, 1 and 2 arguments). When tracing is enable then for each

285 \* function a macro is create. The difference between function and macro is that

286 \* macro is applied to any input arguments so we need to make sure that it is

287 \* always called with proper number of arguments. For that it is wrapped around

288 \* into another macro and dummy arguments to cover for cases when there is less

289 \* arguments in a log call.

290 \*/

291#define Z\_LOG\_MSG\_SIMPLE\_FUNC2(arg\_cnt, \_source, \_level, ...) \

292 COND\_CODE\_0(arg\_cnt, \

293 (z\_log\_msg\_simple\_create\_0(\_source, \_level, GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))), \

294 (COND\_CODE\_1(arg\_cnt, ( \

295 Z\_LOG\_MSG\_SIMPLE\_CREATE\_1(\_source, \_level, \_\_VA\_ARGS\_\_, dummy) \

296 ), ( \

297 Z\_LOG\_MSG\_SIMPLE\_CREATE\_2(\_source, \_level, \_\_VA\_ARGS\_\_, dummy, dummy) \

298 ) \

299 )))

300

[ 310](group__log__msg.md#gaf39825bcdef376cf77e9844aa87b426c)#define LOG\_MSG\_SIMPLE\_FUNC(\_source, \_level, ...) \

311 Z\_LOG\_MSG\_SIMPLE\_FUNC2(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \_source, \_level, \_\_VA\_ARGS\_\_)

312

323#define Z\_LOG\_MSG\_SIMPLE\_ARGS\_CREATE(\_domain\_id, \_source, \_level, ...) \

324 IF\_ENABLED(LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK(\_\_VA\_ARGS\_\_), (\

325 LOG\_MSG\_SIMPLE\_FUNC(\_source, \_level, \_\_VA\_ARGS\_\_); \

326 ))

327

328#define Z\_LOG\_MSG\_STACK\_CREATE(\_cstr\_cnt, \_domain\_id, \_source, \_level, \_data, \_dlen, ...) \

329do { \

330 int \_plen; \

331 uint32\_t \_options = Z\_LOG\_MSG\_CBPRINTF\_FLAGS(\_cstr\_cnt) | \

332 CBPRINTF\_PACKAGE\_ADD\_RW\_STR\_POS; \

333 if (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_) == NULL) { \

334 \_plen = 0; \

335 } else { \

336 CBPRINTF\_STATIC\_PACKAGE(NULL, 0, \_plen, Z\_LOG\_MSG\_ALIGN\_OFFSET, \_options, \

337 \_\_VA\_ARGS\_\_); \

338 } \

339 TOOLCHAIN\_IGNORE\_WSHADOW\_BEGIN \

340 struct log\_msg \*\_msg; \

341 TOOLCHAIN\_IGNORE\_WSHADOW\_END \

342 Z\_LOG\_MSG\_ON\_STACK\_ALLOC(\_msg, Z\_LOG\_MSG\_LEN(\_plen, 0)); \

343 Z\_LOG\_ARM64\_VLA\_PROTECT(); \

344 if (\_plen != 0) { \

345 CBPRINTF\_STATIC\_PACKAGE(\_msg->data, \_plen, \

346 \_plen, Z\_LOG\_MSG\_ALIGN\_OFFSET, \_options, \

347 \_\_VA\_ARGS\_\_);\

348 } \

349 struct log\_msg\_desc \_desc = \

350 Z\_LOG\_MSG\_DESC\_INITIALIZER(\_domain\_id, \_level, \

351 (uint32\_t)\_plen, \_dlen); \

352 LOG\_MSG\_DBG("creating message on stack: package len: %d, data len: %d\n", \

353 \_plen, (int)(\_dlen)); \

354 z\_log\_msg\_static\_create((void \*)(\_source), \_desc, \_msg->data, (\_data)); \

355} while (false)

356

357#ifdef CONFIG\_LOG\_SPEED

358#define Z\_LOG\_MSG\_SIMPLE\_CREATE(\_cstr\_cnt, \_domain\_id, \_source, \_level, ...) do { \

359 int \_plen; \

360 CBPRINTF\_STATIC\_PACKAGE(NULL, 0, \_plen, Z\_LOG\_MSG\_ALIGN\_OFFSET, \

361 Z\_LOG\_MSG\_CBPRINTF\_FLAGS(\_cstr\_cnt), \

362 \_\_VA\_ARGS\_\_); \

363 size\_t \_msg\_wlen = Z\_LOG\_MSG\_ALIGNED\_WLEN(\_plen, 0); \

364 struct log\_msg \*\_msg = z\_log\_msg\_alloc(\_msg\_wlen); \

365 struct log\_msg\_desc \_desc = \

366 Z\_LOG\_MSG\_DESC\_INITIALIZER(\_domain\_id, \_level, (uint32\_t)\_plen, 0); \

367 LOG\_MSG\_DBG("creating message zero copy: package len: %d, msg: %p\n", \

368 \_plen, \_msg); \

369 if (\_msg) { \

370 CBPRINTF\_STATIC\_PACKAGE(\_msg->data, \_plen, \_plen, \

371 Z\_LOG\_MSG\_ALIGN\_OFFSET, \

372 Z\_LOG\_MSG\_CBPRINTF\_FLAGS(\_cstr\_cnt), \

373 \_\_VA\_ARGS\_\_); \

374 } \

375 z\_log\_msg\_finalize(\_msg, (void \*)\_source, \_desc, NULL); \

376} while (false)

377#else

378/\* Alternative empty macro created to speed up compilation when LOG\_SPEED is

379 \* disabled (default).

380 \*/

381#define Z\_LOG\_MSG\_SIMPLE\_CREATE(...)

382#endif

383

384/\* Macro handles case when local variable with log message string is created. It

385 \* replaces original string literal with that variable.

386 \*/

387#define Z\_LOG\_FMT\_ARGS\_2(\_name, ...) \

388 COND\_CODE\_1(CONFIG\_LOG\_FMT\_SECTION, \

389 (COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

390 (\_name), (\_name, GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_)))), \

391 (\_\_VA\_ARGS\_\_))

392

402#define Z\_LOG\_FMT\_ARGS(\_name, ...) \

403 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_, ##\_\_VA\_ARGS\_\_), \

404 (NULL), \

405 (Z\_LOG\_FMT\_ARGS\_2(\_name, ##\_\_VA\_ARGS\_\_)))

406

407#if defined(CONFIG\_LOG\_USE\_TAGGED\_ARGUMENTS)

408

409#define Z\_LOG\_FMT\_TAGGED\_ARGS\_2(\_name, ...) \

410 COND\_CODE\_1(CONFIG\_LOG\_FMT\_SECTION, \

411 (\_name, Z\_CBPRINTF\_TAGGED\_ARGS(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

412 GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))), \

413 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_), \

414 Z\_CBPRINTF\_TAGGED\_ARGS(NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), \

415 GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_))))

416

427#define Z\_LOG\_FMT\_TAGGED\_ARGS(\_name, ...) \

428 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_, ##\_\_VA\_ARGS\_\_), \

429 (Z\_CBPRINTF\_TAGGED\_ARGS(0)), \

430 (Z\_LOG\_FMT\_TAGGED\_ARGS\_2(\_name, ##\_\_VA\_ARGS\_\_)))

431

432#define Z\_LOG\_FMT\_RUNTIME\_ARGS(...) \

433 Z\_LOG\_FMT\_TAGGED\_ARGS(\_\_VA\_ARGS\_\_)

434

435#else

436

437#define Z\_LOG\_FMT\_RUNTIME\_ARGS(...) \

438 Z\_LOG\_FMT\_ARGS(\_\_VA\_ARGS\_\_)

439

440#endif /\* CONFIG\_LOG\_USE\_TAGGED\_ARGUMENTS \*/

441

442/\* Macro handles case when there is no string provided, in that case variable

443 \* is not created.

444 \*/

445#define Z\_LOG\_MSG\_STR\_VAR\_IN\_SECTION(\_name, ...) \

446 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_, ##\_\_VA\_ARGS\_\_), \

447 (/\* No args provided, no variable \*/), \

448 (static const char \_name[] \

449 \_\_in\_section(\_log\_strings, static, \_CONCAT(\_name, \_)) \_\_used \_\_noasan = \

450 GET\_ARG\_N(1, \_\_VA\_ARGS\_\_);))

451

459#define Z\_LOG\_MSG\_STR\_VAR(\_name, ...) \

460 IF\_ENABLED(CONFIG\_LOG\_FMT\_SECTION, \

461 (Z\_LOG\_MSG\_STR\_VAR\_IN\_SECTION(\_name, ##\_\_VA\_ARGS\_\_)))

462

502#if defined(CONFIG\_LOG\_ALWAYS\_RUNTIME) || !defined(CONFIG\_LOG)

503#define Z\_LOG\_MSG\_CREATE2(\_try\_0cpy, \_mode, \_cstr\_cnt, \_domain\_id, \_source,\

504 \_level, \_data, \_dlen, ...) \

505do {\

506 Z\_LOG\_MSG\_STR\_VAR(\_fmt, ##\_\_VA\_ARGS\_\_) \

507 z\_log\_msg\_runtime\_create((\_domain\_id), (void \*)(\_source), \

508 (\_level), (uint8\_t \*)(\_data), (\_dlen),\

509 Z\_LOG\_MSG\_CBPRINTF\_FLAGS(\_cstr\_cnt) | \

510 (IS\_ENABLED(CONFIG\_LOG\_USE\_TAGGED\_ARGUMENTS) ? \

511 CBPRINTF\_PACKAGE\_ARGS\_ARE\_TAGGED : 0), \

512 Z\_LOG\_FMT\_RUNTIME\_ARGS(\_fmt, ##\_\_VA\_ARGS\_\_));\

513 (\_mode) = Z\_LOG\_MSG\_MODE\_RUNTIME; \

514} while (false)

515#else /\* CONFIG\_LOG\_ALWAYS\_RUNTIME || !CONFIG\_LOG \*/

516#define Z\_LOG\_MSG\_CREATE3(\_try\_0cpy, \_mode, \_cstr\_cnt, \_domain\_id, \_source,\

517 \_level, \_data, \_dlen, ...) \

518do { \

519 Z\_LOG\_MSG\_STR\_VAR(\_fmt, ##\_\_VA\_ARGS\_\_); \

520 bool has\_rw\_str = CBPRINTF\_MUST\_RUNTIME\_PACKAGE( \

521 Z\_LOG\_MSG\_CBPRINTF\_FLAGS(\_cstr\_cnt), \

522 \_\_VA\_ARGS\_\_); \

523 if (IS\_ENABLED(CONFIG\_LOG\_SPEED) && (\_try\_0cpy) && ((\_dlen) == 0) && !has\_rw\_str) {\

524 LOG\_MSG\_DBG("create zero-copy message\n");\

525 Z\_LOG\_MSG\_SIMPLE\_CREATE(\_cstr\_cnt, \_domain\_id, \_source, \

526 \_level, Z\_LOG\_FMT\_ARGS(\_fmt, ##\_\_VA\_ARGS\_\_)); \

527 (\_mode) = Z\_LOG\_MSG\_MODE\_ZERO\_COPY; \

528 } else { \

529 IF\_ENABLED(UTIL\_AND(IS\_ENABLED(CONFIG\_LOG\_SIMPLE\_MSG\_OPTIMIZE), \

530 UTIL\_AND(UTIL\_NOT(\_domain\_id), UTIL\_NOT(\_cstr\_cnt))), \

531 ( \

532 bool can\_simple = LOG\_MSG\_SIMPLE\_CHECK(\_\_VA\_ARGS\_\_); \

533 if (can\_simple && ((\_dlen) == 0) && !k\_is\_user\_context()) { \

534 LOG\_MSG\_DBG("create fast message\n");\

535 Z\_LOG\_MSG\_SIMPLE\_ARGS\_CREATE(\_domain\_id, \_source, \_level, \

536 Z\_LOG\_FMT\_ARGS(\_fmt, ##\_\_VA\_ARGS\_\_)); \

537 \_mode = Z\_LOG\_MSG\_MODE\_SIMPLE; \

538 break; \

539 } \

540 ) \

541 ) \

542 LOG\_MSG\_DBG("create on stack message\n");\

543 Z\_LOG\_MSG\_STACK\_CREATE(\_cstr\_cnt, \_domain\_id, \_source, \_level, \_data, \

544 \_dlen, Z\_LOG\_FMT\_ARGS(\_fmt, ##\_\_VA\_ARGS\_\_)); \

545 (\_mode) = Z\_LOG\_MSG\_MODE\_FROM\_STACK; \

546 } \

547 (void)(\_mode); \

548} while (false)

549

550#if defined(\_\_cplusplus)

551#define Z\_AUTO\_TYPE auto

552#else

553#define Z\_AUTO\_TYPE \_\_auto\_type

554#endif

555

556/\* Macro for getting name of a local variable with the exception of the first argument

557 \* which is a formatted string in log message.

558 \*/

559#define Z\_LOG\_LOCAL\_ARG\_NAME(idx, arg) COND\_CODE\_0(idx, (arg), (\_v##idx))

560

561/\* Create local variable from input variable (expect for the first (fmt) argument). \*/

562#define Z\_LOG\_LOCAL\_ARG\_CREATE(idx, arg) \

563 COND\_CODE\_0(idx, (), (Z\_AUTO\_TYPE Z\_LOG\_LOCAL\_ARG\_NAME(idx, arg) = (arg) + 0))

564

565/\* First level of processing creates stack variables to be passed for further processing.

566 \* This is done to prevent multiple evaluations of input arguments (in case argument

567 \* evaluation has side effects, e.g. it is a non-pure function call).

568 \*/

569#define Z\_LOG\_MSG\_CREATE2(\_try\_0cpy, \_mode, \_cstr\_cnt, \_domain\_id, \_source, \

570 \_level, \_data, \_dlen, ...) \

571do { \

572 \_Pragma("GCC diagnostic push") \

573 \_Pragma("GCC diagnostic ignored \"-Wpointer-arith\"") \

574 FOR\_EACH\_IDX(Z\_LOG\_LOCAL\_ARG\_CREATE, (;), \_\_VA\_ARGS\_\_); \

575 \_Pragma("GCC diagnostic pop") \

576 Z\_LOG\_MSG\_CREATE3(\_try\_0cpy, \_mode, \_cstr\_cnt, \_domain\_id, \_source,\

577 \_level, \_data, \_dlen, \

578 FOR\_EACH\_IDX(Z\_LOG\_LOCAL\_ARG\_NAME, (,), \_\_VA\_ARGS\_\_)); \

579} while (false)

580#endif /\* CONFIG\_LOG\_ALWAYS\_RUNTIME || !CONFIG\_LOG \*/

581

582

583#define Z\_LOG\_MSG\_CREATE(\_try\_0cpy, \_mode, \_domain\_id, \_source,\

584 \_level, \_data, \_dlen, ...) \

585 Z\_LOG\_MSG\_CREATE2(\_try\_0cpy, \_mode, UTIL\_CAT(Z\_LOG\_FUNC\_PREFIX\_, \_level), \

586 \_domain\_id, \_source, \_level, \_data, \_dlen, \

587 Z\_LOG\_STR(\_level, \_\_VA\_ARGS\_\_))

588

595struct [log\_msg](structlog__msg.md) \*z\_log\_msg\_alloc([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wlen);

596

610void z\_log\_msg\_finalize(struct [log\_msg](structlog__msg.md) \*msg, const void \*source,

611 const struct [log\_msg\_desc](structlog__msg__desc.md) desc, const void \*[data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e));

612

619\_\_syscall void z\_log\_msg\_simple\_create\_0(const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level,

620 const char \*fmt);

621

629\_\_syscall void z\_log\_msg\_simple\_create\_1(const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level,

630 const char \*fmt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg);

631

640\_\_syscall void z\_log\_msg\_simple\_create\_2(const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level,

641 const char \*fmt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg0, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1);

642

653\_\_syscall void z\_log\_msg\_static\_create(const void \*source,

654 const struct [log\_msg\_desc](structlog__msg__desc.md) desc,

655 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*package, const void \*[data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e));

656

678void z\_log\_msg\_runtime\_vcreate([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) domain\_id, const void \*source,

679 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level, const void \*[data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e),

680 size\_t dlen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) package\_flags,

681 const char \*fmt,

682 va\_list ap);

683

705static inline void z\_log\_msg\_runtime\_create([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) domain\_id,

706 const void \*source,

707 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level, const void \*[data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e),

708 size\_t dlen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) package\_flags,

709 const char \*fmt, ...)

710{

711 va\_list ap;

712

713 va\_start(ap, fmt);

714 z\_log\_msg\_runtime\_vcreate(domain\_id, source, level,

715 [data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e), dlen, package\_flags, fmt, ap);

716 va\_end(ap);

717}

718

719static inline bool z\_log\_item\_is\_msg(const union [log\_msg\_generic](unionlog__msg__generic.md) \*msg)

720{

721 return msg->[generic](unionlog__msg__generic.md#ad1d622e11a94fb14cbb4bd13871751d5).[type](structlog__msg__generic__hdr.md#abf94410d7d163a5cda5615e7fe9fbaf2) == Z\_LOG\_MSG\_LOG;

722}

723

[ 730](group__log__msg.md#gac26779a741754cfb0f79f1cd78ece856)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_msg\_get\_total\_wlen](group__log__msg.md#gac26779a741754cfb0f79f1cd78ece856)(const struct [log\_msg\_desc](structlog__msg__desc.md) desc)

731{

732 return Z\_LOG\_MSG\_ALIGNED\_WLEN(desc.[package\_len](structlog__msg__desc.md#a3b9fb3a9e612ec8642e5e595d6478ac3), desc.[data\_len](structlog__msg__desc.md#aff700ad436ba87af141268e8f7aa5f6f));

733}

734

[ 741](group__log__msg.md#gaaf2e1b6af3957a1d23898ec8ad94e7f7)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_msg\_generic\_get\_wlen](group__log__msg.md#gaaf2e1b6af3957a1d23898ec8ad94e7f7)(const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*item)

742{

743 const union [log\_msg\_generic](unionlog__msg__generic.md) \*generic\_msg = (const union [log\_msg\_generic](unionlog__msg__generic.md) \*)item;

744

745 if (z\_log\_item\_is\_msg(generic\_msg)) {

746 const struct [log\_msg](structlog__msg.md) \*msg = (const struct [log\_msg](structlog__msg.md) \*)generic\_msg;

747

748 return [log\_msg\_get\_total\_wlen](group__log__msg.md#gac26779a741754cfb0f79f1cd78ece856)(msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).[desc](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895));

749 }

750

751 return 0;

752}

753

[ 760](group__log__msg.md#gaa4f92e19f94212a8a580d19b587fcbb1)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [log\_msg\_get\_domain](group__log__msg.md#gaa4f92e19f94212a8a580d19b587fcbb1)(struct [log\_msg](structlog__msg.md) \*msg)

761{

762 return msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).[desc](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895).[domain](structlog__msg__desc.md#a2636fe29ddba79450689b90beff3c3c7);

763}

764

[ 771](group__log__msg.md#ga952503e8252dc60f5920e473b76cfb47)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [log\_msg\_get\_level](group__log__msg.md#ga952503e8252dc60f5920e473b76cfb47)(struct [log\_msg](structlog__msg.md) \*msg)

772{

773 return msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).[desc](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895).[level](structlog__msg__desc.md#a8cc3ca0930b892a6a9b7b73d20f8628e);

774}

775

[ 782](group__log__msg.md#ga2e65669fe7fb9cbb357bdcab0eda02df)static inline const void \*[log\_msg\_get\_source](group__log__msg.md#ga2e65669fe7fb9cbb357bdcab0eda02df)(struct [log\_msg](structlog__msg.md) \*msg)

783{

784 return msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).[source](structlog__msg__hdr.md#aab20cd4267d37793299a2ed3a5e75236);

785}

786

[ 793](group__log__msg.md#ga5ca82bb442eededbfd3e06196e7ea412)[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [log\_msg\_get\_source\_id](group__log__msg.md#ga5ca82bb442eededbfd3e06196e7ea412)(struct [log\_msg](structlog__msg.md) \*msg);

794

[ 801](group__log__msg.md#gae0541cad3c66df189a5c6e454459b3b0)static inline [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) [log\_msg\_get\_timestamp](group__log__msg.md#gae0541cad3c66df189a5c6e454459b3b0)(struct [log\_msg](structlog__msg.md) \*msg)

802{

803 return msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).[timestamp](structlog__msg__hdr.md#a48ba27c6897377fafda1a980422fb2f4);

804}

805

[ 812](group__log__msg.md#ga9750b8652b310e5292f1e510e5bf0ef5)static inline void \*[log\_msg\_get\_tid](group__log__msg.md#ga9750b8652b310e5292f1e510e5bf0ef5)(struct [log\_msg](structlog__msg.md) \*msg)

813{

814#if defined(CONFIG\_LOG\_THREAD\_ID\_PREFIX)

815 return msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).tid;

816#else

817 ARG\_UNUSED(msg);

818 return NULL;

819#endif

820}

821

[ 830](group__log__msg.md#gaed59653e68c2076a3add6abb52471a9e)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[log\_msg\_get\_data](group__log__msg.md#gaed59653e68c2076a3add6abb52471a9e)(struct [log\_msg](structlog__msg.md) \*msg, size\_t \*len)

831{

832 \*len = msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).[desc](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895).[data\_len](structlog__msg__desc.md#aff700ad436ba87af141268e8f7aa5f6f);

833

834 return msg->[data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e) + msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).[desc](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895).[package\_len](structlog__msg__desc.md#a3b9fb3a9e612ec8642e5e595d6478ac3);

835}

836

[ 845](group__log__msg.md#gad433f993ebc12644f9e3476c3d542c58)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[log\_msg\_get\_package](group__log__msg.md#gad433f993ebc12644f9e3476c3d542c58)(struct [log\_msg](structlog__msg.md) \*msg, size\_t \*len)

846{

847 \*len = msg->[hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a).[desc](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895).[package\_len](structlog__msg__desc.md#a3b9fb3a9e612ec8642e5e595d6478ac3);

848

849 return msg->[data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e);

850}

851

855

856#include <zephyr/syscalls/log\_msg.h>

857

858#ifdef \_\_cplusplus

859}

860#endif

861

862#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_MSG\_H\_ \*/

[cbprintf.h](cbprintf_8h.md)

[log\_msg\_get\_source](group__log__msg.md#ga2e65669fe7fb9cbb357bdcab0eda02df)

static const void \* log\_msg\_get\_source(struct log\_msg \*msg)

Get message source data.

**Definition** log\_msg.h:782

[log\_msg\_get\_source\_id](group__log__msg.md#ga5ca82bb442eededbfd3e06196e7ea412)

int16\_t log\_msg\_get\_source\_id(struct log\_msg \*msg)

Get log message source ID.

[log\_msg\_get\_level](group__log__msg.md#ga952503e8252dc60f5920e473b76cfb47)

static uint8\_t log\_msg\_get\_level(struct log\_msg \*msg)

Get log message level.

**Definition** log\_msg.h:771

[log\_msg\_get\_tid](group__log__msg.md#ga9750b8652b310e5292f1e510e5bf0ef5)

static void \* log\_msg\_get\_tid(struct log\_msg \*msg)

Get Thread ID.

**Definition** log\_msg.h:812

[log\_msg\_get\_domain](group__log__msg.md#gaa4f92e19f94212a8a580d19b587fcbb1)

static uint8\_t log\_msg\_get\_domain(struct log\_msg \*msg)

Get log message domain ID.

**Definition** log\_msg.h:760

[log\_msg\_generic\_get\_wlen](group__log__msg.md#gaaf2e1b6af3957a1d23898ec8ad94e7f7)

static uint32\_t log\_msg\_generic\_get\_wlen(const union mpsc\_pbuf\_generic \*item)

Get length of the log item.

**Definition** log\_msg.h:741

[LOG\_MSG\_GENERIC\_HDR](group__log__msg.md#gaba2b53ea6e29c20d452322d664ed4f18)

#define LOG\_MSG\_GENERIC\_HDR

**Definition** log\_msg.h:52

[log\_msg\_get\_total\_wlen](group__log__msg.md#gac26779a741754cfb0f79f1cd78ece856)

static uint32\_t log\_msg\_get\_total\_wlen(const struct log\_msg\_desc desc)

Get total length (in 32 bit words) of a log message.

**Definition** log\_msg.h:730

[log\_msg\_get\_package](group__log__msg.md#gad433f993ebc12644f9e3476c3d542c58)

static uint8\_t \* log\_msg\_get\_package(struct log\_msg \*msg, size\_t \*len)

Get string package.

**Definition** log\_msg.h:845

[log\_msg\_get\_timestamp](group__log__msg.md#gae0541cad3c66df189a5c6e454459b3b0)

static log\_timestamp\_t log\_msg\_get\_timestamp(struct log\_msg \*msg)

Get timestamp.

**Definition** log\_msg.h:801

[log\_msg\_get\_data](group__log__msg.md#gaed59653e68c2076a3add6abb52471a9e)

static uint8\_t \* log\_msg\_get\_data(struct log\_msg \*msg, size\_t \*len)

Get data buffer.

**Definition** log\_msg.h:830

[log\_instance.h](log__instance_8h.md)

[log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)

uint32\_t log\_timestamp\_t

**Definition** log\_msg.h:36

[mpsc\_packet.h](mpsc__packet_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[string.h](string_8h.md)

[log\_msg\_desc](structlog__msg__desc.md)

**Definition** log\_msg.h:56

[log\_msg\_desc::domain](structlog__msg__desc.md#a2636fe29ddba79450689b90beff3c3c7)

uint32\_t domain

**Definition** log\_msg.h:58

[log\_msg\_desc::package\_len](structlog__msg__desc.md#a3b9fb3a9e612ec8642e5e595d6478ac3)

uint32\_t package\_len

**Definition** log\_msg.h:60

[log\_msg\_desc::level](structlog__msg__desc.md#a8cc3ca0930b892a6a9b7b73d20f8628e)

uint32\_t level

**Definition** log\_msg.h:59

[log\_msg\_desc::data\_len](structlog__msg__desc.md#aff700ad436ba87af141268e8f7aa5f6f)

uint32\_t data\_len

**Definition** log\_msg.h:61

[log\_msg\_generic\_hdr](structlog__msg__generic__hdr.md)

**Definition** log\_msg.h:113

[log\_msg\_generic\_hdr::type](structlog__msg__generic__hdr.md#abf94410d7d163a5cda5615e7fe9fbaf2)

uint32\_t type

**Definition** log\_msg.h:114

[log\_msg\_hdr](structlog__msg__hdr.md)

**Definition** log\_msg.h:70

[log\_msg\_hdr::desc](structlog__msg__hdr.md#a2bb4a6020e4a29cc758b7325b8e8c895)

struct log\_msg\_desc desc

**Definition** log\_msg.h:71

[log\_msg\_hdr::timestamp](structlog__msg__hdr.md#a48ba27c6897377fafda1a980422fb2f4)

log\_timestamp\_t timestamp

**Definition** log\_msg.h:80

[log\_msg\_hdr::source](structlog__msg__hdr.md#aab20cd4267d37793299a2ed3a5e75236)

const void \* source

**Definition** log\_msg.h:79

[log\_msg](structlog__msg.md)

**Definition** log\_msg.h:94

[log\_msg::data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e)

uint8\_t data[]

**Definition** log\_msg.h:100

[log\_msg::padding](structlog__msg.md#a539123bce09e55516406cf2a25610e8d)

uint8\_t padding[((sizeof(struct log\_msg\_hdr) % CBPRINTF\_PACKAGE\_ALIGNMENT) > 0 ?(CBPRINTF\_PACKAGE\_ALIGNMENT -(sizeof(struct log\_msg\_hdr) % CBPRINTF\_PACKAGE\_ALIGNMENT)) :0)]

**Definition** log\_msg.h:99

[log\_msg::hdr](structlog__msg.md#a5831ce7bc8d973714a7ca37455890d2a)

struct log\_msg\_hdr hdr

**Definition** log\_msg.h:95

[log\_source\_const\_data](structlog__source__const__data.md)

Constant data associated with the source of log messages.

**Definition** log\_instance.h:17

[log\_source\_dynamic\_data](structlog__source__dynamic__data.md)

Dynamic data associated with the source of log messages.

**Definition** log\_instance.h:30

[atomic.h](sys_2atomic_8h.md)

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[log\_msg\_generic](unionlog__msg__generic.md)

**Definition** log\_msg.h:117

[log\_msg\_generic::buf](unionlog__msg__generic.md#a74b4fa4fff98e914f8e7536fe0be568d)

union mpsc\_pbuf\_generic buf

**Definition** log\_msg.h:118

[log\_msg\_generic::log](unionlog__msg__generic.md#a9a030d553e2104e674d2495b674aa158)

struct log\_msg log

**Definition** log\_msg.h:120

[log\_msg\_generic::generic](unionlog__msg__generic.md#ad1d622e11a94fb14cbb4bd13871751d5)

struct log\_msg\_generic\_hdr generic

**Definition** log\_msg.h:119

[log\_msg\_source](unionlog__msg__source.md)

**Definition** log\_msg.h:64

[log\_msg\_source::fixed](unionlog__msg__source.md#a19ced11229bfe3c6d93c22828e8cb1c8)

const struct log\_source\_const\_data \* fixed

**Definition** log\_msg.h:65

[log\_msg\_source::dynamic](unionlog__msg__source.md#a38427fdbef5b2d35ae2ad75a8db88d37)

struct log\_source\_dynamic\_data \* dynamic

**Definition** log\_msg.h:66

[log\_msg\_source::raw](unionlog__msg__source.md#aceb87931abda0ca5b7f2532df99fcaf6)

void \* raw

**Definition** log\_msg.h:67

[mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md)

Generic packet header.

**Definition** mpsc\_packet.h:49

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_msg.h](log__msg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
