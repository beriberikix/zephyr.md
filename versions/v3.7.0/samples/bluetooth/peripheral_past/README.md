---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/peripheral_past/README.html
original_path: samples/bluetooth/peripheral_past/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Periodic Advertising Synchronization Transfer

## Overview

A simple application demonstrating the BLE Periodic Advertising Synchronization
Transfer (PAST) functionality as the receiver.

## Requirements

- A board with BLE 5.1 support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_past](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_past)
in the Zephyr tree.

Use the sample found under [samples/bluetooth/central\_past](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/central_past) on
another board that will connect to this and transfer a periodic advertisement
sync.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
