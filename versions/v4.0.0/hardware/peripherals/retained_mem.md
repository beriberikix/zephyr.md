---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/retained_mem.html
original_path: hardware/peripherals/retained_mem.html
---

# Retained Memory

## Overview

The retained memory driver API provides a way of reading from/writing to memory
areas whereby the contents of the memory is retained whilst the device is
powered (data may be lost in low power modes).

## Configuration Options

Related configuration options:

- [`CONFIG_RETAINED_MEM`](../../kconfig.md#CONFIG_RETAINED_MEM "CONFIG_RETAINED_MEM")
- [`CONFIG_RETAINED_MEM_INIT_PRIORITY`](../../kconfig.md#CONFIG_RETAINED_MEM_INIT_PRIORITY "CONFIG_RETAINED_MEM_INIT_PRIORITY")
- [`CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE`](../../kconfig.md#CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE "CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE")

## Mutex protection

Mutex protection of retained memory drivers is enabled by default when
applications are compiled with multithreading support. This means that
different threads can safely call the retained memory functions without
clashing with other concurrent thread function usage, but means that retained
memory functions cannot be used from ISRs. It is possible to disable mutex
protection globally on all retained memory drivers by enabling
[`CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE`](../../kconfig.md#CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE "CONFIG_RETAINED_MEM_MUTEX_FORCE_DISABLE") - users are then
responsible for ensuring that the function calls do not conflict with each
other.

## API Reference

[Retained memory driver interface](../../doxygen/html/group__retained__mem__interface.md)
