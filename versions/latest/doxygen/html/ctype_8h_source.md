---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ctype_8h_source.html
original_path: doxygen/html/ctype_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ctype.h

[Go to the documentation of this file.](ctype_8h.md)

1/\* ctype.h \*/

2

3/\*

4 \* Copyright (c) 2015 Intel Corporation.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_CTYPE\_H\_

10#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_CTYPE\_H\_

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](ctype_8h.md#a05d9ca901946ee2f2078c351163dc015)static inline int [isupper](ctype_8h.md#a05d9ca901946ee2f2078c351163dc015)(int a)

17{

18 return (int)((([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))(a)-([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))'A') < 26U);

19}

20

[ 21](ctype_8h.md#ab208778249f6c2cf8339e187e21e11bd)static inline int [isalpha](ctype_8h.md#ab208778249f6c2cf8339e187e21e11bd)(int c)

22{

23 return (int)(((([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))c|32u)-([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))'a') < 26U);

24}

25

[ 26](ctype_8h.md#a9318513eb3136e55002d65bf602f74a7)static inline int [isspace](ctype_8h.md#a9318513eb3136e55002d65bf602f74a7)(int c)

27{

28 return (int)(c == (int)' ' || (([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))c-([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))'\t') < 5U);

29}

30

[ 31](ctype_8h.md#a825ff84641e11035f0b6aa8f86eacbfd)static inline int [isgraph](ctype_8h.md#a825ff84641e11035f0b6aa8f86eacbfd)(int c)

32{

33 return (int)(((([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))c) > ' ') &&

34 ((([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))c) <= ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))'~'));

35}

36

[ 37](ctype_8h.md#ab14b97a75cf7392a543f89b5530e0ad7)static inline int [isprint](ctype_8h.md#ab14b97a75cf7392a543f89b5530e0ad7)(int c)

38{

39 return (int)(((([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))c) >= ' ') &&

40 ((([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))c) <= ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))'~'));

41}

42

[ 43](ctype_8h.md#a7c84919af75ed5a47fab36e2fa13775f)static inline int [isdigit](ctype_8h.md#a7c84919af75ed5a47fab36e2fa13775f)(int a)

44{

45 return (int)((([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))(a)-([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))'0') < 10U);

46}

47

[ 48](ctype_8h.md#a0152b6658f63acfdd96a9409d0142719)static inline int [isxdigit](ctype_8h.md#a0152b6658f63acfdd96a9409d0142719)(int a)

49{

50 unsigned int ua = (unsigned int)a;

51

52 return (int)(((ua - ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))'0') < 10U) ||

53 ((ua | 32U) - ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846))'a' < 6U));

54}

55

[ 56](ctype_8h.md#ab5088a2e14096e665c030d72508e2e9d)static inline int [tolower](ctype_8h.md#ab5088a2e14096e665c030d72508e2e9d)(int chr)

57{

58 return (chr >= (int)'A' && chr <= (int)'Z') ? (chr + 32) : (chr);

59}

60

[ 61](ctype_8h.md#abfe63aca83a67be16cf7b8636260b018)static inline int [toupper](ctype_8h.md#abfe63aca83a67be16cf7b8636260b018)(int chr)

62{

63 return (int)((chr >= (int)'a' && chr <=

64 (int)'z') ? (chr - 32) : (chr));

65}

66

[ 67](ctype_8h.md#ac4c06d14f1ed4d340b63aaeea1a830af)static inline int [isalnum](ctype_8h.md#ac4c06d14f1ed4d340b63aaeea1a830af)(int chr)

68{

69 return (int)([isalpha](ctype_8h.md#ab208778249f6c2cf8339e187e21e11bd)(chr) || [isdigit](ctype_8h.md#a7c84919af75ed5a47fab36e2fa13775f)(chr));

70}

71

[ 72](ctype_8h.md#a5d4143d99c571ef986ffc4a88df64097)static inline int [iscntrl](ctype_8h.md#a5d4143d99c571ef986ffc4a88df64097)(int c)

73{

74 return (int)((((unsigned int)c) <= 31U) || (((unsigned int)c) == 127U));

75}

76

77#ifdef \_\_cplusplus

78}

79#endif

80

81#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_CTYPE\_H\_ \*/

[isxdigit](ctype_8h.md#a0152b6658f63acfdd96a9409d0142719)

static int isxdigit(int a)

**Definition** ctype.h:48

[isupper](ctype_8h.md#a05d9ca901946ee2f2078c351163dc015)

static int isupper(int a)

**Definition** ctype.h:16

[iscntrl](ctype_8h.md#a5d4143d99c571ef986ffc4a88df64097)

static int iscntrl(int c)

**Definition** ctype.h:72

[isdigit](ctype_8h.md#a7c84919af75ed5a47fab36e2fa13775f)

static int isdigit(int a)

**Definition** ctype.h:43

[isgraph](ctype_8h.md#a825ff84641e11035f0b6aa8f86eacbfd)

static int isgraph(int c)

**Definition** ctype.h:31

[isspace](ctype_8h.md#a9318513eb3136e55002d65bf602f74a7)

static int isspace(int c)

**Definition** ctype.h:26

[isprint](ctype_8h.md#ab14b97a75cf7392a543f89b5530e0ad7)

static int isprint(int c)

**Definition** ctype.h:37

[isalpha](ctype_8h.md#ab208778249f6c2cf8339e187e21e11bd)

static int isalpha(int c)

**Definition** ctype.h:21

[tolower](ctype_8h.md#ab5088a2e14096e665c030d72508e2e9d)

static int tolower(int chr)

**Definition** ctype.h:56

[toupper](ctype_8h.md#abfe63aca83a67be16cf7b8636260b018)

static int toupper(int chr)

**Definition** ctype.h:61

[isalnum](ctype_8h.md#ac4c06d14f1ed4d340b63aaeea1a830af)

static int isalnum(int chr)

**Definition** ctype.h:67

[unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846)

#define unsigned

**Definition** types.h:27

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [ctype.h](ctype_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
