---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/loader_8h_source.html
original_path: doxygen/html/loader_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

10#include <[zephyr/llext/elf.h](llext_2elf_8h.md)>

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

[ 50](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e) int (\*[prepare](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e))(struct [llext\_loader](structllext__loader.md) \*ldr);

51

[ 64](structllext__loader.md#a29a16df55b72bc299b338036437f53e0) int (\*[read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0))(struct [llext\_loader](structllext__loader.md) \*ldr, void \*out, size\_t len);

65

[ 77](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d) int (\*[seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d))(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

78

[ 89](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6) void \*(\*peek)(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

90

[ 96](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37) void (\*[finalize](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37))(struct [llext\_loader](structllext__loader.md) \*ldr);

97

99 [elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192) hdr;

100 [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) sects[[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

101 [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*sect\_hdrs;

102 bool sect\_hdrs\_on\_heap;

103 struct llext\_elf\_sect\_map \*sect\_map;

104 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sect\_cnt;

106};

107

109static inline int llext\_prepare(struct [llext\_loader](structllext__loader.md) \*l)

110{

111 if (l->[prepare](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e)) {

112 return l->[prepare](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e)(l);

113 }

114

115 return 0;

116}

117

118static inline int llext\_read(struct [llext\_loader](structllext__loader.md) \*l, void \*buf, size\_t len)

119{

120 return l->[read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0)(l, buf, len);

121}

122

123static inline int llext\_seek(struct [llext\_loader](structllext__loader.md) \*l, size\_t pos)

124{

125 return l->[seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d)(l, pos);

126}

127

128static inline void \*llext\_peek(struct [llext\_loader](structllext__loader.md) \*l, size\_t pos)

129{

130 if (l->[peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)) {

131 return l->[peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)(l, pos);

132 }

133

134 return NULL;

135}

136

137static inline void llext\_finalize(struct [llext\_loader](structllext__loader.md) \*l)

138{

139 if (l->[finalize](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37)) {

140 l->[finalize](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37)(l);

141 }

142}

143/\* @endcond \*/

144

148

149#ifdef \_\_cplusplus

150}

151#endif

152

153#endif /\* ZEPHYR\_LLEXT\_LOADER\_H \*/

[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)

@ LLEXT\_MEM\_COUNT

Number of regions managed by LLEXT.

**Definition** llext.h:57

[elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:461

[elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192)

struct elf64\_ehdr elf\_ehdr\_t

Dynamic features currently not used by LLEXT.

**Definition** elf.h:459

[elf.h](llext_2elf_8h.md)

Data structures and constants defined in the ELF specification.

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

**Definition** loader.h:77

[llext\_loader::read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0)

int(\* read)(struct llext\_loader \*ldr, void \*out, size\_t len)

Function to read (copy) from the loader.

**Definition** loader.h:64

[llext\_loader::prepare](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e)

int(\* prepare)(struct llext\_loader \*ldr)

Optional function to prepare the loader for loading extension.

**Definition** loader.h:50

[llext\_loader::finalize](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37)

void(\* finalize)(struct llext\_loader \*ldr)

Optional function to clean after the extension has been loaded or error occurred.

**Definition** loader.h:96

[llext\_loader::peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)

void \*(\* peek)(struct llext\_loader \*ldr, size\_t pos)

Optional function to peek at an absolute location in the ELF.

**Definition** loader.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [loader.h](loader_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
