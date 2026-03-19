---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/fysetc/ucan/doc/index.html
original_path: boards/fysetc/ucan/doc/index.html
---

# UCAN

Board Overview

[![../../../../_images/ucan.webp](../../../../_images/ucan.webp)
](../../../../_images/ucan.webp)

UCAN

Name:
:   `ucan`

Vendor:
:   Shenzhen Fuyuansheng Electronic Technology Co., Ltd.

Architecture:
:   arm

SoC:
:   stm32f072xb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/fysetc/ucan/doc/index.rst/../..)

## Overview

The FYSETC UCAN is an open-source USB to CAN 2.0B adapter board. More information can be found on
the [UCAN website](https://www.fysetc.com/products/fysetc-ucan-board) and in the [UCAN wiki](https://wiki.fysetc.com/UCAN/).

## Hardware

The UCAN board is equipped with a STM32F072CB microcontroller and features an USB-C connector, a
terminal block for connecting to the CAN bus, and two user LEDs. Schematics and component placement
drawings are available in the [UCAN GitHub repository](https://github.com/FYSETC/UCAN/).

### Supported Features

The `ucan` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The STM32F072CB PLL is driven by an external crystal oscillator (HSE) running at 8 MHz and
configured to provide a system clock of 48 MHz.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

If flashing via USB DFU, short pins `B0` and `3V3` when applying power to the UCAN board in
order to enter the built-in DFU mode.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ucan samples/basic/blinky
west flash
```
