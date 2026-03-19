---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/sensor/ccs811/README.html
original_path: samples/sensor/ccs811/README.html
---

# CCS811 indoor air quality sensor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/sensor/ccs811/README.rst/..)

## Overview

The CCS811 digital gas sensor detects volatile organic compounds (VOCs)
for indoor air quality measurements. VOCs are often categorized as
pollutants and/or sensory irritants and can come from a variety of
sources such as construction materials (paint and carpet), machines
(copiers and processors), and even people (breathing and smoking). It
estimates carbon dioxide (CO2) levels where the main source of VOCs is
human presence.

## Building and Running

### Building and Running on thingy52/nrf52832

```shell
west build -b thingy52/nrf52832 samples/sensor/ccs811
west flash
```

### Sample Output

The sample output below is from a [Nordic Thingy:52](https://www.nordicsemi.com/Software-and-tools/Prototyping-platforms/Nordic-Thingy-52)
(thingy52/nrf52832) that includes this sensor (and others).
After a soft reset, there is a 5-second startup period
where readings are unstable, and then we can see steady
reported measurements of about 400 ppm eC02 and 0 ppb eTVOC.

## See also

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
