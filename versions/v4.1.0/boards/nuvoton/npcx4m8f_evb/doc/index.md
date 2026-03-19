---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nuvoton/npcx4m8f_evb/doc/index.html
original_path: boards/nuvoton/npcx4m8f_evb/doc/index.html
---

# NPCX4M8F\_EVB

Board Overview

[![../../../../_images/npcx4m8f_evb.jpg](../../../../_images/npcx4m8f_evb.jpg)
](../../../../_images/npcx4m8f_evb.jpg)

NPCX4M8F\_EVB

Name:
:   `npcx4m8f_evb`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   npcx4m8f

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/npcx4m8f_evb/doc/index.rst/../..)

## Overview

The NPCX4M8F\_EVB kit is a development platform to evaluate the
Nuvoton NPCX4 series microcontrollers. This board needs to be mated with
part number NPCX498F.

## Hardware

- ARM Cortex-M4F Processor
- 512 KB RAM and 64 KB boot ROM
- ADC & GPIO headers
- UART0 and UART1
- FAN PWM interface
- Jtag interface
- Intel Modular Embedded Controller Card (MECC) headers

### Supported Features

The `npcx4m8f_evb` board supports the hardware features listed below.

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

The NPCX4M8F MCU is configured to use the 120Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 15 MHz. See Processor clock
control register (chapter 4 in user manual)

### Serial Port

UART1 is configured for serial logs.

## Programming and Debugging

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG-only sessions.

### Flashing

If the correct headers are installed, this board supports both J-TAG and also
the ChromiumOS servo.

To flash using Servo V2, μServo, or Servo V4 (CCD), see the
[Chromium EC Flashing Documentation](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board) [[1]](#id2) for more information.

To flash with J-TAG, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

The openocd from Zephyr SDK 0.16.1 doesn’t include npcx4 support, so build openocd from source.:

```text
sudo apt-get install libftdi-dev libusb-1.0.0-dev
git clone https://git.code.sf.net/p/openocd/code ~/openocd
cd ~/openocd
./bootstrap
./configure --enable-jlink --enable-ftdi
make clean
make
sudo make install
```

Build and flash the blinky sample.:

```text
west build -t clean && \
  west build -c -p auto -b npcx4m8f_evb samples/basic/blinky && \
  west flash --openocd /usr/local/bin/openocd
```

### Debugging

Use JTAG/SWD with a J-Link

## References

[[1](#id3)]

[https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)
