---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/shields/x_nucleo_iks01a2/sensorhub/README.html
original_path: samples/shields/x_nucleo_iks01a2/sensorhub/README.html
---

# X-NUCLEO-IKS01A2 shield - SensorHub (Mode 2)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/x_nucleo_iks01a2/sensorhub/README.rst/..)

## Overview

This sample is provided as an example to test the X-NUCLEO-IKS01A2 shield
configured in Sensor Hub mode (Mode 2).
Please refer to [X-NUCLEO-IKS01A2: MEMS Inertial and Environmental Multi sensor shield](../../../../boards/shields/x_nucleo_iks01a2/doc/index.md#x-nucleo-iks01a2) for more info on this configuration.

This sample enables LSM6DSL sensors. Since all other shield
devices are connected to LSM6DSL, the LSM6DSL driver is configured in sensorhub
mode (CONFIG\_LSM6DSL\_SENSORHUB=y) with a selection of one slave only
among LPS22HB and LSM303AGR (default is LSM303AGR)

Then sensor data are displayed periodically

- LSM6DSL 6-Axis acceleration and angular velocity
- LSM6DSL 3-Axis magnetic field intensity (from LSM303AGR mag) - Primary option
- LSM6DSL ambient temperature and atmospheric pressure (from LPS22HB) -
  Secondary option

## Requirements

This sample communicates over I2C with the X-NUCLEO-IKS01A2 shield
stacked on a board with an Arduino connector. The shield must be configured in
Mode 2.

Please note that this sample can’t be used with boards already supporting
one of the sensors available on the shield (such as disco\_l475\_iot1) as zephyr
does not yet support sensors multiple instances.

## References

-X-NUCLEO-IKS01A2: [https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html)

## Building and Running

This sample runs with X-NUCLEO-IKS01A2 stacked on any board with a matching
Arduino connector. For this example, we use a [Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo_f401re) board.

```shell
west build -b nucleo_f401re samples/shields/x_nucleo_iks01a2/sensorhub
```

### Sample Output

> ```shell
> X-NUCLEO-IKS01A2 sensor dashboard
>
> LSM6DSL: Accel (m.s-2): x: 0.0, y: 0.2, z: 10.0
> LSM6DSL: Gyro (dps): x: 0.029, y: -0.030, z: 0.016
> LSM6DSL: Magn (gauss): x: 0.363, y: -0.002, z: -0.559
> 9:: lsm6dsl acc trig 1668
>
> <updated endlessly every 2 seconds>
> ```

## See also

[Sensor Interface](../../../../doxygen/html/group__sensor__interface.md)
