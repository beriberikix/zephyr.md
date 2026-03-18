---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/i2c/target_eeprom/README.html
original_path: samples/drivers/i2c/target_eeprom/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# I2C Target

## Overview

This sample demonstrates how to setup and use the [I2C Target API](../../../../hardware/peripherals/i2c.md#i2c-target-api) using the
[`zephyr,i2c-target-eeprom`](../../../../build/dts/api/bindings/mtd/zephyr%2Ci2c-target-eeprom.md#std-dtcompatible-zephyr-i2c-target-eeprom) device.

## Requirements

This sample requires an I2C peripheral which is capable of acting as a target.

This sample has been tested on [NXP LPCXPRESSO55S69](../../../../boards/nxp/lpcxpresso55s69/doc/index.md#lpcxpresso55s69).

## Building and Running

The code for this sample can be found in [samples/drivers/i2c\_target](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/i2c_target).

To build and flash the application:

```shell
west build -b lpcxpresso55s69/lpc55s69/cpu0 samples/drivers/i2c_target
west flash
```
