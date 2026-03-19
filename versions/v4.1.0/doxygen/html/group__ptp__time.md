---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ptp__time.html
original_path: doxygen/html/group__ptp__time.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PTP time

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Precision Time Protocol time specification.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_ptp\_time](structnet__ptp__time.md) |
|  | (Generalized) Precision Time Protocol Timestamp format. [More...](structnet__ptp__time.md#details) |
| struct | [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) |
|  | Generalized Precision Time Protocol Extended Timestamp format. [More...](structnet__ptp__extended__time.md#details) |

| Functions | |
| --- | --- |
| static [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) | [net\_ptp\_time\_to\_ns](#gaf9f253990e644e161e1b3cc317e8e9e9) (struct [net\_ptp\_time](structnet__ptp__time.md) \*ts) |
|  | Convert a PTP timestamp to a nanosecond precision timestamp, both related to the local network reference clock. |
| static struct [net\_ptp\_time](structnet__ptp__time.md) | [ns\_to\_net\_ptp\_time](#gafd9d45cca3d630ce51109537165d53df) ([net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) nsec) |
|  | Convert a nanosecond precision timestamp to a PTP timestamp, both related to the local network reference clock. |

## Detailed Description

Precision Time Protocol time specification.

Since
:   1.13

Version
:   0.8.0

## Function Documentation

## [◆ ](#gaf9f253990e644e161e1b3cc317e8e9e9)net\_ptp\_time\_to\_ns()

| | [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_ptp\_time\_to\_ns | ( | struct [net\_ptp\_time](structnet__ptp__time.md) \* | *ts* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ptp_time.h](ptp__time_8h.md)>`

Convert a PTP timestamp to a nanosecond precision timestamp, both related to the local network reference clock.

Note
:   Only timestamps representing up to ~290 years can be converted to nanosecond timestamps. Larger timestamps will return the maximum representable nanosecond precision timestamp.

Parameters
:   | ts | the PTP timestamp |
    | --- | --- |

Returns
:   the corresponding nanosecond precision timestamp

## [◆ ](#gafd9d45cca3d630ce51109537165d53df)ns\_to\_net\_ptp\_time()

| | struct [net\_ptp\_time](structnet__ptp__time.md) ns\_to\_net\_ptp\_time | ( | [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) | *nsec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ptp_time.h](ptp__time_8h.md)>`

Convert a nanosecond precision timestamp to a PTP timestamp, both related to the local network reference clock.

Parameters
:   | nsec | a nanosecond precision timestamp |
    | --- | --- |

Returns
:   the corresponding PTP timestamp

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
