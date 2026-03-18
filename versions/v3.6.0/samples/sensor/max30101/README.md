---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/max30101/README.html
original_path: samples/sensor/max30101/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MAX30101 Heart Rate Sensor

## Overview

A sensor application that demonstrates how to poll data from the max30101 heart
rate sensor.

## Building and Running

This project configures the max30101 sensor on the [Hexiwear](../../../boards/arm/hexiwear_k64/doc/index.md#hexiwear-k64) board to
enable the green LED and measure the reflected light with a photodiode. The raw
ADC data prints to the console. Further processing (not included in this
sample) is required to extract a heart rate signal from the light measurement.

```shell
west build -b hexiwear_k64 samples/sensor/max30101
```

### Sample Output

```shell
GREEN=5731
GREEN=5750
GREEN=5748
GREEN=5741
GREEN=5735
GREEN=5737
GREEN=5736
GREEN=5748
```

<repeats endlessly>
