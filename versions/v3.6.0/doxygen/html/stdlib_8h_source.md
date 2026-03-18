---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stdlib_8h_source.html
original_path: doxygen/html/stdlib_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stdlib.h

[Go to the documentation of this file.](stdlib_8h.md)

1/\* stdlib.h \*/

2

3/\*

4 \* Copyright (c) 2011-2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDLIB\_H\_

10#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDLIB\_H\_

11

12#include <stddef.h>

13#include <[limits.h](limits_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](stdlib_8h.md#a6d257fc3f00865d0556ed7327c312b55)unsigned long [strtoul](stdlib_8h.md#a6d257fc3f00865d0556ed7327c312b55)(const char \*nptr, char \*\*endptr, int base);

[ 20](stdlib_8h.md#a311071298c2fe3e5d7057f396a6acfdc)long [strtol](stdlib_8h.md#a311071298c2fe3e5d7057f396a6acfdc)(const char \*nptr, char \*\*endptr, int base);

[ 21](stdlib_8h.md#ae5835422eb2dfc17ea8deb3b15bcc541)unsigned long long [strtoull](stdlib_8h.md#ae5835422eb2dfc17ea8deb3b15bcc541)(const char \*nptr, char \*\*endptr, int base);

[ 22](stdlib_8h.md#afb901aa665b7e2e3e27025ca77fecd1b)long long [strtoll](stdlib_8h.md#afb901aa665b7e2e3e27025ca77fecd1b)(const char \*nptr, char \*\*endptr, int base);

[ 23](stdlib_8h.md#a30670a60464f77af17dfb353353d6df8)int [atoi](stdlib_8h.md#a30670a60464f77af17dfb353353d6df8)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

24

[ 25](stdlib_8h.md#a9c36d0fe3ec4675cbffdc9b52f5fb399)void \*[malloc](stdlib_8h.md#a9c36d0fe3ec4675cbffdc9b52f5fb399)(size\_t size);

[ 26](stdlib_8h.md#a8006724372b77924155bd8618fe57516)void \*[aligned\_alloc](stdlib_8h.md#a8006724372b77924155bd8618fe57516)(size\_t alignment, size\_t size); /\* From C11 \*/

27

[ 28](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711)void [free](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711)(void \*ptr);

[ 29](stdlib_8h.md#a2807e26a012717736641384f91ab2563)void \*[calloc](stdlib_8h.md#a2807e26a012717736641384f91ab2563)(size\_t nmemb, size\_t size);

[ 30](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)void \*[realloc](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)(void \*ptr, size\_t size);

[ 31](stdlib_8h.md#aa34babf7c7883ba6714ac6d010952465)void \*[reallocarray](stdlib_8h.md#aa34babf7c7883ba6714ac6d010952465)(void \*ptr, size\_t nmemb, size\_t size);

32

[ 33](stdlib_8h.md#a5edc8d086d2525fdcd63486536cb4d9a)void \*[bsearch](stdlib_8h.md#a5edc8d086d2525fdcd63486536cb4d9a)(const void \*key, const void \*array,

34 size\_t count, size\_t size,

35 int (\*cmp)(const void \*key, const void \*element));

36

[ 37](stdlib_8h.md#a108744e70f6e2ca952e88277145d5346)void [qsort\_r](stdlib_8h.md#a108744e70f6e2ca952e88277145d5346)(void \*base, size\_t nmemb, size\_t size,

38 int (\*compar)(const void \*, const void \*, void \*), void \*arg);

[ 39](stdlib_8h.md#a216aaec88b41d3e2f8502a5b3365ea81)void [qsort](stdlib_8h.md#a216aaec88b41d3e2f8502a5b3365ea81)(void \*base, size\_t nmemb, size\_t size,

40 int (\*compar)(const void \*, const void \*));

41

[ 42](stdlib_8h.md#a687984f47d8cce148d1b914d2b79612a)#define EXIT\_SUCCESS 0

[ 43](stdlib_8h.md#a73efe787c131b385070f25d18b7c9aa4)#define EXIT\_FAILURE 1

44void \_exit(int status);

[ 45](stdlib_8h.md#af929aa40c441bb81bd806d5b44481af1)static inline void [exit](stdlib_8h.md#af929aa40c441bb81bd806d5b44481af1)(int status)

46{

47 \_exit(status);

48}

[ 49](stdlib_8h.md#a8dec7c95227ff149687066cf04029191)void [abort](stdlib_8h.md#a8dec7c95227ff149687066cf04029191)(void);

50

51#ifdef CONFIG\_MINIMAL\_LIBC\_RAND

52#define RAND\_MAX INT\_MAX

53int rand\_r(unsigned int \*seed);

54int rand(void);

55void srand(unsigned int seed);

56#endif /\* CONFIG\_MINIMAL\_LIBC\_RAND \*/

57

[ 58](stdlib_8h.md#ae0743c61576232ed6a443e6269af2b84)static inline int [abs](stdlib_8h.md#ae0743c61576232ed6a443e6269af2b84)(int \_\_n)

59{

60 return (\_\_n < 0) ? -\_\_n : \_\_n;

61}

62

[ 63](stdlib_8h.md#a8f842d6a8002a51ca6930a076ea86549)static inline long [labs](stdlib_8h.md#a8f842d6a8002a51ca6930a076ea86549)(long \_\_n)

64{

65 return (\_\_n < 0L) ? -\_\_n : \_\_n;

66}

67

[ 68](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)static inline long long [llabs](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)(long long \_\_n)

69{

70 return (\_\_n < 0LL) ? -\_\_n : \_\_n;

71}

72

73#ifdef \_\_cplusplus

74}

75#endif

76

77#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDLIB\_H\_ \*/

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[limits.h](limits_8h.md)

[qsort\_r](stdlib_8h.md#a108744e70f6e2ca952e88277145d5346)

void qsort\_r(void \*base, size\_t nmemb, size\_t size, int(\*compar)(const void \*, const void \*, void \*), void \*arg)

[qsort](stdlib_8h.md#a216aaec88b41d3e2f8502a5b3365ea81)

void qsort(void \*base, size\_t nmemb, size\_t size, int(\*compar)(const void \*, const void \*))

[calloc](stdlib_8h.md#a2807e26a012717736641384f91ab2563)

void \* calloc(size\_t nmemb, size\_t size)

[atoi](stdlib_8h.md#a30670a60464f77af17dfb353353d6df8)

int atoi(const char \*s)

[strtol](stdlib_8h.md#a311071298c2fe3e5d7057f396a6acfdc)

long strtol(const char \*nptr, char \*\*endptr, int base)

[llabs](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)

static long long llabs(long long \_\_n)

**Definition** stdlib.h:68

[bsearch](stdlib_8h.md#a5edc8d086d2525fdcd63486536cb4d9a)

void \* bsearch(const void \*key, const void \*array, size\_t count, size\_t size, int(\*cmp)(const void \*key, const void \*element))

[strtoul](stdlib_8h.md#a6d257fc3f00865d0556ed7327c312b55)

unsigned long strtoul(const char \*nptr, char \*\*endptr, int base)

[aligned\_alloc](stdlib_8h.md#a8006724372b77924155bd8618fe57516)

void \* aligned\_alloc(size\_t alignment, size\_t size)

[abort](stdlib_8h.md#a8dec7c95227ff149687066cf04029191)

void abort(void)

[labs](stdlib_8h.md#a8f842d6a8002a51ca6930a076ea86549)

static long labs(long \_\_n)

**Definition** stdlib.h:63

[malloc](stdlib_8h.md#a9c36d0fe3ec4675cbffdc9b52f5fb399)

void \* malloc(size\_t size)

[reallocarray](stdlib_8h.md#aa34babf7c7883ba6714ac6d010952465)

void \* reallocarray(void \*ptr, size\_t nmemb, size\_t size)

[realloc](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)

void \* realloc(void \*ptr, size\_t size)

[abs](stdlib_8h.md#ae0743c61576232ed6a443e6269af2b84)

static int abs(int \_\_n)

**Definition** stdlib.h:58

[strtoull](stdlib_8h.md#ae5835422eb2dfc17ea8deb3b15bcc541)

unsigned long long strtoull(const char \*nptr, char \*\*endptr, int base)

[exit](stdlib_8h.md#af929aa40c441bb81bd806d5b44481af1)

static void exit(int status)

**Definition** stdlib.h:45

[strtoll](stdlib_8h.md#afb901aa665b7e2e3e27025ca77fecd1b)

long long strtoll(const char \*nptr, char \*\*endptr, int base)

[free](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711)

void free(void \*ptr)

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [stdlib.h](stdlib_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
