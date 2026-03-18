---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/loader_8h_source.html
original_path: doxygen/html/loader_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

23

24#include <[zephyr/llext/llext.h](llext_8h.md)>

25

[ 29](structllext__loader.md)struct [llext\_loader](structllext__loader.md) {

[ 43](structllext__loader.md#a29a16df55b72bc299b338036437f53e0) int (\*[read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0))(struct [llext\_loader](structllext__loader.md) \*ldr, void \*out, size\_t len);

44

[ 57](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d) int (\*[seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d))(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

58

[ 69](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6) void \*(\*peek)(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

70

72 [elf\_ehdr\_t](group__elf.md#gab39a1763256a6b9ccccf8b89836cd192) hdr;

73 [elf\_shdr\_t](group__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) sects[[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

74 enum [llext\_mem](group__llext.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) \*sect\_map;

75 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sect\_cnt;

77};

78

[ 79](group__llext__loader.md#gaf3d8bb89579039b77b10e6d15ff8a712)static inline int [llext\_read](group__llext__loader.md#gaf3d8bb89579039b77b10e6d15ff8a712)(struct [llext\_loader](structllext__loader.md) \*l, void \*buf, size\_t len)

80{

81 return l->[read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0)(l, buf, len);

82}

83

[ 84](group__llext__loader.md#gabbf3d285c9787cebe7bb105bacce15fa)static inline int [llext\_seek](group__llext__loader.md#gabbf3d285c9787cebe7bb105bacce15fa)(struct [llext\_loader](structllext__loader.md) \*l, size\_t pos)

85{

86 return l->[seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d)(l, pos);

87}

88

[ 89](group__llext__loader.md#ga241589ea6309b55ceb59f7e4b583600f)static inline void \*[llext\_peek](group__llext__loader.md#ga241589ea6309b55ceb59f7e4b583600f)(struct [llext\_loader](structllext__loader.md) \*l, size\_t pos)

90{

91 if (l->[peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)) {

92 return l->[peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)(l, pos);

93 }

94

95 return NULL;

96}

97

101

102#ifdef \_\_cplusplus

103}

104#endif

105

106#endif /\* ZEPHYR\_LLEXT\_LOADER\_H \*/

[elf.h](elf_8h.md)

[elf\_shdr\_t](group__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:440

[elf\_ehdr\_t](group__elf.md#gab39a1763256a6b9ccccf8b89836cd192)

struct elf64\_ehdr elf\_ehdr\_t

Machine sized elf header structure.

**Definition** elf.h:438

[llext\_peek](group__llext__loader.md#ga241589ea6309b55ceb59f7e4b583600f)

static void \* llext\_peek(struct llext\_loader \*l, size\_t pos)

**Definition** loader.h:89

[llext\_seek](group__llext__loader.md#gabbf3d285c9787cebe7bb105bacce15fa)

static int llext\_seek(struct llext\_loader \*l, size\_t pos)

**Definition** loader.h:84

[llext\_read](group__llext__loader.md#gaf3d8bb89579039b77b10e6d15ff8a712)

static int llext\_read(struct llext\_loader \*l, void \*buf, size\_t len)

**Definition** loader.h:79

[llext\_mem](group__llext.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)

llext\_mem

List of ELF regions that are stored or referenced in the llext.

**Definition** llext.h:31

[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)

@ LLEXT\_MEM\_COUNT

**Definition** llext.h:41

[llext.h](llext_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:29

[llext\_loader::seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d)

int(\* seek)(struct llext\_loader \*ldr, size\_t pos)

Seek to a new absolute location.

**Definition** loader.h:57

[llext\_loader::read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0)

int(\* read)(struct llext\_loader \*ldr, void \*out, size\_t len)

Read (copy) from the loader.

**Definition** loader.h:43

[llext\_loader::peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)

void \*(\* peek)(struct llext\_loader \*ldr, size\_t pos)

Peek at an absolute location.

**Definition** loader.h:69

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [loader.h](loader_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
