---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/ens210/README.html
original_path: samples/sensor/ens210/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ams ens210 Relative Humidity and Temperature Sensor

## Overview

This sample application demonstrates how to use the ams ens210 sensor to
measure the ambient temperature and relative humidity.

## Building and Running

This sample application uses the sensor connected to the i2c stated in the
app.overlay file.
Flash the binary to a board of choice with a sensor connected.
For example build for a nucleo\_f446re board:

```shell
west build -b nucleo_f446re samples/sensor/ens210
west flash
```

### Sample Output

```shell
device is 0x20001174, name is ENS210
Temperature: 28.28881222 C; Humidity: 25.25689737%
Temperature: 28.28912472 C; Humidity: 25.25799105%
Temperature: 28.28959347 C; Humidity: 25.25760045%
```
