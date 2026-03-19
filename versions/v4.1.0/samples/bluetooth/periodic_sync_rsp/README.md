---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/periodic_sync_rsp/README.html
original_path: samples/bluetooth/periodic_sync_rsp/README.html
---

# Periodic Advertising with Responses (PAwR) Synchronization

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/periodic_sync_rsp/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth LE Periodic Advertising with
Responses Synchronization functionality.

This sample will echo the data received in subevent indications back to the
advertiser.

Which subevent to listen to and in which response slot to respond is
application specific. In this sample it is decided by the PAwR advertiser.
Upon connection it will write to a GATT characteristic
the assigned subevent and response slot.

Flash this sample to multiple devices and they will be given different
subevents and response slots, to that they can communicate with the
advertiser concurrently.

## Requirements

- A board with Bluetooth LE support
- A controller that supports the Periodic Advertising with Responses (PAwR) - Scanner feature

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_sync\_rsp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync_rsp) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_adv\_rsp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv_rsp) on
another board that will start periodic advertising, which will connect to this
sample and transfer the synchronization info.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
