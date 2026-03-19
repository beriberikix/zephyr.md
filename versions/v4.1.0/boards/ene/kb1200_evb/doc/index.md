---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ene/kb1200_evb/doc/index.html
original_path: boards/ene/kb1200_evb/doc/index.html
---

# ENE KB1200\_EVB

Board Overview

Name:
:   `kb1200_evb`

Vendor:
:   ENE Technology, Inc.

Architecture:
:   arm

SoC:
:   kb1200

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ene/kb1200_evb/doc/index.rst/../..)

## Overview

The KB1200\_EVB kit is a development platform to evaluate the
ENE KB1200 series microcontrollers. This board needs to be mated with
part number KB1200.

## Hardware

- ARM Cortex-M4F Processor
- 512KB Flash and 320KB RAM
- ADC & GPIO headers
- SER1, SER2 and SER3
- FAN PWM interface
- ENE Debug interface

### Supported Features

The `kb1200_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The KB1200 MCU is configured to use the 96Mhz internal oscillator with the
on-chip DPLL to generate a resulting EC clock rate of 96MHz/48MHz/24MHz/12MHz.
See Processor clock control register (refer 5.1 General Configuration)

## Programming and Debugging

### Flashing

If the correct headers are installed, this board supports SWD Debug Interface.

To flash with SWD, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

### Debugging

Use SWD with a J-Link

### References
