---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/edac_8h_source.html
original_path: doxygen/html/edac_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

edac.h

[Go to the documentation of this file.](edac_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_EDAC\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_EDAC\_H\_

14

15#include <[errno.h](errno_8h.md)>

16

17#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

18

26

[ 30](group__edac.md#ga3eb3da4d056d8e6167083301eb1276d6)enum [edac\_error\_type](group__edac.md#ga3eb3da4d056d8e6167083301eb1276d6) {

[ 32](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02) [EDAC\_ERROR\_TYPE\_DRAM\_COR](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 34](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f) [EDAC\_ERROR\_TYPE\_DRAM\_UC](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1)

35};

36

42

43typedef void (\*edac\_notify\_callback\_f)(const struct [device](structdevice.md) \*dev, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

44

50\_\_subsystem struct edac\_driver\_api {

51 /\* Error Injection API is disabled by default \*/

52 int (\*inject\_set\_param1)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

53 int (\*inject\_get\_param1)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

54 int (\*inject\_set\_param2)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

55 int (\*inject\_get\_param2)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

56 int (\*inject\_set\_error\_type)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

57 int (\*inject\_get\_error\_type)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value);

58 int (\*inject\_error\_trigger)(const struct device \*dev);

59

60 /\* Error Logging API \*/

61 int (\*ecc\_error\_log\_get)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

62 int (\*ecc\_error\_log\_clear)(const struct device \*dev);

63 int (\*parity\_error\_log\_get)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

64 int (\*parity\_error\_log\_clear)(const struct device \*dev);

65

66 /\* Error stats API \*/

67 int (\*errors\_cor\_get)(const struct device \*dev);

68 int (\*errors\_uc\_get)(const struct device \*dev);

69

70 /\* Notification callback API \*/

71 int (\*notify\_cb\_set)(const struct device \*dev,

72 edac\_notify\_callback\_f cb);

73};

74

78

85

[ 97](group__edac.md#gad058d74c811e77b00730e25f2060cce5)static inline int [edac\_inject\_set\_param1](group__edac.md#gad058d74c811e77b00730e25f2060cce5)(const struct [device](structdevice.md) \*dev,

98 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value)

99{

100 const struct edac\_driver\_api \*api =

101 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

102

103 if (api->inject\_set\_param1 == NULL) {

104 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

105 }

106

107 return api->inject\_set\_param1(dev, value);

108}

109

[ 121](group__edac.md#ga9817f47eeaf532e3789816e412eb5077)static inline int [edac\_inject\_get\_param1](group__edac.md#ga9817f47eeaf532e3789816e412eb5077)(const struct [device](structdevice.md) \*dev,

122 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)

123{

124 const struct edac\_driver\_api \*api =

125 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

126

127 if (api->inject\_get\_param1 == NULL) {

128 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

129 }

130

131 return api->inject\_get\_param1(dev, value);

132

133}

134

[ 146](group__edac.md#ga9ed608245ba68aee6b235752a87a5c39)static inline int [edac\_inject\_set\_param2](group__edac.md#ga9ed608245ba68aee6b235752a87a5c39)(const struct [device](structdevice.md) \*dev,

147 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value)

148{

149 const struct edac\_driver\_api \*api =

150 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

151

152 if (api->inject\_set\_param2 == NULL) {

153 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

154 }

155

156 return api->inject\_set\_param2(dev, value);

157}

158

[ 168](group__edac.md#ga37e097d550f91072b890d6c2d4b215fa)static inline int [edac\_inject\_get\_param2](group__edac.md#ga37e097d550f91072b890d6c2d4b215fa)(const struct [device](structdevice.md) \*dev,

169 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)

170{

171 const struct edac\_driver\_api \*api =

172 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

173

174 if (api->inject\_get\_param2 == NULL) {

175 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

176 }

177

178 return api->inject\_get\_param2(dev, value);

179}

180

[ 192](group__edac.md#ga2b0ea084501faf52aeec5af33a1ca97b)static inline int [edac\_inject\_set\_error\_type](group__edac.md#ga2b0ea084501faf52aeec5af33a1ca97b)(const struct [device](structdevice.md) \*dev,

193 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) error\_type)

194{

195 const struct edac\_driver\_api \*api =

196 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

197

198 if (api->inject\_set\_error\_type == NULL) {

199 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

200 }

201

202 return api->inject\_set\_error\_type(dev, error\_type);

203}

204

[ 216](group__edac.md#gafb0cbc5082e88250a1e5955dd7d1770c)static inline int [edac\_inject\_get\_error\_type](group__edac.md#gafb0cbc5082e88250a1e5955dd7d1770c)(const struct [device](structdevice.md) \*dev,

217 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*error\_type)

218{

219 const struct edac\_driver\_api \*api =

220 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

221

222 if (api->inject\_get\_error\_type == NULL) {

223 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

224 }

225

226 return api->inject\_get\_error\_type(dev, error\_type);

227}

228

[ 239](group__edac.md#gaf02830c2e621e73a7c4add38a92f6d7c)static inline int [edac\_inject\_error\_trigger](group__edac.md#gaf02830c2e621e73a7c4add38a92f6d7c)(const struct [device](structdevice.md) \*dev)

240{

241 const struct edac\_driver\_api \*api =

242 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

243

244 if (api->inject\_error\_trigger == NULL) {

245 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

246 }

247

248 return api->inject\_error\_trigger(dev);

249}

250 /\* End of EDAC Optional Interfaces \*/

252

259

[ 271](group__edac.md#ga905539bb96ff8c9f6f6a9fde6b3928e2)static inline int [edac\_ecc\_error\_log\_get](group__edac.md#ga905539bb96ff8c9f6f6a9fde6b3928e2)(const struct [device](structdevice.md) \*dev,

272 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)

273{

274 const struct edac\_driver\_api \*api =

275 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

276

277 if (api->ecc\_error\_log\_get == NULL) {

278 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

279 }

280

281 return api->ecc\_error\_log\_get(dev, value);

282}

283

[ 294](group__edac.md#gaa8c798b60b3b99ae6b8f8358253d1385)static inline int [edac\_ecc\_error\_log\_clear](group__edac.md#gaa8c798b60b3b99ae6b8f8358253d1385)(const struct [device](structdevice.md) \*dev)

295{

296 const struct edac\_driver\_api \*api =

297 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

298

299 if (api->ecc\_error\_log\_clear == NULL) {

300 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

301 }

302

303 return api->ecc\_error\_log\_clear(dev);

304}

305

[ 317](group__edac.md#gaa6cba09e19de241ed045387c85cc3f1c)static inline int [edac\_parity\_error\_log\_get](group__edac.md#gaa6cba09e19de241ed045387c85cc3f1c)(const struct [device](structdevice.md) \*dev,

318 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)

319{

320 const struct edac\_driver\_api \*api =

321 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

322

323 if (api->parity\_error\_log\_get == NULL) {

324 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

325 }

326

327 return api->parity\_error\_log\_get(dev, value);

328}

329

[ 340](group__edac.md#gab60aa37ba86e2038fe979481cc6134c2)static inline int [edac\_parity\_error\_log\_clear](group__edac.md#gab60aa37ba86e2038fe979481cc6134c2)(const struct [device](structdevice.md) \*dev)

341{

342 const struct edac\_driver\_api \*api =

343 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

344

345 if (api->parity\_error\_log\_clear == NULL) {

346 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

347 }

348

349 return api->parity\_error\_log\_clear(dev);

350}

351

[ 360](group__edac.md#gaea2915b6c3c4eef2c94c6f60e788dcfe)static inline int [edac\_errors\_cor\_get](group__edac.md#gaea2915b6c3c4eef2c94c6f60e788dcfe)(const struct [device](structdevice.md) \*dev)

361{

362 const struct edac\_driver\_api \*api =

363 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

364

365 if (api->errors\_cor\_get == NULL) {

366 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

367 }

368

369 return api->errors\_cor\_get(dev);

370}

371

[ 380](group__edac.md#gaec79969648e56e98031d46abe73c2b82)static inline int [edac\_errors\_uc\_get](group__edac.md#gaec79969648e56e98031d46abe73c2b82)(const struct [device](structdevice.md) \*dev)

381{

382 const struct edac\_driver\_api \*api =

383 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

384

385 if (api->errors\_uc\_get == NULL) {

386 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

387 }

388

389 return api->errors\_uc\_get(dev);

390}

391

[ 403](group__edac.md#ga2def500f72a06271d9a10243bfdf6527)static inline int [edac\_notify\_callback\_set](group__edac.md#ga2def500f72a06271d9a10243bfdf6527)(const struct [device](structdevice.md) \*dev,

404 edac\_notify\_callback\_f cb)

405{

406 const struct edac\_driver\_api \*api = (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

407

408 if (api->notify\_cb\_set == NULL) {

409 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

410 }

411

412 return api->notify\_cb\_set(dev, cb);

413}

414

415 /\* End of EDAC Mandatory Interfaces \*/

417 /\* End of EDAC API \*/

419

420#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_EDAC\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[edac\_inject\_set\_error\_type](group__edac.md#ga2b0ea084501faf52aeec5af33a1ca97b)

static int edac\_inject\_set\_error\_type(const struct device \*dev, uint32\_t error\_type)

Set error type value.

**Definition** edac.h:192

[edac\_notify\_callback\_set](group__edac.md#ga2def500f72a06271d9a10243bfdf6527)

static int edac\_notify\_callback\_set(const struct device \*dev, edac\_notify\_callback\_f cb)

Register callback function for memory error exception.

**Definition** edac.h:403

[edac\_inject\_get\_param2](group__edac.md#ga37e097d550f91072b890d6c2d4b215fa)

static int edac\_inject\_get\_param2(const struct device \*dev, uint64\_t \*value)

Get injection parameter param2.

**Definition** edac.h:168

[edac\_error\_type](group__edac.md#ga3eb3da4d056d8e6167083301eb1276d6)

edac\_error\_type

EDAC error type.

**Definition** edac.h:30

[edac\_ecc\_error\_log\_get](group__edac.md#ga905539bb96ff8c9f6f6a9fde6b3928e2)

static int edac\_ecc\_error\_log\_get(const struct device \*dev, uint64\_t \*value)

Get ECC Error Log.

**Definition** edac.h:271

[edac\_inject\_get\_param1](group__edac.md#ga9817f47eeaf532e3789816e412eb5077)

static int edac\_inject\_get\_param1(const struct device \*dev, uint64\_t \*value)

Get injection parameter param1.

**Definition** edac.h:121

[edac\_inject\_set\_param2](group__edac.md#ga9ed608245ba68aee6b235752a87a5c39)

static int edac\_inject\_set\_param2(const struct device \*dev, uint64\_t value)

Set injection parameter param2.

**Definition** edac.h:146

[edac\_parity\_error\_log\_get](group__edac.md#gaa6cba09e19de241ed045387c85cc3f1c)

static int edac\_parity\_error\_log\_get(const struct device \*dev, uint64\_t \*value)

Get Parity Error Log.

**Definition** edac.h:317

[edac\_ecc\_error\_log\_clear](group__edac.md#gaa8c798b60b3b99ae6b8f8358253d1385)

static int edac\_ecc\_error\_log\_clear(const struct device \*dev)

Clear ECC Error Log.

**Definition** edac.h:294

[edac\_parity\_error\_log\_clear](group__edac.md#gab60aa37ba86e2038fe979481cc6134c2)

static int edac\_parity\_error\_log\_clear(const struct device \*dev)

Clear Parity Error Log.

**Definition** edac.h:340

[edac\_inject\_set\_param1](group__edac.md#gad058d74c811e77b00730e25f2060cce5)

static int edac\_inject\_set\_param1(const struct device \*dev, uint64\_t value)

Set injection parameter param1.

**Definition** edac.h:97

[edac\_errors\_cor\_get](group__edac.md#gaea2915b6c3c4eef2c94c6f60e788dcfe)

static int edac\_errors\_cor\_get(const struct device \*dev)

Get number of correctable errors.

**Definition** edac.h:360

[edac\_errors\_uc\_get](group__edac.md#gaec79969648e56e98031d46abe73c2b82)

static int edac\_errors\_uc\_get(const struct device \*dev)

Get number of uncorrectable errors.

**Definition** edac.h:380

[edac\_inject\_error\_trigger](group__edac.md#gaf02830c2e621e73a7c4add38a92f6d7c)

static int edac\_inject\_error\_trigger(const struct device \*dev)

Set injection control.

**Definition** edac.h:239

[edac\_inject\_get\_error\_type](group__edac.md#gafb0cbc5082e88250a1e5955dd7d1770c)

static int edac\_inject\_get\_error\_type(const struct device \*dev, uint32\_t \*error\_type)

Get error type value.

**Definition** edac.h:216

[EDAC\_ERROR\_TYPE\_DRAM\_UC](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f)

@ EDAC\_ERROR\_TYPE\_DRAM\_UC

Uncorrectable error type.

**Definition** edac.h:34

[EDAC\_ERROR\_TYPE\_DRAM\_COR](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02)

@ EDAC\_ERROR\_TYPE\_DRAM\_COR

Correctable error type.

**Definition** edac.h:32

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [edac.h](edac_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
