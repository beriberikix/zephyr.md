---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/inspect_8h_source.html
original_path: doxygen/html/inspect_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inspect.h

[Go to the documentation of this file.](inspect_8h.md)

1/\*

2 \* Copyright (c) 2025 Arduino SA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_INSPECT\_H

8#define ZEPHYR\_LLEXT\_INSPECT\_H

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <stddef.h>

15#include <[zephyr/llext/llext.h](llext_8h.md)>

16#include <[zephyr/llext/loader.h](loader_8h.md)>

17#include <[zephyr/llext/llext\_internal.h](llext__internal_8h.md)>

18

31

[ 48](group__llext__inspect__apis.md#gabef549f07291126f39b5065be3f73599)static inline int [llext\_get\_region\_info](group__llext__inspect__apis.md#gabef549f07291126f39b5065be3f73599)(const struct [llext\_loader](structllext__loader.md) \*ldr,

49 const struct [llext](structllext.md) \*ext,

50 enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) region,

51 const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*\*hdr,

52 const void \*\*addr, size\_t \*size)

53{

54 if ((unsigned int)region >= [LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)) {

55 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

56 }

57

58 if (hdr) {

59 \*hdr = &ldr->sects[region];

60 }

61

62 /\* address and size compensated for alignment prepad \*/

63 if (addr) {

64 \*addr = (void \*)(([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))ext->[mem](structllext.md#ae9d529433f30ed659758c9b29c9b96bd)[region] + ldr->sects[region].sh\_info);

65 }

66 if (size) {

67 \*size = ext->[mem\_size](structllext.md#a47cfcb60d773a6c16d2fda8cc5011a16)[region] - ldr->sects[region].sh\_info;

68 }

69

70 return 0;

71}

72

[ 86](group__llext__inspect__apis.md#ga655023e915eb0ef60e76c0c1625c63c9)int [llext\_section\_shndx](group__llext__inspect__apis.md#ga655023e915eb0ef60e76c0c1625c63c9)(const struct [llext\_loader](structllext__loader.md) \*ldr, const struct [llext](structllext.md) \*ext,

87 const char \*section\_name);

88

[ 108](group__llext__inspect__apis.md#ga23121962662f057da004ac1c527716e3)static inline int [llext\_get\_section\_info](group__llext__inspect__apis.md#ga23121962662f057da004ac1c527716e3)(const struct [llext\_loader](structllext__loader.md) \*ldr,

109 const struct [llext](structllext.md) \*ext,

110 unsigned int shndx,

111 const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*\*hdr,

112 enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) \*region,

113 size\_t \*offset)

114{

115 if (shndx < 0 || shndx >= ext->sect\_cnt) {

116 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

117 }

118 if (!ldr->sect\_map) {

119 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

120 }

121

122 enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) mem\_idx = ldr->sect\_map[shndx].mem\_idx;

123

124 if (hdr) {

125 \*hdr = &ext->sect\_hdrs[shndx];

126 }

127 if (region) {

128 \*region = mem\_idx;

129 }

130

131 /\* offset compensated for alignment prepad \*/

132 if (offset) {

133 \*offset = ldr->sect\_map[shndx].offset - ldr->sects[mem\_idx].sh\_info;

134 }

135

136 return 0;

137}

138

142

143#ifdef \_\_cplusplus

144}

145#endif

146

147#endif /\* ZEPHYR\_LLEXT\_INSPECT\_H \*/

[llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)

llext\_mem

List of memory regions stored or referenced in the LLEXT subsystem.

**Definition** llext.h:44

[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)

@ LLEXT\_MEM\_COUNT

Number of regions managed by LLEXT.

**Definition** llext.h:57

[elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:463

[llext\_get\_section\_info](group__llext__inspect__apis.md#ga23121962662f057da004ac1c527716e3)

static int llext\_get\_section\_info(const struct llext\_loader \*ldr, const struct llext \*ext, unsigned int shndx, const elf\_shdr\_t \*\*hdr, enum llext\_mem \*region, size\_t \*offset)

Get information about a section for the specified extension.

**Definition** inspect.h:108

[llext\_section\_shndx](group__llext__inspect__apis.md#ga655023e915eb0ef60e76c0c1625c63c9)

int llext\_section\_shndx(const struct llext\_loader \*ldr, const struct llext \*ext, const char \*section\_name)

Get the index of a section with the specified name.

[llext\_get\_region\_info](group__llext__inspect__apis.md#gabef549f07291126f39b5065be3f73599)

static int llext\_get\_region\_info(const struct llext\_loader \*ldr, const struct llext \*ext, enum llext\_mem region, const elf\_shdr\_t \*\*hdr, const void \*\*addr, size\_t \*size)

Get information about a memory region for the specified extension.

**Definition** inspect.h:48

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[llext.h](llext_8h.md)

Support for linkable loadable extensions.

[llext\_internal.h](llext__internal_8h.md)

Private header for linkable loadable extensions.

[loader.h](loader_8h.md)

LLEXT ELF loader context types.

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:80

[llext](structllext.md)

Structure describing a linkable loadable extension.

**Definition** llext.h:80

[llext::mem\_size](structllext.md#a47cfcb60d773a6c16d2fda8cc5011a16)

size\_t mem\_size[LLEXT\_MEM\_COUNT]

Size of each stored region.

**Definition** llext.h:101

[llext::mem](structllext.md#ae9d529433f30ed659758c9b29c9b96bd)

void \* mem[LLEXT\_MEM\_COUNT]

Lookup table of memory regions.

**Definition** llext.h:95

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [inspect.h](inspect_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
