---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/comparator.html
original_path: hardware/peripherals/comparator.html
---

# Comparator

## Overview

An analog comparator compares the voltages of two analog signals connected to its negative and
positive inputs. If the voltage at the positive input is higher than the negative input, the
comparator’s output will be high, otherwise, it will be low.

Comparators can typically set a trigger which triggers on output changes. This trigger can
either invoke a callback, or its status can be polled.

Related configuration options:

- [`CONFIG_COMPARATOR`](../../kconfig.md#CONFIG_COMPARATOR "CONFIG_COMPARATOR")

## Configuration

Embedded comparators can typically be configured at runtime. When enabled, an initial
configuration must be provided using the devicetree. At runtime, comparators can have their
configuration updated using device driver specific APIs. The configuration will be applied
when the comparator is resumed.

## Power management

Comparators are enabled using power management. When resumed, the comparator will actively
compare its inputs, producing an output and detecting edges. When suspended, the comparator
will be inactive.

## Comparator shell

The comparator shell provides the `comp` command with a set of subcommands for the
[shell](../../services/shell/index.md#shell-api) module.

The `comp` shell command provides the following subcommands:

- `get_output` See [`comparator_get_output()`](../../doxygen/html/group__comparator__interface.md#ga89ea48c5d4a9d8c8ec44ee4c987309f3)
- `set_trigger` See [`comparator_set_trigger()`](../../doxygen/html/group__comparator__interface.md#ga964fab6458e020d8717ee7c47a84c1d0)
- `await_trigger` Awaits trigger using the following flow:

  - Set trigger callback using [`comparator_set_trigger_callback()`](../../doxygen/html/group__comparator__interface.md#ga1c9dc5dd46f5bb62b3cf4e2cfcd42509)
  - Await callback or time out after default or optionally provided timeout
  - Clear trigger callback using [`comparator_set_trigger_callback()`](../../doxygen/html/group__comparator__interface.md#ga1c9dc5dd46f5bb62b3cf4e2cfcd42509)
- `trigger_is_pending` See [`comparator_trigger_is_pending()`](../../doxygen/html/group__comparator__interface.md#ga28aa27594c7c3cf5cd7306d47ebf53f9)

Related configuration options:

- [`CONFIG_SHELL`](../../kconfig.md#CONFIG_SHELL "CONFIG_SHELL")
- [`CONFIG_COMPARATOR_SHELL`](../../kconfig.md#CONFIG_COMPARATOR_SHELL "CONFIG_COMPARATOR_SHELL")
- [`CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_DEFAULT_TIMEOUT`](../../kconfig.md#CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_DEFAULT_TIMEOUT "CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_DEFAULT_TIMEOUT")
- [`CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_MAX_TIMEOUT`](../../kconfig.md#CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_MAX_TIMEOUT "CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_MAX_TIMEOUT")

Note

The power management shell can optionally be enabled alongside the comparator shell.

Related configuration options:

- [`CONFIG_PM_DEVICE`](../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE")
- [`CONFIG_PM_DEVICE_SHELL`](../../kconfig.md#CONFIG_PM_DEVICE_SHELL "CONFIG_PM_DEVICE_SHELL")

## API Reference

[Comparator Interface](../../doxygen/html/group__comparator__interface.md)
