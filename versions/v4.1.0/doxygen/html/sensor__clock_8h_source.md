---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor__clock_8h_source.html
original_path: doxygen/html/sensor__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_clock.h

[Go to the documentation of this file.](sensor__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 Cienet

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_SENSOR\_CLOCK\_H\_

8#define ZEPHYR\_DRIVERS\_SENSOR\_CLOCK\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 28](sensor__clock_8h.md#a337e06f1eecc2700268f803cf2eecefb)int [sensor\_clock\_get\_cycles](sensor__clock_8h.md#a337e06f1eecc2700268f803cf2eecefb)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles);

29

[ 39](sensor__clock_8h.md#afe8b63ce73b7a40276996b1ee5408cd6)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sensor\_clock\_cycles\_to\_ns](sensor__clock_8h.md#afe8b63ce73b7a40276996b1ee5408cd6)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles);

40

41#ifdef \_\_cplusplus

42}

43#endif

44

45#endif /\* ZEPHYR\_DRIVERS\_SENSOR\_CLOCK\_H\_ \*/

[sensor\_clock\_get\_cycles](sensor__clock_8h.md#a337e06f1eecc2700268f803cf2eecefb)

int sensor\_clock\_get\_cycles(uint64\_t \*cycles)

Retrieve the current sensor clock cycles.

[sensor\_clock\_cycles\_to\_ns](sensor__clock_8h.md#afe8b63ce73b7a40276996b1ee5408cd6)

uint64\_t sensor\_clock\_cycles\_to\_ns(uint64\_t cycles)

Convert clock cycles to nanoseconds.

[stdint.h](stdint_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor\_clock.h](sensor__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
