---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/norik/octopus_io_board/doc/index.html
original_path: boards/norik/octopus_io_board/doc/index.html
---

# Octopus IO-Board

Board Overview

[![../../../../_images/octopus_io_board.webp](../../../../_images/octopus_io_board.webp)
](../../../../_images/octopus_io_board.webp)

Octopus IO-Board

Name:
:   `octopus_io_board`

Vendor:
:   Norik Systems

Architecture:
:   arm

SoC:
:   nrf9160

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/norik/octopus_io_board/doc/index.rst/../..)

## Overview

Octopus IO-Board is an expansion to the Octopus SoM, which is built around the nRF9160 SiP
offering NB-IoT and LTE-M connectivity, GPS and accelerometer. Octopus IO-Board expands
the capabilities of the Octopus SoM by providing additional peripherals and interfaces for
development and prototyping of low-power IoT applications.

nRF9160 SiP contains ARM Cortex-M33 application processor and the
following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- WDT
- IDAU

Octopus IO-Board offers the following features:

- Battery charger
- USB-C for power
- Solar charger
- Alkaline battery input
- LDO regulator to power Octopus SoM and peripherals
- Battery monitoring using ADC
- 64 Mbit SPI NOR flash
- Dedicated ADC, GPIO, I2C, SPI and UARTE pins for expansion
- Exposed headers for current measurements
- Nano SIM connector
- Tag-Connect TC2030-IDC 6-pin connector for SWD programming and debugging
- 2x3 pinheader for SWD programming and debugging

More information about the board can be found at the [Octopus IO-Board Product Page](https://www.norik.com/octopus-io-board/) [[1]](#id2)
and in the [Octopus IO-Board Documentation](https://www.norik.com/wp-content/uploads/2024/09/Octopus_IO-Board_Datasheet.pdf) [[2]](#id4).

## Hardware

### Connections and IOs

The Octopus IO-Board features multiple dedicated pin headers for peripherals:

- 3x I2C0 bus
- 2x SPI0 bus
- 3x I2C1/SPI1 bus (selectable)
- 1x UARTE0 bus
- 1x Analog input (5 input pins)
- 1x GPIO (7 I/O pins)

The I2C1/SPI1 bus is selectable by the user by cutting/soldering SB8 and SB9 solder bridges and configuring the bus in the device tree.

The GPIO pin header provides 7 I/O pins, which can be used as digital input/output. Some of them also serve as chip selects for SPI peripherals.

### Power supply

The Octopus IO-Board can be powered from the following sources:

- USB-C connector
- Solar cell
- Alkaline battery
- Li-Po battery

When powered from USB-C or solar cell, the board can charge the Li-Po battery. The battery voltage can be monitored using ADC which can
provide information about the battery State of charge (SOC).

When powered from alkaline battery, the user needs to set switch SW1 to ALK position. This ensures that the Li-Ion battery is not charged from the alkaline battery.

The board has a built-in LDO regulator that is used to power the Octopus SoM and peripherals. The EN2 pin can be used to enable/disable output 2 of the LDO regulator.
This can be used to power off peripherals to save power when they are not needed.

The board also has multiple built-in test points for measuring current consumption of the board, which enables the user to measure and optimize the power consumption of the board.

## Programming and Debugging

Norik Octopus IO-Board can be programmed and debugged using the Tag-Connect TC2030-IDC 6-pin connector or 6-pin SWD pinheader.

### Building an application

In most case you’ll need to use `octopus_io_board/nrf9160/ns` board target for building examples.
Some examples don’t require non secure mode and can be built with `octopus_io_board/nrf9160` board target.

### Flashing

Refer to the instruction in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install and
configure all the necessary software.

Here is an example for the Hello World application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom /dev/<tty_device> 115200
```

Replace <tty\_device> with the port where the Octopus IO-Board can be found. For example, under Linux, /dev/ttyACM0.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b octopus_io_board/nrf9160 samples/hello_world
west flash
```

To build and flash the application in non-secure mode, use the following command:

```shell
# From the root of the zephyr repository
west build -b octopus_io_board/nrf9160/ns samples/hello_world
west flash
```

### Debugging

Refer to the instruction in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page for information on
debugging.

### Testing the on-board LED

Use the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") to test the on-board LED. Build and flash the example to make sure Zephyr is running correctly on your board.

```shell
# From the root of the zephyr repository
west build -b octopus_io_board/nrf9160 samples/basic/blinky
west flash
```

## References

[[1](#id3)]

[https://www.norik.com/octopus-io-board/](https://www.norik.com/octopus-io-board/)

[[2](#id5)]

[https://www.norik.com/wp-content/uploads/2024/09/Octopus\_IO-Board\_Datasheet.pdf](https://www.norik.com/wp-content/uploads/2024/09/Octopus_IO-Board_Datasheet.pdf)
