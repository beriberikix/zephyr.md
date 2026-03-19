---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mutex_8h.html
original_path: doxygen/html/mutex_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mutex.h File Reference

`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`  
`#include <zephyr/syscalls/mutex.h>`

[Go to the source code of this file.](mutex_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_mutex](structsys__mutex.md) |

| Macros | |
| --- | --- |
| #define | [SYS\_MUTEX\_DEFINE](group__user__mutex__apis.md#ga486bd6a11d0b0d312cdf8a6a8f66c1a3)(name) |
|  | Statically define and initialize a [sys\_mutex](structsys__mutex.md). |

| Functions | |
| --- | --- |
| static void | [sys\_mutex\_init](group__user__mutex__apis.md#ga5456b75934cb26abc974a45ae82d717b) (struct [sys\_mutex](structsys__mutex.md) \*mutex) |
|  | Initialize a mutex. |
| static int | [sys\_mutex\_lock](group__user__mutex__apis.md#ga6887005f8223d4f36de5ae5c02ba4b17) (struct [sys\_mutex](structsys__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Lock a mutex. |
| static int | [sys\_mutex\_unlock](group__user__mutex__apis.md#ga7d4babcd161600dab5f1842c58be2a1f) (struct [sys\_mutex](structsys__mutex.md) \*mutex) |
|  | Unlock a mutex. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mutex.h](mutex_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
