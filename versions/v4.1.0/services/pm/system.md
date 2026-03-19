---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/pm/system.html
original_path: services/pm/system.html
---

# System Power Management

## Introduction

The kernel enters the idle state when it has nothing to schedule.
Enabling [`CONFIG_PM`](../../kconfig.md#CONFIG_PM "CONFIG_PM") allows the kernel to call upon the
power management subsystem to put an idle system into one of the supported power states.
The kernel requests an amount of time it would like to suspend, then the PM subsystem decides
the appropriate power state to transition to based on the configured power management policy.

It is the application’s responsibility to set up a wake-up event.
A wake-up event will typically be an interrupt triggered by an SoC peripheral module.
Examples include a SysTick, RTC, counter, or GPIO.
Keep in mind that depending on the SoC and the power mode in question,
not all peripherals may be active, and therefore
some wake-up sources may not be usable in all power modes.

The following diagram describes system power management:

digraph G {
compound=true
node [height=1.2 style=rounded]
lock [label="Lock interruptions"]
config\_pm [label="CONFIG\_PM" shape=diamond style="rounded,dashed"]
forced\_state [label="state forced ?", shape=diamond style="rounded,dashed"]
config\_system\_managed\_device\_pm [label="CONFIG\_PM\_DEVICE" shape=diamond style="rounded,dashed"]
config\_system\_managed\_device\_pm2 [label="CONFIG\_PM\_DEVICE" shape=diamond style="rounded,dashed"]
pm\_policy [label="Check policy manager\nfor a power state "]
pm\_suspend\_devices [label="Suspend\ndevices"]
pm\_resume\_devices [label="Resume\ndevices"]
pm\_state\_set [label="Change power state\n(SoC API)" style="rounded,bold"]
pm\_system\_resume [label="Finish wake-up\n(SoC API)\n(restore interruptions)" style="rounded,bold"]
k\_cpu\_idle [label="k\_cpu\_idle()"]
subgraph cluster\_0 {
style=invisible;
lock -> config\_pm
}
subgraph cluster\_1 {
style=dashed
label = "pm\_system\_suspend()"
forced\_state -> config\_system\_managed\_device\_pm [label="yes"]
forced\_state -> pm\_policy [label="no"]
pm\_policy -> config\_system\_managed\_device\_pm
config\_system\_managed\_device\_pm -> pm\_state\_set:e [label="no"]
config\_system\_managed\_device\_pm -> pm\_suspend\_devices [label="yes"]
pm\_suspend\_devices -> pm\_state\_set
pm\_state\_set -> config\_system\_managed\_device\_pm2
config\_system\_managed\_device\_pm2 -> pm\_resume\_devices [label="yes"]
config\_system\_managed\_device\_pm2 -> pm\_system\_resume [label="no"]
pm\_resume\_devices -> pm\_system\_resume
}
{rankdir=LR k\_cpu\_idle; forced\_state}
pm\_policy -> k\_cpu\_idle [label="PM\_STATE\_ACTIVE\n(no power state meet requirements)"]
config\_pm -> k\_cpu\_idle [label="no"]
config\_pm -> forced\_state [label="yes" lhead="cluster\_1"]
pm\_system\_resume:e -> lock:e [constraint=false lhed="cluster\_0"]
}

System power management

### Power States

The power management subsystem defines a set of states described by the
power consumption and context retention associated with each of them.

The set of power states is defined by [`pm_state`](../../doxygen/html/group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5). In general, lower power states
(higher index in the enum) will offer greater power savings and have higher wake latencies.

### Power Management Policies

The power management subsystem supports the following power management policies:

- Residency based
- Application defined

The policy manager is the component of the power management subsystem responsible
for deciding which power state the system should transition to.
The policy manager can only choose between states that have been defined for the platform.
Other constraints placed upon the decision may include locks disallowing certain power states,
or various kinds of minimum and maximum latency values, depending on the policy.

More details on the states definition can be found in the
[`zephyr,power-state`](../../build/dts/api/bindings/power/zephyr%2Cpower-state.md#std-dtcompatible-zephyr-power-state) binding documentation.

#### Residency

Under the residency policy, the system will enter the power state which offers the highest
power savings, with the constraint that the sum of the minimum residency value (see
[`zephyr,power-state`](../../build/dts/api/bindings/power/zephyr%2Cpower-state.md#std-dtcompatible-zephyr-power-state)) and the latency to exit the mode must be
less than or equal to the system idle time duration scheduled by the kernel.

Thus the core logic can be summarized with the following expression:

```c
if (time_to_next_scheduled_event >= (state.min_residency_us + state.exit_latency)) {
   return state
}
```

#### Application

The application defines the power management policy by implementing the
`pm_policy_next_state()` function. In this policy, the application is free
to decide which power state the system should transition to based on the
remaining time until the next scheduled timeout.

An example of an application that defines its own policy can be found in
[tests/subsys/pm/power\_mgmt/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/pm/power_mgmt/).

#### Policy and Power States

The power management subsystem allows different Zephyr components and
applications to configure the policy manager to block the system from transitioning
into certain power states. This can be used by devices when executing tasks in
background to prevent the system from going to a specific state where it would
lose context. See [`pm_policy_state_lock_get()`](../../doxygen/html/group__subsys__pm__sys__policy.md#gabbb379f8572f164addafe93ad3468f3d).

### Examples

Some helpful examples showing different power management features:

- [samples/boards/st/power\_mgmt/blinky/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/st/power_mgmt/blinky/)
- [samples/boards/espressif/deep\_sleep/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/espressif/deep_sleep/)
- [samples/subsys/pm/device\_pm/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/pm/device_pm/)
- [tests/subsys/pm/power\_mgmt/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/pm/power_mgmt/)
- [tests/subsys/pm/power\_mgmt\_soc/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/pm/power_mgmt_soc/)
- [tests/subsys/pm/power\_states\_api/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/pm/power_states_api/)
