---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2posix_2thread_8h_source.html
original_path: doxygen/html/arch_2posix_2thread_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2posix_2thread_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \* Copyright (c) 2017 Oticon A/S

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

19

20#ifndef ZEPHYR\_INCLUDE\_ARCH\_POSIX\_THREAD\_H\_

21#define ZEPHYR\_INCLUDE\_ARCH\_POSIX\_THREAD\_H\_

22

23#ifndef \_ASMLANGUAGE

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

30struct \_callee\_saved {

31 /\* IRQ status before irq\_lock() and call to z\_swap() \*/

32 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) key;

33

34 /\* Return value of z\_swap() \*/

35 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retval;

36

37 /\* Thread status pointer \*/

38 void \*thread\_status;

39};

40

41

42struct \_thread\_arch {

43 /\* nothing for now \*/

44 int dummy;

45};

46

47typedef struct \_thread\_arch \_thread\_arch\_t;

48

49#ifdef \_\_cplusplus

50}

51#endif

52

53#endif /\* \_ASMLANGUAGE \*/

54

55#endif /\* ZEPHYR\_INCLUDE\_ARCH\_POSIX\_THREAD\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [posix](dir_2eaa0886f2679378503a1f6e740c4205.md)
- [thread.h](arch_2posix_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
