---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gmap__lc3__preset_8h_source.html
original_path: doxygen/html/gmap__lc3__preset_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

29#include <[zephyr/bluetooth/audio/bap\_lc3\_preset.h](bap__lc3__preset_8h.md)>

30#include <[zephyr/bluetooth/audio/lc3.h](lc3_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 42](group__bt__gmap__lc3__preset.md#ga6ec3341f2563494a10ae50bd709a6234)#define BT\_GMAP\_LC3\_PRESET\_32\_1\_GR(\_loc, \_stream\_context) \

43 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

44 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

45 \_stream\_context), \

46 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 60U, 1U, 15U, 10000U))

47

[ 54](group__bt__gmap__lc3__preset.md#ga7500c49ffb1d0cbb50faaab296954a9c)#define BT\_GMAP\_LC3\_PRESET\_32\_2\_GR(\_loc, \_stream\_context) \

55 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

56 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

57 \_stream\_context), \

58 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 80U, 1U, 20U, 10000U))

59

[ 66](group__bt__gmap__lc3__preset.md#gac5fbc4c6cd39292baaddfabe0a91547b)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_GR(\_loc, \_stream\_context) \

67 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

68 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

69 \_stream\_context), \

70 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 75U, 1U, 15U, 10000U))

71

[ 80](group__bt__gmap__lc3__preset.md#ga43266a8272f9d38ccfc7f845fb872bfa)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_GR(\_loc, \_stream\_context) \

81 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

82 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

83 \_stream\_context), \

84 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 100U, 1U, 20U, 10000U))

85

[ 92](group__bt__gmap__lc3__preset.md#ga4b904abf0faf7ffef5e8680c90f861a6)#define BT\_GMAP\_LC3\_PRESET\_48\_3\_GR(\_loc, \_stream\_context) \

93 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

94 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

95 \_stream\_context), \

96 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 90U, 1U, 15U, 10000U))

97

[ 106](group__bt__gmap__lc3__preset.md#ga6d5438cd5121dc1853d185ce17278fac)#define BT\_GMAP\_LC3\_PRESET\_48\_4\_GR(\_loc, \_stream\_context) \

107 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

108 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

109 \_stream\_context), \

110 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 120U, 1U, 20U, 10000U))

111

[ 118](group__bt__gmap__lc3__preset.md#ga01fd21cc55b4edbef612e704fc26fa0e)#define BT\_GMAP\_LC3\_PRESET\_16\_1\_GS(\_loc, \_stream\_context) \

119 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

120 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 30U, 1, \

121 \_stream\_context), \

122 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 30U, 1U, 15U, 60000U))

123

[ 130](group__bt__gmap__lc3__preset.md#ga900e8e6e308558d1e307c5726b26f00d)#define BT\_GMAP\_LC3\_PRESET\_16\_2\_GS(\_loc, \_stream\_context) \

131 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ, \

132 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 40U, 1, \

133 \_stream\_context), \

134 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 40U, 1U, 20U, 60000U))

135

[ 142](group__bt__gmap__lc3__preset.md#gad2f2bf8f120332be58c8d3dbfe4e2c48)#define BT\_GMAP\_LC3\_PRESET\_32\_1\_GS(\_loc, \_stream\_context) \

143 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

144 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 60U, 1, \

145 \_stream\_context), \

146 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 60U, 1U, 15U, 60000U))

147

[ 154](group__bt__gmap__lc3__preset.md#ga0261c82920c16db61c2a551b44ea549f)#define BT\_GMAP\_LC3\_PRESET\_32\_2\_GS(\_loc, \_stream\_context) \

155 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ, \

156 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 80U, 1, \

157 \_stream\_context), \

158 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 80U, 1U, 20U, 60000U))

159

[ 166](group__bt__gmap__lc3__preset.md#ga258ac93490e61fbf82e69afa441cbeca)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_GS(\_loc, \_stream\_context) \

167 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

168 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

169 \_stream\_context), \

170 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 75U, 1U, 15U, 60000U))

171

[ 178](group__bt__gmap__lc3__preset.md#ga4136fc4f83ebafb9d7574f7c750840aa)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_GS(\_loc, \_stream\_context) \

179 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

180 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

181 \_stream\_context), \

182 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 100U, 1U, 20U, 60000U))

183

184/\* GMAP LC3 broadcast presets defined by table 3.22 in the GMAP v1.0 specification \*/

185

[ 192](group__bt__gmap__lc3__preset.md#ga50562ea208350e7669255613fe4bef14)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_G(\_loc, \_stream\_context) \

193 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

194 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 75U, 1, \

195 \_stream\_context), \

196 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 75U, 1U, 8U, 10000U))

197

[ 204](group__bt__gmap__lc3__preset.md#gad65b1c65aa9943e80934cbf7234646dc)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_G(\_loc, \_stream\_context) \

205 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

206 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 100U, 1, \

207 \_stream\_context), \

208 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 100U, 1U, 10U, 10000U))

209

[ 216](group__bt__gmap__lc3__preset.md#gabe6f21e869b54c962633ab3ac6be7a91)#define BT\_GMAP\_LC3\_PRESET\_48\_3\_G(\_loc, \_stream\_context) \

217 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

218 BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5, \_loc, 90U, 1, \

219 \_stream\_context), \

220 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(7500u, 90U, 1U, 8U, 10000U))

221

[ 228](group__bt__gmap__lc3__preset.md#ga17d79f07ced6f8605abb88cedad5a4da)#define BT\_GMAP\_LC3\_PRESET\_48\_4\_G(\_loc, \_stream\_context) \

229 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG(BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ, \

230 BT\_AUDIO\_CODEC\_CFG\_DURATION\_10, \_loc, 120u, 1, \

231 \_stream\_context), \

232 BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(10000u, 120U, 1U, 10U, 10000U))

233

234#ifdef \_\_cplusplus

235}

236#endif

238

239#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_LC3\_PRESET\_ \*/

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
