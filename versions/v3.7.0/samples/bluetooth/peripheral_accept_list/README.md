---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/peripheral_accept_list/README.html
original_path: samples/bluetooth/peripheral_accept_list/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Peripheral Accept List

## Overview

This application demonstrates the BLE advertising accept filter list feature.
If no device is bonded to the peripheral, casual advertising will be performed.
Once a device is bonded, on subsequent boots, connection requests will only be
accepted if the central device is on the accept list. Additionally, scan response
data will only be sent to devices that are on the accept list. As a result, some
BLE central devices (such as Android smartphones) might not display the device
in the scan results if the central device is not on the accept list.

This sample also provides two BLE characteristics. To perform a write, devices need
to be bonded, while a read can be done immediately after a connection
(no bonding required).

## Requirements

- A board with BLE support
- Second BLE device acting as a central. For example another Zephyr board or smartphone

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_accept\_list](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_accept_list) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
