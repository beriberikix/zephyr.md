---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/periodic_sync_conn/README.html
original_path: samples/bluetooth/periodic_sync_conn/README.html
---

# Periodic Advertising Connection Procedure (Responder)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/periodic_sync_conn/README.rst/..)

## Overview

A simple application demonstrating the responder side of the BLE
Periodic Advertising Connection Procedure.

This sample will send its address in response to the advertiser when receiving
subevent data. Once the connection is established, it will disconnect and wait
for a new connection to be established.

## Requirements

- A board with Bluetooth LE support
- A controller that supports the Periodic Advertising with Responses (PAwR) - Scanner feature

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_sync\_conn](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync_conn) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_adv\_conn](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv_conn) on
another board that will start periodic advertising and connect to this sample
once synced.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
