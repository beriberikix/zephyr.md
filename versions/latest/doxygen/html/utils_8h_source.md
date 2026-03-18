---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/utils_8h_source.html
original_path: doxygen/html/utils_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

utils.h

[Go to the documentation of this file.](utils_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_LINKER\_UTILS\_H\_

8#define ZEPHYR\_INCLUDE\_LINKER\_UTILS\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11

[ 24](utils_8h.md#a6a48d32446fade9372ab88092d9b4861)static inline bool [linker\_is\_in\_rodata](utils_8h.md#a6a48d32446fade9372ab88092d9b4861)(const void \*addr)

25{

26#if defined(CONFIG\_LINKER\_USE\_PINNED\_SECTION)

27 extern const char lnkr\_pinned\_rodata\_start[];

28 extern const char lnkr\_pinned\_rodata\_end[];

29

30 if (((const char \*)addr >= (const char \*)lnkr\_pinned\_rodata\_start) &&

31 ((const char \*)addr < (const char \*)lnkr\_pinned\_rodata\_end)) {

32 return true;

33 }

34#endif

35

36#if defined(CONFIG\_ARM) || defined(CONFIG\_ARC) || defined(CONFIG\_X86) || \

37 defined(CONFIG\_ARM64) || defined(CONFIG\_NIOS2) || \

38 defined(CONFIG\_RISCV) || defined(CONFIG\_SPARC) || \

39 defined(CONFIG\_MIPS) || defined(CONFIG\_XTENSA)

40 extern char \_\_rodata\_region\_start[];

41 extern char \_\_rodata\_region\_end[];

42 #define RO\_START \_\_rodata\_region\_start

43 #define RO\_END \_\_rodata\_region\_end

44#else

45 #define RO\_START 0

46 #define RO\_END 0

47#endif

48

49 return (((const char \*)addr >= (const char \*)[RO\_START](utils_8h.md#a5927556a88adec513a5d6265c5aa076b)) &&

50 ((const char \*)addr < (const char \*)[RO\_END](utils_8h.md#aac88e44c409fe39f224202ef757c7d25)));

51

52 #undef RO\_START

53 #undef RO\_END

54}

55

56#endif /\* ZEPHYR\_INCLUDE\_LINKER\_UTILS\_H\_ \*/

[stdbool.h](stdbool_8h.md)

[RO\_START](utils_8h.md#a5927556a88adec513a5d6265c5aa076b)

#define RO\_START

[linker\_is\_in\_rodata](utils_8h.md#a6a48d32446fade9372ab88092d9b4861)

static bool linker\_is\_in\_rodata(const void \*addr)

Check if address is in read only section.

**Definition** utils.h:24

[RO\_END](utils_8h.md#aac88e44c409fe39f224202ef757c7d25)

#define RO\_END

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [utils.h](utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
