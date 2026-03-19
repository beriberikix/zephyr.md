---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/hts221/README.html
original_path: samples/sensor/hts221/README.html
---

# HTS221 Temperature and Humidity Monitor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/hts221/README.rst/..)

## Overview

This sample periodically reads temperature and humidity from the HTS221
Temperature & Humidity Sensor and displays it on the console

## Requirements

This sample uses the HTS221 sensor controlled using the I2C interface.

## References

> - HTS211: [https://www.st.com/en/mems-and-sensors/hts221.html](https://www.st.com/en/mems-and-sensors/hts221.html)

## Building and Running

> This project outputs sensor data to the console. It requires an HTS221
> sensor, which is present on the disco\_l475\_iot1 board.

```shell
west build -b disco_l475_iot1 samples/sensor/hts221
```

### Sample Output

> ```shell
> Temperature:25.3 C
> Relative Humidity:40%
> Temperature:25.3 C
> Relative Humidity:40%
> Temperature:25.3 C
> Relative Humidity:40%
> Temperature:25.3 C
> Relative Humidity:40%
>
> <repeats endlessly every 2 seconds>
> ```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
