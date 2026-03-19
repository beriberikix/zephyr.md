---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/mikroe_weather_click/doc/index.html
original_path: boards/shields/mikroe_weather_click/doc/index.html
---

# MikroElektronika Weather Click

## Overview

The MikroElektronika [Weather Click](https://www.mikroe.com/weather-click) features the [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/) integrated
environmental sensor in a [mikroBUS](https://www.mikroe.com/mikrobus)™ form factor. The sensor can
measure relative humidity, barometric pressure, and ambient temperature.

![MikroElektronika Weather Click](../../../../_images/weather-click.webp)

MikroElektronika Weather Click (Credit: MikroElektronika)

## Requirements

This shield can only be used with a board that provides a mikroBUS™
socket and defines a `mikrobus_i2c` node label for the mikroBUS™ I2C
interface (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

For more information about the BME280 and the Weather Click, see the following
documentation:

- [Weather Click](https://www.mikroe.com/weather-click)
- [Weather Click Schematic](https://download.mikroe.com/documents/add-on-boards/click/weather/weather-click-schematic-v101.pdf)
- [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)
- [BME280 Datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf)

## Programming

Set `--shield mikroe_weather_click` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s16 --shield mikroe_weather_click samples/sensor/bme280
```
