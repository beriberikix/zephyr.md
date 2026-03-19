---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__user__semaphore__apis.html
original_path: doxygen/html/group__user__semaphore__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| #define | [SYS\_SEM\_LOCK\_BREAK](#ga2e5d53d02732b7df60853a00ed240cff)   continue |
|  | Leaves a code block guarded with [SYS\_SEM\_LOCK](#ga43f2c8aae5ff633364e141a0c0340e93) after releasing the lock. |
| #define | [SYS\_SEM\_LOCK](#ga43f2c8aae5ff633364e141a0c0340e93)(sem) |
|  | Guards a code block with the given [sys\_sem](structsys__sem.md "sys_sem structure"), automatically acquiring the semaphore before executing the code block. |

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

**Definition** sem.h:35

Statically define and initialize a [sys\_sem](structsys__sem.md "sys_sem structure").

The semaphore can be accessed outside the module where it is defined using:

extern struct [sys\_sem](structsys__sem.md) <name>;

Route this to memory domains using [K\_APP\_DMEM()](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6 "Place data in a partition's data section.").

Parameters
:   | \_name | Name of the semaphore. |
    | --- | --- |
    | \_initial\_count | Initial semaphore count. |
    | \_count\_limit | Maximum permitted semaphore count. |

## [◆ ](#ga43f2c8aae5ff633364e141a0c0340e93)SYS\_SEM\_LOCK

| #define SYS\_SEM\_LOCK | ( |  | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sem.h](sem_8h.md)>`

**Value:**

for (int \_\_rc SYS\_SEM\_LOCK\_ONEXIT = [sys\_sem\_take](#gaf742a29f89a816fa34b8d6d33e221b77)((sem), [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)); ({ \

\_\_ASSERT(\_\_rc >= 0, "Failed to take sem: %d", \_\_rc); \

\_\_rc == 0; \

}); \

({ \

\_\_rc = [sys\_sem\_give](#gaae32032398db1f693ad3f876863f78b4)((sem)); \

\_\_ASSERT(\_\_rc == 0, "Failed to give sem: %d", \_\_rc); \

}), \

\_\_rc = 1)

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1440

[sys\_sem\_give](#gaae32032398db1f693ad3f876863f78b4)

int sys\_sem\_give(struct sys\_sem \*sem)

Give a semaphore.

[sys\_sem\_take](#gaf742a29f89a816fa34b8d6d33e221b77)

int sys\_sem\_take(struct sys\_sem \*sem, k\_timeout\_t timeout)

Take a sys\_sem.

Guards a code block with the given [sys\_sem](structsys__sem.md "sys_sem structure"), automatically acquiring the semaphore before executing the code block.

The semaphore will be released either when reaching the end of the code block or when leaving the block with [SYS\_SEM\_LOCK\_BREAK](#ga2e5d53d02732b7df60853a00ed240cff).

Example usage:

[SYS\_SEM\_LOCK](#ga43f2c8aae5ff633364e141a0c0340e93)(&sem) {

...execute statements with the semaphore held...

if (some\_condition) {

...release the lock and leave the guarded section prematurely:

[SYS\_SEM\_LOCK\_BREAK](#ga2e5d53d02732b7df60853a00ed240cff);

}

...execute statements with the lock held...

}

[SYS\_SEM\_LOCK\_BREAK](#ga2e5d53d02732b7df60853a00ed240cff)

#define SYS\_SEM\_LOCK\_BREAK

Leaves a code block guarded with SYS\_SEM\_LOCK after releasing the lock.

**Definition** sem.h:167

[SYS\_SEM\_LOCK](#ga43f2c8aae5ff633364e141a0c0340e93)

#define SYS\_SEM\_LOCK(sem)

Guards a code block with the given sys\_sem, automatically acquiring the semaphore before executing th...

**Definition** sem.h:207

Behind the scenes this pattern expands to a for-loop whose body is executed exactly once:

for ([sys\_sem\_take](#gaf742a29f89a816fa34b8d6d33e221b77)(&sem, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)); ...; [sys\_sem\_give](#gaae32032398db1f693ad3f876863f78b4)(&sem)) {

...

}

Warning
:   The code block must execute to its end or be left by calling [SYS\_SEM\_LOCK\_BREAK](#ga2e5d53d02732b7df60853a00ed240cff). Otherwise, e.g. if exiting the block with a break, goto or return statement, the semaphore will not be released on exit.

Parameters
:   | sem | Semaphore ([sys\_sem](structsys__sem.md "sys_sem")) used to guard the enclosed code block. |
    | --- | --- |

## [◆ ](#ga2e5d53d02732b7df60853a00ed240cff)SYS\_SEM\_LOCK\_BREAK

| #define SYS\_SEM\_LOCK\_BREAK   continue |
| --- |

`#include <[sem.h](sem_8h.md)>`

Leaves a code block guarded with [SYS\_SEM\_LOCK](#ga43f2c8aae5ff633364e141a0c0340e93) after releasing the lock.

See [SYS\_SEM\_LOCK](#ga43f2c8aae5ff633364e141a0c0340e93) for details.

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
