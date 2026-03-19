---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/grove_light/README.html
original_path: samples/sensor/grove_light/README.html
---

# Grove Light Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/grove_light/README.rst/..)

## Overview

This sample application gets the output of the grove light sensor and prints it to the console, in
units of lux, once every second.

## Requirements

To use this sample, the following hardware is required:

- A board with ADC support
- [Grove Light Sensor](https://wiki.seeedstudio.com/Grove-Light_Sensor/)
- [Grove Base Shield](https://wiki.seeedstudio.com/Base_Shield_V2/)

## Wiring

The easiest way to connect the sensor is to connect it to a Grove shield on a board that supports
Arduino shields. Provide a devicetree overlay that specifies the sensor location. If using the
overlay provided for the sample, the sensor should be connected to A0 on the Grove shield.

## Building and Running

Build and flash the sample as follows, changing `nrf52dk_nrf52832` to your board:

```shell
west build -b nrf52dk_nrf52832 samples/sensor/grove_light
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build v3.6.0-rc1-32-gba639ed6a893 ***
lux: 0.945751
lux: 0.882292
lux: 0.755973
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
