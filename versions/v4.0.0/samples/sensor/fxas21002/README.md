---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/fxas21002/README.html
original_path: samples/sensor/fxas21002/README.html
---

# FXAS21002 Gyroscope Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/fxas21002/README.rst/..)

## Overview

A sensor application that demonstrates how to use the fxas21002 data ready
interrupt to read gyroscope data synchronously.

## Building and Running

This project outputs sensor data to the console. It requires an fxas21002
sensor, which is present on the [Hexiwear](../../../boards/nxp/hexiwear/doc/index.md#hexiwear) board. It does not work on
QEMU.

```shell
west build -b hexiwear/mk64f12 samples/sensor/fxas21002
```

### Sample Output

```shell
X=    -2.063 Y=     0.813 Z=     0.188
X=    -1.750 Y=     1.063 Z=     0.063
X=    -2.000 Y=     0.625 Z=     0.063
X=    -2.188 Y=     0.625 Z=     0.188
X=    -2.125 Y=     1.313 Z=    -0.063
X=    -2.188 Y=     1.188 Z=     0.313
```

<repeats endlessly>

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
