---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/die_temp_polling/README.html
original_path: samples/sensor/die_temp_polling/README.html
---

# CPU die temperature polling

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/die_temp_polling/README.rst/..)

## Overview

This sample periodically reads temperature from the CPU Die
temperature sensor and display the results.

## Building and Running

To run this sample, enable the sensor node that supports `SENSOR_CHAN_DIE_TEMP`
and create an alias named `die-temp0` to link to the node.
The tail `0` is the sensor number. This sample support up to 15 sensors.

```shell
west build -b rpi_pico samples/sensor/die_temp_polling
```

### Sample Output

```shell
CPU Die temperature[dietemp]: 22.6 °C
CPU Die temperature[dietemp]: 22.8 °C
CPU Die temperature[dietemp]: 23.1 °C
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
