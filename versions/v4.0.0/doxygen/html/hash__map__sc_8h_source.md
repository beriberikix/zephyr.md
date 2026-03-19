---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hash__map__sc_8h_source.html
original_path: doxygen/html/hash__map__sc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map\_sc.h

[Go to the documentation of this file.](hash__map__sc_8h.md)

1/\*

2 \* Copyright (c) 2022 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_SC\_H\_

16#define ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_SC\_H\_

17

18#include <[stdbool.h](stdbool_8h.md)>

19#include <stddef.h>

20#include <[stdint.h](stdint_8h.md)>

21#include <[stdlib.h](stdlib_8h.md)>

22

23#include <[zephyr/sys/hash\_function.h](hash__function_8h.md)>

24#include <[zephyr/sys/hash\_map\_api.h](hash__map__api_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 43](hash__map__sc_8h.md#a8360409c9a02327046d6dd1858c82042)#define SYS\_HASHMAP\_SC\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

44 SYS\_HASHMAP\_DEFINE\_ADVANCED(\_name, &sys\_hashmap\_sc\_api, sys\_hashmap\_config, \

45 sys\_hashmap\_data, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

46

[ 60](hash__map__sc_8h.md#aec907531a89db3d4c108a00e06104c5f)#define SYS\_HASHMAP\_SC\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

61 SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED(\_name, &sys\_hashmap\_sc\_api, sys\_hashmap\_config, \

62 sys\_hashmap\_data, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

63

[ 71](hash__map__sc_8h.md#a47cb289884e08dc88027cf525b90315b)#define SYS\_HASHMAP\_SC\_DEFINE\_STATIC(\_name) \

72 SYS\_HASHMAP\_SC\_DEFINE\_STATIC\_ADVANCED( \

73 \_name, sys\_hash32, SYS\_HASHMAP\_DEFAULT\_ALLOCATOR, \

74 SYS\_HASHMAP\_CONFIG(SIZE\_MAX, SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR))

75

[ 83](hash__map__sc_8h.md#abb8b551888eb8936785f27ce6ffbcde2)#define SYS\_HASHMAP\_SC\_DEFINE(\_name) \

84 SYS\_HASHMAP\_SC\_DEFINE\_ADVANCED( \

85 \_name, sys\_hash32, SYS\_HASHMAP\_DEFAULT\_ALLOCATOR, \

86 SYS\_HASHMAP\_CONFIG(SIZE\_MAX, SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR))

87

88#ifdef CONFIG\_SYS\_HASH\_MAP\_CHOICE\_SC

89#define SYS\_HASHMAP\_DEFAULT\_DEFINE(\_name) SYS\_HASHMAP\_SC\_DEFINE(\_name)

90#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_STATIC(\_name) SYS\_HASHMAP\_SC\_DEFINE\_STATIC(\_name)

91#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

92 SYS\_HASHMAP\_SC\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

93#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

94 SYS\_HASHMAP\_SC\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

95#endif

96

97extern const struct [sys\_hashmap\_api](structsys__hashmap__api.md) [sys\_hashmap\_sc\_api](hash__map__sc_8h.md#a4216aeb7b4b499bdba830ae378368588);

98

99#ifdef \_\_cplusplus

100}

101#endif

102

103#endif /\* ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_SC\_H\_ \*/

[hash\_function.h](hash__function_8h.md)

[hash\_map\_api.h](hash__map__api_8h.md)

[sys\_hashmap\_sc\_api](hash__map__sc_8h.md#a4216aeb7b4b499bdba830ae378368588)

const struct sys\_hashmap\_api sys\_hashmap\_sc\_api

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[stdlib.h](stdlib_8h.md)

[sys\_hashmap\_api](structsys__hashmap__api.md)

Generic Hashmap API.

**Definition** hash\_map\_api.h:168

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map\_sc.h](hash__map__sc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
