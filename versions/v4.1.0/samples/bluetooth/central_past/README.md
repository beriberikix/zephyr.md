---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/central_past/README.html
original_path: samples/bluetooth/central_past/README.html
---

# Central Periodic Advertising Sync Transfer (PAST)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/central_past/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth LE Periodic Advertising Sync Transfer
functionality as the sender.

## Requirements

- A board with Bluetooth LE 5.1 support

## Building and Running

This sample can be found under [samples/bluetooth/central\_past](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/central_past) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_adv](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv) on
another board that will start periodic advertising, to which this sample will
establish periodic advertising synchronization.

Use the sample found under [samples/bluetooth/peripheral\_past](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_past) in
the Zephyr tree on another board that will advertise and await a periodic
advertising sync transfer.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
