---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__condvar__apis.html
original_path: doxygen/html/group__condvar__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Condition Variables APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [K\_CONDVAR\_DEFINE](#ga770816651e25f7e7dae992a0b2260c21)(name) |
|  | Statically define and initialize a condition variable. |

| Functions | |
| --- | --- |
| int | [k\_condvar\_init](#gac9b497c56cc4642965afa6c0c6d7ecfc) (struct [k\_condvar](structk__condvar.md) \*condvar) |
|  | Initialize a condition variable. |
| int | [k\_condvar\_signal](#ga0376a8f7dc6e4f1e1eed55940f43015b) (struct [k\_condvar](structk__condvar.md) \*condvar) |
|  | Signals one thread that is pending on the condition variable. |
| int | [k\_condvar\_broadcast](#gad2e46a7b9e1bc934fd1f5cb38dde40d8) (struct [k\_condvar](structk__condvar.md) \*condvar) |
|  | Unblock all threads that are pending on the condition variable. |
| int | [k\_condvar\_wait](#gab2e1d05db4f954755f430ca894e44dbc) (struct [k\_condvar](structk__condvar.md) \*condvar, struct [k\_mutex](structk__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Waits on the condition variable releasing the mutex lock. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga770816651e25f7e7dae992a0b2260c21)K\_CONDVAR\_DEFINE

| #define K\_CONDVAR\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([k\_condvar](structk__condvar.md), name) = \

Z\_CONDVAR\_INITIALIZER(name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[k\_condvar](structk__condvar.md)

**Definition** kernel.h:3029

Statically define and initialize a condition variable.

The condition variable can be accessed outside the module where it is defined using:

extern struct [k\_condvar](structk__condvar.md) <name>;

Parameters
:   | name | Name of the condition variable. |
    | --- | --- |

## Function Documentation

## [◆ ](#gad2e46a7b9e1bc934fd1f5cb38dde40d8)k\_condvar\_broadcast()

| int k\_condvar\_broadcast | ( | struct [k\_condvar](structk__condvar.md) \* | *condvar* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Unblock all threads that are pending on the condition variable.

Parameters
:   | condvar | pointer to a `[k_condvar](structk__condvar.md)` structure |
    | --- | --- |

Returns
:   An integer with number of woken threads on success

## [◆ ](#gac9b497c56cc4642965afa6c0c6d7ecfc)k\_condvar\_init()

| int k\_condvar\_init | ( | struct [k\_condvar](structk__condvar.md) \* | *condvar* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a condition variable.

Parameters
:   | condvar | pointer to a `[k_condvar](structk__condvar.md)` structure |
    | --- | --- |

Return values
:   | 0 | Condition variable created successfully |
    | --- | --- |

## [◆ ](#ga0376a8f7dc6e4f1e1eed55940f43015b)k\_condvar\_signal()

| int k\_condvar\_signal | ( | struct [k\_condvar](structk__condvar.md) \* | *condvar* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Signals one thread that is pending on the condition variable.

Parameters
:   | condvar | pointer to a `[k_condvar](structk__condvar.md)` structure |
    | --- | --- |

Return values
:   | 0 | On success |
    | --- | --- |

## [◆ ](#gab2e1d05db4f954755f430ca894e44dbc)k\_condvar\_wait()

| int k\_condvar\_wait | ( | struct [k\_condvar](structk__condvar.md) \* | *condvar*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mutex](structk__mutex.md) \* | *mutex*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](kernel_8h.md)>`

Waits on the condition variable releasing the mutex lock.

Atomically releases the currently owned mutex, blocks the current thread waiting on the condition variable specified by *condvar*, and finally acquires the mutex again.

The waiting thread unblocks only after another thread calls k\_condvar\_signal, or k\_condvar\_broadcast with the same condition variable.

Parameters
:   | condvar | pointer to a `[k_condvar](structk__condvar.md)` structure |
    | --- | --- |
    | mutex | Address of the mutex. |
    | timeout | Waiting period for the condition variable or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | On success |
    | --- | --- |
    | -EAGAIN | Waiting period timed out. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
