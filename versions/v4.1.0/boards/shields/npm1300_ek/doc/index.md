---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/npm1300_ek/doc/index.html
original_path: boards/shields/npm1300_ek/doc/index.html
---

# nPM1300 EK

## Overview

The nPM1300 EK lets you test different functions and features of the nPM1300
Power Management Integrated Circuit (PMIC).

## Requirements

The nPM1300 EK board is not designed to fit straight into an Arduino connector.
However, the Zephyr shield is designed expecting it to be connected to the
Arduino shield connectors. For example, the I2C lines need to be connected to
the `arduino_i2c` bus. This allows to use the shield with any host board that
supports the Arduino connector.

## Usage

The shield can be used in any application by setting `--shield npm1300_ek`
when invoking `west build`. You can check [nPM1300 EK](../../../../samples/shields/npm1300_ek/doc/index.md#npm1300_ek "Interact with the nPM1300 PMIC using the shell interface.") for a
comprehensive sample.

## References

TBC
