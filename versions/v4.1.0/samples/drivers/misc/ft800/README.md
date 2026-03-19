---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/misc/ft800/README.html
original_path: samples/drivers/misc/ft800/README.html
---

# FT800

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/misc/ft800/README.rst/..)

## Overview

This sample displays a hello message and an incrementing counter using FT800
Embedded Video Engine.

## Requirements

To use this sample, the following hardware is required:

- A board with SPI support
- Display with [FT800 EVE](https://www.ftdichip.com/old2020/Products/ICs/FT800.html) like [VM800C board](https://www.ftdichip.com/old2020/Products/Modules/VM800C.html)

## Wiring

You will need to connect the [FT800 EVE](https://www.ftdichip.com/old2020/Products/ICs/FT800.html) SPI interface onto a board that
supports Arduino shields.

## Building and Running

This sample should work on any board that has SPI enabled and has an Arduino
shield interface. For example, it can be run on the nRF52840-DK board as
described below:

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/misc/ft800
west flash
```

To build the sample for [VM800C board](https://www.ftdichip.com/old2020/Products/Modules/VM800C.html) the shield must be defined as described
below:

```shell
west build -b nrf52840dk/nrf52840 --shield ftdi_vm800c samples/drivers/misc/ft800
west flash
```

## See also

[FT8xx driver APIs](../../../../doxygen/html/group__ft8xx__interface.md)
