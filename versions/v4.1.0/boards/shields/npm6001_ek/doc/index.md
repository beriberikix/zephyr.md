---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/npm6001_ek/doc/index.html
original_path: boards/shields/npm6001_ek/doc/index.html
---

# nPM6001 EK

## Overview

The nPM6001 EK lets you test different functions and features of the nPM6001
Power Management Integrated Circuit (PMIC).

![nPM6001 EK](../../../../_images/npm6001_ek.jpg)

nPM6001 EK

## Requirements

The nPM6001 EK board is not designed to fit straight into an Arduino connector.
However, the Zephyr shield is designed expecting it to be connected to the
Arduino shield connectors. For example, the I2C lines need to be connected to
the `arduino_i2c` bus. This allows to use the shield with any host board that
supports the Arduino connector.

## Usage

The shield can be used in any application by setting `--shield npm6001_ek`
when invoking `west build`. You can check [nPM6001 EK](../../../../samples/shields/npm6001_ek/doc/index.md#npm6001_ek "Interact with the nPM6001 PMIC using the shell interface.") for a
comprehensive sample.

## References

- [nPM6001 EK Manual](https://infocenter.nordicsemi.com/topic/ug_npm6001_ek/UG/nPM6001_EK/intro.html)
