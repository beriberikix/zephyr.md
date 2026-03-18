---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbc__ppc_8h_source.html
original_path: doxygen/html/usbc__ppc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_ppc.h

[Go to the documentation of this file.](usbc__ppc_8h.md)

1/\*

2 \* Copyright 2023 Google LLC

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_PPC\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_PPC\_H\_

14

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17#include <[errno.h](errno_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 24](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9)enum [usbc\_ppc\_event](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9) {

[ 26](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e) [USBC\_PPC\_EVENT\_DEAD\_BATTERY\_ERROR](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e) = 0,

27

[ 29](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109) [USBC\_PPC\_EVENT\_SRC\_OVERVOLTAGE](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109),

[ 31](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6) [USBC\_PPC\_EVENT\_SRC\_REVERSE\_CURRENT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6),

[ 33](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238) [USBC\_PPC\_EVENT\_SRC\_OVERCURRENT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238),

[ 35](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4) [USBC\_PPC\_EVENT\_SRC\_SHORT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4),

36

[ 38](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c) [USBC\_PPC\_EVENT\_OVER\_TEMPERATURE](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c),

[ 40](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94) [USBC\_PPC\_EVENT\_BOTH\_SNKSRC\_ENABLED](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94),

41

[ 43](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759) [USBC\_PPC\_EVENT\_SNK\_REVERSE\_CURRENT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759),

[ 45](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d) [USBC\_PPC\_EVENT\_SNK\_SHORT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d),

[ 47](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e) [USBC\_PPC\_EVENT\_SNK\_OVERVOLTAGE](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e),

48};

49

[ 50](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73)typedef void (\*[usbc\_ppc\_event\_cb\_t](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73))(const struct [device](structdevice.md) \*dev, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), enum [usbc\_ppc\_event](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9) ev);

51

[ 53](structusbc__ppc__drv.md)\_\_subsystem struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) {

[ 54](structusbc__ppc__drv.md#a2641a5d2f8082a9fea2897d60992a81d) int (\*[is\_dead\_battery\_mode](structusbc__ppc__drv.md#a2641a5d2f8082a9fea2897d60992a81d))(const struct [device](structdevice.md) \*dev);

[ 55](structusbc__ppc__drv.md#ac66444729d18d875432ac4d31610c1cc) int (\*[exit\_dead\_battery\_mode](structusbc__ppc__drv.md#ac66444729d18d875432ac4d31610c1cc))(const struct [device](structdevice.md) \*dev);

[ 56](structusbc__ppc__drv.md#a3801f17cd627d99790cfbe45a20831e1) int (\*[is\_vbus\_source](structusbc__ppc__drv.md#a3801f17cd627d99790cfbe45a20831e1))(const struct [device](structdevice.md) \*dev);

[ 57](structusbc__ppc__drv.md#aa67d808b77e460159f6021e32701ede4) int (\*[is\_vbus\_sink](structusbc__ppc__drv.md#aa67d808b77e460159f6021e32701ede4))(const struct [device](structdevice.md) \*dev);

[ 58](structusbc__ppc__drv.md#a60f5d5d55a4037d380338830da3b7aef) int (\*[set\_snk\_ctrl](structusbc__ppc__drv.md#a60f5d5d55a4037d380338830da3b7aef))(const struct [device](structdevice.md) \*dev, bool enable);

[ 59](structusbc__ppc__drv.md#a18b223b9167e3d1aaa524a4f9aec87d5) int (\*[set\_src\_ctrl](structusbc__ppc__drv.md#a18b223b9167e3d1aaa524a4f9aec87d5))(const struct [device](structdevice.md) \*dev, bool enable);

[ 60](structusbc__ppc__drv.md#a5581e4e8c5dd709e85cca3ca3fe9ec09) int (\*[set\_vbus\_discharge](structusbc__ppc__drv.md#a5581e4e8c5dd709e85cca3ca3fe9ec09))(const struct [device](structdevice.md) \*dev, bool enable);

[ 61](structusbc__ppc__drv.md#acfb87bd73f5ed0114e988c24b43910ec) int (\*[is\_vbus\_present](structusbc__ppc__drv.md#acfb87bd73f5ed0114e988c24b43910ec))(const struct [device](structdevice.md) \*dev);

[ 62](structusbc__ppc__drv.md#a0bd893a73fad130849ad9549f6b3b9fd) int (\*[set\_event\_handler](structusbc__ppc__drv.md#a0bd893a73fad130849ad9549f6b3b9fd))(const struct [device](structdevice.md) \*dev, [usbc\_ppc\_event\_cb\_t](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73) handler, void \*data);

[ 63](structusbc__ppc__drv.md#a8b1880f4935bfc32594e8f900d4cf97d) int (\*[dump\_regs](structusbc__ppc__drv.md#a8b1880f4935bfc32594e8f900d4cf97d))(const struct [device](structdevice.md) \*dev);

64};

65

66/\*

67 \* API functions

68 \*/

69

[ 79](usbc__ppc_8h.md#a5f70af9a0d0336c208ff4f7a90c4b665)static inline int [ppc\_is\_dead\_battery\_mode](usbc__ppc_8h.md#a5f70af9a0d0336c208ff4f7a90c4b665)(const struct [device](structdevice.md) \*dev)

80{

81 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

82

83 if (api->[is\_dead\_battery\_mode](structusbc__ppc__drv.md#a2641a5d2f8082a9fea2897d60992a81d) == NULL) {

84 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

85 }

86

87 return api->[is\_dead\_battery\_mode](structusbc__ppc__drv.md#a2641a5d2f8082a9fea2897d60992a81d)(dev);

88}

89

[ 102](usbc__ppc_8h.md#abcbebdf47ca1c8a9b7c2e803bb833f5a)static inline int [ppc\_exit\_dead\_battery\_mode](usbc__ppc_8h.md#abcbebdf47ca1c8a9b7c2e803bb833f5a)(const struct [device](structdevice.md) \*dev)

103{

104 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

105

106 if (api->[exit\_dead\_battery\_mode](structusbc__ppc__drv.md#ac66444729d18d875432ac4d31610c1cc) == NULL) {

107 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

108 }

109

110 return api->[exit\_dead\_battery\_mode](structusbc__ppc__drv.md#ac66444729d18d875432ac4d31610c1cc)(dev);

111}

112

[ 122](usbc__ppc_8h.md#aab85fda6d4030c83052deb1965d814f3)static inline int [ppc\_is\_vbus\_source](usbc__ppc_8h.md#aab85fda6d4030c83052deb1965d814f3)(const struct [device](structdevice.md) \*dev)

123{

124 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

125

126 if (api->[is\_vbus\_source](structusbc__ppc__drv.md#a3801f17cd627d99790cfbe45a20831e1) == NULL) {

127 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

128 }

129

130 return api->[is\_vbus\_source](structusbc__ppc__drv.md#a3801f17cd627d99790cfbe45a20831e1)(dev);

131}

132

[ 142](usbc__ppc_8h.md#af5e3999f3a016e33adf4797b62009d6d)static inline int [ppc\_is\_vbus\_sink](usbc__ppc_8h.md#af5e3999f3a016e33adf4797b62009d6d)(const struct [device](structdevice.md) \*dev)

143{

144 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

145

146 if (api->[is\_vbus\_sink](structusbc__ppc__drv.md#aa67d808b77e460159f6021e32701ede4) == NULL) {

147 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

148 }

149

150 return api->[is\_vbus\_sink](structusbc__ppc__drv.md#aa67d808b77e460159f6021e32701ede4)(dev);

151}

152

[ 162](usbc__ppc_8h.md#ae157ab53326686361309f20dfe5c4e64)static inline int [ppc\_set\_snk\_ctrl](usbc__ppc_8h.md#ae157ab53326686361309f20dfe5c4e64)(const struct [device](structdevice.md) \*dev, bool enable)

163{

164 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

165

166 if (api->[set\_snk\_ctrl](structusbc__ppc__drv.md#a60f5d5d55a4037d380338830da3b7aef) == NULL) {

167 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

168 }

169

170 return api->[set\_snk\_ctrl](structusbc__ppc__drv.md#a60f5d5d55a4037d380338830da3b7aef)(dev, enable);

171}

172

[ 182](usbc__ppc_8h.md#ad38e1b5b5598c23ded44b343af58b791)static inline int [ppc\_set\_src\_ctrl](usbc__ppc_8h.md#ad38e1b5b5598c23ded44b343af58b791)(const struct [device](structdevice.md) \*dev, bool enable)

183{

184 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

185

186 if (api->[set\_src\_ctrl](structusbc__ppc__drv.md#a18b223b9167e3d1aaa524a4f9aec87d5) == NULL) {

187 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

188 }

189

190 return api->[set\_src\_ctrl](structusbc__ppc__drv.md#a18b223b9167e3d1aaa524a4f9aec87d5)(dev, enable);

191}

192

[ 202](usbc__ppc_8h.md#ae66cb0377ffefabf85bc002a2fd04a47)static inline int [ppc\_set\_vbus\_discharge](usbc__ppc_8h.md#ae66cb0377ffefabf85bc002a2fd04a47)(const struct [device](structdevice.md) \*dev, bool enable)

203{

204 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

205

206 if (api->[set\_vbus\_discharge](structusbc__ppc__drv.md#a5581e4e8c5dd709e85cca3ca3fe9ec09) == NULL) {

207 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

208 }

209

210 return api->[set\_vbus\_discharge](structusbc__ppc__drv.md#a5581e4e8c5dd709e85cca3ca3fe9ec09)(dev, enable);

211}

212

[ 222](usbc__ppc_8h.md#acd1ac1ac4ea60f16c58f57c9df11d536)static inline int [ppc\_is\_vbus\_present](usbc__ppc_8h.md#acd1ac1ac4ea60f16c58f57c9df11d536)(const struct [device](structdevice.md) \*dev)

223{

224 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

225

226 if (api->[is\_vbus\_present](structusbc__ppc__drv.md#acfb87bd73f5ed0114e988c24b43910ec) == NULL) {

227 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

228 }

229

230 return api->[is\_vbus\_present](structusbc__ppc__drv.md#acfb87bd73f5ed0114e988c24b43910ec)(dev);

231}

232

[ 242](usbc__ppc_8h.md#a1d59cc94e8d303f0125fc88e5b447a69)static inline int [ppc\_set\_event\_handler](usbc__ppc_8h.md#a1d59cc94e8d303f0125fc88e5b447a69)(const struct [device](structdevice.md) \*dev,

243 [usbc\_ppc\_event\_cb\_t](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73) handler, void \*data)

244{

245 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

246

247 if (api->[set\_event\_handler](structusbc__ppc__drv.md#a0bd893a73fad130849ad9549f6b3b9fd) == NULL) {

248 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

249 }

250

251 return api->[set\_event\_handler](structusbc__ppc__drv.md#a0bd893a73fad130849ad9549f6b3b9fd)(dev, handler, data);

252}

253

[ 262](usbc__ppc_8h.md#aeee650c29ce524b1e4d8ef66f295c1d7)static inline int [ppc\_dump\_regs](usbc__ppc_8h.md#aeee650c29ce524b1e4d8ef66f295c1d7)(const struct [device](structdevice.md) \*dev)

263{

264 const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*api = (const struct [usbc\_ppc\_drv](structusbc__ppc__drv.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

265

266 if (api->[dump\_regs](structusbc__ppc__drv.md#a8b1880f4935bfc32594e8f900d4cf97d) == NULL) {

267 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

268 }

269

270 return api->[dump\_regs](structusbc__ppc__drv.md#a8b1880f4935bfc32594e8f900d4cf97d)(dev);

271}

272

273#ifdef \_\_cplusplus

274}

275#endif

276

277#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USBC\_USBC\_PPC\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[usbc\_ppc\_drv](structusbc__ppc__drv.md)

Structure with pointers to the functions implemented by driver.

**Definition** usbc\_ppc.h:53

[usbc\_ppc\_drv::set\_event\_handler](structusbc__ppc__drv.md#a0bd893a73fad130849ad9549f6b3b9fd)

int(\* set\_event\_handler)(const struct device \*dev, usbc\_ppc\_event\_cb\_t handler, void \*data)

**Definition** usbc\_ppc.h:62

[usbc\_ppc\_drv::set\_src\_ctrl](structusbc__ppc__drv.md#a18b223b9167e3d1aaa524a4f9aec87d5)

int(\* set\_src\_ctrl)(const struct device \*dev, bool enable)

**Definition** usbc\_ppc.h:59

[usbc\_ppc\_drv::is\_dead\_battery\_mode](structusbc__ppc__drv.md#a2641a5d2f8082a9fea2897d60992a81d)

int(\* is\_dead\_battery\_mode)(const struct device \*dev)

**Definition** usbc\_ppc.h:54

[usbc\_ppc\_drv::is\_vbus\_source](structusbc__ppc__drv.md#a3801f17cd627d99790cfbe45a20831e1)

int(\* is\_vbus\_source)(const struct device \*dev)

**Definition** usbc\_ppc.h:56

[usbc\_ppc\_drv::set\_vbus\_discharge](structusbc__ppc__drv.md#a5581e4e8c5dd709e85cca3ca3fe9ec09)

int(\* set\_vbus\_discharge)(const struct device \*dev, bool enable)

**Definition** usbc\_ppc.h:60

[usbc\_ppc\_drv::set\_snk\_ctrl](structusbc__ppc__drv.md#a60f5d5d55a4037d380338830da3b7aef)

int(\* set\_snk\_ctrl)(const struct device \*dev, bool enable)

**Definition** usbc\_ppc.h:58

[usbc\_ppc\_drv::dump\_regs](structusbc__ppc__drv.md#a8b1880f4935bfc32594e8f900d4cf97d)

int(\* dump\_regs)(const struct device \*dev)

**Definition** usbc\_ppc.h:63

[usbc\_ppc\_drv::is\_vbus\_sink](structusbc__ppc__drv.md#aa67d808b77e460159f6021e32701ede4)

int(\* is\_vbus\_sink)(const struct device \*dev)

**Definition** usbc\_ppc.h:57

[usbc\_ppc\_drv::exit\_dead\_battery\_mode](structusbc__ppc__drv.md#ac66444729d18d875432ac4d31610c1cc)

int(\* exit\_dead\_battery\_mode)(const struct device \*dev)

**Definition** usbc\_ppc.h:55

[usbc\_ppc\_drv::is\_vbus\_present](structusbc__ppc__drv.md#acfb87bd73f5ed0114e988c24b43910ec)

int(\* is\_vbus\_present)(const struct device \*dev)

**Definition** usbc\_ppc.h:61

[ppc\_set\_event\_handler](usbc__ppc_8h.md#a1d59cc94e8d303f0125fc88e5b447a69)

static int ppc\_set\_event\_handler(const struct device \*dev, usbc\_ppc\_event\_cb\_t handler, void \*data)

Set the callback used to notify about PPC events.

**Definition** usbc\_ppc.h:242

[usbc\_ppc\_event](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9)

usbc\_ppc\_event

Type of event being notified by Power Path Controller.

**Definition** usbc\_ppc.h:24

[USBC\_PPC\_EVENT\_SRC\_REVERSE\_CURRENT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a3eca3adb253db52fb444c0163781dde6)

@ USBC\_PPC\_EVENT\_SRC\_REVERSE\_CURRENT

Reverse current detected while being in a source role.

**Definition** usbc\_ppc.h:31

[USBC\_PPC\_EVENT\_SRC\_OVERCURRENT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a4fbd9543f2596349d26d7c1cc6278238)

@ USBC\_PPC\_EVENT\_SRC\_OVERCURRENT

Overcurrent detected while being in a source role.

**Definition** usbc\_ppc.h:33

[USBC\_PPC\_EVENT\_SRC\_OVERVOLTAGE](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a54615a71ead7913f6eb708be78fee109)

@ USBC\_PPC\_EVENT\_SRC\_OVERVOLTAGE

Overvoltage detected while being in a source role.

**Definition** usbc\_ppc.h:29

[USBC\_PPC\_EVENT\_SNK\_REVERSE\_CURRENT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a6d189e6a1c326f6746cb3e4abd0a7759)

@ USBC\_PPC\_EVENT\_SNK\_REVERSE\_CURRENT

Reverse current detected while being in a sink role.

**Definition** usbc\_ppc.h:43

[USBC\_PPC\_EVENT\_SNK\_OVERVOLTAGE](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a7e6392785fe1d6f5c3cef3b179952b0e)

@ USBC\_PPC\_EVENT\_SNK\_OVERVOLTAGE

Overvoltage detected while being in a sink role.

**Definition** usbc\_ppc.h:47

[USBC\_PPC\_EVENT\_DEAD\_BATTERY\_ERROR](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9a8e6635e7e347418f328ce5ebcb303d5e)

@ USBC\_PPC\_EVENT\_DEAD\_BATTERY\_ERROR

Exit from dead-battery mode failed.

**Definition** usbc\_ppc.h:26

[USBC\_PPC\_EVENT\_SNK\_SHORT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9aa4434d091f55ad29e7fb46b681fc376d)

@ USBC\_PPC\_EVENT\_SNK\_SHORT

VBUS short detected while being in a sink role.

**Definition** usbc\_ppc.h:45

[USBC\_PPC\_EVENT\_BOTH\_SNKSRC\_ENABLED](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9aaa39462464dfaf5a0f57fa6407114b94)

@ USBC\_PPC\_EVENT\_BOTH\_SNKSRC\_ENABLED

Sink and source paths enabled simultaneously.

**Definition** usbc\_ppc.h:40

[USBC\_PPC\_EVENT\_OVER\_TEMPERATURE](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9ac241608a878e709571144ad5f207140c)

@ USBC\_PPC\_EVENT\_OVER\_TEMPERATURE

Chip over temperature detected.

**Definition** usbc\_ppc.h:38

[USBC\_PPC\_EVENT\_SRC\_SHORT](usbc__ppc_8h.md#a3dbbb1a6701a3a79c9a1d148b239fcf9addcec15b50f34307780822cb1fc329c4)

@ USBC\_PPC\_EVENT\_SRC\_SHORT

VBUS short detected while being in a source role.

**Definition** usbc\_ppc.h:35

[ppc\_is\_dead\_battery\_mode](usbc__ppc_8h.md#a5f70af9a0d0336c208ff4f7a90c4b665)

static int ppc\_is\_dead\_battery\_mode(const struct device \*dev)

Check if PPC is in the dead battery mode.

**Definition** usbc\_ppc.h:79

[usbc\_ppc\_event\_cb\_t](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73)

void(\* usbc\_ppc\_event\_cb\_t)(const struct device \*dev, void \*data, enum usbc\_ppc\_event ev)

**Definition** usbc\_ppc.h:50

[ppc\_is\_vbus\_source](usbc__ppc_8h.md#aab85fda6d4030c83052deb1965d814f3)

static int ppc\_is\_vbus\_source(const struct device \*dev)

Check if the PPC is sourcing the VBUS.

**Definition** usbc\_ppc.h:122

[ppc\_exit\_dead\_battery\_mode](usbc__ppc_8h.md#abcbebdf47ca1c8a9b7c2e803bb833f5a)

static int ppc\_exit\_dead\_battery\_mode(const struct device \*dev)

Request the PPC to exit from the dead battery mode Return from this call doesn't mean that the PPC is...

**Definition** usbc\_ppc.h:102

[ppc\_is\_vbus\_present](usbc__ppc_8h.md#acd1ac1ac4ea60f16c58f57c9df11d536)

static int ppc\_is\_vbus\_present(const struct device \*dev)

Check if VBUS is present.

**Definition** usbc\_ppc.h:222

[ppc\_set\_src\_ctrl](usbc__ppc_8h.md#ad38e1b5b5598c23ded44b343af58b791)

static int ppc\_set\_src\_ctrl(const struct device \*dev, bool enable)

Set the state of VBUS sourcing.

**Definition** usbc\_ppc.h:182

[ppc\_set\_snk\_ctrl](usbc__ppc_8h.md#ae157ab53326686361309f20dfe5c4e64)

static int ppc\_set\_snk\_ctrl(const struct device \*dev, bool enable)

Set the state of VBUS sinking.

**Definition** usbc\_ppc.h:162

[ppc\_set\_vbus\_discharge](usbc__ppc_8h.md#ae66cb0377ffefabf85bc002a2fd04a47)

static int ppc\_set\_vbus\_discharge(const struct device \*dev, bool enable)

Set the state of VBUS discharging.

**Definition** usbc\_ppc.h:202

[ppc\_dump\_regs](usbc__ppc_8h.md#aeee650c29ce524b1e4d8ef66f295c1d7)

static int ppc\_dump\_regs(const struct device \*dev)

Print the values or PPC registers.

**Definition** usbc\_ppc.h:262

[ppc\_is\_vbus\_sink](usbc__ppc_8h.md#af5e3999f3a016e33adf4797b62009d6d)

static int ppc\_is\_vbus\_sink(const struct device \*dev)

Check if the PPC is sinking the VBUS.

**Definition** usbc\_ppc.h:142

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_ppc.h](usbc__ppc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
