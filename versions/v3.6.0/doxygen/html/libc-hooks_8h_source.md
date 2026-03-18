---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/libc-hooks_8h_source.html
original_path: doxygen/html/libc-hooks_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

47/\* Handle deprecated malloc arena size configuration values \*/

48#ifdef CONFIG\_COMMON\_LIBC\_MALLOC

49# if defined(CONFIG\_MINIMAL\_LIBC) && (CONFIG\_MINIMAL\_LIBC\_MALLOC\_ARENA\_SIZE != -2)

50# undef CONFIG\_COMMON\_LIBC\_MALLOC\_ARENA\_SIZE

51# define CONFIG\_COMMON\_LIBC\_MALLOC\_ARENA\_SIZE CONFIG\_MINIMAL\_LIBC\_MALLOC\_ARENA\_SIZE

52# warning Using deprecated setting CONFIG\_MINIMAL\_LIBC\_MALLOC\_ARENA\_SIZE

53# elif defined(CONFIG\_PICOLIBC) && (CONFIG\_PICOLIBC\_HEAP\_SIZE != -2)

54# undef CONFIG\_COMMON\_LIBC\_MALLOC\_ARENA\_SIZE

55# define CONFIG\_COMMON\_LIBC\_MALLOC\_ARENA\_SIZE CONFIG\_PICOLIBC\_HEAP\_SIZE

56# warning Using deprecated setting CONFIG\_PICOLIBC\_HEAP\_SIZE

57# endif

58#endif

59

60#ifdef CONFIG\_USERSPACE

61#ifdef CONFIG\_COMMON\_LIBC\_MALLOC

62

63/\* When using the common malloc implementation with CONFIG\_USERSPACE, the

64 \* heap will be in a separate partition when there's an MPU or MMU

65 \* available.

66 \*/

67#if CONFIG\_COMMON\_LIBC\_MALLOC\_ARENA\_SIZE != 0 && \

68(defined(CONFIG\_MPU) || defined(CONFIG\_MMU))

69#define Z\_MALLOC\_PARTITION\_EXISTS 1

70#endif

71

72#elif defined(CONFIG\_NEWLIB\_LIBC)

73/\* If we are using newlib, the heap arena is in one of two areas:

74 \* - If we have an MPU that requires power of two alignment, the heap bounds

75 \* must be specified in Kconfig via CONFIG\_NEWLIB\_LIBC\_ALIGNED\_HEAP\_SIZE.

76 \* - Otherwise, the heap arena on most arches starts at a suitably

77 \* aligned base addreess after the `\_end` linker symbol, through to the end

78 \* of system RAM.

79 \*/

80#if (!defined(CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT) || \

81 (defined(CONFIG\_MPU\_REQUIRES\_POWER\_OF\_TWO\_ALIGNMENT) && \

82 CONFIG\_NEWLIB\_LIBC\_ALIGNED\_HEAP\_SIZE))

83#define Z\_MALLOC\_PARTITION\_EXISTS 1

84#endif

85

86#endif /\* CONFIG\_NEWLIB\_LIBC \*/

87

88#ifdef Z\_MALLOC\_PARTITION\_EXISTS

89/\* Memory partition containing the libc malloc arena. Configuration controls

90 \* whether this is available, and an arena size may need to be set.

91 \*/

92extern struct [k\_mem\_partition](structk__mem__partition.md) z\_malloc\_partition;

93#endif

94

95#ifdef CONFIG\_NEED\_LIBC\_MEM\_PARTITION

96/\* - All newlib globals will be placed into z\_libc\_partition.

97 \* - Minimal C library globals, if any, will be placed into

98 \* z\_libc\_partition.

99 \* - Stack canary globals will be placed into z\_libc\_partition since

100 \* it is not worth placing in its own partition.

101 \* - Some architectures may place the global pointer to the thread local

102 \* storage in z\_libc\_partition since it is not worth placing in its

103 \* own partition.

104 \*/

105#define Z\_LIBC\_PARTITION\_EXISTS 1

106

107/\* C library globals, except the malloc arena \*/

108extern struct [k\_mem\_partition](structk__mem__partition.md) z\_libc\_partition;

109#endif

110#endif /\* CONFIG\_USERSPACE \*/

111

112#include <syscalls/libc-hooks.h>

113

114/\* C library memory partitions \*/

115#define Z\_LIBC\_DATA K\_APP\_DMEM(z\_libc\_partition)

116

117#ifdef \_\_cplusplus

118}

119#endif

120

121#endif /\* ZEPHYR\_INCLUDE\_SYS\_LIBC\_HOOKS\_H\_ \*/

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
