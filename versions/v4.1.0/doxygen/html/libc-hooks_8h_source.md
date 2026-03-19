---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/libc-hooks_8h_source.html
original_path: doxygen/html/libc-hooks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

41\_\_syscall size\_t zephyr\_fwrite(const void \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) ptr, size\_t size,

42 size\_t nitems, [FILE](stdio_8h.md#ac15bbd02a147d1595cdfb8b2979693d7) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) stream);

43#endif

44

45#endif /\* CONFIG\_NEWLIB\_LIBC \*/

46

47void \_\_stdout\_hook\_install(int (\*hook)(int));

48

49#ifdef CONFIG\_USERSPACE

50#ifdef CONFIG\_COMMON\_LIBC\_MALLOC

51

52/\* When using the common malloc implementation with CONFIG\_USERSPACE, the

53 \* heap will be in a separate partition when there's an MPU or MMU

54 \* available.

55 \*/

56#if CONFIG\_COMMON\_LIBC\_MALLOC\_ARENA\_SIZE != 0 && \

57(defined(CONFIG\_MPU) || defined(CONFIG\_MMU))

58#define Z\_MALLOC\_PARTITION\_EXISTS 1

59#endif

60

61#elif defined(CONFIG\_NEWLIB\_LIBC) && !defined(CONFIG\_NEWLIB\_LIBC\_CUSTOM\_SBRK)

62/\* If we are using newlib, the heap arena is in one of two areas:

63 \* - If we have an MPU that requires power of two alignment, the heap bounds

64 \* must be specified in Kconfig via CONFIG\_NEWLIB\_LIBC\_ALIGNED\_HEAP\_SIZE.

65 \* - Otherwise, the heap arena on most arches starts at a suitably

66 \* aligned base address after the `\_end` linker symbol, through to the end

67 \* of system RAM.

68 \*/

69#if (!defined(CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT) || \

70 (defined(CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT) && \

71 CONFIG\_NEWLIB\_LIBC\_ALIGNED\_HEAP\_SIZE))

72#define Z\_MALLOC\_PARTITION\_EXISTS 1

73#endif

74

75#endif /\* CONFIG\_NEWLIB\_LIBC \*/

76

77#ifdef Z\_MALLOC\_PARTITION\_EXISTS

78/\* Memory partition containing the libc malloc arena. Configuration controls

79 \* whether this is available, and an arena size may need to be set.

80 \*/

81extern struct [k\_mem\_partition](structk__mem__partition.md) z\_malloc\_partition;

82#endif

83

84#ifdef CONFIG\_NEED\_LIBC\_MEM\_PARTITION

85/\* - All newlib globals will be placed into z\_libc\_partition.

86 \* - Minimal C library globals, if any, will be placed into

87 \* z\_libc\_partition.

88 \* - Stack canary globals will be placed into z\_libc\_partition since

89 \* it is not worth placing in its own partition.

90 \* - Some architectures may place the global pointer to the thread local

91 \* storage in z\_libc\_partition since it is not worth placing in its

92 \* own partition.

93 \*/

94#define Z\_LIBC\_PARTITION\_EXISTS 1

95

96/\* C library globals, except the malloc arena \*/

97extern struct [k\_mem\_partition](structk__mem__partition.md) z\_libc\_partition;

98#endif

99#endif /\* CONFIG\_USERSPACE \*/

100

101#include <zephyr/syscalls/libc-hooks.h>

102

103/\* C library memory partitions \*/

104#define Z\_LIBC\_DATA K\_APP\_DMEM(z\_libc\_partition)

105

106#ifdef \_\_cplusplus

107}

108#endif

109

110#endif /\* ZEPHYR\_INCLUDE\_SYS\_LIBC\_HOOKS\_H\_ \*/

[app\_memdomain.h](app__memdomain_8h.md)

[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

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
