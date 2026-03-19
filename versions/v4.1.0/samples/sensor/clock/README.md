---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/clock/README.html
original_path: samples/sensor/clock/README.html
---

# Sensor Clock

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/clock/README.rst/..)

## Overview

This sample application demonstrates how to select the sensor clock source
and utilize the Sensor Clock API.

## Building and Running

The sample below uses the [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) and [nRF52833 DK](../../../boards/nordic/nrf52833dk/doc/index.md#nrf52833dk-nrf52833) boards.

To run this sample, ensure the following configurations:

> - Enable one of the Kconfig options:
>   [`CONFIG_SENSOR_CLOCK_COUNTER`](../../../kconfig.md#CONFIG_SENSOR_CLOCK_COUNTER "CONFIG_SENSOR_CLOCK_COUNTER"),
>   [`CONFIG_SENSOR_CLOCK_RTC`](../../../kconfig.md#CONFIG_SENSOR_CLOCK_RTC "CONFIG_SENSOR_CLOCK_RTC"), or
>   [`CONFIG_SENSOR_CLOCK_SYSTEM`](../../../kconfig.md#CONFIG_SENSOR_CLOCK_SYSTEM "CONFIG_SENSOR_CLOCK_SYSTEM").

Build and run the sample with the following command:

```shell
# From the root of the zephyr repository
west build -b <board to use> samples/sensor/clock
west flash
```

### Sample Output

The application will print the current sensor clock cycles and
their corresponding time in nanoseconds.

```shell
Cycles: 143783087
Nanoseconds: 8986442937
Cycles: 159776386
Nanoseconds: 9986024125
Cycles: 175772543
Nanoseconds: 10985783937
Cycles: 191771203
Nanoseconds: 11985700187
Cycles: 207758870
Nanoseconds: 12984929375
Cycles: 223752074
Nanoseconds: 13984504625

...
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
