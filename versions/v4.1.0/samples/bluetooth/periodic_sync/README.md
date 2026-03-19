---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/periodic_sync/README.html
original_path: samples/bluetooth/periodic_sync/README.html
---

# Periodic Advertising Synchronization

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/periodic_sync/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth LE Periodic Advertising Synchronization
functionality.

## Requirements

- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_sync](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_adv](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv) on
another board that will start periodic advertising, to which this sample will
establish periodic advertising synchronization.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
