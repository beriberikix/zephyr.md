---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/npm1300_ek/doc/index.html
original_path: boards/shields/npm1300_ek/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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

The shield can be used in any application by setting `SHIELD` to
`npm1300_ek`. You can check [nPM1300 EK sample](../../../../samples/shields/npm1300_ek/doc/index.md#npm1300-ek-sample) for a comprehensive
sample.

## References

TBC
