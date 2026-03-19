---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/soc_voltage/README.html
original_path: samples/sensor/soc_voltage/README.html
---

# SoC Voltage Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/soc_voltage/README.rst/..)

## Overview

This sample reads one or more of the various voltage sensors an SoC might have and
displays the results.

## Building and Running

In order to run this sample, enable the sensor node that supports
`SENSOR_CHAN_VOLTAGE` and create an alias named `volt-sensor0` to link to the node.
The tail `0` is the sensor number. This sample support up to 16 sensors.

```shell
west build -b nucleo_g071rb samples/sensor/soc_voltage
```

### Sample Output

```shell
Sensor voltage: 2.99 V
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
