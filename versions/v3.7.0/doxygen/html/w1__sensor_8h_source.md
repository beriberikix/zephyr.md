---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/w1__sensor_8h_source.html
original_path: doxygen/html/w1__sensor_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

w1\_sensor.h

[Go to the documentation of this file.](w1__sensor_8h.md)

1/\*

2 \* Copyright (c) 2022, Thomas Stranger

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_W1\_SENSOR\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_W1\_SENSOR\_H\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

23#include <[zephyr/drivers/w1.h](w1_8h.md)>

24

31

[ 32](group__w1__sensor.md#gae6c6848f94bde562a95f5f987a8c76fc)enum [sensor\_attribute\_w1](group__w1__sensor.md#gae6c6848f94bde562a95f5f987a8c76fc) {

[ 34](group__w1__sensor.md#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36) [SENSOR\_ATTR\_W1\_ROM](group__w1__sensor.md#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

35};

36

[ 43](group__w1__sensor.md#ga947aea2687107b1b3471c3e9eded7504)static inline void [w1\_rom\_to\_sensor\_value](group__w1__sensor.md#ga947aea2687107b1b3471c3e9eded7504)(const struct [w1\_rom](structw1__rom.md) \*rom,

44 struct [sensor\_value](structsensor__value.md) \*val)

45{

46 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = [sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)rom) & [BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)(32);

47 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = [sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)rom) >> 32;

48}

49

[ 56](group__w1__sensor.md#ga3c0b20580be768bcc45f93a4c01ee9db)static inline void [w1\_sensor\_value\_to\_rom](group__w1__sensor.md#ga3c0b20580be768bcc45f93a4c01ee9db)(const struct [sensor\_value](structsensor__value.md) \*val,

57 struct [w1\_rom](structw1__rom.md) \*rom)

58{

59 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) temp64 = (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b)) << 32)

60 | ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe);

61 [sys\_put\_be64](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)(temp64, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)rom);

62}

63

67

68#ifdef \_\_cplusplus

69}

70#endif

71

72#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_W1\_SENSOR\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)

#define BIT64\_MASK(n)

64-bit bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:74

[w1\_sensor\_value\_to\_rom](group__w1__sensor.md#ga3c0b20580be768bcc45f93a4c01ee9db)

static void w1\_sensor\_value\_to\_rom(const struct sensor\_value \*val, struct w1\_rom \*rom)

Function to write an rom id stored in a sensor value to a struct w1\_rom ptr.

**Definition** w1\_sensor.h:56

[w1\_rom\_to\_sensor\_value](group__w1__sensor.md#ga947aea2687107b1b3471c3e9eded7504)

static void w1\_rom\_to\_sensor\_value(const struct w1\_rom \*rom, struct sensor\_value \*val)

Function to write a w1\_rom struct to an sensor value ptr.

**Definition** w1\_sensor.h:43

[sensor\_attribute\_w1](group__w1__sensor.md#gae6c6848f94bde562a95f5f987a8c76fc)

sensor\_attribute\_w1

**Definition** w1\_sensor.h:32

[SENSOR\_ATTR\_W1\_ROM](group__w1__sensor.md#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36)

@ SENSOR\_ATTR\_W1\_ROM

Device unique 1-Wire ROM.

**Definition** w1\_sensor.h:34

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sensor\_value](structsensor__value.md)

Representation of a sensor readout value.

**Definition** sensor.h:51

[sensor\_value::val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b)

int32\_t val2

Fractional part of the value (in one-millionth parts).

**Definition** sensor.h:55

[sensor\_value::val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe)

int32\_t val1

Integer part of the value.

**Definition** sensor.h:53

[w1\_rom](structw1__rom.md)

w1\_rom struct.

**Definition** w1.h:434

[sys\_put\_be64](sys_2byteorder_8h.md#a3e0d2e4e85249497011f5f9ea0d2987c)

static void sys\_put\_be64(uint64\_t val, uint8\_t dst[8])

Put a 64-bit integer as big-endian to arbitrary location.

**Definition** byteorder.h:395

[sys\_get\_be64](sys_2byteorder_8h.md#ad8e00ff5c0b9e394291936d1a570c215)

static uint64\_t sys\_get\_be64(const uint8\_t src[8])

Get a 64-bit integer stored in big-endian format.

**Definition** byteorder.h:576

[w1.h](w1_8h.md)

Public 1-Wire Driver APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [w1\_sensor.h](w1__sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
