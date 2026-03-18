---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__semaphore__apis.html
original_path: doxygen/html/group__semaphore__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Semaphore APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [K\_SEM\_MAX\_LIMIT](#ga689359a77a0cebe737ef644c188f7e57)   UINT\_MAX |
|  | Maximum limit value allowed for a semaphore. |
| #define | [K\_SEM\_DEFINE](#ga018a8aa43e02e704deee7b6341502946)(name, initial\_count, count\_limit) |
|  | Statically define and initialize a semaphore. |

| Functions | |
| --- | --- |
| int | [k\_sem\_init](#gadcd0e6cfba3392fb887222eafe4c1845) (struct k\_sem \*sem, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int initial\_count, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int limit) |
|  | Initialize a semaphore. |
| int | [k\_sem\_take](#gac71e2383c1920dddc45a561cacfef090) (struct k\_sem \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Take a semaphore. |
| void | [k\_sem\_give](#gab9be3cf1988af2cd6afdace52d497c84) (struct k\_sem \*sem) |
|  | Give a semaphore. |
| void | [k\_sem\_reset](#ga1bd12d8d8c1b9c6be9b665d0fefe5562) (struct k\_sem \*sem) |
|  | Resets a semaphore's count to zero. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [k\_sem\_count\_get](#ga58843b581e170a1811fc38eecbfd01f3) (struct k\_sem \*sem) |
|  | Get a semaphore's count. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga018a8aa43e02e704deee7b6341502946)K\_SEM\_DEFINE

| #define K\_SEM\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *initial\_count*, |
|  |  |  | *count\_limit* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(k\_sem, name) = \

Z\_SEM\_INITIALIZER(name, initial\_count, count\_limit); \

BUILD\_ASSERT(((count\_limit) != 0) && \

((initial\_count) <= (count\_limit)) && \

((count\_limit) <= [K\_SEM\_MAX\_LIMIT](#ga689359a77a0cebe737ef644c188f7e57)));

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[K\_SEM\_MAX\_LIMIT](#ga689359a77a0cebe737ef644c188f7e57)

#define K\_SEM\_MAX\_LIMIT

Maximum limit value allowed for a semaphore.

**Definition** kernel.h:3137

Statically define and initialize a semaphore.

The semaphore can be accessed outside the module where it is defined using:

extern struct k\_sem <name>;

Parameters
:   | name | Name of the semaphore. |
    | --- | --- |
    | initial\_count | Initial semaphore count. |
    | count\_limit | Maximum permitted semaphore count. |

## [◆ ](#ga689359a77a0cebe737ef644c188f7e57)K\_SEM\_MAX\_LIMIT

| #define K\_SEM\_MAX\_LIMIT   UINT\_MAX |
| --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Maximum limit value allowed for a semaphore.

This is intended for use when a semaphore does not have an explicit maximum limit, and instead is just used for counting purposes.

## Function Documentation

## [◆ ](#ga58843b581e170a1811fc38eecbfd01f3)k\_sem\_count\_get()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int k\_sem\_count\_get | ( | struct k\_sem \* | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Get a semaphore's count.

This routine returns the current count of *sem*.

Parameters
:   | sem | Address of the semaphore. |
    | --- | --- |

Returns
:   Current semaphore count.

## [◆ ](#gab9be3cf1988af2cd6afdace52d497c84)k\_sem\_give()

| void k\_sem\_give | ( | struct k\_sem \* | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Give a semaphore.

This routine gives *sem*, unless the semaphore is already at its maximum permitted count.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | sem | Address of the semaphore. |
    | --- | --- |

## [◆ ](#gadcd0e6cfba3392fb887222eafe4c1845)k\_sem\_init()

| int k\_sem\_init | ( | struct k\_sem \* | *sem*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *initial\_count*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *limit* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize a semaphore.

This routine initializes a semaphore object, prior to its first use.

Parameters
:   | sem | Address of the semaphore. |
    | --- | --- |
    | initial\_count | Initial semaphore count. |
    | limit | Maximum permitted semaphore count. |

See also
:   [K\_SEM\_MAX\_LIMIT](#ga689359a77a0cebe737ef644c188f7e57)

Return values
:   | 0 | Semaphore created successfully |
    | --- | --- |
    | -EINVAL | Invalid values |

## [◆ ](#ga1bd12d8d8c1b9c6be9b665d0fefe5562)k\_sem\_reset()

| void k\_sem\_reset | ( | struct k\_sem \* | *sem* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Resets a semaphore's count to zero.

This routine sets the count of *sem* to zero. Any outstanding semaphore takes will be aborted with -EAGAIN.

Parameters
:   | sem | Address of the semaphore. |
    | --- | --- |

## [◆ ](#gac71e2383c1920dddc45a561cacfef090)k\_sem\_take()

| int k\_sem\_take | ( | struct k\_sem \* | *sem*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Take a semaphore.

This routine takes *sem*.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | sem | Address of the semaphore. |
    | --- | --- |
    | timeout | Waiting period to take the semaphore, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Semaphore taken. |
    | --- | --- |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out, or the semaphore was reset during the waiting period. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
