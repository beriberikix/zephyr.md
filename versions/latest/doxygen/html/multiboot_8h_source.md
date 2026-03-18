---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/multiboot_8h_source.html
original_path: doxygen/html/multiboot_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

12#include <[stdint.h](stdint_8h.md)>

13

14/\*

15 \* Multiboot (version 1) boot information structure.

16 \*

17 \* Only fields/values of interest to Zephyr are enumerated: at

18 \* present, that means only those pertaining to the framebuffer.

19 \*/

20

[ 21](structmultiboot__info.md)struct [multiboot\_info](structmultiboot__info.md) {

[ 22](structmultiboot__info.md#a33c78eb1aec2573f8293acf9a42fe2a8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structmultiboot__info.md#a33c78eb1aec2573f8293acf9a42fe2a8);

[ 23](structmultiboot__info.md#a8c88b721d871cb57a51feb5cd5fbdb6c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mem\_lower](structmultiboot__info.md#a8c88b721d871cb57a51feb5cd5fbdb6c);

[ 24](structmultiboot__info.md#a8ecb8953e55d1f6b75a3892cdc82a0b5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mem\_upper](structmultiboot__info.md#a8ecb8953e55d1f6b75a3892cdc82a0b5);

[ 25](structmultiboot__info.md#a7709e8650e2fa12efd1acd00245b0ea2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unused0](structmultiboot__info.md#a7709e8650e2fa12efd1acd00245b0ea2)[8];

[ 26](structmultiboot__info.md#a65bfac8b5152c771a4b8eadd408ca0d6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mmap\_length](structmultiboot__info.md#a65bfac8b5152c771a4b8eadd408ca0d6);

[ 27](structmultiboot__info.md#ac977f37274093fd9874d68dfb038e143) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mmap\_addr](structmultiboot__info.md#ac977f37274093fd9874d68dfb038e143);

[ 28](structmultiboot__info.md#a5eb3d633538c372a5edb6be72f9c667b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unused1](structmultiboot__info.md#a5eb3d633538c372a5edb6be72f9c667b)[9];

[ 29](structmultiboot__info.md#a4470854aa62c829c5ada578876a68944) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_addr\_lo](structmultiboot__info.md#a4470854aa62c829c5ada578876a68944);

[ 30](structmultiboot__info.md#a51ec099821903ee057a8163272da2760) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_addr\_hi](structmultiboot__info.md#a51ec099821903ee057a8163272da2760);

[ 31](structmultiboot__info.md#a1a412fb3d3f792b173787a65f32450d6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_pitch](structmultiboot__info.md#a1a412fb3d3f792b173787a65f32450d6);

[ 32](structmultiboot__info.md#ac0d58fbf588108f6f0109db47efeae37) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_width](structmultiboot__info.md#ac0d58fbf588108f6f0109db47efeae37);

[ 33](structmultiboot__info.md#a2a23c846d241bbb1469ec8565e8b3cef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_height](structmultiboot__info.md#a2a23c846d241bbb1469ec8565e8b3cef);

[ 34](structmultiboot__info.md#a0a5bc6718a8cae87416553fa6100b013) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fb\_bpp](structmultiboot__info.md#a0a5bc6718a8cae87416553fa6100b013);

[ 35](structmultiboot__info.md#a33735d95e34f7fc9588cea69efbb5075) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fb\_type](structmultiboot__info.md#a33735d95e34f7fc9588cea69efbb5075);

[ 36](structmultiboot__info.md#a7ddf1b8d00568efa22fbc11074d6fc98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fb\_color\_info](structmultiboot__info.md#a7ddf1b8d00568efa22fbc11074d6fc98)[6];

37};

38

39extern struct [multiboot\_info](structmultiboot__info.md) [multiboot\_info](structmultiboot__info.md);

40

41#ifdef CONFIG\_MULTIBOOT\_INFO

42

43extern void z\_multiboot\_init(struct [multiboot\_info](structmultiboot__info.md) \*info\_pa);

44

45#else

46

47inline void z\_multiboot\_init(struct [multiboot\_info](structmultiboot__info.md) \*info\_pa)

48{

49 ARG\_UNUSED(info\_pa);

50}

51

52#endif /\* CONFIG\_MULTIBOOT\_INFO \*/

53

54/\*

55 \* the mmap\_addr field points to a series of entries of the following form.

56 \*/

57

[ 58](structmultiboot__mmap.md)struct [multiboot\_mmap](structmultiboot__mmap.md) {

[ 59](structmultiboot__mmap.md#ac5e189bd692ac3afa65c0a6bc1e25e08) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structmultiboot__mmap.md#ac5e189bd692ac3afa65c0a6bc1e25e08);

[ 60](structmultiboot__mmap.md#a7ef2fdd1ee5803c160010d821a1e772e) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [base](structmultiboot__mmap.md#a7ef2fdd1ee5803c160010d821a1e772e);

[ 61](structmultiboot__mmap.md#a37729ad5026b219d25f7fe18c2d1e8ca) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [length](structmultiboot__mmap.md#a37729ad5026b219d25f7fe18c2d1e8ca);

[ 62](structmultiboot__mmap.md#a027d1cb939ca67d630ca3ab0143ef3f0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structmultiboot__mmap.md#a027d1cb939ca67d630ca3ab0143ef3f0);

63} \_\_packed;

64

65#endif /\* \_ASMLANGUAGE \*/

66

67/\* Boot type value (see prep\_c.c) \*/

[ 68](multiboot_8h.md#a06ef275439d876f323a821b67e6b4113)#define MULTIBOOT\_BOOT\_TYPE 1

69

70/\*

71 \* Possible values for multiboot\_mmap.type field.

72 \* Other values should be assumed to be unusable ranges.

73 \*/

74

[ 75](multiboot_8h.md#acd771d326981efd04d4127e9c4199cff)#define MULTIBOOT\_MMAP\_RAM 1 /\* available RAM \*/

[ 76](multiboot_8h.md#a132865c50004f3dfeb97d665990c843d)#define MULTIBOOT\_MMAP\_ACPI 3 /\* reserved for ACPI \*/

[ 77](multiboot_8h.md#a6a9dd86351aefc0f8adef49a43427cbf)#define MULTIBOOT\_MMAP\_NVS 4 /\* ACPI non-volatile \*/

[ 78](multiboot_8h.md#a6191e5ddf1f87ea3cccc5a232d74c74d)#define MULTIBOOT\_MMAP\_DEFECTIVE 5 /\* defective RAM module \*/

79

80/\*

81 \* Magic numbers: the kernel multiboot header (see crt0.S) begins with

82 \* MULTIBOOT\_HEADER\_MAGIC to signal to the booter that it supports

83 \* multiboot. On kernel entry, EAX is set to MULTIBOOT\_EAX\_MAGIC to

84 \* signal that the boot loader is multiboot compliant.

85 \*/

86

[ 87](multiboot_8h.md#ab36ad4b4a42c58aac4ad1f2ba13054e9)#define MULTIBOOT\_HEADER\_MAGIC 0x1BADB002

[ 88](multiboot_8h.md#a48040d17caa533b48233cf00f8dc7ba2)#define MULTIBOOT\_EAX\_MAGIC 0x2BADB002

89

90/\*

91 \* Typically, we put no flags in the multiboot header, as it exists solely

92 \* to reassure the loader that we're a valid binary. The exception to this

93 \* is when we want the loader to configure the framebuffer for us.

94 \*/

95

[ 96](multiboot_8h.md#a848a1462fa2f8907c8574136f5410b24)#define MULTIBOOT\_HEADER\_FLAG\_MEM BIT(1) /\* want mem\_/mmap\_\* info \*/

[ 97](multiboot_8h.md#ab615ba7169d9c368345342b256a322d2)#define MULTIBOOT\_HEADER\_FLAG\_FB BIT(2) /\* want fb\_\* info \*/

98

99#ifdef CONFIG\_INTEL\_MULTIBOOTFB\_DISPLAY

100#define MULTIBOOT\_HEADER\_FLAGS \

101 (MULTIBOOT\_HEADER\_FLAG\_FB | MULTIBOOT\_HEADER\_FLAG\_MEM)

102#else

[ 103](multiboot_8h.md#a5447ae8b3b45c8ed17ad61c267250992)#define MULTIBOOT\_HEADER\_FLAGS MULTIBOOT\_HEADER\_FLAG\_MEM

104#endif

105

106/\* The flags in the boot info structure tell us which fields are valid. \*/

107

[ 108](multiboot_8h.md#aac0e678a709bed9459227996d582f2de)#define MULTIBOOT\_INFO\_FLAGS\_MEM (1 << 0) /\* mem\_\* valid \*/

[ 109](multiboot_8h.md#a1795eb5882e173fd014eb8bdeb4e69bc)#define MULTIBOOT\_INFO\_FLAGS\_MMAP (1 << 6) /\* mmap\_\* valid \*/

[ 110](multiboot_8h.md#ad6aeb1c2eacec3b04818f77d0deeeaf6)#define MULTIBOOT\_INFO\_FLAGS\_FB (1 << 12) /\* fb\_\* valid \*/

111

112/\* The only fb\_type we support is RGB. No text modes and no color palettes. \*/

113

[ 114](multiboot_8h.md#a418e7db9b4bfbe3a9a563e8030cf50ed)#define MULTIBOOT\_INFO\_FB\_TYPE\_RGB 1

115

116#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_MULTIBOOT\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[multiboot\_info](structmultiboot__info.md)

**Definition** multiboot.h:21

[multiboot\_info::fb\_bpp](structmultiboot__info.md#a0a5bc6718a8cae87416553fa6100b013)

uint8\_t fb\_bpp

**Definition** multiboot.h:34

[multiboot\_info::fb\_pitch](structmultiboot__info.md#a1a412fb3d3f792b173787a65f32450d6)

uint32\_t fb\_pitch

**Definition** multiboot.h:31

[multiboot\_info::fb\_height](structmultiboot__info.md#a2a23c846d241bbb1469ec8565e8b3cef)

uint32\_t fb\_height

**Definition** multiboot.h:33

[multiboot\_info::fb\_type](structmultiboot__info.md#a33735d95e34f7fc9588cea69efbb5075)

uint8\_t fb\_type

**Definition** multiboot.h:35

[multiboot\_info::flags](structmultiboot__info.md#a33c78eb1aec2573f8293acf9a42fe2a8)

uint32\_t flags

**Definition** multiboot.h:22

[multiboot\_info::fb\_addr\_lo](structmultiboot__info.md#a4470854aa62c829c5ada578876a68944)

uint32\_t fb\_addr\_lo

**Definition** multiboot.h:29

[multiboot\_info::fb\_addr\_hi](structmultiboot__info.md#a51ec099821903ee057a8163272da2760)

uint32\_t fb\_addr\_hi

**Definition** multiboot.h:30

[multiboot\_info::unused1](structmultiboot__info.md#a5eb3d633538c372a5edb6be72f9c667b)

uint32\_t unused1[9]

**Definition** multiboot.h:28

[multiboot\_info::mmap\_length](structmultiboot__info.md#a65bfac8b5152c771a4b8eadd408ca0d6)

uint32\_t mmap\_length

**Definition** multiboot.h:26

[multiboot\_info::unused0](structmultiboot__info.md#a7709e8650e2fa12efd1acd00245b0ea2)

uint32\_t unused0[8]

**Definition** multiboot.h:25

[multiboot\_info::fb\_color\_info](structmultiboot__info.md#a7ddf1b8d00568efa22fbc11074d6fc98)

uint8\_t fb\_color\_info[6]

**Definition** multiboot.h:36

[multiboot\_info::mem\_lower](structmultiboot__info.md#a8c88b721d871cb57a51feb5cd5fbdb6c)

uint32\_t mem\_lower

**Definition** multiboot.h:23

[multiboot\_info::mem\_upper](structmultiboot__info.md#a8ecb8953e55d1f6b75a3892cdc82a0b5)

uint32\_t mem\_upper

**Definition** multiboot.h:24

[multiboot\_info::fb\_width](structmultiboot__info.md#ac0d58fbf588108f6f0109db47efeae37)

uint32\_t fb\_width

**Definition** multiboot.h:32

[multiboot\_info::mmap\_addr](structmultiboot__info.md#ac977f37274093fd9874d68dfb038e143)

uint32\_t mmap\_addr

**Definition** multiboot.h:27

[multiboot\_mmap](structmultiboot__mmap.md)

**Definition** multiboot.h:58

[multiboot\_mmap::type](structmultiboot__mmap.md#a027d1cb939ca67d630ca3ab0143ef3f0)

uint32\_t type

**Definition** multiboot.h:62

[multiboot\_mmap::length](structmultiboot__mmap.md#a37729ad5026b219d25f7fe18c2d1e8ca)

uint64\_t length

**Definition** multiboot.h:61

[multiboot\_mmap::base](structmultiboot__mmap.md#a7ef2fdd1ee5803c160010d821a1e772e)

uint64\_t base

**Definition** multiboot.h:60

[multiboot\_mmap::size](structmultiboot__mmap.md#ac5e189bd692ac3afa65c0a6bc1e25e08)

uint32\_t size

**Definition** multiboot.h:59

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [multiboot.h](multiboot_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
