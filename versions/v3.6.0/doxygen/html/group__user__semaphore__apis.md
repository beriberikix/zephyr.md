---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__user__semaphore__apis.html
original_path: doxygen/html/group__user__semaphore__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

User mode semaphore APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [SYS\_SEM\_DEFINE](#gad7b4e3a8910b78e4beb0ec20524426e1)(\_name, \_initial\_count, \_count\_limit) |
|  | Statically define and initialize a [sys\_sem](structsys__sem.md "sys_sem structure"). |

| Functions | |
| --- | --- |
| int | [sys\_sem\_init](#gae20385545bbf7a9dfd59afa74bf1120a) (struct [sys\_sem](structsys__sem.md) \*sem, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int initial\_count, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int limit) |
|  | Initialize a semaphore. |
| int | [sys\_sem\_give](#gaae32032398db1f693ad3f876863f78b4) (struct [sys\_sem](structsys__sem.md) \*sem) |
|  | Give a semaphore. |
| int | [sys\_sem\_take](#gaf742a29f89a816fa34b8d6d33e221b77) (struct [sys\_sem](structsys__sem.md) \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Take a [sys\_sem](structsys__sem.md "sys_sem structure"). |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [sys\_sem\_count\_get](#ga7b287ca3cc3ab2766d7c1beec1849894) (struct [sys\_sem](structsys__sem.md) \*sem) |
|  | Get [sys\_sem](structsys__sem.md "sys_sem structure")'s value. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gad7b4e3a8910b78e4beb0ec20524426e1)SYS\_SEM\_DEFINE

| #define SYS\_SEM\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_initial\_count*, |
|  |  |  | *\_count\_limit* ) |

`#include <[sem.h](sem_8h.md)>`

**Value:**

struct [sys\_sem](structsys__sem.md) \_name = { \

.futex = { \_initial\_count }, \

.limit = \_count\_limit \

}; \

BUILD\_ASSERT(((\_count\_limit) != 0) && \

((\_initial\_count) <= (\_count\_limit)))

[sys\_sem](structsys__sem.md)

sys\_sem structure

**Definition** sem.h:34

Statically define and initialize a [sys\_sem](structsys__sem.md "sys_sem structure").

The semaphore can be accessed outside the module where it is defined using:

extern struct [sys\_sem](structsys__sem.md) <name>;

Route this to memory domains using [K\_APP\_DMEM()](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6 "Place data in a partition's data section.").

Parameters
:   | \_name | Name of the semaphore. |
    | --- | --- |
    | \_initial\_count | Initial semaphore count. |
    | \_count\_limit | Maximum permitted semaphore count. |

## Function Documentation

## [◆ ](#ga7b287ca3cc3ab2766d7c1beec1849894)sys\_sem\_count\_get()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sys\_sem\_count\_get | ( | struct [sys\_sem](structsys__sem.md) \* | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sem.h](sem_8h.md)>`

Get [sys\_sem](structsys__sem.md "sys_sem structure")'s value.

This routine returns the current value of *sem*.

Parameters
:   | sem | Address of the [sys\_sem](structsys__sem.md "sys_sem structure"). |
    | --- | --- |

Returns
:   Current value of [sys\_sem](structsys__sem.md "sys_sem structure").

## [◆ ](#gaae32032398db1f693ad3f876863f78b4)sys\_sem\_give()

| int sys\_sem\_give | ( | struct [sys\_sem](structsys__sem.md) \* | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sem.h](sem_8h.md)>`

Give a semaphore.

This routine gives *sem*, unless the semaphore is already at its maximum permitted count.

Parameters
:   | sem | Address of the semaphore. |
    | --- | --- |

Return values
:   | 0 | Semaphore given. |
    | --- | --- |
    | -EINVAL | Parameter address not recognized. |
    | -EACCES | Caller does not have enough access. |
    | -EAGAIN | Count reached Maximum permitted count and try again. |

## [◆ ](#gae20385545bbf7a9dfd59afa74bf1120a)sys\_sem\_init()

| int sys\_sem\_init | ( | struct [sys\_sem](structsys__sem.md) \* | *sem*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *initial\_count*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *limit* ) |

`#include <[sem.h](sem_8h.md)>`

Initialize a semaphore.

This routine initializes a semaphore instance, prior to its first use.

Parameters
:   | sem | Address of the semaphore. |
    | --- | --- |
    | initial\_count | Initial semaphore count. |
    | limit | Maximum permitted semaphore count. |

Return values
:   | 0 | Initial success. |
    | --- | --- |
    | -EINVAL | Bad parameters, the value of limit should be located in (0, INT\_MAX] and initial\_count shouldn't be greater than limit. |

## [◆ ](#gaf742a29f89a816fa34b8d6d33e221b77)sys\_sem\_take()

| int sys\_sem\_take | ( | struct [sys\_sem](structsys__sem.md) \* | *sem*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[sem.h](sem_8h.md)>`

Take a [sys\_sem](structsys__sem.md "sys_sem structure").

This routine takes *sem*.

Parameters
:   | sem | Address of the [sys\_sem](structsys__sem.md "sys_sem structure"). |
    | --- | --- |
    | timeout | Waiting period to take the [sys\_sem](structsys__sem.md "sys_sem structure"), or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | [sys\_sem](structsys__sem.md "sys_sem structure") taken. |
    | --- | --- |
    | -EINVAL | Parameter address not recognized. |
    | -ETIMEDOUT | Waiting period timed out. |
    | -EACCES | Caller does not have enough access. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
