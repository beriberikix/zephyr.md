---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/renesas/voice_ra4e1/doc/index.html
original_path: boards/renesas/voice_ra4e1/doc/index.html
---

# RA4E1 Voice User Reference Kit

Board Overview

[![../../../../_images/voice_ra4e1.webp](../../../../_images/voice_ra4e1.webp)
](../../../../_images/voice_ra4e1.webp)

RA4E1 Voice User Reference Kit

Name:
:   `voice_ra4e1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa4e10d2cne

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/voice_ra4e1/doc/index.rst/../..)

## Overview

VOICE-RA4E1 is an edge voice recognition evaluation kit designed to be used by Ecosystem Partners,
Application Engineers, Field Application Engineers, and for Business Development opportunities. The
primary purpose is to evaluate the functionality of projects developed by Ecosystem Partners, and to
facilitate the development of additional partner projects. The kit design to use the RA4E1 MCU with QFN
48pin package as the core logic device, with QSPI flash, OPAMP and power devices chosen from the
Renesas product portfolio.

The MCU in this series incorporates a high-performance Arm Cortex®-M33 core running up to
100 MHz with the following features:

**MCU Native Pin Access**

- R7FA4E10D2CNE MCU (referred to as RA MCU)
- 100 MHz, Arm® Cortex®-M33 core
- 512 KB Code Flash, 8 KB Data Flash, 128 KB SRAM
- 48 pins, LQFP package
- MCU current measurement point for precision current consumption measurement
- Multiple clock sources - Low-precision (~1%) clocks are available internal to the RA MCU.

**Kit Peripheral Features**

Following is a list of the specific features that have been implemented:

- QSPI: One QSPI flash memory device, Dialog AT25SF641B-MHB-T, 64M-bit (8MB).
- PMOD: 1 Digilent PMOD connectors, supporting UART, SPI and I2C configurations.
- Microphones: 1 I2S MEMS digital microphones and 2 MEMS analog microphones, distance between
  each pair of microphones is 50mm which is suitable for beamforming applications.
- Audio out: One stereo audio headphone jack supporting mono output on both channels.
- LEDs: Five LEDs, D2 (Red), D3 (Green) and D4 (Blue) configurable by user, D5 (Blue) as a 3.3V power
  indicator, D8(Green) as a JLOB (J-LINK on board) indicator.
- Buttons: One RESET button (S2), and one USER button (S1).
- Debug: J-Link On-Board debug interface, supporting JTAG or SWD debug port.
- USB: Micro USB-B (J6) for power input and J-Link On-Board function, USB-C (J1) for power input and
  RA4E1 USB Full Speed port as a USB device.
- Form Factor: 7.5 x 6 cm

## Hardware

Detailed hardware features can be found at:

- RA4E1 MCU: [RA4E1 Group User’s Manual Hardware](https://www.renesas.com/en/document/mah/ra4e1-group-users-manual-hardware)
- VOICE-RA4E1 board: [VOICE-RA4E1 - Engineering Manual](https://www.renesas.com/en/document/mat/voice-ra4e1-engineering-manual)

### Supported Features

The `voice_ra4e1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

Applications for the `voice_ra4e1` board can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

Program can be flashed to VOICE-RA4E1 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as describe in [VOICE-RA4E1 - Engineering Manual](https://www.renesas.com/en/document/mat/voice-ra4e1-engineering-manual)
3. Execute west command

   > ```shell
   > west flash -r jlink
   > ```

### Debugging

You can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA4E10D
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

**Note:** It’s verified that we can debug OK on Segger Ozone v3.30d so please use this or later
version of Segger Ozone

## References

- [VOICE-RA4E1 Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/tw001-vuia4e1pocz-ra4e1-voice-user-reference-kit)
- [RA4E1 MCU group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra4e1-100mhz-arm-cortex-m33-entry-line-balanced-low-power-consumption-optimized-feature-integration)
