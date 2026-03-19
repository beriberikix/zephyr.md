---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/we/oceanus1ev/doc/index.html
original_path: boards/we/oceanus1ev/doc/index.html
---

# Oceanus-I EV

Board Overview

[![../../../../_images/we_oceanus1ev.webp](../../../../_images/we_oceanus1ev.webp)
](../../../../_images/we_oceanus1ev.webp)

Oceanus-I EV

Name:
:   `we_oceanus1ev`

Vendor:
:   Würth Elektronik GmbH.

Architecture:
:   arm

SoC:
:   stm32wle5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/we/oceanus1ev/doc/index.rst/../..)

## Overview

The we\_oceanus1ev board is an evaluation board of the [Oceanus-I](https://www.we-online.com/katalog/de/OCEANUS-I) [[1]](#id2) radio module.
It provides support for the [STM32WLE5CC](https://www.st.com/en/microcontrollers-microprocessors/stm32wle5cc.html) [[2]](#id5) ARM CPU and
the following devices:

- CLOCK
- FLASH
- GPIO
- I2C
- NVIC
- RADIO (LoRa)
- RTC
- SPI
- UART
- WDT

## Hardware

The board has below hardware features:

- [Oceanus-I](https://www.we-online.com/katalog/de/OCEANUS-I) [[1]](#id2), 256KB Flash, 64KB RAM with external antenna
- 1 FTDI chip (USB to UART) converter
- 1 I2C WE sensor EV-Boards connector
- 1 SPI WE sensor EV-Boards connector
- 2 application LEDs
- 1 application, and 1 reset push-button

### Supported Features

The `we_oceanus1ev` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

Applications for the `we_oceanus1ev` board can be built the
usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)).

The board debugged and flashed with an external debug probe connected
to the SWD pins, current native support is for the JLink debug probe.

### Flashing

Connect the board to your host computer and build and flash an application.

```shell
# From the root of the zephyr repository
west build -b we_oceanus1ev samples/hello_world
west flash
```

Run a serial terminal to connect with your board. By default, `lpuart1` is
accessible via the on-board FTDI USB to UART converter.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b we_oceanus1ev samples/basic/blinky
west debug
```

## References

[1]
([1](#id3),[2](#id4))

[https://www.we-online.com/katalog/de/OCEANUS-I](https://www.we-online.com/katalog/de/OCEANUS-I)

[[2](#id6)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32wle5cc.html](https://www.st.com/en/microcontrollers-microprocessors/stm32wle5cc.html)
