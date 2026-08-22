---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/weact/bluepillplus_ch32v203/doc/index.html
original_path: boards/weact/bluepillplus_ch32v203/doc/index.html
---

# BluePill Plus CH32V203

Board Overview

[![../../../../_images/bluepillplus_ch32v203.webp](../../../../_images/bluepillplus_ch32v203.webp)
](../../../../_images/bluepillplus_ch32v203.webp)

BluePill Plus CH32V203

Name:
:   `bluepillplus_ch32v203`

Vendor:
:   WeAct Studio

Architecture:
:   riscv

SoC:
:   ch32v203

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/weact/bluepillplus_ch32v203/doc/index.rst/../..)

## Overview

The [WeActStudio](https://github.com/WeActStudio) [[1]](#id2) BluePill Plus CH32V203 hardware provides support for QingKe V4B 32-bit RISC-V
processor and the following devices:

- CLOCK
- GPIO
- NVIC
- UART

The board is equipped with two LEDs and three Buttons.
User can use one of the LEDs and one of the buttons.
The [WCH webpage on CH32V203](https://www.wch-ic.com/products/CH32V203.html) [[2]](#id4) contains the processor’s manuals.
The [WeActStudio webpage on BPP](https://github.com/WeActStudio/WeActStudio.BluePill-Plus-CH32) [[3]](#id6) contains the BluePill’s schematic.

## Hardware

The QingKe V4B 32-bit RISC-V processor of the BluePill Plus CH32V203 is clocked by an external
8 MHz crystal or the internal 8 MHz oscillator and runs up to 144 MHz.
The CH32V203 SoC Features 2-4 USART, 4 GPIO ports, 1-2 SPI, 0-2 I2C, 9-16 ADC, RTC,
CAN, USB Device, USB Host, OPA, and several timers.

### Supported Features

The `bluepillplus_ch32v203` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### LED

- LED0 = Blue User LED

#### Button

- SW0 = User Button

## Programming and Debugging

Applications for the `bluepillplus_ch32v203` board can be built and flashed
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details); however, an external programmer is required since the board
does not have any built-in debug support.

The following pins of the external programmer must be connected to the
following pins on the PCB:

- VCC = VCC
- GND = GND
- SWIO = PA13
- SWCLK = PA14

### Flashing

You can use `minichlink` to flash the board. Once `minichlink` has been set
up, build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b bluepillplus_ch32v203 samples/basic/blinky
west flash
```

### Debugging

This board can be debugged via OpenOCD or `minichlink`.

## References

[[1](#id3)]

[https://github.com/WeActStudio](https://github.com/WeActStudio)

[[2](#id5)]

[https://www.wch-ic.com/products/CH32V203.html](https://www.wch-ic.com/products/CH32V203.html)

[[3](#id7)]

[https://github.com/WeActStudio/WeActStudio.BluePill-Plus-CH32](https://github.com/WeActStudio/WeActStudio.BluePill-Plus-CH32)
