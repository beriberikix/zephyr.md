---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/qt_py_rp2040/doc/index.html
original_path: boards/adafruit/qt_py_rp2040/doc/index.html
---

# QT Py RP2040

Board Overview

[![../../../../_images/qtpy_rp2040.jpg](../../../../_images/qtpy_rp2040.jpg)
](../../../../_images/qtpy_rp2040.jpg)

QT Py RP2040

Name:
:   `adafruit_qt_py_rp2040`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/qt_py_rp2040/doc/index.rst/../..)

## Overview

The Adafruit QT Py RP2040 is a small, low-cost, versatile board from
Adafruit. It is equipped with an RP2040 SoC, an on-board RGB Neopixel,
a USB connector, and a STEMMA QT connector. The USB bootloader allows
it to be flashed without any adapter, in a drag-and-drop manner.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 8MB on-board QSPI flash with XIP capabilities
- 11 GPIO pins
- 4 Analog inputs
- 2 UART peripherals
- 2 SPI controllers
- 2 I2C controllers (one via STEMMA QT connector)
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board RGB LED
- 1 Watchdog timer peripheral

### Supported Features

The `adafruit_qt_py_rp2040` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

#### Default Zephyr Peripheral Mapping:

- UART1\_TX : P20
- UART1\_RX : P5
- I2C0\_SDA : P24
- I2C0\_SCL : P25
- I2C1\_SDA : P22
- I2C1\_SCL : P23
- SPI0\_RX : P4
- SPI0\_SCK : P6
- SPI0\_TX : P3

## Programming and Debugging

### Flashing

#### Using UF2

Since it doesn’t expose the SWD pins, you must flash the Adafruit QT Py RP2040 with
a UF2 file. By default, building an app for this board will generate a
`build/zephyr/zephyr.uf2` file. If the QT Py RP2040 is powered on with the `BOOTSEL`
button pressed, it will appear on the host as a mass storage device. The
UF2 file should be drag-and-dropped to the device, which will flash the QT Py RP2040.
