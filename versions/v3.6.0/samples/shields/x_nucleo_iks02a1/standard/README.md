---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/shields/x_nucleo_iks02a1/standard/README.html
original_path: samples/shields/x_nucleo_iks02a1/standard/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# X-NUCLEO-IKS02A1 shield - Standard (Mode 1)

## Overview

This sample is provided as an example to test the X-NUCLEO-IKS02A1 shield
configured in Standard mode (Mode 1).
Please refer to [X-NUCLEO-IKS02A1: MEMS Inertial and Environmental Multi sensor shield](../../../../boards/shields/x_nucleo_iks02a1/doc/index.md#x-nucleo-iks02a1) for more info on this configuration.

This sample enables all sensors of a X-NUCLEO-IKS02A1 shield, and then
periodically reads and displays data from the shield sensors:

- IIS2MDC 3-Axis magnetic field intensity
- IIS2DLPC 3-Axis acceleration
- ISM330DHCX 6-Axis acceleration and angular velocity

## Requirements

This sample communicates over I2C with the X-NUCLEO-IKS02A1 shield
stacked on a board with an Arduino connector. The board’s I2C must be
configured for the I2C Arduino connector (both for pin muxing
and devicetree). See for example the [ST Nucleo F401RE](../../../../boards/arm/nucleo_f401re/doc/index.md#nucleo-f401re-board) board
source code:

- `$ZEPHYR_BASE/boards/arm/nucleo_f401re/nucleo_f401re.dts`
- `$ZEPHYR_BASE/boards/arm/nucleo_f401re/pinmux.c`

Please note that this sample can’t be used with boards already supporting
one of the sensors available on the shield (such as disco\_l475\_iot1)
as sensors multiple instances are not supported.

## References

- X-NUCLEO-IKS02A1: [https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html)

## Building and Running

This sample runs with X-NUCLEO-IKS02A1 stacked on any board with a matching
Arduino connector. For this example, we use a [ST Nucleo F401RE](../../../../boards/arm/nucleo_f401re/doc/index.md#nucleo-f401re-board) board.

```shell
west build -b nucleo_f401re samples/shields/x_nucleo_iks02a1/standard/
```

### Sample Output

> ```shell
> X-NUCLEO-IKS02A1 sensor Mode 1 dashboard
>
> IIS2DLPC: Accel (m.s-2): x: 0.000, y: 0.000, z: 9.342
> IIS2MDC: Magn (gauss): x: -0.120, y: -0.095, z: -0.338
> IIS2MDC: Temperature: 25.1 C
> ISM330DHCX: Accel (m.s-2): x: 0.182, y: -0.306, z: 9.753
> ISM330DHCX: GYro (dps): x: 0.005, y: 0.001, z: -0.004
> 5:: iis2dlpc trig 809
> 5:: ism330dhcx acc trig 3332
> 5:: ism330dhcx gyr trig 1666
>
> <updated endlessly every 2 seconds>
> ```
