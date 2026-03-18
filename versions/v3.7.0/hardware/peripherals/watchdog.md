---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/watchdog.html
original_path: hardware/peripherals/watchdog.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Watchdog

## Overview

## API Reference

Related code samples

[Watchdog](../../samples/drivers/watchdog/README.md#watchdog "Use the watchdog driver API to reset the board when it gets stuck in an infinite loop.")
:   Use the watchdog driver API to reset the board when it gets stuck in an infinite loop.

*group* Watchdog Interface
:   Watchdog Interface.

    **Since**
    :   1.0

    **Version**
    :   1.0.0

    Watchdog options

    WDT\_OPT\_PAUSE\_IN\_SLEEP
    :   Pause watchdog timer when CPU is in sleep state.

    WDT\_OPT\_PAUSE\_HALTED\_BY\_DBG
    :   Pause watchdog timer when CPU is halted by the debugger.

    Watchdog behavior flags

    WDT\_FLAG\_RESET\_NONE
    :   Reset: none.

    WDT\_FLAG\_RESET\_CPU\_CORE
    :   Reset: CPU core.

    WDT\_FLAG\_RESET\_SOC
    :   Reset: SoC.

    Typedefs

    typedef void (\*wdt\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int channel\_id)
    :   Watchdog callback.

        Param dev:
        :   Watchdog device instance.

        Param channel\_id:
        :   Channel identifier.

    Functions

    int wdt\_setup(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t options)
    :   Set up watchdog instance.

        This function is used for configuring global watchdog settings that affect all timeouts. It should be called after installing timeouts. After successful return, all installed timeouts are valid and must be serviced periodically by calling [wdt\_feed()](#group__watchdog__interface_1ga87265e8988e928eaa380ea29afb6eabe).

        Parameters:
        :   - **dev** – Watchdog device instance.
            - **options** – Configuration options (see [WDT\_OPT](#group__watchdog__interface_1WDT_OPT)).

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If any of the set options is not supported.
            - **-EBUSY** – If watchdog instance has been already setup.
            - **-errno** – In case of any other failure.

    int wdt\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable watchdog instance.

        This function disables the watchdog instance and automatically uninstalls all timeouts. To set up a new watchdog, install timeouts and call [wdt\_setup()](#group__watchdog__interface_1ga822239f3d73585e2d01312657dbbb782) again. Not all watchdogs can be restarted after they are disabled.

        Parameters:
        :   - **dev** – Watchdog device instance.

        Return values:
        :   - **0** – If successful.
            - **-EFAULT** – If watchdog instance is not enabled.
            - **-EPERM** – If watchdog can not be disabled directly by application code.
            - **-errno** – In case of any other failure.

    static inline int wdt\_install\_timeout(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [wdt\_timeout\_cfg](#c.wdt_timeout_cfg) \*cfg)
    :   Install a new timeout.

        Note

        This function must be used before [wdt\_setup()](#group__watchdog__interface_1ga822239f3d73585e2d01312657dbbb782). Changes applied here have no effects until [wdt\_setup()](#group__watchdog__interface_1ga822239f3d73585e2d01312657dbbb782) is called.

        Parameters:
        :   - **dev** – Watchdog device instance.
            - **cfg** – **[in]** Timeout configuration.

        Return values:
        :   - **channel\_id** – If successful, a non-negative value indicating the index of the channel to which the timeout was assigned. This value is supposed to be used as the parameter in calls to [wdt\_feed()](#group__watchdog__interface_1ga87265e8988e928eaa380ea29afb6eabe).
            - **-EBUSY** – If timeout can not be installed while watchdog has already been setup.
            - **-ENOMEM** – If no more timeouts can be installed.
            - **-ENOTSUP** – If any of the set flags is not supported.
            - **-EINVAL** – If any of the window timeout value is out of possible range. This value is also returned if watchdog supports only one timeout value for all timeouts and the supplied timeout window differs from windows for alarms installed so far.
            - **-errno** – In case of any other failure.

    int wdt\_feed(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int channel\_id)
    :   Feed specified watchdog timeout.

        Parameters:
        :   - **dev** – Watchdog device instance.
            - **channel\_id** – Channel index.

        Return values:
        :   - **0** – If successful.
            - **-EAGAIN** – If completing the feed operation would stall the caller, for example due to an in-progress watchdog operation such as a previous [wdt\_feed()](#group__watchdog__interface_1ga87265e8988e928eaa380ea29afb6eabe) call.
            - **-EINVAL** – If there is no installed timeout for supplied channel.
            - **-errno** – In case of any other failure.

    struct wdt\_window
    :   *#include <watchdog.h>*

        Watchdog timeout window.

        Each installed timeout needs feeding within the specified time window, otherwise the watchdog will trigger. If the watchdog instance does not support window timeouts then min value must be equal to 0.

        Note

        If specified values can not be precisely set they are always rounded up.

        Public Members

        uint32\_t min
        :   Lower limit of watchdog feed timeout in milliseconds.

        uint32\_t max
        :   Upper limit of watchdog feed timeout in milliseconds.

    struct wdt\_timeout\_cfg
    :   *#include <watchdog.h>*

        Watchdog timeout configuration.

        Public Members

        struct [wdt\_window](#c.wdt_window) window
        :   Timing parameters of watchdog timeout.

        [wdt\_callback\_t](#c.wdt_callback_t) callback
        :   Timeout callback (can be `NULL`).

        struct [wdt\_timeout\_cfg](#c.wdt_timeout_cfg) \*next
        :   Pointer to the next timeout configuration.

            This field is only available if  [`CONFIG_WDT_MULTISTAGE`](../../kconfig.md#CONFIG_WDT_MULTISTAGE "CONFIG_WDT_MULTISTAGE") is enabled (watchdogs with staged timeouts functionality). Value must be `NULL` for single stage timeout.

        uint8\_t flags
        :   Flags (see [WDT\_FLAGS](#group__watchdog__interface_1WDT_FLAGS)).
