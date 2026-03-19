---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/linker-devnull_8h_source.html
original_path: doxygen/html/linker-devnull_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linker-devnull.h

[Go to the documentation of this file.](linker-devnull_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* DESCRIPTION

9 \* Platform independent set of macros for creating a memory segment for

10 \* aggregating data that shall be kept in the elf file but not in the binary.

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEVNULL\_H\_

14#define ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEVNULL\_H\_

15

16#if defined(CONFIG\_LINKER\_DEVNULL\_MEMORY)

17

18#if defined(CONFIG\_XIP)

19#if (!defined(ROM\_ADDR) && !defined(ROM\_BASE)) || !defined(ROM\_SIZE)

20#error "ROM\_SIZE, ROM\_ADDR or ROM\_BASE not defined"

21#endif

22#endif /\* CONFIG\_XIP \*/

23

24#if (!defined(RAM\_ADDR) && !defined(RAM\_BASE)) || !defined(RAM\_SIZE)

25#error "RAM\_SIZE, RAM\_ADDR or RAM\_BASE not defined"

26#endif

27

28#if defined(CONFIG\_XIP) && !defined(ROM\_ADDR)

29#define ROM\_ADDR ROM\_BASE

30#endif

31

32#if !defined(RAM\_ADDR)

33#define RAM\_ADDR RAM\_BASE

34#endif

35

36#define ROM\_END\_ADDR (ROM\_ADDR + ROM\_SIZE)

37#define DEVNULL\_SIZE CONFIG\_LINKER\_DEVNULL\_MEMORY\_SIZE

38#define ROM\_DEVNULL\_END\_ADDR (ROM\_END\_ADDR + DEVNULL\_SIZE)

39#define MAX\_ADDR UINT32\_MAX

40

41/\* Determine where to put the devnull region. It should be adjacent to the ROM

42 \* region. If ROM starts after RAM or the distance between ROM and RAM is big

43 \* enough to fit the devnull region then devnull region is placed just after

44 \* the ROM region. If it cannot be done then the devnull region is placed before

45 \* the ROM region. It is possible that the devnull region cannot be placed

46 \* adjacent to the ROM (e.g. ROM starts at 0 and RAM follows ROM). In that

47 \* case compilation fails and the devnull region is not supported in that

48 \* configuration.

49 \*/

50#if !defined(CONFIG\_XIP)

51

52#if RAM\_ADDR >= DEVNULL\_SIZE

53#define DEVNULL\_ADDR (RAM\_ADDR - DEVNULL\_SIZE)

54#else

55#define DEVNULL\_ADDR (RAM\_ADDR + RAM\_SIZE)

56#endif

57

58#else /\* CONFIG\_XIP \*/

59

60#if ((ROM\_ADDR > RAM\_ADDR) && ((MAX\_ADDR - ROM\_END\_ADDR) >= DEVNULL\_SIZE)) || \

61 ((ROM\_END\_ADDR + DEVNULL\_SIZE) <= RAM\_ADDR)

62#define DEVNULL\_ADDR ROM\_END\_ADDR

63#elif ROM\_ADDR > DEVNULL\_SIZE

64#define DEVNULL\_ADDR (ROM\_ADDR - DEVNULL\_SIZE)

65#else

66#error "Cannot place devnull segment adjacent to ROM region."

67#endif

68

69#endif /\* CONFIG\_XIP \*/

70

71#define DEVNULL\_REGION DEVNULL\_ROM

72

73#endif /\* CONFIG\_LINKER\_DEVNULL\_MEMORY \*/

74

75#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEVNULL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-devnull.h](linker-devnull_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
