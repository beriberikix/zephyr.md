---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/shields/x_nucleo_iks01a3/sensorhub/README.html
original_path: samples/shields/x_nucleo_iks01a3/sensorhub/README.html
---

# X-NUCLEO-IKS01A3 shield - SensorHub (Mode 2)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/x_nucleo_iks01a3/sensorhub/README.rst/..)

## Overview

This sample is provided as an example to test the X-NUCLEO-IKS01A3 shield
configured in Sensor Hub mode (Mode 2).
Please refer to [X-NUCLEO-IKS01A3: MEMS Inertial and Environmental Multi sensor shield](../../../../boards/shields/x_nucleo_iks01a3/doc/index.md#x-nucleo-iks01a3) for more info on this configuration.

This sample enables LIS2DW12 and LSM6DSO sensors. Since all other shield
devices are connected to LSM6DSO, the LSM6DSO driver is configured in sensorhub
mode (CONFIG\_LSM6DSO\_SENSORHUB=y) with a selection of two maximum slaves
among LPS22HH, HTS221 and LIS2MDL (default is LIS2MDL + LPS22HH).

Then sensor data are displayed periodically

- LIS2DW12 3-Axis acceleration
- LSM6DSO 6-Axis acceleration and angular velocity
- LSM6DSO (from LIS2MDL) 3-Axis magnetic field intensity
- LSM6DSO (from LPS22HH) ambient temperature and atmospheric pressure

Optionally HTS221 can substitute one between LIS2MDL and LPS22HH

- LSM6DSO (from HTS221): ambient temperature and relative humidity

## Requirements

This sample communicates over I2C with the X-NUCLEO-IKS01A3 shield
stacked on a board with an Arduino connector. The board’s I2C must be
configured for the I2C Arduino connector (both for pin muxing
and devicetree). See for example the [Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo_f401re) board
source code:

- `$ZEPHYR_BASE/boards/arm/nucleo_f401re/nucleo_f401re.dts`
- `$ZEPHYR_BASE/boards/arm/nucleo_f401re/pinmux.c`

Please note that this sample can’t be used with boards already supporting
one of the sensors available on the shield (such as disco\_l475\_iot1)
as sensors multiple instances are not supported.

## References

- X-NUCLEO-IKS01A3: [https://www.st.com/en/ecosystems/x-nucleo-iks01a3.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a3.html)

## Building and Running

This sample runs with X-NUCLEO-IKS01A3 stacked on any board with a matching
Arduino connector. For this example, we use a [Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo_f401re) board.

```shell
west build -b nucleo_f401re samples/shields/x_nucleo_iks01a3/sensorhub/
```

### Sample Output

> ```shell
> X-NUCLEO-IKS01A3 sensor dashboard
>
> LIS2DW12: Accel (m.s-2): x: -0.077, y: 0.536, z: 9.648
> LSM6DSO: Accel (m.s-2): x: -0.062, y: -0.028, z: 10.035
> LSM6DSO: GYro (dps): x: -0.003, y: -0.001, z: 0.000
> LSM6DSO: Magn (gauss): x: -0.052, y: -0.222, z: -0.059
> LSM6DSO: Temperature: 27.9 C
> LSM6DSO: Pressure:100.590 kpa
> 1:: lsm6dso acc trig 208
> 1:: lsm6dso gyr trig 208
>
> <updated endlessly every 2 seconds>
> ```

## See also

[Sensor Interface](../../../../doxygen/html/group__sensor__interface.md)
