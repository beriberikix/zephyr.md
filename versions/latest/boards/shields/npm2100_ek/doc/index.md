---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/npm2100_ek/doc/index.html
original_path: boards/shields/npm2100_ek/doc/index.html
---

# nPM2100 EK

## Overview

The nPM2100 EK lets you test different functions and features of the nPM2100
Power Management Integrated Circuit (PMIC).

## Requirements

The nPM2100 EK board is not a direct fit into an Arduino connector. However,
the Zephyr shield must be connected to the Arduino shield connectors. That is,
you need to connect the I2C lines to the `arduino_i2c` bus. This allows to
use the shield with any host board that supports the Arduino connector.

## Usage

To use the shield in any application, build it with the following command:

```shell
west build -b your_board --shield npm2100_ek
```

For a comprehensive sample, refer to [nPM2100 EK](../../../../samples/shields/npm2100_ek/doc/index.md#npm2100_ek "Interact with the nPM2100 PMIC using the EK buttons and the shell interface.").
