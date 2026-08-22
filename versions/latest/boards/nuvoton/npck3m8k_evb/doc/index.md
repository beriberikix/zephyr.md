---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nuvoton/npck3m8k_evb/doc/index.html
original_path: boards/nuvoton/npck3m8k_evb/doc/index.html
---

# NPCK3M8K\_EVB

Board Overview

[![../../../../_images/npck3m8k_evb.webp](../../../../_images/npck3m8k_evb.webp)
](../../../../_images/npck3m8k_evb.webp)

NPCK3M8K\_EVB

Name:
:   `npck3m8k_evb`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   npck3m8k

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/npck3m8k_evb/doc/index.rst/../..)

## Overview

The NPCK3M8K\_EVB kit is a development platform to evaluate the
Nuvoton NPCK3 series microcontrollers. This board is designed to provide
a range of peripherals and interfaces for development and testing. It needs
to be mated with part number NPCK3M8K.

## Hardware

- ARM Cortex-M4F Processor
- 352 KB RAM and 64 KB boot ROM
- GPIO headers
- UART0 and UART1
- JTAG interface

### Supported Features

The `npck3m8k_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The NPCK3M8K MCU is configured to use the 90Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 15 MHz. See Processor clock
control register (chapter 4 in user manual)

### Serial Port

UART1 is configured for serial logs.

## Programming and Debugging

The `npck3m8k_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG only sessions.

### Flashing

Build the application as usual for the `npck3m8k_evb` board.

### Debugging

Use JTAG/SWD with a J-Link.

## References
