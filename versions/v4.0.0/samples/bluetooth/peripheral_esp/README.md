---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/peripheral_esp/README.html
original_path: samples/bluetooth/peripheral_esp/README.html
---

# ESP Peripheral

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_esp/README.rst/..)

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).") sample, except that this
application specifically exposes the ESP (Environmental Sensing Profile) GATT
Service.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_esp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_esp) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Attribute Profile (GATT)](../../../doxygen/html/group__bt__gatt.md)

[Battery Service (BAS)](../../../doxygen/html/group__bt__bas.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
