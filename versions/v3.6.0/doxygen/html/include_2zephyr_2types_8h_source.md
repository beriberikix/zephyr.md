---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2types_8h_source.html
original_path: doxygen/html/include_2zephyr_2types_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

32#ifdef \_\_cplusplus

33/\* Zephyr requires an int main(void) signature with C linkage for the application main if present \*/

34extern int main(void);

35#endif

36

37#ifdef \_\_cplusplus

38}

39#endif

40

41#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_TYPES\_H\_ \*/

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
