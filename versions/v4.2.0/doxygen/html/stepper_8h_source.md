---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stepper_8h_source.html
original_path: doxygen/html/stepper_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper.h

[Go to the documentation of this file.](stepper_8h.md)

1/\*

2 \* SPDX-FileCopyrightText: Copyright (c) 2024 Carl Zeiss Meditec AG

3 \* SPDX-FileCopyrightText: Copyright (c) 2024 Jilay Sandeep Pandya

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_H\_

14

23

24#include <[zephyr/kernel.h](kernel_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26#include <[errno.h](errno_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 35](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) {

[ 37](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) [STEPPER\_MICRO\_STEP\_1](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) = 1,

[ 39](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) [STEPPER\_MICRO\_STEP\_2](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) = 2,

[ 41](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) [STEPPER\_MICRO\_STEP\_4](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) = 4,

[ 43](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) [STEPPER\_MICRO\_STEP\_8](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) = 8,

[ 45](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) [STEPPER\_MICRO\_STEP\_16](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) = 16,

[ 47](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) [STEPPER\_MICRO\_STEP\_32](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) = 32,

[ 49](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) [STEPPER\_MICRO\_STEP\_64](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) = 64,

[ 51](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) [STEPPER\_MICRO\_STEP\_128](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) = 128,

[ 53](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) [STEPPER\_MICRO\_STEP\_256](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) = 256,

54};

55

[ 60](group__stepper__interface.md#ga49df951f1b18bd399a609842514bdbc1)#define MICRO\_STEP\_RES\_INDEX(res) LOG2(res)

61

[ 62](group__stepper__interface.md#ga3196866d26d23c04313d802f2d8c61c1)#define VALID\_MICRO\_STEP\_RES(res) \

63 ((res) == STEPPER\_MICRO\_STEP\_1 || (res) == STEPPER\_MICRO\_STEP\_2 || \

64 (res) == STEPPER\_MICRO\_STEP\_4 || (res) == STEPPER\_MICRO\_STEP\_8 || \

65 (res) == STEPPER\_MICRO\_STEP\_16 || (res) == STEPPER\_MICRO\_STEP\_32 || \

66 (res) == STEPPER\_MICRO\_STEP\_64 || (res) == STEPPER\_MICRO\_STEP\_128 || \

67 (res) == STEPPER\_MICRO\_STEP\_256)

68

[ 72](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) {

[ 74](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) [STEPPER\_DIRECTION\_NEGATIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) = 0,

[ 76](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) [STEPPER\_DIRECTION\_POSITIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) = 1,

77};

78

[ 82](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239)enum [stepper\_run\_mode](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239) {

[ 84](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) [STEPPER\_RUN\_MODE\_HOLD](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) = 0,

[ 86](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) [STEPPER\_RUN\_MODE\_POSITION](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) = 1,

[ 88](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) [STEPPER\_RUN\_MODE\_VELOCITY](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) = 2,

89};

90

[ 94](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f)enum [stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f) {

[ 96](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) [STEPPER\_EVENT\_STEPS\_COMPLETED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) = 0,

[ 98](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) [STEPPER\_EVENT\_STALL\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) = 1,

[ 100](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) [STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) = 2,

[ 102](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) [STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) = 3,

[ 104](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5faf9c22bc201660b258c54473e929e665c) [STEPPER\_EVENT\_STOPPED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5faf9c22bc201660b258c54473e929e665c) = 4,

[ 106](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5faa1811857d120f56e0e7646457fc9e7d4) [STEPPER\_EVENT\_FAULT\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5faa1811857d120f56e0e7646457fc9e7d4) = 5,

107};

108

115

121typedef int (\*stepper\_enable\_t)(const struct [device](structdevice.md) \*dev);

122

128typedef int (\*stepper\_disable\_t)(const struct [device](structdevice.md) \*dev);

129

135typedef int (\*stepper\_set\_micro\_step\_res\_t)(const struct [device](structdevice.md) \*dev,

136 const enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution);

137

143typedef int (\*stepper\_get\_micro\_step\_res\_t)(const struct [device](structdevice.md) \*dev,

144 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution);

150typedef int (\*stepper\_set\_reference\_position\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

151

157typedef int (\*stepper\_get\_actual\_position\_t)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

158

162typedef void (\*stepper\_event\_callback\_t)(const struct [device](structdevice.md) \*dev, const enum [stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f) event,

163 void \*user\_data);

164

170typedef int (\*stepper\_set\_event\_callback\_t)(const struct [device](structdevice.md) \*dev,

171 stepper\_event\_callback\_t callback, void \*user\_data);

177typedef int (\*stepper\_set\_microstep\_interval\_t)(const struct [device](structdevice.md) \*dev,

178 const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) microstep\_interval\_ns);

184typedef int (\*stepper\_move\_by\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

185

191typedef int (\*stepper\_move\_to\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

192

198typedef int (\*stepper\_run\_t)(const struct [device](structdevice.md) \*dev, const enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction);

199

205typedef int (\*stepper\_stop\_t)(const struct [device](structdevice.md) \*dev);

206

212typedef int (\*stepper\_is\_moving\_t)(const struct [device](structdevice.md) \*dev, bool \*is\_moving);

213

217\_\_subsystem struct stepper\_driver\_api {

218 stepper\_enable\_t enable;

219 stepper\_disable\_t disable;

220 stepper\_set\_micro\_step\_res\_t set\_micro\_step\_res;

221 stepper\_get\_micro\_step\_res\_t get\_micro\_step\_res;

222 stepper\_set\_reference\_position\_t set\_reference\_position;

223 stepper\_get\_actual\_position\_t get\_actual\_position;

224 stepper\_set\_event\_callback\_t set\_event\_callback;

225 stepper\_set\_microstep\_interval\_t set\_microstep\_interval;

226 stepper\_move\_by\_t move\_by;

227 stepper\_move\_to\_t move\_to;

228 stepper\_run\_t run;

229 stepper\_stop\_t stop;

230 stepper\_is\_moving\_t is\_moving;

231};

232

236

[ 247](group__stepper__interface.md#ga3395b5f8b401d8175067edfb25c2e0e8)\_\_syscall int [stepper\_enable](group__stepper__interface.md#ga3395b5f8b401d8175067edfb25c2e0e8)(const struct [device](structdevice.md) \*dev);

248

249static inline int z\_impl\_stepper\_enable(const struct [device](structdevice.md) \*dev)

250{

251 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

252

253 return api->enable(dev);

254}

255

[ 269](group__stepper__interface.md#gab892a6b8d8fb34db0e682dd8f7de4218)\_\_syscall int [stepper\_disable](group__stepper__interface.md#gab892a6b8d8fb34db0e682dd8f7de4218)(const struct [device](structdevice.md) \*dev);

270

271static inline int z\_impl\_stepper\_disable(const struct [device](structdevice.md) \*dev)

272{

273 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

274

275 return api->disable(dev);

276}

277

[ 290](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)\_\_syscall int [stepper\_set\_micro\_step\_res](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)(const struct [device](structdevice.md) \*dev,

291 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution);

292

293static inline int z\_impl\_stepper\_set\_micro\_step\_res(const struct [device](structdevice.md) \*dev,

294 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution)

295{

296 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

297

298 if (api->set\_micro\_step\_res == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

299 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

300 }

301

302 if (![VALID\_MICRO\_STEP\_RES](group__stepper__interface.md#ga3196866d26d23c04313d802f2d8c61c1)(resolution)) {

303 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

304 }

305 return api->set\_micro\_step\_res(dev, resolution);

306}

307

[ 318](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e)\_\_syscall int [stepper\_get\_micro\_step\_res](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e)(const struct [device](structdevice.md) \*dev,

319 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution);

320

321static inline int z\_impl\_stepper\_get\_micro\_step\_res(const struct [device](structdevice.md) \*dev,

322 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution)

323{

324 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

325

326 if (api->get\_micro\_step\_res == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

327 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

328 }

329 return api->get\_micro\_step\_res(dev, resolution);

330}

331

[ 342](group__stepper__interface.md#ga472ba1e64876fcaf79ba95edd8261a36)\_\_syscall int [stepper\_set\_reference\_position](group__stepper__interface.md#ga472ba1e64876fcaf79ba95edd8261a36)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

343

344static inline int z\_impl\_stepper\_set\_reference\_position(const struct [device](structdevice.md) \*dev,

345 const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value)

346{

347 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

348

349 if (api->set\_reference\_position == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

350 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

351 }

352 return api->set\_reference\_position(dev, value);

353}

354

[ 365](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157)\_\_syscall int [stepper\_get\_actual\_position](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

366

367static inline int z\_impl\_stepper\_get\_actual\_position(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value)

368{

369 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

370

371 if (api->get\_actual\_position == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

372 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

373 }

374 return api->get\_actual\_position(dev, value);

375}

376

[ 388](group__stepper__interface.md#gad44cc67d4667114c933d82f527ad2b77)\_\_syscall int [stepper\_set\_event\_callback](group__stepper__interface.md#gad44cc67d4667114c933d82f527ad2b77)(const struct [device](structdevice.md) \*dev,

389 stepper\_event\_callback\_t callback, void \*user\_data);

390

391static inline int z\_impl\_stepper\_set\_event\_callback(const struct [device](structdevice.md) \*dev,

392 stepper\_event\_callback\_t callback,

393 void \*user\_data)

394{

395 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

396

397 if (api->set\_event\_callback == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

398 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

399 }

400 return api->set\_event\_callback(dev, callback, user\_data);

401}

402

[ 417](group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7)\_\_syscall int [stepper\_set\_microstep\_interval](group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7)(const struct [device](structdevice.md) \*dev,

418 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) microstep\_interval\_ns);

419

420static inline int z\_impl\_stepper\_set\_microstep\_interval(const struct [device](structdevice.md) \*dev,

421 const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) microstep\_interval\_ns)

422{

423 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

424

425 if (api->set\_microstep\_interval == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

426 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

427 }

428 return api->set\_microstep\_interval(dev, microstep\_interval\_ns);

429}

430

[ 443](group__stepper__interface.md#ga851c6b8f0cfe485095f345f33186535a)\_\_syscall int [stepper\_move\_by](group__stepper__interface.md#ga851c6b8f0cfe485095f345f33186535a)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

444

445static inline int z\_impl\_stepper\_move\_by(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps)

446{

447 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

448

449 return api->move\_by(dev, micro\_steps);

450}

451

[ 465](group__stepper__interface.md#ga7d12d3ff146698662090d8b761a57615)\_\_syscall int [stepper\_move\_to](group__stepper__interface.md#ga7d12d3ff146698662090d8b761a57615)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

466

467static inline int z\_impl\_stepper\_move\_to(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps)

468{

469 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

470

471 if (api->move\_to == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

472 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

473 }

474 return api->move\_to(dev, micro\_steps);

475}

476

[ 491](group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87)\_\_syscall int [stepper\_run](group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87)(const struct [device](structdevice.md) \*dev, enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction);

492

493static inline int z\_impl\_stepper\_run(const struct [device](structdevice.md) \*dev,

494 const enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction)

495{

496 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

497

498 if (api->run == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

499 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

500 }

501 return api->run(dev, direction);

502}

503

[ 514](group__stepper__interface.md#gaa049d39fe611a86904e7a60fc7005abd)\_\_syscall int [stepper\_stop](group__stepper__interface.md#gaa049d39fe611a86904e7a60fc7005abd)(const struct [device](structdevice.md) \*dev);

515

516static inline int z\_impl\_stepper\_stop(const struct [device](structdevice.md) \*dev)

517{

518 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

519

520 if (api->stop == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

521 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

522 }

523 return api->stop(dev);

524}

525

[ 536](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)\_\_syscall int [stepper\_is\_moving](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)(const struct [device](structdevice.md) \*dev, bool \*is\_moving);

537

538static inline int z\_impl\_stepper\_is\_moving(const struct [device](structdevice.md) \*dev, bool \*is\_moving)

539{

540 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

541

542 if (api->is\_moving == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

543 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

544 }

545 return api->is\_moving(dev, is\_moving);

546}

547

551

552#ifdef \_\_cplusplus

553}

554#endif

555

556#include <zephyr/syscalls/stepper.h>

557

558#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)

stepper\_direction

Stepper Motor direction options.

**Definition** stepper.h:72

[VALID\_MICRO\_STEP\_RES](group__stepper__interface.md#ga3196866d26d23c04313d802f2d8c61c1)

#define VALID\_MICRO\_STEP\_RES(res)

**Definition** stepper.h:62

[stepper\_enable](group__stepper__interface.md#ga3395b5f8b401d8175067edfb25c2e0e8)

int stepper\_enable(const struct device \*dev)

Enable stepper driver.

[stepper\_set\_reference\_position](group__stepper__interface.md#ga472ba1e64876fcaf79ba95edd8261a36)

int stepper\_set\_reference\_position(const struct device \*dev, int32\_t value)

Set the reference position of the stepper.

[stepper\_run\_mode](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239)

stepper\_run\_mode

Stepper Motor run mode options.

**Definition** stepper.h:82

[stepper\_set\_microstep\_interval](group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7)

int stepper\_set\_microstep\_interval(const struct device \*dev, uint64\_t microstep\_interval\_ns)

Set the time interval between steps in nanoseconds with immediate effect.

[stepper\_get\_actual\_position](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157)

int stepper\_get\_actual\_position(const struct device \*dev, int32\_t \*value)

Get the actual a.k.a reference position of the stepper.

[stepper\_get\_micro\_step\_res](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e)

int stepper\_get\_micro\_step\_res(const struct device \*dev, enum stepper\_micro\_step\_resolution \*resolution)

Get the micro-step resolution in stepper driver.

[stepper\_move\_to](group__stepper__interface.md#ga7d12d3ff146698662090d8b761a57615)

int stepper\_move\_to(const struct device \*dev, int32\_t micro\_steps)

Set the absolute target position of the stepper.

[stepper\_move\_by](group__stepper__interface.md#ga851c6b8f0cfe485095f345f33186535a)

int stepper\_move\_by(const struct device \*dev, int32\_t micro\_steps)

Set the micro-steps to be moved from the current position i.e.

[stepper\_run](group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87)

int stepper\_run(const struct device \*dev, enum stepper\_direction direction)

Run the stepper with a given step interval in a given direction.

[stepper\_stop](group__stepper__interface.md#gaa049d39fe611a86904e7a60fc7005abd)

int stepper\_stop(const struct device \*dev)

Stop the stepper.

[stepper\_is\_moving](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)

int stepper\_is\_moving(const struct device \*dev, bool \*is\_moving)

Check if the stepper is currently moving.

[stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f)

stepper\_event

Stepper Events.

**Definition** stepper.h:94

[stepper\_disable](group__stepper__interface.md#gab892a6b8d8fb34db0e682dd8f7de4218)

int stepper\_disable(const struct device \*dev)

Disable stepper driver.

[stepper\_set\_micro\_step\_res](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)

int stepper\_set\_micro\_step\_res(const struct device \*dev, enum stepper\_micro\_step\_resolution resolution)

Set the micro-step resolution in stepper driver.

[stepper\_set\_event\_callback](group__stepper__interface.md#gad44cc67d4667114c933d82f527ad2b77)

int stepper\_set\_event\_callback(const struct device \*dev, stepper\_event\_callback\_t callback, void \*user\_data)

Set the callback function to be called when a stepper event occurs.

[stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)

stepper\_micro\_step\_resolution

Stepper Motor micro-step resolution options.

**Definition** stepper.h:35

[STEPPER\_DIRECTION\_POSITIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157)

@ STEPPER\_DIRECTION\_POSITIVE

Positive direction.

**Definition** stepper.h:76

[STEPPER\_DIRECTION\_NEGATIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0)

@ STEPPER\_DIRECTION\_NEGATIVE

Negative direction.

**Definition** stepper.h:74

[STEPPER\_RUN\_MODE\_VELOCITY](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb)

@ STEPPER\_RUN\_MODE\_VELOCITY

Velocity Mode.

**Definition** stepper.h:88

[STEPPER\_RUN\_MODE\_HOLD](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c)

@ STEPPER\_RUN\_MODE\_HOLD

Hold Mode.

**Definition** stepper.h:84

[STEPPER\_RUN\_MODE\_POSITION](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc)

@ STEPPER\_RUN\_MODE\_POSITION

Position Mode.

**Definition** stepper.h:86

[STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0)

@ STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED

Left end switch status changes to pressed.

**Definition** stepper.h:100

[STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3)

@ STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED

Right end switch status changes to pressed.

**Definition** stepper.h:102

[STEPPER\_EVENT\_STEPS\_COMPLETED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4)

@ STEPPER\_EVENT\_STEPS\_COMPLETED

Steps set using move\_by or move\_to have been executed.

**Definition** stepper.h:96

[STEPPER\_EVENT\_STALL\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445)

@ STEPPER\_EVENT\_STALL\_DETECTED

Stall detected.

**Definition** stepper.h:98

[STEPPER\_EVENT\_FAULT\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5faa1811857d120f56e0e7646457fc9e7d4)

@ STEPPER\_EVENT\_FAULT\_DETECTED

Fault with the stepper controller detected.

**Definition** stepper.h:106

[STEPPER\_EVENT\_STOPPED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5faf9c22bc201660b258c54473e929e665c)

@ STEPPER\_EVENT\_STOPPED

Stepper has stopped.

**Definition** stepper.h:104

[STEPPER\_MICRO\_STEP\_64](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370)

@ STEPPER\_MICRO\_STEP\_64

64 micro-steps per full step

**Definition** stepper.h:49

[STEPPER\_MICRO\_STEP\_4](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0)

@ STEPPER\_MICRO\_STEP\_4

4 micro-steps per full step

**Definition** stepper.h:41

[STEPPER\_MICRO\_STEP\_1](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9)

@ STEPPER\_MICRO\_STEP\_1

Full step resolution.

**Definition** stepper.h:37

[STEPPER\_MICRO\_STEP\_2](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990)

@ STEPPER\_MICRO\_STEP\_2

2 micro-steps per full step

**Definition** stepper.h:39

[STEPPER\_MICRO\_STEP\_256](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f)

@ STEPPER\_MICRO\_STEP\_256

256 micro-steps per full step

**Definition** stepper.h:53

[STEPPER\_MICRO\_STEP\_8](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155)

@ STEPPER\_MICRO\_STEP\_8

8 micro-steps per full step

**Definition** stepper.h:43

[STEPPER\_MICRO\_STEP\_16](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8)

@ STEPPER\_MICRO\_STEP\_16

16 micro-steps per full step

**Definition** stepper.h:45

[STEPPER\_MICRO\_STEP\_32](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14)

@ STEPPER\_MICRO\_STEP\_32

32 micro-steps per full step

**Definition** stepper.h:47

[STEPPER\_MICRO\_STEP\_128](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43)

@ STEPPER\_MICRO\_STEP\_128

128 micro-steps per full step

**Definition** stepper.h:51

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[kernel.h](kernel_8h.md)

Public kernel APIs.

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper.h](stepper_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
