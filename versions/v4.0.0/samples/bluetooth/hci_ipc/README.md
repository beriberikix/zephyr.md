---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/hci_ipc/README.html
original_path: samples/bluetooth/hci_ipc/README.html
---

# HCI IPC

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/hci_ipc/README.rst/..)

## Overview

This sample exposes [Bluetooth Controller](../../../connectivity/bluetooth/api/controller.md#bluetooth-controller) support
to another device or CPU using IPC subsystem.

## Requirements

- A board with IPC subsystem and Bluetooth LE support

## Building and Running

This sample can be found under [samples/bluetooth/hci\_ipc](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc)
in the Zephyr tree.

To use this application, you need a board with a Bluetooth controller
and IPC support.
You can then build this application and flash it onto your board in
the usual way. See [Supported Boards and Shields](../../../boards/index.md#boards) for board-specific building and
programming information.

To test this sample, you need a separate device/CPU that acts as Bluetooth
HCI IPC peer.
This sample is compatible with the HCI IPC driver provided by
Zephyr’s Bluetooth [HCI Drivers](../../../connectivity/bluetooth/api/hci_drivers.md#bt-hci-drivers) core. See the
[`CONFIG_BT_HCI_IPC`](../../../kconfig.md#CONFIG_BT_HCI_IPC "CONFIG_BT_HCI_IPC") configuration option for more information.

You might need to adjust the Kconfig configuration of this sample to make it
compatible with the peer application. For example, [`CONFIG_BT_MAX_CONN`](../../../kconfig.md#CONFIG_BT_MAX_CONN "CONFIG_BT_MAX_CONN")
must be equal to the maximum number of connections supported by the peer application.

Refer to [Bluetooth](../bluetooth.md#bluetooth) for general information about Bluetooth samples.

## See also

[HCI RAW channel](../../../doxygen/html/group__hci__raw.md)

[Bluetooth APIs](../../../doxygen/html/group__bluetooth.md)
