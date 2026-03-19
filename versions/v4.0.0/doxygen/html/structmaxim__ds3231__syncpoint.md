---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmaxim__ds3231__syncpoint.html
original_path: doxygen/html/structmaxim__ds3231__syncpoint.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

maxim\_ds3231\_syncpoint Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [RTC DS3231 Interface](group__rtc__ds3231__interface.md)

Register the RTC clock against system clocks.
[More...](#details)

`#include <[maxim_ds3231.h](maxim__ds3231_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [timespec](structtimespec.md) | [rtc](#aff4219f350140cb6a53e73bb91815452) |
|  | Time from the DS3231. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [syncclock](#adb649c698084d6dbb83915aa6e6079b8) |
|  | Value of a local clock at the same instant as [rtc](#aff4219f350140cb6a53e73bb91815452). |

## Detailed Description

Register the RTC clock against system clocks.

This captures the same instant in both the RTC time scale and a stable system clock scale, allowing conversion between those scales.

## Field Documentation

## [◆ ](#aff4219f350140cb6a53e73bb91815452)rtc

| struct [timespec](structtimespec.md) maxim\_ds3231\_syncpoint::rtc |
| --- |

Time from the DS3231.

This maybe in UTC, TAI, or local offset depending on how the RTC is maintained.

## [◆ ](#adb649c698084d6dbb83915aa6e6079b8)syncclock

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) maxim\_ds3231\_syncpoint::syncclock |
| --- |

Value of a local clock at the same instant as [rtc](#aff4219f350140cb6a53e73bb91815452).

This is captured from a stable monotonic system clock running at between 1 kHz and 1 MHz, allowing for microsecond to millisecond accuracy in synchronization.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/rtc/[maxim\_ds3231.h](maxim__ds3231_8h_source.md)

- [maxim\_ds3231\_syncpoint](structmaxim__ds3231__syncpoint.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
