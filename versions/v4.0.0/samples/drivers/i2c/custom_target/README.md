---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/i2c/custom_target/README.html
original_path: samples/drivers/i2c/custom_target/README.html
---

# I2C Custom Target

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/i2c/custom_target/README.rst/..)

## Overview

This sample demonstrates how to setup an I2C custom target on the I2C interface
using the [I2C Target API](../../../../hardware/peripherals/i2c.md#i2c-target-api).

## Requirements

This sample requires an I2C peripheral which is capable of acting as a target.

This sample has been tested on [LPCXPRESSO55S69](../../../../boards/nxp/lpcxpresso55s69/doc/index.md#lpcxpresso55s69).

## Building and Running

The code for this sample can be found in [samples/drivers/i2c/custom\_target](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/i2c/custom_target).

To build and flash the application:

```shell
west build -b lpcxpresso55s69/lpc55s69/cpu0 samples/drivers/i2c/custom_target
west flash
```

## See also

[I2C Interface](../../../../doxygen/html/group__i2c__interface.md)
