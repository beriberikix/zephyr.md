---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sem_8h.html
original_path: doxygen/html/sem_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sem.h File Reference

public [sys\_sem](structsys__sem.md "sys_sem structure") APIs.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](sem_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_sem](structsys__sem.md) |
|  | [sys\_sem](structsys__sem.md "sys_sem structure") structure [More...](structsys__sem.md#details) |

| Macros | |
| --- | --- |
| #define | [SYS\_SEM\_DEFINE](group__user__semaphore__apis.md#gad7b4e3a8910b78e4beb0ec20524426e1)(\_name, \_initial\_count, \_count\_limit) |
|  | Statically define and initialize a [sys\_sem](structsys__sem.md "sys_sem structure"). |

| Functions | |
| --- | --- |
| int | [sys\_sem\_init](group__user__semaphore__apis.md#gae20385545bbf7a9dfd59afa74bf1120a) (struct [sys\_sem](structsys__sem.md) \*sem, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int initial\_count, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int limit) |
|  | Initialize a semaphore. |
| int | [sys\_sem\_give](group__user__semaphore__apis.md#gaae32032398db1f693ad3f876863f78b4) (struct [sys\_sem](structsys__sem.md) \*sem) |
|  | Give a semaphore. |
| int | [sys\_sem\_take](group__user__semaphore__apis.md#gaf742a29f89a816fa34b8d6d33e221b77) (struct [sys\_sem](structsys__sem.md) \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Take a [sys\_sem](structsys__sem.md "sys_sem structure"). |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [sys\_sem\_count\_get](group__user__semaphore__apis.md#ga7b287ca3cc3ab2766d7c1beec1849894) (struct [sys\_sem](structsys__sem.md) \*sem) |
|  | Get [sys\_sem](structsys__sem.md "sys_sem structure")'s value. |

## Detailed Description

public [sys\_sem](structsys__sem.md "sys_sem structure") APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [sem.h](sem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
