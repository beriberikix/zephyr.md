---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/lwm2m__path_8h_source.html
original_path: doxygen/html/lwm2m__path_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lwm2m\_path.h

[Go to the documentation of this file.](lwm2m__path_8h.md)

1/\*

2 \* Copyright (c) 2020 Endian Technologies AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_NET\_LWM2M\_PATH\_H\_

8#define ZEPHYR\_INCLUDE\_NET\_LWM2M\_PATH\_H\_

9

19

[ 43](group__lwm2m__path__helpers.md#ga0ac92ffa4a22bcd407a19e768a5720bd)#define LWM2M\_PATH(...) \

44 LWM2M\_PATH\_MACRO(\_\_VA\_ARGS\_\_, LWM2M\_PATH4, LWM2M\_PATH3, \

45 LWM2M\_PATH2, LWM2M\_PATH1)(\_\_VA\_ARGS\_\_)

46

47

49/\* Internal helper macros for the LWM2M\_PATH macro \*/

50#define LWM2M\_PATH\_VA\_NUM\_ARGS(...) \

51 LWM2M\_PATH\_VA\_NUM\_ARGS\_IMPL(\_\_VA\_ARGS\_\_, 5, 4, 3, 2, 1)

52#define LWM2M\_PATH\_VA\_NUM\_ARGS\_IMPL(\_1, \_2, \_3, \_4, N, ...) N

53

54#define LWM2M\_PATH1(\_x) #\_x

55#define LWM2M\_PATH2(\_x, \_y) #\_x "/" #\_y

56#define LWM2M\_PATH3(\_x, \_y, \_z) #\_x "/" #\_y "/" #\_z

57#define LWM2M\_PATH4(\_a, \_x, \_y, \_z) #\_a "/" #\_x "/" #\_y "/" #\_z

58

59#define LWM2M\_PATH\_MACRO(\_1, \_2, \_3, \_4, NAME, ...) NAME

61

[ 81](group__lwm2m__path__helpers.md#gac3c46145eae19f8c8608429e5b4e9250)#define LWM2M\_OBJ(...) \

82 GET\_OBJ\_MACRO(\_\_VA\_ARGS\_\_, LWM2M\_OBJ4, LWM2M\_OBJ3, LWM2M\_OBJ2, LWM2M\_OBJ1)(\_\_VA\_ARGS\_\_)

83

85/\* Internal helper macros for the LWM2M\_OBJ macro \*/

86#define GET\_OBJ\_MACRO(\_1, \_2, \_3, \_4, NAME, ...) NAME

87#define LWM2M\_OBJ1(oi) (struct lwm2m\_obj\_path) {.obj\_id = oi, .level = 1}

88#define LWM2M\_OBJ2(oi, oii) (struct lwm2m\_obj\_path) {.obj\_id = oi, .obj\_inst\_id = oii, .level = 2}

89#define LWM2M\_OBJ3(oi, oii, ri) (struct lwm2m\_obj\_path) \

90 {.obj\_id = oi, .obj\_inst\_id = oii, .res\_id = ri, .level = 3}

91#define LWM2M\_OBJ4(oi, oii, ri, rii) (struct lwm2m\_obj\_path) \

92 {.obj\_id = oi, .obj\_inst\_id = oii, .res\_id = ri, .res\_inst\_id = rii, .level = 4}

94

96

97#endif /\* ZEPHYR\_INCLUDE\_NET\_LWM2M\_PATH\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [lwm2m\_path.h](lwm2m__path_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
