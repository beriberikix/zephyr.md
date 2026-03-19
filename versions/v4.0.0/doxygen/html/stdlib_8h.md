---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stdlib_8h.html
original_path: doxygen/html/stdlib_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stdlib.h File Reference

`#include <stddef.h>`  
`#include <[limits.h](limits_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](stdlib_8h_source.md)

| Macros | |
| --- | --- |
| #define | [EXIT\_SUCCESS](#a687984f47d8cce148d1b914d2b79612a)   0 |
| #define | [EXIT\_FAILURE](#a73efe787c131b385070f25d18b7c9aa4)   1 |

| Functions | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [strtoul](#a6d257fc3f00865d0556ed7327c312b55) (const char \*nptr, char \*\*endptr, int base) |
| long | [strtol](#a311071298c2fe3e5d7057f396a6acfdc) (const char \*nptr, char \*\*endptr, int base) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long long | [strtoull](#ae5835422eb2dfc17ea8deb3b15bcc541) (const char \*nptr, char \*\*endptr, int base) |
| long long | [strtoll](#afb901aa665b7e2e3e27025ca77fecd1b) (const char \*nptr, char \*\*endptr, int base) |
| int | [atoi](#a30670a60464f77af17dfb353353d6df8) (const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| void \* | [malloc](#a9c36d0fe3ec4675cbffdc9b52f5fb399) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| void \* | [aligned\_alloc](#a8006724372b77924155bd8618fe57516) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) alignment, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| void | [free](#afbedc913aa4651b3c3b4b3aecd9b4711) (void \*ptr) |
| void \* | [calloc](#a2807e26a012717736641384f91ab2563) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nmemb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| void \* | [realloc](#ad28fed1039f35d754710633141b4edf0) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| void \* | [reallocarray](#aa34babf7c7883ba6714ac6d010952465) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nmemb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| void \* | [bsearch](#a5edc8d086d2525fdcd63486536cb4d9a) (const void \*key, const void \*array, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, int(\*cmp)(const void \*key, const void \*element)) |
| void | [qsort\_r](#a108744e70f6e2ca952e88277145d5346) (void \*base, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nmemb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, int(\*compar)(const void \*, const void \*, void \*), void \*arg) |
| void | [qsort](#a216aaec88b41d3e2f8502a5b3365ea81) (void \*base, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nmemb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, int(\*compar)(const void \*, const void \*)) |
| static FUNC\_NORETURN void | [exit](#ab924785decfca67fd65380b76a269206) (int status) |
| FUNC\_NORETURN void | [abort](#a4bef6384a1777699c6eba3125e690419) (void) |
| static int | [abs](#ae0743c61576232ed6a443e6269af2b84) (int \_\_n) |
| static long | [labs](#a8f842d6a8002a51ca6930a076ea86549) (long \_\_n) |
| static long long | [llabs](#a5613b9b7ce990f94ceaaf1f455cc98e6) (long long \_\_n) |
| char \* | [getenv](#ab1ec8cf93b9478de49bb3e77465ab4af) (const char \*name) |

## Macro Definition Documentation

## [◆ ](#a73efe787c131b385070f25d18b7c9aa4)EXIT\_FAILURE

| #define EXIT\_FAILURE   1 |
| --- |

## [◆ ](#a687984f47d8cce148d1b914d2b79612a)EXIT\_SUCCESS

| #define EXIT\_SUCCESS   0 |
| --- |

## Function Documentation

## [◆ ](#a4bef6384a1777699c6eba3125e690419)abort()

| FUNC\_NORETURN void abort | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae0743c61576232ed6a443e6269af2b84)abs()

| | int abs | ( | int | *\_\_n* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8006724372b77924155bd8618fe57516)aligned\_alloc()

| void \* aligned\_alloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *alignment*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

## [◆ ](#a30670a60464f77af17dfb353353d6df8)atoi()

| int atoi | ( | const char \* | *s* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5edc8d086d2525fdcd63486536cb4d9a)bsearch()

| void \* bsearch | ( | const void \* | *key*, |
| --- | --- | --- | --- |
|  |  | const void \* | *array*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | int(\* | *cmp*)(const void \*key, const void \*element) ) |

## [◆ ](#a2807e26a012717736641384f91ab2563)calloc()

| void \* calloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *nmemb*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

## [◆ ](#ab924785decfca67fd65380b76a269206)exit()

| | FUNC\_NORETURN void exit | ( | int | *status* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#afbedc913aa4651b3c3b4b3aecd9b4711)free()

| void free | ( | void \* | *ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ab1ec8cf93b9478de49bb3e77465ab4af)getenv()

| char \* getenv | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a8f842d6a8002a51ca6930a076ea86549)labs()

| | long labs | ( | long | *\_\_n* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5613b9b7ce990f94ceaaf1f455cc98e6)llabs()

| | long long llabs | ( | long long | *\_\_n* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9c36d0fe3ec4675cbffdc9b52f5fb399)malloc()

| void \* malloc | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a216aaec88b41d3e2f8502a5b3365ea81)qsort()

| void qsort | ( | void \* | *base*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *nmemb*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | int(\* | *compar*)(const void \*, const void \*) ) |

## [◆ ](#a108744e70f6e2ca952e88277145d5346)qsort\_r()

| void qsort\_r | ( | void \* | *base*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *nmemb*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | int(\* | *compar*)(const void \*, const void \*, void \*), |
|  |  | void \* | *arg* ) |

## [◆ ](#ad28fed1039f35d754710633141b4edf0)realloc()

| void \* realloc | ( | void \* | *ptr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

## [◆ ](#aa34babf7c7883ba6714ac6d010952465)reallocarray()

| void \* reallocarray | ( | void \* | *ptr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *nmemb*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

## [◆ ](#a311071298c2fe3e5d7057f396a6acfdc)strtol()

| long strtol | ( | const char \* | *nptr*, |
| --- | --- | --- | --- |
|  |  | char \*\* | *endptr*, |
|  |  | int | *base* ) |

## [◆ ](#afb901aa665b7e2e3e27025ca77fecd1b)strtoll()

| long long strtoll | ( | const char \* | *nptr*, |
| --- | --- | --- | --- |
|  |  | char \*\* | *endptr*, |
|  |  | int | *base* ) |

## [◆ ](#a6d257fc3f00865d0556ed7327c312b55)strtoul()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long strtoul | ( | const char \* | *nptr*, |
| --- | --- | --- | --- |
|  |  | char \*\* | *endptr*, |
|  |  | int | *base* ) |

## [◆ ](#ae5835422eb2dfc17ea8deb3b15bcc541)strtoull()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long long strtoull | ( | const char \* | *nptr*, |
| --- | --- | --- | --- |
|  |  | char \*\* | *endptr*, |
|  |  | int | *base* ) |

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [stdlib.h](stdlib_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
