---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/drivers/stepper/generic/README.html
original_path: samples/drivers/stepper/generic/README.html
---

# Stepper

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/stepper/generic/README.rst/..)

## Description

This sample demonstrates how to use the stepper driver API to control a stepper motor. The sample
spins, enables, disables, stops the stepper and outputs the events to the console.

The stepper spins in 4 different modes: ping\_pong\_relative, ping\_pong\_absolute, continuous\_clockwise
and continuous\_anticlockwise. The micro-step interval in nanoseconds can be configured using the
`CONFIG_STEP_INTERVAL_NS`. The sample also demonstrates how to use the stepper callback
to change the direction of the stepper after a certain number of steps.

Pressing any button should change the mode of the stepper. The mode is printed to the console.
Following modes are supported: enable, ping\_pong\_relative, ping\_pong\_absolute, rotate\_cw, rotate\_ccw,
stop and disable.

The sample also has a monitor thread that prints the actual position of the stepper motor every
`CONFIG_MONITOR_THREAD_TIMEOUT_MS` milliseconds.

## Building and Running

This project spins the stepper and outputs the events to the console.

```shell
# From the root of the zephyr repository
west build -b nucleo_g071rb samples/drivers/stepper/generic
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build v4.1.0-568-gad33d28d0348 ***
[00:00:00.000,000] <inf> stepper: Starting generic stepper sample
[00:00:00.000,000] <dbg> stepper: main: stepper is 0x80086b8, name is gpio_stepper
[00:00:00.000,000] <dbg> gpio_stepper_motor_controller: gpio_stepper_set_microstep_interval: Setting Motor step interval to 1000000
[00:00:00.000,000] <dbg> stepper: monitor_thread: Actual position: 0
[00:00:00.491,000] <inf> stepper: mode: enable
[00:00:00.876,000] <inf> stepper: mode: ping pong relative
[00:00:01.000,000] <dbg> stepper: monitor_thread: Actual position: -114
[00:00:01.237,000] <inf> stepper: mode: ping pong absolute
[00:00:01.564,000] <inf> stepper: mode: rotate cw
[00:00:01.871,000] <inf> stepper: mode: rotate ccw
[00:00:02.000,000] <dbg> stepper: monitor_thread: Actual position: 129
[00:00:02.164,000] <inf> stepper: mode: stop
[00:00:02.444,000] <inf> stepper: mode: disable
[00:00:02.755,000] <inf> stepper: mode: enable

<repeats endlessly>
```

## See also

[Stepper Driver Interface](../../../../doxygen/html/group__stepper__interface.md)
