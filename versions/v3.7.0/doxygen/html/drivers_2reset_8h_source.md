---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2reset_8h_source.html
original_path: doxygen/html/drivers_2reset_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reset.h

[Go to the documentation of this file.](drivers_2reset_8h.md)

1/\*

2 \* Copyright (c) 2022 Andrei-Edward Popa <andrei.popa105@yahoo.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RESET\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_RESET\_H\_

14

23

24#include <[errno.h](errno_8h.md)>

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[zephyr/device.h](device_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 34](structreset__dt__spec.md)struct [reset\_dt\_spec](structreset__dt__spec.md) {

[ 36](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889) const struct [device](structdevice.md) \*[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889);

[ 38](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a);

39};

40

[ 71](group__reset__controller__interface.md#ga9f2e9e2e14a6ec9d2848979c77ecad9b)#define RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx) \

72 { \

73 .dev = DEVICE\_DT\_GET(DT\_RESET\_CTLR\_BY\_IDX(node\_id, idx)), \

74 .id = DT\_RESET\_ID\_BY\_IDX(node\_id, idx) \

75 }

76

[ 93](group__reset__controller__interface.md#ga594221ce06a743b591ef285856981793)#define RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value) \

94 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, resets), \

95 (RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)), \

96 (default\_value))

97

[ 105](group__reset__controller__interface.md#gac4b466f492ae7a1c4e19647f41749c6b)#define RESET\_DT\_SPEC\_GET(node\_id) \

106 RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)

107

[ 117](group__reset__controller__interface.md#ga66fa2c042d282b34939bc762240d3705)#define RESET\_DT\_SPEC\_GET\_OR(node\_id, default\_value) \

118 RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)

119

[ 129](group__reset__controller__interface.md#ga539688cb73d17aa02b137fc90965350b)#define RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx) \

130 RESET\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), idx)

131

[ 142](group__reset__controller__interface.md#ga7d14fdead7518b4070ec7123130311b2)#define RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, idx, default\_value) \

143 COND\_CODE\_1(DT\_PROP\_HAS\_IDX(DT\_DRV\_INST(inst), resets, idx), \

144 (RESET\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), idx)), \

145 (default\_value))

146

[ 154](group__reset__controller__interface.md#ga1557bbcabdf02c3db1aa0705ce80baf0)#define RESET\_DT\_SPEC\_INST\_GET(inst) \

155 RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)

156

[ 166](group__reset__controller__interface.md#gadcb4cd7adabb84a479485da421d39c6c)#define RESET\_DT\_SPEC\_INST\_GET\_OR(inst, default\_value) \

167 RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, 0, default\_value)

168

170

176typedef int (\*reset\_api\_status)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

177

183typedef int (\*reset\_api\_line\_assert)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

184

190typedef int (\*reset\_api\_line\_deassert)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

191

197typedef int (\*reset\_api\_line\_toggle)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

198

202\_\_subsystem struct reset\_driver\_api {

203 reset\_api\_status status;

204 reset\_api\_line\_assert line\_assert;

205 reset\_api\_line\_deassert line\_deassert;

206 reset\_api\_line\_toggle line\_toggle;

207};

208

210

[ 224](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762)\_\_syscall int [reset\_status](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

225

226static inline int z\_impl\_reset\_status(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status)

227{

228 const struct reset\_driver\_api \*api = (const struct reset\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

229

230 if (api->status == NULL) {

231 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

232 }

233

234 return api->status(dev, id, status);

235}

236

[ 249](group__reset__controller__interface.md#gaa5d00726d387ff44244bc939a943963d)static inline int [reset\_status\_dt](group__reset__controller__interface.md#gaa5d00726d387ff44244bc939a943963d)(const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status)

250{

251 return [reset\_status](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762)(spec->[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889), spec->[id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a), status);

252}

253

[ 267](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6)\_\_syscall int [reset\_line\_assert](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

268

269static inline int z\_impl\_reset\_line\_assert(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

270{

271 const struct reset\_driver\_api \*api = (const struct reset\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

272

273 if (api->line\_assert == NULL) {

274 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

275 }

276

277 return api->line\_assert(dev, id);

278}

279

[ 291](group__reset__controller__interface.md#gabfe4a15880e38cbf30e293f9143d5080)static inline int [reset\_line\_assert\_dt](group__reset__controller__interface.md#gabfe4a15880e38cbf30e293f9143d5080)(const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec)

292{

293 return [reset\_line\_assert](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6)(spec->[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889), spec->[id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a));

294}

295

[ 309](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941)\_\_syscall int [reset\_line\_deassert](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

310

311static inline int z\_impl\_reset\_line\_deassert(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

312{

313 const struct reset\_driver\_api \*api = (const struct reset\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

314

315 if (api->line\_deassert == NULL) {

316 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

317 }

318

319 return api->line\_deassert(dev, id);

320}

321

[ 333](group__reset__controller__interface.md#ga7c747373b556ee1c00bad4afcdd138c0)static inline int [reset\_line\_deassert\_dt](group__reset__controller__interface.md#ga7c747373b556ee1c00bad4afcdd138c0)(const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec)

334{

335 return [reset\_line\_deassert](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941)(spec->[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889), spec->[id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a));

336}

337

[ 350](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)\_\_syscall int [reset\_line\_toggle](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

351

352static inline int z\_impl\_reset\_line\_toggle(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

353{

354 const struct reset\_driver\_api \*api = (const struct reset\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

355

356 if (api->line\_toggle == NULL) {

357 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

358 }

359

360 return api->line\_toggle(dev, id);

361}

362

[ 374](group__reset__controller__interface.md#gaf3db170375c24999ea1b1954fb3ae184)static inline int [reset\_line\_toggle\_dt](group__reset__controller__interface.md#gaf3db170375c24999ea1b1954fb3ae184)(const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec)

375{

376 return [reset\_line\_toggle](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)(spec->[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889), spec->[id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a));

377}

378

382

383#ifdef \_\_cplusplus

384}

385#endif

386

387#include <zephyr/syscalls/reset.h>

388

389#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RESET\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[reset\_line\_toggle](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)

int reset\_line\_toggle(const struct device \*dev, uint32\_t id)

Reset the device.

[reset\_line\_deassert\_dt](group__reset__controller__interface.md#ga7c747373b556ee1c00bad4afcdd138c0)

static int reset\_line\_deassert\_dt(const struct reset\_dt\_spec \*spec)

Deassert the reset state from a reset\_dt\_spec.

**Definition** reset.h:333

[reset\_status\_dt](group__reset__controller__interface.md#gaa5d00726d387ff44244bc939a943963d)

static int reset\_status\_dt(const struct reset\_dt\_spec \*spec, uint8\_t \*status)

Get the reset status from a reset\_dt\_spec.

**Definition** reset.h:249

[reset\_line\_deassert](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941)

int reset\_line\_deassert(const struct device \*dev, uint32\_t id)

Take out the device from reset state.

[reset\_line\_assert](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6)

int reset\_line\_assert(const struct device \*dev, uint32\_t id)

Put the device in reset state.

[reset\_line\_assert\_dt](group__reset__controller__interface.md#gabfe4a15880e38cbf30e293f9143d5080)

static int reset\_line\_assert\_dt(const struct reset\_dt\_spec \*spec)

Assert the reset state from a reset\_dt\_spec.

**Definition** reset.h:291

[reset\_status](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762)

int reset\_status(const struct device \*dev, uint32\_t id, uint8\_t \*status)

Get the reset status.

[reset\_line\_toggle\_dt](group__reset__controller__interface.md#gaf3db170375c24999ea1b1954fb3ae184)

static int reset\_line\_toggle\_dt(const struct reset\_dt\_spec \*spec)

Reset the device from a reset\_dt\_spec.

**Definition** reset.h:374

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[reset\_dt\_spec](structreset__dt__spec.md)

Reset controller device configuration.

**Definition** reset.h:34

[reset\_dt\_spec::dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889)

const struct device \* dev

Reset controller device.

**Definition** reset.h:36

[reset\_dt\_spec::id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a)

uint32\_t id

Reset line.

**Definition** reset.h:38

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [reset.h](drivers_2reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
