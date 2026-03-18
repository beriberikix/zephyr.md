---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/clock_control.html
original_path: hardware/peripherals/clock_control.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Clock Control

## Overview

The clock control API provides access to clocks in the system, including the
ability to turn them on and off.

## Configuration Options

Related configuration options:

- [`CONFIG_CLOCK_CONTROL`](../../kconfig.md#CONFIG_CLOCK_CONTROL "CONFIG_CLOCK_CONTROL")

## API Reference

Related code samples

[LiteX clock control driver](../../samples/drivers/clock_control_litex/README.md#clock-control-litex "Use LiteX clock control driver to generate multiple clock signals.")
:   Use LiteX clock control driver to generate multiple clock signals.

*group* clock\_control\_interface
:   Clock Control Interface.

    Defines

    CLOCK\_CONTROL\_SUBSYS\_ALL

    Typedefs

    typedef void \*clock\_control\_subsys\_t
    :   [clock\_control\_subsys\_t](#group__clock__control__interface_1gaa7d3935eaaf18902801a7d94859483db) is a type to identify a clock controller sub-system.

        Such data pointed is opaque and relevant only to the clock controller driver instance being used.

    typedef void \*clock\_control\_subsys\_rate\_t
    :   [clock\_control\_subsys\_rate\_t](#group__clock__control__interface_1ga05d8b476ef0331e1502702921d2801f1) is a type to identify a clock controller sub-system rate.

        Such data pointed is opaque and relevant only to set the clock controller rate of the driver instance being used.

    typedef void (\*clock\_control\_cb\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) subsys, void \*user\_data)
    :   Callback called on clock started.

        Param dev:
        :   Device structure whose driver controls the clock.

        Param subsys:
        :   Opaque data representing the clock.

        Param user\_data:
        :   User data.

    typedef int (\*clock\_control)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys)

    typedef int (\*clock\_control\_get)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys, uint32\_t \*rate)

    typedef int (\*clock\_control\_async\_on\_fn)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys, [clock\_control\_cb\_t](#c.clock_control_cb_t) cb, void \*user\_data)

    typedef enum [clock\_control\_status](#c.clock_control_status) (\*clock\_control\_get\_status\_fn)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys)

    typedef int (\*clock\_control\_set)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys, [clock\_control\_subsys\_rate\_t](#c.clock_control_subsys_rate_t) rate)

    typedef int (\*clock\_control\_configure\_fn)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys, void \*data)

    Enums

    enum clock\_control\_status
    :   Current clock status.

        *Values:*

        enumerator CLOCK\_CONTROL\_STATUS\_STARTING

        enumerator CLOCK\_CONTROL\_STATUS\_OFF

        enumerator CLOCK\_CONTROL\_STATUS\_ON

        enumerator CLOCK\_CONTROL\_STATUS\_UNKNOWN

    Functions

    static inline int clock\_control\_on(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys)
    :   Enable a clock controlled by the device.

        On success, the clock is enabled and ready when this function returns. This function may sleep, and thus can only be called from thread context.

        Use [clock\_control\_async\_on()](#group__clock__control__interface_1ga03cedb9723e001d01c495f0abb6acfdf) for non-blocking operation.

        Parameters:
        :   - **dev** – Device structure whose driver controls the clock.
            - **sys** – Opaque data representing the clock.

        Returns:
        :   0 on success, negative errno on failure.

    static inline int clock\_control\_off(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys)
    :   Disable a clock controlled by the device.

        This function is non-blocking and can be called from any context. On success, the clock is disabled when this function returns.

        Parameters:
        :   - **dev** – Device structure whose driver controls the clock
            - **sys** – Opaque data representing the clock

        Returns:
        :   0 on success, negative errno on failure.

    static inline int clock\_control\_async\_on(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys, [clock\_control\_cb\_t](#c.clock_control_cb_t) cb, void \*user\_data)
    :   Request clock to start with notification when clock has been started.

        Function is non-blocking and can be called from any context. User callback is called when clock is started.

        Parameters:
        :   - **dev** – Device.
            - **sys** – A pointer to an opaque data representing the sub-system.
            - **cb** – Callback.
            - **user\_data** – User context passed to the callback.

        Return values:
        :   - **0** – if start is successfully initiated.
            - **-EALREADY** – if clock was already started and is starting or running.
            - **-ENOTSUP** – If the requested mode of operation is not supported.
            - **-ENOSYS** – if the interface is not implemented.
            - **other** – negative errno on vendor specific error.

    static inline enum [clock\_control\_status](#c.clock_control_status) clock\_control\_get\_status(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys)
    :   Get clock status.

        Parameters:
        :   - **dev** – Device.
            - **sys** – A pointer to an opaque data representing the sub-system.

        Returns:
        :   Status.

    static inline int clock\_control\_get\_rate(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys, uint32\_t \*rate)
    :   Obtain the clock rate of given sub-system.

        Parameters:
        :   - **dev** – Pointer to the device structure for the clock controller driver instance
            - **sys** – A pointer to an opaque data representing the sub-system
            - **rate** – **[out]** Subsystem clock rate

        Return values:
        :   - **0** – on successful rate reading.
            - **-EAGAIN** – if rate cannot be read. Some drivers do not support returning the rate when the clock is off.
            - **-ENOTSUP** – if reading the clock rate is not supported for the given sub-system.
            - **-ENOSYS** – if the interface is not implemented.

    static inline int clock\_control\_set\_rate(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys, [clock\_control\_subsys\_rate\_t](#c.clock_control_subsys_rate_t) rate)
    :   Set the rate of the clock controlled by the device.

        On success, the new clock rate is set and ready when this function returns. This function may sleep, and thus can only be called from thread context.

        Parameters:
        :   - **dev** – Device structure whose driver controls the clock.
            - **sys** – Opaque data representing the clock.
            - **rate** – Opaque data representing the clock rate to be used.

        Return values:
        :   - **-EALREADY** – if clock was already in the given rate.
            - **-ENOTSUP** – If the requested mode of operation is not supported.
            - **-ENOSYS** – if the interface is not implemented.
            - **other** – negative errno on vendor specific error.

    static inline int clock\_control\_configure(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [clock\_control\_subsys\_t](#c.clock_control_subsys_t) sys, void \*data)
    :   Configure a source clock.

        This function is non-blocking and can be called from any context. On success, the selected clock is configured as per caller’s request.

        It is caller’s responsibility to ensure that subsequent calls to the API provide the right information to allows [clock\_control](#group__clock__control__interface_1ga459b95cb726892b95537d15273413099) driver to perform the right action (such as using the right clock source on clock\_control\_get\_rate call).

        `data` is implementation specific and could be used to convey supplementary information required for expected clock configuration.

        Parameters:
        :   - **dev** – Device structure whose driver controls the clock
            - **sys** – Opaque data representing the clock
            - **data** – Opaque data providing additional input for clock configuration

        Return values:
        :   - **0** – On success
            - **-ENOSYS** – If the device driver does not implement this call
            - **-errno** – Other negative errno on failure.

    struct clock\_control\_driver\_api
    :   *#include <clock\_control.h>*
