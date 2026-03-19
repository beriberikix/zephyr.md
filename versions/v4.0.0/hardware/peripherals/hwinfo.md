---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/hwinfo.html
original_path: hardware/peripherals/hwinfo.html
---

# Hardware Information

## Overview

The HW Info API provides access to hardware information such as device
identifiers and reset cause flags.

Reset cause flags can be used to determine why the device was reset; for
example due to a watchdog timeout or due to power cycling. Different devices
support different subset of flags. Use
[`hwinfo_get_supported_reset_cause()`](../../doxygen/html/group__hwinfo__interface.md#gaf0d345653c4fbb5f38a78aba766a6bb8) to retrieve the flags that are
supported by that device.

## Configuration Options

Related configuration options:

- [`CONFIG_HWINFO`](../../kconfig.md#CONFIG_HWINFO "CONFIG_HWINFO")

## API Reference

[Hardware Info Interface](../../doxygen/html/group__hwinfo__interface.md)
