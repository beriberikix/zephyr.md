---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/candlelight/doc/index.html
original_path: boards/others/candlelight/doc/index.html
---

# candleLight

Board Overview

[![../../../../_images/candlelight.webp](../../../../_images/candlelight.webp)
](../../../../_images/candlelight.webp)

candleLight

Name:
:   `candlelight`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   stm32f072xb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/candlelight/doc/index.rst/../..)

## Overview

The candleLight is an open-hardware USB to CAN 2.0B adapter board available from a number of
sources.

## Hardware

The candleLight board is equipped with a STM32F072CB microcontroller and features an USB connector,
a DB-9M connector for the CAN bus, and two user LEDs. Schematics and component placement drawings
are available in the [candleLight GitHub repository](https://github.com/HubertD/candleLight).

### Supported Features

The `candlelight` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The STM32F072CB PLL is driven by the internal RC oscillator (HSI) running at 8 MHz and
configured to provide a system clock of 48 MHz.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

If flashing via USB DFU, short resistor `R203` when applying power to the candleLight in order to
enter the built-in DFU mode.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b candlelight samples/basic/blinky
west flash
```
