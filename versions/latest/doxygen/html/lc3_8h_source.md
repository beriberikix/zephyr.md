---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lc3_8h_source.html
original_path: doxygen/html/lc3_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lc3.h

[Go to the documentation of this file.](lc3_8h.md)

1

4

5/\*

6 \* Copyright (c) 2020 Intel Corporation

7 \* Copyright (c) 2022 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_LC3\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_LC3\_H\_

13

20

21#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

22#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h.md)>

23#include <[zephyr/bluetooth/hci\_types.h](hci__types_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

34/\* COND\_CODE\_1 is used to omit an LTV entry in case the \_frames\_per\_sdu is 1.

35 \* COND\_CODE\_1 will evaluate to second argument if the flag parameter(first argument) is 1

36 \* - removing one layer of paranteses.

37 \* If the flags argument is != 1 it will evaluate to the third argument which inserts a LTV

38 \* entry for the max\_frames\_per\_sdu value.

39 \*/

40

[ 41](group__BT__AUDIO__CODEC__LC3.md#ga8d679b241585ff5ebff0d97bb22dfda9)#define BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \

42 \_max\_frames\_per\_sdu) \

43 { \

44 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ, BT\_BYTES\_LIST\_LE16(\_freq)), \

45 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION, (\_duration)), \

46 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT, (\_chan\_count)), \

47 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN, \

48 BT\_BYTES\_LIST\_LE16(\_len\_min), \

49 BT\_BYTES\_LIST\_LE16(\_len\_max)), \

50 COND\_CODE\_1(\_max\_frames\_per\_sdu, (), \

51 (BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT, \

52 (\_max\_frames\_per\_sdu)))) \

53 }

54

[ 58](group__BT__AUDIO__CODEC__LC3.md#ga9b5d5e300a7b41060329dbdd2cd073f6)#define BT\_AUDIO\_CODEC\_CAP\_LC3\_META(\_prefer\_context) \

59 { \

60 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT, \

61 BT\_BYTES\_LIST\_LE16(\_prefer\_context)) \

62 }

63

[ 76](group__BT__AUDIO__CODEC__LC3.md#gac474746e7314ebf7ed77b8937191cdc1)#define BT\_AUDIO\_CODEC\_CAP\_LC3(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \

77 \_max\_frames\_per\_sdu, \_prefer\_context) \

78 BT\_AUDIO\_CODEC\_CAP(BT\_HCI\_CODING\_FORMAT\_LC3, 0x0000, 0x0000, \

79 BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA(\_freq, \_duration, \_chan\_count, \_len\_min, \

80 \_len\_max, \_max\_frames\_per\_sdu), \

81 BT\_AUDIO\_CODEC\_CAP\_LC3\_META(\_prefer\_context))

82

[ 93](group__BT__AUDIO__CODEC__LC3.md#ga497ff0aa1d7dcfeea6ec549e5fb155d6)#define BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu) \

94 { \

95 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_FREQ, (\_freq)), \

96 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_DURATION, (\_duration)), \

97 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC, BT\_BYTES\_LIST\_LE32(\_loc)), \

98 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN, BT\_BYTES\_LIST\_LE16(\_len)), \

99 COND\_CODE\_1(\_frames\_per\_sdu, (), \

100 (BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU, \

101 (\_frames\_per\_sdu)))) \

102 }

103

[ 107](group__BT__AUDIO__CODEC__LC3.md#ga2c00f8bd526305d878624c6f1b8030f8)#define BT\_AUDIO\_CODEC\_CFG\_LC3\_META(\_stream\_context) \

108 { \

109 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT, \

110 BT\_BYTES\_LIST\_LE16(\_stream\_context)) \

111 }

112

[ 123](group__BT__AUDIO__CODEC__LC3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu, \_stream\_context) \

124 BT\_AUDIO\_CODEC\_CFG( \

125 BT\_HCI\_CODING\_FORMAT\_LC3, 0x0000, 0x0000, \

126 BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu), \

127 BT\_AUDIO\_CODEC\_CFG\_LC3\_META(\_stream\_context))

128

[ 135](group__BT__AUDIO__CODEC__LC3.md#gaee65a79f2bb704bf5296b778a0e3ad2c)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1(\_loc, \_stream\_context) \

136 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \

137 \_loc, 26u, 1, \_stream\_context)

138

[ 144](group__BT__AUDIO__CODEC__LC3.md#gae279ffa1d4eef72d94083bdae968c102)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2(\_loc, \_stream\_context) \

145 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \

146 \_loc, 30u, 1, \_stream\_context)

147

[ 153](group__BT__AUDIO__CODEC__LC3.md#gaff29f4ccabab99c7e25fcbf9d10cc789)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1(\_loc, \_stream\_context) \

154 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \

155 \_loc, 30u, 1, \_stream\_context)

156

[ 162](group__BT__AUDIO__CODEC__LC3.md#gabf16c8c87682fd9faf180af129bddfd5)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2(\_loc, \_stream\_context) \

163 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \

164 \_loc, 40u, 1, \_stream\_context)

165

[ 172](group__BT__AUDIO__CODEC__LC3.md#ga0655c6ca0c99002493a854cb88969a2b)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1(\_loc, \_stream\_context) \

173 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \

174 \_loc, 45u, 1, \_stream\_context)

175

[ 181](group__BT__AUDIO__CODEC__LC3.md#gae8c8a34377b910f52d851dadb9f4216b)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2(\_loc, \_stream\_context) \

182 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \

183 \_loc, 60u, 1, \_stream\_context)

184

[ 190](group__BT__AUDIO__CODEC__LC3.md#ga57a7bf0bbf38e70cfc27e1c267092277)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1(\_loc, \_stream\_context) \

191 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \

192 \_loc, 60u, 1, \_stream\_context)

193

[ 199](group__BT__AUDIO__CODEC__LC3.md#ga25879311182d38adaca5238cdf016ac4)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2(\_loc, \_stream\_context) \

200 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \

201 \_loc, 80u, 1, \_stream\_context)

202

[ 208](group__BT__AUDIO__CODEC__LC3.md#gad046616ed5367d1e2c674df545def632)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1(\_loc, \_stream\_context) \

209 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \

210 \_loc, 98u, 1, \_stream\_context)

211

[ 217](group__BT__AUDIO__CODEC__LC3.md#ga7789d2447105581e5e520c930f19f8ed)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2(\_loc, \_stream\_context) \

218 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \

219 \_loc, 130u, 1, \_stream\_context)

220

[ 226](group__BT__AUDIO__CODEC__LC3.md#ga613c2f21212b626f83e37c5614e7129e)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context) \

227 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \

228 \_loc, 75u, 1, \_stream\_context)

229

[ 235](group__BT__AUDIO__CODEC__LC3.md#gab5342debdef776007a78576f8d0917dd)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context) \

236 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \

237 \_loc, 100u, 1, \_stream\_context)

238

[ 244](group__BT__AUDIO__CODEC__LC3.md#ga60f65e6c9b9f940a66756f91c82cd64e)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3(\_loc, \_stream\_context) \

245 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \

246 \_loc, 90u, 1, \_stream\_context)

247

[ 253](group__BT__AUDIO__CODEC__LC3.md#gaefa8bdddf5b56cad4b9096eac1abb49d)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4(\_loc, \_stream\_context) \

254 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \

255 \_loc, 120u, 1, \_stream\_context)

256

[ 262](group__BT__AUDIO__CODEC__LC3.md#ga3366230cd60d3e3b05e7cb2a56cfdd26)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5(\_loc, \_stream\_context) \

263 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \

264 \_loc, 117u, 1, \_stream\_context)

265

[ 271](group__BT__AUDIO__CODEC__LC3.md#ga428a49b8528e62f6f686837dc95ba1b6)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6(\_loc, \_stream\_context) \

272 BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \

273 \_loc, 155u, 1, \_stream\_context)

274

[ 277](group__BT__AUDIO__CODEC__LC3.md#ga5bfa82c8858a4fb3fcd7ce26afbd7601)#define BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5(\_framing, \_sdu, \_rtn, \_latency, \_pd) \

278 BT\_AUDIO\_CODEC\_QOS(7500u, \_framing, BT\_AUDIO\_CODEC\_QOS\_2M, \_sdu, \_rtn, \_latency, \_pd)

279

[ 282](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)#define BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(\_sdu, \_rtn, \_latency, \_pd) \

283 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, \_sdu, \_rtn, \_latency, \_pd)

284

[ 287](group__BT__AUDIO__CODEC__LC3.md#gad951d0fb06dfe085db73228eef500bbc)#define BT\_AUDIO\_CODEC\_LC3\_QOS\_10(\_framing, \_sdu, \_rtn, \_latency, \_pd) \

288 BT\_AUDIO\_CODEC\_QOS(10000u, \_framing, BT\_AUDIO\_CODEC\_QOS\_2M, \_sdu, \_rtn, \_latency, \_pd)

289

[ 292](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)#define BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(\_sdu, \_rtn, \_latency, \_pd) \

293 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, \_sdu, \_rtn, \_latency, \_pd)

294

295#ifdef \_\_cplusplus

296}

297#endif

298

302

303#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_LC3\_H\_ \*/

[byteorder.h](bluetooth_2byteorder_8h.md)

Bluetooth byteorder API.

[hci\_types.h](hci__types_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [lc3.h](lc3_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
