---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/coredump.html
original_path: hardware/peripherals/coredump.html
---

# Coredump Device

## Overview

The coredump device is a pseudo-device driver with two types.A COREDUMP\_TYPE\_MEMCPY
type exposes device tree bindings for memory address/size values to be included in
any dump. And the driver exposes an API to add/remove dump memory regions at runtime.
A COREDUMP\_TYPE\_CALLBACK device requires exactly one entry in the memory-regions
array with a size of 0 and a desired size. The driver will statically allocate memory
of the desired size and provide an API to register a callback function to fill that
memory when a dump occurs.

## Configuration Options

Related configuration options:

- [`CONFIG_COREDUMP_DEVICE`](../../kconfig.md#CONFIG_COREDUMP_DEVICE "CONFIG_COREDUMP_DEVICE")

## API Reference

[Coredump pseudo-device driver APIs](../../doxygen/html/group__coredump__device__interface.md)
