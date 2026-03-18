---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ptp__time_8h.html
original_path: doxygen/html/ptp__time_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ptp\_time.h File Reference

Public functions for the Precision Time Protocol time specification.
[More...](#details)

`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`  
`#include <[zephyr/net/net_time.h](net__time_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](ptp__time_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_ptp\_time](structnet__ptp__time.md) |
|  | (Generalized) Precision Time Protocol Timestamp format. [More...](structnet__ptp__time.md#details) |
| struct | [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) |
|  | Generalized Precision Time Protocol Extended Timestamp format. [More...](structnet__ptp__extended__time.md#details) |

| Functions | |
| --- | --- |
| static [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) | [net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9) (struct [net\_ptp\_time](structnet__ptp__time.md) \*ts) |
|  | Convert a PTP timestamp to a nanosecond precision timestamp, both related to the local network reference clock. |
| static struct [net\_ptp\_time](structnet__ptp__time.md) | [ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df) ([net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) nsec) |
|  | Convert a nanosecond precision timestamp to a PTP timestamp, both related to the local network reference clock. |

## Detailed Description

Public functions for the Precision Time Protocol time specification.

References are to version 2019 of IEEE 1588, ("PTP") and version 2020 of IEEE 802.1AS ("gPTP").

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ptp\_time.h](ptp__time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
