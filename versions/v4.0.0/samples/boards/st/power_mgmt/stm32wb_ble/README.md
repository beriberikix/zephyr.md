---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/st/power_mgmt/stm32wb_ble/README.html
original_path: samples/boards/st/power_mgmt/stm32wb_ble/README.html
---

# Bluetooth Low Energy Power Management on STM32WB

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/power_mgmt/stm32wb_ble/README.rst/..)

## Overview

A simple application demonstrating the BLE operations (advertising) with
Zephyr power management enabled ([`CONFIG_PM`](../../../../../kconfig.md#CONFIG_PM "CONFIG_PM")).

After startup, a first 2 seconds beacon is performed, 1 second break and
beacon is started again.
BLE link is then disabled and started up again after 2 seconds, then same
beacon sequence happens.

Finally, platform shutdown is triggered. It can be restarted by pressing the
board reset button.

Using a power measurement tool, user can observe the platform reaching STOP2 mode
before beacon is started and between advertising peaks besides as SHUTDOWN mode
when requested.

## Requirements

- For now, only compatible with nucleo\_wb55rg.

## See also

[System power off](../../../../../doxygen/html/group__sys__poweroff.md)

[Generic Access Profile (GAP)](../../../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../../../doxygen/html/group__bluetooth.md)
