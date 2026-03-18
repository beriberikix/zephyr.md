---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/stm32/power_mgmt/stop3/README.html
original_path: samples/boards/stm32/power_mgmt/stop3/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# STM32 PM STOP3 mode

## Overview

This sample is a minimum application to demonstrate basic power management
behavior in a basic blinking LED set up and STM32U5 STOP3 low power mode.

## Requirements

At the moment, only `nucleo_u575zi_q` board is supported.
The board shall have an RTC to use it during the standby mode as a replacement
for LPTIM (which is disabled).

## Building and Running

Build and flash examples as follows:

```shell
west build -b nucleo_u575zi_q samples/boards/stm32/power_mgmt/stop3
west flash
```

After flashing, the LED starts to blink.

## PM configurations

By default, [`CONFIG_PM_DEVICE`](../../../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") and [`CONFIG_PM_DEVICE_RUNTIME`](../../../../../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME")
are enabled.
