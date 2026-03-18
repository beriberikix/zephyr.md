---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2pinctrl_8h_source.html
original_path: doxygen/html/drivers_2pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

20

21#include <[errno.h](errno_8h.md)>

22

23#include <[zephyr/device.h](device_8h.md)>

24#include <[zephyr/devicetree.h](devicetree_8h.md)>

25#include <[zephyr/devicetree/pinctrl.h](devicetree_2pinctrl_8h.md)>

26#include <pinctrl\_soc.h>

27#include <[zephyr/sys/util.h](util_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

38

[ 40](group__pinctrl__interface.md#ga9bc564353cb9b1a7238c9fe8796023e6)#define PINCTRL\_STATE\_DEFAULT 0U

[ 42](group__pinctrl__interface.md#ga2ea5ac271930e0e2e9f77952b2dbea1b)#define PINCTRL\_STATE\_SLEEP 1U

43

[ 45](group__pinctrl__interface.md#ga25989d7b48b2d7aa4f8ca6a30d9c9077)#define PINCTRL\_STATE\_PRIV\_START 2U

46

48

[ 50](structpinctrl__state.md)struct [pinctrl\_state](structpinctrl__state.md) {

[ 52](structpinctrl__state.md#a99ceb5bff2b8e50109e5915140eebe76) const pinctrl\_soc\_pin\_t \*[pins](structpinctrl__state.md#a99ceb5bff2b8e50109e5915140eebe76);

[ 54](structpinctrl__state.md#aa015854e6eae7b86fffb282b07652573) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin\_cnt](structpinctrl__state.md#aa015854e6eae7b86fffb282b07652573);

[ 56](structpinctrl__state.md#acae4c7cfc06471533f6d977e1f2ba623) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structpinctrl__state.md#acae4c7cfc06471533f6d977e1f2ba623);

57};

58

[ 60](structpinctrl__dev__config.md)struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) {

61#if defined(CONFIG\_PINCTRL\_STORE\_REG) || defined(\_\_DOXYGEN\_\_)

[ 66](structpinctrl__dev__config.md#a69db43c310985f38f0802a3e9f82fd62) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [reg](structpinctrl__dev__config.md#a69db43c310985f38f0802a3e9f82fd62);

67#endif /\* defined(CONFIG\_PINCTRL\_STORE\_REG) || defined(\_\_DOXYGEN\_\_) \*/

[ 69](structpinctrl__dev__config.md#a57dcdf2f712de95f8e8568e2be4b52e6) const struct [pinctrl\_state](structpinctrl__state.md) \*[states](structpinctrl__dev__config.md#a57dcdf2f712de95f8e8568e2be4b52e6);

[ 71](structpinctrl__dev__config.md#a0af0d0115eaa9729c1fe782666ad0e66) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state\_cnt](structpinctrl__dev__config.md#a0af0d0115eaa9729c1fe782666ad0e66);

72};

73

[ 75](group__pinctrl__interface.md#ga6e283a1a1b040323b96227b2ea8f731e)#define PINCTRL\_REG\_NONE 0U

76

78

79#if !defined(CONFIG\_PM) && !defined(CONFIG\_PM\_DEVICE)

81#define PINCTRL\_SKIP\_SLEEP 1

82#endif

83

90#define Z\_PINCTRL\_STATE\_ID(state\_idx, node\_id) \

91 \_CONCAT(PINCTRL\_STATE\_, \

92 DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(node\_id, state\_idx))

93

100#define Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id) \

101 \_CONCAT(\_\_pinctrl\_dev\_config, DEVICE\_DT\_NAME\_GET(node\_id))

102

109#define Z\_PINCTRL\_STATES\_NAME(node\_id) \

110 \_CONCAT(\_\_pinctrl\_states, DEVICE\_DT\_NAME\_GET(node\_id))

111

119#define Z\_PINCTRL\_STATE\_PINS\_NAME(state\_idx, node\_id) \

120 \_CONCAT(\_\_pinctrl\_state\_pins\_ ## state\_idx, DEVICE\_DT\_NAME\_GET(node\_id))

121

133#define Z\_PINCTRL\_SKIP\_STATE(state\_idx, node\_id) \

134 \_CONCAT(PINCTRL\_SKIP\_, \

135 DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(node\_id, state\_idx))

136

143#define Z\_PINCTRL\_STATE\_PINS\_DEFINE(state\_idx, node\_id) \

144 COND\_CODE\_1(Z\_PINCTRL\_SKIP\_STATE(state\_idx, node\_id), (), \

145 (static const pinctrl\_soc\_pin\_t \

146 Z\_PINCTRL\_STATE\_PINS\_NAME(state\_idx, node\_id)[] = \

147 Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, pinctrl\_ ## state\_idx)))

148

155#define Z\_PINCTRL\_STATE\_INIT(state\_idx, node\_id) \

156 COND\_CODE\_1(Z\_PINCTRL\_SKIP\_STATE(state\_idx, node\_id), (), \

157 ({ \

158 .id = Z\_PINCTRL\_STATE\_ID(state\_idx, node\_id), \

159 .pins = Z\_PINCTRL\_STATE\_PINS\_NAME(state\_idx, node\_id), \

160 .pin\_cnt = ARRAY\_SIZE(Z\_PINCTRL\_STATE\_PINS\_NAME(state\_idx, \

161 node\_id)) \

162 }))

163

169#define Z\_PINCTRL\_STATES\_DEFINE(node\_id) \

170 static const struct pinctrl\_state \

171 Z\_PINCTRL\_STATES\_NAME(node\_id)[] = { \

172 LISTIFY(DT\_NUM\_PINCTRL\_STATES(node\_id), \

173 Z\_PINCTRL\_STATE\_INIT, (,), node\_id) \

174 };

175

176#ifdef CONFIG\_PINCTRL\_STORE\_REG

182#define Z\_PINCTRL\_DEV\_CONFIG\_INIT(node\_id) \

183 { \

184 .reg = DT\_REG\_ADDR(node\_id), \

185 .states = Z\_PINCTRL\_STATES\_NAME(node\_id), \

186 .state\_cnt = ARRAY\_SIZE(Z\_PINCTRL\_STATES\_NAME(node\_id)), \

187 }

188#else

189#define Z\_PINCTRL\_DEV\_CONFIG\_INIT(node\_id) \

190 { \

191 .states = Z\_PINCTRL\_STATES\_NAME(node\_id), \

192 .state\_cnt = ARRAY\_SIZE(Z\_PINCTRL\_STATES\_NAME(node\_id)), \

193 }

194#endif

195

196#ifdef CONFIG\_PINCTRL\_NON\_STATIC

197#define Z\_PINCTRL\_DEV\_CONFIG\_STATIC

198#else

199#define Z\_PINCTRL\_DEV\_CONFIG\_STATIC static

200#endif

201

202#ifdef CONFIG\_PINCTRL\_DYNAMIC

203#define Z\_PINCTRL\_DEV\_CONFIG\_CONST

204#else

205#define Z\_PINCTRL\_DEV\_CONFIG\_CONST const

206#endif

207

209

210#if defined(CONFIG\_PINCTRL\_NON\_STATIC) || defined(\_\_DOXYGEN\_\_)

[ 223](group__pinctrl__interface.md#ga636656676e81c65e1133607c972d65f4)#define PINCTRL\_DT\_DEV\_CONFIG\_DECLARE(node\_id) \

224 extern Z\_PINCTRL\_DEV\_CONFIG\_CONST struct pinctrl\_dev\_config \

225 Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id)

226#endif /\* defined(CONFIG\_PINCTRL\_NON\_STATIC) || defined(\_\_DOXYGEN\_\_) \*/

227

[ 239](group__pinctrl__interface.md#gace422fcd4b28e6e6e6fdbbc64b99468f)#define PINCTRL\_DT\_DEFINE(node\_id) \

240 LISTIFY(DT\_NUM\_PINCTRL\_STATES(node\_id), \

241 Z\_PINCTRL\_STATE\_PINS\_DEFINE, (;), node\_id); \

242 Z\_PINCTRL\_STATES\_DEFINE(node\_id) \

243 Z\_PINCTRL\_DEV\_CONFIG\_STATIC Z\_PINCTRL\_DEV\_CONFIG\_CONST \

244 struct pinctrl\_dev\_config Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id) = \

245 Z\_PINCTRL\_DEV\_CONFIG\_INIT(node\_id)

246

[ 254](group__pinctrl__interface.md#ga8e984a57fd3c7a04cc921131ce79ac28)#define PINCTRL\_DT\_INST\_DEFINE(inst) PINCTRL\_DT\_DEFINE(DT\_DRV\_INST(inst))

255

[ 262](group__pinctrl__interface.md#ga502c3b6faec140188dd5d614f4777918)#define PINCTRL\_DT\_DEV\_CONFIG\_GET(node\_id) &Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id)

263

[ 272](group__pinctrl__interface.md#ga32748ffc5be4710707c7f1d9380cf93c)#define PINCTRL\_DT\_INST\_DEV\_CONFIG\_GET(inst) \

273 PINCTRL\_DT\_DEV\_CONFIG\_GET(DT\_DRV\_INST(inst))

274

[ 285](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50)int [pinctrl\_lookup\_state](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50)(const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id,

286 const struct [pinctrl\_state](structpinctrl__state.md) \*\*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

287

[ 304](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b)int [pinctrl\_configure\_pins](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b)(const pinctrl\_soc\_pin\_t \*[pins](structpinctrl__state.md#a99ceb5bff2b8e50109e5915140eebe76), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin\_cnt](structpinctrl__state.md#aa015854e6eae7b86fffb282b07652573),

305 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) reg);

306

[ 316](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b)static inline int [pinctrl\_apply\_state\_direct](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b)(

317 const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config,

318 const struct [pinctrl\_state](structpinctrl__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

319{

320 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) reg;

321

322#ifdef CONFIG\_PINCTRL\_STORE\_REG

323 reg = config->[reg](structpinctrl__dev__config.md#a69db43c310985f38f0802a3e9f82fd62);

324#else

325 ARG\_UNUSED(config);

326 reg = [PINCTRL\_REG\_NONE](group__pinctrl__interface.md#ga6e283a1a1b040323b96227b2ea8f731e);

327#endif

328

329 return [pinctrl\_configure\_pins](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b)([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->pins, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->pin\_cnt, reg);

330}

331

[ 342](group__pinctrl__interface.md#ga16a9391222345d00dbc5c39c45f429f9)static inline int [pinctrl\_apply\_state](group__pinctrl__interface.md#ga16a9391222345d00dbc5c39c45f429f9)(const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config,

343 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id)

344{

345 int ret;

346 const struct [pinctrl\_state](structpinctrl__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

347

348 ret = [pinctrl\_lookup\_state](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50)(config, id, &[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

349 if (ret < 0) {

350 return ret;

351 }

352

353 return [pinctrl\_apply\_state\_direct](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b)(config, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

354}

355

356#if defined(CONFIG\_PINCTRL\_DYNAMIC) || defined(\_\_DOXYGEN\_\_)

361

[ 374](group__pinctrl__interface__dynamic.md#ga202dbcf2bcde364733996673dbdf2922)#define PINCTRL\_DT\_STATE\_PINS\_DEFINE(node\_id, prop) \

375 static const pinctrl\_soc\_pin\_t prop ## \_pins[] = \

376 Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop); \

377

378

[ 413](group__pinctrl__interface__dynamic.md#ga6331121c706ba721e5bd43491dcc14d2)#define PINCTRL\_DT\_STATE\_INIT(prop, state) \

414 { \

415 .id = state, \

416 .pins = prop ## \_pins, \

417 .pin\_cnt = ARRAY\_SIZE(prop ## \_pins) \

418 }

419

[ 437](group__pinctrl__interface__dynamic.md#ga647115208cbed7534a98c56d93a517b8)int [pinctrl\_update\_states](group__pinctrl__interface__dynamic.md#ga647115208cbed7534a98c56d93a517b8)(struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config,

438 const struct [pinctrl\_state](structpinctrl__state.md) \*states,

439 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) state\_cnt);

440

442#else

443static inline int [pinctrl\_update\_states](group__pinctrl__interface__dynamic.md#ga647115208cbed7534a98c56d93a517b8)(

444 struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config,

445 const struct [pinctrl\_state](structpinctrl__state.md) \*states, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) state\_cnt)

446{

447 ARG\_UNUSED(config);

448 ARG\_UNUSED(states);

449 ARG\_UNUSED(state\_cnt);

450 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

451}

452#endif /\* defined(CONFIG\_PINCTRL\_DYNAMIC) || defined(\_\_DOXYGEN\_\_) \*/

453

454#ifdef \_\_cplusplus

455}

456#endif

457

461

462#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PINCTRL\_H\_ \*/

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

**Definition** pinctrl.h:342

[pinctrl\_configure\_pins](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b)

int pinctrl\_configure\_pins(const pinctrl\_soc\_pin\_t \*pins, uint8\_t pin\_cnt, uintptr\_t reg)

Configure a set of pins.

[pinctrl\_apply\_state\_direct](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b)

static int pinctrl\_apply\_state\_direct(const struct pinctrl\_dev\_config \*config, const struct pinctrl\_state \*state)

Apply a state directly from the provided state configuration.

**Definition** pinctrl.h:316

[pinctrl\_lookup\_state](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50)

int pinctrl\_lookup\_state(const struct pinctrl\_dev\_config \*config, uint8\_t id, const struct pinctrl\_state \*\*state)

Find the state configuration for the given state id.

[PINCTRL\_REG\_NONE](group__pinctrl__interface.md#ga6e283a1a1b040323b96227b2ea8f731e)

#define PINCTRL\_REG\_NONE

Utility macro to indicate no register is used.

**Definition** pinctrl.h:75

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[pinctrl\_dev\_config](structpinctrl__dev__config.md)

Pin controller configuration for a given device.

**Definition** pinctrl.h:60

[pinctrl\_dev\_config::state\_cnt](structpinctrl__dev__config.md#a0af0d0115eaa9729c1fe782666ad0e66)

uint8\_t state\_cnt

Number of state configurations.

**Definition** pinctrl.h:71

[pinctrl\_dev\_config::states](structpinctrl__dev__config.md#a57dcdf2f712de95f8e8568e2be4b52e6)

const struct pinctrl\_state \* states

List of state configurations.

**Definition** pinctrl.h:69

[pinctrl\_dev\_config::reg](structpinctrl__dev__config.md#a69db43c310985f38f0802a3e9f82fd62)

uintptr\_t reg

Device address (only available if <code>CONFIG\_PINCTRL\_STORE\_REG</code> <verbatim>embed:rst:inline...

**Definition** pinctrl.h:66

[pinctrl\_state](structpinctrl__state.md)

Pin control state configuration.

**Definition** pinctrl.h:50

[pinctrl\_state::pins](structpinctrl__state.md#a99ceb5bff2b8e50109e5915140eebe76)

const pinctrl\_soc\_pin\_t \* pins

Pin configurations.

**Definition** pinctrl.h:52

[pinctrl\_state::pin\_cnt](structpinctrl__state.md#aa015854e6eae7b86fffb282b07652573)

uint8\_t pin\_cnt

Number of pin configurations.

**Definition** pinctrl.h:54

[pinctrl\_state::id](structpinctrl__state.md#acae4c7cfc06471533f6d977e1f2ba623)

uint8\_t id

State identifier (see PINCTRL\_STATES).

**Definition** pinctrl.h:56

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl.h](drivers_2pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
