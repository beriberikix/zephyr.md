---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/peripheral_accept_list/README.html
original_path: samples/bluetooth/peripheral_accept_list/README.html
---

# Peripheral Accept List

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_accept_list/README.rst/..)

## Overview

This application demonstrates the Bluetooth LE advertising accept filter list feature.
If no device is bonded to the peripheral, casual advertising will be performed.
Once a device is bonded, on subsequent boots, connection requests will only be
accepted if the central device is on the accept list. Additionally, scan response
data will only be sent to devices that are on the accept list. As a result, some
BLE central devices (such as Android smartphones) might not display the device
in the scan results if the central device is not on the accept list.

This sample also provides two Bluetooth LE characteristics. To perform a write, devices need
to be bonded, while a read can be done immediately after a connection
(no bonding required).

## Requirements

- A board with Bluetooth LE support
- Second Bluetooth LE device acting as a central. For example another Zephyr board or smartphone

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_accept\_list](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_accept_list) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Connection management](../../../doxygen/html/group__bt__conn.md)

[Generic Attribute Profile (GATT)](../../../doxygen/html/group__bt__gatt.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
