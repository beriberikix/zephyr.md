---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fdc2x1x_8h_source.html
original_path: doxygen/html/fdc2x1x_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fdc2x1x.h

[Go to the documentation of this file.](fdc2x1x_8h.md)

1/\*

2 \* Copyright (c) 2020 arithmetics.io

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_FDC2X1X\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_FDC2X1X\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

20

[ 21](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424)enum [sensor\_channel\_fdc2x1x](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424) {

[ 23](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50) [SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH0](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

[ 25](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720) [SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH1](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720),

[ 27](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332) [SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH2](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332),

[ 29](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837) [SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH3](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837),

30

[ 32](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491) [SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH0](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491),

[ 34](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed) [SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH1](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed),

[ 36](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3) [SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH2](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3),

[ 38](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d) [SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH3](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d),

39};

40

41#ifdef \_\_cplusplus

42}

43#endif

44

45#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_FDC2X1X\_ \*/

[sensor\_channel\_fdc2x1x](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424)

sensor\_channel\_fdc2x1x

**Definition** fdc2x1x.h:21

[SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH1](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed)

@ SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH1

CH1 Frequency, in MHz.

**Definition** fdc2x1x.h:34

[SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH0](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491)

@ SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH0

CH0 Frequency, in MHz.

**Definition** fdc2x1x.h:32

[SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH3](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d)

@ SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH3

CH3 Frequency, in MHz.

**Definition** fdc2x1x.h:38

[SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH3](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837)

@ SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH3

CH3 Capacitance, in Picofarad.

**Definition** fdc2x1x.h:29

[SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH2](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332)

@ SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH2

CH2 Capacitance, in Picofarad.

**Definition** fdc2x1x.h:27

[SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH1](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720)

@ SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH1

CH1 Capacitance, in Picofarad.

**Definition** fdc2x1x.h:25

[SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH2](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3)

@ SENSOR\_CHAN\_FDC2X1X\_FREQ\_CH2

CH2 Frequency, in MHz.

**Definition** fdc2x1x.h:36

[SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH0](fdc2x1x_8h.md#a54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50)

@ SENSOR\_CHAN\_FDC2X1X\_CAPACITANCE\_CH0

CH0 Capacitance, in Picofarad.

**Definition** fdc2x1x.h:23

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:208

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [fdc2x1x.h](fdc2x1x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
