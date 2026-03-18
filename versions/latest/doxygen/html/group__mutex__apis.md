---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mutex__apis.html
original_path: doxygen/html/group__mutex__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Mutex APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_mutex](structk__mutex.md) |
|  | Mutex Structure. [More...](structk__mutex.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_MUTEX\_DEFINE](#gab6f3d98fabbdc0918bbc9934d61d63f3)(name) |
|  | Statically define and initialize a mutex. |

| Functions | |
| --- | --- |
| int | [k\_mutex\_init](#ga56b64952fb8b78b00268a21c28b41480) (struct [k\_mutex](structk__mutex.md) \*mutex) |
|  | Initialize a mutex. |
| int | [k\_mutex\_lock](#ga850549358645249c285669baa49c33b0) (struct [k\_mutex](structk__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Lock a mutex. |
| int | [k\_mutex\_unlock](#ga360f4c0e7258b0d7030cdb1f452b2c31) (struct [k\_mutex](structk__mutex.md) \*mutex) |
|  | Unlock a mutex. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gab6f3d98fabbdc0918bbc9934d61d63f3)K\_MUTEX\_DEFINE

| #define K\_MUTEX\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_mutex](structk__mutex.md), name) = \

Z\_MUTEX\_INITIALIZER(name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

Statically define and initialize a mutex.

The mutex can be accessed outside the module where it is defined using:

extern struct [k\_mutex](structk__mutex.md) <name>;

Parameters
:   | name | Name of the mutex. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga56b64952fb8b78b00268a21c28b41480)k\_mutex\_init()

| int k\_mutex\_init | ( | struct [k\_mutex](structk__mutex.md) \* | *mutex* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize a mutex.

This routine initializes a mutex object, prior to its first use.

Upon completion, the mutex is available and does not have an owner.

Parameters
:   | mutex | Address of the mutex. |
    | --- | --- |

Return values
:   | 0 | Mutex object created |
    | --- | --- |

## [◆ ](#ga850549358645249c285669baa49c33b0)k\_mutex\_lock()

| int k\_mutex\_lock | ( | struct [k\_mutex](structk__mutex.md) \* | *mutex*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Lock a mutex.

This routine locks *mutex*. If the mutex is locked by another thread, the calling thread waits until the mutex becomes available or until a timeout occurs.

A thread is permitted to lock a mutex it has already locked. The operation completes immediately and the lock count is increased by 1.

Mutexes may not be locked in ISRs.

Parameters
:   | mutex | Address of the mutex. |
    | --- | --- |
    | timeout | Waiting period to lock the mutex, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Mutex locked. |
    | --- | --- |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

## [◆ ](#ga360f4c0e7258b0d7030cdb1f452b2c31)k\_mutex\_unlock()

| int k\_mutex\_unlock | ( | struct [k\_mutex](structk__mutex.md) \* | *mutex* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Unlock a mutex.

This routine unlocks *mutex*. The mutex must already be locked by the calling thread.

The mutex cannot be claimed by another thread until it has been unlocked by the calling thread as many times as it was previously locked by that thread.

Mutexes may not be unlocked in ISRs, as mutexes must only be manipulated in thread context due to ownership and priority inheritance semantics.

Parameters
:   | mutex | Address of the mutex. |
    | --- | --- |

Return values
:   | 0 | Mutex unlocked. |
    | --- | --- |
    | -EPERM | The current thread does not own the mutex |
    | -EINVAL | The mutex is not locked |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
