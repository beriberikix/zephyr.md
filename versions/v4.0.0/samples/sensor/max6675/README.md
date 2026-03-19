---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/sensor/max6675/README.html
original_path: samples/sensor/max6675/README.html
---

# MAX6675 K-thermocouple to digital converter

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/max6675/README.rst/..)

## Overview

This is a sample application to read an external MAX6675
cold-junction-compensated K-thermocouple to digital converter.

## Requirements

- MAX6675 wired to your board SPI bus
- K-thermocouple connected to MAX6675 T+/T- inputs

## References

> - MAX6675: [https://datasheets.maximintegrated.com/en/ds/MAX6675.pdf](https://datasheets.maximintegrated.com/en/ds/MAX6675.pdf)

## Building and Running

This sample can be built with any board that supports SPI. A sample overlay is
provided for the NUCLEO-F030R8 board.

```shell
west build -b nucleo_f030r8 samples/sensor/max6675
```

### Sample Output

The application will read and print sensor temperature every second. Note that
temperature fetch will fail if the K-thermocouple is not connected. This is
because MAX6675 is able to detect if the K-thermocouple is connected or not.

```shell
Temperature: 25.25 C
Temperature: 25.50 C

<repeats endlessly every second>
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
