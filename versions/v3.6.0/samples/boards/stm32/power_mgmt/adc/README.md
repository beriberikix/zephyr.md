---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/stm32/power_mgmt/adc/README.html
original_path: samples/boards/stm32/power_mgmt/adc/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# STM32 PM ADC

## Overview

This sample is a minimum application to demonstrate basic power management
behavior in a basic ADC set up in low power context.

## Requirements

The board should support enabling PM. For a STM32 based target, it means that
it should support a clock source alternative to Cortex Systick that can be used
in core sleep states, as LPTIM ([`st,stm32-lptim`](../../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim)).

## Building and Running

Build and flash as follows, changing `nucleo_wb55rg` for your board:

```shell
west build -b nucleo_wb55rg samples/boards/stm32/power_mgmt/adc
west flash
```

After flashing, the console shows the ADC measurement in the form:
`ADC reading[0]:`
`- adc@50040000, channel 3: 1158 = 932 mV`

## PM configurations

By default, [`CONFIG_PM_DEVICE`](../../../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") and [`CONFIG_PM_DEVICE_RUNTIME`](../../../../../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME") are
enabled.
On STM32WB, we can observe a power consumption of about 25µA with both kconfig
enabled, 27.5µA without (each time with [`CONFIG_PM`](../../../../../kconfig.md#CONFIG_PM "CONFIG_PM") enabled).
