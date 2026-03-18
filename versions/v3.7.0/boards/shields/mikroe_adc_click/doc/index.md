---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/shields/mikroe_adc_click/doc/index.html
original_path: boards/shields/mikroe_adc_click/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MikroElektronika ADC Click

## Overview

The MikroElektronika ADC Click carries the [MCP3204](https://www.microchip.com/wwwproducts/en/en010533) 12-bit
Analog-to-Digital converter in a [mikroBUS](https://www.mikroe.com/mikrobus)™ form factor.

![MikroElektronika ADC Click](../../../../_images/adc-click.jpg)

MikroElektronika ADC Click (Credit: MikroElektronika)

## Requirements

This shield can only be used with a development board that provides a
configuration for mikroBUS connectors and defines a node alias for the mikroBUS
SPI interface (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

For more information about interfacing the MCP3204 and the ADC Click,
see the following documentation:

- [MCP3204 Datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21298e.pdf)
- [ADC Click](https://www.mikroe.com/adc-click)

## Programming

Set `--shield mikro_adc_click` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s16 --shield mikroe_adc_click <my_app>
```
