---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/logging/ble_backend/README.html
original_path: samples/subsys/logging/ble_backend/README.html
---

# Bluetooth logging backend

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/logging/ble_backend/README.rst/..)

## Overview

Sample that demonstrates how to setup and use the Bluetooth Logging backend. The
Bluetooth Logger uses the NRF Connect SDK NUS service as UUID to make it compatible
with already existing apps to debug Bluetooth connections over UART.

The notification size of the Bluetooth backend buffer is dependent on the
transmission size of the mtu set with [`CONFIG_BT_L2CAP_TX_MTU`](../../../../kconfig.md#CONFIG_BT_L2CAP_TX_MTU "CONFIG_BT_L2CAP_TX_MTU"). Be sure
to change this configuration to increase the logger throughput over Bluetooth.

## Requirements

- A board with Bluetooth LE support

## Building and Running

This sample can be found under [samples/subsys/logging/ble\_backend](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/logging/ble_backend) in the
Zephyr tree.

The Bluetooth logger can be tested with the NRF Toolbox app or any similar app that can connect over
Bluetooth and detect the NRF NUS UUID service.

## See also

[Logging API](../../../../doxygen/html/group__log__api.md)

[Logger backend interface](../../../../doxygen/html/group__log__backend.md)

[Generic Attribute Profile (GATT)](../../../../doxygen/html/group__bt__gatt.md)
