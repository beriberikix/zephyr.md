---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/peripheral_hids/README.html
original_path: samples/bluetooth/peripheral_hids/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Peripheral HIDs

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble-peripheral) sample, except that this
application specifically exposes the HID GATT Service. The report map used is
for a generic mouse.

In the default configuration the sample uses passkey authentication (displays a
code on the peripheral and requires that to be entered on the host during
pairing) and requires an authenticated link to access the GATT characteristics.
To disable authentication and just use encrypted channels instead, build the
sample with CONFIG\_SAMPLE\_BT\_USE\_AUTHENTICATION=n.

## Requirements

- BlueZ running on the host, or
- A board with BLE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_hids](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_hids) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
