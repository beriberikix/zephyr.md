---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/central_otc/README.html
original_path: samples/bluetooth/central_otc/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Central OTC

## Overview

Similar to the [Central](../central/README.md#bluetooth-central) sample, except that this
application specifically looks for the OTS (Object Transfer) GATT Service.
And this sample is to select object sequentially, to read metadata, to write data,
to read data, and to calculate checksum of selected objects.

## Requirements

- A board with BLE support and 4 buttons.

## Building and Running

This sample can be found under [samples/bluetooth/central\_otc](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/central_otc) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
