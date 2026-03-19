---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/observer/README.html
original_path: samples/bluetooth/observer/README.html
---

# Observer

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/observer/README.rst/..)

## Overview

A simple application demonstrating Bluetooth Low Energy Observer role
functionality. The application will periodically scan for devices nearby.
If any found, prints the address of the device, the RSSI value, the Advertising
type, and the Advertising data length to the console.

If the used Bluetooth Low Energy Controller supports Extended Scanning, you may
enable [`CONFIG_BT_EXT_ADV`](../../../kconfig.md#CONFIG_BT_EXT_ADV "CONFIG_BT_EXT_ADV") in the project configuration file. Refer to the
project configuration file for further details.

## Requirements

- A board with Bluetooth Low Energy support

## Building and Running

This sample can be found under [samples/bluetooth/observer](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/observer) in the
Zephyr tree.

See [Bluetooth samples section](../bluetooth.md#bluetooth) for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
