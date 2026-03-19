---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/google/icetower/doc/index.html
original_path: boards/google/icetower/doc/index.html
---

# Icetower Development Board

Board Overview

Name:
:   `google_icetower`

Vendor:
:   Google, Inc.

Architecture:
:   arm

SoC:
:   stm32h743xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/google/icetower/doc/index.rst/../..)

## Overview

Google Icetower Development Board is a board created by Google for
fingerprint-related functionality development.

Board has connectors for fingerprint sensors. Console is exposed over [μServo](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md) [[2]](#id3)
connector. MCU can be flashed using μServo or SWD.

## Hardware

- STM32H7A3VIT6 LQFP100 package

### Pin Mapping

#### Default Zephyr Peripheral Mapping:

- USART\_1 TX/RX : PA9/PA10
- SPI\_1 CS/CLK/MISO/MOSI : PA4/PA5/PA6/PA7
- SPI\_4 CS/CLK/MISO/MOSI : PE11/PE12/PE13/PE14

## Programming and Debugging

Build application as usual for the `google_icetower` board, and flash
using μServo or an external J-Link connected to J4. If μServo is used, please
follow the [Chromium EC Flashing Documentation](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board) [[1]](#id1).

### Debugging

Use SWD with a J-Link or ST-Link. Remember that SW2 must be set to CORESIGHT.

## References

[[1](#id2)]

[https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)

[[2](#id4)]

[https://chromium.googlesource.com/chromiumos/third\_party/hdctools/+/master/docs/servo\_micro.md](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/master/docs/servo_micro.md)
