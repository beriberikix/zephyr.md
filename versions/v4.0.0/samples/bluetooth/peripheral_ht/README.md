---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/peripheral_ht/README.html
original_path: samples/bluetooth/peripheral_ht/README.html
---

# Health Thermometer (Peripheral)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_ht/README.rst/..)

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).") sample, except that this
application specifically exposes the HT (Health Thermometer) GATT Service.

On Nordic nRF devices, this sample uses the built-in TEMP peripheral to return
die temperature values. On other boards, it will generate dummy temperature
values.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_ht](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_ht) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Battery Service (BAS)](../../../doxygen/html/group__bt__bas.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
