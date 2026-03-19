---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/bbc/microbit/doc/index.html
original_path: boards/bbc/microbit/doc/index.html
---

# micro:bit

Board Overview

[![../../../../_images/bbc_microbit.jpg](../../../../_images/bbc_microbit.jpg)
](../../../../_images/bbc_microbit.jpg)

micro:bit

Name:
:   `bbc_microbit`

Vendor:
:   BBC

Architecture:
:   arm

SoC:
:   nrf51822

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/bbc/microbit/doc/index.rst/../..)

## Overview

The Micro Bit (also referred to as BBC Micro Bit, stylized as micro:bit) is an
ARM-based embedded system designed by the BBC for use in computer education in
the UK.

The board is 4 cm × 5 cm and has an ARM Cortex-M0 processor, accelerometer and
magnetometer sensors, Bluetooth and USB connectivity, a display consisting of
25 LEDs, two programmable buttons, and can be powered by either USB or an
external battery pack. The device inputs and outputs are through five ring
connectors that are part of the 23-pin edge connector.

More information about the board can be found at the [microbit website](http://www.microbit.org/) [[1]](#id2).

## Hardware

The micro:bit has the following physical features:

- 25 individually-programmable LEDs
- 2 programmable buttons
- Physical connection pins
- Light and temperature sensors
- Motion sensors (accelerometer and compass)
- Wireless Communication, via Radio and Bluetooth
- USB interface

### Supported Features

The `bbc_microbit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

### Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF51 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b bbc_microbit samples/hello_world
west flash
```

## References

[[1](#id3)]

[http://www.microbit.org/](http://www.microbit.org/)
