---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/shields/mikroe_accel13_click/doc/index.html
original_path: boards/shields/mikroe_accel13_click/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MikroElektronika ACCEL 13 Click

## Overview

The MikroElektronika ACCEL 13 Click carries the [IIS2DLPC](https://www.st.com/en/mems-and-sensors/iis2dlpc.html) ultra-low
power triaxial accelerometer sensor in a [mikroBUS](https://www.mikroe.com/mikrobus)™ form factor.

The [IIS2DLPC](https://www.st.com/en/mems-and-sensors/iis2dlpc.html) sensor supports both SPI and I2C bus protocols. Currently
only I2C is supported for this shield.

![MikroElektronika ACCEL 13 Click](../../../../_images/accel-13-click.jpg)

MikroElektronika ACCEL 13 Click (Credit: MikroElektronika)

## Requirements

This shield can only be used with a development board that provides a
configuration for mikroBUS connectors and defines a node alias for the mikroBUS
I2C interface (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

For more information about interfacing the IIS2DLPC and the ACCEL 13 Click,
see the following documentation:

- [IIS2DLPC Datasheet](https://www.st.com/resource/en/datasheet/iis2dlpc.pdf)
- [ACCEL 13 Click](https://www.mikroe.com/accel-13-click)

## Programming

Set `--shield mikro_accel13_click` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s69 --shield mikroe_accel13_click test/boards/board_shell
```
