---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/riscv_2structs_8h_source.html
original_path: doxygen/html/riscv_2structs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

structs.h

[Go to the documentation of this file.](riscv_2structs_8h.md)

1/\*

2 \* Copyright (c) BayLibre SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_RISCV\_STRUCTS\_H\_

8#define ZEPHYR\_INCLUDE\_RISCV\_STRUCTS\_H\_

9

10/\* Per CPU architecture specifics \*/

11struct \_cpu\_arch {

12#ifdef CONFIG\_USERSPACE

13 unsigned long user\_exc\_sp;

14 unsigned long user\_exc\_tmp0;

15 unsigned long user\_exc\_tmp1;

16#endif

17#if defined(CONFIG\_SMP) || (CONFIG\_MP\_MAX\_NUM\_CPUS > 1)

18 unsigned long hartid;

19 bool online;

20#endif

21#ifdef CONFIG\_FPU\_SHARING

22 [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) fpu\_owner;

23 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fpu\_state;

24#endif

25};

26

27#endif /\* ZEPHYR\_INCLUDE\_RISCV\_STRUCTS\_H\_ \*/

[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4)

atomic\_ptr\_t atomic\_ptr\_val\_t

**Definition** atomic\_types.h:18

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [structs.h](riscv_2structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
