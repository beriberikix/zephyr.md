---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fcb_8h_source.html
original_path: doxygen/html/fcb_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

19#include <[zephyr/kernel.h](kernel_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

33

39

[ 40](group__fcb__data__structures.md#gaccabb1cb7f83c0d8919571cf3de7ee47)#define FCB\_MAX\_LEN (0x3fffu)

41

[ 51](structfcb__entry.md)struct [fcb\_entry](structfcb__entry.md) {

[ 52](structfcb__entry.md#aa564f9f79012beb20265bc5e85816fea) struct [flash\_sector](structflash__sector.md) \*[fe\_sector](structfcb__entry.md#aa564f9f79012beb20265bc5e85816fea);

54

[ 55](structfcb__entry.md#a6d01cb2107949bf4f0a2779c9781261f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fe\_elem\_off](structfcb__entry.md#a6d01cb2107949bf4f0a2779c9781261f);

57

[ 58](structfcb__entry.md#a82cba5933875498c804f31722a6e90f9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fe\_data\_off](structfcb__entry.md#a82cba5933875498c804f31722a6e90f9);

60

[ 61](structfcb__entry.md#aa207d21d51bc2c7aa838ca9dc3b52be7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fe\_data\_len](structfcb__entry.md#aa207d21d51bc2c7aa838ca9dc3b52be7);

62};

63

[ 70](group__fcb__data__structures.md#ga9b47a1aa59039995107c8e23dfacf43f)#define FCB\_ENTRY\_FA\_DATA\_OFF(entry) (entry.fe\_sector->fs\_off +\

71 entry.fe\_data\_off)

72

[ 76](structfcb__entry__ctx.md)struct [fcb\_entry\_ctx](structfcb__entry__ctx.md) {

[ 77](structfcb__entry__ctx.md#a0da5217647b82c8799a6cde221253680) struct [fcb\_entry](structfcb__entry.md) [loc](structfcb__entry__ctx.md#a0da5217647b82c8799a6cde221253680);

[ 78](structfcb__entry__ctx.md#a8b491cd670e609c2b4d897d15e37eb2b) const struct [flash\_area](structflash__area.md) \*[fap](structfcb__entry__ctx.md#a8b491cd670e609c2b4d897d15e37eb2b);

80};

81

[ 85](group__fcb__data__structures.md#ga2fc8801bea1d91a422aa622bcf4cb6e0)#define FCB\_FLAGS\_CRC\_DISABLED BIT(0)

86

[ 94](structfcb.md)struct [fcb](structfcb.md) {

95 /\* Caller of fcb\_init fills this in \*/

[ 96](structfcb.md#a4206faa9ed633ba2315163c52e557397) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [f\_magic](structfcb.md#a4206faa9ed633ba2315163c52e557397);

104

[ 105](structfcb.md#a030b96abd6c857295f154197278cca69) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_version](structfcb.md#a030b96abd6c857295f154197278cca69);

[ 106](structfcb.md#aa642058028d755c7bc5b6814a4cb8c16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_sector\_cnt](structfcb.md#aa642058028d755c7bc5b6814a4cb8c16);

[ 107](structfcb.md#aab748de6989e30de6571fc94d66ee365) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_scratch\_cnt](structfcb.md#aab748de6989e30de6571fc94d66ee365);

111

[ 112](structfcb.md#afc96f045d541c8d141d3427884f1fb44) struct [flash\_sector](structflash__sector.md) \*[f\_sectors](structfcb.md#afc96f045d541c8d141d3427884f1fb44);

114

115 /\* Flash circular buffer internal state \*/

[ 116](structfcb.md#a1f30c78d7e02748fbf0bf5033d4bdadf) struct [k\_mutex](structk__mutex.md) [f\_mtx](structfcb.md#a1f30c78d7e02748fbf0bf5033d4bdadf);

118

[ 119](structfcb.md#ac6dc6236f8b03e4b03f691c55b4d3327) struct [flash\_sector](structflash__sector.md) \*[f\_oldest](structfcb.md#ac6dc6236f8b03e4b03f691c55b4d3327);

123

[ 124](structfcb.md#a1f7922dc1e8076bcfffca117260d5e02) struct [fcb\_entry](structfcb__entry.md) [f\_active](structfcb.md#a1f7922dc1e8076bcfffca117260d5e02);

[ 125](structfcb.md#a8da1d0b4bef7d9ddcd5922d9bbef0cef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [f\_active\_id](structfcb.md#a8da1d0b4bef7d9ddcd5922d9bbef0cef);

127

[ 128](structfcb.md#aa745e88d4477408b40a759dd1baea637) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_align](structfcb.md#aa745e88d4477408b40a759dd1baea637);

130

[ 131](structfcb.md#a16cfc82afc8abe70291f4b462e617f2f) const struct [flash\_area](structflash__area.md) \*[fap](structfcb.md#a16cfc82afc8abe70291f4b462e617f2f);

135

[ 136](structfcb.md#a614c6441395637c6c0a17a4fd6107db3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [f\_erase\_value](structfcb.md#a614c6441395637c6c0a17a4fd6107db3);

140#ifdef CONFIG\_FCB\_ALLOW\_FIXED\_ENDMARKER

141 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) f\_flags;

143#endif

144};

145

149

156

[ 165](group__fcb__api.md#gab304f3e9e28f6229d7ddbe638eda2f70)int [fcb\_init](group__fcb__api.md#gab304f3e9e28f6229d7ddbe638eda2f70)(int f\_area\_id, struct [fcb](structfcb.md) \*fcbp);

166

[ 182](group__fcb__api.md#gad567d124d8b0fe181ed54cfbe33b315c)int [fcb\_append](group__fcb__api.md#gad567d124d8b0fe181ed54cfbe33b315c)(struct [fcb](structfcb.md) \*fcbp, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, struct [fcb\_entry](structfcb__entry.md) \*loc);

183

[ 192](group__fcb__api.md#gaae445e8376db192ce45fff9dcf95c954)int [fcb\_append\_finish](group__fcb__api.md#gaae445e8376db192ce45fff9dcf95c954)(struct [fcb](structfcb.md) \*fcbp, struct [fcb\_entry](structfcb__entry.md) \*append\_loc);

193

[ 209](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea)typedef int (\*[fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea))(struct [fcb\_entry\_ctx](structfcb__entry__ctx.md) \*loc\_ctx, void \*arg);

210

[ 226](group__fcb__api.md#gad50e579ec9430a23ef5525e74ceb21b2)int [fcb\_walk](group__fcb__api.md#gad50e579ec9430a23ef5525e74ceb21b2)(struct [fcb](structfcb.md) \*fcbp, struct [flash\_sector](structflash__sector.md) \*sector, [fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea) cb, void \*cb\_arg);

227

[ 244](group__fcb__api.md#ga7908a252a09ebbb98b60a505220072bc)int [fcb\_getnext](group__fcb__api.md#ga7908a252a09ebbb98b60a505220072bc)(struct [fcb](structfcb.md) \*fcbp, struct [fcb\_entry](structfcb__entry.md) \*[loc](structfcb__entry__ctx.md#a0da5217647b82c8799a6cde221253680));

245

[ 254](group__fcb__api.md#gad2fb288645e678dd6ea05b0871d5e774)int [fcb\_rotate](group__fcb__api.md#gad2fb288645e678dd6ea05b0871d5e774)(struct [fcb](structfcb.md) \*fcbp);

255

[ 266](group__fcb__api.md#ga22b2bab8af3004c93e5d40659ccfec29)int [fcb\_append\_to\_scratch](group__fcb__api.md#ga22b2bab8af3004c93e5d40659ccfec29)(struct [fcb](structfcb.md) \*fcbp);

267

[ 275](group__fcb__api.md#gaa9beaa3f5a6cc52b7e460d5670fdaabf)int [fcb\_free\_sector\_cnt](group__fcb__api.md#gaa9beaa3f5a6cc52b7e460d5670fdaabf)(struct [fcb](structfcb.md) \*fcbp);

276

[ 284](group__fcb__api.md#gade8af12645d769ce3b27848976ada32a)int [fcb\_is\_empty](group__fcb__api.md#gade8af12645d769ce3b27848976ada32a)(struct [fcb](structfcb.md) \*fcbp);

285

[ 295](group__fcb__api.md#gac15df95c0d9bed45c9da39802411598d)int [fcb\_offset\_last\_n](group__fcb__api.md#gac15df95c0d9bed45c9da39802411598d)(struct [fcb](structfcb.md) \*fcbp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) entries, struct [fcb\_entry](structfcb__entry.md) \*last\_n\_entry);

296

[ 304](group__fcb__api.md#gaab78da410b7e709854e29219eb02a0c9)int [fcb\_clear](group__fcb__api.md#gaab78da410b7e709854e29219eb02a0c9)(struct [fcb](structfcb.md) \*fcbp);

305

309

316

[ 328](group__fcb__internal.md#ga0b921b509dab767661058d164e80f55e)int [fcb\_flash\_read](group__fcb__internal.md#ga0b921b509dab767661058d164e80f55e)(const struct [fcb](structfcb.md) \*fcbp, const struct [flash\_sector](structflash__sector.md) \*sector, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394),

329 void \*dst, size\_t len);

330

[ 342](group__fcb__internal.md#gafcfb9b6d4b5c0e593c0a9e512a0ec309)int [fcb\_flash\_write](group__fcb__internal.md#gafcfb9b6d4b5c0e593c0a9e512a0ec309)(const struct [fcb](structfcb.md) \*fcbp, const struct [flash\_sector](structflash__sector.md) \*sector, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394),

343 const void \*src, size\_t len);

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

[fcb\_append\_to\_scratch](group__fcb__api.md#ga22b2bab8af3004c93e5d40659ccfec29)

int fcb\_append\_to\_scratch(struct fcb \*fcbp)

Start using the scratch block.

[fcb\_getnext](group__fcb__api.md#ga7908a252a09ebbb98b60a505220072bc)

int fcb\_getnext(struct fcb \*fcbp, struct fcb\_entry \*loc)

Get next fcb entry location.

[fcb\_free\_sector\_cnt](group__fcb__api.md#gaa9beaa3f5a6cc52b7e460d5670fdaabf)

int fcb\_free\_sector\_cnt(struct fcb \*fcbp)

Get free sector count.

[fcb\_clear](group__fcb__api.md#gaab78da410b7e709854e29219eb02a0c9)

int fcb\_clear(struct fcb \*fcbp)

Clear fcb instance storage.

[fcb\_append\_finish](group__fcb__api.md#gaae445e8376db192ce45fff9dcf95c954)

int fcb\_append\_finish(struct fcb \*fcbp, struct fcb\_entry \*append\_loc)

Finishes entry append operation.

[fcb\_init](group__fcb__api.md#gab304f3e9e28f6229d7ddbe638eda2f70)

int fcb\_init(int f\_area\_id, struct fcb \*fcbp)

Initialize FCB instance.

[fcb\_offset\_last\_n](group__fcb__api.md#gac15df95c0d9bed45c9da39802411598d)

int fcb\_offset\_last\_n(struct fcb \*fcbp, uint8\_t entries, struct fcb\_entry \*last\_n\_entry)

Finds the fcb entry that gives back up to n entries at the end.

[fcb\_rotate](group__fcb__api.md#gad2fb288645e678dd6ea05b0871d5e774)

int fcb\_rotate(struct fcb \*fcbp)

Rotate fcb sectors.

[fcb\_walk](group__fcb__api.md#gad50e579ec9430a23ef5525e74ceb21b2)

int fcb\_walk(struct fcb \*fcbp, struct flash\_sector \*sector, fcb\_walk\_cb cb, void \*cb\_arg)

Walk over all entries in the FCB sector.

[fcb\_append](group__fcb__api.md#gad567d124d8b0fe181ed54cfbe33b315c)

int fcb\_append(struct fcb \*fcbp, uint16\_t len, struct fcb\_entry \*loc)

Appends an entry to circular buffer.

[fcb\_is\_empty](group__fcb__api.md#gade8af12645d769ce3b27848976ada32a)

int fcb\_is\_empty(struct fcb \*fcbp)

Check whether FCB has any data.

[fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea)

int(\* fcb\_walk\_cb)(struct fcb\_entry\_ctx \*loc\_ctx, void \*arg)

FCB Walk callback function type.

**Definition** fcb.h:209

[fcb\_flash\_read](group__fcb__internal.md#ga0b921b509dab767661058d164e80f55e)

int fcb\_flash\_read(const struct fcb \*fcbp, const struct flash\_sector \*sector, off\_t off, void \*dst, size\_t len)

Read raw data from the fcb flash sector.

[fcb\_flash\_write](group__fcb__internal.md#gafcfb9b6d4b5c0e593c0a9e512a0ec309)

int fcb\_flash\_write(const struct fcb \*fcbp, const struct flash\_sector \*sector, off\_t off, const void \*src, size\_t len)

Write raw data to the fcb flash sector.

[inttypes.h](inttypes_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

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

**Definition** fcb.h:76

[fcb\_entry\_ctx::loc](structfcb__entry__ctx.md#a0da5217647b82c8799a6cde221253680)

struct fcb\_entry loc

FCB entry info.

**Definition** fcb.h:77

[fcb\_entry\_ctx::fap](structfcb__entry__ctx.md#a8b491cd670e609c2b4d897d15e37eb2b)

const struct flash\_area \* fap

Flash area where the entry is placed.

**Definition** fcb.h:78

[fcb\_entry](structfcb__entry.md)

FCB entry info structure.

**Definition** fcb.h:51

[fcb\_entry::fe\_elem\_off](structfcb__entry.md#a6d01cb2107949bf4f0a2779c9781261f)

uint32\_t fe\_elem\_off

Offset from the start of the sector to beginning of element.

**Definition** fcb.h:55

[fcb\_entry::fe\_data\_off](structfcb__entry.md#a82cba5933875498c804f31722a6e90f9)

uint32\_t fe\_data\_off

Offset from the start of the sector to the start of element.

**Definition** fcb.h:58

[fcb\_entry::fe\_data\_len](structfcb__entry.md#aa207d21d51bc2c7aa838ca9dc3b52be7)

uint16\_t fe\_data\_len

Size of data area in fcb entry.

**Definition** fcb.h:61

[fcb\_entry::fe\_sector](structfcb__entry.md#aa564f9f79012beb20265bc5e85816fea)

struct flash\_sector \* fe\_sector

Pointer to info about sector where data are placed.

**Definition** fcb.h:52

[fcb](structfcb.md)

FCB instance structure.

**Definition** fcb.h:94

[fcb::f\_version](structfcb.md#a030b96abd6c857295f154197278cca69)

uint8\_t f\_version

Current version number of the data.

**Definition** fcb.h:105

[fcb::fap](structfcb.md#a16cfc82afc8abe70291f4b462e617f2f)

const struct flash\_area \* fap

Flash area used by the fcb instance, internal state.

**Definition** fcb.h:131

[fcb::f\_mtx](structfcb.md#a1f30c78d7e02748fbf0bf5033d4bdadf)

struct k\_mutex f\_mtx

Locking for accessing the FCB data, internal state.

**Definition** fcb.h:116

[fcb::f\_active](structfcb.md#a1f7922dc1e8076bcfffca117260d5e02)

struct fcb\_entry f\_active

internal state

**Definition** fcb.h:124

[fcb::f\_magic](structfcb.md#a4206faa9ed633ba2315163c52e557397)

uint32\_t f\_magic

Magic value, should not be 0xFFFFFFFF.

**Definition** fcb.h:96

[fcb::f\_erase\_value](structfcb.md#a614c6441395637c6c0a17a4fd6107db3)

uint8\_t f\_erase\_value

The value flash takes when it is erased.

**Definition** fcb.h:136

[fcb::f\_active\_id](structfcb.md#a8da1d0b4bef7d9ddcd5922d9bbef0cef)

uint16\_t f\_active\_id

Flash location where the newest data is, internal state.

**Definition** fcb.h:125

[fcb::f\_sector\_cnt](structfcb.md#aa642058028d755c7bc5b6814a4cb8c16)

uint8\_t f\_sector\_cnt

Number of elements in sector array.

**Definition** fcb.h:106

[fcb::f\_align](structfcb.md#aa745e88d4477408b40a759dd1baea637)

uint8\_t f\_align

writes to flash have to aligned to this, internal state

**Definition** fcb.h:128

[fcb::f\_scratch\_cnt](structfcb.md#aab748de6989e30de6571fc94d66ee365)

uint8\_t f\_scratch\_cnt

Number of sectors to keep empty.

**Definition** fcb.h:107

[fcb::f\_oldest](structfcb.md#ac6dc6236f8b03e4b03f691c55b4d3327)

struct flash\_sector \* f\_oldest

Pointer to flash sector containing the oldest data, internal state.

**Definition** fcb.h:119

[fcb::f\_sectors](structfcb.md#afc96f045d541c8d141d3427884f1fb44)

struct flash\_sector \* f\_sectors

Array of sectors, must be contiguous.

**Definition** fcb.h:112

[flash\_area](structflash__area.md)

Flash partition.

**Definition** flash\_map.h:54

[flash\_sector](structflash__sector.md)

Structure for transfer flash sector boundaries.

**Definition** flash\_map.h:76

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [fcb.h](fcb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
