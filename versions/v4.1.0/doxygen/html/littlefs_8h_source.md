---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/littlefs_8h_source.html
original_path: doxygen/html/littlefs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

littlefs.h

[Go to the documentation of this file.](littlefs_8h.md)

1/\*

2 \* Copyright (c) 2019 Bolt Innovation Management, LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_FS\_LITTLEFS\_H\_

8#define ZEPHYR\_INCLUDE\_FS\_LITTLEFS\_H\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[zephyr/storage/flash\_map.h](flash__map_8h.md)>

13

14#include <lfs.h>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 26](littlefs_8h.md#a45c16b03d0092e70d7e85a26cb432d5a)#define FS\_LITTLEFS\_DISK\_VERSION\_MAJOR\_GET(disk\_version) FIELD\_GET(GENMASK(31, 16), disk\_version)

27

[ 34](littlefs_8h.md#a1eca4a3091a41b0706016881667a8381)#define FS\_LITTLEFS\_DISK\_VERSION\_MINOR\_GET(disk\_version) FIELD\_GET(GENMASK(15, 0), disk\_version)

35

[ 37](structfs__littlefs.md)struct [fs\_littlefs](structfs__littlefs.md) {

38 /\* Defaulted in driver, customizable before mount. \*/

[ 39](structfs__littlefs.md#ab9b4cd8ce0aedfd071ea184d92b1224a) struct lfs\_config [cfg](structfs__littlefs.md#ab9b4cd8ce0aedfd071ea184d92b1224a);

40

41 /\* Must be cfg.cache\_size \*/

[ 42](structfs__littlefs.md#ac1b102a94e6db2dfb4ca0d0bee5a561e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[read\_buffer](structfs__littlefs.md#ac1b102a94e6db2dfb4ca0d0bee5a561e);

43

44 /\* Must be cfg.cache\_size \*/

[ 45](structfs__littlefs.md#a239d1ac90cc0de3a9cca766d41180def) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[prog\_buffer](structfs__littlefs.md#a239d1ac90cc0de3a9cca766d41180def);

46

47 /\* Must be cfg.lookahead\_size/4 elements, and

48 \* cfg.lookahead\_size must be a multiple of 8.

49 \*/

[ 50](structfs__littlefs.md#a7cd0dcd14e83138ba2ed698f55377e49) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[lookahead\_buffer](structfs__littlefs.md#a7cd0dcd14e83138ba2ed698f55377e49)[CONFIG\_FS\_LITTLEFS\_LOOKAHEAD\_SIZE / sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))];

51

52 /\* These structures are filled automatically at mount. \*/

[ 53](structfs__littlefs.md#a3a1902a64f78b65743786d154b435439) struct [lfs](structfs__littlefs.md#a3a1902a64f78b65743786d154b435439) [lfs](structfs__littlefs.md#a3a1902a64f78b65743786d154b435439);

[ 54](structfs__littlefs.md#a0ebbf427f161722fc269573d86e562c5) void \*[backend](structfs__littlefs.md#a0ebbf427f161722fc269573d86e562c5);

[ 55](structfs__littlefs.md#a337c24352a8f39c1d1f55682126341b5) struct [k\_mutex](structk__mutex.md) [mutex](structfs__littlefs.md#a337c24352a8f39c1d1f55682126341b5);

56};

57

[ 86](littlefs_8h.md#a1560f156ad9d0f9aed149b1ed5cb537b)#define FS\_LITTLEFS\_DECLARE\_CUSTOM\_CONFIG(name, alignment, read\_sz, prog\_sz, cache\_sz, \

87 lookahead\_sz) \

88 static uint8\_t \_\_aligned(alignment) name ## \_read\_buffer[cache\_sz]; \

89 static uint8\_t \_\_aligned(alignment) name ## \_prog\_buffer[cache\_sz]; \

90 static uint32\_t name ## \_lookahead\_buffer[(lookahead\_sz) / sizeof(uint32\_t)]; \

91 static struct fs\_littlefs name = { \

92 .cfg = { \

93 .read\_size = (read\_sz), \

94 .prog\_size = (prog\_sz), \

95 .cache\_size = (cache\_sz), \

96 .lookahead\_size = (lookahead\_sz), \

97 .read\_buffer = name ## \_read\_buffer, \

98 .prog\_buffer = name ## \_prog\_buffer, \

99 .lookahead\_buffer = name ## \_lookahead\_buffer, \

100 }, \

101 }

102

[ 112](littlefs_8h.md#a9f584969a034fb4058c28fed33164d7a)#define FS\_LITTLEFS\_DECLARE\_DEFAULT\_CONFIG(name) \

113 FS\_LITTLEFS\_DECLARE\_CUSTOM\_CONFIG(name, \

114 4, \

115 CONFIG\_FS\_LITTLEFS\_READ\_SIZE, \

116 CONFIG\_FS\_LITTLEFS\_PROG\_SIZE, \

117 CONFIG\_FS\_LITTLEFS\_CACHE\_SIZE, \

118 CONFIG\_FS\_LITTLEFS\_LOOKAHEAD\_SIZE)

119

120#ifdef \_\_cplusplus

121}

122#endif

123

124#endif /\* ZEPHYR\_INCLUDE\_FS\_LITTLEFS\_H\_ \*/

[flash\_map.h](flash__map_8h.md)

Public API for flash map.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[fs\_littlefs](structfs__littlefs.md)

Filesystem info structure for LittleFS mount.

**Definition** littlefs.h:37

[fs\_littlefs::backend](structfs__littlefs.md#a0ebbf427f161722fc269573d86e562c5)

void \* backend

**Definition** littlefs.h:54

[fs\_littlefs::prog\_buffer](structfs__littlefs.md#a239d1ac90cc0de3a9cca766d41180def)

uint8\_t \* prog\_buffer

**Definition** littlefs.h:45

[fs\_littlefs::mutex](structfs__littlefs.md#a337c24352a8f39c1d1f55682126341b5)

struct k\_mutex mutex

**Definition** littlefs.h:55

[fs\_littlefs::lfs](structfs__littlefs.md#a3a1902a64f78b65743786d154b435439)

struct lfs lfs

**Definition** littlefs.h:53

[fs\_littlefs::lookahead\_buffer](structfs__littlefs.md#a7cd0dcd14e83138ba2ed698f55377e49)

uint32\_t \* lookahead\_buffer[CONFIG\_FS\_LITTLEFS\_LOOKAHEAD\_SIZE/sizeof(uint32\_t)]

**Definition** littlefs.h:50

[fs\_littlefs::cfg](structfs__littlefs.md#ab9b4cd8ce0aedfd071ea184d92b1224a)

struct lfs\_config cfg

**Definition** littlefs.h:39

[fs\_littlefs::read\_buffer](structfs__littlefs.md#ac1b102a94e6db2dfb4ca0d0bee5a561e)

uint8\_t \* read\_buffer

**Definition** littlefs.h:42

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [littlefs.h](littlefs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
