---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mhz19b_8h_source.html
original_path: doxygen/html/mhz19b_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mhz19b.h

[Go to the documentation of this file.](mhz19b_8h.md)

1/\*

2 \* Copyright (c) 2021 G-Technologies Sdn. Bhd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MHZ19B\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MHZ19B\_H\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

23

[ 24](mhz19b_8h.md#a8f990e8276817f44f1dc822fe9cb26f3)enum [sensor\_attribute\_mhz19b](mhz19b_8h.md#a8f990e8276817f44f1dc822fe9cb26f3) {

[ 26](mhz19b_8h.md#a8f990e8276817f44f1dc822fe9cb26f3a31b1be7489dc1d15a526c6062dab81fa) [SENSOR\_ATTR\_MHZ19B\_ABC](mhz19b_8h.md#a8f990e8276817f44f1dc822fe9cb26f3a31b1be7489dc1d15a526c6062dab81fa) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

27};

28

29#ifdef \_\_cplusplus

30}

31#endif

32

33#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MHZ19B\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[sensor\_attribute\_mhz19b](mhz19b_8h.md#a8f990e8276817f44f1dc822fe9cb26f3)

sensor\_attribute\_mhz19b

**Definition** mhz19b.h:24

[SENSOR\_ATTR\_MHZ19B\_ABC](mhz19b_8h.md#a8f990e8276817f44f1dc822fe9cb26f3a31b1be7489dc1d15a526c6062dab81fa)

@ SENSOR\_ATTR\_MHZ19B\_ABC

Automatic Baseline Correction Self Calibration Function.

**Definition** mhz19b.h:26

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [mhz19b.h](mhz19b_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
