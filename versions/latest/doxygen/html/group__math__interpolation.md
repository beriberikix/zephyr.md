---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__math__interpolation.html
original_path: doxygen/html/group__math__interpolation.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Math Interpolation Functions

[Utilities](group__utilities.md)

Linear interpolation utilities for mathematical operations.
[More...](#details)

| Functions | |
| --- | --- |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [linear\_interpolate](#ga8abbb1799796222b39a051819bd19a2a) (const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*x\_axis, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*y\_axis, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) x) |
|  | Perform a linear interpolation across an arbitrary curve. |

## Detailed Description

Linear interpolation utilities for mathematical operations.

## Function Documentation

## [◆ ](#ga8abbb1799796222b39a051819bd19a2a)linear\_interpolate()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) linear\_interpolate | ( | const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *x\_axis*, | | --- | --- | --- | --- | |  |  | const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *y\_axis*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *x* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/math/interpolation.h](interpolation_8h.md)>`

Perform a linear interpolation across an arbitrary curve.

Note
:   Result rounding occurs away from 0, e.g: 1.5 -> 2, -5.5 -> -6

Parameters
:   | x\_axis | Ascending list of X co-ordinates for *y\_axis* data points |
    | --- | --- |
    | y\_axis | Y co-ordinates for each X data point |
    | len | Length of the *x\_axis* and *y\_axis* arrays |
    | x | X co-ordinate to lookup |

Return values
:   | y\_axis[0] | if x < x\_axis[0] |
    | --- | --- |
    | y\_axis[len | - 1] if x > x\_axis[len - 1] |
    | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | Linear interpolation between the two nearest *y\_axis* values. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
