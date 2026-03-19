---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2pinctrl_8h_source.html
original_path: doxygen/html/drivers_2pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl.h

[Go to the documentation of this file.](drivers_2pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

10

11#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_H\_

12#define ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_H\_

13

22

23#include <[errno.h](errno_8h.md)>

24

25#include <[zephyr/device.h](device_8h.md)>

26#include <[zephyr/devicetree.h](devicetree_8h.md)>

27#include <[zephyr/devicetree/pinctrl.h](devicetree_2pinctrl_8h.md)>

28#include <pinctrl\_soc.h>

29#include <[zephyr/sys/util.h](sys_2util_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

40

[ 42](group__pinctrl__interface.md#ga9bc564353cb9b1a7238c9fe8796023e6)#define PINCTRL\_STATE\_DEFAULT 0U

[ 44](group__pinctrl__interface.md#ga2ea5ac271930e0e2e9f77952b2dbea1b)#define PINCTRL\_STATE\_SLEEP 1U

45

[ 47](group__pinctrl__interface.md#ga25989d7b48b2d7aa4f8ca6a30d9c9077)#define PINCTRL\_STATE\_PRIV\_START 2U

48

50

[ 52](structpinctrl__state.md)struct [pinctrl\_state](structpinctrl__state.md) {

[ 54](structpinctrl__state.md#a99ceb5bff2b8e50109e5915140eebe76) const [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d) \*[pins](structpinctrl__state.md#a99ceb5bff2b8e50109e5915140eebe76);

[ 56](structpinctrl__state.md#aa015854e6eae7b86fffb282b07652573) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin\_cnt](structpinctrl__state.md#aa015854e6eae7b86fffb282b07652573);

[ 58](structpinctrl__state.md#acae4c7cfc06471533f6d977e1f2ba623) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structpinctrl__state.md#acae4c7cfc06471533f6d977e1f2ba623);

59};

60

[ 62](structpinctrl__dev__config.md)struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) {

63#if defined(CONFIG\_PINCTRL\_STORE\_REG) || defined(\_\_DOXYGEN\_\_)

[ 68](structpinctrl__dev__config.md#a69db43c310985f38f0802a3e9f82fd62) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [reg](structpinctrl__dev__config.md#a69db43c310985f38f0802a3e9f82fd62);

69#endif /\* defined(CONFIG\_PINCTRL\_STORE\_REG) || defined(\_\_DOXYGEN\_\_) \*/

[ 71](structpinctrl__dev__config.md#a57dcdf2f712de95f8e8568e2be4b52e6) const struct [pinctrl\_state](structpinctrl__state.md) \*[states](structpinctrl__dev__config.md#a57dcdf2f712de95f8e8568e2be4b52e6);

[ 73](structpinctrl__dev__config.md#a0af0d0115eaa9729c1fe782666ad0e66) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state\_cnt](structpinctrl__dev__config.md#a0af0d0115eaa9729c1fe782666ad0e66);

74};

75

[ 77](group__pinctrl__interface.md#ga6e283a1a1b040323b96227b2ea8f731e)#define PINCTRL\_REG\_NONE 0U

78

80

81#if !defined(CONFIG\_PM) && !defined(CONFIG\_PM\_DEVICE)

83#define PINCTRL\_SKIP\_SLEEP 1

84#endif

85

92#define Z\_PINCTRL\_STATE\_ID(state\_idx, node\_id) \

93 \_CONCAT(PINCTRL\_STATE\_, \

94 DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(node\_id, state\_idx))

95

102#define Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id) \

103 \_CONCAT(\_\_pinctrl\_dev\_config, DEVICE\_DT\_NAME\_GET(node\_id))

104

111#define Z\_PINCTRL\_STATES\_NAME(node\_id) \

112 \_CONCAT(\_\_pinctrl\_states, DEVICE\_DT\_NAME\_GET(node\_id))

113

121#define Z\_PINCTRL\_STATE\_PINS\_NAME(state\_idx, node\_id) \

122 \_CONCAT(\_\_pinctrl\_state\_pins\_ ## state\_idx, DEVICE\_DT\_NAME\_GET(node\_id))

123

135#define Z\_PINCTRL\_SKIP\_STATE(state\_idx, node\_id) \

136 \_CONCAT(PINCTRL\_SKIP\_, \

137 DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(node\_id, state\_idx))

138

145#define Z\_PINCTRL\_STATE\_PINS\_DEFINE(state\_idx, node\_id) \

146 COND\_CODE\_1(Z\_PINCTRL\_SKIP\_STATE(state\_idx, node\_id), (), \

147 (static const pinctrl\_soc\_pin\_t \

148 Z\_PINCTRL\_STATE\_PINS\_NAME(state\_idx, node\_id)[] = \

149 Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, pinctrl\_ ## state\_idx)))

150

157#define Z\_PINCTRL\_STATE\_INIT(state\_idx, node\_id) \

158 COND\_CODE\_1(Z\_PINCTRL\_SKIP\_STATE(state\_idx, node\_id), (), \

159 ({ \

160 .id = Z\_PINCTRL\_STATE\_ID(state\_idx, node\_id), \

161 .pins = Z\_PINCTRL\_STATE\_PINS\_NAME(state\_idx, node\_id), \

162 .pin\_cnt = ARRAY\_SIZE(Z\_PINCTRL\_STATE\_PINS\_NAME(state\_idx, \

163 node\_id)) \

164 }))

165

171#define Z\_PINCTRL\_STATES\_DEFINE(node\_id) \

172 static const struct pinctrl\_state \

173 Z\_PINCTRL\_STATES\_NAME(node\_id)[] = { \

174 LISTIFY(DT\_NUM\_PINCTRL\_STATES(node\_id), \

175 Z\_PINCTRL\_STATE\_INIT, (,), node\_id) \

176 };

177

178#ifdef CONFIG\_PINCTRL\_STORE\_REG

184#define Z\_PINCTRL\_DEV\_CONFIG\_INIT(node\_id) \

185 { \

186 .reg = DT\_REG\_ADDR(node\_id), \

187 .states = Z\_PINCTRL\_STATES\_NAME(node\_id), \

188 .state\_cnt = ARRAY\_SIZE(Z\_PINCTRL\_STATES\_NAME(node\_id)), \

189 }

190#else

191#define Z\_PINCTRL\_DEV\_CONFIG\_INIT(node\_id) \

192 { \

193 .states = Z\_PINCTRL\_STATES\_NAME(node\_id), \

194 .state\_cnt = ARRAY\_SIZE(Z\_PINCTRL\_STATES\_NAME(node\_id)), \

195 }

196#endif

197

198#ifdef CONFIG\_PINCTRL\_NON\_STATIC

199#define Z\_PINCTRL\_DEV\_CONFIG\_STATIC

200#else

201#define Z\_PINCTRL\_DEV\_CONFIG\_STATIC static

202#endif

203

204#ifdef CONFIG\_PINCTRL\_DYNAMIC

205#define Z\_PINCTRL\_DEV\_CONFIG\_CONST

206#else

207#define Z\_PINCTRL\_DEV\_CONFIG\_CONST const

208#endif

209

211

212#if defined(CONFIG\_PINCTRL\_NON\_STATIC) || defined(\_\_DOXYGEN\_\_)

[ 225](group__pinctrl__interface.md#ga636656676e81c65e1133607c972d65f4)#define PINCTRL\_DT\_DEV\_CONFIG\_DECLARE(node\_id) \

226 extern Z\_PINCTRL\_DEV\_CONFIG\_CONST struct pinctrl\_dev\_config \

227 Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id)

228#endif /\* defined(CONFIG\_PINCTRL\_NON\_STATIC) || defined(\_\_DOXYGEN\_\_) \*/

229

[ 241](group__pinctrl__interface.md#gace422fcd4b28e6e6e6fdbbc64b99468f)#define PINCTRL\_DT\_DEFINE(node\_id) \

242 LISTIFY(DT\_NUM\_PINCTRL\_STATES(node\_id), \

243 Z\_PINCTRL\_STATE\_PINS\_DEFINE, (;), node\_id); \

244 Z\_PINCTRL\_STATES\_DEFINE(node\_id) \

245 Z\_PINCTRL\_DEV\_CONFIG\_STATIC Z\_PINCTRL\_DEV\_CONFIG\_CONST \

246 struct pinctrl\_dev\_config Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id) = \

247 Z\_PINCTRL\_DEV\_CONFIG\_INIT(node\_id)

248

[ 256](group__pinctrl__interface.md#ga8e984a57fd3c7a04cc921131ce79ac28)#define PINCTRL\_DT\_INST\_DEFINE(inst) PINCTRL\_DT\_DEFINE(DT\_DRV\_INST(inst))

257

[ 264](group__pinctrl__interface.md#ga502c3b6faec140188dd5d614f4777918)#define PINCTRL\_DT\_DEV\_CONFIG\_GET(node\_id) &Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id)

265

[ 274](group__pinctrl__interface.md#ga32748ffc5be4710707c7f1d9380cf93c)#define PINCTRL\_DT\_INST\_DEV\_CONFIG\_GET(inst) \

275 PINCTRL\_DT\_DEV\_CONFIG\_GET(DT\_DRV\_INST(inst))

276

[ 287](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50)int [pinctrl\_lookup\_state](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50)(const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

288 const struct [pinctrl\_state](structpinctrl__state.md) \*\*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

289

[ 306](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b)int [pinctrl\_configure\_pins](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b)(const [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d) \*[pins](structpinctrl__state.md#a99ceb5bff2b8e50109e5915140eebe76), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin\_cnt](structpinctrl__state.md#aa015854e6eae7b86fffb282b07652573),

307 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) reg);

308

[ 318](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b)static inline int [pinctrl\_apply\_state\_direct](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b)(

319 const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config,

320 const struct [pinctrl\_state](structpinctrl__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

321{

322 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) reg;

323

324#ifdef CONFIG\_PINCTRL\_STORE\_REG

325 reg = config->[reg](structpinctrl__dev__config.md#a69db43c310985f38f0802a3e9f82fd62);

326#else

327 ARG\_UNUSED(config);

328 reg = [PINCTRL\_REG\_NONE](group__pinctrl__interface.md#ga6e283a1a1b040323b96227b2ea8f731e);

329#endif

330

331 return [pinctrl\_configure\_pins](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->pins, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->pin\_cnt, reg);

332}

333

[ 344](group__pinctrl__interface.md#ga16a9391222345d00dbc5c39c45f429f9)static inline int [pinctrl\_apply\_state](group__pinctrl__interface.md#ga16a9391222345d00dbc5c39c45f429f9)(const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config,

345 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id)

346{

347 int ret;

348 const struct [pinctrl\_state](structpinctrl__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

349

350 ret = [pinctrl\_lookup\_state](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50)(config, id, &[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

351 if (ret < 0) {

352 return ret;

353 }

354

355 return [pinctrl\_apply\_state\_direct](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b)(config, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

356}

357

358#if defined(CONFIG\_PINCTRL\_DYNAMIC) || defined(\_\_DOXYGEN\_\_)

363

[ 376](group__pinctrl__interface__dynamic.md#ga202dbcf2bcde364733996673dbdf2922)#define PINCTRL\_DT\_STATE\_PINS\_DEFINE(node\_id, prop) \

377 static const pinctrl\_soc\_pin\_t prop ## \_pins[] = \

378 Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop); \

379

380

[ 415](group__pinctrl__interface__dynamic.md#ga6331121c706ba721e5bd43491dcc14d2)#define PINCTRL\_DT\_STATE\_INIT(prop, state) \

416 { \

417 .pins = prop ## \_pins, \

418 .pin\_cnt = ARRAY\_SIZE(prop ## \_pins), \

419 .id = state \

420 }

421

[ 439](group__pinctrl__interface__dynamic.md#ga647115208cbed7534a98c56d93a517b8)int [pinctrl\_update\_states](group__pinctrl__interface__dynamic.md#ga647115208cbed7534a98c56d93a517b8)(struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config,

440 const struct [pinctrl\_state](structpinctrl__state.md) \*states,

441 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) state\_cnt);

442

444#else

445static inline int [pinctrl\_update\_states](group__pinctrl__interface__dynamic.md#ga647115208cbed7534a98c56d93a517b8)(

446 struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config,

447 const struct [pinctrl\_state](structpinctrl__state.md) \*states, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) state\_cnt)

448{

449 ARG\_UNUSED(config);

450 ARG\_UNUSED(states);

451 ARG\_UNUSED(state\_cnt);

452 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

453}

454#endif /\* defined(CONFIG\_PINCTRL\_DYNAMIC) || defined(\_\_DOXYGEN\_\_) \*/

455

456#ifdef \_\_cplusplus

457}

458#endif

459

463

464#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_H\_ \*/

[device.h](device_8h.md)

[pinctrl.h](devicetree_2pinctrl_8h.md)

Devicetree pin control helpers.

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[errno.h](errno_8h.md)

System error numbers.

[pinctrl\_update\_states](group__pinctrl__interface__dynamic.md#ga647115208cbed7534a98c56d93a517b8)

int pinctrl\_update\_states(struct pinctrl\_dev\_config \*config, const struct pinctrl\_state \*states, uint8\_t state\_cnt)

Update states with a new set.

[pinctrl\_apply\_state](group__pinctrl__interface.md#ga16a9391222345d00dbc5c39c45f429f9)

static int pinctrl\_apply\_state(const struct pinctrl\_dev\_config \*config, uint8\_t id)

Apply a state from the given device configuration.

**Definition** pinctrl.h:344

[pinctrl\_configure\_pins](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b)

int pinctrl\_configure\_pins(const pinctrl\_soc\_pin\_t \*pins, uint8\_t pin\_cnt, uintptr\_t reg)

Configure a set of pins.

[pinctrl\_apply\_state\_direct](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b)

static int pinctrl\_apply\_state\_direct(const struct pinctrl\_dev\_config \*config, const struct pinctrl\_state \*state)

Apply a state directly from the provided state configuration.

**Definition** pinctrl.h:318

[pinctrl\_lookup\_state](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50)

int pinctrl\_lookup\_state(const struct pinctrl\_dev\_config \*config, uint8\_t id, const struct pinctrl\_state \*\*state)

Find the state configuration for the given state id.

[PINCTRL\_REG\_NONE](group__pinctrl__interface.md#ga6e283a1a1b040323b96227b2ea8f731e)

#define PINCTRL\_REG\_NONE

Utility macro to indicate no register is used.

**Definition** pinctrl.h:77

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d)

struct pinctrl\_soc\_pin pinctrl\_soc\_pin\_t

Type for R-Car pin.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[pinctrl\_dev\_config](structpinctrl__dev__config.md)

Pin controller configuration for a given device.

**Definition** pinctrl.h:62

[pinctrl\_dev\_config::state\_cnt](structpinctrl__dev__config.md#a0af0d0115eaa9729c1fe782666ad0e66)

uint8\_t state\_cnt

Number of state configurations.

**Definition** pinctrl.h:73

[pinctrl\_dev\_config::states](structpinctrl__dev__config.md#a57dcdf2f712de95f8e8568e2be4b52e6)

const struct pinctrl\_state \* states

List of state configurations.

**Definition** pinctrl.h:71

[pinctrl\_dev\_config::reg](structpinctrl__dev__config.md#a69db43c310985f38f0802a3e9f82fd62)

uintptr\_t reg

Device address (only available if.

**Definition** pinctrl.h:68

[pinctrl\_state](structpinctrl__state.md)

Pin control state configuration.

**Definition** pinctrl.h:52

[pinctrl\_state::pins](structpinctrl__state.md#a99ceb5bff2b8e50109e5915140eebe76)

const pinctrl\_soc\_pin\_t \* pins

Pin configurations.

**Definition** pinctrl.h:54

[pinctrl\_state::pin\_cnt](structpinctrl__state.md#aa015854e6eae7b86fffb282b07652573)

uint8\_t pin\_cnt

Number of pin configurations.

**Definition** pinctrl.h:56

[pinctrl\_state::id](structpinctrl__state.md#acae4c7cfc06471533f6d977e1f2ba623)

uint8\_t id

State identifier (see PINCTRL\_STATES).

**Definition** pinctrl.h:58

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl.h](drivers_2pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
