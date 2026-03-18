---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/sensor/lsm6dsl/README.html
original_path: samples/sensor/lsm6dsl/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LSM6DSL: IMU sensor Monitor

## Overview

This sample sets the LSM6DSL accelerometer and gyroscope to 104Hz
and enable a trigger on data ready. It displays on the console the
values for accelerometer and gyroscope, plus optionally the values of
any magnetometer or pressure sensor attached to it (sensorhub function).

## Requirements

This sample uses the LSM6DSL sensor controlled using the I2C or SPI interface.
It has been tested on both [96Boards Argonkey](../../../boards/arm/96b_argonkey/doc/index.md#b-argonkey) and disco\_l475\_iot1 board.

## References

- LSM6DSL [https://www.st.com/en/mems-and-sensors/lsm6dsl.html](https://www.st.com/en/mems-and-sensors/lsm6dsl.html)

## Building and Running

> This project outputs sensor data to the console. It requires an LSM6DSL
> sensor, which is present on both the [96Boards Argonkey](../../../boards/arm/96b_argonkey/doc/index.md#b-argonkey) and disco\_l475\_iot1 board.

### Building on ArgonKey board

```shell
west build -b 96b_argonkey samples/sensor/lsm6dsl
```

### Building on disco\_l475\_iot1 board

```shell
west build -b disco_l475_iot1 samples/sensor/lsm6dsl
```

### Building on nrf52840dk\_nrf52840 board with x-nucleo-iks01a2 shield

```shell
west build -b nrf52840dk_nrf52840 samples/sensor/lsm6dsl -- -DSHIELD=x_nucleo_iks01a2
```

### Sample Output

```shell
LSM6DSL sensor samples:

accel (-3.184000 -0.697000 9.207000) m/s2
gyro (0.065000 -0.029000 0.002000) dps
magn (-0.042000 0.294000 -0.408000) gauss
- (0) (trig_cnt: 190474)

<repeats endlessly every 2 seconds>
```

Note

The magn row is displayed only when running sample onto 96b\_argonkey board, where a magnetometer is connected to LSM6DSL.
