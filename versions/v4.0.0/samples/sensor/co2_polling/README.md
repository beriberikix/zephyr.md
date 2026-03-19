---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/co2_polling/README.html
original_path: samples/sensor/co2_polling/README.html
---

# Generic CO2 polling sample

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/co2_polling/README.rst/..)

## Overview

A sensor sample that demonstrates how to poll a CO2 sensor.

## Building and Running

This sample reads the CO2 sensor and print the values continuously.

```shell
west build -b <board to use> samples/sensor/co2_polling
west flash
```

### Sample Output

```shell
CO2 940 ppm
CO2 950 ppm
```

<repeats endlessly>

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
