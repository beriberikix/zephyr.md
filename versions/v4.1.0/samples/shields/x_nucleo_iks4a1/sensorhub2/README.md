---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/shields/x_nucleo_iks4a1/sensorhub2/README.html
original_path: samples/shields/x_nucleo_iks4a1/sensorhub2/README.html
---

# X-NUCLEO-IKS4A1: shield SHUB2 (Mode 2) sample

## Overview

This sample is provided as an example to test the X-NUCLEO-IKS4A1 shield
configured in Sensor Hub mode (Mode 2).
Please refer to [Mode 2: LSM6DSO16IS SensorHub Mode (SHUB2)](../../../../boards/shields/x_nucleo_iks4a1/doc/index.md#x-nucleo-iks4a1-mode-2) for more info on this configuration.

This sample enables LSM6DSO16IS IMU in sensorhub mode with LIS2MDL magnetometer and
LPS22DF pressure and temperature sensor.

Then sensor data are displayed periodically

- LSM6DSO16IS 6-Axis acceleration and angular velocity
- LSM6DSO16IS (from LIS2MDL) 3-Axis magnetic field intensity
- LSM6DSO16IS (from LPS22DF) ambient temperature and atmospheric pressure

## Requirements

This sample communicates over I2C with the X-NUCLEO-IKS4A1 shield
stacked on a board with an Arduino connector, e.g. the
[Nucleo F411RE](../../../../boards/st/nucleo_f411re/doc/index.md#nucleo_f411re) board.

## Building and Running

This sample runs with X-NUCLEO-IKS4A1 stacked on any board with a matching
Arduino connector. For this example, we use a [Nucleo F411RE](../../../../boards/st/nucleo_f411re/doc/index.md#nucleo_f411re) board.

```shell
west build -b nucleo_f411re samples/shields/x_nucleo_iks4a1/sensorhub2/
west flash
```

### Sample Output

> ```shell
> X-NUCLEO-IKS01A4 sensor dashboard
>
> LSM6DSO16IS: Accel (m.s-2): x: 0.081, y: -0.177, z: 9.945
> LSM6DSO16IS: GYro (dps): x: 0.001, y: -0.000, z: 0.004
> LSM6DSO16IS: Magn (gauss): x: 0.217, y: 0.015, z: -0.415
> LSM6DSO16IS: Temperature: 20.8 C
> LSM6DSO16IS: Pressure:99.756 kpa
> 736:: lsm6dso16is acc trig 314944
>
> <updated endlessly every 2 seconds>
> ```

## References

[X-NUCLEO-IKS4A1: MEMS Inertial and Environmental Multi sensor shield](../../../../boards/shields/x_nucleo_iks4a1/doc/index.md#x-nucleo-iks4a1)
