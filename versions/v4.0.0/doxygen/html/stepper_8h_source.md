---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stepper_8h_source.html
original_path: doxygen/html/stepper_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper.h

[Go to the documentation of this file.](stepper_8h.md)

1

7

8/\*

9 \* SPDX-FileCopyrightText: Copyright (c) 2024 Carl Zeiss Meditec AG

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_H\_

15

22

23#include <[zephyr/kernel.h](kernel_8h.md)>

24#include <[zephyr/device.h](device_8h.md)>

25#include <[errno.h](errno_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 31](group__stepper__interface.md#ga49df951f1b18bd399a609842514bdbc1)#define MICRO\_STEP\_RES\_INDEX(res) LOG2(res)

32

[ 36](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) {

[ 38](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) [STEPPER\_MICRO\_STEP\_1](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9) = 1,

[ 40](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) [STEPPER\_MICRO\_STEP\_2](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990) = 2,

[ 42](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) [STEPPER\_MICRO\_STEP\_4](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0) = 4,

[ 44](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) [STEPPER\_MICRO\_STEP\_8](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155) = 8,

[ 46](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) [STEPPER\_MICRO\_STEP\_16](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8) = 16,

[ 48](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) [STEPPER\_MICRO\_STEP\_32](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14) = 32,

[ 50](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) [STEPPER\_MICRO\_STEP\_64](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370) = 64,

[ 52](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) [STEPPER\_MICRO\_STEP\_128](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43) = 128,

[ 54](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) [STEPPER\_MICRO\_STEP\_256](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f) = 256,

55};

56

[ 60](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) {

[ 62](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) [STEPPER\_DIRECTION\_NEGATIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0) = 0,

[ 64](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) [STEPPER\_DIRECTION\_POSITIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157) = 1,

65};

66

[ 70](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239)enum [stepper\_run\_mode](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239) {

[ 72](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) [STEPPER\_RUN\_MODE\_HOLD](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c) = 0,

[ 74](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) [STEPPER\_RUN\_MODE\_POSITION](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc) = 1,

[ 76](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) [STEPPER\_RUN\_MODE\_VELOCITY](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb) = 2,

77};

78

[ 82](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f)enum [stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f) {

[ 84](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) [STEPPER\_EVENT\_STEPS\_COMPLETED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4) = 0,

[ 86](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) [STEPPER\_EVENT\_STALL\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445) = 1,

[ 88](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) [STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0) = 2,

[ 90](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) [STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3) = 3,

91};

92

99

105typedef int (\*stepper\_enable\_t)(const struct [device](structdevice.md) \*dev, const bool enable);

106

112typedef int (\*stepper\_move\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

113

119typedef int (\*stepper\_set\_max\_velocity\_t)(const struct [device](structdevice.md) \*dev,

120 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) micro\_steps\_per\_second);

121

127typedef int (\*stepper\_set\_micro\_step\_res\_t)(const struct [device](structdevice.md) \*dev,

128 const enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution);

129

135typedef int (\*stepper\_get\_micro\_step\_res\_t)(const struct [device](structdevice.md) \*dev,

136 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution);

142typedef int (\*stepper\_set\_actual\_position\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

143

149typedef int (\*stepper\_get\_actual\_position\_t)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

150

156typedef int (\*stepper\_set\_target\_position\_t)(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

157

163typedef int (\*stepper\_is\_moving\_t)(const struct [device](structdevice.md) \*dev, bool \*is\_moving);

164

170typedef int (\*stepper\_enable\_constant\_velocity\_mode\_t)(const struct [device](structdevice.md) \*dev,

171 const enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction,

172 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

173

177typedef void (\*stepper\_event\_callback\_t)(const struct [device](structdevice.md) \*dev, const enum [stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f) event,

178 void \*user\_data);

179

185typedef int (\*stepper\_set\_event\_callback\_t)(const struct [device](structdevice.md) \*dev,

186 stepper\_event\_callback\_t callback, void \*user\_data);

187

191\_\_subsystem struct stepper\_driver\_api {

192 stepper\_enable\_t enable;

193 stepper\_move\_t move;

194 stepper\_set\_max\_velocity\_t set\_max\_velocity;

195 stepper\_set\_micro\_step\_res\_t set\_micro\_step\_res;

196 stepper\_get\_micro\_step\_res\_t get\_micro\_step\_res;

197 stepper\_set\_actual\_position\_t set\_actual\_position;

198 stepper\_get\_actual\_position\_t get\_actual\_position;

199 stepper\_set\_target\_position\_t set\_target\_position;

200 stepper\_is\_moving\_t is\_moving;

201 stepper\_enable\_constant\_velocity\_mode\_t enable\_constant\_velocity\_mode;

202 stepper\_set\_event\_callback\_t set\_event\_callback;

203};

204

208

[ 218](group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450)\_\_syscall int [stepper\_enable](group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450)(const struct [device](structdevice.md) \*dev, const bool enable);

219

220static inline int z\_impl\_stepper\_enable(const struct [device](structdevice.md) \*dev, const bool enable)

221{

222 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

223

224 return api->enable(dev, enable);

225}

226

[ 236](group__stepper__interface.md#ga7622a8e1e95b2bbb2dc1273bd84e88a5)\_\_syscall int [stepper\_move](group__stepper__interface.md#ga7622a8e1e95b2bbb2dc1273bd84e88a5)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps);

237

238static inline int z\_impl\_stepper\_move(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) micro\_steps)

239{

240 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

241

242 return api->move(dev, micro\_steps);

243}

244

[ 261](group__stepper__interface.md#gabbb691c2f1beb2bdc7e856a7f77b4de4)\_\_syscall int [stepper\_set\_max\_velocity](group__stepper__interface.md#gabbb691c2f1beb2bdc7e856a7f77b4de4)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) micro\_steps\_per\_second);

262

263static inline int z\_impl\_stepper\_set\_max\_velocity(const struct [device](structdevice.md) \*dev,

264 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) micro\_steps\_per\_second)

265{

266 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

267

268 return api->set\_max\_velocity(dev, micro\_steps\_per\_second);

269}

270

[ 282](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)\_\_syscall int [stepper\_set\_micro\_step\_res](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)(const struct [device](structdevice.md) \*dev,

283 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution);

284

285static inline int z\_impl\_stepper\_set\_micro\_step\_res(const struct [device](structdevice.md) \*dev,

286 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) resolution)

287{

288 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

289

290 if (api->set\_micro\_step\_res == NULL) {

291 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

292 }

293 return api->set\_micro\_step\_res(dev, resolution);

294}

295

[ 306](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e)\_\_syscall int [stepper\_get\_micro\_step\_res](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e)(const struct [device](structdevice.md) \*dev,

307 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution);

308

309static inline int z\_impl\_stepper\_get\_micro\_step\_res(const struct [device](structdevice.md) \*dev,

310 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*resolution)

311{

312 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

313

314 if (api->get\_micro\_step\_res == NULL) {

315 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

316 }

317 return api->get\_micro\_step\_res(dev, resolution);

318}

319

[ 330](group__stepper__interface.md#gaf312a93167aabb39d814c6548991d6c6)\_\_syscall int [stepper\_set\_actual\_position](group__stepper__interface.md#gaf312a93167aabb39d814c6548991d6c6)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

331

332static inline int z\_impl\_stepper\_set\_actual\_position(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value)

333{

334 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

335

336 if (api->set\_actual\_position == NULL) {

337 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

338 }

339 return api->set\_actual\_position(dev, value);

340}

341

[ 352](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157)\_\_syscall int [stepper\_get\_actual\_position](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

353

354static inline int z\_impl\_stepper\_get\_actual\_position(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value)

355{

356 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

357

358 if (api->get\_actual\_position == NULL) {

359 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

360 }

361 return api->get\_actual\_position(dev, value);

362}

363

[ 374](group__stepper__interface.md#ga2417b3ca2f77553bcd6a8b909e5f4d27)\_\_syscall int [stepper\_set\_target\_position](group__stepper__interface.md#ga2417b3ca2f77553bcd6a8b909e5f4d27)(const struct [device](structdevice.md) \*dev, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

375

376static inline int z\_impl\_stepper\_set\_target\_position(const struct [device](structdevice.md) \*dev, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value)

377{

378 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

379

380 if (api->set\_target\_position == NULL) {

381 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

382 }

383 return api->set\_target\_position(dev, value);

384}

385

[ 396](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)\_\_syscall int [stepper\_is\_moving](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)(const struct [device](structdevice.md) \*dev, bool \*is\_moving);

397

398static inline int z\_impl\_stepper\_is\_moving(const struct [device](structdevice.md) \*dev, bool \*is\_moving)

399{

400 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

401

402 if (api->is\_moving == NULL) {

403 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

404 }

405 return api->is\_moving(dev, is\_moving);

406}

407

[ 426](group__stepper__interface.md#ga430250f6e3544e5bba49d5b6ceba1bf9)\_\_syscall int [stepper\_enable\_constant\_velocity\_mode](group__stepper__interface.md#ga430250f6e3544e5bba49d5b6ceba1bf9)(const struct [device](structdevice.md) \*dev,

427 enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction,

428 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

429

430static inline int z\_impl\_stepper\_enable\_constant\_velocity\_mode(

431 const struct [device](structdevice.md) \*dev, const enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01) direction, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value)

432{

433 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

434

435 if (api->enable\_constant\_velocity\_mode == NULL) {

436 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

437 }

438 return api->enable\_constant\_velocity\_mode(dev, direction, value);

439}

440

[ 452](group__stepper__interface.md#gaeaaab5037a4c0f4e5aa9ebc12340517c)\_\_syscall int [stepper\_set\_callback](group__stepper__interface.md#gaeaaab5037a4c0f4e5aa9ebc12340517c)(const struct [device](structdevice.md) \*dev, stepper\_event\_callback\_t callback,

453 void \*user\_data);

454

455static inline int z\_impl\_stepper\_set\_callback(const struct [device](structdevice.md) \*dev,

456 stepper\_event\_callback\_t callback, void \*user\_data)

457{

458 const struct stepper\_driver\_api \*api = (const struct stepper\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

459

460 if (api->set\_event\_callback == NULL) {

461 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

462 }

463 return api->set\_event\_callback(dev, callback, user\_data);

464}

465

469

470#ifdef \_\_cplusplus

471}

472#endif

473

474#include <zephyr/syscalls/stepper.h>

475

476#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)

stepper\_direction

Stepper Motor direction options.

**Definition** stepper.h:60

[stepper\_set\_target\_position](group__stepper__interface.md#ga2417b3ca2f77553bcd6a8b909e5f4d27)

int stepper\_set\_target\_position(const struct device \*dev, int32\_t value)

Set the absolute target position of the stepper.

[stepper\_enable](group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450)

int stepper\_enable(const struct device \*dev, const bool enable)

Enable or Disable Motor Controller.

[stepper\_enable\_constant\_velocity\_mode](group__stepper__interface.md#ga430250f6e3544e5bba49d5b6ceba1bf9)

int stepper\_enable\_constant\_velocity\_mode(const struct device \*dev, enum stepper\_direction direction, uint32\_t value)

Enable constant velocity mode for the stepper with a given velocity.

[stepper\_run\_mode](group__stepper__interface.md#ga5f9c911155e7c19afa4dc6827313c239)

stepper\_run\_mode

Stepper Motor run mode options.

**Definition** stepper.h:70

[stepper\_get\_actual\_position](group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157)

int stepper\_get\_actual\_position(const struct device \*dev, int32\_t \*value)

Get the actual a.k.a reference position of the stepper.

[stepper\_get\_micro\_step\_res](group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e)

int stepper\_get\_micro\_step\_res(const struct device \*dev, enum stepper\_micro\_step\_resolution \*resolution)

Get the microstep resolution in stepper motor controller.

[stepper\_move](group__stepper__interface.md#ga7622a8e1e95b2bbb2dc1273bd84e88a5)

int stepper\_move(const struct device \*dev, int32\_t micro\_steps)

Set the micro\_steps to be moved from the current position i.e.

[stepper\_is\_moving](group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c)

int stepper\_is\_moving(const struct device \*dev, bool \*is\_moving)

Check if the stepper motor is currently moving.

[stepper\_event](group__stepper__interface.md#gab1534238fbf8d2270ea4f69d3a558b5f)

stepper\_event

Stepper Events.

**Definition** stepper.h:82

[stepper\_set\_max\_velocity](group__stepper__interface.md#gabbb691c2f1beb2bdc7e856a7f77b4de4)

int stepper\_set\_max\_velocity(const struct device \*dev, uint32\_t micro\_steps\_per\_second)

Set the target velocity to be reached by the motor.

[stepper\_set\_micro\_step\_res](group__stepper__interface.md#gac3f2e315551e11500513dac837567625)

int stepper\_set\_micro\_step\_res(const struct device \*dev, enum stepper\_micro\_step\_resolution resolution)

Set the microstep resolution in stepper motor controller.

[stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)

stepper\_micro\_step\_resolution

Stepper Motor micro step resolution options.

**Definition** stepper.h:36

[stepper\_set\_callback](group__stepper__interface.md#gaeaaab5037a4c0f4e5aa9ebc12340517c)

int stepper\_set\_callback(const struct device \*dev, stepper\_event\_callback\_t callback, void \*user\_data)

Set the callback function to be called when a stepper event occurs.

[stepper\_set\_actual\_position](group__stepper__interface.md#gaf312a93167aabb39d814c6548991d6c6)

int stepper\_set\_actual\_position(const struct device \*dev, int32\_t value)

Set the actual a.k.a reference position of the stepper.

[STEPPER\_DIRECTION\_POSITIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01a2ce2e43e0434d362c81394039dd2e157)

@ STEPPER\_DIRECTION\_POSITIVE

Positive direction.

**Definition** stepper.h:64

[STEPPER\_DIRECTION\_NEGATIVE](group__stepper__interface.md#gga04be36af941edfd3a52fda2fb0ee2a01aedaeb192b2d3c806f33f6c13eba0f1b0)

@ STEPPER\_DIRECTION\_NEGATIVE

Negative direction.

**Definition** stepper.h:62

[STEPPER\_RUN\_MODE\_VELOCITY](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239a4509d405cd2ffb0db2f8d7b2b1e2bfeb)

@ STEPPER\_RUN\_MODE\_VELOCITY

Velocity Mode.

**Definition** stepper.h:76

[STEPPER\_RUN\_MODE\_HOLD](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239abeb4fc4d06f05dd2dad9fafd0a16026c)

@ STEPPER\_RUN\_MODE\_HOLD

Hold Mode.

**Definition** stepper.h:72

[STEPPER\_RUN\_MODE\_POSITION](group__stepper__interface.md#gga5f9c911155e7c19afa4dc6827313c239ae24b1de11e7b7ff440fb9f3ea85f67bc)

@ STEPPER\_RUN\_MODE\_POSITION

Position Mode.

**Definition** stepper.h:74

[STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3815a2913aef2f234c36936294685fc0)

@ STEPPER\_EVENT\_LEFT\_END\_STOP\_DETECTED

Left end switch status changes to pressed.

**Definition** stepper.h:88

[STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa3d2b06294740a8f7d84c0a81b011b8e3)

@ STEPPER\_EVENT\_RIGHT\_END\_STOP\_DETECTED

Right end switch status changes to pressed.

**Definition** stepper.h:90

[STEPPER\_EVENT\_STEPS\_COMPLETED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa7b52130939a6bc32f66d860f256ab8c4)

@ STEPPER\_EVENT\_STEPS\_COMPLETED

Steps set using move or set\_target\_position have been executed.

**Definition** stepper.h:84

[STEPPER\_EVENT\_STALL\_DETECTED](group__stepper__interface.md#ggab1534238fbf8d2270ea4f69d3a558b5fa99db863b18d3e004a06de3f7d1abe445)

@ STEPPER\_EVENT\_STALL\_DETECTED

Stall detected.

**Definition** stepper.h:86

[STEPPER\_MICRO\_STEP\_64](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a25ea7a12d2ec3751e941f446b9637370)

@ STEPPER\_MICRO\_STEP\_64

64 micro steps per full step

**Definition** stepper.h:50

[STEPPER\_MICRO\_STEP\_4](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c5dd8c5054a1a66e65cceba719ca5e0)

@ STEPPER\_MICRO\_STEP\_4

4 micro steps per full step

**Definition** stepper.h:42

[STEPPER\_MICRO\_STEP\_1](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a4c72780b13eb7f5ee5c433420a0eede9)

@ STEPPER\_MICRO\_STEP\_1

Full step resolution.

**Definition** stepper.h:38

[STEPPER\_MICRO\_STEP\_2](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a6f42ccb9a398946ce4eeac20c364f990)

@ STEPPER\_MICRO\_STEP\_2

2 micro steps per full step

**Definition** stepper.h:40

[STEPPER\_MICRO\_STEP\_256](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30a7ff93a287c10971ac50644de2ae0161f)

@ STEPPER\_MICRO\_STEP\_256

256 micro steps per full step

**Definition** stepper.h:54

[STEPPER\_MICRO\_STEP\_8](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30aae2b109417f88201514bedd0e2c71155)

@ STEPPER\_MICRO\_STEP\_8

8 micro steps per full step

**Definition** stepper.h:44

[STEPPER\_MICRO\_STEP\_16](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30ac04236cc36c1201539f3fcc4aef1f1d8)

@ STEPPER\_MICRO\_STEP\_16

16 micro steps per full step

**Definition** stepper.h:46

[STEPPER\_MICRO\_STEP\_32](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30af733d75d60220ae98bb08ee3a4c49d14)

@ STEPPER\_MICRO\_STEP\_32

32 micro steps per full step

**Definition** stepper.h:48

[STEPPER\_MICRO\_STEP\_128](group__stepper__interface.md#ggad8d053f92eb3a194652b4600af531e30afc6d0ffc96256600c74b00057ec55e43)

@ STEPPER\_MICRO\_STEP\_128

128 micro steps per full step

**Definition** stepper.h:52

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper.h](stepper_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
