---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gmap__lc3__preset_8h_source.html
original_path: doxygen/html/gmap__lc3__preset_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gmap\_lc3\_preset.h

[Go to the documentation of this file.](gmap__lc3__preset_8h.md)

1

9

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_LC3\_PRESET\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_LC3\_PRESET\_

12

27

28#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

29#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>

30#include <[zephyr/bluetooth/audio/bap\_lc3\_preset.h](bap__lc3__preset_8h.md)>

31#include <[zephyr/bluetooth/audio/lc3.h](lc3_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

[ 43](group__bt__gmap__lc3__preset.md#ga6ec3341f2563494a10ae50bd709a6234)#define BT\_GMAP\_LC3\_PRESET\_32\_1\_GR(\_loc, \_stream\_context) \

44 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

45 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

46 \_stream\_context), \

47 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 60U, 1U, 15U, 10000U))

48

[ 55](group__bt__gmap__lc3__preset.md#ga7500c49ffb1d0cbb50faaab296954a9c)#define BT\_GMAP\_LC3\_PRESET\_32\_2\_GR(\_loc, \_stream\_context) \

56 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

57 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

58 \_stream\_context), \

59 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 80U, 1U, 20U, 10000U))

60

[ 67](group__bt__gmap__lc3__preset.md#gac5fbc4c6cd39292baaddfabe0a91547b)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_GR(\_loc, \_stream\_context) \

68 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

69 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

70 \_stream\_context), \

71 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 75U, 1U, 15U, 10000U))

72

[ 81](group__bt__gmap__lc3__preset.md#ga43266a8272f9d38ccfc7f845fb872bfa)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_GR(\_loc, \_stream\_context) \

82 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

83 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

84 \_stream\_context), \

85 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 100U, 1U, 20U, 10000U))

86

[ 93](group__bt__gmap__lc3__preset.md#ga4b904abf0faf7ffef5e8680c90f861a6)#define BT\_GMAP\_LC3\_PRESET\_48\_3\_GR(\_loc, \_stream\_context) \

94 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

95 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

96 \_stream\_context), \

97 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 90U, 1U, 15U, 10000U))

98

[ 107](group__bt__gmap__lc3__preset.md#ga6d5438cd5121dc1853d185ce17278fac)#define BT\_GMAP\_LC3\_PRESET\_48\_4\_GR(\_loc, \_stream\_context) \

108 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

109 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

110 \_stream\_context), \

111 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 120U, 1U, 20U, 10000U))

112

[ 119](group__bt__gmap__lc3__preset.md#ga01fd21cc55b4edbef612e704fc26fa0e)#define BT\_GMAP\_LC3\_PRESET\_16\_1\_GS(\_loc, \_stream\_context) \

120 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

121 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

122 \_stream\_context), \

123 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 30U, 1U, 15U, 60000U))

124

[ 131](group__bt__gmap__lc3__preset.md#ga900e8e6e308558d1e307c5726b26f00d)#define BT\_GMAP\_LC3\_PRESET\_16\_2\_GS(\_loc, \_stream\_context) \

132 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

133 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

134 \_stream\_context), \

135 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 40U, 1U, 20U, 60000U))

136

[ 143](group__bt__gmap__lc3__preset.md#gad2f2bf8f120332be58c8d3dbfe4e2c48)#define BT\_GMAP\_LC3\_PRESET\_32\_1\_GS(\_loc, \_stream\_context) \

144 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

145 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

146 \_stream\_context), \

147 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 60U, 1U, 15U, 60000U))

148

[ 155](group__bt__gmap__lc3__preset.md#ga0261c82920c16db61c2a551b44ea549f)#define BT\_GMAP\_LC3\_PRESET\_32\_2\_GS(\_loc, \_stream\_context) \

156 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

157 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

158 \_stream\_context), \

159 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 80U, 1U, 20U, 60000U))

160

[ 167](group__bt__gmap__lc3__preset.md#ga258ac93490e61fbf82e69afa441cbeca)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_GS(\_loc, \_stream\_context) \

168 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

169 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

170 \_stream\_context), \

171 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 75U, 1U, 15U, 60000U))

172

[ 179](group__bt__gmap__lc3__preset.md#ga4136fc4f83ebafb9d7574f7c750840aa)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_GS(\_loc, \_stream\_context) \

180 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

181 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

182 \_stream\_context), \

183 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 100U, 1U, 20U, 60000U))

184

185/\* GMAP LC3 broadcast presets defined by table 3.22 in the GMAP v1.0 specification \*/

186

[ 193](group__bt__gmap__lc3__preset.md#ga50562ea208350e7669255613fe4bef14)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_G(\_loc, \_stream\_context) \

194 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

195 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

196 \_stream\_context), \

197 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 75U, 1U, 8U, 10000U))

198

[ 205](group__bt__gmap__lc3__preset.md#gad65b1c65aa9943e80934cbf7234646dc)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_G(\_loc, \_stream\_context) \

206 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

207 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

208 \_stream\_context), \

209 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 100U, 1U, 10U, 10000U))

210

[ 217](group__bt__gmap__lc3__preset.md#gabe6f21e869b54c962633ab3ac6be7a91)#define BT\_GMAP\_LC3\_PRESET\_48\_3\_G(\_loc, \_stream\_context) \

218 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

219 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

220 \_stream\_context), \

221 BT\_BAP\_QOS\_CFG\_UNFRAMED(7500u, 90U, 1U, 8U, 10000U))

222

[ 229](group__bt__gmap__lc3__preset.md#ga17d79f07ced6f8605abb88cedad5a4da)#define BT\_GMAP\_LC3\_PRESET\_48\_4\_G(\_loc, \_stream\_context) \

230 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

231 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

232 \_stream\_context), \

233 BT\_BAP\_QOS\_CFG\_UNFRAMED(10000u, 120U, 1U, 10U, 10000U))

234

235#ifdef \_\_cplusplus

236}

237#endif

239

240#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_LC3\_PRESET\_ \*/

[bap.h](bap_8h.md)

Header for Bluetooth BAP.

[bap\_lc3\_preset.h](bap__lc3__preset_8h.md)

Header for Bluetooth BAP LC3 presets.

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[lc3.h](lc3_8h.md)

Bluetooth LC3 codec handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [gmap\_lc3\_preset.h](gmap__lc3__preset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
