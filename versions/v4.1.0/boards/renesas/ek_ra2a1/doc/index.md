---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/renesas/ek_ra2a1/doc/index.html
original_path: boards/renesas/ek_ra2a1/doc/index.html
---

# RA2A1 Evaluation Kit

Board Overview

[![../../../../_images/ek_ra2a1.webp](../../../../_images/ek_ra2a1.webp)
](../../../../_images/ek_ra2a1.webp)

RA2A1 Evaluation Kit

Name:
:   `ek_ra2a1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa2a1ab3cfm

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_ra2a1/doc/index.rst/../..)

## Overview

The EK-RA2A1 is an evaluation kit for Renesas RA2A1 Microcontroller Group.

Renesas RA2A1 Microcontroller Group has following features

- 48MHz, Arm Cortex-M23 core
- 256kB Code Flash, 8kB Data Flash, 32kB SRAM
- USB 2.0 Full-Sppeed
- SCI x 3
- SPI x 2
- I2C x 2
- CAN x 1
- 16-bit A/D Converter
- 24-bit Sigma-Delta A/D Converter
- 12-bit D/A Converter
- 8-bit D/A Converter x 2
- High-Speed Analog Comparator
- Low-Power Analog Comparator
- OPAMP x 3
- Temperature Sensor
- General PWM Timer 32-bit x 1
- General PWM Timer 16-bit x 6
- Low Power Asynchronous General-Purpose Timer x 2
- Watchdog Timer
- 49 Input/Output pins

## Hardware

Detail Hardware feature for the RA2A1 MCU group can be found at [RA2A1 Group User’s Manual Hardware](https://www.renesas.com/en/document/mah/renesas-ra2a1-group-users-manual-hardware) [[1]](#id3)

[![RA2A1 MCU group feature](../../../../_images/ra2a1_block_diagram.webp)
](../../../../_images/ra2a1_block_diagram.webp)

RA2A1 Block diagram (Credit: Renesas Electronics Corporation)

Detail Hardware feature for the EK-RA2A1 MCU can be found at [EK-RA2A1 - User’s Manual](https://www.renesas.com/en/document/mah/renesas-ra2a1-group-users-manual-hardware) [[1]](#id3)

EK-RA2A1 has following features.

- Native pin access through 4x 40-pin male headers
- MCU current measurement points
- SEGGER J-Link on-board programmer and debugger
- Two Digilent Pmod (SPI and UART)
- User LED
- Mechanical user button
- Capacitive user button

### Supported Features

The `ek_ra2a1` board supports the hardware features listed below.

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
[Run an Application](../../../../develop/application/index.md#application-run) for more details.

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ek_ra2a1 samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done with onboard J-Link debug adapter.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b ek_ra2a1 samples/basic/blinky
west debug
```

## References

[1]
([1](#id4),[2](#id5))

[https://www.renesas.com/en/document/mah/renesas-ra2a1-group-users-manual-hardware](https://www.renesas.com/en/document/mah/renesas-ra2a1-group-users-manual-hardware)
