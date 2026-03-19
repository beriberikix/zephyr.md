---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/shields/x_nucleo_iks01a1/README.html
original_path: samples/shields/x_nucleo_iks01a1/README.html
---

# X-NUCLEO-IKS01A1 shield

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/x_nucleo_iks01a1/README.rst/..)

## Overview

This sample enables all sensors of a X-NUCLEO-IKS01A1 shield, and then
periodically reads and displays data from the shield sensors:

- HTS221: Temperature and humidity
- LPS25HB: Atmospheric pressure
- LIS3MDL: 3-axis Magnetic field intensity
- LSM6DSL: 3-Axis Acceleration

## Requirements

This sample communicates over I2C with the X-NUCLEO-IKS01A1 shield
stacked on a board with an Arduino connector. The board’s I2C must be
configured for the I2C Arduino connector (both for pin muxing
and devicetree).
Please note that this sample can’t be used with boards already supporting
one of the sensors available on the shield (such as disco\_l475\_iot1) as zephyr
does not yet support sensors multiple instances.

## References

-X-NUCLEO-IKS01A1: [https://www.st.com/en/ecosystems/x-nucleo-iks01a1.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a1.html)

## Building and Running

This sample runs with X-NUCLEO-IKS01A1 stacked on any board with a matching
Arduino connector. For this example, we use a [Nucleo F429ZI](../../../boards/st/nucleo_f429zi/doc/index.md#nucleo_f429zi) board.

```shell
west build -b nucleo_f429zi samples/shields/x_nucleo_iks01a1
```

### Sample Output

> ```shell
> X-NUCLEO-IKS01A1 sensor dashboard
>
> HTS221: Temperature:29.1 C
> HTS221: Relative Humidity:46.0%
> LPS25HB: Pressure:100.0 kpa
> LIS3MDL: Magnetic field (gauss): x: 0.1, y: -0.4, z: 0.4
> LSM6DS0: Acceleration (m.s-2): x: -0.0, y: -0.1, z: 9.7
>
>
> <updated endlessly every 2 seconds>
> ```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
