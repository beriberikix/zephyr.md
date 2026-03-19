---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/lps22hh/README.html
original_path: samples/sensor/lps22hh/README.html
---

# LPSS22HH Temperature and Pressure Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/lps22hh/README.rst/..)

## Overview

This sample periodically reads pressure from the LPS22HH MEMS pressure
sensor and displays it on the console.

## Requirements

This sample uses the LPS22HH sensor controlled using the I2C interface.

## References

- LPS22HH: [https://www.st.com/en/mems-and-sensors/lps22hh.html](https://www.st.com/en/mems-and-sensors/lps22hh.html)

## Building and Running

This project outputs sensor data to the console. It requires an LPS22HH
sensor, which is present on the X-NUCLEO-IKS01A3 shield.

```shell
west build -b nrf52dk/nrf52832 --shield x_nucleo_iks01a3 samples/sensor/lps22hh
```

### Sample Output

```shell
Configured for triggered collection at 1 Hz
Observation: 1
Pressure: 97.474 kPa
Temperature: 22.19 C
Observation: 2
Pressure: 97.466 kPa
Temperature: 22.21 C
Observation: 3
Pressure: 97.473 kPa
Temperature: 22.21 C
Observation: 4
Pressure: 97.455 kPa
Temperature: 22.21 C

<repeats endlessly every second>
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
