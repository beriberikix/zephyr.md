---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/vl53l0x/README.html
original_path: samples/sensor/vl53l0x/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# VL53L0X: Time Of Flight sensor

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
