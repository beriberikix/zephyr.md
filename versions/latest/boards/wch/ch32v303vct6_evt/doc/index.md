---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/wch/ch32v303vct6_evt/doc/index.html
original_path: boards/wch/ch32v303vct6_evt/doc/index.html
---

# WCH CH32V303VCT6\_EVT

Board Overview

[![../../../../_images/ch32v303vct6_evt.webp](../../../../_images/ch32v303vct6_evt.webp)
](../../../../_images/ch32v303vct6_evt.webp)

WCH CH32V303VCT6\_EVT

Name:
:   `ch32v303vct6_evt`

Vendor:
:   WinChipHead

Architecture:
:   riscv

SoC:
:   ch32v303

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/wch/ch32v303vct6_evt/doc/index.rst/../..)

## Overview

The [WCH](http://www.wch-ic.com) [[1]](#id2) CH32V303VCT6-EVT hardware provides support for QingKe V4F 32-bit RISC-V
processor.

The [WCH webpage on CH32V303](https://www.wch-ic.com/products/CH32V303.html) [[2]](#id4) contains
the processor’s information and the datasheet.

## Hardware

The QingKe V4F 32-bit RISC-V processor of the WCH CH32V303VCT6-EVT is clocked by an external
32 MHz crystal or the internal 8 MHz oscillator and runs up to 144 MHz.
The CH32V303 SoC features 8 USART, 4 GPIO ports, 3 SPI, 2 I2C, 2 ADC, RTC,
CAN, USB Host/Device, and 4 OPA.

### Supported Features

The `ch32v303vct6_evt` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

Applications for the `ch32v303vct6_evt` board target can be built and flashed
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details); however, an external programmer (like the [WCH LinkE](https://www.wch-ic.com/products/WCH-Link.html) [[3]](#id6)) is required since the board
does not have any built-in debug support.

### Flashing

You can use `minichlink` to flash the board. Once `minichlink` has been set
up, build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b ch32v303vct6_evt samples/hello_world
west flash
```

### Debugging

This board can be debugged via OpenOCD using the WCH openOCD liberated fork, available at [https://github.com/jnk0le/openocd-wch](https://github.com/jnk0le/openocd-wch).

## References

[[1](#id3)]

[http://www.wch-ic.com](http://www.wch-ic.com)

[[2](#id5)]

[https://www.wch-ic.com/products/CH32V303.html](https://www.wch-ic.com/products/CH32V303.html)

[[3](#id7)]

[https://www.wch-ic.com/products/WCH-Link.html](https://www.wch-ic.com/products/WCH-Link.html)
