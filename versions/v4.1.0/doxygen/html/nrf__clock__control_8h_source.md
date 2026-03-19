---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nrf__clock__control_8h_source.html
original_path: doxygen/html/nrf__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

11#if defined(NRF\_CLOCK) && !defined(NRF\_LFRC)

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

120

125bool z\_nrf\_clock\_calibration\_is\_in\_progress(void);

126

133struct [onoff\_manager](structonoff__manager.md) \*z\_nrf\_clock\_control\_get\_onoff([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys);

134

143void z\_nrf\_clock\_control\_lf\_on(enum nrf\_lfclk\_start\_mode start\_mode);

144

157void z\_nrf\_clock\_bt\_ctlr\_hf\_request(void);

158

163void z\_nrf\_clock\_bt\_ctlr\_hf\_release(void);

164

165#endif /\* defined(CONFIG\_CLOCK\_CONTROL\_NRF) \*/

166

167

168#if defined(CONFIG\_CLOCK\_CONTROL\_NRF2)

169

170/\* Specifies to use the maximum available frequency for a given clock. \*/

171#define NRF\_CLOCK\_CONTROL\_FREQUENCY\_MAX UINT32\_MAX

172

173/\* Specifies to use the maximum available accuracy for a given clock. \*/

174#define NRF\_CLOCK\_CONTROL\_ACCURACY\_MAX 1

175/\* Specifies the required clock accuracy in parts-per-million. \*/

176#define NRF\_CLOCK\_CONTROL\_ACCURACY\_PPM(ppm) (ppm)

177

178/\* Specifies that high precision of the clock is required. \*/

179#define NRF\_CLOCK\_CONTROL\_PRECISION\_HIGH 1

180/\* Specifies that default precision of the clock is sufficient. \*/

181#define NRF\_CLOCK\_CONTROL\_PRECISION\_DEFAULT 0

182

183struct nrf\_clock\_spec {

184 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency;

185 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) accuracy : 15;

186 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) precision : 1;

187};

188

189\_\_subsystem struct nrf\_clock\_control\_driver\_api {

190 struct clock\_control\_driver\_api std\_api;

191

192 int (\*request)(const struct device \*dev,

193 const struct nrf\_clock\_spec \*spec,

194 struct onoff\_client \*cli);

195 int (\*release)(const struct device \*dev,

196 const struct nrf\_clock\_spec \*spec);

197 int (\*cancel\_or\_release)(const struct device \*dev,

198 const struct nrf\_clock\_spec \*spec,

199 struct onoff\_client \*cli);

200};

201

234static inline

235int nrf\_clock\_control\_request(const struct [device](structdevice.md) \*dev,

236 const struct nrf\_clock\_spec \*spec,

237 struct [onoff\_client](structonoff__client.md) \*cli)

238{

239 const struct nrf\_clock\_control\_driver\_api \*api =

240 (const struct nrf\_clock\_control\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

241

242 return api->request(dev, spec, cli);

243}

244

259int nrf\_clock\_control\_request\_sync(const struct [device](structdevice.md) \*dev,

260 const struct nrf\_clock\_spec \*spec,

261 [k\_timeout\_t](structk__timeout__t.md) timeout);

262

277static inline

278int nrf\_clock\_control\_release(const struct [device](structdevice.md) \*dev,

279 const struct nrf\_clock\_spec \*spec)

280{

281 const struct nrf\_clock\_control\_driver\_api \*api =

282 (const struct nrf\_clock\_control\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

283

284 return api->release(dev, spec);

285}

286

309static inline

310int nrf\_clock\_control\_cancel\_or\_release(const struct [device](structdevice.md) \*dev,

311 const struct nrf\_clock\_spec \*spec,

312 struct [onoff\_client](structonoff__client.md) \*cli)

313{

314 const struct nrf\_clock\_control\_driver\_api \*api =

315 (const struct nrf\_clock\_control\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

316

317 return api->cancel\_or\_release(dev, spec, cli);

318}

319

331void nrf\_clock\_control\_hfxo\_request(void);

332

342void nrf\_clock\_control\_hfxo\_release(void);

343

344#endif /\* defined(CONFIG\_CLOCK\_CONTROL\_NRF2) \*/

345

[ 358](nrf__clock__control_8h.md#aab71ee0624ed3d35e089d4c095a3bcfc)#define NRF\_PERIPH\_GET\_FREQUENCY(node) \

359 COND\_CODE\_1(DT\_CLOCKS\_HAS\_IDX(node, 0), \

360 (COND\_CODE\_1(DT\_NODE\_HAS\_PROP(DT\_CLOCKS\_CTLR(node), clock\_frequency), \

361 (DT\_PROP(DT\_CLOCKS\_CTLR(node), clock\_frequency)), \

362 (DT\_PROP\_LAST(DT\_CLOCKS\_CTLR(node), supported\_clock\_frequency)))), \

363 (NRFX\_MHZ\_TO\_HZ(16)))

364

365#ifdef \_\_cplusplus

366}

367#endif

368

369#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NRF\_CLOCK\_CONTROL\_H\_ \*/

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

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

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
