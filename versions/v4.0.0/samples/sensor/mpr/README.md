---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/mpr/README.html
original_path: samples/sensor/mpr/README.html
---

# MPR Pressure Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/mpr/README.rst/..)

## Overview

This sample application periodically (1Hz) measures atmospheric pressure in
kilopascal. The result is written to the console.

## References

- MPR: [https://sensing.honeywell.com/micropressure-mpr-series](https://sensing.honeywell.com/micropressure-mpr-series)

## Wiring

This sample uses an MPRLS0025PA00001A sensor controlled using the i2c
interface. Connect **VIN**, **GND** and Interface: **SDA**, **SCL**.

## Building and Running

This project outputs sensor data to the console. It requires a sensor from the
MPR series.
It does not work on QEMU.
In the sample below the [Arduino Due](../../../boards/arduino/due/doc/index.md#arduino-due) board is used.

```shell
# From the root of the zephyr repository
west build -b arduino_due samples/sensor/mpr
west flash
```

## Sample Output

```shell
pressure value: 101.976303 kPa
pressure value: 101.986024 kPa
pressure value: 101.989736 kPa
pressure value: 101.987424 kPa
pressure value: 101.992099 kPa
pressure value: 101.989171 kPa
pressure value: 101.984226 kPa

<repeats endlessly>
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
