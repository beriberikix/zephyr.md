---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/central_hr/README.html
original_path: samples/bluetooth/central_hr/README.html
---

# Heart-rate Monitor (Central)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/central_hr/README.rst/..)

## Overview

Similar to the [Central](../central/README.md#ble_central "Implement basic Bluetooth LE Central role functionality (scanning and connecting).") sample, except that this
application specifically looks for heart-rate monitors and reports the
heart-rate readings once connected.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/central\_hr](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/central_hr) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
