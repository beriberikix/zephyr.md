---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree_2mbox_8h_source.html
original_path: doxygen/html/devicetree_2mbox_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mbox.h

[Go to the documentation of this file.](devicetree_2mbox_8h.md)

1

5

6/\*

7 \* Copyright (c) 2022 Carlo Caione <ccaione@baylibre.com>

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_MBOX\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_MBOX\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 52](group__devicetree-mbox.md#gabb96e9b997d99ed54d167d592d623ff7)#define DT\_MBOX\_CTLR\_BY\_NAME(node\_id, name) \

53 DT\_PHANDLE\_BY\_NAME(node\_id, mboxes, name)

54

[ 89](group__devicetree-mbox.md#ga4ea23945e3aacae6a8daacb4c24c88e4)#define DT\_MBOX\_CHANNEL\_BY\_NAME(node\_id, name) \

90 DT\_PHA\_BY\_NAME\_OR(node\_id, mboxes, name, channel, 0)

91

95

96#ifdef \_\_cplusplus

97}

98#endif

99

100#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_MBOX\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [mbox.h](devicetree_2mbox_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
