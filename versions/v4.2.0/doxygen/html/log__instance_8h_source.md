---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/log__instance_8h_source.html
original_path: doxygen/html/log__instance_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_instance.h

[Go to the documentation of this file.](log__instance_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_INSTANCE\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_INSTANCE\_H\_

8

9#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

10#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 17](structlog__source__const__data.md)struct [log\_source\_const\_data](structlog__source__const__data.md) {

[ 18](structlog__source__const__data.md#af1556767951362b57c14a5c3e717270b) const char \*[name](structlog__source__const__data.md#af1556767951362b57c14a5c3e717270b);

[ 19](structlog__source__const__data.md#acb4c059f66bc535885ecc56cbfa5b8b6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](structlog__source__const__data.md#acb4c059f66bc535885ecc56cbfa5b8b6);

20};

21

[ 23](structlog__source__dynamic__data.md)struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) {

[ 24](structlog__source__dynamic__data.md#a92adbfc1beaf3cb08340f054de8819ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [filters](structlog__source__dynamic__data.md#a92adbfc1beaf3cb08340f054de8819ef);

25#if defined(CONFIG\_64BIT)

26 /\* Workaround: Ensure that structure size is a multiple of 8 bytes. \*/

27 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dummy\_64;

28#endif

29};

30

37#define Z\_LOG\_ITEM\_CONST\_DATA(\_name) UTIL\_CAT(log\_const\_, \_name)

38

50#define Z\_LOG\_CONST\_ITEM\_REGISTER(\_name, \_str\_name, \_level) \

51 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_const, \

52 log\_source\_const\_data, \

53 Z\_LOG\_ITEM\_CONST\_DATA(\_name)) = \

54 { \

55 .name = \_str\_name, \

56 .level = (\_level), \

57 }

58

[ 67](log__instance_8h.md#a88d644c0d8e7b8985a37dca7f467ad9b)#define LOG\_OBJECT\_PTR\_INIT(\_name, \_object) \

68 IF\_ENABLED(CONFIG\_LOG, (.\_name = \_object,))

69

74#define Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst\_name) \

75 UTIL\_CAT(\_module\_name, UTIL\_CAT(\_, \_inst\_name))

76

86#define Z\_LOG\_OBJECT\_PTR(\_name) \

87 COND\_CODE\_1(CONFIG\_LOG\_RUNTIME\_FILTERING, \

88 (&LOG\_ITEM\_DYNAMIC\_DATA(\_name)), \

89 (&Z\_LOG\_ITEM\_CONST\_DATA(\_name))) \

90

[ 100](log__instance_8h.md#a96ff8eee1b58c6b6025a29608b5113b8)#define LOG\_INSTANCE\_PTR(\_module\_name, \_inst\_name) \

101 Z\_LOG\_OBJECT\_PTR(Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst\_name))

102

[ 115](log__instance_8h.md#a7389934373419d74129407ffba7ea3e3)#define LOG\_INSTANCE\_PTR\_INIT(\_name, \_module\_name, \_inst\_name) \

116 LOG\_OBJECT\_PTR\_INIT(\_name, LOG\_INSTANCE\_PTR(\_module\_name, \_inst\_name))

117

118#define Z\_LOG\_INSTANCE\_STRUCT \

119 COND\_CODE\_1(CONFIG\_LOG\_RUNTIME\_FILTERING, \

120 (struct log\_source\_dynamic\_data), \

121 (const struct log\_source\_const\_data))

122

[ 133](log__instance_8h.md#a224e4a75dca6d1b363ef49e96730dcfd)#define LOG\_INSTANCE\_PTR\_DECLARE(\_name) \

134 COND\_CODE\_1(CONFIG\_LOG, (Z\_LOG\_INSTANCE\_STRUCT \* \_name), \

135 (int \_name[TOOLCHAIN\_HAS\_ZLA ? 0 : 1]))

136

137#define Z\_LOG\_RUNTIME\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name) \

138 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_dynamic, log\_source\_dynamic\_data, \

139 LOG\_INSTANCE\_DYNAMIC\_DATA(\_module\_name, \_inst\_name))

140

141#define Z\_LOG\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name, \_level) \

142 Z\_LOG\_CONST\_ITEM\_REGISTER( \

143 Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst\_name), \

144 STRINGIFY(\_module\_name.\_inst\_name), \

145 \_level); \

146 IF\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING, \

147 (Z\_LOG\_RUNTIME\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name)))

148

[ 160](log__instance_8h.md#ad18f1e8ffbef38f285f70d8005fa144f)#define LOG\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name, \_level) \

161 IF\_ENABLED(CONFIG\_LOG, (Z\_LOG\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name, \_level)))

162

163#ifdef \_\_cplusplus

164}

165#endif

166

167#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_INSTANCE\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[log\_source\_const\_data](structlog__source__const__data.md)

Constant data associated with the source of log messages.

**Definition** log\_instance.h:17

[log\_source\_const\_data::level](structlog__source__const__data.md#acb4c059f66bc535885ecc56cbfa5b8b6)

uint8\_t level

**Definition** log\_instance.h:19

[log\_source\_const\_data::name](structlog__source__const__data.md#af1556767951362b57c14a5c3e717270b)

const char \* name

**Definition** log\_instance.h:18

[log\_source\_dynamic\_data](structlog__source__dynamic__data.md)

Dynamic data associated with the source of log messages.

**Definition** log\_instance.h:23

[log\_source\_dynamic\_data::filters](structlog__source__dynamic__data.md#a92adbfc1beaf3cb08340f054de8819ef)

uint32\_t filters

**Definition** log\_instance.h:24

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_instance.h](log__instance_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
