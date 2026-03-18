---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/flash_8h_source.html
original_path: doxygen/html/flash_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash.h

[Go to the documentation of this file.](flash_8h.md)

1/\*

2 \* Copyright (c) 2017-2024 Nordic Semiconductor ASA

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

53

[ 59](structflash__parameters.md)struct [flash\_parameters](structflash__parameters.md) {

[ 61](structflash__parameters.md#a9795a3e4fae4d7b81745e876f62ab3a8) const size\_t [write\_block\_size](structflash__parameters.md#a9795a3e4fae4d7b81745e876f62ab3a8);

62

64 /\* User code should call flash\_params\_get\_ functions on flash\_parameters

65 \* to get capabilities, rather than accessing object contents directly.

66 \*/

67 struct {

68 /\* Device has no explicit erase, so it either erases on

69 \* write or does not require it at all.

70 \* This also includes devices that support erase but

71 \* do not require it.

72 \*/

73 bool no\_explicit\_erase: 1;

74 } caps;

[ 77](structflash__parameters.md#a218b0cbc797572ce096d0d6f55475ff9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [erase\_value](structflash__parameters.md#a218b0cbc797572ce096d0d6f55475ff9);

78};

79

[ 81](group__flash__interface.md#ga760f7d79cb9f23bc0326abfea85808aa)#define FLASH\_ERASE\_C\_EXPLICIT 0x01

[ 85](group__flash__interface.md#ga82adeb566049cfbbced1c50db5d17760)#define FLASH\_ERASE\_CAPS\_UNSET (int)-1

86/\* The values below are now reserved but not used \*/

[ 87](group__flash__interface.md#ga37f63f7c484ae89c9a133fbe2616a8ea)#define FLASH\_ERASE\_C\_SUPPORTED 0x02

[ 88](group__flash__interface.md#gaf0257b23bbe071c5b1e0294e7d31fca4)#define FLASH\_ERASE\_C\_VAL\_BIT 0x04

[ 89](group__flash__interface.md#ga6dc21974c3db6b5b7a69cdfb170b2c06)#define FLASH\_ERASE\_UNIFORM\_PAGE 0x08

90

91

92/\* @brief Parser for flash\_parameters for retrieving erase capabilities

93 \*

94 \* The functions parses flash\_parameters type object and returns combination

95 \* of erase capabilities of 0 if device does not have any.

96 \* Not that in some cases availability of erase may be dependent on driver

97 \* options, so even if by hardware design a device provides some erase

98 \* capabilities, the function may return 0 if these been disabled or not

99 \* implemented by driver.

100 \*

101 \* @param p pointer to flash\_parameters type object

102 \*

103 \* @return 0 or combination of FLASH\_ERASE\_C\_ capabilities.

104 \*/

105static inline

[ 106](group__flash__interface.md#gabc73e8888dcb8f4f79cd80b8d02a6a2c)int [flash\_params\_get\_erase\_cap](group__flash__interface.md#gabc73e8888dcb8f4f79cd80b8d02a6a2c)(const struct [flash\_parameters](structflash__parameters.md) \*p)

107{

108#if defined(CONFIG\_FLASH\_HAS\_EXPLICIT\_ERASE)

109#if defined(CONFIG\_FLASH\_HAS\_NO\_EXPLICIT\_ERASE)

110 return (p->caps.no\_explicit\_erase) ? 0 : [FLASH\_ERASE\_C\_EXPLICIT](group__flash__interface.md#ga760f7d79cb9f23bc0326abfea85808aa);

111#else

112 ARG\_UNUSED(p);

113 return [FLASH\_ERASE\_C\_EXPLICIT](group__flash__interface.md#ga760f7d79cb9f23bc0326abfea85808aa);

114#endif

115#endif

116 return 0;

117}

118

122

127

[ 128](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290)typedef int (\*[flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

129 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

130 size\_t len);

[ 139](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)typedef int (\*[flash\_api\_write](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

140 const void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t len);

141

[ 155](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5)typedef int (\*[flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

156 size\_t size);

157

158typedef const struct [flash\_parameters](structflash__parameters.md)\* (\*flash\_api\_get\_parameters)(const struct [device](structdevice.md) \*dev);

159

160#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 182](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5)typedef void (\*[flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5))(const struct [device](structdevice.md) \*dev,

183 const struct [flash\_pages\_layout](structflash__pages__layout.md) \*\*layout,

184 size\_t \*layout\_size);

185#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

186

[ 187](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5)typedef int (\*[flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

188 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t len);

[ 189](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994)typedef int (\*[flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id);

[ 190](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2)typedef int (\*[flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

191 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out);

192

[ 193](structflash__driver__api.md)\_\_subsystem struct [flash\_driver\_api](structflash__driver__api.md) {

[ 194](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480) [flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290) [read](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480);

[ 195](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4) [flash\_api\_write](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba) [write](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4);

[ 196](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15) [flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5) [erase](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15);

[ 197](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc) [flash\_api\_get\_parameters](group__flash__internal__interface.md#ga2dee3874cb1be4ef4dab599963c30e70) [get\_parameters](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc);

198#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 199](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b) [flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5) [page\_layout](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b);

200#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

201#if defined(CONFIG\_FLASH\_JESD216\_API)

[ 202](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c) [flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5) [sfdp\_read](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c);

[ 203](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b) [flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994) [read\_jedec\_id](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b);

204#endif /\* CONFIG\_FLASH\_JESD216\_API \*/

205#if defined(CONFIG\_FLASH\_EX\_OP\_ENABLED)

206 [flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2) ex\_op;

207#endif /\* CONFIG\_FLASH\_EX\_OP\_ENABLED \*/

208};

209

213

218

[ 232](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)\_\_syscall int [flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data,

233 size\_t len);

234

235static inline int z\_impl\_flash\_read(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

236 void \*data,

237 size\_t len)

238{

239 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

240 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

241

242 return api->read(dev, offset, data, len);

243}

244

[ 263](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)\_\_syscall int [flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

264 const void \*data,

265 size\_t len);

266

267static inline int z\_impl\_flash\_write(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

268 const void \*data, size\_t len)

269{

270 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

271 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

272 int rc;

273

274 rc = api->write(dev, offset, data, len);

275

276 return rc;

277}

278

[ 307](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)\_\_syscall int [flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t size);

308

309static inline int z\_impl\_flash\_erase(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

310 size\_t size)

311{

312 int rc = -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

313

314 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

315 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

316

317 if (api->erase != NULL) {

318 rc = api->erase(dev, offset, size);

319 }

320

321 return rc;

322}

323

[ 339](group__flash__interface.md#ga022838332e905b0111d5136dd963889b)\_\_syscall int [flash\_fill](group__flash__interface.md#ga022838332e905b0111d5136dd963889b)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t size);

340

[ 378](group__flash__interface.md#ga11eda0cdc7be12636a90d2e8c7264e4a)\_\_syscall int [flash\_flatten](group__flash__interface.md#ga11eda0cdc7be12636a90d2e8c7264e4a)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t size);

379

[ 380](structflash__pages__info.md)struct [flash\_pages\_info](structflash__pages__info.md) {

[ 381](structflash__pages__info.md#a5c841987fef1636b83141871456ea867) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [start\_offset](structflash__pages__info.md#a5c841987fef1636b83141871456ea867); /\* offset from the base of flash address \*/

[ 382](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1) size\_t [size](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1);

[ 383](structflash__pages__info.md#adca463710082164f4323d3011235eb6f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structflash__pages__info.md#adca463710082164f4323d3011235eb6f);

384};

385

386#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 396](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)\_\_syscall int [flash\_get\_page\_info\_by\_offs](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)(const struct [device](structdevice.md) \*dev,

397 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

398 struct [flash\_pages\_info](structflash__pages__info.md) \*info);

399

[ 409](group__flash__interface.md#gaae733082fa92f80261d5895d3f81a98b)\_\_syscall int [flash\_get\_page\_info\_by\_idx](group__flash__interface.md#gaae733082fa92f80261d5895d3f81a98b)(const struct [device](structdevice.md) \*dev,

410 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) page\_index,

411 struct [flash\_pages\_info](structflash__pages__info.md) \*info);

412

[ 420](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)\_\_syscall size\_t [flash\_get\_page\_count](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)(const struct [device](structdevice.md) \*dev);

421

[ 432](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f))(const struct [flash\_pages\_info](structflash__pages__info.md) \*info, void \*data);

433

[ 446](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe)void [flash\_page\_foreach](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe)(const struct [device](structdevice.md) \*dev, [flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f) cb,

447 void \*data);

448#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

449

450#if defined(CONFIG\_FLASH\_JESD216\_API)

[ 471](group__flash__interface.md#ga8e9b921299bfb059bf72445a2ffa5a97)\_\_syscall int [flash\_sfdp\_read](group__flash__interface.md#ga8e9b921299bfb059bf72445a2ffa5a97)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

472 void \*data, size\_t len);

473

474static inline int z\_impl\_flash\_sfdp\_read(const struct [device](structdevice.md) \*dev,

475 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

476 void \*data, size\_t len)

477{

478 int rv = -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

479 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

480 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

481

482 if (api->sfdp\_read != NULL) {

483 rv = api->sfdp\_read(dev, offset, data, len);

484 }

485 return rv;

486}

487

[ 499](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7)\_\_syscall int [flash\_read\_jedec\_id](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id);

500

501static inline int z\_impl\_flash\_read\_jedec\_id(const struct [device](structdevice.md) \*dev,

502 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id)

503{

504 int rv = -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

505 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

506 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

507

508 if (api->read\_jedec\_id != NULL) {

509 rv = api->read\_jedec\_id(dev, id);

510 }

511 return rv;

512}

513#endif /\* CONFIG\_FLASH\_JESD216\_API \*/

514

[ 526](group__flash__interface.md#gaadfb323bc1b4efa39e7bc0a048c472a6)\_\_syscall size\_t [flash\_get\_write\_block\_size](group__flash__interface.md#gaadfb323bc1b4efa39e7bc0a048c472a6)(const struct [device](structdevice.md) \*dev);

527

528static inline size\_t z\_impl\_flash\_get\_write\_block\_size(const struct [device](structdevice.md) \*dev)

529{

530 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

531 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

532

533 return api->get\_parameters(dev)->write\_block\_size;

534}

535

536

[ 548](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3)\_\_syscall const struct [flash\_parameters](structflash__parameters.md) \*[flash\_get\_parameters](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3)(const struct [device](structdevice.md) \*dev);

549

550static inline const struct [flash\_parameters](structflash__parameters.md) \*z\_impl\_flash\_get\_parameters(const struct [device](structdevice.md) \*dev)

551{

552 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

553 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

554

555 return api->get\_parameters(dev);

556}

557

[ 583](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c)\_\_syscall int [flash\_ex\_op](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

584 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out);

585

586/\*

587 \* Extended operation interface provides flexible way for supporting flash

588 \* controller features. Code space is divided equally into Zephyr codes

589 \* (MSb == 0) and vendor codes (MSb == 1). This way we can easily add extended

590 \* operations to the drivers without cluttering the API or problems with API

591 \* incompatibility. Extended operation can be promoted from vendor codes to

592 \* Zephyr codes if the feature is available in most flash controllers and

593 \* can be represented in the same way.

594 \*

595 \* It's not forbidden to have operation in Zephyr codes and vendor codes for

596 \* the same functionality. In this case, vendor operation could provide more

597 \* specific access when abstraction in Zephyr counterpart is insufficient.

598 \*/

[ 599](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)#define FLASH\_EX\_OP\_VENDOR\_BASE 0x8000

[ 600](group__flash__interface.md#gafc0aa899b7ea452d048d8ee67d2e6f06)#define FLASH\_EX\_OP\_IS\_VENDOR(c) ((c) & FLASH\_EX\_OP\_VENDOR\_BASE)

601

[ 605](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51)enum [flash\_ex\_op\_types](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51) {

606 /\*

607 \* Reset flash device.

608 \*/

[ 609](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd) [FLASH\_EX\_OP\_RESET](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd) = 0,

610};

611

612static inline int z\_impl\_flash\_ex\_op(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

613 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out)

614{

615#if defined(CONFIG\_FLASH\_EX\_OP\_ENABLED)

616 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

617 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

618

619 if (api->ex\_op == NULL) {

620 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

621 }

622

623 return api->ex\_op(dev, code, in, out);

624#else

625 ARG\_UNUSED(dev);

626 ARG\_UNUSED(code);

627 ARG\_UNUSED(in);

628 ARG\_UNUSED(out);

629

630 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

631#endif /\* CONFIG\_FLASH\_EX\_OP\_ENABLED \*/

632}

633

634#ifdef \_\_cplusplus

635}

636#endif

637

641

642#include <zephyr/syscalls/flash.h>

643

644#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[flash\_fill](group__flash__interface.md#ga022838332e905b0111d5136dd963889b)

int flash\_fill(const struct device \*dev, uint8\_t val, off\_t offset, size\_t size)

Fill selected range of device with specified value.

[flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)

int flash\_erase(const struct device \*dev, off\_t offset, size\_t size)

Erase part or all of a flash memory.

[flash\_get\_parameters](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3)

const struct flash\_parameters \* flash\_get\_parameters(const struct device \*dev)

Get pointer to flash\_parameters structure.

[flash\_flatten](group__flash__interface.md#ga11eda0cdc7be12636a90d2e8c7264e4a)

int flash\_flatten(const struct device \*dev, off\_t offset, size\_t size)

Erase part or all of a flash memory or level it.

[flash\_page\_foreach](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe)

void flash\_page\_foreach(const struct device \*dev, flash\_page\_cb cb, void \*data)

Iterate over all flash pages on a device.

[flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)

bool(\* flash\_page\_cb)(const struct flash\_pages\_info \*info, void \*data)

Callback type for iterating over flash pages present on a device.

**Definition** flash.h:432

[flash\_ex\_op](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c)

int flash\_ex\_op(const struct device \*dev, uint16\_t code, const uintptr\_t in, void \*out)

Execute flash extended operation on given device.

[FLASH\_ERASE\_C\_EXPLICIT](group__flash__interface.md#ga760f7d79cb9f23bc0326abfea85808aa)

#define FLASH\_ERASE\_C\_EXPLICIT

Set for ordinary Flash where erase is needed before write of random data.

**Definition** flash.h:81

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

[flash\_params\_get\_erase\_cap](group__flash__interface.md#gabc73e8888dcb8f4f79cd80b8d02a6a2c)

static int flash\_params\_get\_erase\_cap(const struct flash\_parameters \*p)

**Definition** flash.h:106

[flash\_read\_jedec\_id](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7)

int flash\_read\_jedec\_id(const struct device \*dev, uint8\_t \*id)

Read the JEDEC ID from a compatible flash device.

[flash\_ex\_op\_types](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51)

flash\_ex\_op\_types

Enumeration for extra flash operations.

**Definition** flash.h:605

[flash\_get\_page\_count](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)

size\_t flash\_get\_page\_count(const struct device \*dev)

Get the total number of flash pages.

[flash\_get\_page\_info\_by\_offs](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)

int flash\_get\_page\_info\_by\_offs(const struct device \*dev, off\_t offset, struct flash\_pages\_info \*info)

Get the size and start offset of flash page at certain flash offset.

[FLASH\_EX\_OP\_RESET](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd)

@ FLASH\_EX\_OP\_RESET

**Definition** flash.h:609

[flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994)

int(\* flash\_api\_read\_jedec\_id)(const struct device \*dev, uint8\_t \*id)

**Definition** flash.h:189

[flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5)

int(\* flash\_api\_erase)(const struct device \*dev, off\_t offset, size\_t size)

Flash erase implementation handler type.

**Definition** flash.h:155

[flash\_api\_get\_parameters](group__flash__internal__interface.md#ga2dee3874cb1be4ef4dab599963c30e70)

const struct flash\_parameters \*(\* flash\_api\_get\_parameters)(const struct device \*dev)

**Definition** flash.h:158

[flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290)

int(\* flash\_api\_read)(const struct device \*dev, off\_t offset, void \*data, size\_t len)

**Definition** flash.h:128

[flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5)

void(\* flash\_api\_pages\_layout)(const struct device \*dev, const struct flash\_pages\_layout \*\*layout, size\_t \*layout\_size)

Retrieve a flash device's layout.

**Definition** flash.h:182

[flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5)

int(\* flash\_api\_sfdp\_read)(const struct device \*dev, off\_t offset, void \*data, size\_t len)

**Definition** flash.h:187

[flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2)

int(\* flash\_api\_ex\_op)(const struct device \*dev, uint16\_t code, const uintptr\_t in, void \*out)

**Definition** flash.h:190

[flash\_api\_write](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)

int(\* flash\_api\_write)(const struct device \*dev, off\_t offset, const void \*data, size\_t len)

Flash write implementation handler type.

**Definition** flash.h:139

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

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

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[flash\_driver\_api](structflash__driver__api.md)

**Definition** flash.h:193

[flash\_driver\_api::sfdp\_read](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c)

flash\_api\_sfdp\_read sfdp\_read

**Definition** flash.h:202

[flash\_driver\_api::get\_parameters](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc)

flash\_api\_get\_parameters get\_parameters

**Definition** flash.h:197

[flash\_driver\_api::page\_layout](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b)

flash\_api\_pages\_layout page\_layout

**Definition** flash.h:199

[flash\_driver\_api::read](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480)

flash\_api\_read read

**Definition** flash.h:194

[flash\_driver\_api::write](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4)

flash\_api\_write write

**Definition** flash.h:195

[flash\_driver\_api::erase](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15)

flash\_api\_erase erase

**Definition** flash.h:196

[flash\_driver\_api::read\_jedec\_id](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b)

flash\_api\_read\_jedec\_id read\_jedec\_id

**Definition** flash.h:203

[flash\_pages\_info](structflash__pages__info.md)

**Definition** flash.h:380

[flash\_pages\_info::size](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1)

size\_t size

**Definition** flash.h:382

[flash\_pages\_info::start\_offset](structflash__pages__info.md#a5c841987fef1636b83141871456ea867)

off\_t start\_offset

**Definition** flash.h:381

[flash\_pages\_info::index](structflash__pages__info.md#adca463710082164f4323d3011235eb6f)

uint32\_t index

**Definition** flash.h:383

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

**Definition** flash.h:59

[flash\_parameters::erase\_value](structflash__parameters.md#a218b0cbc797572ce096d0d6f55475ff9)

uint8\_t erase\_value

Value the device is filled in erased areas.

**Definition** flash.h:77

[flash\_parameters::write\_block\_size](structflash__parameters.md#a9795a3e4fae4d7b81745e876f62ab3a8)

const size\_t write\_block\_size

Minimal write alignment and size.

**Definition** flash.h:61

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash.h](flash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
