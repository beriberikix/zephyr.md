---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/shields/dac80508_evm/doc/index.html
original_path: boards/shields/dac80508_evm/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# DAC80508 Evaluation Module

## Overview

The Texas Instruments DAC80508 Evaluation Module (EVM) is a
DAC development module for the TI DAC80508 series.

![DAC80508 EVM](../../../../_images/dac80508evm-board-photo.jpg)

## Requirements

This shield can only be used with a development board that provides a
configuration for Arduino connectors and defines a node alias for the
SPI interface (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

The SPI connector pins on the DAC80508 EVM can be connected to the
Arduino headers of the development board using jumper wires.
In addition, 5V must be connected to the DAC80508 EVM’s TP6(VDD).

![DAC80508 EVM + STM32F746G_DISCO](../../../../_images/dac80508evm_connected.jpg)

For more information about interfacing the DAC80508 series and the
DACx0508 EVM in particular, see these TI documents:

- [DACx0508 Evaluation Module User’s Guide](https://www.ti.com/lit/pdf/slau734)
- [DAC80508 True 16-bit, 8-channel, SPI](https://www.ti.com/product/DAC80508)
