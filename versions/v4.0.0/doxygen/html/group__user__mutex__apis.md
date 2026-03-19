---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__user__mutex__apis.html
original_path: doxygen/html/group__user__mutex__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

User mode mutex APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [SYS\_MUTEX\_DEFINE](#ga486bd6a11d0b0d312cdf8a6a8f66c1a3)(name) |
|  | Statically define and initialize a [sys\_mutex](structsys__mutex.md). |

| Functions | |
| --- | --- |
| static void | [sys\_mutex\_init](#ga5456b75934cb26abc974a45ae82d717b) (struct [sys\_mutex](structsys__mutex.md) \*mutex) |
|  | Initialize a mutex. |
| static int | [sys\_mutex\_lock](#ga6887005f8223d4f36de5ae5c02ba4b17) (struct [sys\_mutex](structsys__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Lock a mutex. |
| static int | [sys\_mutex\_unlock](#ga7d4babcd161600dab5f1842c58be2a1f) (struct [sys\_mutex](structsys__mutex.md) \*mutex) |
|  | Unlock a mutex. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga486bd6a11d0b0d312cdf8a6a8f66c1a3)SYS\_MUTEX\_DEFINE

| #define SYS\_MUTEX\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mutex.h](mutex_8h.md)>`

**Value:**

struct [sys\_mutex](structsys__mutex.md) name

[sys\_mutex](structsys__mutex.md)

**Definition** mutex.h:28

Statically define and initialize a [sys\_mutex](structsys__mutex.md).

The mutex can be accessed outside the module where it is defined using:

extern struct [sys\_mutex](structsys__mutex.md) <name>;

Route this to memory domains using [K\_APP\_DMEM()](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6 "Place data in a partition's data section.").

Parameters
:   | name | Name of the mutex. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga5456b75934cb26abc974a45ae82d717b)sys\_mutex\_init()

| | void sys\_mutex\_init | ( | struct [sys\_mutex](structsys__mutex.md) \* | *mutex* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mutex.h](mutex_8h.md)>`

Initialize a mutex.

This routine initializes a mutex object, prior to its first use.

Upon completion, the mutex is available and does not have an owner.

This routine is only necessary to call when userspace is disabled and the mutex was not created with [SYS\_MUTEX\_DEFINE()](#ga486bd6a11d0b0d312cdf8a6a8f66c1a3).

Parameters
:   | mutex | Address of the mutex. |
    | --- | --- |

## [◆ ](#ga6887005f8223d4f36de5ae5c02ba4b17)sys\_mutex\_lock()

| | int sys\_mutex\_lock | ( | struct [sys\_mutex](structsys__mutex.md) \* | *mutex*, | | --- | --- | --- | --- | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mutex.h](mutex_8h.md)>`

Lock a mutex.

This routine locks *mutex*. If the mutex is locked by another thread, the calling thread waits until the mutex becomes available or until a timeout occurs.

A thread is permitted to lock a mutex it has already locked. The operation completes immediately and the lock count is increased by 1.

Parameters
:   | mutex | Address of the mutex, which may reside in user memory |
    | --- | --- |
    | timeout | Waiting period to lock the mutex, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Mutex locked. |
    | --- | --- |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |
    | -EACCES | Caller has no access to provided mutex address |
    | -EINVAL | Provided mutex not recognized by the kernel |

## [◆ ](#ga7d4babcd161600dab5f1842c58be2a1f)sys\_mutex\_unlock()

| | int sys\_mutex\_unlock | ( | struct [sys\_mutex](structsys__mutex.md) \* | *mutex* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mutex.h](mutex_8h.md)>`

Unlock a mutex.

This routine unlocks *mutex*. The mutex must already be locked by the calling thread.

The mutex cannot be claimed by another thread until it has been unlocked by the calling thread as many times as it was previously locked by that thread.

Parameters
:   | mutex | Address of the mutex, which may reside in user memory |
    | --- | --- |

Return values
:   | 0 | Mutex unlocked |
    | --- | --- |
    | -EACCES | Caller has no access to provided mutex address |
    | -EINVAL | Provided mutex not recognized by the kernel or mutex wasn't locked |
    | -EPERM | Caller does not own the mutex |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
