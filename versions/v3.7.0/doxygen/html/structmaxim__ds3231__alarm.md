---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmaxim__ds3231__alarm.html
original_path: doxygen/html/structmaxim__ds3231__alarm.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

maxim\_ds3231\_alarm Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [RTC DS3231 Interface](group__rtc__ds3231__interface.md)

Information defining the alarm configuration.
[More...](#details)

`#include <[maxim_ds3231.h](maxim__ds3231_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) | [time](#a363a2dc65517c3d00de7658ce421937f) |
|  | Time specification for an RTC alarm. |
| [maxim\_ds3231\_alarm\_callback\_handler\_t](group__rtc__ds3231__interface.md#ga684b29dc1c11d8df698437f27e6d0403) | [handler](#a9628b99ed059a64f25143291c0df1c8c) |
|  | Handler to be invoked when alarms are signalled. |
| void \* | [user\_data](#a192fb8c10246bfe466e74aafbb45d720) |
|  | User-provided pointer passed to alarm callback. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a98ebc645761cc0d035e269fa8d3f9c68) |
|  | Flags controlling configuration of the alarm alarm. |

## Detailed Description

Information defining the alarm configuration.

DS3231 alarms can be set to fire at specific times or at the rollover of minute, hour, day, or day of week.

When an alarm is configured with a handler an interrupt will be generated and the handler called from the system work queue.

When an alarm is configured without a handler, or a persisted alarm is present, alarms can be read using [maxim\_ds3231\_check\_alarms()](group__rtc__ds3231__interface.md#gab2091298eb9b94da29ad79616b707bad "Check for and clear flags indicating that an alarm has fired.").

## Field Documentation

## [◆ ](#a98ebc645761cc0d035e269fa8d3f9c68)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) maxim\_ds3231\_alarm::flags |
| --- |

Flags controlling configuration of the alarm alarm.

See MAXIM\_DS3231\_ALARM\_FLAGS\_IGNSE and related constants.

Note that as described the alarm mask fields require that if a unit is not ignored, higher-precision units must also not be ignored. For example, if match on hours is enabled, match on minutes and seconds must also be enabled. Failure to comply with this requirement will cause [maxim\_ds3231\_set\_alarm()](group__rtc__ds3231__interface.md#ga8f876ad2e16e88d80a2f914be3df49b1 "Configure a DS3231 alarm.") to return an error, leaving the alarm configuration unchanged.

## [◆ ](#a9628b99ed059a64f25143291c0df1c8c)handler

| [maxim\_ds3231\_alarm\_callback\_handler\_t](group__rtc__ds3231__interface.md#ga684b29dc1c11d8df698437f27e6d0403) maxim\_ds3231\_alarm::handler |
| --- |

Handler to be invoked when alarms are signalled.

If this is null the alarm will not be triggered by the INTn/SQW GPIO. This is a "persisted" alarm from its role in using the DS3231 to trigger a wake from deep sleep. The application should use [maxim\_ds3231\_check\_alarms()](group__rtc__ds3231__interface.md#gab2091298eb9b94da29ad79616b707bad "Check for and clear flags indicating that an alarm has fired.") to determine whether such an alarm has been triggered.

If this is not null the driver will monitor the ISW GPIO for alarm signals and will invoke the handler with a parameter carrying the value returned by [maxim\_ds3231\_check\_alarms()](group__rtc__ds3231__interface.md#gab2091298eb9b94da29ad79616b707bad "Check for and clear flags indicating that an alarm has fired."). The corresponding status flags will be cleared in the device before the handler is invoked.

The handler will be invoked from the system work queue.

## [◆ ](#a363a2dc65517c3d00de7658ce421937f)time

| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) maxim\_ds3231\_alarm::time |
| --- |

Time specification for an RTC alarm.

Though specified as a UNIX time, the alarm parameters are determined by converting to civil time and interpreting the component hours, minutes, seconds, day-of-week, and day-of-month fields, mediated by the corresponding [flags](#a98ebc645761cc0d035e269fa8d3f9c68).

The year and month are ignored, but be aware that [gmtime()](lib_2libc_2minimal_2include_2time_8h.md#a4bc4ff58d4ac838a36ba939747e5833e) determines day-of-week based on calendar date. Decoded alarm times will fall within 1978-01 since 1978-01-01 (first of month) was a Sunday (first of week).

## [◆ ](#a192fb8c10246bfe466e74aafbb45d720)user\_data

| void\* maxim\_ds3231\_alarm::user\_data |
| --- |

User-provided pointer passed to alarm callback.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/rtc/[maxim\_ds3231.h](maxim__ds3231_8h_source.md)

- [maxim\_ds3231\_alarm](structmaxim__ds3231__alarm.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
