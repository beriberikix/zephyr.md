---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/reset.html
original_path: hardware/peripherals/reset.html
---

# Reset Controller

## Overview

Reset controllers are units that control the reset signals to multiple
peripherals. The reset controller API allows peripheral drivers to request
control over their reset input signals, including the ability to assert,
deassert and toggle those signals. Also, the reset status of the reset input
signal can be checked.

Mainly, the line\_assert and line\_deassert API functions are optional because
in most cases we want to toggle the reset signals.

## Configuration Options

Related configuration options:

- [`CONFIG_RESET`](../../kconfig.md#CONFIG_RESET "CONFIG_RESET")

## API Reference

[Reset Controller Interface](../../doxygen/html/group__reset__controller__interface.md)
