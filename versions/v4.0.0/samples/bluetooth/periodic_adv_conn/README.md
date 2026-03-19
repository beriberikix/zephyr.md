---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/periodic_adv_conn/README.html
original_path: samples/bluetooth/periodic_adv_conn/README.html
---

# Periodic Advertising Connection Procedure (Initiator)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/periodic_adv_conn/README.rst/..)

## Overview

A simple application demonstrating the initiator side of the BLE
Periodic Advertising Connection Procedure.

How the initiator decides the address of the synced device to connect to
is application specific. This sample will connect to any synced device
responding with its address. Once the connection is established, it will
wait for disconnect before connecting to another synced device.

## Requirements

- A board with Bluetooth LE support
- A controller that supports the Periodic Advertising with Responses (PAwR) - Advertiser feature

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_adv\_conn](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv_conn) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_sync\_conn](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync_conn) in the
Zephyr tree that will synchronize and respond to this sample.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
