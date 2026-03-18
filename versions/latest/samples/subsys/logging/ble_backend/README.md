---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/logging/ble_backend/README.html
original_path: samples/subsys/logging/ble_backend/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# BLE logging backend

## Overview

Sample that demonstrates how to setup and use the BLE Logging backend. The
BLE Logger uses the NRF Connect SDK NUS service as UUID to make it compatible
with already existing apps to debug BLE connections over UART.

The notification size of the ble backend buffer is dependent on the
transmission size of the mtu set with CONFIG\_BT\_L2CAP\_TX\_MTU. Be sure
to change this configuration to increase the logger throughput over BLE.

## Requirements

- A board with BLE support

## Building and Running

This sample can be found under [samples/subsys/logging/ble\_backend](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/logging/ble_backend) in the
Zephyr tree.

The BLE logger can be tested with the NRF Toolbox app or any similar app that can connect over
BLE and detect the NRF NUS UUID service.
