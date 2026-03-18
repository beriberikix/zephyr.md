---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/veaa_x_3/README.html
original_path: samples/sensor/veaa_x_3/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# VEAA-X-3 sample

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
