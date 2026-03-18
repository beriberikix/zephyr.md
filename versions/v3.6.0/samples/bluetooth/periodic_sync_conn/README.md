---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/periodic_sync_conn/README.html
original_path: samples/bluetooth/periodic_sync_conn/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Periodic Advertising Connection Procedure - Responder

## Overview

A simple application demonstrating the responder side of the BLE
Periodic Advertising Connection Procedure.

This sample will send its address in response to the advertiser when receiving
subevent data. Once the connection is established, it will disconnect and wait
for a new connection to be established.

## Requirements

- A board with BLE support
- A controller that supports the Periodic Advertising with Responses (PAwR) - Scanner feature

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_sync\_conn](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync_conn) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_adv\_conn](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv_conn) on
another board that will start periodic advertising and connect to this sample
once synced.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
