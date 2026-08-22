---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wch/ch32v003f4p6_dev_board/doc/index.html
original_path: boards/wch/ch32v003f4p6_dev_board/doc/index.html
---

# WCH CH32V003F4P6 Development Board

Board Overview

[![../../../../_images/ch32v003f4p6_dev_board.webp](../../../../_images/ch32v003f4p6_dev_board.webp)
](../../../../_images/ch32v003f4p6_dev_board.webp)

WCH CH32V003F4P6 Development Board

Name:
:   `ch32v003f4p6_dev_board`

Vendor:
:   WinChipHead

Architecture:
:   riscv

SoC:
:   ch32v003

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wch/ch32v003f4p6_dev_board/doc/index.rst/../..)

## Overview

The [WCH](http://www.wch-ic.com) [[1]](#id2) CH32V003F4P6 Development Board hardware provides support for
QingKe V2A 32-bit RISC-V processor and the following devices:

- CLOCK
- GPIO
- NVIC

The board is equipped with one LED, wired to PD1 and SWIO pins.
The [WCH webpage on CH32V003](https://www.wch-ic.com/products/CH32V003.html) [[2]](#id4) contains the processor’s information
and the datasheet.

## Hardware

The QingKe V2A 32-bit RISC-V processor of the WCH CH32V003F4P6\_DEV\_BOARD is clocked
by an internal RC oscillator and runs at 24 MHz.

### Supported Features

The `ch32v003f4p6_dev_board` board supports the hardware features listed below.

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

- LED1 (red) = PD1

## Programming and Debugging

The `ch32v003f4p6_dev_board` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `ch32v003f4p6_dev_board` board target can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details); however, an external programmer is required since the board
does not have any built-in debug support.

The following pins of the external programmer must be connected to the
following pins on the PCB (see image):

- VCC = VCC (do not power the board from the USB port at the same time)
- GND = GND
- SWIO = PD1

### Flashing

SWIO pin is connected to PD1 and also to led on the board. By default, the function
of PD1 is SWD. To use the led on the board, the function of PD1 is changed to GPIO
if PD1 is not put to ground (see [boards/wch/ch32v003f4p6\_dev\_board/board.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wch/ch32v003f4p6_dev_board/board.c)).
In order to be able to reflash the board, if some zephyr application is already loaded
in flash, power on the board with PD1 put to ground to let PD1 as SWIO. After that,
reconnect the external debugger SWDIO pin to PD1/SWIO to be able to flash the board
using the external debugger.

You can use `minichlink` to flash the board. Once `minichlink` has been set
up, build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ch32v003f4p6_dev_board samples/basic/blinky
west flash
```

### Debugging

This board can be debugged via OpenOCD or `minichlink`.

## Testing the LED on the WCH CH32V003F4P6\_DEV\_BOARD

There is 1 sample program that allow you to test that the LED on the board is
working properly with Zephyr:

```shell
samples/basic/blinky
```

You can build and flash the examples to make sure Zephyr is running
correctly on your board. The button and LED definition can be found
in [boards/wch/ch32v003f4p6\_dev\_board/ch32v003f4p6\_dev\_board.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wch/ch32v003f4p6_dev_board/ch32v003f4p6_dev_board.dts).

## References

[[1](#id3)]

[http://www.wch-ic.com](http://www.wch-ic.com)

[[2](#id5)]

[https://www.wch-ic.com/products/CH32V003.html](https://www.wch-ic.com/products/CH32V003.html)
