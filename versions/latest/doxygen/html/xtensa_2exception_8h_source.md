---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/xtensa_2exception_8h_source.html
original_path: doxygen/html/xtensa_2exception_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](xtensa_2exception_8h.md)

1/\*

2 \* Copyright (c) 2014 Wind River Systems, Inc.

3 \* Copyright (c) 2016 Cadence Design Systems, Inc.

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_EXCEPTION\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_EXCEPTION\_H\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22#ifndef \_ASMLANGUAGE

23

24/\* Xtensa uses a variable length stack frame depending on how many

25 \* register windows are in use. This isn't a struct type, it just

26 \* matches the register/stack-unit width.

27 \*/

28typedef int z\_arch\_esf\_t;

29

30#endif

31

32#ifdef \_\_cplusplus

33}

34#endif

35

36

37#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_EXCEPTION\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [exception.h](xtensa_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
