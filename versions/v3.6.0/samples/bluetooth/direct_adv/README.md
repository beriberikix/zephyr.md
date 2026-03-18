---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/direct_adv/README.html
original_path: samples/bluetooth/direct_adv/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Direct Advertising

## Overview

Application demonstrating the BLE Direct Advertising capability. If no device is bonded
to the peripheral, casual advertising will be performed. Once bonded, on every subsequent
boot direct advertising to the bonded central will be performed. Additionally this sample
provides two BLE characteristics. To perform write, devices need to be bonded, while read
can be done just after connection (no bonding required).

Please note that direct advertising towards iOS based devices is not allowed.
For more information about designing BLE devices for Apple products refer to
“Accessory Design Guidelines for Apple Devices”.

## Requirements

- A board with BLE support
- Second BLE device acting as a central with enabled privacy. For example another Zephyr board
  or any modern smartphone

## Building and Running

This sample can be found under [samples/bluetooth/direct\_adv](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direct_adv) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
