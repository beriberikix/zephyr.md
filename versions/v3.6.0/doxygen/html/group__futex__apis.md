---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__futex__apis.html
original_path: doxygen/html/group__futex__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FUTEX APIs

[Kernel APIs](group__kernel__apis.md)

| Functions | |
| --- | --- |
| int | [k\_futex\_wait](#ga596bfa265f88567ad9e80fd38cd433d3) (struct [k\_futex](structk__futex.md) \*futex, int expected, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Pend the current thread on a futex. |
| int | [k\_futex\_wake](#ga62de1aeb7c5c273aed20d0e05336d7a0) (struct [k\_futex](structk__futex.md) \*futex, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wake\_all) |
|  | Wake one/all threads pending on a futex. |

## Detailed Description

## Function Documentation

## [◆ ](#ga596bfa265f88567ad9e80fd38cd433d3)k\_futex\_wait()

| int k\_futex\_wait | ( | struct [k\_futex](structk__futex.md) \* | *futex*, |
| --- | --- | --- | --- |
|  |  | int | *expected*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Pend the current thread on a futex.

Tests that the supplied futex contains the expected value, and if so, goes to sleep until some other thread calls [k\_futex\_wake()](#ga62de1aeb7c5c273aed20d0e05336d7a0) on it.

Parameters
:   | futex | Address of the futex. |
    | --- | --- |
    | expected | Expected value of the futex, if it is different the caller will not wait on it. |
    | timeout | Non-negative waiting period on the futex, or one of the special values K\_NO\_WAIT or K\_FOREVER. |

Return values
:   | -EACCES | Caller does not have read access to futex address. |
    | --- | --- |
    | -EAGAIN | If the futex value did not match the expected parameter. |
    | -EINVAL | Futex parameter address not recognized by the kernel. |
    | -ETIMEDOUT | Thread woke up due to timeout and not a futex wakeup. |
    | 0 | if the caller went to sleep and was woken up. The caller should check the futex's value on wakeup to determine if it needs to block again. |

## [◆ ](#ga62de1aeb7c5c273aed20d0e05336d7a0)k\_futex\_wake()

| int k\_futex\_wake | ( | struct [k\_futex](structk__futex.md) \* | *futex*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *wake\_all* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Wake one/all threads pending on a futex.

Wake up the highest priority thread pending on the supplied futex, or wakeup all the threads pending on the supplied futex, and the behavior depends on wake\_all.

Parameters
:   | futex | Futex to wake up pending threads. |
    | --- | --- |
    | wake\_all | If true, wake up all pending threads; If false, wakeup the highest priority thread. |

Return values
:   | -EACCES | Caller does not have access to the futex address. |
    | --- | --- |
    | -EINVAL | Futex parameter address not recognized by the kernel. |
    | Number | of threads that were woken up. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
