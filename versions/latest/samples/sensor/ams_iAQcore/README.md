---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/ams_iAQcore/README.html
original_path: samples/sensor/ams_iAQcore/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ams iAQcore Indoor air quality sensor

## Overview

This sample application demonstrates how to use the ams iAQcore sensor to
measure CO2 equivalent and VOC. The CO2 value is a predicted value derived from
VOC. The values are fetched and printed every second.

## Building and Running

This sample application uses the sensor connected to the i2c stated in the
app.overlay file.
Flash the binary to a board of choice with a sensor connected.
This sample can run on every board with i2c.
For example build for a nucleo\_f446re board:

```shell
west build -b nucleo_f446re samples/sensor/ams_iAQcore
west flash
```

### Sample Output

```shell
device is 0x20001a08, name is IAQ_CORE
Co2: 882.000000ppm; VOC: 244.000000ppb
Co2: 863.000000ppm; VOC: 239.000000ppb
Co2: 836.000000ppm; VOC: 232.000000ppb
```
