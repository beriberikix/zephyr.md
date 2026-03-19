---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/weact/usb2canfdv1/doc/index.html
original_path: boards/weact/usb2canfdv1/doc/index.html
---

# USB2CANFDV1

Board Overview

[![../../../../_images/usb2canfdv1.webp](../../../../_images/usb2canfdv1.webp)
](../../../../_images/usb2canfdv1.webp)

USB2CANFDV1

Name:
:   `usb2canfdv1`

Vendor:
:   WeAct Studio

Architecture:
:   arm

SoC:
:   stm32g0b1xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/weact/usb2canfdv1/doc/index.rst/../..)

## Overview

The WeAct Studio USB2CANFDV1 is a dedicated USB to CAN FD adapter board. More information can be
found on the [USB2CANFDV1 website](https://github.com/WeActStudio/WeActStudio.USB2CANFDV1).

## Hardware

The USB2CANFDV1 is equipped with a STM32G0B1CBT6 microcontroller and features a USB-C connector, a
terminal block for connecting to the CAN bus, and three LEDs.

### Supported Features

The `usb2canfdv1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The STM32G0B1CBT6 PLL is driven by an external crystal oscillator (HSE) running at 16 MHz and
configured to provide a system clock of 60 MHz. This allows generating a FDCAN1 core clock of 80
MHz.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b usb2canfdv1 samples/basic/blinky
west flash
```
