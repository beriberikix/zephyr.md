---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/peripheral_past/README.html
original_path: samples/bluetooth/peripheral_past/README.html
---

# Periodic Advertising Synchronization Transfer Peripheral

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_past/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth LE Periodic Advertising Synchronization
Transfer (PAST) functionality as the receiver.

## Requirements

- A board with Bluetooth LE 5.1 support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_past](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_past)
in the Zephyr tree.

Use the sample found under [samples/bluetooth/central\_past](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/central_past) on
another board that will connect to this and transfer a periodic advertisement
sync.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
