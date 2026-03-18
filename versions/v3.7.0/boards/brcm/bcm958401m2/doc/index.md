---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/brcm/bcm958401m2/doc/index.html
original_path: boards/brcm/bcm958401m2/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Broadcom BCM958401M2

## Overview

The Broadcom BCM958401M2 board utilizes the Valkyrie BCM58400 SoC to
provide support for PCIe offload engine functionality.

## Hardware

The BCM958401M2 is a PCIe card with the following physical features:

- PCIe Gen3 interface
- RS232 UART (optionally populated)
- JTAG (optionally populated)

### Supported Features

The Broadcom BCM958401M2 board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| UART | on-chip | serial port |

Other hardware features have not been enabled yet for this board.

The default configuration can be found in
[boards/brcm/bcm958401m2/bcm958401m2\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/brcm/bcm958401m2/bcm958401m2_defconfig)

### Connections and IOs

## Programming and Debugging

### Flashing

The flash on board is not supported by Zephyr at this time.
Board is booted over PCIe interface.

### Debugging

The bcm958401m2 board includes pads for soldering a JTAG connector.
Zephyr applications running on the M7 core can also be tested by observing UART console output.

## References
