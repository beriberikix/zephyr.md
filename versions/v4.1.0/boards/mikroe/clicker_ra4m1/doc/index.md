---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/mikroe/clicker_ra4m1/doc/index.html
original_path: boards/mikroe/clicker_ra4m1/doc/index.html
---

# Clicker RA4M1

Board Overview

[![../../../../_images/mikroe_clicker_ra4m1.jpg](../../../../_images/mikroe_clicker_ra4m1.jpg)
](../../../../_images/mikroe_clicker_ra4m1.jpg)

Clicker RA4M1

Name:
:   `mikroe_clicker_ra4m1`

Vendor:
:   MikroElektronika d.o.o.

Architecture:
:   arm

SoC:
:   r7fa4m1ab3cfm

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/mikroe/clicker_ra4m1/doc/index.rst/../..)

## Overview

The Mikroe Clicker RA4M1 development board contains a Renesas Cortex-M4 based
R7FA4M1AB3CFM Microcontroller operating at up to 48 MHz with 256 KB of Flash
memory and 32 KB of SRAM.

## Hardware

The Clicker RA4M1 board contains a USB Type-C connector, two LEDs, two push
buttons, and a reset button. It has J-Link onboard and mikroBUS socket for
interfacing with external electronics. For more information about the
development board see the [Clicker RA4M1 website](https://www.mikroe.com/ra4m1-clicker) [[1]](#id2).

### Supported Features

The `mikroe_clicker_ra4m1` board supports the hardware features listed below.

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

You can build and flash an application in the usual way (See
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done in the usual way.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.mikroe.com/ra4m1-clicker](https://www.mikroe.com/ra4m1-clicker)
