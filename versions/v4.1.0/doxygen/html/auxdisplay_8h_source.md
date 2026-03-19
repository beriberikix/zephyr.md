---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/auxdisplay_8h_source.html
original_path: doxygen/html/auxdisplay_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

23

24#include <[stdint.h](stdint_8h.md)>

25#include <stddef.h>

26#include <[zephyr/kernel.h](kernel_8h.md)>

27#include <[zephyr/device.h](device_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 34](group__auxdisplay__interface.md#ga0bd1d97b360f3138887a5e3e4729e01b)#define AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED 0

35

[ 37](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [auxdisplay\_mode\_t](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2);

38

[ 40](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504)enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) {

[ 42](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) [AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) = 0,

43

[ 47](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28) [AUXDISPLAY\_POSITION\_RELATIVE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28),

48

[ 52](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558) [AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558),

53

[ 54](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23) [AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23),

55};

56

[ 58](group__auxdisplay__interface.md#ga5f95ac69e18091883e7121103014be10)enum [auxdisplay\_direction](group__auxdisplay__interface.md#ga5f95ac69e18091883e7121103014be10) {

[ 60](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599) [AUXDISPLAY\_DIRECTION\_RIGHT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599) = 0,

61

[ 63](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352) [AUXDISPLAY\_DIRECTION\_LEFT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10a4744906285765c922f4016f31db9e352),

64

[ 65](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3) [AUXDISPLAY\_DIRECTION\_COUNT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3),

66};

67

[ 71](structauxdisplay__light.md)struct [auxdisplay\_light](structauxdisplay__light.md) {

[ 73](structauxdisplay__light.md#a4cd0c416ce77a45949feb90ae9f254a1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minimum](structauxdisplay__light.md#a4cd0c416ce77a45949feb90ae9f254a1);

74

[ 76](structauxdisplay__light.md#a8f40f5fd3f825f1ee8c34891804cc003) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [maximum](structauxdisplay__light.md#a8f40f5fd3f825f1ee8c34891804cc003);

77};

78

[ 80](structauxdisplay__capabilities.md)struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) {

[ 82](structauxdisplay__capabilities.md#ac0fc352a5799328211ae6f8c94cdcd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [columns](structauxdisplay__capabilities.md#ac0fc352a5799328211ae6f8c94cdcd7a);

83

[ 85](structauxdisplay__capabilities.md#af1bcdc27adb678ca4447614a22366aba) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rows](structauxdisplay__capabilities.md#af1bcdc27adb678ca4447614a22366aba);

86

[ 88](structauxdisplay__capabilities.md#a55ac50abb253e64e9fb7be6542801dc9) [auxdisplay\_mode\_t](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2) [mode](structauxdisplay__capabilities.md#a55ac50abb253e64e9fb7be6542801dc9);

89

[ 91](structauxdisplay__capabilities.md#a15e3926754baaefffa1eff45573a59b1) struct [auxdisplay\_light](structauxdisplay__light.md) [brightness](structauxdisplay__capabilities.md#a15e3926754baaefffa1eff45573a59b1);

92

[ 94](structauxdisplay__capabilities.md#ace4d7b099428e5f7164c3e9e318c1feb) struct [auxdisplay\_light](structauxdisplay__light.md) [backlight](structauxdisplay__capabilities.md#ace4d7b099428e5f7164c3e9e318c1feb);

95

[ 97](structauxdisplay__capabilities.md#a4b66412a2000fe09f30c555befbd11d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [custom\_characters](structauxdisplay__capabilities.md#a4b66412a2000fe09f30c555befbd11d0);

98

[ 100](structauxdisplay__capabilities.md#ad77f390f5a6bdbebabc703fdc77322a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [custom\_character\_width](structauxdisplay__capabilities.md#ad77f390f5a6bdbebabc703fdc77322a3);

101

[ 103](structauxdisplay__capabilities.md#adc88b37e9f73a98560099c94c8797741) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [custom\_character\_height](structauxdisplay__capabilities.md#adc88b37e9f73a98560099c94c8797741);

104};

105

[ 107](structauxdisplay__custom__data.md)struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) {

[ 109](structauxdisplay__custom__data.md#acfd41be1569cc43bd09824c5e46b8d51) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structauxdisplay__custom__data.md#acfd41be1569cc43bd09824c5e46b8d51);

110

[ 112](structauxdisplay__custom__data.md#ac995ecff9634acbc535a47b37134c6e1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structauxdisplay__custom__data.md#ac995ecff9634acbc535a47b37134c6e1);

113

[ 115](structauxdisplay__custom__data.md#aa9c3b2af7c07e71e8cc5cd3eae058729) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [options](structauxdisplay__custom__data.md#aa9c3b2af7c07e71e8cc5cd3eae058729);

116};

117

[ 119](structauxdisplay__character.md)struct [auxdisplay\_character](structauxdisplay__character.md) {

[ 121](structauxdisplay__character.md#a9f0bb424b9918e0f0c07c12eb4235677) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [index](structauxdisplay__character.md#a9f0bb424b9918e0f0c07c12eb4235677);

122

[ 128](structauxdisplay__character.md#a4b011716576201818278aa853bfe542e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structauxdisplay__character.md#a4b011716576201818278aa853bfe542e);

129

[ 133](structauxdisplay__character.md#a217dd562886158efec238649fb4ade04) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [character\_code](structauxdisplay__character.md#a217dd562886158efec238649fb4ade04);

134};

135

141

147typedef int (\*auxdisplay\_display\_on\_t)(const struct [device](structdevice.md) \*dev);

148

154typedef int (\*auxdisplay\_display\_off\_t)(const struct [device](structdevice.md) \*dev);

155

161typedef int (\*auxdisplay\_cursor\_set\_enabled\_t)(const struct [device](structdevice.md) \*dev, bool enabled);

162

168typedef int (\*auxdisplay\_position\_blinking\_set\_enabled\_t)(const struct [device](structdevice.md) \*dev,

169 bool enabled);

170

176typedef int (\*auxdisplay\_cursor\_shift\_set\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) direction,

177 bool display\_shift);

178

184typedef int (\*auxdisplay\_cursor\_position\_set\_t)(const struct [device](structdevice.md) \*dev,

185 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

186 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

187

193typedef int (\*auxdisplay\_cursor\_position\_get\_t)(const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x,

194 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y);

195

201typedef int (\*auxdisplay\_display\_position\_set\_t)(const struct [device](structdevice.md) \*dev,

202 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

203 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

204

210typedef int (\*auxdisplay\_display\_position\_get\_t)(const struct [device](structdevice.md) \*dev, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x,

211 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y);

212

218typedef int (\*auxdisplay\_capabilities\_get\_t)(const struct [device](structdevice.md) \*dev,

219 struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \*capabilities);

220

226typedef int (\*auxdisplay\_clear\_t)(const struct [device](structdevice.md) \*dev);

227

234typedef int (\*auxdisplay\_brightness\_get\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*brightness);

235

241typedef int (\*auxdisplay\_brightness\_set\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness);

242

249typedef int (\*auxdisplay\_backlight\_get\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*backlight);

250

256typedef int (\*auxdisplay\_backlight\_set\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) backlight);

257

263typedef int (\*auxdisplay\_is\_busy\_t)(const struct [device](structdevice.md) \*dev);

264

270typedef int (\*auxdisplay\_custom\_character\_set\_t)(const struct [device](structdevice.md) \*dev,

271 struct [auxdisplay\_character](structauxdisplay__character.md) \*character);

272

278typedef int (\*auxdisplay\_write\_t)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

279

285typedef int (\*auxdisplay\_custom\_command\_t)(const struct [device](structdevice.md) \*dev,

286 struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \*command);

287

288\_\_subsystem struct auxdisplay\_driver\_api {

289 auxdisplay\_display\_on\_t display\_on;

290 auxdisplay\_display\_off\_t display\_off;

291 auxdisplay\_cursor\_set\_enabled\_t cursor\_set\_enabled;

292 auxdisplay\_position\_blinking\_set\_enabled\_t position\_blinking\_set\_enabled;

293 auxdisplay\_cursor\_shift\_set\_t cursor\_shift\_set;

294 auxdisplay\_cursor\_position\_set\_t cursor\_position\_set;

295 auxdisplay\_cursor\_position\_get\_t cursor\_position\_get;

296 auxdisplay\_display\_position\_set\_t display\_position\_set;

297 auxdisplay\_display\_position\_get\_t display\_position\_get;

298 auxdisplay\_capabilities\_get\_t capabilities\_get;

299 auxdisplay\_clear\_t clear;

300 auxdisplay\_brightness\_get\_t brightness\_get;

301 auxdisplay\_brightness\_set\_t brightness\_set;

302 auxdisplay\_backlight\_get\_t backlight\_get;

303 auxdisplay\_backlight\_set\_t backlight\_set;

304 auxdisplay\_is\_busy\_t is\_busy;

305 auxdisplay\_custom\_character\_set\_t custom\_character\_set;

306 auxdisplay\_write\_t write;

307 auxdisplay\_custom\_command\_t custom\_command;

308};

309

313

[ 323](group__auxdisplay__interface.md#gaffb3c1c41d810355fe2da3558ebba0c2)\_\_syscall int [auxdisplay\_display\_on](group__auxdisplay__interface.md#gaffb3c1c41d810355fe2da3558ebba0c2)(const struct [device](structdevice.md) \*dev);

324

325static inline int z\_impl\_auxdisplay\_display\_on(const struct [device](structdevice.md) \*dev)

326{

327 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

328

329 if (!api->display\_on) {

330 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

331 }

332

333 return api->display\_on(dev);

334}

335

[ 345](group__auxdisplay__interface.md#ga625f399720417715090793c7f6d63f7e)\_\_syscall int [auxdisplay\_display\_off](group__auxdisplay__interface.md#ga625f399720417715090793c7f6d63f7e)(const struct [device](structdevice.md) \*dev);

346

347static inline int z\_impl\_auxdisplay\_display\_off(const struct [device](structdevice.md) \*dev)

348{

349 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

350

351 if (!api->display\_off) {

352 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

353 }

354

355 return api->display\_off(dev);

356}

357

[ 368](group__auxdisplay__interface.md#ga7191475b362f728cc92eb07cb1f2ed00)\_\_syscall int [auxdisplay\_cursor\_set\_enabled](group__auxdisplay__interface.md#ga7191475b362f728cc92eb07cb1f2ed00)(const struct [device](structdevice.md) \*dev,

369 bool enabled);

370

371static inline int z\_impl\_auxdisplay\_cursor\_set\_enabled(const struct [device](structdevice.md) \*dev,

372 bool enabled)

373{

374 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

375

376 if (!api->cursor\_set\_enabled) {

377 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

378 }

379

380 return api->cursor\_set\_enabled(dev, enabled);

381}

382

[ 393](group__auxdisplay__interface.md#ga7102ec9941f8b3131a18e4ff7b640241)\_\_syscall int [auxdisplay\_position\_blinking\_set\_enabled](group__auxdisplay__interface.md#ga7102ec9941f8b3131a18e4ff7b640241)(const struct [device](structdevice.md) \*dev,

394 bool enabled);

395

396static inline int z\_impl\_auxdisplay\_position\_blinking\_set\_enabled(const struct [device](structdevice.md) \*dev,

397 bool enabled)

398{

399 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

400

401 if (!api->position\_blinking\_set\_enabled) {

402 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

403 }

404

405 return api->position\_blinking\_set\_enabled(dev, enabled);

406}

407

[ 421](group__auxdisplay__interface.md#gafb18729b4897cea83dbfc1c7241f5b2d)\_\_syscall int [auxdisplay\_cursor\_shift\_set](group__auxdisplay__interface.md#gafb18729b4897cea83dbfc1c7241f5b2d)(const struct [device](structdevice.md) \*dev,

422 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) direction, bool display\_shift);

423

424static inline int z\_impl\_auxdisplay\_cursor\_shift\_set(const struct [device](structdevice.md) \*dev,

425 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) direction,

426 bool display\_shift)

427{

428 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

429

430 if (!api->cursor\_shift\_set) {

431 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

432 }

433

434 if (direction >= [AUXDISPLAY\_DIRECTION\_COUNT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3)) {

435 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

436 }

437

438 return api->cursor\_shift\_set(dev, direction, display\_shift);

439}

440

[ 454](group__auxdisplay__interface.md#ga9c6302789d9cc9e481dd7c54ef370988)\_\_syscall int [auxdisplay\_cursor\_position\_set](group__auxdisplay__interface.md#ga9c6302789d9cc9e481dd7c54ef370988)(const struct [device](structdevice.md) \*dev,

455 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

456 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

457

458static inline int z\_impl\_auxdisplay\_cursor\_position\_set(const struct [device](structdevice.md) \*dev,

459 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

460 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y)

461{

462 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

463

464 if (!api->cursor\_position\_set) {

465 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

466 } else if (type >= [AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)) {

467 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

468 } else if (type == [AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) && (x < 0 || y < 0)) {

469 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

470 }

471

472 return api->cursor\_position\_set(dev, type, x, y);

473}

474

[ 487](group__auxdisplay__interface.md#ga37bd5403c876ff294be5ea72292de4b4)\_\_syscall int [auxdisplay\_cursor\_position\_get](group__auxdisplay__interface.md#ga37bd5403c876ff294be5ea72292de4b4)(const struct [device](structdevice.md) \*dev,

488 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y);

489

490static inline int z\_impl\_auxdisplay\_cursor\_position\_get(const struct [device](structdevice.md) \*dev,

491 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y)

492{

493 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

494

495 if (!api->cursor\_position\_get) {

496 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

497 }

498

499 return api->cursor\_position\_get(dev, x, y);

500}

501

[ 515](group__auxdisplay__interface.md#ga02e8e930203cfb1410752a0ffee9a34e)\_\_syscall int [auxdisplay\_display\_position\_set](group__auxdisplay__interface.md#ga02e8e930203cfb1410752a0ffee9a34e)(const struct [device](structdevice.md) \*dev,

516 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

517 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

518

519static inline int z\_impl\_auxdisplay\_display\_position\_set(const struct [device](structdevice.md) \*dev,

520 enum [auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504) type,

521 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y)

522{

523 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

524

525 if (!api->display\_position\_set) {

526 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

527 } else if (type >= [AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)) {

528 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

529 } else if (type == [AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404) && (x < 0 || y < 0)) {

530 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

531 }

532

533 return api->display\_position\_set(dev, type, x, y);

534}

535

[ 548](group__auxdisplay__interface.md#ga1f9e363765d715edb899901a14c54674)\_\_syscall int [auxdisplay\_display\_position\_get](group__auxdisplay__interface.md#ga1f9e363765d715edb899901a14c54674)(const struct [device](structdevice.md) \*dev,

549 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y);

550

551static inline int z\_impl\_auxdisplay\_display\_position\_get(const struct [device](structdevice.md) \*dev,

552 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*y)

553{

554 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

555

556 if (!api->display\_position\_get) {

557 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

558 }

559

560 return api->display\_position\_get(dev, x, y);

561}

562

[ 572](group__auxdisplay__interface.md#ga4dd5cba56d4b90b77ae8ad02122ef81c)\_\_syscall int [auxdisplay\_capabilities\_get](group__auxdisplay__interface.md#ga4dd5cba56d4b90b77ae8ad02122ef81c)(const struct [device](structdevice.md) \*dev,

573 struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \*capabilities);

574

575static inline int z\_impl\_auxdisplay\_capabilities\_get(const struct [device](structdevice.md) \*dev,

576 struct [auxdisplay\_capabilities](structauxdisplay__capabilities.md) \*capabilities)

577{

578 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

579

580 return api->capabilities\_get(dev, capabilities);

581}

582

[ 593](group__auxdisplay__interface.md#gaa5a643603353319946c823cc959b74b3)\_\_syscall int [auxdisplay\_clear](group__auxdisplay__interface.md#gaa5a643603353319946c823cc959b74b3)(const struct [device](structdevice.md) \*dev);

594

595static inline int z\_impl\_auxdisplay\_clear(const struct [device](structdevice.md) \*dev)

596{

597 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

598

599 return api->clear(dev);

600}

601

[ 612](group__auxdisplay__interface.md#ga1f5be6fefc759607d2859a648a1fb3b8)\_\_syscall int [auxdisplay\_brightness\_get](group__auxdisplay__interface.md#ga1f5be6fefc759607d2859a648a1fb3b8)(const struct [device](structdevice.md) \*dev,

613 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*brightness);

614

615static inline int z\_impl\_auxdisplay\_brightness\_get(const struct [device](structdevice.md) \*dev,

616 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*brightness)

617{

618 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

619

620 if (!api->brightness\_get) {

621 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

622 }

623

624 return api->brightness\_get(dev, brightness);

625}

626

[ 638](group__auxdisplay__interface.md#ga34b31b70fdc57e33fc46f1048cc25e1a)\_\_syscall int [auxdisplay\_brightness\_set](group__auxdisplay__interface.md#ga34b31b70fdc57e33fc46f1048cc25e1a)(const struct [device](structdevice.md) \*dev,

639 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness);

640

641static inline int z\_impl\_auxdisplay\_brightness\_set(const struct [device](structdevice.md) \*dev,

642 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness)

643{

644 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

645

646 if (!api->brightness\_set) {

647 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

648 }

649

650 return api->brightness\_set(dev, brightness);

651}

652

[ 663](group__auxdisplay__interface.md#gaf10ebdbe821894ccbeccb35bfa985fea)\_\_syscall int [auxdisplay\_backlight\_get](group__auxdisplay__interface.md#gaf10ebdbe821894ccbeccb35bfa985fea)(const struct [device](structdevice.md) \*dev,

664 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*backlight);

665

666static inline int z\_impl\_auxdisplay\_backlight\_get(const struct [device](structdevice.md) \*dev,

667 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*backlight)

668{

669 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

670

671 if (!api->backlight\_get) {

672 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

673 }

674

675 return api->backlight\_get(dev, backlight);

676}

677

[ 689](group__auxdisplay__interface.md#ga28aef24928543329c706513cc7e5b814)\_\_syscall int [auxdisplay\_backlight\_set](group__auxdisplay__interface.md#ga28aef24928543329c706513cc7e5b814)(const struct [device](structdevice.md) \*dev,

690 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) backlight);

691

692static inline int z\_impl\_auxdisplay\_backlight\_set(const struct [device](structdevice.md) \*dev,

693 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) backlight)

694{

695 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

696

697 if (!api->backlight\_set) {

698 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

699 }

700

701 return api->backlight\_set(dev, backlight);

702}

703

[ 714](group__auxdisplay__interface.md#ga2af115a23f370e0770b3c998ecf0b96b)\_\_syscall int [auxdisplay\_is\_busy](group__auxdisplay__interface.md#ga2af115a23f370e0770b3c998ecf0b96b)(const struct [device](structdevice.md) \*dev);

715

716static inline int z\_impl\_auxdisplay\_is\_busy(const struct [device](structdevice.md) \*dev)

717{

718 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

719

720 if (!api->is\_busy) {

721 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

722 }

723

724 return api->is\_busy(dev);

725}

726

[ 747](group__auxdisplay__interface.md#gaf03a1068b0aed1f27ee9e2e61066da08)\_\_syscall int [auxdisplay\_custom\_character\_set](group__auxdisplay__interface.md#gaf03a1068b0aed1f27ee9e2e61066da08)(const struct [device](structdevice.md) \*dev,

748 struct [auxdisplay\_character](structauxdisplay__character.md) \*character);

749

750static inline int z\_impl\_auxdisplay\_custom\_character\_set(const struct [device](structdevice.md) \*dev,

751 struct [auxdisplay\_character](structauxdisplay__character.md) \*character)

752{

753 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

754

755 if (!api->custom\_character\_set) {

756 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

757 }

758

759 return api->custom\_character\_set(dev, character);

760}

761

[ 773](group__auxdisplay__interface.md#ga231dd862cda34ea4c0c8870675556f8d)\_\_syscall int [auxdisplay\_write](group__auxdisplay__interface.md#ga231dd862cda34ea4c0c8870675556f8d)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

774 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

775

776static inline int z\_impl\_auxdisplay\_write(const struct [device](structdevice.md) \*dev,

777 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

778{

779 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

780

781 return api->write(dev, data, len);

782}

783

[ 795](group__auxdisplay__interface.md#ga87064057ae857f81431e6e9f139a6aaa)\_\_syscall int [auxdisplay\_custom\_command](group__auxdisplay__interface.md#ga87064057ae857f81431e6e9f139a6aaa)(const struct [device](structdevice.md) \*dev,

796 struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \*data);

797

798static inline int z\_impl\_auxdisplay\_custom\_command(const struct [device](structdevice.md) \*dev,

799 struct [auxdisplay\_custom\_data](structauxdisplay__custom__data.md) \*data)

800{

801 struct auxdisplay\_driver\_api \*api = (struct auxdisplay\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

802

803 if (!api->custom\_command) {

804 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

805 }

806

807 return api->custom\_command(dev, data);

808}

809

810#ifdef \_\_cplusplus

811}

812#endif

813

817

818#include <zephyr/syscalls/auxdisplay.h>

819

820#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_AUXDISPLAY\_H\_ \*/

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

**Definition** auxdisplay.h:58

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

**Definition** auxdisplay.h:37

[auxdisplay\_custom\_command](group__auxdisplay__interface.md#ga87064057ae857f81431e6e9f139a6aaa)

int auxdisplay\_custom\_command(const struct device \*dev, struct auxdisplay\_custom\_data \*data)

Send a custom command to the display (if supported by driver).

[auxdisplay\_position](group__auxdisplay__interface.md#ga98b0be37fc76df0ae4dec0bef6c94504)

auxdisplay\_position

Used for moving the cursor or display position.

**Definition** auxdisplay.h:40

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

**Definition** auxdisplay.h:63

[AUXDISPLAY\_DIRECTION\_COUNT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10ad58b4bb90fac2daff787329f34046ca3)

@ AUXDISPLAY\_DIRECTION\_COUNT

**Definition** auxdisplay.h:65

[AUXDISPLAY\_DIRECTION\_RIGHT](group__auxdisplay__interface.md#gga5f95ac69e18091883e7121103014be10afa02cc4de309a884fdc92e265cc2e599)

@ AUXDISPLAY\_DIRECTION\_RIGHT

Each character will be placed to the right of existing characters.

**Definition** auxdisplay.h:60

[AUXDISPLAY\_POSITION\_COUNT](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a2c95b6af944fa7a83d6f3168ee4e5d23)

@ AUXDISPLAY\_POSITION\_COUNT

**Definition** auxdisplay.h:54

[AUXDISPLAY\_POSITION\_ABSOLUTE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a3157133a1038e919792e4824849b9404)

@ AUXDISPLAY\_POSITION\_ABSOLUTE

Moves to specified X,Y position.

**Definition** auxdisplay.h:42

[AUXDISPLAY\_POSITION\_RELATIVE](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504a7783c940a94fb769f798e21f6ed3fa28)

@ AUXDISPLAY\_POSITION\_RELATIVE

Shifts current position by +/- X,Y position, does not take display direction into consideration.

**Definition** auxdisplay.h:47

[AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION](group__auxdisplay__interface.md#gga98b0be37fc76df0ae4dec0bef6c94504ae415e7b58e24cf78dab27a29c3c23558)

@ AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION

Shifts current position by +/- X,Y position, takes display direction into consideration.

**Definition** auxdisplay.h:52

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[kernel.h](kernel_8h.md)

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

**Definition** auxdisplay.h:80

[auxdisplay\_capabilities::brightness](structauxdisplay__capabilities.md#a15e3926754baaefffa1eff45573a59b1)

struct auxdisplay\_light brightness

Brightness details for display (if supported).

**Definition** auxdisplay.h:91

[auxdisplay\_capabilities::custom\_characters](structauxdisplay__capabilities.md#a4b66412a2000fe09f30c555befbd11d0)

uint8\_t custom\_characters

Number of custom characters supported by display (0 if unsupported).

**Definition** auxdisplay.h:97

[auxdisplay\_capabilities::mode](structauxdisplay__capabilities.md#a55ac50abb253e64e9fb7be6542801dc9)

auxdisplay\_mode\_t mode

Display-specific data (e.g.

**Definition** auxdisplay.h:88

[auxdisplay\_capabilities::columns](structauxdisplay__capabilities.md#ac0fc352a5799328211ae6f8c94cdcd7a)

uint16\_t columns

Number of character columns.

**Definition** auxdisplay.h:82

[auxdisplay\_capabilities::backlight](structauxdisplay__capabilities.md#ace4d7b099428e5f7164c3e9e318c1feb)

struct auxdisplay\_light backlight

Backlight details for display (if supported).

**Definition** auxdisplay.h:94

[auxdisplay\_capabilities::custom\_character\_width](structauxdisplay__capabilities.md#ad77f390f5a6bdbebabc703fdc77322a3)

uint8\_t custom\_character\_width

Width (in pixels) of a custom character, supplied custom characters should match.

**Definition** auxdisplay.h:100

[auxdisplay\_capabilities::custom\_character\_height](structauxdisplay__capabilities.md#adc88b37e9f73a98560099c94c8797741)

uint8\_t custom\_character\_height

Height (in pixels) of a custom character, supplied custom characters should match.

**Definition** auxdisplay.h:103

[auxdisplay\_capabilities::rows](structauxdisplay__capabilities.md#af1bcdc27adb678ca4447614a22366aba)

uint16\_t rows

Number of character rows.

**Definition** auxdisplay.h:85

[auxdisplay\_character](structauxdisplay__character.md)

Structure for a custom character.

**Definition** auxdisplay.h:119

[auxdisplay\_character::character\_code](structauxdisplay__character.md#a217dd562886158efec238649fb4ade04)

uint8\_t character\_code

Will be updated with custom character index to use in the display write function to disaplay this cus...

**Definition** auxdisplay.h:133

[auxdisplay\_character::data](structauxdisplay__character.md#a4b011716576201818278aa853bfe542e)

uint8\_t \* data

Custom character pixel data, a character must be valid for a display consisting of a uint8 array of s...

**Definition** auxdisplay.h:128

[auxdisplay\_character::index](structauxdisplay__character.md#a9f0bb424b9918e0f0c07c12eb4235677)

uint8\_t index

Custom character index on the display.

**Definition** auxdisplay.h:121

[auxdisplay\_custom\_data](structauxdisplay__custom__data.md)

Structure for a custom command.

**Definition** auxdisplay.h:107

[auxdisplay\_custom\_data::options](structauxdisplay__custom__data.md#aa9c3b2af7c07e71e8cc5cd3eae058729)

uint32\_t options

Display-driver specific options for command.

**Definition** auxdisplay.h:115

[auxdisplay\_custom\_data::len](structauxdisplay__custom__data.md#ac995ecff9634acbc535a47b37134c6e1)

uint16\_t len

Length of supplied data.

**Definition** auxdisplay.h:112

[auxdisplay\_custom\_data::data](structauxdisplay__custom__data.md#acfd41be1569cc43bd09824c5e46b8d51)

uint8\_t \* data

Raw command data to be sent.

**Definition** auxdisplay.h:109

[auxdisplay\_light](structauxdisplay__light.md)

Light levels for brightness and/or backlight.

**Definition** auxdisplay.h:71

[auxdisplay\_light::minimum](structauxdisplay__light.md#a4cd0c416ce77a45949feb90ae9f254a1)

uint8\_t minimum

Minimum light level supported.

**Definition** auxdisplay.h:73

[auxdisplay\_light::maximum](structauxdisplay__light.md#a8f40f5fd3f825f1ee8c34891804cc003)

uint8\_t maximum

Maximum light level supported.

**Definition** auxdisplay.h:76

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [auxdisplay.h](auxdisplay_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
