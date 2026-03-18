---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/rtc.html
original_path: hardware/peripherals/rtc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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

## Configuration Options

Related configuration options:

- [`CONFIG_RTC`](../../kconfig.md#CONFIG_RTC "CONFIG_RTC")
- [`CONFIG_RTC_ALARM`](../../kconfig.md#CONFIG_RTC_ALARM "CONFIG_RTC_ALARM")
- [`CONFIG_RTC_UPDATE`](../../kconfig.md#CONFIG_RTC_UPDATE "CONFIG_RTC_UPDATE")
- [`CONFIG_RTC_CALIBRATION`](../../kconfig.md#CONFIG_RTC_CALIBRATION "CONFIG_RTC_CALIBRATION")

## API Reference

*group* rtc\_interface
:   RTC Interface.

    RTC Interface Alarm

    int rtc\_alarm\_get\_supported\_fields(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t id, uint16\_t \*mask)
    :   API for getting the supported fields of the RTC alarm time.

        Note

        Bits in the mask param are defined here [RTC\_ALARM\_TIME\_MASK](#group__rtc__interface_1RTC_ALARM_TIME_MASK).

        Parameters:
        :   - **dev** – Device instance
            - **id** – Id of the alarm
            - **mask** – Mask of fields in the alarm time which are supported

        Returns:
        :   0 if successful

        Returns:
        :   -EINVAL if id is out of range or time is invalid

        Returns:
        :   -ENOTSUP if API is not supported by hardware

        Returns:
        :   -errno code if failure

    int rtc\_alarm\_set\_time(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t id, uint16\_t mask, const struct [rtc\_time](#c.rtc_time) \*timeptr)
    :   API for setting RTC alarm time.

        To enable an RTC alarm, one or more fields of the RTC alarm time must be enabled. The mask designates which fields of the RTC alarm time to enable. If the mask parameter is 0, the alarm will be disabled. The RTC alarm will trigger when all enabled fields of the alarm time match the RTC time.

        Note

        The timeptr param may be NULL if the mask param is 0

        Note

        Only the enabled fields in the timeptr param need to be configured

        Note

        Bits in the mask param are defined here [RTC\_ALARM\_TIME\_MASK](#group__rtc__interface_1RTC_ALARM_TIME_MASK)

        Parameters:
        :   - **dev** – Device instance
            - **id** – Id of the alarm
            - **mask** – Mask of fields in the alarm time to enable
            - **timeptr** – The alarm time to set

        Returns:
        :   0 if successful

        Returns:
        :   -EINVAL if id is out of range or time is invalid

        Returns:
        :   -ENOTSUP if API is not supported by hardware

        Returns:
        :   -errno code if failure

    int rtc\_alarm\_get\_time(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t id, uint16\_t \*mask, struct [rtc\_time](#c.rtc_time) \*timeptr)
    :   API for getting RTC alarm time.

        Note

        Bits in the mask param are defined here [RTC\_ALARM\_TIME\_MASK](#group__rtc__interface_1RTC_ALARM_TIME_MASK)

        Parameters:
        :   - **dev** – Device instance
            - **id** – Id of the alarm
            - **mask** – Destination for mask of fields which are enabled in the alarm time
            - **timeptr** – Destination for the alarm time

        Returns:
        :   0 if successful

        Returns:
        :   -EINVAL if id is out of range

        Returns:
        :   -ENOTSUP if API is not supported by hardware

        Returns:
        :   -errno code if failure

    int rtc\_alarm\_is\_pending(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t id)
    :   API for testing if RTC alarm is pending.

        Test whether or not the alarm with id is pending. If the alarm is pending, the pending status is cleared.

        Parameters:
        :   - **dev** – Device instance
            - **id** – Id of the alarm to test

        Returns:
        :   1 if alarm was pending

        Returns:
        :   0 if alarm was not pending

        Returns:
        :   -EINVAL if id is out of range

        Returns:
        :   -ENOTSUP if API is not supported by hardware

        Returns:
        :   -errno code if failure

    int rtc\_alarm\_set\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t id, [rtc\_alarm\_callback](#c.rtc_alarm_callback) callback, void \*user\_data)
    :   API for setting alarm callback.

        Setting the alarm callback for an alarm, will enable the alarm callback. When the callback for an alarm is enabled, the alarm triggered event will invoke the callback, after which the alarm pending status will be cleared automatically. The alarm will remain enabled until manually disabled using [rtc\_alarm\_set\_time()](#group__rtc__interface_1ga1fc9f0ec9642dfbf742ea541a20bdad5).

        To disable the alarm callback for an alarm, the `callback` and `user_data` parameters must be set to NULL. When the alarm callback for an alarm is disabled, the alarm triggered event will set the alarm status to “pending”. To check if the alarm status is “pending”, use [rtc\_alarm\_is\_pending()](#group__rtc__interface_1ga531c379c437a91df44a45e95063700e8).

        Parameters:
        :   - **dev** – Device instance
            - **id** – Id of the alarm for which the callback shall be set
            - **callback** – Callback called when alarm occurs
            - **user\_data** – Optional user data passed to callback

        Returns:
        :   0 if successful

        Returns:
        :   -EINVAL if id is out of range

        Returns:
        :   -ENOTSUP if API is not supported by hardware

        Returns:
        :   -errno code if failure

    RTC Interface Update

    int rtc\_update\_set\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [rtc\_update\_callback](#c.rtc_update_callback) callback, void \*user\_data)
    :   API for setting update callback.

        Setting the update callback will enable the update callback. The update callback will be invoked every time the RTC clock is updated by 1 second. It can be used to synchronize the RTC clock with other clock sources.

        To disable the update callback for the RTC clock, the `callback` and `user_data` parameters must be set to NULL.

        Parameters:
        :   - **dev** – Device instance
            - **callback** – Callback called when update occurs
            - **user\_data** – Optional user data passed to callback

        Returns:
        :   0 if successful

        Returns:
        :   -ENOTSUP if API is not supported by hardware

        Returns:
        :   -errno code if failure

    RTC Interface Calibration

    int rtc\_set\_calibration(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int32\_t calibration)
    :   API for setting RTC calibration.

        Calibration is applied to the RTC clock input. A positive calibration value will increase the frequency of the RTC clock, a negative value will decrease the frequency of the RTC clock.

        Parameters:
        :   - **dev** – Device instance
            - **calibration** – Calibration to set in parts per billion

        Returns:
        :   0 if successful

        Returns:
        :   -EINVAL if calibration is out of range

        Returns:
        :   -ENOTSUP if API is not supported by hardware

        Returns:
        :   -errno code if failure

    int rtc\_get\_calibration(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int32\_t \*calibration)
    :   API for getting RTC calibration.

        Parameters:
        :   - **dev** – Device instance
            - **calibration** – Destination for calibration in parts per billion

        Returns:
        :   0 if successful

        Returns:
        :   -ENOTSUP if API is not supported by hardware

        Returns:
        :   -errno code if failure

    RTC Interface Helpers

    static inline struct tm \*rtc\_time\_to\_tm(struct [rtc\_time](#c.rtc_time) \*timeptr)
    :   Convenience function for safely casting a [rtc\_time](#structrtc__time) pointer to a tm pointer.

    RTC Alarm Time Mask

    Mask for alarm time fields to enable when setting alarm time

    RTC\_ALARM\_TIME\_MASK\_SECOND

    RTC\_ALARM\_TIME\_MASK\_MINUTE

    RTC\_ALARM\_TIME\_MASK\_HOUR

    RTC\_ALARM\_TIME\_MASK\_MONTHDAY

    RTC\_ALARM\_TIME\_MASK\_MONTH

    RTC\_ALARM\_TIME\_MASK\_YEAR

    RTC\_ALARM\_TIME\_MASK\_WEEKDAY

    RTC\_ALARM\_TIME\_MASK\_YEARDAY

    RTC\_ALARM\_TIME\_MASK\_NSEC

    Typedefs

    typedef void (\*rtc\_update\_callback)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, void \*user\_data)
    :   RTC update event callback.

        Param dev:
        :   Device instance invoking the handler

        Param user\_data:
        :   Optional user data provided when update irq callback is set

    typedef void (\*rtc\_alarm\_callback)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t id, void \*user\_data)
    :   RTC alarm triggered callback.

        Param dev:
        :   Device instance invoking the handler

        Param id:
        :   Alarm id

        Param user\_data:
        :   Optional user data passed with the alarm configuration

    Functions

    int rtc\_set\_time(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [rtc\_time](#c.rtc_time) \*timeptr)
    :   API for setting RTC time.

        Parameters:
        :   - **dev** – Device instance
            - **timeptr** – The time to set

        Returns:
        :   0 if successful

        Returns:
        :   -EINVAL if RTC time is invalid or exceeds hardware capabilities

        Returns:
        :   -errno code if failure

    int rtc\_get\_time(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [rtc\_time](#c.rtc_time) \*timeptr)
    :   API for getting RTC time.

        Parameters:
        :   - **dev** – Device instance
            - **timeptr** – Destination for the time

        Returns:
        :   0 if successful

        Returns:
        :   -ENODATA if RTC time has not been set

        Returns:
        :   -errno code if failure

    struct rtc\_time
    :   *#include <rtc.h>*

        Structure for storing date and time values with sub-second precision.

        The structure is 1-1 mapped to the struct tm for the members `tm_sec` to `tm_isdst` making it compatible with the standard time library.

        Note

        Use [rtc\_time\_to\_tm()](#group__rtc__interface_1gac2bb774a4b512f76c35a0a6723a7c807) to safely cast from a [rtc\_time](#structrtc__time) pointer to a tm pointer.

        Public Members

        int tm\_sec
        :   Seconds [0, 59].

        int tm\_min
        :   Minutes [0, 59].

        int tm\_hour
        :   Hours [0, 23].

        int tm\_mday
        :   Day of the month [1, 31].

        int tm\_mon
        :   Month [0, 11].

        int tm\_year
        :   Year - 1900.

        int tm\_wday
        :   Day of the week [0, 6] (Sunday = 0) (Unknown = -1).

        int tm\_yday
        :   Day of the year [0, 365] (Unknown = -1).

        int tm\_isdst
        :   Daylight saving time flag [-1] (Unknown = -1).

        int tm\_nsec
        :   Nanoseconds [0, 999999999] (Unknown = 0).

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
the time using [`rtc_get_time()`](#c.rtc_get_time) will return `-ENODATA`, until the time is
set using [`rtc_set_time()`](#c.rtc_set_time). The RTC will then behave as a real RTC, until the
application is reset.

The emulated RTC device driver is built for the compatible
[`zephyr,rtc-emul`](../../build/dts/api/bindings/rtc/zephyr%2Crtc-emul.md#std-dtcompatible-zephyr-rtc-emul) and will be included if [`CONFIG_RTC`](../../kconfig.md#CONFIG_RTC "CONFIG_RTC")
is selected.
