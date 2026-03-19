---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/max17262/README.html
original_path: samples/sensor/max17262/README.html
---

# MAX17262 Fuel Gauge Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/max17262/README.rst/..)

## Overview

This sample application periodically reads voltage, current and temperature
data from the MAX17262 device that implements SENSOR\_CHAN\_GAUGE\_VOLTAGE,
SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT, and SENSOR\_CHAN\_GAUGE\_TEMP.

## Requirements

The MAX17262 is an ultra-low power fuel-gauge IC which implements the Maxim
ModelGauge m5 algorithm. The IC monitors a single-cell battery pack and
supports internal current sensing for up to 3.1A pulse current. The IC
provides best performance for batteries with 100mAhr to 6Ahr capacity.

This sample requires a board which provides a configuration for Arduino
connectors and defines node aliases for the I2C interface.
For more info about the node structure see
[samples/sensor/max17262/app.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/max17262/app.overlay)

## Building and Running

This sample application uses an MAX17262 sensor connected to a board via I2C.
Connect the sensor pins according to the connection diagram given in the
[max17262 datasheet](https://datasheets.maximintegrated.com/en/ds/MAX17262.pdf) [[1]](#id1).

```shell
west build -b nrf52840dk/nrf52840 samples/sensor/max17262
west flash
```

### Sample Output

To check output of this sample , any serial console program can be used.
This example uses `picocom` on the serial port `/dev/ttyUSB0`:

```shell
$ sudo picocom -D /dev/ttyUSB0
```

```shell
V: 3.626406 V; I: -3.437500 mA; T: 28.011718 °C
V: 3.626406 V; I: -3.437500 mA; T: 28.011718 °C
V: 3.626406 V; I: -3.437500 mA; T: 28.011718 °C
```

## References

[[1](#id2)]

[https://datasheets.maximintegrated.com/en/ds/MAX17262.pdf](https://datasheets.maximintegrated.com/en/ds/MAX17262.pdf)

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
