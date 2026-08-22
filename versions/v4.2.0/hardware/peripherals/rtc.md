---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/hardware/peripherals/rtc.html
original_path: hardware/peripherals/rtc.html
---

# Real-Time Clock (RTC)

## Overview

**Glossary**

| Word | Definition |
| --- | --- |
| Real-time clock | Low power device tracking time using broken-down time |
| Real-time counter | Low power counter which can be used to track time |
| RTC | Acronym for real-time clock |

An RTC is a low power device which tracks time using broken-down time.
It should not be confused with low-power counters which sometimes share
the same name, acronym, or both.

RTCs are usually optimized for low energy consumption and are usually
kept running even when the system is in a low power state.

RTCs usually contain one or more alarms which can be configured to
trigger at a given time. These alarms are commonly used to wake up the
system from a low power state.

## Devicetree bindings

RTC bindings must include the `rtc-device.yaml` binding, which
includes the `base.yaml` binding and the required `alarms-count`
property.

```yaml
include: rtc-device.yaml
```

## Device driver design

### Driver init

RTCs are never powered off by the system. On init, drivers should
expect the RTC is either:

- Powered, configured, and running.
- Powered, unconfigured, and stopped.

On init, drivers shall ensure the RTC is configured correctly, while
preserving the time, alarms, and running status.

Time is set by calling [`rtc_set_time()`](../../doxygen/html/group__rtc__interface.md#ga52982b434c740e86aa5f3e35e9bee4a7), at which point the
RTC will start running. Alarms pending status is cleared by
[`rtc_alarm_is_pending()`](../../doxygen/html/group__rtc__interface.md#ga531c379c437a91df44a45e95063700e8) or by an alarm callback resulting
from [`rtc_alarm_set_callback()`](../../doxygen/html/group__rtc__interface.md#ga90d7f422ca15cf679aa7ba61fb5373f0).

### GPIO routed interrupts

RTCs with connected interrupt output pins shall configure and enable
them on init. The host may enable and disable interrupts for its
GPIOs, but RTC interrupt output pins must remain enabled.

This ensures consistent behavior between internally and externally
connected RTCs, and allows for system wakeup through GPIO on any
enabled RTC event like alarms or update.

Note

RTCs with unconnected interrupt output pins are not allowed to
periodically poll the RTC to emulate it being connected.
[`rtc_alarm_set_callback()`](../../doxygen/html/group__rtc__interface.md#ga90d7f422ca15cf679aa7ba61fb5373f0) and
[`rtc_update_set_callback()`](../../doxygen/html/group__rtc__interface.md#ga0b2b2b44077dcdb73feb007f87cc47b3) shall return `-ENOTSUP` in
this case.

### Clock output

If supported, the clock output configuration is defined in the
devicetree. The output is configured by the driver on init.

## Configuration Options

Related configuration options:

- [`CONFIG_RTC`](../../kconfig.md#CONFIG_RTC "CONFIG_RTC")
- [`CONFIG_RTC_ALARM`](../../kconfig.md#CONFIG_RTC_ALARM "CONFIG_RTC_ALARM")
- [`CONFIG_RTC_UPDATE`](../../kconfig.md#CONFIG_RTC_UPDATE "CONFIG_RTC_UPDATE")
- [`CONFIG_RTC_CALIBRATION`](../../kconfig.md#CONFIG_RTC_CALIBRATION "CONFIG_RTC_CALIBRATION")

## API Reference

[RTC Interface](../../doxygen/html/group__rtc__interface.md)

Related code samples

- [Real-Time Clock (RTC)](../../samples/drivers/rtc/README.md#rtc "Set and read the date/time from a Real-Time Clock.")Set and read the date/time from a Real-Time Clock.

## RTC device driver test suite

The test suite validates the behavior of the RTC device driver. It
is designed to be portable between boards. It uses the device tree
alias `rtc` to designate the RTC device to test.

This test suite tests the following:

- Setting and getting the time.
- RTC Time incrementing correctly.
- Alarms if supported by hardware, with and without callback enabled
- Calibration if supported by hardware.

The calibration test tests a range of values which are printed to the
console to be manually compared. The user must review the set and
gotten values to ensure they are valid.

By default, only the mandatory setting and getting of time is enabled
for testing. To test the optional alarms, update event callback
and clock calibration, these must be enabled by selecting
[`CONFIG_RTC_ALARM`](../../kconfig.md#CONFIG_RTC_ALARM "CONFIG_RTC_ALARM"), [`CONFIG_RTC_UPDATE`](../../kconfig.md#CONFIG_RTC_UPDATE "CONFIG_RTC_UPDATE")
and [`CONFIG_RTC_CALIBRATION`](../../kconfig.md#CONFIG_RTC_CALIBRATION "CONFIG_RTC_CALIBRATION").

The following examples build the test suite for the `native_sim`
board. To build the test suite for a different board, replace the
`native_sim` board with your board.

To build the test application with the default configuration, testing
only the mandatory features, the following command can be used for
reference:

```shell
# From the root of the zephyr repository
west build -b native_sim tests/drivers/rtc/rtc_api
```

To build the test with additional RTC features enabled, use menuconfig
to enable the additional features by updating the configuration. The
following command can be used for reference:

```shell
# From the root of the zephyr repository
west build -b native_sim tests/drivers/rtc/rtc_api
west build -t menuconfig
```

Then build the test application using the following command:

```shell
# From the root of the zephyr repository
west build -b native_sim tests/drivers/rtc/rtc_api
```

To run the test suite, flash and run the application on your board, the output will
be printed to the console.

Note

The tests take up to 30 seconds each if they are testing real hardware.

## RTC emulated device

The emulated RTC device fully implements the RTC API, and will behave like a real
RTC device, with the following limitations:

- RTC time is not persistent across application initialization.
- RTC alarms are not persistent across application initialization.
- RTC time will drift over time.

Every time an application is initialized, the RTC’s time and alarms are reset. Reading
the time using [`rtc_get_time()`](../../doxygen/html/group__rtc__interface.md#ga208321104a1cdb39173317e6911aea87) will return `-ENODATA`, until the time is
set using [`rtc_set_time()`](../../doxygen/html/group__rtc__interface.md#ga52982b434c740e86aa5f3e35e9bee4a7). The RTC will then behave as a real RTC, until the
application is reset.

The emulated RTC device driver is built for the compatible
[`zephyr,rtc-emul`](../../build/dts/api/bindings/rtc/zephyr%2Crtc-emul.md#std-dtcompatible-zephyr-rtc-emul) and will be included if [`CONFIG_RTC`](../../kconfig.md#CONFIG_RTC "CONFIG_RTC")
is selected.

## History of RTCs in Zephyr

RTCs have been supported before this API was created, using the
[Counter](counter.md#counter-api) API. The unix timestamp was used to convert
between broken-down time and the unix timestamp within the RTC
drivers, which internally used the broken-down time representation.

The disadvantages of this approach were that hardware counters could
not be set to a specific count, requiring all RTCs to use device
specific APIs to set the time, converting from unix time to
broken-down time, unnecessarily in some cases, and some common
features missing, like input clock calibration and the update
callback.
