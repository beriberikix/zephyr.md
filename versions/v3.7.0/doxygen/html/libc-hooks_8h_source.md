---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/libc-hooks_8h_source.html
original_path: doxygen/html/libc-hooks_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

libc-hooks.h

[Go to the documentation of this file.](libc-hooks_8h.md)

1/\*

2 \* Copyright (c) 2018, Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_LIBC\_HOOKS\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_LIBC\_HOOKS\_H\_

9

10#include <[zephyr/toolchain.h](toolchain_8h.md)>

11#include <[zephyr/app\_memory/app\_memdomain.h](app__memdomain_8h.md)>

12#include <[stdio.h](stdio_8h.md)>

13#include <stddef.h>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19/\*

20 \* Private header for specifying accessory functions to the C library internals

21 \* that need to call into the kernel as system calls

22 \*/

23

24#if defined(CONFIG\_NEWLIB\_LIBC) || defined(CONFIG\_ARCMWDT\_LIBC)

25

26/\* syscall generation ignores preprocessor, ensure this is defined to ensure

27 \* we don't have compile errors

28 \*/

29\_\_syscall int zephyr\_read\_stdin(char \*buf, int nbytes);

30

31\_\_syscall int zephyr\_write\_stdout(const void \*buf, int nbytes);

32

33#else

34/\* Minimal libc and picolibc \*/

35

[ 36](libc-hooks_8h.md#ac5b3b7e59825b80ba65bb6346ee88e3c)\_\_syscall int [zephyr\_fputc](libc-hooks_8h.md#ac5b3b7e59825b80ba65bb6346ee88e3c)(int c, [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \* stream);

37

38#ifdef CONFIG\_MINIMAL\_LIBC

39/\* Minimal libc only \*/

40

41\_\_syscall size\_t zephyr\_fwrite(const void \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) ptr, size\_t size,

42 size\_t nitems, [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream);

43#endif

44

45#endif /\* CONFIG\_NEWLIB\_LIBC \*/

46

47#ifdef CONFIG\_USERSPACE

48#ifdef CONFIG\_COMMON\_LIBC\_MALLOC

49

50/\* When using the common malloc implementation with CONFIG\_USERSPACE, the

51 \* heap will be in a separate partition when there's an MPU or MMU

52 \* available.

53 \*/

54#if CONFIG\_COMMON\_LIBC\_MALLOC\_ARENA\_SIZE != 0 && \

55(defined(CONFIG\_MPU) || defined(CONFIG\_MMU))

56#define Z\_MALLOC\_PARTITION\_EXISTS 1

57#endif

58

59#elif defined(CONFIG\_NEWLIB\_LIBC)

60/\* If we are using newlib, the heap arena is in one of two areas:

61 \* - If we have an MPU that requires power of two alignment, the heap bounds

62 \* must be specified in Kconfig via CONFIG\_NEWLIB\_LIBC\_ALIGNED\_HEAP\_SIZE.

63 \* - Otherwise, the heap arena on most arches starts at a suitably

64 \* aligned base address after the `\_end` linker symbol, through to the end

65 \* of system RAM.

66 \*/

67#if (!defined(CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT) || \

68 (defined(CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT) && \

69 CONFIG\_NEWLIB\_LIBC\_ALIGNED\_HEAP\_SIZE))

70#define Z\_MALLOC\_PARTITION\_EXISTS 1

71#endif

72

73#endif /\* CONFIG\_NEWLIB\_LIBC \*/

74

75#ifdef Z\_MALLOC\_PARTITION\_EXISTS

76/\* Memory partition containing the libc malloc arena. Configuration controls

77 \* whether this is available, and an arena size may need to be set.

78 \*/

79extern struct [k\_mem\_partition](structk__mem__partition.md) z\_malloc\_partition;

80#endif

81

82#ifdef CONFIG\_NEED\_LIBC\_MEM\_PARTITION

83/\* - All newlib globals will be placed into z\_libc\_partition.

84 \* - Minimal C library globals, if any, will be placed into

85 \* z\_libc\_partition.

86 \* - Stack canary globals will be placed into z\_libc\_partition since

87 \* it is not worth placing in its own partition.

88 \* - Some architectures may place the global pointer to the thread local

89 \* storage in z\_libc\_partition since it is not worth placing in its

90 \* own partition.

91 \*/

92#define Z\_LIBC\_PARTITION\_EXISTS 1

93

94/\* C library globals, except the malloc arena \*/

95extern struct [k\_mem\_partition](structk__mem__partition.md) z\_libc\_partition;

96#endif

97#endif /\* CONFIG\_USERSPACE \*/

98

99#include <zephyr/syscalls/libc-hooks.h>

100

101/\* C library memory partitions \*/

102#define Z\_LIBC\_DATA K\_APP\_DMEM(z\_libc\_partition)

103

104#ifdef \_\_cplusplus

105}

106#endif

107

108#endif /\* ZEPHYR\_INCLUDE\_SYS\_LIBC\_HOOKS\_H\_ \*/

[app\_memdomain.h](app__memdomain_8h.md)

[ZRESTRICT](common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[zephyr\_fputc](libc-hooks_8h.md#ac5b3b7e59825b80ba65bb6346ee88e3c)

int zephyr\_fputc(int c, FILE \*stream)

[stdio.h](stdio_8h.md)

[FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7)

int FILE

**Definition** stdio.h:22

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [libc-hooks.h](libc-hooks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
