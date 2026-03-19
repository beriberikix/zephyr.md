---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/peripheral_hr/README.html
original_path: samples/bluetooth/peripheral_hr/README.html
---

# Heart-rate Monitor (Peripheral)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_hr/README.rst/..)

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).") sample, except that this
application specifically exposes the HR (Heart Rate) GATT Service. Once a device
connects it will generate dummy heart-rate values.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_hr](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_hr) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Heart Rate Service (HRS)](../../../doxygen/html/group__bt__hrs.md)

[Battery Service (BAS)](../../../doxygen/html/group__bt__bas.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
