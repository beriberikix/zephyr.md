---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/kb2040/doc/index.html
original_path: boards/adafruit/kb2040/doc/index.html
---

# KB2040

Board Overview

[![../../../../_images/kb2040.jpg](../../../../_images/kb2040.jpg)
](../../../../_images/kb2040.jpg)

KB2040

Name:
:   `adafruit_kb2040`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/kb2040/doc/index.rst/../..)

## Overview

The Adafruit KB2040 is a small, low-cost, versatile board from
Adafruit. It is equipped with an RP2040 SoC, an on-board RGB Neopixel,
a USB connector, and a STEMMA QT connector. The USB bootloader allows
it to be flashed without any adapter, in a drag-and-drop manner.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 8MB on-board QSPI flash with XIP capabilities
- 18 GPIO pins
- 4 Analog inputs
- 1 UART peripherals
- 1 SPI controllers
- 2 I2C controllers (one via STEMMA QT connector)
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board RGB LED
- 1 Watchdog timer peripheral

### Supported Features

The `adafruit_kb2040` board supports the hardware features listed below.

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

- UART0\_TX : P0
- UART0\_RX : P1
- I2C1\_SDA : P2
- I2C1\_SCL : P3
- SPI0\_RX : P20
- SPI0\_SCK : P18
- SPI0\_TX : P19

## Programming and Debugging

### Flashing

#### Using UF2

Since it doesn’t expose the SWD pins, you must flash the Adafruit KB2040 with
a UF2 file. By default, building an app for this board will generate a
`build/zephyr/zephyr.uf2` file. If the KB2040 is powered on with the `BOOTSEL`
button pressed, it will appear on the host as a mass storage device. The
UF2 file should be drag-and-dropped to the device, which will flash the KB2040.
