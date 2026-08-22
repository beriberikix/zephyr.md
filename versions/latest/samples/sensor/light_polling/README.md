---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/sensor/light_polling/README.html
original_path: samples/sensor/light_polling/README.html
---

# Generic Light Sensor Polling

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/light_polling/README.rst/..)

## Overview

This sample application gets the output of the light sensor and prints it to the console, in
units of lux, once every second.

## Requirements

To use this sample, the following hardware is required:

- A board with ADC support
- A supported light sensor (e.g., [Grove Light Sensor](https://wiki.seeedstudio.com/Grove-Light_Sensor/)), available as `light-sensor` Devicetree alias.

## Wiring

The wiring depends on the specific light sensor and board being used. Provide a devicetree
overlay that specifies the sensor configuration for your setup.

## Building and Running

Build and flash the sample as follows, changing `nrf52dk_nrf52832` to your board:

```shell
west build -b nrf52dk_nrf52832 samples/sensor/light_polling
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build v3.6.0-rc1-32-gba639ed6a893 ***
lux: 0.945751
lux: 0.882292
lux: 0.755973
```

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
