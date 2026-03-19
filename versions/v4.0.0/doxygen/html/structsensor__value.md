---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsensor__value.html
original_path: doxygen/html/structsensor__value.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_value Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Sensor Interface](group__sensor__interface.md)

Representation of a sensor readout value.
[More...](#details)

`#include <[sensor.h](sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [val1](#af21dddb084da4c42a7e77b48edf26fbe) |
|  | Integer part of the value. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [val2](#a91f81bd0f5da69084cf3c629fde68a1b) |
|  | Fractional part of the value (in one-millionth parts). |

## Detailed Description

Representation of a sensor readout value.

The value is represented as having an integer and a fractional part, and can be obtained using the formula val1 + val2 \* 10^(-6). Negative values also adhere to the above formula, but may need special attention. Here are some examples of the value representation:

```
 0.5: val1 =  0, val2 =  500000
-0.5: val1 =  0, val2 = -500000
-1.0: val1 = -1, val2 =  0
-1.5: val1 = -1, val2 = -500000
```

## Field Documentation

## [◆ ](#af21dddb084da4c42a7e77b48edf26fbe)val1

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sensor\_value::val1 |
| --- |

Integer part of the value.

## [◆ ](#a91f81bd0f5da69084cf3c629fde68a1b)val2

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sensor\_value::val2 |
| --- |

Fractional part of the value (in one-millionth parts).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor.h](sensor_8h_source.md)

- [sensor\_value](structsensor__value.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
