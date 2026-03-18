---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/flash__map_8h_source.html
original_path: doxygen/html/flash__map_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_map.h

[Go to the documentation of this file.](flash__map_8h.md)

1/\*

2 \* Copyright (c) 2017-2024 Nordic Semiconductor ASA

3 \* Copyright (c) 2015 Runtime Inc

4 \* Copyright (c) 2023 Sensorfy B.V.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

13

14#ifndef ZEPHYR\_INCLUDE\_STORAGE\_FLASH\_MAP\_H\_

15#define ZEPHYR\_INCLUDE\_STORAGE\_FLASH\_MAP\_H\_

16

26

27/\*

28 \* This API makes it possible to operate on flash areas easily and

29 \* effectively.

30 \*

31 \* The system contains global data about flash areas. Every area

32 \* contains an ID number, offset, and length.

33 \*/

34

38#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

39#include <stddef.h>

40#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

41#include <[zephyr/device.h](device_8h.md)>

42#include <[zephyr/devicetree.h](devicetree_8h.md)>

43

44#ifdef \_\_cplusplus

45extern "C" {

46#endif

47

[ 49](group__flash__area__api.md#ga3435d1517409d28c06f3bb11be4aea4c)#define SOC\_FLASH\_0\_ID 0

[ 51](group__flash__area__api.md#ga8317a2991704a09e43b17189769ac8da)#define SPI\_FLASH\_0\_ID 1

52

[ 59](structflash__area.md)struct [flash\_area](structflash__area.md) {

[ 61](structflash__area.md#acfe73a1f4f00fdf58129b21e5b71f5d4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fa\_id](structflash__area.md#acfe73a1f4f00fdf58129b21e5b71f5d4);

[ 62](structflash__area.md#af98b8f20c0219bfcdd2fc20037845a99) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pad16](structflash__area.md#af98b8f20c0219bfcdd2fc20037845a99);

[ 64](structflash__area.md#a3a362ad9aa44725a0b0188042a2ee257) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [fa\_off](structflash__area.md#a3a362ad9aa44725a0b0188042a2ee257);

[ 66](structflash__area.md#a6c3c23c4c628f48c92505dddf4b24edf) size\_t [fa\_size](structflash__area.md#a6c3c23c4c628f48c92505dddf4b24edf);

[ 68](structflash__area.md#a941637492ab4e321e3b08de19cd769d2) const struct [device](structdevice.md) \*[fa\_dev](structflash__area.md#a941637492ab4e321e3b08de19cd769d2);

69#if CONFIG\_FLASH\_MAP\_LABELS

71 const char \*fa\_label;

72#endif

73};

74

[ 81](structflash__sector.md)struct [flash\_sector](structflash__sector.md) {

[ 83](structflash__sector.md#a2e9899681d4ec66fac277a7a52e1830b) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [fs\_off](structflash__sector.md#a2e9899681d4ec66fac277a7a52e1830b);

[ 85](structflash__sector.md#ab1fef4b1b6978d25b5f809d778888f75) size\_t [fs\_size](structflash__sector.md#ab1fef4b1b6978d25b5f809d778888f75);

86};

87

88#if defined(CONFIG\_FLASH\_AREA\_CHECK\_INTEGRITY)

95struct flash\_area\_check {

96 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*match;

97 size\_t clen;

98 size\_t [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394);

99 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rbuf;

100 size\_t rblen;

101};

102

112int flash\_area\_check\_int\_sha256(const struct [flash\_area](structflash__area.md) \*fa,

113 const struct flash\_area\_check \*fac);

114#endif

115

[ 129](group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7)int [flash\_area\_open](group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const struct [flash\_area](structflash__area.md) \*\*fa);

130

[ 139](group__flash__area__api.md#gaff2ae50bb961846f5d5362c90e0c7a39)void [flash\_area\_close](group__flash__area__api.md#gaff2ae50bb961846f5d5362c90e0c7a39)(const struct [flash\_area](structflash__area.md) \*fa);

140

[ 155](group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127)int [flash\_area\_read](group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127)(const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), void \*dst,

156 size\_t len);

157

[ 172](group__flash__area__api.md#gaa56052f8d6bf4f6966752bc21f5cceb8)int [flash\_area\_write](group__flash__area__api.md#gaa56052f8d6bf4f6966752bc21f5cceb8)(const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), const void \*src,

173 size\_t len);

174

[ 188](group__flash__area__api.md#gacc5cbff19d23773115f3334f862814d2)int [flash\_area\_erase](group__flash__area__api.md#gacc5cbff19d23773115f3334f862814d2)(const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), size\_t len);

189

[ 211](group__flash__area__api.md#gafd097d05f5bfe91695bc7793e82cabcd)int [flash\_area\_flatten](group__flash__area__api.md#gafd097d05f5bfe91695bc7793e82cabcd)(const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), size\_t len);

212

[ 223](group__flash__area__api.md#ga13b7294e84544373e97b8c0274859f6e)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flash\_area\_align](group__flash__area__api.md#ga13b7294e84544373e97b8c0274859f6e)(const struct [flash\_area](structflash__area.md) \*fa);

224

[ 237](group__flash__area__api.md#ga5c89e0be6c41058beb1c3f87a0c9c94f)int [flash\_area\_get\_sectors](group__flash__area__api.md#ga5c89e0be6c41058beb1c3f87a0c9c94f)(int fa\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*count,

238 struct [flash\_sector](structflash__sector.md) \*sectors);

239

[ 247](group__flash__area__api.md#gab9d0b43faefa1f25805e7def82819f2c)typedef void (\*[flash\_area\_cb\_t](group__flash__area__api.md#gab9d0b43faefa1f25805e7def82819f2c))(const struct [flash\_area](structflash__area.md) \*fa,

248 void \*user\_data);

249

[ 256](group__flash__area__api.md#ga34e74955153f8576acdbff1a524f2d37)void [flash\_area\_foreach](group__flash__area__api.md#ga34e74955153f8576acdbff1a524f2d37)([flash\_area\_cb\_t](group__flash__area__api.md#gab9d0b43faefa1f25805e7def82819f2c) user\_cb, void \*user\_data);

257

[ 266](group__flash__area__api.md#ga557d5fd981b0d52d0eb483ab218c497c)int [flash\_area\_has\_driver](group__flash__area__api.md#ga557d5fd981b0d52d0eb483ab218c497c)(const struct [flash\_area](structflash__area.md) \*fa);

267

[ 275](group__flash__area__api.md#gaed7d16e272d7644f556d2edaa942b308)const struct [device](structdevice.md) \*[flash\_area\_get\_device](group__flash__area__api.md#gaed7d16e272d7644f556d2edaa942b308)(const struct [flash\_area](structflash__area.md) \*fa);

276

277#if CONFIG\_FLASH\_MAP\_LABELS

285const char \*flash\_area\_label(const struct [flash\_area](structflash__area.md) \*fa);

286#endif

287

[ 297](group__flash__area__api.md#ga1f16d59cecb25c5143c6a923b3b2f466)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flash\_area\_erased\_val](group__flash__area__api.md#ga1f16d59cecb25c5143c6a923b3b2f466)(const struct [flash\_area](structflash__area.md) \*fa);

298

[ 307](group__flash__area__api.md#gabb94759e5717302724f08f90f941a945)#define FIXED\_PARTITION\_EXISTS(label) DT\_FIXED\_PARTITION\_EXISTS(DT\_NODELABEL(label))

308

[ 316](group__flash__area__api.md#ga60d5298007e2ee261b915a110389e76a)#define FIXED\_PARTITION\_ID(label) DT\_FIXED\_PARTITION\_ID(DT\_NODELABEL(label))

317

[ 325](group__flash__area__api.md#ga9229bc06458c19baf093ced063a9494b)#define FIXED\_PARTITION\_OFFSET(label) DT\_REG\_ADDR(DT\_NODELABEL(label))

326

[ 334](group__flash__area__api.md#gaf26b80f089d25283c01ed54b5a27988c)#define FIXED\_PARTITION\_NODE\_OFFSET(node) DT\_REG\_ADDR(node)

335

[ 343](group__flash__area__api.md#ga2dbc50d9f80d7f7c597c75cbd536cd50)#define FIXED\_PARTITION\_SIZE(label) DT\_REG\_SIZE(DT\_NODELABEL(label))

344

[ 352](group__flash__area__api.md#ga526459438c6de09abb727585d22b7004)#define FIXED\_PARTITION\_NODE\_SIZE(node) DT\_REG\_SIZE(node)

353

[ 361](group__flash__area__api.md#gacca3f32100a4e46cb7da21ea8bf0782c)#define FLASH\_AREA\_DEVICE(label) \

362 DEVICE\_DT\_GET(DT\_MTD\_FROM\_FIXED\_PARTITION(DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL(label)))

363

[ 371](group__flash__area__api.md#ga3c92b6797feb183da38b8b57e77f2d17)#define FIXED\_PARTITION\_DEVICE(label) \

372 DEVICE\_DT\_GET(DT\_MTD\_FROM\_FIXED\_PARTITION(DT\_NODELABEL(label)))

373

[ 381](group__flash__area__api.md#gad64fb220f82870acce62661bfa94991a)#define FIXED\_PARTITION\_NODE\_DEVICE(node) \

382 DEVICE\_DT\_GET(DT\_MTD\_FROM\_FIXED\_PARTITION(node))

383

384#ifdef \_\_cplusplus

385}

386#endif

387

391

392#endif /\* ZEPHYR\_INCLUDE\_STORAGE\_FLASH\_MAP\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[flash\_area\_align](group__flash__area__api.md#ga13b7294e84544373e97b8c0274859f6e)

uint32\_t flash\_area\_align(const struct flash\_area \*fa)

Get write block size of the flash area.

[flash\_area\_erased\_val](group__flash__area__api.md#ga1f16d59cecb25c5143c6a923b3b2f466)

uint8\_t flash\_area\_erased\_val(const struct flash\_area \*fa)

Get the value expected to be read when accessing any erased flash byte.

[flash\_area\_foreach](group__flash__area__api.md#ga34e74955153f8576acdbff1a524f2d37)

void flash\_area\_foreach(flash\_area\_cb\_t user\_cb, void \*user\_data)

Iterate over flash map.

[flash\_area\_has\_driver](group__flash__area__api.md#ga557d5fd981b0d52d0eb483ab218c497c)

int flash\_area\_has\_driver(const struct flash\_area \*fa)

Check whether given flash area has supporting flash driver in the system.

[flash\_area\_get\_sectors](group__flash__area__api.md#ga5c89e0be6c41058beb1c3f87a0c9c94f)

int flash\_area\_get\_sectors(int fa\_id, uint32\_t \*count, struct flash\_sector \*sectors)

Retrieve info about sectors within the area.

[flash\_area\_open](group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7)

int flash\_area\_open(uint8\_t id, const struct flash\_area \*\*fa)

Retrieve partitions flash area from the flash\_map.

[flash\_area\_read](group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127)

int flash\_area\_read(const struct flash\_area \*fa, off\_t off, void \*dst, size\_t len)

Read flash area data.

[flash\_area\_write](group__flash__area__api.md#gaa56052f8d6bf4f6966752bc21f5cceb8)

int flash\_area\_write(const struct flash\_area \*fa, off\_t off, const void \*src, size\_t len)

Write data to flash area.

[flash\_area\_cb\_t](group__flash__area__api.md#gab9d0b43faefa1f25805e7def82819f2c)

void(\* flash\_area\_cb\_t)(const struct flash\_area \*fa, void \*user\_data)

Flash map iteration callback.

**Definition** flash\_map.h:247

[flash\_area\_erase](group__flash__area__api.md#gacc5cbff19d23773115f3334f862814d2)

int flash\_area\_erase(const struct flash\_area \*fa, off\_t off, size\_t len)

Erase flash area.

[flash\_area\_get\_device](group__flash__area__api.md#gaed7d16e272d7644f556d2edaa942b308)

const struct device \* flash\_area\_get\_device(const struct flash\_area \*fa)

Get driver for given flash area.

[flash\_area\_flatten](group__flash__area__api.md#gafd097d05f5bfe91695bc7793e82cabcd)

int flash\_area\_flatten(const struct flash\_area \*fa, off\_t off, size\_t len)

Erase flash area or fill with erase-value.

[flash\_area\_close](group__flash__area__api.md#gaff2ae50bb961846f5d5362c90e0c7a39)

void flash\_area\_close(const struct flash\_area \*fa)

Close flash\_area.

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[flash\_area](structflash__area.md)

Flash partition.

**Definition** flash\_map.h:59

[flash\_area::fa\_off](structflash__area.md#a3a362ad9aa44725a0b0188042a2ee257)

off\_t fa\_off

Start offset from the beginning of the flash device.

**Definition** flash\_map.h:64

[flash\_area::fa\_size](structflash__area.md#a6c3c23c4c628f48c92505dddf4b24edf)

size\_t fa\_size

Total size.

**Definition** flash\_map.h:66

[flash\_area::fa\_dev](structflash__area.md#a941637492ab4e321e3b08de19cd769d2)

const struct device \* fa\_dev

Backing flash device.

**Definition** flash\_map.h:68

[flash\_area::fa\_id](structflash__area.md#acfe73a1f4f00fdf58129b21e5b71f5d4)

uint8\_t fa\_id

ID number.

**Definition** flash\_map.h:61

[flash\_area::pad16](structflash__area.md#af98b8f20c0219bfcdd2fc20037845a99)

uint16\_t pad16

**Definition** flash\_map.h:62

[flash\_sector](structflash__sector.md)

Structure for transfer flash sector boundaries.

**Definition** flash\_map.h:81

[flash\_sector::fs\_off](structflash__sector.md#a2e9899681d4ec66fac277a7a52e1830b)

off\_t fs\_off

Sector offset from the beginning of the flash device.

**Definition** flash\_map.h:83

[flash\_sector::fs\_size](structflash__sector.md#ab1fef4b1b6978d25b5f809d778888f75)

size\_t fs\_size

Sector size in bytes.

**Definition** flash\_map.h:85

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [storage](dir_9ae83148a5180e4d77f53cf673d8ea1c.md)
- [flash\_map.h](flash__map_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
