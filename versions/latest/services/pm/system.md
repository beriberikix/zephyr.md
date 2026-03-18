---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/pm/system.html
original_path: services/pm/system.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# System Power Management

The kernel enters the idle state when it has nothing to schedule. If enabled via
the [`CONFIG_PM`](../../kconfig.md#CONFIG_PM "CONFIG_PM") Kconfig option, the Power Management
Subsystem can put an idle system in one of the supported power states, based
on the selected power management policy and the duration of the idle time
allotted by the kernel.

It is an application responsibility to set up a wake up event. A wake up event
will typically be an interrupt triggered by one of the SoC peripheral modules
such as a SysTick, RTC, counter, or GPIO. Depending on the power mode entered,
only some SoC peripheral modules may be active and can be used as a wake up
source.

The following diagram describes system power management:

![System power management](../../_images/system-pm.svg)

Some handful examples using different power management features:

- [samples/boards/stm32/power\_mgmt/blinky/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/stm32/power_mgmt/blinky/)
- [samples/boards/esp32/deep\_sleep/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/esp32/deep_sleep/)
- [samples/subsys/pm/device\_pm/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/pm/device_pm/)
- [tests/subsys/pm/power\_mgmt/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/pm/power_mgmt/)
- [tests/subsys/pm/power\_mgmt\_soc/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/pm/power_mgmt_soc/)
- [tests/subsys/pm/power\_states\_api/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/pm/power_states_api/)

## Power States

The power management subsystem contains a set of states based on
power consumption and context retention.

The list of available power states is defined by [`pm_state`](api/index.md#c.pm_state "pm_state"). In
general power states with higher indexes will offer greater power savings and
have higher wake latencies.

## Power Management Policies

The power management subsystem supports the following power management policies:

- Residency based
- Application defined

The policy manager is responsible for informing the power subsystem which
power state the system should transition to based on states defined by the
platform and other constraints such as a list of allowed states.

More details on the states definition can be found in the
[`zephyr,power-state`](../../build/dts/api/bindings/power/zephyr%2Cpower-state.md#std-dtcompatible-zephyr-power-state) binding documentation.

### Residency

The power management system enters the power state which offers the highest
power savings, and with a minimum residency value (see
[`zephyr,power-state`](../../build/dts/api/bindings/power/zephyr%2Cpower-state.md#std-dtcompatible-zephyr-power-state)) less than or equal to the scheduled system
idle time duration.

This policy also accounts for the time necessary to become active
again. The core logic used by this policy to select the best power
state is:

```c
if (time_to_next_scheduled_event >= (state.min_residency_us + state.exit_latency))) {
   return state
}
```

### Application

The application defines the power management policy by implementing the
`pm_policy_next_state()` function. In this policy the application is free
to decide which power state the system should transition to based on the
remaining time for the next scheduled timeout.

An example of an application that defines its own policy can be found in
[tests/subsys/pm/power\_mgmt/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/pm/power_mgmt/).

### Policy and Power States

The power management subsystem allows different Zephyr components and
applications to configure the policy manager to block system from transitioning
into certain power states. This can be used by devices when executing tasks in
background to prevent the system from going to a specific state where it would
lose context.
