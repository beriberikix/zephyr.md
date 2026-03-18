---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/led_pca9633/README.html
original_path: samples/drivers/led_pca9633/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# PCA9633 LED

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

Build the application for the [ST Nucleo F334R8](../../../boards/st/nucleo_f334r8/doc/index.md#nucleo-f334r8-board) board, and connect
a PCA9633 LED driver on the bus I2C Arduino.

```shell
west build -b nucleo_f334r8_board samples/drivers/led_pca9633
```

For flashing the application, refer to the Flashing section of the
[ST Nucleo F334R8](../../../boards/st/nucleo_f334r8/doc/index.md#nucleo-f334r8-board) board documentation.

## References

- PCA9633: [https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf](https://www.nxp.com/docs/en/data-sheet/PCA9633.pdf)
