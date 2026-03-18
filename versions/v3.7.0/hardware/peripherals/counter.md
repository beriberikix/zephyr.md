---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/counter.html
original_path: hardware/peripherals/counter.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Counter

## Overview

## API Reference

Related code samples

[Counter Alarm](../../samples/drivers/counter/alarm/README.md#alarm "Implement an alarm application using the counter API.")
:   Implement an alarm application using the counter API.

[DS3231 TCXO RTC](../../samples/drivers/counter/maxim_ds3231/README.md#ds3231 "Interact with a DS3231 real-time clock using the counter API and dedicated driver API.")
:   Interact with a DS3231 real-time clock using the counter API and dedicated driver API.

*group* Counter Interface
:   Counter Interface.

    **Since**
    :   1.14

    **Version**
    :   0.8.0

    Counter device capabilities

    COUNTER\_CONFIG\_INFO\_COUNT\_UP
    :   Counter count up flag.

    Flags used by counter\_top\_cfg.

    COUNTER\_TOP\_CFG\_DONT\_RESET
    :   Flag preventing counter reset when top value is changed.

        If flags is set then counter is free running while top value is updated, otherwise counter is reset (see [counter\_set\_top\_value()](#group__counter__interface_1ga2d92f5564cdd1ecc56029c3a45e666f0)).

    COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE
    :   Flag instructing counter to reset itself if changing top value results in counter going out of new top value bound.

        See [COUNTER\_TOP\_CFG\_DONT\_RESET](#group__counter__interface_1ga9a30c647361912c2ce8e0566cf53dea7).

    Alarm configuration flags

    Used in alarm configuration structure ([counter\_alarm\_cfg](#structcounter__alarm__cfg)).

    COUNTER\_ALARM\_CFG\_ABSOLUTE
    :   Counter alarm absolute value flag.

        Ticks relation to counter value. If set ticks are treated as absolute value, else it is relative to the counter reading performed during the call.

    COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE
    :   Alarm flag enabling immediate expiration when driver detects that absolute alarm was set too late.

        Alarm callback must be called from the same context as if it was set on time.

    Counter guard period flags

    Used by [counter\_set\_guard\_period](#group__counter__interface_1gab6851411dabf191d3391715d632111b0) and [counter\_get\_guard\_period](#group__counter__interface_1ga55a101d237c8472ad5cacf65363c536f).

    COUNTER\_GUARD\_PERIOD\_LATE\_TO\_SET
    :   Identifies guard period needed for detection of late setting of absolute alarm (see [counter\_set\_channel\_alarm](#group__counter__interface_1ga00a2857d993a84a56e8e222727f3d85e)).

    Typedefs

    typedef void (\*counter\_alarm\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t chan\_id, uint32\_t ticks, void \*user\_data)
    :   Alarm callback.

        Param dev:
        :   Pointer to the device structure for the driver instance.

        Param chan\_id:
        :   Channel ID.

        Param ticks:
        :   Counter value that triggered the alarm.

        Param user\_data:
        :   User data.

    typedef void (\*counter\_top\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, void \*user\_data)
    :   Callback called when counter turns around.

        Param dev:
        :   Pointer to the device structure for the driver instance.

        Param user\_data:
        :   User data provided in [counter\_set\_top\_value](#group__counter__interface_1ga2d92f5564cdd1ecc56029c3a45e666f0).

    typedef int (\*counter\_api\_start)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)

    typedef int (\*counter\_api\_stop)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)

    typedef int (\*counter\_api\_get\_value)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*ticks)

    typedef int (\*counter\_api\_get\_value\_64)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t \*ticks)

    typedef int (\*counter\_api\_set\_alarm)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t chan\_id, const struct [counter\_alarm\_cfg](#c.counter_alarm_cfg) \*alarm\_cfg)

    typedef int (\*counter\_api\_cancel\_alarm)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t chan\_id)

    typedef int (\*counter\_api\_set\_top\_value)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [counter\_top\_cfg](#c.counter_top_cfg) \*cfg)

    typedef uint32\_t (\*counter\_api\_get\_pending\_int)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)

    typedef uint32\_t (\*counter\_api\_get\_top\_value)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)

    typedef uint32\_t (\*counter\_api\_get\_guard\_period)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t flags)

    typedef int (\*counter\_api\_set\_guard\_period)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t ticks, uint32\_t flags)

    typedef uint32\_t (\*counter\_api\_get\_freq)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)

    Functions

    bool counter\_is\_counting\_up(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Function to check if counter is counting up.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the driver instance.

        Return values:
        :   - **true** – if counter is counting up.
            - **false** – if counter is counting down.

    uint8\_t counter\_get\_num\_of\_channels(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Function to get number of alarm channels.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the driver instance.

        Returns:
        :   Number of alarm channels.

    uint32\_t counter\_get\_frequency(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Function to get counter frequency.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the driver instance.

        Returns:
        :   Frequency of the counter in Hz, or zero if the counter does not have a fixed frequency.

    uint32\_t counter\_us\_to\_ticks(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t us)
    :   Function to convert microseconds to ticks.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the driver instance.
            - **us** – **[in]** Microseconds.

        Returns:
        :   Converted ticks. Ticks will be saturated if exceed 32 bits.

    uint64\_t counter\_ticks\_to\_us(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t ticks)
    :   Function to convert ticks to microseconds.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the driver instance.
            - **ticks** – **[in]** Ticks.

        Returns:
        :   Converted microseconds.

    uint32\_t counter\_get\_max\_top\_value(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Function to retrieve maximum top value that can be set.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the driver instance.

        Returns:
        :   Max top value.

    int counter\_start(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Start counter device in free running mode.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int counter\_stop(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Stop counter device.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if the device doesn’t support stopping the counter.

    int counter\_get\_value(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*ticks)
    :   Get current counter value.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ticks** – Pointer to where to store the current counter value

        Return values:
        :   - **0** – If successful.
            - **Negative** – error code on failure getting the counter value

    int counter\_get\_value\_64(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t \*ticks)
    :   Get current counter 64-bit value.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ticks** – Pointer to where to store the current counter value

        Return values:
        :   - **0** – If successful.
            - **Negative** – error code on failure getting the counter value

    int counter\_set\_channel\_alarm(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t chan\_id, const struct [counter\_alarm\_cfg](#c.counter_alarm_cfg) \*alarm\_cfg)
    :   Set a single shot alarm on a channel.

        After expiration alarm can be set again, disabling is not needed. When alarm expiration handler is called, channel is considered available and can be set again in that context.

        Note

        API is not thread safe.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **chan\_id** – Channel ID.
            - **alarm\_cfg** – Alarm configuration.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if request is not supported (device does not support interrupts or requested channel).
            - **-EINVAL** – if alarm settings are invalid.
            - **-ETIME** – if absolute alarm was set too late.
            - **-EBUSY** – if alarm is already active.

    int counter\_cancel\_channel\_alarm(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t chan\_id)
    :   Cancel an alarm on a channel.

        Note

        API is not thread safe.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **chan\_id** – Channel ID.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if request is not supported or the counter was not started yet.

    int counter\_set\_top\_value(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [counter\_top\_cfg](#c.counter_top_cfg) \*cfg)
    :   Set counter top value.

        Function sets top value and optionally resets the counter to 0 or top value depending on counter direction. On turnaround, counter can be reset and optional callback is periodically called. Top value can only be changed when there is no active channel alarm.

        [COUNTER\_TOP\_CFG\_DONT\_RESET](#group__counter__interface_1ga9a30c647361912c2ce8e0566cf53dea7) prevents counter reset. When counter is running while top value is updated, it is possible that counter progresses outside the new top value. In that case, error is returned and optionally driver can reset the counter (see [COUNTER\_TOP\_CFG\_RESET\_WHEN\_LATE](#group__counter__interface_1ga45562a4ddd743f74213a03d83a774b11)).

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **cfg** – Configuration. Cannot be NULL.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if request is not supported (e.g. top value cannot be changed or counter cannot/must be reset during top value update).
            - **-EBUSY** – if any alarm is active.
            - **-ETIME** – if [COUNTER\_TOP\_CFG\_DONT\_RESET](#group__counter__interface_1ga9a30c647361912c2ce8e0566cf53dea7) was set and new top value is smaller than current counter value (counter counting up).

    int counter\_get\_pending\_int(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Function to get pending interrupts.

        The purpose of this function is to return the interrupt status register for the device. This is especially useful when waking up from low power states to check the wake up source.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **1** – if any counter interrupt is pending.
            - **0** – if no counter interrupt is pending.

    uint32\_t counter\_get\_top\_value(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Function to retrieve current top value.

        Parameters:
        :   - **dev** – **[in]** Pointer to the device structure for the driver instance.

        Returns:
        :   Top value.

    int counter\_set\_guard\_period(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t ticks, uint32\_t flags)
    :   Set guard period in counter ticks.

        When setting an absolute alarm value close to the current counter value there is a risk that the counter will have counted past the given absolute value before the driver manages to activate the alarm. If this would go unnoticed then the alarm would only expire after the timer has wrapped and reached the given absolute value again after a full timer period. This could take a long time in case of a 32 bit timer. Setting a sufficiently large guard period will help the driver detect unambiguously whether it is late or not.

        The guard period should be as many counter ticks as the driver will need at most to actually activate the alarm after the driver API has been called. If the driver finds that the counter has just passed beyond the given absolute tick value but is still close enough to fall within the guard period, it will assume that it is “late”, i.e. that the intended expiry time has already passed. Depending on the [COUNTER\_ALARM\_CFG\_EXPIRE\_WHEN\_LATE](#group__counter__interface_1ga87dffd2a1cadedfc30e7d39af547c336) flag the driver will either ignore the alarm or expire it immediately in such a case.

        If, however, the counter is past the given absolute tick value but outside the guard period, then the driver will assume that this is intentional and let the counter wrap around to/from zero before it expires.

        More precisely:

        - When counting upwards (see [COUNTER\_CONFIG\_INFO\_COUNT\_UP](#group__counter__interface_1ga8fa40ff6404936e5b05bb9c67871f70c)) the given absolute tick value must be above (now + guard\_period) % top\_value to be accepted by the driver.
        - When counting downwards, the given absolute tick value must be less than (now + top\_value - guard\_period) % top\_value to be accepted.

        Examples:

        - counting upwards, now = 4950, top value = 5000, guard period = 100: absolute tick value >= (4950 + 100) % 5000 = 50
        - counting downwards, now = 50, top value = 5000, guard period = 100: absolute tick value <= (50 + 5000 - \* 100) % 5000 = 4950

        If you need only short alarm periods, you can set the guard period very high (e.g. half of the counter top value) which will make it highly unlikely that the counter will ever unintentionally wrap.

        The guard period is set to 0 on initialization (no protection).

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ticks** – Guard period in counter ticks.
            - **flags** – See [COUNTER\_GUARD\_PERIOD\_FLAGS](#group__counter__interface_1COUNTER_GUARD_PERIOD_FLAGS).

        Return values:
        :   - **0** – if successful.
            - **-ENOTSUP** – if function or flags are not supported.
            - **-EINVAL** – if ticks value is invalid.

    uint32\_t counter\_get\_guard\_period(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t flags)
    :   Return guard period.

        See also

        [counter\_set\_guard\_period](#group__counter__interface_1gab6851411dabf191d3391715d632111b0).

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **flags** – See [COUNTER\_GUARD\_PERIOD\_FLAGS](#group__counter__interface_1COUNTER_GUARD_PERIOD_FLAGS).

        Returns:
        :   Guard period given in counter ticks or 0 if function or flags are not supported.

    struct counter\_alarm\_cfg
    :   *#include <counter.h>*

        Alarm callback structure.

        Public Members

        [counter\_alarm\_callback\_t](#c.counter_alarm_callback_t) callback
        :   Callback called on alarm (cannot be NULL).

        uint32\_t ticks
        :   Number of ticks that triggers the alarm.

            It can be relative (to now) or an absolute value (see [COUNTER\_ALARM\_CFG\_ABSOLUTE](#group__counter__interface_1ga4842d212424f92c5a3b39116ec6c2fd2)). Both, relative and absolute, alarm values can be any value between zero and the current top value (see [counter\_get\_top\_value](#group__counter__interface_1ga13d14903a03ab10062002a81b8302424)). When setting an absolute alarm value close to the current counter value there is a risk that the counter will have counted past the given absolute value before the driver manages to activate the alarm. Therefore a guard period can be defined that lets the driver decide unambiguously whether it is late or not (see [counter\_set\_guard\_period](#group__counter__interface_1gab6851411dabf191d3391715d632111b0)). If the counter is clock driven then ticks can be converted to microseconds (see [counter\_ticks\_to\_us](#group__counter__interface_1ga9fbcb710091084e638c45f62c25d954c)). Alternatively, the counter implementation may count asynchronous events.

        void \*user\_data
        :   User data returned in callback.

        uint32\_t flags
        :   Alarm flags (see [COUNTER\_ALARM\_FLAGS](#group__counter__interface_1COUNTER_ALARM_FLAGS)).

    struct counter\_top\_cfg
    :   *#include <counter.h>*

        Top value configuration structure.

        Public Members

        uint32\_t ticks
        :   Top value.

        [counter\_top\_callback\_t](#c.counter_top_callback_t) callback
        :   Callback function (can be NULL).

        void \*user\_data
        :   User data passed to callback function (not valid if callback is NULL).

        uint32\_t flags
        :   Flags (see [COUNTER\_TOP\_FLAGS](#group__counter__interface_1COUNTER_TOP_FLAGS)).

    struct counter\_config\_info
    :   *#include <counter.h>*

        Structure with generic counter features.

        Public Members

        uint32\_t max\_top\_value
        :   Maximal (default) top value on which counter is reset (cleared or reloaded).

        uint32\_t freq
        :   Frequency of the source clock if synchronous events are counted.

        uint8\_t flags
        :   Flags (see [COUNTER\_FLAGS](#group__counter__interface_1COUNTER_FLAGS)).

        uint8\_t channels
        :   Number of channels that can be used for setting alarm.

            See also

            [counter\_set\_channel\_alarm](#group__counter__interface_1ga00a2857d993a84a56e8e222727f3d85e)

    struct counter\_driver\_api
    :   *#include <counter.h>*
