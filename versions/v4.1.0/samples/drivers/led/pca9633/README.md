---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/led/pca9633/README.html
original_path: samples/drivers/led/pca9633/README.html
---

# PCA9633 LED

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/led/pca9633/README.rst/..)

## Overview

This sample controls 4 LEDs connected to a PCA9633 driver, using the
following pattern:

> 1. turn on LEDs
> 2. turn off LEDs
> 3. set the brightness to 50%
> 4. turn off LEDs
> 5. blink the LEDs
> 6. turn off LEDs

## Building and Running

Build the application for the [Nucleo F334R8](../../../../boards/st/nucleo_f334r8/doc/index.md#nucleo_f334r8) board, and connect
a PCA9633 LED driver on the bus I2C Arduino.

```shell
west build -b nucleo_f334r8_board samples/drivers/led/pca9633
```

For flashing the application, refer to the Flashing section of the
[Nucleo F334R8](../../../../boards/st/nucleo_f334r8/doc/index.md#nucleo_f334r8) board documentation.

## References

- PCA9633: [https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf](https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf)

## See also

[LED Interface](../../../../doxygen/html/group__led__interface.md)
