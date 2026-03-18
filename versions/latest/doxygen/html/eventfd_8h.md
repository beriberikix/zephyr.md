---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/eventfd_8h.html
original_path: doxygen/html/eventfd_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eventfd.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/posix/fcntl.h](include_2zephyr_2posix_2fcntl_8h_source.md)>`

[Go to the source code of this file.](eventfd_8h_source.md)

| Macros | |
| --- | --- |
| #define | [EFD\_IN\_USE](#abcdfb656e756cf2a492aff987df8d5f2)   0x1 \_\_DEPRECATED\_MACRO |
| #define | [EFD\_SEMAPHORE](#aa1cf1f9ea4d84916ad5fdf7105d4ee1f)   0x2 |
| #define | [EFD\_NONBLOCK](#a04677f5ad8d61c569b9c32ec35b05e7a)   [O\_NONBLOCK](include_2zephyr_2posix_2fcntl_8h.md#a39d33ce33804efd4d52606d59071c6d8) |
| #define | [EFD\_FLAGS\_SET](#a0959e68b487308e9dd8586e56f072781)   ([EFD\_SEMAPHORE](#aa1cf1f9ea4d84916ad5fdf7105d4ee1f) | [EFD\_NONBLOCK](#a04677f5ad8d61c569b9c32ec35b05e7a)) \_\_DEPRECATED\_MACRO |

| Typedefs | |
| --- | --- |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [eventfd\_t](#ad6a5579f52209e68c4196c5473677db5) |

| Functions | |
| --- | --- |
| int | [eventfd](#ab06039421a08cedb36946381608fa7f7) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int initval, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Create a file descriptor for event notification. |
| int | [eventfd\_read](#a32e55549cb7aea88db8a14be9ed5d092) (int fd, [eventfd\_t](#ad6a5579f52209e68c4196c5473677db5) \*value) |
|  | Read from an eventfd. |
| int | [eventfd\_write](#a9c7aafe8ee787e3ba362fb6aab3e5542) (int fd, [eventfd\_t](#ad6a5579f52209e68c4196c5473677db5) value) |
|  | Write to an eventfd. |

## Macro Definition Documentation

## [◆ ](#a0959e68b487308e9dd8586e56f072781)EFD\_FLAGS\_SET

| #define EFD\_FLAGS\_SET   ([EFD\_SEMAPHORE](#aa1cf1f9ea4d84916ad5fdf7105d4ee1f) | [EFD\_NONBLOCK](#a04677f5ad8d61c569b9c32ec35b05e7a)) \_\_DEPRECATED\_MACRO |
| --- |

## [◆ ](#abcdfb656e756cf2a492aff987df8d5f2)EFD\_IN\_USE

| #define EFD\_IN\_USE   0x1 \_\_DEPRECATED\_MACRO |
| --- |

## [◆ ](#a04677f5ad8d61c569b9c32ec35b05e7a)EFD\_NONBLOCK

| #define EFD\_NONBLOCK   [O\_NONBLOCK](include_2zephyr_2posix_2fcntl_8h.md#a39d33ce33804efd4d52606d59071c6d8) |
| --- |

## [◆ ](#aa1cf1f9ea4d84916ad5fdf7105d4ee1f)EFD\_SEMAPHORE

| #define EFD\_SEMAPHORE   0x2 |
| --- |

## Typedef Documentation

## [◆ ](#ad6a5579f52209e68c4196c5473677db5)eventfd\_t

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [eventfd\_t](#ad6a5579f52209e68c4196c5473677db5) |
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
|  |  | [eventfd\_t](#ad6a5579f52209e68c4196c5473677db5) \* | *value* ) |

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
|  |  | [eventfd\_t](#ad6a5579f52209e68c4196c5473677db5) | *value* ) |

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
- [eventfd.h](eventfd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
