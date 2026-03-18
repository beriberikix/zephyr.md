---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/central_past/README.html
original_path: samples/bluetooth/central_past/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Central Periodic Advertising Sync Transfer (PAST)

## Overview

A simple application demonstrating the BLE Periodic Advertising Sync Transfer
functionality as the sender.

## Requirements

- A board with BLE 5.1 support

## Building and Running

This sample can be found under [samples/bluetooth/central\_past](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/central_past) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_adv](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv) on
another board that will start periodic advertising, to which this sample will
establish periodic advertising synchronization.

Use the sample found under [samples/bluetooth/peripheral\_past](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_past) in
the Zephyr tree on another board that will advertise and await a periodic
advertising sync transfer.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
