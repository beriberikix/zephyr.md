---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/periodic_adv_conn/README.html
original_path: samples/bluetooth/periodic_adv_conn/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Periodic Advertising Connection Procedure - Initiator

## Overview

A simple application demonstrating the initiator side of the BLE
Periodic Advertising Connection Procedure.

How the initiator decides the address of the synced device to connect to
is application specific. This sample will connect to any synced device
responding with its address. Once the connection is established, it will
wait for disconnect before connecting to another synced device.

## Requirements

- A board with BLE support
- A controller that supports the Periodic Advertising with Responses (PAwR) - Advertiser feature

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_adv\_conn](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv_conn) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_sync\_conn](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync_conn) in the
Zephyr tree that will synchronize and respond to this sample.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
