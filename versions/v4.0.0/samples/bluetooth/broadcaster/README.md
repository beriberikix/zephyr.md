---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/broadcaster/README.html
original_path: samples/bluetooth/broadcaster/README.html
---

# Broadcaster

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/broadcaster/README.rst/..)

## Overview

A simple application demonstrating Bluetooth Low Energy Broadcaster role functionality.
The application will periodically send out advertising packets with
a manufacturer data element. The content of the data is a single byte
indicating how many advertising packets the device has sent
(the number will roll back to 0 after 255).

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/broadcaster](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/broadcaster) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
