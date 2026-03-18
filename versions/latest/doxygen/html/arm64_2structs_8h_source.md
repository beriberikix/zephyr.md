---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arm64_2structs_8h_source.html
original_path: doxygen/html/arm64_2structs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

structs.h

[Go to the documentation of this file.](arm64_2structs_8h.md)

1/\*

2 \* Copyright (c) BayLibre SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARM64\_STRUCTS\_H\_

8#define ZEPHYR\_INCLUDE\_ARM64\_STRUCTS\_H\_

9

10/\* Per CPU architecture specifics \*/

11struct \_cpu\_arch {

12#ifdef CONFIG\_FPU\_SHARING

13 [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) fpu\_owner;

14#endif

15#ifdef CONFIG\_ARM64\_SAFE\_EXCEPTION\_STACK

16 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) safe\_exception\_stack;

17 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) current\_stack\_limit;

18 /\* Saved the corrupted stack pointer when stack overflow, else 0 \*/

19 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) corrupted\_sp;

20#endif

21};

22

23#endif /\* ZEPHYR\_INCLUDE\_ARM64\_STRUCTS\_H\_ \*/

[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4)

atomic\_ptr\_t atomic\_ptr\_val\_t

**Definition** atomic\_types.h:18

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [structs.h](arm64_2structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
