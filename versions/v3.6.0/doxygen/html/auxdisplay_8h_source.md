---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/auxdisplay_8h_source.html
original_path: doxygen/html/auxdisplay_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

auxdisplay.h

[Go to the documentation of this file.](auxdisplay_8h.md)

1/\*

2 \* Copyright (c) 2022-2023 Jamie McCrae

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_AUXDISPLAY\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_AUXDISPLAY\_H\_

14

21

22#include <[stdint.h](stdint_8h.md)>

23#include <stddef.h>

24#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 32](group__auxdisplay__interface.md#ga0bd1d97b360f3138887a5e3e4729e01b)#define AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED 0

33

[ 35](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [auxdisplay\_mode\_t](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2);

36

[ 38](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504)enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) {

[ 40](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) [AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) = 0,

41

[ 45](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28) [AUXDISPLAY\_POSITION\_RELATIVE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28),

46

[ 50](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558) [AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558),

51

[ 52](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23) [AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23),

53};

54

[ 56](group__auxdisplay__interface.md#ga5f95ac69e18091883e7121103014be10)enum [auxdisplay\_direction](group__auxdisplay__interface.md#ga5f95ac69e18091883e7121103014be10) {

[ 58](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599) [AUXDISPLAY\_DIRECTION\_RIGHT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599) = 0,

59

[ 61](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352) [AUXDISPLAY\_DIRECTION\_LEFT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352),

62

[ 63](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3) [AUXDISPLAY\_DIRECTION\_COUNT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3),

64};

65

[ 69](structauxdisplay__light.md)struct [auxdisplay\_light](structauxdisplay__light.md) {

[ 71](structauxdisplay__light.md#a4cd0c416ce77a45949feb90ae9f254a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minimum](structauxdisplay__light.md#a4cd0c416ce77a45949feb90ae9f254a1);

72

[ 74](structauxdisplay__light.md#a8f40f5fd3f825f1ee8c34891804cc003) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maximum](structauxdisplay__light.md#a8f40f5fd3f825f1ee8c34891804cc003);

75};

76

[ 78](structauxdisplay__capabilities.md)struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) {

[ 80](structauxdisplay__capabilities.md#ac0fc352a5799328211ae6f8c94cdcd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [columns](structauxdisplay__capabilities.md#ac0fc352a5799328211ae6f8c94cdcd7a);

81

[ 83](structauxdisplay__capabilities.md#af1bcdc27adb678ca4447614a22366aba) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rows](structauxdisplay__capabilities.md#af1bcdc27adb678ca4447614a22366aba);

84

[ 86](structauxdisplay__capabilities.md#a55ac50abb253e64e9fb7be6542801dc9) [auxdisplay\_mode\_t](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2) [mode](structauxdisplay__capabilities.md#a55ac50abb253e64e9fb7be6542801dc9);

87

[ 89](structauxdisplay__capabilities.md#a15e3926754baaefffa1eff45573a59b1) struct [auxdisplay\_light](structauxdisplay__light.md) [brightness](structauxdisplay__capabilities.md#a15e3926754baaefffa1eff45573a59b1);

90

[ 92](structauxdisplay__capabilities.md#ace4d7b099428e5f7164c3e9e318c1feb) struct [auxdisplay\_light](structauxdisplay__light.md) [backlight](structauxdisplay__capabilities.md#ace4d7b099428e5f7164c3e9e318c1feb);

93

[ 95](structauxdisplay__capabilities.md#a4b66412a2000fe09f30c555befbd11d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [custom\_characters](structauxdisplay__capabilities.md#a4b66412a2000fe09f30c555befbd11d0);

96

[ 98](structauxdisplay__capabilities.md#ad77f390f5a6bdbebabc703fdc77322a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [custom\_character\_width](structauxdisplay__capabilities.md#ad77f390f5a6bdbebabc703fdc77322a3);

99

[ 101](structauxdisplay__capabilities.md#adc88b37e9f73a98560099c94c8797741) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [custom\_character\_height](structauxdisplay__capabilities.md#adc88b37e9f73a98560099c94c8797741);

102};

103

[ 105](structauxdisplay__custom__data.md)struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) {

[ 107](structauxdisplay__custom__data.md#acfd41be1569cc43bd09824c5e46b8d51) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structauxdisplay__custom__data.md#acfd41be1569cc43bd09824c5e46b8d51);

108

[ 110](structauxdisplay__custom__data.md#ac995ecff9634acbc535a47b37134c6e1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structauxdisplay__custom__data.md#ac995ecff9634acbc535a47b37134c6e1);

111

[ 113](structauxdisplay__custom__data.md#aa9c3b2af7c07e71e8cc5cd3eae058729) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structauxdisplay__custom__data.md#aa9c3b2af7c07e71e8cc5cd3eae058729);

114};

115

[ 117](structauxdisplay__character.md)struct [auxdisplay\_character](structauxdisplay__character.md) {

[ 119](structauxdisplay__character.md#a9f0bb424b9918e0f0c07c12eb4235677) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structauxdisplay__character.md#a9f0bb424b9918e0f0c07c12eb4235677);

120

[ 126](structauxdisplay__character.md#a4b011716576201818278aa853bfe542e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structauxdisplay__character.md#a4b011716576201818278aa853bfe542e);

127

[ 131](structauxdisplay__character.md#a217dd562886158efec238649fb4ade04) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [character\_code](structauxdisplay__character.md#a217dd562886158efec238649fb4ade04);

132};

133

139

145typedef int (\*auxdisplay\_display\_on\_t)(const struct [device](structdevice.md) \*dev);

146

152typedef int (\*auxdisplay\_display\_off\_t)(const struct [device](structdevice.md) \*dev);

153

159typedef int (\*auxdisplay\_cursor\_set\_enabled\_t)(const struct [device](structdevice.md) \*dev, bool enabled);

160

166typedef int (\*auxdisplay\_position\_blinking\_set\_enabled\_t)(const struct [device](structdevice.md) \*dev,

167 bool enabled);

168

174typedef int (\*auxdisplay\_cursor\_shift\_set\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) direction,

175 bool display\_shift);

176

182typedef int (\*auxdisplay\_cursor\_position\_set\_t)(const struct [device](structdevice.md) \*dev,

183 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

184 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

185

191typedef int (\*auxdisplay\_cursor\_position\_get\_t)(const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x,

192 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y);

193

199typedef int (\*auxdisplay\_display\_position\_set\_t)(const struct [device](structdevice.md) \*dev,

200 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

201 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

202

208typedef int (\*auxdisplay\_display\_position\_get\_t)(const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x,

209 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y);

210

216typedef int (\*auxdisplay\_capabilities\_get\_t)(const struct [device](structdevice.md) \*dev,

217 struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \*capabilities);

218

224typedef int (\*auxdisplay\_clear\_t)(const struct [device](structdevice.md) \*dev);

225

232typedef int (\*auxdisplay\_brightness\_get\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*brightness);

233

239typedef int (\*auxdisplay\_brightness\_set\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness);

240

247typedef int (\*auxdisplay\_backlight\_get\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*backlight);

248

254typedef int (\*auxdisplay\_backlight\_set\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) backlight);

255

261typedef int (\*auxdisplay\_is\_busy\_t)(const struct [device](structdevice.md) \*dev);

262

268typedef int (\*auxdisplay\_custom\_character\_set\_t)(const struct [device](structdevice.md) \*dev,

269 struct [auxdisplay\_character](structauxdisplay__character.md) \*character);

270

276typedef int (\*auxdisplay\_write\_t)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

277

283typedef int (\*auxdisplay\_custom\_command\_t)(const struct [device](structdevice.md) \*dev,

284 struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \*command);

285

286\_\_subsystem struct auxdisplay\_driver\_api {

287 auxdisplay\_display\_on\_t display\_on;

288 auxdisplay\_display\_off\_t display\_off;

289 auxdisplay\_cursor\_set\_enabled\_t cursor\_set\_enabled;

290 auxdisplay\_position\_blinking\_set\_enabled\_t position\_blinking\_set\_enabled;

291 auxdisplay\_cursor\_shift\_set\_t cursor\_shift\_set;

292 auxdisplay\_cursor\_position\_set\_t cursor\_position\_set;

293 auxdisplay\_cursor\_position\_get\_t cursor\_position\_get;

294 auxdisplay\_display\_position\_set\_t display\_position\_set;

295 auxdisplay\_display\_position\_get\_t display\_position\_get;

296 auxdisplay\_capabilities\_get\_t capabilities\_get;

297 auxdisplay\_clear\_t clear;

298 auxdisplay\_brightness\_get\_t brightness\_get;

299 auxdisplay\_brightness\_set\_t brightness\_set;

300 auxdisplay\_backlight\_get\_t backlight\_get;

301 auxdisplay\_backlight\_set\_t backlight\_set;

302 auxdisplay\_is\_busy\_t is\_busy;

303 auxdisplay\_custom\_character\_set\_t custom\_character\_set;

304 auxdisplay\_write\_t write;

305 auxdisplay\_custom\_command\_t custom\_command;

306};

307

311

[ 321](group__auxdisplay__interface.md#gaffb3c1c41d810355fe2da3558ebba0c2)\_\_syscall int [auxdisplay\_display\_on](group__auxdisplay__interface.md#gaffb3c1c41d810355fe2da3558ebba0c2)(const struct [device](structdevice.md) \*dev);

322

323static inline int z\_impl\_auxdisplay\_display\_on(const struct [device](structdevice.md) \*dev)

324{

325 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

326

327 if (!api->display\_on) {

328 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

329 }

330

331 return api->display\_on(dev);

332}

333

[ 343](group__auxdisplay__interface.md#ga625f399720417715090793c7f6d63f7e)\_\_syscall int [auxdisplay\_display\_off](group__auxdisplay__interface.md#ga625f399720417715090793c7f6d63f7e)(const struct [device](structdevice.md) \*dev);

344

345static inline int z\_impl\_auxdisplay\_display\_off(const struct [device](structdevice.md) \*dev)

346{

347 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

348

349 if (!api->display\_off) {

350 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

351 }

352

353 return api->display\_off(dev);

354}

355

[ 366](group__auxdisplay__interface.md#ga7191475b362f728cc92eb07cb1f2ed00)\_\_syscall int [auxdisplay\_cursor\_set\_enabled](group__auxdisplay__interface.md#ga7191475b362f728cc92eb07cb1f2ed00)(const struct [device](structdevice.md) \*dev,

367 bool enabled);

368

369static inline int z\_impl\_auxdisplay\_cursor\_set\_enabled(const struct [device](structdevice.md) \*dev,

370 bool enabled)

371{

372 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

373

374 if (!api->cursor\_set\_enabled) {

375 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

376 }

377

378 return api->cursor\_set\_enabled(dev, enabled);

379}

380

[ 391](group__auxdisplay__interface.md#ga7102ec9941f8b3131a18e4ff7b640241)\_\_syscall int [auxdisplay\_position\_blinking\_set\_enabled](group__auxdisplay__interface.md#ga7102ec9941f8b3131a18e4ff7b640241)(const struct [device](structdevice.md) \*dev,

392 bool enabled);

393

394static inline int z\_impl\_auxdisplay\_position\_blinking\_set\_enabled(const struct [device](structdevice.md) \*dev,

395 bool enabled)

396{

397 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

398

399 if (!api->position\_blinking\_set\_enabled) {

400 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

401 }

402

403 return api->position\_blinking\_set\_enabled(dev, enabled);

404}

405

[ 419](group__auxdisplay__interface.md#gafb18729b4897cea83dbfc1c7241f5b2d)\_\_syscall int [auxdisplay\_cursor\_shift\_set](group__auxdisplay__interface.md#gafb18729b4897cea83dbfc1c7241f5b2d)(const struct [device](structdevice.md) \*dev,

420 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) direction, bool display\_shift);

421

422static inline int z\_impl\_auxdisplay\_cursor\_shift\_set(const struct [device](structdevice.md) \*dev,

423 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) direction,

424 bool display\_shift)

425{

426 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

427

428 if (!api->cursor\_shift\_set) {

429 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

430 }

431

432 if (direction >= [AUXDISPLAY\_DIRECTION\_COUNT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3)) {

433 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

434 }

435

436 return api->cursor\_shift\_set(dev, direction, display\_shift);

437}

438

[ 452](group__auxdisplay__interface.md#ga9c6302789d9cc9e481dd7c54ef370988)\_\_syscall int [auxdisplay\_cursor\_position\_set](group__auxdisplay__interface.md#ga9c6302789d9cc9e481dd7c54ef370988)(const struct [device](structdevice.md) \*dev,

453 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

454 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

455

456static inline int z\_impl\_auxdisplay\_cursor\_position\_set(const struct [device](structdevice.md) \*dev,

457 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

458 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y)

459{

460 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

461

462 if (!api->cursor\_position\_set) {

463 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

464 } else if (type >= [AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)) {

465 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

466 } else if (type == [AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) && (x < 0 || y < 0)) {

467 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

468 }

469

470 return api->cursor\_position\_set(dev, type, x, y);

471}

472

[ 485](group__auxdisplay__interface.md#ga37bd5403c876ff294be5ea72292de4b4)\_\_syscall int [auxdisplay\_cursor\_position\_get](group__auxdisplay__interface.md#ga37bd5403c876ff294be5ea72292de4b4)(const struct [device](structdevice.md) \*dev,

486 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y);

487

488static inline int z\_impl\_auxdisplay\_cursor\_position\_get(const struct [device](structdevice.md) \*dev,

489 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y)

490{

491 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

492

493 if (!api->cursor\_position\_get) {

494 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

495 }

496

497 return api->cursor\_position\_get(dev, x, y);

498}

499

[ 513](group__auxdisplay__interface.md#ga02e8e930203cfb1410752a0ffee9a34e)\_\_syscall int [auxdisplay\_display\_position\_set](group__auxdisplay__interface.md#ga02e8e930203cfb1410752a0ffee9a34e)(const struct [device](structdevice.md) \*dev,

514 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

515 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

516

517static inline int z\_impl\_auxdisplay\_display\_position\_set(const struct [device](structdevice.md) \*dev,

518 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

519 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y)

520{

521 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

522

523 if (!api->display\_position\_set) {

524 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

525 } else if (type >= [AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)) {

526 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

527 } else if (type == [AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) && (x < 0 || y < 0)) {

528 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

529 }

530

531 return api->display\_position\_set(dev, type, x, y);

532}

533

[ 546](group__auxdisplay__interface.md#ga1f9e363765d715edb899901a14c54674)\_\_syscall int [auxdisplay\_display\_position\_get](group__auxdisplay__interface.md#ga1f9e363765d715edb899901a14c54674)(const struct [device](structdevice.md) \*dev,

547 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y);

548

549static inline int z\_impl\_auxdisplay\_display\_position\_get(const struct [device](structdevice.md) \*dev,

550 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y)

551{

552 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

553

554 if (!api->display\_position\_get) {

555 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

556 }

557

558 return api->display\_position\_get(dev, x, y);

559}

560

[ 570](group__auxdisplay__interface.md#ga4dd5cba56d4b90b77ae8ad02122ef81c)\_\_syscall int [auxdisplay\_capabilities\_get](group__auxdisplay__interface.md#ga4dd5cba56d4b90b77ae8ad02122ef81c)(const struct [device](structdevice.md) \*dev,

571 struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \*capabilities);

572

573static inline int z\_impl\_auxdisplay\_capabilities\_get(const struct [device](structdevice.md) \*dev,

574 struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \*capabilities)

575{

576 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

577

578 return api->capabilities\_get(dev, capabilities);

579}

580

[ 591](group__auxdisplay__interface.md#gaa5a643603353319946c823cc959b74b3)\_\_syscall int [auxdisplay\_clear](group__auxdisplay__interface.md#gaa5a643603353319946c823cc959b74b3)(const struct [device](structdevice.md) \*dev);

592

593static inline int z\_impl\_auxdisplay\_clear(const struct [device](structdevice.md) \*dev)

594{

595 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

596

597 return api->clear(dev);

598}

599

[ 610](group__auxdisplay__interface.md#ga1f5be6fefc759607d2859a648a1fb3b8)\_\_syscall int [auxdisplay\_brightness\_get](group__auxdisplay__interface.md#ga1f5be6fefc759607d2859a648a1fb3b8)(const struct [device](structdevice.md) \*dev,

611 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*brightness);

612

613static inline int z\_impl\_auxdisplay\_brightness\_get(const struct [device](structdevice.md) \*dev,

614 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*brightness)

615{

616 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

617

618 if (!api->brightness\_get) {

619 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

620 }

621

622 return api->brightness\_get(dev, brightness);

623}

624

[ 636](group__auxdisplay__interface.md#ga34b31b70fdc57e33fc46f1048cc25e1a)\_\_syscall int [auxdisplay\_brightness\_set](group__auxdisplay__interface.md#ga34b31b70fdc57e33fc46f1048cc25e1a)(const struct [device](structdevice.md) \*dev,

637 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness);

638

639static inline int z\_impl\_auxdisplay\_brightness\_set(const struct [device](structdevice.md) \*dev,

640 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness)

641{

642 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

643

644 if (!api->brightness\_set) {

645 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

646 }

647

648 return api->brightness\_set(dev, brightness);

649}

650

[ 661](group__auxdisplay__interface.md#gaf10ebdbe821894ccbeccb35bfa985fea)\_\_syscall int [auxdisplay\_backlight\_get](group__auxdisplay__interface.md#gaf10ebdbe821894ccbeccb35bfa985fea)(const struct [device](structdevice.md) \*dev,

662 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*backlight);

663

664static inline int z\_impl\_auxdisplay\_backlight\_get(const struct [device](structdevice.md) \*dev,

665 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*backlight)

666{

667 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

668

669 if (!api->backlight\_get) {

670 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

671 }

672

673 return api->backlight\_get(dev, backlight);

674}

675

[ 687](group__auxdisplay__interface.md#ga28aef24928543329c706513cc7e5b814)\_\_syscall int [auxdisplay\_backlight\_set](group__auxdisplay__interface.md#ga28aef24928543329c706513cc7e5b814)(const struct [device](structdevice.md) \*dev,

688 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) backlight);

689

690static inline int z\_impl\_auxdisplay\_backlight\_set(const struct [device](structdevice.md) \*dev,

691 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) backlight)

692{

693 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

694

695 if (!api->backlight\_set) {

696 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

697 }

698

699 return api->backlight\_set(dev, backlight);

700}

701

[ 712](group__auxdisplay__interface.md#ga2af115a23f370e0770b3c998ecf0b96b)\_\_syscall int [auxdisplay\_is\_busy](group__auxdisplay__interface.md#ga2af115a23f370e0770b3c998ecf0b96b)(const struct [device](structdevice.md) \*dev);

713

714static inline int z\_impl\_auxdisplay\_is\_busy(const struct [device](structdevice.md) \*dev)

715{

716 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

717

718 if (!api->is\_busy) {

719 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

720 }

721

722 return api->is\_busy(dev);

723}

724

[ 745](group__auxdisplay__interface.md#gaf03a1068b0aed1f27ee9e2e61066da08)\_\_syscall int [auxdisplay\_custom\_character\_set](group__auxdisplay__interface.md#gaf03a1068b0aed1f27ee9e2e61066da08)(const struct [device](structdevice.md) \*dev,

746 struct [auxdisplay\_character](structauxdisplay__character.md) \*character);

747

748static inline int z\_impl\_auxdisplay\_custom\_character\_set(const struct [device](structdevice.md) \*dev,

749 struct [auxdisplay\_character](structauxdisplay__character.md) \*character)

750{

751 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

752

753 if (!api->custom\_character\_set) {

754 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

755 }

756

757 return api->custom\_character\_set(dev, character);

758}

759

[ 771](group__auxdisplay__interface.md#ga231dd862cda34ea4c0c8870675556f8d)\_\_syscall int [auxdisplay\_write](group__auxdisplay__interface.md#ga231dd862cda34ea4c0c8870675556f8d)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

772 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

773

774static inline int z\_impl\_auxdisplay\_write(const struct [device](structdevice.md) \*dev,

775 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

776{

777 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

778

779 return api->write(dev, data, len);

780}

781

[ 793](group__auxdisplay__interface.md#ga87064057ae857f81431e6e9f139a6aaa)\_\_syscall int [auxdisplay\_custom\_command](group__auxdisplay__interface.md#ga87064057ae857f81431e6e9f139a6aaa)(const struct [device](structdevice.md) \*dev,

794 struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \*data);

795

796static inline int z\_impl\_auxdisplay\_custom\_command(const struct [device](structdevice.md) \*dev,

797 struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \*data)

798{

799 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

800

801 if (!api->custom\_command) {

802 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

803 }

804

805 return api->custom\_command(dev, data);

806}

807

808#ifdef \_\_cplusplus

809}

810#endif

811

815

816#include <syscalls/auxdisplay.h>

817

818#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_AUXDISPLAY\_H\_ \*/

[device.h](device_8h.md)

[auxdisplay\_display\_position\_set](group__auxdisplay__interface.md#ga02e8e930203cfb1410752a0ffee9a34e)

int auxdisplay\_display\_position\_set(const struct device \*dev, enum auxdisplay\_position type, int16\_t x, int16\_t y)

Set display position on an auxiliary display.

[auxdisplay\_brightness\_get](group__auxdisplay__interface.md#ga1f5be6fefc759607d2859a648a1fb3b8)

int auxdisplay\_brightness\_get(const struct device \*dev, uint8\_t \*brightness)

Get the current brightness level of an auxiliary display.

[auxdisplay\_display\_position\_get](group__auxdisplay__interface.md#ga1f9e363765d715edb899901a14c54674)

int auxdisplay\_display\_position\_get(const struct device \*dev, int16\_t \*x, int16\_t \*y)

Get current display position on an auxiliary display.

[auxdisplay\_write](group__auxdisplay__interface.md#ga231dd862cda34ea4c0c8870675556f8d)

int auxdisplay\_write(const struct device \*dev, const uint8\_t \*data, uint16\_t len)

Write data to auxiliary display screen at current position.

[auxdisplay\_backlight\_set](group__auxdisplay__interface.md#ga28aef24928543329c706513cc7e5b814)

int auxdisplay\_backlight\_set(const struct device \*dev, uint8\_t backlight)

Update the backlight level of an auxiliary display.

[auxdisplay\_is\_busy](group__auxdisplay__interface.md#ga2af115a23f370e0770b3c998ecf0b96b)

int auxdisplay\_is\_busy(const struct device \*dev)

Check if an auxiliary display driver is busy.

[auxdisplay\_brightness\_set](group__auxdisplay__interface.md#ga34b31b70fdc57e33fc46f1048cc25e1a)

int auxdisplay\_brightness\_set(const struct device \*dev, uint8\_t brightness)

Update the brightness level of an auxiliary display.

[auxdisplay\_cursor\_position\_get](group__auxdisplay__interface.md#ga37bd5403c876ff294be5ea72292de4b4)

int auxdisplay\_cursor\_position\_get(const struct device \*dev, int16\_t \*x, int16\_t \*y)

Get current cursor on an auxiliary display.

[auxdisplay\_capabilities\_get](group__auxdisplay__interface.md#ga4dd5cba56d4b90b77ae8ad02122ef81c)

int auxdisplay\_capabilities\_get(const struct device \*dev, struct auxdisplay\_capabilities \*capabilities)

Fetch capabilities (and details) of auxiliary display.

[auxdisplay\_direction](group__auxdisplay__interface.md#ga5f95ac69e18091883e7121103014be10)

auxdisplay\_direction

Used for setting character append position.

**Definition** auxdisplay.h:56

[auxdisplay\_display\_off](group__auxdisplay__interface.md#ga625f399720417715090793c7f6d63f7e)

int auxdisplay\_display\_off(const struct device \*dev)

Turn display off.

[auxdisplay\_position\_blinking\_set\_enabled](group__auxdisplay__interface.md#ga7102ec9941f8b3131a18e4ff7b640241)

int auxdisplay\_position\_blinking\_set\_enabled(const struct device \*dev, bool enabled)

Set cursor blinking status on an auxiliary display.

[auxdisplay\_cursor\_set\_enabled](group__auxdisplay__interface.md#ga7191475b362f728cc92eb07cb1f2ed00)

int auxdisplay\_cursor\_set\_enabled(const struct device \*dev, bool enabled)

Set cursor enabled status on an auxiliary display.

[auxdisplay\_mode\_t](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2)

uint32\_t auxdisplay\_mode\_t

Used to describe the mode of an auxiliary (text) display.

**Definition** auxdisplay.h:35

[auxdisplay\_custom\_command](group__auxdisplay__interface.md#ga87064057ae857f81431e6e9f139a6aaa)

int auxdisplay\_custom\_command(const struct device \*dev, struct auxdisplay\_custom\_data \*data)

Send a custom command to the display (if supported by driver).

[auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504)

auxdisplay\_position

Used for moving the cursor or display position.

**Definition** auxdisplay.h:38

[auxdisplay\_cursor\_position\_set](group__auxdisplay__interface.md#ga9c6302789d9cc9e481dd7c54ef370988)

int auxdisplay\_cursor\_position\_set(const struct device \*dev, enum auxdisplay\_position type, int16\_t x, int16\_t y)

Set cursor (and write position) on an auxiliary display.

[auxdisplay\_clear](group__auxdisplay__interface.md#gaa5a643603353319946c823cc959b74b3)

int auxdisplay\_clear(const struct device \*dev)

Clear display of auxiliary display and return to home position (note that this does not reset the dis...

[auxdisplay\_custom\_character\_set](group__auxdisplay__interface.md#gaf03a1068b0aed1f27ee9e2e61066da08)

int auxdisplay\_custom\_character\_set(const struct device \*dev, struct auxdisplay\_character \*character)

Sets a custom character in the display, the custom character struct must contain the pixel data for t...

[auxdisplay\_backlight\_get](group__auxdisplay__interface.md#gaf10ebdbe821894ccbeccb35bfa985fea)

int auxdisplay\_backlight\_get(const struct device \*dev, uint8\_t \*backlight)

Get the backlight level details of an auxiliary display.

[auxdisplay\_cursor\_shift\_set](group__auxdisplay__interface.md#gafb18729b4897cea83dbfc1c7241f5b2d)

int auxdisplay\_cursor\_shift\_set(const struct device \*dev, uint8\_t direction, bool display\_shift)

Set cursor shift after character write and display shift.

[auxdisplay\_display\_on](group__auxdisplay__interface.md#gaffb3c1c41d810355fe2da3558ebba0c2)

int auxdisplay\_display\_on(const struct device \*dev)

Turn display on.

[AUXDISPLAY\_DIRECTION\_LEFT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352)

@ AUXDISPLAY\_DIRECTION\_LEFT

Each character will be placed to the left of existing characters.

**Definition** auxdisplay.h:61

[AUXDISPLAY\_DIRECTION\_COUNT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3)

@ AUXDISPLAY\_DIRECTION\_COUNT

**Definition** auxdisplay.h:63

[AUXDISPLAY\_DIRECTION\_RIGHT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599)

@ AUXDISPLAY\_DIRECTION\_RIGHT

Each character will be placed to the right of existing characters.

**Definition** auxdisplay.h:58

[AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)

@ AUXDISPLAY\_POSITION\_COUNT

**Definition** auxdisplay.h:52

[AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404)

@ AUXDISPLAY\_POSITION\_ABSOLUTE

Moves to specified X,Y position.

**Definition** auxdisplay.h:40

[AUXDISPLAY\_POSITION\_RELATIVE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28)

@ AUXDISPLAY\_POSITION\_RELATIVE

Shifts current position by +/- X,Y position, does not take display direction into consideration.

**Definition** auxdisplay.h:45

[AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558)

@ AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION

Shifts current position by +/- X,Y position, takes display direction into consideration.

**Definition** auxdisplay.h:50

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:61

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[auxdisplay\_capabilities](structauxdisplay__capabilities.md)

Structure holding display capabilities.

**Definition** auxdisplay.h:78

[auxdisplay\_capabilities::brightness](structauxdisplay__capabilities.md#a15e3926754baaefffa1eff45573a59b1)

struct auxdisplay\_light brightness

Brightness details for display (if supported).

**Definition** auxdisplay.h:89

[auxdisplay\_capabilities::custom\_characters](structauxdisplay__capabilities.md#a4b66412a2000fe09f30c555befbd11d0)

uint8\_t custom\_characters

Number of custom characters supported by display (0 if unsupported).

**Definition** auxdisplay.h:95

[auxdisplay\_capabilities::mode](structauxdisplay__capabilities.md#a55ac50abb253e64e9fb7be6542801dc9)

auxdisplay\_mode\_t mode

Display-specific data (e.g.

**Definition** auxdisplay.h:86

[auxdisplay\_capabilities::columns](structauxdisplay__capabilities.md#ac0fc352a5799328211ae6f8c94cdcd7a)

uint16\_t columns

Number of character columns.

**Definition** auxdisplay.h:80

[auxdisplay\_capabilities::backlight](structauxdisplay__capabilities.md#ace4d7b099428e5f7164c3e9e318c1feb)

struct auxdisplay\_light backlight

Backlight details for display (if supported).

**Definition** auxdisplay.h:92

[auxdisplay\_capabilities::custom\_character\_width](structauxdisplay__capabilities.md#ad77f390f5a6bdbebabc703fdc77322a3)

uint8\_t custom\_character\_width

Width (in pixels) of a custom character, supplied custom characters should match.

**Definition** auxdisplay.h:98

[auxdisplay\_capabilities::custom\_character\_height](structauxdisplay__capabilities.md#adc88b37e9f73a98560099c94c8797741)

uint8\_t custom\_character\_height

Height (in pixels) of a custom character, supplied custom characters should match.

**Definition** auxdisplay.h:101

[auxdisplay\_capabilities::rows](structauxdisplay__capabilities.md#af1bcdc27adb678ca4447614a22366aba)

uint16\_t rows

Number of character rows.

**Definition** auxdisplay.h:83

[auxdisplay\_character](structauxdisplay__character.md)

Structure for a custom character.

**Definition** auxdisplay.h:117

[auxdisplay\_character::character\_code](structauxdisplay__character.md#a217dd562886158efec238649fb4ade04)

uint8\_t character\_code

Will be updated with custom character index to use in the display write function to disaplay this cus...

**Definition** auxdisplay.h:131

[auxdisplay\_character::data](structauxdisplay__character.md#a4b011716576201818278aa853bfe542e)

uint8\_t \* data

Custom character pixel data, a character must be valid for a display consisting of a uint8 array of s...

**Definition** auxdisplay.h:126

[auxdisplay\_character::index](structauxdisplay__character.md#a9f0bb424b9918e0f0c07c12eb4235677)

uint8\_t index

Custom character index on the display.

**Definition** auxdisplay.h:119

[auxdisplay\_custom\_data](structauxdisplay__custom__data.md)

Structure for a custom command.

**Definition** auxdisplay.h:105

[auxdisplay\_custom\_data::options](structauxdisplay__custom__data.md#aa9c3b2af7c07e71e8cc5cd3eae058729)

uint32\_t options

Display-driver specific options for command.

**Definition** auxdisplay.h:113

[auxdisplay\_custom\_data::len](structauxdisplay__custom__data.md#ac995ecff9634acbc535a47b37134c6e1)

uint16\_t len

Length of supplied data.

**Definition** auxdisplay.h:110

[auxdisplay\_custom\_data::data](structauxdisplay__custom__data.md#acfd41be1569cc43bd09824c5e46b8d51)

uint8\_t \* data

Raw command data to be sent.

**Definition** auxdisplay.h:107

[auxdisplay\_light](structauxdisplay__light.md)

Light levels for brightness and/or backlight.

**Definition** auxdisplay.h:69

[auxdisplay\_light::minimum](structauxdisplay__light.md#a4cd0c416ce77a45949feb90ae9f254a1)

uint8\_t minimum

Minimum light level supported.

**Definition** auxdisplay.h:71

[auxdisplay\_light::maximum](structauxdisplay__light.md#a8f40f5fd3f825f1ee8c34891804cc003)

uint8\_t maximum

Maximum light level supported.

**Definition** auxdisplay.h:74

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
- [auxdisplay.h](auxdisplay_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
