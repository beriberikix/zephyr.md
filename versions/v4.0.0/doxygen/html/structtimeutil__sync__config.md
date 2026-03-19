---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structtimeutil__sync__config.html
original_path: doxygen/html/structtimeutil__sync__config.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timeutil\_sync\_config Struct Reference

[Utilities](group__utilities.md) » [Time Utility APIs](group__timeutil__apis.md) » [Time Synchronization APIs](group__timeutil__sync__apis.md)

Immutable state for synchronizing two clocks.
[More...](#details)

`#include <[timeutil.h](timeutil_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ref\_Hz](#a0ee43492ae85a6305a326046501a8ac7) |
|  | The nominal instance counter rate in Hz. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [local\_Hz](#a4c180ceb790108292c8c7a825792603f) |
|  | The nominal local counter rate in Hz. |

## Detailed Description

Immutable state for synchronizing two clocks.

Values required to convert durations between two time scales.

Note
:   The accuracy of the translation and calculated skew between sources depends on the resolution of these frequencies. A reference frequency with microsecond or nanosecond resolution would produce the most accurate tracking when the local reference is the Zephyr tick counter. A reference source like an RTC chip with 1 Hz resolution requires a much larger interval between sampled instants to detect relative clock drift.

## Field Documentation

## [◆ ](#a4c180ceb790108292c8c7a825792603f)local\_Hz

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeutil\_sync\_config::local\_Hz |
| --- |

The nominal local counter rate in Hz.

This value is assumed to be inaccurate but reasonably stable. For a local clock driven by a crystal oscillator an error of 25 ppm is common; for an RC oscillator larger errors should be expected. The timeutil\_sync infrastructure can calculate the skew between the local and reference clocks and apply it when converting between time scales.

The value must be positive.

## [◆ ](#a0ee43492ae85a6305a326046501a8ac7)ref\_Hz

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeutil\_sync\_config::ref\_Hz |
| --- |

The nominal instance counter rate in Hz.

This value is assumed to be precise, but may drift depending on the reference clock source.

The value must be positive.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[timeutil.h](timeutil_8h_source.md)

- [timeutil\_sync\_config](structtimeutil__sync__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
