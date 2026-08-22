---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/nrf__clock__control_8h_source.html
original_path: doxygen/html/nrf__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

11#include <[zephyr/sys/onoff.h](onoff_8h.md)>

12#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18#if defined(CONFIG\_CLOCK\_CONTROL\_NRF)

19

20#include <hal/nrf\_clock.h>

21

26enum clock\_control\_nrf\_type {

27 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK,

28 CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK,

29#if NRF\_CLOCK\_HAS\_HFCLK24M

30 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK24M,

31#endif

32#if NRF\_CLOCK\_HAS\_HFCLK192M

33 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK192M,

34#endif

35#if NRF\_CLOCK\_HAS\_HFCLKAUDIO

36 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLKAUDIO,

37#endif

38 CLOCK\_CONTROL\_NRF\_TYPE\_COUNT

39};

40

41/\* Define can be used with clock control API instead of enum directly to

42 \* increase code readability.

43 \*/

44#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF \

45 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK)

46#define CLOCK\_CONTROL\_NRF\_SUBSYS\_LF \

47 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK)

48#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF24M \

49 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK24M)

50#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF192M \

51 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK192M)

52#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HFAUDIO \

53 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLKAUDIO)

54

56enum nrf\_lfclk\_start\_mode {

57 CLOCK\_CONTROL\_NRF\_LF\_START\_NOWAIT,

58 CLOCK\_CONTROL\_NRF\_LF\_START\_AVAILABLE,

59 CLOCK\_CONTROL\_NRF\_LF\_START\_STABLE,

60};

61

62/\* Define 32KHz clock source \*/

63#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_RC

64#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_RC

65#endif

66#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_XTAL

67#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL

68#endif

69#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_SYNTH

70#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_SYNTH

71#endif

72#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_EXT\_LOW\_SWING

73#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL\_LOW\_SWING

74#endif

75#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_EXT\_FULL\_SWING

76#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL\_FULL\_SWING

77#endif

78

79/\* Define 32KHz clock accuracy \*/

80#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_500PPM

81#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 0

82#endif

83#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_250PPM

84#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 1

85#endif

86#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_150PPM

87#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 2

88#endif

89#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_100PPM

90#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 3

91#endif

92#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_75PPM

93#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 4

94#endif

95#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_50PPM

96#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 5

97#endif

98#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_30PPM

99#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 6

100#endif

101#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_20PPM

102#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 7

103#endif

104

106void z\_nrf\_clock\_calibration\_force\_start(void);

107

114int z\_nrf\_clock\_calibration\_count(void);

115

122int z\_nrf\_clock\_calibration\_skips\_count(void);

123

124

129bool z\_nrf\_clock\_calibration\_is\_in\_progress(void);

130

137struct [onoff\_manager](structonoff__manager.md) \*z\_nrf\_clock\_control\_get\_onoff([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys);

138

147void z\_nrf\_clock\_control\_lf\_on(enum nrf\_lfclk\_start\_mode start\_mode);

148

161void z\_nrf\_clock\_bt\_ctlr\_hf\_request(void);

162

167void z\_nrf\_clock\_bt\_ctlr\_hf\_release(void);

168

174[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_nrf\_clock\_bt\_ctlr\_hf\_get\_startup\_time\_us(void);

175

176#endif /\* defined(CONFIG\_CLOCK\_CONTROL\_NRF) \*/

177

178/\* Specifies to use the maximum available frequency for a given clock. \*/

[ 179](nrf__clock__control_8h.md#a23770353a9de4e4bec02bca693c6709e)#define NRF\_CLOCK\_CONTROL\_FREQUENCY\_MAX UINT32\_MAX

180

181/\* Specifies to use the maximum available accuracy for a given clock. \*/

[ 182](nrf__clock__control_8h.md#af6cb7f3b8b7bb9540751639e1e48f229)#define NRF\_CLOCK\_CONTROL\_ACCURACY\_MAX 1

183/\* Specifies the required clock accuracy in parts-per-million. \*/

[ 184](nrf__clock__control_8h.md#a4a7fdc5110eef82b86b642d40d9dc02e)#define NRF\_CLOCK\_CONTROL\_ACCURACY\_PPM(ppm) (ppm)

185

186/\* Specifies that high precision of the clock is required. \*/

[ 187](nrf__clock__control_8h.md#a0c870f2b78d538f7a33cf47110ed6ea7)#define NRF\_CLOCK\_CONTROL\_PRECISION\_HIGH 1

188/\* Specifies that default precision of the clock is sufficient. \*/

[ 189](nrf__clock__control_8h.md#a15b112b62c60a7b9ca0b7fd2fccd5cca)#define NRF\_CLOCK\_CONTROL\_PRECISION\_DEFAULT 0

190

[ 191](structnrf__clock__spec.md)struct [nrf\_clock\_spec](structnrf__clock__spec.md) {

[ 192](structnrf__clock__spec.md#a8d2232359a3a5ad6983d12ab7b85abcb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frequency](structnrf__clock__spec.md#a8d2232359a3a5ad6983d12ab7b85abcb);

[ 193](structnrf__clock__spec.md#a40cedf052174f7da613e746c51c332cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [accuracy](structnrf__clock__spec.md#a40cedf052174f7da613e746c51c332cd) : 15;

[ 194](structnrf__clock__spec.md#a42d88be6efe24d4740fc74f5c839fad6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [precision](structnrf__clock__spec.md#a42d88be6efe24d4740fc74f5c839fad6) : 1;

195};

196

[ 197](structnrf__clock__control__driver__api.md)\_\_subsystem struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) {

[ 198](structnrf__clock__control__driver__api.md#ac2bd169ad00d069e5b4dc384c7d05a69) struct [clock\_control\_driver\_api](structclock__control__driver__api.md) [std\_api](structnrf__clock__control__driver__api.md#ac2bd169ad00d069e5b4dc384c7d05a69);

199

[ 200](structnrf__clock__control__driver__api.md#a5ad4fb66f464ffac5e5b221a53c276bc) int (\*[request](structnrf__clock__control__driver__api.md#a5ad4fb66f464ffac5e5b221a53c276bc))(const struct [device](structdevice.md) \*dev,

201 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec,

202 struct [onoff\_client](structonoff__client.md) \*cli);

[ 203](structnrf__clock__control__driver__api.md#aca297620f0fc63b8fd2769cb069d144a) int (\*[release](structnrf__clock__control__driver__api.md#aca297620f0fc63b8fd2769cb069d144a))(const struct [device](structdevice.md) \*dev,

204 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec);

[ 205](structnrf__clock__control__driver__api.md#a86ac5fa7b2dbae88e4be8f4adde37319) int (\*[cancel\_or\_release](structnrf__clock__control__driver__api.md#a86ac5fa7b2dbae88e4be8f4adde37319))(const struct [device](structdevice.md) \*dev,

206 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec,

207 struct [onoff\_client](structonoff__client.md) \*cli);

[ 208](structnrf__clock__control__driver__api.md#a37b6a7723376a51f112fdeda13219604) int (\*[resolve](structnrf__clock__control__driver__api.md#a37b6a7723376a51f112fdeda13219604))(const struct [device](structdevice.md) \*dev,

209 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*req\_spec,

210 struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*res\_spec);

[ 211](structnrf__clock__control__driver__api.md#ac9570d7876580df1b66d108c7b0aa78b) int (\*[get\_startup\_time](structnrf__clock__control__driver__api.md#ac9570d7876580df1b66d108c7b0aa78b))(const struct [device](structdevice.md) \*dev,

212 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec,

213 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*startup\_time\_us);

214};

215

248static inline

[ 249](nrf__clock__control_8h.md#a2da9657c008b903a9131238bde6ed1ac)int [nrf\_clock\_control\_request](nrf__clock__control_8h.md#a2da9657c008b903a9131238bde6ed1ac)(const struct [device](structdevice.md) \*dev,

250 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec,

251 struct [onoff\_client](structonoff__client.md) \*cli)

252{

253 const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*api =

254 (const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

255

256 return api->[request](structnrf__clock__control__driver__api.md#a5ad4fb66f464ffac5e5b221a53c276bc)(dev, spec, cli);

257}

258

[ 273](nrf__clock__control_8h.md#af334bc4e8b5ca0eb63b2bc4b1d963ac8)int [nrf\_clock\_control\_request\_sync](nrf__clock__control_8h.md#af334bc4e8b5ca0eb63b2bc4b1d963ac8)(const struct [device](structdevice.md) \*dev,

274 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec,

275 [k\_timeout\_t](structk__timeout__t.md) timeout);

276

291static inline

[ 292](nrf__clock__control_8h.md#aa46e3e407fb02b206772c438a0108634)int [nrf\_clock\_control\_release](nrf__clock__control_8h.md#aa46e3e407fb02b206772c438a0108634)(const struct [device](structdevice.md) \*dev,

293 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec)

294{

295 const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*api =

296 (const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

297

298 return api->[release](structnrf__clock__control__driver__api.md#aca297620f0fc63b8fd2769cb069d144a)(dev, spec);

299}

300

323static inline

[ 324](nrf__clock__control_8h.md#a3ecff5c6b37ced253c030fd032c61a70)int [nrf\_clock\_control\_cancel\_or\_release](nrf__clock__control_8h.md#a3ecff5c6b37ced253c030fd032c61a70)(const struct [device](structdevice.md) \*dev,

325 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec,

326 struct [onoff\_client](structonoff__client.md) \*cli)

327{

328 const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*api =

329 (const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

330

331 return api->[cancel\_or\_release](structnrf__clock__control__driver__api.md#a86ac5fa7b2dbae88e4be8f4adde37319)(dev, spec, cli);

332}

333

[ 344](nrf__clock__control_8h.md#add7ed9d76f521cc2894ba21abc8e4d94)static inline int [nrf\_clock\_control\_resolve](nrf__clock__control_8h.md#add7ed9d76f521cc2894ba21abc8e4d94)(const struct [device](structdevice.md) \*dev,

345 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*req\_spec,

346 struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*res\_spec)

347{

348 const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*api =

349 (const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

350

351 if (api->[resolve](structnrf__clock__control__driver__api.md#a37b6a7723376a51f112fdeda13219604) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

352 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

353 }

354

355 return api->[resolve](structnrf__clock__control__driver__api.md#a37b6a7723376a51f112fdeda13219604)(dev, req\_spec, res\_spec);

356}

357

[ 368](nrf__clock__control_8h.md#a0ac2c96482c7551b16f1cc4eadd01560)static inline int [nrf\_clock\_control\_get\_startup\_time](nrf__clock__control_8h.md#a0ac2c96482c7551b16f1cc4eadd01560)(const struct [device](structdevice.md) \*dev,

369 const struct [nrf\_clock\_spec](structnrf__clock__spec.md) \*spec,

370 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*startup\_time\_us)

371{

372 const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*api =

373 (const struct [nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

374

375 if (api->[get\_startup\_time](structnrf__clock__control__driver__api.md#ac9570d7876580df1b66d108c7b0aa78b) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

376 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

377 }

378

379 return api->[get\_startup\_time](structnrf__clock__control__driver__api.md#ac9570d7876580df1b66d108c7b0aa78b)(dev, spec, startup\_time\_us);

380}

381

[ 393](nrf__clock__control_8h.md#a259dfa1a679d21c4b92ecbf9fdfd3d13)void [nrf\_clock\_control\_hfxo\_request](nrf__clock__control_8h.md#a259dfa1a679d21c4b92ecbf9fdfd3d13)(void);

394

[ 404](nrf__clock__control_8h.md#a502110bf4c35eca120f883ba766705b7)void [nrf\_clock\_control\_hfxo\_release](nrf__clock__control_8h.md#a502110bf4c35eca120f883ba766705b7)(void);

405

406#ifdef \_\_cplusplus

407}

408#endif

409

410#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NRF\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[device.h](device_8h.md)

[clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db)

void \* clock\_control\_subsys\_t

clock\_control\_subsys\_t is a type to identify a clock controller sub-system.

**Definition** clock\_control.h:58

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[nrf\_clock\_control\_get\_startup\_time](nrf__clock__control_8h.md#a0ac2c96482c7551b16f1cc4eadd01560)

static int nrf\_clock\_control\_get\_startup\_time(const struct device \*dev, const struct nrf\_clock\_spec \*spec, uint32\_t \*startup\_time\_us)

Get the startup time of a clock.

**Definition** nrf\_clock\_control.h:368

[nrf\_clock\_control\_hfxo\_request](nrf__clock__control_8h.md#a259dfa1a679d21c4b92ecbf9fdfd3d13)

void nrf\_clock\_control\_hfxo\_request(void)

Request the HFXO from Zero Latency Interrupt context.

[nrf\_clock\_control\_request](nrf__clock__control_8h.md#a2da9657c008b903a9131238bde6ed1ac)

static int nrf\_clock\_control\_request(const struct device \*dev, const struct nrf\_clock\_spec \*spec, struct onoff\_client \*cli)

Request a reservation to use a given clock with specified attributes.

**Definition** nrf\_clock\_control.h:249

[nrf\_clock\_control\_cancel\_or\_release](nrf__clock__control_8h.md#a3ecff5c6b37ced253c030fd032c61a70)

static int nrf\_clock\_control\_cancel\_or\_release(const struct device \*dev, const struct nrf\_clock\_spec \*spec, struct onoff\_client \*cli)

Safely cancel a reservation request.

**Definition** nrf\_clock\_control.h:324

[nrf\_clock\_control\_hfxo\_release](nrf__clock__control_8h.md#a502110bf4c35eca120f883ba766705b7)

void nrf\_clock\_control\_hfxo\_release(void)

Release the HFXO from Zero Latency Interrupt context.

[nrf\_clock\_control\_release](nrf__clock__control_8h.md#aa46e3e407fb02b206772c438a0108634)

static int nrf\_clock\_control\_release(const struct device \*dev, const struct nrf\_clock\_spec \*spec)

Release a reserved use of a clock.

**Definition** nrf\_clock\_control.h:292

[nrf\_clock\_control\_resolve](nrf__clock__control_8h.md#add7ed9d76f521cc2894ba21abc8e4d94)

static int nrf\_clock\_control\_resolve(const struct device \*dev, const struct nrf\_clock\_spec \*req\_spec, struct nrf\_clock\_spec \*res\_spec)

Resolve a requested clock spec to resulting spec.

**Definition** nrf\_clock\_control.h:344

[nrf\_clock\_control\_request\_sync](nrf__clock__control_8h.md#af334bc4e8b5ca0eb63b2bc4b1d963ac8)

int nrf\_clock\_control\_request\_sync(const struct device \*dev, const struct nrf\_clock\_spec \*spec, k\_timeout\_t timeout)

Synchronously request a reservation to use a given clock with specified attributes.

[onoff.h](onoff_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[clock\_control\_driver\_api](structclock__control__driver__api.md)

**Definition** clock\_control.h:102

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[nrf\_clock\_control\_driver\_api](structnrf__clock__control__driver__api.md)

**Definition** nrf\_clock\_control.h:197

[nrf\_clock\_control\_driver\_api::resolve](structnrf__clock__control__driver__api.md#a37b6a7723376a51f112fdeda13219604)

int(\* resolve)(const struct device \*dev, const struct nrf\_clock\_spec \*req\_spec, struct nrf\_clock\_spec \*res\_spec)

**Definition** nrf\_clock\_control.h:208

[nrf\_clock\_control\_driver\_api::request](structnrf__clock__control__driver__api.md#a5ad4fb66f464ffac5e5b221a53c276bc)

int(\* request)(const struct device \*dev, const struct nrf\_clock\_spec \*spec, struct onoff\_client \*cli)

**Definition** nrf\_clock\_control.h:200

[nrf\_clock\_control\_driver\_api::cancel\_or\_release](structnrf__clock__control__driver__api.md#a86ac5fa7b2dbae88e4be8f4adde37319)

int(\* cancel\_or\_release)(const struct device \*dev, const struct nrf\_clock\_spec \*spec, struct onoff\_client \*cli)

**Definition** nrf\_clock\_control.h:205

[nrf\_clock\_control\_driver\_api::std\_api](structnrf__clock__control__driver__api.md#ac2bd169ad00d069e5b4dc384c7d05a69)

struct clock\_control\_driver\_api std\_api

**Definition** nrf\_clock\_control.h:198

[nrf\_clock\_control\_driver\_api::get\_startup\_time](structnrf__clock__control__driver__api.md#ac9570d7876580df1b66d108c7b0aa78b)

int(\* get\_startup\_time)(const struct device \*dev, const struct nrf\_clock\_spec \*spec, uint32\_t \*startup\_time\_us)

**Definition** nrf\_clock\_control.h:211

[nrf\_clock\_control\_driver\_api::release](structnrf__clock__control__driver__api.md#aca297620f0fc63b8fd2769cb069d144a)

int(\* release)(const struct device \*dev, const struct nrf\_clock\_spec \*spec)

**Definition** nrf\_clock\_control.h:203

[nrf\_clock\_spec](structnrf__clock__spec.md)

**Definition** nrf\_clock\_control.h:191

[nrf\_clock\_spec::accuracy](structnrf__clock__spec.md#a40cedf052174f7da613e746c51c332cd)

uint16\_t accuracy

**Definition** nrf\_clock\_control.h:193

[nrf\_clock\_spec::precision](structnrf__clock__spec.md#a42d88be6efe24d4740fc74f5c839fad6)

uint16\_t precision

**Definition** nrf\_clock\_control.h:194

[nrf\_clock\_spec::frequency](structnrf__clock__spec.md#a8d2232359a3a5ad6983d12ab7b85abcb)

uint32\_t frequency

**Definition** nrf\_clock\_control.h:192

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
