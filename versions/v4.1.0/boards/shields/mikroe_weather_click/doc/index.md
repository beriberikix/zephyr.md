---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/mikroe_weather_click/doc/index.html
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
interface or a `mikrobus_spi` node label for the mikroBUS™ SPI
interface (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

Note

By default the Weather Click is configured to use the I2C interface. In
order to use the SPI interface the jumper settings must be changed. See
the [Weather Click Schematic](https://download.mikroe.com/documents/add-on-boards/click/weather/weather-click-schematic-v101.pdf) for further details.

For more information about the BME280 and the Weather Click, see the following
documentation:

- [Weather Click](https://www.mikroe.com/weather-click)
- [Weather Click Schematic](https://download.mikroe.com/documents/add-on-boards/click/weather/weather-click-schematic-v101.pdf)
- [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)
- [BME280 Datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf)

## Programming

Set `--shield mikroe_weather_click_i2c` or
`--shield mikroe_weather_click_spi` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s16 --shield [mikroe_weather_click_i2c | mikroe_weather_click_spi] samples/sensor/bme280
```
