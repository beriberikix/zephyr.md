---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/stm32/power_mgmt/stm32wb_ble/README.html
original_path: samples/boards/stm32/power_mgmt/stm32wb_ble/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# STM32: PM BLE Power Management (STM32WB)

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
