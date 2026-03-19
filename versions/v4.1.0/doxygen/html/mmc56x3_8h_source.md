---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mmc56x3_8h_source.html
original_path: doxygen/html/mmc56x3_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mmc56x3.h

[Go to the documentation of this file.](mmc56x3_8h.md)

1/\*

2 \* Copyright (c) 2023 Kurtis Dinelle

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MMC56X3\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MMC56X3\_H\_

17

18#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8)enum [sensor\_attribute\_mmc56x3](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8) {

25 /\* Bandwidth selection bit 0.

26 \*

27 \* Adjust length of decimation filter. Controls duration of

28 \* each measurement. Affects ODR; see datasheet for details.

29 \*/

[ 30](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a9cf5f5faa59252aa253a6ad708bf2e1b) [SENSOR\_ATTR\_BANDWIDTH\_SELECTION\_BITS\_0](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a9cf5f5faa59252aa253a6ad708bf2e1b) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) + 1,

31

32 /\* Bandwidth selection bit 1.

33 \*

34 \* Adjust length of decimation filter. Controls duration of

35 \* each measurement. Affects ODR; see datasheet for details.

36 \*/

[ 37](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a4100c5eb1d3a101f409ba20100af6630) [SENSOR\_ATTR\_BANDWIDTH\_SELECTION\_BITS\_1](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a4100c5eb1d3a101f409ba20100af6630),

38

39 /\* Automatic self reset.

40 \*

41 \* Enable automatic self-reset function.

42 \* Affects ODR; see datasheet for details.

43 \*/

[ 44](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a318620970dbe7fd406bcb27d4387253f) [SENSOR\_ATTR\_AUTOMATIC\_SELF\_RESET](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a318620970dbe7fd406bcb27d4387253f),

45};

46

47#ifdef \_\_cplusplus

48}

49#endif

50

51#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_MMC56X3\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[sensor\_attribute\_mmc56x3](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8)

sensor\_attribute\_mmc56x3

**Definition** mmc56x3.h:24

[SENSOR\_ATTR\_AUTOMATIC\_SELF\_RESET](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a318620970dbe7fd406bcb27d4387253f)

@ SENSOR\_ATTR\_AUTOMATIC\_SELF\_RESET

**Definition** mmc56x3.h:44

[SENSOR\_ATTR\_BANDWIDTH\_SELECTION\_BITS\_1](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a4100c5eb1d3a101f409ba20100af6630)

@ SENSOR\_ATTR\_BANDWIDTH\_SELECTION\_BITS\_1

**Definition** mmc56x3.h:37

[SENSOR\_ATTR\_BANDWIDTH\_SELECTION\_BITS\_0](mmc56x3_8h.md#af722f9a8bf8bae84c57aaa1ece387ad8a9cf5f5faa59252aa253a6ad708bf2e1b)

@ SENSOR\_ATTR\_BANDWIDTH\_SELECTION\_BITS\_0

**Definition** mmc56x3.h:30

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [mmc56x3.h](mmc56x3_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
