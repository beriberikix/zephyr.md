---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm_2structs_8h_source.html
original_path: doxygen/html/arm_2structs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

structs.h

[Go to the documentation of this file.](arm_2structs_8h.md)

1/\*

2 \* Copyright (c) 2023 Arm Limited (or its affiliates). All rights reserved.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARM\_STRUCTS\_H\_

7#define ZEPHYR\_INCLUDE\_ARM\_STRUCTS\_H\_

8

9#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

10

11#if defined(CONFIG\_CPU\_AARCH32\_CORTEX\_A) || defined(CONFIG\_CPU\_AARCH32\_CORTEX\_R)

12/\* Per CPU architecture specifics \*/

13struct \_cpu\_arch {

14 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) exc\_depth;

15};

16

17#else

18

19/\* Default definitions when no architecture specific definitions exist. \*/

20

21/\* Per CPU architecture specifics (empty) \*/

22struct \_cpu\_arch {

23#ifdef \_\_cplusplus

24 /\* This struct will have a size 0 in C which is not allowed in C++ (it'll have a size 1). To

25 \* prevent this, we add a 1 byte dummy variable.

26 \*/

27 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dummy;

28#endif

29};

30

31#endif

32

33#endif /\* ZEPHYR\_INCLUDE\_ARM\_STRUCTS\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [structs.h](arm_2structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
