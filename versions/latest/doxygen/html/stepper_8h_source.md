---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stepper_8h_source.html
original_path: doxygen/html/stepper_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 36](group__stepper__interface.md#ga49df951f1b18bd399a609842514bdbc1)#define MICRO\_STEP\_RES\_INDEX(res) LOG2(res)

37

[ 41](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) {

[ 43](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) [STEPPER\_MICRO\_STEP\_1](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) = 1,

[ 45](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) [STEPPER\_MICRO\_STEP\_2](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) = 2,

[ 47](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) [STEPPER\_MICRO\_STEP\_4](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) = 4,

[ 49](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) [STEPPER\_MICRO\_STEP\_8](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) = 8,

[ 51](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) [STEPPER\_MICRO\_STEP\_16](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) = 16,

[ 53](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) [STEPPER\_MICRO\_STEP\_32](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) = 32,

[ 55](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) [STEPPER\_MICRO\_STEP\_64](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) = 64,

[ 57](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) [STEPPER\_MICRO\_STEP\_128](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) = 128,

[ 59](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) [STEPPER\_MICRO\_STEP\_256](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) = 256,

60};

61

[ 65](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) {

[ 67](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) [STEPPER\_DIRECTION\_NEGATIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) = 0,

[ 69](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) [STEPPER\_DIRECTION\_POSITIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) = 1,

70};

71

[ 75](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239)enum [stepper\_run\_mode](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239) {

[ 77](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) [STEPPER\_RUN\_MODE\_HOLD](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) = 0,

[ 79](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) [STEPPER\_RUN\_MODE\_POSITION](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) = 1,

[ 81](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) [STEPPER\_RUN\_MODE\_VELOCITY](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) = 2,

82};

83

[ 87](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f)enum [stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f) {

[ 89](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) [STEPPER\_EVENT\_STEPS\_COMPLETED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) = 0,

[ 91](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) [STEPPER\_EVENT\_STALL\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) = 1,

[ 93](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) [STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) = 2,

[ 95](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) [STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) = 3,

96};

97

104

110typedef int (\*stepper\_enable\_t)(const struct [device](structdevice.md) \*dev, const bool enable);

111

117typedef int (\*stepper\_set\_micro\_step\_res\_t)(const struct [device](structdevice.md) \*dev,

118 const enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution);

119

125typedef int (\*stepper\_get\_micro\_step\_res\_t)(const struct [device](structdevice.md) \*dev,

126 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution);

132typedef int (\*stepper\_set\_reference\_position\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

133

139typedef int (\*stepper\_get\_actual\_position\_t)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

140

144typedef void (\*stepper\_event\_callback\_t)(const struct [device](structdevice.md) \*dev, const enum [stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f) event,

145 void \*user\_data);

146

152typedef int (\*stepper\_set\_event\_callback\_t)(const struct [device](structdevice.md) \*dev,

153 stepper\_event\_callback\_t callback, void \*user\_data);

159typedef int (\*stepper\_set\_microstep\_interval\_t)(const struct [device](structdevice.md) \*dev,

160 const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) microstep\_interval\_ns);

166typedef int (\*stepper\_move\_by\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

167

173typedef int (\*stepper\_move\_to\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

174

180typedef int (\*stepper\_run\_t)(const struct [device](structdevice.md) \*dev, const enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction);

181

187typedef int (\*stepper\_is\_moving\_t)(const struct [device](structdevice.md) \*dev, bool \*is\_moving);

188

192\_\_subsystem struct stepper\_driver\_api {

193 stepper\_enable\_t enable;

194 stepper\_set\_micro\_step\_res\_t set\_micro\_step\_res;

195 stepper\_get\_micro\_step\_res\_t get\_micro\_step\_res;

196 stepper\_set\_reference\_position\_t set\_reference\_position;

197 stepper\_get\_actual\_position\_t get\_actual\_position;

198 stepper\_set\_event\_callback\_t set\_event\_callback;

199 stepper\_set\_microstep\_interval\_t set\_microstep\_interval;

200 stepper\_move\_by\_t move\_by;

201 stepper\_move\_to\_t move\_to;

202 stepper\_run\_t run;

203 stepper\_is\_moving\_t is\_moving;

204};

205

209

[ 222](group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450)\_\_syscall int [stepper\_enable](group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450)(const struct [device](structdevice.md) \*dev, const bool enable);

223

224static inline int z\_impl\_stepper\_enable(const struct [device](structdevice.md) \*dev, const bool enable)

225{

226 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

227

228 return api->enable(dev, enable);

229}

230

[ 242](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)\_\_syscall int [stepper\_set\_micro\_step\_res](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)(const struct [device](structdevice.md) \*dev,

243 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution);

244

245static inline int z\_impl\_stepper\_set\_micro\_step\_res(const struct [device](structdevice.md) \*dev,

246 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution)

247{

248 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

249

250 if (api->set\_micro\_step\_res == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

251 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

252 }

253 return api->set\_micro\_step\_res(dev, resolution);

254}

255

[ 266](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e)\_\_syscall int [stepper\_get\_micro\_step\_res](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e)(const struct [device](structdevice.md) \*dev,

267 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution);

268

269static inline int z\_impl\_stepper\_get\_micro\_step\_res(const struct [device](structdevice.md) \*dev,

270 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution)

271{

272 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

273

274 if (api->get\_micro\_step\_res == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

275 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

276 }

277 return api->get\_micro\_step\_res(dev, resolution);

278}

279

[ 290](group__stepper__interface.md#ga472ba1e64876fcaf79ba95edd8261a36)\_\_syscall int [stepper\_set\_reference\_position](group__stepper__interface.md#ga472ba1e64876fcaf79ba95edd8261a36)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

291

292static inline int z\_impl\_stepper\_set\_reference\_position(const struct [device](structdevice.md) \*dev,

293 const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value)

294{

295 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

296

297 if (api->set\_reference\_position == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

298 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

299 }

300 return api->set\_reference\_position(dev, value);

301}

302

[ 313](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157)\_\_syscall int [stepper\_get\_actual\_position](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

314

315static inline int z\_impl\_stepper\_get\_actual\_position(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value)

316{

317 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

318

319 if (api->get\_actual\_position == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

320 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

321 }

322 return api->get\_actual\_position(dev, value);

323}

324

[ 336](group__stepper__interface.md#gad44cc67d4667114c933d82f527ad2b77)\_\_syscall int [stepper\_set\_event\_callback](group__stepper__interface.md#gad44cc67d4667114c933d82f527ad2b77)(const struct [device](structdevice.md) \*dev,

337 stepper\_event\_callback\_t callback, void \*user\_data);

338

339static inline int z\_impl\_stepper\_set\_event\_callback(const struct [device](structdevice.md) \*dev,

340 stepper\_event\_callback\_t callback,

341 void \*user\_data)

342{

343 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

344

345 if (api->set\_event\_callback == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

346 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

347 }

348 return api->set\_event\_callback(dev, callback, user\_data);

349}

350

[ 365](group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7)\_\_syscall int [stepper\_set\_microstep\_interval](group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7)(const struct [device](structdevice.md) \*dev,

366 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) microstep\_interval\_ns);

367

368static inline int z\_impl\_stepper\_set\_microstep\_interval(const struct [device](structdevice.md) \*dev,

369 const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) microstep\_interval\_ns)

370{

371 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

372

373 if (api->set\_microstep\_interval == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

374 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

375 }

376 return api->set\_microstep\_interval(dev, microstep\_interval\_ns);

377}

378

[ 392](group__stepper__interface.md#ga851c6b8f0cfe485095f345f33186535a)\_\_syscall int [stepper\_move\_by](group__stepper__interface.md#ga851c6b8f0cfe485095f345f33186535a)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

393

394static inline int z\_impl\_stepper\_move\_by(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps)

395{

396 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

397

398 return api->move\_by(dev, micro\_steps);

399}

400

[ 415](group__stepper__interface.md#ga7d12d3ff146698662090d8b761a57615)\_\_syscall int [stepper\_move\_to](group__stepper__interface.md#ga7d12d3ff146698662090d8b761a57615)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

416

417static inline int z\_impl\_stepper\_move\_to(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps)

418{

419 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

420

421 if (api->move\_to == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

422 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

423 }

424 return api->move\_to(dev, micro\_steps);

425}

426

[ 442](group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87)\_\_syscall int [stepper\_run](group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87)(const struct [device](structdevice.md) \*dev, enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction);

443

444static inline int z\_impl\_stepper\_run(const struct [device](structdevice.md) \*dev,

445 const enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction)

446{

447 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

448

449 if (api->run == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

450 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

451 }

452 return api->run(dev, direction);

453}

454

[ 465](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)\_\_syscall int [stepper\_is\_moving](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)(const struct [device](structdevice.md) \*dev, bool \*is\_moving);

466

467static inline int z\_impl\_stepper\_is\_moving(const struct [device](structdevice.md) \*dev, bool \*is\_moving)

468{

469 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

470

471 if (api->is\_moving == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

472 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

473 }

474 return api->is\_moving(dev, is\_moving);

475}

476

480

481#ifdef \_\_cplusplus

482}

483#endif

484

485#include <zephyr/syscalls/stepper.h>

486

487#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)

stepper\_direction

Stepper Motor direction options.

**Definition** stepper.h:65

[stepper\_enable](group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450)

int stepper\_enable(const struct device \*dev, const bool enable)

Enable or disable stepper driver.

[stepper\_set\_reference\_position](group__stepper__interface.md#ga472ba1e64876fcaf79ba95edd8261a36)

int stepper\_set\_reference\_position(const struct device \*dev, int32\_t value)

Set the reference position of the stepper.

[stepper\_run\_mode](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239)

stepper\_run\_mode

Stepper Motor run mode options.

**Definition** stepper.h:75

[stepper\_set\_microstep\_interval](group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7)

int stepper\_set\_microstep\_interval(const struct device \*dev, uint64\_t microstep\_interval\_ns)

Set the time interval between steps in nanoseconds.

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

[stepper\_is\_moving](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)

int stepper\_is\_moving(const struct device \*dev, bool \*is\_moving)

Check if the stepper is currently moving.

[stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f)

stepper\_event

Stepper Events.

**Definition** stepper.h:87

[stepper\_set\_micro\_step\_res](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)

int stepper\_set\_micro\_step\_res(const struct device \*dev, enum stepper\_micro\_step\_resolution resolution)

Set the micro-step resolution in stepper driver.

[stepper\_set\_event\_callback](group__stepper__interface.md#gad44cc67d4667114c933d82f527ad2b77)

int stepper\_set\_event\_callback(const struct device \*dev, stepper\_event\_callback\_t callback, void \*user\_data)

Set the callback function to be called when a stepper event occurs.

[stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)

stepper\_micro\_step\_resolution

Stepper Motor micro-step resolution options.

**Definition** stepper.h:41

[STEPPER\_DIRECTION\_POSITIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157)

@ STEPPER\_DIRECTION\_POSITIVE

Positive direction.

**Definition** stepper.h:69

[STEPPER\_DIRECTION\_NEGATIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0)

@ STEPPER\_DIRECTION\_NEGATIVE

Negative direction.

**Definition** stepper.h:67

[STEPPER\_RUN\_MODE\_VELOCITY](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb)

@ STEPPER\_RUN\_MODE\_VELOCITY

Velocity Mode.

**Definition** stepper.h:81

[STEPPER\_RUN\_MODE\_HOLD](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c)

@ STEPPER\_RUN\_MODE\_HOLD

Hold Mode.

**Definition** stepper.h:77

[STEPPER\_RUN\_MODE\_POSITION](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc)

@ STEPPER\_RUN\_MODE\_POSITION

Position Mode.

**Definition** stepper.h:79

[STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0)

@ STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED

Left end switch status changes to pressed.

**Definition** stepper.h:93

[STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3)

@ STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED

Right end switch status changes to pressed.

**Definition** stepper.h:95

[STEPPER\_EVENT\_STEPS\_COMPLETED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4)

@ STEPPER\_EVENT\_STEPS\_COMPLETED

Steps set using move\_by or move\_to have been executed.

**Definition** stepper.h:89

[STEPPER\_EVENT\_STALL\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445)

@ STEPPER\_EVENT\_STALL\_DETECTED

Stall detected.

**Definition** stepper.h:91

[STEPPER\_MICRO\_STEP\_64](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370)

@ STEPPER\_MICRO\_STEP\_64

64 micro-steps per full step

**Definition** stepper.h:55

[STEPPER\_MICRO\_STEP\_4](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0)

@ STEPPER\_MICRO\_STEP\_4

4 micro-steps per full step

**Definition** stepper.h:47

[STEPPER\_MICRO\_STEP\_1](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9)

@ STEPPER\_MICRO\_STEP\_1

Full step resolution.

**Definition** stepper.h:43

[STEPPER\_MICRO\_STEP\_2](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990)

@ STEPPER\_MICRO\_STEP\_2

2 micro-steps per full step

**Definition** stepper.h:45

[STEPPER\_MICRO\_STEP\_256](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f)

@ STEPPER\_MICRO\_STEP\_256

256 micro-steps per full step

**Definition** stepper.h:59

[STEPPER\_MICRO\_STEP\_8](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155)

@ STEPPER\_MICRO\_STEP\_8

8 micro-steps per full step

**Definition** stepper.h:49

[STEPPER\_MICRO\_STEP\_16](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8)

@ STEPPER\_MICRO\_STEP\_16

16 micro-steps per full step

**Definition** stepper.h:51

[STEPPER\_MICRO\_STEP\_32](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14)

@ STEPPER\_MICRO\_STEP\_32

32 micro-steps per full step

**Definition** stepper.h:53

[STEPPER\_MICRO\_STEP\_128](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43)

@ STEPPER\_MICRO\_STEP\_128

128 micro-steps per full step

**Definition** stepper.h:57

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

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper.h](stepper_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
