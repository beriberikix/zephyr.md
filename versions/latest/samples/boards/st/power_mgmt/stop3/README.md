---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/st/power_mgmt/stop3/README.html
original_path: samples/boards/st/power_mgmt/stop3/README.html
---

# STOP3 mode

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/power_mgmt/stop3/README.rst/..)

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
west build -b nucleo_u575zi_q samples/boards/st/power_mgmt/stop3
west flash
```

After flashing, the LED starts to blink.

## PM configurations

By default, [`CONFIG_PM_DEVICE`](../../../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") and [`CONFIG_PM_DEVICE_RUNTIME`](../../../../../kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME")
are enabled.
