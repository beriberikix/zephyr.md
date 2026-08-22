---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wch/linkw/doc/index.html
original_path: boards/wch/linkw/doc/index.html
---

# WCH LinkW

Board Overview

[![../../../../_images/linkw.webp](../../../../_images/linkw.webp)
](../../../../_images/linkw.webp)

WCH LinkW

Name:
:   `linkw`

Vendor:
:   WinChipHead

Architecture:
:   riscv

SoC:
:   ch32v208

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wch/linkw/doc/index.rst/../..)

## Overview

The [WCH](http://www.wch-ic.com) [[1]](#id2) LinkW hardware provides support for QingKe V4C 32-bit RISC-V
processor and the following devices:

- CLOCK
- GPIO
- NVIC

The board is equipped with two LEDs and two Buttons.
The [WCH webpage on CH32V208](https://www.wch-ic.com/products/CH32V208.html) [[2]](#id4) contains the processor’s manuals.
The [WCH webpage on LinkW](https://www.wch-ic.com/products/WCH-Link.html) [[3]](#id6) contains the LinkW’s schematic.

## Hardware

The QingKe V4C 32-bit RISC-V processor of the WCH LinkW is clocked by an external
32 MHz crystal or the internal 8 MHz oscillator and runs up to 144 MHz.
The CH32V208 SoC Features 4 USART, 4 GPIO ports, 2 SPI, 2 I2C, ADC, RTC,
CAN, 2 USB Device, USB Host, OPA, ETH with PHY, several timers, and BLE 5.3.

### Supported Features

The `linkw` board supports the hardware features listed below.

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

- LED0 = Green Mode LED
- LED1 = Blue Activity LED

#### Button

- SW0 = Mode Select Button (Active Low)
- SW1 = Bootstrap Button (Active High)

## Programming and Debugging

The `linkw` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `linkw` board target can be built and flashed
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
west build -b linkw samples/basic/blinky
west flash
```

### Debugging

This board can be debugged via OpenOCD or `minichlink`.

## References

[[1](#id3)]

[http://www.wch-ic.com](http://www.wch-ic.com)

[[2](#id5)]

[https://www.wch-ic.com/products/CH32V208.html](https://www.wch-ic.com/products/CH32V208.html)

[[3](#id7)]

[https://www.wch-ic.com/products/WCH-Link.html](https://www.wch-ic.com/products/WCH-Link.html)
