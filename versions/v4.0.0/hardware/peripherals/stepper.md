---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/stepper.html
original_path: hardware/peripherals/stepper.html
---

# Steppers

The stepper driver API provides a set of functions for controlling and configuring stepper drivers.

## Configure Stepper Driver

- Configure **micro-stepping resolution** using [`stepper_set_micro_step_res()`](../../doxygen/html/group__stepper__interface.md#gac3f2e315551e11500513dac837567625)
  and [`stepper_get_micro_step_res()`](../../doxygen/html/group__stepper__interface.md#ga72c54073cd703fd747533c01a447113e).
- Configure **actual position a.k.a step count** in microsteps using [`stepper_set_actual_position()`](../../doxygen/html/group__stepper__interface.md#gaf312a93167aabb39d814c6548991d6c6)
  and [`stepper_get_actual_position()`](../../doxygen/html/group__stepper__interface.md#ga6880673dcb5648c3da139a980d319157).
- Set **max velocity** in micro-steps per second using [`stepper_set_max_velocity()`](../../doxygen/html/group__stepper__interface.md#gabbb691c2f1beb2bdc7e856a7f77b4de4)
- **Enable** the stepper driver using [`stepper_enable()`](../../doxygen/html/group__stepper__interface.md#ga3fbda29131df4618204f7df86b82f450).

## Control Stepper

- **Move by** +/- micro-steps also known as **relative movement** using [`stepper_move()`](../../doxygen/html/group__stepper__interface.md#ga7622a8e1e95b2bbb2dc1273bd84e88a5).
- **Move to** a specific position also known as **absolute movement**
  using [`stepper_set_target_position()`](../../doxygen/html/group__stepper__interface.md#ga2417b3ca2f77553bcd6a8b909e5f4d27).
- Run continuously with a **constant velocity** in a specific direction until
  a stop is detected using [`stepper_enable_constant_velocity_mode()`](../../doxygen/html/group__stepper__interface.md#ga430250f6e3544e5bba49d5b6ceba1bf9).
- Check if the stepper is **moving** using [`stepper_is_moving()`](../../doxygen/html/group__stepper__interface.md#gaaba23377932454df4eb5a43437beb18c).

## Device Tree

In the context of stepper controllers device tree provides the initial hardware
configuration for stepper drivers on a per device level. Each device must specify
a device tree binding in Zephyr, and ideally, a set of hardware configuration options
for things such as current settings, ramp parameters and furthermore. These can then
be used in a boards devicetree to configure a stepper driver to its initial state.

See examples in:

- [`adi,tmc5041`](../../build/dts/api/bindings/stepper/adi/adi%2Ctmc5041.md#std-dtcompatible-adi-tmc5041)

## Discord

Zephyr has a [stepper discord](https://discord.com/channels/720317445772017664/1278263869982375946) channel for stepper related discussions, which
is open to all.

### API Reference

A common set of functions which should be implemented by all stepper drivers.

[Stepper Controller Interface](../../doxygen/html/group__stepper__interface.md)

### Stepper controller specific APIs

## Trinamic

[Trinamic Stepper Controller Interface](../../doxygen/html/group__trinamic__stepper__interface.md)
