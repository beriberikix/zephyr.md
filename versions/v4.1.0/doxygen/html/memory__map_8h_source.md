---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/memory__map_8h_source.html
original_path: doxygen/html/memory__map_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory\_map.h

[Go to the documentation of this file.](memory__map_8h.md)

1/\*

2 \* Copyright (c) 2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_MEMORY\_MAP\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_MEMORY\_MAP\_H\_

17

18#include <[zephyr/sys/util.h](sys_2util_8h.md)>

19

20/\* 0x00000000 -> 0x1fffffff: Code in ROM [0.5 GB] \*/

21#define \_CODE\_BASE\_ADDR 0x00000000

22#define \_CODE\_END\_ADDR 0x1FFFFFFF

23

24/\* 0x20000000 -> 0x3fffffff: SRAM [0.5GB] \*/

25#define \_SRAM\_BASE\_ADDR 0x20000000

26#define \_SRAM\_BIT\_BAND\_REGION 0x20000000

27#define \_SRAM\_BIT\_BAND\_REGION\_END 0x200FFFFF

28#define \_SRAM\_BIT\_BAND\_ALIAS 0x22000000

29#define \_SRAM\_BIT\_BAND\_ALIAS\_END 0x23FFFFFF

30#define \_SRAM\_END\_ADDR 0x3FFFFFFF

31

32/\* 0x40000000 -> 0x5fffffff: Peripherals [0.5GB] \*/

33#define \_PERI\_BASE\_ADDR 0x40000000

34#define \_PERI\_BIT\_BAND\_REGION 0x40000000

35#define \_PERI\_BIT\_BAND\_REGION\_END 0x400FFFFF

36#define \_PERI\_BIT\_BAND\_ALIAS 0x42000000

37#define \_PERI\_BIT\_BAND\_ALIAS\_END 0x43FFFFFF

38#define \_PERI\_END\_ADDR 0x5FFFFFFF

39

40/\* 0x60000000 -> 0x9fffffff: external RAM [1GB] \*/

41#define \_ERAM\_BASE\_ADDR 0x60000000

42#define \_ERAM\_END\_ADDR 0x9FFFFFFF

43

44/\* 0xa0000000 -> 0xdfffffff: external devices [1GB] \*/

45#define \_EDEV\_BASE\_ADDR 0xA0000000

46#define \_EDEV\_END\_ADDR 0xDFFFFFFF

47

48/\* 0xe0000000 -> 0xffffffff: varies by processor (see below) \*/

49

50/\* 0xe0000000 -> 0xe00fffff: private peripheral bus \*/

51/\* 0xe0000000 -> 0xe003ffff: internal [256KB] \*/

52#define \_PPB\_INT\_BASE\_ADDR 0xE0000000

53#if defined(CONFIG\_CPU\_CORTEX\_M0) || defined(CONFIG\_CPU\_CORTEX\_M0PLUS) || \

54 defined(CONFIG\_CPU\_CORTEX\_M1)

55#define \_PPB\_INT\_RSVD\_0 0xE0000000

56#define \_PPB\_INT\_DWT 0xE0001000

57#define \_PPB\_INT\_BPU 0xE0002000

58#define \_PPB\_INT\_RSVD\_1 0xE0003000

59#define \_PPB\_INT\_SCS 0xE000E000

60#define \_PPB\_INT\_RSVD\_2 0xE000F000

61#elif defined(CONFIG\_CPU\_CORTEX\_M3) || defined(CONFIG\_CPU\_CORTEX\_M4) || \

62 defined(CONFIG\_CPU\_CORTEX\_M7)

63#define \_PPB\_INT\_ITM 0xE0000000

64#define \_PPB\_INT\_DWT 0xE0001000

65#define \_PPB\_INT\_FPB 0xE0002000

66#define \_PPB\_INT\_RSVD\_1 0xE0003000

67#define \_PPB\_INT\_SCS 0xE000E000

68#define \_PPB\_INT\_RSVD\_2 0xE000F000

69#elif defined(CONFIG\_CPU\_CORTEX\_M23) || defined(CONFIG\_CPU\_CORTEX\_M33) || \

70 defined(CONFIG\_CPU\_CORTEX\_M55) || defined(CONFIG\_CPU\_CORTEX\_M85)

71#define \_PPB\_INT\_RSVD\_0 0xE0000000

72#define \_PPB\_INT\_SCS 0xE000E000

73#define \_PPB\_INT\_SCB 0xE000ED00

74#define \_PPB\_INT\_RSVD\_1 0xE002E000

75#else

76#error Unknown CPU

77#endif

78#define \_PPB\_INT\_END\_ADDR 0xE003FFFF

79

80/\* 0xe0000000 -> 0xe00fffff: private peripheral bus \*/

81/\* 0xe0040000 -> 0xe00fffff: external [768K] \*/

82#define \_PPB\_EXT\_BASE\_ADDR 0xE0040000

83#if defined(CONFIG\_CPU\_CORTEX\_M0) || defined(CONFIG\_CPU\_CORTEX\_M0PLUS) || \

84 defined(CONFIG\_CPU\_CORTEX\_M1) || defined(CONFIG\_CPU\_CORTEX\_M23)

85#elif defined(CONFIG\_CPU\_CORTEX\_M3) || defined(CONFIG\_CPU\_CORTEX\_M4)

86#define \_PPB\_EXT\_TPIU 0xE0040000

87#define \_PPB\_EXT\_ETM 0xE0041000

88#define \_PPB\_EXT\_PPB 0xE0042000

89#define \_PPB\_EXT\_ROM\_TABLE 0xE00FF000

90#define \_PPB\_EXT\_END\_ADDR 0xE00FFFFF

91#elif defined(CONFIG\_CPU\_CORTEX\_M33) || defined(CONFIG\_CPU\_CORTEX\_M55) || \

92 defined(CONFIG\_CPU\_CORTEX\_M85)

93#undef \_PPB\_EXT\_BASE\_ADDR

94#define \_PPB\_EXT\_BASE\_ADDR 0xE0044000

95#define \_PPB\_EXT\_ROM\_TABLE 0xE00FF000

96#define \_PPB\_EXT\_END\_ADDR 0xE00FFFFF

97#elif defined(CONFIG\_CPU\_CORTEX\_M7)

98#define \_PPB\_EXT\_BASE\_ADDR 0xE0040000

99#define \_PPB\_EXT\_RSVD\_TPIU 0xE0040000

100#define \_PPB\_EXT\_ETM 0xE0041000

101#define \_PPB\_EXT\_CTI 0xE0042000

102#define \_PPB\_EXT\_PPB 0xE0043000

103#define \_PPB\_EXT\_PROC\_ROM\_TABLE 0xE00FE000

104#define \_PPB\_EXT\_PPB\_ROM\_TABLE 0xE00FF000

105#else

106#error Unknown CPU

107#endif

108#define \_PPB\_EXT\_END\_ADDR 0xE00FFFFF

109

110/\* 0xe0100000 -> 0xffffffff: vendor-specific [0.5GB-1MB or 511MB] \*/

111#define \_VENDOR\_BASE\_ADDR 0xE0100000

112#define \_VENDOR\_END\_ADDR 0xFFFFFFFF

113

114#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_M\_MEMORY\_MAP\_H\_ \*/

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [memory\_map.h](memory__map_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
