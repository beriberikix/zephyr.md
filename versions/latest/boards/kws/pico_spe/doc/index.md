---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/kws/pico_spe/doc/index.html
original_path: boards/kws/pico_spe/doc/index.html
---

# Pico-SPE

Board Overview

[![../../../../_images/pico_spe.webp](../../../../_images/pico_spe.webp)
](../../../../_images/pico_spe.webp)

Pico-SPE

Name:
:   `pico_spe`

Vendor:
:   KWS Computersysteme Gmbh

Architecture:
:   arm

SoC:
:   rp2040

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/kws/pico_spe/doc/index.rst/../..)

## Overview

The Pico-SPE is a small, low-cost, versatile boards from
KWS Computersysteme Gmbh. They are equipped with an RP2040 SoC, an on-board LED,
a USB connector, an SWD interface. The Pico-SPE additionally contains an
Microchip LAN8651 10Base-T1S module. The USB bootloader allows the
ability to flash without any adapter, in a drag-and-drop manner.
It is also possible to flash and debug the boards with their SWD interface,
using an external adapter.

## Hardware

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 16MB on-board QSPI flash with XIP capabilities
- 16 GPIO pins
- 3 Analog inputs
- 2 UART peripherals
- 2 I2C controllers
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board LED
- 1 Watchdog timer peripheral
- Microchip LAN8651 10Base-T1S

### Supported Features

The `pico_spe` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

External pin mapping on the Pico-SPE is identical to the Pico, but note that internal
RP2040 GPIO lines 10, 11, 12, 13, 20, 21 are routed to the Microchip LAN8651 on the
Pico-SPE.

#### Default Zephyr Peripheral Mapping:

- UART0\_TX : P0
- UART0\_RX : P1
- I2C0\_SDA : P4
- I2C0\_SCL : P5
- I2C1\_SDA : P6
- I2C1\_SCL : P7
- ADC\_CH0 : P26
- ADC\_CH1 : P27
- ADC\_CH2 : P28

## Programmable I/O (PIO)

The RP2040 SoC comes with two PIO periherals. These are two simple
co-processors that are designed for I/O operations. The PIOs run
a custom instruction set, generated from a custom assembly language.
PIO programs are assembled using **pioasm**, a tool provided by Raspberry Pi.

Zephyr does not (currently) assemble PIO programs. Rather, they should be
manually assembled and embedded in source code. An example of how this is done
can be found at [drivers/serial/uart\_rpi\_pico\_pio.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/uart_rpi_pico_pio.c).

### Sample: SPI via PIO

The [BME280 humidity and pressure sensor](../../../../samples/sensor/bme280/README.md#bme280 "Get temperature, pressure, and humidity data from a BME280 sensor.") sample includes a
demonstration of using the PIO SPI driver to communicate with an
environmental sensor. The PIO SPI driver supports using any
combination of GPIO pins for an SPI bus, as well as allowing up to
four independent SPI buses on a single board (using the two SPI
devices as well as both PIO devices).

## Programming and Debugging

The `pico_spe` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

The SWD interface can be used to program and debug the device,
e.g. using OpenOCD with the [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) .

The overall explanation regarding flashing and debugging is the same as for [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico).
Refer to [Programming and Debugging](../../../raspberrypi/rpi_pico/doc/index.md#rpi-pico-programming-and-debugging) for more information. N.b. OpenOCD support requires using Raspberry Pi’s forked version of OpenOCD.

Below is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b pico_spe samples/basic/blinky
west flash --openocd /usr/local/bin/openocd
```
