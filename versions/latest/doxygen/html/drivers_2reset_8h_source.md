---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2reset_8h_source.html
original_path: doxygen/html/drivers_2reset_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

21

22#include <[errno.h](errno_8h.md)>

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 32](structreset__dt__spec.md)struct [reset\_dt\_spec](structreset__dt__spec.md) {

[ 34](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889) const struct [device](structdevice.md) \*[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889);

[ 36](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a);

37};

38

[ 69](group__reset__controller__interface.md#ga9f2e9e2e14a6ec9d2848979c77ecad9b)#define RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx) \

70 { \

71 .dev = DEVICE\_DT\_GET(DT\_RESET\_CTLR\_BY\_IDX(node\_id, idx)), \

72 .id = DT\_RESET\_ID\_BY\_IDX(node\_id, idx) \

73 }

74

[ 82](group__reset__controller__interface.md#gac4b466f492ae7a1c4e19647f41749c6b)#define RESET\_DT\_SPEC\_GET(node\_id) \

83 RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)

84

[ 94](group__reset__controller__interface.md#ga539688cb73d17aa02b137fc90965350b)#define RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx) \

95 RESET\_DT\_SPEC\_GET\_BY\_IDX(DT\_DRV\_INST(inst), idx)

96

[ 104](group__reset__controller__interface.md#ga1557bbcabdf02c3db1aa0705ce80baf0)#define RESET\_DT\_SPEC\_INST\_GET(inst) \

105 RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)

106

108

114typedef int (\*reset\_api\_status)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

115

121typedef int (\*reset\_api\_line\_assert)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

122

128typedef int (\*reset\_api\_line\_deassert)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

129

135typedef int (\*reset\_api\_line\_toggle)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

136

140\_\_subsystem struct reset\_driver\_api {

141 reset\_api\_status status;

142 reset\_api\_line\_assert line\_assert;

143 reset\_api\_line\_deassert line\_deassert;

144 reset\_api\_line\_toggle line\_toggle;

145};

146

148

[ 162](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762)\_\_syscall int [reset\_status](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status);

163

164static inline int z\_impl\_reset\_status(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status)

165{

166 const struct reset\_driver\_api \*api = (const struct reset\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

167

168 if (api->status == NULL) {

169 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

170 }

171

172 return api->status(dev, id, status);

173}

174

[ 187](group__reset__controller__interface.md#gaa5d00726d387ff44244bc939a943963d)static inline int [reset\_status\_dt](group__reset__controller__interface.md#gaa5d00726d387ff44244bc939a943963d)(const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status)

188{

189 return [reset\_status](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762)(spec->[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889), spec->[id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a), status);

190}

191

[ 205](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6)\_\_syscall int [reset\_line\_assert](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

206

207static inline int z\_impl\_reset\_line\_assert(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

208{

209 const struct reset\_driver\_api \*api = (const struct reset\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

210

211 if (api->line\_assert == NULL) {

212 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

213 }

214

215 return api->line\_assert(dev, id);

216}

217

[ 229](group__reset__controller__interface.md#gabfe4a15880e38cbf30e293f9143d5080)static inline int [reset\_line\_assert\_dt](group__reset__controller__interface.md#gabfe4a15880e38cbf30e293f9143d5080)(const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec)

230{

231 return [reset\_line\_assert](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6)(spec->[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889), spec->[id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a));

232}

233

[ 247](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941)\_\_syscall int [reset\_line\_deassert](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

248

249static inline int z\_impl\_reset\_line\_deassert(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

250{

251 const struct reset\_driver\_api \*api = (const struct reset\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

252

253 if (api->line\_deassert == NULL) {

254 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

255 }

256

257 return api->line\_deassert(dev, id);

258}

259

[ 271](group__reset__controller__interface.md#ga7c747373b556ee1c00bad4afcdd138c0)static inline int [reset\_line\_deassert\_dt](group__reset__controller__interface.md#ga7c747373b556ee1c00bad4afcdd138c0)(const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec)

272{

273 return [reset\_line\_deassert](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941)(spec->[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889), spec->[id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a));

274}

275

[ 288](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)\_\_syscall int [reset\_line\_toggle](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

289

290static inline int z\_impl\_reset\_line\_toggle(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

291{

292 const struct reset\_driver\_api \*api = (const struct reset\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

293

294 if (api->line\_toggle == NULL) {

295 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

296 }

297

298 return api->line\_toggle(dev, id);

299}

300

[ 312](group__reset__controller__interface.md#gaf3db170375c24999ea1b1954fb3ae184)static inline int [reset\_line\_toggle\_dt](group__reset__controller__interface.md#gaf3db170375c24999ea1b1954fb3ae184)(const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec)

313{

314 return [reset\_line\_toggle](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)(spec->[dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889), spec->[id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a));

315}

316

320

321#ifdef \_\_cplusplus

322}

323#endif

324

325#include <syscalls/reset.h>

326

327#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RESET\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[reset\_line\_toggle](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e)

int reset\_line\_toggle(const struct device \*dev, uint32\_t id)

Reset the device.

[reset\_line\_deassert\_dt](group__reset__controller__interface.md#ga7c747373b556ee1c00bad4afcdd138c0)

static int reset\_line\_deassert\_dt(const struct reset\_dt\_spec \*spec)

Deassert the reset state from a reset\_dt\_spec.

**Definition** reset.h:271

[reset\_status\_dt](group__reset__controller__interface.md#gaa5d00726d387ff44244bc939a943963d)

static int reset\_status\_dt(const struct reset\_dt\_spec \*spec, uint8\_t \*status)

Get the reset status from a reset\_dt\_spec.

**Definition** reset.h:187

[reset\_line\_deassert](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941)

int reset\_line\_deassert(const struct device \*dev, uint32\_t id)

Take out the device from reset state.

[reset\_line\_assert](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6)

int reset\_line\_assert(const struct device \*dev, uint32\_t id)

Put the device in reset state.

[reset\_line\_assert\_dt](group__reset__controller__interface.md#gabfe4a15880e38cbf30e293f9143d5080)

static int reset\_line\_assert\_dt(const struct reset\_dt\_spec \*spec)

Assert the reset state from a reset\_dt\_spec.

**Definition** reset.h:229

[reset\_status](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762)

int reset\_status(const struct device \*dev, uint32\_t id, uint8\_t \*status)

Get the reset status.

[reset\_line\_toggle\_dt](group__reset__controller__interface.md#gaf3db170375c24999ea1b1954fb3ae184)

static int reset\_line\_toggle\_dt(const struct reset\_dt\_spec \*spec)

Reset the device from a reset\_dt\_spec.

**Definition** reset.h:312

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[reset\_dt\_spec](structreset__dt__spec.md)

Reset controller device configuration.

**Definition** reset.h:32

[reset\_dt\_spec::dev](structreset__dt__spec.md#ab5adeaabc9b0f78f856b1ce3ab8c3889)

const struct device \* dev

Reset controller device.

**Definition** reset.h:34

[reset\_dt\_spec::id](structreset__dt__spec.md#afdafd2a7b827e180dd6021de9c0dba7a)

uint32\_t id

Reset line.

**Definition** reset.h:36

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [reset.h](drivers_2reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
