---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zvfs_2eventfd_8h_source.html
original_path: doxygen/html/zvfs_2eventfd_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eventfd.h

[Go to the documentation of this file.](zvfs_2eventfd_8h.md)

1/\*

2 \* Copyright (c) 2020 Tobias Svehagen

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_ZVFS\_EVENTFD\_H\_

8#define ZEPHYR\_INCLUDE\_ZEPHYR\_ZVFS\_EVENTFD\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](zvfs_2eventfd_8h.md#acab48945c7bdd3530651feeb169b75f6)#define ZVFS\_EFD\_SEMAPHORE 2

[ 19](zvfs_2eventfd_8h.md#a6374eeebdd4ebe2d5580f5be79839c26)#define ZVFS\_EFD\_NONBLOCK 0x4000

20

[ 21](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [zvfs\_eventfd\_t](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad);

22

[ 38](zvfs_2eventfd_8h.md#af970bc2d7c58286477ae098ce03843ca)int [zvfs\_eventfd](zvfs_2eventfd_8h.md#af970bc2d7c58286477ae098ce03843ca)(unsigned int initval, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

39

[ 50](zvfs_2eventfd_8h.md#a350f18c251bf9e925d3632a6ae8fa1f3)int [zvfs\_eventfd\_read](zvfs_2eventfd_8h.md#a350f18c251bf9e925d3632a6ae8fa1f3)(int fd, [zvfs\_eventfd\_t](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad) \*value);

51

[ 60](zvfs_2eventfd_8h.md#a75c589c08e741558dc4086d84713e031)int [zvfs\_eventfd\_write](zvfs_2eventfd_8h.md#a75c589c08e741558dc4086d84713e031)(int fd, [zvfs\_eventfd\_t](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad) value);

61

62#ifdef \_\_cplusplus

63}

64#endif

65

66#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_ZVFS\_EVENTFD\_H\_ \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdint.h](stdint_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[zvfs\_eventfd\_t](zvfs_2eventfd_8h.md#a2f8a313f0a8175844c91c78d5b9340ad)

uint64\_t zvfs\_eventfd\_t

**Definition** eventfd.h:21

[zvfs\_eventfd\_read](zvfs_2eventfd_8h.md#a350f18c251bf9e925d3632a6ae8fa1f3)

int zvfs\_eventfd\_read(int fd, zvfs\_eventfd\_t \*value)

Read from a ZVFS eventfd.

[zvfs\_eventfd\_write](zvfs_2eventfd_8h.md#a75c589c08e741558dc4086d84713e031)

int zvfs\_eventfd\_write(int fd, zvfs\_eventfd\_t value)

Write to a ZVFS eventfd.

[zvfs\_eventfd](zvfs_2eventfd_8h.md#af970bc2d7c58286477ae098ce03843ca)

int zvfs\_eventfd(unsigned int initval, int flags)

Create a file descriptor for ZVFS event notification.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [zvfs](dir_a6e4a0e6a33fa53cdc30153b7c96e222.md)
- [eventfd.h](zvfs_2eventfd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
