---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h_source.html
original_path: doxygen/html/subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h

[Go to the documentation of this file.](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef ZEPHYR\_SUBSYS\_TESTSUITE\_ZTEST\_INCLUDE\_ARCH\_CPU\_H

5#define ZEPHYR\_SUBSYS\_TESTSUITE\_ZTEST\_INCLUDE\_ARCH\_CPU\_H

6

7/\* This file exists as a hack around Zephyr's dependencies \*/

8

9#include <[inttypes.h](inttypes_8h.md)>

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

15/\* Architecture thread structure \*/

16struct \_callee\_saved {

17#ifdef CONFIG\_CPP

18 /\* C++ does not allow empty structs, add an extra 1 byte \*/

19 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) c;

20#endif

21};

22

23typedef struct \_callee\_saved \_callee\_saved\_t;

24

25struct \_thread\_arch {

26#ifdef CONFIG\_CPP

27 /\* C++ does not allow empty structs, add an extra 1 byte \*/

28 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) c;

29#endif

30};

31

32typedef struct \_thread\_arch \_thread\_arch\_t;

33

34/\* Architecture functions \*/

[ 35](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

36{

37 return 0;

38}

39

[ 40](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

41{

42 return 0;

43}

44

[ 45](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

46{

47 return 0;

48}

49

[ 50](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#aa2b2745d8e99b8730b44805f4d3bbf05)static inline void [arch\_irq\_unlock](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#aa2b2745d8e99b8730b44805f4d3bbf05)(unsigned int key)

51{

52 ARG\_UNUSED(key);

53}

54

[ 55](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a1b827afafc622d412962f568b78726dc)static inline bool [arch\_irq\_unlocked](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a1b827afafc622d412962f568b78726dc)(unsigned int key)

56{

57 return 0;

58}

59

60#ifdef \_\_cplusplus

61}

62#endif /\* \_\_cplusplus \*/

63

64#include <[zephyr/sys/arch\_interface.h](arch__interface_8h.md)>

65

66

67#endif /\* ZEPHYR\_SUBSYS\_TESTSUITE\_ZTEST\_INCLUDE\_ARCH\_CPU\_H \*/

[arch\_interface.h](arch__interface_8h.md)

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[inttypes.h](inttypes_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[arch\_irq\_lock](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** cpu.h:45

[arch\_irq\_unlocked](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a1b827afafc622d412962f568b78726dc)

static bool arch\_irq\_unlocked(unsigned int key)

**Definition** cpu.h:55

[arch\_k\_cycle\_get\_32](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#a9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

**Definition** cpu.h:35

[arch\_irq\_unlock](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#aa2b2745d8e99b8730b44805f4d3bbf05)

static void arch\_irq\_unlock(unsigned int key)

**Definition** cpu.h:50

[arch\_k\_cycle\_get\_64](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md#acc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

**Definition** cpu.h:40

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [arch](dir_e42bd8a5ae419d47808ff796159491b8.md)
- [cpu.h](subsys_2testsuite_2ztest_2include_2zephyr_2arch_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
