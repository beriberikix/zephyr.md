---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/observer/README.html
original_path: samples/bluetooth/observer/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Observer

## Overview

A simple application demonstrating Bluetooth Low Energy Observer role
functionality. The application will periodically scan for devices nearby.
If any found, prints the address of the device, the RSSI value, the Advertising
type, and the Advertising data length to the console.

If the used Bluetooth Low Energy Controller supports Extended Scanning, you may
enable CONFIG\_BT\_EXT\_ADV in the project configuration file. Refer to the
project configuration file for further details.

## Requirements

- A board with Bluetooth Low Energy support

## Building and Running

This sample can be found under [samples/bluetooth/observer](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/observer) in the
Zephyr tree.

See [Bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
