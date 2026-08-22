---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wch/ch32v006evt/doc/index.html
original_path: boards/wch/ch32v006evt/doc/index.html
---

# WCH CH32V006EVT

Board Overview

[![../../../../_images/ch32v006evt.webp](../../../../_images/ch32v006evt.webp)
](../../../../_images/ch32v006evt.webp)

WCH CH32V006EVT

Name:
:   `ch32v006evt`

Vendor:
:   WinChipHead

Architecture:
:   riscv

SoC:
:   ch32v006

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wch/ch32v006evt/doc/index.rst/../..)

## Overview

The [WCH](http://www.wch-ic.com) [[1]](#id2) CH32V006EVT is an evaluation board for the RISC-V based CH32V006K8U6
SOC.

The board is equipped with a power LED, reset button, USB port for power, and
two user LEDs. The [WCH webpage on CH32V006](https://www.wch-ic.com/downloads/CH32V006DS0_PDF.html) [[2]](#id4) contains the processor’s
information and the datasheet.

## Hardware

The QingKe V2C 32-bit RISC-V processor of the WCH CH32V006EVT is clocked by an
external crystal and runs at 48 MHz.

### Supported Features

The `ch32v006evt` board supports the hardware features listed below.

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

- LED1 = Unconnected. Connect to an I/O pin (PD0).
- LED2 = Unconnected. Connect to an I/O pin (PC0).

## Programming and Debugging

The `ch32v006evt` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `ch32v006evt` board can be built and flashed
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details); however, an external programmer is required since the board
does not have any built-in debug support.

Connect the programmer to the following pins on the PCB:

- VCC = VCC (do not power the board from the USB port at the same time)
- GND = GND
- SWIO = PD1

### Flashing

You can use [minichlink](https://github.com/cnlohr/ch32fun/tree/master/minichlink) [[3]](#id6) to flash the board. Once `minichlink` has been set
up, build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ch32v006evt samples/basic/blinky
west flash
```

### Debugging

This board can be debugged via OpenOCD or `minichlink`.

## Testing the LED on the WCH CH32V006EVT

The `blinky` sample can be used to test that the LEDs on the board are working
properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")

You can build and flash the examples to make sure Zephyr is running
correctly on your board. The LED definitions can be found in
[boards/wch/ch32v006evt/ch32v006evt.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/wch/ch32v006evt/ch32v006evt.dts).

## References

[[1](#id3)]

[http://www.wch-ic.com](http://www.wch-ic.com)

[[2](#id5)]

[https://www.wch-ic.com/downloads/CH32V006DS0\_PDF.html](https://www.wch-ic.com/downloads/CH32V006DS0_PDF.html)

[[3](#id7)]

[https://github.com/cnlohr/ch32fun/tree/master/minichlink](https://github.com/cnlohr/ch32fun/tree/master/minichlink)
