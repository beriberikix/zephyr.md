---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/grove_temperature/README.html
original_path: samples/sensor/grove_temperature/README.html
---

# Grove Temperature Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/grove_temperature/README.rst/..)

## Overview

This sample application gets the output of the grove temperature sensor and prints it to the
console, in units of celsius, once every second. When the [`CONFIG_GROVE_LCD_RGB`](../../../kconfig.md#CONFIG_GROVE_LCD_RGB "CONFIG_GROVE_LCD_RGB")
and [`CONFIG_I2C`](../../../kconfig.md#CONFIG_I2C "CONFIG_I2C") options are set, the temperature will also be displayed on the
Grove LCD display.

## Requirements

To use this sample, the following hardware is required:

- A board with ADC support
- [Grove Temperature Sensor](https://wiki.seeedstudio.com/Grove-Temperature_Sensor_V1.2/)
- [Grove Base Shield](https://wiki.seeedstudio.com/Base_Shield_V2/)
- [Grove LCD](https://wiki.seeedstudio.com/Grove-LCD_RGB_Backlight/) [optional]

## Wiring

The easiest way to connect the sensor is to connect it to a Grove shield on a board that supports
Arduino shields. Provide a devicetree overlay that specifies the sensor location. If using the
overlay provided for the sample, the sensor should be connected to A0 on the Grove shield. The
Grove LCD, if being used, should be connected to I2C on the Grove shield and the overlay needs to
contain an entry for it.

## Building and Running

Build and flash the sample as follows, changing `nrf52dk_nrf52832` to your board:

```shell
west build -b nrf52dk_nrf52832 samples/sensor/grove_temperature
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build v3.6.0-rc1-32-gba639ed6a893 ***
Temperature: 22.90 C
Temperature: 22.96 C
Temperature: 22.82 C
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
