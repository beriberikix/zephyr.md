---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/posix_2sys_2eventfd_8h.html
original_path: doxygen/html/posix_2sys_2eventfd_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eventfd.h File Reference

`#include <[zephyr/zvfs/eventfd.h](zvfs_2eventfd_8h_source.md)>`

[Go to the source code of this file.](posix_2sys_2eventfd_8h_source.md)

| Macros | |
| --- | --- |
| #define | [EFD\_SEMAPHORE](#aa1cf1f9ea4d84916ad5fdf7105d4ee1f)   [ZVFS\_EFD\_SEMAPHORE](zvfs_2eventfd_8h.md#acab48945c7bdd3530651feeb169b75f6) |
| #define | [EFD\_NONBLOCK](#a04677f5ad8d61c569b9c32ec35b05e7a)   [ZVFS\_EFD\_NONBLOCK](zvfs_2eventfd_8h.md#a6374eeebdd4ebe2d5580f5be79839c26) |

| Typedefs | |
| --- | --- |
| typedef [zvfs\_eventfd\_t](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad) | [eventfd\_t](#ac8eb3d8ee0d064d293a5433c2c1f6165) |

| Functions | |
| --- | --- |
| int | [eventfd](#ab06039421a08cedb36946381608fa7f7) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int initval, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Create a file descriptor for event notification. |
| int | [eventfd\_read](#a32e55549cb7aea88db8a14be9ed5d092) (int fd, [eventfd\_t](#ac8eb3d8ee0d064d293a5433c2c1f6165) \*value) |
|  | Read from an eventfd. |
| int | [eventfd\_write](#a9c7aafe8ee787e3ba362fb6aab3e5542) (int fd, [eventfd\_t](#ac8eb3d8ee0d064d293a5433c2c1f6165) value) |
|  | Write to an eventfd. |

## Macro Definition Documentation

## [◆ ](#a04677f5ad8d61c569b9c32ec35b05e7a)EFD\_NONBLOCK

| #define EFD\_NONBLOCK   [ZVFS\_EFD\_NONBLOCK](zvfs_2eventfd_8h.md#a6374eeebdd4ebe2d5580f5be79839c26) |
| --- |

## [◆ ](#aa1cf1f9ea4d84916ad5fdf7105d4ee1f)EFD\_SEMAPHORE

| #define EFD\_SEMAPHORE   [ZVFS\_EFD\_SEMAPHORE](zvfs_2eventfd_8h.md#acab48945c7bdd3530651feeb169b75f6) |
| --- |

## Typedef Documentation

## [◆ ](#ac8eb3d8ee0d064d293a5433c2c1f6165)eventfd\_t

| typedef [zvfs\_eventfd\_t](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad) [eventfd\_t](#ac8eb3d8ee0d064d293a5433c2c1f6165) |
| --- |

## Function Documentation

## [◆ ](#ab06039421a08cedb36946381608fa7f7)eventfd()

| int eventfd | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *initval*, |
| --- | --- | --- | --- |
|  |  | int | *flags* ) |

Create a file descriptor for event notification.

The returned file descriptor can be used with POSIX read/write calls or with the eventfd\_read/eventfd\_write functions.

It also supports polling and by including an eventfd in a call to poll, it is possible to signal and wake the polling thread by simply writing to the eventfd.

When using read() and write() on an eventfd, the size must always be at least 8 bytes or the operation will fail with EINVAL.

Returns
:   New eventfd file descriptor on success, -1 on error

## [◆ ](#a32e55549cb7aea88db8a14be9ed5d092)eventfd\_read()

| int eventfd\_read | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [eventfd\_t](#ac8eb3d8ee0d064d293a5433c2c1f6165) \* | *value* ) |

Read from an eventfd.

If call is successful, the value parameter will have the value 1

Parameters
:   | fd | File descriptor |
    | --- | --- |
    | value | Pointer for storing the read value |

Returns
:   0 on success, -1 on error

## [◆ ](#a9c7aafe8ee787e3ba362fb6aab3e5542)eventfd\_write()

| int eventfd\_write | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [eventfd\_t](#ac8eb3d8ee0d064d293a5433c2c1f6165) | *value* ) |

Write to an eventfd.

Parameters
:   | fd | File descriptor |
    | --- | --- |
    | value | Value to write |

Returns
:   0 on success, -1 on error

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [eventfd.h](posix_2sys_2eventfd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
