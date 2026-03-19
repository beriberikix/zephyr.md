---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/candlelightfd/doc/index.html
original_path: boards/others/candlelightfd/doc/index.html
---

# candleLightFD

Board Overview

[![../../../../_images/candlelightfd.webp](../../../../_images/candlelightfd.webp)
](../../../../_images/candlelightfd.webp)

candleLightFD

Name:
:   `candlelightfd`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   stm32g0b1xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/candlelightfd/doc/index.rst/../..)

## Overview

The candleLight FD is an open-hardware USB to CAN FD adapter board available from Linux Automation GmBH.
Find more information about the board at the [Linux Automation website](https://linux-automation.com/en/products/candlelight-fd.html).

## Hardware

The candleLight FD board is equipped with a STM32G0B1CBT6 microcontroller and features an USB-C connector,
a DB-9M connector for the CAN bus, and two user LEDs. Schematics and component placement drawings
are available in the [candleLight FD GitHub repository](https://github.com/linux-automation/candleLightFD).

### Supported Features

The `candlelightfd` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The STM32G0B1CBT6 PLL is driven by an external crystal oscillator (HSE) running at 8 MHz and
configured to provide a system clock of 60 MHz. This allows generating a FDCAN1 and FDCAN2 core
clock of 80 MHz.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

If flashing via USB DFU, short jumper `BOOT` when applying power to the candleLight FD in order to
enter the built-in DFU mode.

### Variants

The candleLight FD is can be retrofitted with a second transceiver, making it a dual CAN FD device:

- `candlelightfd`: The default variant.
- `candlelightfd_stm32g0b1xx_dual`: Variant for the dual CAN FD.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b candlelightfd samples/basic/blinky
west flash
```
