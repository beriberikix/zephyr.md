---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/espi__saf_8h_source.html
original_path: doxygen/html/espi__saf_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_saf.h

[Go to the documentation of this file.](espi__saf_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_ESPI\_SAF\_H\_

13#define ZEPHYR\_INCLUDE\_ESPI\_SAF\_H\_

14

15#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <[zephyr/device.h](device_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

30

86

87

92

93

95

96struct espi\_saf\_hw\_cfg;

97struct espi\_saf\_flash\_cfg;

98struct espi\_saf\_pr;

99

[ 103](structespi__saf__cfg.md)struct [espi\_saf\_cfg](structespi__saf__cfg.md) {

[ 104](structespi__saf__cfg.md#ab07ab3b33980f6865cbadbbcb5e203c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [nflash\_devices](structespi__saf__cfg.md#ab07ab3b33980f6865cbadbbcb5e203c0);

[ 105](structespi__saf__cfg.md#a20da4ce3549c53adb038dab7a5bed8a8) struct espi\_saf\_hw\_cfg [hwcfg](structespi__saf__cfg.md#a20da4ce3549c53adb038dab7a5bed8a8);

[ 106](structespi__saf__cfg.md#a99d90bcf04f3f09ac5fb739b390a42c8) struct espi\_saf\_flash\_cfg \*[flash\_cfgs](structespi__saf__cfg.md#a99d90bcf04f3f09ac5fb739b390a42c8);

107};

108

[ 112](structespi__saf__packet.md)struct [espi\_saf\_packet](structespi__saf__packet.md) {

[ 113](structespi__saf__packet.md#a8ee8a45b3490746f893f6b17fb96b815) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flash\_addr](structespi__saf__packet.md#a8ee8a45b3490746f893f6b17fb96b815);

[ 114](structespi__saf__packet.md#a00bfcab9fe2b928be3ea3485c5e91401) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structespi__saf__packet.md#a00bfcab9fe2b928be3ea3485c5e91401);

[ 115](structespi__saf__packet.md#af88017b76b64b77c95d9684981f48482) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structespi__saf__packet.md#af88017b76b64b77c95d9684981f48482);

116};

117

118/\*

119 \*defined in espi.h

120 \* struct espi\_callback

121 \* typedef void (\*espi\_callback\_handler\_t)()

122 \*/

123

131typedef int (\*espi\_saf\_api\_config)(const struct [device](structdevice.md) \*dev,

132 const struct [espi\_saf\_cfg](structespi__saf__cfg.md) \*cfg);

133

134typedef int (\*espi\_saf\_api\_set\_protection\_regions)(

135 const struct [device](structdevice.md) \*dev,

136 const struct espi\_saf\_protection \*pr);

137

138typedef int (\*espi\_saf\_api\_activate)(const struct [device](structdevice.md) \*dev);

139

140typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*espi\_saf\_api\_get\_channel\_status)(const struct [device](structdevice.md) \*dev);

141

142typedef int (\*espi\_saf\_api\_flash\_read)(const struct [device](structdevice.md) \*dev,

143 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt);

144typedef int (\*espi\_saf\_api\_flash\_write)(const struct [device](structdevice.md) \*dev,

145 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt);

146typedef int (\*espi\_saf\_api\_flash\_erase)(const struct [device](structdevice.md) \*dev,

147 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt);

148typedef int (\*espi\_saf\_api\_flash\_unsuccess)(const struct [device](structdevice.md) \*dev,

149 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt);

150/\* Callbacks and traffic intercept \*/

151typedef int (\*espi\_saf\_api\_manage\_callback)(const struct [device](structdevice.md) \*dev,

152 struct espi\_callback \*callback,

153 bool set);

154

155\_\_subsystem struct espi\_saf\_driver\_api {

156 espi\_saf\_api\_config config;

157 espi\_saf\_api\_set\_protection\_regions set\_protection\_regions;

158 espi\_saf\_api\_activate activate;

159 espi\_saf\_api\_get\_channel\_status get\_channel\_status;

160 espi\_saf\_api\_flash\_read [flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f);

161 espi\_saf\_api\_flash\_write [flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324);

162 espi\_saf\_api\_flash\_erase [flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95);

163 espi\_saf\_api\_flash\_unsuccess flash\_unsuccess;

164 espi\_saf\_api\_manage\_callback manage\_callback;

165};

166

170

[ 219](group__espi__interface.md#ga34b0f6336aec45016d97528767b09434)\_\_syscall int [espi\_saf\_config](group__espi__interface.md#ga34b0f6336aec45016d97528767b09434)(const struct [device](structdevice.md) \*dev,

220 const struct [espi\_saf\_cfg](structespi__saf__cfg.md) \*cfg);

221

222static inline int z\_impl\_espi\_saf\_config(const struct [device](structdevice.md) \*dev,

223 const struct [espi\_saf\_cfg](structespi__saf__cfg.md) \*cfg)

224{

225 const struct espi\_saf\_driver\_api \*api =

226 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

227

228 return api->config(dev, cfg);

229}

230

[ 245](group__espi__interface.md#ga273a9707f3ca501ed2dd3019cdeaa363)\_\_syscall int [espi\_saf\_set\_protection\_regions](group__espi__interface.md#ga273a9707f3ca501ed2dd3019cdeaa363)(

246 const struct [device](structdevice.md) \*dev,

247 const struct espi\_saf\_protection \*pr);

248

249static inline int z\_impl\_espi\_saf\_set\_protection\_regions(

250 const struct [device](structdevice.md) \*dev,

251 const struct espi\_saf\_protection \*pr)

252{

253 const struct espi\_saf\_driver\_api \*api =

254 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

255

256 return api->set\_protection\_regions(dev, pr);

257}

258

[ 271](group__espi__interface.md#gaafe30738c18a16b056ed8dcf8638eb84)\_\_syscall int [espi\_saf\_activate](group__espi__interface.md#gaafe30738c18a16b056ed8dcf8638eb84)(const struct [device](structdevice.md) \*dev);

272

273static inline int z\_impl\_espi\_saf\_activate(const struct [device](structdevice.md) \*dev)

274{

275 const struct espi\_saf\_driver\_api \*api =

276 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

277

278 return api->activate(dev);

279}

280

[ 291](group__espi__interface.md#ga8b53a93559f0c67953e283f59107aa22)\_\_syscall bool [espi\_saf\_get\_channel\_status](group__espi__interface.md#ga8b53a93559f0c67953e283f59107aa22)(const struct [device](structdevice.md) \*dev);

292

293static inline bool z\_impl\_espi\_saf\_get\_channel\_status(

294 const struct [device](structdevice.md) \*dev)

295{

296 const struct espi\_saf\_driver\_api \*api =

297 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

298

299 return api->get\_channel\_status(dev);

300}

301

[ 315](group__espi__interface.md#ga0f5017eac05f928e635fec8e5f877c7d)\_\_syscall int [espi\_saf\_flash\_read](group__espi__interface.md#ga0f5017eac05f928e635fec8e5f877c7d)(const struct [device](structdevice.md) \*dev,

316 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt);

317

318static inline int z\_impl\_espi\_saf\_flash\_read(const struct [device](structdevice.md) \*dev,

319 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt)

320{

321 const struct espi\_saf\_driver\_api \*api =

322 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

323

324 if (!api->flash\_read) {

325 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

326 }

327

328 return api->flash\_read(dev, pckt);

329}

330

[ 344](group__espi__interface.md#ga104175f74019e58b8b7901f3dae245db)\_\_syscall int [espi\_saf\_flash\_write](group__espi__interface.md#ga104175f74019e58b8b7901f3dae245db)(const struct [device](structdevice.md) \*dev,

345 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt);

346

347static inline int z\_impl\_espi\_saf\_flash\_write(const struct [device](structdevice.md) \*dev,

348 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt)

349{

350 const struct espi\_saf\_driver\_api \*api =

351 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

352

353 if (!api->flash\_write) {

354 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

355 }

356

357 return api->flash\_write(dev, pckt);

358}

359

[ 373](group__espi__interface.md#ga15855a2ac593b97dc1a3e83ac9eda300)\_\_syscall int [espi\_saf\_flash\_erase](group__espi__interface.md#ga15855a2ac593b97dc1a3e83ac9eda300)(const struct [device](structdevice.md) \*dev,

374 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt);

375

376static inline int z\_impl\_espi\_saf\_flash\_erase(const struct [device](structdevice.md) \*dev,

377 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt)

378{

379 const struct espi\_saf\_driver\_api \*api =

380 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

381

382 if (!api->flash\_erase) {

383 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

384 }

385

386 return api->flash\_erase(dev, pckt);

387}

388

[ 402](group__espi__interface.md#ga6c54d9274b1a8e883484bd892f606fd5)\_\_syscall int [espi\_saf\_flash\_unsuccess](group__espi__interface.md#ga6c54d9274b1a8e883484bd892f606fd5)(const struct [device](structdevice.md) \*dev,

403 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt);

404

405static inline int z\_impl\_espi\_saf\_flash\_unsuccess(const struct [device](structdevice.md) \*dev,

406 struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt)

407{

408 const struct espi\_saf\_driver\_api \*api =

409 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

410

411 if (!api->flash\_unsuccess) {

412 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

413 }

414

415 return api->flash\_unsuccess(dev, pckt);

416}

417

479

[ 488](group__espi__interface.md#ga324283c28e6a33be112571621d1568e8)static inline void [espi\_saf\_init\_callback](group__espi__interface.md#ga324283c28e6a33be112571621d1568e8)(struct espi\_callback \*callback,

489 [espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46) handler,

490 enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) evt\_type)

491{

492 \_\_ASSERT(callback, "Callback pointer should not be NULL");

493 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

494

495 callback->handler = handler;

496 callback->evt\_type = evt\_type;

497}

498

[ 511](group__espi__interface.md#gadb881f847082f713bb0159d1e474980a)static inline int [espi\_saf\_add\_callback](group__espi__interface.md#gadb881f847082f713bb0159d1e474980a)(const struct [device](structdevice.md) \*dev,

512 struct espi\_callback \*callback)

513{

514 const struct espi\_saf\_driver\_api \*api =

515 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

516

517 if (!api->manage\_callback) {

518 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

519 }

520

521 return api->manage\_callback(dev, callback, true);

522}

523

[ 540](group__espi__interface.md#gaf987842bc7dad310c7270aed50086af9)static inline int [espi\_saf\_remove\_callback](group__espi__interface.md#gaf987842bc7dad310c7270aed50086af9)(const struct [device](structdevice.md) \*dev,

541 struct espi\_callback \*callback)

542{

543 const struct espi\_saf\_driver\_api \*api =

544 (const struct espi\_saf\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

545

546 if (!api->manage\_callback) {

547 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

548 }

549

550 return api->manage\_callback(dev, callback, false);

551}

552

553#ifdef \_\_cplusplus

554}

555#endif

556

560#include <zephyr/syscalls/espi\_saf.h>

561#endif /\* ZEPHYR\_INCLUDE\_ESPI\_SAF\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[device.h](device_8h.md)

[espi\_saf\_flash\_read](group__espi__interface.md#ga0f5017eac05f928e635fec8e5f877c7d)

int espi\_saf\_flash\_read(const struct device \*dev, struct espi\_saf\_packet \*pckt)

Sends a read request packet for slave attached flash.

[espi\_saf\_flash\_write](group__espi__interface.md#ga104175f74019e58b8b7901f3dae245db)

int espi\_saf\_flash\_write(const struct device \*dev, struct espi\_saf\_packet \*pckt)

Sends a write request packet for slave attached flash.

[espi\_saf\_flash\_erase](group__espi__interface.md#ga15855a2ac593b97dc1a3e83ac9eda300)

int espi\_saf\_flash\_erase(const struct device \*dev, struct espi\_saf\_packet \*pckt)

Sends a write request packet for slave attached flash.

[espi\_saf\_set\_protection\_regions](group__espi__interface.md#ga273a9707f3ca501ed2dd3019cdeaa363)

int espi\_saf\_set\_protection\_regions(const struct device \*dev, const struct espi\_saf\_protection \*pr)

Set one or more SAF protection regions.

[espi\_saf\_init\_callback](group__espi__interface.md#ga324283c28e6a33be112571621d1568e8)

static void espi\_saf\_init\_callback(struct espi\_callback \*callback, espi\_callback\_handler\_t handler, enum espi\_bus\_event evt\_type)

Callback model.

**Definition** espi\_saf.h:488

[espi\_saf\_config](group__espi__interface.md#ga34b0f6336aec45016d97528767b09434)

int espi\_saf\_config(const struct device \*dev, const struct espi\_saf\_cfg \*cfg)

Configure operation of a eSPI controller.

[espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128)

espi\_bus\_event

eSPI bus event.

**Definition** espi.h:114

[espi\_saf\_flash\_unsuccess](group__espi__interface.md#ga6c54d9274b1a8e883484bd892f606fd5)

int espi\_saf\_flash\_unsuccess(const struct device \*dev, struct espi\_saf\_packet \*pckt)

Response unsuccessful completion for slave attached flash.

[espi\_saf\_get\_channel\_status](group__espi__interface.md#ga8b53a93559f0c67953e283f59107aa22)

bool espi\_saf\_get\_channel\_status(const struct device \*dev)

Query to see if SAF is ready.

[espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46)

void(\* espi\_callback\_handler\_t)(const struct device \*dev, struct espi\_callback \*cb, struct espi\_event espi\_evt)

Define the application callback handler function signature.

**Definition** espi.h:413

[espi\_saf\_activate](group__espi__interface.md#gaafe30738c18a16b056ed8dcf8638eb84)

int espi\_saf\_activate(const struct device \*dev)

Activate SAF block.

[espi\_saf\_add\_callback](group__espi__interface.md#gadb881f847082f713bb0159d1e474980a)

static int espi\_saf\_add\_callback(const struct device \*dev, struct espi\_callback \*callback)

Add an application callback.

**Definition** espi\_saf.h:511

[espi\_saf\_remove\_callback](group__espi__interface.md#gaf987842bc7dad310c7270aed50086af9)

static int espi\_saf\_remove\_callback(const struct device \*dev, struct espi\_callback \*callback)

Remove an application callback.

**Definition** espi\_saf.h:540

[flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)

int flash\_erase(const struct device \*dev, off\_t offset, size\_t size)

Erase part or all of a flash memory.

[flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)

int flash\_write(const struct device \*dev, off\_t offset, const void \*data, size\_t len)

Write buffer into flash memory.

[flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)

int flash\_read(const struct device \*dev, off\_t offset, void \*data, size\_t len)

Read data from flash.

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[types.h](include_2zephyr_2types_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[espi\_saf\_cfg](structespi__saf__cfg.md)

eSPI SAF configuration parameters

**Definition** espi\_saf.h:103

[espi\_saf\_cfg::hwcfg](structespi__saf__cfg.md#a20da4ce3549c53adb038dab7a5bed8a8)

struct espi\_saf\_hw\_cfg hwcfg

**Definition** espi\_saf.h:105

[espi\_saf\_cfg::flash\_cfgs](structespi__saf__cfg.md#a99d90bcf04f3f09ac5fb739b390a42c8)

struct espi\_saf\_flash\_cfg \* flash\_cfgs

**Definition** espi\_saf.h:106

[espi\_saf\_cfg::nflash\_devices](structespi__saf__cfg.md#ab07ab3b33980f6865cbadbbcb5e203c0)

uint8\_t nflash\_devices

**Definition** espi\_saf.h:104

[espi\_saf\_packet](structespi__saf__packet.md)

eSPI SAF transaction packet format

**Definition** espi\_saf.h:112

[espi\_saf\_packet::buf](structespi__saf__packet.md#a00bfcab9fe2b928be3ea3485c5e91401)

uint8\_t \* buf

**Definition** espi\_saf.h:114

[espi\_saf\_packet::flash\_addr](structespi__saf__packet.md#a8ee8a45b3490746f893f6b17fb96b815)

uint32\_t flash\_addr

**Definition** espi\_saf.h:113

[espi\_saf\_packet::len](structespi__saf__packet.md#af88017b76b64b77c95d9684981f48482)

uint32\_t len

**Definition** espi\_saf.h:115

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [espi\_saf.h](espi__saf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
