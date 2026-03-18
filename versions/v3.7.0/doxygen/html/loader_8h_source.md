---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/loader_8h_source.html
original_path: doxygen/html/loader_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loader.h

[Go to the documentation of this file.](loader_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_LOADER\_H

8#define ZEPHYR\_LLEXT\_LOADER\_H

9

10#include <[zephyr/llext/elf.h](elf_8h.md)>

11#include <stddef.h>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

28

29#include <[zephyr/llext/llext.h](llext_8h.md)>

30

32struct llext\_elf\_sect\_map; /\* defined in llext\_priv.h \*/

34

[ 42](structllext__loader.md)struct [llext\_loader](structllext__loader.md) {

[ 55](structllext__loader.md#a29a16df55b72bc299b338036437f53e0) int (\*[read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0))(struct [llext\_loader](structllext__loader.md) \*ldr, void \*out, size\_t len);

56

[ 68](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d) int (\*[seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d))(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

69

[ 80](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6) void \*(\*peek)(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

81

83 [elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192) hdr;

84 [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) sects[[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

85 [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*sect\_hdrs;

86 bool sect\_hdrs\_on\_heap;

87 struct llext\_elf\_sect\_map \*sect\_map;

88 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sect\_cnt;

90};

91

93static inline int llext\_read(struct [llext\_loader](structllext__loader.md) \*l, void \*buf, size\_t len)

94{

95 return l->[read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0)(l, buf, len);

96}

97

98static inline int llext\_seek(struct [llext\_loader](structllext__loader.md) \*l, size\_t pos)

99{

100 return l->[seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d)(l, pos);

101}

102

103static inline void \*llext\_peek(struct [llext\_loader](structllext__loader.md) \*l, size\_t pos)

104{

105 if (l->[peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)) {

106 return l->[peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)(l, pos);

107 }

108

109 return NULL;

110}

111/\* @endcond \*/

112

116

117#ifdef \_\_cplusplus

118}

119#endif

120

121#endif /\* ZEPHYR\_LLEXT\_LOADER\_H \*/

[elf.h](elf_8h.md)

Data structures and constants defined in the ELF specification.

[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)

@ LLEXT\_MEM\_COUNT

Number of regions managed by LLEXT.

**Definition** llext.h:54

[elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:504

[elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192)

struct elf64\_ehdr elf\_ehdr\_t

Relocation names (should be moved to arch-specific files).

**Definition** elf.h:502

[llext.h](llext_8h.md)

Support for linkable loadable extensions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:42

[llext\_loader::seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d)

int(\* seek)(struct llext\_loader \*ldr, size\_t pos)

Function to seek to a new absolute location in the stream.

**Definition** loader.h:68

[llext\_loader::read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0)

int(\* read)(struct llext\_loader \*ldr, void \*out, size\_t len)

Function to read (copy) from the loader.

**Definition** loader.h:55

[llext\_loader::peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)

void \*(\* peek)(struct llext\_loader \*ldr, size\_t pos)

Optional function to peek at an absolute location in the ELF.

**Definition** loader.h:80

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [loader.h](loader_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
