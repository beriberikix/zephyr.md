---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/max30101/README.html
original_path: samples/sensor/max30101/README.html
---

# MAX30101 Heart Rate Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/max30101/README.rst/..)

## Overview

A sensor application that demonstrates how to poll data from the max30101 heart
rate sensor.

## Building and Running

This project configures the max30101 sensor on the [Hexiwear](../../../boards/nxp/hexiwear/doc/index.md#hexiwear) board to
enable the green LED and measure the reflected light with a photodiode. The raw
ADC data prints to the console. Further processing (not included in this
sample) is required to extract a heart rate signal from the light measurement.

```shell
west build -b hexiwear/mk64f12 samples/sensor/max30101
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
