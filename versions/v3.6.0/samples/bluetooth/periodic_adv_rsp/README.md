---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/periodic_adv_rsp/README.html
original_path: samples/bluetooth/periodic_adv_rsp/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: Periodic Advertising with Responses (PAwR) Advertiser

## Overview

A simple application demonstrating the BLE Periodic Advertising with
Responses Advertiser functionality.

This sample will scan for the corresponding sync sample and send the required
synchronization info to it. The advertising data is a counter that increases
for each subevent.

Multiple devices can synchronize and respond to one advertiser.

Which subevent to listen to and in which response slot to respond is
application specific. In this sample it is decided by the PAwR advertiser.
Upon connection it will write to a GATT characteristic
the assigned subevent and response slot.

## Requirements

- A board with BLE support
- A controller that supports the Periodic Advertising with Responses (PAwR) - Advertiser feature

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_adv\_rsp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv_rsp) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_sync\_rsp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync_rsp) in the
Zephyr tree that will synchronize and respond to this sample.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
