---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/periodic_sync/README.html
original_path: samples/bluetooth/periodic_sync/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Periodic Advertising Synchronization

## Overview

A simple application demonstrating the BLE Periodic Advertising Synchronization
functionality.

## Requirements

- A board with BLE support

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_sync](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_adv](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv) on
another board that will start periodic advertising, to which this sample will
establish periodic advertising synchronization.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
