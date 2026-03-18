---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/bluetooth/hci_usb_h4/README.html
original_path: samples/bluetooth/hci_usb_h4/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: HCI H4 over USB

## Overview

Make a USB H4 Bluetooth dongle out of Zephyr. Requires USB device support from
the board it runs on (e.g. [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) supports both BLE and
USB).

## Requirements

- Bluetooth stack running on the host (e.g. BlueZ)
- A board with Bluetooth and USB support in Zephyr

## Building and Running

This sample can be found under [samples/bluetooth/hci\_usb\_h4](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_usb_h4) in
the Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
