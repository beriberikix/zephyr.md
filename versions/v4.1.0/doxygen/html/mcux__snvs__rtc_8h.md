---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mcux__snvs__rtc_8h.html
original_path: doxygen/html/mcux__snvs__rtc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_snvs\_rtc.h File Reference

Real-time clock control based on the MCUX IMX SNVS counter API.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](mcux__snvs__rtc_8h_source.md)

| Functions | |
| --- | --- |
| int | [mcux\_snvs\_rtc\_set](#a9f9c1ee4ccae8d219507778f4bebae6e) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks) |
|  | Set the current counter value. |

## Detailed Description

Real-time clock control based on the MCUX IMX SNVS counter API.

The core Zephyr API to this device is as a counter.

Additional implementation details a user should take into account:

- an optional SRTC can be enabled (default) with configuration options
- the high power channel (id 0) is always available, the low power channel (id 1) is optional
- the low power alarm can be used to assert a wake-up
- the counter has a fixed 1Hz period

## Function Documentation

## [◆ ](#a9f9c1ee4ccae8d219507778f4bebae6e)mcux\_snvs\_rtc\_set()

| int mcux\_snvs\_rtc\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ticks* ) |

Set the current counter value.

As the counter advances at 1Hz this will usually be set to the current UNIX time stamp.

Parameters
:   | dev | the IMX SNVS RTC device pointer. |
    | --- | --- |
    | ticks | the new value of the internal counter |

Return values
:   | non-negative | on success |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc](dir_fe6de79d2b035e3fa4834af86b312149.md)
- [mcux\_snvs\_rtc.h](mcux__snvs__rtc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
