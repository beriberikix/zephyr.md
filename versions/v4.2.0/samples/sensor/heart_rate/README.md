---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/sensor/heart_rate/README.html
original_path: samples/sensor/heart_rate/README.html
---

# Heart Rate Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/heart_rate/README.rst/..)

## Overview

A sensor application that demonstrates how to poll data from a heart rate
sensor.

## Requirements

- A supported heart rate sensor (e.g., MAX30101 or BH1790), available as `heart-rate-sensor` Devicetree alias.

## Building and Running

This project configures a sensor on the board to enable the green LED and
measure the reflected light with a photodiode. The raw data prints to the
console. Further processing (not included in this sample) is required to
extract a heart rate signal from the light measurement.

```shell
west build -b hexiwear/mk64f12 samples/sensor/heart_rate
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

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
