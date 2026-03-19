---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nuvoton/npcx7m6fb_evb/doc/index.html
original_path: boards/nuvoton/npcx7m6fb_evb/doc/index.html
---

# NPCX7M6FB\_EVB

Board Overview

[![../../../../_images/npcx7m6fb_evb.jpg](../../../../_images/npcx7m6fb_evb.jpg)
](../../../../_images/npcx7m6fb_evb.jpg)

NPCX7M6FB\_EVB

Name:
:   `npcx7m6fb_evb`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   npcx7m6fb

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/npcx7m6fb_evb/doc/index.rst/../..)

## Overview

The NPCX7M6FB\_EVB kit is a development platform to evaluate the
Nuvoton NPCX7 series microcontrollers. This board needs to be mated with
part number NPCX796FB.

## Hardware

- ARM Cortex-M4F Processor
- 256 KB RAM and 64 KB boot ROM
- ADC & GPIO headers
- UART0 and UART1
- FAN PWM interface
- Jtag interface
- Intel Modular Embedded Controller Card (MECC) headers

### Supported Features

The `npcx7m6fb_evb` board supports the hardware features listed below.

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

### System Clock

The NPCX7M6FB MCU is configured to use the 90Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 15 MHz. See Processor clock
control register (chapter 4 in user manual)

### Serial Port

UART1 is configured for serial logs.

## Programming and Debugging

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG only sessions.

### Flashing

If the correct IDC headers are installed, this board supports both J-TAG and
also the ChromiumOS servo.

To flash using Servo V2, μServo, or Servo V4 (CCD), see the
[Chromium EC Flashing Documentation](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board) [[1]](#id2) for more information.

To flash with J-TAG, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

```shell
# From the root of the zephyr repository
west build -b npcx7m6fb_evb samples/hello_world
west flash
```

### Debugging

Use JTAG/SWD with a J-Link

## References

[[1](#id3)]

[https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)
