---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/stepper.html
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
- **Enable** the stepper driver using [`stepper_enable()`](../../doxygen/html/group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450).

## Control Stepper

- **Move by** +/- micro-steps also known as **relative movement** using [`stepper_move_by()`](../../doxygen/html/group__stepper__interface.md#ga851c6b8f0cfe485095f345f33186535a).
- **Move to** a specific position also known as **absolute movement** using [`stepper_move_to()`](../../doxygen/html/group__stepper__interface.md#ga7d12d3ff146698662090d8b761a57615).
- Run continuously with a **constant step interval** in a specific direction until
  a stop is detected using [`stepper_run()`](../../doxygen/html/group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87).
- Check if the stepper is **moving** using [`stepper_is_moving()`](../../doxygen/html/group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c).
- Register an **event callback** using [`stepper_set_event_callback()`](../../doxygen/html/group__stepper__interface.md#gad44cc67d4667114c933d82f527ad2b77).

## Device Tree

In the context of stepper controllers device tree provides the initial hardware
configuration for stepper drivers on a per device level. Each device must specify
a device tree binding in Zephyr, and ideally, a set of hardware configuration options
for things such as current settings, ramp parameters and furthermore. These can then
be used in a boards devicetree to configure a stepper driver to its initial state.

See examples in:

- [`zephyr,gpio-stepper`](../../build/dts/api/bindings/stepper/zephyr%2Cgpio-stepper.md#std-dtcompatible-zephyr-gpio-stepper)
- [`adi,tmc50xx`](../../build/dts/api/bindings/stepper/adi/adi%2Ctmc50xx.md#std-dtcompatible-adi-tmc50xx)

## Discord

Zephyr has a [stepper discord](https://discord.com/channels/720317445772017664/1278263869982375946) channel for stepper related discussions, which
is open to all.

### API Reference

A common set of functions which should be implemented by all stepper drivers.

[Stepper Driver Interface](../../doxygen/html/group__stepper__interface.md)

Related code samples

- [TMC50XX stepper](../../samples/drivers/stepper/tmc50xx/README.md#tmc50xx "Rotate a TMC50XX stepper motor and change velocity at runtime.")Rotate a TMC50XX stepper motor and change velocity at runtime.

### Stepper controller specific APIs

## Trinamic

[Trinamic Stepper Controller Interface](../../doxygen/html/group__trinamic__stepper__interface.md)
