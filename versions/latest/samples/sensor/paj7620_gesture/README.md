---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/sensor/paj7620_gesture/README.html
original_path: samples/sensor/paj7620_gesture/README.html
---

# PAJ7620 Gesture Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/paj7620_gesture/README.rst/..)

## Overview

This sample application gets the output of a gesture sensor (paj7620) using either polling or
triggers (depending on CONFIG\_APP\_USE\_POLLING) and outputs the corresponding gesture to the
console, each time one is detected.

## Requirements

To use this sample, the following hardware is required:

- A board with I2C support and GPIO to detect external interrutps
- PAJ7620 sensor

## Building and Running

This sample outputs data to the console. It requires a PAJ7620 sensor.

```shell
west build -b nucleo_f334r8 samples/sensor/paj7620_gesture
```

### Sample Output

```shell
Gesture LEFT
Gesture RIGHT
Gesture UP
Gesture DOWN
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
