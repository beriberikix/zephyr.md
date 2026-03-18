---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/ms5837/README.html
original_path: samples/sensor/ms5837/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MS5837 Sensor Sample

## Overview

This sample application retrieves the pressure and temperature from a MS5837
sensor every 10 seconds, and prints this information to the UART console.

## Requirements

- [nRF52840 Preview development kit](http://www.nordicsemi.com/eng/Products/nRF52840-Preview-DK) [[1]](#id1)
- MS5837 sensor

## Wiring

The nrf52840 Preview development kit should be connected as follows to the
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

See [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) on how to flash the build.

## References

[[1](#id2)]

[http://www.nordicsemi.com/eng/Products/nRF52840-Preview-DK](http://www.nordicsemi.com/eng/Products/nRF52840-Preview-DK)
