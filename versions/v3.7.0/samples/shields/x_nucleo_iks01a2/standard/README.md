---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/shields/x_nucleo_iks01a2/standard/README.html
original_path: samples/shields/x_nucleo_iks01a2/standard/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# X-NUCLEO-IKS01A2 shield - Standard (Mode 1)

## Overview

This sample enables all sensors of a X-NUCLEO-IKS01A2 shield, and then
periodically reads and displays data from the shield sensors:

- HTS221: Ambient temperature and relative humidity
- LPS22HB: Atmospheric pressure and ambient temperature
- LSM6DSL: 3-Axis Acceleration and 3-Axis Angular Velocity
- LSM303AGR 3-Axis Acceleration and 3-axis Magnetic field intensity

## Requirements

This sample communicates over I2C with the X-NUCLEO-IKS01A2 shield
stacked on a board with an Arduino connector. The board’s I2C must be
configured for the I2C Arduino connector in the devicetree. See for
example the [ST Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo-f401re-board) board source code:

- [boards/st/nucleo\_f401re/nucleo\_f401re.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f401re/nucleo_f401re.dts)
- [boards/st/nucleo\_f401re/arduino\_r3\_connector.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f401re/arduino_r3_connector.dtsi)

Please note that this sample can’t be used with boards already supporting
one of the sensors available on the shield (such as disco\_l475\_iot1) as zephyr
does not yet support sensors multiple instances.

## References

-X-NUCLEO-IKS01A2: [https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html)

## Building and Running

This sample runs with X-NUCLEO-IKS01A2 stacked on any board with a matching
Arduino connector. For this example, we use a [ST Nucleo F401RE](../../../../boards/st/nucleo_f401re/doc/index.md#nucleo-f401re-board) board.

```shell
west build -b nucleo_f401re samples/shields/x_nucleo_iks01a2/standard
```

### Sample Output

> ```shell
> X-NUCLEO-IKS01A2 sensor dashboard
>
> HTS221: Temperature: 26.3 C
> HTS221: Relative Humidity: 44.5%
> LPS22HB: Pressure:99.220 kpa
> LPS22HB: Temperature: 26.1 C
> LSM6DSL: Accel (m.s-2): x: -0.0, y: -0.1, z: 10.0
> LSM6DSL: Gyro (dps): x: 0.028, y: -0.025, z: 0.014
> LSM303AGR: Accel (m.s-2): x: 0.3, y: -0.1, z: 9.7
> LSM303AGR: Magn (gauss): x: -0.221, y: -0.042, z: -0.458
>
> <updated endlessly every 2 seconds>
> ```
