---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nuvoton/npcm400_evb/doc/index.html
original_path: boards/nuvoton/npcm400_evb/doc/index.html
---

# NPCM400\_EVB

Board Overview

[![../../../../_images/npcm400_evb.webp](../../../../_images/npcm400_evb.webp)
](../../../../_images/npcm400_evb.webp)

NPCM400\_EVB

Name:
:   `npcm400_evb`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   npcm400

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/npcm400_evb/doc/index.rst/../..)

## Overview

The NPCM400\_EVB kit is a development platform to evaluate the
Nuvoton NPCM4 series microcontrollers. This board needs to be mated with
part number NPCM400 Satellite Management Controller (SMC).

## Hardware

- ARM Cortex-M4F Processor
- Core clock up to 100 MHz
- 1MB Integrated Flash
- 32KB cache for XIP and Data
- 768 KB RAM and 64 KB boot ROM
- ADC & GPIO headers
- UART0 and UART1
- I2C/I3C
- RMII
- USB2.0 Device
- USB1.1 Host
- Secure Boot is supported

### Supported Features

The `npcm400_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

Nuvoton to provide the schematic for this board.

### Serial Port

UART0 is configured for serial logs. The default serial setup is 115200 8N1.

## Programming and Debugging

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG-only sessions.

### Flashing

If the correct headers are installed, this board supports J-TAG.

To flash with J-TAG, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b npcm400_evb samples/hello_world
west flash
```

Open a serial terminal, and you should see the following message in the terminal:

```shell
Hello World! npcm400_evb/npcm400
```

### Debugging

Use JTAG/SWD with a J-Link

## References
