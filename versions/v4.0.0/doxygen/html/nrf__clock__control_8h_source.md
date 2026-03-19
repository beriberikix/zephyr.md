---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nrf__clock__control_8h_source.html
original_path: doxygen/html/nrf__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_clock\_control.h

[Go to the documentation of this file.](nrf__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2016 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NRF\_CLOCK\_CONTROL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NRF\_CLOCK\_CONTROL\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#ifdef NRF\_CLOCK

12#include <hal/nrf\_clock.h>

13#endif

14#include <[zephyr/sys/onoff.h](onoff_8h.md)>

15#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21#if defined(CONFIG\_CLOCK\_CONTROL\_NRF)

22

27enum clock\_control\_nrf\_type {

28 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK,

29 CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK,

30#if NRF\_CLOCK\_HAS\_HFCLK192M

31 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK192M,

32#endif

33#if NRF\_CLOCK\_HAS\_HFCLKAUDIO

34 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLKAUDIO,

35#endif

36 CLOCK\_CONTROL\_NRF\_TYPE\_COUNT

37};

38

39/\* Define can be used with clock control API instead of enum directly to

40 \* increase code readability.

41 \*/

42#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF \

43 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK)

44#define CLOCK\_CONTROL\_NRF\_SUBSYS\_LF \

45 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK)

46#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF192M \

47 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK192M)

48#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HFAUDIO \

49 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLKAUDIO)

50

52enum nrf\_lfclk\_start\_mode {

53 CLOCK\_CONTROL\_NRF\_LF\_START\_NOWAIT,

54 CLOCK\_CONTROL\_NRF\_LF\_START\_AVAILABLE,

55 CLOCK\_CONTROL\_NRF\_LF\_START\_STABLE,

56};

57

58/\* Define 32KHz clock source \*/

59#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_RC

60#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_RC

61#endif

62#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_XTAL

63#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL

64#endif

65#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_SYNTH

66#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_SYNTH

67#endif

68#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_EXT\_LOW\_SWING

69#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL\_LOW\_SWING

70#endif

71#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_EXT\_FULL\_SWING

72#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL\_FULL\_SWING

73#endif

74

75/\* Define 32KHz clock accuracy \*/

76#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_500PPM

77#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 0

78#endif

79#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_250PPM

80#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 1

81#endif

82#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_150PPM

83#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 2

84#endif

85#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_100PPM

86#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 3

87#endif

88#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_75PPM

89#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 4

90#endif

91#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_50PPM

92#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 5

93#endif

94#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_30PPM

95#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 6

96#endif

97#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_20PPM

98#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 7

99#endif

100

102void z\_nrf\_clock\_calibration\_force\_start(void);

103

110int z\_nrf\_clock\_calibration\_count(void);

111

118int z\_nrf\_clock\_calibration\_skips\_count(void);

119

126struct [onoff\_manager](structonoff__manager.md) \*z\_nrf\_clock\_control\_get\_onoff([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys);

127

136void z\_nrf\_clock\_control\_lf\_on(enum nrf\_lfclk\_start\_mode start\_mode);

137

150void z\_nrf\_clock\_bt\_ctlr\_hf\_request(void);

151

156void z\_nrf\_clock\_bt\_ctlr\_hf\_release(void);

157

158#endif /\* defined(CONFIG\_CLOCK\_CONTROL\_NRF) \*/

159

160

161#if defined(CONFIG\_CLOCK\_CONTROL\_NRF2)

162

163/\* Specifies to use the maximum available frequency for a given clock. \*/

164#define NRF\_CLOCK\_CONTROL\_FREQUENCY\_MAX UINT32\_MAX

165

166/\* Specifies to use the maximum available accuracy for a given clock. \*/

167#define NRF\_CLOCK\_CONTROL\_ACCURACY\_MAX 1

168/\* Specifies the required clock accuracy in parts-per-million. \*/

169#define NRF\_CLOCK\_CONTROL\_ACCURACY\_PPM(ppm) (ppm)

170

171/\* Specifies that high precision of the clock is required. \*/

172#define NRF\_CLOCK\_CONTROL\_PRECISION\_HIGH 1

173/\* Specifies that default precision of the clock is sufficient. \*/

174#define NRF\_CLOCK\_CONTROL\_PRECISION\_DEFAULT 0

175

176struct nrf\_clock\_spec {

177 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency;

178 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) accuracy : 15;

179 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) precision : 1;

180};

181

182\_\_subsystem struct nrf\_clock\_control\_driver\_api {

183 struct clock\_control\_driver\_api std\_api;

184

185 int (\*request)(const struct device \*dev,

186 const struct nrf\_clock\_spec \*spec,

187 struct onoff\_client \*cli);

188 int (\*release)(const struct device \*dev,

189 const struct nrf\_clock\_spec \*spec);

190 int (\*cancel\_or\_release)(const struct device \*dev,

191 const struct nrf\_clock\_spec \*spec,

192 struct onoff\_client \*cli);

193};

194

227static inline

228int nrf\_clock\_control\_request(const struct [device](structdevice.md) \*dev,

229 const struct nrf\_clock\_spec \*spec,

230 struct [onoff\_client](structonoff__client.md) \*cli)

231{

232 const struct nrf\_clock\_control\_driver\_api \*api =

233 (const struct nrf\_clock\_control\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

234

235 return api->request(dev, spec, cli);

236}

237

252static inline

253int nrf\_clock\_control\_release(const struct [device](structdevice.md) \*dev,

254 const struct nrf\_clock\_spec \*spec)

255{

256 const struct nrf\_clock\_control\_driver\_api \*api =

257 (const struct nrf\_clock\_control\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

258

259 return api->release(dev, spec);

260}

261

284static inline

285int nrf\_clock\_control\_cancel\_or\_release(const struct [device](structdevice.md) \*dev,

286 const struct nrf\_clock\_spec \*spec,

287 struct [onoff\_client](structonoff__client.md) \*cli)

288{

289 const struct nrf\_clock\_control\_driver\_api \*api =

290 (const struct nrf\_clock\_control\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

291

292 return api->cancel\_or\_release(dev, spec, cli);

293}

294

295#endif /\* defined(CONFIG\_CLOCK\_CONTROL\_NRF2) \*/

296

297#ifdef \_\_cplusplus

298}

299#endif

300

301#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NRF\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[device.h](device_8h.md)

[clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db)

void \* clock\_control\_subsys\_t

clock\_control\_subsys\_t is a type to identify a clock controller sub-system.

**Definition** clock\_control.h:58

[onoff.h](onoff_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[onoff\_client](structonoff__client.md)

State associated with a client of an on-off service.

**Definition** onoff.h:274

[onoff\_manager](structonoff__manager.md)

State associated with an on-off manager.

**Definition** onoff.h:154

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [nrf\_clock\_control.h](nrf__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
