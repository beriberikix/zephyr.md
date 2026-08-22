---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rsk_rx130/doc/index.html
original_path: boards/renesas/rsk_rx130/doc/index.html
---

# Renesas Starter Kit for RX130

Board Overview

[![../../../../_images/rsk_rx130.webp](../../../../_images/rsk_rx130.webp)
](../../../../_images/rsk_rx130.webp)

Renesas Starter Kit for RX130

Name:
:   `rsk_rx130`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   rx

SoC:
:   r5f51308axfp

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rsk_rx130/doc/index.rst/../..)

## Overview

The Renesas Starter Kit for RX130-512KB is the perfect starter kit for
developers who are new to the RX130 (Program Flash 512KB, Pin Count 100-pin),
which operates at up to 32 MHz and is based on the RXv1 core architecture,
making it suitable for various embedded applications

**MCU Native Pin Access**

The RSKRX130-512KB includes:

- 32-MHz, 32-bit RX MCUs in 100 pins LFQFP package, Micon Pin Headers
- Direct MCU pin access through standard headers for easy peripheral integration
- Internal high-speed oscillator and low-speed on-chip oscillators
- Three low power consumption modes

**System Control and Debugging**

- USB Full-Speed Device (mini-B connector) for communication and power
- Power source options:

  - USB-powered (debug port)
  - External power supply via standard input
- Debugging support:

  - Via Jlink debugger with RX adapter boards.
- User LEDs and buttons:

  - Four User LEDs (red x2, yellow, green)
  - Power LED (green) indicating availability of regulated power
  - One Reset button, three User buttons
- Ecosystems expansions:

  - Two Digilent Pmod (LCD and Spare) connectors
  - 2Kbit I2C EEPROM

**Special Feature Access**

- IEC60730 compliance
- Capacitive touch sensing unit
- LCD drive capability for displaying data or status in real-time applications

## Hardware

Detailed hardware features can be found at:

- RX130 MCU: [RX130 Group User’s Manual Hardware](https://www.renesas.com/en/document/mah/rx130-group-users-manual-hardware-rev300)
- RSK-RX130-512KB: [RSK\_RX130\_512KB - User’s Manual](https://www.renesas.com/en/document/mat/renesas-starter-kit-rx130-512kb-users-manual-rev100)

### Supported Features

The `rsk_rx130` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

The `rsk_rx130` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `rsk_rx130@512kb` board target can be built, flashed, and
debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

If you want to build Zephyr application for RSK-RX130 board using Renesas GCC RX toolchain follow
the steps below:

> - Download and install GCC for RX toolchain:
>
>   [https://llvm-gcc-renesas.com/rx-download-toolchains/](https://llvm-gcc-renesas.com/rx-download-toolchains/)
> - Set env variable:
>
> > ```shell
> > export ZEPHYR_TOOLCHAIN_VARIANT=cross-compile
> > export CROSS_COMPILE=<Path to your toolchain>/bin/rx-elf-
> > ```
>
> - Build the Blinky Sample for RSK-RX130-512KB:
>
> > ```shell
> > cd ~/zephyrproject/zephyr
> > west build -p always -b rsk_rx130@512kb samples/basic/blinky
> > ```

### Flashing

Program can be flashed to RSKRX130-512KB using Jlink with RX adapter boards, by
connecting the board’s debug connector port to the host PC. Here’s an example
for building and flashing the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rsk_rx130@512kb samples/hello_world
west flash
```

### Debugging

You can use [Renesas Debug extension](https://marketplace.visualstudio.com/items?itemName=RenesasElectronicsCorporation.renesas-debug) on Visual Studio code for a visual debug interface.
The configuration for launch.json is as below.

```json
{
  "version": "0.2.0",
  "configurations": [
      {
          "type": "renesas-hardware",
          "request": "launch",
          "name": "Renesas GDB Hardware Debugging",
          "target": {
              "deviceFamily": "RX",
              "device": "R5F51308",
              "debuggerType": "SEGGERJLINKRX",
          }
      }
  ]
}
```

## References

- [RSK\_RX130\_512KB Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/rx130-512kb-starter-kit-renesas-starter-kit-rx130-512kb)
- [RX130 MCU group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/rx130-cost-optimized-high-performance-32-bit-microcontroller-enhanced-touch-key-function-and-5v-operation)
