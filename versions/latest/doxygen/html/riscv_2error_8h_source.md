---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/riscv_2error_8h_source.html
original_path: doxygen/html/riscv_2error_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h

[Go to the documentation of this file.](riscv_2error_8h.md)

1/\*

2 \* Copyright (c) 2020 BayLibre, SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ERROR\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ERROR\_H\_

16

17#include <[zephyr/arch/riscv/syscall.h](arch_2riscv_2syscall_8h.md)>

18#include <[zephyr/arch/riscv/exception.h](riscv_2exception_8h.md)>

19#include <[stdbool.h](stdbool_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

25#ifdef CONFIG\_USERSPACE

26

[ 27](riscv_2error_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

28 if (k\_is\_user\_context()) { \

29 arch\_syscall\_invoke1(reason\_p, \

30 K\_SYSCALL\_USER\_FAULT); \

31 } else { \

32 compiler\_barrier(); \

33 arch\_syscall\_invoke1(reason\_p, \

34 RV\_ECALL\_RUNTIME\_EXCEPT);\

35 } \

36 CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

37 } while (false)

38#else

39#define ARCH\_EXCEPT(reason\_p) \

40 arch\_syscall\_invoke1(reason\_p, RV\_ECALL\_RUNTIME\_EXCEPT)

41#endif

42

[ 43](riscv_2error_8h.md#a1389d40b6fee2cbe28523075139aad72)\_\_syscall void [user\_fault](riscv_2error_8h.md#a1389d40b6fee2cbe28523075139aad72)(unsigned int reason);

44

45#include <syscalls/error.h>

46

47#ifdef \_\_cplusplus

48}

49#endif

50

51#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RISCV\_ERROR\_H\_ \*/

[syscall.h](arch_2riscv_2syscall_8h.md)

RISCV specific syscall header.

[user\_fault](riscv_2error_8h.md#a1389d40b6fee2cbe28523075139aad72)

void user\_fault(unsigned int reason)

[exception.h](riscv_2exception_8h.md)

RISCV public exception handling.

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [error.h](riscv_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
