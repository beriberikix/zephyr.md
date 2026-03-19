---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/renesas/ek_ra4m1/doc/index.html
original_path: boards/renesas/ek_ra4m1/doc/index.html
---

# RA4M1 Evaluation Kit

Board Overview

[![../../../../_images/ek_ra4m1.webp](../../../../_images/ek_ra4m1.webp)
](../../../../_images/ek_ra4m1.webp)

RA4M1 Evaluation Kit

Name:
:   `ek_ra4m1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa4m1ab3cfp

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_ra4m1/doc/index.rst/../..)

## Overview

The MCU integrates multiple series of software- and pin-compatible Arm®-based 32-bit
cores that share a common set of Renesas peripherals to facilitate design scalability
and efficient platform-based product development.
The MCU provides an optimal combination of low-power, high-performance Arm Cortex®-M4 core
running up to 48 MHz with the following features:

**Renesas RA4M1 Microcontroller Group**

- R7FA4M1AB3CFP
- 100-pin LQFP package
- 48 MHz Arm® Cortex®-M4 core with Floating Point Unit (FPU)
- 32 KB SRAM
- 256 KB code flash memory
- 8 KB data flash memory

**Connectivity**

- A Device USB connector for the Main MCU
- SEGGER J-Link® On-Board (OB) interface for debugging and programming of the RA4M1 MCU. A
  10pin JTAG/SWD interface is also provided for connecting optional external debuggers and
  programmers.
- Two PMOD connectors, allowing use of appropriate PMOD compliant peripheral plug-in modules for
  rapid prototyping
- Pin headers for access to power and signals for the Main MCU

**Multiple clock sources**

- Main MCU oscillator crystals, providing precision 12.000 MHz and 32,768 Hz external reference
  clocks
- Additional low-precision clocks are available internal to the Main MCU

**General purpose I/O ports**

- One jumper to allow measuring of Main MCU current
- Copper jumpers on PCB bottom side for configuration and access to selected MCU signals

**Operating voltage**

- External 5 V input through the Debug USB connector supplies the on-board power regulator to power
  logic and interfaces on the board. External 5 V or 3.3 V may be also supplied through alternate
  locations on the board.
- A two-color board status LED indicating availability of regulated power and connection status of the J-Link
  interface.
- A red User LED, controlled by the Main MCU firmware
- A User Push-Button switch, User Capacitive Touch Button sensor, and an optional User Potentiometer,
  all of which are controlled by the Main MCU firmware
- MCU reset push-button switch
- MCU boot configuration jumper

## Hardware

Detailed hardware features can be found at:

- RA4M1 MCU: [RA4M1 Group User’s Manual Hardware](https://www.renesas.com/us/en/document/mah/renesas-ra4m1-group-users-manual-hardware?r=1054146)
- EK-RA4M1 board: [EK-RA4M1 - User’s Manual](https://www.renesas.com/us/en/document/mat/ek-ra4m1-v1-users-manual)

### Supported Features

The `ek_ra4m1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

Applications for the `ek_ra4m1` board can be built, flashed, and debugged
in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details on building and running.

### Flashing

Program can be flashed to EK-RA4M1 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as describe in [EK-RA4M1 - User’s Manual](https://www.renesas.com/us/en/document/mat/ek-ra4m1-v1-users-manual)
3. Execute west command

> ```shell
> west flash -r jlink
> ```

### Debugging

You can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA4M1AB
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

**Note:** It’s verified that we can debug OK on Segger Ozone v3.30d so please use this or later
version of Segger Ozone

## References

- [EK-RA4M1 Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ek-ra4m1-evaluation-kit-ra4m1-mcu-group)
- [RA4M1 MCU group Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra4m1-32-bit-microcontrollers-48mhz-arm-cortex-m4-and-lcd-controller-and-cap-touch-hmi)
