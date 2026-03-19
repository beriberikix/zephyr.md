---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/peripheral_hids/README.html
original_path: samples/bluetooth/peripheral_hids/README.html
---

# HID Peripheral

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_hids/README.rst/..)

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).") sample, except that this
application specifically exposes the HID GATT Service. The report map used is
for a generic mouse.

In the default configuration the sample uses passkey authentication (displays a
code on the peripheral and requires that to be entered on the host during
pairing) and requires an authenticated link to access the GATT characteristics.
To disable authentication and just use encrypted channels instead, build the
sample with `CONFIG_SAMPLE_BT_USE_AUTHENTICATION=n`.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_hids](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_hids) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Attribute Profile (GATT)](../../../doxygen/html/group__bt__gatt.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
