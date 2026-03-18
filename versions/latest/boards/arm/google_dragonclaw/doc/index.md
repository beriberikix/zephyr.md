---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/google_dragonclaw/doc/index.html
original_path: boards/arm/google_dragonclaw/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Google Dragonclaw Development Board

## Overview

Dragonclaw is a board created by Google for fingerprint-related functionality
development. See the [Dragonclaw Schematics](https://www.chromium.org/chromium-os/dragonclaw/dragonclaw_v0.2.html) [[1]](#id1) for board schematics, layout and
BOM.

Board has connectors for fingerprint sensors. Console is exposed over μServo
connector. MCU can be flashed using μServo or SWD.

## Hardware

- STM32F412CGU6 UFQFPN48 package

### Peripherial Mapping

- USART\_1 TX/RX : PA9/PA10
- USART\_2 TX/RX : PA2/PA3
- SPI\_1 CS/CLK/MISO/MOSI : PA4/PA5/PA6/PA7
- SPI\_2 CS/CLK/MISO/MOSI : PB12/PB13/PB14/PB15

## Programming and Debugging

Build application as usual for the `dragonclaw` board, and flash
using μServo or an external J-Link connected to J4. If μServo is used, please
follow the [Chromium EC Flashing Documentation](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board) [[2]](#id3).

### Debugging

Use SWD with a J-Link or ST-Link. Remember that SW2 must be set to CORESIGHT.

## References

[[1](#id2)]

[https://www.chromium.org/chromium-os/dragonclaw/dragonclaw\_v0.2.html](https://www.chromium.org/chromium-os/dragonclaw/dragonclaw_v0.2.html)

[[2](#id4)]

[https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)
