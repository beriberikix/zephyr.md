---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hash__map__cxx_8h_source.html
original_path: doxygen/html/hash__map__cxx_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map\_cxx.h

[Go to the documentation of this file.](hash__map__cxx_8h.md)

1/\*

2 \* Copyright (c) 2022 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

17

18#ifndef ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_CXX\_H\_

19#define ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_CXX\_H\_

20

21#include <stddef.h>

22

23#include <[zephyr/sys/hash\_function.h](hash__function_8h.md)>

24#include <[zephyr/sys/hash\_map\_api.h](hash__map__api_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 43](hash__map__cxx_8h.md#ad528dfdf1ce8accb00db14b19cd56283)#define SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

44 SYS\_HASHMAP\_DEFINE\_ADVANCED(\_name, &sys\_hashmap\_cxx\_api, sys\_hashmap\_config, \

45 sys\_hashmap\_data, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

46

[ 60](hash__map__cxx_8h.md#ad675ea9b18e4183170e0e7ae6ad5bc96)#define SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

61 SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED(\_name, &sys\_hashmap\_cxx\_api, sys\_hashmap\_config, \

62 sys\_hashmap\_data, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

63

[ 71](hash__map__cxx_8h.md#aa45fa7446daaee2ad7cf90e14c6a60ac)#define SYS\_HASHMAP\_CXX\_DEFINE\_STATIC(\_name) \

72 SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED( \

73 \_name, sys\_hash32, SYS\_HASHMAP\_DEFAULT\_ALLOCATOR, \

74 SYS\_HASHMAP\_CONFIG(SIZE\_MAX, SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR))

75

[ 83](hash__map__cxx_8h.md#a10ff440e16c333ab59d3c3c2f60dedf1)#define SYS\_HASHMAP\_CXX\_DEFINE(\_name) \

84 SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED( \

85 \_name, sys\_hash32, SYS\_HASHMAP\_DEFAULT\_ALLOCATOR, \

86 SYS\_HASHMAP\_CONFIG(SIZE\_MAX, SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR))

87

88#ifdef CONFIG\_SYS\_HASH\_MAP\_CHOICE\_CXX

89#define SYS\_HASHMAP\_DEFAULT\_DEFINE(\_name) SYS\_HASHMAP\_CXX\_DEFINE(\_name)

90#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_STATIC(\_name) SYS\_HASHMAP\_CXX\_DEFINE\_STATIC(\_name)

91#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

92 SYS\_HASHMAP\_CXX\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

93#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

94 SYS\_HASHMAP\_CXX\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

95#endif

96

97extern const struct [sys\_hashmap\_api](structsys__hashmap__api.md) [sys\_hashmap\_cxx\_api](hash__map__cxx_8h.md#a53cf8ff9450b396239a928d7d079297c);

98

99#ifdef \_\_cplusplus

100}

101#endif

102

103#endif /\* ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_CXX\_H\_ \*/

[hash\_function.h](hash__function_8h.md)

[hash\_map\_api.h](hash__map__api_8h.md)

[sys\_hashmap\_cxx\_api](hash__map__cxx_8h.md#a53cf8ff9450b396239a928d7d079297c)

const struct sys\_hashmap\_api sys\_hashmap\_cxx\_api

[sys\_hashmap\_api](structsys__hashmap__api.md)

Generic Hashmap API.

**Definition** hash\_map\_api.h:168

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map\_cxx.h](hash__map__cxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
