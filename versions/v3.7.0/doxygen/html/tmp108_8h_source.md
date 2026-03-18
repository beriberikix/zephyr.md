---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/tmp108_8h_source.html
original_path: doxygen/html/tmp108_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmp108.h

[Go to the documentation of this file.](tmp108_8h.md)

1/\*

2 \* Copyright (c) 2021, Jimmy Johnson <catch22@fastmail.net>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP108\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP108\_H\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

[ 22](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263ac)enum [sensor\_attribute\_tmp\_108](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263ac) {

[ 24](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca7d3aaeefef79d21d14b094a73859aad5) [SENSOR\_ATTR\_TMP108\_ONE\_SHOT\_MODE](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca7d3aaeefef79d21d14b094a73859aad5) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 26](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca77ad914dd8719431e411c521ba439f51) [SENSOR\_ATTR\_TMP108\_SHUTDOWN\_MODE](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca77ad914dd8719431e411c521ba439f51),

[ 28](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca15ffb18b0a416692f198df2974695845) [SENSOR\_ATTR\_TMP108\_CONTINUOUS\_CONVERSION\_MODE](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca15ffb18b0a416692f198df2974695845),

[ 30](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca7368db02e4565f72373efbcf8d671feb) [SENSOR\_ATTR\_TMP108\_ALERT\_POLARITY](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca7368db02e4565f72373efbcf8d671feb)

31};

32

[ 34](tmp108_8h.md#a8d041a318c3d3ec133079a630ae33748)#define TMP108\_OVER\_TEMP\_MASK 0x1000U

35

[ 37](tmp108_8h.md#a3d9d079354814ebac6580499851d8846)#define TMP108\_UNDER\_TEMP\_MASK 0x0800U

38

[ 40](tmp108_8h.md#aeb7ae5deef7c19daa33a7b90105f6e72)#define A6212\_ALERT\_TEMP\_MASK 0x0020U

41

42#ifdef \_\_cplusplus

43}

44#endif

45

46#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_TMP108\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[sensor\_attribute\_tmp\_108](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263ac)

sensor\_attribute\_tmp\_108

**Definition** tmp108.h:22

[SENSOR\_ATTR\_TMP108\_CONTINUOUS\_CONVERSION\_MODE](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca15ffb18b0a416692f198df2974695845)

@ SENSOR\_ATTR\_TMP108\_CONTINUOUS\_CONVERSION\_MODE

Turn on continuous conversion.

**Definition** tmp108.h:28

[SENSOR\_ATTR\_TMP108\_ALERT\_POLARITY](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca7368db02e4565f72373efbcf8d671feb)

@ SENSOR\_ATTR\_TMP108\_ALERT\_POLARITY

Set the alert pin polarity.

**Definition** tmp108.h:30

[SENSOR\_ATTR\_TMP108\_SHUTDOWN\_MODE](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca77ad914dd8719431e411c521ba439f51)

@ SENSOR\_ATTR\_TMP108\_SHUTDOWN\_MODE

Shutdown the sensor.

**Definition** tmp108.h:26

[SENSOR\_ATTR\_TMP108\_ONE\_SHOT\_MODE](tmp108_8h.md#a27e0be5adff7e6b9ddee08ab329263aca7d3aaeefef79d21d14b094a73859aad5)

@ SENSOR\_ATTR\_TMP108\_ONE\_SHOT\_MODE

Turn on power saving/one shot mode.

**Definition** tmp108.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tmp108.h](tmp108_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
