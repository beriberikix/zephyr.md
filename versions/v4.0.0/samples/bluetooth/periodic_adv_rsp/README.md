---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/periodic_adv_rsp/README.html
original_path: samples/bluetooth/periodic_adv_rsp/README.html
---

# Periodic Advertising with Responses (PAwR) Advertiser

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/periodic_adv_rsp/README.rst/..)

## Overview

A simple application demonstrating the Bluetooth LE Periodic Advertising with
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

- A board with Bluetooth LE support
- A controller that supports the Periodic Advertising with Responses (PAwR) - Advertiser feature

## Building and Running

This sample can be found under [samples/bluetooth/periodic\_adv\_rsp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_adv_rsp) in
the Zephyr tree.

Use the sample found under [samples/bluetooth/periodic\_sync\_rsp](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/periodic_sync_rsp) in the
Zephyr tree that will synchronize and respond to this sample.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Generic Access Profile (GAP)](../../../doxygen/html/group__bt__gap.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
