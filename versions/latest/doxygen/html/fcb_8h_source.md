---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fcb_8h_source.html
original_path: doxygen/html/fcb_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcb.h

[Go to the documentation of this file.](fcb_8h.md)

1/\*

2 \* Copyright (c) 2017-2023 Nordic Semiconductor ASA

3 \* Copyright (c) 2015 Runtime Inc

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_FS\_FCB\_H\_

8#define ZEPHYR\_INCLUDE\_FS\_FCB\_H\_

9

10/\*

11 \* Flash circular buffer.

12 \*/

13#include <[inttypes.h](inttypes_8h.md)>

14#include <[limits.h](limits_8h.md)>

15

16#include <[zephyr/storage/flash\_map.h](flash__map_8h.md)>

17#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

18

19#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

31

37

[ 38](group__fcb__data__structures.md#gaccabb1cb7f83c0d8919571cf3de7ee47)#define FCB\_MAX\_LEN (CHAR\_MAX | CHAR\_MAX << 7)

39

[ 49](structfcb__entry.md)struct [fcb\_entry](structfcb__entry.md) {

[ 50](structfcb__entry.md#aa564f9f79012beb20265bc5e85816fea) struct [flash\_sector](structflash__sector.md) \*[fe\_sector](structfcb__entry.md#aa564f9f79012beb20265bc5e85816fea);

52

[ 53](structfcb__entry.md#a6d01cb2107949bf4f0a2779c9781261f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fe\_elem\_off](structfcb__entry.md#a6d01cb2107949bf4f0a2779c9781261f);

55

[ 56](structfcb__entry.md#a82cba5933875498c804f31722a6e90f9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fe\_data\_off](structfcb__entry.md#a82cba5933875498c804f31722a6e90f9);

58

[ 59](structfcb__entry.md#aa207d21d51bc2c7aa838ca9dc3b52be7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fe\_data\_len](structfcb__entry.md#aa207d21d51bc2c7aa838ca9dc3b52be7);

60};

61

[ 68](group__fcb__data__structures.md#ga9b47a1aa59039995107c8e23dfacf43f)#define FCB\_ENTRY\_FA\_DATA\_OFF(entry) (entry.fe\_sector->fs\_off +\

69 entry.fe\_data\_off)

70

[ 74](structfcb__entry__ctx.md)struct [fcb\_entry\_ctx](structfcb__entry__ctx.md) {

[ 75](structfcb__entry__ctx.md#a0da5217647b82c8799a6cde221253680) struct [fcb\_entry](structfcb__entry.md) [loc](structfcb__entry__ctx.md#a0da5217647b82c8799a6cde221253680);

[ 76](structfcb__entry__ctx.md#a8b491cd670e609c2b4d897d15e37eb2b) const struct [flash\_area](structflash__area.md) \*[fap](structfcb__entry__ctx.md#a8b491cd670e609c2b4d897d15e37eb2b);

78};

79

[ 83](group__fcb__data__structures.md#ga2fc8801bea1d91a422aa622bcf4cb6e0)#define FCB\_FLAGS\_CRC\_DISABLED BIT(0)

84

[ 92](structfcb.md)struct [fcb](structfcb.md) {

93 /\* Caller of fcb\_init fills this in \*/

[ 94](structfcb.md#a4206faa9ed633ba2315163c52e557397) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [f\_magic](structfcb.md#a4206faa9ed633ba2315163c52e557397);

102

[ 103](structfcb.md#a030b96abd6c857295f154197278cca69) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_version](structfcb.md#a030b96abd6c857295f154197278cca69);

[ 104](structfcb.md#aa642058028d755c7bc5b6814a4cb8c16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_sector\_cnt](structfcb.md#aa642058028d755c7bc5b6814a4cb8c16);

[ 105](structfcb.md#aab748de6989e30de6571fc94d66ee365) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_scratch\_cnt](structfcb.md#aab748de6989e30de6571fc94d66ee365);

109

[ 110](structfcb.md#afc96f045d541c8d141d3427884f1fb44) struct [flash\_sector](structflash__sector.md) \*[f\_sectors](structfcb.md#afc96f045d541c8d141d3427884f1fb44);

112

113 /\* Flash circular buffer internal state \*/

[ 114](structfcb.md#a1f30c78d7e02748fbf0bf5033d4bdadf) struct [k\_mutex](structk__mutex.md) [f\_mtx](structfcb.md#a1f30c78d7e02748fbf0bf5033d4bdadf);

116

[ 117](structfcb.md#ac6dc6236f8b03e4b03f691c55b4d3327) struct [flash\_sector](structflash__sector.md) \*[f\_oldest](structfcb.md#ac6dc6236f8b03e4b03f691c55b4d3327);

121

[ 122](structfcb.md#a1f7922dc1e8076bcfffca117260d5e02) struct [fcb\_entry](structfcb__entry.md) [f\_active](structfcb.md#a1f7922dc1e8076bcfffca117260d5e02);

[ 123](structfcb.md#a8da1d0b4bef7d9ddcd5922d9bbef0cef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [f\_active\_id](structfcb.md#a8da1d0b4bef7d9ddcd5922d9bbef0cef);

125

[ 126](structfcb.md#aa745e88d4477408b40a759dd1baea637) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_align](structfcb.md#aa745e88d4477408b40a759dd1baea637);

128

[ 129](structfcb.md#a16cfc82afc8abe70291f4b462e617f2f) const struct [flash\_area](structflash__area.md) \*[fap](structfcb.md#a16cfc82afc8abe70291f4b462e617f2f);

133

[ 134](structfcb.md#a614c6441395637c6c0a17a4fd6107db3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_erase\_value](structfcb.md#a614c6441395637c6c0a17a4fd6107db3);

138#ifdef CONFIG\_FCB\_ALLOW\_FIXED\_ENDMARKER

139 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) f\_flags;

141#endif

142};

143

147

154

[ 163](group__fcb__api.md#ga318d35b6f023bb4079aaf76c01a59b96)int [fcb\_init](group__fcb__api.md#ga318d35b6f023bb4079aaf76c01a59b96)(int f\_area\_id, struct [fcb](structfcb.md) \*[fcb](structfcb.md));

164

[ 180](group__fcb__api.md#ga46a06d5c3bf945ba807b6960a354d744)int [fcb\_append](group__fcb__api.md#ga46a06d5c3bf945ba807b6960a354d744)(struct [fcb](structfcb.md) \*[fcb](structfcb.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, struct [fcb\_entry](structfcb__entry.md) \*loc);

181

[ 190](group__fcb__api.md#ga2d8581e0784546fd73e4cd2f8baeebd9)int [fcb\_append\_finish](group__fcb__api.md#ga2d8581e0784546fd73e4cd2f8baeebd9)(struct [fcb](structfcb.md) \*[fcb](structfcb.md), struct [fcb\_entry](structfcb__entry.md) \*append\_loc);

191

[ 207](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea)typedef int (\*[fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea))(struct [fcb\_entry\_ctx](structfcb__entry__ctx.md) \*loc\_ctx, void \*arg);

208

[ 224](group__fcb__api.md#ga2e22f120b3f1d729f8e861f0c0e448fb)int [fcb\_walk](group__fcb__api.md#ga2e22f120b3f1d729f8e861f0c0e448fb)(struct [fcb](structfcb.md) \*[fcb](structfcb.md), struct [flash\_sector](structflash__sector.md) \*sector, [fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea) cb,

225 void \*cb\_arg);

226

[ 243](group__fcb__api.md#gaeeeb1d66ebc6dcefde1e07c3d8bdf4bc)int [fcb\_getnext](group__fcb__api.md#gaeeeb1d66ebc6dcefde1e07c3d8bdf4bc)(struct [fcb](structfcb.md) \*[fcb](structfcb.md), struct [fcb\_entry](structfcb__entry.md) \*[loc](structfcb__entry__ctx.md#a0da5217647b82c8799a6cde221253680));

244

[ 253](group__fcb__api.md#gab749a92fa5890a35996c27f9f2b8f98f)int [fcb\_rotate](group__fcb__api.md#gab749a92fa5890a35996c27f9f2b8f98f)(struct [fcb](structfcb.md) \*[fcb](structfcb.md));

254

[ 265](group__fcb__api.md#gaf26d681ddea9b22d06122184b5a09566)int [fcb\_append\_to\_scratch](group__fcb__api.md#gaf26d681ddea9b22d06122184b5a09566)(struct [fcb](structfcb.md) \*[fcb](structfcb.md));

266

[ 274](group__fcb__api.md#ga2dec5f90b687466997eb25be43448daa)int [fcb\_free\_sector\_cnt](group__fcb__api.md#ga2dec5f90b687466997eb25be43448daa)(struct [fcb](structfcb.md) \*[fcb](structfcb.md));

275

[ 283](group__fcb__api.md#ga76d29d337d5e457f065ed897297ba6cb)int [fcb\_is\_empty](group__fcb__api.md#ga76d29d337d5e457f065ed897297ba6cb)(struct [fcb](structfcb.md) \*[fcb](structfcb.md));

284

[ 294](group__fcb__api.md#gacf4b86d660b7f3a3b73477defd86590c)int [fcb\_offset\_last\_n](group__fcb__api.md#gacf4b86d660b7f3a3b73477defd86590c)(struct [fcb](structfcb.md) \*[fcb](structfcb.md), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) entries,

295 struct [fcb\_entry](structfcb__entry.md) \*last\_n\_entry);

296

[ 304](group__fcb__api.md#gab3d5c09980af72f0de1692682c8dfef1)int [fcb\_clear](group__fcb__api.md#gab3d5c09980af72f0de1692682c8dfef1)(struct [fcb](structfcb.md) \*[fcb](structfcb.md));

305

309

316

[ 328](group__fcb__internal.md#ga85e3a7fcd92a029b16f7aebdfd7fd546)int [fcb\_flash\_read](group__fcb__internal.md#ga85e3a7fcd92a029b16f7aebdfd7fd546)(const struct [fcb](structfcb.md) \*[fcb](structfcb.md), const struct [flash\_sector](structflash__sector.md) \*sector,

329 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), void \*dst, size\_t len);

330

[ 342](group__fcb__internal.md#ga181d43e24799940105185fef9436ce8d)int [fcb\_flash\_write](group__fcb__internal.md#ga181d43e24799940105185fef9436ce8d)(const struct [fcb](structfcb.md) \*[fcb](structfcb.md), const struct [flash\_sector](structflash__sector.md) \*sector,

343 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), const void \*src, size\_t len);

344

348

349#ifdef \_\_cplusplus

350}

351#endif

352

353#endif /\* ZEPHYR\_INCLUDE\_FS\_FCB\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[flash\_map.h](flash__map_8h.md)

Public API for flash map.

[fcb\_append\_finish](group__fcb__api.md#ga2d8581e0784546fd73e4cd2f8baeebd9)

int fcb\_append\_finish(struct fcb \*fcb, struct fcb\_entry \*append\_loc)

Finishes entry append operation.

[fcb\_free\_sector\_cnt](group__fcb__api.md#ga2dec5f90b687466997eb25be43448daa)

int fcb\_free\_sector\_cnt(struct fcb \*fcb)

Get free sector count.

[fcb\_walk](group__fcb__api.md#ga2e22f120b3f1d729f8e861f0c0e448fb)

int fcb\_walk(struct fcb \*fcb, struct flash\_sector \*sector, fcb\_walk\_cb cb, void \*cb\_arg)

Walk over all entries in the FCB sector.

[fcb\_init](group__fcb__api.md#ga318d35b6f023bb4079aaf76c01a59b96)

int fcb\_init(int f\_area\_id, struct fcb \*fcb)

Initialize FCB instance.

[fcb\_append](group__fcb__api.md#ga46a06d5c3bf945ba807b6960a354d744)

int fcb\_append(struct fcb \*fcb, uint16\_t len, struct fcb\_entry \*loc)

Appends an entry to circular buffer.

[fcb\_is\_empty](group__fcb__api.md#ga76d29d337d5e457f065ed897297ba6cb)

int fcb\_is\_empty(struct fcb \*fcb)

Check whether FCB has any data.

[fcb\_clear](group__fcb__api.md#gab3d5c09980af72f0de1692682c8dfef1)

int fcb\_clear(struct fcb \*fcb)

Clear fcb instance storage.

[fcb\_rotate](group__fcb__api.md#gab749a92fa5890a35996c27f9f2b8f98f)

int fcb\_rotate(struct fcb \*fcb)

Rotate fcb sectors.

[fcb\_offset\_last\_n](group__fcb__api.md#gacf4b86d660b7f3a3b73477defd86590c)

int fcb\_offset\_last\_n(struct fcb \*fcb, uint8\_t entries, struct fcb\_entry \*last\_n\_entry)

Finds the fcb entry that gives back up to n entries at the end.

[fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea)

int(\* fcb\_walk\_cb)(struct fcb\_entry\_ctx \*loc\_ctx, void \*arg)

FCB Walk callback function type.

**Definition** fcb.h:207

[fcb\_getnext](group__fcb__api.md#gaeeeb1d66ebc6dcefde1e07c3d8bdf4bc)

int fcb\_getnext(struct fcb \*fcb, struct fcb\_entry \*loc)

Get next fcb entry location.

[fcb\_append\_to\_scratch](group__fcb__api.md#gaf26d681ddea9b22d06122184b5a09566)

int fcb\_append\_to\_scratch(struct fcb \*fcb)

Start using the scratch block.

[fcb\_flash\_write](group__fcb__internal.md#ga181d43e24799940105185fef9436ce8d)

int fcb\_flash\_write(const struct fcb \*fcb, const struct flash\_sector \*sector, off\_t off, const void \*src, size\_t len)

Write raw data to the fcb flash sector.

[fcb\_flash\_read](group__fcb__internal.md#ga85e3a7fcd92a029b16f7aebdfd7fd546)

int fcb\_flash\_read(const struct fcb \*fcb, const struct flash\_sector \*sector, off\_t off, void \*dst, size\_t len)

Read raw data from the fcb flash sector.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[inttypes.h](inttypes_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[limits.h](limits_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[fcb\_entry\_ctx](structfcb__entry__ctx.md)

Structure for transferring complete information about FCB entry location within flash memory.

**Definition** fcb.h:74

[fcb\_entry\_ctx::loc](structfcb__entry__ctx.md#a0da5217647b82c8799a6cde221253680)

struct fcb\_entry loc

FCB entry info.

**Definition** fcb.h:75

[fcb\_entry\_ctx::fap](structfcb__entry__ctx.md#a8b491cd670e609c2b4d897d15e37eb2b)

const struct flash\_area \* fap

Flash area where the entry is placed.

**Definition** fcb.h:76

[fcb\_entry](structfcb__entry.md)

FCB entry info structure.

**Definition** fcb.h:49

[fcb\_entry::fe\_elem\_off](structfcb__entry.md#a6d01cb2107949bf4f0a2779c9781261f)

uint32\_t fe\_elem\_off

Offset from the start of the sector to beginning of element.

**Definition** fcb.h:53

[fcb\_entry::fe\_data\_off](structfcb__entry.md#a82cba5933875498c804f31722a6e90f9)

uint32\_t fe\_data\_off

Offset from the start of the sector to the start of element.

**Definition** fcb.h:56

[fcb\_entry::fe\_data\_len](structfcb__entry.md#aa207d21d51bc2c7aa838ca9dc3b52be7)

uint16\_t fe\_data\_len

Size of data area in fcb entry.

**Definition** fcb.h:59

[fcb\_entry::fe\_sector](structfcb__entry.md#aa564f9f79012beb20265bc5e85816fea)

struct flash\_sector \* fe\_sector

Pointer to info about sector where data are placed.

**Definition** fcb.h:50

[fcb](structfcb.md)

FCB instance structure.

**Definition** fcb.h:92

[fcb::f\_version](structfcb.md#a030b96abd6c857295f154197278cca69)

uint8\_t f\_version

Current version number of the data.

**Definition** fcb.h:103

[fcb::fap](structfcb.md#a16cfc82afc8abe70291f4b462e617f2f)

const struct flash\_area \* fap

Flash area used by the fcb instance, internal state.

**Definition** fcb.h:129

[fcb::f\_mtx](structfcb.md#a1f30c78d7e02748fbf0bf5033d4bdadf)

struct k\_mutex f\_mtx

Locking for accessing the FCB data, internal state.

**Definition** fcb.h:114

[fcb::f\_active](structfcb.md#a1f7922dc1e8076bcfffca117260d5e02)

struct fcb\_entry f\_active

internal state

**Definition** fcb.h:122

[fcb::f\_magic](structfcb.md#a4206faa9ed633ba2315163c52e557397)

uint32\_t f\_magic

Magic value, should not be 0xFFFFFFFF.

**Definition** fcb.h:94

[fcb::f\_erase\_value](structfcb.md#a614c6441395637c6c0a17a4fd6107db3)

uint8\_t f\_erase\_value

The value flash takes when it is erased.

**Definition** fcb.h:134

[fcb::f\_active\_id](structfcb.md#a8da1d0b4bef7d9ddcd5922d9bbef0cef)

uint16\_t f\_active\_id

Flash location where the newest data is, internal state.

**Definition** fcb.h:123

[fcb::f\_sector\_cnt](structfcb.md#aa642058028d755c7bc5b6814a4cb8c16)

uint8\_t f\_sector\_cnt

Number of elements in sector array.

**Definition** fcb.h:104

[fcb::f\_align](structfcb.md#aa745e88d4477408b40a759dd1baea637)

uint8\_t f\_align

writes to flash have to aligned to this, internal state

**Definition** fcb.h:126

[fcb::f\_scratch\_cnt](structfcb.md#aab748de6989e30de6571fc94d66ee365)

uint8\_t f\_scratch\_cnt

Number of sectors to keep empty.

**Definition** fcb.h:105

[fcb::f\_oldest](structfcb.md#ac6dc6236f8b03e4b03f691c55b4d3327)

struct flash\_sector \* f\_oldest

Pointer to flash sector containing the oldest data, internal state.

**Definition** fcb.h:117

[fcb::f\_sectors](structfcb.md#afc96f045d541c8d141d3427884f1fb44)

struct flash\_sector \* f\_sectors

Array of sectors, must be contiguous.

**Definition** fcb.h:110

[flash\_area](structflash__area.md)

Flash partition.

**Definition** flash\_map.h:57

[flash\_sector](structflash__sector.md)

Structure for transfer flash sector boundaries.

**Definition** flash\_map.h:79

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [fcb.h](fcb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
