---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/broadcaster/README.html
original_path: samples/bluetooth/broadcaster/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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
