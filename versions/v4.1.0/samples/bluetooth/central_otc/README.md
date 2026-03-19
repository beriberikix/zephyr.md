---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/central_otc/README.html
original_path: samples/bluetooth/central_otc/README.html
---

# Central OTC

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/central_otc/README.rst/..)

## Overview

Similar to the [Central](../central/README.md#ble_central "Implement basic Bluetooth LE Central role functionality (scanning and connecting).") sample, except that this
application specifically looks for the OTS (Object Transfer) GATT Service.
And this sample is to select object sequentially, to read metadata, to write data,
to read data, and to calculate checksum of selected objects.

## Requirements

- A board with Bluetooth LE support and 4 buttons.

## Building and Running

This sample can be found under [samples/bluetooth/central\_otc](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/central_otc) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
