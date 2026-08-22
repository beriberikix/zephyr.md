---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/llext__internal_8h_source.html
original_path: doxygen/html/llext__internal_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_internal.h

[Go to the documentation of this file.](llext__internal_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_INTERNAL\_H

8#define ZEPHYR\_LLEXT\_INTERNAL\_H

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/llext/llext.h](llext_8h.md)>

15

20

22

23

24struct llext\_elf\_sect\_map {

25 enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) mem\_idx;

26 size\_t offset;

27};

28

29const void \*llext\_loaded\_sect\_ptr(struct [llext\_loader](structllext__loader.md) \*ldr, struct [llext](structllext.md) \*ext, unsigned int sh\_ndx);

30

31

32static inline const char \*llext\_string(const struct [llext\_loader](structllext__loader.md) \*ldr, const struct [llext](structllext.md) \*ext,

33 enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) mem\_idx, unsigned int idx)

34{

35 return (const char \*)ext->[mem](structllext.md#ae9d529433f30ed659758c9b29c9b96bd)[mem\_idx] + idx;

36}

37

38static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) llext\_get\_reloc\_instruction\_location(struct [llext\_loader](structllext__loader.md) \*ldr,

39 struct [llext](structllext.md) \*ext,

40 int shndx,

41 const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rela)

42{

43 return ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) llext\_loaded\_sect\_ptr(ldr, ext, shndx) + rela->[r\_offset](structelf64__rela.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4);

44}

45

46static inline const char \*llext\_section\_name(const struct [llext\_loader](structllext__loader.md) \*ldr,

47 const struct [llext](structllext.md) \*ext,

48 const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*shdr)

49{

50 return llext\_string(ldr, ext, [LLEXT\_MEM\_SHSTRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e), shdr->[sh\_name](structelf64__shdr.md#af58da5c7c3e7712c51396eb937e1e783));

51}

52

53static inline const char \*llext\_symbol\_name(const struct [llext\_loader](structllext__loader.md) \*ldr,

54 const struct [llext](structllext.md) \*ext,

55 const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym)

56{

57 if ([ELF\_ST\_TYPE](group__llext__elf.md#ga972d66fcb6578448641a95d7a321dc4b)(sym->[st\_info](structelf64__sym.md#a48d593f11ef3d04b1f5d46f92aaa9839)) == [STT\_SECTION](group__llext__elf.md#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)) {

58 return llext\_section\_name(ldr, ext, ext->sect\_hdrs + sym->[st\_shndx](structelf64__sym.md#a285d9d47f979f7c0a3ae9ed18408d191));

59 } else {

60 return llext\_string(ldr, ext, [LLEXT\_MEM\_STRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17), sym->[st\_name](structelf64__sym.md#aee1394841b7752ed58b47da46f83c0a5));

61 }

62}

63

64/\*

65 \* Determine address of a symbol.

66 \*/

67int llext\_lookup\_symbol(struct [llext\_loader](structllext__loader.md) \*ldr, struct [llext](structllext.md) \*ext, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*link\_addr,

68 const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym, const char \*name,

69 const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*shdr);

70

71/\*

72 \* Read the symbol entry corresponding to a relocation from the binary.

73 \*/

74int llext\_read\_symbol(struct [llext\_loader](structllext__loader.md) \*ldr, struct [llext](structllext.md) \*ext, const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel,

75 [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym);

76

78

[ 90](llext__internal_8h.md#ace4d09c365b139a1def5af2f3372067a)int [arch\_elf\_relocate\_local](llext__internal_8h.md#ace4d09c365b139a1def5af2f3372067a)(struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext, const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel,

91 const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rel\_addr,

92 const struct [llext\_load\_param](structllext__load__param.md) \*ldr\_parm);

93

[ 105](llext__internal_8h.md#acf5a8cd07260bd76f990530ad41453f0)int [arch\_elf\_relocate\_global](llext__internal_8h.md#acf5a8cd07260bd76f990530ad41453f0)(struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext, const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel,

106 const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rel\_addr, const void \*link\_addr);

107

108#ifdef \_\_cplusplus

109}

110#endif

111

112#endif /\* ZEPHYR\_LLEXT\_INTERNAL\_H \*/

[llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)

llext\_mem

List of memory regions stored or referenced in the LLEXT subsystem.

**Definition** llext.h:44

[LLEXT\_MEM\_SHSTRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e)

@ LLEXT\_MEM\_SHSTRTAB

Section name strings.

**Definition** llext.h:52

[LLEXT\_MEM\_STRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17)

@ LLEXT\_MEM\_STRTAB

Symbol name strings.

**Definition** llext.h:51

[elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e)

struct elf64\_sym elf\_sym\_t

Machine sized symbol struct.

**Definition** elf.h:477

[ELF\_ST\_TYPE](group__llext__elf.md#ga972d66fcb6578448641a95d7a321dc4b)

#define ELF\_ST\_TYPE

Machine sized macro alias for obtaining a symbol type.

**Definition** elf.h:485

[STT\_SECTION](group__llext__elf.md#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)

#define STT\_SECTION

Section.

**Definition** elf.h:269

[elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:463

[elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)

struct elf64\_rela elf\_rela\_t

Machine sized relocation struct with addend.

**Definition** elf.h:475

[llext.h](llext_8h.md)

Support for linkable loadable extensions.

[arch\_elf\_relocate\_local](llext__internal_8h.md#ace4d09c365b139a1def5af2f3372067a)

int arch\_elf\_relocate\_local(struct llext\_loader \*loader, struct llext \*ext, const elf\_rela\_t \*rel, const elf\_sym\_t \*sym, uint8\_t \*rel\_addr, const struct llext\_load\_param \*ldr\_parm)

Architecture specific function for local binding relocations.

[arch\_elf\_relocate\_global](llext__internal_8h.md#acf5a8cd07260bd76f990530ad41453f0)

int arch\_elf\_relocate\_global(struct llext\_loader \*loader, struct llext \*ext, const elf\_rela\_t \*rel, const elf\_sym\_t \*sym, uint8\_t \*rel\_addr, const void \*link\_addr)

Architecture specific function for global binding relocations.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[elf64\_rela::r\_offset](structelf64__rela.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4)

elf64\_addr r\_offset

Offset in the section to perform a relocation.

**Definition** elf.h:378

[elf64\_shdr::sh\_name](structelf64__shdr.md#af58da5c7c3e7712c51396eb937e1e783)

elf64\_word sh\_name

Section header name index in section header string table.

**Definition** elf.h:179

[elf64\_sym::st\_shndx](structelf64__sym.md#a285d9d47f979f7c0a3ae9ed18408d191)

elf64\_half st\_shndx

Symbols related section given by section header index.

**Definition** elf.h:251

[elf64\_sym::st\_info](structelf64__sym.md#a48d593f11ef3d04b1f5d46f92aaa9839)

unsigned char st\_info

Symbol binding and type information.

**Definition** elf.h:247

[elf64\_sym::st\_name](structelf64__sym.md#aee1394841b7752ed58b47da46f83c0a5)

elf64\_word st\_name

Name of the symbol as an index into the symbol string table.

**Definition** elf.h:245

[llext\_load\_param](structllext__load__param.md)

Advanced llext\_load parameters.

**Definition** llext.h:150

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:80

[llext](structllext.md)

Structure describing a linkable loadable extension.

**Definition** llext.h:80

[llext::mem](structllext.md#ae9d529433f30ed659758c9b29c9b96bd)

void \* mem[LLEXT\_MEM\_COUNT]

Lookup table of memory regions.

**Definition** llext.h:95

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [llext\_internal.h](llext__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
