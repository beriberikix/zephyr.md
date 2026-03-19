---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/wsen__pads__2511020213301_8h_source.html
original_path: doxygen/html/wsen__pads__2511020213301_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wsen\_pads\_2511020213301.h

[Go to the documentation of this file.](wsen__pads__2511020213301_8h.md)

1/\*

2 \* Copyright (c) 2025 Würth Elektronik eiSos GmbH & Co. KG

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_WSEN\_PADS\_2511020213301\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_WSEN\_PADS\_2511020213301\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

21

[ 22](wsen__pads__2511020213301_8h.md#abe93eb98b441283aa3c80cf5435cb3c7)enum [sensor\_attribute\_wsen\_pads\_2511020213301](wsen__pads__2511020213301_8h.md#abe93eb98b441283aa3c80cf5435cb3c7) {

[ 23](wsen__pads__2511020213301_8h.md#abe93eb98b441283aa3c80cf5435cb3c7aa0b318faad21456c3a9c471674b26726) [SENSOR\_ATTR\_WSEN\_PADS\_2511020213301\_REFERENCE\_POINT](wsen__pads__2511020213301_8h.md#abe93eb98b441283aa3c80cf5435cb3c7aa0b318faad21456c3a9c471674b26726) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

24};

25

26#ifdef CONFIG\_WSEN\_PADS\_2511020213301\_PRESSURE\_THRESHOLD

27enum sensor\_trigger\_wsen\_pads\_2511020213301 {

28 SENSOR\_TRIG\_WSEN\_PADS\_2511020213301\_THRESHOLD\_UPPER = [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921),

29 SENSOR\_TRIG\_WSEN\_PADS\_2511020213301\_THRESHOLD\_LOWER,

30};

31#endif /\* CONFIG\_WSEN\_PADS\_2511020213301\_PRESSURE\_THRESHOLD \*/

32

33#ifdef \_\_cplusplus

34}

35#endif

36

37#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_WSEN\_PADS\_2511020213301\_H\_ \*/

[SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)

@ SENSOR\_TRIG\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:284

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_attribute\_wsen\_pads\_2511020213301](wsen__pads__2511020213301_8h.md#abe93eb98b441283aa3c80cf5435cb3c7)

sensor\_attribute\_wsen\_pads\_2511020213301

**Definition** wsen\_pads\_2511020213301.h:22

[SENSOR\_ATTR\_WSEN\_PADS\_2511020213301\_REFERENCE\_POINT](wsen__pads__2511020213301_8h.md#abe93eb98b441283aa3c80cf5435cb3c7aa0b318faad21456c3a9c471674b26726)

@ SENSOR\_ATTR\_WSEN\_PADS\_2511020213301\_REFERENCE\_POINT

**Definition** wsen\_pads\_2511020213301.h:23

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [wsen\_pads\_2511020213301.h](wsen__pads__2511020213301_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
