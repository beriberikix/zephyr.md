---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2arm64_2mm_8h_source.html
original_path: doxygen/html/arch_2arm64_2mm_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm.h

[Go to the documentation of this file.](arch_2arm64_2mm_8h.md)

1/\*

2 \* Copyright (c) 2021 Arm Limited (or its affiliates). All rights reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_MM\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_MM\_H\_

8

9#if defined(CONFIG\_ARM\_MMU)

10#include <[zephyr/arch/arm64/arm\_mmu.h](4_2arm__mmu_8h.md)>

11/\*

12 \* When mmu enabled, some section addresses need to be aligned with

13 \* page size which is CONFIG\_MMU\_PAGE\_SIZE

14 \*/

15#define MEM\_DOMAIN\_ALIGN\_AND\_SIZE CONFIG\_MMU\_PAGE\_SIZE

16#elif defined(CONFIG\_ARM\_MPU)

17#include <[zephyr/arch/arm64/cortex\_r/arm\_mpu.h](4_2cortex__r_2arm__mpu_8h.md)>

18/\*

19 \* When mpu enabled, some section addresses need to be aligned with

20 \* mpu region min align size which is

21 \* CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE

22 \*/

23#define MEM\_DOMAIN\_ALIGN\_AND\_SIZE CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE

24#endif

25

26#ifndef \_ASMLANGUAGE

27

28struct [k\_thread](structk__thread.md);

29void z\_arm64\_thread\_mem\_domains\_init(struct [k\_thread](structk__thread.md) \*thread);

30void z\_arm64\_swap\_mem\_domains(struct [k\_thread](structk__thread.md) \*thread);

31

32#endif /\* \_ASMLANGUAGE \*/

33

34#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_MM\_H\_ \*/

[arm\_mmu.h](4_2arm__mmu_8h.md)

[arm\_mpu.h](4_2cortex__r_2arm__mpu_8h.md)

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [mm.h](arch_2arm64_2mm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
