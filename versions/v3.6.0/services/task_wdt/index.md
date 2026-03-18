---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/task_wdt/index.html
original_path: services/task_wdt/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Task Watchdog

## Overview

Many microcontrollers feature a hardware watchdog timer peripheral. Its purpose
is to trigger an action (usually a system reset) in case of severe software
malfunctions. Once initialized, the watchdog timer has to be restarted (“fed”)
in regular intervals to prevent it from timing out. If the software got stuck
and does not manage to feed the watchdog anymore, the corrective action is
triggered to bring the system back to normal operation.

In real-time operating systems with multiple tasks running in parallel, a
single watchdog instance may not be sufficient anymore, as it can be used for
only one task. This software watchdog based on kernel timers provides a method
to supervise multiple threads or tasks (called watchdog channels).

An existing hardware watchdog can be used as an optional fallback if the task
watchdog itself or the scheduler has a malfunction.

The task watchdog uses a kernel timer as its backend. If configured properly,
the timer ISR is never actually called during normal operation, as the timer is
continuously updated in the feed calls.

It’s currently not possible to have multiple instances of task watchdogs.
Instead, the task watchdog API can be accessed globally to add or delete new
channels without passing around a context or device pointer in the firmware.

The maximum number of channels is predefined via Kconfig and should be adjusted
to match exactly the number of channels required by the application.

## Configuration Options

Related configuration options can be found under
[subsys/task\_wdt/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/task_wdt/Kconfig).

- [`CONFIG_TASK_WDT`](../../kconfig.md#CONFIG_TASK_WDT "CONFIG_TASK_WDT")
- [`CONFIG_TASK_WDT_CHANNELS`](../../kconfig.md#CONFIG_TASK_WDT_CHANNELS "CONFIG_TASK_WDT_CHANNELS")
- [`CONFIG_TASK_WDT_HW_FALLBACK`](../../kconfig.md#CONFIG_TASK_WDT_HW_FALLBACK "CONFIG_TASK_WDT_HW_FALLBACK")
- [`CONFIG_TASK_WDT_MIN_TIMEOUT`](../../kconfig.md#CONFIG_TASK_WDT_MIN_TIMEOUT "CONFIG_TASK_WDT_MIN_TIMEOUT")
- [`CONFIG_TASK_WDT_HW_FALLBACK_DELAY`](../../kconfig.md#CONFIG_TASK_WDT_HW_FALLBACK_DELAY "CONFIG_TASK_WDT_HW_FALLBACK_DELAY")

## API Reference

Related code samples

[Task watchdog](../../samples/subsys/task_wdt/README.md#task-wdt "Monitor a thread using a task watchdog.")
:   Monitor a thread using a task watchdog.

*group* task\_wdt\_api
:   Task Watchdog APIs.

    Typedefs

    typedef void (\*task\_wdt\_callback\_t)(int channel\_id, void \*user\_data)
    :   Task watchdog callback.

    Functions

    int task\_wdt\_init(const struct [device](../../kernel/drivers/index.md#c.device "device") \*hw\_wdt)
    :   Initialize task watchdog.

        This function sets up necessary kernel timers and the hardware watchdog (if desired as fallback). It has to be called before [task\_wdt\_add()](#group__task__wdt__api_1ga26484bd148a9e2910d9989a1d9598230) and [task\_wdt\_feed()](#group__task__wdt__api_1ga00fc594cace06d6308efa1ded45a22fc).

        Parameters:
        :   - **hw\_wdt** – Pointer to the hardware watchdog device used as fallback. Pass NULL if no hardware watchdog fallback is desired.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If assigning a hardware watchdog is not supported.
            - **-Errno** – Negative errno if the fallback hw\_wdt is used and the install timeout API fails. See [wdt\_install\_timeout()](../../hardware/peripherals/watchdog.md#group__watchdog__interface_1ga5be7aa7f1987be0e69c74b62d1c126a5) API for possible return values.

    int task\_wdt\_add(uint32\_t reload\_period, [task\_wdt\_callback\_t](#c.task_wdt_callback_t) callback, void \*user\_data)
    :   Install new timeout.

        Adds a new timeout to the list of task watchdog channels.

        Parameters:
        :   - **reload\_period** – Period in milliseconds used to reset the timeout
            - **callback** – Function to be called when watchdog timer expired. Pass NULL to use system reset handler.
            - **user\_data** – User data to associate with the watchdog channel.

        Return values:
        :   - **channel\_id** – If successful, a non-negative value indicating the index of the channel to which the timeout was assigned. This ID is supposed to be used as the parameter in calls to [task\_wdt\_feed()](#group__task__wdt__api_1ga00fc594cace06d6308efa1ded45a22fc).
            - **-EINVAL** – If the reload\_period is invalid.
            - **-ENOMEM** – If no more timeouts can be installed.

    int task\_wdt\_delete(int channel\_id)
    :   Delete task watchdog channel.

        Deletes the specified channel from the list of task watchdog channels. The channel is now available again for other tasks via [task\_wdt\_add()](#group__task__wdt__api_1ga26484bd148a9e2910d9989a1d9598230) function.

        Parameters:
        :   - **channel\_id** – Index of the channel as returned by [task\_wdt\_add()](#group__task__wdt__api_1ga26484bd148a9e2910d9989a1d9598230).

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If there is no installed timeout for supplied channel.

    int task\_wdt\_feed(int channel\_id)
    :   Feed specified watchdog channel.

        This function loops through all installed task watchdogs and updates the internal kernel timer used as for the software watchdog with the next due timeout.

        Parameters:
        :   - **channel\_id** – Index of the fed channel as returned by [task\_wdt\_add()](#group__task__wdt__api_1ga26484bd148a9e2910d9989a1d9598230).

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If there is no installed timeout for supplied channel.
