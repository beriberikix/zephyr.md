---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/sensor/max6675/README.html
original_path: samples/sensor/max6675/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MAX6675 K-thermocouple to digital converter

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
