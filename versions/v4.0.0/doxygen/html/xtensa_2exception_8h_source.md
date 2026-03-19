---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/xtensa_2exception_8h_source.html
original_path: doxygen/html/xtensa_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

28struct [arch\_esf](structarch__esf.md) {

[ 29](structarch__esf.md#a8b96563526cec43c5b37bdacd3e3e065) int [dummy](structarch__esf.md#ae44a189aed30d7bd9cbb860f7c177d4d);

30};

31

32#endif

33

34#ifdef \_\_cplusplus

35}

36#endif

37

38

39#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_EXCEPTION\_H\_ \*/

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::dummy](structarch__esf.md#ae44a189aed30d7bd9cbb860f7c177d4d)

uint32\_t dummy

**Definition** exception.h:19

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [exception.h](xtensa_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
