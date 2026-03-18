---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__time_8h.html
original_path: doxygen/html/net__time_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_time.h File Reference

Representation of nanosecond resolution elapsed time and timestamps in the network stack.
[More...](#details)

`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`

[Go to the source code of this file.](net__time_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NET\_TIME\_MAX](group__net__time.md#ga38c90d968fc905093de2db057e6fa199)   [INT64\_MAX](stdint_8h.md#ad0d744f05898e32d01f73f8af3cd2071) |
|  | The largest positive time value that can be represented by [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56 "Any occurrence of net_time_t specifies a concept of nanosecond resolution scalar time span,..."). |
| #define | [NET\_TIME\_MIN](group__net__time.md#ga732cb69409953ce0ce08991179afe718)   [INT64\_MIN](stdint_8h.md#ab21f12f372f67b8ff0aa3432336ede67) |
|  | The smallest negative time value that can be represented by [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56 "Any occurrence of net_time_t specifies a concept of nanosecond resolution scalar time span,..."). |
| #define | [NET\_TIME\_SEC\_MAX](group__net__time.md#gabcd93249b790bea7ed6f8aab9ebe568a)   ([NET\_TIME\_MAX](group__net__time.md#ga38c90d968fc905093de2db057e6fa199) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) |
|  | The largest positive number of seconds that can be safely represented by [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56 "Any occurrence of net_time_t specifies a concept of nanosecond resolution scalar time span,..."). |
| #define | [NET\_TIME\_SEC\_MIN](group__net__time.md#ga1fe8655623f0db550f7ae501b161940b)   ([NET\_TIME\_MIN](group__net__time.md#ga732cb69409953ce0ce08991179afe718) / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)) |
|  | The smallest negative number of seconds that can be safely represented by [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56 "Any occurrence of net_time_t specifies a concept of nanosecond resolution scalar time span,..."). |

| Typedefs | |
| --- | --- |
| typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) |
|  | Any occurrence of [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56 "Any occurrence of net_time_t specifies a concept of nanosecond resolution scalar time span,...") specifies a concept of nanosecond resolution scalar time span, future (positive) or past (negative) relative time or absolute timestamp referred to some local network uptime reference clock that does not wrap during uptime and is - in a certain, well-defined sense - common to all local network interfaces, sometimes even to remote interfaces on the same network. |

## Detailed Description

Representation of nanosecond resolution elapsed time and timestamps in the network stack.

Inspired by [https://github.com/torvalds/linux/blob/master/include/linux/ktime.h](https://github.com/torvalds/linux/blob/master/include/linux/ktime.h) and [https://github.com/torvalds/linux/blob/master/](https://github.com/torvalds/linux/blob/master/)[tools/]include/linux/time64.h

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_time.h](net__time_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
