---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bap__lc3__preset_8h_source.html
original_path: doxygen/html/bap__lc3__preset_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bap\_lc3\_preset.h

[Go to the documentation of this file.](bap__lc3__preset_8h.md)

1

9

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_LC3\_PRESET\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_LC3\_PRESET\_

12

28

29#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

30#include <[zephyr/bluetooth/audio/lc3.h](lc3_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 37](structbt__bap__lc3__preset.md)struct [bt\_bap\_lc3\_preset](structbt__bap__lc3__preset.md) {

[ 39](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) [codec\_cfg](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da);

[ 41](structbt__bap__lc3__preset.md#ab0708b8f1020c369278279e139992c93) struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) [qos](structbt__bap__lc3__preset.md#ab0708b8f1020c369278279e139992c93);

42};

43

[ 45](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)#define BT\_BAP\_LC3\_PRESET(\_codec, \_qos) \

46 { \

47 .codec\_cfg = \_codec, .qos = \_qos, \

48 }

49

50/\* LC3 Unicast presets defined by table 5.2 in the BAP v1.0 specification \*/

51

[ 58](group__bt__bap__lc3__preset.md#gac1a211ed3116a0b7f0b181abd0ae6e8a)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_1\_1(\_loc, \_stream\_context) \

59 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

60 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 26u, 1, \

61 \_stream\_context), \

62 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 26u, 2u, 8u, 40000u))

63

[ 70](group__bt__bap__lc3__preset.md#ga8caa6c9cf34f45ac36f6450d9f076126)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_2\_1(\_loc, \_stream\_context) \

71 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

72 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 30U, 1, \

73 \_stream\_context), \

74 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 30u, 2u, 10u, 40000u))

75

[ 82](group__bt__bap__lc3__preset.md#gaac67456c95c688b83b460bdcc0c696f1)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_1\_1(\_loc, \_stream\_context) \

83 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

84 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

85 \_stream\_context), \

86 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 30u, 2u, 8u, 40000u))

87

[ 96](group__bt__bap__lc3__preset.md#gaf5b1892e96c1f63c73dddfeda0843eeb)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_2\_1(\_loc, \_stream\_context) \

97 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

98 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

99 \_stream\_context), \

100 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 40u, 2u, 10u, 40000u))

101

[ 108](group__bt__bap__lc3__preset.md#gabb43386a22cd9415c491a846aef85310)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_1\_1(\_loc, \_stream\_context) \

109 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

110 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 45U, 1, \

111 \_stream\_context), \

112 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 45u, 2u, 8u, 40000u))

113

[ 122](group__bt__bap__lc3__preset.md#ga24555bc6189ad58f584be0bbbf085e24)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_2\_1(\_loc, \_stream\_context) \

123 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

124 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 60U, 1, \

125 \_stream\_context), \

126 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 60u, 2u, 10u, 40000u))

127

[ 134](group__bt__bap__lc3__preset.md#ga39de4252e742ce815633ae7a50062f98)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_1\_1(\_loc, \_stream\_context) \

135 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

136 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

137 \_stream\_context), \

138 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 60u, 2u, 8u, 40000u))

139

[ 146](group__bt__bap__lc3__preset.md#ga93a1fbdf0feba790464c41e362aea307)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_2\_1(\_loc, \_stream\_context) \

147 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

148 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

149 \_stream\_context), \

150 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 80u, 2u, 10u, 40000u))

151

[ 158](group__bt__bap__lc3__preset.md#gae9795a9dc12aa60c74a4aad0c35b18ac)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_1\_1(\_loc, \_stream\_context) \

159 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

160 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 97U, 1, \

161 \_stream\_context), \

162 BT\_AUDIO\_CODEC\_QOS\_FRAMED(8163u, 97u, 5u, 24u, 40000u))

163

[ 170](group__bt__bap__lc3__preset.md#ga5508e46240176f5b054467609b635f0d)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_2\_1(\_loc, \_stream\_context) \

171 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

172 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 130U, 1, \

173 \_stream\_context), \

174 BT\_AUDIO\_CODEC\_QOS\_FRAMED(10884u, 130u, 5u, 31u, 40000u))

175

[ 182](group__bt__bap__lc3__preset.md#gaf2ad00922314b8ee06d3a001d1eafd94)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_1\_1(\_loc, \_stream\_context) \

183 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

184 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

185 \_stream\_context), \

186 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 75u, 5u, 15u, 40000u))

187

[ 194](group__bt__bap__lc3__preset.md#gaea3354a3c92d889324f48260216c15bf)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_2\_1(\_loc, \_stream\_context) \

195 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

196 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

197 \_stream\_context), \

198 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 100u, 5u, 20u, 40000u))

199

[ 206](group__bt__bap__lc3__preset.md#gabe085646c5709fcaa2ec830f006105c0)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_3\_1(\_loc, \_stream\_context) \

207 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

208 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

209 \_stream\_context), \

210 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 90u, 5u, 15u, 40000u))

211

[ 218](group__bt__bap__lc3__preset.md#ga5a2c91592853163f3c88d490a8b6bd49)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_4\_1(\_loc, \_stream\_context) \

219 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

220 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

221 \_stream\_context), \

222 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 120u, 5u, 20u, 40000u))

223

[ 230](group__bt__bap__lc3__preset.md#ga9dbd2e240b5a733044ab78ec73e6532e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_5\_1(\_loc, \_stream\_context) \

231 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

232 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 117u, \

233 1, \_stream\_context), \

234 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 117u, 5u, 15u, 40000u))

235

[ 242](group__bt__bap__lc3__preset.md#gaa4ee0f200c3484b1708a10ba5f5185a4)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_6\_1(\_loc, \_stream\_context) \

243 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

244 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 155u, 1, \

245 \_stream\_context), \

246 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 155u, 5u, 20u, 40000u))

247

254/\* Following presets are for unicast high reliability audio data \*/

[ 255](group__bt__bap__lc3__preset.md#ga332cb00a9cfbf31444b9ca86ecb69cae)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_1\_2(\_loc, \_stream\_context) \

256 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

257 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 26u, 1, \

258 \_stream\_context), \

259 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 26u, 13u, 75u, 40000u))

260

[ 267](group__bt__bap__lc3__preset.md#ga945c808feda5dd50d47f78a420c90768)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_2\_2(\_loc, \_stream\_context) \

268 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

269 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 30U, 1, \

270 \_stream\_context), \

271 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 30u, 13u, 95u, 40000u))

272

[ 279](group__bt__bap__lc3__preset.md#ga0191f12d56220dd5ef0842ccd5acbc2c)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_1\_2(\_loc, \_stream\_context) \

280 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

281 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

282 \_stream\_context), \

283 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 30u, 13u, 75u, 40000u))

284

[ 291](group__bt__bap__lc3__preset.md#gac4bb73b877cb170ad24f16d422d5752e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_2\_2(\_loc, \_stream\_context) \

292 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

293 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

294 \_stream\_context), \

295 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 40u, 13u, 95u, 40000u))

296

[ 303](group__bt__bap__lc3__preset.md#ga9055c137e206deab6c9d756db6dc24b5)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_1\_2(\_loc, \_stream\_context) \

304 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

305 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 45U, 1, \

306 \_stream\_context), \

307 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 45u, 13u, 75u, 40000u))

308

[ 315](group__bt__bap__lc3__preset.md#ga3d044b67ae42487129e9df35a79e099e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_2\_2(\_loc, \_stream\_context) \

316 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

317 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 60U, 1, \

318 \_stream\_context), \

319 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 60u, 13u, 95u, 40000u))

320

[ 327](group__bt__bap__lc3__preset.md#ga8e99870c84c8fc3bc7f294f534ee9b9d)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_1\_2(\_loc, \_stream\_context) \

328 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

329 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

330 \_stream\_context), \

331 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 60u, 13u, 75u, 40000u))

332

[ 339](group__bt__bap__lc3__preset.md#ga01eb8a840451b914b8152f4d90a493c9)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_2\_2(\_loc, \_stream\_context) \

340 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

341 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

342 \_stream\_context), \

343 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 80u, 13u, 95u, 40000u))

344

[ 351](group__bt__bap__lc3__preset.md#ga70f32a61655cfc1bdd73164902b8b436)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_1\_2(\_loc, \_stream\_context) \

352 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

353 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 97U, 1, \

354 \_stream\_context), \

355 BT\_AUDIO\_CODEC\_QOS\_FRAMED(8163u, 97u, 13u, 80u, 40000u))

356

[ 363](group__bt__bap__lc3__preset.md#ga66ea64d32c6b28bcf65e991e677f0567)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_2\_2(\_loc, \_stream\_context) \

364 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

365 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 130U, 1, \

366 \_stream\_context), \

367 BT\_AUDIO\_CODEC\_QOS\_FRAMED(10884u, 130u, 13u, 85u, 40000u))

368

[ 375](group__bt__bap__lc3__preset.md#ga4efe7f4016a829e3d301108eef8ef93c)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_1\_2(\_loc, \_stream\_context) \

376 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

377 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

378 \_stream\_context), \

379 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 75u, 13u, 75u, 40000u))

380

[ 387](group__bt__bap__lc3__preset.md#ga178d09a96e9e0823aed7c8965794ffe3)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_2\_2(\_loc, \_stream\_context) \

388 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

389 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

390 \_stream\_context), \

391 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 100u, 13u, 95u, 40000u))

392

[ 399](group__bt__bap__lc3__preset.md#gabfba888ded2aa54c044e8862d0b95da0)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_3\_2(\_loc, \_stream\_context) \

400 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

401 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

402 \_stream\_context), \

403 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 90u, 13u, 75u, 40000u))

404

[ 411](group__bt__bap__lc3__preset.md#ga7624cdd35f1eec81c17acf41dd9c85f3)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_4\_2(\_loc, \_stream\_context) \

412 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

413 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

414 \_stream\_context), \

415 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 120u, 13u, 100u, 40000u))

416

[ 423](group__bt__bap__lc3__preset.md#gacd6af79c79e587e9c0f858672ec79f49)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_5\_2(\_loc, \_stream\_context) \

424 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

425 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 117u, \

426 1, \_stream\_context), \

427 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 117u, 13u, 75u, 40000u))

428

[ 435](group__bt__bap__lc3__preset.md#gaea427c1bb97174941d7feae359e7f8fd)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_6\_2(\_loc, \_stream\_context) \

436 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

437 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 155u, 1, \

438 \_stream\_context), \

439 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 155u, 13u, 100u, 40000u))

440

447/\* LC3 Broadcast presets defined by table 6.4 in the BAP v1.0 specification \*/

[ 448](group__bt__bap__lc3__preset.md#ga71551e9a3382c4c3391cdbe3f3b155eb)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_1\_1(\_loc, \_stream\_context) \

449 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

450 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 26u, 1, \

451 \_stream\_context), \

452 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 26u, 2u, 8u, 40000u))

453

[ 460](group__bt__bap__lc3__preset.md#ga09a29e1a76185dfd783d428f862ea8dd)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_2\_1(\_loc, \_stream\_context) \

461 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

462 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 30U, 1, \

463 \_stream\_context), \

464 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 30u, 2u, 10u, 40000u))

465

[ 472](group__bt__bap__lc3__preset.md#gaa17732bcb085e97856bd5e7a65a3255c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_1\_1(\_loc, \_stream\_context) \

473 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

474 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

475 \_stream\_context), \

476 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 30u, 2u, 8u, 40000u))

477

[ 486](group__bt__bap__lc3__preset.md#ga8ded042093c310e84ccc76c4d9a67b9c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_2\_1(\_loc, \_stream\_context) \

487 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

488 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

489 \_stream\_context), \

490 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 40u, 2u, 10u, 40000u))

491

[ 498](group__bt__bap__lc3__preset.md#ga2a4ccfe1ce99443f2e07ec629e22a1af)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_1\_1(\_loc, \_stream\_context) \

499 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

500 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 45U, 1, \

501 \_stream\_context), \

502 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 45u, 2u, 8u, 40000u))

503

[ 512](group__bt__bap__lc3__preset.md#ga38c76ab52c627c2d1622b9fd2511367a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_2\_1(\_loc, \_stream\_context) \

513 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

514 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 60U, 1, \

515 \_stream\_context), \

516 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 60u, 2u, 10u, 40000u))

517

[ 524](group__bt__bap__lc3__preset.md#ga3842c0a4531a087830d133924542282f)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_1\_1(\_loc, \_stream\_context) \

525 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

526 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

527 \_stream\_context), \

528 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 60u, 2u, 8u, 40000u))

529

[ 536](group__bt__bap__lc3__preset.md#ga883b0d45657ae3a4902d2c9df3392447)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_2\_1(\_loc, \_stream\_context) \

537 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

538 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

539 \_stream\_context), \

540 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 80u, 2u, 10u, 40000u))

541

[ 548](group__bt__bap__lc3__preset.md#ga31f25a4a4549659370bd2d3040aca84a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_1\_1(\_loc, \_stream\_context) \

549 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

550 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 97U, 1, \

551 \_stream\_context), \

552 BT\_AUDIO\_CODEC\_QOS\_FRAMED(8163u, 97u, 4u, 24u, 40000u))

553

[ 560](group__bt__bap__lc3__preset.md#ga09345dd8d9afecfae24aecf760576aeb)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_2\_1(\_loc, \_stream\_context) \

561 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

562 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 130U, 1, \

563 \_stream\_context), \

564 BT\_AUDIO\_CODEC\_QOS\_FRAMED(10884u, 130u, 4u, 31u, 40000u))

565

[ 572](group__bt__bap__lc3__preset.md#gab22a08b23523b080340727261213c8fc)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_1\_1(\_loc, \_stream\_context) \

573 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

574 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

575 \_stream\_context), \

576 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 75u, 4u, 15u, 40000u))

577

[ 584](group__bt__bap__lc3__preset.md#ga7d280583165d63be595af48fed07309a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_2\_1(\_loc, \_stream\_context) \

585 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

586 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

587 \_stream\_context), \

588 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 100u, 4u, 20u, 40000u))

589

[ 596](group__bt__bap__lc3__preset.md#ga8046777cdace9ed5c29d4ce347396c41)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_3\_1(\_loc, \_stream\_context) \

597 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

598 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

599 \_stream\_context), \

600 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 90u, 4u, 15u, 40000u))

601

[ 608](group__bt__bap__lc3__preset.md#gace016322c5fda54a55fa60af45250191)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_4\_1(\_loc, \_stream\_context) \

609 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

610 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

611 \_stream\_context), \

612 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 120u, 4u, 20u, 40000u))

613

[ 620](group__bt__bap__lc3__preset.md#gaa1c10f0cf98a707e73cb86b05838b60b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_5\_1(\_loc, \_stream\_context) \

621 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

622 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 117u, \

623 1, \_stream\_context), \

624 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 117u, 4u, 15u, 40000u))

625

[ 632](group__bt__bap__lc3__preset.md#ga729a73a1c6484d7538dd469b2b0f8e5e)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_6\_1(\_loc, \_stream\_context) \

633 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

634 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 155u, 1, \

635 \_stream\_context), \

636 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 155u, 4u, 20u, 40000u))

637

644/\* Following presets are for broadcast high reliability audio data \*/

[ 645](group__bt__bap__lc3__preset.md#ga8038c67898c42e0671fb341eedd416d1)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_1\_2(\_loc, \_stream\_context) \

646 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

647 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 26u, 1, \

648 \_stream\_context), \

649 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 26u, 4u, 45u, 40000u))

650

[ 657](group__bt__bap__lc3__preset.md#gac24afbdcea6eadac1123ba4553d79b8b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_2\_2(\_loc, \_stream\_context) \

658 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

659 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 30U, 1, \

660 \_stream\_context), \

661 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 30u, 4u, 60u, 40000u))

662

[ 669](group__bt__bap__lc3__preset.md#gaa87f899e5205e7513a2d480ae8e8f448)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_1\_2(\_loc, \_stream\_context) \

670 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

671 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

672 \_stream\_context), \

673 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 30u, 4u, 45u, 40000u))

674

[ 683](group__bt__bap__lc3__preset.md#ga1c0bd6076e559c349bcf3c511d4d5e03)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_2\_2(\_loc, \_stream\_context) \

684 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

685 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

686 \_stream\_context), \

687 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 40u, 4u, 60u, 40000u))

688

[ 695](group__bt__bap__lc3__preset.md#gabc3b1b68ea7da77de6720679084c69db)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_1\_2(\_loc, \_stream\_context) \

696 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

697 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 45U, 1, \

698 \_stream\_context), \

699 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 45u, 4u, 45u, 40000u))

700

[ 709](group__bt__bap__lc3__preset.md#gad435c834787acf0634e4fab408f8965f)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_2\_2(\_loc, \_stream\_context) \

710 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

711 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 60U, 1, \

712 \_stream\_context), \

713 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 60u, 4u, 60u, 40000u))

714

[ 721](group__bt__bap__lc3__preset.md#ga2e89f8a6c6410057c7e5de2a56535e14)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_1\_2(\_loc, \_stream\_context) \

722 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

723 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

724 \_stream\_context), \

725 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 60u, 4u, 45u, 40000u))

726

[ 733](group__bt__bap__lc3__preset.md#ga2c92af221ebc679c8fdab5ce96b3457c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_2\_2(\_loc, \_stream\_context) \

734 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

735 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

736 \_stream\_context), \

737 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 80u, 4u, 60u, 40000u))

738

[ 745](group__bt__bap__lc3__preset.md#gae2d56f56ad6fbc074dcd7443f4c7d460)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_1\_2(\_loc, \_stream\_context) \

746 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

747 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 97U, 1, \

748 \_stream\_context), \

749 BT\_AUDIO\_CODEC\_QOS\_FRAMED(8163u, 97u, 4u, 54u, 40000u))

750

[ 757](group__bt__bap__lc3__preset.md#gae4ee9d2021680837e3565a0efe4dc500)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_2\_2(\_loc, \_stream\_context) \

758 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

759 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 130U, 1, \

760 \_stream\_context), \

761 BT\_AUDIO\_CODEC\_QOS\_FRAMED(10884u, 130u, 4u, 60u, 40000u))

762

[ 769](group__bt__bap__lc3__preset.md#gaa26017b9af7f3cf272b691a636af7ee4)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_1\_2(\_loc, \_stream\_context) \

770 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

771 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

772 \_stream\_context), \

773 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 75u, 4u, 50u, 40000u))

774

[ 781](group__bt__bap__lc3__preset.md#gaca9c3e309005396ccad12aa61b76b84b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_2\_2(\_loc, \_stream\_context) \

782 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

783 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

784 \_stream\_context), \

785 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 100u, 4u, 65u, 40000u))

786

[ 793](group__bt__bap__lc3__preset.md#gaa165b8b8ee72a23734d5f0b0a601e545)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_3\_2(\_loc, \_stream\_context) \

794 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

795 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

796 \_stream\_context), \

797 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 90u, 4u, 50u, 40000u))

798

[ 805](group__bt__bap__lc3__preset.md#ga309020ab3bfd78b6ce0c2e6b2bf8d556)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_4\_2(\_loc, \_stream\_context) \

806 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

807 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

808 \_stream\_context), \

809 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 120u, 4u, 65u, 40000u))

810

[ 817](group__bt__bap__lc3__preset.md#gaacf70e1663e6a2d3418e3daae804a6c0)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_5\_2(\_loc, \_stream\_context) \

818 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

819 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 117u, \

820 1, \_stream\_context), \

821 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 117u, 4u, 50u, 40000u))

822

[ 829](group__bt__bap__lc3__preset.md#ga6e3b3a3869024ba1fe4ea8f9047a225d)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_6\_2(\_loc, \_stream\_context) \

830 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

831 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 155u, 1, \

832 \_stream\_context), \

833 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 155u, 4u, 65u, 40000u))

834

835#ifdef \_\_cplusplus

836}

837#endif

839

840#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_LC3\_PRESET\_ \*/

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[lc3.h](lc3_8h.md)

Bluetooth LC3 codec handling.

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:703

[bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)

Codec QoS structure.

**Definition** audio.h:849

[bt\_bap\_lc3\_preset](structbt__bap__lc3__preset.md)

Struct to hold a BAP defined LC3 preset.

**Definition** bap\_lc3\_preset.h:37

[bt\_bap\_lc3\_preset::codec\_cfg](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da)

struct bt\_audio\_codec\_cfg codec\_cfg

The LC3 Codec.

**Definition** bap\_lc3\_preset.h:39

[bt\_bap\_lc3\_preset::qos](structbt__bap__lc3__preset.md#ab0708b8f1020c369278279e139992c93)

struct bt\_audio\_codec\_qos qos

The BAP spec defined QoS values.

**Definition** bap\_lc3\_preset.h:41

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [bap\_lc3\_preset.h](bap__lc3__preset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
