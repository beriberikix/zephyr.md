---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bap__lc3__preset_8h_source.html
original_path: doxygen/html/bap__lc3__preset_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bap\_lc3\_preset.h

[Go to the documentation of this file.](bap__lc3__preset_8h.md)

1

8

9#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_LC3\_PRESET\_

10#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_LC3\_PRESET\_

11

12#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

13

[ 15](structbt__bap__lc3__preset.md)struct [bt\_bap\_lc3\_preset](structbt__bap__lc3__preset.md) {

[ 17](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da) struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) [codec\_cfg](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da);

[ 19](structbt__bap__lc3__preset.md#ab0708b8f1020c369278279e139992c93) struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) [qos](structbt__bap__lc3__preset.md#ab0708b8f1020c369278279e139992c93);

20};

21

[ 23](bap__lc3__preset_8h.md#a9f2075cd5019d356bc7ccf7f9cbc63bb)#define BT\_BAP\_LC3\_PRESET(\_codec, \_qos) \

24 { \

25 .codec\_cfg = \_codec, .qos = \_qos, \

26 }

27

28/\* LC3 Unicast presets defined by table 5.2 in the BAP v1.0 specification \*/

29

[ 36](bap__lc3__preset_8h.md#ac1a211ed3116a0b7f0b181abd0ae6e8a)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_1\_1(\_loc, \_stream\_context) \

37 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1(\_loc, \_stream\_context), \

38 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(26u, 2u, 8u, 40000u))

39

[ 46](bap__lc3__preset_8h.md#a8caa6c9cf34f45ac36f6450d9f076126)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_2\_1(\_loc, \_stream\_context) \

47 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2(\_loc, \_stream\_context), \

48 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(30u, 2u, 10u, 40000u))

49

[ 56](bap__lc3__preset_8h.md#aac67456c95c688b83b460bdcc0c696f1)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_1\_1(\_loc, \_stream\_context) \

57 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1(\_loc, \_stream\_context), \

58 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(30u, 2u, 8u, 40000u))

59

[ 68](bap__lc3__preset_8h.md#af5b1892e96c1f63c73dddfeda0843eeb)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_2\_1(\_loc, \_stream\_context) \

69 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2(\_loc, \_stream\_context), \

70 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(40u, 2u, 10u, 40000u))

71

[ 78](bap__lc3__preset_8h.md#abb43386a22cd9415c491a846aef85310)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_1\_1(\_loc, \_stream\_context) \

79 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1(\_loc, \_stream\_context), \

80 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(45u, 2u, 8u, 40000u))

81

[ 90](bap__lc3__preset_8h.md#a24555bc6189ad58f584be0bbbf085e24)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_2\_1(\_loc, \_stream\_context) \

91 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2(\_loc, \_stream\_context), \

92 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(60u, 2u, 10u, 40000u))

93

[ 100](bap__lc3__preset_8h.md#a39de4252e742ce815633ae7a50062f98)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_1\_1(\_loc, \_stream\_context) \

101 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1(\_loc, \_stream\_context), \

102 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(60u, 2u, 8u, 40000u))

103

[ 110](bap__lc3__preset_8h.md#a93a1fbdf0feba790464c41e362aea307)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_2\_1(\_loc, \_stream\_context) \

111 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2(\_loc, \_stream\_context), \

112 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(80u, 2u, 10u, 40000u))

113

[ 120](bap__lc3__preset_8h.md#ae9795a9dc12aa60c74a4aad0c35b18ac)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_1\_1(\_loc, \_stream\_context) \

121 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1(\_loc, \_stream\_context), \

122 BT\_AUDIO\_CODEC\_QOS(8163u, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, \

123 BT\_AUDIO\_CODEC\_QOS\_2M, 97u, 5u, 24u, 40000u))

124

[ 131](bap__lc3__preset_8h.md#a5508e46240176f5b054467609b635f0d)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_2\_1(\_loc, \_stream\_context) \

132 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2(\_loc, \_stream\_context), \

133 BT\_AUDIO\_CODEC\_QOS(10884u, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, \

134 BT\_AUDIO\_CODEC\_QOS\_2M, 130u, 5u, 31u, 40000u))

135

[ 142](bap__lc3__preset_8h.md#af2ad00922314b8ee06d3a001d1eafd94)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_1\_1(\_loc, \_stream\_context) \

143 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context), \

144 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(75u, 5u, 15u, 40000u))

145

[ 152](bap__lc3__preset_8h.md#aea3354a3c92d889324f48260216c15bf)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_2\_1(\_loc, \_stream\_context) \

153 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context), \

154 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(100u, 5u, 20u, 40000u))

155

[ 162](bap__lc3__preset_8h.md#abe085646c5709fcaa2ec830f006105c0)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_3\_1(\_loc, \_stream\_context) \

163 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3(\_loc, \_stream\_context), \

164 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(90u, 5u, 15u, 40000u))

165

[ 172](bap__lc3__preset_8h.md#a5a2c91592853163f3c88d490a8b6bd49)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_4\_1(\_loc, \_stream\_context) \

173 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4(\_loc, \_stream\_context), \

174 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(120u, 5u, 20u, 40000u))

175

[ 182](bap__lc3__preset_8h.md#a9dbd2e240b5a733044ab78ec73e6532e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_5\_1(\_loc, \_stream\_context) \

183 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5(\_loc, \_stream\_context), \

184 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(117u, 5u, 15u, 40000u))

185

[ 192](bap__lc3__preset_8h.md#aa4ee0f200c3484b1708a10ba5f5185a4)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_6\_1(\_loc, \_stream\_context) \

193 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6(\_loc, \_stream\_context), \

194 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(155u, 5u, 20u, 40000u))

195

202/\* Following presets are for unicast high reliability audio data \*/

[ 203](bap__lc3__preset_8h.md#a332cb00a9cfbf31444b9ca86ecb69cae)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_1\_2(\_loc, \_stream\_context) \

204 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1(\_loc, \_stream\_context), \

205 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(26u, 13u, 75u, 40000u))

206

[ 213](bap__lc3__preset_8h.md#a945c808feda5dd50d47f78a420c90768)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_8\_2\_2(\_loc, \_stream\_context) \

214 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2(\_loc, \_stream\_context), \

215 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(30u, 13u, 95u, 40000u))

216

[ 223](bap__lc3__preset_8h.md#a0191f12d56220dd5ef0842ccd5acbc2c)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_1\_2(\_loc, \_stream\_context) \

224 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1(\_loc, \_stream\_context), \

225 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(30u, 13u, 75u, 40000u))

226

[ 233](bap__lc3__preset_8h.md#ac4bb73b877cb170ad24f16d422d5752e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_16\_2\_2(\_loc, \_stream\_context) \

234 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2(\_loc, \_stream\_context), \

235 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(40u, 13u, 95u, 40000u))

236

[ 243](bap__lc3__preset_8h.md#a9055c137e206deab6c9d756db6dc24b5)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_1\_2(\_loc, \_stream\_context) \

244 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1(\_loc, \_stream\_context), \

245 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(45u, 13u, 75u, 40000u))

246

[ 253](bap__lc3__preset_8h.md#a3d044b67ae42487129e9df35a79e099e)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_24\_2\_2(\_loc, \_stream\_context) \

254 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2(\_loc, \_stream\_context), \

255 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(60u, 13u, 95u, 40000u))

256

[ 263](bap__lc3__preset_8h.md#a8e99870c84c8fc3bc7f294f534ee9b9d)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_1\_2(\_loc, \_stream\_context) \

264 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1(\_loc, \_stream\_context), \

265 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(60u, 13u, 75u, 40000u))

266

[ 273](bap__lc3__preset_8h.md#a01eb8a840451b914b8152f4d90a493c9)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_32\_2\_2(\_loc, \_stream\_context) \

274 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2(\_loc, \_stream\_context), \

275 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(80u, 13u, 95u, 40000u))

276

[ 283](bap__lc3__preset_8h.md#a70f32a61655cfc1bdd73164902b8b436)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_1\_2(\_loc, \_stream\_context) \

284 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1(\_loc, \_stream\_context), \

285 BT\_AUDIO\_CODEC\_QOS(8163u, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, \

286 BT\_AUDIO\_CODEC\_QOS\_2M, 97u, 13u, 80u, 40000u))

287

[ 294](bap__lc3__preset_8h.md#a66ea64d32c6b28bcf65e991e677f0567)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_441\_2\_2(\_loc, \_stream\_context) \

295 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2(\_loc, \_stream\_context), \

296 BT\_AUDIO\_CODEC\_QOS(10884u, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, \

297 BT\_AUDIO\_CODEC\_QOS\_2M, 130u, 13u, 85u, 40000u))

298

[ 305](bap__lc3__preset_8h.md#a4efe7f4016a829e3d301108eef8ef93c)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_1\_2(\_loc, \_stream\_context) \

306 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context), \

307 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(75u, 13u, 75u, 40000u))

308

[ 315](bap__lc3__preset_8h.md#a178d09a96e9e0823aed7c8965794ffe3)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_2\_2(\_loc, \_stream\_context) \

316 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context), \

317 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(100u, 13u, 95u, 40000u))

318

[ 325](bap__lc3__preset_8h.md#abfba888ded2aa54c044e8862d0b95da0)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_3\_2(\_loc, \_stream\_context) \

326 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3(\_loc, \_stream\_context), \

327 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(90u, 13u, 75u, 40000u))

328

[ 335](bap__lc3__preset_8h.md#a7624cdd35f1eec81c17acf41dd9c85f3)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_4\_2(\_loc, \_stream\_context) \

336 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4(\_loc, \_stream\_context), \

337 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(120u, 13u, 100u, 40000u))

338

[ 345](bap__lc3__preset_8h.md#acd6af79c79e587e9c0f858672ec79f49)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_5\_2(\_loc, \_stream\_context) \

346 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5(\_loc, \_stream\_context), \

347 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(117u, 13u, 75u, 40000u))

348

[ 355](bap__lc3__preset_8h.md#aea427c1bb97174941d7feae359e7f8fd)#define BT\_BAP\_LC3\_UNICAST\_PRESET\_48\_6\_2(\_loc, \_stream\_context) \

356 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6(\_loc, \_stream\_context), \

357 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(155u, 13u, 100u, 40000u))

358

365/\* LC3 Broadcast presets defined by table 6.4 in the BAP v1.0 specification \*/

[ 366](bap__lc3__preset_8h.md#a71551e9a3382c4c3391cdbe3f3b155eb)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_1\_1(\_loc, \_stream\_context) \

367 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1(\_loc, \_stream\_context), \

368 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(26u, 2u, 8u, 40000u))

369

[ 376](bap__lc3__preset_8h.md#a09a29e1a76185dfd783d428f862ea8dd)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_2\_1(\_loc, \_stream\_context) \

377 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2(\_loc, \_stream\_context), \

378 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(30u, 2u, 10u, 40000u))

379

[ 386](bap__lc3__preset_8h.md#aa17732bcb085e97856bd5e7a65a3255c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_1\_1(\_loc, \_stream\_context) \

387 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1(\_loc, \_stream\_context), \

388 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(30u, 2u, 8u, 40000u))

389

[ 398](bap__lc3__preset_8h.md#a8ded042093c310e84ccc76c4d9a67b9c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_2\_1(\_loc, \_stream\_context) \

399 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2(\_loc, \_stream\_context), \

400 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(40u, 2u, 10u, 40000u))

401

[ 408](bap__lc3__preset_8h.md#a2a4ccfe1ce99443f2e07ec629e22a1af)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_1\_1(\_loc, \_stream\_context) \

409 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1(\_loc, \_stream\_context), \

410 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(45u, 2u, 8u, 40000u))

411

[ 420](bap__lc3__preset_8h.md#a38c76ab52c627c2d1622b9fd2511367a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_2\_1(\_loc, \_stream\_context) \

421 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2(\_loc, \_stream\_context), \

422 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(60u, 2u, 10u, 40000u))

423

[ 430](bap__lc3__preset_8h.md#a3842c0a4531a087830d133924542282f)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_1\_1(\_loc, \_stream\_context) \

431 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1(\_loc, \_stream\_context), \

432 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(60u, 2u, 8u, 40000u))

433

[ 440](bap__lc3__preset_8h.md#a883b0d45657ae3a4902d2c9df3392447)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_2\_1(\_loc, \_stream\_context) \

441 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2(\_loc, \_stream\_context), \

442 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(80u, 2u, 10u, 40000u))

443

[ 450](bap__lc3__preset_8h.md#a31f25a4a4549659370bd2d3040aca84a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_1\_1(\_loc, \_stream\_context) \

451 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1(\_loc, \_stream\_context), \

452 BT\_AUDIO\_CODEC\_QOS(8163u, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, \

453 BT\_AUDIO\_CODEC\_QOS\_2M, 97u, 4u, 24u, 40000u))

454

[ 461](bap__lc3__preset_8h.md#a09345dd8d9afecfae24aecf760576aeb)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_2\_1(\_loc, \_stream\_context) \

462 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2(\_loc, \_stream\_context), \

463 BT\_AUDIO\_CODEC\_QOS(10884u, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, \

464 BT\_AUDIO\_CODEC\_QOS\_2M, 130u, 4u, 31u, 40000u))

465

[ 472](bap__lc3__preset_8h.md#ab22a08b23523b080340727261213c8fc)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_1\_1(\_loc, \_stream\_context) \

473 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context), \

474 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(75u, 4u, 15u, 40000u))

475

[ 482](bap__lc3__preset_8h.md#a7d280583165d63be595af48fed07309a)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_2\_1(\_loc, \_stream\_context) \

483 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context), \

484 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(100u, 4u, 20u, 40000u))

485

[ 492](bap__lc3__preset_8h.md#a8046777cdace9ed5c29d4ce347396c41)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_3\_1(\_loc, \_stream\_context) \

493 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3(\_loc, \_stream\_context), \

494 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(90u, 4u, 15u, 40000u))

495

[ 502](bap__lc3__preset_8h.md#ace016322c5fda54a55fa60af45250191)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_4\_1(\_loc, \_stream\_context) \

503 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4(\_loc, \_stream\_context), \

504 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(120u, 4u, 20u, 40000u))

505

[ 512](bap__lc3__preset_8h.md#aa1c10f0cf98a707e73cb86b05838b60b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_5\_1(\_loc, \_stream\_context) \

513 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5(\_loc, \_stream\_context), \

514 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(117u, 4u, 15u, 40000u))

515

[ 522](bap__lc3__preset_8h.md#a729a73a1c6484d7538dd469b2b0f8e5e)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_6\_1(\_loc, \_stream\_context) \

523 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6(\_loc, \_stream\_context), \

524 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(155u, 4u, 20u, 40000u))

525

532/\* Following presets are for broadcast high reliability audio data \*/

[ 533](bap__lc3__preset_8h.md#a8038c67898c42e0671fb341eedd416d1)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_1\_2(\_loc, \_stream\_context) \

534 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1(\_loc, \_stream\_context), \

535 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(26u, 4u, 45u, 40000u))

536

[ 543](bap__lc3__preset_8h.md#ac24afbdcea6eadac1123ba4553d79b8b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_8\_2\_2(\_loc, \_stream\_context) \

544 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2(\_loc, \_stream\_context), \

545 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(30u, 4u, 60u, 40000u))

546

[ 553](bap__lc3__preset_8h.md#aa87f899e5205e7513a2d480ae8e8f448)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_1\_2(\_loc, \_stream\_context) \

554 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1(\_loc, \_stream\_context), \

555 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(30u, 4u, 45u, 40000u))

556

[ 565](bap__lc3__preset_8h.md#a1c0bd6076e559c349bcf3c511d4d5e03)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_16\_2\_2(\_loc, \_stream\_context) \

566 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2(\_loc, \_stream\_context), \

567 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(40u, 4u, 60u, 40000u))

568

[ 575](bap__lc3__preset_8h.md#abc3b1b68ea7da77de6720679084c69db)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_1\_2(\_loc, \_stream\_context) \

576 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1(\_loc, \_stream\_context), \

577 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(45u, 4u, 45u, 40000u))

578

[ 587](bap__lc3__preset_8h.md#ad435c834787acf0634e4fab408f8965f)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_24\_2\_2(\_loc, \_stream\_context) \

588 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2(\_loc, \_stream\_context), \

589 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(60u, 4u, 60u, 40000u))

590

[ 597](bap__lc3__preset_8h.md#a2e89f8a6c6410057c7e5de2a56535e14)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_1\_2(\_loc, \_stream\_context) \

598 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1(\_loc, \_stream\_context), \

599 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(60u, 4u, 45u, 40000u))

600

[ 607](bap__lc3__preset_8h.md#a2c92af221ebc679c8fdab5ce96b3457c)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_32\_2\_2(\_loc, \_stream\_context) \

608 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2(\_loc, \_stream\_context), \

609 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(80u, 4u, 60u, 40000u))

610

[ 617](bap__lc3__preset_8h.md#ae2d56f56ad6fbc074dcd7443f4c7d460)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_1\_2(\_loc, \_stream\_context) \

618 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1(\_loc, \_stream\_context), \

619 BT\_AUDIO\_CODEC\_QOS(8163u, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, \

620 BT\_AUDIO\_CODEC\_QOS\_2M, 97u, 4u, 54u, 40000u))

621

[ 628](bap__lc3__preset_8h.md#ae4ee9d2021680837e3565a0efe4dc500)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_441\_2\_2(\_loc, \_stream\_context) \

629 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2(\_loc, \_stream\_context), \

630 BT\_AUDIO\_CODEC\_QOS(10884u, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, \

631 BT\_AUDIO\_CODEC\_QOS\_2M, 130u, 4u, 60u, 40000u))

632

[ 639](bap__lc3__preset_8h.md#aa26017b9af7f3cf272b691a636af7ee4)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_1\_2(\_loc, \_stream\_context) \

640 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context), \

641 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(75u, 4u, 50u, 40000u))

642

[ 649](bap__lc3__preset_8h.md#aca9c3e309005396ccad12aa61b76b84b)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_2\_2(\_loc, \_stream\_context) \

650 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context), \

651 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(100u, 4u, 65u, 40000u))

652

[ 659](bap__lc3__preset_8h.md#aa165b8b8ee72a23734d5f0b0a601e545)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_3\_2(\_loc, \_stream\_context) \

660 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3(\_loc, \_stream\_context), \

661 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(90u, 4u, 50u, 40000u))

662

[ 669](bap__lc3__preset_8h.md#a309020ab3bfd78b6ce0c2e6b2bf8d556)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_4\_2(\_loc, \_stream\_context) \

670 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4(\_loc, \_stream\_context), \

671 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(120u, 4u, 65u, 40000u))

672

[ 679](bap__lc3__preset_8h.md#aacf70e1663e6a2d3418e3daae804a6c0)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_5\_2(\_loc, \_stream\_context) \

680 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5(\_loc, \_stream\_context), \

681 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(117u, 4u, 50u, 40000u))

682

[ 689](bap__lc3__preset_8h.md#a6e3b3a3869024ba1fe4ea8f9047a225d)#define BT\_BAP\_LC3\_BROADCAST\_PRESET\_48\_6\_2(\_loc, \_stream\_context) \

690 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6(\_loc, \_stream\_context), \

691 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(155u, 4u, 65u, 40000u))

692

693#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_BAP\_LC3\_PRESET\_ \*/

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:584

[bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)

Codec QoS structure.

**Definition** audio.h:702

[bt\_bap\_lc3\_preset](structbt__bap__lc3__preset.md)

Struct to hold a BAP defined LC3 preset.

**Definition** bap\_lc3\_preset.h:15

[bt\_bap\_lc3\_preset::codec\_cfg](structbt__bap__lc3__preset.md#a2615416828c62842a076749796beb6da)

struct bt\_audio\_codec\_cfg codec\_cfg

The LC3 Codec.

**Definition** bap\_lc3\_preset.h:17

[bt\_bap\_lc3\_preset::qos](structbt__bap__lc3__preset.md#ab0708b8f1020c369278279e139992c93)

struct bt\_audio\_codec\_qos qos

The BAP spec defined QoS values.

**Definition** bap\_lc3\_preset.h:19

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [bap\_lc3\_preset.h](bap__lc3__preset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
