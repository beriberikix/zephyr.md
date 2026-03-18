---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/mikroe/clicker_ra4m1/doc/index.html
original_path: boards/mikroe/clicker_ra4m1/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Mikroe Clicker RA4M1

## Overview

The Mikroe Clicker RA4M1 development board contains a Renesas Cortex-M4 based
R7FA4M1AB3CFM Microcontroller operating at up to 48 MHz with 256 KB of Flash
memory and 32 KB of SRAM.

![Clicker RA4M1](../../../../_images/mikroe_clicker_ra4m1.jpg)

Clicker RA4M1 (Credit: MikroElektronika d.o.o.)

## Hardware

The Clicker RA4M1 board contains a USB Type-C connector, two LEDs, two push
buttons, and a reset button. It has J-Link onboard and mikroBUS socket for
interfacing with external electronics. For more information about the
development board see the [Clicker RA4M1 website](https://www.mikroe.com/ra4m1-clicker) [[1]](#id3).

### Supported Features

The Zephyr Mikroe Clicker RA4M1 configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | GPIO output GPIO input |

Other hardware features have not been enabled yet for this board.

The default configuration can be found in the defconfig file:
[boards/mikroe/clicker\_ra4m1/mikroe\_clicker\_ra4m1\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/mikroe/clicker_ra4m1/mikroe_clicker_ra4m1_defconfig).

## Programming and debugging

### Building & Flashing

You can build and flash an application in the usual way (See
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done in the usual way.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 samples/basic/blinky
west debug
```

## References

[[1](#id4)]

[https://www.mikroe.com/ra4m1-clicker](https://www.mikroe.com/ra4m1-clicker)
