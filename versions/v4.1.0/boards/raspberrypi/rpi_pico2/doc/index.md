---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/raspberrypi/rpi_pico2/doc/index.html
original_path: boards/raspberrypi/rpi_pico2/doc/index.html
---

# Raspberry Pi Pico 2

Board Overview

[![../../../../_images/rpi_pico2.webp](../../../../_images/rpi_pico2.webp)
](../../../../_images/rpi_pico2.webp)

Raspberry Pi Pico 2

Name:
:   `rpi_pico2`

Vendor:
:   Raspberry Pi Foundation

Architecture:
:   arm

SoC:
:   rp2350a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/raspberrypi/rpi_pico2/doc/index.rst/../..)

## Overview

The Raspberry Pi Pico 2 is the second-generation product in the Raspberry Pi
Pico family. From the [Raspberry Pi website](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) is referred to as Pico 2.

There are many limitations of the board currently. Including but not limited to:
- The Zephyr build only supports configuring the RP2350A with the Cortex-M33 cores.
- As with the Pico 1, there’s no support for running any code on the second core.

## Hardware

- Dual Cortex-M33 or Hazard3 processors at up to 150MHz
- 520KB of SRAM, and 4MB of on-board flash memory
- USB 1.1 with device and host support
- Low-power sleep and dormant modes
- Drag-and-drop programming using mass storage over USB
- 26 multi-function GPIO pins including 3 that can be used for ADC
- 2 SPI, 2 I2C, 2 UART, 3 12-bit 500ksps Analogue to Digital - Converter (ADC), 24 controllable PWM channels
- 2 Timer with 4 alarms, 1 AON Timer
- Temperature sensor
- 3 Programmable IO (PIO) blocks, 12 state machines total for custom peripheral support

  - Flexible, user-programmable high-speed IO
  - Can emulate interfaces such as SD Card and VGA

### Supported Features

The `rpi_pico2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The default pin mapping is unchanged from the Pico 1 (see [Pin Mapping](../../rpi_pico/doc/index.md#rpi-pico-pin-mapping)).

## Programming and Debugging

As with the Pico 1, the SWD interface can be used to program and debug the
device, e.g. using OpenOCD with the [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) .

## References
