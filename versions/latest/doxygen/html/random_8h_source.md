---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/random_8h_source.html
original_path: doxygen/html/random_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

random.h

[Go to the documentation of this file.](random_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \* Copyright (c) 2023 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

20

21#ifndef ZEPHYR\_INCLUDE\_RANDOM\_RANDOM\_H\_

22#define ZEPHYR\_INCLUDE\_RANDOM\_RANDOM\_H\_

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <stddef.h>

26#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

27

34

35#ifdef \_\_cplusplus

36extern "C" {

37#endif

38

[ 48](group__random__api.md#ga9adb8fe5d17088418788877e568cdbd2)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_rand32\_get](group__random__api.md#ga9adb8fe5d17088418788877e568cdbd2)(void);

49

[ 61](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)\_\_syscall void [sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)(void \*dst, size\_t len);

62

[ 76](group__random__api.md#ga98f123f216b5df6e27eb980d6e5dec86)\_\_syscall int [sys\_csrand\_get](group__random__api.md#ga98f123f216b5df6e27eb980d6e5dec86)(void \*dst, size\_t len);

77

78#ifdef \_\_cplusplus

79}

80#endif

81

85

86#include <syscalls/random.h>

87#endif /\* ZEPHYR\_INCLUDE\_RANDOM\_RANDOM\_H\_ \*/

[sys\_csrand\_get](group__random__api.md#ga98f123f216b5df6e27eb980d6e5dec86)

int sys\_csrand\_get(void \*dst, size\_t len)

Fill the destination buffer with cryptographically secure random data values.

[sys\_rand32\_get](group__random__api.md#ga9adb8fe5d17088418788877e568cdbd2)

uint32\_t sys\_rand32\_get(void)

Return a 32-bit random value that should pass general randomness tests.

[sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)

void sys\_rand\_get(void \*dst, size\_t len)

Fill the destination buffer with random data values that should pass general randomness tests.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [random](dir_0a0921beff714d16ead0b6fce37bcefe.md)
- [random.h](random_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
