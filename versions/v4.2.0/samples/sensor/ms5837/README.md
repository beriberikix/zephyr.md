---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/sensor/ms5837/README.html
original_path: samples/sensor/ms5837/README.html
---

# MS5837 Digital Pressure Sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/ms5837/README.rst/..)

## Overview

This sample application retrieves the pressure and temperature from a MS5837
sensor every 10 seconds, and prints this information to the UART console.

## Requirements

- [nRF52840 Development kit](https://www.nordicsemi.com/Products/Development-hardware/nRF52840-DK) [[1]](#id1)
- MS5837 sensor

## Wiring

The nrf52840 Development kit should be connected as follows to the
MS5837 sensor.

| nrf52840  Pin | MS5837  Pin |
| --- | --- |
| P0.3 | SCL |
| P0.31 | SDA |

## Building and Running

Build this sample using the following commands:

```shell
west build -b nrf52840dk/nrf52840 samples/sensor/ms5837
```

See [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk) on how to flash the build.

## References

[[1](#id2)]

[https://www.nordicsemi.com/Products/Development-hardware/nRF52840-DK](https://www.nordicsemi.com/Products/Development-hardware/nRF52840-DK)

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
