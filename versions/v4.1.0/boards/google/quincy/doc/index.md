---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/google/quincy/doc/index.html
original_path: boards/google/quincy/doc/index.html
---

# Quincy

Board Overview

Name:
:   `google_quincy`

Vendor:
:   Google, Inc.

Architecture:
:   arm

SoC:
:   npcx9mfp

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/google/quincy/doc/index.rst/../..)

## Overview

Google Quincy is a board created for fingerprint-related functionality
development.

The board has connectors for fingerprint sensors. A UART Console is exposed
over μServo and USB connectors. The MCU can be flashed using μServo or SWD.

## Hardware

- NPCX99FPA0BX VFBGA144 package

### Peripheral Mapping

- UART\_1 (CONSOLE) TX/RX : GPIO65/GPIO64
- UART\_2 (PROG) TX/RX : GPIO86/GPIO75
- SPI\_0 (SHI) CS/CLK/MISO/MOSI : GPIO53/GPIO55/GPIO47/GPIO46
- SPI\_1 (SPIP) CS/CLK/MISO/MOSI : GPIOA6/GPIOA1/GPIO95/GPIOA3
- SPI\_2 (GP) CS/CLK/MISO/MOSI : GPIO30/GPIO25/GPIO24/GPIO31

## Programming and Debugging

Build application as usual for the `google_quincy` board target, and flash
using μServo or an external J-Link connected to J4. If μServo is used, please
follow the [Chromium EC Flashing Documentation](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board) [[1]](#id1) and
[Chromium Servo Micro Documentation](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md) [[2]](#id3).

### Debugging

Use SWD with a J-Link.

## References

[[1](#id2)]

[https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)

[[2](#id4)]

[https://chromium.googlesource.com/chromiumos/third\_party/hdctools/+/master/docs/servo\_micro.md](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md)
