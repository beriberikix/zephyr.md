---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/bluetooth/hci_usb/README.html
original_path: samples/bluetooth/hci_usb/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth: HCI USB

## Overview

Make a USB Bluetooth dongle out of Zephyr. Requires USB device support from the
board it runs on (e.g. [nRF52840 DK](../../../boards/arm/nrf52840dk_nrf52840/doc/index.md#nrf52840dk-nrf52840) supports both BLE and USB).

## Requirements

- Bluetooth stack running on the host (e.g. BlueZ)
- A board with Bluetooth and USB support in Zephyr

## Building and Running

This sample can be found under [samples/bluetooth/hci\_usb](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_usb) in the
Zephyr tree.

See [bluetooth samples section](../bluetooth.md#bluetooth-samples) for details.
