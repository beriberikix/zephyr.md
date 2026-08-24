---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/x86_2ia32_2structs_8h_source.html
original_path: doxygen/html/x86_2ia32_2structs_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

structs.h

[Go to the documentation of this file.](x86_2ia32_2structs_8h.md)

1/\*

2 \* Copyright (c) 2025 Intel

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_X86\_STRUCTS\_H\_

7#define ZEPHYR\_INCLUDE\_X86\_STRUCTS\_H\_

8

9#include <[stdint.h](stdint_8h.md)>

10

11struct [k\_thread](structk__thread.md);

12

13/\* Per CPU architecture specifics (empty) \*/

14struct \_cpu\_arch {

15

16#if defined(CONFIG\_FPU\_SHARING)

17 /\*

18 \* A 'sse\_owner' field does not exist in addition to the 'fpu\_owner'

19 \* field since it's not possible to divide the IA-32 non-integer

20 \* registers into 2 distinct blocks owned by differing threads. In

21 \* other words, given that the 'fxnsave/fxrstor' instructions

22 \* save/restore both the X87 FPU and XMM registers, it's not possible

23 \* for a thread to only "own" the XMM registers.

24 \*/

25

26 struct k\_thread \*fpu\_owner;

27#elif defined(\_\_cplusplus)

28 /\* Ensure this struct does not have a size of 0 which is not allowed in C++. \*/

29 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dummy;

30#endif

31};

32

33#endif /\* ZEPHYR\_INCLUDE\_X86\_STRUCTS\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:262

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [structs.h](x86_2ia32_2structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
