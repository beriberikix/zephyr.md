---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/broadcaster/README.html
original_path: samples/bluetooth/broadcaster/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Broadcaster

## Overview

A simple application demonstrating Bluetooth Low Energy Broadcaster role functionality.
The application will periodically send out advertising packets with
a manufacturer data element. The content of the data is a single byte
indicating how many advertising packets the device has sent
(the number will roll back to 0 after 255).

## Requirements

- BlueZ running on the host, or
- A board with BLE support

## Building and Running

This sample can be found under [samples/bluetooth/broadcaster](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/broadcaster) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
