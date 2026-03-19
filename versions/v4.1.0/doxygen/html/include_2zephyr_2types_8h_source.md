---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/include_2zephyr_2types_8h_source.html
original_path: doxygen/html/include_2zephyr_2types_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

types.h

[Go to the documentation of this file.](include_2zephyr_2types_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_TYPES\_H\_

8#define ZEPHYR\_INCLUDE\_ZEPHYR\_TYPES\_H\_

9

10#include <stddef.h>

11#include <[stdint.h](stdint_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17/\*

18 \* A type with strong alignment requirements, similar to C11 max\_align\_t. It can

19 \* be used to force alignment of data structures allocated on the stack or as

20 \* return \* type for heap allocators.

21 \*/

22typedef union {

23 long long thelonglong;

24 long double thelongdouble;

25 [uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40) theuintmax\_t;

26 size\_t thesize\_t;

27 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) theuintptr\_t;

28 void \*thepvoid;

29 void (\*thepfunc)(void);

30} z\_max\_align\_t;

31

32/\*

33 \* Thread local variables are declared with different keywords depending on

34 \* which C/C++ standard that is used. C++11 and C23 uses "thread\_local" whilst

35 \* C11 uses "\_Thread\_local". Previously the GNU "\_\_thread" keyword was used

36 \* which is the same in both gcc and g++.

37 \*/

38#ifndef Z\_THREAD\_LOCAL

39#if defined(\_\_cplusplus) && (\_\_cplusplus) >= 201103L /\* C++11 \*/

40#define Z\_THREAD\_LOCAL thread\_local

41#elif defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) >= 202311L /\* C23 \*/

42#define Z\_THREAD\_LOCAL thread\_local

43#elif defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) >= 201112L /\* C11 \*/

44#define Z\_THREAD\_LOCAL \_Thread\_local

45#else /\* Default back to old behavior which used the GNU keyword. \*/

46#define Z\_THREAD\_LOCAL \_\_thread

47#endif

48#endif /\* Z\_THREAD\_LOCAL \*/

49

50#ifdef \_\_cplusplus

51/\* Zephyr requires an int main(void) signature with C linkage for the application main if present \*/

52extern int main(void);

53#endif

54

55#ifdef \_\_cplusplus

56}

57#endif

58

59#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_TYPES\_H\_ \*/

[stdint.h](stdint_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uintmax\_t](stdint_8h.md#aac7deaa1633720ec64bd432bbc31af40)

\_\_UINT64\_TYPE\_\_ uintmax\_t

**Definition** stdint.h:92

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [types.h](include_2zephyr_2types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
