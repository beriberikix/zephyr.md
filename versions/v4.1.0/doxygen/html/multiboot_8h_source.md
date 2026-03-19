---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/multiboot_8h_source.html
original_path: doxygen/html/multiboot_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

multiboot.h

[Go to the documentation of this file.](multiboot_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_MULTIBOOT\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_X86\_MULTIBOOT\_H\_

9

10#ifndef \_ASMLANGUAGE

11

12#include "[multiboot\_info.h](multiboot__info_8h.md)"

13

14extern struct [multiboot\_info](structmultiboot__info.md) [multiboot\_info](structmultiboot__info.md);

15

16#ifdef CONFIG\_MULTIBOOT\_INFO

17

18void z\_multiboot\_init(struct [multiboot\_info](structmultiboot__info.md) \*info\_pa);

19

20#else

21

22inline void z\_multiboot\_init(struct [multiboot\_info](structmultiboot__info.md) \*info\_pa)

23{

24 ARG\_UNUSED(info\_pa);

25}

26

27#endif /\* CONFIG\_MULTIBOOT\_INFO \*/

28

29/\*

30 \* the mmap\_addr field points to a series of entries of the following form.

31 \*/

32

[ 33](structmultiboot__mmap.md)struct [multiboot\_mmap](structmultiboot__mmap.md) {

[ 34](structmultiboot__mmap.md#ac5e189bd692ac3afa65c0a6bc1e25e08) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structmultiboot__mmap.md#ac5e189bd692ac3afa65c0a6bc1e25e08);

[ 35](structmultiboot__mmap.md#a7ef2fdd1ee5803c160010d821a1e772e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [base](structmultiboot__mmap.md#a7ef2fdd1ee5803c160010d821a1e772e);

[ 36](structmultiboot__mmap.md#a37729ad5026b219d25f7fe18c2d1e8ca) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [length](structmultiboot__mmap.md#a37729ad5026b219d25f7fe18c2d1e8ca);

[ 37](structmultiboot__mmap.md#a027d1cb939ca67d630ca3ab0143ef3f0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structmultiboot__mmap.md#a027d1cb939ca67d630ca3ab0143ef3f0);

38} \_\_packed;

39

40#endif /\* \_ASMLANGUAGE \*/

41

42/\* Boot type value (see prep\_c.c) \*/

[ 43](multiboot_8h.md#a06ef275439d876f323a821b67e6b4113)#define MULTIBOOT\_BOOT\_TYPE 1

44

45/\*

46 \* Possible values for multiboot\_mmap.type field.

47 \* Other values should be assumed to be unusable ranges.

48 \*/

49

[ 50](multiboot_8h.md#acd771d326981efd04d4127e9c4199cff)#define MULTIBOOT\_MMAP\_RAM 1 /\* available RAM \*/

[ 51](multiboot_8h.md#a132865c50004f3dfeb97d665990c843d)#define MULTIBOOT\_MMAP\_ACPI 3 /\* reserved for ACPI \*/

[ 52](multiboot_8h.md#a6a9dd86351aefc0f8adef49a43427cbf)#define MULTIBOOT\_MMAP\_NVS 4 /\* ACPI non-volatile \*/

[ 53](multiboot_8h.md#a6191e5ddf1f87ea3cccc5a232d74c74d)#define MULTIBOOT\_MMAP\_DEFECTIVE 5 /\* defective RAM module \*/

54

55/\*

56 \* Magic numbers: the kernel multiboot header (see crt0.S) begins with

57 \* MULTIBOOT\_HEADER\_MAGIC to signal to the booter that it supports

58 \* multiboot. On kernel entry, EAX is set to MULTIBOOT\_EAX\_MAGIC to

59 \* signal that the boot loader is multiboot compliant.

60 \*/

61

[ 62](multiboot_8h.md#ab36ad4b4a42c58aac4ad1f2ba13054e9)#define MULTIBOOT\_HEADER\_MAGIC 0x1BADB002

[ 63](multiboot_8h.md#a48040d17caa533b48233cf00f8dc7ba2)#define MULTIBOOT\_EAX\_MAGIC 0x2BADB002

64

65/\*

66 \* Typically, we put no flags in the multiboot header, as it exists solely

67 \* to reassure the loader that we're a valid binary. The exception to this

68 \* is when we want the loader to configure the framebuffer for us.

69 \*/

70

[ 71](multiboot_8h.md#a848a1462fa2f8907c8574136f5410b24)#define MULTIBOOT\_HEADER\_FLAG\_MEM BIT(1) /\* want mem\_/mmap\_\* info \*/

[ 72](multiboot_8h.md#ab615ba7169d9c368345342b256a322d2)#define MULTIBOOT\_HEADER\_FLAG\_FB BIT(2) /\* want fb\_\* info \*/

73

74#ifdef CONFIG\_INTEL\_MULTIBOOTFB\_DISPLAY

75#define MULTIBOOT\_HEADER\_FLAGS \

76 (MULTIBOOT\_HEADER\_FLAG\_FB | MULTIBOOT\_HEADER\_FLAG\_MEM)

77#else

[ 78](multiboot_8h.md#a5447ae8b3b45c8ed17ad61c267250992)#define MULTIBOOT\_HEADER\_FLAGS MULTIBOOT\_HEADER\_FLAG\_MEM

79#endif

80

81/\* The flags in the boot info structure tell us which fields are valid. \*/

82

[ 83](multiboot_8h.md#aac0e678a709bed9459227996d582f2de)#define MULTIBOOT\_INFO\_FLAGS\_MEM BIT(0) /\* mem\_\* valid \*/

[ 84](multiboot_8h.md#a8ec06e0c5da815a0190a921e8622cdaa)#define MULTIBOOT\_INFO\_FLAGS\_CMDLINE BIT(2) /\* cmdline\* valid \*/

[ 85](multiboot_8h.md#a1795eb5882e173fd014eb8bdeb4e69bc)#define MULTIBOOT\_INFO\_FLAGS\_MMAP BIT(6) /\* mmap\_\* valid \*/

[ 86](multiboot_8h.md#ad6aeb1c2eacec3b04818f77d0deeeaf6)#define MULTIBOOT\_INFO\_FLAGS\_FB BIT(12) /\* fb\_\* valid \*/

87

88/\* The only fb\_type we support is RGB. No text modes and no color palettes. \*/

89

[ 90](multiboot_8h.md#a418e7db9b4bfbe3a9a563e8030cf50ed)#define MULTIBOOT\_INFO\_FB\_TYPE\_RGB 1

91

92#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_MULTIBOOT\_H\_ \*/

[multiboot\_info.h](multiboot__info_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[multiboot\_info](structmultiboot__info.md)

**Definition** multiboot\_info.h:18

[multiboot\_mmap](structmultiboot__mmap.md)

**Definition** multiboot.h:33

[multiboot\_mmap::type](structmultiboot__mmap.md#a027d1cb939ca67d630ca3ab0143ef3f0)

uint32\_t type

**Definition** multiboot.h:37

[multiboot\_mmap::length](structmultiboot__mmap.md#a37729ad5026b219d25f7fe18c2d1e8ca)

uint64\_t length

**Definition** multiboot.h:36

[multiboot\_mmap::base](structmultiboot__mmap.md#a7ef2fdd1ee5803c160010d821a1e772e)

uint64\_t base

**Definition** multiboot.h:35

[multiboot\_mmap::size](structmultiboot__mmap.md#ac5e189bd692ac3afa65c0a6bc1e25e08)

uint32\_t size

**Definition** multiboot.h:34

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [multiboot.h](multiboot_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
