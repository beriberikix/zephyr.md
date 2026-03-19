---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/shields/x_nucleo_iks02a1/sensorhub/README.html
original_path: samples/shields/x_nucleo_iks02a1/sensorhub/README.html
---

# X-NUCLEO-IKS02A1 shield - SensorHub (Mode 2)

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/x_nucleo_iks02a1/sensorhub/README.rst/..)

## Overview

This sample is provided as an example to test the X-NUCLEO-IKS02A1 shield
configured in Sensor Hub mode (Mode 2).
Please refer to [X-NUCLEO-IKS02A1: MEMS Inertial and Environmental Multi sensor shield](../../../../boards/shields/x_nucleo_iks02a1/doc/index.md#x-nucleo-iks02a1) for more info on this configuration.

This sample enables IIS2DLPC and ISM330DHCX sensors. Since all other shield
devices are connected to ISM330DHCX, the ISM330DHCX driver is configured in sensorhub
mode (CONFIG\_ISM330DHCX\_SENSORHUB=y) with the IIS2MDC magnetometer as external
slave.

Then sensor data are displayed periodically

- IIS2DLPC 3-Axis acceleration
- ISM330DHCX 6-Axis acceleration and angular velocity
- ISM330DHCX (from IIS2MDC) 3-Axis magnetic field intensity

## Requirements

This sample communicates over I2C with the X-NUCLEO-IKS02A1 shield
stacked on a board with an Arduino connector. The board’s I2C must be
configured for the I2C Arduino connector (both for pin muxing
and devicetree). See for example the [Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo_f401re) board
source code:

- [boards/st/nucleo\_f401re/nucleo\_f401re.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f401re/nucleo_f401re.dts)

Please note that this sample can’t be used with boards already supporting
one of the sensors available on the shield (such as disco\_l475\_iot1)
as sensors multiple instances are not supported.

## References

- X-NUCLEO-IKS02A1: [https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html)

## Building and Running

This sample runs with X-NUCLEO-IKS02A1 stacked on any board with a matching
Arduino connector. For this example, we use a [Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo_f401re) board.

```shell
west build -b nucleo_f401re samples/shields/x_nucleo_iks02a1/sensorhub/
```

### Sample Output

> ```shell
> X-NUCLEO-IKS02A1 sensor Mode 2 dashboard
>
> IIS2DLPC: Accel (m.s-2): x: 0.077, y: -0.766, z: 9.878
> ISM330DHCX: Accel (m.s-2): x: 0.383, y: -0.234, z: 9.763
> ISM330DHCX: GYro (dps): x: 0.004, y: 0.003, z: -0.005
> ISM330DHCX: Magn (gauss): x: 0.171, y: 0.225, z: -0.363
> 7:: iis2dlpc trig 1215
> 7:: ism330dhcx acc trig 2494
> 7:: ism330dhcx gyr trig 2494
>
> <updated endlessly every 2 seconds>
> ```

## See also

[Sensor Interface](../../../../doxygen/html/group__sensor__interface.md)
