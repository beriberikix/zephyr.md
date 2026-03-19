---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/st/bluetooth/interactive_gui/README.html
original_path: samples/boards/st/bluetooth/interactive_gui/README.html
---

# Bluetooth: ST Interactive GUI

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/bluetooth/interactive_gui/README.rst/..)

## Overview

Expose the Bluetooth network coprocessor via UART to a PC to be used
with the ST BlueNRG GUI app. In this case, the main MCU becomes an intermediate level,
and it passes the data between the host (PC) and controller.

## Requirements

- A board based on BlueNRG BLE module such as [Disco L475 IOT01 (B-L475E-IOT01A)](../../../../../boards/st/disco_l475_iot1/doc/index.md#disco_l475_iot1)
- [BlueNRG GUI](https://www.st.com/en/embedded-software/stsw-bnrgui.html) application installed on your PC

## Default UART settings

It depends on the board default settings for `zephyr,bt-c2h-uart` DTS property.
The UART default settings are:

- Baudrate: 115200 bps
- 8 bits, no parity, 1 stop bit

## Building and Running

This sample can be found under [samples/boards/st/bluetooth/interactive\_gui](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/st/bluetooth/interactive_gui) in the
Zephyr tree.

## See also

[BlueNRG HCI driver extended API](../../../../../doxygen/html/group__bluenrg__hci__driver.md)

[Bluetooth APIs](../../../../../doxygen/html/group__bluetooth.md)
