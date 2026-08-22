---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/pimoroni/pico_plus2/doc/index.html
original_path: boards/pimoroni/pico_plus2/doc/index.html
---

# Pimoroni Pico Plus2

Board Overview

[![../../../../_images/pico_plus2.webp](../../../../_images/pico_plus2.webp)
](../../../../_images/pico_plus2.webp)

Pimoroni Pico Plus2

Name:
:   `pico_plus2`

Vendor:
:   Pimoroni Ltd.

Architecture:
:   arm

SoC:
:   rp2350b

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/pimoroni/pico_plus2/doc/index.rst/../..)

## Overview

The [Pimoroni Pico Plus 2](https://shop.pimoroni.com/products/pimoroni-pico-plus-2) [[1]](#id2) is a compact and versatile board featuring the Raspberry Pi RP2350B SoC.
It includes USB Type-C, Qwiic/STEMMA QT connectors, SP/CE connectors, a debug connector,
a reset button, and a BOOT button.

## Hardware

- Dual Cortex-M33 or Hazard3 processors at up to 150MHz
- 520KB of SRAM, and 4MB of on-board flash memory
- 16MB of on-board QSPI flash (supports XiP)
- 8MB of PSRAM
- USB 1.1 with device and host support
- Low-power sleep and dormant modes
- Drag-and-drop programming using mass storage over USB
- 48 multi-function GPIO pins including 8 that can be used for ADC
- 2 SPI, 2 I2C, 2 UART, 3 12-bit 500ksps Analogue to Digital - Converter (ADC), 24 controllable PWM channels
- 2 Timer with 4 alarms, 1 AON Timer
- Temperature sensor
- 3 Programmable IO (PIO) blocks, 12 state machines total for custom peripheral support
- USB-C connector for power, programming, and data transfer
- Qwiic/STEMMA QT(Qw/ST) connector
- SP/CE connector
- 3-pin debug connector, this can use with [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) [[2]](#id4).
- Reset button and BOOT button (BOOT button also usable as a user switch)

### Supported Features

The `pico_plus2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

You can use peripherals that are made by using the PIO.
See [PIO Based Features](../../../raspberrypi/rpi_pico/doc/index.md#rpi-pico-pio-based-features)

## Programming and Debugging

The `pico_plus2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

The overall explanation regarding flashing and debugging is the same as or [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico).
See [Programming and Debugging](../../../raspberrypi/rpi_pico/doc/index.md#rpi-pico-programming-and-debugging) in [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico) documentation. N.b. OpenOCD support requires using Raspberry Pi’s forked version of OpenOCD.

Below is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b pico_plus2/rp2350b/m33 samples/basic/blinky
west flash --openocd /usr/local/bin/openocd
```

[[1](#id3)]

[https://shop.pimoroni.com/products/pimoroni-pico-plus-2](https://shop.pimoroni.com/products/pimoroni-pico-plus-2)

[[2](#id5)]

[https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html)
