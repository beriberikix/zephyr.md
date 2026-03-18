---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/stm32/power_mgmt/suspend_to_ram/README.html
original_path: samples/boards/stm32/power_mgmt/suspend_to_ram/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# STM32 PM Suspend to RAM

## Overview

This sample is a minimum application to demonstrate basic power management
behavior in a basic blinking LED set up using the [GPIO API](../../../../../hardware/peripherals/gpio.md#gpio-api) in
low power context + ADC measurements and entropy.

## Requirements

The board should support enabling PM. For a STM32 based target, it means that
it should support a clock source alternative to Cortex Systick that can be used
in core sleep states, as LPTIM ([`st,stm32-lptim`](../../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim)).
The board shall have an RTC to use it during the standby mode as a replacement
for LPTIM (which is disabled). The board shall also have RAM retention to be
able to restore context after standby.

## Building and Running

Build and flash Blinky as follows, changing `stm32wba55cg` for your board:

```shell
west build -b stm32wba55cg samples/boards/stm32/power_mgmt/suspend_to_ram
west flash
```

After flashing, the LED starts to blink.

## PM configurations

By default, [`CONFIG_PM_DEVICE`](../../../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") and [`CONFIG_PM_DEVICE_RUNTIME`](../../../../../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME")
are enabled.
