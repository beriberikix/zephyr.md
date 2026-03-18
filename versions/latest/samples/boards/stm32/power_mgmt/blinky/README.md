---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/stm32/power_mgmt/blinky/README.html
original_path: samples/boards/stm32/power_mgmt/blinky/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# STM32 PM Blinky

## Overview

This sample is a minimum application to demonstrate basic power management
behavior in a basic blinking LED set up using the [GPIO API](../../../../../hardware/peripherals/gpio.md#gpio-api) in
low power context.
Note that lptim instance selected for the low power timer is named **&stm32\_lp\_tick\_source**
When setting a prescaler to decrease the lptimer input clock frequency, the system can sleep
for a longer timeout value and the CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC is adjusted.
For example, when clocking the low power Timer with LSE clock at 32768Hz and adding a
prescaler of <32>, then the kernel sleep period can reach 65536 \* 32/32768 = 64 seconds
CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC is set to 1024.

## Requirements

The board should support enabling PM. For a STM32 based target, it means that
it should support a clock source alternative to Cortex Systick that can be used
in core sleep states, as LPTIM ([`st,stm32-lptim`](../../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim)).

## Building and Running

Build and flash Blinky as follows, changing `stm32l562e_dk` for your board:

```shell
west build -b stm32l562e_dk samples/basic/blinky
west flash
```

After flashing, the LED starts to blink with a fixed period (SLEEP\_TIME\_MS).
When LPTIM input clock has a prescaler, longer perdiod (up to 64 seconds)
of low power can be tested.

## PM configurations

By default, [`CONFIG_PM_DEVICE`](../../../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") and [`CONFIG_PM_DEVICE_RUNTIME`](../../../../../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME") are
enabled, but user can also deactivate one or the other to see each configuration
in play.
