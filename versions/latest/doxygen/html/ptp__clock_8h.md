---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ptp__clock_8h.html
original_path: doxygen/html/ptp__clock_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ptp\_clock.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/net/ptp_time.h](ptp__time_8h_source.md)>`  
`#include <syscalls/ptp_clock.h>`

[Go to the source code of this file.](ptp__clock_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ptp\_clock\_driver\_api](structptp__clock__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [PTP\_CLOCK\_NAME](#a31fba0e7a6444b3301cbe0372e6d1996)   "PTP\_CLOCK" |

| Functions | |
| --- | --- |
| static int | [ptp\_clock\_set](#a41123183be722b3423d5e993d3cde7c2) (const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md)) |
|  | Set the time of the PTP clock. |
| int | [ptp\_clock\_get](#a443f97ef2766e87c0b42c6ad6f7b63b4) (const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md)) |
|  | Get the time of the PTP clock. |
| static int | [ptp\_clock\_adjust](#abd11d19b5ec5491e5813bf7cb74ab9b0) (const struct [device](structdevice.md) \*dev, int increment) |
|  | Adjust the PTP clock time. |
| static int | [ptp\_clock\_rate\_adjust](#a310ee4974e6f3b01c4aa1b985194e57a) (const struct [device](structdevice.md) \*dev, double rate) |
|  | Adjust the PTP clock time change rate when compared to its neighbor. |

## Macro Definition Documentation

## [◆ ](#a31fba0e7a6444b3301cbe0372e6d1996)PTP\_CLOCK\_NAME

| #define PTP\_CLOCK\_NAME   "PTP\_CLOCK" |
| --- |

## Function Documentation

## [◆ ](#abd11d19b5ec5491e5813bf7cb74ab9b0)ptp\_clock\_adjust()

| | int ptp\_clock\_adjust | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | int | *increment* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Adjust the PTP clock time.

Parameters
:   | dev | PTP clock device |
    | --- | --- |
    | increment | Increment of the clock in nanoseconds |

Returns
:   0 if ok, <0 if error

## [◆ ](#a443f97ef2766e87c0b42c6ad6f7b63b4)ptp\_clock\_get()

| int ptp\_clock\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [net\_ptp\_time](structnet__ptp__time.md) \* | *tm* ) |

Get the time of the PTP clock.

Parameters
:   | dev | PTP clock device |
    | --- | --- |
    | [tm](structtm.md) | Where to store the current time. |

Returns
:   0 if ok, <0 if error

## [◆ ](#a310ee4974e6f3b01c4aa1b985194e57a)ptp\_clock\_rate\_adjust()

| | int ptp\_clock\_rate\_adjust | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | double | *rate* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Adjust the PTP clock time change rate when compared to its neighbor.

Parameters
:   | dev | PTP clock device |
    | --- | --- |
    | rate | Rate of the clock time change |

Returns
:   0 if ok, <0 if error

## [◆ ](#a41123183be722b3423d5e993d3cde7c2)ptp\_clock\_set()

| | int ptp\_clock\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [net\_ptp\_time](structnet__ptp__time.md) \* | *tm* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set the time of the PTP clock.

Parameters
:   | dev | PTP clock device |
    | --- | --- |
    | [tm](structtm.md) | Time to set |

Returns
:   0 if ok, <0 if error

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ptp\_clock.h](ptp__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
