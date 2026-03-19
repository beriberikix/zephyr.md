---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/hci_usb/README.html
original_path: samples/bluetooth/hci_usb/README.html
---

# HCI USB

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/hci_usb/README.rst/..)

## Overview

Make a USB Bluetooth dongle out of Zephyr. Requires USB device support from the
board it runs on (e.g. [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) supports both Bluetooth LE and USB).

## Requirements

- Bluetooth stack running on the host (e.g. BlueZ)
- A board with Bluetooth and USB support in Zephyr

## Building and Running

This sample can be found under [samples/bluetooth/hci\_usb](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_usb) in the
Zephyr tree.

See [Bluetooth](../bluetooth.md#bluetooth) samples for details.

## See also

[HCI RAW channel](../../../doxygen/html/group__hci__raw.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)

[USB Device Core API](../../../doxygen/html/group____usb__device__core__api.md)

[USB device core API](../../../doxygen/html/group__usbd__api.md)
