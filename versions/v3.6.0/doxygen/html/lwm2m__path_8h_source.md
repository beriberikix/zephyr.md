---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lwm2m__path_8h_source.html
original_path: doxygen/html/lwm2m__path_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

16

[ 40](group__lwm2m__path__helpers.md#ga0ac92ffa4a22bcd407a19e768a5720bd)#define LWM2M\_PATH(...) \

41 LWM2M\_PATH\_MACRO(\_\_VA\_ARGS\_\_, LWM2M\_PATH4, LWM2M\_PATH3, \

42 LWM2M\_PATH2, LWM2M\_PATH1)(\_\_VA\_ARGS\_\_)

43

44

46/\* Internal helper macros for the LWM2M\_PATH macro \*/

47#define LWM2M\_PATH\_VA\_NUM\_ARGS(...) \

48 LWM2M\_PATH\_VA\_NUM\_ARGS\_IMPL(\_\_VA\_ARGS\_\_, 5, 4, 3, 2, 1)

49#define LWM2M\_PATH\_VA\_NUM\_ARGS\_IMPL(\_1, \_2, \_3, \_4, N, ...) N

50

51#define LWM2M\_PATH1(\_x) #\_x

52#define LWM2M\_PATH2(\_x, \_y) #\_x "/" #\_y

53#define LWM2M\_PATH3(\_x, \_y, \_z) #\_x "/" #\_y "/" #\_z

54#define LWM2M\_PATH4(\_a, \_x, \_y, \_z) #\_a "/" #\_x "/" #\_y "/" #\_z

55

56#define LWM2M\_PATH\_MACRO(\_1, \_2, \_3, \_4, NAME, ...) NAME

58

[ 78](group__lwm2m__path__helpers.md#gac3c46145eae19f8c8608429e5b4e9250)#define LWM2M\_OBJ(...) \

79 GET\_OBJ\_MACRO(\_\_VA\_ARGS\_\_, LWM2M\_OBJ4, LWM2M\_OBJ3, LWM2M\_OBJ2, LWM2M\_OBJ1)(\_\_VA\_ARGS\_\_)

80

82/\* Internal helper macros for the LWM2M\_OBJ macro \*/

83#define GET\_OBJ\_MACRO(\_1, \_2, \_3, \_4, NAME, ...) NAME

84#define LWM2M\_OBJ1(oi) (struct lwm2m\_obj\_path) {.obj\_id = oi, .level = 1}

85#define LWM2M\_OBJ2(oi, oii) (struct lwm2m\_obj\_path) {.obj\_id = oi, .obj\_inst\_id = oii, .level = 2}

86#define LWM2M\_OBJ3(oi, oii, ri) (struct lwm2m\_obj\_path) \

87 {.obj\_id = oi, .obj\_inst\_id = oii, .res\_id = ri, .level = 3}

88#define LWM2M\_OBJ4(oi, oii, ri, rii) (struct lwm2m\_obj\_path) \

89 {.obj\_id = oi, .obj\_inst\_id = oii, .res\_id = ri, .res\_inst\_id = rii, .level = 4}

91

93

94#endif /\* ZEPHYR\_INCLUDE\_NET\_LWM2M\_PATH\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [lwm2m\_path.h](lwm2m__path_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
