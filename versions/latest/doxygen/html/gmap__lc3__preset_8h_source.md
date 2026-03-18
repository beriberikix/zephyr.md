---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gmap__lc3__preset_8h_source.html
original_path: doxygen/html/gmap__lc3__preset_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gmap\_lc3\_preset.h

[Go to the documentation of this file.](gmap__lc3__preset_8h.md)

1

8

9#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_LC3\_PRESET\_

10#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_LC3\_PRESET\_

11

12#include <[zephyr/bluetooth/audio/bap\_lc3\_preset.h](bap__lc3__preset_8h.md)>

13

14/\* GMAP LC3 unicast presets defined by table 3.16 in the GMAP v1.0 specification \*/

15

[ 22](gmap__lc3__preset_8h.md#a6ec3341f2563494a10ae50bd709a6234)#define BT\_GMAP\_LC3\_PRESET\_32\_1\_GR(\_loc, \_stream\_context) \

23 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1(\_loc, \_stream\_context), \

24 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(60U, 1U, 15U, 10000U))

25

[ 32](gmap__lc3__preset_8h.md#a7500c49ffb1d0cbb50faaab296954a9c)#define BT\_GMAP\_LC3\_PRESET\_32\_2\_GR(\_loc, \_stream\_context) \

33 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2(\_loc, \_stream\_context), \

34 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(80U, 1U, 20U, 10000U))

35

[ 42](gmap__lc3__preset_8h.md#ac5fbc4c6cd39292baaddfabe0a91547b)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_GR(\_loc, \_stream\_context) \

43 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context), \

44 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(75U, 1U, 15U, 10000U))

45

[ 54](gmap__lc3__preset_8h.md#a43266a8272f9d38ccfc7f845fb872bfa)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_GR(\_loc, \_stream\_context) \

55 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context), \

56 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(100U, 1U, 20U, 10000U))

57

[ 64](gmap__lc3__preset_8h.md#a4b904abf0faf7ffef5e8680c90f861a6)#define BT\_GMAP\_LC3\_PRESET\_48\_3\_GR(\_loc, \_stream\_context) \

65 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3(\_loc, \_stream\_context), \

66 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(90U, 1U, 15U, 10000U))

67

[ 76](gmap__lc3__preset_8h.md#a6d5438cd5121dc1853d185ce17278fac)#define BT\_GMAP\_LC3\_PRESET\_48\_4\_GR(\_loc, \_stream\_context) \

77 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4(\_loc, \_stream\_context), \

78 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(120U, 1U, 20U, 10000U))

79

[ 86](gmap__lc3__preset_8h.md#a01fd21cc55b4edbef612e704fc26fa0e)#define BT\_GMAP\_LC3\_PRESET\_16\_1\_GS(\_loc, \_stream\_context) \

87 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1(\_loc, \_stream\_context), \

88 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(30U, 1U, 15U, 60000U))

89

[ 96](gmap__lc3__preset_8h.md#a900e8e6e308558d1e307c5726b26f00d)#define BT\_GMAP\_LC3\_PRESET\_16\_2\_GS(\_loc, \_stream\_context) \

97 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2(\_loc, \_stream\_context), \

98 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(40U, 1U, 20U, 60000U))

99

[ 106](gmap__lc3__preset_8h.md#ad2f2bf8f120332be58c8d3dbfe4e2c48)#define BT\_GMAP\_LC3\_PRESET\_32\_1\_GS(\_loc, \_stream\_context) \

107 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1(\_loc, \_stream\_context), \

108 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(60U, 1U, 15U, 60000U))

109

[ 116](gmap__lc3__preset_8h.md#a0261c82920c16db61c2a551b44ea549f)#define BT\_GMAP\_LC3\_PRESET\_32\_2\_GS(\_loc, \_stream\_context) \

117 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2(\_loc, \_stream\_context), \

118 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(80U, 1U, 20U, 60000U))

119

[ 126](gmap__lc3__preset_8h.md#a258ac93490e61fbf82e69afa441cbeca)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_GS(\_loc, \_stream\_context) \

127 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context), \

128 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(75U, 1U, 15U, 60000U))

129

[ 136](gmap__lc3__preset_8h.md#a4136fc4f83ebafb9d7574f7c750840aa)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_GS(\_loc, \_stream\_context) \

137 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context), \

138 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(100U, 1U, 20U, 60000U))

139

140/\* GMAP LC3 broadcast presets defined by table 3.22 in the GMAP v1.0 specification \*/

141

[ 148](gmap__lc3__preset_8h.md#a50562ea208350e7669255613fe4bef14)#define BT\_GMAP\_LC3\_PRESET\_48\_1\_G(\_loc, \_stream\_context) \

149 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1(\_loc, \_stream\_context), \

150 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(75U, 1U, 8U, 10000U))

151

[ 158](gmap__lc3__preset_8h.md#ad65b1c65aa9943e80934cbf7234646dc)#define BT\_GMAP\_LC3\_PRESET\_48\_2\_G(\_loc, \_stream\_context) \

159 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2(\_loc, \_stream\_context), \

160 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(100U, 1U, 10U, 10000U))

161

[ 168](gmap__lc3__preset_8h.md#abe6f21e869b54c962633ab3ac6be7a91)#define BT\_GMAP\_LC3\_PRESET\_48\_3\_G(\_loc, \_stream\_context) \

169 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3(\_loc, \_stream\_context), \

170 BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED(90U, 1U, 8U, 10000U))

171

[ 178](gmap__lc3__preset_8h.md#a17d79f07ced6f8605abb88cedad5a4da)#define BT\_GMAP\_LC3\_PRESET\_48\_4\_G(\_loc, \_stream\_context) \

179 BT\_BAP\_LC3\_PRESET(BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4(\_loc, \_stream\_context), \

180 BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED(120U, 1U, 10U, 10000U))

181

182#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_LC3\_PRESET\_ \*/

[bap\_lc3\_preset.h](bap__lc3__preset_8h.md)

Header for Bluetooth BAP LC3 presets.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [gmap\_lc3\_preset.h](gmap__lc3__preset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
