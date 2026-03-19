---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/printk-hooks_8h_source.html
original_path: doxygen/html/printk-hooks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

printk-hooks.h

[Go to the documentation of this file.](printk-hooks_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_PRINTK\_HOOKS\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_PRINTK\_HOOKS\_H\_

9

[ 17](printk-hooks_8h.md#a17d0c01ee515cc6f962dbd56a4c9b36f)typedef int (\*[printk\_hook\_fn\_t](printk-hooks_8h.md#a17d0c01ee515cc6f962dbd56a4c9b36f))(int c);

18

26void \_\_printk\_hook\_install([printk\_hook\_fn\_t](printk-hooks_8h.md#a17d0c01ee515cc6f962dbd56a4c9b36f) fn);

27

36[printk\_hook\_fn\_t](printk-hooks_8h.md#a17d0c01ee515cc6f962dbd56a4c9b36f) \_\_printk\_get\_hook(void);

37

38#endif /\* ZEPHYR\_INCLUDE\_SYS\_PRINTK\_HOOKS\_H\_ \*/

[printk\_hook\_fn\_t](printk-hooks_8h.md#a17d0c01ee515cc6f962dbd56a4c9b36f)

int(\* printk\_hook\_fn\_t)(int c)

printk function handler

**Definition** printk-hooks.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [printk-hooks.h](printk-hooks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
