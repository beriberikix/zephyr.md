---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/co2_polling/README.html
original_path: samples/sensor/co2_polling/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Generic CO2 polling sample

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
