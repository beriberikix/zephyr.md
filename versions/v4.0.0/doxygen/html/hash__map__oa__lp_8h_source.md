---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hash__map__oa__lp_8h_source.html
original_path: doxygen/html/hash__map__oa__lp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map\_oa\_lp.h

[Go to the documentation of this file.](hash__map__oa__lp_8h.md)

1/\*

2 \* Copyright (c) 2022 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_OA\_LP\_H\_

16#define ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_OA\_LP\_H\_

17

18#include <stddef.h>

19

20#include <[zephyr/sys/hash\_function.h](hash__function_8h.md)>

21#include <[zephyr/sys/hash\_map\_api.h](hash__map__api_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 27](structsys__hashmap__oa__lp__data.md)struct [sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md) {

[ 28](structsys__hashmap__oa__lp__data.md#a4f989f86a54a1806a33539a3834eeb60) void \*[buckets](structsys__hashmap__oa__lp__data.md#a4f989f86a54a1806a33539a3834eeb60);

[ 29](structsys__hashmap__oa__lp__data.md#ac129a45aacac72b3c9974e6c7c7e19fd) size\_t [n\_buckets](structsys__hashmap__oa__lp__data.md#ac129a45aacac72b3c9974e6c7c7e19fd);

[ 30](structsys__hashmap__oa__lp__data.md#a2a4c622b61b78989e66c831d6dc75988) size\_t [size](structsys__hashmap__oa__lp__data.md#a2a4c622b61b78989e66c831d6dc75988);

[ 31](structsys__hashmap__oa__lp__data.md#a3cc4ecc190d8ed71211c659ff2402a8f) size\_t [n\_tombstones](structsys__hashmap__oa__lp__data.md#a3cc4ecc190d8ed71211c659ff2402a8f);

32};

33

[ 47](hash__map__oa__lp_8h.md#aa9287e614c6ea567ae022be887c730fc)#define SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

48 SYS\_HASHMAP\_DEFINE\_ADVANCED(\_name, &sys\_hashmap\_oa\_lp\_api, sys\_hashmap\_config, \

49 sys\_hashmap\_oa\_lp\_data, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

50

[ 64](hash__map__oa__lp_8h.md#a6ad7aa3485e69dcb0a204276aae74128)#define SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

65 SYS\_HASHMAP\_DEFINE\_STATIC\_ADVANCED(\_name, &sys\_hashmap\_oa\_lp\_api, sys\_hashmap\_config, \

66 sys\_hashmap\_oa\_lp\_data, \_hash\_func, \_alloc\_func, \

67 \_\_VA\_ARGS\_\_)

68

[ 76](hash__map__oa__lp_8h.md#a19cd65566823c760ee3961214992952b)#define SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC(\_name) \

77 SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED( \

78 \_name, sys\_hash32, SYS\_HASHMAP\_DEFAULT\_ALLOCATOR, \

79 SYS\_HASHMAP\_CONFIG(SIZE\_MAX, SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR))

80

[ 88](hash__map__oa__lp_8h.md#a591f4c0f17011fbec639ecd5a61a9c07)#define SYS\_HASHMAP\_OA\_LP\_DEFINE(\_name) \

89 SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED( \

90 \_name, sys\_hash32, SYS\_HASHMAP\_DEFAULT\_ALLOCATOR, \

91 SYS\_HASHMAP\_CONFIG(SIZE\_MAX, SYS\_HASHMAP\_DEFAULT\_LOAD\_FACTOR))

92

93#ifdef CONFIG\_SYS\_HASH\_MAP\_CHOICE\_OA\_LP

94#define SYS\_HASHMAP\_DEFAULT\_DEFINE(\_name) SYS\_HASHMAP\_OA\_LP\_DEFINE(\_name)

95#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_STATIC(\_name) SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC(\_name)

96#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

97 SYS\_HASHMAP\_OA\_LP\_DEFINE\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

98#define SYS\_HASHMAP\_DEFAULT\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, ...) \

99 SYS\_HASHMAP\_OA\_LP\_DEFINE\_STATIC\_ADVANCED(\_name, \_hash\_func, \_alloc\_func, \_\_VA\_ARGS\_\_)

100#endif

101

102extern const struct [sys\_hashmap\_api](structsys__hashmap__api.md) [sys\_hashmap\_oa\_lp\_api](hash__map__oa__lp_8h.md#ab4383b628d3da139a3bf276eefde82f9);

103

104#ifdef \_\_cplusplus

105}

106#endif

107

108#endif /\* ZEPHYR\_INCLUDE\_SYS\_HASH\_MAP\_OA\_LP\_H\_ \*/

[hash\_function.h](hash__function_8h.md)

[hash\_map\_api.h](hash__map__api_8h.md)

[sys\_hashmap\_oa\_lp\_api](hash__map__oa__lp_8h.md#ab4383b628d3da139a3bf276eefde82f9)

const struct sys\_hashmap\_api sys\_hashmap\_oa\_lp\_api

[sys\_hashmap\_api](structsys__hashmap__api.md)

Generic Hashmap API.

**Definition** hash\_map\_api.h:168

[sys\_hashmap\_oa\_lp\_data](structsys__hashmap__oa__lp__data.md)

**Definition** hash\_map\_oa\_lp.h:27

[sys\_hashmap\_oa\_lp\_data::size](structsys__hashmap__oa__lp__data.md#a2a4c622b61b78989e66c831d6dc75988)

size\_t size

**Definition** hash\_map\_oa\_lp.h:30

[sys\_hashmap\_oa\_lp\_data::n\_tombstones](structsys__hashmap__oa__lp__data.md#a3cc4ecc190d8ed71211c659ff2402a8f)

size\_t n\_tombstones

**Definition** hash\_map\_oa\_lp.h:31

[sys\_hashmap\_oa\_lp\_data::buckets](structsys__hashmap__oa__lp__data.md#a4f989f86a54a1806a33539a3834eeb60)

void \* buckets

**Definition** hash\_map\_oa\_lp.h:28

[sys\_hashmap\_oa\_lp\_data::n\_buckets](structsys__hashmap__oa__lp__data.md#ac129a45aacac72b3c9974e6c7c7e19fd)

size\_t n\_buckets

**Definition** hash\_map\_oa\_lp.h:29

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map\_oa\_lp.h](hash__map__oa__lp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
