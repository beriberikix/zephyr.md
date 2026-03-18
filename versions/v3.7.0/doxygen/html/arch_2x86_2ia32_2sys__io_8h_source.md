---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arch_2x86_2ia32_2sys__io_8h_source.html
original_path: doxygen/html/arch_2x86_2ia32_2sys__io_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_io.h

[Go to the documentation of this file.](arch_2x86_2ia32_2sys__io_8h.md)

1/\*

2 \* Copyright (c) 2015, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\* Implementation of sys\_io.h's documented functions \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SYS\_IO\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SYS\_IO\_H\_

11

12#if !defined(\_ASMLANGUAGE)

13

14#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16#include <stddef.h>

17

18static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 19](arch_2x86_2ia32_2sys__io_8h.md#ab74f07a31f01e5866d397e91b012abf7) void [sys\_io\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#ab74f07a31f01e5866d397e91b012abf7)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

20{

21 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg = 0;

22

23 \_\_asm\_\_ volatile("inl %w1, %0;\n\t"

24 "btsl %2, %0;\n\t"

25 "outl %0, %w1;\n\t"

26 :

27 : "a" (reg), "Nd" (port), "Ir" (bit));

28}

29

30static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 31](arch_2x86_2ia32_2sys__io_8h.md#a6a6ece8db6858d64378c6cce47a64238) void [sys\_io\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a6a6ece8db6858d64378c6cce47a64238)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

32{

33 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg = 0;

34

35 \_\_asm\_\_ volatile("inl %w1, %0;\n\t"

36 "btrl %2, %0;\n\t"

37 "outl %0, %w1;\n\t"

38 :

39 : "a" (reg), "Nd" (port), "Ir" (bit));

40}

41

42static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 43](arch_2x86_2ia32_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d) int [sys\_io\_test\_bit](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

44{

45 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

46

47 \_\_asm\_\_ volatile("inl %w1, %0\n\t"

48 "btl %2, %0\n\t"

49 : "=a" (ret)

50 : "Nd" (port), "Ir" (bit));

51

52 return (ret & 1U);

53}

54

55static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 56](arch_2x86_2ia32_2sys__io_8h.md#a070e38b330fc6402de5aae6192abd41b) int [sys\_io\_test\_and\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#a070e38b330fc6402de5aae6192abd41b)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

57{

58 int ret;

59

60 ret = [sys\_io\_test\_bit](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d)(port, bit);

61 [sys\_io\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#ab74f07a31f01e5866d397e91b012abf7)(port, bit);

62

63 return ret;

64}

65

66static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 67](arch_2x86_2ia32_2sys__io_8h.md#a41953bee114b3317cd7bcdfbad4738b9) int [sys\_io\_test\_and\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a41953bee114b3317cd7bcdfbad4738b9)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

68{

69 int ret;

70

71 ret = [sys\_io\_test\_bit](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d)(port, bit);

72 [sys\_io\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a6a6ece8db6858d64378c6cce47a64238)(port, bit);

73

74 return ret;

75}

76

77#endif /\* \_ASMLANGUAGE \*/

78

79#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SYS\_IO\_H\_ \*/

[sys\_io\_test\_and\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#a070e38b330fc6402de5aae6192abd41b)

static ALWAYS\_INLINE int sys\_io\_test\_and\_set\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:108

[sys\_io\_test\_bit](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d)

static ALWAYS\_INLINE int sys\_io\_test\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:90

[sys\_io\_test\_and\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a41953bee114b3317cd7bcdfbad4738b9)

static ALWAYS\_INLINE int sys\_io\_test\_and\_clear\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:119

[sys\_io\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a6a6ece8db6858d64378c6cce47a64238)

static ALWAYS\_INLINE void sys\_io\_clear\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:76

[sys\_io\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#ab74f07a31f01e5866d397e91b012abf7)

static ALWAYS\_INLINE void sys\_io\_set\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:62

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[sys\_io.h](sys_2sys__io_8h.md)

[io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86)

uint32\_t io\_port\_t

**Definition** sys\_io.h:19

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [sys\_io.h](arch_2x86_2ia32_2sys__io_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
