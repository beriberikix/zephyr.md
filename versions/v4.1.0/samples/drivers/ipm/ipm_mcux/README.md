---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/ipm/ipm_mcux/README.html
original_path: samples/drivers/ipm/ipm_mcux/README.html
---

# IPM on NXP LPC

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/ipm/ipm_mcux/README.rst/..)

## Overview

Some NXP microcontrollers from LPC family are dual-core, this
sample application uses a mailbox to send messages from one
processor core to the other.

This sample applies to the following boards:
:   - [LPCXPRESSO54114](../../../../boards/nxp/lpcxpresso54114/doc/index.md#lpcxpresso54114), two core processors (Cortex-M4F and Cortex-M0+)
    - [LPCXPRESSO55S69](../../../../boards/nxp/lpcxpresso55s69/doc/index.md#lpcxpresso55s69), two core processors (dual Cortex-M33)

## Requirements

- [LPCXPRESSO54114](../../../../boards/nxp/lpcxpresso54114/doc/index.md#lpcxpresso54114) board
- [LPCXPRESSO55S69](../../../../boards/nxp/lpcxpresso55s69/doc/index.md#lpcxpresso55s69) board

## Building the application for lpcxpresso54114/lpc54114/m4

```shell
# From the root of the zephyr repository
west build -b lpcxpresso54114/lpc54114/m4 --sysbuild samples/drivers/ipm/ipm_mcux
west debug
```

## Building the application for lpcxpresso55s69/lpc55s69/cpu0

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s69/lpc55s69/cpu0 --sysbuild samples/drivers/ipm/ipm_mcux
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

## See also

[IPM Interface](../../../../doxygen/html/group__ipm__interface.md)
