---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xbr818_8h_source.html
original_path: doxygen/html/xbr818_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xbr818.h

[Go to the documentation of this file.](xbr818_8h.md)

1/\*

2 \* Copyright (c) 2024, MASSDRIVER EI (massdriver.space)

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_XBR818\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_XBR818\_H\_

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 21](xbr818_8h.md#a2f524848967d71fe6c7557355a064bec)enum [sensor\_attribute\_xbr818](xbr818_8h.md#a2f524848967d71fe6c7557355a064bec) {

[ 25](xbr818_8h.md#a2f524848967d71fe6c7557355a064becaa9f1b6389623e1f197b4e9d41ce784ed) [SENSOR\_ATTR\_XBR818\_DELAY\_TIME](xbr818_8h.md#a2f524848967d71fe6c7557355a064becaa9f1b6389623e1f197b4e9d41ce784ed) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 29](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca69b529d03c9898dd1dad0907ea090434) [SENSOR\_ATTR\_XBR818\_LOCK\_TIME](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca69b529d03c9898dd1dad0907ea090434),

[ 33](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca7fdfc87ccda9cbf8c1dc5c5b3b093467) [SENSOR\_ATTR\_XBR818\_NOISE\_FLOOR](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca7fdfc87ccda9cbf8c1dc5c5b3b093467),

[ 37](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca91dd8effcc638ecdf035ef5c051f75ad) [SENSOR\_ATTR\_XBR818\_RF\_POWER](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca91dd8effcc638ecdf035ef5c051f75ad)

38};

39

40#ifdef \_\_cplusplus

41}

42#endif

43

44#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_XBR818\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[sensor\_attribute\_xbr818](xbr818_8h.md#a2f524848967d71fe6c7557355a064bec)

sensor\_attribute\_xbr818

**Definition** xbr818.h:21

[SENSOR\_ATTR\_XBR818\_LOCK\_TIME](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca69b529d03c9898dd1dad0907ea090434)

@ SENSOR\_ATTR\_XBR818\_LOCK\_TIME

How long output stays triggered after no more activity is detected, in seconds.

**Definition** xbr818.h:29

[SENSOR\_ATTR\_XBR818\_NOISE\_FLOOR](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca7fdfc87ccda9cbf8c1dc5c5b3b093467)

@ SENSOR\_ATTR\_XBR818\_NOISE\_FLOOR

Noise floor Threshold for Radar, 16 first LSBs of the integer part.

**Definition** xbr818.h:33

[SENSOR\_ATTR\_XBR818\_RF\_POWER](xbr818_8h.md#a2f524848967d71fe6c7557355a064beca91dd8effcc638ecdf035ef5c051f75ad)

@ SENSOR\_ATTR\_XBR818\_RF\_POWER

RF Power for Radar, 0 to 7, LSB of the integer part.

**Definition** xbr818.h:37

[SENSOR\_ATTR\_XBR818\_DELAY\_TIME](xbr818_8h.md#a2f524848967d71fe6c7557355a064becaa9f1b6389623e1f197b4e9d41ce784ed)

@ SENSOR\_ATTR\_XBR818\_DELAY\_TIME

Time of received activity before output is triggered, in seconds.

**Definition** xbr818.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [xbr818.h](xbr818_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
