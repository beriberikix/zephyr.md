---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/thingy53_nrf5340/doc/index.html
original_path: boards/arm/thingy53_nrf5340/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Thingy:53

## Overview

Zephyr uses the thingy53\_nrf5340 board configuration for building
for the Thingy:53 board. The board has the nRF5340 MCU processor, a set of
environmental sensors, a pushbutton, and RGB LED.

The nRF5340 is a dual-core SoC based on the Arm® Cortex®-M33 architecture, with:

- a full-featured Arm Cortex-M33F core with DSP instructions, FPU, and
  Armv8-M Security Extension, running at up to 128 MHz, referred to as
  the **application core**
- a secondary Arm Cortex-M33 core, with a reduced feature set, running at
  a fixed 64 MHz, referred to as the **network core**.

The nrf5340dk\_nrf5340\_cpuapp build target provides support for the application
core on the nRF5340 SoC. The nrf5340dk\_nrf5340\_cpunet build target provides
support for the network core on the nRF5340 SoC.

The [Nordic Semiconductor Infocenter](http://infocenter.nordicsemi.com/) [[1]](#id1) contains the processor’s information and
the datasheet.

## Programming and Debugging

### Flashing

Flashing Zephyr onto Thingy:53 requires an external J-Link programmer. The
programmer is attached to the P9 programming header.

### Debugging

Thingy:53 does not have an on-board J-Link debug IC as some other nRF5
development boards, however, instructions from the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page
also apply to this board, with the additional step of connecting an external
debugger. A development board with a Debug out connector such as the
[nRF5340 DK](../../nrf5340dk_nrf5340/doc/index.md#nrf5340dk-nrf5340) can be used as a debugger with Thingy:53.

## References

[[1](#id2)]

[http://infocenter.nordicsemi.com/](http://infocenter.nordicsemi.com/)
