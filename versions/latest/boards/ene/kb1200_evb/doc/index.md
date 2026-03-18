---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/ene/kb1200_evb/doc/index.html
original_path: boards/ene/kb1200_evb/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ENE KB1200\_EVB

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

The following features are supported:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| ADC | on-chip | adc controller |
| CLOCK | on-chip | reset and clock control |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c port/controller |
| PINMUX | on-chip | pinmux |
| PMU | on-chip | power management |
| PSL | on-chip | power switch logic |
| PWM | on-chip | pulse width modulator |
| TACH | on-chip | tachometer sensor |
| SER | on-chip | serial port-polling; serial port-interrupt |
| WDT | on-chip | watchdog |

Other hardware features are not currently supported by Zephyr (at the moment)

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
