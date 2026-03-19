---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/kernel_2mm_8h_source.html
original_path: doxygen/html/kernel_2mm_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm.h

[Go to the documentation of this file.](kernel_2mm_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_KERNEL\_MM\_H

8#define ZEPHYR\_INCLUDE\_KERNEL\_MM\_H

9

10#include <[zephyr/sys/util.h](sys_2util_8h.md)>

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12#if defined(CONFIG\_ARM\_MMU) && defined(CONFIG\_ARM64)

13#include <[zephyr/arch/arm64/arm\_mem.h](arm__mem_8h.md)>

14#endif /\* CONFIG\_ARM\_MMU && CONFIG\_ARM64 \*/

15

16#include <[zephyr/kernel/internal/mm.h](kernel_2internal_2mm_8h.md)>

17

24

32

[ 34](group__kernel__memory__management.md#gaae7605452be94d1bd6e0364e9db113c6)#define K\_MEM\_CACHE\_NONE 2

35

[ 37](group__kernel__memory__management.md#ga1c8d5fee98c68b08cc6acf781eb35320)#define K\_MEM\_CACHE\_WT 1

38

[ 40](group__kernel__memory__management.md#ga802a69d7a53cafcf357861ab50258c99)#define K\_MEM\_CACHE\_WB 0

41

42/\*

43 \* ARM64 Specific flags are defined in arch/arm64/arm\_mem.h,

44 \* pay attention to be not conflicted when updating these flags.

45 \*/

46

[ 48](group__kernel__memory__management.md#gaae828c97c7bae5d235b863ff3b6b913e)#define K\_MEM\_CACHE\_MASK (BIT(3) - 1)

49

51

59

[ 61](group__kernel__memory__management.md#gab9ea94b7155e276f0b653bc1a081866e)#define K\_MEM\_PERM\_RW BIT(3)

62

[ 64](group__kernel__memory__management.md#gaf1b0db3c1c5b28b1810f39cdac03f9de)#define K\_MEM\_PERM\_EXEC BIT(4)

65

[ 67](group__kernel__memory__management.md#gaa96222e46728d507ca229796a5724425)#define K\_MEM\_PERM\_USER BIT(5)

68

70

76

[ 78](group__kernel__memory__management.md#ga36c4d2ede2f91490bc20ec399df663be)#define K\_MEM\_DIRECT\_MAP BIT(6)

79

81

82#ifndef \_ASMLANGUAGE

83#include <[stdint.h](stdint_8h.md)>

84#include <stddef.h>

85#include <[inttypes.h](inttypes_8h.md)>

86

87#ifdef \_\_cplusplus

88extern "C" {

89#endif

90

96

[ 106](group__kernel__memory__management.md#ga0a3569731c9a9f8e94e913f840b4be61)#define K\_MEM\_MAP\_UNINIT BIT(16)

107

[ 115](group__kernel__memory__management.md#ga7bed120eac76f03a55b1ab8a1f61ce8b)#define K\_MEM\_MAP\_LOCK BIT(17)

116

[ 134](group__kernel__memory__management.md#ga1275f42967e72f16c58bc3351656bced)#define K\_MEM\_MAP\_UNPAGED BIT(18)

135

137

[ 149](group__kernel__memory__management.md#gabb315b4994193147e9f51b0c3268bfcd)size\_t [k\_mem\_free\_get](group__kernel__memory__management.md#gabb315b4994193147e9f51b0c3268bfcd)(void);

150

[ 190](group__kernel__memory__management.md#gacf5f9c43ac2c31c376fed4a19f607feb)static inline void \*[k\_mem\_map](group__kernel__memory__management.md#gacf5f9c43ac2c31c376fed4a19f607feb)(size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

191{

192 return [k\_mem\_map\_phys\_guard](group__kernel__mm__internal__apis.md#ga2aeab99cba24ac3fd9479dbd421f6c5c)(([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), size, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), true);

193}

194

195#ifdef CONFIG\_DEMAND\_MAPPING

236static inline void \*k\_mem\_map\_unpaged([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

237{

238 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) |= [K\_MEM\_MAP\_UNPAGED](group__kernel__memory__management.md#ga1275f42967e72f16c58bc3351656bced);

239 return [k\_mem\_map\_phys\_guard](group__kernel__mm__internal__apis.md#ga2aeab99cba24ac3fd9479dbd421f6c5c)(location, size, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), false);

240}

241#endif

242

[ 256](group__kernel__memory__management.md#ga1867ea13671daae6a5f38929ea9fd64a)static inline void [k\_mem\_unmap](group__kernel__memory__management.md#ga1867ea13671daae6a5f38929ea9fd64a)(void \*addr, size\_t size)

257{

258 [k\_mem\_unmap\_phys\_guard](group__kernel__mm__internal__apis.md#gaca476fbacb86815edd4898b13ecf5120)(addr, size, true);

259}

260

[ 276](group__kernel__memory__management.md#gaf4740377cd87525fc81fa2ddafef084d)int [k\_mem\_update\_flags](group__kernel__memory__management.md#gaf4740377cd87525fc81fa2ddafef084d)(void \*addr, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

277

[ 291](group__kernel__memory__management.md#gad9a0110394e8026e27deb15687321ee9)size\_t [k\_mem\_region\_align](group__kernel__memory__management.md#gad9a0110394e8026e27deb15687321ee9)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*aligned\_addr, size\_t \*aligned\_size,

292 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, size\_t size, size\_t align);

293

294#ifdef \_\_cplusplus

295}

296#endif

297

299

300#endif /\* !\_ASMLANGUAGE \*/

301#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_MM\_H \*/

[arm\_mem.h](arm__mem_8h.md)

[K\_MEM\_MAP\_UNPAGED](group__kernel__memory__management.md#ga1275f42967e72f16c58bc3351656bced)

#define K\_MEM\_MAP\_UNPAGED

Region will be unpaged i.e.

**Definition** mm.h:134

[k\_mem\_unmap](group__kernel__memory__management.md#ga1867ea13671daae6a5f38929ea9fd64a)

static void k\_mem\_unmap(void \*addr, size\_t size)

Un-map mapped memory.

**Definition** mm.h:256

[k\_mem\_free\_get](group__kernel__memory__management.md#gabb315b4994193147e9f51b0c3268bfcd)

size\_t k\_mem\_free\_get(void)

Return the amount of free memory available.

[k\_mem\_map](group__kernel__memory__management.md#gacf5f9c43ac2c31c376fed4a19f607feb)

static void \* k\_mem\_map(size\_t size, uint32\_t flags)

Map anonymous memory into Zephyr's address space.

**Definition** mm.h:190

[k\_mem\_region\_align](group__kernel__memory__management.md#gad9a0110394e8026e27deb15687321ee9)

size\_t k\_mem\_region\_align(uintptr\_t \*aligned\_addr, size\_t \*aligned\_size, uintptr\_t addr, size\_t size, size\_t align)

Given an arbitrary region, provide a aligned region that covers it.

[k\_mem\_update\_flags](group__kernel__memory__management.md#gaf4740377cd87525fc81fa2ddafef084d)

int k\_mem\_update\_flags(void \*addr, size\_t size, uint32\_t flags)

Modify memory mapping attribute flags.

[k\_mem\_map\_phys\_guard](group__kernel__mm__internal__apis.md#ga2aeab99cba24ac3fd9479dbd421f6c5c)

void \* k\_mem\_map\_phys\_guard(uintptr\_t phys, size\_t size, uint32\_t flags, bool is\_anon)

Map memory into virtual address space with guard pages.

[k\_mem\_unmap\_phys\_guard](group__kernel__mm__internal__apis.md#gaca476fbacb86815edd4898b13ecf5120)

void k\_mem\_unmap\_phys\_guard(void \*addr, size\_t size, bool is\_anon)

Un-map memory mapped via k\_mem\_map\_phys\_guard().

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[inttypes.h](inttypes_8h.md)

[mm.h](kernel_2internal_2mm_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [mm.h](kernel_2mm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
