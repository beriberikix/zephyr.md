---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/kws/pico2_spe/doc/index.html
original_path: boards/kws/pico2_spe/doc/index.html
---

# Pico2-SPE

Board Overview

[![../../../../_images/pico2_spe.webp](../../../../_images/pico2_spe.webp)
](../../../../_images/pico2_spe.webp)

Pico2-SPE

Name:
:   `pico2_spe`

Vendor:
:   KWS Computersysteme Gmbh

Architecture:
:   arm

SoC:
:   rp2350a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/kws/pico2_spe/doc/index.rst/../..)

## Overview

The Pico2-SPE is a small, low-cost, versatile boards from
KWS Computersysteme Gmbh. They are equipped with an RP2350a SoC, an on-board LED,
a USB connector, an SWD interface. The Pico2-SPE additionally contains an
Microchip LAN8651 10Base-T1S module. The USB bootloader allows the
ability to flash without any adapter, in a drag-and-drop manner.
It is also possible to flash and debug the boards with their SWD interface,
using an external adapter.

## Hardware

- Dual Cortex-M33 or Hazard3 processors at up to 150MHz
- 520KB of SRAM, and 4MB of on-board flash memory
- USB 1.1 with device and host support
- Low-power sleep and dormant modes
- Drag-and-drop programming using mass storage over USB
- 26 multi-function GPIO pins including 3 that can be used for ADC
- 1 SPI, 2 I2C, 2 UART, 3 12-bit 500ksps Analogue to Digital - Converter (ADC), 24 controllable PWM channels
- 2 Timer with 4 alarms, 1 AON Timer
- Temperature sensor
- Microchip LAN8651 10Base-T1S
- 3 Programmable IO (PIO) blocks, 12 state machines total for custom peripheral support

  - Flexible, user-programmable high-speed IO
  - Can emulate interfaces such as SD Card and VGA

### Supported Features

The `pico2_spe` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The default pin mapping is unchanged from the Pico-SPE.

## Programming and Debugging

The `pico2_spe` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

As with the Pico-SPE, the SWD interface can be used to program and debug the device,
e.g. using OpenOCD with the [Raspberry Pi Debug Probe](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) .

The overall explanation regarding flashing and debugging is the same as for [Raspberry Pi Pico](../../../raspberrypi/rpi_pico/doc/index.md#rpi_pico).
Refer to [Programming and Debugging](../../../raspberrypi/rpi_pico/doc/index.md#rpi-pico-programming-and-debugging) for more information. N.b. OpenOCD support requires using Raspberry Pi’s forked version of OpenOCD.

Below is an example of building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b pico2_spe/rp2350a/m33 samples/basic/blinky
west flash --openocd /usr/local/bin/openocd
```

## References
