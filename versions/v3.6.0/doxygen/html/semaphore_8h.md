---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/semaphore_8h.html
original_path: doxygen/html/semaphore_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

semaphore.h File Reference

`#include <[zephyr/posix/time.h](include_2zephyr_2posix_2time_8h_source.md)>`  
`#include "[posix_types.h](posix__types_8h_source.md)"`

[Go to the source code of this file.](semaphore_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SEM\_FAILED](#a2ef55dcb46a51cb0f879f4c1724bdded)   (([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*) 0) |

| Functions | |
| --- | --- |
| int | [sem\_destroy](#a42cc945f89772ca24e87a569a5f2dbd7) ([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore) |
| int | [sem\_getvalue](#af4d15a2fd215951eb7ea2424ffdd335e) ([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) semaphore, int \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) value) |
| int | [sem\_init](#a1fee59859601fb325fafb32ee41b5691) ([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore, int pshared, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int value) |
| int | [sem\_post](#a2bee748f81a960f80dfccf675f38e3d8) ([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore) |
| int | [sem\_timedwait](#a91a6510735a16f94defc52ecbb7971ac) ([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) semaphore, struct [timespec](structtimespec.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) abstime) |
| int | [sem\_trywait](#a0f2fd32f79e2815f52f2afd2f5069960) ([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore) |
| int | [sem\_wait](#a355d892eec64a2dc95143635469c6524) ([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*semaphore) |
| [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \* | [sem\_open](#a0ed06fc3db017281dc6f1eefff97053a) (const char \*name, int oflags,...) |
| int | [sem\_unlink](#a776256d1a473906f8b7490689bfcb75c) (const char \*name) |
| int | [sem\_close](#a4e398fea1080fd7919e5c72ee94e2fc5) ([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*sem) |

## Macro Definition Documentation

## [◆ ](#a2ef55dcb46a51cb0f879f4c1724bdded)SEM\_FAILED

| #define SEM\_FAILED   (([sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*) 0) |
| --- |

## Function Documentation

## [◆ ](#a4e398fea1080fd7919e5c72ee94e2fc5)sem\_close()

| int sem\_close | ( | [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \* | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a42cc945f89772ca24e87a569a5f2dbd7)sem\_destroy()

| int sem\_destroy | ( | [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \* | *semaphore* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#af4d15a2fd215951eb7ea2424ffdd335e)sem\_getvalue()

| int sem\_getvalue | ( | [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *semaphore*, |
| --- | --- | --- | --- |
|  |  | int \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *value* ) |

## [◆ ](#a1fee59859601fb325fafb32ee41b5691)sem\_init()

| int sem\_init | ( | [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \* | *semaphore*, |
| --- | --- | --- | --- |
|  |  | int | *pshared*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *value* ) |

## [◆ ](#a0ed06fc3db017281dc6f1eefff97053a)sem\_open()

| [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \* sem\_open | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | int | *oflags*, |
|  |  |  | *...* ) |

## [◆ ](#a2bee748f81a960f80dfccf675f38e3d8)sem\_post()

| int sem\_post | ( | [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \* | *semaphore* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a91a6510735a16f94defc52ecbb7971ac)sem\_timedwait()

| int sem\_timedwait | ( | [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *semaphore*, |
| --- | --- | --- | --- |
|  |  | struct [timespec](structtimespec.md) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) | *abstime* ) |

## [◆ ](#a0f2fd32f79e2815f52f2afd2f5069960)sem\_trywait()

| int sem\_trywait | ( | [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \* | *semaphore* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a776256d1a473906f8b7490689bfcb75c)sem\_unlink()

| int sem\_unlink | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a355d892eec64a2dc95143635469c6524)sem\_wait()

| int sem\_wait | ( | [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e) \* | *semaphore* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [semaphore.h](semaphore_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
