---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/flash_8h_source.html
original_path: doxygen/html/flash_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 168](group__flash__internal__interface.md#ga2dee3874cb1be4ef4dab599963c30e70)typedef int (\*[flash\_api\_get\_size](group__flash__internal__interface.md#ga97ab6540136589aaafbe049cf4302285))(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*size);

169

170typedef const struct [flash\_parameters](structflash__parameters.md)\* (\*flash\_api\_get\_parameters)(const struct [device](structdevice.md) \*dev);

171

172#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 194](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5)typedef void (\*[flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5))(const struct [device](structdevice.md) \*dev,

195 const struct [flash\_pages\_layout](structflash__pages__layout.md) \*\*[layout](bindesc_8h.md#af8174bbae9567135fe17f1e55621f641),

196 size\_t \*layout\_size);

197#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

198

[ 199](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5)typedef int (\*[flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

200 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t len);

[ 201](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994)typedef int (\*[flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id);

[ 202](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2)typedef int (\*[flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

203 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out);

204

[ 205](structflash__driver__api.md)\_\_subsystem struct [flash\_driver\_api](structflash__driver__api.md) {

[ 206](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480) [flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290) [read](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480);

[ 207](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4) [flash\_api\_write](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba) [write](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4);

[ 208](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15) [flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5) [erase](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15);

[ 209](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc) [flash\_api\_get\_parameters](group__flash__internal__interface.md#ga2dee3874cb1be4ef4dab599963c30e70) [get\_parameters](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc);

[ 210](structflash__driver__api.md#aa59f704dfaa541860983a89731a47302) [flash\_api\_get\_size](group__flash__internal__interface.md#ga97ab6540136589aaafbe049cf4302285) [get\_size](structflash__driver__api.md#aa59f704dfaa541860983a89731a47302);

211#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 212](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b) [flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5) [page\_layout](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b);

213#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

214#if defined(CONFIG\_FLASH\_JESD216\_API)

[ 215](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c) [flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5) [sfdp\_read](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c);

[ 216](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b) [flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994) [read\_jedec\_id](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b);

217#endif /\* CONFIG\_FLASH\_JESD216\_API \*/

218#if defined(CONFIG\_FLASH\_EX\_OP\_ENABLED)

219 [flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2) ex\_op;

220#endif /\* CONFIG\_FLASH\_EX\_OP\_ENABLED \*/

221};

222

226

231

[ 245](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)\_\_syscall int [flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data,

246 size\_t len);

247

248static inline int z\_impl\_flash\_read(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

249 void \*data,

250 size\_t len)

251{

252 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

253 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

254

255 return api->read(dev, offset, data, len);

256}

257

[ 276](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)\_\_syscall int [flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

277 const void \*data,

278 size\_t len);

279

280static inline int z\_impl\_flash\_write(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

281 const void \*data, size\_t len)

282{

283 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

284 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

285 int rc;

286

287 rc = api->write(dev, offset, data, len);

288

289 return rc;

290}

291

[ 320](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)\_\_syscall int [flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t size);

321

322static inline int z\_impl\_flash\_erase(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

323 size\_t size)

324{

325 int rc = -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

326

327 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

328 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

329

330 if (api->erase != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

331 rc = api->erase(dev, offset, size);

332 }

333

334 return rc;

335}

336

[ 350](group__flash__interface.md#ga471edb53a2b1abe3dff0f4e2d216521e)\_\_syscall int [flash\_get\_size](group__flash__interface.md#ga471edb53a2b1abe3dff0f4e2d216521e)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*size);

351

352static inline int z\_impl\_flash\_get\_size(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*size)

353{

354 int rc = -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

355 const struct [flash\_driver\_api](structflash__driver__api.md) \*api = (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

356

357 if (api->get\_size != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

358 rc = api->get\_size(dev, size);

359 }

360

361 return rc;

362}

363

[ 379](group__flash__interface.md#ga022838332e905b0111d5136dd963889b)\_\_syscall int [flash\_fill](group__flash__interface.md#ga022838332e905b0111d5136dd963889b)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t size);

380

[ 418](group__flash__interface.md#ga11eda0cdc7be12636a90d2e8c7264e4a)\_\_syscall int [flash\_flatten](group__flash__interface.md#ga11eda0cdc7be12636a90d2e8c7264e4a)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, size\_t size);

419

[ 420](structflash__pages__info.md)struct [flash\_pages\_info](structflash__pages__info.md) {

[ 421](structflash__pages__info.md#a5c841987fef1636b83141871456ea867) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [start\_offset](structflash__pages__info.md#a5c841987fef1636b83141871456ea867); /\* offset from the base of flash address \*/

[ 422](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1) size\_t [size](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1);

[ 423](structflash__pages__info.md#adca463710082164f4323d3011235eb6f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structflash__pages__info.md#adca463710082164f4323d3011235eb6f);

424};

425

426#if defined(CONFIG\_FLASH\_PAGE\_LAYOUT)

[ 436](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)\_\_syscall int [flash\_get\_page\_info\_by\_offs](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)(const struct [device](structdevice.md) \*dev,

437 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

438 struct [flash\_pages\_info](structflash__pages__info.md) \*info);

439

[ 449](group__flash__interface.md#gaae733082fa92f80261d5895d3f81a98b)\_\_syscall int [flash\_get\_page\_info\_by\_idx](group__flash__interface.md#gaae733082fa92f80261d5895d3f81a98b)(const struct [device](structdevice.md) \*dev,

450 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) page\_index,

451 struct [flash\_pages\_info](structflash__pages__info.md) \*info);

452

[ 460](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)\_\_syscall size\_t [flash\_get\_page\_count](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)(const struct [device](structdevice.md) \*dev);

461

[ 472](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f))(const struct [flash\_pages\_info](structflash__pages__info.md) \*info, void \*data);

473

[ 486](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe)void [flash\_page\_foreach](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe)(const struct [device](structdevice.md) \*dev, [flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f) cb,

487 void \*data);

488#endif /\* CONFIG\_FLASH\_PAGE\_LAYOUT \*/

489

490#if defined(CONFIG\_FLASH\_JESD216\_API)

[ 511](group__flash__interface.md#ga8e9b921299bfb059bf72445a2ffa5a97)\_\_syscall int [flash\_sfdp\_read](group__flash__interface.md#ga8e9b921299bfb059bf72445a2ffa5a97)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

512 void \*data, size\_t len);

513

514static inline int z\_impl\_flash\_sfdp\_read(const struct [device](structdevice.md) \*dev,

515 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

516 void \*data, size\_t len)

517{

518 int rv = -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

519 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

520 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

521

522 if (api->sfdp\_read != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

523 rv = api->sfdp\_read(dev, offset, data, len);

524 }

525 return rv;

526}

527

[ 539](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7)\_\_syscall int [flash\_read\_jedec\_id](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id);

540

541static inline int z\_impl\_flash\_read\_jedec\_id(const struct [device](structdevice.md) \*dev,

542 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id)

543{

544 int rv = -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

545 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

546 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

547

548 if (api->read\_jedec\_id != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

549 rv = api->read\_jedec\_id(dev, id);

550 }

551 return rv;

552}

553#endif /\* CONFIG\_FLASH\_JESD216\_API \*/

554

[ 566](group__flash__interface.md#gaadfb323bc1b4efa39e7bc0a048c472a6)\_\_syscall size\_t [flash\_get\_write\_block\_size](group__flash__interface.md#gaadfb323bc1b4efa39e7bc0a048c472a6)(const struct [device](structdevice.md) \*dev);

567

568static inline size\_t z\_impl\_flash\_get\_write\_block\_size(const struct [device](structdevice.md) \*dev)

569{

570 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

571 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

572

573 return api->get\_parameters(dev)->write\_block\_size;

574}

575

576

[ 588](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3)\_\_syscall const struct [flash\_parameters](structflash__parameters.md) \*[flash\_get\_parameters](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3)(const struct [device](structdevice.md) \*dev);

589

590static inline const struct [flash\_parameters](structflash__parameters.md) \*z\_impl\_flash\_get\_parameters(const struct [device](structdevice.md) \*dev)

591{

592 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

593 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

594

595 return api->get\_parameters(dev);

596}

597

[ 623](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c)\_\_syscall int [flash\_ex\_op](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

624 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out);

625

[ 654](group__flash__interface.md#ga847407358a20d3d5918d8ef11657ce2b)\_\_syscall int [flash\_copy](group__flash__interface.md#ga847407358a20d3d5918d8ef11657ce2b)(const struct [device](structdevice.md) \*src\_dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) src\_offset,

655 const struct [device](structdevice.md) \*dst\_dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) dst\_offset, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

656 size\_t buf\_size);

657/\*

658 \* Extended operation interface provides flexible way for supporting flash

659 \* controller features. Code space is divided equally into Zephyr codes

660 \* (MSb == 0) and vendor codes (MSb == 1). This way we can easily add extended

661 \* operations to the drivers without cluttering the API or problems with API

662 \* incompatibility. Extended operation can be promoted from vendor codes to

663 \* Zephyr codes if the feature is available in most flash controllers and

664 \* can be represented in the same way.

665 \*

666 \* It's not forbidden to have operation in Zephyr codes and vendor codes for

667 \* the same functionality. In this case, vendor operation could provide more

668 \* specific access when abstraction in Zephyr counterpart is insufficient.

669 \*/

[ 670](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)#define FLASH\_EX\_OP\_VENDOR\_BASE 0x8000

[ 671](group__flash__interface.md#gafc0aa899b7ea452d048d8ee67d2e6f06)#define FLASH\_EX\_OP\_IS\_VENDOR(c) ((c) & FLASH\_EX\_OP\_VENDOR\_BASE)

672

[ 676](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51)enum [flash\_ex\_op\_types](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51) {

677 /\*

678 \* Reset flash device.

679 \*/

[ 680](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd) [FLASH\_EX\_OP\_RESET](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd) = 0,

681};

682

683static inline int z\_impl\_flash\_ex\_op(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code,

684 const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out)

685{

686#if defined(CONFIG\_FLASH\_EX\_OP\_ENABLED)

687 const struct [flash\_driver\_api](structflash__driver__api.md) \*api =

688 (const struct [flash\_driver\_api](structflash__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

689

690 if (api->ex\_op == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

691 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

692 }

693

694 return api->ex\_op(dev, code, in, out);

695#else

696 ARG\_UNUSED(dev);

697 ARG\_UNUSED(code);

698 ARG\_UNUSED(in);

699 ARG\_UNUSED(out);

700

701 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

702#endif /\* CONFIG\_FLASH\_EX\_OP\_ENABLED \*/

703}

704

705#ifdef \_\_cplusplus

706}

707#endif

708

712

713#include <zephyr/syscalls/flash.h>

714

715#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_H\_ \*/

[layout](bindesc_8h.md#af8174bbae9567135fe17f1e55621f641)

Incorrect memory layout

**Definition** bindesc.h:314

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

**Definition** flash.h:472

[flash\_get\_size](group__flash__interface.md#ga471edb53a2b1abe3dff0f4e2d216521e)

int flash\_get\_size(const struct device \*dev, uint64\_t \*size)

Get device size in bytes.

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

[flash\_copy](group__flash__interface.md#ga847407358a20d3d5918d8ef11657ce2b)

int flash\_copy(const struct device \*src\_dev, off\_t src\_offset, const struct device \*dst\_dev, off\_t dst\_offset, off\_t size, uint8\_t \*buf, size\_t buf\_size)

Copy flash memory from one device to another.

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

**Definition** flash.h:676

[flash\_get\_page\_count](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e)

size\_t flash\_get\_page\_count(const struct device \*dev)

Get the total number of flash pages.

[flash\_get\_page\_info\_by\_offs](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979)

int flash\_get\_page\_info\_by\_offs(const struct device \*dev, off\_t offset, struct flash\_pages\_info \*info)

Get the size and start offset of flash page at certain flash offset.

[FLASH\_EX\_OP\_RESET](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd)

@ FLASH\_EX\_OP\_RESET

**Definition** flash.h:680

[flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994)

int(\* flash\_api\_read\_jedec\_id)(const struct device \*dev, uint8\_t \*id)

**Definition** flash.h:201

[flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5)

int(\* flash\_api\_erase)(const struct device \*dev, off\_t offset, size\_t size)

Flash erase implementation handler type.

**Definition** flash.h:155

[flash\_api\_get\_parameters](group__flash__internal__interface.md#ga2dee3874cb1be4ef4dab599963c30e70)

const struct flash\_parameters \*(\* flash\_api\_get\_parameters)(const struct device \*dev)

**Definition** flash.h:170

[flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290)

int(\* flash\_api\_read)(const struct device \*dev, off\_t offset, void \*data, size\_t len)

**Definition** flash.h:128

[flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5)

void(\* flash\_api\_pages\_layout)(const struct device \*dev, const struct flash\_pages\_layout \*\*layout, size\_t \*layout\_size)

Retrieve a flash device's layout.

**Definition** flash.h:194

[flash\_api\_get\_size](group__flash__internal__interface.md#ga97ab6540136589aaafbe049cf4302285)

int(\* flash\_api\_get\_size)(const struct device \*dev, uint64\_t \*size)

Get device size in bytes.

**Definition** flash.h:168

[flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5)

int(\* flash\_api\_sfdp\_read)(const struct device \*dev, off\_t offset, void \*data, size\_t len)

**Definition** flash.h:199

[flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2)

int(\* flash\_api\_ex\_op)(const struct device \*dev, uint16\_t code, const uintptr\_t in, void \*out)

**Definition** flash.h:202

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

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

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

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

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

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[flash\_driver\_api](structflash__driver__api.md)

**Definition** flash.h:205

[flash\_driver\_api::sfdp\_read](structflash__driver__api.md#a0d8122a16fe671099cb9c13459fc022c)

flash\_api\_sfdp\_read sfdp\_read

**Definition** flash.h:215

[flash\_driver\_api::get\_parameters](structflash__driver__api.md#a2696431e3b94db2f8a830e3142a577fc)

flash\_api\_get\_parameters get\_parameters

**Definition** flash.h:209

[flash\_driver\_api::page\_layout](structflash__driver__api.md#a82b03b535d86e98c083b701176a5556b)

flash\_api\_pages\_layout page\_layout

**Definition** flash.h:212

[flash\_driver\_api::read](structflash__driver__api.md#aa3f58e76ce1a1bacf57d874a4e190480)

flash\_api\_read read

**Definition** flash.h:206

[flash\_driver\_api::get\_size](structflash__driver__api.md#aa59f704dfaa541860983a89731a47302)

flash\_api\_get\_size get\_size

**Definition** flash.h:210

[flash\_driver\_api::write](structflash__driver__api.md#aa799a18761bbe6d43a82dc12a8de44c4)

flash\_api\_write write

**Definition** flash.h:207

[flash\_driver\_api::erase](structflash__driver__api.md#acaf3275b42cb048eca00818026f10f15)

flash\_api\_erase erase

**Definition** flash.h:208

[flash\_driver\_api::read\_jedec\_id](structflash__driver__api.md#add4026f7bd3a49de6de1dfee7c43d57b)

flash\_api\_read\_jedec\_id read\_jedec\_id

**Definition** flash.h:216

[flash\_pages\_info](structflash__pages__info.md)

**Definition** flash.h:420

[flash\_pages\_info::size](structflash__pages__info.md#a1ef4b965caaeed26014a6d6ae85c93c1)

size\_t size

**Definition** flash.h:422

[flash\_pages\_info::start\_offset](structflash__pages__info.md#a5c841987fef1636b83141871456ea867)

off\_t start\_offset

**Definition** flash.h:421

[flash\_pages\_info::index](structflash__pages__info.md#adca463710082164f4323d3011235eb6f)

uint32\_t index

**Definition** flash.h:423

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
