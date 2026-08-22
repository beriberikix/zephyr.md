---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/sparkfun/pro_micro_rp2040/doc/index.html
original_path: boards/sparkfun/pro_micro_rp2040/doc/index.html
---

# Pro Micro RP2040

Board Overview

[![../../../../_images/sparkfun_pro_micro_rp2040.jpg](../../../../_images/sparkfun_pro_micro_rp2040.jpg)
](../../../../_images/sparkfun_pro_micro_rp2040.jpg)

Pro Micro RP2040

Name:
:   `sparkfun_pro_micro_rp2040`

Vendor:
:   SparkFun Electronics

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/sparkfun/pro_micro_rp2040/doc/index.rst/../..)

## Overview

The SparkFun Pro Micro RP2040 is a small, low-cost, versatile board from
SparkFun. It is equipped with an RP2040 SoC, an on-board WS2812 addressable
LED, a USB connector, and a Qwiic connector. The USB bootloader allows it
to be flashed without any adapter, in a drag-and-drop manner.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 16MB on-board QSPI flash with XIP capabilities
- 18 GPIO pins
- 4 Analog inputs
- 1 UART peripherals
- 1 SPI controllers
- 2 I2C controllers (one via Qwiic connector)
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board RGB LED
- 1 Watchdog timer peripheral

### Supported Features

The `sparkfun_pro_micro_rp2040` board supports the hardware features listed below.

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
- SPI0\_SCK : P22
- SPI0\_TX : P23

## Programming and Debugging

The `sparkfun_pro_micro_rp2040` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Flashing

#### Using UF2

The Pro Micro board does make the SWD pins available on pads on the
underside of the board. You can solder to these pins, and use a JTag
debugger. You can also flash the SparkFun ProMicro RP2040 with a UF2 file.
By default, building an app for this board will generate a
`build/zephyr/zephyr.uf2` file. If the Pro Micro RP2040 is powered on with
the `BOOTSEL` button pressed, it will appear on the host as a mass storage
device. The UF2 file should be copied to the device, which will
flash the Pro Micro RP2040.
