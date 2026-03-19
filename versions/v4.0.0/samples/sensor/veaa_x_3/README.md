---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/veaa_x_3/README.html
original_path: samples/sensor/veaa_x_3/README.html
---

# VEAA-X-3 proportional pressure control valve

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/veaa_x_3/README.rst/..)

## Overview

A sensor sample that demonstrates how to use a VEAA-X-3 device.

## Building and Running

This sample sets the valve setpoint then reads the actual pressure.
This is done continuously. When the maximum supported pressure is reached the setpoint is reset to
the valve’s minimum supported pressure value.

```shell
west build -b <board to use> samples/sensor/veaa_x_3
west flash
```

### Sample Output

```shell
Testing test_veaa_x_3
Valve range: 1 to 200 kPa
Setpoint:    1 kPa, actual:   1 kPa
Setpoint:    2 kPa, actual:   2 kPa
Setpoint:    3 kPa, actual:   3 kPa
...
Setpoint:  199 kPa, actual: 199 kPa
Setpoint:  200 kPa, actual: 200 kPa
Setpoint:    1 kPa, actual:   1 kPa
<repeats endlessly>
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
