---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kernel__version_8h_source.html
original_path: doxygen/html/kernel__version_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel\_version.h

[Go to the documentation of this file.](kernel__version_8h.md)

1/\* kernel version support \*/

2

3/\*

4 \* Copyright (c) 2015 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_KERNEL\_VERSION\_H\_

10#define ZEPHYR\_INCLUDE\_KERNEL\_VERSION\_H\_

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 33](group__version__apis.md#ga607e6596eedd6b15e52d707dfd886cb1)#define SYS\_KERNEL\_VER\_MAJOR(ver) (((ver) >> 24) & 0xFF)

[ 34](group__version__apis.md#ga8074ea738e2f8aa7ab5e3e75b411286f)#define SYS\_KERNEL\_VER\_MINOR(ver) (((ver) >> 16) & 0xFF)

[ 35](group__version__apis.md#ga59bdad0b6a5ab7b36b3abdccfc6aec5f)#define SYS\_KERNEL\_VER\_PATCHLEVEL(ver) (((ver) >> 8) & 0xFF)

36

37/\* kernel version routines \*/

38

[ 47](group__version__apis.md#ga7979b71e0ee58ec1951b675a29368374)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_kernel\_version\_get](group__version__apis.md#ga7979b71e0ee58ec1951b675a29368374)(void);

48

52

53#ifdef \_\_cplusplus

54}

55#endif

56

57#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_VERSION\_H\_ \*/

[sys\_kernel\_version\_get](group__version__apis.md#ga7979b71e0ee58ec1951b675a29368374)

uint32\_t sys\_kernel\_version\_get(void)

Return the kernel version of the present build.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel\_version.h](kernel__version_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
