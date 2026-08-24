---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/hardware/peripherals/stepper.html
original_path: hardware/peripherals/stepper.html
---

# Steppers

The stepper driver API provides a set of functions for controlling and configuring stepper drivers.

## Configure Stepper Driver

- Configure **micro-stepping resolution** using [`stepper_set_micro_step_res()`](../../doxygen/html/group__stepper__interface.md#gac3f2e315551e11500513dac837567625)
  and [`stepper_get_micro_step_res()`](../../doxygen/html/group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e).
- Configure **reference position** in microsteps using [`stepper_set_reference_position()`](../../doxygen/html/group__stepper__interface.md#ga472ba1e64876fcaf79ba95edd8261a36)
  and [`stepper_get_actual_position()`](../../doxygen/html/group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157).
- Set **step interval** in nanoseconds between steps using [`stepper_set_microstep_interval()`](../../doxygen/html/group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7)
- **Enable** the stepper driver using [`stepper_enable()`](../../doxygen/html/group__stepper__interface.md#ga3395b5f8b401d8175067edfb25c2e0e8).
- **Disable** the stepper driver using [`stepper_disable()`](../../doxygen/html/group__stepper__interface.md#gab892a6b8d8fb34db0e682dd8f7de4218).

## Control Stepper

- **Move by** +/- micro-steps also known as **relative movement** using [`stepper_move_by()`](../../doxygen/html/group__stepper__interface.md#ga851c6b8f0cfe485095f345f33186535a).
- **Move to** a specific position also known as **absolute movement** using [`stepper_move_to()`](../../doxygen/html/group__stepper__interface.md#ga7d12d3ff146698662090d8b761a57615).
- Run continuously with a **constant step interval** in a specific direction until
  a stop is detected using [`stepper_run()`](../../doxygen/html/group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87).
- **Stop** the stepper using [`stepper_stop()`](../../doxygen/html/group__stepper__interface.md#gaa049d39fe611a86904e7a60fc7005abd).
- Check if the stepper is **moving** using [`stepper_is_moving()`](../../doxygen/html/group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c).
- Register an **event callback** using [`stepper_set_event_callback()`](../../doxygen/html/group__stepper__interface.md#gad44cc67d4667114c933d82f527ad2b77).

## Device Tree

In the context of stepper controllers device tree provides the initial hardware
configuration for stepper drivers on a per device level. Each device must specify
a device tree binding in Zephyr, and ideally, a set of hardware configuration options
for things such as current settings, ramp parameters and furthermore. These can then
be used in a boards devicetree to configure a stepper driver to its initial state.

See examples in:

- [`zephyr,gpio-stepper`](../../build/dts/api/bindings/stepper/zephyr,gpio-stepper.md#std-dtcompatible-zephyr-gpio-stepper)
- [`adi,tmc50xx`](../../build/dts/api/bindings/stepper/adi/adi,tmc50xx.md#std-dtcompatible-adi-tmc50xx)

## Discord

Zephyr has a [stepper discord](https://discord.com/channels/720317445772017664/1278263869982375946) channel for stepper related discussions, which
is open to all.

## Stepper API Test Suite

The stepper API test suite provides a set of tests that can be used to verify the functionality of
stepper drivers.

```shell
# From the root of the zephyr repository
west build -b <board> --extra-dtc-overlay <path/to/board.overlay> tests/drivers/stepper/stepper_api
west flash
```

## Sample Output

Below is a snippet of the test output for the tmc50xx stepper driver. Since
[`stepper_set_microstep_interval()`](../../doxygen/html/group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7) is not implemented by the driver the corresponding tests
have been skipped.

```shell
===================================================================
TESTSUITE stepper succeeded

------ TESTSUITE SUMMARY START ------

SUITE PASS - 100.00% [stepper]: pass = 4, fail = 0, skip = 2, total = 6 duration = 0.069 seconds
 - PASS - [stepper.test_actual_position] duration = 0.016 seconds
 - PASS - [stepper.test_get_micro_step_res] duration = 0.013 seconds
 - SKIP - [stepper.test_set_micro_step_interval_invalid_zero] duration = 0.007 seconds
 - PASS - [stepper.test_set_micro_step_res_incorrect] duration = 0.010 seconds
 - PASS - [stepper.test_stop] duration = 0.016 seconds
 - SKIP - [stepper.test_target_position_w_fixed_step_interval] duration = 0.007 seconds

------ TESTSUITE SUMMARY END ------

===================================================================
PROJECT EXECUTION SUCCESSFUL
```

### API Reference

A common set of functions which should be implemented by all stepper drivers.

[Stepper Driver Interface](../../doxygen/html/group__stepper__interface.md)

Related code samples

- [Stepper](../../samples/drivers/stepper/generic/README.md#stepper "Rotate a stepper motor in 4 different modes.")Rotate a stepper motor in 4 different modes.
- [TMC50XX stepper](../../samples/drivers/stepper/tmc50xx/README.md#tmc50xx "Rotate a TMC50XX stepper motor and change velocity at runtime.")Rotate a TMC50XX stepper motor and change velocity at runtime.

### Stepper controller specific APIs

## Trinamic

[Trinamic Stepper Controller Interface](../../doxygen/html/group__trinamic__stepper__interface.md)
