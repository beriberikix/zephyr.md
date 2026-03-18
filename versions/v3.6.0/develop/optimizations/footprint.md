---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/optimizations/footprint.html
original_path: develop/optimizations/footprint.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Optimizing for Footprint

## Stack Sizes

Stack sizes of various system threads are specified generously to allow for
usage in different scenarios on as many supported platforms as possible. You
should start the optimization process by reviewing all stack sizes and adjusting
them for your application:

[`CONFIG_ISR_STACK_SIZE`](../../kconfig.md#CONFIG_ISR_STACK_SIZE "CONFIG_ISR_STACK_SIZE")
:   Set to 2048 by default

[`CONFIG_MAIN_STACK_SIZE`](../../kconfig.md#CONFIG_MAIN_STACK_SIZE "CONFIG_MAIN_STACK_SIZE")
:   Set to 1024 by default

[`CONFIG_IDLE_STACK_SIZE`](../../kconfig.md#CONFIG_IDLE_STACK_SIZE "CONFIG_IDLE_STACK_SIZE")
:   Set to 320 by default

[`CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE`](../../kconfig.md#CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE "CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE")
:   Set to 1024 by default

[`CONFIG_PRIVILEGED_STACK_SIZE`](../../kconfig.md#CONFIG_PRIVILEGED_STACK_SIZE "CONFIG_PRIVILEGED_STACK_SIZE")
:   Set to 1024 by default, depends on userspace feature.

## Unused Peripherals

Some peripherals are enabled by default. You can disable unused
peripherals in your project configuration, for example:

```text
CONFIG_GPIO=n
CONFIG_SPI=n
```

## Various Debug/Informational Options

The following options are enabled by default to provide more information about
the running application and to provide means for debugging and error handling:

[`CONFIG_BOOT_BANNER`](../../kconfig.md#CONFIG_BOOT_BANNER "CONFIG_BOOT_BANNER")
:   This option can be disabled to save a few bytes.

[`CONFIG_DEBUG`](../../kconfig.md#CONFIG_DEBUG "CONFIG_DEBUG")
:   This option can be disabled for production builds

## MPU/MMU Support

Depending on your application and platform needs, you can disable MPU/MMU
support to gain some memory and improve performance. Consider the consequences
of this configuration choice though, because you’ll lose advanced stack
checking and support.
