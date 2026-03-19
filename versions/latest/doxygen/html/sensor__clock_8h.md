---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor__clock_8h.html
original_path: doxygen/html/sensor__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_clock.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](sensor__clock_8h_source.md)

| Functions | |
| --- | --- |
| int | [sensor\_clock\_get\_cycles](#a337e06f1eecc2700268f803cf2eecefb) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles) |
|  | Retrieve the current sensor clock cycles. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sensor\_clock\_cycles\_to\_ns](#afe8b63ce73b7a40276996b1ee5408cd6) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles) |
|  | Convert clock cycles to nanoseconds. |

## Function Documentation

## [◆ ](#afe8b63ce73b7a40276996b1ee5408cd6)sensor\_clock\_cycles\_to\_ns()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sensor\_clock\_cycles\_to\_ns | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *cycles* | ) |  |
| --- | --- | --- | --- | --- | --- |

Convert clock cycles to nanoseconds.

This function converts clock cycles into nanoseconds based on the clock frequency.

Parameters
:   | cycles | Clock cycles to convert. |
    | --- | --- |

Returns
:   Time in nanoseconds.

## [◆ ](#a337e06f1eecc2700268f803cf2eecefb)sensor\_clock\_get\_cycles()

| int sensor\_clock\_get\_cycles | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *cycles* | ) |  |
| --- | --- | --- | --- | --- | --- |

Retrieve the current sensor clock cycles.

This function obtains the current cycle count from the selected sensor clock source. The clock source may be the system clock or an external clock, depending on the configuration.

Parameters
:   | [out] | cycles | Pointer to a 64-bit unsigned integer where the current clock cycle count will be stored. |
    | --- | --- | --- |

Returns
:   0 on success, or an error code on failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor\_clock.h](sensor__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
