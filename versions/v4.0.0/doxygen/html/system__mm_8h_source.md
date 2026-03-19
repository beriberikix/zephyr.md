---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/system__mm_8h_source.html
original_path: doxygen/html/system__mm_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

system\_mm.h

[Go to the documentation of this file.](system__mm_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SYSTEM\_MM\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SYSTEM\_MM\_H\_

17

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19

20#ifndef \_ASMLANGUAGE

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

36

44

[ 46](group__mm__drv__apis.md#gafe1b7f8b4075da1b461f2a74d3142e49)#define SYS\_MM\_MEM\_CACHE\_NONE 2

47

[ 49](group__mm__drv__apis.md#gaed12cd6841eb0fd0af1cefe1d7a6b5aa)#define SYS\_MM\_MEM\_CACHE\_WT 1

50

[ 52](group__mm__drv__apis.md#gad0859fb79c8da1d1af0f38ea63064b8c)#define SYS\_MM\_MEM\_CACHE\_WB 0

53

[ 55](group__mm__drv__apis.md#ga43050af5740a0449da7998b48f540817)#define SYS\_MM\_MEM\_CACHE\_MASK (BIT(3) - 1)

56

60

68

[ 70](group__mm__drv__apis.md#ga8547ea32c40b038daa34ee76cbaee275)#define SYS\_MM\_MEM\_PERM\_RW BIT(3)

71

[ 73](group__mm__drv__apis.md#gac564b8d2148bd7c0ac07313f0fa9861c)#define SYS\_MM\_MEM\_PERM\_EXEC BIT(4)

74

[ 76](group__mm__drv__apis.md#gad86f6d8cbb3102ad3e8375d10cb4551c)#define SYS\_MM\_MEM\_PERM\_USER BIT(5)

77

81

89

[ 110](group__mm__drv__apis.md#ga7097d4d8880cb0c3d5db7623ffc11b26)int [sys\_mm\_drv\_map\_page](group__mm__drv__apis.md#ga7097d4d8880cb0c3d5db7623ffc11b26)(void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

111

[ 133](group__mm__drv__apis.md#ga1186a31d55b24791d800e8f0aef311da)int [sys\_mm\_drv\_map\_region](group__mm__drv__apis.md#ga1186a31d55b24791d800e8f0aef311da)(void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys,

134 size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

135

[ 157](group__mm__drv__apis.md#gab36baa1ed134e5a69ea16451991b920e)int [sys\_mm\_drv\_map\_array](group__mm__drv__apis.md#gab36baa1ed134e5a69ea16451991b920e)(void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys,

158 size\_t cnt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

159

[ 181](group__mm__drv__apis.md#gab78668dd05ab1d4d17ca5bbe3182b0eb)int [sys\_mm\_drv\_unmap\_page](group__mm__drv__apis.md#gab78668dd05ab1d4d17ca5bbe3182b0eb)(void \*virt);

182

[ 205](group__mm__drv__apis.md#gadc3ed78e29aef49b7578b9090dcaacbc)int [sys\_mm\_drv\_unmap\_region](group__mm__drv__apis.md#gadc3ed78e29aef49b7578b9090dcaacbc)(void \*virt, size\_t size);

206

[ 234](group__mm__drv__apis.md#gae46a4189560e314e96f8bee80b55b40b)int [sys\_mm\_drv\_remap\_region](group__mm__drv__apis.md#gae46a4189560e314e96f8bee80b55b40b)(void \*virt\_old, size\_t size, void \*virt\_new);

235

239

247

[ 279](group__mm__drv__apis.md#ga3b2e4b2b359d4fcba104e43866d30d14)int [sys\_mm\_drv\_move\_region](group__mm__drv__apis.md#ga3b2e4b2b359d4fcba104e43866d30d14)(void \*virt\_old, size\_t size, void \*virt\_new,

280 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys\_new);

281

[ 314](group__mm__drv__apis.md#gab172793104608d2a5acae0eb40c50177)int [sys\_mm\_drv\_move\_array](group__mm__drv__apis.md#gab172793104608d2a5acae0eb40c50177)(void \*virt\_old, size\_t size, void \*virt\_new,

315 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys\_new, size\_t phys\_cnt);

316

320

328

348

[ 349](group__mm__drv__apis.md#ga188aebe0dcb10e8a4d620cf0bf9a0444)int [sys\_mm\_drv\_update\_page\_flags](group__mm__drv__apis.md#ga188aebe0dcb10e8a4d620cf0bf9a0444)(void \*virt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

350

371

[ 372](group__mm__drv__apis.md#ga60a9aa179216ed7ac5179c3a7eeb97d3)int [sys\_mm\_drv\_update\_region\_flags](group__mm__drv__apis.md#ga60a9aa179216ed7ac5179c3a7eeb97d3)(void \*virt, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

373

377

385

[ 403](group__mm__drv__apis.md#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)int [sys\_mm\_drv\_page\_phys\_get](group__mm__drv__apis.md#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)(void \*virt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*phys);

404

[ 411](structsys__mm__drv__region.md)struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) {

[ 412](structsys__mm__drv__region.md#a8dfa465f83cf5f6115094b6b5727f418) void \*[addr](structsys__mm__drv__region.md#a8dfa465f83cf5f6115094b6b5727f418);

[ 413](structsys__mm__drv__region.md#a5b48a908a5393fec377edcd3760c18ad) size\_t [size](structsys__mm__drv__region.md#a5b48a908a5393fec377edcd3760c18ad);

[ 414](structsys__mm__drv__region.md#a6838fe4bd4daab440152c4d666a4597d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attr](structsys__mm__drv__region.md#a6838fe4bd4daab440152c4d666a4597d);

415};

416

417/\* TODO is it safe to assume no valid region has size == 0? \*/

[ 424](group__mm__drv__apis.md#gabd2c5de68d1976e4d0a8086523d66e7a)#define SYS\_MM\_DRV\_MEMORY\_REGION\_FOREACH(regions, iter) \

425 for (iter = regions; iter->size; iter++)

426

[ 438](group__mm__drv__apis.md#gaf2c06488bd4ff3ecd1285ce7d70321c9)const struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) \*[sys\_mm\_drv\_query\_memory\_regions](group__mm__drv__apis.md#gaf2c06488bd4ff3ecd1285ce7d70321c9)(void);

439

[ 450](group__mm__drv__apis.md#gab8d3585ffe98796a5c74d0bb9fc634d1)void [sys\_mm\_drv\_query\_memory\_regions\_free](group__mm__drv__apis.md#gab8d3585ffe98796a5c74d0bb9fc634d1)(const struct [sys\_mm\_drv\_region](structsys__mm__drv__region.md) \*regions);

451

455

459

460#ifdef \_\_cplusplus

461}

462#endif

463

464#endif /\* \_ASMLANGUAGE \*/

465

466#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SYSTEM\_MM\_H\_ \*/

[sys\_mm\_drv\_map\_region](group__mm__drv__apis.md#ga1186a31d55b24791d800e8f0aef311da)

int sys\_mm\_drv\_map\_region(void \*virt, uintptr\_t phys, size\_t size, uint32\_t flags)

Map a region of physical memory into the virtual address space.

[sys\_mm\_drv\_update\_page\_flags](group__mm__drv__apis.md#ga188aebe0dcb10e8a4d620cf0bf9a0444)

int sys\_mm\_drv\_update\_page\_flags(void \*virt, uint32\_t flags)

Update memory page flags.

[sys\_mm\_drv\_move\_region](group__mm__drv__apis.md#ga3b2e4b2b359d4fcba104e43866d30d14)

int sys\_mm\_drv\_move\_region(void \*virt\_old, size\_t size, void \*virt\_new, uintptr\_t phys\_new)

Physically move memory, with copy.

[sys\_mm\_drv\_update\_region\_flags](group__mm__drv__apis.md#ga60a9aa179216ed7ac5179c3a7eeb97d3)

int sys\_mm\_drv\_update\_region\_flags(void \*virt, size\_t size, uint32\_t flags)

Update memory region flags.

[sys\_mm\_drv\_map\_page](group__mm__drv__apis.md#ga7097d4d8880cb0c3d5db7623ffc11b26)

int sys\_mm\_drv\_map\_page(void \*virt, uintptr\_t phys, uint32\_t flags)

Map one physical page into the virtual address space.

[sys\_mm\_drv\_page\_phys\_get](group__mm__drv__apis.md#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)

int sys\_mm\_drv\_page\_phys\_get(void \*virt, uintptr\_t \*phys)

Get the mapped physical memory address from virtual address.

[sys\_mm\_drv\_move\_array](group__mm__drv__apis.md#gab172793104608d2a5acae0eb40c50177)

int sys\_mm\_drv\_move\_array(void \*virt\_old, size\_t size, void \*virt\_new, uintptr\_t \*phys\_new, size\_t phys\_cnt)

Physically move memory, with copy.

[sys\_mm\_drv\_map\_array](group__mm__drv__apis.md#gab36baa1ed134e5a69ea16451991b920e)

int sys\_mm\_drv\_map\_array(void \*virt, uintptr\_t \*phys, size\_t cnt, uint32\_t flags)

Map an array of physical memory into the virtual address space.

[sys\_mm\_drv\_unmap\_page](group__mm__drv__apis.md#gab78668dd05ab1d4d17ca5bbe3182b0eb)

int sys\_mm\_drv\_unmap\_page(void \*virt)

Remove mapping for one page of the provided virtual address.

[sys\_mm\_drv\_query\_memory\_regions\_free](group__mm__drv__apis.md#gab8d3585ffe98796a5c74d0bb9fc634d1)

void sys\_mm\_drv\_query\_memory\_regions\_free(const struct sys\_mm\_drv\_region \*regions)

Free the memory array returned by sys\_mm\_drv\_query\_memory\_regions.

[sys\_mm\_drv\_unmap\_region](group__mm__drv__apis.md#gadc3ed78e29aef49b7578b9090dcaacbc)

int sys\_mm\_drv\_unmap\_region(void \*virt, size\_t size)

Remove mappings for a provided virtual address range.

[sys\_mm\_drv\_remap\_region](group__mm__drv__apis.md#gae46a4189560e314e96f8bee80b55b40b)

int sys\_mm\_drv\_remap\_region(void \*virt\_old, size\_t size, void \*virt\_new)

Remap virtual pages into new address.

[sys\_mm\_drv\_query\_memory\_regions](group__mm__drv__apis.md#gaf2c06488bd4ff3ecd1285ce7d70321c9)

const struct sys\_mm\_drv\_region \* sys\_mm\_drv\_query\_memory\_regions(void)

Query available memory regions.

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[sys\_mm\_drv\_region](structsys__mm__drv__region.md)

Represents an available memory region.

**Definition** system\_mm.h:411

[sys\_mm\_drv\_region::size](structsys__mm__drv__region.md#a5b48a908a5393fec377edcd3760c18ad)

size\_t size

Size of the memory region.

**Definition** system\_mm.h:413

[sys\_mm\_drv\_region::attr](structsys__mm__drv__region.md#a6838fe4bd4daab440152c4d666a4597d)

uint32\_t attr

Driver defined attributes of the memory region.

**Definition** system\_mm.h:414

[sys\_mm\_drv\_region::addr](structsys__mm__drv__region.md#a8dfa465f83cf5f6115094b6b5727f418)

void \* addr

Address of the memory region.

**Definition** system\_mm.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mm](dir_464cfbc388e9245b11da9b89dd2be842.md)
- [system\_mm.h](system__mm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
