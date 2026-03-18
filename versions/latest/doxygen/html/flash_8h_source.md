---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/flash_8h_source.html
original_path: doxygen/html/flash_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash.h

[Go to the documentation of this file.](flash_8h.md)

1/\*

2 \* Copyright (c) 2017 Nordic Semiconductor ASA

3 \* Copyright (c) 2016 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_H\_

15

22

23#include <[errno.h](errno_8h.md)>

24

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <stddef.h>

27#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

28#include <[zephyr/device.h](device_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 35](structflash__pages__layout.md)struct [flash\_pages\_layout](structflash__pages__layout.md) {

[ 36](structflash__pages__layout.md#af5e496e680dbe9f4fd2738e6dc2534ec) size\_t [pages\_count](structflash__pages__layout.md#af5e496e680dbe9f4fd2738e6dc2534ec); /\* count of pages sequence of the same size \*/

[ 37](structflash__pages__layout.md#aabdad4d8a197936f7756950bc73326ee) size\_t [pages\_size](structflash__pages__layout.md#aabdad4d8a197936f7756950bc73326ee);

38};

39#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

40

44

51

[ 57](structflash__parameters.md)struct [flash\_parameters](structflash__parameters.md) {

[ 58](structflash__parameters.md#a9795a3e4fae4d7b81745e876f62ab3a8) const size\_t [write\_block\_size](structflash__parameters.md#a9795a3e4fae4d7b81745e876f62ab3a8);

[ 59](structflash__parameters.md#a218b0cbc797572ce096d0d6f55475ff9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [erase\_value](structflash__parameters.md#a218b0cbc797572ce096d0d6f55475ff9); /\* Byte value of erased flash \*/

60};

61

65

70

[ 71](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290)typedef int (\*[flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

72 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

73 size\_t len);

[ 82](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)typedef int (\*[flash\_api\_write](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

83 const void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t len);

84

[ 93](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5)typedef int (\*[flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

94 size\_t size);

95

96typedef const struct [flash\_parameters](structflash__parameters.md)\* (\*flash\_api\_get\_parameters)(const struct [device](structdevice.md) \*dev);

97

98#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 120](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5)typedef void (\*[flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5))(const struct [device](structdevice.md) \*dev,

121 const struct [flash\_pages\_layout](structflash__pages__layout.md) \*\*[layout](bindesc_8h.md#af8174bbae9567135fe17f1e55621f641),

122 size\_t \*layout\_size);

123#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

124

[ 125](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5)typedef int (\*[flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

126 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t len);

[ 127](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994)typedef int (\*[flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id);

[ 128](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2)typedef int (\*[flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

129 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out);

130

[ 131](structflash__driver__api.md)\_\_subsystem struct [flash\_driver\_api](structflash__driver__api.md) {

[ 132](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480) [flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290) [read](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480);

[ 133](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4) [flash\_api\_write](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba) [write](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4);

[ 134](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15) [flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5) [erase](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15);

[ 135](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc) [flash\_api\_get\_parameters](group__flash__internal__interface.md#ga2dee3874cb1be4ef4dab599963c30e70) [get\_parameters](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc);

136#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 137](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b) [flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5) [page\_layout](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b);

138#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

139#if defined(CONFIG\_FLASH\_JESD216\_API)

[ 140](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c) [flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5) [sfdp\_read](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c);

[ 141](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b) [flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994) [read\_jedec\_id](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b);

142#endif /\* CONFIG\_FLASH\_JESD216\_API \*/

143#if defined(CONFIG\_FLASH\_EX\_OP\_ENABLED)

144 [flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2) ex\_op;

145#endif /\* CONFIG\_FLASH\_EX\_OP\_ENABLED \*/

146};

147

151

156

[ 170](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)\_\_syscall int [flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data,

171 size\_t len);

172

173static inline int z\_impl\_flash\_read(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

174 void \*data,

175 size\_t len)

176{

177 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

178 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

179

180 return api->read(dev, offset, data, len);

181}

182

[ 201](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)\_\_syscall int [flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

202 const void \*data,

203 size\_t len);

204

205static inline int z\_impl\_flash\_write(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

206 const void \*data, size\_t len)

207{

208 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

209 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

210 int rc;

211

212 rc = api->write(dev, offset, data, len);

213

214 return rc;

215}

216

[ 238](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)\_\_syscall int [flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t size);

239

240static inline int z\_impl\_flash\_erase(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

241 size\_t size)

242{

243 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

244 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

245 int rc;

246

247 rc = api->erase(dev, offset, size);

248

249 return rc;

250}

251

[ 252](structflash__pages__info.md)struct [flash\_pages\_info](structflash__pages__info.md) {

[ 253](structflash__pages__info.md#a5c841987fef1636b83141871456ea867) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [start\_offset](structflash__pages__info.md#a5c841987fef1636b83141871456ea867); /\* offset from the base of flash address \*/

[ 254](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1) size\_t [size](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1);

[ 255](structflash__pages__info.md#adca463710082164f4323d3011235eb6f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structflash__pages__info.md#adca463710082164f4323d3011235eb6f);

256};

257

258#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 268](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)\_\_syscall int [flash\_get\_page\_info\_by\_offs](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)(const struct [device](structdevice.md) \*dev,

269 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

270 struct [flash\_pages\_info](structflash__pages__info.md) \*info);

271

[ 281](group__flash__interface.md#gaae733082fa92f80261d5895d3f81a98b)\_\_syscall int [flash\_get\_page\_info\_by\_idx](group__flash__interface.md#gaae733082fa92f80261d5895d3f81a98b)(const struct [device](structdevice.md) \*dev,

282 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) page\_index,

283 struct [flash\_pages\_info](structflash__pages__info.md) \*info);

284

[ 292](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)\_\_syscall size\_t [flash\_get\_page\_count](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)(const struct [device](structdevice.md) \*dev);

293

[ 304](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f))(const struct [flash\_pages\_info](structflash__pages__info.md) \*info, void \*data);

305

[ 318](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe)void [flash\_page\_foreach](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe)(const struct [device](structdevice.md) \*dev, [flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f) cb,

319 void \*data);

320#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

321

322#if defined(CONFIG\_FLASH\_JESD216\_API)

[ 343](group__flash__interface.md#ga8e9b921299bfb059bf72445a2ffa5a97)\_\_syscall int [flash\_sfdp\_read](group__flash__interface.md#ga8e9b921299bfb059bf72445a2ffa5a97)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

344 void \*data, size\_t len);

345

346static inline int z\_impl\_flash\_sfdp\_read(const struct [device](structdevice.md) \*dev,

347 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

348 void \*data, size\_t len)

349{

350 int rv = -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

351 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

352 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

353

354 if (api->sfdp\_read != NULL) {

355 rv = api->sfdp\_read(dev, offset, data, len);

356 }

357 return rv;

358}

359

[ 371](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7)\_\_syscall int [flash\_read\_jedec\_id](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id);

372

373static inline int z\_impl\_flash\_read\_jedec\_id(const struct [device](structdevice.md) \*dev,

374 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id)

375{

376 int rv = -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

377 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

378 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

379

380 if (api->read\_jedec\_id != NULL) {

381 rv = api->read\_jedec\_id(dev, id);

382 }

383 return rv;

384}

385#endif /\* CONFIG\_FLASH\_JESD216\_API \*/

386

[ 398](group__flash__interface.md#gaadfb323bc1b4efa39e7bc0a048c472a6)\_\_syscall size\_t [flash\_get\_write\_block\_size](group__flash__interface.md#gaadfb323bc1b4efa39e7bc0a048c472a6)(const struct [device](structdevice.md) \*dev);

399

400static inline size\_t z\_impl\_flash\_get\_write\_block\_size(const struct [device](structdevice.md) \*dev)

401{

402 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

403 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

404

405 return api->get\_parameters(dev)->write\_block\_size;

406}

407

408

[ 420](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3)\_\_syscall const struct [flash\_parameters](structflash__parameters.md) \*[flash\_get\_parameters](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3)(const struct [device](structdevice.md) \*dev);

421

422static inline const struct [flash\_parameters](structflash__parameters.md) \*z\_impl\_flash\_get\_parameters(const struct [device](structdevice.md) \*dev)

423{

424 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

425 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

426

427 return api->get\_parameters(dev);

428}

429

[ 455](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c)\_\_syscall int [flash\_ex\_op](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

456 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out);

457

458/\*

459 \* Extended operation interface provides flexible way for supporting flash

460 \* controller features. Code space is divided equally into Zephyr codes

461 \* (MSb == 0) and vendor codes (MSb == 1). This way we can easily add extended

462 \* operations to the drivers without cluttering the API or problems with API

463 \* incompatibility. Extended operation can be promoted from vendor codes to

464 \* Zephyr codes if the feature is available in most flash controllers and

465 \* can be represented in the same way.

466 \*

467 \* It's not forbidden to have operation in Zephyr codes and vendor codes for

468 \* the same functionality. In this case, vendor operation could provide more

469 \* specific access when abstraction in Zephyr counterpart is insufficient.

470 \*/

[ 471](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)#define FLASH\_EX\_OP\_VENDOR\_BASE 0x8000

[ 472](group__flash__interface.md#gafc0aa899b7ea452d048d8ee67d2e6f06)#define FLASH\_EX\_OP\_IS\_VENDOR(c) ((c) & FLASH\_EX\_OP\_VENDOR\_BASE)

473

[ 477](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51)enum [flash\_ex\_op\_types](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51) {

478 /\*

479 \* Reset flash device.

480 \*/

[ 481](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd) [FLASH\_EX\_OP\_RESET](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd) = 0,

482};

483

484static inline int z\_impl\_flash\_ex\_op(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

485 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out)

486{

487#if defined(CONFIG\_FLASH\_EX\_OP\_ENABLED)

488 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

489 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

490

491 if (api->ex\_op == NULL) {

492 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

493 }

494

495 return api->ex\_op(dev, code, in, out);

496#else

497 ARG\_UNUSED(dev);

498 ARG\_UNUSED(code);

499 ARG\_UNUSED(in);

500 ARG\_UNUSED(out);

501

502 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

503#endif /\* CONFIG\_FLASH\_EX\_OP\_ENABLED \*/

504}

505

506#ifdef \_\_cplusplus

507}

508#endif

509

513

514#include <syscalls/flash.h>

515

516#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_H\_ \*/

[layout](bindesc_8h.md#af8174bbae9567135fe17f1e55621f641)

Incorrect memory layout

**Definition** bindesc.h:288

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)

int flash\_erase(const struct device \*dev, off\_t offset, size\_t size)

Erase part or all of a flash memory.

[flash\_get\_parameters](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3)

const struct flash\_parameters \* flash\_get\_parameters(const struct device \*dev)

Get pointer to flash\_parameters structure.

[flash\_page\_foreach](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe)

void flash\_page\_foreach(const struct device \*dev, flash\_page\_cb cb, void \*data)

Iterate over all flash pages on a device.

[flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)

bool(\* flash\_page\_cb)(const struct flash\_pages\_info \*info, void \*data)

Callback type for iterating over flash pages present on a device.

**Definition** flash.h:304

[flash\_ex\_op](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c)

int flash\_ex\_op(const struct device \*dev, uint16\_t code, const uintptr\_t in, void \*out)

Execute flash extended operation on given device.

[flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)

int flash\_write(const struct device \*dev, off\_t offset, const void \*data, size\_t len)

Write buffer into flash memory.

[flash\_sfdp\_read](group__flash__interface.md#ga8e9b921299bfb059bf72445a2ffa5a97)

int flash\_sfdp\_read(const struct device \*dev, off\_t offset, void \*data, size\_t len)

Read data from Serial Flash Discoverable Parameters.

[flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)

int flash\_read(const struct device \*dev, off\_t offset, void \*data, size\_t len)

Read data from flash.

[flash\_get\_write\_block\_size](group__flash__interface.md#gaadfb323bc1b4efa39e7bc0a048c472a6)

size\_t flash\_get\_write\_block\_size(const struct device \*dev)

Get the minimum write block size supported by the driver.

[flash\_get\_page\_info\_by\_idx](group__flash__interface.md#gaae733082fa92f80261d5895d3f81a98b)

int flash\_get\_page\_info\_by\_idx(const struct device \*dev, uint32\_t page\_index, struct flash\_pages\_info \*info)

Get the size and start offset of flash page of certain index.

[flash\_read\_jedec\_id](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7)

int flash\_read\_jedec\_id(const struct device \*dev, uint8\_t \*id)

Read the JEDEC ID from a compatible flash device.

[flash\_ex\_op\_types](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51)

flash\_ex\_op\_types

Enumeration for extra flash operations.

**Definition** flash.h:477

[flash\_get\_page\_count](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)

size\_t flash\_get\_page\_count(const struct device \*dev)

Get the total number of flash pages.

[flash\_get\_page\_info\_by\_offs](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)

int flash\_get\_page\_info\_by\_offs(const struct device \*dev, off\_t offset, struct flash\_pages\_info \*info)

Get the size and start offset of flash page at certain flash offset.

[FLASH\_EX\_OP\_RESET](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd)

@ FLASH\_EX\_OP\_RESET

**Definition** flash.h:481

[flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994)

int(\* flash\_api\_read\_jedec\_id)(const struct device \*dev, uint8\_t \*id)

**Definition** flash.h:127

[flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5)

int(\* flash\_api\_erase)(const struct device \*dev, off\_t offset, size\_t size)

Flash erase implementation handler type.

**Definition** flash.h:93

[flash\_api\_get\_parameters](group__flash__internal__interface.md#ga2dee3874cb1be4ef4dab599963c30e70)

const struct flash\_parameters \*(\* flash\_api\_get\_parameters)(const struct device \*dev)

**Definition** flash.h:96

[flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290)

int(\* flash\_api\_read)(const struct device \*dev, off\_t offset, void \*data, size\_t len)

**Definition** flash.h:71

[flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5)

void(\* flash\_api\_pages\_layout)(const struct device \*dev, const struct flash\_pages\_layout \*\*layout, size\_t \*layout\_size)

Retrieve a flash device's layout.

**Definition** flash.h:120

[flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5)

int(\* flash\_api\_sfdp\_read)(const struct device \*dev, off\_t offset, void \*data, size\_t len)

**Definition** flash.h:125

[flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2)

int(\* flash\_api\_ex\_op)(const struct device \*dev, uint16\_t code, const uintptr\_t in, void \*out)

**Definition** flash.h:128

[flash\_api\_write](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)

int(\* flash\_api\_write)(const struct device \*dev, off\_t offset, const void \*data, size\_t len)

Flash write implementation handler type.

**Definition** flash.h:82

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

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

[flash\_driver\_api](structflash__driver__api.md)

**Definition** flash.h:131

[flash\_driver\_api::sfdp\_read](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c)

flash\_api\_sfdp\_read sfdp\_read

**Definition** flash.h:140

[flash\_driver\_api::get\_parameters](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc)

flash\_api\_get\_parameters get\_parameters

**Definition** flash.h:135

[flash\_driver\_api::page\_layout](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b)

flash\_api\_pages\_layout page\_layout

**Definition** flash.h:137

[flash\_driver\_api::read](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480)

flash\_api\_read read

**Definition** flash.h:132

[flash\_driver\_api::write](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4)

flash\_api\_write write

**Definition** flash.h:133

[flash\_driver\_api::erase](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15)

flash\_api\_erase erase

**Definition** flash.h:134

[flash\_driver\_api::read\_jedec\_id](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b)

flash\_api\_read\_jedec\_id read\_jedec\_id

**Definition** flash.h:141

[flash\_pages\_info](structflash__pages__info.md)

**Definition** flash.h:252

[flash\_pages\_info::size](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1)

size\_t size

**Definition** flash.h:254

[flash\_pages\_info::start\_offset](structflash__pages__info.md#a5c841987fef1636b83141871456ea867)

off\_t start\_offset

**Definition** flash.h:253

[flash\_pages\_info::index](structflash__pages__info.md#adca463710082164f4323d3011235eb6f)

uint32\_t index

**Definition** flash.h:255

[flash\_pages\_layout](structflash__pages__layout.md)

**Definition** flash.h:35

[flash\_pages\_layout::pages\_size](structflash__pages__layout.md#aabdad4d8a197936f7756950bc73326ee)

size\_t pages\_size

**Definition** flash.h:37

[flash\_pages\_layout::pages\_count](structflash__pages__layout.md#af5e496e680dbe9f4fd2738e6dc2534ec)

size\_t pages\_count

**Definition** flash.h:36

[flash\_parameters](structflash__parameters.md)

Flash memory parameters.

**Definition** flash.h:57

[flash\_parameters::erase\_value](structflash__parameters.md#a218b0cbc797572ce096d0d6f55475ff9)

uint8\_t erase\_value

**Definition** flash.h:59

[flash\_parameters::write\_block\_size](structflash__parameters.md#a9795a3e4fae4d7b81745e876f62ab3a8)

const size\_t write\_block\_size

**Definition** flash.h:58

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash.h](flash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
