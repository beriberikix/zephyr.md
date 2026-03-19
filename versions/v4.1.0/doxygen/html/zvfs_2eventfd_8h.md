---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zvfs_2eventfd_8h.html
original_path: doxygen/html/zvfs_2eventfd_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eventfd.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](zvfs_2eventfd_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ZVFS\_EFD\_SEMAPHORE](#acab48945c7bdd3530651feeb169b75f6)   2 |
| #define | [ZVFS\_EFD\_NONBLOCK](#a6374eeebdd4ebe2d5580f5be79839c26)   0x4000 |

| Typedefs | |
| --- | --- |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [zvfs\_eventfd\_t](#a2f8a313f0a8175844c91c78d5b9340ad) |

| Functions | |
| --- | --- |
| int | [zvfs\_eventfd](#af970bc2d7c58286477ae098ce03843ca) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int initval, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Create a file descriptor for ZVFS event notification. |
| int | [zvfs\_eventfd\_read](#a350f18c251bf9e925d3632a6ae8fa1f3) (int fd, [zvfs\_eventfd\_t](#a2f8a313f0a8175844c91c78d5b9340ad) \*value) |
|  | Read from a ZVFS eventfd. |
| int | [zvfs\_eventfd\_write](#a75c589c08e741558dc4086d84713e031) (int fd, [zvfs\_eventfd\_t](#a2f8a313f0a8175844c91c78d5b9340ad) value) |
|  | Write to a ZVFS eventfd. |

## Macro Definition Documentation

## [◆ ](#a6374eeebdd4ebe2d5580f5be79839c26)ZVFS\_EFD\_NONBLOCK

| #define ZVFS\_EFD\_NONBLOCK   0x4000 |
| --- |

## [◆ ](#acab48945c7bdd3530651feeb169b75f6)ZVFS\_EFD\_SEMAPHORE

| #define ZVFS\_EFD\_SEMAPHORE   2 |
| --- |

## Typedef Documentation

## [◆ ](#a2f8a313f0a8175844c91c78d5b9340ad)zvfs\_eventfd\_t

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [zvfs\_eventfd\_t](#a2f8a313f0a8175844c91c78d5b9340ad) |
| --- |

## Function Documentation

## [◆ ](#af970bc2d7c58286477ae098ce03843ca)zvfs\_eventfd()

| int zvfs\_eventfd | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *initval*, |
| --- | --- | --- | --- |
|  |  | int | *flags* ) |

Create a file descriptor for ZVFS event notification.

The returned file descriptor can be used with POSIX read/write calls or with the [zvfs\_eventfd\_read](#a350f18c251bf9e925d3632a6ae8fa1f3) or [zvfs\_eventfd\_write](#a75c589c08e741558dc4086d84713e031) functions.

It also supports polling and by including an eventfd in a call to poll, it is possible to signal and wake the polling thread by simply writing to the eventfd.

When using read() and write() on a ZVFS eventfd, the size must always be at least 8 bytes or the operation will fail with EINVAL.

Returns
:   New ZVFS eventfd file descriptor on success, -1 on error

## [◆ ](#a350f18c251bf9e925d3632a6ae8fa1f3)zvfs\_eventfd\_read()

| int zvfs\_eventfd\_read | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [zvfs\_eventfd\_t](#a2f8a313f0a8175844c91c78d5b9340ad) \* | *value* ) |

Read from a ZVFS eventfd.

If call is successful, the value parameter will have the value 1

Parameters
:   | fd | File descriptor |
    | --- | --- |
    | value | Pointer for storing the read value |

Returns
:   0 on success, -1 on error

## [◆ ](#a75c589c08e741558dc4086d84713e031)zvfs\_eventfd\_write()

| int zvfs\_eventfd\_write | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [zvfs\_eventfd\_t](#a2f8a313f0a8175844c91c78d5b9340ad) | *value* ) |

Write to a ZVFS eventfd.

Parameters
:   | fd | File descriptor |
    | --- | --- |
    | value | Value to write |

Returns
:   0 on success, -1 on error

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [zvfs](dir_a6e4a0e6a33fa53cdc30153b7c96e222.md)
- [eventfd.h](zvfs_2eventfd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
