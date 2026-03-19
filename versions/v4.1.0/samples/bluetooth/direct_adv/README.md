---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/direct_adv/README.html
original_path: samples/bluetooth/direct_adv/README.html
---

# Direct Advertising

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/direct_adv/README.rst/..)

## Overview

Application demonstrating the Bluetooth LE Direct Advertising capability. If no device is bonded
to the peripheral, casual advertising will be performed. Once bonded, on every subsequent
boot direct advertising to the bonded central will be performed. Additionally this sample
provides two Bluetooth LE characteristics. To perform write, devices need to be bonded, while read
can be done just after connection (no bonding required).

Please note that direct advertising towards iOS based devices is not allowed.
For more information about designing Bluetooth LE devices for Apple products refer to
“Accessory Design Guidelines for Apple Devices”.

## Requirements

- A board with Bluetooth LE support
- Second Bluetooth LE device acting as a central with enabled privacy. For example another Zephyr board
  or any modern smartphone

## Building and Running

This sample can be found under [samples/bluetooth/direct\_adv](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/direct_adv) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
