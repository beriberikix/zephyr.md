---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/edac_8h_source.html
original_path: doxygen/html/edac_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

24

[ 28](group__edac.md#ga3eb3da4d056d8e6167083301eb1276d6)enum [edac\_error\_type](group__edac.md#ga3eb3da4d056d8e6167083301eb1276d6) {

[ 30](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02) [EDAC\_ERROR\_TYPE\_DRAM\_COR](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 32](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f) [EDAC\_ERROR\_TYPE\_DRAM\_UC](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1)

33};

34

40

41typedef void (\*edac\_notify\_callback\_f)(const struct [device](structdevice.md) \*dev, void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

42

48\_\_subsystem struct edac\_driver\_api {

49 /\* Error Injection API is disabled by default \*/

50 int (\*inject\_set\_param1)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

51 int (\*inject\_get\_param1)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

52 int (\*inject\_set\_param2)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

53 int (\*inject\_get\_param2)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

54 int (\*inject\_set\_error\_type)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

55 int (\*inject\_get\_error\_type)(const struct device \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value);

56 int (\*inject\_error\_trigger)(const struct device \*dev);

57

58 /\* Error Logging API \*/

59 int (\*ecc\_error\_log\_get)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

60 int (\*ecc\_error\_log\_clear)(const struct device \*dev);

61 int (\*parity\_error\_log\_get)(const struct device \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

62 int (\*parity\_error\_log\_clear)(const struct device \*dev);

63

64 /\* Error stats API \*/

65 int (\*errors\_cor\_get)(const struct device \*dev);

66 int (\*errors\_uc\_get)(const struct device \*dev);

67

68 /\* Notification callback API \*/

69 int (\*notify\_cb\_set)(const struct device \*dev,

70 edac\_notify\_callback\_f cb);

71};

72

76

83

[ 95](group__edac.md#gad058d74c811e77b00730e25f2060cce5)static inline int [edac\_inject\_set\_param1](group__edac.md#gad058d74c811e77b00730e25f2060cce5)(const struct [device](structdevice.md) \*dev,

96 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value)

97{

98 const struct edac\_driver\_api \*api =

99 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

100

101 if (api->inject\_set\_param1 == NULL) {

102 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

103 }

104

105 return api->inject\_set\_param1(dev, value);

106}

107

[ 119](group__edac.md#ga9817f47eeaf532e3789816e412eb5077)static inline int [edac\_inject\_get\_param1](group__edac.md#ga9817f47eeaf532e3789816e412eb5077)(const struct [device](structdevice.md) \*dev,

120 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)

121{

122 const struct edac\_driver\_api \*api =

123 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

124

125 if (api->inject\_get\_param1 == NULL) {

126 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

127 }

128

129 return api->inject\_get\_param1(dev, value);

130

131}

132

[ 144](group__edac.md#ga9ed608245ba68aee6b235752a87a5c39)static inline int [edac\_inject\_set\_param2](group__edac.md#ga9ed608245ba68aee6b235752a87a5c39)(const struct [device](structdevice.md) \*dev,

145 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value)

146{

147 const struct edac\_driver\_api \*api =

148 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

149

150 if (api->inject\_set\_param2 == NULL) {

151 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

152 }

153

154 return api->inject\_set\_param2(dev, value);

155}

156

[ 166](group__edac.md#ga37e097d550f91072b890d6c2d4b215fa)static inline int [edac\_inject\_get\_param2](group__edac.md#ga37e097d550f91072b890d6c2d4b215fa)(const struct [device](structdevice.md) \*dev,

167 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)

168{

169 const struct edac\_driver\_api \*api =

170 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

171

172 if (api->inject\_get\_param2 == NULL) {

173 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

174 }

175

176 return api->inject\_get\_param2(dev, value);

177}

178

[ 190](group__edac.md#ga2b0ea084501faf52aeec5af33a1ca97b)static inline int [edac\_inject\_set\_error\_type](group__edac.md#ga2b0ea084501faf52aeec5af33a1ca97b)(const struct [device](structdevice.md) \*dev,

191 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) error\_type)

192{

193 const struct edac\_driver\_api \*api =

194 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

195

196 if (api->inject\_set\_error\_type == NULL) {

197 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

198 }

199

200 return api->inject\_set\_error\_type(dev, error\_type);

201}

202

[ 214](group__edac.md#gafb0cbc5082e88250a1e5955dd7d1770c)static inline int [edac\_inject\_get\_error\_type](group__edac.md#gafb0cbc5082e88250a1e5955dd7d1770c)(const struct [device](structdevice.md) \*dev,

215 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*error\_type)

216{

217 const struct edac\_driver\_api \*api =

218 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

219

220 if (api->inject\_get\_error\_type == NULL) {

221 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

222 }

223

224 return api->inject\_get\_error\_type(dev, error\_type);

225}

226

[ 237](group__edac.md#gaf02830c2e621e73a7c4add38a92f6d7c)static inline int [edac\_inject\_error\_trigger](group__edac.md#gaf02830c2e621e73a7c4add38a92f6d7c)(const struct [device](structdevice.md) \*dev)

238{

239 const struct edac\_driver\_api \*api =

240 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

241

242 if (api->inject\_error\_trigger == NULL) {

243 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

244 }

245

246 return api->inject\_error\_trigger(dev);

247}

248 /\* End of EDAC Optional Interfaces \*/

250

257

[ 269](group__edac.md#ga905539bb96ff8c9f6f6a9fde6b3928e2)static inline int [edac\_ecc\_error\_log\_get](group__edac.md#ga905539bb96ff8c9f6f6a9fde6b3928e2)(const struct [device](structdevice.md) \*dev,

270 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)

271{

272 const struct edac\_driver\_api \*api =

273 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

274

275 if (api->ecc\_error\_log\_get == NULL) {

276 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

277 }

278

279 return api->ecc\_error\_log\_get(dev, value);

280}

281

[ 292](group__edac.md#gaa8c798b60b3b99ae6b8f8358253d1385)static inline int [edac\_ecc\_error\_log\_clear](group__edac.md#gaa8c798b60b3b99ae6b8f8358253d1385)(const struct [device](structdevice.md) \*dev)

293{

294 const struct edac\_driver\_api \*api =

295 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

296

297 if (api->ecc\_error\_log\_clear == NULL) {

298 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

299 }

300

301 return api->ecc\_error\_log\_clear(dev);

302}

303

[ 315](group__edac.md#gaa6cba09e19de241ed045387c85cc3f1c)static inline int [edac\_parity\_error\_log\_get](group__edac.md#gaa6cba09e19de241ed045387c85cc3f1c)(const struct [device](structdevice.md) \*dev,

316 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value)

317{

318 const struct edac\_driver\_api \*api =

319 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

320

321 if (api->parity\_error\_log\_get == NULL) {

322 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

323 }

324

325 return api->parity\_error\_log\_get(dev, value);

326}

327

[ 338](group__edac.md#gab60aa37ba86e2038fe979481cc6134c2)static inline int [edac\_parity\_error\_log\_clear](group__edac.md#gab60aa37ba86e2038fe979481cc6134c2)(const struct [device](structdevice.md) \*dev)

339{

340 const struct edac\_driver\_api \*api =

341 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

342

343 if (api->parity\_error\_log\_clear == NULL) {

344 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

345 }

346

347 return api->parity\_error\_log\_clear(dev);

348}

349

[ 358](group__edac.md#gaea2915b6c3c4eef2c94c6f60e788dcfe)static inline int [edac\_errors\_cor\_get](group__edac.md#gaea2915b6c3c4eef2c94c6f60e788dcfe)(const struct [device](structdevice.md) \*dev)

359{

360 const struct edac\_driver\_api \*api =

361 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

362

363 if (api->errors\_cor\_get == NULL) {

364 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

365 }

366

367 return api->errors\_cor\_get(dev);

368}

369

[ 378](group__edac.md#gaec79969648e56e98031d46abe73c2b82)static inline int [edac\_errors\_uc\_get](group__edac.md#gaec79969648e56e98031d46abe73c2b82)(const struct [device](structdevice.md) \*dev)

379{

380 const struct edac\_driver\_api \*api =

381 (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

382

383 if (api->errors\_uc\_get == NULL) {

384 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

385 }

386

387 return api->errors\_uc\_get(dev);

388}

389

[ 401](group__edac.md#ga2def500f72a06271d9a10243bfdf6527)static inline int [edac\_notify\_callback\_set](group__edac.md#ga2def500f72a06271d9a10243bfdf6527)(const struct [device](structdevice.md) \*dev,

402 edac\_notify\_callback\_f cb)

403{

404 const struct edac\_driver\_api \*api = (const struct edac\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

405

406 if (api->notify\_cb\_set == NULL) {

407 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

408 }

409

410 return api->notify\_cb\_set(dev, cb);

411}

412

413 /\* End of EDAC Mandatory Interfaces \*/

415 /\* End of EDAC API \*/

417

418#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_EDAC\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[edac\_inject\_set\_error\_type](group__edac.md#ga2b0ea084501faf52aeec5af33a1ca97b)

static int edac\_inject\_set\_error\_type(const struct device \*dev, uint32\_t error\_type)

Set error type value.

**Definition** edac.h:190

[edac\_notify\_callback\_set](group__edac.md#ga2def500f72a06271d9a10243bfdf6527)

static int edac\_notify\_callback\_set(const struct device \*dev, edac\_notify\_callback\_f cb)

Register callback function for memory error exception.

**Definition** edac.h:401

[edac\_inject\_get\_param2](group__edac.md#ga37e097d550f91072b890d6c2d4b215fa)

static int edac\_inject\_get\_param2(const struct device \*dev, uint64\_t \*value)

Get injection parameter param2.

**Definition** edac.h:166

[edac\_error\_type](group__edac.md#ga3eb3da4d056d8e6167083301eb1276d6)

edac\_error\_type

EDAC error type.

**Definition** edac.h:28

[edac\_ecc\_error\_log\_get](group__edac.md#ga905539bb96ff8c9f6f6a9fde6b3928e2)

static int edac\_ecc\_error\_log\_get(const struct device \*dev, uint64\_t \*value)

Get ECC Error Log.

**Definition** edac.h:269

[edac\_inject\_get\_param1](group__edac.md#ga9817f47eeaf532e3789816e412eb5077)

static int edac\_inject\_get\_param1(const struct device \*dev, uint64\_t \*value)

Get injection parameter param1.

**Definition** edac.h:119

[edac\_inject\_set\_param2](group__edac.md#ga9ed608245ba68aee6b235752a87a5c39)

static int edac\_inject\_set\_param2(const struct device \*dev, uint64\_t value)

Set injection parameter param2.

**Definition** edac.h:144

[edac\_parity\_error\_log\_get](group__edac.md#gaa6cba09e19de241ed045387c85cc3f1c)

static int edac\_parity\_error\_log\_get(const struct device \*dev, uint64\_t \*value)

Get Parity Error Log.

**Definition** edac.h:315

[edac\_ecc\_error\_log\_clear](group__edac.md#gaa8c798b60b3b99ae6b8f8358253d1385)

static int edac\_ecc\_error\_log\_clear(const struct device \*dev)

Clear ECC Error Log.

**Definition** edac.h:292

[edac\_parity\_error\_log\_clear](group__edac.md#gab60aa37ba86e2038fe979481cc6134c2)

static int edac\_parity\_error\_log\_clear(const struct device \*dev)

Clear Parity Error Log.

**Definition** edac.h:338

[edac\_inject\_set\_param1](group__edac.md#gad058d74c811e77b00730e25f2060cce5)

static int edac\_inject\_set\_param1(const struct device \*dev, uint64\_t value)

Set injection parameter param1.

**Definition** edac.h:95

[edac\_errors\_cor\_get](group__edac.md#gaea2915b6c3c4eef2c94c6f60e788dcfe)

static int edac\_errors\_cor\_get(const struct device \*dev)

Get number of correctable errors.

**Definition** edac.h:358

[edac\_errors\_uc\_get](group__edac.md#gaec79969648e56e98031d46abe73c2b82)

static int edac\_errors\_uc\_get(const struct device \*dev)

Get number of uncorrectable errors.

**Definition** edac.h:378

[edac\_inject\_error\_trigger](group__edac.md#gaf02830c2e621e73a7c4add38a92f6d7c)

static int edac\_inject\_error\_trigger(const struct device \*dev)

Set injection control.

**Definition** edac.h:237

[edac\_inject\_get\_error\_type](group__edac.md#gafb0cbc5082e88250a1e5955dd7d1770c)

static int edac\_inject\_get\_error\_type(const struct device \*dev, uint32\_t \*error\_type)

Get error type value.

**Definition** edac.h:214

[EDAC\_ERROR\_TYPE\_DRAM\_UC](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f)

@ EDAC\_ERROR\_TYPE\_DRAM\_UC

Uncorrectable error type.

**Definition** edac.h:32

[EDAC\_ERROR\_TYPE\_DRAM\_COR](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02)

@ EDAC\_ERROR\_TYPE\_DRAM\_COR

Correctable error type.

**Definition** edac.h:30

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [edac.h](edac_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
