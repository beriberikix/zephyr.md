---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/devicetree_2can_8h_source.html
original_path: doxygen/html/devicetree_2can_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can.h

[Go to the documentation of this file.](devicetree_2can_8h.md)

1

5

6/\*

7 \* Copyright (c) 2022 Vestas Wind Systems A/S

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_CAN\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_CAN\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 63](group__devicetree-can.md#ga9c56ded2142fbd8a4a7facffd3dd549d)#define DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE(node\_id, max) \

64 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, phys), \

65 MIN(DT\_PROP(DT\_PHANDLE(node\_id, phys), max\_bitrate), max), \

66 MIN(DT\_PROP\_OR(DT\_CHILD(node\_id, can\_transceiver), max\_bitrate, max), max))

67

[ 75](group__devicetree-can.md#gacac28e33d8a749518485c687a563763f)#define DT\_INST\_CAN\_TRANSCEIVER\_MAX\_BITRATE(inst, max) \

76 DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE(DT\_DRV\_INST(inst), max)

77

81

82#ifdef \_\_cplusplus

83}

84#endif

85

86#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_CAN\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [can.h](devicetree_2can_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
