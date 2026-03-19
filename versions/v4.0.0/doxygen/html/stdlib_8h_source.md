---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stdlib_8h_source.html
original_path: doxygen/html/stdlib_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

15#include <[zephyr/toolchain.h](toolchain_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 21](stdlib_8h.md#a6d257fc3f00865d0556ed7327c312b55)unsigned long [strtoul](stdlib_8h.md#a6d257fc3f00865d0556ed7327c312b55)(const char \*nptr, char \*\*endptr, int base);

[ 22](stdlib_8h.md#a311071298c2fe3e5d7057f396a6acfdc)long [strtol](stdlib_8h.md#a311071298c2fe3e5d7057f396a6acfdc)(const char \*nptr, char \*\*endptr, int base);

[ 23](stdlib_8h.md#ae5835422eb2dfc17ea8deb3b15bcc541)unsigned long long [strtoull](stdlib_8h.md#ae5835422eb2dfc17ea8deb3b15bcc541)(const char \*nptr, char \*\*endptr, int base);

[ 24](stdlib_8h.md#afb901aa665b7e2e3e27025ca77fecd1b)long long [strtoll](stdlib_8h.md#afb901aa665b7e2e3e27025ca77fecd1b)(const char \*nptr, char \*\*endptr, int base);

[ 25](stdlib_8h.md#a30670a60464f77af17dfb353353d6df8)int [atoi](stdlib_8h.md#a30670a60464f77af17dfb353353d6df8)(const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

26

[ 27](stdlib_8h.md#a9c36d0fe3ec4675cbffdc9b52f5fb399)void \*[malloc](stdlib_8h.md#a9c36d0fe3ec4675cbffdc9b52f5fb399)(size\_t size);

[ 28](stdlib_8h.md#a8006724372b77924155bd8618fe57516)void \*[aligned\_alloc](stdlib_8h.md#a8006724372b77924155bd8618fe57516)(size\_t alignment, size\_t size); /\* From C11 \*/

29

[ 30](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711)void [free](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711)(void \*ptr);

[ 31](stdlib_8h.md#a2807e26a012717736641384f91ab2563)void \*[calloc](stdlib_8h.md#a2807e26a012717736641384f91ab2563)(size\_t nmemb, size\_t size);

[ 32](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)void \*[realloc](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)(void \*ptr, size\_t size);

[ 33](stdlib_8h.md#aa34babf7c7883ba6714ac6d010952465)void \*[reallocarray](stdlib_8h.md#aa34babf7c7883ba6714ac6d010952465)(void \*ptr, size\_t nmemb, size\_t size);

34

[ 35](stdlib_8h.md#a5edc8d086d2525fdcd63486536cb4d9a)void \*[bsearch](stdlib_8h.md#a5edc8d086d2525fdcd63486536cb4d9a)(const void \*key, const void \*array,

36 size\_t count, size\_t size,

37 int (\*cmp)(const void \*key, const void \*element));

38

[ 39](stdlib_8h.md#a108744e70f6e2ca952e88277145d5346)void [qsort\_r](stdlib_8h.md#a108744e70f6e2ca952e88277145d5346)(void \*base, size\_t nmemb, size\_t size,

40 int (\*compar)(const void \*, const void \*, void \*), void \*arg);

[ 41](stdlib_8h.md#a216aaec88b41d3e2f8502a5b3365ea81)void [qsort](stdlib_8h.md#a216aaec88b41d3e2f8502a5b3365ea81)(void \*base, size\_t nmemb, size\_t size,

42 int (\*compar)(const void \*, const void \*));

43

[ 44](stdlib_8h.md#a687984f47d8cce148d1b914d2b79612a)#define EXIT\_SUCCESS 0

[ 45](stdlib_8h.md#a73efe787c131b385070f25d18b7c9aa4)#define EXIT\_FAILURE 1

46FUNC\_NORETURN void \_exit(int status);

[ 47](stdlib_8h.md#ab924785decfca67fd65380b76a269206)FUNC\_NORETURN static inline void [exit](stdlib_8h.md#ab924785decfca67fd65380b76a269206)(int status)

48{

49 \_exit(status);

50}

[ 51](stdlib_8h.md#a4bef6384a1777699c6eba3125e690419)FUNC\_NORETURN void [abort](stdlib_8h.md#a4bef6384a1777699c6eba3125e690419)(void);

52

53#ifdef CONFIG\_MINIMAL\_LIBC\_RAND

54#define RAND\_MAX INT\_MAX

55int rand\_r(unsigned int \*seed);

56int rand(void);

57void srand(unsigned int seed);

58#endif /\* CONFIG\_MINIMAL\_LIBC\_RAND \*/

59

[ 60](stdlib_8h.md#ae0743c61576232ed6a443e6269af2b84)static inline int [abs](stdlib_8h.md#ae0743c61576232ed6a443e6269af2b84)(int \_\_n)

61{

62 return (\_\_n < 0) ? -\_\_n : \_\_n;

63}

64

[ 65](stdlib_8h.md#a8f842d6a8002a51ca6930a076ea86549)static inline long [labs](stdlib_8h.md#a8f842d6a8002a51ca6930a076ea86549)(long \_\_n)

66{

67 return (\_\_n < 0L) ? -\_\_n : \_\_n;

68}

69

[ 70](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)static inline long long [llabs](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)(long long \_\_n)

71{

72 return (\_\_n < 0LL) ? -\_\_n : \_\_n;

73}

74

[ 75](stdlib_8h.md#ab1ec8cf93b9478de49bb3e77465ab4af)char \*[getenv](stdlib_8h.md#ab1ec8cf93b9478de49bb3e77465ab4af)(const char \*name);

76#if \_POSIX\_C\_SOURCE >= 200112L

77int setenv(const char \*name, const char \*val, int overwrite);

78int unsetenv(const char \*name);

79#endif

80

81#ifdef \_BSD\_SOURCE

82int getenv\_r(const char \*name, char \*buf, size\_t len);

83#endif

84

85#ifdef \_\_cplusplus

86}

87#endif

88

89#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_STDLIB\_H\_ \*/

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

[abort](stdlib_8h.md#a4bef6384a1777699c6eba3125e690419)

FUNC\_NORETURN void abort(void)

[llabs](stdlib_8h.md#a5613b9b7ce990f94ceaaf1f455cc98e6)

static long long llabs(long long \_\_n)

**Definition** stdlib.h:70

[bsearch](stdlib_8h.md#a5edc8d086d2525fdcd63486536cb4d9a)

void \* bsearch(const void \*key, const void \*array, size\_t count, size\_t size, int(\*cmp)(const void \*key, const void \*element))

[strtoul](stdlib_8h.md#a6d257fc3f00865d0556ed7327c312b55)

unsigned long strtoul(const char \*nptr, char \*\*endptr, int base)

[aligned\_alloc](stdlib_8h.md#a8006724372b77924155bd8618fe57516)

void \* aligned\_alloc(size\_t alignment, size\_t size)

[labs](stdlib_8h.md#a8f842d6a8002a51ca6930a076ea86549)

static long labs(long \_\_n)

**Definition** stdlib.h:65

[malloc](stdlib_8h.md#a9c36d0fe3ec4675cbffdc9b52f5fb399)

void \* malloc(size\_t size)

[reallocarray](stdlib_8h.md#aa34babf7c7883ba6714ac6d010952465)

void \* reallocarray(void \*ptr, size\_t nmemb, size\_t size)

[getenv](stdlib_8h.md#ab1ec8cf93b9478de49bb3e77465ab4af)

char \* getenv(const char \*name)

[exit](stdlib_8h.md#ab924785decfca67fd65380b76a269206)

static FUNC\_NORETURN void exit(int status)

**Definition** stdlib.h:47

[realloc](stdlib_8h.md#ad28fed1039f35d754710633141b4edf0)

void \* realloc(void \*ptr, size\_t size)

[abs](stdlib_8h.md#ae0743c61576232ed6a443e6269af2b84)

static int abs(int \_\_n)

**Definition** stdlib.h:60

[strtoull](stdlib_8h.md#ae5835422eb2dfc17ea8deb3b15bcc541)

unsigned long long strtoull(const char \*nptr, char \*\*endptr, int base)

[strtoll](stdlib_8h.md#afb901aa665b7e2e3e27025ca77fecd1b)

long long strtoll(const char \*nptr, char \*\*endptr, int base)

[free](stdlib_8h.md#afbedc913aa4651b3c3b4b3aecd9b4711)

void free(void \*ptr)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [stdlib.h](stdlib_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
