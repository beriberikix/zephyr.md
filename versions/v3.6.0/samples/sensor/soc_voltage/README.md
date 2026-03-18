---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/soc_voltage/README.html
original_path: samples/sensor/soc_voltage/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SoC voltage sensor measurement

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
