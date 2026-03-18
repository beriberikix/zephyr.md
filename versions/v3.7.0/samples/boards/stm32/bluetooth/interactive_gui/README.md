---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/stm32/bluetooth/interactive_gui/README.html
original_path: samples/boards/stm32/bluetooth/interactive_gui/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth: ST Interactive GUI

Expose ST BlueNRG Bluetooth network coprocessor over UART

## Overview

Expose the Bluetooth network coprocessor via UART to a PC to be used
with the ST BlueNRG GUI app. In this case, the main MCU becomes an intermediate level,
and it passes the data between the host (PC) and controller.

## Requirements

- A board based on BlueNRG BLE module such as [ST Disco L475 IOT01 (B-L475E-IOT01A)](../../../../../boards/st/disco_l475_iot1/doc/index.md#disco-l475-iot1-board)
- [BlueNRG GUI](https://www.st.com/en/embedded-software/stsw-bnrgui.html) application installed on your PC

## Default UART settings

It depends on the board default settings for `zephyr,bt-c2h-uart` DTS property.
The UART default settings are:

- Baudrate: 115200 bps
- 8 bits, no parity, 1 stop bit

## Building and Running

This sample can be found under [samples/boards/stm32/bluetooth/interactive\_gui](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/stm32/bluetooth/interactive_gui) in the
Zephyr tree.
