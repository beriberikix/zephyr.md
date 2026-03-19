---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/blinfo_8h_source.html
original_path: doxygen/html/blinfo_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

blinfo.h

[Go to the documentation of this file.](blinfo_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_RETENTION\_BLINFO\_

13#define ZEPHYR\_INCLUDE\_RETENTION\_BLINFO\_

14

15#include <[stdint.h](stdint_8h.md)>

16#include <stddef.h>

17#include <[zephyr/kernel.h](kernel_8h.md)>

18

19#if defined(CONFIG\_RETENTION\_BOOTLOADER\_INFO\_TYPE\_MCUBOOT)

20#include <bootutil/boot\_status.h>

21#endif

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

35

36#if defined(CONFIG\_RETENTION\_BOOTLOADER\_INFO\_OUTPUT\_FUNCTION) || defined(\_\_DOXYGEN\_\_)

[ 49](group__bootloader__info__interface.md#ga7b172c65244678070c9b6ca6e24cee0f)int [blinfo\_lookup](group__bootloader__info__interface.md#ga7b172c65244678070c9b6ca6e24cee0f)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key, char \*val, int val\_len\_max);

50#endif

51

55

56#ifdef \_\_cplusplus

57}

58#endif

59

60#endif /\* ZEPHYR\_INCLUDE\_RETENTION\_BLINFO\_ \*/

[blinfo\_lookup](group__bootloader__info__interface.md#ga7b172c65244678070c9b6ca6e24cee0f)

int blinfo\_lookup(uint16\_t key, char \*val, int val\_len\_max)

Returns bootinfo information.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [retention](dir_acb4c99582103da541bc87f13e94ee5a.md)
- [blinfo.h](blinfo_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
