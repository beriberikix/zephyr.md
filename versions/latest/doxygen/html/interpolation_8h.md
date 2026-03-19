---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/interpolation_8h.html
original_path: doxygen/html/interpolation_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

interpolation.h File Reference

Provide linear interpolation functions.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[math.h](math_8h_source.md)>`

[Go to the source code of this file.](interpolation_8h_source.md)

| Functions | |
| --- | --- |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [linear\_interpolate](#a8abbb1799796222b39a051819bd19a2a) (const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*x\_axis, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*y\_axis, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) x) |
|  | Perform a linear interpolation across an arbitrary curve. |

## Detailed Description

Provide linear interpolation functions.

## Function Documentation

## [◆ ](#a8abbb1799796222b39a051819bd19a2a)linear\_interpolate()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) linear\_interpolate | ( | const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *x\_axis*, | | --- | --- | --- | --- | |  |  | const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *y\_axis*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *x* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [math](dir_76cc2d861a01f89f8d0ad119e28af149.md)
- [interpolation.h](interpolation_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
