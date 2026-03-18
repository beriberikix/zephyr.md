---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/broadcaster_multiple/README.html
original_path: samples/bluetooth/broadcaster_multiple/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Multiple Broadcaster

## Overview

A simple application demonstrating the Bluetooth Low Energy Broadcaster that
uses multiple advertising sets functionality.

This sample advertises two non-connectable non-scannable advertising sets with
two different SID. Number of advertising sets can be increased by updating the
CONFIG\_BT\_EXT\_ADV\_MAX\_ADV\_SET value in the project configuration file.

When building this sample combined with a Bluetooth LE Controller, the
advertising data length can be increased from the default 31 bytes by updating
the Controller’s CONFIG\_BT\_CTLR\_ADV\_DATA\_LEN\_MAX value. The size of the
manufacturer data is calculated to maximize the use of supported AD data length.

## Requirements

- A board with Bluetooth Low Energy with Extended Advertising support.

## Building and Running

This sample can be found under
[samples/bluetooth/broadcaster\_multiple](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/broadcaster_multiple) in the Zephyr tree.

To test this sample use the Observer sample with Extended Scanning enabled,
found under
[samples/bluetooth/observer](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/observer) in the Zephyr tree.

See [Bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
