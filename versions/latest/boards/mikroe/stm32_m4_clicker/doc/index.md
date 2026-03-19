---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/mikroe/stm32_m4_clicker/doc/index.html
original_path: boards/mikroe/stm32_m4_clicker/doc/index.html
---

# STM32 M4 Clicker

Board Overview

[![../../../../_images/stm32_m4_clicker.webp](../../../../_images/stm32_m4_clicker.webp)
](../../../../_images/stm32_m4_clicker.webp)

STM32 M4 Clicker

Name:
:   `mikroe_stm32_m4_clicker`

Vendor:
:   MikroElektronika d.o.o.

Architecture:
:   arm

SoC:
:   stm32f415xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/mikroe/stm32_m4_clicker/doc/index.rst/../..)

## Overview

The Mikroe STM32 M4 Clicker development board contains a STMicroelectronics
Cortex-M4 based STM32F415RG Microcontroller operating at up to 168 MHz with
1 MB of Flash memory and 192 KB of SRAM.

## Hardware

The STM32 M4 Clicker board contains a USB connector, two LEDs, two push
buttons, and a reset button. It features a mikroBUS socket for interfacing
with external electronics. For more information about the development
board see the [STM32 M4 Clicker website](https://www.mikroe.com/clicker-stm32f4) [[1]](#id2).

### Supported Features

The `mikroe_stm32_m4_clicker` board supports the hardware features listed below.

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
west build -b mikroe_stm32_m4_clicker samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done in the usual way.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b mikroe_stm32_m4_clicker samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.mikroe.com/clicker-stm32f4](https://www.mikroe.com/clicker-stm32f4)
