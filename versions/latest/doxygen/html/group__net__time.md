---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__net__time.html
original_path: doxygen/html/group__net__time.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network time representation.

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

| Macros | |
| --- | --- |
| #define | [NET\_TIME\_MAX](#ga38c90d968fc905093de2db057e6fa199)   [INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071) |
|  | The largest positive time value that can be represented by [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56). |
| #define | [NET\_TIME\_MIN](#ga732cb69409953ce0ce08991179afe718)   [INT64\_MIN](stdint_8h.md#ab21f12f372f67b8ff0aa3432336ede67) |
|  | The smallest negative time value that can be represented by [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56). |
| #define | [NET\_TIME\_SEC\_MAX](#gabcd93249b790bea7ed6f8aab9ebe568a)   ([NET\_TIME\_MAX](#ga38c90d968fc905093de2db057e6fa199) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) |
|  | The largest positive number of seconds that can be safely represented by [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56). |
| #define | [NET\_TIME\_SEC\_MIN](#ga1fe8655623f0db550f7ae501b161940b)   ([NET\_TIME\_MIN](#ga732cb69409953ce0ce08991179afe718) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) |
|  | The smallest negative number of seconds that can be safely represented by [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56). |

| Typedefs | |
| --- | --- |
| typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) |
|  | Any occurrence of [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) specifies a concept of nanosecond resolution scalar time span, future (positive) or past (negative) relative time or absolute timestamp referred to some local network uptime reference clock that does not wrap during uptime and is - in a certain, well-defined sense - common to all local network interfaces, sometimes even to remote interfaces on the same network. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga38c90d968fc905093de2db057e6fa199)NET\_TIME\_MAX

| #define NET\_TIME\_MAX   [INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071) |
| --- |

`#include <[net_time.h](net__time_8h.md)>`

The largest positive time value that can be represented by [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56).

## [◆ ](#ga732cb69409953ce0ce08991179afe718)NET\_TIME\_MIN

| #define NET\_TIME\_MIN   [INT64\_MIN](stdint_8h.md#ab21f12f372f67b8ff0aa3432336ede67) |
| --- |

`#include <[net_time.h](net__time_8h.md)>`

The smallest negative time value that can be represented by [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56).

## [◆ ](#gabcd93249b790bea7ed6f8aab9ebe568a)NET\_TIME\_SEC\_MAX

| #define NET\_TIME\_SEC\_MAX   ([NET\_TIME\_MAX](#ga38c90d968fc905093de2db057e6fa199) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) |
| --- |

`#include <[net_time.h](net__time_8h.md)>`

The largest positive number of seconds that can be safely represented by [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56).

## [◆ ](#ga1fe8655623f0db550f7ae501b161940b)NET\_TIME\_SEC\_MIN

| #define NET\_TIME\_SEC\_MIN   ([NET\_TIME\_MIN](#ga732cb69409953ce0ce08991179afe718) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) |
| --- |

`#include <[net_time.h](net__time_8h.md)>`

The smallest negative number of seconds that can be safely represented by [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56).

## Typedef Documentation

## [◆ ](#gaf1da332e3909fca30de991cc2f950e56)net\_time\_t

| typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) |
| --- |

`#include <[net_time.h](net__time_8h.md)>`

Any occurrence of [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) specifies a concept of nanosecond resolution scalar time span, future (positive) or past (negative) relative time or absolute timestamp referred to some local network uptime reference clock that does not wrap during uptime and is - in a certain, well-defined sense - common to all local network interfaces, sometimes even to remote interfaces on the same network.

This type is EXPERIMENTAL. Usage is currently restricted to representation of time within the network subsystem.

Timed network protocols (PTP, TDMA, ...) usually require several local or remote interfaces to share a common notion of elapsed time within well-defined tolerances. Network uptime therefore differs from time represented by a single hardware counter peripheral in that it will need to be represented in several distinct hardware peripherals with different frequencies, accuracy and precision. To co-operate, these hardware counters will have to be "syntonized" or "disciplined" (i.e. frequency and phase locked) with respect to a common local or remote network reference time signal. Be aware that while syntonized clocks share the same frequency and phase, they do not usually share the same epoch (zero-point).

This also explains why network time, if represented as a cycle value of some specific hardware counter, will never be "precise" but only can be "good
enough" with respect to the tolerances (resolution, drift, jitter) required by a given network protocol. All counter peripherals involved in a timed network protocol must comply with these tolerances.

Please use specific cycle/tick counter values rather than [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) whenever possible especially when referring to the kernel system clock or values of any single counter peripheral.

[net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) cannot represent general clocks referred to an arbitrary epoch as it only covers roughly +/- ~290 years. It also cannot be used to represent time according to a more complex timescale (e.g. including leap seconds, time adjustments, complex calendars or time zones). In these cases you may use [timespec](structtimespec.md "timespec") (C11, POSIX.1-2001), [timeval](structtimeval.md "timeval") (POSIX.1-2001) or broken down time as in [tm](structtm.md "tm") (C90). The advantage of [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) over these structured time representations is lower memory footprint, faster and simpler scalar arithmetics and easier conversion from/to low-level hardware counter values. Also [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) can be used in the network stack as well as in applications while POSIX concepts cannot. Converting [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) from/to structured time representations is possible in a limited way but - except for [timespec](structtimespec.md "timespec") - requires concepts that must be implemented by higher-level APIs. Utility functions converting from/to [timespec](structtimespec.md "timespec") will be provided as part of the [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) API as and when needed.

If you want to represent more coarse grained scalar time in network applications, use [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7 "time_t") (C99, POSIX.1-2001) which is specified to represent seconds or [suseconds\_t](__timespec_8h.md#ad7acf95ceafb15a1d8d86af0c4982995 "suseconds_t") (POSIX.1-2001) for microsecond resolution. Kernel [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2 "k_ticks_t") and cycles (both specific to Zephyr) have an unspecified resolution but are useful to represent kernel timer values and implement high resolution spinning.

If you need even finer grained time resolution, you may want to look at (g)PTP concepts, see [net\_ptp\_extended\_time](structnet__ptp__extended__time.md "net_ptp_extended_time").

The reason why we don't use [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) directly to represent scalar nanosecond resolution times in the network stack is that it has been shown in the past that fields using generic type will often not be used correctly (e.g. with the wrong resolution or to represent underspecified concepts of time with unclear syntonization semantics).

Any API that exposes or consumes [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) values SHALL ensure that it maintains the specified contract including all protocol specific tolerances and therefore clients can rely on common semantics of this type. This makes times coming from different hardware peripherals and even from different network nodes comparable within well-defined limits and therefore [net\_time\_t](#gaf1da332e3909fca30de991cc2f950e56) is the ideal intermediate building block for timed network protocols.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
