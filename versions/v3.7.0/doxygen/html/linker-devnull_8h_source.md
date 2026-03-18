---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/linker-devnull_8h_source.html
original_path: doxygen/html/linker-devnull_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

14

15#if defined(CONFIG\_LINKER\_DEVNULL\_MEMORY)

16

17#if defined(CONFIG\_XIP)

18#if (!defined(ROM\_ADDR) && !defined(ROM\_BASE)) || !defined(ROM\_SIZE)

19#error "ROM\_SIZE, ROM\_ADDR or ROM\_BASE not defined"

20#endif

21#endif /\* CONFIG\_XIP \*/

22

23#if (!defined(RAM\_ADDR) && !defined(RAM\_BASE)) || !defined(RAM\_SIZE)

24#error "RAM\_SIZE, RAM\_ADDR or RAM\_BASE not defined"

25#endif

26

27#if defined(CONFIG\_XIP) && !defined(ROM\_ADDR)

28#define ROM\_ADDR ROM\_BASE

29#endif

30

31#if !defined(RAM\_ADDR)

32#define RAM\_ADDR RAM\_BASE

33#endif

34

35#define ROM\_END\_ADDR (ROM\_ADDR + ROM\_SIZE)

36#define DEVNULL\_SIZE CONFIG\_LINKER\_DEVNULL\_MEMORY\_SIZE

37#define ROM\_DEVNULL\_END\_ADDR (ROM\_END\_ADDR + DEVNULL\_SIZE)

38#define MAX\_ADDR UINT32\_MAX

39

40/\* Determine where to put the devnull region. It should be adjacent to the ROM

41 \* region. If ROM starts after RAM or the distance between ROM and RAM is big

42 \* enough to fit the devnull region then devnull region is placed just after

43 \* the ROM region. If it cannot be done then the devnull region is placed before

44 \* the ROM region. It is possible that the devnull region cannot be placed

45 \* adjacent to the ROM (e.g. ROM starts at 0 and RAM follows ROM). In that

46 \* case compilation fails and the devnull region is not supported in that

47 \* configuration.

48 \*/

49#if !defined(CONFIG\_XIP)

50

51#if RAM\_ADDR >= DEVNULL\_SIZE

52#define DEVNULL\_ADDR (RAM\_ADDR - DEVNULL\_SIZE)

53#else

54#define DEVNULL\_ADDR (RAM\_ADDR + RAM\_SIZE)

55#endif

56

57#else /\* CONFIG\_XIP \*/

58

59#if ((ROM\_ADDR > RAM\_ADDR) && ((MAX\_ADDR - ROM\_END\_ADDR) >= DEVNULL\_SIZE)) || \

60 ((ROM\_END\_ADDR + DEVNULL\_SIZE) <= RAM\_ADDR)

61#define DEVNULL\_ADDR ROM\_END\_ADDR

62#elif ROM\_ADDR > DEVNULL\_SIZE

63#define DEVNULL\_ADDR (ROM\_ADDR - DEVNULL\_SIZE)

64#else

65#error "Cannot place devnull segment adjacent to ROM region."

66#endif

67

68#endif /\* CONFIG\_XIP \*/

69

70#define DEVNULL\_REGION DEVNULL\_ROM

71

72#endif /\* CONFIG\_LINKER\_DEVNULL\_MEMORY \*/

73

74#endif /\* ZEPHYR\_INCLUDE\_LINKER\_LINKER\_DEVNULL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [linker-devnull.h](linker-devnull_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
