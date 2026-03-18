---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mips_2exception_8h_source.html
original_path: doxygen/html/mips_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](mips_2exception_8h.md)

1/\*

2 \* Copyright (c) 2021 Antony Pavlov <antonynpavlov@gmail.com>

3 \*

4 \* based on include/arch/riscv/exception.h

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_MIPS\_EXPCEPTION\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_MIPS\_EXPCEPTION\_H\_

11

12#ifndef \_ASMLANGUAGE

13#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20struct \_\_esf {

21 unsigned long ra; /\* return address \*/

22 unsigned long gp; /\* global pointer \*/

23

24 unsigned long t0; /\* Caller-saved temporary register \*/

25 unsigned long t1; /\* Caller-saved temporary register \*/

26 unsigned long t2; /\* Caller-saved temporary register \*/

27 unsigned long t3; /\* Caller-saved temporary register \*/

28 unsigned long t4; /\* Caller-saved temporary register \*/

29 unsigned long t5; /\* Caller-saved temporary register \*/

30 unsigned long t6; /\* Caller-saved temporary register \*/

31 unsigned long t7; /\* Caller-saved temporary register \*/

32 unsigned long t8; /\* Caller-saved temporary register \*/

33 unsigned long t9; /\* Caller-saved temporary register \*/

34

35 unsigned long a0; /\* function argument \*/

36 unsigned long a1; /\* function argument \*/

37 unsigned long a2; /\* function argument \*/

38 unsigned long a3; /\* function argument \*/

39

40 unsigned long v0; /\* return value \*/

41 unsigned long v1; /\* return value \*/

42

43 unsigned long at; /\* assembly temporary \*/

44

45 unsigned long epc;

46 unsigned long badvaddr;

47 unsigned long hi;

48 unsigned long lo;

49 unsigned long status;

50 unsigned long cause;

51};

52

53typedef struct \_\_esf z\_arch\_esf\_t;

54

55#ifdef \_\_cplusplus

56}

57#endif

58

59#endif /\* \_ASMLANGUAGE \*/

60

61#endif /\* ZEPHYR\_INCLUDE\_ARCH\_MIPS\_EXPCEPTION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [mips](dir_fc8c8ea71cc5b300c3fa15bb05243853.md)
- [exception.h](mips_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
