---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/renesas/ek_ra2l1/doc/index.html
original_path: boards/renesas/ek_ra2l1/doc/index.html
---

# ek\_ra2l1

Board Overview

[![../../../../_images/ek_ra2l1.webp](../../../../_images/ek_ra2l1.webp)
](../../../../_images/ek_ra2l1.webp)

ek\_ra2l1

Name:
:   `ek_ra2l1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa2l1abxxfp

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_ra2l1/doc/index.rst/../..)

## Overview

The EK-RA2L1 is an evaluation kit for Renesas RA2L1 Microcontroller Group.

Renesas RA2L1 Microcontroller Group has following features

- 48MHz, Arm Cortex-M23 core
- 256kB or 128kB Code Flash, 8kB Data Flash, 32kB SRAM (divided on 2 equal areas
  with- and without- ECC support)
- SCI x 5
- SPI x 2
- I2C x 2
- CAN x 1
- 12-bit A/D Converter
- 12-bit D/A Converter
- Low-Power Analog Comparator x 2
- Temperature Sensor
- General PWM Timer 32-bit x 4
- General PWM Timer 16-bit x 6
- Low Power Asynchronous General-Purpose Timer x 2
- Watchdog Timer (WDT)
- Independent Watchdog Timer (IWDT)
- up to 85 Input/Output pins (depends on the package type)

## Hardware

EK-RA2L1 has following features.

- Native pin access through 1 x 40-pin and 3 x 20-pin male headers
- MCU current measurement points for precision current consumption measurement
- Multiple clock sources – Low-precision clocks are available internal to the MCU.
  Additionally, MCU oscillator and sub-clock oscillator crystals,
  20.000 MHz and 32,768 Hz, are provided for precision
- SEGGER J-Link on-board programmer and debugger
- Two Digilent Pmod (SPI and UART)
- Three user LEDs (red, blue, green)
- Power LED (white) indicating availability of regulated power
- Debug LED (yellow) indicating the debug connection
- Two user buttons
- One reset button

### Supported Features

The `ek_ra2l1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and debugging

### Building & Flashing

You can build and flash an application with onboard J-Link debug adapter.
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ek_ra2l1 samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done with onboard J-Link debug adapter.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b ek_ra2l1 samples/basic/blinky
west debug
```

Or you can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA2L1AB
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

## References
