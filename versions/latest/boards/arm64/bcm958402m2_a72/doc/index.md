---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm64/bcm958402m2_a72/doc/index.html
original_path: boards/arm64/bcm958402m2_a72/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Broadcom BCM958402M2 (Cortex-A72)

## Overview

The Broadcom bcm958402m2\_a72 board utilizes the Viper BCM58402\_A72 SoC
to provide support for PCIe offload engine functionality.

## Hardware

The bcm958402m2\_a72 is a PCIe card with the following physical features:

- PCIe Gen4 interface
- RS232 UART (optionally populated)
- JTAG (optionally populated)

### Supported Features

The Broadcom bcm958402m2\_a72 board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GIC-500 | on-chip | GICv3 interrupt controller |
| UART | on-chip | NS16550 compatible serial port |

Other hardware features have not been enabled yet for this board.

The default configuration can be found in the defconfig file:

> `boards/arm/bcm958402m2_a72/bcm958402m2_a72_defconfig`

## Programming and Debugging

### Flashing

The flash on board is not supported by Zephyr at this time.
Board is booted over PCIe interface.

### Debugging

The bcm958402m2\_a72 board includes pads for soldering a JTAG connector.
Zephyr applications running on the Cortex-A72 core can also be tested
by observing UART console output.
