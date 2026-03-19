---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html
original_path: doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

types.h

[Go to the documentation of this file.](lib_2libc_2minimal_2include_2sys_2types_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \* Copyright (c) 2017 ARM Ltd

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_TYPES\_H\_

9#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_TYPES\_H\_

10

11#include <[stdint.h](stdint_8h.md)>

12#include <[sys/\_types.h](__types_8h.md)>

13

[ 14](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00)typedef unsigned int [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00);

15

16#if !defined(\_\_ssize\_t\_defined)

17#define \_\_ssize\_t\_defined

18

19/\* Static code analysis tool can raise a violation

20 \* in the line below where name of macro 'unsigned' is the same

21 \* as keyword. It is made on purpose, deliberated deviation.

22 \*

23 \* We trick compiler to make sure the type of ssize\_t won't be unsigned long.

24 \* As otherwise the type of ssize\_t will be unsigned long

25 \* which is not correct. More details view in commit b889120

26 \*/

[ 27](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846)#define unsigned signed /\* parasoft-suppress MISRAC2012-RULE\_20\_4-a MISRAC2012-RULE\_20\_4-b \*/

[ 28](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)typedef \_\_SIZE\_TYPE\_\_ [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118);

29#undef unsigned

30

31#endif

32

33#if !defined(\_\_off\_t\_defined)

34#define \_\_off\_t\_defined

35/\* off\_t is defined such that it matches the size of a pointer \*/

[ 36](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)typedef \_\_INTPTR\_TYPE\_\_ [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f);

37#endif

38

39#if !defined(\_\_time\_t\_defined)

40#define \_\_time\_t\_defined

41typedef \_TIME\_T\_ [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7);

42#endif

43

44#if !defined(\_\_suseconds\_t\_defined)

45#define \_\_suseconds\_t\_defined

46typedef \_SUSECONDS\_T\_ [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995);

47#endif

48

49#if !defined(\_\_mem\_word\_t\_defined)

50#define \_\_mem\_word\_t\_defined

51

52/\*

53 \* The mem\_word\_t should match the optimal memory access word width

54 \* on the target platform. Here we defaults it to uintptr\_t.

55 \*/

56

[ 57](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4b99a5e6f726119280d6c241f140ebb6)typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [mem\_word\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4b99a5e6f726119280d6c241f140ebb6);

58

59#define Z\_MEM\_WORD\_T\_WIDTH \_\_INTPTR\_WIDTH\_\_

60

61#endif

62

63#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_TYPES\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995)

\_SUSECONDS\_T\_ suseconds\_t

**Definition** \_timespec.h:19

[\_types.h](__types_8h.md)

[mem\_word\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4b99a5e6f726119280d6c241f140ebb6)

uintptr\_t mem\_word\_t

**Definition** types.h:57

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00)

unsigned int mode\_t

**Definition** types.h:14

[stdint.h](stdint_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [sys](dir_4d70b020f8f8c9ca462b8905bdfa3f4f.md)
- [types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
