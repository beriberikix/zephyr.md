---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/i2c/target_eeprom/README.html
original_path: samples/drivers/i2c/target_eeprom/README.html
---

# I2C Target

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/i2c/target_eeprom/README.rst/..)

## Overview

This sample demonstrates how to setup and use the [I2C Target API](../../../../hardware/peripherals/i2c.md#i2c-target-api) using the
[`zephyr,i2c-target-eeprom`](../../../../build/dts/api/bindings/mtd/zephyr%2Ci2c-target-eeprom.md#std-dtcompatible-zephyr-i2c-target-eeprom) device.

## Requirements

This sample requires an I2C peripheral which is capable of acting as a target.

This sample has been tested on [LPCXPRESSO55S69](../../../../boards/nxp/lpcxpresso55s69/doc/index.md#lpcxpresso55s69).

## Building and Running

The code for this sample can be found in [samples/drivers/i2c/target\_eeprom](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/i2c/target_eeprom).

To build and flash the application:

```shell
west build -b lpcxpresso55s69/lpc55s69/cpu0 samples/drivers/i2c/target_eeprom
west flash
```

## See also

[I2C Interface](../../../../doxygen/html/group__i2c__interface.md)
