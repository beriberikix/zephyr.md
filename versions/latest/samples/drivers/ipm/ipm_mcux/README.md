---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/ipm/ipm_mcux/README.html
original_path: samples/drivers/ipm/ipm_mcux/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# IPM on NXP LPC

## Overview

Some NXP microcontrollers from LPC family are dual-core, this
sample application uses a mailbox to send messages from one
processor core to the other.

This sample applies to the following boards:
:   - [NXP LPCXPRESSO54114](../../../../boards/arm/lpcxpresso54114/doc/index.md#lpcxpresso54114), two core processors (Cortex-M4F and Cortex-M0+)
    - [NXP LPCXPRESSO55S69](../../../../boards/arm/lpcxpresso55s69/doc/index.md#lpcxpresso55s69), two core processors (dual Cortex-M33)

## Requirements

- [NXP LPCXPRESSO54114](../../../../boards/arm/lpcxpresso54114/doc/index.md#lpcxpresso54114) board
- [NXP LPCXPRESSO55S69](../../../../boards/arm/lpcxpresso55s69/doc/index.md#lpcxpresso55s69) board

## Building the application for lpcxpresso54114\_m4

```shell
# From the root of the zephyr repository
west build -b lpcxpresso54114_m4 samples/drivers/ipm/ipm_mcux
west debug
```

## Building the application for lpcxpresso55s69\_cpu0

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s69_cpu0 samples/drivers/ipm/ipm_mcux
west debug
```

## Running

Open a serial terminal (minicom, putty, etc.) and connect the board with the
following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and the following message will appear on the corresponding
serial port:

```shell
***** Booting Zephyr OS v1.11.0-764-g4e3007a *****
Hello World from MASTER! arm
Received: 1
...
Received: 99
```
