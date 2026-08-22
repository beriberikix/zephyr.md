---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ene/kb1062_evb/doc/index.html
original_path: boards/ene/kb1062_evb/doc/index.html
---

# ENE KB1062\_EVB

Board Overview

Name:
:   `kb1062_evb`

Vendor:
:   ENE Technology, Inc.

Architecture:
:   arm

SoC:
:   kb1062

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ene/kb1062_evb/doc/index.rst/../..)

## Overview

The KB1062\_EVB kit is a development platform to evaluate the
ENE KB106X series microcontrollers. This board needs to be mated with
part number KB1062.

## Hardware

- ARM Cortex-M3 Processor
- 256KB Flash and 64KB RAM
- ADC & GPIO headers
- SER serial port
- FAN PWM interface
- ENE Debug interface

### Supported Features

The `kb1062_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The KB106x MCU is configured to use the 48Mhz internal oscillator with the
on-chip DPLL to generate a resulting EC clock rate of 48MHz/24MHz
See Processor clock control register (refer 5.1 General Configuration)

## Programming and Debugging

The `kb1062_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Flashing

If the correct headers are installed, this board supports SWD Debug Interface.

To flash with SWD, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

### Debugging

Use SWD with a J-Link

### References
