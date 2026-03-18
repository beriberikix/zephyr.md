---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dmic_8h_source.html
original_path: doxygen/html/dmic_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dmic.h

[Go to the documentation of this file.](dmic_8h.md)

1/\*

2 \* Copyright (c) 2018, Intel Corporation

3 \*

4 \* Author: Seppo Ingalsuo <seppo.ingalsuo@linux.intel.com>

5 \* Sathish Kuttan <sathish.k.kuttan@intel.com>

6 \*

7 \* SPDX-License-Identifier: Apache-2.0

8 \*/

9

16

17#ifndef ZEPHYR\_INCLUDE\_AUDIO\_DMIC\_H\_

18#define ZEPHYR\_INCLUDE\_AUDIO\_DMIC\_H\_

19

20

26

34

35#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

36#include <[zephyr/device.h](device_8h.md)>

37

38#ifdef \_\_cplusplus

39extern "C" {

40#endif

41

[ 45](group__audio__dmic__interface.md#gac99a4f579b6aa45bb6cce1f797247a23)enum [dmic\_state](group__audio__dmic__interface.md#gac99a4f579b6aa45bb6cce1f797247a23) {

[ 46](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be) [DMIC\_STATE\_UNINIT](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be),

[ 47](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1) [DMIC\_STATE\_INITIALIZED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1),

[ 48](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826) [DMIC\_STATE\_CONFIGURED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826),

[ 49](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4) [DMIC\_STATE\_ACTIVE](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4),

[ 50](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81) [DMIC\_STATE\_PAUSED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81),

[ 51](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba) [DMIC\_STATE\_ERROR](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba),

52};

53

[ 57](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14)enum [dmic\_trigger](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14) {

[ 58](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23) [DMIC\_TRIGGER\_STOP](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23),

[ 59](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa) [DMIC\_TRIGGER\_START](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa),

[ 60](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5) [DMIC\_TRIGGER\_PAUSE](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5),

[ 61](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804) [DMIC\_TRIGGER\_RELEASE](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804),

[ 62](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79) [DMIC\_TRIGGER\_RESET](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79),

63};

64

[ 68](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991)enum [pdm\_lr](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991) {

[ 69](group__audio__dmic__interface.md#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345) [PDM\_CHAN\_LEFT](group__audio__dmic__interface.md#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345),

[ 70](group__audio__dmic__interface.md#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0) [PDM\_CHAN\_RIGHT](group__audio__dmic__interface.md#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0),

71};

72

[ 76](structpdm__io__cfg.md)struct [pdm\_io\_cfg](structpdm__io__cfg.md) {

[ 82](structpdm__io__cfg.md#ae308635d30eaee617cb62c03c0255f37) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [min\_pdm\_clk\_freq](structpdm__io__cfg.md#ae308635d30eaee617cb62c03c0255f37);

[ 84](structpdm__io__cfg.md#a4f07b2239435b0ac21e1049413d1a03a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_pdm\_clk\_freq](structpdm__io__cfg.md#a4f07b2239435b0ac21e1049413d1a03a);

[ 86](structpdm__io__cfg.md#a14d6d390746f7731c4ff203a4beec5fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_pdm\_clk\_dc](structpdm__io__cfg.md#a14d6d390746f7731c4ff203a4beec5fe);

[ 88](structpdm__io__cfg.md#aa03fbcc1f17fb2597bfa8c1898b74455) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_pdm\_clk\_dc](structpdm__io__cfg.md#aa03fbcc1f17fb2597bfa8c1898b74455);

92

[ 98](structpdm__io__cfg.md#a4a12d293f2c8edae3e7e5b71646ee55e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pdm\_clk\_pol](structpdm__io__cfg.md#a4a12d293f2c8edae3e7e5b71646ee55e);

[ 100](structpdm__io__cfg.md#aa242b3383b20e0673ed47eea8450e9a7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pdm\_data\_pol](structpdm__io__cfg.md#aa242b3383b20e0673ed47eea8450e9a7);

[ 102](structpdm__io__cfg.md#a692d7e838db86ca84558eb3e3170551a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pdm\_clk\_skew](structpdm__io__cfg.md#a692d7e838db86ca84558eb3e3170551a);

106};

107

[ 114](structpcm__stream__cfg.md)struct [pcm\_stream\_cfg](structpcm__stream__cfg.md) {

[ 116](structpcm__stream__cfg.md#ae6e3790576f910943b0383f4731a5545) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcm\_rate](structpcm__stream__cfg.md#ae6e3790576f910943b0383f4731a5545);

[ 118](structpcm__stream__cfg.md#a7d9fd0039bc25de292f35f60c99c6615) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pcm\_width](structpcm__stream__cfg.md#a7d9fd0039bc25de292f35f60c99c6615);

[ 120](structpcm__stream__cfg.md#a3c224ba6f6c6fa7a128a739b6f1c36bf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [block\_size](structpcm__stream__cfg.md#a3c224ba6f6c6fa7a128a739b6f1c36bf);

[ 122](structpcm__stream__cfg.md#ade324dcfe8604fcb94400544ddb4517e) struct k\_mem\_slab \*[mem\_slab](structpcm__stream__cfg.md#ade324dcfe8604fcb94400544ddb4517e);

123};

124

[ 146](structpdm__chan__cfg.md)struct [pdm\_chan\_cfg](structpdm__chan__cfg.md) {

[ 151](structpdm__chan__cfg.md#a028c8cd3dfcf0bfce618ef8937a7b211) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [req\_chan\_map\_lo](structpdm__chan__cfg.md#a028c8cd3dfcf0bfce618ef8937a7b211);

[ 152](structpdm__chan__cfg.md#a11a258f6b21126e1d50c5a3f46b2cad7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [req\_chan\_map\_hi](structpdm__chan__cfg.md#a11a258f6b21126e1d50c5a3f46b2cad7);

154

[ 159](structpdm__chan__cfg.md#a34d2e2d03df48e26245835d4df88b60b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [act\_chan\_map\_lo](structpdm__chan__cfg.md#a34d2e2d03df48e26245835d4df88b60b);

[ 160](structpdm__chan__cfg.md#a9a91e9341f4c033243effbebd5ffa194) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [act\_chan\_map\_hi](structpdm__chan__cfg.md#a9a91e9341f4c033243effbebd5ffa194);

162

[ 164](structpdm__chan__cfg.md#aa2518c6f577c3fd92ec009fa134a6185) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [req\_num\_chan](structpdm__chan__cfg.md#aa2518c6f577c3fd92ec009fa134a6185);

[ 166](structpdm__chan__cfg.md#a3268169aaee14827cb15778fbc44ceb1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [act\_num\_chan](structpdm__chan__cfg.md#a3268169aaee14827cb15778fbc44ceb1);

[ 168](structpdm__chan__cfg.md#ae1398759382606cc60cf8944a1b9e5f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [req\_num\_streams](structpdm__chan__cfg.md#ae1398759382606cc60cf8944a1b9e5f6);

[ 170](structpdm__chan__cfg.md#a7614fefd7976ba7b195afb4e81f7100e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [act\_num\_streams](structpdm__chan__cfg.md#a7614fefd7976ba7b195afb4e81f7100e);

171};

172

[ 176](structdmic__cfg.md)struct [dmic\_cfg](structdmic__cfg.md) {

[ 177](structdmic__cfg.md#abac7595e0a03cf976d8359a86259f54b) struct [pdm\_io\_cfg](structpdm__io__cfg.md) [io](structdmic__cfg.md#abac7595e0a03cf976d8359a86259f54b);

[ 182](structdmic__cfg.md#a90f08070236a8e2c07c30edc54c687a5) struct [pcm\_stream\_cfg](structpcm__stream__cfg.md) \*[streams](structdmic__cfg.md#a90f08070236a8e2c07c30edc54c687a5);

[ 183](structdmic__cfg.md#aaef2d2b475ce65d18c48d60cd1d393c4) struct [pdm\_chan\_cfg](structpdm__chan__cfg.md) [channel](structdmic__cfg.md#aaef2d2b475ce65d18c48d60cd1d393c4);

184};

185

189struct \_dmic\_ops {

190 int (\*configure)(const struct [device](structdevice.md) \*dev, struct [dmic\_cfg](structdmic__cfg.md) \*config);

191 int (\*trigger)(const struct [device](structdevice.md) \*dev, enum [dmic\_trigger](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

192 int (\*read)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stream, void \*\*buffer,

193 size\_t \*size, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

194};

195

[ 208](group__audio__dmic__interface.md#ga5d1fcefaf085962d779b8082b3480cbd)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dmic\_build\_channel\_map](group__audio__dmic__interface.md#ga5d1fcefaf085962d779b8082b3480cbd)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm,

209 enum [pdm\_lr](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991) lr)

210{

211 return ((((pdm & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(3)) << 1) | lr) <<

212 ((channel & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(3)) \* 4U));

213}

214

[ 227](group__audio__dmic__interface.md#gaa1fded235751a71632965011a62ddead)static inline void [dmic\_parse\_channel\_map](group__audio__dmic__interface.md#gaa1fded235751a71632965011a62ddead)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_map\_lo,

228 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_map\_hi, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*pdm, enum [pdm\_lr](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991) \*lr)

229{

230 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_map;

231

232 channel\_map = (channel < 8) ? channel\_map\_lo : channel\_map\_hi;

233 channel\_map >>= ((channel & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(3)) \* 4U);

234

235 \*pdm = (channel\_map >> 1) & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(3);

236 \*lr = (enum [pdm\_lr](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991)) (channel\_map & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0));

237}

238

[ 250](group__audio__dmic__interface.md#gaf5abf489fe6ed18c2daea5d918aa2f80)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dmic\_build\_clk\_skew\_map](group__audio__dmic__interface.md#gaf5abf489fe6ed18c2daea5d918aa2f80)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) skew)

251{

252 return ((skew & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(4)) << ((pdm & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(3)) \* 4U));

253}

254

[ 266](group__audio__dmic__interface.md#ga09fc7074323c2f3115b06c5212d21fc7)static inline int [dmic\_configure](group__audio__dmic__interface.md#ga09fc7074323c2f3115b06c5212d21fc7)(const struct [device](structdevice.md) \*dev,

267 struct [dmic\_cfg](structdmic__cfg.md) \*cfg)

268{

269 const struct \_dmic\_ops \*api =

270 (const struct \_dmic\_ops \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

271

272 return api->configure(dev, cfg);

273}

274

[ 285](group__audio__dmic__interface.md#ga051e82f30b76f0fca789ba0147054184)static inline int [dmic\_trigger](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14)(const struct [device](structdevice.md) \*dev,

286 enum [dmic\_trigger](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615))

287{

288 const struct \_dmic\_ops \*api =

289 (const struct \_dmic\_ops \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

290

291 return api->trigger(dev, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

292}

293

[ 309](group__audio__dmic__interface.md#ga74b51bddaa175c518d45211f936d08e6)static inline int [dmic\_read](group__audio__dmic__interface.md#ga74b51bddaa175c518d45211f936d08e6)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stream,

310 void \*\*buffer,

311 size\_t \*size, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

312{

313 const struct \_dmic\_ops \*api =

314 (const struct \_dmic\_ops \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

315

316 return api->read(dev, stream, buffer, size, timeout);

317}

318

319#ifdef \_\_cplusplus

320}

321#endif

322

326

327#endif /\* ZEPHYR\_INCLUDE\_AUDIO\_DMIC\_H\_ \*/

[device.h](device_8h.md)

[BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

**Definition** adc.h:14

[dmic\_configure](group__audio__dmic__interface.md#ga09fc7074323c2f3115b06c5212d21fc7)

static int dmic\_configure(const struct device \*dev, struct dmic\_cfg \*cfg)

Configure the DMIC driver and controller(s).

**Definition** dmic.h:266

[dmic\_trigger](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14)

dmic\_trigger

DMIC driver trigger commands.

**Definition** dmic.h:57

[dmic\_build\_channel\_map](group__audio__dmic__interface.md#ga5d1fcefaf085962d779b8082b3480cbd)

static uint32\_t dmic\_build\_channel\_map(uint8\_t channel, uint8\_t pdm, enum pdm\_lr lr)

Build the channel map to populate struct pdm\_chan\_cfg.

**Definition** dmic.h:208

[dmic\_read](group__audio__dmic__interface.md#ga74b51bddaa175c518d45211f936d08e6)

static int dmic\_read(const struct device \*dev, uint8\_t stream, void \*\*buffer, size\_t \*size, int32\_t timeout)

Read received decimated PCM data stream.

**Definition** dmic.h:309

[pdm\_lr](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991)

pdm\_lr

PDM Channels LEFT / RIGHT.

**Definition** dmic.h:68

[dmic\_parse\_channel\_map](group__audio__dmic__interface.md#gaa1fded235751a71632965011a62ddead)

static void dmic\_parse\_channel\_map(uint32\_t channel\_map\_lo, uint32\_t channel\_map\_hi, uint8\_t channel, uint8\_t \*pdm, enum pdm\_lr \*lr)

Helper function to parse the channel map in pdm\_chan\_cfg.

**Definition** dmic.h:227

[dmic\_state](group__audio__dmic__interface.md#gac99a4f579b6aa45bb6cce1f797247a23)

dmic\_state

DMIC driver states.

**Definition** dmic.h:45

[dmic\_build\_clk\_skew\_map](group__audio__dmic__interface.md#gaf5abf489fe6ed18c2daea5d918aa2f80)

static uint32\_t dmic\_build\_clk\_skew\_map(uint8\_t pdm, uint8\_t skew)

Build a bit map of clock skew values for each PDM channel.

**Definition** dmic.h:250

[DMIC\_TRIGGER\_START](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa)

@ DMIC\_TRIGGER\_START

Start stream.

**Definition** dmic.h:59

[DMIC\_TRIGGER\_PAUSE](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5)

@ DMIC\_TRIGGER\_PAUSE

Pause stream.

**Definition** dmic.h:60

[DMIC\_TRIGGER\_RELEASE](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804)

@ DMIC\_TRIGGER\_RELEASE

Release paused stream.

**Definition** dmic.h:61

[DMIC\_TRIGGER\_RESET](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79)

@ DMIC\_TRIGGER\_RESET

Reset stream.

**Definition** dmic.h:62

[DMIC\_TRIGGER\_STOP](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23)

@ DMIC\_TRIGGER\_STOP

Stop stream.

**Definition** dmic.h:58

[PDM\_CHAN\_RIGHT](group__audio__dmic__interface.md#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0)

@ PDM\_CHAN\_RIGHT

Right channel.

**Definition** dmic.h:70

[PDM\_CHAN\_LEFT](group__audio__dmic__interface.md#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345)

@ PDM\_CHAN\_LEFT

Left channel.

**Definition** dmic.h:69

[DMIC\_STATE\_PAUSED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81)

@ DMIC\_STATE\_PAUSED

Paused.

**Definition** dmic.h:50

[DMIC\_STATE\_UNINIT](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be)

@ DMIC\_STATE\_UNINIT

Uninitialized.

**Definition** dmic.h:46

[DMIC\_STATE\_CONFIGURED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826)

@ DMIC\_STATE\_CONFIGURED

Configured.

**Definition** dmic.h:48

[DMIC\_STATE\_INITIALIZED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1)

@ DMIC\_STATE\_INITIALIZED

Initialized.

**Definition** dmic.h:47

[DMIC\_STATE\_ERROR](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba)

@ DMIC\_STATE\_ERROR

Error.

**Definition** dmic.h:51

[DMIC\_STATE\_ACTIVE](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4)

@ DMIC\_STATE\_ACTIVE

Active.

**Definition** dmic.h:49

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[dmic\_cfg](structdmic__cfg.md)

Input configuration structure for the DMIC configuration API.

**Definition** dmic.h:176

[dmic\_cfg::streams](structdmic__cfg.md#a90f08070236a8e2c07c30edc54c687a5)

struct pcm\_stream\_cfg \* streams

Array of pcm\_stream\_cfg for application to provide configuration for each stream.

**Definition** dmic.h:182

[dmic\_cfg::channel](structdmic__cfg.md#aaef2d2b475ce65d18c48d60cd1d393c4)

struct pdm\_chan\_cfg channel

**Definition** dmic.h:183

[dmic\_cfg::io](structdmic__cfg.md#abac7595e0a03cf976d8359a86259f54b)

struct pdm\_io\_cfg io

**Definition** dmic.h:177

[pcm\_stream\_cfg](structpcm__stream__cfg.md)

Configuration of the PCM streams to be output by the PDM hardware.

**Definition** dmic.h:114

[pcm\_stream\_cfg::block\_size](structpcm__stream__cfg.md#a3c224ba6f6c6fa7a128a739b6f1c36bf)

uint16\_t block\_size

PCM sample block size per transfer.

**Definition** dmic.h:120

[pcm\_stream\_cfg::pcm\_width](structpcm__stream__cfg.md#a7d9fd0039bc25de292f35f60c99c6615)

uint8\_t pcm\_width

PCM sample width of stream.

**Definition** dmic.h:118

[pcm\_stream\_cfg::mem\_slab](structpcm__stream__cfg.md#ade324dcfe8604fcb94400544ddb4517e)

struct k\_mem\_slab \* mem\_slab

SLAB for DMIC driver to allocate buffers for stream.

**Definition** dmic.h:122

[pcm\_stream\_cfg::pcm\_rate](structpcm__stream__cfg.md#ae6e3790576f910943b0383f4731a5545)

uint32\_t pcm\_rate

PCM sample rate of stream.

**Definition** dmic.h:116

[pdm\_chan\_cfg](structpdm__chan__cfg.md)

Mapping/ordering of the PDM channels to logical PCM output channel.

**Definition** dmic.h:146

[pdm\_chan\_cfg::req\_chan\_map\_lo](structpdm__chan__cfg.md#a028c8cd3dfcf0bfce618ef8937a7b211)

uint32\_t req\_chan\_map\_lo

Channels 0 to 7.

**Definition** dmic.h:151

[pdm\_chan\_cfg::req\_chan\_map\_hi](structpdm__chan__cfg.md#a11a258f6b21126e1d50c5a3f46b2cad7)

uint32\_t req\_chan\_map\_hi

Channels 8 to 15.

**Definition** dmic.h:152

[pdm\_chan\_cfg::act\_num\_chan](structpdm__chan__cfg.md#a3268169aaee14827cb15778fbc44ceb1)

uint8\_t act\_num\_chan

Actual number of channels that the driver could configure.

**Definition** dmic.h:166

[pdm\_chan\_cfg::act\_chan\_map\_lo](structpdm__chan__cfg.md#a34d2e2d03df48e26245835d4df88b60b)

uint32\_t act\_chan\_map\_lo

Channels 0 to 7.

**Definition** dmic.h:159

[pdm\_chan\_cfg::act\_num\_streams](structpdm__chan__cfg.md#a7614fefd7976ba7b195afb4e81f7100e)

uint8\_t act\_num\_streams

Actual number of streams that the driver could configure.

**Definition** dmic.h:170

[pdm\_chan\_cfg::act\_chan\_map\_hi](structpdm__chan__cfg.md#a9a91e9341f4c033243effbebd5ffa194)

uint32\_t act\_chan\_map\_hi

Channels 8 to 15.

**Definition** dmic.h:160

[pdm\_chan\_cfg::req\_num\_chan](structpdm__chan__cfg.md#aa2518c6f577c3fd92ec009fa134a6185)

uint8\_t req\_num\_chan

Requested number of channels.

**Definition** dmic.h:164

[pdm\_chan\_cfg::req\_num\_streams](structpdm__chan__cfg.md#ae1398759382606cc60cf8944a1b9e5f6)

uint8\_t req\_num\_streams

Requested number of streams for each channel.

**Definition** dmic.h:168

[pdm\_io\_cfg](structpdm__io__cfg.md)

PDM Input/Output signal configuration.

**Definition** dmic.h:76

[pdm\_io\_cfg::min\_pdm\_clk\_dc](structpdm__io__cfg.md#a14d6d390746f7731c4ff203a4beec5fe)

uint8\_t min\_pdm\_clk\_dc

Minimum duty cycle in % supported by the mic.

**Definition** dmic.h:86

[pdm\_io\_cfg::pdm\_clk\_pol](structpdm__io__cfg.md#a4a12d293f2c8edae3e7e5b71646ee55e)

uint8\_t pdm\_clk\_pol

Bit mask to optionally invert PDM clock.

**Definition** dmic.h:98

[pdm\_io\_cfg::max\_pdm\_clk\_freq](structpdm__io__cfg.md#a4f07b2239435b0ac21e1049413d1a03a)

uint32\_t max\_pdm\_clk\_freq

Maximum clock frequency supported by the mic.

**Definition** dmic.h:84

[pdm\_io\_cfg::pdm\_clk\_skew](structpdm__io__cfg.md#a692d7e838db86ca84558eb3e3170551a)

uint32\_t pdm\_clk\_skew

Collection of clock skew values for each PDM port.

**Definition** dmic.h:102

[pdm\_io\_cfg::max\_pdm\_clk\_dc](structpdm__io__cfg.md#aa03fbcc1f17fb2597bfa8c1898b74455)

uint8\_t max\_pdm\_clk\_dc

Maximum duty cycle in % supported by the mic.

**Definition** dmic.h:88

[pdm\_io\_cfg::pdm\_data\_pol](structpdm__io__cfg.md#aa242b3383b20e0673ed47eea8450e9a7)

uint8\_t pdm\_data\_pol

Bit mask to optionally invert mic data.

**Definition** dmic.h:100

[pdm\_io\_cfg::min\_pdm\_clk\_freq](structpdm__io__cfg.md#ae308635d30eaee617cb62c03c0255f37)

uint32\_t min\_pdm\_clk\_freq

Minimum clock frequency supported by the mic.

**Definition** dmic.h:82

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [audio](dir_07210b4c80db401fef5ca2f0f02fdac3.md)
- [dmic.h](dmic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
