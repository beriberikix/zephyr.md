---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mem__manage_8h_source.html
original_path: doxygen/html/mem__manage_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_manage.h

[Go to the documentation of this file.](mem__manage_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_MEM\_MANAGE\_H

8#define ZEPHYR\_INCLUDE\_SYS\_MEM\_MANAGE\_H

9

16

17#ifndef \_ASMLANGUAGE

18#include <[stdbool.h](stdbool_8h.md)>

19#include <[stdint.h](stdint_8h.md)>

20

[ 38](group__memory__management.md#gaef71defc60c1d898d5ece56c6826a2e1)bool [sys\_mm\_is\_phys\_addr\_in\_range](group__memory__management.md#gaef71defc60c1d898d5ece56c6826a2e1)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys);

39

[ 57](group__memory__management.md#ga1a4b707eae142c8f871a198b865e3d16)bool [sys\_mm\_is\_virt\_addr\_in\_range](group__memory__management.md#ga1a4b707eae142c8f871a198b865e3d16)(void \*virt);

58

60

61#endif /\* !\_ASMLANGUAGE \*/

62#endif /\* ZEPHYR\_INCLUDE\_SYS\_MEM\_MANAGE\_H \*/

[sys\_mm\_is\_virt\_addr\_in\_range](group__memory__management.md#ga1a4b707eae142c8f871a198b865e3d16)

bool sys\_mm\_is\_virt\_addr\_in\_range(void \*virt)

Check if a virtual address is within range of virtual memory.

[sys\_mm\_is\_phys\_addr\_in\_range](group__memory__management.md#gaef71defc60c1d898d5ece56c6826a2e1)

bool sys\_mm\_is\_phys\_addr\_in\_range(uintptr\_t phys)

Check if a physical address is within range of physical memory.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mem\_manage.h](mem__manage_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
