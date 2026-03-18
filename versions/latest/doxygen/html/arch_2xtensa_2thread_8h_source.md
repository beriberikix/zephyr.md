---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2xtensa_2thread_8h_source.html
original_path: doxygen/html/arch_2xtensa_2thread_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

13/\* Xtensa doesn't use these structs, but Zephyr core requires they be

14 \* defined so they can be included in struct \_thread\_base. Dummy

15 \* field exists for sizeof compatibility with C++.

16 \*/

17

18struct \_callee\_saved {

19 char dummy;

20};

21

22typedef struct \_callee\_saved \_callee\_saved\_t;

23

24struct \_thread\_arch {

25 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) last\_cpu;

26#ifdef CONFIG\_USERSPACE

27 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ptables;

28

29 /\* Initial privilege mode stack pointer when doing a system call.

30 \* Un-set for surpervisor threads.

31 \*/

32 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*psp;

33#endif

34};

35

36typedef struct \_thread\_arch \_thread\_arch\_t;

37

38#endif /\* \_ASMLANGUAGE \*/

39

40#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_THREAD\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [thread.h](arch_2xtensa_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
