---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stack_8h_source.html
original_path: doxygen/html/stack_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stack.h

[Go to the documentation of this file.](stack_8h.md)

1

5

6/\*

7 \* Copyright (c) 2015 Intel Corporation

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEBUG\_STACK\_H\_

13#define ZEPHYR\_INCLUDE\_DEBUG\_STACK\_H\_

14

15#include <[zephyr/logging/log.h](log_8h.md)>

16#include <[zephyr/toolchain.h](toolchain_8h.md)>

17#include <[stdbool.h](stdbool_8h.md)>

18

[ 19](stack_8h.md#afeac222d2c3b1887fcc97221c6a3054d)static inline void [log\_stack\_usage](stack_8h.md#afeac222d2c3b1887fcc97221c6a3054d)(const struct [k\_thread](structk__thread.md) \*thread)

20{

21#if defined(CONFIG\_INIT\_STACKS) && defined(CONFIG\_THREAD\_STACK\_INFO)

22 size\_t unused, size = thread->[stack\_info](structk__thread.md#a8be452e7b016fc901adad8518d7fe518).size;

23

24 [TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5)([TOOLCHAIN\_WARNING\_SHADOW](toolchain_8h.md#ae917ae1adad468956fa5d28a50d10670));

25 [LOG\_MODULE\_DECLARE](group__log__api.md#ga8193b0e10e5ee64b86848bb52be31869)(os, CONFIG\_KERNEL\_LOG\_LEVEL);

26 [TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561)([TOOLCHAIN\_WARNING\_SHADOW](toolchain_8h.md#ae917ae1adad468956fa5d28a50d10670));

27

28 if (k\_thread\_stack\_space\_get(thread, &unused) == 0) {

29 unsigned int pcnt = ((size - unused) \* 100U) / size;

30 const char \*tname;

31

32 tname = [k\_thread\_name\_get](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)(([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647))thread);

33 if (tname == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

34 tname = "unknown";

35 }

36

37 [LOG\_INF](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)("%p (%s):\tunused %zu\tusage %zu / %zu (%u %%)",

38 thread, tname, unused, size - unused, size,

39 pcnt);

40 }

41#else

42 ARG\_UNUSED(thread);

43#endif

44}

45#endif /\* ZEPHYR\_INCLUDE\_DEBUG\_STACK\_H\_ \*/

[LOG\_MODULE\_DECLARE](group__log__api.md#ga8193b0e10e5ee64b86848bb52be31869)

#define LOG\_MODULE\_DECLARE(...)

Macro for declaring a log module (not registering it).

**Definition** log.h:438

[LOG\_INF](group__log__api.md#ga9c338f3170acf38a8532d1181d26704e)

#define LOG\_INF(...)

Writes an INFO level message to the log.

**Definition** log.h:69

[k\_thread\_name\_get](group__thread__apis.md#gadebf45da56dee393164569742459dc0a)

const char \* k\_thread\_name\_get(k\_tid\_t thread)

Get thread name.

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:383

[log.h](log_8h.md)

[log\_stack\_usage](stack_8h.md#afeac222d2c3b1887fcc97221c6a3054d)

static void log\_stack\_usage(const struct k\_thread \*thread)

**Definition** stack.h:19

[stdbool.h](stdbool_8h.md)

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:262

[k\_thread::stack\_info](structk__thread.md#a8be452e7b016fc901adad8518d7fe518)

struct \_thread\_stack\_info stack\_info

Stack Info.

**Definition** thread.h:320

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[TOOLCHAIN\_DISABLE\_WARNING](toolchain_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5)

#define TOOLCHAIN\_DISABLE\_WARNING(warning)

Disable the specified compiler warning for all compilers.

**Definition** toolchain.h:254

[TOOLCHAIN\_ENABLE\_WARNING](toolchain_8h.md#a5365fdbb6323f48ddca9ab4149e9a561)

#define TOOLCHAIN\_ENABLE\_WARNING(warning)

Re-enable the specified compiler warning for all compilers.

**Definition** toolchain.h:264

[TOOLCHAIN\_WARNING\_SHADOW](toolchain_8h.md#ae917ae1adad468956fa5d28a50d10670)

#define TOOLCHAIN\_WARNING\_SHADOW

Toolchain-specific warning for shadow variables.

**Definition** toolchain.h:224

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [stack.h](stack_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
