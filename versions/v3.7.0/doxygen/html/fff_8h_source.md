---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fff_8h_source.html
original_path: doxygen/html/fff_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fff.h

[Go to the documentation of this file.](fff_8h.md)

1/\*

2LICENSE

3

4The MIT License (MIT)

5

6Copyright (c) 2010 Michael Long

7

8Permission is hereby granted, free of charge, to any person obtaining a copy

9of this software and associated documentation files (the "Software"), to deal

10in the Software without restriction, including without limitation the rights

11to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

12copies of the Software, and to permit persons to whom the Software is

13furnished to do so, subject to the following conditions:

14

15The above copyright notice and this permission notice shall be included in all

16copies or substantial portions of the Software.

17

18THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

19IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

20FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

21AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

22LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

23OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

24SOFTWARE.

25\*/

26#ifndef FAKE\_FUNCTIONS

27#define FAKE\_FUNCTIONS

28

29#include <stdarg.h>

30#include <[string.h](string_8h.md)> /\* For memset and memcpy \*/

31

[ 32](fff_8h.md#a9fe16236d19cf8512af62a965887e038)#define FFF\_MAX\_ARGS (20u)

33#ifndef FFF\_ARG\_HISTORY\_LEN

[ 34](fff_8h.md#a7e08b23090c6385246513b05f4bcd948)#define FFF\_ARG\_HISTORY\_LEN (50u)

35#endif

36#ifndef FFF\_CALL\_HISTORY\_LEN

[ 37](fff_8h.md#a8056b9838c2f7a0defc054404737777b)#define FFF\_CALL\_HISTORY\_LEN (50u)

38#endif

39#ifndef FFF\_GCC\_FUNCTION\_ATTRIBUTES

[ 40](fff_8h.md#a946034885bca653eb96b3506fee510d9)#define FFF\_GCC\_FUNCTION\_ATTRIBUTES

41#endif

42#ifndef CUSTOM\_FFF\_FUNCTION\_TEMPLATE

[ 43](fff_8h.md#a3afca787a52954d620bfc1cf15c00c09)#define CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN, FUNCNAME, ...) RETURN (\*FUNCNAME)(\_\_VA\_ARGS\_\_)

44#endif /\* CUSTOM\_FFF\_FUNCTION\_TEMPLATE \*/

45/\* -- INTERNAL HELPER MACROS -- \*/

[ 46](fff_8h.md#acdca2e59514f2393766c66ccb235fdee)#define SET\_RETURN\_SEQ(FUNCNAME, ARRAY\_POINTER, ARRAY\_LEN) \

47 FUNCNAME##\_fake.return\_val\_seq = ARRAY\_POINTER; \

48 FUNCNAME##\_fake.return\_val\_seq\_len = ARRAY\_LEN;

[ 49](fff_8h.md#a312c7ffe4911b7ee89c96ba5a710394a)#define SET\_CUSTOM\_FAKE\_SEQ(FUNCNAME, ARRAY\_POINTER, ARRAY\_LEN) \

50 FUNCNAME##\_fake.custom\_fake\_seq = ARRAY\_POINTER; \

51 FUNCNAME##\_fake.custom\_fake\_seq\_len = ARRAY\_LEN;

52

53/\* Defining a function to reset a fake function \*/

[ 54](fff_8h.md#aeb6d3347167d658bbd604805a5ea4648)#define RESET\_FAKE(FUNCNAME) \

55 { \

56 FUNCNAME##\_reset(); \

57 }

58

[ 59](fff_8h.md#a17de136cb5d33eaa97f32453f0092867)#define DECLARE\_ARG(type, n, FUNCNAME) \

60 type arg##n##\_val; \

61 type arg##n##\_history[FFF\_ARG\_HISTORY\_LEN];

62

[ 63](fff_8h.md#acf9b31d0f297d9ebf8613e9f8e3873de)#define DECLARE\_ALL\_FUNC\_COMMON \

64 unsigned int call\_count; \

65 unsigned int arg\_history\_len; \

66 unsigned int arg\_histories\_dropped;

67

[ 68](fff_8h.md#a75f63764ee2938556c973f0bde7fb017)#define DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

69 RETURN\_TYPE return\_val\_history[FFF\_ARG\_HISTORY\_LEN];

70

[ 71](fff_8h.md#a3e2f865bd86814ffac51b1dc1e4d3450)#define SAVE\_ARG(FUNCNAME, n) \

72 memcpy((void \*)&FUNCNAME##\_fake.arg##n##\_val, (void \*)&arg##n, sizeof(arg##n));

73

[ 74](fff_8h.md#a9de5f1b447452968c07a477fbfec9c9e)#define ROOM\_FOR\_MORE\_HISTORY(FUNCNAME) FUNCNAME##\_fake.call\_count < FFF\_ARG\_HISTORY\_LEN

75

[ 76](fff_8h.md#af7caefd665b7c070c1cee343ca572dce)#define SAVE\_RET\_HISTORY(FUNCNAME, RETVAL) \

77 if ((FUNCNAME##\_fake.call\_count - 1) < FFF\_ARG\_HISTORY\_LEN) \

78 memcpy((void \*)&FUNCNAME##\_fake \

79 .return\_val\_history[FUNCNAME##\_fake.call\_count - 1], \

80 (const void \*)&RETVAL, sizeof(RETVAL));

81

[ 82](fff_8h.md#afb6d5256553c3be825f7f83fe6d5dde9)#define SAVE\_ARG\_HISTORY(FUNCNAME, ARGN) \

83 memcpy((void \*)&FUNCNAME##\_fake.arg##ARGN##\_history[FUNCNAME##\_fake.call\_count], \

84 (void \*)&arg##ARGN, sizeof(arg##ARGN));

85

[ 86](fff_8h.md#adcf92825fec9b9478398765cb84cd00f)#define HISTORY\_DROPPED(FUNCNAME) FUNCNAME##\_fake.arg\_histories\_dropped++

87

[ 88](fff_8h.md#a80bea996d8adbb85983d092aedf27615)#define DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

89 RETURN\_TYPE return\_val; \

90 int return\_val\_seq\_len; \

91 int return\_val\_seq\_idx; \

92 RETURN\_TYPE \*return\_val\_seq;

93

[ 94](fff_8h.md#a7884e082e23fc3f1b4a23a6f4b6fd303)#define DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

95 int custom\_fake\_seq\_len; \

96 int custom\_fake\_seq\_idx;

97

[ 98](fff_8h.md#ae570ba4a02c31f264f5da7d092c8cac4)#define INCREMENT\_CALL\_COUNT(FUNCNAME) FUNCNAME##\_fake.call\_count++

99

[ 100](fff_8h.md#af19fef1f0025bb4733e998d35bc03310)#define RETURN\_FAKE\_RESULT(FUNCNAME) \

101 if (FUNCNAME##\_fake.return\_val\_seq\_len) { /\* then its a sequence \*/ \

102 if (FUNCNAME##\_fake.return\_val\_seq\_idx < FUNCNAME##\_fake.return\_val\_seq\_len) { \

103 SAVE\_RET\_HISTORY( \

104 FUNCNAME, \

105 FUNCNAME##\_fake \

106 .return\_val\_seq[FUNCNAME##\_fake.return\_val\_seq\_idx]) \

107 return FUNCNAME##\_fake \

108 .return\_val\_seq[FUNCNAME##\_fake.return\_val\_seq\_idx++]; \

109 } \

110 SAVE\_RET\_HISTORY( \

111 FUNCNAME, \

112 FUNCNAME##\_fake.return\_val\_seq[FUNCNAME##\_fake.return\_val\_seq\_len - 1]) \

113 return FUNCNAME##\_fake.return\_val\_seq[FUNCNAME##\_fake.return\_val\_seq\_len - \

114 1]; /\* return last element \*/ \

115 } \

116 SAVE\_RET\_HISTORY(FUNCNAME, FUNCNAME##\_fake.return\_val) \

117 return FUNCNAME##\_fake.return\_val;

118

119#ifdef \_\_cplusplus

120#define FFF\_EXTERN\_C extern "C" {

121#define FFF\_END\_EXTERN\_C }

122#else /\* ansi c \*/

[ 123](fff_8h.md#ac3290fea38c680b4048fb9146760c635)#define FFF\_EXTERN\_C

[ 124](fff_8h.md#a159a878a982506014524691639f0d0a4)#define FFF\_END\_EXTERN\_C

125#endif /\* cpp/ansi c \*/

126

[ 127](fff_8h.md#aec1937352832e066bddd2220ccc8a503)#define DEFINE\_RESET\_FUNCTION(FUNCNAME) \

128 void FUNCNAME##\_reset(void) \

129 { \

130 memset((void \*)&FUNCNAME##\_fake, 0, \

131 sizeof(FUNCNAME##\_fake) - sizeof(FUNCNAME##\_fake.custom\_fake) - \

132 sizeof(FUNCNAME##\_fake.custom\_fake\_seq)); \

133 FUNCNAME##\_fake.custom\_fake = NULL; \

134 FUNCNAME##\_fake.custom\_fake\_seq = NULL; \

135 FUNCNAME##\_fake.arg\_history\_len = FFF\_ARG\_HISTORY\_LEN; \

136 }

137/\* -- END INTERNAL HELPER MACROS -- \*/

138

[ 139](fff_8h.md#a5a81a0e0882be6192f4f18c7b8d41aa1)typedef void (\*[fff\_function\_t](fff_8h.md#a5a81a0e0882be6192f4f18c7b8d41aa1))(void);

[ 140](structfff__globals__t.md)typedef struct {

[ 141](structfff__globals__t.md#a22ffdf4369472e55dbdf96ae898ca4cf) [fff\_function\_t](fff_8h.md#a5a81a0e0882be6192f4f18c7b8d41aa1) [call\_history](structfff__globals__t.md#a22ffdf4369472e55dbdf96ae898ca4cf)[[FFF\_CALL\_HISTORY\_LEN](fff_8h.md#a8056b9838c2f7a0defc054404737777b)];

[ 142](structfff__globals__t.md#ad5c29f2faa27bef5e706417cd2a73eb5) unsigned int [call\_history\_idx](structfff__globals__t.md#ad5c29f2faa27bef5e706417cd2a73eb5);

143} [fff\_globals\_t](structfff__globals__t.md);

144

145[FFF\_EXTERN\_C](fff_8h.md#ac3290fea38c680b4048fb9146760c635)

146extern [fff\_globals\_t](structfff__globals__t.md) [fff](fff_8h.md#a484e7178f2bbf168acc8ce2111c913f2);

147[FFF\_END\_EXTERN\_C](fff_8h.md#a159a878a982506014524691639f0d0a4)

148

[ 149](fff_8h.md#a960321ea6641d5d565950f67f3caebb1)#define DEFINE\_FFF\_GLOBALS \

150 FFF\_EXTERN\_C \

151 fff\_globals\_t fff; \

152 FFF\_END\_EXTERN\_C

153

[ 154](fff_8h.md#a8f15da2835ad360aee7683bf15e304ca)#define FFF\_RESET\_HISTORY() \

155 fff.call\_history\_idx = 0; \

156 memset(fff.call\_history, 0, sizeof(fff.call\_history));

157

[ 158](fff_8h.md#a539b3c049757e910bee6c8c6f5414e30)#define REGISTER\_CALL(function) \

159 if (fff.call\_history\_idx < FFF\_CALL\_HISTORY\_LEN) \

160 fff.call\_history[fff.call\_history\_idx++] = (fff\_function\_t)function;

161

[ 162](fff_8h.md#ab78d1321173c5ec6fa029201d80b7243)#define DECLARE\_FAKE\_VOID\_FUNC0(FUNCNAME) \

163 typedef struct FUNCNAME##\_Fake { \

164 DECLARE\_ALL\_FUNC\_COMMON \

165 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

166 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, void); \

167 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, void); \

168 } FUNCNAME##\_Fake; \

169 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

170 void FUNCNAME##\_reset(void); \

171 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(void);

172

[ 173](fff_8h.md#aad05785f517f7bfed8fbdabd94197b31)#define DEFINE\_FAKE\_VOID\_FUNC0(FUNCNAME) \

174 FUNCNAME##\_Fake FUNCNAME##\_fake; \

175 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(void) \

176 { \

177 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

178 } else { \

179 HISTORY\_DROPPED(FUNCNAME); \

180 } \

181 INCREMENT\_CALL\_COUNT(FUNCNAME); \

182 REGISTER\_CALL(FUNCNAME); \

183 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

184 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

185 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

186 FUNCNAME##\_fake \

187 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++](); \

188 } else { \

189 FUNCNAME##\_fake \

190 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - \

191 1](); \

192 } \

193 } \

194 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

195 FUNCNAME##\_fake.custom\_fake(); \

196 } \

197 } \

198 DEFINE\_RESET\_FUNCTION(FUNCNAME)

199

[ 200](fff_8h.md#a4d1ab0fa0d0d90f90177ad393870fc15)#define FAKE\_VOID\_FUNC0(FUNCNAME) \

201 DECLARE\_FAKE\_VOID\_FUNC0(FUNCNAME) \

202 DEFINE\_FAKE\_VOID\_FUNC0(FUNCNAME)

203

[ 204](fff_8h.md#ab99f92d18abc83674d17291169275712)#define DECLARE\_FAKE\_VOID\_FUNC1(FUNCNAME, ARG0\_TYPE) \

205 typedef struct FUNCNAME##\_Fake { \

206 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

207 DECLARE\_ALL\_FUNC\_COMMON \

208 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

209 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE); \

210 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE); \

211 } FUNCNAME##\_Fake; \

212 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

213 void FUNCNAME##\_reset(void); \

214 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0);

215

[ 216](fff_8h.md#a4b83661285f76e002833cf73600a0ef4)#define DEFINE\_FAKE\_VOID\_FUNC1(FUNCNAME, ARG0\_TYPE) \

217 FUNCNAME##\_Fake FUNCNAME##\_fake; \

218 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0) \

219 { \

220 SAVE\_ARG(FUNCNAME, 0); \

221 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

222 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

223 } else { \

224 HISTORY\_DROPPED(FUNCNAME); \

225 } \

226 INCREMENT\_CALL\_COUNT(FUNCNAME); \

227 REGISTER\_CALL(FUNCNAME); \

228 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

229 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

230 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

231 FUNCNAME##\_fake \

232 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

233 arg0); \

234 } else { \

235 FUNCNAME##\_fake \

236 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

237 arg0); \

238 } \

239 } \

240 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

241 FUNCNAME##\_fake.custom\_fake(arg0); \

242 } \

243 } \

244 DEFINE\_RESET\_FUNCTION(FUNCNAME)

245

[ 246](fff_8h.md#aefef27bc3014a5535c02cc7b9c043355)#define FAKE\_VOID\_FUNC1(FUNCNAME, ARG0\_TYPE) \

247 DECLARE\_FAKE\_VOID\_FUNC1(FUNCNAME, ARG0\_TYPE) \

248 DEFINE\_FAKE\_VOID\_FUNC1(FUNCNAME, ARG0\_TYPE)

249

[ 250](fff_8h.md#a0ac9e87dc810b8a5bb6e6c532e6be39d)#define DECLARE\_FAKE\_VOID\_FUNC2(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE) \

251 typedef struct FUNCNAME##\_Fake { \

252 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

253 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

254 DECLARE\_ALL\_FUNC\_COMMON \

255 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

256 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE); \

257 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE); \

258 } FUNCNAME##\_Fake; \

259 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

260 void FUNCNAME##\_reset(void); \

261 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1);

262

[ 263](fff_8h.md#a5be5bb3c42fca77b248404aff6cd2027)#define DEFINE\_FAKE\_VOID\_FUNC2(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE) \

264 FUNCNAME##\_Fake FUNCNAME##\_fake; \

265 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1) \

266 { \

267 SAVE\_ARG(FUNCNAME, 0); \

268 SAVE\_ARG(FUNCNAME, 1); \

269 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

270 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

271 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

272 } else { \

273 HISTORY\_DROPPED(FUNCNAME); \

274 } \

275 INCREMENT\_CALL\_COUNT(FUNCNAME); \

276 REGISTER\_CALL(FUNCNAME); \

277 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

278 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

279 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

280 FUNCNAME##\_fake \

281 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

282 arg0, arg1); \

283 } else { \

284 FUNCNAME##\_fake \

285 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

286 arg0, arg1); \

287 } \

288 } \

289 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

290 FUNCNAME##\_fake.custom\_fake(arg0, arg1); \

291 } \

292 } \

293 DEFINE\_RESET\_FUNCTION(FUNCNAME)

294

[ 295](fff_8h.md#a58cde3d8a1e79effd038c63a59e55104)#define FAKE\_VOID\_FUNC2(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE) \

296 DECLARE\_FAKE\_VOID\_FUNC2(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE) \

297 DEFINE\_FAKE\_VOID\_FUNC2(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE)

298

[ 299](fff_8h.md#ad5293b1eb48a7d4d5a11c3c75aaa5d71)#define DECLARE\_FAKE\_VOID\_FUNC3(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE) \

300 typedef struct FUNCNAME##\_Fake { \

301 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

302 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

303 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

304 DECLARE\_ALL\_FUNC\_COMMON \

305 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

306 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE); \

307 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

308 ARG2\_TYPE); \

309 } FUNCNAME##\_Fake; \

310 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

311 void FUNCNAME##\_reset(void); \

312 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2);

313

[ 314](fff_8h.md#a6d2c55ab70f5fb9acd9760d9d09e42f9)#define DEFINE\_FAKE\_VOID\_FUNC3(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE) \

315 FUNCNAME##\_Fake FUNCNAME##\_fake; \

316 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2) \

317 { \

318 SAVE\_ARG(FUNCNAME, 0); \

319 SAVE\_ARG(FUNCNAME, 1); \

320 SAVE\_ARG(FUNCNAME, 2); \

321 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

322 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

323 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

324 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

325 } else { \

326 HISTORY\_DROPPED(FUNCNAME); \

327 } \

328 INCREMENT\_CALL\_COUNT(FUNCNAME); \

329 REGISTER\_CALL(FUNCNAME); \

330 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

331 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

332 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

333 FUNCNAME##\_fake \

334 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

335 arg0, arg1, arg2); \

336 } else { \

337 FUNCNAME##\_fake \

338 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

339 arg0, arg1, arg2); \

340 } \

341 } \

342 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

343 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2); \

344 } \

345 } \

346 DEFINE\_RESET\_FUNCTION(FUNCNAME)

347

[ 348](fff_8h.md#aa130f9e166b31b1156fceccda8dc31df)#define FAKE\_VOID\_FUNC3(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE) \

349 DECLARE\_FAKE\_VOID\_FUNC3(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE) \

350 DEFINE\_FAKE\_VOID\_FUNC3(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE)

351

[ 352](fff_8h.md#a7db609175d368a7f64569899944cbc83)#define DECLARE\_FAKE\_VOID\_FUNC4(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE) \

353 typedef struct FUNCNAME##\_Fake { \

354 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

355 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

356 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

357 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

358 DECLARE\_ALL\_FUNC\_COMMON \

359 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

360 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

361 ARG3\_TYPE); \

362 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

363 ARG2\_TYPE, ARG3\_TYPE); \

364 } FUNCNAME##\_Fake; \

365 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

366 void FUNCNAME##\_reset(void); \

367 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

368 ARG3\_TYPE arg3);

369

[ 370](fff_8h.md#a1dd59da676a468c78c4d71482b227a3f)#define DEFINE\_FAKE\_VOID\_FUNC4(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE) \

371 FUNCNAME##\_Fake FUNCNAME##\_fake; \

372 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

373 ARG3\_TYPE arg3) \

374 { \

375 SAVE\_ARG(FUNCNAME, 0); \

376 SAVE\_ARG(FUNCNAME, 1); \

377 SAVE\_ARG(FUNCNAME, 2); \

378 SAVE\_ARG(FUNCNAME, 3); \

379 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

380 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

381 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

382 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

383 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

384 } else { \

385 HISTORY\_DROPPED(FUNCNAME); \

386 } \

387 INCREMENT\_CALL\_COUNT(FUNCNAME); \

388 REGISTER\_CALL(FUNCNAME); \

389 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

390 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

391 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

392 FUNCNAME##\_fake \

393 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

394 arg0, arg1, arg2, arg3); \

395 } else { \

396 FUNCNAME##\_fake \

397 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

398 arg0, arg1, arg2, arg3); \

399 } \

400 } \

401 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

402 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3); \

403 } \

404 } \

405 DEFINE\_RESET\_FUNCTION(FUNCNAME)

406

[ 407](fff_8h.md#afad7544f90a9db9c9d14d6565006a314)#define FAKE\_VOID\_FUNC4(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE) \

408 DECLARE\_FAKE\_VOID\_FUNC4(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE) \

409 DEFINE\_FAKE\_VOID\_FUNC4(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE)

410

[ 411](fff_8h.md#acad2449d38b7d37e8cfc81920a4cb4cf)#define DECLARE\_FAKE\_VOID\_FUNC5(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE) \

412 typedef struct FUNCNAME##\_Fake { \

413 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

414 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

415 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

416 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

417 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

418 DECLARE\_ALL\_FUNC\_COMMON \

419 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

420 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

421 ARG3\_TYPE, ARG4\_TYPE); \

422 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

423 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE); \

424 } FUNCNAME##\_Fake; \

425 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

426 void FUNCNAME##\_reset(void); \

427 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

428 ARG3\_TYPE arg3, ARG4\_TYPE arg4);

429

[ 430](fff_8h.md#a0d1fba2ef7aa0c128f2773a640c536e3)#define DEFINE\_FAKE\_VOID\_FUNC5(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE) \

431 FUNCNAME##\_Fake FUNCNAME##\_fake; \

432 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

433 ARG3\_TYPE arg3, ARG4\_TYPE arg4) \

434 { \

435 SAVE\_ARG(FUNCNAME, 0); \

436 SAVE\_ARG(FUNCNAME, 1); \

437 SAVE\_ARG(FUNCNAME, 2); \

438 SAVE\_ARG(FUNCNAME, 3); \

439 SAVE\_ARG(FUNCNAME, 4); \

440 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

441 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

442 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

443 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

444 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

445 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

446 } else { \

447 HISTORY\_DROPPED(FUNCNAME); \

448 } \

449 INCREMENT\_CALL\_COUNT(FUNCNAME); \

450 REGISTER\_CALL(FUNCNAME); \

451 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

452 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

453 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

454 FUNCNAME##\_fake \

455 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

456 arg0, arg1, arg2, arg3, arg4); \

457 } else { \

458 FUNCNAME##\_fake \

459 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

460 arg0, arg1, arg2, arg3, arg4); \

461 } \

462 } \

463 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

464 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4); \

465 } \

466 } \

467 DEFINE\_RESET\_FUNCTION(FUNCNAME)

468

[ 469](fff_8h.md#ae468697dd7626c63a5093cc505b9056b)#define FAKE\_VOID\_FUNC5(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE) \

470 DECLARE\_FAKE\_VOID\_FUNC5(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE) \

471 DEFINE\_FAKE\_VOID\_FUNC5(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE)

472

[ 473](fff_8h.md#a791750f81a0ab23de808df374498812b)#define DECLARE\_FAKE\_VOID\_FUNC6(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

474 ARG5\_TYPE) \

475 typedef struct FUNCNAME##\_Fake { \

476 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

477 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

478 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

479 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

480 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

481 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

482 DECLARE\_ALL\_FUNC\_COMMON \

483 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

484 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

485 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE); \

486 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

487 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE); \

488 } FUNCNAME##\_Fake; \

489 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

490 void FUNCNAME##\_reset(void); \

491 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

492 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5);

493

[ 494](fff_8h.md#a644fc466c398bee48c8b47b02f40d7c5)#define DEFINE\_FAKE\_VOID\_FUNC6(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

495 ARG5\_TYPE) \

496 FUNCNAME##\_Fake FUNCNAME##\_fake; \

497 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

498 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5) \

499 { \

500 SAVE\_ARG(FUNCNAME, 0); \

501 SAVE\_ARG(FUNCNAME, 1); \

502 SAVE\_ARG(FUNCNAME, 2); \

503 SAVE\_ARG(FUNCNAME, 3); \

504 SAVE\_ARG(FUNCNAME, 4); \

505 SAVE\_ARG(FUNCNAME, 5); \

506 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

507 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

508 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

509 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

510 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

511 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

512 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

513 } else { \

514 HISTORY\_DROPPED(FUNCNAME); \

515 } \

516 INCREMENT\_CALL\_COUNT(FUNCNAME); \

517 REGISTER\_CALL(FUNCNAME); \

518 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

519 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

520 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

521 FUNCNAME##\_fake \

522 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

523 arg0, arg1, arg2, arg3, arg4, arg5); \

524 } else { \

525 FUNCNAME##\_fake \

526 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

527 arg0, arg1, arg2, arg3, arg4, arg5); \

528 } \

529 } \

530 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

531 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5); \

532 } \

533 } \

534 DEFINE\_RESET\_FUNCTION(FUNCNAME)

535

[ 536](fff_8h.md#a13e908e62ea8cc666d2b52af87d31d94)#define FAKE\_VOID\_FUNC6(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

537 ARG5\_TYPE) \

538 DECLARE\_FAKE\_VOID\_FUNC6(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

539 ARG5\_TYPE) \

540 DEFINE\_FAKE\_VOID\_FUNC6(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

541 ARG5\_TYPE)

542

[ 543](fff_8h.md#a5e93a67a7a9398e66cd5d8c32b2cf97b)#define DECLARE\_FAKE\_VOID\_FUNC7(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

544 ARG5\_TYPE, ARG6\_TYPE) \

545 typedef struct FUNCNAME##\_Fake { \

546 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

547 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

548 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

549 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

550 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

551 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

552 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

553 DECLARE\_ALL\_FUNC\_COMMON \

554 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

555 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

556 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE); \

557 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

558 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

559 ARG6\_TYPE); \

560 } FUNCNAME##\_Fake; \

561 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

562 void FUNCNAME##\_reset(void); \

563 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

564 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

565 ARG6\_TYPE arg6);

566

[ 567](fff_8h.md#a952ad059564364677d12eb60e3502ced)#define DEFINE\_FAKE\_VOID\_FUNC7(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

568 ARG5\_TYPE, ARG6\_TYPE) \

569 FUNCNAME##\_Fake FUNCNAME##\_fake; \

570 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

571 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

572 ARG6\_TYPE arg6) \

573 { \

574 SAVE\_ARG(FUNCNAME, 0); \

575 SAVE\_ARG(FUNCNAME, 1); \

576 SAVE\_ARG(FUNCNAME, 2); \

577 SAVE\_ARG(FUNCNAME, 3); \

578 SAVE\_ARG(FUNCNAME, 4); \

579 SAVE\_ARG(FUNCNAME, 5); \

580 SAVE\_ARG(FUNCNAME, 6); \

581 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

582 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

583 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

584 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

585 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

586 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

587 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

588 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

589 } else { \

590 HISTORY\_DROPPED(FUNCNAME); \

591 } \

592 INCREMENT\_CALL\_COUNT(FUNCNAME); \

593 REGISTER\_CALL(FUNCNAME); \

594 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

595 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

596 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

597 FUNCNAME##\_fake \

598 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

599 arg0, arg1, arg2, arg3, arg4, arg5, arg6); \

600 } else { \

601 FUNCNAME##\_fake \

602 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

603 arg0, arg1, arg2, arg3, arg4, arg5, arg6); \

604 } \

605 } \

606 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

607 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6); \

608 } \

609 } \

610 DEFINE\_RESET\_FUNCTION(FUNCNAME)

611

[ 612](fff_8h.md#af4c9613946a4564812695db47c18c7fe)#define FAKE\_VOID\_FUNC7(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

613 ARG5\_TYPE, ARG6\_TYPE) \

614 DECLARE\_FAKE\_VOID\_FUNC7(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

615 ARG5\_TYPE, ARG6\_TYPE) \

616 DEFINE\_FAKE\_VOID\_FUNC7(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

617 ARG5\_TYPE, ARG6\_TYPE)

618

[ 619](fff_8h.md#a40ded2b5aa02187f35c64597decd85e3)#define DECLARE\_FAKE\_VOID\_FUNC8(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

620 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE) \

621 typedef struct FUNCNAME##\_Fake { \

622 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

623 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

624 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

625 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

626 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

627 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

628 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

629 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

630 DECLARE\_ALL\_FUNC\_COMMON \

631 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

632 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

633 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

634 ARG7\_TYPE); \

635 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

636 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

637 ARG6\_TYPE, ARG7\_TYPE); \

638 } FUNCNAME##\_Fake; \

639 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

640 void FUNCNAME##\_reset(void); \

641 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

642 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

643 ARG6\_TYPE arg6, ARG7\_TYPE arg7);

644

[ 645](fff_8h.md#ae9ad8635021363488ca5a60f7443172b)#define DEFINE\_FAKE\_VOID\_FUNC8(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

646 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE) \

647 FUNCNAME##\_Fake FUNCNAME##\_fake; \

648 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

649 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

650 ARG6\_TYPE arg6, ARG7\_TYPE arg7) \

651 { \

652 SAVE\_ARG(FUNCNAME, 0); \

653 SAVE\_ARG(FUNCNAME, 1); \

654 SAVE\_ARG(FUNCNAME, 2); \

655 SAVE\_ARG(FUNCNAME, 3); \

656 SAVE\_ARG(FUNCNAME, 4); \

657 SAVE\_ARG(FUNCNAME, 5); \

658 SAVE\_ARG(FUNCNAME, 6); \

659 SAVE\_ARG(FUNCNAME, 7); \

660 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

661 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

662 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

663 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

664 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

665 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

666 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

667 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

668 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

669 } else { \

670 HISTORY\_DROPPED(FUNCNAME); \

671 } \

672 INCREMENT\_CALL\_COUNT(FUNCNAME); \

673 REGISTER\_CALL(FUNCNAME); \

674 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

675 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

676 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

677 FUNCNAME##\_fake \

678 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

679 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7); \

680 } else { \

681 FUNCNAME##\_fake \

682 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

683 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7); \

684 } \

685 } \

686 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

687 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

688 arg7); \

689 } \

690 } \

691 DEFINE\_RESET\_FUNCTION(FUNCNAME)

692

[ 693](fff_8h.md#a414c19398243ecb3b6e6089a970b517d)#define FAKE\_VOID\_FUNC8(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

694 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE) \

695 DECLARE\_FAKE\_VOID\_FUNC8(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

696 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE) \

697 DEFINE\_FAKE\_VOID\_FUNC8(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

698 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE)

699

[ 700](fff_8h.md#aeb6fdcc872b8cac7a43e567912ead87a)#define DECLARE\_FAKE\_VOID\_FUNC9(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

701 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE) \

702 typedef struct FUNCNAME##\_Fake { \

703 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

704 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

705 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

706 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

707 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

708 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

709 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

710 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

711 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

712 DECLARE\_ALL\_FUNC\_COMMON \

713 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

714 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

715 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

716 ARG7\_TYPE, ARG8\_TYPE); \

717 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

718 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

719 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE); \

720 } FUNCNAME##\_Fake; \

721 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

722 void FUNCNAME##\_reset(void); \

723 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

724 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

725 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8);

726

[ 727](fff_8h.md#a1e82227c0a74849ca3df99fea2da718f)#define DEFINE\_FAKE\_VOID\_FUNC9(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

728 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE) \

729 FUNCNAME##\_Fake FUNCNAME##\_fake; \

730 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

731 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

732 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8) \

733 { \

734 SAVE\_ARG(FUNCNAME, 0); \

735 SAVE\_ARG(FUNCNAME, 1); \

736 SAVE\_ARG(FUNCNAME, 2); \

737 SAVE\_ARG(FUNCNAME, 3); \

738 SAVE\_ARG(FUNCNAME, 4); \

739 SAVE\_ARG(FUNCNAME, 5); \

740 SAVE\_ARG(FUNCNAME, 6); \

741 SAVE\_ARG(FUNCNAME, 7); \

742 SAVE\_ARG(FUNCNAME, 8); \

743 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

744 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

745 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

746 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

747 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

748 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

749 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

750 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

751 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

752 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

753 } else { \

754 HISTORY\_DROPPED(FUNCNAME); \

755 } \

756 INCREMENT\_CALL\_COUNT(FUNCNAME); \

757 REGISTER\_CALL(FUNCNAME); \

758 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

759 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

760 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

761 FUNCNAME##\_fake \

762 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

763 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

764 arg8); \

765 } else { \

766 FUNCNAME##\_fake \

767 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

768 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

769 arg8); \

770 } \

771 } \

772 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

773 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

774 arg7, arg8); \

775 } \

776 } \

777 DEFINE\_RESET\_FUNCTION(FUNCNAME)

778

[ 779](fff_8h.md#a9bfcd16a665682cbc7acc723762fc057)#define FAKE\_VOID\_FUNC9(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

780 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE) \

781 DECLARE\_FAKE\_VOID\_FUNC9(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

782 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE) \

783 DEFINE\_FAKE\_VOID\_FUNC9(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

784 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE)

785

[ 786](fff_8h.md#a89b7e7d5b41cb8658b44ef43e51bc460)#define DECLARE\_FAKE\_VOID\_FUNC10(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

787 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE) \

788 typedef struct FUNCNAME##\_Fake { \

789 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

790 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

791 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

792 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

793 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

794 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

795 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

796 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

797 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

798 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

799 DECLARE\_ALL\_FUNC\_COMMON \

800 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

801 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

802 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

803 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE); \

804 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

805 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

806 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE); \

807 } FUNCNAME##\_Fake; \

808 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

809 void FUNCNAME##\_reset(void); \

810 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

811 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

812 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9);

813

[ 814](fff_8h.md#ab3d57c134c4ded89611bd80eeb4f2ba6)#define DEFINE\_FAKE\_VOID\_FUNC10(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

815 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE) \

816 FUNCNAME##\_Fake FUNCNAME##\_fake; \

817 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

818 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

819 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9) \

820 { \

821 SAVE\_ARG(FUNCNAME, 0); \

822 SAVE\_ARG(FUNCNAME, 1); \

823 SAVE\_ARG(FUNCNAME, 2); \

824 SAVE\_ARG(FUNCNAME, 3); \

825 SAVE\_ARG(FUNCNAME, 4); \

826 SAVE\_ARG(FUNCNAME, 5); \

827 SAVE\_ARG(FUNCNAME, 6); \

828 SAVE\_ARG(FUNCNAME, 7); \

829 SAVE\_ARG(FUNCNAME, 8); \

830 SAVE\_ARG(FUNCNAME, 9); \

831 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

832 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

833 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

834 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

835 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

836 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

837 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

838 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

839 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

840 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

841 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

842 } else { \

843 HISTORY\_DROPPED(FUNCNAME); \

844 } \

845 INCREMENT\_CALL\_COUNT(FUNCNAME); \

846 REGISTER\_CALL(FUNCNAME); \

847 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

848 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

849 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

850 FUNCNAME##\_fake \

851 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

852 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

853 arg8, arg9); \

854 } else { \

855 FUNCNAME##\_fake \

856 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

857 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

858 arg8, arg9); \

859 } \

860 } \

861 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

862 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

863 arg7, arg8, arg9); \

864 } \

865 } \

866 DEFINE\_RESET\_FUNCTION(FUNCNAME)

867

[ 868](fff_8h.md#adb8da71d91ec087bc164e858626c3357)#define FAKE\_VOID\_FUNC10(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

869 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE) \

870 DECLARE\_FAKE\_VOID\_FUNC10(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

871 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE) \

872 DEFINE\_FAKE\_VOID\_FUNC10(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

873 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE)

874

[ 875](fff_8h.md#ac56a1d374d97f590e42a06748b081ab1)#define DECLARE\_FAKE\_VOID\_FUNC11(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

876 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

877 ARG10\_TYPE) \

878 typedef struct FUNCNAME##\_Fake { \

879 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

880 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

881 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

882 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

883 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

884 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

885 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

886 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

887 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

888 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

889 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

890 DECLARE\_ALL\_FUNC\_COMMON \

891 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

892 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

893 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

894 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE); \

895 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

896 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

897 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

898 ARG10\_TYPE); \

899 } FUNCNAME##\_Fake; \

900 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

901 void FUNCNAME##\_reset(void); \

902 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

903 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

904 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, \

905 ARG9\_TYPE arg9, ARG10\_TYPE arg10);

906

[ 907](fff_8h.md#a2385b31aafd13aa6ade4e9610c68364f)#define DEFINE\_FAKE\_VOID\_FUNC11(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

908 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE) \

909 FUNCNAME##\_Fake FUNCNAME##\_fake; \

910 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

911 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

912 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, \

913 ARG9\_TYPE arg9, ARG10\_TYPE arg10) \

914 { \

915 SAVE\_ARG(FUNCNAME, 0); \

916 SAVE\_ARG(FUNCNAME, 1); \

917 SAVE\_ARG(FUNCNAME, 2); \

918 SAVE\_ARG(FUNCNAME, 3); \

919 SAVE\_ARG(FUNCNAME, 4); \

920 SAVE\_ARG(FUNCNAME, 5); \

921 SAVE\_ARG(FUNCNAME, 6); \

922 SAVE\_ARG(FUNCNAME, 7); \

923 SAVE\_ARG(FUNCNAME, 8); \

924 SAVE\_ARG(FUNCNAME, 9); \

925 SAVE\_ARG(FUNCNAME, 10); \

926 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

927 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

928 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

929 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

930 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

931 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

932 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

933 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

934 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

935 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

936 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

937 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

938 } else { \

939 HISTORY\_DROPPED(FUNCNAME); \

940 } \

941 INCREMENT\_CALL\_COUNT(FUNCNAME); \

942 REGISTER\_CALL(FUNCNAME); \

943 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

944 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

945 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

946 FUNCNAME##\_fake \

947 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

948 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

949 arg8, arg9, arg10); \

950 } else { \

951 FUNCNAME##\_fake \

952 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

953 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

954 arg8, arg9, arg10); \

955 } \

956 } \

957 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

958 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

959 arg7, arg8, arg9, arg10); \

960 } \

961 } \

962 DEFINE\_RESET\_FUNCTION(FUNCNAME)

963

[ 964](fff_8h.md#a8d25089ec9fc33f35b9f23b875cf7973)#define FAKE\_VOID\_FUNC11(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

965 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE) \

966 DECLARE\_FAKE\_VOID\_FUNC11(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

967 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

968 ARG10\_TYPE) \

969 DEFINE\_FAKE\_VOID\_FUNC11(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

970 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE)

971

[ 972](fff_8h.md#a5c21dacfa939513c65af526392f8e709)#define DECLARE\_FAKE\_VOID\_FUNC12(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

973 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

974 ARG10\_TYPE, ARG11\_TYPE) \

975 typedef struct FUNCNAME##\_Fake { \

976 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

977 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

978 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

979 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

980 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

981 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

982 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

983 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

984 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

985 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

986 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

987 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

988 DECLARE\_ALL\_FUNC\_COMMON \

989 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

990 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

991 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

992 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

993 ARG11\_TYPE); \

994 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

995 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

996 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

997 ARG10\_TYPE, ARG11\_TYPE); \

998 } FUNCNAME##\_Fake; \

999 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1000 void FUNCNAME##\_reset(void); \

1001 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1002 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1003 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1004 ARG10\_TYPE arg10, ARG11\_TYPE arg11);

1005

[ 1006](fff_8h.md#a5708a8e4a97808e7609565f5a481bfdc)#define DEFINE\_FAKE\_VOID\_FUNC12(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1007 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1008 ARG11\_TYPE) \

1009 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1010 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1011 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1012 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1013 ARG10\_TYPE arg10, ARG11\_TYPE arg11) \

1014 { \

1015 SAVE\_ARG(FUNCNAME, 0); \

1016 SAVE\_ARG(FUNCNAME, 1); \

1017 SAVE\_ARG(FUNCNAME, 2); \

1018 SAVE\_ARG(FUNCNAME, 3); \

1019 SAVE\_ARG(FUNCNAME, 4); \

1020 SAVE\_ARG(FUNCNAME, 5); \

1021 SAVE\_ARG(FUNCNAME, 6); \

1022 SAVE\_ARG(FUNCNAME, 7); \

1023 SAVE\_ARG(FUNCNAME, 8); \

1024 SAVE\_ARG(FUNCNAME, 9); \

1025 SAVE\_ARG(FUNCNAME, 10); \

1026 SAVE\_ARG(FUNCNAME, 11); \

1027 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

1028 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

1029 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

1030 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

1031 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

1032 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

1033 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

1034 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

1035 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

1036 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

1037 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

1038 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

1039 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

1040 } else { \

1041 HISTORY\_DROPPED(FUNCNAME); \

1042 } \

1043 INCREMENT\_CALL\_COUNT(FUNCNAME); \

1044 REGISTER\_CALL(FUNCNAME); \

1045 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

1046 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

1047 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

1048 FUNCNAME##\_fake \

1049 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

1050 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1051 arg8, arg9, arg10, arg11); \

1052 } else { \

1053 FUNCNAME##\_fake \

1054 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

1055 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1056 arg8, arg9, arg10, arg11); \

1057 } \

1058 } \

1059 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

1060 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

1061 arg7, arg8, arg9, arg10, arg11); \

1062 } \

1063 } \

1064 DEFINE\_RESET\_FUNCTION(FUNCNAME)

1065

[ 1066](fff_8h.md#a21e9cdea3474881dfa764fecad2e213e)#define FAKE\_VOID\_FUNC12(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1067 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1068 ARG11\_TYPE) \

1069 DECLARE\_FAKE\_VOID\_FUNC12(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1070 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1071 ARG10\_TYPE, ARG11\_TYPE) \

1072 DEFINE\_FAKE\_VOID\_FUNC12(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1073 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1074 ARG11\_TYPE)

1075

[ 1076](fff_8h.md#aaf0768b35079ab19f05d7f6e74dc3b82)#define DECLARE\_FAKE\_VOID\_FUNC13(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1077 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1078 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE) \

1079 typedef struct FUNCNAME##\_Fake { \

1080 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

1081 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

1082 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

1083 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

1084 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

1085 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

1086 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

1087 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

1088 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

1089 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

1090 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

1091 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

1092 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

1093 DECLARE\_ALL\_FUNC\_COMMON \

1094 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

1095 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

1096 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

1097 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1098 ARG11\_TYPE, ARG12\_TYPE); \

1099 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

1100 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

1101 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1102 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE); \

1103 } FUNCNAME##\_Fake; \

1104 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1105 void FUNCNAME##\_reset(void); \

1106 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1107 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1108 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1109 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12);

1110

[ 1111](fff_8h.md#ad812a9430d0b3037e4b39d01c1f0c2d3)#define DEFINE\_FAKE\_VOID\_FUNC13(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1112 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1113 ARG11\_TYPE, ARG12\_TYPE) \

1114 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1115 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1116 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1117 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1118 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12) \

1119 { \

1120 SAVE\_ARG(FUNCNAME, 0); \

1121 SAVE\_ARG(FUNCNAME, 1); \

1122 SAVE\_ARG(FUNCNAME, 2); \

1123 SAVE\_ARG(FUNCNAME, 3); \

1124 SAVE\_ARG(FUNCNAME, 4); \

1125 SAVE\_ARG(FUNCNAME, 5); \

1126 SAVE\_ARG(FUNCNAME, 6); \

1127 SAVE\_ARG(FUNCNAME, 7); \

1128 SAVE\_ARG(FUNCNAME, 8); \

1129 SAVE\_ARG(FUNCNAME, 9); \

1130 SAVE\_ARG(FUNCNAME, 10); \

1131 SAVE\_ARG(FUNCNAME, 11); \

1132 SAVE\_ARG(FUNCNAME, 12); \

1133 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

1134 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

1135 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

1136 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

1137 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

1138 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

1139 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

1140 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

1141 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

1142 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

1143 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

1144 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

1145 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

1146 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

1147 } else { \

1148 HISTORY\_DROPPED(FUNCNAME); \

1149 } \

1150 INCREMENT\_CALL\_COUNT(FUNCNAME); \

1151 REGISTER\_CALL(FUNCNAME); \

1152 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

1153 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

1154 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

1155 FUNCNAME##\_fake \

1156 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

1157 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1158 arg8, arg9, arg10, arg11, arg12); \

1159 } else { \

1160 FUNCNAME##\_fake \

1161 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

1162 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1163 arg8, arg9, arg10, arg11, arg12); \

1164 } \

1165 } \

1166 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

1167 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

1168 arg7, arg8, arg9, arg10, arg11, arg12); \

1169 } \

1170 } \

1171 DEFINE\_RESET\_FUNCTION(FUNCNAME)

1172

[ 1173](fff_8h.md#ab19f5b41ae3d06ab9231207d53a37fbc)#define FAKE\_VOID\_FUNC13(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1174 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1175 ARG11\_TYPE, ARG12\_TYPE) \

1176 DECLARE\_FAKE\_VOID\_FUNC13(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1177 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1178 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE) \

1179 DEFINE\_FAKE\_VOID\_FUNC13(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1180 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1181 ARG11\_TYPE, ARG12\_TYPE)

1182

[ 1183](fff_8h.md#aa05cf613317374b18eae66786cfe5085)#define DECLARE\_FAKE\_VOID\_FUNC14(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1184 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1185 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE) \

1186 typedef struct FUNCNAME##\_Fake { \

1187 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

1188 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

1189 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

1190 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

1191 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

1192 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

1193 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

1194 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

1195 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

1196 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

1197 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

1198 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

1199 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

1200 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

1201 DECLARE\_ALL\_FUNC\_COMMON \

1202 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

1203 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

1204 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

1205 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1206 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE); \

1207 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

1208 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

1209 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1210 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE); \

1211 } FUNCNAME##\_Fake; \

1212 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1213 void FUNCNAME##\_reset(void); \

1214 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1215 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1216 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1217 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13);

1218

[ 1219](fff_8h.md#ac2f88e7448d773b07def79bac5cf5c48)#define DEFINE\_FAKE\_VOID\_FUNC14(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1220 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1221 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE) \

1222 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1223 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1224 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1225 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1226 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13) \

1227 { \

1228 SAVE\_ARG(FUNCNAME, 0); \

1229 SAVE\_ARG(FUNCNAME, 1); \

1230 SAVE\_ARG(FUNCNAME, 2); \

1231 SAVE\_ARG(FUNCNAME, 3); \

1232 SAVE\_ARG(FUNCNAME, 4); \

1233 SAVE\_ARG(FUNCNAME, 5); \

1234 SAVE\_ARG(FUNCNAME, 6); \

1235 SAVE\_ARG(FUNCNAME, 7); \

1236 SAVE\_ARG(FUNCNAME, 8); \

1237 SAVE\_ARG(FUNCNAME, 9); \

1238 SAVE\_ARG(FUNCNAME, 10); \

1239 SAVE\_ARG(FUNCNAME, 11); \

1240 SAVE\_ARG(FUNCNAME, 12); \

1241 SAVE\_ARG(FUNCNAME, 13); \

1242 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

1243 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

1244 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

1245 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

1246 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

1247 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

1248 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

1249 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

1250 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

1251 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

1252 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

1253 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

1254 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

1255 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

1256 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

1257 } else { \

1258 HISTORY\_DROPPED(FUNCNAME); \

1259 } \

1260 INCREMENT\_CALL\_COUNT(FUNCNAME); \

1261 REGISTER\_CALL(FUNCNAME); \

1262 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

1263 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

1264 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

1265 FUNCNAME##\_fake \

1266 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

1267 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1268 arg8, arg9, arg10, arg11, arg12, arg13); \

1269 } else { \

1270 FUNCNAME##\_fake \

1271 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

1272 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1273 arg8, arg9, arg10, arg11, arg12, arg13); \

1274 } \

1275 } \

1276 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

1277 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

1278 arg7, arg8, arg9, arg10, arg11, arg12, arg13); \

1279 } \

1280 } \

1281 DEFINE\_RESET\_FUNCTION(FUNCNAME)

1282

[ 1283](fff_8h.md#ad1fd5d16c5c06accd0e0935aa87362e4)#define FAKE\_VOID\_FUNC14(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1284 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1285 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE) \

1286 DECLARE\_FAKE\_VOID\_FUNC14(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1287 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1288 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE) \

1289 DEFINE\_FAKE\_VOID\_FUNC14(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1290 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1291 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE)

1292

[ 1293](fff_8h.md#aceafe8d7497febee03ca223e6a1825cc)#define DECLARE\_FAKE\_VOID\_FUNC15(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1294 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1295 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE) \

1296 typedef struct FUNCNAME##\_Fake { \

1297 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

1298 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

1299 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

1300 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

1301 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

1302 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

1303 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

1304 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

1305 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

1306 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

1307 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

1308 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

1309 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

1310 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

1311 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

1312 DECLARE\_ALL\_FUNC\_COMMON \

1313 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

1314 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

1315 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

1316 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1317 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE); \

1318 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

1319 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

1320 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1321 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

1322 ARG14\_TYPE); \

1323 } FUNCNAME##\_Fake; \

1324 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1325 void FUNCNAME##\_reset(void); \

1326 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1327 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1328 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1329 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1330 ARG14\_TYPE arg14);

1331

[ 1332](fff_8h.md#a77185fcaba50dc80513bbe745601df57)#define DEFINE\_FAKE\_VOID\_FUNC15(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1333 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1334 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE) \

1335 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1336 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1337 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1338 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1339 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1340 ARG14\_TYPE arg14) \

1341 { \

1342 SAVE\_ARG(FUNCNAME, 0); \

1343 SAVE\_ARG(FUNCNAME, 1); \

1344 SAVE\_ARG(FUNCNAME, 2); \

1345 SAVE\_ARG(FUNCNAME, 3); \

1346 SAVE\_ARG(FUNCNAME, 4); \

1347 SAVE\_ARG(FUNCNAME, 5); \

1348 SAVE\_ARG(FUNCNAME, 6); \

1349 SAVE\_ARG(FUNCNAME, 7); \

1350 SAVE\_ARG(FUNCNAME, 8); \

1351 SAVE\_ARG(FUNCNAME, 9); \

1352 SAVE\_ARG(FUNCNAME, 10); \

1353 SAVE\_ARG(FUNCNAME, 11); \

1354 SAVE\_ARG(FUNCNAME, 12); \

1355 SAVE\_ARG(FUNCNAME, 13); \

1356 SAVE\_ARG(FUNCNAME, 14); \

1357 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

1358 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

1359 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

1360 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

1361 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

1362 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

1363 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

1364 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

1365 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

1366 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

1367 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

1368 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

1369 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

1370 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

1371 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

1372 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

1373 } else { \

1374 HISTORY\_DROPPED(FUNCNAME); \

1375 } \

1376 INCREMENT\_CALL\_COUNT(FUNCNAME); \

1377 REGISTER\_CALL(FUNCNAME); \

1378 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

1379 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

1380 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

1381 FUNCNAME##\_fake \

1382 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

1383 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1384 arg8, arg9, arg10, arg11, arg12, arg13, arg14); \

1385 } else { \

1386 FUNCNAME##\_fake \

1387 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

1388 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1389 arg8, arg9, arg10, arg11, arg12, arg13, arg14); \

1390 } \

1391 } \

1392 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

1393 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

1394 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

1395 arg14); \

1396 } \

1397 } \

1398 DEFINE\_RESET\_FUNCTION(FUNCNAME)

1399

[ 1400](fff_8h.md#a806e50b8d63bffcc906936625f41c689)#define FAKE\_VOID\_FUNC15(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1401 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1402 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE) \

1403 DECLARE\_FAKE\_VOID\_FUNC15(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1404 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1405 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE) \

1406 DEFINE\_FAKE\_VOID\_FUNC15(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1407 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1408 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE)

1409

[ 1410](fff_8h.md#a6626de18acd8522b9bca2fe4d9ef19c2)#define DECLARE\_FAKE\_VOID\_FUNC16(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1411 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1412 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1413 ARG15\_TYPE) \

1414 typedef struct FUNCNAME##\_Fake { \

1415 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

1416 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

1417 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

1418 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

1419 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

1420 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

1421 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

1422 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

1423 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

1424 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

1425 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

1426 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

1427 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

1428 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

1429 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

1430 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

1431 DECLARE\_ALL\_FUNC\_COMMON \

1432 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

1433 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

1434 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

1435 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1436 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1437 ARG15\_TYPE); \

1438 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

1439 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

1440 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1441 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

1442 ARG14\_TYPE, ARG15\_TYPE); \

1443 } FUNCNAME##\_Fake; \

1444 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1445 void FUNCNAME##\_reset(void); \

1446 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1447 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1448 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1449 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1450 ARG14\_TYPE arg14, ARG15\_TYPE arg15);

1451

[ 1452](fff_8h.md#a4eb90f29d11ce17adf5bc260591309ba)#define DEFINE\_FAKE\_VOID\_FUNC16(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1453 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1454 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE) \

1455 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1456 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1457 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1458 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1459 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1460 ARG14\_TYPE arg14, ARG15\_TYPE arg15) \

1461 { \

1462 SAVE\_ARG(FUNCNAME, 0); \

1463 SAVE\_ARG(FUNCNAME, 1); \

1464 SAVE\_ARG(FUNCNAME, 2); \

1465 SAVE\_ARG(FUNCNAME, 3); \

1466 SAVE\_ARG(FUNCNAME, 4); \

1467 SAVE\_ARG(FUNCNAME, 5); \

1468 SAVE\_ARG(FUNCNAME, 6); \

1469 SAVE\_ARG(FUNCNAME, 7); \

1470 SAVE\_ARG(FUNCNAME, 8); \

1471 SAVE\_ARG(FUNCNAME, 9); \

1472 SAVE\_ARG(FUNCNAME, 10); \

1473 SAVE\_ARG(FUNCNAME, 11); \

1474 SAVE\_ARG(FUNCNAME, 12); \

1475 SAVE\_ARG(FUNCNAME, 13); \

1476 SAVE\_ARG(FUNCNAME, 14); \

1477 SAVE\_ARG(FUNCNAME, 15); \

1478 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

1479 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

1480 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

1481 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

1482 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

1483 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

1484 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

1485 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

1486 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

1487 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

1488 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

1489 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

1490 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

1491 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

1492 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

1493 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

1494 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

1495 } else { \

1496 HISTORY\_DROPPED(FUNCNAME); \

1497 } \

1498 INCREMENT\_CALL\_COUNT(FUNCNAME); \

1499 REGISTER\_CALL(FUNCNAME); \

1500 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

1501 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

1502 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

1503 FUNCNAME##\_fake \

1504 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

1505 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1506 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

1507 arg15); \

1508 } else { \

1509 FUNCNAME##\_fake \

1510 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

1511 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1512 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

1513 arg15); \

1514 } \

1515 } \

1516 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

1517 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

1518 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

1519 arg14, arg15); \

1520 } \

1521 } \

1522 DEFINE\_RESET\_FUNCTION(FUNCNAME)

1523

[ 1524](fff_8h.md#a56ee31a1360d616f1b4c6b6a28cada9b)#define FAKE\_VOID\_FUNC16(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1525 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1526 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE) \

1527 DECLARE\_FAKE\_VOID\_FUNC16(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1528 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1529 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1530 ARG15\_TYPE) \

1531 DEFINE\_FAKE\_VOID\_FUNC16(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1532 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1533 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE)

1534

[ 1535](fff_8h.md#a9c749a10123e7a232983b2c39e88f321)#define DECLARE\_FAKE\_VOID\_FUNC17(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1536 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1537 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1538 ARG15\_TYPE, ARG16\_TYPE) \

1539 typedef struct FUNCNAME##\_Fake { \

1540 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

1541 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

1542 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

1543 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

1544 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

1545 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

1546 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

1547 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

1548 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

1549 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

1550 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

1551 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

1552 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

1553 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

1554 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

1555 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

1556 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

1557 DECLARE\_ALL\_FUNC\_COMMON \

1558 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

1559 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

1560 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

1561 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1562 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1563 ARG15\_TYPE, ARG16\_TYPE); \

1564 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

1565 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

1566 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1567 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

1568 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE); \

1569 } FUNCNAME##\_Fake; \

1570 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1571 void FUNCNAME##\_reset(void); \

1572 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1573 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1574 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1575 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1576 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16);

1577

[ 1578](fff_8h.md#a856d61bce56fe69e7644bfb2642b62f1)#define DEFINE\_FAKE\_VOID\_FUNC17(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1579 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1580 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

1581 ARG16\_TYPE) \

1582 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1583 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1584 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1585 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1586 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1587 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16) \

1588 { \

1589 SAVE\_ARG(FUNCNAME, 0); \

1590 SAVE\_ARG(FUNCNAME, 1); \

1591 SAVE\_ARG(FUNCNAME, 2); \

1592 SAVE\_ARG(FUNCNAME, 3); \

1593 SAVE\_ARG(FUNCNAME, 4); \

1594 SAVE\_ARG(FUNCNAME, 5); \

1595 SAVE\_ARG(FUNCNAME, 6); \

1596 SAVE\_ARG(FUNCNAME, 7); \

1597 SAVE\_ARG(FUNCNAME, 8); \

1598 SAVE\_ARG(FUNCNAME, 9); \

1599 SAVE\_ARG(FUNCNAME, 10); \

1600 SAVE\_ARG(FUNCNAME, 11); \

1601 SAVE\_ARG(FUNCNAME, 12); \

1602 SAVE\_ARG(FUNCNAME, 13); \

1603 SAVE\_ARG(FUNCNAME, 14); \

1604 SAVE\_ARG(FUNCNAME, 15); \

1605 SAVE\_ARG(FUNCNAME, 16); \

1606 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

1607 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

1608 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

1609 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

1610 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

1611 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

1612 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

1613 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

1614 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

1615 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

1616 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

1617 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

1618 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

1619 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

1620 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

1621 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

1622 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

1623 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

1624 } else { \

1625 HISTORY\_DROPPED(FUNCNAME); \

1626 } \

1627 INCREMENT\_CALL\_COUNT(FUNCNAME); \

1628 REGISTER\_CALL(FUNCNAME); \

1629 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

1630 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

1631 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

1632 FUNCNAME##\_fake \

1633 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

1634 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1635 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

1636 arg15, arg16); \

1637 } else { \

1638 FUNCNAME##\_fake \

1639 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

1640 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1641 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

1642 arg15, arg16); \

1643 } \

1644 } \

1645 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

1646 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

1647 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

1648 arg14, arg15, arg16); \

1649 } \

1650 } \

1651 DEFINE\_RESET\_FUNCTION(FUNCNAME)

1652

[ 1653](fff_8h.md#aeceaa28703812886d75e5d1f8523908f)#define FAKE\_VOID\_FUNC17(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1654 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1655 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE) \

1656 DECLARE\_FAKE\_VOID\_FUNC17(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1657 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1658 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1659 ARG15\_TYPE, ARG16\_TYPE) \

1660 DEFINE\_FAKE\_VOID\_FUNC17(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1661 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1662 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

1663 ARG16\_TYPE)

1664

[ 1665](fff_8h.md#acc54024599a35ba5474cd6af3882a23f)#define DECLARE\_FAKE\_VOID\_FUNC18(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1666 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1667 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1668 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE) \

1669 typedef struct FUNCNAME##\_Fake { \

1670 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

1671 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

1672 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

1673 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

1674 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

1675 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

1676 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

1677 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

1678 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

1679 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

1680 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

1681 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

1682 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

1683 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

1684 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

1685 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

1686 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

1687 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

1688 DECLARE\_ALL\_FUNC\_COMMON \

1689 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

1690 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

1691 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

1692 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1693 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1694 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE); \

1695 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

1696 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

1697 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1698 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

1699 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE); \

1700 } FUNCNAME##\_Fake; \

1701 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1702 void FUNCNAME##\_reset(void); \

1703 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1704 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1705 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1706 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1707 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17);

1708

[ 1709](fff_8h.md#a3807c729bbb5aecb21bde565f683bf85)#define DEFINE\_FAKE\_VOID\_FUNC18(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1710 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1711 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

1712 ARG16\_TYPE, ARG17\_TYPE) \

1713 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1714 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1715 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1716 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1717 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1718 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17) \

1719 { \

1720 SAVE\_ARG(FUNCNAME, 0); \

1721 SAVE\_ARG(FUNCNAME, 1); \

1722 SAVE\_ARG(FUNCNAME, 2); \

1723 SAVE\_ARG(FUNCNAME, 3); \

1724 SAVE\_ARG(FUNCNAME, 4); \

1725 SAVE\_ARG(FUNCNAME, 5); \

1726 SAVE\_ARG(FUNCNAME, 6); \

1727 SAVE\_ARG(FUNCNAME, 7); \

1728 SAVE\_ARG(FUNCNAME, 8); \

1729 SAVE\_ARG(FUNCNAME, 9); \

1730 SAVE\_ARG(FUNCNAME, 10); \

1731 SAVE\_ARG(FUNCNAME, 11); \

1732 SAVE\_ARG(FUNCNAME, 12); \

1733 SAVE\_ARG(FUNCNAME, 13); \

1734 SAVE\_ARG(FUNCNAME, 14); \

1735 SAVE\_ARG(FUNCNAME, 15); \

1736 SAVE\_ARG(FUNCNAME, 16); \

1737 SAVE\_ARG(FUNCNAME, 17); \

1738 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

1739 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

1740 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

1741 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

1742 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

1743 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

1744 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

1745 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

1746 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

1747 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

1748 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

1749 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

1750 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

1751 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

1752 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

1753 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

1754 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

1755 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

1756 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

1757 } else { \

1758 HISTORY\_DROPPED(FUNCNAME); \

1759 } \

1760 INCREMENT\_CALL\_COUNT(FUNCNAME); \

1761 REGISTER\_CALL(FUNCNAME); \

1762 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

1763 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

1764 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

1765 FUNCNAME##\_fake \

1766 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

1767 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1768 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

1769 arg15, arg16, arg17); \

1770 } else { \

1771 FUNCNAME##\_fake \

1772 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

1773 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1774 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

1775 arg15, arg16, arg17); \

1776 } \

1777 } \

1778 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

1779 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

1780 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

1781 arg14, arg15, arg16, arg17); \

1782 } \

1783 } \

1784 DEFINE\_RESET\_FUNCTION(FUNCNAME)

1785

[ 1786](fff_8h.md#a5d279d4853993e051ea6143f01e62674)#define FAKE\_VOID\_FUNC18(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1787 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1788 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, \

1789 ARG17\_TYPE) \

1790 DECLARE\_FAKE\_VOID\_FUNC18(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1791 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1792 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1793 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE) \

1794 DEFINE\_FAKE\_VOID\_FUNC18(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1795 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1796 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

1797 ARG16\_TYPE, ARG17\_TYPE)

1798

[ 1799](fff_8h.md#a44dbb38d4f03f4ed7d278c07a63f2987)#define DECLARE\_FAKE\_VOID\_FUNC19(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1800 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1801 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1802 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE) \

1803 typedef struct FUNCNAME##\_Fake { \

1804 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

1805 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

1806 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

1807 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

1808 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

1809 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

1810 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

1811 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

1812 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

1813 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

1814 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

1815 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

1816 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

1817 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

1818 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

1819 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

1820 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

1821 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

1822 DECLARE\_ARG(ARG18\_TYPE, 18, FUNCNAME) \

1823 DECLARE\_ALL\_FUNC\_COMMON \

1824 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

1825 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

1826 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

1827 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1828 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1829 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE); \

1830 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

1831 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

1832 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1833 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

1834 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

1835 ARG18\_TYPE); \

1836 } FUNCNAME##\_Fake; \

1837 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1838 void FUNCNAME##\_reset(void); \

1839 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1840 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1841 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1842 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1843 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

1844 ARG18\_TYPE arg18);

1845

[ 1846](fff_8h.md#aa432ec8a525737c2e40227578d1924ef)#define DEFINE\_FAKE\_VOID\_FUNC19(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1847 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1848 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

1849 ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE) \

1850 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1851 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1852 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1853 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1854 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1855 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

1856 ARG18\_TYPE arg18) \

1857 { \

1858 SAVE\_ARG(FUNCNAME, 0); \

1859 SAVE\_ARG(FUNCNAME, 1); \

1860 SAVE\_ARG(FUNCNAME, 2); \

1861 SAVE\_ARG(FUNCNAME, 3); \

1862 SAVE\_ARG(FUNCNAME, 4); \

1863 SAVE\_ARG(FUNCNAME, 5); \

1864 SAVE\_ARG(FUNCNAME, 6); \

1865 SAVE\_ARG(FUNCNAME, 7); \

1866 SAVE\_ARG(FUNCNAME, 8); \

1867 SAVE\_ARG(FUNCNAME, 9); \

1868 SAVE\_ARG(FUNCNAME, 10); \

1869 SAVE\_ARG(FUNCNAME, 11); \

1870 SAVE\_ARG(FUNCNAME, 12); \

1871 SAVE\_ARG(FUNCNAME, 13); \

1872 SAVE\_ARG(FUNCNAME, 14); \

1873 SAVE\_ARG(FUNCNAME, 15); \

1874 SAVE\_ARG(FUNCNAME, 16); \

1875 SAVE\_ARG(FUNCNAME, 17); \

1876 SAVE\_ARG(FUNCNAME, 18); \

1877 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

1878 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

1879 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

1880 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

1881 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

1882 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

1883 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

1884 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

1885 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

1886 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

1887 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

1888 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

1889 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

1890 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

1891 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

1892 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

1893 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

1894 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

1895 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

1896 SAVE\_ARG\_HISTORY(FUNCNAME, 18); \

1897 } else { \

1898 HISTORY\_DROPPED(FUNCNAME); \

1899 } \

1900 INCREMENT\_CALL\_COUNT(FUNCNAME); \

1901 REGISTER\_CALL(FUNCNAME); \

1902 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

1903 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

1904 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

1905 FUNCNAME##\_fake \

1906 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

1907 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1908 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

1909 arg15, arg16, arg17, arg18); \

1910 } else { \

1911 FUNCNAME##\_fake \

1912 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

1913 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

1914 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

1915 arg15, arg16, arg17, arg18); \

1916 } \

1917 } \

1918 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

1919 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

1920 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

1921 arg14, arg15, arg16, arg17, arg18); \

1922 } \

1923 } \

1924 DEFINE\_RESET\_FUNCTION(FUNCNAME)

1925

[ 1926](fff_8h.md#a0a05ecd4abf83561a2a0c2f66eba41e1)#define FAKE\_VOID\_FUNC19(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1927 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1928 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, \

1929 ARG17\_TYPE, ARG18\_TYPE) \

1930 DECLARE\_FAKE\_VOID\_FUNC19(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1931 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1932 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1933 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE) \

1934 DEFINE\_FAKE\_VOID\_FUNC19(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1935 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1936 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

1937 ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE)

1938

[ 1939](fff_8h.md#aeaa57c8271e8705750e5cd99ac13d3e8)#define DECLARE\_FAKE\_VOID\_FUNC20(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1940 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1941 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1942 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ARG19\_TYPE) \

1943 typedef struct FUNCNAME##\_Fake { \

1944 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

1945 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

1946 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

1947 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

1948 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

1949 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

1950 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

1951 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

1952 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

1953 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

1954 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

1955 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

1956 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

1957 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

1958 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

1959 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

1960 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

1961 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

1962 DECLARE\_ARG(ARG18\_TYPE, 18, FUNCNAME) \

1963 DECLARE\_ARG(ARG19\_TYPE, 19, FUNCNAME) \

1964 DECLARE\_ALL\_FUNC\_COMMON \

1965 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

1966 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

1967 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

1968 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1969 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

1970 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, \

1971 ARG19\_TYPE); \

1972 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

1973 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

1974 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

1975 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

1976 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

1977 ARG18\_TYPE, ARG19\_TYPE); \

1978 } FUNCNAME##\_Fake; \

1979 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

1980 void FUNCNAME##\_reset(void); \

1981 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1982 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1983 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1984 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1985 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

1986 ARG18\_TYPE arg18, ARG19\_TYPE arg19);

1987

[ 1988](fff_8h.md#aeeb4a64bc7a19211dcfc9b2696dc0a26)#define DEFINE\_FAKE\_VOID\_FUNC20(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

1989 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

1990 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

1991 ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ARG19\_TYPE) \

1992 FUNCNAME##\_Fake FUNCNAME##\_fake; \

1993 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

1994 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

1995 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

1996 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

1997 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

1998 ARG18\_TYPE arg18, ARG19\_TYPE arg19) \

1999 { \

2000 SAVE\_ARG(FUNCNAME, 0); \

2001 SAVE\_ARG(FUNCNAME, 1); \

2002 SAVE\_ARG(FUNCNAME, 2); \

2003 SAVE\_ARG(FUNCNAME, 3); \

2004 SAVE\_ARG(FUNCNAME, 4); \

2005 SAVE\_ARG(FUNCNAME, 5); \

2006 SAVE\_ARG(FUNCNAME, 6); \

2007 SAVE\_ARG(FUNCNAME, 7); \

2008 SAVE\_ARG(FUNCNAME, 8); \

2009 SAVE\_ARG(FUNCNAME, 9); \

2010 SAVE\_ARG(FUNCNAME, 10); \

2011 SAVE\_ARG(FUNCNAME, 11); \

2012 SAVE\_ARG(FUNCNAME, 12); \

2013 SAVE\_ARG(FUNCNAME, 13); \

2014 SAVE\_ARG(FUNCNAME, 14); \

2015 SAVE\_ARG(FUNCNAME, 15); \

2016 SAVE\_ARG(FUNCNAME, 16); \

2017 SAVE\_ARG(FUNCNAME, 17); \

2018 SAVE\_ARG(FUNCNAME, 18); \

2019 SAVE\_ARG(FUNCNAME, 19); \

2020 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2021 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2022 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2023 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2024 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

2025 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

2026 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

2027 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

2028 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

2029 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

2030 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

2031 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

2032 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

2033 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

2034 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

2035 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

2036 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

2037 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

2038 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

2039 SAVE\_ARG\_HISTORY(FUNCNAME, 18); \

2040 SAVE\_ARG\_HISTORY(FUNCNAME, 19); \

2041 } else { \

2042 HISTORY\_DROPPED(FUNCNAME); \

2043 } \

2044 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2045 REGISTER\_CALL(FUNCNAME); \

2046 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2047 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2048 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2049 FUNCNAME##\_fake \

2050 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2051 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

2052 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

2053 arg15, arg16, arg17, arg18, arg19); \

2054 } else { \

2055 FUNCNAME##\_fake \

2056 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2057 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

2058 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

2059 arg15, arg16, arg17, arg18, arg19); \

2060 } \

2061 } \

2062 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2063 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

2064 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

2065 arg14, arg15, arg16, arg17, arg18, arg19); \

2066 } \

2067 } \

2068 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2069

[ 2070](fff_8h.md#af1ef3d6b16dcc11bb18aa1e43fb3e131)#define FAKE\_VOID\_FUNC20(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

2071 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

2072 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, \

2073 ARG17\_TYPE, ARG18\_TYPE, ARG19\_TYPE) \

2074 DECLARE\_FAKE\_VOID\_FUNC20(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

2075 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

2076 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

2077 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ARG19\_TYPE) \

2078 DEFINE\_FAKE\_VOID\_FUNC20(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

2079 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

2080 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

2081 ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ARG19\_TYPE)

2082

[ 2083](fff_8h.md#a948e9a55b1fb4d8faefeb5586ed87b54)#define DECLARE\_FAKE\_VALUE\_FUNC0(RETURN\_TYPE, FUNCNAME) \

2084 typedef struct FUNCNAME##\_Fake { \

2085 DECLARE\_ALL\_FUNC\_COMMON \

2086 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2087 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2088 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2089 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, void); \

2090 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, void); \

2091 } FUNCNAME##\_Fake; \

2092 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2093 void FUNCNAME##\_reset(void); \

2094 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(void);

2095

[ 2096](fff_8h.md#a62e52bb4169a4064e240fee1d6d0ffef)#define DEFINE\_FAKE\_VALUE\_FUNC0(RETURN\_TYPE, FUNCNAME) \

2097 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2098 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(void) \

2099 { \

2100 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2101 } else { \

2102 HISTORY\_DROPPED(FUNCNAME); \

2103 } \

2104 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2105 REGISTER\_CALL(FUNCNAME); \

2106 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2107 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2108 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2109 RETURN\_TYPE ret = \

2110 FUNCNAME##\_fake.custom\_fake\_seq \

2111 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++](); \

2112 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2113 return ret; \

2114 } else { \

2115 RETURN\_TYPE ret = \

2116 FUNCNAME##\_fake.custom\_fake\_seq \

2117 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1](); \

2118 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2119 return ret; \

2120 return FUNCNAME##\_fake \

2121 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - \

2122 1](); \

2123 } \

2124 } \

2125 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2126 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake(); \

2127 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2128 return ret; \

2129 return FUNCNAME##\_fake.custom\_fake(); \

2130 } \

2131 RETURN\_FAKE\_RESULT(FUNCNAME) \

2132 } \

2133 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2134

[ 2135](fff_8h.md#ad5a62862651ac48fdabbcb2ec166a856)#define FAKE\_VALUE\_FUNC0(RETURN\_TYPE, FUNCNAME) \

2136 DECLARE\_FAKE\_VALUE\_FUNC0(RETURN\_TYPE, FUNCNAME) \

2137 DEFINE\_FAKE\_VALUE\_FUNC0(RETURN\_TYPE, FUNCNAME)

2138

[ 2139](fff_8h.md#a6a83cf86c84df816f5a5a7378940a141)#define DECLARE\_FAKE\_VALUE\_FUNC1(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE) \

2140 typedef struct FUNCNAME##\_Fake { \

2141 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2142 DECLARE\_ALL\_FUNC\_COMMON \

2143 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2144 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2145 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2146 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE); \

2147 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE); \

2148 } FUNCNAME##\_Fake; \

2149 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2150 void FUNCNAME##\_reset(void); \

2151 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0);

2152

[ 2153](fff_8h.md#ad5b9dbf0ecde74490845fdb24ab9c82f)#define DEFINE\_FAKE\_VALUE\_FUNC1(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE) \

2154 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2155 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0) \

2156 { \

2157 SAVE\_ARG(FUNCNAME, 0); \

2158 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2159 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2160 } else { \

2161 HISTORY\_DROPPED(FUNCNAME); \

2162 } \

2163 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2164 REGISTER\_CALL(FUNCNAME); \

2165 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2166 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2167 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2168 RETURN\_TYPE ret = \

2169 FUNCNAME##\_fake.custom\_fake\_seq \

2170 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++](arg0); \

2171 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2172 return ret; \

2173 } else { \

2174 RETURN\_TYPE ret = \

2175 FUNCNAME##\_fake.custom\_fake\_seq \

2176 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1](arg0); \

2177 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2178 return ret; \

2179 return FUNCNAME##\_fake \

2180 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2181 arg0); \

2182 } \

2183 } \

2184 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2185 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake(arg0); \

2186 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2187 return ret; \

2188 return FUNCNAME##\_fake.custom\_fake(arg0); \

2189 } \

2190 RETURN\_FAKE\_RESULT(FUNCNAME) \

2191 } \

2192 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2193

[ 2194](fff_8h.md#a9aa6f70cb4fafba7117582cdd568af7a)#define FAKE\_VALUE\_FUNC1(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE) \

2195 DECLARE\_FAKE\_VALUE\_FUNC1(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE) \

2196 DEFINE\_FAKE\_VALUE\_FUNC1(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE)

2197

[ 2198](fff_8h.md#a47f6a10ebc54d48df5dfb294920faf2c)#define DECLARE\_FAKE\_VALUE\_FUNC2(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE) \

2199 typedef struct FUNCNAME##\_Fake { \

2200 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2201 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2202 DECLARE\_ALL\_FUNC\_COMMON \

2203 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2204 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2205 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2206 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE); \

2207 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE); \

2208 } FUNCNAME##\_Fake; \

2209 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2210 void FUNCNAME##\_reset(void); \

2211 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1);

2212

[ 2213](fff_8h.md#aabc1f9414d1aec0ce34a88addca6ea44)#define DEFINE\_FAKE\_VALUE\_FUNC2(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE) \

2214 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2215 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1) \

2216 { \

2217 SAVE\_ARG(FUNCNAME, 0); \

2218 SAVE\_ARG(FUNCNAME, 1); \

2219 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2220 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2221 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2222 } else { \

2223 HISTORY\_DROPPED(FUNCNAME); \

2224 } \

2225 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2226 REGISTER\_CALL(FUNCNAME); \

2227 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2228 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2229 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2230 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

2231 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2232 arg0, arg1); \

2233 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2234 return ret; \

2235 } else { \

2236 RETURN\_TYPE ret = \

2237 FUNCNAME##\_fake.custom\_fake\_seq \

2238 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1](arg0, \

2239 arg1); \

2240 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2241 return ret; \

2242 return FUNCNAME##\_fake \

2243 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2244 arg0, arg1); \

2245 } \

2246 } \

2247 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2248 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1); \

2249 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2250 return ret; \

2251 return FUNCNAME##\_fake.custom\_fake(arg0, arg1); \

2252 } \

2253 RETURN\_FAKE\_RESULT(FUNCNAME) \

2254 } \

2255 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2256

[ 2257](fff_8h.md#a1334c40947b6a71442d3a8363ab85e45)#define FAKE\_VALUE\_FUNC2(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE) \

2258 DECLARE\_FAKE\_VALUE\_FUNC2(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE) \

2259 DEFINE\_FAKE\_VALUE\_FUNC2(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE)

2260

[ 2261](fff_8h.md#af8d6323b2ca5983fcfbcc5e99d1a22a6)#define DECLARE\_FAKE\_VALUE\_FUNC3(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE) \

2262 typedef struct FUNCNAME##\_Fake { \

2263 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2264 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2265 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2266 DECLARE\_ALL\_FUNC\_COMMON \

2267 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2268 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2269 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2270 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2271 ARG2\_TYPE); \

2272 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

2273 ARG2\_TYPE); \

2274 } FUNCNAME##\_Fake; \

2275 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2276 void FUNCNAME##\_reset(void); \

2277 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

2278 ARG2\_TYPE arg2);

2279

[ 2280](fff_8h.md#a174910cf63261390944368b656443d7c)#define DEFINE\_FAKE\_VALUE\_FUNC3(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE) \

2281 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2282 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

2283 ARG2\_TYPE arg2) \

2284 { \

2285 SAVE\_ARG(FUNCNAME, 0); \

2286 SAVE\_ARG(FUNCNAME, 1); \

2287 SAVE\_ARG(FUNCNAME, 2); \

2288 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2289 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2290 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2291 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2292 } else { \

2293 HISTORY\_DROPPED(FUNCNAME); \

2294 } \

2295 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2296 REGISTER\_CALL(FUNCNAME); \

2297 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2298 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2299 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2300 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

2301 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2302 arg0, arg1, arg2); \

2303 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2304 return ret; \

2305 } else { \

2306 RETURN\_TYPE ret = \

2307 FUNCNAME##\_fake.custom\_fake\_seq \

2308 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2309 arg0, arg1, arg2); \

2310 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2311 return ret; \

2312 return FUNCNAME##\_fake \

2313 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2314 arg0, arg1, arg2); \

2315 } \

2316 } \

2317 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2318 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2); \

2319 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2320 return ret; \

2321 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2); \

2322 } \

2323 RETURN\_FAKE\_RESULT(FUNCNAME) \

2324 } \

2325 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2326

[ 2327](fff_8h.md#a13274b15d56763d56365c6cb7b36e9b0)#define FAKE\_VALUE\_FUNC3(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE) \

2328 DECLARE\_FAKE\_VALUE\_FUNC3(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE) \

2329 DEFINE\_FAKE\_VALUE\_FUNC3(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE)

2330

[ 2331](fff_8h.md#a1cd827d54f1ce2de5be6bfffa183a42b)#define DECLARE\_FAKE\_VALUE\_FUNC4(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2332 ARG3\_TYPE) \

2333 typedef struct FUNCNAME##\_Fake { \

2334 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2335 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2336 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2337 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

2338 DECLARE\_ALL\_FUNC\_COMMON \

2339 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2340 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2341 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2342 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2343 ARG2\_TYPE, ARG3\_TYPE); \

2344 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

2345 ARG2\_TYPE, ARG3\_TYPE); \

2346 } FUNCNAME##\_Fake; \

2347 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2348 void FUNCNAME##\_reset(void); \

2349 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

2350 ARG2\_TYPE arg2, ARG3\_TYPE arg3);

2351

[ 2352](fff_8h.md#aec251b7082fd92db673c7797d678db1b)#define DEFINE\_FAKE\_VALUE\_FUNC4(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE) \

2353 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2354 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

2355 ARG2\_TYPE arg2, ARG3\_TYPE arg3) \

2356 { \

2357 SAVE\_ARG(FUNCNAME, 0); \

2358 SAVE\_ARG(FUNCNAME, 1); \

2359 SAVE\_ARG(FUNCNAME, 2); \

2360 SAVE\_ARG(FUNCNAME, 3); \

2361 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2362 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2363 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2364 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2365 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

2366 } else { \

2367 HISTORY\_DROPPED(FUNCNAME); \

2368 } \

2369 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2370 REGISTER\_CALL(FUNCNAME); \

2371 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2372 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2373 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2374 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

2375 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2376 arg0, arg1, arg2, arg3); \

2377 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2378 return ret; \

2379 } else { \

2380 RETURN\_TYPE ret = \

2381 FUNCNAME##\_fake.custom\_fake\_seq \

2382 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2383 arg0, arg1, arg2, arg3); \

2384 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2385 return ret; \

2386 return FUNCNAME##\_fake \

2387 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2388 arg0, arg1, arg2, arg3); \

2389 } \

2390 } \

2391 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2392 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3); \

2393 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2394 return ret; \

2395 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3); \

2396 } \

2397 RETURN\_FAKE\_RESULT(FUNCNAME) \

2398 } \

2399 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2400

[ 2401](fff_8h.md#a985a7e10aaad6a1108f5093afb4aad91)#define FAKE\_VALUE\_FUNC4(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE) \

2402 DECLARE\_FAKE\_VALUE\_FUNC4(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2403 ARG3\_TYPE) \

2404 DEFINE\_FAKE\_VALUE\_FUNC4(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE)

2405

[ 2406](fff_8h.md#a4bb680a4fd1ecaafaa4fb52efae21b3a)#define DECLARE\_FAKE\_VALUE\_FUNC5(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2407 ARG3\_TYPE, ARG4\_TYPE) \

2408 typedef struct FUNCNAME##\_Fake { \

2409 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2410 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2411 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2412 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

2413 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

2414 DECLARE\_ALL\_FUNC\_COMMON \

2415 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2416 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2417 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2418 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2419 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE); \

2420 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

2421 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE); \

2422 } FUNCNAME##\_Fake; \

2423 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2424 void FUNCNAME##\_reset(void); \

2425 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2426 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4);

2427

[ 2428](fff_8h.md#a11206579c82b79ffcc5cbc98e874dc88)#define DEFINE\_FAKE\_VALUE\_FUNC5(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2429 ARG4\_TYPE) \

2430 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2431 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2432 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4) \

2433 { \

2434 SAVE\_ARG(FUNCNAME, 0); \

2435 SAVE\_ARG(FUNCNAME, 1); \

2436 SAVE\_ARG(FUNCNAME, 2); \

2437 SAVE\_ARG(FUNCNAME, 3); \

2438 SAVE\_ARG(FUNCNAME, 4); \

2439 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2440 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2441 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2442 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2443 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

2444 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

2445 } else { \

2446 HISTORY\_DROPPED(FUNCNAME); \

2447 } \

2448 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2449 REGISTER\_CALL(FUNCNAME); \

2450 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2451 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2452 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2453 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

2454 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2455 arg0, arg1, arg2, arg3, arg4); \

2456 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2457 return ret; \

2458 } else { \

2459 RETURN\_TYPE ret = \

2460 FUNCNAME##\_fake.custom\_fake\_seq \

2461 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2462 arg0, arg1, arg2, arg3, arg4); \

2463 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2464 return ret; \

2465 return FUNCNAME##\_fake \

2466 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2467 arg0, arg1, arg2, arg3, arg4); \

2468 } \

2469 } \

2470 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2471 RETURN\_TYPE ret = \

2472 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4); \

2473 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2474 return ret; \

2475 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4); \

2476 } \

2477 RETURN\_FAKE\_RESULT(FUNCNAME) \

2478 } \

2479 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2480

[ 2481](fff_8h.md#a005a828cb8cd31d85d9d3974416a12fc)#define FAKE\_VALUE\_FUNC5(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2482 ARG4\_TYPE) \

2483 DECLARE\_FAKE\_VALUE\_FUNC5(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2484 ARG3\_TYPE, ARG4\_TYPE) \

2485 DEFINE\_FAKE\_VALUE\_FUNC5(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2486 ARG4\_TYPE)

2487

[ 2488](fff_8h.md#a5b811ace680aa63e501539244f10249f)#define DECLARE\_FAKE\_VALUE\_FUNC6(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2489 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE) \

2490 typedef struct FUNCNAME##\_Fake { \

2491 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2492 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2493 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2494 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

2495 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

2496 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

2497 DECLARE\_ALL\_FUNC\_COMMON \

2498 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2499 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2500 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2501 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2502 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE); \

2503 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

2504 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE); \

2505 } FUNCNAME##\_Fake; \

2506 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2507 void FUNCNAME##\_reset(void); \

2508 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

2509 ARG2\_TYPE arg2, ARG3\_TYPE arg3, \

2510 ARG4\_TYPE arg4, ARG5\_TYPE arg5);

2511

[ 2512](fff_8h.md#a3cbf5347f876ac0e6c530b0461f88aae)#define DEFINE\_FAKE\_VALUE\_FUNC6(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2513 ARG4\_TYPE, ARG5\_TYPE) \

2514 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2515 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

2516 ARG2\_TYPE arg2, ARG3\_TYPE arg3, \

2517 ARG4\_TYPE arg4, ARG5\_TYPE arg5) \

2518 { \

2519 SAVE\_ARG(FUNCNAME, 0); \

2520 SAVE\_ARG(FUNCNAME, 1); \

2521 SAVE\_ARG(FUNCNAME, 2); \

2522 SAVE\_ARG(FUNCNAME, 3); \

2523 SAVE\_ARG(FUNCNAME, 4); \

2524 SAVE\_ARG(FUNCNAME, 5); \

2525 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2526 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2527 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2528 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2529 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

2530 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

2531 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

2532 } else { \

2533 HISTORY\_DROPPED(FUNCNAME); \

2534 } \

2535 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2536 REGISTER\_CALL(FUNCNAME); \

2537 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2538 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2539 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2540 RETURN\_TYPE ret = \

2541 FUNCNAME##\_fake.custom\_fake\_seq \

2542 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2543 arg0, arg1, arg2, arg3, arg4, arg5); \

2544 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2545 return ret; \

2546 } else { \

2547 RETURN\_TYPE ret = \

2548 FUNCNAME##\_fake.custom\_fake\_seq \

2549 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2550 arg0, arg1, arg2, arg3, arg4, arg5); \

2551 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2552 return ret; \

2553 return FUNCNAME##\_fake \

2554 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2555 arg0, arg1, arg2, arg3, arg4, arg5); \

2556 } \

2557 } \

2558 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2559 RETURN\_TYPE ret = \

2560 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5); \

2561 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2562 return ret; \

2563 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5); \

2564 } \

2565 RETURN\_FAKE\_RESULT(FUNCNAME) \

2566 } \

2567 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2568

[ 2569](fff_8h.md#a1e7329a3880facae95f57016933a1710)#define FAKE\_VALUE\_FUNC6(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2570 ARG4\_TYPE, ARG5\_TYPE) \

2571 DECLARE\_FAKE\_VALUE\_FUNC6(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2572 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE) \

2573 DEFINE\_FAKE\_VALUE\_FUNC6(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2574 ARG4\_TYPE, ARG5\_TYPE)

2575

[ 2576](fff_8h.md#a4dc16c4fa9b91c60d91f4c046934c50d)#define DECLARE\_FAKE\_VALUE\_FUNC7(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2577 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE) \

2578 typedef struct FUNCNAME##\_Fake { \

2579 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2580 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2581 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2582 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

2583 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

2584 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

2585 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

2586 DECLARE\_ALL\_FUNC\_COMMON \

2587 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2588 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2589 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2590 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2591 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

2592 ARG6\_TYPE); \

2593 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

2594 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

2595 ARG6\_TYPE); \

2596 } FUNCNAME##\_Fake; \

2597 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2598 void FUNCNAME##\_reset(void); \

2599 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2600 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

2601 ARG5\_TYPE arg5, ARG6\_TYPE arg6);

2602

[ 2603](fff_8h.md#a35abd788057adafc718bea84e17029eb)#define DEFINE\_FAKE\_VALUE\_FUNC7(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2604 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE) \

2605 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2606 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2607 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

2608 ARG5\_TYPE arg5, ARG6\_TYPE arg6) \

2609 { \

2610 SAVE\_ARG(FUNCNAME, 0); \

2611 SAVE\_ARG(FUNCNAME, 1); \

2612 SAVE\_ARG(FUNCNAME, 2); \

2613 SAVE\_ARG(FUNCNAME, 3); \

2614 SAVE\_ARG(FUNCNAME, 4); \

2615 SAVE\_ARG(FUNCNAME, 5); \

2616 SAVE\_ARG(FUNCNAME, 6); \

2617 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2618 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2619 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2620 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2621 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

2622 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

2623 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

2624 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

2625 } else { \

2626 HISTORY\_DROPPED(FUNCNAME); \

2627 } \

2628 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2629 REGISTER\_CALL(FUNCNAME); \

2630 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2631 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2632 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2633 RETURN\_TYPE ret = \

2634 FUNCNAME##\_fake.custom\_fake\_seq \

2635 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2636 arg0, arg1, arg2, arg3, arg4, arg5, arg6); \

2637 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2638 return ret; \

2639 } else { \

2640 RETURN\_TYPE ret = \

2641 FUNCNAME##\_fake.custom\_fake\_seq \

2642 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2643 arg0, arg1, arg2, arg3, arg4, arg5, arg6); \

2644 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2645 return ret; \

2646 return FUNCNAME##\_fake \

2647 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2648 arg0, arg1, arg2, arg3, arg4, arg5, arg6); \

2649 } \

2650 } \

2651 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2652 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, \

2653 arg4, arg5, arg6); \

2654 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2655 return ret; \

2656 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

2657 arg6); \

2658 } \

2659 RETURN\_FAKE\_RESULT(FUNCNAME) \

2660 } \

2661 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2662

[ 2663](fff_8h.md#a69b1ecedd06e63cb40af937c167562ca)#define FAKE\_VALUE\_FUNC7(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2664 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE) \

2665 DECLARE\_FAKE\_VALUE\_FUNC7(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2666 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE) \

2667 DEFINE\_FAKE\_VALUE\_FUNC7(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2668 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE)

2669

[ 2670](fff_8h.md#a3d565c07339708db8917c4b732c81fed)#define DECLARE\_FAKE\_VALUE\_FUNC8(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2671 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE) \

2672 typedef struct FUNCNAME##\_Fake { \

2673 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2674 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2675 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2676 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

2677 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

2678 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

2679 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

2680 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

2681 DECLARE\_ALL\_FUNC\_COMMON \

2682 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2683 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2684 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2685 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2686 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

2687 ARG6\_TYPE, ARG7\_TYPE); \

2688 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

2689 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

2690 ARG6\_TYPE, ARG7\_TYPE); \

2691 } FUNCNAME##\_Fake; \

2692 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2693 void FUNCNAME##\_reset(void); \

2694 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2695 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

2696 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7);

2697

[ 2698](fff_8h.md#aa714d55175dc73f6058d628bcaa09a6b)#define DEFINE\_FAKE\_VALUE\_FUNC8(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2699 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE) \

2700 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2701 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2702 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

2703 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7) \

2704 { \

2705 SAVE\_ARG(FUNCNAME, 0); \

2706 SAVE\_ARG(FUNCNAME, 1); \

2707 SAVE\_ARG(FUNCNAME, 2); \

2708 SAVE\_ARG(FUNCNAME, 3); \

2709 SAVE\_ARG(FUNCNAME, 4); \

2710 SAVE\_ARG(FUNCNAME, 5); \

2711 SAVE\_ARG(FUNCNAME, 6); \

2712 SAVE\_ARG(FUNCNAME, 7); \

2713 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2714 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2715 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2716 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2717 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

2718 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

2719 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

2720 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

2721 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

2722 } else { \

2723 HISTORY\_DROPPED(FUNCNAME); \

2724 } \

2725 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2726 REGISTER\_CALL(FUNCNAME); \

2727 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2728 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2729 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2730 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

2731 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2732 arg0, arg1, arg2, arg3, arg4, \

2733 arg5, arg6, arg7); \

2734 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2735 return ret; \

2736 } else { \

2737 RETURN\_TYPE ret = \

2738 FUNCNAME##\_fake.custom\_fake\_seq \

2739 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2740 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

2741 arg7); \

2742 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2743 return ret; \

2744 return FUNCNAME##\_fake \

2745 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2746 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7); \

2747 } \

2748 } \

2749 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2750 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, \

2751 arg4, arg5, arg6, arg7); \

2752 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2753 return ret; \

2754 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

2755 arg6, arg7); \

2756 } \

2757 RETURN\_FAKE\_RESULT(FUNCNAME) \

2758 } \

2759 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2760

[ 2761](fff_8h.md#a2c198934771fd04db81577fee5db49e6)#define FAKE\_VALUE\_FUNC8(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2762 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE) \

2763 DECLARE\_FAKE\_VALUE\_FUNC8(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2764 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE) \

2765 DEFINE\_FAKE\_VALUE\_FUNC8(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2766 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE)

2767

[ 2768](fff_8h.md#af107425ea18f1c488feaaf35402cd212)#define DECLARE\_FAKE\_VALUE\_FUNC9(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2769 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE) \

2770 typedef struct FUNCNAME##\_Fake { \

2771 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2772 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2773 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2774 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

2775 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

2776 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

2777 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

2778 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

2779 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

2780 DECLARE\_ALL\_FUNC\_COMMON \

2781 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2782 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2783 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2784 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2785 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

2786 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE); \

2787 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

2788 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

2789 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE); \

2790 } FUNCNAME##\_Fake; \

2791 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2792 void FUNCNAME##\_reset(void); \

2793 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2794 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

2795 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8);

2796

[ 2797](fff_8h.md#a3a28ceda7883c1b0a01e125d7206780f)#define DEFINE\_FAKE\_VALUE\_FUNC9(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2798 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE) \

2799 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2800 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2801 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

2802 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8) \

2803 { \

2804 SAVE\_ARG(FUNCNAME, 0); \

2805 SAVE\_ARG(FUNCNAME, 1); \

2806 SAVE\_ARG(FUNCNAME, 2); \

2807 SAVE\_ARG(FUNCNAME, 3); \

2808 SAVE\_ARG(FUNCNAME, 4); \

2809 SAVE\_ARG(FUNCNAME, 5); \

2810 SAVE\_ARG(FUNCNAME, 6); \

2811 SAVE\_ARG(FUNCNAME, 7); \

2812 SAVE\_ARG(FUNCNAME, 8); \

2813 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2814 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2815 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2816 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2817 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

2818 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

2819 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

2820 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

2821 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

2822 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

2823 } else { \

2824 HISTORY\_DROPPED(FUNCNAME); \

2825 } \

2826 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2827 REGISTER\_CALL(FUNCNAME); \

2828 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2829 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2830 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2831 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

2832 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2833 arg0, arg1, arg2, arg3, arg4, \

2834 arg5, arg6, arg7, arg8); \

2835 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2836 return ret; \

2837 } else { \

2838 RETURN\_TYPE ret = \

2839 FUNCNAME##\_fake.custom\_fake\_seq \

2840 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2841 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

2842 arg7, arg8); \

2843 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2844 return ret; \

2845 return FUNCNAME##\_fake \

2846 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2847 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

2848 arg8); \

2849 } \

2850 } \

2851 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2852 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

2853 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8); \

2854 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2855 return ret; \

2856 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

2857 arg6, arg7, arg8); \

2858 } \

2859 RETURN\_FAKE\_RESULT(FUNCNAME) \

2860 } \

2861 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2862

[ 2863](fff_8h.md#accab85b0ce3cd20c1e101c5e0171189c)#define FAKE\_VALUE\_FUNC9(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2864 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE) \

2865 DECLARE\_FAKE\_VALUE\_FUNC9(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2866 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE) \

2867 DEFINE\_FAKE\_VALUE\_FUNC9(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2868 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE)

2869

[ 2870](fff_8h.md#a8443637605560af0ca45ddd274a72d4f)#define DECLARE\_FAKE\_VALUE\_FUNC10(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2871 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

2872 ARG8\_TYPE, ARG9\_TYPE) \

2873 typedef struct FUNCNAME##\_Fake { \

2874 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2875 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2876 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2877 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

2878 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

2879 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

2880 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

2881 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

2882 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

2883 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

2884 DECLARE\_ALL\_FUNC\_COMMON \

2885 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2886 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2887 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2888 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2889 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

2890 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE); \

2891 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

2892 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

2893 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE); \

2894 } FUNCNAME##\_Fake; \

2895 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

2896 void FUNCNAME##\_reset(void); \

2897 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2898 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

2899 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9);

2900

[ 2901](fff_8h.md#a1c60bac0421fbba415f25a3604391305)#define DEFINE\_FAKE\_VALUE\_FUNC10(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2902 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

2903 ARG9\_TYPE) \

2904 FUNCNAME##\_Fake FUNCNAME##\_fake; \

2905 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

2906 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

2907 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9) \

2908 { \

2909 SAVE\_ARG(FUNCNAME, 0); \

2910 SAVE\_ARG(FUNCNAME, 1); \

2911 SAVE\_ARG(FUNCNAME, 2); \

2912 SAVE\_ARG(FUNCNAME, 3); \

2913 SAVE\_ARG(FUNCNAME, 4); \

2914 SAVE\_ARG(FUNCNAME, 5); \

2915 SAVE\_ARG(FUNCNAME, 6); \

2916 SAVE\_ARG(FUNCNAME, 7); \

2917 SAVE\_ARG(FUNCNAME, 8); \

2918 SAVE\_ARG(FUNCNAME, 9); \

2919 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

2920 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

2921 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

2922 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

2923 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

2924 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

2925 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

2926 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

2927 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

2928 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

2929 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

2930 } else { \

2931 HISTORY\_DROPPED(FUNCNAME); \

2932 } \

2933 INCREMENT\_CALL\_COUNT(FUNCNAME); \

2934 REGISTER\_CALL(FUNCNAME); \

2935 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

2936 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

2937 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

2938 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

2939 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

2940 arg0, arg1, arg2, arg3, arg4, \

2941 arg5, arg6, arg7, arg8, arg9); \

2942 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2943 return ret; \

2944 } else { \

2945 RETURN\_TYPE ret = \

2946 FUNCNAME##\_fake.custom\_fake\_seq \

2947 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2948 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

2949 arg7, arg8, arg9); \

2950 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2951 return ret; \

2952 return FUNCNAME##\_fake \

2953 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

2954 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

2955 arg8, arg9); \

2956 } \

2957 } \

2958 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

2959 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

2960 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9); \

2961 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

2962 return ret; \

2963 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

2964 arg6, arg7, arg8, arg9); \

2965 } \

2966 RETURN\_FAKE\_RESULT(FUNCNAME) \

2967 } \

2968 DEFINE\_RESET\_FUNCTION(FUNCNAME)

2969

[ 2970](fff_8h.md#a239a00463bf260bb1b5fb97c558f643c)#define FAKE\_VALUE\_FUNC10(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

2971 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE) \

2972 DECLARE\_FAKE\_VALUE\_FUNC10(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2973 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

2974 ARG8\_TYPE, ARG9\_TYPE) \

2975 DEFINE\_FAKE\_VALUE\_FUNC10(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2976 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

2977 ARG9\_TYPE)

2978

[ 2979](fff_8h.md#ad5b18b0f43594b9840cd21fbfb1a970e)#define DECLARE\_FAKE\_VALUE\_FUNC11(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

2980 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

2981 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE) \

2982 typedef struct FUNCNAME##\_Fake { \

2983 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

2984 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

2985 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

2986 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

2987 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

2988 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

2989 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

2990 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

2991 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

2992 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

2993 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

2994 DECLARE\_ALL\_FUNC\_COMMON \

2995 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

2996 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

2997 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

2998 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

2999 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3000 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3001 ARG10\_TYPE); \

3002 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

3003 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3004 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3005 ARG10\_TYPE); \

3006 } FUNCNAME##\_Fake; \

3007 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

3008 void FUNCNAME##\_reset(void); \

3009 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3010 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3011 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3012 ARG10\_TYPE arg10);

3013

[ 3014](fff_8h.md#ab34b8e7016523cf44a55eb2365779f1d)#define DEFINE\_FAKE\_VALUE\_FUNC11(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3015 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3016 ARG9\_TYPE, ARG10\_TYPE) \

3017 FUNCNAME##\_Fake FUNCNAME##\_fake; \

3018 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3019 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3020 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3021 ARG10\_TYPE arg10) \

3022 { \

3023 SAVE\_ARG(FUNCNAME, 0); \

3024 SAVE\_ARG(FUNCNAME, 1); \

3025 SAVE\_ARG(FUNCNAME, 2); \

3026 SAVE\_ARG(FUNCNAME, 3); \

3027 SAVE\_ARG(FUNCNAME, 4); \

3028 SAVE\_ARG(FUNCNAME, 5); \

3029 SAVE\_ARG(FUNCNAME, 6); \

3030 SAVE\_ARG(FUNCNAME, 7); \

3031 SAVE\_ARG(FUNCNAME, 8); \

3032 SAVE\_ARG(FUNCNAME, 9); \

3033 SAVE\_ARG(FUNCNAME, 10); \

3034 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

3035 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

3036 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

3037 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

3038 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

3039 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

3040 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

3041 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

3042 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

3043 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

3044 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

3045 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

3046 } else { \

3047 HISTORY\_DROPPED(FUNCNAME); \

3048 } \

3049 INCREMENT\_CALL\_COUNT(FUNCNAME); \

3050 REGISTER\_CALL(FUNCNAME); \

3051 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

3052 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

3053 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

3054 RETURN\_TYPE ret = \

3055 FUNCNAME##\_fake.custom\_fake\_seq \

3056 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

3057 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3058 arg7, arg8, arg9, arg10); \

3059 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3060 return ret; \

3061 } else { \

3062 RETURN\_TYPE ret = \

3063 FUNCNAME##\_fake.custom\_fake\_seq \

3064 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3065 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3066 arg7, arg8, arg9, arg10); \

3067 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3068 return ret; \

3069 return FUNCNAME##\_fake \

3070 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3071 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

3072 arg8, arg9, arg10); \

3073 } \

3074 } \

3075 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

3076 RETURN\_TYPE ret = \

3077 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3078 arg6, arg7, arg8, arg9, arg10); \

3079 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3080 return ret; \

3081 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3082 arg6, arg7, arg8, arg9, arg10); \

3083 } \

3084 RETURN\_FAKE\_RESULT(FUNCNAME) \

3085 } \

3086 DEFINE\_RESET\_FUNCTION(FUNCNAME)

3087

[ 3088](fff_8h.md#aef947c55d333c5d39302f9d7c072068f)#define FAKE\_VALUE\_FUNC11(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

3089 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3090 ARG10\_TYPE) \

3091 DECLARE\_FAKE\_VALUE\_FUNC11(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3092 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3093 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE) \

3094 DEFINE\_FAKE\_VALUE\_FUNC11(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3095 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3096 ARG9\_TYPE, ARG10\_TYPE)

3097

[ 3098](fff_8h.md#af8a62cb713b5aafbdc8151fb0bb3edea)#define DECLARE\_FAKE\_VALUE\_FUNC12(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3099 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3100 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE) \

3101 typedef struct FUNCNAME##\_Fake { \

3102 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

3103 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

3104 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

3105 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

3106 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

3107 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

3108 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

3109 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

3110 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

3111 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

3112 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

3113 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

3114 DECLARE\_ALL\_FUNC\_COMMON \

3115 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

3116 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

3117 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

3118 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

3119 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3120 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3121 ARG10\_TYPE, ARG11\_TYPE); \

3122 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

3123 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3124 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3125 ARG10\_TYPE, ARG11\_TYPE); \

3126 } FUNCNAME##\_Fake; \

3127 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

3128 void FUNCNAME##\_reset(void); \

3129 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3130 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3131 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3132 ARG10\_TYPE arg10, ARG11\_TYPE arg11);

3133

[ 3134](fff_8h.md#a72888ed0fa6e5bf0910b1cae49768987)#define DEFINE\_FAKE\_VALUE\_FUNC12(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3135 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3136 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE) \

3137 FUNCNAME##\_Fake FUNCNAME##\_fake; \

3138 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3139 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3140 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3141 ARG10\_TYPE arg10, ARG11\_TYPE arg11) \

3142 { \

3143 SAVE\_ARG(FUNCNAME, 0); \

3144 SAVE\_ARG(FUNCNAME, 1); \

3145 SAVE\_ARG(FUNCNAME, 2); \

3146 SAVE\_ARG(FUNCNAME, 3); \

3147 SAVE\_ARG(FUNCNAME, 4); \

3148 SAVE\_ARG(FUNCNAME, 5); \

3149 SAVE\_ARG(FUNCNAME, 6); \

3150 SAVE\_ARG(FUNCNAME, 7); \

3151 SAVE\_ARG(FUNCNAME, 8); \

3152 SAVE\_ARG(FUNCNAME, 9); \

3153 SAVE\_ARG(FUNCNAME, 10); \

3154 SAVE\_ARG(FUNCNAME, 11); \

3155 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

3156 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

3157 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

3158 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

3159 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

3160 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

3161 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

3162 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

3163 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

3164 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

3165 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

3166 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

3167 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

3168 } else { \

3169 HISTORY\_DROPPED(FUNCNAME); \

3170 } \

3171 INCREMENT\_CALL\_COUNT(FUNCNAME); \

3172 REGISTER\_CALL(FUNCNAME); \

3173 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

3174 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

3175 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

3176 RETURN\_TYPE ret = \

3177 FUNCNAME##\_fake.custom\_fake\_seq \

3178 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

3179 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3180 arg7, arg8, arg9, arg10, arg11); \

3181 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3182 return ret; \

3183 } else { \

3184 RETURN\_TYPE ret = \

3185 FUNCNAME##\_fake.custom\_fake\_seq \

3186 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3187 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3188 arg7, arg8, arg9, arg10, arg11); \

3189 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3190 return ret; \

3191 return FUNCNAME##\_fake \

3192 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3193 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

3194 arg8, arg9, arg10, arg11); \

3195 } \

3196 } \

3197 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

3198 RETURN\_TYPE ret = \

3199 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3200 arg6, arg7, arg8, arg9, arg10, arg11); \

3201 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3202 return ret; \

3203 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3204 arg6, arg7, arg8, arg9, arg10, arg11); \

3205 } \

3206 RETURN\_FAKE\_RESULT(FUNCNAME) \

3207 } \

3208 DEFINE\_RESET\_FUNCTION(FUNCNAME)

3209

[ 3210](fff_8h.md#ac6b73a2497fc39cfaeb525862c3b6a51)#define FAKE\_VALUE\_FUNC12(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

3211 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3212 ARG10\_TYPE, ARG11\_TYPE) \

3213 DECLARE\_FAKE\_VALUE\_FUNC12(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3214 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3215 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE) \

3216 DEFINE\_FAKE\_VALUE\_FUNC12(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3217 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3218 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE)

3219

[ 3220](fff_8h.md#a838229e3b762996e5b7516058545230e)#define DECLARE\_FAKE\_VALUE\_FUNC13(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3221 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3222 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE) \

3223 typedef struct FUNCNAME##\_Fake { \

3224 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

3225 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

3226 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

3227 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

3228 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

3229 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

3230 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

3231 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

3232 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

3233 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

3234 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

3235 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

3236 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

3237 DECLARE\_ALL\_FUNC\_COMMON \

3238 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

3239 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

3240 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

3241 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

3242 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3243 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3244 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE); \

3245 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

3246 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3247 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3248 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE); \

3249 } FUNCNAME##\_Fake; \

3250 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

3251 void FUNCNAME##\_reset(void); \

3252 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3253 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3254 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3255 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12);

3256

[ 3257](fff_8h.md#ae59a14cae520210e50d6b90206d444c4)#define DEFINE\_FAKE\_VALUE\_FUNC13(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3258 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3259 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE) \

3260 FUNCNAME##\_Fake FUNCNAME##\_fake; \

3261 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3262 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3263 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3264 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12) \

3265 { \

3266 SAVE\_ARG(FUNCNAME, 0); \

3267 SAVE\_ARG(FUNCNAME, 1); \

3268 SAVE\_ARG(FUNCNAME, 2); \

3269 SAVE\_ARG(FUNCNAME, 3); \

3270 SAVE\_ARG(FUNCNAME, 4); \

3271 SAVE\_ARG(FUNCNAME, 5); \

3272 SAVE\_ARG(FUNCNAME, 6); \

3273 SAVE\_ARG(FUNCNAME, 7); \

3274 SAVE\_ARG(FUNCNAME, 8); \

3275 SAVE\_ARG(FUNCNAME, 9); \

3276 SAVE\_ARG(FUNCNAME, 10); \

3277 SAVE\_ARG(FUNCNAME, 11); \

3278 SAVE\_ARG(FUNCNAME, 12); \

3279 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

3280 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

3281 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

3282 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

3283 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

3284 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

3285 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

3286 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

3287 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

3288 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

3289 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

3290 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

3291 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

3292 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

3293 } else { \

3294 HISTORY\_DROPPED(FUNCNAME); \

3295 } \

3296 INCREMENT\_CALL\_COUNT(FUNCNAME); \

3297 REGISTER\_CALL(FUNCNAME); \

3298 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

3299 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

3300 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

3301 RETURN\_TYPE ret = \

3302 FUNCNAME##\_fake.custom\_fake\_seq \

3303 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

3304 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3305 arg7, arg8, arg9, arg10, arg11, arg12); \

3306 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3307 return ret; \

3308 } else { \

3309 RETURN\_TYPE ret = \

3310 FUNCNAME##\_fake.custom\_fake\_seq \

3311 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3312 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3313 arg7, arg8, arg9, arg10, arg11, arg12); \

3314 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3315 return ret; \

3316 return FUNCNAME##\_fake \

3317 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3318 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

3319 arg8, arg9, arg10, arg11, arg12); \

3320 } \

3321 } \

3322 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

3323 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

3324 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

3325 arg11, arg12); \

3326 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3327 return ret; \

3328 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3329 arg6, arg7, arg8, arg9, arg10, arg11, \

3330 arg12); \

3331 } \

3332 RETURN\_FAKE\_RESULT(FUNCNAME) \

3333 } \

3334 DEFINE\_RESET\_FUNCTION(FUNCNAME)

3335

[ 3336](fff_8h.md#ae56328e2d79d4a552ff00291c8ba67b1)#define FAKE\_VALUE\_FUNC13(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

3337 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3338 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE) \

3339 DECLARE\_FAKE\_VALUE\_FUNC13(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3340 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3341 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE) \

3342 DEFINE\_FAKE\_VALUE\_FUNC13(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3343 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3344 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE)

3345

[ 3346](fff_8h.md#affd0ac22309e028e7cdd40f1a1bab0fe)#define DECLARE\_FAKE\_VALUE\_FUNC14(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3347 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3348 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3349 ARG13\_TYPE) \

3350 typedef struct FUNCNAME##\_Fake { \

3351 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

3352 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

3353 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

3354 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

3355 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

3356 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

3357 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

3358 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

3359 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

3360 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

3361 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

3362 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

3363 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

3364 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

3365 DECLARE\_ALL\_FUNC\_COMMON \

3366 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

3367 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

3368 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

3369 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

3370 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3371 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3372 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE); \

3373 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

3374 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3375 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3376 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE); \

3377 } FUNCNAME##\_Fake; \

3378 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

3379 void FUNCNAME##\_reset(void); \

3380 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3381 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3382 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3383 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13);

3384

[ 3385](fff_8h.md#a9af2e1b3c9cb76cae085c40600b2b42d)#define DEFINE\_FAKE\_VALUE\_FUNC14(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3386 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3387 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE) \

3388 FUNCNAME##\_Fake FUNCNAME##\_fake; \

3389 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3390 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3391 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3392 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13) \

3393 { \

3394 SAVE\_ARG(FUNCNAME, 0); \

3395 SAVE\_ARG(FUNCNAME, 1); \

3396 SAVE\_ARG(FUNCNAME, 2); \

3397 SAVE\_ARG(FUNCNAME, 3); \

3398 SAVE\_ARG(FUNCNAME, 4); \

3399 SAVE\_ARG(FUNCNAME, 5); \

3400 SAVE\_ARG(FUNCNAME, 6); \

3401 SAVE\_ARG(FUNCNAME, 7); \

3402 SAVE\_ARG(FUNCNAME, 8); \

3403 SAVE\_ARG(FUNCNAME, 9); \

3404 SAVE\_ARG(FUNCNAME, 10); \

3405 SAVE\_ARG(FUNCNAME, 11); \

3406 SAVE\_ARG(FUNCNAME, 12); \

3407 SAVE\_ARG(FUNCNAME, 13); \

3408 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

3409 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

3410 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

3411 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

3412 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

3413 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

3414 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

3415 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

3416 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

3417 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

3418 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

3419 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

3420 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

3421 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

3422 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

3423 } else { \

3424 HISTORY\_DROPPED(FUNCNAME); \

3425 } \

3426 INCREMENT\_CALL\_COUNT(FUNCNAME); \

3427 REGISTER\_CALL(FUNCNAME); \

3428 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

3429 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

3430 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

3431 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

3432 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

3433 arg0, arg1, arg2, arg3, arg4, \

3434 arg5, arg6, arg7, arg8, arg9, \

3435 arg10, arg11, arg12, arg13); \

3436 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3437 return ret; \

3438 } else { \

3439 RETURN\_TYPE ret = \

3440 FUNCNAME##\_fake.custom\_fake\_seq \

3441 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3442 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3443 arg7, arg8, arg9, arg10, arg11, arg12, \

3444 arg13); \

3445 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3446 return ret; \

3447 return FUNCNAME##\_fake \

3448 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3449 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

3450 arg8, arg9, arg10, arg11, arg12, arg13); \

3451 } \

3452 } \

3453 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

3454 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

3455 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

3456 arg11, arg12, arg13); \

3457 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3458 return ret; \

3459 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3460 arg6, arg7, arg8, arg9, arg10, arg11, \

3461 arg12, arg13); \

3462 } \

3463 RETURN\_FAKE\_RESULT(FUNCNAME) \

3464 } \

3465 DEFINE\_RESET\_FUNCTION(FUNCNAME)

3466

[ 3467](fff_8h.md#afa8ee1479fb614e8500e3c839bf28074)#define FAKE\_VALUE\_FUNC14(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

3468 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3469 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE) \

3470 DECLARE\_FAKE\_VALUE\_FUNC14(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3471 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3472 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3473 ARG13\_TYPE) \

3474 DEFINE\_FAKE\_VALUE\_FUNC14(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3475 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3476 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE)

3477

[ 3478](fff_8h.md#a659eb5ac371eeb6d7df92f2854be4d74)#define DECLARE\_FAKE\_VALUE\_FUNC15(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3479 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3480 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3481 ARG13\_TYPE, ARG14\_TYPE) \

3482 typedef struct FUNCNAME##\_Fake { \

3483 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

3484 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

3485 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

3486 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

3487 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

3488 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

3489 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

3490 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

3491 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

3492 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

3493 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

3494 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

3495 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

3496 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

3497 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

3498 DECLARE\_ALL\_FUNC\_COMMON \

3499 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

3500 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

3501 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

3502 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

3503 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3504 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3505 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3506 ARG14\_TYPE); \

3507 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

3508 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3509 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3510 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3511 ARG14\_TYPE); \

3512 } FUNCNAME##\_Fake; \

3513 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

3514 void FUNCNAME##\_reset(void); \

3515 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3516 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3517 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3518 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

3519 ARG14\_TYPE arg14);

3520

[ 3521](fff_8h.md#a979de81c768223e742fa2b7799a2ab15)#define DEFINE\_FAKE\_VALUE\_FUNC15(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3522 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3523 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3524 ARG14\_TYPE) \

3525 FUNCNAME##\_Fake FUNCNAME##\_fake; \

3526 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3527 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3528 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3529 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

3530 ARG14\_TYPE arg14) \

3531 { \

3532 SAVE\_ARG(FUNCNAME, 0); \

3533 SAVE\_ARG(FUNCNAME, 1); \

3534 SAVE\_ARG(FUNCNAME, 2); \

3535 SAVE\_ARG(FUNCNAME, 3); \

3536 SAVE\_ARG(FUNCNAME, 4); \

3537 SAVE\_ARG(FUNCNAME, 5); \

3538 SAVE\_ARG(FUNCNAME, 6); \

3539 SAVE\_ARG(FUNCNAME, 7); \

3540 SAVE\_ARG(FUNCNAME, 8); \

3541 SAVE\_ARG(FUNCNAME, 9); \

3542 SAVE\_ARG(FUNCNAME, 10); \

3543 SAVE\_ARG(FUNCNAME, 11); \

3544 SAVE\_ARG(FUNCNAME, 12); \

3545 SAVE\_ARG(FUNCNAME, 13); \

3546 SAVE\_ARG(FUNCNAME, 14); \

3547 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

3548 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

3549 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

3550 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

3551 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

3552 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

3553 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

3554 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

3555 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

3556 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

3557 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

3558 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

3559 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

3560 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

3561 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

3562 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

3563 } else { \

3564 HISTORY\_DROPPED(FUNCNAME); \

3565 } \

3566 INCREMENT\_CALL\_COUNT(FUNCNAME); \

3567 REGISTER\_CALL(FUNCNAME); \

3568 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

3569 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

3570 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

3571 RETURN\_TYPE ret = \

3572 FUNCNAME##\_fake.custom\_fake\_seq \

3573 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

3574 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3575 arg7, arg8, arg9, arg10, arg11, arg12, \

3576 arg13, arg14); \

3577 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3578 return ret; \

3579 } else { \

3580 RETURN\_TYPE ret = \

3581 FUNCNAME##\_fake.custom\_fake\_seq \

3582 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3583 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3584 arg7, arg8, arg9, arg10, arg11, arg12, \

3585 arg13, arg14); \

3586 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3587 return ret; \

3588 return FUNCNAME##\_fake \

3589 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3590 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

3591 arg8, arg9, arg10, arg11, arg12, arg13, arg14); \

3592 } \

3593 } \

3594 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

3595 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

3596 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

3597 arg11, arg12, arg13, arg14); \

3598 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3599 return ret; \

3600 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3601 arg6, arg7, arg8, arg9, arg10, arg11, \

3602 arg12, arg13, arg14); \

3603 } \

3604 RETURN\_FAKE\_RESULT(FUNCNAME) \

3605 } \

3606 DEFINE\_RESET\_FUNCTION(FUNCNAME)

3607

[ 3608](fff_8h.md#a8e21a45a081f9ceec7873894044f0ed2)#define FAKE\_VALUE\_FUNC15(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

3609 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3610 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE) \

3611 DECLARE\_FAKE\_VALUE\_FUNC15(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3612 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3613 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3614 ARG13\_TYPE, ARG14\_TYPE) \

3615 DEFINE\_FAKE\_VALUE\_FUNC15(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3616 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3617 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3618 ARG14\_TYPE)

3619

[ 3620](fff_8h.md#a2de8127bd0723cf0fbb1fb6816ba87ca)#define DECLARE\_FAKE\_VALUE\_FUNC16(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3621 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3622 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3623 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE) \

3624 typedef struct FUNCNAME##\_Fake { \

3625 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

3626 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

3627 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

3628 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

3629 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

3630 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

3631 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

3632 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

3633 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

3634 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

3635 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

3636 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

3637 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

3638 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

3639 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

3640 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

3641 DECLARE\_ALL\_FUNC\_COMMON \

3642 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

3643 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

3644 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

3645 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

3646 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3647 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3648 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3649 ARG14\_TYPE, ARG15\_TYPE); \

3650 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

3651 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3652 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3653 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3654 ARG14\_TYPE, ARG15\_TYPE); \

3655 } FUNCNAME##\_Fake; \

3656 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

3657 void FUNCNAME##\_reset(void); \

3658 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3659 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3660 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3661 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

3662 ARG14\_TYPE arg14, ARG15\_TYPE arg15);

3663

[ 3664](fff_8h.md#aa02c71c3a8dd95ad081f41166e6f5906)#define DEFINE\_FAKE\_VALUE\_FUNC16(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3665 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3666 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3667 ARG14\_TYPE, ARG15\_TYPE) \

3668 FUNCNAME##\_Fake FUNCNAME##\_fake; \

3669 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3670 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3671 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3672 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

3673 ARG14\_TYPE arg14, ARG15\_TYPE arg15) \

3674 { \

3675 SAVE\_ARG(FUNCNAME, 0); \

3676 SAVE\_ARG(FUNCNAME, 1); \

3677 SAVE\_ARG(FUNCNAME, 2); \

3678 SAVE\_ARG(FUNCNAME, 3); \

3679 SAVE\_ARG(FUNCNAME, 4); \

3680 SAVE\_ARG(FUNCNAME, 5); \

3681 SAVE\_ARG(FUNCNAME, 6); \

3682 SAVE\_ARG(FUNCNAME, 7); \

3683 SAVE\_ARG(FUNCNAME, 8); \

3684 SAVE\_ARG(FUNCNAME, 9); \

3685 SAVE\_ARG(FUNCNAME, 10); \

3686 SAVE\_ARG(FUNCNAME, 11); \

3687 SAVE\_ARG(FUNCNAME, 12); \

3688 SAVE\_ARG(FUNCNAME, 13); \

3689 SAVE\_ARG(FUNCNAME, 14); \

3690 SAVE\_ARG(FUNCNAME, 15); \

3691 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

3692 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

3693 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

3694 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

3695 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

3696 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

3697 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

3698 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

3699 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

3700 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

3701 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

3702 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

3703 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

3704 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

3705 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

3706 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

3707 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

3708 } else { \

3709 HISTORY\_DROPPED(FUNCNAME); \

3710 } \

3711 INCREMENT\_CALL\_COUNT(FUNCNAME); \

3712 REGISTER\_CALL(FUNCNAME); \

3713 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

3714 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

3715 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

3716 RETURN\_TYPE ret = \

3717 FUNCNAME##\_fake.custom\_fake\_seq \

3718 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

3719 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3720 arg7, arg8, arg9, arg10, arg11, arg12, \

3721 arg13, arg14, arg15); \

3722 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3723 return ret; \

3724 } else { \

3725 RETURN\_TYPE ret = \

3726 FUNCNAME##\_fake.custom\_fake\_seq \

3727 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3728 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3729 arg7, arg8, arg9, arg10, arg11, arg12, \

3730 arg13, arg14, arg15); \

3731 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3732 return ret; \

3733 return FUNCNAME##\_fake \

3734 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3735 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

3736 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

3737 arg15); \

3738 } \

3739 } \

3740 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

3741 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

3742 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

3743 arg11, arg12, arg13, arg14, arg15); \

3744 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3745 return ret; \

3746 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3747 arg6, arg7, arg8, arg9, arg10, arg11, \

3748 arg12, arg13, arg14, arg15); \

3749 } \

3750 RETURN\_FAKE\_RESULT(FUNCNAME) \

3751 } \

3752 DEFINE\_RESET\_FUNCTION(FUNCNAME)

3753

[ 3754](fff_8h.md#a9d52c41a6e49a04b8cb12fa7d06bbef9)#define FAKE\_VALUE\_FUNC16(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

3755 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3756 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE) \

3757 DECLARE\_FAKE\_VALUE\_FUNC16(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3758 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3759 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3760 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE) \

3761 DEFINE\_FAKE\_VALUE\_FUNC16(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3762 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3763 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3764 ARG14\_TYPE, ARG15\_TYPE)

3765

[ 3766](fff_8h.md#a62fa4be4928d28fe06a7fecc24e7d2c8)#define DECLARE\_FAKE\_VALUE\_FUNC17(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3767 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3768 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3769 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE) \

3770 typedef struct FUNCNAME##\_Fake { \

3771 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

3772 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

3773 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

3774 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

3775 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

3776 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

3777 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

3778 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

3779 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

3780 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

3781 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

3782 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

3783 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

3784 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

3785 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

3786 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

3787 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

3788 DECLARE\_ALL\_FUNC\_COMMON \

3789 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

3790 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

3791 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

3792 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

3793 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3794 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3795 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3796 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE); \

3797 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

3798 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3799 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3800 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3801 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE); \

3802 } FUNCNAME##\_Fake; \

3803 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

3804 void FUNCNAME##\_reset(void); \

3805 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3806 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3807 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3808 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

3809 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16);

3810

[ 3811](fff_8h.md#a9ad367d0db0e3a0bc64aed8375e2970d)#define DEFINE\_FAKE\_VALUE\_FUNC17(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3812 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3813 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3814 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE) \

3815 FUNCNAME##\_Fake FUNCNAME##\_fake; \

3816 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3817 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3818 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3819 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

3820 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16) \

3821 { \

3822 SAVE\_ARG(FUNCNAME, 0); \

3823 SAVE\_ARG(FUNCNAME, 1); \

3824 SAVE\_ARG(FUNCNAME, 2); \

3825 SAVE\_ARG(FUNCNAME, 3); \

3826 SAVE\_ARG(FUNCNAME, 4); \

3827 SAVE\_ARG(FUNCNAME, 5); \

3828 SAVE\_ARG(FUNCNAME, 6); \

3829 SAVE\_ARG(FUNCNAME, 7); \

3830 SAVE\_ARG(FUNCNAME, 8); \

3831 SAVE\_ARG(FUNCNAME, 9); \

3832 SAVE\_ARG(FUNCNAME, 10); \

3833 SAVE\_ARG(FUNCNAME, 11); \

3834 SAVE\_ARG(FUNCNAME, 12); \

3835 SAVE\_ARG(FUNCNAME, 13); \

3836 SAVE\_ARG(FUNCNAME, 14); \

3837 SAVE\_ARG(FUNCNAME, 15); \

3838 SAVE\_ARG(FUNCNAME, 16); \

3839 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

3840 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

3841 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

3842 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

3843 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

3844 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

3845 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

3846 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

3847 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

3848 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

3849 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

3850 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

3851 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

3852 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

3853 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

3854 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

3855 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

3856 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

3857 } else { \

3858 HISTORY\_DROPPED(FUNCNAME); \

3859 } \

3860 INCREMENT\_CALL\_COUNT(FUNCNAME); \

3861 REGISTER\_CALL(FUNCNAME); \

3862 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

3863 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

3864 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

3865 RETURN\_TYPE ret = \

3866 FUNCNAME##\_fake.custom\_fake\_seq \

3867 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

3868 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3869 arg7, arg8, arg9, arg10, arg11, arg12, \

3870 arg13, arg14, arg15, arg16); \

3871 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3872 return ret; \

3873 } else { \

3874 RETURN\_TYPE ret = \

3875 FUNCNAME##\_fake.custom\_fake\_seq \

3876 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3877 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

3878 arg7, arg8, arg9, arg10, arg11, arg12, \

3879 arg13, arg14, arg15, arg16); \

3880 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3881 return ret; \

3882 return FUNCNAME##\_fake \

3883 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

3884 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

3885 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

3886 arg15, arg16); \

3887 } \

3888 } \

3889 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

3890 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

3891 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

3892 arg11, arg12, arg13, arg14, arg15, arg16); \

3893 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

3894 return ret; \

3895 return FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

3896 arg6, arg7, arg8, arg9, arg10, arg11, \

3897 arg12, arg13, arg14, arg15, arg16); \

3898 } \

3899 RETURN\_FAKE\_RESULT(FUNCNAME) \

3900 } \

3901 DEFINE\_RESET\_FUNCTION(FUNCNAME)

3902

[ 3903](fff_8h.md#ac82e6c8cdd519f7847589ad50fa9c6a2)#define FAKE\_VALUE\_FUNC17(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

3904 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3905 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

3906 ARG16\_TYPE) \

3907 DECLARE\_FAKE\_VALUE\_FUNC17(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3908 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3909 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3910 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE) \

3911 DEFINE\_FAKE\_VALUE\_FUNC17(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3912 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3913 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3914 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE)

3915

[ 3916](fff_8h.md#a6180641e8d1a481c7f7c651976120f5d)#define DECLARE\_FAKE\_VALUE\_FUNC18(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3917 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

3918 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

3919 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE) \

3920 typedef struct FUNCNAME##\_Fake { \

3921 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

3922 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

3923 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

3924 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

3925 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

3926 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

3927 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

3928 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

3929 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

3930 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

3931 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

3932 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

3933 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

3934 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

3935 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

3936 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

3937 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

3938 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

3939 DECLARE\_ALL\_FUNC\_COMMON \

3940 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

3941 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

3942 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

3943 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

3944 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3945 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3946 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3947 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE); \

3948 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

3949 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

3950 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

3951 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3952 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE); \

3953 } FUNCNAME##\_Fake; \

3954 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

3955 void FUNCNAME##\_reset(void); \

3956 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3957 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3958 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3959 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

3960 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17);

3961

[ 3962](fff_8h.md#a01c76aa6a209e2d81058cafcecb8fe20)#define DEFINE\_FAKE\_VALUE\_FUNC18(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

3963 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

3964 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

3965 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE) \

3966 FUNCNAME##\_Fake FUNCNAME##\_fake; \

3967 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

3968 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

3969 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

3970 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

3971 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17) \

3972 { \

3973 SAVE\_ARG(FUNCNAME, 0); \

3974 SAVE\_ARG(FUNCNAME, 1); \

3975 SAVE\_ARG(FUNCNAME, 2); \

3976 SAVE\_ARG(FUNCNAME, 3); \

3977 SAVE\_ARG(FUNCNAME, 4); \

3978 SAVE\_ARG(FUNCNAME, 5); \

3979 SAVE\_ARG(FUNCNAME, 6); \

3980 SAVE\_ARG(FUNCNAME, 7); \

3981 SAVE\_ARG(FUNCNAME, 8); \

3982 SAVE\_ARG(FUNCNAME, 9); \

3983 SAVE\_ARG(FUNCNAME, 10); \

3984 SAVE\_ARG(FUNCNAME, 11); \

3985 SAVE\_ARG(FUNCNAME, 12); \

3986 SAVE\_ARG(FUNCNAME, 13); \

3987 SAVE\_ARG(FUNCNAME, 14); \

3988 SAVE\_ARG(FUNCNAME, 15); \

3989 SAVE\_ARG(FUNCNAME, 16); \

3990 SAVE\_ARG(FUNCNAME, 17); \

3991 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

3992 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

3993 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

3994 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

3995 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

3996 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

3997 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

3998 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

3999 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

4000 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

4001 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

4002 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

4003 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

4004 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

4005 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

4006 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

4007 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

4008 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

4009 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

4010 } else { \

4011 HISTORY\_DROPPED(FUNCNAME); \

4012 } \

4013 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4014 REGISTER\_CALL(FUNCNAME); \

4015 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4016 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4017 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4018 RETURN\_TYPE ret = \

4019 FUNCNAME##\_fake.custom\_fake\_seq \

4020 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4021 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

4022 arg7, arg8, arg9, arg10, arg11, arg12, \

4023 arg13, arg14, arg15, arg16, arg17); \

4024 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4025 return ret; \

4026 } else { \

4027 RETURN\_TYPE ret = \

4028 FUNCNAME##\_fake.custom\_fake\_seq \

4029 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4030 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

4031 arg7, arg8, arg9, arg10, arg11, arg12, \

4032 arg13, arg14, arg15, arg16, arg17); \

4033 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4034 return ret; \

4035 return FUNCNAME##\_fake \

4036 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4037 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

4038 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

4039 arg15, arg16, arg17); \

4040 } \

4041 } \

4042 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

4043 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

4044 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

4045 arg11, arg12, arg13, arg14, arg15, arg16, arg17); \

4046 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4047 return ret; \

4048 return FUNCNAME##\_fake.custom\_fake( \

4049 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

4050 arg11, arg12, arg13, arg14, arg15, arg16, arg17); \

4051 } \

4052 RETURN\_FAKE\_RESULT(FUNCNAME) \

4053 } \

4054 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4055

[ 4056](fff_8h.md#a1700f2f44a151442dde87ee04a6daeb0)#define FAKE\_VALUE\_FUNC18(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4057 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

4058 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

4059 ARG16\_TYPE, ARG17\_TYPE) \

4060 DECLARE\_FAKE\_VALUE\_FUNC18(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4061 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

4062 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

4063 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE) \

4064 DEFINE\_FAKE\_VALUE\_FUNC18(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4065 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

4066 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

4067 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE)

4068

[ 4069](fff_8h.md#a7b693395304ea68930b75cafc7e58703)#define DECLARE\_FAKE\_VALUE\_FUNC19( \

4070 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4071 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

4072 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE) \

4073 typedef struct FUNCNAME##\_Fake { \

4074 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4075 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4076 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4077 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

4078 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

4079 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

4080 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

4081 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

4082 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

4083 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

4084 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

4085 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

4086 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

4087 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

4088 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

4089 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

4090 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

4091 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

4092 DECLARE\_ARG(ARG18\_TYPE, 18, FUNCNAME) \

4093 DECLARE\_ALL\_FUNC\_COMMON \

4094 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

4095 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

4096 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4097 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

4098 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4099 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

4100 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

4101 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

4102 ARG18\_TYPE); \

4103 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4104 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4105 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

4106 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

4107 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

4108 ARG18\_TYPE); \

4109 } FUNCNAME##\_Fake; \

4110 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4111 void FUNCNAME##\_reset(void); \

4112 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

4113 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

4114 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

4115 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

4116 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

4117 ARG18\_TYPE arg18);

4118

[ 4119](fff_8h.md#ac4ce594cdfe81ee690a15efd2695ef8a)#define DEFINE\_FAKE\_VALUE\_FUNC19(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4120 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

4121 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

4122 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE) \

4123 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4124 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

4125 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

4126 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

4127 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

4128 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

4129 ARG18\_TYPE arg18) \

4130 { \

4131 SAVE\_ARG(FUNCNAME, 0); \

4132 SAVE\_ARG(FUNCNAME, 1); \

4133 SAVE\_ARG(FUNCNAME, 2); \

4134 SAVE\_ARG(FUNCNAME, 3); \

4135 SAVE\_ARG(FUNCNAME, 4); \

4136 SAVE\_ARG(FUNCNAME, 5); \

4137 SAVE\_ARG(FUNCNAME, 6); \

4138 SAVE\_ARG(FUNCNAME, 7); \

4139 SAVE\_ARG(FUNCNAME, 8); \

4140 SAVE\_ARG(FUNCNAME, 9); \

4141 SAVE\_ARG(FUNCNAME, 10); \

4142 SAVE\_ARG(FUNCNAME, 11); \

4143 SAVE\_ARG(FUNCNAME, 12); \

4144 SAVE\_ARG(FUNCNAME, 13); \

4145 SAVE\_ARG(FUNCNAME, 14); \

4146 SAVE\_ARG(FUNCNAME, 15); \

4147 SAVE\_ARG(FUNCNAME, 16); \

4148 SAVE\_ARG(FUNCNAME, 17); \

4149 SAVE\_ARG(FUNCNAME, 18); \

4150 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4151 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4152 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4153 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

4154 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

4155 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

4156 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

4157 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

4158 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

4159 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

4160 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

4161 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

4162 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

4163 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

4164 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

4165 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

4166 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

4167 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

4168 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

4169 SAVE\_ARG\_HISTORY(FUNCNAME, 18); \

4170 } else { \

4171 HISTORY\_DROPPED(FUNCNAME); \

4172 } \

4173 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4174 REGISTER\_CALL(FUNCNAME); \

4175 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4176 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4177 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4178 RETURN\_TYPE ret = \

4179 FUNCNAME##\_fake.custom\_fake\_seq \

4180 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4181 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

4182 arg7, arg8, arg9, arg10, arg11, arg12, \

4183 arg13, arg14, arg15, arg16, arg17, arg18); \

4184 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4185 return ret; \

4186 } else { \

4187 RETURN\_TYPE ret = \

4188 FUNCNAME##\_fake.custom\_fake\_seq \

4189 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4190 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

4191 arg7, arg8, arg9, arg10, arg11, arg12, \

4192 arg13, arg14, arg15, arg16, arg17, arg18); \

4193 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4194 return ret; \

4195 return FUNCNAME##\_fake \

4196 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4197 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

4198 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

4199 arg15, arg16, arg17, arg18); \

4200 } \

4201 } \

4202 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

4203 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

4204 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

4205 arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18); \

4206 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4207 return ret; \

4208 return FUNCNAME##\_fake.custom\_fake( \

4209 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

4210 arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18); \

4211 } \

4212 RETURN\_FAKE\_RESULT(FUNCNAME) \

4213 } \

4214 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4215

[ 4216](fff_8h.md#a081325395551ad3c3133db73f1a5ab88)#define FAKE\_VALUE\_FUNC19(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4217 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

4218 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

4219 ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE) \

4220 DECLARE\_FAKE\_VALUE\_FUNC19(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4221 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

4222 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

4223 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

4224 ARG18\_TYPE) \

4225 DEFINE\_FAKE\_VALUE\_FUNC19(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4226 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

4227 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

4228 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE)

4229

[ 4230](fff_8h.md#a3cbe4d374201ecaf7738808aa7c7ee47)#define DECLARE\_FAKE\_VALUE\_FUNC20( \

4231 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4232 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

4233 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ARG19\_TYPE) \

4234 typedef struct FUNCNAME##\_Fake { \

4235 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4236 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4237 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4238 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

4239 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

4240 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

4241 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

4242 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

4243 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

4244 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

4245 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

4246 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

4247 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

4248 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

4249 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

4250 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

4251 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

4252 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

4253 DECLARE\_ARG(ARG18\_TYPE, 18, FUNCNAME) \

4254 DECLARE\_ARG(ARG19\_TYPE, 19, FUNCNAME) \

4255 DECLARE\_ALL\_FUNC\_COMMON \

4256 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

4257 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

4258 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4259 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

4260 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4261 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

4262 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

4263 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

4264 ARG18\_TYPE, ARG19\_TYPE); \

4265 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4266 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4267 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

4268 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

4269 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

4270 ARG18\_TYPE, ARG19\_TYPE); \

4271 } FUNCNAME##\_Fake; \

4272 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4273 void FUNCNAME##\_reset(void); \

4274 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

4275 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

4276 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

4277 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

4278 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

4279 ARG18\_TYPE arg18, ARG19\_TYPE arg19);

4280

[ 4281](fff_8h.md#a084f14c44539895dee0f18232dd74981)#define DEFINE\_FAKE\_VALUE\_FUNC20( \

4282 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4283 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

4284 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ARG19\_TYPE) \

4285 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4286 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

4287 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

4288 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

4289 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

4290 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

4291 ARG18\_TYPE arg18, ARG19\_TYPE arg19) \

4292 { \

4293 SAVE\_ARG(FUNCNAME, 0); \

4294 SAVE\_ARG(FUNCNAME, 1); \

4295 SAVE\_ARG(FUNCNAME, 2); \

4296 SAVE\_ARG(FUNCNAME, 3); \

4297 SAVE\_ARG(FUNCNAME, 4); \

4298 SAVE\_ARG(FUNCNAME, 5); \

4299 SAVE\_ARG(FUNCNAME, 6); \

4300 SAVE\_ARG(FUNCNAME, 7); \

4301 SAVE\_ARG(FUNCNAME, 8); \

4302 SAVE\_ARG(FUNCNAME, 9); \

4303 SAVE\_ARG(FUNCNAME, 10); \

4304 SAVE\_ARG(FUNCNAME, 11); \

4305 SAVE\_ARG(FUNCNAME, 12); \

4306 SAVE\_ARG(FUNCNAME, 13); \

4307 SAVE\_ARG(FUNCNAME, 14); \

4308 SAVE\_ARG(FUNCNAME, 15); \

4309 SAVE\_ARG(FUNCNAME, 16); \

4310 SAVE\_ARG(FUNCNAME, 17); \

4311 SAVE\_ARG(FUNCNAME, 18); \

4312 SAVE\_ARG(FUNCNAME, 19); \

4313 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4314 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4315 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4316 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

4317 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

4318 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

4319 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

4320 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

4321 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

4322 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

4323 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

4324 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

4325 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

4326 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

4327 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

4328 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

4329 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

4330 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

4331 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

4332 SAVE\_ARG\_HISTORY(FUNCNAME, 18); \

4333 SAVE\_ARG\_HISTORY(FUNCNAME, 19); \

4334 } else { \

4335 HISTORY\_DROPPED(FUNCNAME); \

4336 } \

4337 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4338 REGISTER\_CALL(FUNCNAME); \

4339 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4340 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4341 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4342 RETURN\_TYPE ret = \

4343 FUNCNAME##\_fake.custom\_fake\_seq \

4344 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4345 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

4346 arg7, arg8, arg9, arg10, arg11, arg12, \

4347 arg13, arg14, arg15, arg16, arg17, arg18, \

4348 arg19); \

4349 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4350 return ret; \

4351 } else { \

4352 RETURN\_TYPE ret = \

4353 FUNCNAME##\_fake.custom\_fake\_seq \

4354 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4355 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

4356 arg7, arg8, arg9, arg10, arg11, arg12, \

4357 arg13, arg14, arg15, arg16, arg17, arg18, \

4358 arg19); \

4359 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4360 return ret; \

4361 return FUNCNAME##\_fake \

4362 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4363 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

4364 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

4365 arg15, arg16, arg17, arg18, arg19); \

4366 } \

4367 } \

4368 if (FUNCNAME##\_fake.custom\_fake != NULL) { \

4369 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake( \

4370 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

4371 arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19); \

4372 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

4373 return ret; \

4374 return FUNCNAME##\_fake.custom\_fake( \

4375 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

4376 arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19); \

4377 } \

4378 RETURN\_FAKE\_RESULT(FUNCNAME) \

4379 } \

4380 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4381

[ 4382](fff_8h.md#a524f904609e4e167e91843c72a3a581a)#define FAKE\_VALUE\_FUNC20(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4383 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

4384 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

4385 ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ARG19\_TYPE) \

4386 DECLARE\_FAKE\_VALUE\_FUNC20(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4387 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

4388 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

4389 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

4390 ARG18\_TYPE, ARG19\_TYPE) \

4391 DEFINE\_FAKE\_VALUE\_FUNC20(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4392 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

4393 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

4394 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, \

4395 ARG19\_TYPE)

4396

[ 4397](fff_8h.md#a19ae03da4f0f7453b71c238fc1ed6e18)#define DECLARE\_FAKE\_VOID\_FUNC2\_VARARG(FUNCNAME, ARG0\_TYPE, ...) \

4398 typedef struct FUNCNAME##\_Fake { \

4399 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4400 DECLARE\_ALL\_FUNC\_COMMON \

4401 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4402 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, va\_list ap); \

4403 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, va\_list ap); \

4404 } FUNCNAME##\_Fake; \

4405 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4406 void FUNCNAME##\_reset(void); \

4407 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ...);

4408

[ 4409](fff_8h.md#a15c1de982a410806500750616f9ea8dd)#define DEFINE\_FAKE\_VOID\_FUNC2\_VARARG(FUNCNAME, ARG0\_TYPE, ...) \

4410 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4411 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ...) \

4412 { \

4413 SAVE\_ARG(FUNCNAME, 0); \

4414 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4415 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4416 } else { \

4417 HISTORY\_DROPPED(FUNCNAME); \

4418 } \

4419 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4420 REGISTER\_CALL(FUNCNAME); \

4421 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4422 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4423 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4424 va\_list ap; \

4425 va\_start(ap, arg0); \

4426 FUNCNAME##\_fake \

4427 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4428 arg0, ap); \

4429 va\_end(ap); \

4430 } else { \

4431 va\_list ap; \

4432 va\_start(ap, arg0); \

4433 FUNCNAME##\_fake \

4434 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4435 arg0, ap); \

4436 va\_end(ap); \

4437 } \

4438 } \

4439 if (FUNCNAME##\_fake.custom\_fake) { \

4440 va\_list ap; \

4441 va\_start(ap, arg0); \

4442 FUNCNAME##\_fake.custom\_fake(arg0, ap); \

4443 va\_end(ap); \

4444 } \

4445 } \

4446 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4447

[ 4448](fff_8h.md#af7f77072c7be0d90c2819103fd3d807b)#define FAKE\_VOID\_FUNC2\_VARARG(FUNCNAME, ARG0\_TYPE, ...) \

4449 DECLARE\_FAKE\_VOID\_FUNC2\_VARARG(FUNCNAME, ARG0\_TYPE, ...) \

4450 DEFINE\_FAKE\_VOID\_FUNC2\_VARARG(FUNCNAME, ARG0\_TYPE, ...)

4451

[ 4452](fff_8h.md#a74f04ff5a88ae9280a5557e8eaf06956)#define DECLARE\_FAKE\_VOID\_FUNC3\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...) \

4453 typedef struct FUNCNAME##\_Fake { \

4454 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4455 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4456 DECLARE\_ALL\_FUNC\_COMMON \

4457 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4458 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, va\_list ap); \

4459 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4460 va\_list ap); \

4461 } FUNCNAME##\_Fake; \

4462 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4463 void FUNCNAME##\_reset(void); \

4464 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ...);

4465

[ 4466](fff_8h.md#a469bd42c340d8af32b306c66e6ec01bd)#define DEFINE\_FAKE\_VOID\_FUNC3\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...) \

4467 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4468 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ...) \

4469 { \

4470 SAVE\_ARG(FUNCNAME, 0); \

4471 SAVE\_ARG(FUNCNAME, 1); \

4472 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4473 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4474 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4475 } else { \

4476 HISTORY\_DROPPED(FUNCNAME); \

4477 } \

4478 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4479 REGISTER\_CALL(FUNCNAME); \

4480 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4481 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4482 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4483 va\_list ap; \

4484 va\_start(ap, arg1); \

4485 FUNCNAME##\_fake \

4486 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4487 arg0, arg1, ap); \

4488 va\_end(ap); \

4489 } else { \

4490 va\_list ap; \

4491 va\_start(ap, arg1); \

4492 FUNCNAME##\_fake \

4493 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4494 arg0, arg1, ap); \

4495 va\_end(ap); \

4496 } \

4497 } \

4498 if (FUNCNAME##\_fake.custom\_fake) { \

4499 va\_list ap; \

4500 va\_start(ap, arg1); \

4501 FUNCNAME##\_fake.custom\_fake(arg0, arg1, ap); \

4502 va\_end(ap); \

4503 } \

4504 } \

4505 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4506

[ 4507](fff_8h.md#a8325ad081f3c2e59fc1ade6afc555d26)#define FAKE\_VOID\_FUNC3\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...) \

4508 DECLARE\_FAKE\_VOID\_FUNC3\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...) \

4509 DEFINE\_FAKE\_VOID\_FUNC3\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...)

4510

[ 4511](fff_8h.md#a0faaccd964dc084ede95d4b630619e98)#define DECLARE\_FAKE\_VOID\_FUNC4\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ...) \

4512 typedef struct FUNCNAME##\_Fake { \

4513 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4514 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4515 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4516 DECLARE\_ALL\_FUNC\_COMMON \

4517 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4518 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4519 va\_list ap); \

4520 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4521 ARG2\_TYPE, va\_list ap); \

4522 } FUNCNAME##\_Fake; \

4523 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4524 void FUNCNAME##\_reset(void); \

4525 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4526 ...);

4527

[ 4528](fff_8h.md#a767025172bf445ca5977f3db6d10398d)#define DEFINE\_FAKE\_VOID\_FUNC4\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ...) \

4529 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4530 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4531 ...) \

4532 { \

4533 SAVE\_ARG(FUNCNAME, 0); \

4534 SAVE\_ARG(FUNCNAME, 1); \

4535 SAVE\_ARG(FUNCNAME, 2); \

4536 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4537 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4538 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4539 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

4540 } else { \

4541 HISTORY\_DROPPED(FUNCNAME); \

4542 } \

4543 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4544 REGISTER\_CALL(FUNCNAME); \

4545 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4546 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4547 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4548 va\_list ap; \

4549 va\_start(ap, arg2); \

4550 FUNCNAME##\_fake \

4551 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4552 arg0, arg1, arg2, ap); \

4553 va\_end(ap); \

4554 } else { \

4555 va\_list ap; \

4556 va\_start(ap, arg2); \

4557 FUNCNAME##\_fake \

4558 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4559 arg0, arg1, arg2, ap); \

4560 va\_end(ap); \

4561 } \

4562 } \

4563 if (FUNCNAME##\_fake.custom\_fake) { \

4564 va\_list ap; \

4565 va\_start(ap, arg2); \

4566 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, ap); \

4567 va\_end(ap); \

4568 } \

4569 } \

4570 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4571

[ 4572](fff_8h.md#a00db07fb43beba1c4f8406e3077c91dd)#define FAKE\_VOID\_FUNC4\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ...) \

4573 DECLARE\_FAKE\_VOID\_FUNC4\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ...) \

4574 DEFINE\_FAKE\_VOID\_FUNC4\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ...)

4575

[ 4576](fff_8h.md#a0295797c2f161be4295e5eaf8e48fead)#define DECLARE\_FAKE\_VOID\_FUNC5\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ...) \

4577 typedef struct FUNCNAME##\_Fake { \

4578 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4579 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4580 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4581 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

4582 DECLARE\_ALL\_FUNC\_COMMON \

4583 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4584 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4585 ARG3\_TYPE, va\_list ap); \

4586 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4587 ARG2\_TYPE, ARG3\_TYPE, va\_list ap); \

4588 } FUNCNAME##\_Fake; \

4589 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4590 void FUNCNAME##\_reset(void); \

4591 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4592 ARG3\_TYPE arg3, ...);

4593

[ 4594](fff_8h.md#a0513cedb6dcde38b1f9692aa9b4de027)#define DEFINE\_FAKE\_VOID\_FUNC5\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ...) \

4595 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4596 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4597 ARG3\_TYPE arg3, ...) \

4598 { \

4599 SAVE\_ARG(FUNCNAME, 0); \

4600 SAVE\_ARG(FUNCNAME, 1); \

4601 SAVE\_ARG(FUNCNAME, 2); \

4602 SAVE\_ARG(FUNCNAME, 3); \

4603 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4604 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4605 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4606 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

4607 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

4608 } else { \

4609 HISTORY\_DROPPED(FUNCNAME); \

4610 } \

4611 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4612 REGISTER\_CALL(FUNCNAME); \

4613 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4614 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4615 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4616 va\_list ap; \

4617 va\_start(ap, arg3); \

4618 FUNCNAME##\_fake \

4619 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4620 arg0, arg1, arg2, arg3, ap); \

4621 va\_end(ap); \

4622 } else { \

4623 va\_list ap; \

4624 va\_start(ap, arg3); \

4625 FUNCNAME##\_fake \

4626 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4627 arg0, arg1, arg2, arg3, ap); \

4628 va\_end(ap); \

4629 } \

4630 } \

4631 if (FUNCNAME##\_fake.custom\_fake) { \

4632 va\_list ap; \

4633 va\_start(ap, arg3); \

4634 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, ap); \

4635 va\_end(ap); \

4636 } \

4637 } \

4638 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4639

[ 4640](fff_8h.md#a3dabcc2b94546b6ab4e803d7d5563a3c)#define FAKE\_VOID\_FUNC5\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ...) \

4641 DECLARE\_FAKE\_VOID\_FUNC5\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ...) \

4642 DEFINE\_FAKE\_VOID\_FUNC5\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ...)

4643

[ 4644](fff_8h.md#a5155152335e8ef321799d608133a9ec0)#define DECLARE\_FAKE\_VOID\_FUNC6\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4645 ARG4\_TYPE, ...) \

4646 typedef struct FUNCNAME##\_Fake { \

4647 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4648 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4649 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4650 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

4651 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

4652 DECLARE\_ALL\_FUNC\_COMMON \

4653 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4654 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4655 ARG3\_TYPE, ARG4\_TYPE, va\_list ap); \

4656 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4657 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, va\_list ap); \

4658 } FUNCNAME##\_Fake; \

4659 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4660 void FUNCNAME##\_reset(void); \

4661 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4662 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ...);

4663

[ 4664](fff_8h.md#a7ee9ea8f7a8795f8db2bbeb59637cd24)#define DEFINE\_FAKE\_VOID\_FUNC6\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4665 ARG4\_TYPE, ...) \

4666 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4667 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4668 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ...) \

4669 { \

4670 SAVE\_ARG(FUNCNAME, 0); \

4671 SAVE\_ARG(FUNCNAME, 1); \

4672 SAVE\_ARG(FUNCNAME, 2); \

4673 SAVE\_ARG(FUNCNAME, 3); \

4674 SAVE\_ARG(FUNCNAME, 4); \

4675 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4676 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4677 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4678 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

4679 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

4680 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

4681 } else { \

4682 HISTORY\_DROPPED(FUNCNAME); \

4683 } \

4684 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4685 REGISTER\_CALL(FUNCNAME); \

4686 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4687 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4688 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4689 va\_list ap; \

4690 va\_start(ap, arg4); \

4691 FUNCNAME##\_fake \

4692 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4693 arg0, arg1, arg2, arg3, arg4, ap); \

4694 va\_end(ap); \

4695 } else { \

4696 va\_list ap; \

4697 va\_start(ap, arg4); \

4698 FUNCNAME##\_fake \

4699 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4700 arg0, arg1, arg2, arg3, arg4, ap); \

4701 va\_end(ap); \

4702 } \

4703 } \

4704 if (FUNCNAME##\_fake.custom\_fake) { \

4705 va\_list ap; \

4706 va\_start(ap, arg4); \

4707 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, ap); \

4708 va\_end(ap); \

4709 } \

4710 } \

4711 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4712

[ 4713](fff_8h.md#a8e6b3fac4903049fceb6b2cb4ed68d4b)#define FAKE\_VOID\_FUNC6\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

4714 ...) \

4715 DECLARE\_FAKE\_VOID\_FUNC6\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4716 ARG4\_TYPE, ...) \

4717 DEFINE\_FAKE\_VOID\_FUNC6\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4718 ARG4\_TYPE, ...)

4719

[ 4720](fff_8h.md#a6922359f1cc8afcc6cea212c255fc3b2)#define DECLARE\_FAKE\_VOID\_FUNC7\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4721 ARG4\_TYPE, ARG5\_TYPE, ...) \

4722 typedef struct FUNCNAME##\_Fake { \

4723 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4724 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4725 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4726 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

4727 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

4728 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

4729 DECLARE\_ALL\_FUNC\_COMMON \

4730 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4731 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4732 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, va\_list ap); \

4733 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4734 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4735 va\_list ap); \

4736 } FUNCNAME##\_Fake; \

4737 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4738 void FUNCNAME##\_reset(void); \

4739 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4740 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

4741 ...);

4742

[ 4743](fff_8h.md#ab5658d6d0f1ee8b3150db490a22eae70)#define DEFINE\_FAKE\_VOID\_FUNC7\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4744 ARG4\_TYPE, ARG5\_TYPE, ...) \

4745 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4746 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4747 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

4748 ...) \

4749 { \

4750 SAVE\_ARG(FUNCNAME, 0); \

4751 SAVE\_ARG(FUNCNAME, 1); \

4752 SAVE\_ARG(FUNCNAME, 2); \

4753 SAVE\_ARG(FUNCNAME, 3); \

4754 SAVE\_ARG(FUNCNAME, 4); \

4755 SAVE\_ARG(FUNCNAME, 5); \

4756 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4757 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4758 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4759 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

4760 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

4761 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

4762 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

4763 } else { \

4764 HISTORY\_DROPPED(FUNCNAME); \

4765 } \

4766 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4767 REGISTER\_CALL(FUNCNAME); \

4768 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4769 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4770 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4771 va\_list ap; \

4772 va\_start(ap, arg5); \

4773 FUNCNAME##\_fake \

4774 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4775 arg0, arg1, arg2, arg3, arg4, arg5, ap); \

4776 va\_end(ap); \

4777 } else { \

4778 va\_list ap; \

4779 va\_start(ap, arg5); \

4780 FUNCNAME##\_fake \

4781 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4782 arg0, arg1, arg2, arg3, arg4, arg5, ap); \

4783 va\_end(ap); \

4784 } \

4785 } \

4786 if (FUNCNAME##\_fake.custom\_fake) { \

4787 va\_list ap; \

4788 va\_start(ap, arg5); \

4789 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, ap); \

4790 va\_end(ap); \

4791 } \

4792 } \

4793 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4794

[ 4795](fff_8h.md#a359f5c6c11491ebefeaef39af46f7dbe)#define FAKE\_VOID\_FUNC7\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

4796 ARG5\_TYPE, ...) \

4797 DECLARE\_FAKE\_VOID\_FUNC7\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4798 ARG4\_TYPE, ARG5\_TYPE, ...) \

4799 DEFINE\_FAKE\_VOID\_FUNC7\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4800 ARG4\_TYPE, ARG5\_TYPE, ...)

4801

[ 4802](fff_8h.md#aa091b8821f8fea722d584d7ba2382737)#define DECLARE\_FAKE\_VOID\_FUNC8\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4803 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...) \

4804 typedef struct FUNCNAME##\_Fake { \

4805 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4806 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4807 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4808 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

4809 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

4810 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

4811 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

4812 DECLARE\_ALL\_FUNC\_COMMON \

4813 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4814 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4815 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

4816 va\_list ap); \

4817 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4818 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4819 ARG6\_TYPE, va\_list ap); \

4820 } FUNCNAME##\_Fake; \

4821 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4822 void FUNCNAME##\_reset(void); \

4823 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4824 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

4825 ARG6\_TYPE arg6, ...);

4826

[ 4827](fff_8h.md#a342eb638211e1ff580d3f963452573a8)#define DEFINE\_FAKE\_VOID\_FUNC8\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4828 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...) \

4829 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4830 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4831 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

4832 ARG6\_TYPE arg6, ...) \

4833 { \

4834 SAVE\_ARG(FUNCNAME, 0); \

4835 SAVE\_ARG(FUNCNAME, 1); \

4836 SAVE\_ARG(FUNCNAME, 2); \

4837 SAVE\_ARG(FUNCNAME, 3); \

4838 SAVE\_ARG(FUNCNAME, 4); \

4839 SAVE\_ARG(FUNCNAME, 5); \

4840 SAVE\_ARG(FUNCNAME, 6); \

4841 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4842 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4843 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4844 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

4845 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

4846 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

4847 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

4848 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

4849 } else { \

4850 HISTORY\_DROPPED(FUNCNAME); \

4851 } \

4852 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4853 REGISTER\_CALL(FUNCNAME); \

4854 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4855 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4856 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4857 va\_list ap; \

4858 va\_start(ap, arg6); \

4859 FUNCNAME##\_fake \

4860 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4861 arg0, arg1, arg2, arg3, arg4, arg5, arg6, ap); \

4862 va\_end(ap); \

4863 } else { \

4864 va\_list ap; \

4865 va\_start(ap, arg6); \

4866 FUNCNAME##\_fake \

4867 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4868 arg0, arg1, arg2, arg3, arg4, arg5, arg6, ap); \

4869 va\_end(ap); \

4870 } \

4871 } \

4872 if (FUNCNAME##\_fake.custom\_fake) { \

4873 va\_list ap; \

4874 va\_start(ap, arg6); \

4875 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, ap); \

4876 va\_end(ap); \

4877 } \

4878 } \

4879 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4880

[ 4881](fff_8h.md#a80d814e30b71b255bd895159a48255a2)#define FAKE\_VOID\_FUNC8\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

4882 ARG5\_TYPE, ARG6\_TYPE, ...) \

4883 DECLARE\_FAKE\_VOID\_FUNC8\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4884 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...) \

4885 DEFINE\_FAKE\_VOID\_FUNC8\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4886 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...)

4887

[ 4888](fff_8h.md#ae9e0bac974f2896447a43a9ab172b32d)#define DECLARE\_FAKE\_VOID\_FUNC9\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4889 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ...) \

4890 typedef struct FUNCNAME##\_Fake { \

4891 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4892 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4893 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4894 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

4895 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

4896 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

4897 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

4898 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

4899 DECLARE\_ALL\_FUNC\_COMMON \

4900 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4901 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4902 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

4903 ARG7\_TYPE, va\_list ap); \

4904 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4905 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

4906 ARG6\_TYPE, ARG7\_TYPE, va\_list ap); \

4907 } FUNCNAME##\_Fake; \

4908 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

4909 void FUNCNAME##\_reset(void); \

4910 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4911 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

4912 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ...);

4913

[ 4914](fff_8h.md#a5e75d183e638913ff04557e731fcf26b)#define DEFINE\_FAKE\_VOID\_FUNC9\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4915 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ...) \

4916 FUNCNAME##\_Fake FUNCNAME##\_fake; \

4917 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

4918 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

4919 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ...) \

4920 { \

4921 SAVE\_ARG(FUNCNAME, 0); \

4922 SAVE\_ARG(FUNCNAME, 1); \

4923 SAVE\_ARG(FUNCNAME, 2); \

4924 SAVE\_ARG(FUNCNAME, 3); \

4925 SAVE\_ARG(FUNCNAME, 4); \

4926 SAVE\_ARG(FUNCNAME, 5); \

4927 SAVE\_ARG(FUNCNAME, 6); \

4928 SAVE\_ARG(FUNCNAME, 7); \

4929 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

4930 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

4931 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

4932 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

4933 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

4934 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

4935 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

4936 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

4937 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

4938 } else { \

4939 HISTORY\_DROPPED(FUNCNAME); \

4940 } \

4941 INCREMENT\_CALL\_COUNT(FUNCNAME); \

4942 REGISTER\_CALL(FUNCNAME); \

4943 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

4944 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

4945 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

4946 va\_list ap; \

4947 va\_start(ap, arg7); \

4948 FUNCNAME##\_fake \

4949 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

4950 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

4951 ap); \

4952 va\_end(ap); \

4953 } else { \

4954 va\_list ap; \

4955 va\_start(ap, arg7); \

4956 FUNCNAME##\_fake \

4957 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

4958 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

4959 ap); \

4960 va\_end(ap); \

4961 } \

4962 } \

4963 if (FUNCNAME##\_fake.custom\_fake) { \

4964 va\_list ap; \

4965 va\_start(ap, arg7); \

4966 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

4967 arg7, ap); \

4968 va\_end(ap); \

4969 } \

4970 } \

4971 DEFINE\_RESET\_FUNCTION(FUNCNAME)

4972

[ 4973](fff_8h.md#ae70833e8db4f25117882ba0a66edb8e9)#define FAKE\_VOID\_FUNC9\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

4974 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ...) \

4975 DECLARE\_FAKE\_VOID\_FUNC9\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4976 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ...) \

4977 DEFINE\_FAKE\_VOID\_FUNC9\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4978 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ...)

4979

[ 4980](fff_8h.md#acd01ba98ea01b3a46ebacfa6b17b3ab1)#define DECLARE\_FAKE\_VOID\_FUNC10\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

4981 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

4982 ...) \

4983 typedef struct FUNCNAME##\_Fake { \

4984 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

4985 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

4986 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

4987 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

4988 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

4989 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

4990 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

4991 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

4992 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

4993 DECLARE\_ALL\_FUNC\_COMMON \

4994 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

4995 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

4996 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

4997 ARG7\_TYPE, ARG8\_TYPE, va\_list ap); \

4998 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

4999 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5000 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, va\_list ap); \

5001 } FUNCNAME##\_Fake; \

5002 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5003 void FUNCNAME##\_reset(void); \

5004 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5005 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5006 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ...);

5007

[ 5008](fff_8h.md#a7e421d2bbb8ed172c70cf03445253fc7)#define DEFINE\_FAKE\_VOID\_FUNC10\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5009 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ...) \

5010 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5011 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5012 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5013 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ...) \

5014 { \

5015 SAVE\_ARG(FUNCNAME, 0); \

5016 SAVE\_ARG(FUNCNAME, 1); \

5017 SAVE\_ARG(FUNCNAME, 2); \

5018 SAVE\_ARG(FUNCNAME, 3); \

5019 SAVE\_ARG(FUNCNAME, 4); \

5020 SAVE\_ARG(FUNCNAME, 5); \

5021 SAVE\_ARG(FUNCNAME, 6); \

5022 SAVE\_ARG(FUNCNAME, 7); \

5023 SAVE\_ARG(FUNCNAME, 8); \

5024 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5025 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5026 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5027 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5028 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5029 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5030 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5031 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5032 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5033 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5034 } else { \

5035 HISTORY\_DROPPED(FUNCNAME); \

5036 } \

5037 INCREMENT\_CALL\_COUNT(FUNCNAME); \

5038 REGISTER\_CALL(FUNCNAME); \

5039 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

5040 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

5041 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

5042 va\_list ap; \

5043 va\_start(ap, arg8); \

5044 FUNCNAME##\_fake \

5045 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

5046 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5047 arg8, ap); \

5048 va\_end(ap); \

5049 } else { \

5050 va\_list ap; \

5051 va\_start(ap, arg8); \

5052 FUNCNAME##\_fake \

5053 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

5054 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5055 arg8, ap); \

5056 va\_end(ap); \

5057 } \

5058 } \

5059 if (FUNCNAME##\_fake.custom\_fake) { \

5060 va\_list ap; \

5061 va\_start(ap, arg8); \

5062 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

5063 arg7, arg8, ap); \

5064 va\_end(ap); \

5065 } \

5066 } \

5067 DEFINE\_RESET\_FUNCTION(FUNCNAME)

5068

[ 5069](fff_8h.md#a32a2c4da519c9f138ca9aedb12f50837)#define FAKE\_VOID\_FUNC10\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

5070 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ...) \

5071 DECLARE\_FAKE\_VOID\_FUNC10\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5072 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5073 ...) \

5074 DEFINE\_FAKE\_VOID\_FUNC10\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5075 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ...)

5076

[ 5077](fff_8h.md#a0108da8b62bb8dca9ea8bfe2c57a3631)#define DECLARE\_FAKE\_VOID\_FUNC11\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5078 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5079 ARG9\_TYPE, ...) \

5080 typedef struct FUNCNAME##\_Fake { \

5081 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

5082 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

5083 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

5084 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

5085 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

5086 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

5087 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

5088 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

5089 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

5090 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

5091 DECLARE\_ALL\_FUNC\_COMMON \

5092 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

5093 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

5094 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5095 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, va\_list ap); \

5096 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

5097 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5098 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

5099 va\_list ap); \

5100 } FUNCNAME##\_Fake; \

5101 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5102 void FUNCNAME##\_reset(void); \

5103 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

5104 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

5105 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, \

5106 ARG9\_TYPE arg9, ...);

5107

[ 5108](fff_8h.md#a83ead1c05b6a39ba2fd12fb2893eaa77)#define DEFINE\_FAKE\_VOID\_FUNC11\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5109 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5110 ARG9\_TYPE, ...) \

5111 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5112 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

5113 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

5114 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, \

5115 ARG9\_TYPE arg9, ...) \

5116 { \

5117 SAVE\_ARG(FUNCNAME, 0); \

5118 SAVE\_ARG(FUNCNAME, 1); \

5119 SAVE\_ARG(FUNCNAME, 2); \

5120 SAVE\_ARG(FUNCNAME, 3); \

5121 SAVE\_ARG(FUNCNAME, 4); \

5122 SAVE\_ARG(FUNCNAME, 5); \

5123 SAVE\_ARG(FUNCNAME, 6); \

5124 SAVE\_ARG(FUNCNAME, 7); \

5125 SAVE\_ARG(FUNCNAME, 8); \

5126 SAVE\_ARG(FUNCNAME, 9); \

5127 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5128 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5129 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5130 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5131 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5132 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5133 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5134 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5135 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5136 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5137 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

5138 } else { \

5139 HISTORY\_DROPPED(FUNCNAME); \

5140 } \

5141 INCREMENT\_CALL\_COUNT(FUNCNAME); \

5142 REGISTER\_CALL(FUNCNAME); \

5143 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

5144 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

5145 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

5146 va\_list ap; \

5147 va\_start(ap, arg9); \

5148 FUNCNAME##\_fake \

5149 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

5150 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5151 arg8, arg9, ap); \

5152 va\_end(ap); \

5153 } else { \

5154 va\_list ap; \

5155 va\_start(ap, arg9); \

5156 FUNCNAME##\_fake \

5157 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

5158 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5159 arg8, arg9, ap); \

5160 va\_end(ap); \

5161 } \

5162 } \

5163 if (FUNCNAME##\_fake.custom\_fake) { \

5164 va\_list ap; \

5165 va\_start(ap, arg9); \

5166 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

5167 arg7, arg8, arg9, ap); \

5168 va\_end(ap); \

5169 } \

5170 } \

5171 DEFINE\_RESET\_FUNCTION(FUNCNAME)

5172

[ 5173](fff_8h.md#a9a91dc87e93a7756e0a44acbb6b93835)#define FAKE\_VOID\_FUNC11\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

5174 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ...) \

5175 DECLARE\_FAKE\_VOID\_FUNC11\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5176 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5177 ARG9\_TYPE, ...) \

5178 DEFINE\_FAKE\_VOID\_FUNC11\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5179 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5180 ARG9\_TYPE, ...)

5181

[ 5182](fff_8h.md#ae3d2d1e0dea556432f4a1e82e30d108c)#define DECLARE\_FAKE\_VOID\_FUNC12\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5183 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5184 ARG9\_TYPE, ARG10\_TYPE, ...) \

5185 typedef struct FUNCNAME##\_Fake { \

5186 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

5187 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

5188 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

5189 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

5190 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

5191 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

5192 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

5193 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

5194 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

5195 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

5196 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

5197 DECLARE\_ALL\_FUNC\_COMMON \

5198 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

5199 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

5200 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5201 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5202 va\_list ap); \

5203 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

5204 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5205 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

5206 ARG10\_TYPE, va\_list ap); \

5207 } FUNCNAME##\_Fake; \

5208 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5209 void FUNCNAME##\_reset(void); \

5210 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

5211 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

5212 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, \

5213 ARG9\_TYPE arg9, ARG10\_TYPE arg10, ...);

5214

[ 5215](fff_8h.md#a4b79f0ab13a914081a3db2f8b315a06d)#define DEFINE\_FAKE\_VOID\_FUNC12\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5216 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5217 ARG9\_TYPE, ARG10\_TYPE, ...) \

5218 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5219 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, \

5220 ARG3\_TYPE arg3, ARG4\_TYPE arg4, ARG5\_TYPE arg5, \

5221 ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, \

5222 ARG9\_TYPE arg9, ARG10\_TYPE arg10, ...) \

5223 { \

5224 SAVE\_ARG(FUNCNAME, 0); \

5225 SAVE\_ARG(FUNCNAME, 1); \

5226 SAVE\_ARG(FUNCNAME, 2); \

5227 SAVE\_ARG(FUNCNAME, 3); \

5228 SAVE\_ARG(FUNCNAME, 4); \

5229 SAVE\_ARG(FUNCNAME, 5); \

5230 SAVE\_ARG(FUNCNAME, 6); \

5231 SAVE\_ARG(FUNCNAME, 7); \

5232 SAVE\_ARG(FUNCNAME, 8); \

5233 SAVE\_ARG(FUNCNAME, 9); \

5234 SAVE\_ARG(FUNCNAME, 10); \

5235 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5236 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5237 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5238 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5239 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5240 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5241 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5242 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5243 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5244 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5245 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

5246 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

5247 } else { \

5248 HISTORY\_DROPPED(FUNCNAME); \

5249 } \

5250 INCREMENT\_CALL\_COUNT(FUNCNAME); \

5251 REGISTER\_CALL(FUNCNAME); \

5252 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

5253 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

5254 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

5255 va\_list ap; \

5256 va\_start(ap, arg10); \

5257 FUNCNAME##\_fake \

5258 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

5259 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5260 arg8, arg9, arg10, ap); \

5261 va\_end(ap); \

5262 } else { \

5263 va\_list ap; \

5264 va\_start(ap, arg10); \

5265 FUNCNAME##\_fake \

5266 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

5267 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5268 arg8, arg9, arg10, ap); \

5269 va\_end(ap); \

5270 } \

5271 } \

5272 if (FUNCNAME##\_fake.custom\_fake) { \

5273 va\_list ap; \

5274 va\_start(ap, arg10); \

5275 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

5276 arg7, arg8, arg9, arg10, ap); \

5277 va\_end(ap); \

5278 } \

5279 } \

5280 DEFINE\_RESET\_FUNCTION(FUNCNAME)

5281

[ 5282](fff_8h.md#a2c0248635fbf5aca41a40e51b35c34f2)#define FAKE\_VOID\_FUNC12\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

5283 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5284 ...) \

5285 DECLARE\_FAKE\_VOID\_FUNC12\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5286 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5287 ARG9\_TYPE, ARG10\_TYPE, ...) \

5288 DEFINE\_FAKE\_VOID\_FUNC12\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5289 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5290 ARG9\_TYPE, ARG10\_TYPE, ...)

5291

[ 5292](fff_8h.md#ad1d8dc0189d40c026e69a9b8b8e2a2d4)#define DECLARE\_FAKE\_VOID\_FUNC13\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5293 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5294 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...) \

5295 typedef struct FUNCNAME##\_Fake { \

5296 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

5297 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

5298 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

5299 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

5300 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

5301 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

5302 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

5303 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

5304 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

5305 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

5306 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

5307 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

5308 DECLARE\_ALL\_FUNC\_COMMON \

5309 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

5310 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

5311 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5312 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5313 ARG11\_TYPE, va\_list ap); \

5314 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

5315 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5316 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

5317 ARG10\_TYPE, ARG11\_TYPE, va\_list ap); \

5318 } FUNCNAME##\_Fake; \

5319 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5320 void FUNCNAME##\_reset(void); \

5321 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5322 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5323 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5324 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ...);

5325

[ 5326](fff_8h.md#a328ff349ea79804e3f35f5d62b8349d7)#define DEFINE\_FAKE\_VOID\_FUNC13\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5327 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5328 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...) \

5329 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5330 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5331 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5332 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5333 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ...) \

5334 { \

5335 SAVE\_ARG(FUNCNAME, 0); \

5336 SAVE\_ARG(FUNCNAME, 1); \

5337 SAVE\_ARG(FUNCNAME, 2); \

5338 SAVE\_ARG(FUNCNAME, 3); \

5339 SAVE\_ARG(FUNCNAME, 4); \

5340 SAVE\_ARG(FUNCNAME, 5); \

5341 SAVE\_ARG(FUNCNAME, 6); \

5342 SAVE\_ARG(FUNCNAME, 7); \

5343 SAVE\_ARG(FUNCNAME, 8); \

5344 SAVE\_ARG(FUNCNAME, 9); \

5345 SAVE\_ARG(FUNCNAME, 10); \

5346 SAVE\_ARG(FUNCNAME, 11); \

5347 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5348 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5349 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5350 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5351 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5352 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5353 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5354 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5355 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5356 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5357 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

5358 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

5359 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

5360 } else { \

5361 HISTORY\_DROPPED(FUNCNAME); \

5362 } \

5363 INCREMENT\_CALL\_COUNT(FUNCNAME); \

5364 REGISTER\_CALL(FUNCNAME); \

5365 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

5366 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

5367 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

5368 va\_list ap; \

5369 va\_start(ap, arg11); \

5370 FUNCNAME##\_fake \

5371 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

5372 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5373 arg8, arg9, arg10, arg11, ap); \

5374 va\_end(ap); \

5375 } else { \

5376 va\_list ap; \

5377 va\_start(ap, arg11); \

5378 FUNCNAME##\_fake \

5379 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

5380 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5381 arg8, arg9, arg10, arg11, ap); \

5382 va\_end(ap); \

5383 } \

5384 } \

5385 if (FUNCNAME##\_fake.custom\_fake) { \

5386 va\_list ap; \

5387 va\_start(ap, arg11); \

5388 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

5389 arg7, arg8, arg9, arg10, arg11, ap); \

5390 va\_end(ap); \

5391 } \

5392 } \

5393 DEFINE\_RESET\_FUNCTION(FUNCNAME)

5394

[ 5395](fff_8h.md#a415fd0c4e4108c5fa4688a925a8997a6)#define FAKE\_VOID\_FUNC13\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

5396 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5397 ARG11\_TYPE, ...) \

5398 DECLARE\_FAKE\_VOID\_FUNC13\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5399 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5400 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...) \

5401 DEFINE\_FAKE\_VOID\_FUNC13\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5402 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5403 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...)

5404

[ 5405](fff_8h.md#a657787bee781a1b29af84f4a6dae3ca1)#define DECLARE\_FAKE\_VOID\_FUNC14\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5406 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5407 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ...) \

5408 typedef struct FUNCNAME##\_Fake { \

5409 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

5410 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

5411 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

5412 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

5413 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

5414 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

5415 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

5416 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

5417 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

5418 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

5419 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

5420 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

5421 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

5422 DECLARE\_ALL\_FUNC\_COMMON \

5423 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

5424 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

5425 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5426 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5427 ARG11\_TYPE, ARG12\_TYPE, va\_list ap); \

5428 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

5429 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5430 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

5431 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, va\_list ap); \

5432 } FUNCNAME##\_Fake; \

5433 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5434 void FUNCNAME##\_reset(void); \

5435 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5436 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5437 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5438 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ...);

5439

[ 5440](fff_8h.md#a94c42d0d6ab50320b5b84754bbb8e6c5)#define DEFINE\_FAKE\_VOID\_FUNC14\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5441 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5442 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ...) \

5443 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5444 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5445 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5446 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5447 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ...) \

5448 { \

5449 SAVE\_ARG(FUNCNAME, 0); \

5450 SAVE\_ARG(FUNCNAME, 1); \

5451 SAVE\_ARG(FUNCNAME, 2); \

5452 SAVE\_ARG(FUNCNAME, 3); \

5453 SAVE\_ARG(FUNCNAME, 4); \

5454 SAVE\_ARG(FUNCNAME, 5); \

5455 SAVE\_ARG(FUNCNAME, 6); \

5456 SAVE\_ARG(FUNCNAME, 7); \

5457 SAVE\_ARG(FUNCNAME, 8); \

5458 SAVE\_ARG(FUNCNAME, 9); \

5459 SAVE\_ARG(FUNCNAME, 10); \

5460 SAVE\_ARG(FUNCNAME, 11); \

5461 SAVE\_ARG(FUNCNAME, 12); \

5462 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5463 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5464 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5465 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5466 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5467 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5468 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5469 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5470 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5471 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5472 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

5473 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

5474 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

5475 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

5476 } else { \

5477 HISTORY\_DROPPED(FUNCNAME); \

5478 } \

5479 INCREMENT\_CALL\_COUNT(FUNCNAME); \

5480 REGISTER\_CALL(FUNCNAME); \

5481 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

5482 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

5483 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

5484 va\_list ap; \

5485 va\_start(ap, arg12); \

5486 FUNCNAME##\_fake \

5487 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

5488 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5489 arg8, arg9, arg10, arg11, arg12, ap); \

5490 va\_end(ap); \

5491 } else { \

5492 va\_list ap; \

5493 va\_start(ap, arg12); \

5494 FUNCNAME##\_fake \

5495 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

5496 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5497 arg8, arg9, arg10, arg11, arg12, ap); \

5498 va\_end(ap); \

5499 } \

5500 } \

5501 if (FUNCNAME##\_fake.custom\_fake) { \

5502 va\_list ap; \

5503 va\_start(ap, arg12); \

5504 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

5505 arg7, arg8, arg9, arg10, arg11, arg12, ap); \

5506 va\_end(ap); \

5507 } \

5508 } \

5509 DEFINE\_RESET\_FUNCTION(FUNCNAME)

5510

[ 5511](fff_8h.md#ac67617b894e59d7f71a21fa53c85ca11)#define FAKE\_VOID\_FUNC14\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

5512 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5513 ARG11\_TYPE, ARG12\_TYPE, ...) \

5514 DECLARE\_FAKE\_VOID\_FUNC14\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5515 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5516 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ...) \

5517 DEFINE\_FAKE\_VOID\_FUNC14\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5518 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5519 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ...)

5520

[ 5521](fff_8h.md#a4c04b800b89d6a40b0b0b85f52684007)#define DECLARE\_FAKE\_VOID\_FUNC15\_VARARG( \

5522 FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5523 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ...) \

5524 typedef struct FUNCNAME##\_Fake { \

5525 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

5526 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

5527 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

5528 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

5529 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

5530 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

5531 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

5532 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

5533 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

5534 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

5535 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

5536 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

5537 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

5538 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

5539 DECLARE\_ALL\_FUNC\_COMMON \

5540 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

5541 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

5542 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5543 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5544 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, va\_list ap); \

5545 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

5546 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5547 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

5548 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5549 va\_list ap); \

5550 } FUNCNAME##\_Fake; \

5551 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5552 void FUNCNAME##\_reset(void); \

5553 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5554 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5555 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5556 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, ...);

5557

[ 5558](fff_8h.md#ad83ab899a7bded1ed9cf24d9c7ce7bb0)#define DEFINE\_FAKE\_VOID\_FUNC15\_VARARG( \

5559 FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5560 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ...) \

5561 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5562 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5563 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5564 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5565 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, ...) \

5566 { \

5567 SAVE\_ARG(FUNCNAME, 0); \

5568 SAVE\_ARG(FUNCNAME, 1); \

5569 SAVE\_ARG(FUNCNAME, 2); \

5570 SAVE\_ARG(FUNCNAME, 3); \

5571 SAVE\_ARG(FUNCNAME, 4); \

5572 SAVE\_ARG(FUNCNAME, 5); \

5573 SAVE\_ARG(FUNCNAME, 6); \

5574 SAVE\_ARG(FUNCNAME, 7); \

5575 SAVE\_ARG(FUNCNAME, 8); \

5576 SAVE\_ARG(FUNCNAME, 9); \

5577 SAVE\_ARG(FUNCNAME, 10); \

5578 SAVE\_ARG(FUNCNAME, 11); \

5579 SAVE\_ARG(FUNCNAME, 12); \

5580 SAVE\_ARG(FUNCNAME, 13); \

5581 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5582 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5583 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5584 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5585 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5586 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5587 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5588 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5589 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5590 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5591 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

5592 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

5593 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

5594 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

5595 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

5596 } else { \

5597 HISTORY\_DROPPED(FUNCNAME); \

5598 } \

5599 INCREMENT\_CALL\_COUNT(FUNCNAME); \

5600 REGISTER\_CALL(FUNCNAME); \

5601 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

5602 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

5603 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

5604 va\_list ap; \

5605 va\_start(ap, arg13); \

5606 FUNCNAME##\_fake \

5607 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

5608 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5609 arg8, arg9, arg10, arg11, arg12, arg13, ap); \

5610 va\_end(ap); \

5611 } else { \

5612 va\_list ap; \

5613 va\_start(ap, arg13); \

5614 FUNCNAME##\_fake \

5615 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

5616 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5617 arg8, arg9, arg10, arg11, arg12, arg13, ap); \

5618 va\_end(ap); \

5619 } \

5620 } \

5621 if (FUNCNAME##\_fake.custom\_fake) { \

5622 va\_list ap; \

5623 va\_start(ap, arg13); \

5624 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

5625 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

5626 ap); \

5627 va\_end(ap); \

5628 } \

5629 } \

5630 DEFINE\_RESET\_FUNCTION(FUNCNAME)

5631

[ 5632](fff_8h.md#a3ba1ccb012fb9eef8c7fbb4d65cbf3aa)#define FAKE\_VOID\_FUNC15\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

5633 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5634 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ...) \

5635 DECLARE\_FAKE\_VOID\_FUNC15\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5636 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5637 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5638 ...) \

5639 DEFINE\_FAKE\_VOID\_FUNC15\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5640 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5641 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5642 ...)

5643

[ 5644](fff_8h.md#a3a80418cf5690557ab082814235292ae)#define DECLARE\_FAKE\_VOID\_FUNC16\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5645 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5646 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5647 ARG14\_TYPE, ...) \

5648 typedef struct FUNCNAME##\_Fake { \

5649 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

5650 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

5651 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

5652 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

5653 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

5654 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

5655 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

5656 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

5657 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

5658 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

5659 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

5660 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

5661 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

5662 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

5663 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

5664 DECLARE\_ALL\_FUNC\_COMMON \

5665 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

5666 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

5667 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5668 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5669 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

5670 va\_list ap); \

5671 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

5672 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5673 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

5674 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5675 ARG14\_TYPE, va\_list ap); \

5676 } FUNCNAME##\_Fake; \

5677 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5678 void FUNCNAME##\_reset(void); \

5679 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5680 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5681 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5682 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

5683 ARG14\_TYPE arg14, ...);

5684

[ 5685](fff_8h.md#a369d94509dc93d98dbbf1b2288ff9dac)#define DEFINE\_FAKE\_VOID\_FUNC16\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5686 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5687 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5688 ARG14\_TYPE, ...) \

5689 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5690 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5691 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5692 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5693 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

5694 ARG14\_TYPE arg14, ...) \

5695 { \

5696 SAVE\_ARG(FUNCNAME, 0); \

5697 SAVE\_ARG(FUNCNAME, 1); \

5698 SAVE\_ARG(FUNCNAME, 2); \

5699 SAVE\_ARG(FUNCNAME, 3); \

5700 SAVE\_ARG(FUNCNAME, 4); \

5701 SAVE\_ARG(FUNCNAME, 5); \

5702 SAVE\_ARG(FUNCNAME, 6); \

5703 SAVE\_ARG(FUNCNAME, 7); \

5704 SAVE\_ARG(FUNCNAME, 8); \

5705 SAVE\_ARG(FUNCNAME, 9); \

5706 SAVE\_ARG(FUNCNAME, 10); \

5707 SAVE\_ARG(FUNCNAME, 11); \

5708 SAVE\_ARG(FUNCNAME, 12); \

5709 SAVE\_ARG(FUNCNAME, 13); \

5710 SAVE\_ARG(FUNCNAME, 14); \

5711 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5712 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5713 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5714 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5715 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5716 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5717 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5718 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5719 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5720 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5721 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

5722 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

5723 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

5724 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

5725 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

5726 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

5727 } else { \

5728 HISTORY\_DROPPED(FUNCNAME); \

5729 } \

5730 INCREMENT\_CALL\_COUNT(FUNCNAME); \

5731 REGISTER\_CALL(FUNCNAME); \

5732 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

5733 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

5734 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

5735 va\_list ap; \

5736 va\_start(ap, arg14); \

5737 FUNCNAME##\_fake \

5738 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

5739 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5740 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

5741 ap); \

5742 va\_end(ap); \

5743 } else { \

5744 va\_list ap; \

5745 va\_start(ap, arg14); \

5746 FUNCNAME##\_fake \

5747 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

5748 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5749 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

5750 ap); \

5751 va\_end(ap); \

5752 } \

5753 } \

5754 if (FUNCNAME##\_fake.custom\_fake) { \

5755 va\_list ap; \

5756 va\_start(ap, arg14); \

5757 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

5758 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

5759 arg14, ap); \

5760 va\_end(ap); \

5761 } \

5762 } \

5763 DEFINE\_RESET\_FUNCTION(FUNCNAME)

5764

[ 5765](fff_8h.md#a915975b009035e8208f51c0b1ad2ff2a)#define FAKE\_VOID\_FUNC16\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

5766 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5767 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ...) \

5768 DECLARE\_FAKE\_VOID\_FUNC16\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5769 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5770 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5771 ARG14\_TYPE, ...) \

5772 DEFINE\_FAKE\_VOID\_FUNC16\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5773 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5774 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5775 ARG14\_TYPE, ...)

5776

[ 5777](fff_8h.md#a94aa5611d9828a6689319ad8e9f27808)#define DECLARE\_FAKE\_VOID\_FUNC17\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5778 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5779 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5780 ARG14\_TYPE, ARG15\_TYPE, ...) \

5781 typedef struct FUNCNAME##\_Fake { \

5782 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

5783 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

5784 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

5785 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

5786 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

5787 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

5788 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

5789 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

5790 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

5791 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

5792 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

5793 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

5794 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

5795 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

5796 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

5797 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

5798 DECLARE\_ALL\_FUNC\_COMMON \

5799 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

5800 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

5801 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5802 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5803 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

5804 ARG15\_TYPE, va\_list ap); \

5805 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

5806 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5807 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

5808 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5809 ARG14\_TYPE, ARG15\_TYPE, va\_list ap); \

5810 } FUNCNAME##\_Fake; \

5811 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5812 void FUNCNAME##\_reset(void); \

5813 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5814 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5815 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5816 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

5817 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ...);

5818

[ 5819](fff_8h.md#a16c8aa7a192b28b9012574b44e7a12f3)#define DEFINE\_FAKE\_VOID\_FUNC17\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5820 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5821 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5822 ARG14\_TYPE, ARG15\_TYPE, ...) \

5823 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5824 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5825 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5826 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5827 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

5828 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ...) \

5829 { \

5830 SAVE\_ARG(FUNCNAME, 0); \

5831 SAVE\_ARG(FUNCNAME, 1); \

5832 SAVE\_ARG(FUNCNAME, 2); \

5833 SAVE\_ARG(FUNCNAME, 3); \

5834 SAVE\_ARG(FUNCNAME, 4); \

5835 SAVE\_ARG(FUNCNAME, 5); \

5836 SAVE\_ARG(FUNCNAME, 6); \

5837 SAVE\_ARG(FUNCNAME, 7); \

5838 SAVE\_ARG(FUNCNAME, 8); \

5839 SAVE\_ARG(FUNCNAME, 9); \

5840 SAVE\_ARG(FUNCNAME, 10); \

5841 SAVE\_ARG(FUNCNAME, 11); \

5842 SAVE\_ARG(FUNCNAME, 12); \

5843 SAVE\_ARG(FUNCNAME, 13); \

5844 SAVE\_ARG(FUNCNAME, 14); \

5845 SAVE\_ARG(FUNCNAME, 15); \

5846 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5847 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5848 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5849 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5850 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5851 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5852 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5853 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5854 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5855 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5856 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

5857 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

5858 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

5859 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

5860 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

5861 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

5862 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

5863 } else { \

5864 HISTORY\_DROPPED(FUNCNAME); \

5865 } \

5866 INCREMENT\_CALL\_COUNT(FUNCNAME); \

5867 REGISTER\_CALL(FUNCNAME); \

5868 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

5869 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

5870 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

5871 va\_list ap; \

5872 va\_start(ap, arg15); \

5873 FUNCNAME##\_fake \

5874 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

5875 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5876 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

5877 arg15, ap); \

5878 va\_end(ap); \

5879 } else { \

5880 va\_list ap; \

5881 va\_start(ap, arg15); \

5882 FUNCNAME##\_fake \

5883 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

5884 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

5885 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

5886 arg15, ap); \

5887 va\_end(ap); \

5888 } \

5889 } \

5890 if (FUNCNAME##\_fake.custom\_fake) { \

5891 va\_list ap; \

5892 va\_start(ap, arg15); \

5893 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

5894 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

5895 arg14, arg15, ap); \

5896 va\_end(ap); \

5897 } \

5898 } \

5899 DEFINE\_RESET\_FUNCTION(FUNCNAME)

5900

[ 5901](fff_8h.md#ac8022204a5d9787da1f697f1bbf6d680)#define FAKE\_VOID\_FUNC17\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

5902 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5903 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ...) \

5904 DECLARE\_FAKE\_VOID\_FUNC17\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5905 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5906 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5907 ARG14\_TYPE, ARG15\_TYPE, ...) \

5908 DEFINE\_FAKE\_VOID\_FUNC17\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5909 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5910 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5911 ARG14\_TYPE, ARG15\_TYPE, ...)

5912

[ 5913](fff_8h.md#af12dc6175433ce77ba12e9bc9cb5b157)#define DECLARE\_FAKE\_VOID\_FUNC18\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5914 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5915 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5916 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...) \

5917 typedef struct FUNCNAME##\_Fake { \

5918 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

5919 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

5920 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

5921 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

5922 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

5923 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

5924 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

5925 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

5926 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

5927 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

5928 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

5929 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

5930 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

5931 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

5932 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

5933 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

5934 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

5935 DECLARE\_ALL\_FUNC\_COMMON \

5936 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

5937 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

5938 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

5939 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

5940 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

5941 ARG15\_TYPE, ARG16\_TYPE, va\_list ap); \

5942 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

5943 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

5944 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

5945 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5946 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, va\_list ap); \

5947 } FUNCNAME##\_Fake; \

5948 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

5949 void FUNCNAME##\_reset(void); \

5950 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5951 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5952 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5953 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

5954 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ...);

5955

[ 5956](fff_8h.md#acb753e9ce63f37cdb40e105efef15f61)#define DEFINE\_FAKE\_VOID\_FUNC18\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

5957 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

5958 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

5959 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...) \

5960 FUNCNAME##\_Fake FUNCNAME##\_fake; \

5961 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

5962 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

5963 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

5964 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

5965 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ...) \

5966 { \

5967 SAVE\_ARG(FUNCNAME, 0); \

5968 SAVE\_ARG(FUNCNAME, 1); \

5969 SAVE\_ARG(FUNCNAME, 2); \

5970 SAVE\_ARG(FUNCNAME, 3); \

5971 SAVE\_ARG(FUNCNAME, 4); \

5972 SAVE\_ARG(FUNCNAME, 5); \

5973 SAVE\_ARG(FUNCNAME, 6); \

5974 SAVE\_ARG(FUNCNAME, 7); \

5975 SAVE\_ARG(FUNCNAME, 8); \

5976 SAVE\_ARG(FUNCNAME, 9); \

5977 SAVE\_ARG(FUNCNAME, 10); \

5978 SAVE\_ARG(FUNCNAME, 11); \

5979 SAVE\_ARG(FUNCNAME, 12); \

5980 SAVE\_ARG(FUNCNAME, 13); \

5981 SAVE\_ARG(FUNCNAME, 14); \

5982 SAVE\_ARG(FUNCNAME, 15); \

5983 SAVE\_ARG(FUNCNAME, 16); \

5984 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

5985 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

5986 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

5987 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

5988 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

5989 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

5990 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

5991 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

5992 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

5993 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

5994 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

5995 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

5996 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

5997 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

5998 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

5999 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

6000 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

6001 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

6002 } else { \

6003 HISTORY\_DROPPED(FUNCNAME); \

6004 } \

6005 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6006 REGISTER\_CALL(FUNCNAME); \

6007 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6008 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6009 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6010 va\_list ap; \

6011 va\_start(ap, arg16); \

6012 FUNCNAME##\_fake \

6013 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6014 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

6015 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

6016 arg15, arg16, ap); \

6017 va\_end(ap); \

6018 } else { \

6019 va\_list ap; \

6020 va\_start(ap, arg16); \

6021 FUNCNAME##\_fake \

6022 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6023 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

6024 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

6025 arg15, arg16, ap); \

6026 va\_end(ap); \

6027 } \

6028 } \

6029 if (FUNCNAME##\_fake.custom\_fake) { \

6030 va\_list ap; \

6031 va\_start(ap, arg16); \

6032 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

6033 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

6034 arg14, arg15, arg16, ap); \

6035 va\_end(ap); \

6036 } \

6037 } \

6038 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6039

[ 6040](fff_8h.md#a8b469e775e2389b55f07c12406e75f25)#define FAKE\_VOID\_FUNC18\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

6041 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

6042 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

6043 ARG16\_TYPE, ...) \

6044 DECLARE\_FAKE\_VOID\_FUNC18\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6045 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

6046 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6047 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...) \

6048 DEFINE\_FAKE\_VOID\_FUNC18\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6049 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

6050 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6051 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...)

6052

[ 6053](fff_8h.md#ac46d069ba405218bdbdaaa8b06f3600d)#define DECLARE\_FAKE\_VOID\_FUNC19\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6054 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

6055 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6056 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...) \

6057 typedef struct FUNCNAME##\_Fake { \

6058 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6059 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6060 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

6061 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

6062 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

6063 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

6064 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

6065 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

6066 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

6067 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

6068 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

6069 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

6070 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

6071 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

6072 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

6073 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

6074 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

6075 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

6076 DECLARE\_ALL\_FUNC\_COMMON \

6077 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6078 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6079 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

6080 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

6081 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

6082 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, va\_list ap); \

6083 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6084 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6085 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

6086 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6087 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

6088 va\_list ap); \

6089 } FUNCNAME##\_Fake; \

6090 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6091 void FUNCNAME##\_reset(void); \

6092 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

6093 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

6094 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

6095 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

6096 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, ...);

6097

[ 6098](fff_8h.md#aac92bd4880ccf37cdbe49e15431744a5)#define DEFINE\_FAKE\_VOID\_FUNC19\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6099 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

6100 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6101 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...) \

6102 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6103 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

6104 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

6105 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

6106 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

6107 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, ...) \

6108 { \

6109 SAVE\_ARG(FUNCNAME, 0); \

6110 SAVE\_ARG(FUNCNAME, 1); \

6111 SAVE\_ARG(FUNCNAME, 2); \

6112 SAVE\_ARG(FUNCNAME, 3); \

6113 SAVE\_ARG(FUNCNAME, 4); \

6114 SAVE\_ARG(FUNCNAME, 5); \

6115 SAVE\_ARG(FUNCNAME, 6); \

6116 SAVE\_ARG(FUNCNAME, 7); \

6117 SAVE\_ARG(FUNCNAME, 8); \

6118 SAVE\_ARG(FUNCNAME, 9); \

6119 SAVE\_ARG(FUNCNAME, 10); \

6120 SAVE\_ARG(FUNCNAME, 11); \

6121 SAVE\_ARG(FUNCNAME, 12); \

6122 SAVE\_ARG(FUNCNAME, 13); \

6123 SAVE\_ARG(FUNCNAME, 14); \

6124 SAVE\_ARG(FUNCNAME, 15); \

6125 SAVE\_ARG(FUNCNAME, 16); \

6126 SAVE\_ARG(FUNCNAME, 17); \

6127 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6128 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6129 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

6130 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

6131 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

6132 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

6133 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

6134 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

6135 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

6136 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

6137 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

6138 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

6139 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

6140 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

6141 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

6142 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

6143 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

6144 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

6145 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

6146 } else { \

6147 HISTORY\_DROPPED(FUNCNAME); \

6148 } \

6149 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6150 REGISTER\_CALL(FUNCNAME); \

6151 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6152 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6153 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6154 va\_list ap; \

6155 va\_start(ap, arg17); \

6156 FUNCNAME##\_fake \

6157 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6158 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

6159 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

6160 arg15, arg16, arg17, ap); \

6161 va\_end(ap); \

6162 } else { \

6163 va\_list ap; \

6164 va\_start(ap, arg17); \

6165 FUNCNAME##\_fake \

6166 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6167 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

6168 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

6169 arg15, arg16, arg17, ap); \

6170 va\_end(ap); \

6171 } \

6172 } \

6173 if (FUNCNAME##\_fake.custom\_fake) { \

6174 va\_list ap; \

6175 va\_start(ap, arg17); \

6176 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

6177 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

6178 arg14, arg15, arg16, arg17, ap); \

6179 va\_end(ap); \

6180 } \

6181 } \

6182 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6183

[ 6184](fff_8h.md#adf5d7dc8081e25b0fb856c605c758208)#define FAKE\_VOID\_FUNC19\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

6185 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

6186 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

6187 ARG16\_TYPE, ARG17\_TYPE, ...) \

6188 DECLARE\_FAKE\_VOID\_FUNC19\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6189 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

6190 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6191 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...) \

6192 DEFINE\_FAKE\_VOID\_FUNC19\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6193 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

6194 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6195 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...)

6196

[ 6197](fff_8h.md#af04d79c629295397d2fff5ed9401e19e)#define DECLARE\_FAKE\_VOID\_FUNC20\_VARARG( \

6198 FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

6199 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6200 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ...) \

6201 typedef struct FUNCNAME##\_Fake { \

6202 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6203 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6204 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

6205 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

6206 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

6207 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

6208 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

6209 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

6210 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

6211 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

6212 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

6213 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

6214 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

6215 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

6216 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

6217 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

6218 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

6219 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

6220 DECLARE\_ARG(ARG18\_TYPE, 18, FUNCNAME) \

6221 DECLARE\_ALL\_FUNC\_COMMON \

6222 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6223 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6224 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

6225 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

6226 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, \

6227 ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, \

6228 va\_list ap); \

6229 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(void, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6230 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6231 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

6232 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6233 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

6234 ARG18\_TYPE, va\_list ap); \

6235 } FUNCNAME##\_Fake; \

6236 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6237 void FUNCNAME##\_reset(void); \

6238 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

6239 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

6240 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

6241 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

6242 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

6243 ARG18\_TYPE arg18, ...);

6244

[ 6245](fff_8h.md#aaaf2f22fdad18fde5c3cd3e0c03706e4)#define DEFINE\_FAKE\_VOID\_FUNC20\_VARARG( \

6246 FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, \

6247 ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

6248 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ...) \

6249 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6250 void FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

6251 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

6252 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

6253 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

6254 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

6255 ARG18\_TYPE arg18, ...) \

6256 { \

6257 SAVE\_ARG(FUNCNAME, 0); \

6258 SAVE\_ARG(FUNCNAME, 1); \

6259 SAVE\_ARG(FUNCNAME, 2); \

6260 SAVE\_ARG(FUNCNAME, 3); \

6261 SAVE\_ARG(FUNCNAME, 4); \

6262 SAVE\_ARG(FUNCNAME, 5); \

6263 SAVE\_ARG(FUNCNAME, 6); \

6264 SAVE\_ARG(FUNCNAME, 7); \

6265 SAVE\_ARG(FUNCNAME, 8); \

6266 SAVE\_ARG(FUNCNAME, 9); \

6267 SAVE\_ARG(FUNCNAME, 10); \

6268 SAVE\_ARG(FUNCNAME, 11); \

6269 SAVE\_ARG(FUNCNAME, 12); \

6270 SAVE\_ARG(FUNCNAME, 13); \

6271 SAVE\_ARG(FUNCNAME, 14); \

6272 SAVE\_ARG(FUNCNAME, 15); \

6273 SAVE\_ARG(FUNCNAME, 16); \

6274 SAVE\_ARG(FUNCNAME, 17); \

6275 SAVE\_ARG(FUNCNAME, 18); \

6276 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6277 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6278 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

6279 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

6280 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

6281 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

6282 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

6283 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

6284 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

6285 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

6286 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

6287 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

6288 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

6289 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

6290 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

6291 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

6292 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

6293 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

6294 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

6295 SAVE\_ARG\_HISTORY(FUNCNAME, 18); \

6296 } else { \

6297 HISTORY\_DROPPED(FUNCNAME); \

6298 } \

6299 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6300 REGISTER\_CALL(FUNCNAME); \

6301 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6302 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6303 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6304 va\_list ap; \

6305 va\_start(ap, arg18); \

6306 FUNCNAME##\_fake \

6307 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6308 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

6309 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

6310 arg15, arg16, arg17, arg18, ap); \

6311 va\_end(ap); \

6312 } else { \

6313 va\_list ap; \

6314 va\_start(ap, arg18); \

6315 FUNCNAME##\_fake \

6316 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6317 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

6318 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

6319 arg15, arg16, arg17, arg18, ap); \

6320 va\_end(ap); \

6321 } \

6322 } \

6323 if (FUNCNAME##\_fake.custom\_fake) { \

6324 va\_list ap; \

6325 va\_start(ap, arg18); \

6326 FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

6327 arg7, arg8, arg9, arg10, arg11, arg12, arg13, \

6328 arg14, arg15, arg16, arg17, arg18, ap); \

6329 va\_end(ap); \

6330 } \

6331 } \

6332 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6333

[ 6334](fff_8h.md#abea0034f61e8213a7ed974fe433abd8a)#define FAKE\_VOID\_FUNC20\_VARARG(FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

6335 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, \

6336 ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, \

6337 ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ...) \

6338 DECLARE\_FAKE\_VOID\_FUNC20\_VARARG( \

6339 FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6340 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

6341 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ...) \

6342 DEFINE\_FAKE\_VOID\_FUNC20\_VARARG( \

6343 FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6344 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

6345 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ...)

6346

[ 6347](fff_8h.md#a5d2d9698d2cae1c854618af035114f50)#define DECLARE\_FAKE\_VALUE\_FUNC2\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ...) \

6348 typedef struct FUNCNAME##\_Fake { \

6349 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6350 DECLARE\_ALL\_FUNC\_COMMON \

6351 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

6352 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

6353 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6354 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, va\_list ap); \

6355 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, \

6356 va\_list ap); \

6357 } FUNCNAME##\_Fake; \

6358 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6359 void FUNCNAME##\_reset(void); \

6360 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ...);

6361

[ 6362](fff_8h.md#a055c12609dd2e0550d44a0081480a1a9)#define DEFINE\_FAKE\_VALUE\_FUNC2\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ...) \

6363 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6364 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ...) \

6365 { \

6366 SAVE\_ARG(FUNCNAME, 0); \

6367 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6368 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6369 } else { \

6370 HISTORY\_DROPPED(FUNCNAME); \

6371 } \

6372 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6373 REGISTER\_CALL(FUNCNAME); \

6374 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6375 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6376 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6377 va\_list ap; \

6378 va\_start(ap, arg0); \

6379 RETURN\_TYPE ret = \

6380 FUNCNAME##\_fake.custom\_fake\_seq \

6381 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++](arg0, ap); \

6382 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6383 va\_end(ap); \

6384 return ret; \

6385 } else { \

6386 va\_list ap; \

6387 va\_start(ap, arg0); \

6388 RETURN\_TYPE ret = \

6389 FUNCNAME##\_fake.custom\_fake\_seq \

6390 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1](arg0, \

6391 ap); \

6392 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6393 va\_end(ap); \

6394 return ret; \

6395 return FUNCNAME##\_fake \

6396 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6397 arg0, ap); \

6398 } \

6399 } \

6400 if (FUNCNAME##\_fake.custom\_fake) { \

6401 RETURN\_TYPE ret; \

6402 va\_list ap; \

6403 va\_start(ap, arg0); \

6404 ret = FUNCNAME##\_fake.custom\_fake(arg0, ap); \

6405 va\_end(ap); \

6406 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6407 return ret; \

6408 } \

6409 RETURN\_FAKE\_RESULT(FUNCNAME) \

6410 } \

6411 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6412

[ 6413](fff_8h.md#a66932b4394798f2538ab8b6e7b2ab0dc)#define FAKE\_VALUE\_FUNC2\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ...) \

6414 DECLARE\_FAKE\_VALUE\_FUNC2\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ...) \

6415 DEFINE\_FAKE\_VALUE\_FUNC2\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ...)

6416

[ 6417](fff_8h.md#a99543788ab009f0fb3c921a87d9ad601)#define DECLARE\_FAKE\_VALUE\_FUNC3\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...) \

6418 typedef struct FUNCNAME##\_Fake { \

6419 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6420 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6421 DECLARE\_ALL\_FUNC\_COMMON \

6422 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

6423 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

6424 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6425 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

6426 va\_list ap); \

6427 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6428 va\_list ap); \

6429 } FUNCNAME##\_Fake; \

6430 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6431 void FUNCNAME##\_reset(void); \

6432 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ...);

6433

[ 6434](fff_8h.md#a810f802ed9d083edc6d1fa6ec322bbb4)#define DEFINE\_FAKE\_VALUE\_FUNC3\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...) \

6435 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6436 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, ...) \

6437 { \

6438 SAVE\_ARG(FUNCNAME, 0); \

6439 SAVE\_ARG(FUNCNAME, 1); \

6440 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6441 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6442 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

6443 } else { \

6444 HISTORY\_DROPPED(FUNCNAME); \

6445 } \

6446 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6447 REGISTER\_CALL(FUNCNAME); \

6448 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6449 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6450 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6451 va\_list ap; \

6452 va\_start(ap, arg1); \

6453 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

6454 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6455 arg0, arg1, ap); \

6456 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6457 va\_end(ap); \

6458 return ret; \

6459 } else { \

6460 va\_list ap; \

6461 va\_start(ap, arg1); \

6462 RETURN\_TYPE ret = \

6463 FUNCNAME##\_fake.custom\_fake\_seq \

6464 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6465 arg0, arg1, ap); \

6466 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6467 va\_end(ap); \

6468 return ret; \

6469 return FUNCNAME##\_fake \

6470 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6471 arg0, arg1, ap); \

6472 } \

6473 } \

6474 if (FUNCNAME##\_fake.custom\_fake) { \

6475 RETURN\_TYPE ret; \

6476 va\_list ap; \

6477 va\_start(ap, arg1); \

6478 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, ap); \

6479 va\_end(ap); \

6480 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6481 return ret; \

6482 } \

6483 RETURN\_FAKE\_RESULT(FUNCNAME) \

6484 } \

6485 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6486

[ 6487](fff_8h.md#a7041cd452e948044d81fa68b47043adf)#define FAKE\_VALUE\_FUNC3\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...) \

6488 DECLARE\_FAKE\_VALUE\_FUNC3\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...) \

6489 DEFINE\_FAKE\_VALUE\_FUNC3\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ...)

6490

[ 6491](fff_8h.md#a3ec0ddd9e71f6004aa192f927f54cc7b)#define DECLARE\_FAKE\_VALUE\_FUNC4\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6492 ...) \

6493 typedef struct FUNCNAME##\_Fake { \

6494 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6495 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6496 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

6497 DECLARE\_ALL\_FUNC\_COMMON \

6498 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

6499 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

6500 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6501 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

6502 ARG2\_TYPE, va\_list ap); \

6503 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6504 ARG2\_TYPE, va\_list ap); \

6505 } FUNCNAME##\_Fake; \

6506 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6507 void FUNCNAME##\_reset(void); \

6508 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

6509 ARG2\_TYPE arg2, ...);

6510

[ 6511](fff_8h.md#abd15b0317a504f24065d40057f5f139e)#define DEFINE\_FAKE\_VALUE\_FUNC4\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6512 ...) \

6513 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6514 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

6515 ARG2\_TYPE arg2, ...) \

6516 { \

6517 SAVE\_ARG(FUNCNAME, 0); \

6518 SAVE\_ARG(FUNCNAME, 1); \

6519 SAVE\_ARG(FUNCNAME, 2); \

6520 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6521 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6522 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

6523 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

6524 } else { \

6525 HISTORY\_DROPPED(FUNCNAME); \

6526 } \

6527 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6528 REGISTER\_CALL(FUNCNAME); \

6529 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6530 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6531 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6532 va\_list ap; \

6533 va\_start(ap, arg2); \

6534 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

6535 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6536 arg0, arg1, arg2, ap); \

6537 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6538 va\_end(ap); \

6539 return ret; \

6540 } else { \

6541 va\_list ap; \

6542 va\_start(ap, arg2); \

6543 RETURN\_TYPE ret = \

6544 FUNCNAME##\_fake.custom\_fake\_seq \

6545 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6546 arg0, arg1, arg2, ap); \

6547 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6548 va\_end(ap); \

6549 return ret; \

6550 return FUNCNAME##\_fake \

6551 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6552 arg0, arg1, arg2, ap); \

6553 } \

6554 } \

6555 if (FUNCNAME##\_fake.custom\_fake) { \

6556 RETURN\_TYPE ret; \

6557 va\_list ap; \

6558 va\_start(ap, arg2); \

6559 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, ap); \

6560 va\_end(ap); \

6561 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6562 return ret; \

6563 } \

6564 RETURN\_FAKE\_RESULT(FUNCNAME) \

6565 } \

6566 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6567

[ 6568](fff_8h.md#a110f02cca4cc6805b747033e90c22da6)#define FAKE\_VALUE\_FUNC4\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ...) \

6569 DECLARE\_FAKE\_VALUE\_FUNC4\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6570 ...) \

6571 DEFINE\_FAKE\_VALUE\_FUNC4\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ...)

6572

[ 6573](fff_8h.md#a3073f275a8b2a0339626f1bc4419ab73)#define DECLARE\_FAKE\_VALUE\_FUNC5\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6574 ARG3\_TYPE, ...) \

6575 typedef struct FUNCNAME##\_Fake { \

6576 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6577 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6578 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

6579 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

6580 DECLARE\_ALL\_FUNC\_COMMON \

6581 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

6582 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

6583 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6584 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

6585 ARG2\_TYPE, ARG3\_TYPE, va\_list ap); \

6586 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6587 ARG2\_TYPE, ARG3\_TYPE, va\_list ap); \

6588 } FUNCNAME##\_Fake; \

6589 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6590 void FUNCNAME##\_reset(void); \

6591 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

6592 ARG2\_TYPE arg2, ARG3\_TYPE arg3, ...);

6593

[ 6594](fff_8h.md#ac64b930c343659fd4c0a710854ba5487)#define DEFINE\_FAKE\_VALUE\_FUNC5\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6595 ARG3\_TYPE, ...) \

6596 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6597 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

6598 ARG2\_TYPE arg2, ARG3\_TYPE arg3, ...) \

6599 { \

6600 SAVE\_ARG(FUNCNAME, 0); \

6601 SAVE\_ARG(FUNCNAME, 1); \

6602 SAVE\_ARG(FUNCNAME, 2); \

6603 SAVE\_ARG(FUNCNAME, 3); \

6604 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6605 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6606 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

6607 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

6608 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

6609 } else { \

6610 HISTORY\_DROPPED(FUNCNAME); \

6611 } \

6612 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6613 REGISTER\_CALL(FUNCNAME); \

6614 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6615 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6616 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6617 va\_list ap; \

6618 va\_start(ap, arg3); \

6619 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

6620 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6621 arg0, arg1, arg2, arg3, ap); \

6622 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6623 va\_end(ap); \

6624 return ret; \

6625 } else { \

6626 va\_list ap; \

6627 va\_start(ap, arg3); \

6628 RETURN\_TYPE ret = \

6629 FUNCNAME##\_fake.custom\_fake\_seq \

6630 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6631 arg0, arg1, arg2, arg3, ap); \

6632 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6633 va\_end(ap); \

6634 return ret; \

6635 return FUNCNAME##\_fake \

6636 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6637 arg0, arg1, arg2, arg3, ap); \

6638 } \

6639 } \

6640 if (FUNCNAME##\_fake.custom\_fake) { \

6641 RETURN\_TYPE ret; \

6642 va\_list ap; \

6643 va\_start(ap, arg3); \

6644 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, ap); \

6645 va\_end(ap); \

6646 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6647 return ret; \

6648 } \

6649 RETURN\_FAKE\_RESULT(FUNCNAME) \

6650 } \

6651 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6652

[ 6653](fff_8h.md#ab70ba49903d873771a6c3d3c06c866d1)#define FAKE\_VALUE\_FUNC5\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6654 ...) \

6655 DECLARE\_FAKE\_VALUE\_FUNC5\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6656 ARG3\_TYPE, ...) \

6657 DEFINE\_FAKE\_VALUE\_FUNC5\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6658 ARG3\_TYPE, ...)

6659

[ 6660](fff_8h.md#ac9f429b0b9e6b4c24f4cac64ffafb71e)#define DECLARE\_FAKE\_VALUE\_FUNC6\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6661 ARG3\_TYPE, ARG4\_TYPE, ...) \

6662 typedef struct FUNCNAME##\_Fake { \

6663 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6664 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6665 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

6666 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

6667 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

6668 DECLARE\_ALL\_FUNC\_COMMON \

6669 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

6670 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

6671 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6672 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

6673 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, va\_list ap); \

6674 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6675 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, va\_list ap); \

6676 } FUNCNAME##\_Fake; \

6677 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6678 void FUNCNAME##\_reset(void); \

6679 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

6680 ARG2\_TYPE arg2, ARG3\_TYPE arg3, \

6681 ARG4\_TYPE arg4, ...);

6682

[ 6683](fff_8h.md#a02a8e22aebe0eb817faeb41cc0c9f47a)#define DEFINE\_FAKE\_VALUE\_FUNC6\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6684 ARG3\_TYPE, ARG4\_TYPE, ...) \

6685 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6686 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

6687 ARG2\_TYPE arg2, ARG3\_TYPE arg3, \

6688 ARG4\_TYPE arg4, ...) \

6689 { \

6690 SAVE\_ARG(FUNCNAME, 0); \

6691 SAVE\_ARG(FUNCNAME, 1); \

6692 SAVE\_ARG(FUNCNAME, 2); \

6693 SAVE\_ARG(FUNCNAME, 3); \

6694 SAVE\_ARG(FUNCNAME, 4); \

6695 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6696 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6697 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

6698 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

6699 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

6700 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

6701 } else { \

6702 HISTORY\_DROPPED(FUNCNAME); \

6703 } \

6704 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6705 REGISTER\_CALL(FUNCNAME); \

6706 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6707 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6708 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6709 va\_list ap; \

6710 va\_start(ap, arg4); \

6711 RETURN\_TYPE ret = \

6712 FUNCNAME##\_fake.custom\_fake\_seq \

6713 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6714 arg0, arg1, arg2, arg3, arg4, ap); \

6715 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6716 va\_end(ap); \

6717 return ret; \

6718 } else { \

6719 va\_list ap; \

6720 va\_start(ap, arg4); \

6721 RETURN\_TYPE ret = \

6722 FUNCNAME##\_fake.custom\_fake\_seq \

6723 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6724 arg0, arg1, arg2, arg3, arg4, ap); \

6725 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6726 va\_end(ap); \

6727 return ret; \

6728 return FUNCNAME##\_fake \

6729 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6730 arg0, arg1, arg2, arg3, arg4, ap); \

6731 } \

6732 } \

6733 if (FUNCNAME##\_fake.custom\_fake) { \

6734 RETURN\_TYPE ret; \

6735 va\_list ap; \

6736 va\_start(ap, arg4); \

6737 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, ap); \

6738 va\_end(ap); \

6739 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6740 return ret; \

6741 } \

6742 RETURN\_FAKE\_RESULT(FUNCNAME) \

6743 } \

6744 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6745

[ 6746](fff_8h.md#a89bfd68c7fa15b0e07840cc4a7aadc8f)#define FAKE\_VALUE\_FUNC6\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6747 ARG4\_TYPE, ...) \

6748 DECLARE\_FAKE\_VALUE\_FUNC6\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6749 ARG3\_TYPE, ARG4\_TYPE, ...) \

6750 DEFINE\_FAKE\_VALUE\_FUNC6\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6751 ARG3\_TYPE, ARG4\_TYPE, ...)

6752

[ 6753](fff_8h.md#af3c79611e723530cd1bd00f1722f6995)#define DECLARE\_FAKE\_VALUE\_FUNC7\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6754 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ...) \

6755 typedef struct FUNCNAME##\_Fake { \

6756 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6757 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6758 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

6759 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

6760 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

6761 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

6762 DECLARE\_ALL\_FUNC\_COMMON \

6763 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

6764 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

6765 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6766 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

6767 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6768 va\_list ap); \

6769 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6770 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6771 va\_list ap); \

6772 } FUNCNAME##\_Fake; \

6773 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6774 void FUNCNAME##\_reset(void); \

6775 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

6776 ARG2\_TYPE arg2, ARG3\_TYPE arg3, \

6777 ARG4\_TYPE arg4, ARG5\_TYPE arg5, ...);

6778

[ 6779](fff_8h.md#ae5722cc7a84cd2f36d9305ebf59bdbac)#define DEFINE\_FAKE\_VALUE\_FUNC7\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6780 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ...) \

6781 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6782 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME(ARG0\_TYPE arg0, ARG1\_TYPE arg1, \

6783 ARG2\_TYPE arg2, ARG3\_TYPE arg3, \

6784 ARG4\_TYPE arg4, ARG5\_TYPE arg5, ...) \

6785 { \

6786 SAVE\_ARG(FUNCNAME, 0); \

6787 SAVE\_ARG(FUNCNAME, 1); \

6788 SAVE\_ARG(FUNCNAME, 2); \

6789 SAVE\_ARG(FUNCNAME, 3); \

6790 SAVE\_ARG(FUNCNAME, 4); \

6791 SAVE\_ARG(FUNCNAME, 5); \

6792 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6793 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6794 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

6795 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

6796 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

6797 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

6798 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

6799 } else { \

6800 HISTORY\_DROPPED(FUNCNAME); \

6801 } \

6802 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6803 REGISTER\_CALL(FUNCNAME); \

6804 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6805 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6806 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6807 va\_list ap; \

6808 va\_start(ap, arg5); \

6809 RETURN\_TYPE ret = \

6810 FUNCNAME##\_fake.custom\_fake\_seq \

6811 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6812 arg0, arg1, arg2, arg3, arg4, arg5, ap); \

6813 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6814 va\_end(ap); \

6815 return ret; \

6816 } else { \

6817 va\_list ap; \

6818 va\_start(ap, arg5); \

6819 RETURN\_TYPE ret = \

6820 FUNCNAME##\_fake.custom\_fake\_seq \

6821 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6822 arg0, arg1, arg2, arg3, arg4, arg5, ap); \

6823 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6824 va\_end(ap); \

6825 return ret; \

6826 return FUNCNAME##\_fake \

6827 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6828 arg0, arg1, arg2, arg3, arg4, arg5, ap); \

6829 } \

6830 } \

6831 if (FUNCNAME##\_fake.custom\_fake) { \

6832 RETURN\_TYPE ret; \

6833 va\_list ap; \

6834 va\_start(ap, arg5); \

6835 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, ap); \

6836 va\_end(ap); \

6837 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6838 return ret; \

6839 } \

6840 RETURN\_FAKE\_RESULT(FUNCNAME) \

6841 } \

6842 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6843

[ 6844](fff_8h.md#a41466d19c8859ccefb833346e50040d6)#define FAKE\_VALUE\_FUNC7\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6845 ARG4\_TYPE, ARG5\_TYPE, ...) \

6846 DECLARE\_FAKE\_VALUE\_FUNC7\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6847 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ...) \

6848 DEFINE\_FAKE\_VALUE\_FUNC7\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6849 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ...)

6850

[ 6851](fff_8h.md#ad105145746a5c7d32dbb757025360f5a)#define DECLARE\_FAKE\_VALUE\_FUNC8\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6852 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...) \

6853 typedef struct FUNCNAME##\_Fake { \

6854 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6855 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6856 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

6857 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

6858 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

6859 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

6860 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

6861 DECLARE\_ALL\_FUNC\_COMMON \

6862 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

6863 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

6864 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6865 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

6866 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6867 ARG6\_TYPE, va\_list ap); \

6868 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6869 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6870 ARG6\_TYPE, va\_list ap); \

6871 } FUNCNAME##\_Fake; \

6872 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6873 void FUNCNAME##\_reset(void); \

6874 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

6875 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

6876 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ...);

6877

[ 6878](fff_8h.md#ae366265309730ff96774d0231926e6a1)#define DEFINE\_FAKE\_VALUE\_FUNC8\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6879 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...) \

6880 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6881 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

6882 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

6883 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ...) \

6884 { \

6885 SAVE\_ARG(FUNCNAME, 0); \

6886 SAVE\_ARG(FUNCNAME, 1); \

6887 SAVE\_ARG(FUNCNAME, 2); \

6888 SAVE\_ARG(FUNCNAME, 3); \

6889 SAVE\_ARG(FUNCNAME, 4); \

6890 SAVE\_ARG(FUNCNAME, 5); \

6891 SAVE\_ARG(FUNCNAME, 6); \

6892 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6893 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

6894 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

6895 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

6896 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

6897 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

6898 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

6899 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

6900 } else { \

6901 HISTORY\_DROPPED(FUNCNAME); \

6902 } \

6903 INCREMENT\_CALL\_COUNT(FUNCNAME); \

6904 REGISTER\_CALL(FUNCNAME); \

6905 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

6906 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

6907 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

6908 va\_list ap; \

6909 va\_start(ap, arg6); \

6910 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

6911 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

6912 arg0, arg1, arg2, arg3, arg4, \

6913 arg5, arg6, ap); \

6914 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6915 va\_end(ap); \

6916 return ret; \

6917 } else { \

6918 va\_list ap; \

6919 va\_start(ap, arg6); \

6920 RETURN\_TYPE ret = \

6921 FUNCNAME##\_fake.custom\_fake\_seq \

6922 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6923 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

6924 ap); \

6925 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6926 va\_end(ap); \

6927 return ret; \

6928 return FUNCNAME##\_fake \

6929 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

6930 arg0, arg1, arg2, arg3, arg4, arg5, arg6, ap); \

6931 } \

6932 } \

6933 if (FUNCNAME##\_fake.custom\_fake) { \

6934 RETURN\_TYPE ret; \

6935 va\_list ap; \

6936 va\_start(ap, arg6); \

6937 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

6938 arg6, ap); \

6939 va\_end(ap); \

6940 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

6941 return ret; \

6942 } \

6943 RETURN\_FAKE\_RESULT(FUNCNAME) \

6944 } \

6945 DEFINE\_RESET\_FUNCTION(FUNCNAME)

6946

[ 6947](fff_8h.md#a207f79401d9ff3a62e4ea7e6526ab0fc)#define FAKE\_VALUE\_FUNC8\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

6948 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...) \

6949 DECLARE\_FAKE\_VALUE\_FUNC8\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6950 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...) \

6951 DEFINE\_FAKE\_VALUE\_FUNC8\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6952 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ...)

6953

[ 6954](fff_8h.md#a19f245de1df09aa17ac0926a75d9467b)#define DECLARE\_FAKE\_VALUE\_FUNC9\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6955 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

6956 ...) \

6957 typedef struct FUNCNAME##\_Fake { \

6958 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

6959 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

6960 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

6961 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

6962 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

6963 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

6964 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

6965 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

6966 DECLARE\_ALL\_FUNC\_COMMON \

6967 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

6968 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

6969 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

6970 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

6971 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6972 ARG6\_TYPE, ARG7\_TYPE, va\_list ap); \

6973 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

6974 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

6975 ARG6\_TYPE, ARG7\_TYPE, va\_list ap); \

6976 } FUNCNAME##\_Fake; \

6977 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

6978 void FUNCNAME##\_reset(void); \

6979 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

6980 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

6981 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ...);

6982

[ 6983](fff_8h.md#a9624bdec8ff8da6ac1ead2246cf5566d)#define DEFINE\_FAKE\_VALUE\_FUNC9\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

6984 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ...) \

6985 FUNCNAME##\_Fake FUNCNAME##\_fake; \

6986 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

6987 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

6988 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ...) \

6989 { \

6990 SAVE\_ARG(FUNCNAME, 0); \

6991 SAVE\_ARG(FUNCNAME, 1); \

6992 SAVE\_ARG(FUNCNAME, 2); \

6993 SAVE\_ARG(FUNCNAME, 3); \

6994 SAVE\_ARG(FUNCNAME, 4); \

6995 SAVE\_ARG(FUNCNAME, 5); \

6996 SAVE\_ARG(FUNCNAME, 6); \

6997 SAVE\_ARG(FUNCNAME, 7); \

6998 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

6999 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

7000 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

7001 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

7002 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

7003 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

7004 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

7005 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

7006 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

7007 } else { \

7008 HISTORY\_DROPPED(FUNCNAME); \

7009 } \

7010 INCREMENT\_CALL\_COUNT(FUNCNAME); \

7011 REGISTER\_CALL(FUNCNAME); \

7012 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

7013 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

7014 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

7015 va\_list ap; \

7016 va\_start(ap, arg7); \

7017 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

7018 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

7019 arg0, arg1, arg2, arg3, arg4, \

7020 arg5, arg6, arg7, ap); \

7021 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7022 va\_end(ap); \

7023 return ret; \

7024 } else { \

7025 va\_list ap; \

7026 va\_start(ap, arg7); \

7027 RETURN\_TYPE ret = \

7028 FUNCNAME##\_fake.custom\_fake\_seq \

7029 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7030 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7031 arg7, ap); \

7032 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7033 va\_end(ap); \

7034 return ret; \

7035 return FUNCNAME##\_fake \

7036 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7037 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

7038 ap); \

7039 } \

7040 } \

7041 if (FUNCNAME##\_fake.custom\_fake) { \

7042 RETURN\_TYPE ret; \

7043 va\_list ap; \

7044 va\_start(ap, arg7); \

7045 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

7046 arg6, arg7, ap); \

7047 va\_end(ap); \

7048 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7049 return ret; \

7050 } \

7051 RETURN\_FAKE\_RESULT(FUNCNAME) \

7052 } \

7053 DEFINE\_RESET\_FUNCTION(FUNCNAME)

7054

[ 7055](fff_8h.md#a9ddde412da565d8be225d5988b2cc8e5)#define FAKE\_VALUE\_FUNC9\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, \

7056 ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ...) \

7057 DECLARE\_FAKE\_VALUE\_FUNC9\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7058 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7059 ...) \

7060 DEFINE\_FAKE\_VALUE\_FUNC9\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7061 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ...)

7062

[ 7063](fff_8h.md#a64ebae32657c1c9cec054b1d42c801a1)#define DECLARE\_FAKE\_VALUE\_FUNC10\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7064 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7065 ARG8\_TYPE, ...) \

7066 typedef struct FUNCNAME##\_Fake { \

7067 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

7068 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

7069 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

7070 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

7071 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

7072 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

7073 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

7074 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

7075 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

7076 DECLARE\_ALL\_FUNC\_COMMON \

7077 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

7078 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

7079 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

7080 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

7081 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7082 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, va\_list ap); \

7083 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

7084 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7085 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, va\_list ap); \

7086 } FUNCNAME##\_Fake; \

7087 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

7088 void FUNCNAME##\_reset(void); \

7089 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7090 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7091 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ...);

7092

[ 7093](fff_8h.md#a91437e334af86369e6f19565549c1d47)#define DEFINE\_FAKE\_VALUE\_FUNC10\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7094 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7095 ARG8\_TYPE, ...) \

7096 FUNCNAME##\_Fake FUNCNAME##\_fake; \

7097 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7098 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7099 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ...) \

7100 { \

7101 SAVE\_ARG(FUNCNAME, 0); \

7102 SAVE\_ARG(FUNCNAME, 1); \

7103 SAVE\_ARG(FUNCNAME, 2); \

7104 SAVE\_ARG(FUNCNAME, 3); \

7105 SAVE\_ARG(FUNCNAME, 4); \

7106 SAVE\_ARG(FUNCNAME, 5); \

7107 SAVE\_ARG(FUNCNAME, 6); \

7108 SAVE\_ARG(FUNCNAME, 7); \

7109 SAVE\_ARG(FUNCNAME, 8); \

7110 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

7111 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

7112 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

7113 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

7114 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

7115 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

7116 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

7117 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

7118 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

7119 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

7120 } else { \

7121 HISTORY\_DROPPED(FUNCNAME); \

7122 } \

7123 INCREMENT\_CALL\_COUNT(FUNCNAME); \

7124 REGISTER\_CALL(FUNCNAME); \

7125 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

7126 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

7127 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

7128 va\_list ap; \

7129 va\_start(ap, arg8); \

7130 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

7131 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

7132 arg0, arg1, arg2, arg3, arg4, \

7133 arg5, arg6, arg7, arg8, ap); \

7134 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7135 va\_end(ap); \

7136 return ret; \

7137 } else { \

7138 va\_list ap; \

7139 va\_start(ap, arg8); \

7140 RETURN\_TYPE ret = \

7141 FUNCNAME##\_fake.custom\_fake\_seq \

7142 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7143 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7144 arg7, arg8, ap); \

7145 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7146 va\_end(ap); \

7147 return ret; \

7148 return FUNCNAME##\_fake \

7149 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7150 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

7151 arg8, ap); \

7152 } \

7153 } \

7154 if (FUNCNAME##\_fake.custom\_fake) { \

7155 RETURN\_TYPE ret; \

7156 va\_list ap; \

7157 va\_start(ap, arg8); \

7158 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

7159 arg6, arg7, arg8, ap); \

7160 va\_end(ap); \

7161 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7162 return ret; \

7163 } \

7164 RETURN\_FAKE\_RESULT(FUNCNAME) \

7165 } \

7166 DEFINE\_RESET\_FUNCTION(FUNCNAME)

7167

[ 7168](fff_8h.md#a548e2d8519f4215b0333d3852d2ac476)#define FAKE\_VALUE\_FUNC10\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7169 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

7170 ...) \

7171 DECLARE\_FAKE\_VALUE\_FUNC10\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7172 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7173 ARG8\_TYPE, ...) \

7174 DEFINE\_FAKE\_VALUE\_FUNC10\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7175 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7176 ARG8\_TYPE, ...)

7177

[ 7178](fff_8h.md#a8ed97e9f471e28dcba2bb8be13144f40)#define DECLARE\_FAKE\_VALUE\_FUNC11\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7179 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7180 ARG8\_TYPE, ARG9\_TYPE, ...) \

7181 typedef struct FUNCNAME##\_Fake { \

7182 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

7183 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

7184 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

7185 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

7186 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

7187 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

7188 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

7189 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

7190 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

7191 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

7192 DECLARE\_ALL\_FUNC\_COMMON \

7193 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

7194 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

7195 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

7196 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

7197 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7198 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7199 va\_list ap); \

7200 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

7201 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7202 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7203 va\_list ap); \

7204 } FUNCNAME##\_Fake; \

7205 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

7206 void FUNCNAME##\_reset(void); \

7207 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7208 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7209 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7210 ...);

7211

[ 7212](fff_8h.md#ab864891f3dfce47bdb9dbfc9df572510)#define DEFINE\_FAKE\_VALUE\_FUNC11\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7213 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7214 ARG8\_TYPE, ARG9\_TYPE, ...) \

7215 FUNCNAME##\_Fake FUNCNAME##\_fake; \

7216 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7217 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7218 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7219 ...) \

7220 { \

7221 SAVE\_ARG(FUNCNAME, 0); \

7222 SAVE\_ARG(FUNCNAME, 1); \

7223 SAVE\_ARG(FUNCNAME, 2); \

7224 SAVE\_ARG(FUNCNAME, 3); \

7225 SAVE\_ARG(FUNCNAME, 4); \

7226 SAVE\_ARG(FUNCNAME, 5); \

7227 SAVE\_ARG(FUNCNAME, 6); \

7228 SAVE\_ARG(FUNCNAME, 7); \

7229 SAVE\_ARG(FUNCNAME, 8); \

7230 SAVE\_ARG(FUNCNAME, 9); \

7231 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

7232 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

7233 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

7234 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

7235 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

7236 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

7237 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

7238 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

7239 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

7240 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

7241 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

7242 } else { \

7243 HISTORY\_DROPPED(FUNCNAME); \

7244 } \

7245 INCREMENT\_CALL\_COUNT(FUNCNAME); \

7246 REGISTER\_CALL(FUNCNAME); \

7247 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

7248 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

7249 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

7250 va\_list ap; \

7251 va\_start(ap, arg9); \

7252 RETURN\_TYPE ret = \

7253 FUNCNAME##\_fake.custom\_fake\_seq \

7254 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

7255 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7256 arg7, arg8, arg9, ap); \

7257 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7258 va\_end(ap); \

7259 return ret; \

7260 } else { \

7261 va\_list ap; \

7262 va\_start(ap, arg9); \

7263 RETURN\_TYPE ret = \

7264 FUNCNAME##\_fake.custom\_fake\_seq \

7265 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7266 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7267 arg7, arg8, arg9, ap); \

7268 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7269 va\_end(ap); \

7270 return ret; \

7271 return FUNCNAME##\_fake \

7272 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7273 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

7274 arg8, arg9, ap); \

7275 } \

7276 } \

7277 if (FUNCNAME##\_fake.custom\_fake) { \

7278 RETURN\_TYPE ret; \

7279 va\_list ap; \

7280 va\_start(ap, arg9); \

7281 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

7282 arg6, arg7, arg8, arg9, ap); \

7283 va\_end(ap); \

7284 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7285 return ret; \

7286 } \

7287 RETURN\_FAKE\_RESULT(FUNCNAME) \

7288 } \

7289 DEFINE\_RESET\_FUNCTION(FUNCNAME)

7290

[ 7291](fff_8h.md#a7644ee914444059dd72fff3c31c3493c)#define FAKE\_VALUE\_FUNC11\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7292 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

7293 ARG9\_TYPE, ...) \

7294 DECLARE\_FAKE\_VALUE\_FUNC11\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7295 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7296 ARG8\_TYPE, ARG9\_TYPE, ...) \

7297 DEFINE\_FAKE\_VALUE\_FUNC11\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7298 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7299 ARG8\_TYPE, ARG9\_TYPE, ...)

7300

[ 7301](fff_8h.md#a2c0649135693216866dd3ba3e4eecd74)#define DECLARE\_FAKE\_VALUE\_FUNC12\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7302 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7303 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ...) \

7304 typedef struct FUNCNAME##\_Fake { \

7305 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

7306 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

7307 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

7308 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

7309 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

7310 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

7311 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

7312 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

7313 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

7314 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

7315 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

7316 DECLARE\_ALL\_FUNC\_COMMON \

7317 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

7318 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

7319 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

7320 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

7321 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7322 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7323 ARG10\_TYPE, va\_list ap); \

7324 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

7325 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7326 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7327 ARG10\_TYPE, va\_list ap); \

7328 } FUNCNAME##\_Fake; \

7329 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

7330 void FUNCNAME##\_reset(void); \

7331 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7332 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7333 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7334 ARG10\_TYPE arg10, ...);

7335

[ 7336](fff_8h.md#a617ca5c38fa77a4373f57ea2569aa147)#define DEFINE\_FAKE\_VALUE\_FUNC12\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7337 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7338 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ...) \

7339 FUNCNAME##\_Fake FUNCNAME##\_fake; \

7340 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7341 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7342 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7343 ARG10\_TYPE arg10, ...) \

7344 { \

7345 SAVE\_ARG(FUNCNAME, 0); \

7346 SAVE\_ARG(FUNCNAME, 1); \

7347 SAVE\_ARG(FUNCNAME, 2); \

7348 SAVE\_ARG(FUNCNAME, 3); \

7349 SAVE\_ARG(FUNCNAME, 4); \

7350 SAVE\_ARG(FUNCNAME, 5); \

7351 SAVE\_ARG(FUNCNAME, 6); \

7352 SAVE\_ARG(FUNCNAME, 7); \

7353 SAVE\_ARG(FUNCNAME, 8); \

7354 SAVE\_ARG(FUNCNAME, 9); \

7355 SAVE\_ARG(FUNCNAME, 10); \

7356 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

7357 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

7358 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

7359 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

7360 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

7361 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

7362 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

7363 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

7364 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

7365 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

7366 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

7367 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

7368 } else { \

7369 HISTORY\_DROPPED(FUNCNAME); \

7370 } \

7371 INCREMENT\_CALL\_COUNT(FUNCNAME); \

7372 REGISTER\_CALL(FUNCNAME); \

7373 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

7374 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

7375 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

7376 va\_list ap; \

7377 va\_start(ap, arg10); \

7378 RETURN\_TYPE ret = \

7379 FUNCNAME##\_fake.custom\_fake\_seq \

7380 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

7381 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7382 arg7, arg8, arg9, arg10, ap); \

7383 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7384 va\_end(ap); \

7385 return ret; \

7386 } else { \

7387 va\_list ap; \

7388 va\_start(ap, arg10); \

7389 RETURN\_TYPE ret = \

7390 FUNCNAME##\_fake.custom\_fake\_seq \

7391 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7392 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7393 arg7, arg8, arg9, arg10, ap); \

7394 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7395 va\_end(ap); \

7396 return ret; \

7397 return FUNCNAME##\_fake \

7398 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7399 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

7400 arg8, arg9, arg10, ap); \

7401 } \

7402 } \

7403 if (FUNCNAME##\_fake.custom\_fake) { \

7404 RETURN\_TYPE ret; \

7405 va\_list ap; \

7406 va\_start(ap, arg10); \

7407 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

7408 arg6, arg7, arg8, arg9, arg10, ap); \

7409 va\_end(ap); \

7410 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7411 return ret; \

7412 } \

7413 RETURN\_FAKE\_RESULT(FUNCNAME) \

7414 } \

7415 DEFINE\_RESET\_FUNCTION(FUNCNAME)

7416

[ 7417](fff_8h.md#a42f90a86851e2098b1eab28e1295e915)#define FAKE\_VALUE\_FUNC12\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7418 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

7419 ARG9\_TYPE, ARG10\_TYPE, ...) \

7420 DECLARE\_FAKE\_VALUE\_FUNC12\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7421 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7422 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ...) \

7423 DEFINE\_FAKE\_VALUE\_FUNC12\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7424 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7425 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ...)

7426

[ 7427](fff_8h.md#af7d9d104dd399230a29df38f0f6e4218)#define DECLARE\_FAKE\_VALUE\_FUNC13\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7428 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7429 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...) \

7430 typedef struct FUNCNAME##\_Fake { \

7431 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

7432 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

7433 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

7434 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

7435 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

7436 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

7437 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

7438 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

7439 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

7440 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

7441 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

7442 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

7443 DECLARE\_ALL\_FUNC\_COMMON \

7444 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

7445 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

7446 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

7447 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

7448 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7449 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7450 ARG10\_TYPE, ARG11\_TYPE, va\_list ap); \

7451 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

7452 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7453 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7454 ARG10\_TYPE, ARG11\_TYPE, va\_list ap); \

7455 } FUNCNAME##\_Fake; \

7456 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

7457 void FUNCNAME##\_reset(void); \

7458 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7459 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7460 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7461 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ...);

7462

[ 7463](fff_8h.md#ac1df4c398ebc5513f0d4cf74fc05fc26)#define DEFINE\_FAKE\_VALUE\_FUNC13\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7464 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7465 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...) \

7466 FUNCNAME##\_Fake FUNCNAME##\_fake; \

7467 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7468 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7469 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7470 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ...) \

7471 { \

7472 SAVE\_ARG(FUNCNAME, 0); \

7473 SAVE\_ARG(FUNCNAME, 1); \

7474 SAVE\_ARG(FUNCNAME, 2); \

7475 SAVE\_ARG(FUNCNAME, 3); \

7476 SAVE\_ARG(FUNCNAME, 4); \

7477 SAVE\_ARG(FUNCNAME, 5); \

7478 SAVE\_ARG(FUNCNAME, 6); \

7479 SAVE\_ARG(FUNCNAME, 7); \

7480 SAVE\_ARG(FUNCNAME, 8); \

7481 SAVE\_ARG(FUNCNAME, 9); \

7482 SAVE\_ARG(FUNCNAME, 10); \

7483 SAVE\_ARG(FUNCNAME, 11); \

7484 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

7485 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

7486 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

7487 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

7488 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

7489 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

7490 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

7491 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

7492 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

7493 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

7494 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

7495 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

7496 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

7497 } else { \

7498 HISTORY\_DROPPED(FUNCNAME); \

7499 } \

7500 INCREMENT\_CALL\_COUNT(FUNCNAME); \

7501 REGISTER\_CALL(FUNCNAME); \

7502 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

7503 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

7504 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

7505 va\_list ap; \

7506 va\_start(ap, arg11); \

7507 RETURN\_TYPE ret = \

7508 FUNCNAME##\_fake.custom\_fake\_seq \

7509 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

7510 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7511 arg7, arg8, arg9, arg10, arg11, ap); \

7512 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7513 va\_end(ap); \

7514 return ret; \

7515 } else { \

7516 va\_list ap; \

7517 va\_start(ap, arg11); \

7518 RETURN\_TYPE ret = \

7519 FUNCNAME##\_fake.custom\_fake\_seq \

7520 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7521 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7522 arg7, arg8, arg9, arg10, arg11, ap); \

7523 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7524 va\_end(ap); \

7525 return ret; \

7526 return FUNCNAME##\_fake \

7527 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7528 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

7529 arg8, arg9, arg10, arg11, ap); \

7530 } \

7531 } \

7532 if (FUNCNAME##\_fake.custom\_fake) { \

7533 RETURN\_TYPE ret; \

7534 va\_list ap; \

7535 va\_start(ap, arg11); \

7536 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

7537 arg6, arg7, arg8, arg9, arg10, arg11, \

7538 ap); \

7539 va\_end(ap); \

7540 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7541 return ret; \

7542 } \

7543 RETURN\_FAKE\_RESULT(FUNCNAME) \

7544 } \

7545 DEFINE\_RESET\_FUNCTION(FUNCNAME)

7546

[ 7547](fff_8h.md#ade58c9f6c27408a675db113cf26fb513)#define FAKE\_VALUE\_FUNC13\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7548 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

7549 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...) \

7550 DECLARE\_FAKE\_VALUE\_FUNC13\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7551 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7552 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...) \

7553 DEFINE\_FAKE\_VALUE\_FUNC13\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7554 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7555 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ...)

7556

[ 7557](fff_8h.md#ac8aef7fc8156bb0a3737c208ac8bf4b0)#define DECLARE\_FAKE\_VALUE\_FUNC14\_VARARG( \

7558 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7559 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ...) \

7560 typedef struct FUNCNAME##\_Fake { \

7561 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

7562 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

7563 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

7564 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

7565 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

7566 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

7567 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

7568 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

7569 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

7570 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

7571 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

7572 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

7573 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

7574 DECLARE\_ALL\_FUNC\_COMMON \

7575 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

7576 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

7577 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

7578 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

7579 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7580 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7581 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, va\_list ap); \

7582 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

7583 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7584 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7585 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, va\_list ap); \

7586 } FUNCNAME##\_Fake; \

7587 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

7588 void FUNCNAME##\_reset(void); \

7589 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7590 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7591 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7592 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ...);

7593

[ 7594](fff_8h.md#a2f332c7e95a85a63827811513d929f65)#define DEFINE\_FAKE\_VALUE\_FUNC14\_VARARG( \

7595 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7596 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ...) \

7597 FUNCNAME##\_Fake FUNCNAME##\_fake; \

7598 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7599 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7600 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7601 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ...) \

7602 { \

7603 SAVE\_ARG(FUNCNAME, 0); \

7604 SAVE\_ARG(FUNCNAME, 1); \

7605 SAVE\_ARG(FUNCNAME, 2); \

7606 SAVE\_ARG(FUNCNAME, 3); \

7607 SAVE\_ARG(FUNCNAME, 4); \

7608 SAVE\_ARG(FUNCNAME, 5); \

7609 SAVE\_ARG(FUNCNAME, 6); \

7610 SAVE\_ARG(FUNCNAME, 7); \

7611 SAVE\_ARG(FUNCNAME, 8); \

7612 SAVE\_ARG(FUNCNAME, 9); \

7613 SAVE\_ARG(FUNCNAME, 10); \

7614 SAVE\_ARG(FUNCNAME, 11); \

7615 SAVE\_ARG(FUNCNAME, 12); \

7616 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

7617 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

7618 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

7619 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

7620 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

7621 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

7622 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

7623 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

7624 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

7625 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

7626 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

7627 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

7628 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

7629 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

7630 } else { \

7631 HISTORY\_DROPPED(FUNCNAME); \

7632 } \

7633 INCREMENT\_CALL\_COUNT(FUNCNAME); \

7634 REGISTER\_CALL(FUNCNAME); \

7635 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

7636 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

7637 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

7638 va\_list ap; \

7639 va\_start(ap, arg12); \

7640 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

7641 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

7642 arg0, arg1, arg2, arg3, arg4, \

7643 arg5, arg6, arg7, arg8, arg9, \

7644 arg10, arg11, arg12, ap); \

7645 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7646 va\_end(ap); \

7647 return ret; \

7648 } else { \

7649 va\_list ap; \

7650 va\_start(ap, arg12); \

7651 RETURN\_TYPE ret = \

7652 FUNCNAME##\_fake.custom\_fake\_seq \

7653 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7654 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7655 arg7, arg8, arg9, arg10, arg11, arg12, \

7656 ap); \

7657 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7658 va\_end(ap); \

7659 return ret; \

7660 return FUNCNAME##\_fake \

7661 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7662 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

7663 arg8, arg9, arg10, arg11, arg12, ap); \

7664 } \

7665 } \

7666 if (FUNCNAME##\_fake.custom\_fake) { \

7667 RETURN\_TYPE ret; \

7668 va\_list ap; \

7669 va\_start(ap, arg12); \

7670 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

7671 arg6, arg7, arg8, arg9, arg10, arg11, \

7672 arg12, ap); \

7673 va\_end(ap); \

7674 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7675 return ret; \

7676 } \

7677 RETURN\_FAKE\_RESULT(FUNCNAME) \

7678 } \

7679 DEFINE\_RESET\_FUNCTION(FUNCNAME)

7680

[ 7681](fff_8h.md#adbc16d4d9917f40986035301f6036798)#define FAKE\_VALUE\_FUNC14\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7682 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

7683 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ...) \

7684 DECLARE\_FAKE\_VALUE\_FUNC14\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7685 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7686 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7687 ...) \

7688 DEFINE\_FAKE\_VALUE\_FUNC14\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7689 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7690 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7691 ...)

7692

[ 7693](fff_8h.md#ad10b8b34bff18c89db11ba209b357bf8)#define DECLARE\_FAKE\_VALUE\_FUNC15\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7694 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7695 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7696 ARG13\_TYPE, ...) \

7697 typedef struct FUNCNAME##\_Fake { \

7698 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

7699 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

7700 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

7701 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

7702 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

7703 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

7704 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

7705 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

7706 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

7707 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

7708 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

7709 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

7710 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

7711 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

7712 DECLARE\_ALL\_FUNC\_COMMON \

7713 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

7714 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

7715 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

7716 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

7717 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7718 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7719 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

7720 va\_list ap); \

7721 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

7722 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7723 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7724 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

7725 va\_list ap); \

7726 } FUNCNAME##\_Fake; \

7727 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

7728 void FUNCNAME##\_reset(void); \

7729 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7730 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7731 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7732 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, ...);

7733

[ 7734](fff_8h.md#a443698c58358056723e784aaa43a7393)#define DEFINE\_FAKE\_VALUE\_FUNC15\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7735 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7736 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7737 ARG13\_TYPE, ...) \

7738 FUNCNAME##\_Fake FUNCNAME##\_fake; \

7739 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7740 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7741 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7742 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, ...) \

7743 { \

7744 SAVE\_ARG(FUNCNAME, 0); \

7745 SAVE\_ARG(FUNCNAME, 1); \

7746 SAVE\_ARG(FUNCNAME, 2); \

7747 SAVE\_ARG(FUNCNAME, 3); \

7748 SAVE\_ARG(FUNCNAME, 4); \

7749 SAVE\_ARG(FUNCNAME, 5); \

7750 SAVE\_ARG(FUNCNAME, 6); \

7751 SAVE\_ARG(FUNCNAME, 7); \

7752 SAVE\_ARG(FUNCNAME, 8); \

7753 SAVE\_ARG(FUNCNAME, 9); \

7754 SAVE\_ARG(FUNCNAME, 10); \

7755 SAVE\_ARG(FUNCNAME, 11); \

7756 SAVE\_ARG(FUNCNAME, 12); \

7757 SAVE\_ARG(FUNCNAME, 13); \

7758 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

7759 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

7760 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

7761 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

7762 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

7763 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

7764 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

7765 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

7766 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

7767 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

7768 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

7769 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

7770 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

7771 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

7772 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

7773 } else { \

7774 HISTORY\_DROPPED(FUNCNAME); \

7775 } \

7776 INCREMENT\_CALL\_COUNT(FUNCNAME); \

7777 REGISTER\_CALL(FUNCNAME); \

7778 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

7779 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

7780 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

7781 va\_list ap; \

7782 va\_start(ap, arg13); \

7783 RETURN\_TYPE ret = FUNCNAME##\_fake.custom\_fake\_seq \

7784 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

7785 arg0, arg1, arg2, arg3, arg4, \

7786 arg5, arg6, arg7, arg8, arg9, \

7787 arg10, arg11, arg12, arg13, ap); \

7788 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7789 va\_end(ap); \

7790 return ret; \

7791 } else { \

7792 va\_list ap; \

7793 va\_start(ap, arg13); \

7794 RETURN\_TYPE ret = \

7795 FUNCNAME##\_fake.custom\_fake\_seq \

7796 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7797 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7798 arg7, arg8, arg9, arg10, arg11, arg12, \

7799 arg13, ap); \

7800 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7801 va\_end(ap); \

7802 return ret; \

7803 return FUNCNAME##\_fake \

7804 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7805 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

7806 arg8, arg9, arg10, arg11, arg12, arg13, ap); \

7807 } \

7808 } \

7809 if (FUNCNAME##\_fake.custom\_fake) { \

7810 RETURN\_TYPE ret; \

7811 va\_list ap; \

7812 va\_start(ap, arg13); \

7813 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

7814 arg6, arg7, arg8, arg9, arg10, arg11, \

7815 arg12, arg13, ap); \

7816 va\_end(ap); \

7817 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7818 return ret; \

7819 } \

7820 RETURN\_FAKE\_RESULT(FUNCNAME) \

7821 } \

7822 DEFINE\_RESET\_FUNCTION(FUNCNAME)

7823

[ 7824](fff_8h.md#a8a743f3140d8dc842fcb428a7e1b3ef6)#define FAKE\_VALUE\_FUNC15\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7825 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

7826 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, ...) \

7827 DECLARE\_FAKE\_VALUE\_FUNC15\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7828 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7829 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7830 ARG13\_TYPE, ...) \

7831 DEFINE\_FAKE\_VALUE\_FUNC15\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7832 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7833 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7834 ARG13\_TYPE, ...)

7835

[ 7836](fff_8h.md#ae5075eeaae885b3753dbe384804d967d)#define DECLARE\_FAKE\_VALUE\_FUNC16\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7837 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7838 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7839 ARG13\_TYPE, ARG14\_TYPE, ...) \

7840 typedef struct FUNCNAME##\_Fake { \

7841 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

7842 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

7843 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

7844 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

7845 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

7846 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

7847 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

7848 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

7849 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

7850 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

7851 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

7852 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

7853 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

7854 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

7855 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

7856 DECLARE\_ALL\_FUNC\_COMMON \

7857 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

7858 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

7859 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

7860 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

7861 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7862 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7863 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

7864 ARG14\_TYPE, va\_list ap); \

7865 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

7866 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

7867 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

7868 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

7869 ARG14\_TYPE, va\_list ap); \

7870 } FUNCNAME##\_Fake; \

7871 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

7872 void FUNCNAME##\_reset(void); \

7873 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7874 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7875 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7876 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

7877 ARG14\_TYPE arg14, ...);

7878

[ 7879](fff_8h.md#a746f44d12427084add654d09718b62b3)#define DEFINE\_FAKE\_VALUE\_FUNC16\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7880 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7881 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7882 ARG13\_TYPE, ARG14\_TYPE, ...) \

7883 FUNCNAME##\_Fake FUNCNAME##\_fake; \

7884 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

7885 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

7886 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

7887 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

7888 ARG14\_TYPE arg14, ...) \

7889 { \

7890 SAVE\_ARG(FUNCNAME, 0); \

7891 SAVE\_ARG(FUNCNAME, 1); \

7892 SAVE\_ARG(FUNCNAME, 2); \

7893 SAVE\_ARG(FUNCNAME, 3); \

7894 SAVE\_ARG(FUNCNAME, 4); \

7895 SAVE\_ARG(FUNCNAME, 5); \

7896 SAVE\_ARG(FUNCNAME, 6); \

7897 SAVE\_ARG(FUNCNAME, 7); \

7898 SAVE\_ARG(FUNCNAME, 8); \

7899 SAVE\_ARG(FUNCNAME, 9); \

7900 SAVE\_ARG(FUNCNAME, 10); \

7901 SAVE\_ARG(FUNCNAME, 11); \

7902 SAVE\_ARG(FUNCNAME, 12); \

7903 SAVE\_ARG(FUNCNAME, 13); \

7904 SAVE\_ARG(FUNCNAME, 14); \

7905 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

7906 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

7907 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

7908 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

7909 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

7910 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

7911 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

7912 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

7913 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

7914 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

7915 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

7916 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

7917 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

7918 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

7919 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

7920 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

7921 } else { \

7922 HISTORY\_DROPPED(FUNCNAME); \

7923 } \

7924 INCREMENT\_CALL\_COUNT(FUNCNAME); \

7925 REGISTER\_CALL(FUNCNAME); \

7926 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

7927 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

7928 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

7929 va\_list ap; \

7930 va\_start(ap, arg14); \

7931 RETURN\_TYPE ret = \

7932 FUNCNAME##\_fake.custom\_fake\_seq \

7933 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

7934 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7935 arg7, arg8, arg9, arg10, arg11, arg12, \

7936 arg13, arg14, ap); \

7937 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7938 va\_end(ap); \

7939 return ret; \

7940 } else { \

7941 va\_list ap; \

7942 va\_start(ap, arg14); \

7943 RETURN\_TYPE ret = \

7944 FUNCNAME##\_fake.custom\_fake\_seq \

7945 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7946 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

7947 arg7, arg8, arg9, arg10, arg11, arg12, \

7948 arg13, arg14, ap); \

7949 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7950 va\_end(ap); \

7951 return ret; \

7952 return FUNCNAME##\_fake \

7953 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

7954 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

7955 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

7956 ap); \

7957 } \

7958 } \

7959 if (FUNCNAME##\_fake.custom\_fake) { \

7960 RETURN\_TYPE ret; \

7961 va\_list ap; \

7962 va\_start(ap, arg14); \

7963 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

7964 arg6, arg7, arg8, arg9, arg10, arg11, \

7965 arg12, arg13, arg14, ap); \

7966 va\_end(ap); \

7967 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

7968 return ret; \

7969 } \

7970 RETURN\_FAKE\_RESULT(FUNCNAME) \

7971 } \

7972 DEFINE\_RESET\_FUNCTION(FUNCNAME)

7973

[ 7974](fff_8h.md#a386d3e4a3498c39e848d0d0128bc63b8)#define FAKE\_VALUE\_FUNC16\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7975 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

7976 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

7977 ARG14\_TYPE, ...) \

7978 DECLARE\_FAKE\_VALUE\_FUNC16\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7979 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7980 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7981 ARG13\_TYPE, ARG14\_TYPE, ...) \

7982 DEFINE\_FAKE\_VALUE\_FUNC16\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7983 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7984 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7985 ARG13\_TYPE, ARG14\_TYPE, ...)

7986

[ 7987](fff_8h.md#a8f6fe5cc2130029e5a81455760704466)#define DECLARE\_FAKE\_VALUE\_FUNC17\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

7988 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

7989 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

7990 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ...) \

7991 typedef struct FUNCNAME##\_Fake { \

7992 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

7993 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

7994 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

7995 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

7996 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

7997 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

7998 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

7999 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

8000 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

8001 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

8002 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

8003 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

8004 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

8005 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

8006 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

8007 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

8008 DECLARE\_ALL\_FUNC\_COMMON \

8009 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

8010 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

8011 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

8012 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

8013 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8014 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

8015 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8016 ARG14\_TYPE, ARG15\_TYPE, va\_list ap); \

8017 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

8018 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8019 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

8020 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8021 ARG14\_TYPE, ARG15\_TYPE, va\_list ap); \

8022 } FUNCNAME##\_Fake; \

8023 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

8024 void FUNCNAME##\_reset(void); \

8025 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

8026 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

8027 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

8028 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

8029 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ...);

8030

[ 8031](fff_8h.md#af6cb9d0ec0fe20c8c12d7db33dc98043)#define DEFINE\_FAKE\_VALUE\_FUNC17\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8032 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8033 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8034 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ...) \

8035 FUNCNAME##\_Fake FUNCNAME##\_fake; \

8036 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

8037 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

8038 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

8039 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

8040 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ...) \

8041 { \

8042 SAVE\_ARG(FUNCNAME, 0); \

8043 SAVE\_ARG(FUNCNAME, 1); \

8044 SAVE\_ARG(FUNCNAME, 2); \

8045 SAVE\_ARG(FUNCNAME, 3); \

8046 SAVE\_ARG(FUNCNAME, 4); \

8047 SAVE\_ARG(FUNCNAME, 5); \

8048 SAVE\_ARG(FUNCNAME, 6); \

8049 SAVE\_ARG(FUNCNAME, 7); \

8050 SAVE\_ARG(FUNCNAME, 8); \

8051 SAVE\_ARG(FUNCNAME, 9); \

8052 SAVE\_ARG(FUNCNAME, 10); \

8053 SAVE\_ARG(FUNCNAME, 11); \

8054 SAVE\_ARG(FUNCNAME, 12); \

8055 SAVE\_ARG(FUNCNAME, 13); \

8056 SAVE\_ARG(FUNCNAME, 14); \

8057 SAVE\_ARG(FUNCNAME, 15); \

8058 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

8059 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

8060 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

8061 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

8062 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

8063 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

8064 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

8065 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

8066 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

8067 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

8068 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

8069 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

8070 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

8071 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

8072 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

8073 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

8074 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

8075 } else { \

8076 HISTORY\_DROPPED(FUNCNAME); \

8077 } \

8078 INCREMENT\_CALL\_COUNT(FUNCNAME); \

8079 REGISTER\_CALL(FUNCNAME); \

8080 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

8081 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

8082 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

8083 va\_list ap; \

8084 va\_start(ap, arg15); \

8085 RETURN\_TYPE ret = \

8086 FUNCNAME##\_fake.custom\_fake\_seq \

8087 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

8088 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

8089 arg7, arg8, arg9, arg10, arg11, arg12, \

8090 arg13, arg14, arg15, ap); \

8091 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8092 va\_end(ap); \

8093 return ret; \

8094 } else { \

8095 va\_list ap; \

8096 va\_start(ap, arg15); \

8097 RETURN\_TYPE ret = \

8098 FUNCNAME##\_fake.custom\_fake\_seq \

8099 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

8100 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

8101 arg7, arg8, arg9, arg10, arg11, arg12, \

8102 arg13, arg14, arg15, ap); \

8103 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8104 va\_end(ap); \

8105 return ret; \

8106 return FUNCNAME##\_fake \

8107 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

8108 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

8109 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

8110 arg15, ap); \

8111 } \

8112 } \

8113 if (FUNCNAME##\_fake.custom\_fake) { \

8114 RETURN\_TYPE ret; \

8115 va\_list ap; \

8116 va\_start(ap, arg15); \

8117 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

8118 arg6, arg7, arg8, arg9, arg10, arg11, \

8119 arg12, arg13, arg14, arg15, ap); \

8120 va\_end(ap); \

8121 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8122 return ret; \

8123 } \

8124 RETURN\_FAKE\_RESULT(FUNCNAME) \

8125 } \

8126 DEFINE\_RESET\_FUNCTION(FUNCNAME)

8127

[ 8128](fff_8h.md#a44a01d946d96a7276392967f399d3c04)#define FAKE\_VALUE\_FUNC17\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8129 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

8130 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8131 ARG14\_TYPE, ARG15\_TYPE, ...) \

8132 DECLARE\_FAKE\_VALUE\_FUNC17\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8133 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8134 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8135 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ...) \

8136 DEFINE\_FAKE\_VALUE\_FUNC17\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8137 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8138 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8139 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ...)

8140

[ 8141](fff_8h.md#aaae630900f1772772db8b3b825401109)#define DECLARE\_FAKE\_VALUE\_FUNC18\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8142 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8143 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8144 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...) \

8145 typedef struct FUNCNAME##\_Fake { \

8146 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

8147 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

8148 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

8149 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

8150 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

8151 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

8152 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

8153 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

8154 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

8155 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

8156 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

8157 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

8158 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

8159 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

8160 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

8161 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

8162 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

8163 DECLARE\_ALL\_FUNC\_COMMON \

8164 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

8165 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

8166 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

8167 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

8168 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8169 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

8170 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8171 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, va\_list ap); \

8172 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

8173 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8174 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

8175 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8176 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, va\_list ap); \

8177 } FUNCNAME##\_Fake; \

8178 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

8179 void FUNCNAME##\_reset(void); \

8180 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

8181 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

8182 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

8183 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

8184 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ...);

8185

[ 8186](fff_8h.md#a3fda8602ff37f8f4b6161fa2ff3a6a2c)#define DEFINE\_FAKE\_VALUE\_FUNC18\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8187 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8188 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8189 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...) \

8190 FUNCNAME##\_Fake FUNCNAME##\_fake; \

8191 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

8192 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

8193 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

8194 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

8195 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ...) \

8196 { \

8197 SAVE\_ARG(FUNCNAME, 0); \

8198 SAVE\_ARG(FUNCNAME, 1); \

8199 SAVE\_ARG(FUNCNAME, 2); \

8200 SAVE\_ARG(FUNCNAME, 3); \

8201 SAVE\_ARG(FUNCNAME, 4); \

8202 SAVE\_ARG(FUNCNAME, 5); \

8203 SAVE\_ARG(FUNCNAME, 6); \

8204 SAVE\_ARG(FUNCNAME, 7); \

8205 SAVE\_ARG(FUNCNAME, 8); \

8206 SAVE\_ARG(FUNCNAME, 9); \

8207 SAVE\_ARG(FUNCNAME, 10); \

8208 SAVE\_ARG(FUNCNAME, 11); \

8209 SAVE\_ARG(FUNCNAME, 12); \

8210 SAVE\_ARG(FUNCNAME, 13); \

8211 SAVE\_ARG(FUNCNAME, 14); \

8212 SAVE\_ARG(FUNCNAME, 15); \

8213 SAVE\_ARG(FUNCNAME, 16); \

8214 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

8215 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

8216 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

8217 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

8218 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

8219 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

8220 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

8221 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

8222 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

8223 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

8224 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

8225 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

8226 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

8227 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

8228 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

8229 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

8230 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

8231 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

8232 } else { \

8233 HISTORY\_DROPPED(FUNCNAME); \

8234 } \

8235 INCREMENT\_CALL\_COUNT(FUNCNAME); \

8236 REGISTER\_CALL(FUNCNAME); \

8237 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

8238 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

8239 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

8240 va\_list ap; \

8241 va\_start(ap, arg16); \

8242 RETURN\_TYPE ret = \

8243 FUNCNAME##\_fake.custom\_fake\_seq \

8244 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

8245 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

8246 arg7, arg8, arg9, arg10, arg11, arg12, \

8247 arg13, arg14, arg15, arg16, ap); \

8248 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8249 va\_end(ap); \

8250 return ret; \

8251 } else { \

8252 va\_list ap; \

8253 va\_start(ap, arg16); \

8254 RETURN\_TYPE ret = \

8255 FUNCNAME##\_fake.custom\_fake\_seq \

8256 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

8257 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

8258 arg7, arg8, arg9, arg10, arg11, arg12, \

8259 arg13, arg14, arg15, arg16, ap); \

8260 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8261 va\_end(ap); \

8262 return ret; \

8263 return FUNCNAME##\_fake \

8264 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

8265 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

8266 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

8267 arg15, arg16, ap); \

8268 } \

8269 } \

8270 if (FUNCNAME##\_fake.custom\_fake) { \

8271 RETURN\_TYPE ret; \

8272 va\_list ap; \

8273 va\_start(ap, arg16); \

8274 ret = FUNCNAME##\_fake.custom\_fake(arg0, arg1, arg2, arg3, arg4, arg5, \

8275 arg6, arg7, arg8, arg9, arg10, arg11, \

8276 arg12, arg13, arg14, arg15, arg16, ap); \

8277 va\_end(ap); \

8278 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8279 return ret; \

8280 } \

8281 RETURN\_FAKE\_RESULT(FUNCNAME) \

8282 } \

8283 DEFINE\_RESET\_FUNCTION(FUNCNAME)

8284

[ 8285](fff_8h.md#a39c943b89513a64a068958756ad398c0)#define FAKE\_VALUE\_FUNC18\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8286 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

8287 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8288 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...) \

8289 DECLARE\_FAKE\_VALUE\_FUNC18\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8290 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8291 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8292 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...) \

8293 DEFINE\_FAKE\_VALUE\_FUNC18\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8294 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8295 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8296 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ...)

8297

[ 8298](fff_8h.md#ad65f3d0f53936ae4b250455f1fd8c6b2)#define DECLARE\_FAKE\_VALUE\_FUNC19\_VARARG( \

8299 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8300 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8301 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...) \

8302 typedef struct FUNCNAME##\_Fake { \

8303 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

8304 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

8305 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

8306 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

8307 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

8308 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

8309 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

8310 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

8311 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

8312 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

8313 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

8314 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

8315 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

8316 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

8317 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

8318 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

8319 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

8320 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

8321 DECLARE\_ALL\_FUNC\_COMMON \

8322 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

8323 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

8324 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

8325 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

8326 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8327 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

8328 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8329 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

8330 va\_list ap); \

8331 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

8332 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8333 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

8334 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8335 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

8336 va\_list ap); \

8337 } FUNCNAME##\_Fake; \

8338 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

8339 void FUNCNAME##\_reset(void); \

8340 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

8341 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

8342 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

8343 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

8344 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, ...);

8345

[ 8346](fff_8h.md#af7ae4f2d324f4abcb96f189aca9ba4a4)#define DEFINE\_FAKE\_VALUE\_FUNC19\_VARARG( \

8347 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8348 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8349 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...) \

8350 FUNCNAME##\_Fake FUNCNAME##\_fake; \

8351 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

8352 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

8353 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

8354 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

8355 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, ...) \

8356 { \

8357 SAVE\_ARG(FUNCNAME, 0); \

8358 SAVE\_ARG(FUNCNAME, 1); \

8359 SAVE\_ARG(FUNCNAME, 2); \

8360 SAVE\_ARG(FUNCNAME, 3); \

8361 SAVE\_ARG(FUNCNAME, 4); \

8362 SAVE\_ARG(FUNCNAME, 5); \

8363 SAVE\_ARG(FUNCNAME, 6); \

8364 SAVE\_ARG(FUNCNAME, 7); \

8365 SAVE\_ARG(FUNCNAME, 8); \

8366 SAVE\_ARG(FUNCNAME, 9); \

8367 SAVE\_ARG(FUNCNAME, 10); \

8368 SAVE\_ARG(FUNCNAME, 11); \

8369 SAVE\_ARG(FUNCNAME, 12); \

8370 SAVE\_ARG(FUNCNAME, 13); \

8371 SAVE\_ARG(FUNCNAME, 14); \

8372 SAVE\_ARG(FUNCNAME, 15); \

8373 SAVE\_ARG(FUNCNAME, 16); \

8374 SAVE\_ARG(FUNCNAME, 17); \

8375 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

8376 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

8377 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

8378 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

8379 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

8380 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

8381 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

8382 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

8383 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

8384 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

8385 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

8386 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

8387 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

8388 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

8389 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

8390 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

8391 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

8392 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

8393 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

8394 } else { \

8395 HISTORY\_DROPPED(FUNCNAME); \

8396 } \

8397 INCREMENT\_CALL\_COUNT(FUNCNAME); \

8398 REGISTER\_CALL(FUNCNAME); \

8399 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

8400 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

8401 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

8402 va\_list ap; \

8403 va\_start(ap, arg17); \

8404 RETURN\_TYPE ret = \

8405 FUNCNAME##\_fake.custom\_fake\_seq \

8406 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

8407 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

8408 arg7, arg8, arg9, arg10, arg11, arg12, \

8409 arg13, arg14, arg15, arg16, arg17, ap); \

8410 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8411 va\_end(ap); \

8412 return ret; \

8413 } else { \

8414 va\_list ap; \

8415 va\_start(ap, arg17); \

8416 RETURN\_TYPE ret = \

8417 FUNCNAME##\_fake.custom\_fake\_seq \

8418 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

8419 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

8420 arg7, arg8, arg9, arg10, arg11, arg12, \

8421 arg13, arg14, arg15, arg16, arg17, ap); \

8422 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8423 va\_end(ap); \

8424 return ret; \

8425 return FUNCNAME##\_fake \

8426 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

8427 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

8428 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

8429 arg15, arg16, arg17, ap); \

8430 } \

8431 } \

8432 if (FUNCNAME##\_fake.custom\_fake) { \

8433 RETURN\_TYPE ret; \

8434 va\_list ap; \

8435 va\_start(ap, arg17); \

8436 ret = FUNCNAME##\_fake.custom\_fake( \

8437 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

8438 arg11, arg12, arg13, arg14, arg15, arg16, arg17, ap); \

8439 va\_end(ap); \

8440 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8441 return ret; \

8442 } \

8443 RETURN\_FAKE\_RESULT(FUNCNAME) \

8444 } \

8445 DEFINE\_RESET\_FUNCTION(FUNCNAME)

8446

[ 8447](fff_8h.md#a8ce5cddcbf414475e145ba643306bb8a)#define FAKE\_VALUE\_FUNC19\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8448 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

8449 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8450 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...) \

8451 DECLARE\_FAKE\_VALUE\_FUNC19\_VARARG( \

8452 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

8453 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, \

8454 ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...) \

8455 DEFINE\_FAKE\_VALUE\_FUNC19\_VARARG( \

8456 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, \

8457 ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, \

8458 ARG12\_TYPE, ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ...)

8459

[ 8460](fff_8h.md#ae8257da23b3ca173810ccff3be179180)#define DECLARE\_FAKE\_VALUE\_FUNC20\_VARARG( \

8461 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8462 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8463 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ...) \

8464 typedef struct FUNCNAME##\_Fake { \

8465 DECLARE\_ARG(ARG0\_TYPE, 0, FUNCNAME) \

8466 DECLARE\_ARG(ARG1\_TYPE, 1, FUNCNAME) \

8467 DECLARE\_ARG(ARG2\_TYPE, 2, FUNCNAME) \

8468 DECLARE\_ARG(ARG3\_TYPE, 3, FUNCNAME) \

8469 DECLARE\_ARG(ARG4\_TYPE, 4, FUNCNAME) \

8470 DECLARE\_ARG(ARG5\_TYPE, 5, FUNCNAME) \

8471 DECLARE\_ARG(ARG6\_TYPE, 6, FUNCNAME) \

8472 DECLARE\_ARG(ARG7\_TYPE, 7, FUNCNAME) \

8473 DECLARE\_ARG(ARG8\_TYPE, 8, FUNCNAME) \

8474 DECLARE\_ARG(ARG9\_TYPE, 9, FUNCNAME) \

8475 DECLARE\_ARG(ARG10\_TYPE, 10, FUNCNAME) \

8476 DECLARE\_ARG(ARG11\_TYPE, 11, FUNCNAME) \

8477 DECLARE\_ARG(ARG12\_TYPE, 12, FUNCNAME) \

8478 DECLARE\_ARG(ARG13\_TYPE, 13, FUNCNAME) \

8479 DECLARE\_ARG(ARG14\_TYPE, 14, FUNCNAME) \

8480 DECLARE\_ARG(ARG15\_TYPE, 15, FUNCNAME) \

8481 DECLARE\_ARG(ARG16\_TYPE, 16, FUNCNAME) \

8482 DECLARE\_ARG(ARG17\_TYPE, 17, FUNCNAME) \

8483 DECLARE\_ARG(ARG18\_TYPE, 18, FUNCNAME) \

8484 DECLARE\_ALL\_FUNC\_COMMON \

8485 DECLARE\_VALUE\_FUNCTION\_VARIABLES(RETURN\_TYPE) \

8486 DECLARE\_RETURN\_VALUE\_HISTORY(RETURN\_TYPE) \

8487 DECLARE\_CUSTOM\_FAKE\_SEQ\_VARIABLES \

8488 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, custom\_fake, ARG0\_TYPE, ARG1\_TYPE, \

8489 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8490 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

8491 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8492 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

8493 ARG18\_TYPE, va\_list ap); \

8494 CUSTOM\_FFF\_FUNCTION\_TEMPLATE(RETURN\_TYPE, \*custom\_fake\_seq, ARG0\_TYPE, ARG1\_TYPE, \

8495 ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8496 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, \

8497 ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8498 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, \

8499 ARG18\_TYPE, va\_list ap); \

8500 } FUNCNAME##\_Fake; \

8501 extern FUNCNAME##\_Fake FUNCNAME##\_fake; \

8502 void FUNCNAME##\_reset(void); \

8503 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

8504 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

8505 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

8506 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

8507 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

8508 ARG18\_TYPE arg18, ...);

8509

[ 8510](fff_8h.md#af7ec99fb8707830f4a2de63d5f4f7552)#define DEFINE\_FAKE\_VALUE\_FUNC20\_VARARG( \

8511 RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, \

8512 ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8513 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ...) \

8514 FUNCNAME##\_Fake FUNCNAME##\_fake; \

8515 RETURN\_TYPE FFF\_GCC\_FUNCTION\_ATTRIBUTES FUNCNAME( \

8516 ARG0\_TYPE arg0, ARG1\_TYPE arg1, ARG2\_TYPE arg2, ARG3\_TYPE arg3, ARG4\_TYPE arg4, \

8517 ARG5\_TYPE arg5, ARG6\_TYPE arg6, ARG7\_TYPE arg7, ARG8\_TYPE arg8, ARG9\_TYPE arg9, \

8518 ARG10\_TYPE arg10, ARG11\_TYPE arg11, ARG12\_TYPE arg12, ARG13\_TYPE arg13, \

8519 ARG14\_TYPE arg14, ARG15\_TYPE arg15, ARG16\_TYPE arg16, ARG17\_TYPE arg17, \

8520 ARG18\_TYPE arg18, ...) \

8521 { \

8522 SAVE\_ARG(FUNCNAME, 0); \

8523 SAVE\_ARG(FUNCNAME, 1); \

8524 SAVE\_ARG(FUNCNAME, 2); \

8525 SAVE\_ARG(FUNCNAME, 3); \

8526 SAVE\_ARG(FUNCNAME, 4); \

8527 SAVE\_ARG(FUNCNAME, 5); \

8528 SAVE\_ARG(FUNCNAME, 6); \

8529 SAVE\_ARG(FUNCNAME, 7); \

8530 SAVE\_ARG(FUNCNAME, 8); \

8531 SAVE\_ARG(FUNCNAME, 9); \

8532 SAVE\_ARG(FUNCNAME, 10); \

8533 SAVE\_ARG(FUNCNAME, 11); \

8534 SAVE\_ARG(FUNCNAME, 12); \

8535 SAVE\_ARG(FUNCNAME, 13); \

8536 SAVE\_ARG(FUNCNAME, 14); \

8537 SAVE\_ARG(FUNCNAME, 15); \

8538 SAVE\_ARG(FUNCNAME, 16); \

8539 SAVE\_ARG(FUNCNAME, 17); \

8540 SAVE\_ARG(FUNCNAME, 18); \

8541 if (ROOM\_FOR\_MORE\_HISTORY(FUNCNAME)) { \

8542 SAVE\_ARG\_HISTORY(FUNCNAME, 0); \

8543 SAVE\_ARG\_HISTORY(FUNCNAME, 1); \

8544 SAVE\_ARG\_HISTORY(FUNCNAME, 2); \

8545 SAVE\_ARG\_HISTORY(FUNCNAME, 3); \

8546 SAVE\_ARG\_HISTORY(FUNCNAME, 4); \

8547 SAVE\_ARG\_HISTORY(FUNCNAME, 5); \

8548 SAVE\_ARG\_HISTORY(FUNCNAME, 6); \

8549 SAVE\_ARG\_HISTORY(FUNCNAME, 7); \

8550 SAVE\_ARG\_HISTORY(FUNCNAME, 8); \

8551 SAVE\_ARG\_HISTORY(FUNCNAME, 9); \

8552 SAVE\_ARG\_HISTORY(FUNCNAME, 10); \

8553 SAVE\_ARG\_HISTORY(FUNCNAME, 11); \

8554 SAVE\_ARG\_HISTORY(FUNCNAME, 12); \

8555 SAVE\_ARG\_HISTORY(FUNCNAME, 13); \

8556 SAVE\_ARG\_HISTORY(FUNCNAME, 14); \

8557 SAVE\_ARG\_HISTORY(FUNCNAME, 15); \

8558 SAVE\_ARG\_HISTORY(FUNCNAME, 16); \

8559 SAVE\_ARG\_HISTORY(FUNCNAME, 17); \

8560 SAVE\_ARG\_HISTORY(FUNCNAME, 18); \

8561 } else { \

8562 HISTORY\_DROPPED(FUNCNAME); \

8563 } \

8564 INCREMENT\_CALL\_COUNT(FUNCNAME); \

8565 REGISTER\_CALL(FUNCNAME); \

8566 if (FUNCNAME##\_fake.custom\_fake\_seq\_len) { /\* a sequence of custom fakes \*/ \

8567 if (FUNCNAME##\_fake.custom\_fake\_seq\_idx < \

8568 FUNCNAME##\_fake.custom\_fake\_seq\_len) { \

8569 va\_list ap; \

8570 va\_start(ap, arg18); \

8571 RETURN\_TYPE ret = \

8572 FUNCNAME##\_fake.custom\_fake\_seq \

8573 [FUNCNAME##\_fake.custom\_fake\_seq\_idx++]( \

8574 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

8575 arg7, arg8, arg9, arg10, arg11, arg12, \

8576 arg13, arg14, arg15, arg16, arg17, arg18, \

8577 ap); \

8578 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8579 va\_end(ap); \

8580 return ret; \

8581 } else { \

8582 va\_list ap; \

8583 va\_start(ap, arg18); \

8584 RETURN\_TYPE ret = \

8585 FUNCNAME##\_fake.custom\_fake\_seq \

8586 [FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

8587 arg0, arg1, arg2, arg3, arg4, arg5, arg6, \

8588 arg7, arg8, arg9, arg10, arg11, arg12, \

8589 arg13, arg14, arg15, arg16, arg17, arg18, \

8590 ap); \

8591 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8592 va\_end(ap); \

8593 return ret; \

8594 return FUNCNAME##\_fake \

8595 .custom\_fake\_seq[FUNCNAME##\_fake.custom\_fake\_seq\_len - 1]( \

8596 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, \

8597 arg8, arg9, arg10, arg11, arg12, arg13, arg14, \

8598 arg15, arg16, arg17, arg18, ap); \

8599 } \

8600 } \

8601 if (FUNCNAME##\_fake.custom\_fake) { \

8602 RETURN\_TYPE ret; \

8603 va\_list ap; \

8604 va\_start(ap, arg18); \

8605 ret = FUNCNAME##\_fake.custom\_fake( \

8606 arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, \

8607 arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, ap); \

8608 va\_end(ap); \

8609 SAVE\_RET\_HISTORY(FUNCNAME, ret); \

8610 return ret; \

8611 } \

8612 RETURN\_FAKE\_RESULT(FUNCNAME) \

8613 } \

8614 DEFINE\_RESET\_FUNCTION(FUNCNAME)

8615

[ 8616](fff_8h.md#ac6857f08f38fe78385824b2b48c12c38)#define FAKE\_VALUE\_FUNC20\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8617 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, ARG8\_TYPE, \

8618 ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, ARG13\_TYPE, \

8619 ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, ARG17\_TYPE, ARG18\_TYPE, ...) \

8620 DECLARE\_FAKE\_VALUE\_FUNC20\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8621 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8622 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8623 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, \

8624 ARG17\_TYPE, ARG18\_TYPE, ...) \

8625 DEFINE\_FAKE\_VALUE\_FUNC20\_VARARG(RETURN\_TYPE, FUNCNAME, ARG0\_TYPE, ARG1\_TYPE, ARG2\_TYPE, \

8626 ARG3\_TYPE, ARG4\_TYPE, ARG5\_TYPE, ARG6\_TYPE, ARG7\_TYPE, \

8627 ARG8\_TYPE, ARG9\_TYPE, ARG10\_TYPE, ARG11\_TYPE, ARG12\_TYPE, \

8628 ARG13\_TYPE, ARG14\_TYPE, ARG15\_TYPE, ARG16\_TYPE, \

8629 ARG17\_TYPE, ARG18\_TYPE, ...)

8630

8631/\* MSVC expand macro fix \*/

[ 8632](fff_8h.md#ae4b532a93c757194ec73b6790a3e6b1f)#define EXPAND(x) x

8633

[ 8634](fff_8h.md#aed4e92e74d3346203733f847c1fb7c13)#define PP\_NARG\_MINUS2(...) EXPAND(PP\_NARG\_MINUS2\_(\_\_VA\_ARGS\_\_, PP\_RSEQ\_N\_MINUS2()))

8635

[ 8636](fff_8h.md#acdd3fc1d1e62fd3f5da6cc3a0b121e73)#define PP\_NARG\_MINUS2\_(...) EXPAND(PP\_ARG\_MINUS2\_N(\_\_VA\_ARGS\_\_))

8637

[ 8638](fff_8h.md#a9a912895f5250d258e6b634c889c7ad4)#define PP\_ARG\_MINUS2\_N(returnVal, \_0, \_1, \_2, \_3, \_4, \_5, \_6, \_7, \_8, \_9, \_10, \_11, \_12, \_13, \

8639 \_14, \_15, \_16, \_17, \_18, \_19, \_20, N, ...) \

8640 N

8641

[ 8642](fff_8h.md#ad8efeac53da71c035282ee9a13880a14)#define PP\_RSEQ\_N\_MINUS2() 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0

8643

[ 8644](fff_8h.md#ae35e4e10e3c657c61184fb4f80a9d436)#define PP\_NARG\_MINUS1(...) EXPAND(PP\_NARG\_MINUS1\_(\_\_VA\_ARGS\_\_, PP\_RSEQ\_N\_MINUS1()))

8645

[ 8646](fff_8h.md#aa751f94e24b84d18435bb22958c913b9)#define PP\_NARG\_MINUS1\_(...) EXPAND(PP\_ARG\_MINUS1\_N(\_\_VA\_ARGS\_\_))

8647

[ 8648](fff_8h.md#a74c9d9781a319bc4adf2d1847ab41309)#define PP\_ARG\_MINUS1\_N(\_0, \_1, \_2, \_3, \_4, \_5, \_6, \_7, \_8, \_9, \_10, \_11, \_12, \_13, \_14, \_15, \_16, \

8649 \_17, \_18, \_19, \_20, N, ...) \

8650 N

8651

[ 8652](fff_8h.md#acca5a4e5675ac18afa05990b1c7485b7)#define PP\_RSEQ\_N\_MINUS1() 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0

8653

8654/\* DECLARE AND DEFINE FAKE FUNCTIONS - PLACE IN TEST FILES \*/

8655

[ 8656](fff_8h.md#aadc3f4cfe5d96785e3b49be014aa1677)#define FAKE\_VALUE\_FUNC(...) EXPAND(FUNC\_VALUE\_(PP\_NARG\_MINUS2(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8657

[ 8658](fff_8h.md#a8625ed13dfb3b5021bb8d532f2160ff8)#define FUNC\_VALUE\_(N, ...) EXPAND(FUNC\_VALUE\_N(N, \_\_VA\_ARGS\_\_))

8659

[ 8660](fff_8h.md#af0fddd67177d21091ab7d222d8edd6fd)#define FUNC\_VALUE\_N(N, ...) EXPAND(FAKE\_VALUE\_FUNC##N(\_\_VA\_ARGS\_\_))

8661

[ 8662](fff_8h.md#af5e0d3e09a9383ac72a9cb45eb4ed831)#define FAKE\_VOID\_FUNC(...) EXPAND(FUNC\_VOID\_(PP\_NARG\_MINUS1(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8663

[ 8664](fff_8h.md#a857495061e2f86db044bb9f633251c65)#define FUNC\_VOID\_(N, ...) EXPAND(FUNC\_VOID\_N(N, \_\_VA\_ARGS\_\_))

8665

[ 8666](fff_8h.md#ada990ce44fa8e5d9a4caf5927863f36a)#define FUNC\_VOID\_N(N, ...) EXPAND(FAKE\_VOID\_FUNC##N(\_\_VA\_ARGS\_\_))

8667

[ 8668](fff_8h.md#a4e4091beb2608b5c7a929430d4792aec)#define FAKE\_VALUE\_FUNC\_VARARG(...) \

8669 EXPAND(FUNC\_VALUE\_VARARG\_(PP\_NARG\_MINUS2(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8670

[ 8671](fff_8h.md#adb78632deb47379a8285bc264237935f)#define FUNC\_VALUE\_VARARG\_(N, ...) EXPAND(FUNC\_VALUE\_VARARG\_N(N, \_\_VA\_ARGS\_\_))

8672

[ 8673](fff_8h.md#a8bad1e0d559ae90637eb3540a7ee1c86)#define FUNC\_VALUE\_VARARG\_N(N, ...) EXPAND(FAKE\_VALUE\_FUNC##N##\_VARARG(\_\_VA\_ARGS\_\_))

8674

[ 8675](fff_8h.md#ac8b77bf5df60b851a5bd47df4a44f500)#define FAKE\_VOID\_FUNC\_VARARG(...) \

8676 EXPAND(FUNC\_VOID\_VARARG\_(PP\_NARG\_MINUS1(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8677

[ 8678](fff_8h.md#a7a47778eec2fc8899485b5e8ecb54d38)#define FUNC\_VOID\_VARARG\_(N, ...) EXPAND(FUNC\_VOID\_VARARG\_N(N, \_\_VA\_ARGS\_\_))

8679

[ 8680](fff_8h.md#acfe60afe98148f50fde7ec8623a8ef78)#define FUNC\_VOID\_VARARG\_N(N, ...) EXPAND(FAKE\_VOID\_FUNC##N##\_VARARG(\_\_VA\_ARGS\_\_))

8681

8682/\* DECLARE FAKE FUNCTIONS - PLACE IN HEADER FILES \*/

8683

[ 8684](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)#define DECLARE\_FAKE\_VALUE\_FUNC(...) \

8685 EXPAND(DECLARE\_FUNC\_VALUE\_(PP\_NARG\_MINUS2(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8686

[ 8687](fff_8h.md#a87931f735fdb8221f2f4c18146c59c80)#define DECLARE\_FUNC\_VALUE\_(N, ...) EXPAND(DECLARE\_FUNC\_VALUE\_N(N, \_\_VA\_ARGS\_\_))

8688

[ 8689](fff_8h.md#a5b8bdf38c87d97882d04d74f3839b813)#define DECLARE\_FUNC\_VALUE\_N(N, ...) EXPAND(DECLARE\_FAKE\_VALUE\_FUNC##N(\_\_VA\_ARGS\_\_))

8690

[ 8691](fff_8h.md#ab3a6abd531c44d2ec1d249e3e100ff3c)#define DECLARE\_FAKE\_VOID\_FUNC(...) \

8692 EXPAND(DECLARE\_FUNC\_VOID\_(PP\_NARG\_MINUS1(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8693

[ 8694](fff_8h.md#ad87ab733f2f23db8ca737780762de08a)#define DECLARE\_FUNC\_VOID\_(N, ...) EXPAND(DECLARE\_FUNC\_VOID\_N(N, \_\_VA\_ARGS\_\_))

8695

[ 8696](fff_8h.md#a748f971c722172983ee913eddcd314be)#define DECLARE\_FUNC\_VOID\_N(N, ...) EXPAND(DECLARE\_FAKE\_VOID\_FUNC##N(\_\_VA\_ARGS\_\_))

8697

[ 8698](fff_8h.md#a39b335c8e8abf1374f3fa7a0eb33af02)#define DECLARE\_FAKE\_VALUE\_FUNC\_VARARG(...) \

8699 EXPAND(DECLARE\_FUNC\_VALUE\_VARARG\_(PP\_NARG\_MINUS2(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8700

[ 8701](fff_8h.md#ac856370d2778373e8e54051fde2fa989)#define DECLARE\_FUNC\_VALUE\_VARARG\_(N, ...) EXPAND(DECLARE\_FUNC\_VALUE\_VARARG\_N(N, \_\_VA\_ARGS\_\_))

8702

[ 8703](fff_8h.md#ab937c4d965dabb880726bd23da7d6eb3)#define DECLARE\_FUNC\_VALUE\_VARARG\_N(N, ...) EXPAND(DECLARE\_FAKE\_VALUE\_FUNC##N##\_VARARG(\_\_VA\_ARGS\_\_))

8704

[ 8705](fff_8h.md#a5429350244d1df3de79ebef250c246f5)#define DECLARE\_FAKE\_VOID\_FUNC\_VARARG(...) \

8706 EXPAND(DECLARE\_FUNC\_VOID\_VARARG\_(PP\_NARG\_MINUS1(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8707

[ 8708](fff_8h.md#a60434cdb325162d901144a4f819e9838)#define DECLARE\_FUNC\_VOID\_VARARG\_(N, ...) EXPAND(DECLARE\_FUNC\_VOID\_VARARG\_N(N, \_\_VA\_ARGS\_\_))

8709

[ 8710](fff_8h.md#aeb0be3312437c670286bd893b65f5793)#define DECLARE\_FUNC\_VOID\_VARARG\_N(N, ...) EXPAND(DECLARE\_FAKE\_VOID\_FUNC##N##\_VARARG(\_\_VA\_ARGS\_\_))

8711

8712/\* DEFINE FAKE FUNCTIONS - PLACE IN SOURCE FILES \*/

8713

[ 8714](fff_8h.md#a4d9be23c4ca81be38396a83bc94164c0)#define DEFINE\_FAKE\_VALUE\_FUNC(...) \

8715 EXPAND(DEFINE\_FUNC\_VALUE\_(PP\_NARG\_MINUS2(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8716

[ 8717](fff_8h.md#aec6f33309a6e05463eff93190db809ba)#define DEFINE\_FUNC\_VALUE\_(N, ...) EXPAND(DEFINE\_FUNC\_VALUE\_N(N, \_\_VA\_ARGS\_\_))

8718

[ 8719](fff_8h.md#a65ae8b005afece51e4ead99d32402420)#define DEFINE\_FUNC\_VALUE\_N(N, ...) EXPAND(DEFINE\_FAKE\_VALUE\_FUNC##N(\_\_VA\_ARGS\_\_))

8720

[ 8721](fff_8h.md#a1629581dedc52dad4772c16b3c314828)#define DEFINE\_FAKE\_VOID\_FUNC(...) \

8722 EXPAND(DEFINE\_FUNC\_VOID\_(PP\_NARG\_MINUS1(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8723

[ 8724](fff_8h.md#a9647ac5bbd553454c66976056c556b25)#define DEFINE\_FUNC\_VOID\_(N, ...) EXPAND(DEFINE\_FUNC\_VOID\_N(N, \_\_VA\_ARGS\_\_))

8725

[ 8726](fff_8h.md#a5a3498cf3b25c3e6522649a5a25d9345)#define DEFINE\_FUNC\_VOID\_N(N, ...) EXPAND(DEFINE\_FAKE\_VOID\_FUNC##N(\_\_VA\_ARGS\_\_))

8727

[ 8728](fff_8h.md#a196c287be676a9365f5148afbd48963b)#define DEFINE\_FAKE\_VALUE\_FUNC\_VARARG(...) \

8729 EXPAND(DEFINE\_FUNC\_VALUE\_VARARG\_(PP\_NARG\_MINUS2(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8730

[ 8731](fff_8h.md#a361c899a66081746b4fde72592c24951)#define DEFINE\_FUNC\_VALUE\_VARARG\_(N, ...) EXPAND(DEFINE\_FUNC\_VALUE\_VARARG\_N(N, \_\_VA\_ARGS\_\_))

8732

[ 8733](fff_8h.md#ad3d6408954b8ef607d73e2675874ec01)#define DEFINE\_FUNC\_VALUE\_VARARG\_N(N, ...) EXPAND(DEFINE\_FAKE\_VALUE\_FUNC##N##\_VARARG(\_\_VA\_ARGS\_\_))

8734

[ 8735](fff_8h.md#a7ce249593a53d0e2f32384c4bf9c8eb2)#define DEFINE\_FAKE\_VOID\_FUNC\_VARARG(...) \

8736 EXPAND(DEFINE\_FUNC\_VOID\_VARARG\_(PP\_NARG\_MINUS1(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_))

8737

[ 8738](fff_8h.md#a69bd746c1b79978ee0ff2ce43df47284)#define DEFINE\_FUNC\_VOID\_VARARG\_(N, ...) EXPAND(DEFINE\_FUNC\_VOID\_VARARG\_N(N, \_\_VA\_ARGS\_\_))

8739

[ 8740](fff_8h.md#aff7cb4e68c42ad329632d6fbd1d523e8)#define DEFINE\_FUNC\_VOID\_VARARG\_N(N, ...) EXPAND(DEFINE\_FAKE\_VOID\_FUNC##N##\_VARARG(\_\_VA\_ARGS\_\_))

8741

8742#endif /\* FAKE\_FUNCTIONS \*/

[FFF\_END\_EXTERN\_C](fff_8h.md#a159a878a982506014524691639f0d0a4)

#define FFF\_END\_EXTERN\_C

**Definition** fff.h:124

[fff](fff_8h.md#a484e7178f2bbf168acc8ce2111c913f2)

fff\_globals\_t fff

[fff\_function\_t](fff_8h.md#a5a81a0e0882be6192f4f18c7b8d41aa1)

void(\* fff\_function\_t)(void)

**Definition** fff.h:139

[FFF\_CALL\_HISTORY\_LEN](fff_8h.md#a8056b9838c2f7a0defc054404737777b)

#define FFF\_CALL\_HISTORY\_LEN

**Definition** fff.h:37

[FFF\_EXTERN\_C](fff_8h.md#ac3290fea38c680b4048fb9146760c635)

#define FFF\_EXTERN\_C

**Definition** fff.h:123

[string.h](string_8h.md)

[fff\_globals\_t](structfff__globals__t.md)

**Definition** fff.h:140

[fff\_globals\_t::call\_history](structfff__globals__t.md#a22ffdf4369472e55dbdf96ae898ca4cf)

fff\_function\_t call\_history[(50u)]

**Definition** fff.h:141

[fff\_globals\_t::call\_history\_idx](structfff__globals__t.md#ad5c29f2faa27bef5e706417cd2a73eb5)

unsigned int call\_history\_idx

**Definition** fff.h:142

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [fff.h](fff_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
