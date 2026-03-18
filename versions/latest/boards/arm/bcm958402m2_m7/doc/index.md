---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/bcm958402m2_m7/doc/index.html
original_path: boards/arm/bcm958402m2_m7/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Broadcom BCM958402M2 (Cortex-M7)

## Overview

The Broadcom bcm958402m2\_m7 board utilizes the Viper BCM58402\_M7 SoC to
provide support for PCIe offload engine functionality.

## Hardware

The bcm958402m2\_m7 is a PCIe card with the following physical features:

- PCIe Gen4 interface
- RS232 UART (optionally populated)
- JTAG (optionally populated)

### Supported Features

The Broadcom bcm958402m2\_m7 board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| UART | on-chip | Compatible with UART NS16550 |

Other hardware features have not been enabled yet for this board.

The default configuration can be found in the defconfig file:

> `boards/arm/bcm958402m2_m7/bcm958402m2_m7_defconfig`

## Programming and Debugging

### Flashing

The flash on board is not supported by Zephyr at this time.
Board is booted over PCIe interface.

### Debugging

The bcm958402m2\_m7 board includes pads for soldering a JTAG connector.
Zephyr applications running on the M7 core can also be tested
by observing UART console output.
