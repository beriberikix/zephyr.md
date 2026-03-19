---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2xtensa_2thread_8h_source.html
original_path: doxygen/html/arch_2xtensa_2thread_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2xtensa_2thread_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_THREAD\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_THREAD\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#ifndef \_ASMLANGUAGE

12

13#ifdef CONFIG\_XTENSA\_MPU

14#include <[zephyr/arch/xtensa/mpu.h](xtensa_2mpu_8h.md)>

15#endif

16

17/\* Xtensa doesn't use these structs, but Zephyr core requires they be

18 \* defined so they can be included in struct \_thread\_base. Dummy

19 \* field exists for sizeof compatibility with C++.

20 \*/

21

22struct \_callee\_saved {

23 char dummy;

24};

25

26typedef struct \_callee\_saved \_callee\_saved\_t;

27

28struct \_thread\_arch {

29 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) last\_cpu;

30#ifdef CONFIG\_USERSPACE

31

32#ifdef CONFIG\_XTENSA\_MMU

33 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ptables;

34#endif

35

36#ifdef CONFIG\_XTENSA\_MPU

37 /\* Pointer to the memory domain's MPU map. \*/

38 struct xtensa\_mpu\_map \*mpu\_map;

39#endif

40

41 /\* Initial privilege mode stack pointer when doing a system call.

42 \* Un-set for surpervisor threads.

43 \*/

44 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*psp;

45#endif

46};

47

48typedef struct \_thread\_arch \_thread\_arch\_t;

49

50#endif /\* \_ASMLANGUAGE \*/

51

52#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_THREAD\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[mpu.h](xtensa_2mpu_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [thread.h](arch_2xtensa_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
