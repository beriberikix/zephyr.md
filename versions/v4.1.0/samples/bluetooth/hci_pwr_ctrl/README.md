---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/bluetooth/hci_pwr_ctrl/README.html
original_path: samples/bluetooth/hci_pwr_ctrl/README.html
---

# HCI Power Control

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/hci_pwr_ctrl/README.rst/..)

## Overview

This sample application demonstrates the dynamic Tx power control over the LL
of the Bluetooth LE controller via Zephyr HCI VS commands. The application implements a
peripheral advertising with varying Tx power. The initial advertiser TX power
for the first 5s of the application is the Kconfig set default TX power. Then,
the TX power variation of the advertiser is a repeatedly descending staircase
pattern ranging from -4 dBm to -30 dBm where the Tx power levels decrease every
5s.

Upon successful connection, the connection RSSI strength is being monitored and
the Tx power of the peripheral device is modulated per connection accordingly
such that energy is being saved depending on how powerful the RSSI of the
connection is. The peripheral implements a simple GATT profile exposing the
HR service notifying connected centrals about a dummy HR each 2s.

## Requirements

- BlueZ running on the host, or
- A board with Bluetooth LE support
- A central device & monitor (e.g. nRF Connect) to check the RSSI values
  obtained from the peripheral.

## Building and Running

This sample can be found under [samples/bluetooth/hci\_pwr\_ctrl](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_pwr_ctrl)
in the Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[Heart Rate Service (HRS)](../../../doxygen/html/group__bt__hrs.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
