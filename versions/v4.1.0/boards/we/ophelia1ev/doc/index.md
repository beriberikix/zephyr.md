---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/we/ophelia1ev/doc/index.html
original_path: boards/we/ophelia1ev/doc/index.html
---

# Ophelia-I EV NRF52805

Board Overview

[![../../../../_images/we_ophelia1ev_nrf52805.jpg](../../../../_images/we_ophelia1ev_nrf52805.jpg)
](../../../../_images/we_ophelia1ev_nrf52805.jpg)

Ophelia-I EV NRF52805

Name:
:   `we_ophelia1ev`

Vendor:
:   Würth Elektronik GmbH.

Architecture:
:   arm

SoC:
:   nrf52805

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/we/ophelia1ev/doc/index.rst/../..)

## Overview

The we\_ophelia1ev\_nrf52805 board is an evaluation board of the Ophelia-I radio module.
It provides support for the Nordic Semiconductor nRF52805 ARM CPU and
the following devices:

- CLOCK
- FLASH
- GPIO
- I2C
- NVIC
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- WDT

## Hardware

The Ophelia-I uses the internal low frequency RC oscillator
and provides the so called smart antenna connection, that allows
to choose between the module’s integrated PCB antenna and an external
antenna that can be connected to the available SMA connector.

### Supported Features

The `we_ophelia1ev` board supports the hardware features listed below.

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

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF52 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b we_ophelia1ev/nrf52805 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## References
