---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/broadcaster_multiple/README.html
original_path: samples/bluetooth/broadcaster_multiple/README.html
---

# Multiple Broadcaster

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/broadcaster_multiple/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth Low Energy Broadcaster that
uses multiple advertising sets functionality.

This sample advertises two non-connectable non-scannable advertising sets with
two different SID. Number of advertising sets can be increased by updating the
[`CONFIG_BT_EXT_ADV_MAX_ADV_SET`](../../../kconfig.md#CONFIG_BT_EXT_ADV_MAX_ADV_SET "CONFIG_BT_EXT_ADV_MAX_ADV_SET") value in the project configuration file.

When building this sample combined with a Bluetooth LE Controller, the
advertising data length can be increased from the default 31 bytes by updating
the Controller’s [`CONFIG_BT_CTLR_ADV_DATA_LEN_MAX`](../../../kconfig.md#CONFIG_BT_CTLR_ADV_DATA_LEN_MAX "CONFIG_BT_CTLR_ADV_DATA_LEN_MAX") value. The size of the
manufacturer data is calculated to maximize the use of supported AD data length.

## Requirements

- A board with Bluetooth Low Energy with Extended Advertising support.

## Building and Running

This sample can be found under
[samples/bluetooth/broadcaster\_multiple](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/broadcaster_multiple) in the Zephyr tree.

To test this sample use the Observer sample with Extended Scanning enabled,
found under
[samples/bluetooth/observer](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/observer) in the Zephyr tree.

See [Bluetooth samples section](../bluetooth.md#bluetooth) for details.

## See also

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
