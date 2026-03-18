---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/fxas21002/README.html
original_path: samples/sensor/fxas21002/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# FXAS21002 Gyroscope Sensor

## Overview

A sensor application that demonstrates how to use the fxas21002 data ready
interrupt to read gyroscope data synchronously.

## Building and Running

This project outputs sensor data to the console. It requires an fxas21002
sensor, which is present on the [Hexiwear](../../../boards/arm/hexiwear_k64/doc/index.md#hexiwear-k64) board. It does not work on
QEMU.

```shell
west build -b hexiwear_k64 samples/sensor/fxas21002
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
