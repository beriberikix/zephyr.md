---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/peripheral_iso/README.html
original_path: samples/bluetooth/peripheral_iso/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Peripheral ISO

## Overview

Similar to the [Peripheral](../peripheral/README.md#ble-peripheral) sample, except that this application enables
support for connected isochronous (ISO) channels.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth Low Energy 5.2 support
- A Bluetooth Controller and board that supports setting
  CONFIG\_BT\_CTLR\_PERIPHERAL\_ISO=y

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_iso](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_iso) in the Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
