---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/scan_adv/README.html
original_path: samples/bluetooth/scan_adv/README.html
---

# Scan & Advertise

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/scan_adv/README.rst/..)

## Overview

A simple application demonstrating combined Bluetooth LE Broadcaster & Observer
role functionality. The application will periodically send out
advertising packets with a manufacturer data element. The content of the
data is a single byte indicating how many advertising packets the device
has received (the number will roll back to 0 after 255).

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/scan\_adv](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/scan_adv) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
