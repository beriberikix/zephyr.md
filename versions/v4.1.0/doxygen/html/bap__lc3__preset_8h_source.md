---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bap__lc3__preset_8h_source.html
original_path: doxygen/html/bap__lc3__preset_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

30#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>

31#include <[zephyr/bluetooth/audio/lc3.h](lc3_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

[ 38](structbt__bap__lc3__preset.md)struct [bt\_bap\_lc3\_preset](structbt__bap__lc3__preset.md) {

[ 40](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) [codec\_cfg](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da);

[ 42](structbt__bap__lc3__preset.md#a8f5954471875861bfd387446060e9565) struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) [qos](structbt__bap__lc3__preset.md#a8f5954471875861bfd387446060e9565);

43};

44

[ 46](group__bt__bap__lc3__preset.md#ga9f2075cd5019d356bc7ccf7f9cbc63bb)#define BT\_BAP\_LC3\_PRESET(\_codec, \_qos) \

47 { \

48 .codec\_cfg = \_codec, .qos = \_qos, \

49 }

50

51/\* LC3 Unicast presets defined by table 5.2 in the BAP v1.0 specification \*/

52

[ 59](group__bt__bap__lc3__preset.md#gac1a211ed3116a0b7f0b181abd0ae6e8a)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_1\_1(\_loc, \_stream\_context) \

60 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

61 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 26u, 1, \

62 \_stream\_context), \

63 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 26u, 2u, 8u, 40000u))

64

[ 71](group__bt__bap__lc3__preset.md#ga8caa6c9cf34f45ac36f6450d9f076126)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_2\_1(\_loc, \_stream\_context) \

72 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

73 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 30U, 1, \

74 \_stream\_context), \

75 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 30u, 2u, 10u, 40000u))

76

[ 83](group__bt__bap__lc3__preset.md#gaac67456c95c688b83b460bdcc0c696f1)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_1\_1(\_loc, \_stream\_context) \

84 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

85 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

86 \_stream\_context), \

87 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 30u, 2u, 8u, 40000u))

88

[ 97](group__bt__bap__lc3__preset.md#gaf5b1892e96c1f63c73dddfeda0843eeb)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_2\_1(\_loc, \_stream\_context) \

98 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

99 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

100 \_stream\_context), \

101 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 40u, 2u, 10u, 40000u))

102

[ 109](group__bt__bap__lc3__preset.md#gabb43386a22cd9415c491a846aef85310)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_1\_1(\_loc, \_stream\_context) \

110 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

111 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 45U, 1, \

112 \_stream\_context), \

113 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 45u, 2u, 8u, 40000u))

114

[ 123](group__bt__bap__lc3__preset.md#ga24555bc6189ad58f584be0bbbf085e24)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_2\_1(\_loc, \_stream\_context) \

124 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

125 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 60U, 1, \

126 \_stream\_context), \

127 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 60u, 2u, 10u, 40000u))

128

[ 135](group__bt__bap__lc3__preset.md#ga39de4252e742ce815633ae7a50062f98)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_1\_1(\_loc, \_stream\_context) \

136 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

137 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

138 \_stream\_context), \

139 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 60u, 2u, 8u, 40000u))

140

[ 147](group__bt__bap__lc3__preset.md#ga93a1fbdf0feba790464c41e362aea307)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_2\_1(\_loc, \_stream\_context) \

148 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

149 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

150 \_stream\_context), \

151 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 80u, 2u, 10u, 40000u))

152

[ 159](group__bt__bap__lc3__preset.md#gae9795a9dc12aa60c74a4aad0c35b18ac)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_1\_1(\_loc, \_stream\_context) \

160 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

161 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 97U, 1, \

162 \_stream\_context), \

163 BT\_BAP\_QOS\_CFG\_FRAMED(8163u, 97u, 5u, 24u, 40000u))

164

[ 171](group__bt__bap__lc3__preset.md#ga5508e46240176f5b054467609b635f0d)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_2\_1(\_loc, \_stream\_context) \

172 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

173 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 130U, 1, \

174 \_stream\_context), \

175 BT\_BAP\_QOS\_CFG\_FRAMED(10884u, 130u, 5u, 31u, 40000u))

176

[ 183](group__bt__bap__lc3__preset.md#gaf2ad00922314b8ee06d3a001d1eafd94)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_1\_1(\_loc, \_stream\_context) \

184 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

185 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

186 \_stream\_context), \

187 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 75u, 5u, 15u, 40000u))

188

[ 195](group__bt__bap__lc3__preset.md#gaea3354a3c92d889324f48260216c15bf)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_2\_1(\_loc, \_stream\_context) \

196 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

197 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

198 \_stream\_context), \

199 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 100u, 5u, 20u, 40000u))

200

[ 207](group__bt__bap__lc3__preset.md#gabe085646c5709fcaa2ec830f006105c0)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_3\_1(\_loc, \_stream\_context) \

208 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

209 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

210 \_stream\_context), \

211 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 90u, 5u, 15u, 40000u))

212

[ 219](group__bt__bap__lc3__preset.md#ga5a2c91592853163f3c88d490a8b6bd49)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_4\_1(\_loc, \_stream\_context) \

220 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

221 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

222 \_stream\_context), \

223 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 120u, 5u, 20u, 40000u))

224

[ 231](group__bt__bap__lc3__preset.md#ga9dbd2e240b5a733044ab78ec73e6532e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_5\_1(\_loc, \_stream\_context) \

232 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

233 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 117u, \

234 1, \_stream\_context), \

235 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 117u, 5u, 15u, 40000u))

236

[ 243](group__bt__bap__lc3__preset.md#gaa4ee0f200c3484b1708a10ba5f5185a4)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_6\_1(\_loc, \_stream\_context) \

244 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

245 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 155u, 1, \

246 \_stream\_context), \

247 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 155u, 5u, 20u, 40000u))

248

255/\* Following presets are for unicast high reliability audio data \*/

[ 256](group__bt__bap__lc3__preset.md#ga332cb00a9cfbf31444b9ca86ecb69cae)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_1\_2(\_loc, \_stream\_context) \

257 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

258 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 26u, 1, \

259 \_stream\_context), \

260 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 26u, 13u, 75u, 40000u))

261

[ 268](group__bt__bap__lc3__preset.md#ga945c808feda5dd50d47f78a420c90768)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_2\_2(\_loc, \_stream\_context) \

269 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

270 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 30U, 1, \

271 \_stream\_context), \

272 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 30u, 13u, 95u, 40000u))

273

[ 280](group__bt__bap__lc3__preset.md#ga0191f12d56220dd5ef0842ccd5acbc2c)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_1\_2(\_loc, \_stream\_context) \

281 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

282 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

283 \_stream\_context), \

284 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 30u, 13u, 75u, 40000u))

285

[ 292](group__bt__bap__lc3__preset.md#gac4bb73b877cb170ad24f16d422d5752e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_2\_2(\_loc, \_stream\_context) \

293 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

294 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

295 \_stream\_context), \

296 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 40u, 13u, 95u, 40000u))

297

[ 304](group__bt__bap__lc3__preset.md#ga9055c137e206deab6c9d756db6dc24b5)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_1\_2(\_loc, \_stream\_context) \

305 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

306 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 45U, 1, \

307 \_stream\_context), \

308 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 45u, 13u, 75u, 40000u))

309

[ 316](group__bt__bap__lc3__preset.md#ga3d044b67ae42487129e9df35a79e099e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_2\_2(\_loc, \_stream\_context) \

317 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

318 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 60U, 1, \

319 \_stream\_context), \

320 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 60u, 13u, 95u, 40000u))

321

[ 328](group__bt__bap__lc3__preset.md#ga8e99870c84c8fc3bc7f294f534ee9b9d)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_1\_2(\_loc, \_stream\_context) \

329 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

330 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

331 \_stream\_context), \

332 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 60u, 13u, 75u, 40000u))

333

[ 340](group__bt__bap__lc3__preset.md#ga01eb8a840451b914b8152f4d90a493c9)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_2\_2(\_loc, \_stream\_context) \

341 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

342 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

343 \_stream\_context), \

344 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 80u, 13u, 95u, 40000u))

345

[ 352](group__bt__bap__lc3__preset.md#ga70f32a61655cfc1bdd73164902b8b436)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_1\_2(\_loc, \_stream\_context) \

353 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

354 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 97U, 1, \

355 \_stream\_context), \

356 BT\_BAP\_QOS\_CFG\_FRAMED(8163u, 97u, 13u, 80u, 40000u))

357

[ 364](group__bt__bap__lc3__preset.md#ga66ea64d32c6b28bcf65e991e677f0567)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_2\_2(\_loc, \_stream\_context) \

365 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

366 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 130U, 1, \

367 \_stream\_context), \

368 BT\_BAP\_QOS\_CFG\_FRAMED(10884u, 130u, 13u, 85u, 40000u))

369

[ 376](group__bt__bap__lc3__preset.md#ga4efe7f4016a829e3d301108eef8ef93c)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_1\_2(\_loc, \_stream\_context) \

377 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

378 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

379 \_stream\_context), \

380 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 75u, 13u, 75u, 40000u))

381

[ 388](group__bt__bap__lc3__preset.md#ga178d09a96e9e0823aed7c8965794ffe3)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_2\_2(\_loc, \_stream\_context) \

389 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

390 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

391 \_stream\_context), \

392 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 100u, 13u, 95u, 40000u))

393

[ 400](group__bt__bap__lc3__preset.md#gabfba888ded2aa54c044e8862d0b95da0)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_3\_2(\_loc, \_stream\_context) \

401 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

402 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

403 \_stream\_context), \

404 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 90u, 13u, 75u, 40000u))

405

[ 412](group__bt__bap__lc3__preset.md#ga7624cdd35f1eec81c17acf41dd9c85f3)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_4\_2(\_loc, \_stream\_context) \

413 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

414 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

415 \_stream\_context), \

416 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 120u, 13u, 100u, 40000u))

417

[ 424](group__bt__bap__lc3__preset.md#gacd6af79c79e587e9c0f858672ec79f49)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_5\_2(\_loc, \_stream\_context) \

425 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

426 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 117u, \

427 1, \_stream\_context), \

428 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 117u, 13u, 75u, 40000u))

429

[ 436](group__bt__bap__lc3__preset.md#gaea427c1bb97174941d7feae359e7f8fd)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_6\_2(\_loc, \_stream\_context) \

437 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

438 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 155u, 1, \

439 \_stream\_context), \

440 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 155u, 13u, 100u, 40000u))

441

448/\* LC3 Broadcast presets defined by table 6.4 in the BAP v1.0 specification \*/

[ 449](group__bt__bap__lc3__preset.md#ga71551e9a3382c4c3391cdbe3f3b155eb)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_1\_1(\_loc, \_stream\_context) \

450 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

451 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 26u, 1, \

452 \_stream\_context), \

453 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 26u, 2u, 8u, 40000u))

454

[ 461](group__bt__bap__lc3__preset.md#ga09a29e1a76185dfd783d428f862ea8dd)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_2\_1(\_loc, \_stream\_context) \

462 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

463 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 30U, 1, \

464 \_stream\_context), \

465 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 30u, 2u, 10u, 40000u))

466

[ 473](group__bt__bap__lc3__preset.md#gaa17732bcb085e97856bd5e7a65a3255c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_1\_1(\_loc, \_stream\_context) \

474 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

475 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

476 \_stream\_context), \

477 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 30u, 2u, 8u, 40000u))

478

[ 487](group__bt__bap__lc3__preset.md#ga8ded042093c310e84ccc76c4d9a67b9c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_2\_1(\_loc, \_stream\_context) \

488 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

489 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

490 \_stream\_context), \

491 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 40u, 2u, 10u, 40000u))

492

[ 499](group__bt__bap__lc3__preset.md#ga2a4ccfe1ce99443f2e07ec629e22a1af)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_1\_1(\_loc, \_stream\_context) \

500 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

501 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 45U, 1, \

502 \_stream\_context), \

503 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 45u, 2u, 8u, 40000u))

504

[ 513](group__bt__bap__lc3__preset.md#ga38c76ab52c627c2d1622b9fd2511367a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_2\_1(\_loc, \_stream\_context) \

514 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

515 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 60U, 1, \

516 \_stream\_context), \

517 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 60u, 2u, 10u, 40000u))

518

[ 525](group__bt__bap__lc3__preset.md#ga3842c0a4531a087830d133924542282f)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_1\_1(\_loc, \_stream\_context) \

526 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

527 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

528 \_stream\_context), \

529 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 60u, 2u, 8u, 40000u))

530

[ 537](group__bt__bap__lc3__preset.md#ga883b0d45657ae3a4902d2c9df3392447)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_2\_1(\_loc, \_stream\_context) \

538 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

539 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

540 \_stream\_context), \

541 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 80u, 2u, 10u, 40000u))

542

[ 549](group__bt__bap__lc3__preset.md#ga31f25a4a4549659370bd2d3040aca84a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_1\_1(\_loc, \_stream\_context) \

550 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

551 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 97U, 1, \

552 \_stream\_context), \

553 BT\_BAP\_QOS\_CFG\_FRAMED(8163u, 97u, 4u, 24u, 40000u))

554

[ 561](group__bt__bap__lc3__preset.md#ga09345dd8d9afecfae24aecf760576aeb)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_2\_1(\_loc, \_stream\_context) \

562 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

563 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 130U, 1, \

564 \_stream\_context), \

565 BT\_BAP\_QOS\_CFG\_FRAMED(10884u, 130u, 4u, 31u, 40000u))

566

[ 573](group__bt__bap__lc3__preset.md#gab22a08b23523b080340727261213c8fc)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_1\_1(\_loc, \_stream\_context) \

574 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

575 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

576 \_stream\_context), \

577 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 75u, 4u, 15u, 40000u))

578

[ 585](group__bt__bap__lc3__preset.md#ga7d280583165d63be595af48fed07309a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_2\_1(\_loc, \_stream\_context) \

586 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

587 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

588 \_stream\_context), \

589 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 100u, 4u, 20u, 40000u))

590

[ 597](group__bt__bap__lc3__preset.md#ga8046777cdace9ed5c29d4ce347396c41)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_3\_1(\_loc, \_stream\_context) \

598 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

599 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

600 \_stream\_context), \

601 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 90u, 4u, 15u, 40000u))

602

[ 609](group__bt__bap__lc3__preset.md#gace016322c5fda54a55fa60af45250191)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_4\_1(\_loc, \_stream\_context) \

610 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

611 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

612 \_stream\_context), \

613 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 120u, 4u, 20u, 40000u))

614

[ 621](group__bt__bap__lc3__preset.md#gaa1c10f0cf98a707e73cb86b05838b60b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_5\_1(\_loc, \_stream\_context) \

622 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

623 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 117u, \

624 1, \_stream\_context), \

625 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 117u, 4u, 15u, 40000u))

626

[ 633](group__bt__bap__lc3__preset.md#ga729a73a1c6484d7538dd469b2b0f8e5e)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_6\_1(\_loc, \_stream\_context) \

634 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

635 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 155u, 1, \

636 \_stream\_context), \

637 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 155u, 4u, 20u, 40000u))

638

645/\* Following presets are for broadcast high reliability audio data \*/

[ 646](group__bt__bap__lc3__preset.md#ga8038c67898c42e0671fb341eedd416d1)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_1\_2(\_loc, \_stream\_context) \

647 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

648 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 26u, 1, \

649 \_stream\_context), \

650 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 26u, 4u, 45u, 40000u))

651

[ 658](group__bt__bap__lc3__preset.md#gac24afbdcea6eadac1123ba4553d79b8b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_2\_2(\_loc, \_stream\_context) \

659 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, \

660 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 30U, 1, \

661 \_stream\_context), \

662 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 30u, 4u, 60u, 40000u))

663

[ 670](group__bt__bap__lc3__preset.md#gaa87f899e5205e7513a2d480ae8e8f448)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_1\_2(\_loc, \_stream\_context) \

671 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

672 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

673 \_stream\_context), \

674 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 30u, 4u, 45u, 40000u))

675

[ 684](group__bt__bap__lc3__preset.md#ga1c0bd6076e559c349bcf3c511d4d5e03)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_2\_2(\_loc, \_stream\_context) \

685 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

686 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

687 \_stream\_context), \

688 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 40u, 4u, 60u, 40000u))

689

[ 696](group__bt__bap__lc3__preset.md#gabc3b1b68ea7da77de6720679084c69db)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_1\_2(\_loc, \_stream\_context) \

697 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

698 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 45U, 1, \

699 \_stream\_context), \

700 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 45u, 4u, 45u, 40000u))

701

[ 710](group__bt__bap__lc3__preset.md#gad435c834787acf0634e4fab408f8965f)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_2\_2(\_loc, \_stream\_context) \

711 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, \

712 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 60U, 1, \

713 \_stream\_context), \

714 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 60u, 4u, 60u, 40000u))

715

[ 722](group__bt__bap__lc3__preset.md#ga2e89f8a6c6410057c7e5de2a56535e14)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_1\_2(\_loc, \_stream\_context) \

723 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

724 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

725 \_stream\_context), \

726 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 60u, 4u, 45u, 40000u))

727

[ 734](group__bt__bap__lc3__preset.md#ga2c92af221ebc679c8fdab5ce96b3457c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_2\_2(\_loc, \_stream\_context) \

735 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

736 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

737 \_stream\_context), \

738 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 80u, 4u, 60u, 40000u))

739

[ 746](group__bt__bap__lc3__preset.md#gae2d56f56ad6fbc074dcd7443f4c7d460)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_1\_2(\_loc, \_stream\_context) \

747 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

748 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 97U, 1, \

749 \_stream\_context), \

750 BT\_BAP\_QOS\_CFG\_FRAMED(8163u, 97u, 4u, 54u, 40000u))

751

[ 758](group__bt__bap__lc3__preset.md#gae4ee9d2021680837e3565a0efe4dc500)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_2\_2(\_loc, \_stream\_context) \

759 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, \

760 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 130U, 1, \

761 \_stream\_context), \

762 BT\_BAP\_QOS\_CFG\_FRAMED(10884u, 130u, 4u, 60u, 40000u))

763

[ 770](group__bt__bap__lc3__preset.md#gaa26017b9af7f3cf272b691a636af7ee4)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_1\_2(\_loc, \_stream\_context) \

771 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

772 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

773 \_stream\_context), \

774 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 75u, 4u, 50u, 40000u))

775

[ 782](group__bt__bap__lc3__preset.md#gaca9c3e309005396ccad12aa61b76b84b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_2\_2(\_loc, \_stream\_context) \

783 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

784 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

785 \_stream\_context), \

786 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 100u, 4u, 65u, 40000u))

787

[ 794](group__bt__bap__lc3__preset.md#gaa165b8b8ee72a23734d5f0b0a601e545)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_3\_2(\_loc, \_stream\_context) \

795 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

796 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

797 \_stream\_context), \

798 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 90u, 4u, 50u, 40000u))

799

[ 806](group__bt__bap__lc3__preset.md#ga309020ab3bfd78b6ce0c2e6b2bf8d556)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_4\_2(\_loc, \_stream\_context) \

807 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

808 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

809 \_stream\_context), \

810 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 120u, 4u, 65u, 40000u))

811

[ 818](group__bt__bap__lc3__preset.md#gaacf70e1663e6a2d3418e3daae804a6c0)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_5\_2(\_loc, \_stream\_context) \

819 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

820 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 117u, \

821 1, \_stream\_context), \

822 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 117u, 4u, 50u, 40000u))

823

[ 830](group__bt__bap__lc3__preset.md#ga6e3b3a3869024ba1fe4ea8f9047a225d)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_6\_2(\_loc, \_stream\_context) \

831 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

832 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 155u, 1, \

833 \_stream\_context), \

834 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 155u, 4u, 65u, 40000u))

835

836#ifdef \_\_cplusplus

837}

838#endif

840

841#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_LC3\_PRESET\_ \*/

[bap.h](bap_8h.md)

Header for Bluetooth BAP.

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[lc3.h](lc3_8h.md)

Bluetooth LC3 codec handling.

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:718

[bt\_bap\_lc3\_preset](structbt__bap__lc3__preset.md)

Struct to hold a BAP defined LC3 preset.

**Definition** bap\_lc3\_preset.h:38

[bt\_bap\_lc3\_preset::codec\_cfg](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da)

struct bt\_audio\_codec\_cfg codec\_cfg

The LC3 Codec.

**Definition** bap\_lc3\_preset.h:40

[bt\_bap\_lc3\_preset::qos](structbt__bap__lc3__preset.md#a8f5954471875861bfd387446060e9565)

struct bt\_bap\_qos\_cfg qos

The BAP spec defined QoS values.

**Definition** bap\_lc3\_preset.h:42

[bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md)

QoS configuration structure.

**Definition** bap.h:135

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [bap\_lc3\_preset.h](bap__lc3__preset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
