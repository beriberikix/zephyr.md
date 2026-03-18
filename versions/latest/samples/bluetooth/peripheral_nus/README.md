---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/peripheral_nus/README.html
original_path: samples/bluetooth/peripheral_nus/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: Peripheral NUS

## Overview

This sample demonstrates the usage of the NUS service (Nordic UART Service) as a serial
endpoint to exchange data. In this case, the sample assumes the data is UTF-8 encoded,
but it may be binary data. Once the user connects to the device and subscribes to the TX
characteristic, it will start receiving periodic notifications with “Hello World!n”.

## Requirements

- BlueZ running on the host, or
- A board with BLE support

## Building and Running

This sample can be found under [samples/bluetooth/peripheral\_nus](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/peripheral_nus) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
