---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uart__internal_8h_source.html
original_path: doxygen/html/uart__internal_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_internal.h

[Go to the documentation of this file.](uart__internal_8h.md)

1/\*

2 \* Copyright (c) 2018-2019 Nordic Semiconductor ASA

3 \* Copyright (c) 2015 Wind River Systems, Inc.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_UART\_UART\_INTERNAL\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_UART\_UART\_INTERNAL\_H\_

15

16#include <[errno.h](errno_8h.md)>

17#include <stddef.h>

18

19#include <[zephyr/device.h](device_8h.md)>

20

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

36typedef void (\*uart\_irq\_config\_func\_t)(const struct [device](structdevice.md) \*dev);

37

39\_\_subsystem struct uart\_driver\_api {

40

41#ifdef CONFIG\_UART\_ASYNC\_API

42

43 int (\*callback\_set)(const struct device \*dev, [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback, void \*user\_data);

44

45 int (\*tx)(const struct device \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

46 int (\*tx\_abort)(const struct device \*dev);

47

48 int (\*rx\_enable)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

49 int (\*rx\_buf\_rsp)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len);

50 int (\*rx\_disable)(const struct device \*dev);

51

52#ifdef CONFIG\_UART\_WIDE\_DATA

53 int (\*tx\_u16)(const struct device \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

54 int (\*rx\_enable\_u16)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

55 int (\*rx\_buf\_rsp\_u16)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, size\_t len);

56#endif

57

58#endif

59

61 int (\*poll\_in)(const struct device \*dev, unsigned char \*p\_char);

62 void (\*poll\_out)(const struct device \*dev, unsigned char out\_char);

63

64#ifdef CONFIG\_UART\_WIDE\_DATA

65 int (\*poll\_in\_u16)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16);

66 void (\*poll\_out\_u16)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16);

67#endif

68

70 int (\*err\_check)(const struct device \*dev);

71

72#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

74 int (\*configure)(const struct device \*dev, const struct uart\_config \*cfg);

75 int (\*config\_get)(const struct device \*dev, struct uart\_config \*cfg);

76#endif

77

78#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

79

81 int (\*fifo\_fill)(const struct device \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data, int len);

82

83#ifdef CONFIG\_UART\_WIDE\_DATA

84 int (\*fifo\_fill\_u16)(const struct device \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data, int len);

85#endif

86

88 int (\*fifo\_read)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data, const int size);

89

90#ifdef CONFIG\_UART\_WIDE\_DATA

91 int (\*fifo\_read\_u16)(const struct device \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data, const int size);

92#endif

93

95 void (\*irq\_tx\_enable)(const struct device \*dev);

96

98 void (\*irq\_tx\_disable)(const struct device \*dev);

99

101 int (\*irq\_tx\_ready)(const struct device \*dev);

102

104 void (\*irq\_rx\_enable)(const struct device \*dev);

105

107 void (\*irq\_rx\_disable)(const struct device \*dev);

108

110 int (\*irq\_tx\_complete)(const struct device \*dev);

111

113 int (\*irq\_rx\_ready)(const struct device \*dev);

114

116 void (\*irq\_err\_enable)(const struct device \*dev);

117

119 void (\*irq\_err\_disable)(const struct device \*dev);

120

122 int (\*irq\_is\_pending)(const struct device \*dev);

123

125 int (\*irq\_update)(const struct device \*dev);

126

128 void (\*irq\_callback\_set)(const struct device \*dev, [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb,

129 void \*user\_data);

130

131#endif

132

133#ifdef CONFIG\_UART\_LINE\_CTRL

134 int (\*line\_ctrl\_set)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

135 int (\*line\_ctrl\_get)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

136#endif

137

138#ifdef CONFIG\_UART\_DRV\_CMD

139 int (\*drv\_cmd)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p);

140#endif

141};

142

143static inline int z\_impl\_uart\_err\_check(const struct [device](structdevice.md) \*dev)

144{

145 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

146

147 if (api->err\_check == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

148 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

149 }

150

151 return api->err\_check(dev);

152}

153

154static inline int z\_impl\_uart\_poll\_in(const struct [device](structdevice.md) \*dev, unsigned char \*p\_char)

155{

156 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

157

158 if (api->poll\_in == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

159 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

160 }

161

162 return api->poll\_in(dev, p\_char);

163}

164

165static inline int z\_impl\_uart\_poll\_in\_u16(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16)

166{

167#ifdef CONFIG\_UART\_WIDE\_DATA

168 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

169

170 if (api->poll\_in\_u16 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

171 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

172 }

173

174 return api->poll\_in\_u16(dev, p\_u16);

175#else

176 ARG\_UNUSED(dev);

177 ARG\_UNUSED(p\_u16);

178 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

179#endif

180}

181

182static inline void z\_impl\_uart\_poll\_out(const struct [device](structdevice.md) \*dev, unsigned char out\_char)

183{

184 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

185

186 api->poll\_out(dev, out\_char);

187}

188

189static inline void z\_impl\_uart\_poll\_out\_u16(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16)

190{

191#ifdef CONFIG\_UART\_WIDE\_DATA

192 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

193

194 api->poll\_out\_u16(dev, out\_u16);

195#else

196 ARG\_UNUSED(dev);

197 ARG\_UNUSED(out\_u16);

198#endif

199}

200

201static inline int z\_impl\_uart\_configure(const struct [device](structdevice.md) \*dev, const struct [uart\_config](structuart__config.md) \*cfg)

202{

203#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

204 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

205

206 if (api->configure == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

207 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

208 }

209 return api->configure(dev, cfg);

210#else

211 ARG\_UNUSED(dev);

212 ARG\_UNUSED(cfg);

213 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

214#endif

215}

216

217static inline int z\_impl\_uart\_config\_get(const struct [device](structdevice.md) \*dev, struct [uart\_config](structuart__config.md) \*cfg)

218{

219#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

220 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

221

222 if (api->config\_get == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

223 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

224 }

225

226 return api->config\_get(dev, cfg);

227#else

228 ARG\_UNUSED(dev);

229 ARG\_UNUSED(cfg);

230 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

231#endif

232}

233

234static inline int [uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data, int size)

235{

236#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

237 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

238

239 if (api->fifo\_fill == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

240 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

241 }

242

243 return api->fifo\_fill(dev, tx\_data, size);

244#else

245 ARG\_UNUSED(dev);

246 ARG\_UNUSED(tx\_data);

247 ARG\_UNUSED(size);

248 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

249#endif

250}

251

252static inline int [uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data, int size)

253{

254#if defined(CONFIG\_UART\_INTERRUPT\_DRIVEN) && defined(CONFIG\_UART\_WIDE\_DATA)

255 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

256

257 if (api->fifo\_fill\_u16 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

258 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

259 }

260

261 return api->fifo\_fill\_u16(dev, tx\_data, size);

262#else

263 ARG\_UNUSED(dev);

264 ARG\_UNUSED(tx\_data);

265 ARG\_UNUSED(size);

266 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

267#endif

268}

269

270static inline int [uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data, const int size)

271{

272#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

273 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

274

275 if (api->fifo\_read == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

276 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

277 }

278

279 return api->fifo\_read(dev, rx\_data, size);

280#else

281 ARG\_UNUSED(dev);

282 ARG\_UNUSED(rx\_data);

283 ARG\_UNUSED(size);

284 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

285#endif

286}

287

288static inline int [uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data, const int size)

289{

290#if defined(CONFIG\_UART\_INTERRUPT\_DRIVEN) && defined(CONFIG\_UART\_WIDE\_DATA)

291 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

292

293 if (api->fifo\_read\_u16 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

294 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

295 }

296

297 return api->fifo\_read\_u16(dev, rx\_data, size);

298#else

299 ARG\_UNUSED(dev);

300 ARG\_UNUSED(rx\_data);

301 ARG\_UNUSED(size);

302 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

303#endif

304}

305

306static inline void z\_impl\_uart\_irq\_tx\_enable(const struct [device](structdevice.md) \*dev)

307{

308#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

309 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

310

311 if (api->irq\_tx\_enable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

312 api->irq\_tx\_enable(dev);

313 }

314#else

315 ARG\_UNUSED(dev);

316#endif

317}

318

319static inline void z\_impl\_uart\_irq\_tx\_disable(const struct [device](structdevice.md) \*dev)

320{

321#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

322 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

323

324 if (api->irq\_tx\_disable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

325 api->irq\_tx\_disable(dev);

326 }

327#else

328 ARG\_UNUSED(dev);

329#endif

330}

331

332static inline int [uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)(const struct [device](structdevice.md) \*dev)

333{

334#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

335 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

336

337 if (api->irq\_tx\_ready == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

338 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

339 }

340

341 return api->irq\_tx\_ready(dev);

342#else

343 ARG\_UNUSED(dev);

344 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

345#endif

346}

347

348static inline void z\_impl\_uart\_irq\_rx\_enable(const struct [device](structdevice.md) \*dev)

349{

350#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

351 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

352

353 if (api->irq\_rx\_enable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

354 api->irq\_rx\_enable(dev);

355 }

356#else

357 ARG\_UNUSED(dev);

358#endif

359}

360

361static inline void z\_impl\_uart\_irq\_rx\_disable(const struct [device](structdevice.md) \*dev)

362{

363#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

364 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

365

366 if (api->irq\_rx\_disable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

367 api->irq\_rx\_disable(dev);

368 }

369#else

370 ARG\_UNUSED(dev);

371#endif

372}

373

374static inline int [uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)(const struct [device](structdevice.md) \*dev)

375{

376#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

377 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

378

379 if (api->irq\_tx\_complete == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

380 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

381 }

382 return api->irq\_tx\_complete(dev);

383#else

384 ARG\_UNUSED(dev);

385 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

386#endif

387}

388

389static inline int [uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)(const struct [device](structdevice.md) \*dev)

390{

391#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

392 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

393

394 if (api->irq\_rx\_ready == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

395 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

396 }

397 return api->irq\_rx\_ready(dev);

398#else

399 ARG\_UNUSED(dev);

400 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

401#endif

402}

403

404static inline void z\_impl\_uart\_irq\_err\_enable(const struct [device](structdevice.md) \*dev)

405{

406#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

407 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

408

409 if (api->irq\_err\_enable) {

410 api->irq\_err\_enable(dev);

411 }

412#else

413 ARG\_UNUSED(dev);

414#endif

415}

416

417static inline void z\_impl\_uart\_irq\_err\_disable(const struct [device](structdevice.md) \*dev)

418{

419#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

420 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

421

422 if (api->irq\_err\_disable) {

423 api->irq\_err\_disable(dev);

424 }

425#else

426 ARG\_UNUSED(dev);

427#endif

428}

429

430static inline int z\_impl\_uart\_irq\_is\_pending(const struct [device](structdevice.md) \*dev)

431{

432#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

433 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

434

435 if (api->irq\_is\_pending == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

436 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

437 }

438 return api->irq\_is\_pending(dev);

439#else

440 ARG\_UNUSED(dev);

441 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

442#endif

443}

444

445static inline int z\_impl\_uart\_irq\_update(const struct [device](structdevice.md) \*dev)

446{

447#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

448 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

449

450 if (api->irq\_update == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

451 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

452 }

453 return api->irq\_update(dev);

454#else

455 ARG\_UNUSED(dev);

456 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

457#endif

458}

459

460static inline int [uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)(const struct [device](structdevice.md) \*dev,

461 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb, void \*user\_data)

462{

463#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

464 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

465

466 if ((api != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) && (api->irq\_callback\_set != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4))) {

467 api->irq\_callback\_set(dev, cb, user\_data);

468 return 0;

469 } else {

470 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

471 }

472#else

473 ARG\_UNUSED(dev);

474 ARG\_UNUSED(cb);

475 ARG\_UNUSED(user\_data);

476 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

477#endif

478}

479

480static inline int [uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)(const struct [device](structdevice.md) \*dev, [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb)

481{

482 return [uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)(dev, cb, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

483}

484

485static inline int [uart\_callback\_set](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)(const struct [device](structdevice.md) \*dev, [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback,

486 void \*user\_data)

487{

488#ifdef CONFIG\_UART\_ASYNC\_API

489 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

490

491 if (api->callback\_set == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

492 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

493 }

494

495 return api->callback\_set(dev, callback, user\_data);

496#else

497 ARG\_UNUSED(dev);

498 ARG\_UNUSED(callback);

499 ARG\_UNUSED(user\_data);

500 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

501#endif

502}

503

504static inline int z\_impl\_uart\_tx(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len,

505 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

506

507{

508#ifdef CONFIG\_UART\_ASYNC\_API

509 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

510

511 return api->tx(dev, buf, len, timeout);

512#else

513 ARG\_UNUSED(dev);

514 ARG\_UNUSED(buf);

515 ARG\_UNUSED(len);

516 ARG\_UNUSED(timeout);

517 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

518#endif

519}

520

521static inline int z\_impl\_uart\_tx\_u16(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, size\_t len,

522 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

523

524{

525#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

526 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

527

528 return api->tx\_u16(dev, buf, len, timeout);

529#else

530 ARG\_UNUSED(dev);

531 ARG\_UNUSED(buf);

532 ARG\_UNUSED(len);

533 ARG\_UNUSED(timeout);

534 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

535#endif

536}

537

538static inline int z\_impl\_uart\_tx\_abort(const struct [device](structdevice.md) \*dev)

539{

540#ifdef CONFIG\_UART\_ASYNC\_API

541 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

542

543 return api->tx\_abort(dev);

544#else

545 ARG\_UNUSED(dev);

546 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

547#endif

548}

549

550static inline int z\_impl\_uart\_rx\_enable(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len,

551 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

552{

553#ifdef CONFIG\_UART\_ASYNC\_API

554 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

555

556 return api->rx\_enable(dev, buf, len, timeout);

557#else

558 ARG\_UNUSED(dev);

559 ARG\_UNUSED(buf);

560 ARG\_UNUSED(len);

561 ARG\_UNUSED(timeout);

562 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

563#endif

564}

565

566static inline int z\_impl\_uart\_rx\_enable\_u16(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, size\_t len,

567 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

568{

569#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

570 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

571

572 return api->rx\_enable\_u16(dev, buf, len, timeout);

573#else

574 ARG\_UNUSED(dev);

575 ARG\_UNUSED(buf);

576 ARG\_UNUSED(len);

577 ARG\_UNUSED(timeout);

578 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

579#endif

580}

581

582static inline int [uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len)

583{

584#ifdef CONFIG\_UART\_ASYNC\_API

585 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

586

587 return api->rx\_buf\_rsp(dev, buf, len);

588#else

589 ARG\_UNUSED(dev);

590 ARG\_UNUSED(buf);

591 ARG\_UNUSED(len);

592 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

593#endif

594}

595

596static inline int [uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, size\_t len)

597{

598#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

599 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

600

601 return api->rx\_buf\_rsp\_u16(dev, buf, len);

602#else

603 ARG\_UNUSED(dev);

604 ARG\_UNUSED(buf);

605 ARG\_UNUSED(len);

606 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

607#endif

608}

609

610static inline int z\_impl\_uart\_rx\_disable(const struct [device](structdevice.md) \*dev)

611{

612#ifdef CONFIG\_UART\_ASYNC\_API

613 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

614

615 return api->rx\_disable(dev);

616#else

617 ARG\_UNUSED(dev);

618 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

619#endif

620}

621

622static inline int z\_impl\_uart\_line\_ctrl\_set(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

623{

624#ifdef CONFIG\_UART\_LINE\_CTRL

625 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

626

627 if (api->line\_ctrl\_set == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

628 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

629 }

630 return api->line\_ctrl\_set(dev, ctrl, val);

631#else

632 ARG\_UNUSED(dev);

633 ARG\_UNUSED(ctrl);

634 ARG\_UNUSED(val);

635 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

636#endif

637}

638

639static inline int z\_impl\_uart\_line\_ctrl\_get(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val)

640{

641#ifdef CONFIG\_UART\_LINE\_CTRL

642 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

643

644 if (api->line\_ctrl\_get == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

645 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

646 }

647 return api->line\_ctrl\_get(dev, ctrl, val);

648#else

649 ARG\_UNUSED(dev);

650 ARG\_UNUSED(ctrl);

651 ARG\_UNUSED(val);

652 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

653#endif

654}

655

656static inline int z\_impl\_uart\_drv\_cmd(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p)

657{

658#ifdef CONFIG\_UART\_DRV\_CMD

659 const struct uart\_driver\_api \*api = (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

660

661 if (api->drv\_cmd == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

662 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

663 }

664 return api->drv\_cmd(dev, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), p);

665#else

666 ARG\_UNUSED(dev);

667 ARG\_UNUSED([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

668 ARG\_UNUSED(p);

669 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

670#endif

671}

672

673#ifdef \_\_cplusplus

674}

675#endif

676

678

679#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_UART\_INTERNAL\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)

void(\* uart\_callback\_t)(const struct device \*dev, struct uart\_event \*evt, void \*user\_data)

Define the application callback function signature for uart\_callback\_set() function.

**Definition** uart.h:316

[uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)

static int uart\_rx\_buf\_rsp(const struct device \*dev, uint8\_t \*buf, size\_t len)

Provide receive buffer in response to UART\_RX\_BUF\_REQUEST event.

[uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)

static int uart\_rx\_buf\_rsp\_u16(const struct device \*dev, uint16\_t \*buf, size\_t len)

Provide wide data receive buffer in response to UART\_RX\_BUF\_REQUEST event.

[uart\_callback\_set](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)

static int uart\_callback\_set(const struct device \*dev, uart\_callback\_t callback, void \*user\_data)

Set event handler function.

[uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)

static int uart\_fifo\_read\_u16(const struct device \*dev, uint16\_t \*rx\_data, const int size)

Read wide data from FIFO.

[uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)

static int uart\_irq\_tx\_ready(const struct device \*dev)

Check if UART TX buffer can accept bytes.

[uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)

static int uart\_irq\_callback\_set(const struct device \*dev, uart\_irq\_callback\_user\_data\_t cb)

Set the IRQ callback function pointer (legacy).

[uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)

static int uart\_irq\_tx\_complete(const struct device \*dev)

Check if UART TX block finished transmission.

[uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)

static int uart\_fifo\_fill\_u16(const struct device \*dev, const uint16\_t \*tx\_data, int size)

Fill FIFO with wide data.

[uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)

static int uart\_fifo\_read(const struct device \*dev, uint8\_t \*rx\_data, const int size)

Read data from FIFO.

[uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)

static int uart\_irq\_rx\_ready(const struct device \*dev)

Check if UART RX buffer has a received char.

[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)

void(\* uart\_irq\_callback\_user\_data\_t)(const struct device \*dev, void \*user\_data)

Define the application callback function signature for uart\_irq\_callback\_user\_data\_set() function.

**Definition** uart.h:140

[uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)

static int uart\_irq\_callback\_user\_data\_set(const struct device \*dev, uart\_irq\_callback\_user\_data\_t cb, void \*user\_data)

Set the IRQ callback function pointer.

[uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)

static int uart\_fifo\_fill(const struct device \*dev, const uint8\_t \*tx\_data, int size)

Fill FIFO with data.

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[uart\_config](structuart__config.md)

UART controller configuration structure.

**Definition** uart.h:120

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart](dir_eceb547fc512cd90b0f2ab20ab1dbc9a.md)
- [uart\_internal.h](uart__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
