---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/log__instance_8h_source.html
original_path: doxygen/html/log__instance_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

20#ifdef CONFIG\_NIOS2

21 /\* Workaround alert! Dummy data to ensure that structure is >8 bytes.

22 \* Nios2 uses global pointer register for structures <=8 bytes and

23 \* apparently does not handle well variables placed in custom sections.

24 \*/

25 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dummy;

26#endif

27};

28

[ 30](structlog__source__dynamic__data.md)struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) {

[ 31](structlog__source__dynamic__data.md#a92adbfc1beaf3cb08340f054de8819ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [filters](structlog__source__dynamic__data.md#a92adbfc1beaf3cb08340f054de8819ef);

32#ifdef CONFIG\_NIOS2

33 /\* Workaround alert! Dummy data to ensure that structure is >8 bytes.

34 \* Nios2 uses global pointer register for structures <=8 bytes and

35 \* apparently does not handle well variables placed in custom sections.

36 \*/

37 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dummy[2];

38#endif

39#if defined(CONFIG\_RISCV) && defined(CONFIG\_64BIT)

40 /\* Workaround: RV64 needs to ensure that structure is just 8 bytes. \*/

41 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dummy;

42#endif

43};

44

51#define Z\_LOG\_ITEM\_CONST\_DATA(\_name) UTIL\_CAT(log\_const\_, \_name)

52

64#define Z\_LOG\_CONST\_ITEM\_REGISTER(\_name, \_str\_name, \_level) \

65 const STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_const, \

66 log\_source\_const\_data, \

67 Z\_LOG\_ITEM\_CONST\_DATA(\_name)) = \

68 { \

69 .name = \_str\_name, \

70 .level = (\_level), \

71 }

72

[ 81](log__instance_8h.md#a88d644c0d8e7b8985a37dca7f467ad9b)#define LOG\_OBJECT\_PTR\_INIT(\_name, \_object) \

82 IF\_ENABLED(CONFIG\_LOG, (.\_name = \_object,))

83

88#define Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst\_name) \

89 UTIL\_CAT(\_module\_name, UTIL\_CAT(\_, \_inst\_name))

90

100#define Z\_LOG\_OBJECT\_PTR(\_name) \

101 COND\_CODE\_1(CONFIG\_LOG\_RUNTIME\_FILTERING, \

102 (&LOG\_ITEM\_DYNAMIC\_DATA(\_name)), \

103 (&Z\_LOG\_ITEM\_CONST\_DATA(\_name))) \

104

[ 114](log__instance_8h.md#a96ff8eee1b58c6b6025a29608b5113b8)#define LOG\_INSTANCE\_PTR(\_module\_name, \_inst\_name) \

115 Z\_LOG\_OBJECT\_PTR(Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst\_name))

116

[ 129](log__instance_8h.md#a7389934373419d74129407ffba7ea3e3)#define LOG\_INSTANCE\_PTR\_INIT(\_name, \_module\_name, \_inst\_name) \

130 LOG\_OBJECT\_PTR\_INIT(\_name, LOG\_INSTANCE\_PTR(\_module\_name, \_inst\_name))

131

132#define Z\_LOG\_INSTANCE\_STRUCT \

133 COND\_CODE\_1(CONFIG\_LOG\_RUNTIME\_FILTERING, \

134 (struct log\_source\_dynamic\_data), \

135 (const struct log\_source\_const\_data))

136

[ 147](log__instance_8h.md#a224e4a75dca6d1b363ef49e96730dcfd)#define LOG\_INSTANCE\_PTR\_DECLARE(\_name) \

148 COND\_CODE\_1(CONFIG\_LOG, (Z\_LOG\_INSTANCE\_STRUCT \* \_name), \

149 (int \_name[TOOLCHAIN\_HAS\_ZLA ? 0 : 1]))

150

151#define Z\_LOG\_RUNTIME\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name) \

152 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(log\_dynamic, log\_source\_dynamic\_data, \

153 LOG\_INSTANCE\_DYNAMIC\_DATA(\_module\_name, \_inst\_name))

154

155#define Z\_LOG\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name, \_level) \

156 Z\_LOG\_CONST\_ITEM\_REGISTER( \

157 Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst\_name), \

158 STRINGIFY(\_module\_name.\_inst\_name), \

159 \_level); \

160 IF\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING, \

161 (Z\_LOG\_RUNTIME\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name)))

162

[ 174](log__instance_8h.md#ad18f1e8ffbef38f285f70d8005fa144f)#define LOG\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name, \_level) \

175 IF\_ENABLED(CONFIG\_LOG, (Z\_LOG\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name, \_level)))

176

177#ifdef \_\_cplusplus

178}

179#endif

180

181#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_INSTANCE\_H\_ \*/

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

**Definition** log\_instance.h:30

[log\_source\_dynamic\_data::filters](structlog__source__dynamic__data.md#a92adbfc1beaf3cb08340f054de8819ef)

uint32\_t filters

**Definition** log\_instance.h:31

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_instance.h](log__instance_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
