---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/dac161s997_8h_source.html
original_path: doxygen/html/dac161s997_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dac161s997.h

[Go to the documentation of this file.](dac161s997_8h.md)

1/\*

2 \* Copyright (c) 2025 Prevas A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DAC\_DAC161S997\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DAC\_DAC161S997\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/device.h](device_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](uniondac161s997__status.md)union [dac161s997\_status](uniondac161s997__status.md) {

[ 18](uniondac161s997__status.md#ae607e4cf155134e1924ab6e82fd4c77c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [raw](uniondac161s997__status.md#ae607e4cf155134e1924ab6e82fd4c77c);

19 struct {

[ 23](uniondac161s997__status.md#a976624fa275ddcdbe02532ef49df1bec) bool [current\_loop\_status](uniondac161s997__status.md#a976624fa275ddcdbe02532ef49df1bec): 1;

[ 27](uniondac161s997__status.md#ae6b7aa08e791c7a16734ab0f749fba7f) bool [loop\_status](uniondac161s997__status.md#ae6b7aa08e791c7a16734ab0f749fba7f): 1;

[ 33](uniondac161s997__status.md#a607f3408e26204ab5d7587f45551a31e) bool [spi\_timeout\_error](uniondac161s997__status.md#a607f3408e26204ab5d7587f45551a31e): 1;

[ 39](uniondac161s997__status.md#a39d07d6166ac1472f79eaf9e3d13c750) bool [frame\_status](uniondac161s997__status.md#a39d07d6166ac1472f79eaf9e3d13c750): 1;

[ 43](uniondac161s997__status.md#a96c43cb002dea17b7824288d9092cb90) bool [error\_level\_pin\_state](uniondac161s997__status.md#a96c43cb002dea17b7824288d9092cb90): 1;

[ 47](uniondac161s997__status.md#a55ea538eb473b99d4f15831f59844094) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dac\_resolution](uniondac161s997__status.md#a55ea538eb473b99d4f15831f59844094): 3;

48 } \_\_packed;

49};

50

[ 58](dac161s997_8h.md#a24c693e8a7c22c6340db7595a01ef09f)typedef void (\*[dac161s997\_error\_callback\_t](dac161s997_8h.md#a24c693e8a7c22c6340db7595a01ef09f))(const struct [device](structdevice.md) \*dev,

59 const union [dac161s997\_status](uniondac161s997__status.md) \*status);

60

[ 71](dac161s997_8h.md#ab81de98755b9bffd8e4599fbe4ceb557)int [dac161s997\_set\_error\_callback](dac161s997_8h.md#ab81de98755b9bffd8e4599fbe4ceb557)(const struct [device](structdevice.md) \*dev, [dac161s997\_error\_callback\_t](dac161s997_8h.md#a24c693e8a7c22c6340db7595a01ef09f) cb);

72

73#ifdef \_\_cplusplus

74}

75#endif

76

77#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DAC\_DAC161S997\_H\_ \*/

[dac161s997\_error\_callback\_t](dac161s997_8h.md#a24c693e8a7c22c6340db7595a01ef09f)

void(\* dac161s997\_error\_callback\_t)(const struct device \*dev, const union dac161s997\_status \*status)

Callback to invoke when an error is triggered.

**Definition** dac161s997.h:58

[dac161s997\_set\_error\_callback](dac161s997_8h.md#ab81de98755b9bffd8e4599fbe4ceb557)

int dac161s997\_set\_error\_callback(const struct device \*dev, dac161s997\_error\_callback\_t cb)

Set callback to invoke when an error is triggered.

[device.h](device_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[dac161s997\_status](uniondac161s997__status.md)

**Definition** dac161s997.h:17

[dac161s997\_status::frame\_status](uniondac161s997__status.md#a39d07d6166ac1472f79eaf9e3d13c750)

bool frame\_status

A frame error is caused by an incorrect number of clocks during a register write.

**Definition** dac161s997.h:39

[dac161s997\_status::dac\_resolution](uniondac161s997__status.md#a55ea538eb473b99d4f15831f59844094)

uint8\_t dac\_resolution

DAC resolution register.

**Definition** dac161s997.h:47

[dac161s997\_status::spi\_timeout\_error](uniondac161s997__status.md#a607f3408e26204ab5d7587f45551a31e)

bool spi\_timeout\_error

True if a SPI command has not been received within SPI timeout period (default 100 ms).

**Definition** dac161s997.h:33

[dac161s997\_status::error\_level\_pin\_state](uniondac161s997__status.md#a96c43cb002dea17b7824288d9092cb90)

bool error\_level\_pin\_state

Returns the state of the ERR\_LVL pin.

**Definition** dac161s997.h:43

[dac161s997\_status::current\_loop\_status](uniondac161s997__status.md#a976624fa275ddcdbe02532ef49df1bec)

bool current\_loop\_status

True if the DAC161S997 is unable to maintain the output current.

**Definition** dac161s997.h:23

[dac161s997\_status::raw](uniondac161s997__status.md#ae607e4cf155134e1924ab6e82fd4c77c)

uint8\_t raw

**Definition** dac161s997.h:18

[dac161s997\_status::loop\_status](uniondac161s997__status.md#ae6b7aa08e791c7a16734ab0f749fba7f)

bool loop\_status

Identical to current\_loop\_status except this bit is sticky.

**Definition** dac161s997.h:27

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dac](dir_6fd694d6a6f65d036ccf37605ee5a399.md)
- [dac161s997.h](dac161s997_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
