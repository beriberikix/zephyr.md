---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/peripheral_hr/README.html
original_path: samples/bluetooth/peripheral_hr/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Peripheral HR

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble-peripheral) sample, except that this
application specifically exposes the HR (Heart Rate) GATT Service. Once a device
connects it will generate dummy heart-rate values.

## Requirements

- BlueZ running on the host, or
- A board with BLE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_hr](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_hr) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
