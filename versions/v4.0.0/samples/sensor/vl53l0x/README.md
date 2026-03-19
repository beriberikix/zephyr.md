---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/vl53l0x/README.html
original_path: samples/sensor/vl53l0x/README.html
---

# VL53L0X Time Of Flight sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/vl53l0x/README.rst/..)

## Overview

This sample periodically measures distance between vl53l0x sensor
and target. The result is displayed on the console.
It also shows how we can use the vl53l0x as a proximity sensor.

## Requirements

This sample uses the VL53L0X sensor controlled using the I2C interface.

## References

> - VL53L0X: [https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x.html](https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x.html)

## Building and Running

> This project outputs sensor data to the console. It requires a VL53L0X
> sensor, which is present on the disco\_l475\_iot1 board.
>
> ```shell
> # From the root of the zephyr repository
> west build -b None samples/sensor/vl53l0x/
> west flash
> ```

### Sample Output

> ```shell
> prox is 0
> distance is 1938
> prox is 1
> distance is 70
> prox is 0
> distance is 1995
>
> <repeats endlessly every second>
> ```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
