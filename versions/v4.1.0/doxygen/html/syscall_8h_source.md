---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/syscall_8h_source.html
original_path: doxygen/html/syscall_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscall.h

[Go to the documentation of this file.](syscall_8h.md)

1/\*

2 \* Copyright (c) 2017, Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_INCLUDE\_SYSCALL\_H\_

9#define ZEPHYR\_INCLUDE\_SYSCALL\_H\_

10

11#include <zephyr/syscall\_list.h>

12#include <[zephyr/arch/syscall.h](arch_2syscall_8h.md)>

13#include <[stdbool.h](stdbool_8h.md)>

14

15#ifndef \_ASMLANGUAGE

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <[zephyr/linker/sections.h](sections_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23/\*

24 \* System Call Declaration macros

25 \*

26 \* These macros are used in public header files to declare system calls.

27 \* They generate inline functions which have different implementations

28 \* depending on the current compilation context:

29 \*

30 \* - Kernel-only code, or CONFIG\_USERSPACE disabled, these inlines will

31 \* directly call the implementation

32 \* - User-only code, these inlines will marshal parameters and elevate

33 \* privileges

34 \* - Mixed or indeterminate code, these inlines will do a runtime check

35 \* to determine what course of action is needed.

36 \*

37 \* All system calls require a verifier function and an implementation

38 \* function. These must follow a naming convention. For a system call

39 \* named k\_foo():

40 \*

41 \* - The handler function will be named z\_vrfy\_k\_foo(). Handler

42 \* functions have the same type signature as the wrapped call,

43 \* verify arguments passed up from userspace, and call the

44 \* implementation function. See documentation for that typedef for

45 \* more information. - The implementation function will be named

46 \* z\_impl\_k\_foo(). This is the actual implementation of the system

47 \* call.

48 \*/

49

86typedef [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) (\*\_k\_syscall\_handler\_t)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg1, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg2,

87 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg3, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg4,

88 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg5, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) arg6,

89 void \*ssf);

90

91/\* True if a syscall function must trap to the kernel, usually a

92 \* compile-time decision.

93 \*/

94static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool z\_syscall\_trap(void)

95{

96 bool ret = false;

97#ifdef CONFIG\_USERSPACE

98#if defined(\_\_ZEPHYR\_SUPERVISOR\_\_)

99 ret = false;

100#elif defined(\_\_ZEPHYR\_USER\_\_)

101 ret = true;

102#else

103 ret = [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)();

104#endif

105#endif

106 return ret;

107}

108

114\_\_pinned\_func

[ 115](syscall_8h.md#acd625881dd1a23de2573fa86d870df20)static inline bool [k\_is\_user\_context](syscall_8h.md#acd625881dd1a23de2573fa86d870df20)(void)

116{

117#ifdef CONFIG\_USERSPACE

118 return [arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)();

119#else

120 return false;

121#endif

122}

123

124#ifdef \_\_cplusplus

125}

126#endif

127

128#endif /\* \_ASMLANGUAGE \*/

129

130#endif

[arch\_is\_user\_context](arch_2arc_2syscall_8h.md#a89ab53a218add419e37f89c1f5fd955f)

static bool arch\_is\_user\_context(void)

**Definition** syscall.h:181

[syscall.h](arch_2syscall_8h.md)

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[stdbool.h](stdbool_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[k\_is\_user\_context](syscall_8h.md#acd625881dd1a23de2573fa86d870df20)

static \_\_pinned\_func bool k\_is\_user\_context(void)

Indicate whether the CPU is currently in user mode.

**Definition** syscall.h:115

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [syscall.h](syscall_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
