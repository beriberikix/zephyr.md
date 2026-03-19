---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm__mpu__mem__cfg_8h_source.html
original_path: doxygen/html/arm__mpu__mem__cfg_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu\_mem\_cfg.h

[Go to the documentation of this file.](arm__mpu__mem__cfg_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_ARM\_CORTEX\_M\_MPU\_MEM\_CFG\_H\_

7#define \_ARM\_CORTEX\_M\_MPU\_MEM\_CFG\_H\_

8

9#include <[zephyr/arch/arm/mpu/arm\_mpu.h](mpu_2arm__mpu_8h.md)>

10

11#if !defined(CONFIG\_ARMV8\_M\_BASELINE) && !defined(CONFIG\_ARMV8\_M\_MAINLINE)

12

13/\* Flash Region Definitions \*/

14#if CONFIG\_FLASH\_SIZE <= 64

[ 15](arm__mpu__mem__cfg_8h.md#a8f182fd3aea44e059fd05b76f7e40f5c)#define REGION\_FLASH\_SIZE REGION\_64K

16#elif CONFIG\_FLASH\_SIZE <= 128

17#define REGION\_FLASH\_SIZE REGION\_128K

18#elif CONFIG\_FLASH\_SIZE <= 256

19#define REGION\_FLASH\_SIZE REGION\_256K

20#elif CONFIG\_FLASH\_SIZE <= 512

21#define REGION\_FLASH\_SIZE REGION\_512K

22#elif CONFIG\_FLASH\_SIZE <= 1024

23#define REGION\_FLASH\_SIZE REGION\_1M

24#elif CONFIG\_FLASH\_SIZE <= 2048

25#define REGION\_FLASH\_SIZE REGION\_2M

26#elif CONFIG\_FLASH\_SIZE <= 4096

27#define REGION\_FLASH\_SIZE REGION\_4M

28#elif CONFIG\_FLASH\_SIZE <= 8192

29#define REGION\_FLASH\_SIZE REGION\_8M

30#elif CONFIG\_FLASH\_SIZE <= 16384

31#define REGION\_FLASH\_SIZE REGION\_16M

32#elif CONFIG\_FLASH\_SIZE <= 65536

33#define REGION\_FLASH\_SIZE REGION\_64M

34#elif CONFIG\_FLASH\_SIZE <= 131072

35#define REGION\_FLASH\_SIZE REGION\_128M

36#elif CONFIG\_FLASH\_SIZE <= 262144

37#define REGION\_FLASH\_SIZE REGION\_256M

38#elif CONFIG\_FLASH\_SIZE <= 524288

39#define REGION\_FLASH\_SIZE REGION\_512M

40#elif CONFIG\_FLASH\_SIZE <= 1048576

41#define REGION\_FLASH\_SIZE REGION\_1G

42#elif CONFIG\_FLASH\_SIZE <= 2097152

43#define REGION\_FLASH\_SIZE REGION\_2G

44#elif CONFIG\_FLASH\_SIZE <= 4194304

45#define REGION\_FLASH\_SIZE REGION\_4G

46#else

47#error "Unsupported flash size configuration"

48#endif

49

50/\* SRAM Region Definitions \*/

51#if CONFIG\_SRAM\_SIZE <= 16

[ 52](arm__mpu__mem__cfg_8h.md#afceef70334f1d1398cffd94b2c7aae67)#define REGION\_SRAM\_SIZE REGION\_16K

53#elif CONFIG\_SRAM\_SIZE <= 32

54#define REGION\_SRAM\_SIZE REGION\_32K

55#elif CONFIG\_SRAM\_SIZE <= 64

56#define REGION\_SRAM\_SIZE REGION\_64K

57#elif CONFIG\_SRAM\_SIZE <= 128

58#define REGION\_SRAM\_SIZE REGION\_128K

59#elif CONFIG\_SRAM\_SIZE <= 256

60#define REGION\_SRAM\_SIZE REGION\_256K

61#elif CONFIG\_SRAM\_SIZE <= 512

62#define REGION\_SRAM\_SIZE REGION\_512K

63#elif CONFIG\_SRAM\_SIZE <= 1024

64#define REGION\_SRAM\_SIZE REGION\_1M

65#elif CONFIG\_SRAM\_SIZE <= 2048

66#define REGION\_SRAM\_SIZE REGION\_2M

67#elif CONFIG\_SRAM\_SIZE <= 4096

68#define REGION\_SRAM\_SIZE REGION\_4M

69#elif CONFIG\_SRAM\_SIZE <= 8192

70#define REGION\_SRAM\_SIZE REGION\_8M

71#elif CONFIG\_SRAM\_SIZE <= 16384

72#define REGION\_SRAM\_SIZE REGION\_16M

73#elif CONFIG\_SRAM\_SIZE <= 32768

74#define REGION\_SRAM\_SIZE REGION\_32M

75#elif CONFIG\_SRAM\_SIZE <= 65536

76#define REGION\_SRAM\_SIZE REGION\_64M

77#elif CONFIG\_SRAM\_SIZE <= 131072

78#define REGION\_SRAM\_SIZE REGION\_128M

79#elif CONFIG\_SRAM\_SIZE <= 262144

80#define REGION\_SRAM\_SIZE REGION\_256M

81#elif CONFIG\_SRAM\_SIZE <= 524288

82#define REGION\_SRAM\_SIZE REGION\_512M

83#elif CONFIG\_SRAM\_SIZE <= 1048576

84#define REGION\_SRAM\_SIZE REGION\_1G

85#elif CONFIG\_SRAM\_SIZE <= 2097152

86#define REGION\_SRAM\_SIZE REGION\_2G

87#elif CONFIG\_SRAM\_SIZE <= 4194304

88#define REGION\_SRAM\_SIZE REGION\_4G

89#else

90#error "Unsupported sram size configuration"

91#endif

92

93#endif /\* !ARMV8\_M\_BASELINE && !ARMV8\_M\_MAINLINE \*/

94

95#endif /\* \_ARM\_CORTEX\_M\_MPU\_MEM\_CFG\_H\_ \*/

[arm\_mpu.h](mpu_2arm__mpu_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [arm\_mpu\_mem\_cfg.h](arm__mpu__mem__cfg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
