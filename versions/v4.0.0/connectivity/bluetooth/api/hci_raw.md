---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/api/hci_raw.html
original_path: connectivity/bluetooth/api/hci_raw.html
---

# HCI RAW channel

## Overview

HCI RAW channel API is intended to expose HCI interface to the remote entity.
The local Bluetooth controller gets owned by the remote entity and host
Bluetooth stack is not used. RAW API provides direct access to packets which
are sent and received by the Bluetooth HCI driver.

## API Reference

[HCI RAW channel](../../../doxygen/html/group__hci__raw.md)

Related code samples

- [HCI 3-wire (H:5)](../../../samples/bluetooth/hci_uart_3wire/README.md#bluetooth_hci_uart_3wire "Expose a Bluetooth controller to another device or CPU over H5:HCI transport.")Expose a Bluetooth controller to another device or CPU over H5:HCI transport.
- [HCI H4 over USB](../../../samples/bluetooth/hci_usb_h4/README.md#bluetooth_hci_usb_h4 "Turn a Zephyr board into a USB H4 Bluetooth dongle (Linux/BlueZ only).")Turn a Zephyr board into a USB H4 Bluetooth dongle (Linux/BlueZ only).
- [HCI IPC](../../../samples/bluetooth/hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.")Expose a Bluetooth controller to another device or CPU using the IPC subsystem.
- [HCI SPI](../../../samples/bluetooth/hci_spi/README.md#bluetooth_hci_spi "Expose a Bluetooth controller to another device or CPU over SPI.")Expose a Bluetooth controller to another device or CPU over SPI.
- [HCI UART](../../../samples/bluetooth/hci_uart/README.md#bluetooth_hci_uart "Expose a Bluetooth controller to another device or CPU over UART.")Expose a Bluetooth controller to another device or CPU over UART.
- [HCI UART async](../../../samples/bluetooth/hci_uart_async/README.md#bluetooth_hci_uart_async "Expose a Bluetooth controller to another device or CPU over asynchronous UART.")Expose a Bluetooth controller to another device or CPU over asynchronous UART.
- [HCI USB](../../../samples/bluetooth/hci_usb/README.md#bluetooth_hci_usb "Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).")Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).
