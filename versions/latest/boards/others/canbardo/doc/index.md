---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/canbardo/doc/index.html
original_path: boards/others/canbardo/doc/index.html
---

# CANbardo

Board Overview

[![../../../../_images/canbardo.webp](../../../../_images/canbardo.webp)
](../../../../_images/canbardo.webp)

CANbardo

Name:
:   `canbardo`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   same70n20b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/canbardo/doc/index.rst/../..)

## Overview

CANbardo is an open hardware Universal Serial Bus (USB) to Controller Area Network (CAN) adapter
board. It is designed to be compatible with the open source [CANnectivity USB to CAN adapter firmware](../../../../develop/manifest/external/cannectivity.md#external-module-cannectivity).

## Hardware

The CANbardo board is equipped with an Atmel SAME70N20B microcontroller and features an USB-C
connector (high-speed USB 2.0), two DB-9M connectors for CAN FD (up to 8 Mbit/s), a number of status
LEDs, and a push button. Schematics and component placement drawings are available in the [CANbardo
GitHub repository](https://github.com/CANbardo/canbardo).

### Supported Features

The `canbardo` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The SAME70N20B is driven by a 12 MHz crystal and configured to provide a system clock of 300
MHz. The two CAN FD controllers have a core clock frequency of 80 MHz.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b canbardo samples/basic/blinky
west flash
```
