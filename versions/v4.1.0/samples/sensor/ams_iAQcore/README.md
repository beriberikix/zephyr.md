---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/ams_iAQcore/README.html
original_path: samples/sensor/ams_iAQcore/README.html
---

# ams iAQcore indoor air quality sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/ams_iAQcore/README.rst/..)

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

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
