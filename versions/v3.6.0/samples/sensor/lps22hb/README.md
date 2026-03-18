---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/lps22hb/README.html
original_path: samples/sensor/lps22hb/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LPS22HB: Temperature and Pressure Monitor

## Overview

This sample periodically reads pressure from the LPS22HB MEMS pressure
sensor and displays it on the console.

## Requirements

This sample uses the LPS22HB sensor controlled using the I2C interface.

## References

- LPS22HB: [https://www.st.com/en/mems-and-sensors/lps22hb.html](https://www.st.com/en/mems-and-sensors/lps22hb.html)

## Building and Running

This project outputs sensor data to the console. It requires an LPS22HB
sensor, which is present on the disco\_l475\_iot1 board.

```shell
west build -b disco_l475_iot1 samples/sensor/lps22hb
```

### Sample Output

```shell
Observation:1
Pressure:98.7 kPa
Temperature:22.5 C
Observation:2
Pressure:98.7 kPa
Temperature:22.5 C
Observation:3
Pressure:98.7 kPa
Temperature:22.5 C

<repeats endlessly every 2 seconds>
```
